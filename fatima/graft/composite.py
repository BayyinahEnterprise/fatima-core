"""
Composite graft boundary -- five-level guarantees across sub-molecules.

A composite document is a set of sub-molecules plus inter-molecule bonds.
The composite gate returns a verdict that is honest about the weakest
sub-molecule -- because a chain of evidence is only as strong as its
weakest link.

The composite does not aggregate upward. A composite of ten sub-molecules
does not become more confident with each addition. It can only be capped
by its weakest member. This is the correct monotone behaviour, and it
prevents the "swarm confidence" fracture that would otherwise appear at
scale.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Mapping

from fatima.verification.verdict import Verdict, VerificationReport
from fatima.graft.report import GraftReport


@dataclass(frozen=True)
class CompositeGraftReport:
    """Report from composite-level graft verification.

    Attributes
    ----------
    overall : GraftReport
        The composed verdict across all sub-molecules and inter-bonds.
    per_sub : dict
        Mapping of sub-molecule ID to its VerificationReport.
    inter_bond_status : GraftReport
        The inter-bond structural/integrity report.
    """

    overall: GraftReport
    per_sub: Mapping[str, VerificationReport]
    inter_bond_status: GraftReport


def verify_composite_grafts(
    sub_reports: Mapping[str, VerificationReport],
    inter_bond_report: GraftReport,
) -> CompositeGraftReport:
    """Compose sub-molecule reports plus inter-bond checks.

    The composite verdict is the meet of:
      - every sub-molecule's final verdict
      - the inter-bond structural/integrity report

    Confidence is the minimum across all.

    An empty sub-map is UNKNOWN -- never VERIFIED.
    A missing inter-bond report is UNKNOWN -- never assumed satisfied.
    """
    if not sub_reports:
        return CompositeGraftReport(
            overall=GraftReport.absent(
                "composite", "no sub-molecules supplied"
            ),
            per_sub={},
            inter_bond_status=GraftReport.absent(
                "inter_bond", "no sub-molecules supplied"
            ),
        )

    # Compose sub-molecule verdicts via lattice meet.
    verdict = Verdict.VERIFIED
    confidence = 1.0
    notes: list[str] = []

    for sid, r in sub_reports.items():
        verdict = verdict & r.verdict
        confidence = min(confidence, r.confidence)
        if r.verdict is not Verdict.VERIFIED:
            notes.append(f"{sid}: {r.verdict.value}")

    # Include inter-bond report in the meet.
    verdict = verdict & inter_bond_report.verdict
    confidence = min(confidence, inter_bond_report.confidence)
    notes.extend(inter_bond_report.notes)

    overall = GraftReport(
        layer="composite",
        verdict=verdict,
        confidence=confidence,
        notes=tuple(notes),
        code=verdict.value,
    )

    return CompositeGraftReport(
        overall=overall,
        per_sub=dict(sub_reports),
        inter_bond_status=inter_bond_report,
    )
