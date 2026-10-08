"""
Independence ledger -- structural non-collusion check.

Three correlated keys can collapse independence: the author, the
reviewer, and the anchor all being the same institution under different
key names. The Canon's F-01 measured exactly this pattern.

This check cannot prove independence -- that would require a trust model
stronger than cryptography. It can falsify obvious collapse. Passing
the check does not establish independence; it removes three specific
counterexamples.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from fatima.verification.verdict import Verdict
from fatima.graft.report import GraftReport


@dataclass(frozen=True)
class EvidenceParty:
    """A declared participant in the evidence chain.

    Attributes
    ----------
    role : str
        "author", "semantic_reviewer", or "anchor".
    key_id : str
        Cryptographic key identifier.
    lineage : str
        Declared organisational lineage. Not cryptographically bound --
        a soft signal only. Shared lineage yields UNKNOWN, not VIOLATED,
        because lineage is a declaration, not a proof.
    """

    role: str
    key_id: str
    lineage: str


@dataclass(frozen=True)
class IndependenceRecord:
    """The declared independence structure of an artifact's evidence."""

    author: EvidenceParty
    semantic_reviewer: Optional[EvidenceParty] = None
    anchor: Optional[EvidenceParty] = None


def check_independence(record: IndependenceRecord) -> GraftReport:
    """Three independence conditions.

    (1) Reviewer key != author key.
    (2) Anchor key != author key AND anchor key != reviewer key.
    (3) If lineages are declared, at least the reviewer's lineage differs
        from the author's. This is a soft condition: lineage is not
        cryptographically bound, so failure here yields UNKNOWN, not
        VIOLATED.

    The check cannot prove independence. It can only falsify obvious
    collapse. Passing this check is necessary, never sufficient.
    """
    failures: list[str] = []
    unknowns: list[str] = []

    if (
        record.semantic_reviewer
        and record.semantic_reviewer.key_id == record.author.key_id
    ):
        failures.append("reviewer key equals author key")

    if record.anchor:
        if record.anchor.key_id == record.author.key_id:
            failures.append("anchor key equals author key")
        if (
            record.semantic_reviewer
            and record.anchor.key_id == record.semantic_reviewer.key_id
        ):
            failures.append("anchor key equals reviewer key")

    if (
        record.semantic_reviewer
        and record.semantic_reviewer.lineage == record.author.lineage
    ):
        unknowns.append(
            "reviewer lineage matches author lineage; independence unproven"
        )

    if failures:
        return GraftReport.invalid("independence", "; ".join(failures))
    if unknowns:
        return GraftReport.absent("independence", "; ".join(unknowns))
    return GraftReport.ok(
        "independence",
        1.0,
        "no declared collapse; independence still not proven",
    )
