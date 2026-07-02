# query-plan-risk

> Flag risky database query plans from explain-plan notes.

## Field memo Overview

Flag risky database query plans from explain-plan notes. It solves review drift by turning plain-text plans into deterministic CI-friendly findings.

## Input Contract

Accepts query plan notes. The reader supports plain text, JSON, JSONL, and CSV so the
tool can fit into scripts, CI jobs, and review exports.

## CLI Walkthrough

```bash
python -m pip install -e ".[dev]"
query-plan-risk examples/sample.txt
query-plan-risk examples/sample.txt --json --fail-on medium
python -m query_plan_risk --help
```

## Rule Surface

| Rule | Severity | Meaning |
|---|---:|---|
| `seq-scan` | high | sequential scan detected |
| `disk-sort` | medium | disk sort detected |
| `huge-loop` | low | large nested loop detected |

## Validation Notes

```bash
ruff check .
pytest
python -m query_plan_risk --help
```

Example risky input:

```text
nested_loop huge sort disk seq_scan true
```

Architecture: `cli.py` handles arguments, `core.py` reads and evaluates records, and
`rules.py` keeps the project-specific policy explicit.

License: MIT.
