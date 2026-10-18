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
Three-valued verification verdict.

Derived from NC-P1 of the Non-Advantage of Concealment paper:
verification is never binary pass/fail.  A system must distinguish
between confirmed integrity, insufficient evidence, and confirmed
violation.

VERIFIED  — all examined structural relationships are consistent;
            the evidence supports integrity at the examined level.
UNKNOWN   — insufficient evidence to confirm or deny integrity;
            some relationships could not be checked, or the
            cross-section examined was not sufficient for
            reconstruction.  Per NC-P4, UNKNOWN cannot authorise
            irreversible effect.
VIOLATED  — at least one structural inconsistency detected;
            the specific violation is recorded in the report.

The verdict carries a confidence measure (0.0–1.0) reflecting the
fraction of verifiable structure that was actually examined, and a
monotone-degradation guarantee from NC-P2: partial structural loss
reduces confidence proportionally, never silently.
"""

from __future__ import annotations

import enum
from dataclasses import dataclass, field
from typing import Optional


class Verdict(enum.Enum):
    """Three-valued verification outcome."""

    VERIFIED = "VERIFIED"
    UNKNOWN = "UNKNOWN"
    VIOLATED = "VIOLATED"

    def __and__(self, other: Verdict) -> Verdict:
        """Lattice meet: VIOLATED < UNKNOWN < VERIFIED.

        Composing two verdicts yields the *worst* of the two, which
        implements monotone trust degradation (NC-P2): combining a
        VERIFIED with an UNKNOWN cannot upgrade to VERIFIED.
        """
        if not isinstance(other, Verdict):
            return NotImplemented
        order = {Verdict.VIOLATED: 0, Verdict.UNKNOWN: 1, Verdict.VERIFIED: 2}
        return self if order[self] <= order[other] else other

    def __or__(self, other: Verdict) -> Verdict:
        """Lattice join: the *best* of the two.

        Useful when multiple independent verification paths exist and
        any one sufficing is acceptable (holographic property: any
        sufficient cross-section reconstructs the whole).
        """
        if not isinstance(other, Verdict):
            return NotImplemented
        order = {Verdict.VIOLATED: 0, Verdict.UNKNOWN: 1, Verdict.VERIFIED: 2}
        return self if order[self] >= order[other] else other


@dataclass(frozen=True)
class VerificationReport:
    """Immutable report produced by a verification pass.

    Attributes
    ----------
    verdict : Verdict
        The three-valued outcome.
    level : int
        Verification level (1–5) per Chapter 15 of the FATIMA paper.
    confidence : float
        Fraction of verifiable structure actually examined (0.0–1.0).
        Monotone-degradation guarantee: if k atoms out of n are
        examinable, confidence <= k/n.
    examined : int
        Number of structural relationships examined.
    total : int
        Total structural relationships in the encoding.
    violations : tuple[str, ...]
        Human-readable descriptions of each detected violation.
    level_name : str
        One of: syntactic, structural, holographic, fitrah, authenticity.
    """

    verdict: Verdict
    level: int
    confidence: float
    examined: int
    total: int
    violations: tuple[str, ...] = ()
    level_name: str = ""

    def __post_init__(self) -> None:
        if not (0.0 <= self.confidence <= 1.0):
            raise ValueError(f"confidence must be in [0, 1], got {self.confidence}")
        if not (1 <= self.level <= 5):
            raise ValueError(f"level must be in [1, 5], got {self.level}")

    @staticmethod
    def compose(*reports: VerificationReport) -> VerificationReport:
        """Compose multiple reports via lattice meet (NC-P2).

        The composed verdict is the worst of the components.
        Confidence is the minimum.  All violations are collected.
        The level is the highest examined.
        """
        if not reports:
            return VerificationReport(
                verdict=Verdict.UNKNOWN,
                level=1,
                confidence=0.0,
                examined=0,
                total=0,
                level_name="none",
            )
        verdict = reports[0].verdict
        for r in reports[1:]:
            verdict = verdict & r.verdict
        return VerificationReport(
            verdict=verdict,
            level=max(r.level for r in reports),
            confidence=min(r.confidence for r in reports),
            examined=sum(r.examined for r in reports),
            total=sum(r.total for r in reports),
            violations=tuple(v for r in reports for v in r.violations),
            level_name=max(reports, key=lambda r: r.level).level_name,
        )
# Bismillah ir-Rahman ir-Rahim
