"""Behavioral invariants for evidence gates and candidate retrieval (stdlib only)."""
import copy
from datetime import date
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "skills/design-direction/scripts/catalog.py"
spec = importlib.util.spec_from_file_location("catalog", SCRIPT)
catalog = importlib.util.module_from_spec(spec)
spec.loader.exec_module(catalog)
AS_OF = date(2026, 11, 1)


class CatalogTests(unittest.TestCase):
    def setUp(self):
        self.data = json.loads(catalog.DEFAULT.read_text())
        self.template = copy.deepcopy(self.data["records"][1])

    def reviewed(self, rid="reviewed-sample", family="index", content=None):
        r = copy.deepcopy(self.template)
        r.update(id=rid, url="https://example.org/" + rid, structure_family=family,
                 content_types=content or ["articles"])
        e = r["evidence"]
        e.update(level="whole-site-reviewed", observed_on="2026-11-01", pages=[], screenshots=[])
        for kind, viewport in [("home", "desktop"), ("inner", "desktop"), ("inner", "mobile")]:
            capture = f"fixtures/{rid}-{kind}-{viewport}.png"
            e["screenshots"].append(capture)
            e["pages"].append(dict(kind=kind, viewport=viewport, extent="full", url=r["url"],
                                   observed_on="2026-11-01", capture=capture, note="Synthetic test metadata; not real site evidence."))
        e["interactions"] = [dict(task="Open article and return", result="pass", observed_on="2026-11-01", note="Synthetic fixture")]
        return r

    def test_seed_valid_but_not_whole_site_recommendations(self):
        self.assertEqual(catalog.validate(self.data), [])
        result = catalog.shortlist(self.data, "read", ["articles"], as_of=AS_OF)
        self.assertEqual(result["candidates"], [])
        self.assertTrue(result["coverage_gap"])

    def test_partial_requires_opt_in_and_never_admits_text_only(self):
        result = catalog.shortlist(self.data, "experience", include_partial=True, as_of=AS_OF)
        ids = {r["id"] for r in result["candidates"]}
        self.assertNotIn("evan-luo", ids)
        self.assertIn("brittany-chiang", ids)
        self.assertTrue(all(r["evidence_gaps"] for r in result["candidates"]))

    def test_content_coverage_precedes_variety_and_reports_gaps(self):
        self.data["records"] = [self.reviewed("a", "same", ["articles"]),
                                self.reviewed("b", "same", ["articles", "projects"]),
                                self.reviewed("c", "different", ["articles"])]
        result = catalog.shortlist(self.data, "read", ["articles", "projects"], as_of=AS_OF)
        self.assertEqual([r["id"] for r in result["candidates"]], ["b", "c", "a"])
        self.assertEqual(result["candidates"][1]["content_missing"], ["projects"])

    def test_density_exclusion_and_modes_are_hard_filters(self):
        result = catalog.shortlist(self.data, "read", ["articles"], density="high",
                                   exclude=["josh-comeau"], include_partial=True, as_of=AS_OF)
        self.assertEqual([r["id"] for r in result["candidates"]], ["aistar"])
        self.assertEqual(catalog.shortlist(self.data, "operate", include_partial=True, as_of=AS_OF)["candidates"], [])

    def test_fake_reviewed_status_is_rejected(self):
        self.data["records"][0]["evidence"]["level"] = "whole-site-reviewed"
        self.assertTrue(catalog.validate(self.data))

    def test_current_reviewed_evidence_can_pass(self):
        self.data["records"] = [self.reviewed()]
        self.assertEqual(catalog.validate(self.data), [])
        self.assertEqual(len(catalog.shortlist(self.data, "read", as_of=AS_OF)["candidates"]), 1)

    def test_stale_future_missing_capture_and_failed_task_do_not_pass(self):
        for mutation in ("stale", "future", "capture", "interaction"):
            with self.subTest(mutation=mutation):
                r = self.reviewed()
                if mutation == "stale":
                    for p in r["evidence"]["pages"]:
                        p["observed_on"] = "2025-01-01"
                elif mutation == "future":
                    r["evidence"]["observed_on"] = "2027-01-01"
                elif mutation == "capture":
                    r["evidence"]["pages"][1]["capture"] = None
                else:
                    r["evidence"]["interactions"][0]["result"] = "fail"
                self.data["records"] = [r]
                self.assertEqual(catalog.shortlist(self.data, "read", as_of=AS_OF)["candidates"], [])

    def test_duplicate_url_and_unsafe_scheme_rejected(self):
        self.data["records"][1]["url"] = self.data["records"][0]["url"].rstrip("/") + "/#intro"
        self.assertTrue(catalog.validate(self.data))
        self.data["records"][1]["url"] = "javascript:alert(1)"
        self.assertTrue(catalog.validate(self.data))

    def test_cli_invalid_json_fails_cleanly(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp) / "bad.json"
            p.write_text("{bad")
            result = subprocess.run([sys.executable, str(SCRIPT), "--catalog", str(p), "validate"], capture_output=True, text=True)
        self.assertNotEqual(result.returncode, 0)
        self.assertNotIn("Traceback", result.stderr)

    def test_malformed_fields_report_errors_instead_of_crashing(self):
        r = self.data["records"][0]
        r["asset_requirement"] = {}
        r["evidence"].update(level=[], screenshots=None)
        r["evidence"]["pages"][0].update(kind=[], capture="unknown.png")
        self.assertTrue(catalog.validate(self.data))

    def test_cli_works_from_another_directory(self):
        with tempfile.TemporaryDirectory() as tmp:
            result = subprocess.run([sys.executable, str(SCRIPT), "shortlist", "--mode", "read", "--content", "articles", "--include-partial", "--as-of", AS_OF.isoformat()], cwd=tmp, capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(len(json.loads(result.stdout)["candidates"]), 3)


if __name__ == "__main__":
    unittest.main()
