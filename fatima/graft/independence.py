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
# Bismillah ir-Rahman ir-Rahim
