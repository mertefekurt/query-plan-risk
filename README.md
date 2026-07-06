# Query Plan Risk

> A small command-line review pass for database review.

![Query Plan Risk cover](assets/readme-cover.svg)

Flag risky database query plans from explain-plan notes. The repository is intentionally plain: a small command, a visible rule surface, and enough examples to make the behavior inspectable.

## Signals in plain English

- `seq-scan` (high): sequential scan detected. Fix: review indexes and predicates.
- `disk-sort` (medium): disk sort detected. Fix: add index or raise work memory intentionally.
- `huge-loop` (low): large nested loop detected. Fix: check join order and cardinality.

## Input and report

The reader accepts text, JSON, JSONL, or CSV. The default report is readable in a terminal or pull request; `--json` keeps the same findings available to automation.

## Demo

```bash
git clone https://github.com/mertefekurt/query-plan-risk.git
cd query-plan-risk
python -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
query-plan-risk examples/sample.txt
query-plan-risk examples/sample.txt --json
```

## Sanity checks

```bash
ruff check .
pytest
python -m query_plan_risk --help
```
