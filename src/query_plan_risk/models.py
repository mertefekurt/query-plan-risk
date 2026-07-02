from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class Rule:
    code: str
    severity: str
    pattern: str
    message: str
    recommendation: str


@dataclass(frozen=True)
class Finding:
    code: str
    severity: str
    subject: str
    message: str
    recommendation: str

    def to_dict(self) -> dict[str, str]:
        return {
            "code": self.code,
            "severity": self.severity,
            "message": self.message,
            "recommendation": self.recommendation,
            "subject": self.subject,
        }


@dataclass(frozen=True)
class AuditReport:
    findings: tuple[Finding, ...]
    records_scanned: int
    risk_level: str
    score: int

    def to_dict(self) -> dict[str, Any]:
        return {
            "findings": [finding.to_dict() for finding in self.findings],
            "records_scanned": self.records_scanned,
            "risk_level": self.risk_level,
            "score": self.score,
        }
