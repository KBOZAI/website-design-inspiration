#!/usr/bin/env python3
"""Offline case validation and evidence-aware retrieval; not an aesthetic scorer."""
import argparse
from datetime import date
import json
from pathlib import Path
import re
import sys
from urllib.parse import urlsplit, urlunsplit

DEFAULT = Path(__file__).resolve().parents[1] / "references" / "catalog.json"
MODES = {"read", "operate", "persuade", "experience"}
CONTENT = {"articles", "projects", "resume", "photos", "links", "notes", "data", "products", "forms"}
LEVELS = {"text-only", "desktop-home-only", "desktop-partial", "whole-site-reviewed"}
DENSITIES = {"low": "低", "medium": "中", "high": "高"}


def web_url(value):
    if not isinstance(value, str) or any(c.isspace() for c in value):
        return False
    try:
        u = urlsplit(value)
        return u.scheme in {"http", "https"} and bool(u.hostname) and not u.username and not u.password
    except ValueError:
        return False


def canonical_url(value):
    u = urlsplit(value)
    return urlunsplit((u.scheme.lower(), u.netloc.lower(), u.path.rstrip("/"), u.query, ""))


def valid_date(value):
    try:
        return isinstance(value, str) and date.fromisoformat(value).isoformat() == value
    except ValueError:
        return False


def nonempty(value):
    return isinstance(value, str) and bool(value.strip())


def evidence_gaps(record, as_of, max_age):
    e = record["evidence"]
    gaps = []
    def recent(value):
        age = (as_of - date.fromisoformat(value)).days
        return 0 <= age <= max_age
    def has_page(kind=None, viewport=None):
        return any((kind is None or p["kind"] == kind)
                   and (viewport is None or p["viewport"] == viewport)
                   and p["extent"] == "full" and nonempty(p.get("capture"))
                   and recent(p["observed_on"]) for p in e["pages"])
    for label, kind, viewport in [("desktop full homepage capture", "home", "desktop"),
                                  ("desktop full inner-page capture", "inner", "desktop"),
                                  ("mobile full-page capture", None, "mobile")]:
        if not has_page(kind, viewport):
            gaps.append("missing or stale: " + label)
    if not any(t["result"] == "pass" and recent(t["observed_on"]) for t in e["interactions"]):
        gaps.append("missing or stale: passed core interaction")
    if any(t["result"] == "fail" and recent(t["observed_on"]) for t in e["interactions"]):
        gaps.append("unresolved failed interaction; update evidence after retest")
    if not recent(e["observed_on"]):
        gaps.append("record observation is stale or later than the evaluation date")
    if e["level"] != "whole-site-reviewed":
        gaps.append("historical partial inspection; not a whole-site recommendation")
    return gaps


def validate(data):
    errors = []
    if not isinstance(data, dict) or data.get("schema_version") != 2 or not isinstance(data.get("records"), list):
        return ["expected schema_version 2 and a records array"]
    if not valid_date(data.get("updated_on")):
        errors.append("invalid updated_on")
    ids, urls = set(), set()
    for i, r in enumerate(data["records"]):
        label = f"record {i}"
        if not isinstance(r, dict):
            errors.append(label + ": expected object")
            continue
        start = len(errors)
        rid = r.get("id")
        if not isinstance(rid, str) or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", rid) or rid in ids:
            errors.append(label + ": invalid or duplicate id")
        else:
            ids.add(rid)
        for field in ("name", "structure_family", "classification_note", "use_when", "do_not_copy_blindly"):
            if not nonempty(r.get(field)):
                errors.append(label + ": missing " + field)
        if not web_url(r.get("url")):
            errors.append(label + ": invalid original URL")
        else:
            url = canonical_url(r["url"])
            if url in urls:
                errors.append(label + ": duplicate original URL")
            urls.add(url)
        for field, allowed in (("modes", MODES), ("content_types", CONTENT)):
            v = r.get(field)
            if not isinstance(v, list) or not v or any(not isinstance(x, str) or x not in allowed for x in v):
                errors.append(label + ": invalid " + field)
        if r.get("asset_requirement") not in ("text-first", "mixed", "image-led"):
            errors.append(label + ": invalid asset_requirement")
        tags = r.get("tags", {})
        if not isinstance(tags, dict) or tags.get("density") not in DENSITIES.values():
            errors.append(label + ": invalid tags/density")
        elif not isinstance(tags.get("layout"), list) or not tags["layout"] or not all(nonempty(x) for x in tags["layout"]) or not nonempty(tags.get("mood")):
            errors.append(label + ": missing layout/mood")
        if not isinstance(r.get("sections"), list) or not r["sections"] or not all(nonempty(x) for x in r["sections"]):
            errors.append(label + ": missing sections")
        e = r.get("evidence")
        if not isinstance(e, dict):
            errors.append(label + ": missing evidence")
            continue
        if not isinstance(e.get("level"), str) or e["level"] not in LEVELS or not valid_date(e.get("observed_on")):
            errors.append(label + ": invalid evidence level/date")
        for field in ("note", "source", "rights"):
            if not nonempty(e.get(field)):
                errors.append(label + ": missing evidence " + field)
        if not isinstance(e.get("screenshots"), list) or not all(nonempty(x) for x in e["screenshots"]):
            errors.append(label + ": screenshots must be a list of references")
        pages = e.get("pages")
        if not isinstance(pages, list) or not pages:
            errors.append(label + ": missing page observations")
        else:
            for p in pages:
                if not isinstance(p, dict):
                    errors.append(label + ": invalid page observation")
                    continue
                if (p.get("kind") not in ("home", "inner") or p.get("viewport") not in ("desktop", "mobile")
                    or p.get("extent") not in ("full", "partial", "first-screen", "text")
                    or not web_url(p.get("url")) or not valid_date(p.get("observed_on")) or not nonempty(p.get("note"))):
                    errors.append(label + ": invalid page fields")
                if p.get("capture") is not None and (not nonempty(p["capture"]) or not isinstance(e.get("screenshots"), list) or p["capture"] not in e["screenshots"]):
                    errors.append(label + ": page capture must occur in screenshots")
                if e.get("level") == "text-only" and (p.get("extent") != "text" or p.get("capture")):
                    errors.append(label + ": text-only record cannot claim visual evidence")
        interactions = e.get("interactions")
        if not isinstance(interactions, list):
            errors.append(label + ": interactions must be an array")
        else:
            for t in interactions:
                if not isinstance(t, dict) or t.get("result") not in ("pass", "fail") or not nonempty(t.get("task")) or not valid_date(t.get("observed_on")) or not nonempty(t.get("note")):
                    errors.append(label + ": invalid interaction evidence")
        if len(errors) == start and e["level"] == "whole-site-reviewed":
            gaps = evidence_gaps(r, date.fromisoformat(e["observed_on"]), 90)
            if gaps:
                errors.append(label + ": unsupported whole-site-reviewed claim: " + "; ".join(gaps))
    return errors


def shortlist(data, mode, content=(), density=None, exclude=(), include_partial=False,
              limit=3, as_of=None, max_age=90):
    as_of = as_of or date.today()
    wanted = set(content)
    eligible = []
    for r in data["records"]:
        if r["id"] in exclude or mode not in r["modes"] or r["evidence"]["level"] == "text-only":
            continue
        if density and r["tags"]["density"] != DENSITIES[density]:
            continue
        covered = wanted.intersection(r["content_types"])
        if wanted and not covered:
            continue
        gaps = evidence_gaps(r, as_of, max_age)
        if gaps and not include_partial:
            continue
        eligible.append((r, covered, gaps))
    chosen, families = [], set()
    while eligible and len(chosen) < limit:
        eligible.sort(key=lambda item: (-len(item[1]), item[0]["structure_family"] in families,
                                       bool(item[2]), item[0]["id"]))
        r, covered, gaps = eligible.pop(0)
        families.add(r["structure_family"])
        chosen.append({"id": r["id"], "name": r["name"], "url": r["url"],
                       "structure_family": r["structure_family"], "sections": r["sections"],
                       "content_covered": sorted(covered), "content_missing": sorted(wanted - covered),
                       "asset_requirement": r["asset_requirement"], "fit_reason": r["use_when"],
                       "adaptation_risk": r["do_not_copy_blindly"],
                       "evidence_level": r["evidence"]["level"], "observed_on": r["evidence"]["observed_on"],
                       "evidence_gaps": gaps, "needs_live_verification": True})
    return {"as_of": as_of.isoformat(), "policy": "partial-candidates" if include_partial else "whole-site-reviewed",
            "mode": mode, "requested_content": sorted(wanted), "candidates": chosen,
            "coverage_gap": len(chosen) < limit,
            "note": "Retrieval only, not aesthetic approval. Open current pages before recommending; never fill gaps with invented cases."}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--catalog", type=Path, default=DEFAULT)
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("validate")
    pick = sub.add_parser("shortlist")
    pick.add_argument("--mode", choices=sorted(MODES), required=True)
    pick.add_argument("--content", choices=sorted(CONTENT), action="append", default=[])
    pick.add_argument("--density", choices=sorted(DENSITIES))
    pick.add_argument("--exclude", action="append", default=[])
    pick.add_argument("--include-partial", action="store_true")
    pick.add_argument("--limit", type=int, choices=range(1, 6), default=3)
    pick.add_argument("--as-of", type=date.fromisoformat, default=date.today())
    pick.add_argument("--max-age-days", type=int, default=90)
    args = parser.parse_args()
    try:
        data = json.loads(args.catalog.read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        parser.error(str(exc))
    errors = validate(data)
    if errors:
        print(json.dumps({"valid": False, "errors": errors}, ensure_ascii=False, indent=2))
        return 1
    if args.command == "validate":
        print(json.dumps({"valid": True, "records": len(data["records"])}))
        return 0
    if args.max_age_days < 0:
        parser.error("--max-age-days must be nonnegative")
    unknown = set(args.exclude) - {r["id"] for r in data["records"]}
    if unknown:
        parser.error("unknown excluded IDs: " + ", ".join(sorted(unknown)))
    print(json.dumps(shortlist(data, args.mode, args.content, args.density, args.exclude,
                               args.include_partial, args.limit, args.as_of, args.max_age_days),
                     ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
