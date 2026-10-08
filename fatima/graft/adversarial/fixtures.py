"""
Fixture pairs -- the smallest unit of semantic adversarial memory.

Each pair carries:
  - a source text
  - a graph proposed for that source
  - a declared relation ("paraphrase" | "negation" | "elaboration")
  - an expected semantic outcome under L4

These are NOT claims that L4 understands meaning. They are claims
that L4, when given an independent reviewer's attestation, correctly
reports the reviewer's verdict. The fixtures test the plumbing, not
the semantic understanding itself. Confusing the two would be the
same category collapse the Canon identified.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal


Relation = Literal["paraphrase", "negation", "elaboration"]


@dataclass(frozen=True)
class FixturePair:
    """A paired test case for semantic plumbing verification.

    Attributes
    ----------
    fixture_id : str
        Unique identifier.
    source : bytes
        The original text.
    graph_bytes : bytes
        A proposed graph encoding of the source.
    declared_relation : Relation
        The relationship between source and graph.
    expected_faithful : bool
        Whether a correct reviewer would attest this as faithful.
    """

    fixture_id: str
    source: bytes
    graph_bytes: bytes
    declared_relation: Relation
    expected_faithful: bool


# --- Paraphrase pairs: meaning-preserving reformulations ---

PARAPHRASE_PAIRS = (
    FixturePair(
        fixture_id="para-001",
        source=b"The treaty was sealed in the spring.",
        graph_bytes=(
            b'{"atoms":[{"atom_id":"a1","content":"treaty sealed"},'
            b'{"atom_id":"a2","content":"in spring"}]}'
        ),
        declared_relation="paraphrase",
        expected_faithful=True,
    ),
    FixturePair(
        fixture_id="para-002",
        source=b"No animal was harmed during filming.",
        graph_bytes=(
            b'{"atoms":[{"atom_id":"a1","content":"animal welfare maintained"},'
            b'{"atom_id":"a2","content":"during filming"}]}'
        ),
        declared_relation="paraphrase",
        expected_faithful=True,
    ),
)


# --- Negation pairs: meaning-inverting reformulations ---

NEGATION_PAIRS = (
    FixturePair(
        fixture_id="neg-001",
        source=b"The treaty was sealed in the spring.",
        graph_bytes=(
            b'{"atoms":[{"atom_id":"a1","content":"treaty sealed"},'
            b'{"atom_id":"a2","content":"but not in spring"}]}'
        ),
        declared_relation="negation",
        expected_faithful=False,
    ),
    FixturePair(
        fixture_id="neg-002",
        source=b"All participants consented to the terms.",
        graph_bytes=(
            b'{"atoms":[{"atom_id":"a1","content":"participants"},'
            b'{"atom_id":"a2","content":"did not all consent to terms"}]}'
        ),
        declared_relation="negation",
        expected_faithful=False,
    ),
)


def check_fixture_pair(
    pair: FixturePair,
    reviewer_attested_faithful: bool,
) -> tuple[bool, str]:
    """Return (passed, reason).

    The test asserts that the reviewer's attestation, once supplied,
    propagates correctly through the L4 check -- that the plumbing does
    not invert or drop the reviewer's verdict. It does NOT assert that
    a reviewer would attest correctly. That is out of scope for the
    plumbing test and is disclosed as such.
    """
    if pair.expected_faithful == reviewer_attested_faithful:
        return True, "reviewer verdict matches fixture expectation"
    return (
        False,
        f"reviewer attested {reviewer_attested_faithful}; "
        f"fixture expects {pair.expected_faithful}",
    )
