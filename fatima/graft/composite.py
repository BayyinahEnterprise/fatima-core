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
# Bismillah ir-Rahman ir-Rahim
