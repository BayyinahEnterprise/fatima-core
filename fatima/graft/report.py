"""
GraftReport -- a lightweight report for the graft and provenance layers.

The existing VerificationReport is tied to the five verification levels
(L1-L5) with examined/total counters for proportional checks. The graft
layer sits above L1-L5 and is concerned with binary evidence presence
(attested or not, independent or not, anchored or not). This module
provides a report type appropriate for that layer.

The Verdict class is shared with the existing verification system.
"""

from __future__ import annotations

from dataclasses import dataclass
from fatima.verification.verdict import Verdict


@dataclass(frozen=True)
class GraftReport:
    """Report from a graft-layer check.

    Attributes
    ----------
    layer : str
        Which graft layer produced this report (e.g. "graft", "independence",
        "anchor", "composite", "manifest").
    verdict : Verdict
        Three-valued outcome: VERIFIED, UNKNOWN, VIOLATED.
    confidence : float
        Evidence confidence, 0.0 to 1.0.
    notes : tuple[str, ...]
        Human-readable details.
    code : str
        Machine-readable status tag.
    """

    layer: str
    verdict: Verdict
    confidence: float
    notes: tuple[str, ...] = ()
    code: str = ""

    @classmethod
    def absent(cls, layer: str, reason: str) -> GraftReport:
        """Evidence absent -- verdict is UNKNOWN."""
        return cls(
            layer=layer,
            verdict=Verdict.UNKNOWN,
            confidence=0.0,
            notes=(reason,),
            code="ABSENT",
        )

    @classmethod
    def invalid(cls, layer: str, reason: str) -> GraftReport:
        """Evidence present but invalid -- verdict is VIOLATED."""
        return cls(
            layer=layer,
            verdict=Verdict.VIOLATED,
            confidence=0.0,
            notes=(reason,),
            code="INVALID",
        )

    @classmethod
    def ok(cls, layer: str, confidence: float, note: str) -> GraftReport:
        """Evidence present and valid -- verdict is VERIFIED."""
        return cls(
            layer=layer,
            verdict=Verdict.VERIFIED,
            confidence=confidence,
            notes=(note,),
            code="OK",
        )

    def meet(self, other: GraftReport) -> GraftReport:
        """Lattice meet of two reports -- monotone degradation."""
        verdict = self.verdict & other.verdict
        confidence = min(self.confidence, other.confidence)
        notes = self.notes + other.notes
        return GraftReport(
            layer=f"{self.layer}+{other.layer}",
            verdict=verdict,
            confidence=confidence,
            notes=notes,
            code=verdict.value,
        )
