#!/usr/bin/env python3
"""Exercise an already available Impeccable engine; never installs anything."""
import argparse
from datetime import date
import json
import os
from pathlib import Path
import subprocess
import tempfile


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--engine", type=Path, required=True)
    parser.add_argument("--as-of", type=date.fromisoformat, required=True)
    args = parser.parse_args()
    engine = args.engine.resolve()
    root = Path(__file__).resolve().parent
    cases = [("before.html", True, 2), ("after.html", True, 0),
             ("intentional.html", False, 0), ("intentional.html", True, 2),
             ("missing.html", True, 1)]
    results = []
    env = dict(os.environ, DO_NOT_TRACK="1")
    with tempfile.TemporaryDirectory() as tmp:
        for name, raw, expected in cases:
            target = root / "fixtures" / name
            cmd = [str(engine), "detect", "--json"]
            if raw:
                cmd.append("--no-config")
            proc = subprocess.run(cmd + [str(target)], cwd=tmp, env=env, text=True, capture_output=True, timeout=30)
            findings = json.loads(proc.stdout)
            rules = sorted({x["antipattern"] for x in findings})
            passed = proc.returncode == expected
            if expected == 2:
                passed = passed and {"gradient-text", "ai-color-palette"}.issubset(rules)
            elif expected == 0:
                passed = passed and findings == []
            elif expected == 1:
                passed = passed and bool(proc.stderr)
            results.append(dict(target=name, no_config=raw, exit_code=proc.returncode,
                                findings=len(findings), rules=rules, stderr_present=bool(proc.stderr), passed=passed))
    version = subprocess.run([str(engine), "--version"], env=env, capture_output=True, text=True, timeout=10)
    report = dict(tested_on=args.as_of.isoformat(), engine_version=version.stdout.strip(),
                  scope="Static HTML CLI only; no browser, hooks, installation or design-effectiveness test",
                  cases=results, passed=all(x["passed"] for x in results))
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if report["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
