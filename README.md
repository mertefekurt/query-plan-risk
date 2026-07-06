# Query Plan Risk

![Query Plan Risk cover](assets/readme-cover.svg)

> Flag risky database query plans from explain-plan notes

![stack](https://img.shields.io/badge/stack-Python-b45309?style=flat-square) ![python](https://img.shields.io/badge/python-3.11-be185d?style=flat-square) ![license](https://img.shields.io/badge/license-MIT-4b5563?style=flat-square) ![ci](https://img.shields.io/badge/ci-GitHub%20Actions-2563eb?style=flat-square)

## At a glance

| Area | Detail |
| --- | --- |
| Focus | database review |
| Command | `query-plan-risk` |
| Formats | text, JSON, JSONL, CSV |
| Output | Markdown table or JSON |

## What it checks

| Rule | Severity | What it catches |
| --- | --- | --- |
| `seq-scan` | high | sequential scan detected |
| `disk-sort` | medium | disk sort detected |
| `huge-loop` | low | large nested loop detected |

## Try it locally

```bash
python -m pip install -e ".[dev]"
query-plan-risk examples/sample.txt
query-plan-risk examples/sample.txt --json --fail-on medium
```

## Notes from the code

`rules.py` keeps the project policy explicit, while `core.py` handles parsing and report rendering. The CLI stays thin on purpose so the checks are easy to test.

## Verify

```bash
python -m pip install -e ".[dev]"
ruff check .
pytest
python -m query_plan_risk --help
```
