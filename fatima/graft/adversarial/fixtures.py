# Bismillah ir-Rahman ir-Rahim
# 
# Al-Asma ul-Husna -- The 99 Beautiful Names of Allah
#   Allah -- The God
#   Ar-Rahman -- The Most Merciful
#   Ar-Rahim -- The Most Compassionate
#   Al-Malik -- The King
#   Al-Quddus -- The Most Holy
#   As-Salam -- The Source of Peace
#   Al-Mu'min -- The Guardian of Faith
#   Al-Muhaymin -- The Protector
#   Al-Aziz -- The Almighty
#   Al-Jabbar -- The Compeller
#   Al-Mutakabbir -- The Supreme
#   Al-Khaliq -- The Creator
#   Al-Bari -- The Evolver
#   Al-Musawwir -- The Fashioner
#   Al-Ghaffar -- The Forgiver
#   Al-Qahhar -- The Subduer
#   Al-Wahhab -- The Bestower
#   Ar-Razzaq -- The Provider
#   Al-Fattah -- The Opener
#   Al-Alim -- The All-Knowing
#   Al-Qabid -- The Restrainer
#   Al-Basit -- The Expander
#   Al-Khafid -- The Abaser
#   Ar-Rafi -- The Exalter
#   Al-Mu'izz -- The Bestower of Honor
#   Al-Mudhill -- The Humiliator
#   As-Sami -- The All-Hearing
#   Al-Basir -- The All-Seeing
#   Al-Hakam -- The Judge
#   Al-Adl -- The Just
#   Al-Latif -- The Subtle One
#   Al-Khabir -- The All-Aware
#   Al-Halim -- The Forbearing
#   Al-Azim -- The Magnificent
#   Al-Ghafur -- The All-Forgiving
#   Ash-Shakur -- The Appreciative
#   Al-Ali -- The Most High
#   Al-Kabir -- The Most Great
#   Al-Hafiz -- The Preserver
#   Al-Muqit -- The Sustainer
#   Al-Hasib -- The Reckoner
#   Al-Jalil -- The Majestic
#   Al-Karim -- The Generous
#   Ar-Raqib -- The Watchful
#   Al-Mujib -- The Responsive
#   Al-Wasi -- The All-Encompassing
#   Al-Hakim -- The Perfectly Wise
#   Al-Wadud -- The Loving One
#   Al-Majid -- The Most Glorious
#   Al-Ba'ith -- The Resurrector
#   Ash-Shahid -- The Witness
#   Al-Haqq -- The Truth
#   Al-Wakil -- The Trustee
#   Al-Qawiyy -- The Most Strong
#   Al-Matin -- The Firm One
#   Al-Waliyy -- The Protector
#   Al-Hamid -- The Praiseworthy
#   Al-Muhsi -- The Accounter
#   Al-Mubdi -- The Originator
#   Al-Mu'id -- The Restorer
#   Al-Muhyi -- The Giver of Life
#   Al-Mumit -- The Creator of Death
#   Al-Hayy -- The Ever Living
#   Al-Qayyum -- The Self-Subsisting
#   Al-Wajid -- The Finder
#   Al-Majid -- The Noble
#   Al-Wahid -- The Unique
#   Al-Ahad -- The One
#   As-Samad -- The Eternal
#   Al-Qadir -- The Able
#   Al-Muqtadir -- The Powerful
#   Al-Muqaddim -- The Expediter
#   Al-Mu'akhkhir -- The Delayer
#   Al-Awwal -- The First
#   Al-Akhir -- The Last
#   Az-Zahir -- The Manifest
#   Al-Batin -- The Hidden
#   Al-Wali -- The Governor
#   Al-Muta'ali -- The Most Exalted
#   Al-Barr -- The Source of Goodness
#   At-Tawwab -- The Acceptor of Repentance
#   Al-Muntaqim -- The Avenger
#   Al-Afuww -- The Pardoner
#   Ar-Ra'uf -- The Most Kind
#   Malik-ul-Mulk -- Owner of Sovereignty
#   Dhul-Jalali wal-Ikram -- Lord of Majesty and Generosity
#   Al-Muqsit -- The Equitable
#   Al-Jami -- The Gatherer
#   Al-Ghaniyy -- The Self-Sufficient
#   Al-Mughni -- The Enricher
#   Al-Mani -- The Preventer
#   Ad-Darr -- The Distresser
#   An-Nafi -- The Propitious
#   An-Nur -- The Light
#   Al-Hadi -- The Guide
#   Al-Badi -- The Originator
#   Al-Baqi -- The Everlasting
#   Al-Warith -- The Inheritor
#   Ar-Rashid -- The Guide to the Right Path
#   As-Sabur -- The Patient
# 
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
# Bismillah ir-Rahman ir-Rahim
