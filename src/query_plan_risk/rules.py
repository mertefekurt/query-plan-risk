from __future__ import annotations

from query_plan_risk.models import Rule

PROJECT_NAME = 'query-plan-risk'
SUMMARY = 'Flag risky database query plans from explain-plan notes.'
SAMPLE_RISK = 'nested_loop huge sort disk seq_scan true'
SAMPLE_CLEAN = 'index_scan true rows 120 sort memory'
TEXT_FIELDS = ("text", "content", "description", "summary", "body", "notes", "message")
SUBJECT_FIELDS = ("id", "name", "path", "service", "endpoint", "field", "event")

RULES = (
    Rule(
        code='seq-scan',
        severity='high',
        pattern='seq_scan\\s+true',
        message='sequential scan detected',
        recommendation='review indexes and predicates',
    ),
    Rule(
        code='disk-sort',
        severity='medium',
        pattern='sort\\s+disk',
        message='disk sort detected',
        recommendation='add index or raise work memory intentionally',
    ),
    Rule(
        code='huge-loop',
        severity='low',
        pattern='nested_loop\\s+huge',
        message='large nested loop detected',
        recommendation='check join order and cardinality',
    ),
)
