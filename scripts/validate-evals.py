#!/usr/bin/env python3
"""Validate eval test_cases.yaml files."""
import sys, os

try:
    import yaml
except ImportError:
    print("Installing pyyaml...")
    os.system(f"{sys.executable} -m pip install -q pyyaml")
    import yaml

skills = ["plan-product", "plan-eng", "code-review", "ship", "qa", "retro"]
errors = 0

for skill in skills:
    path = f"{skill}/evals/test_cases.yaml"
    if not os.path.isfile(path):
        print(f"\u274c {skill}: evals/test_cases.yaml missing")
        errors += 1
        continue

    with open(path) as f:
        data = yaml.safe_load(f)

    if not isinstance(data, list):
        print(f"\u274c {skill}: must be a YAML list")
        errors += 1
        continue

    for i, case in enumerate(data):
        for field in ["id", "prompt", "expectations"]:
            if field not in case or not case[field]:
                print(f"\u274c {skill}: case {i} missing '{field}'")
                errors += 1

    print(f"\u2705 {skill}: {len(data)} test case(s) valid")

if errors:
    print(f"\n{errors} error(s) found.")
    sys.exit(1)
