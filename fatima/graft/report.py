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
# Bismillah ir-Rahman ir-Rahim
