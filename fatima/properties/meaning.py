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
Property 4: Meaning-Integrity.

Semantic distortion must be detectable even when syntactic integrity
is preserved.  This is the property that crosses Shannon's boundary.

Shannon's framework treats all bit-preserving operations as
integrity-preserving.  FATIMA treats bit-preserving operations
that alter meaning as integrity violations.

The mechanism is structural cross-reference: every meaningful unit
is related to every other meaningful unit through structural
relationships that are themselves encoded.  Altering the meaning
of any unit while preserving its bits requires altering the
structural relationships — and these alterations are detectable.
"""

from __future__ import annotations

from fatima.core.molecule import Molecule
from fatima.verification.verdict import Verdict, VerificationReport


def check_meaning_integrity(molecule: Molecule) -> VerificationReport:
    """Check Property 4 without mutating the object being verified.

    Established commitments are treated as expected values.  The verifier
    recomputes fresh values through pure functions and compares them.

    Detected mismatch => VIOLATED.
    Missing commitment/evidence => UNKNOWN.
    Complete agreement => VERIFIED.

    This separation closes Canon finding F-03: verification can no longer
    erase the evidence of tampering by recomputing *into* the stored field.
    """
    violations: list[str] = []
    unknowns: list[str] = []
    total_checks = 0

    if molecule.atom_count == 0:
        return VerificationReport(
            verdict=Verdict.UNKNOWN,
            level=4,
            confidence=0.0,
            examined=0,
            total=0,
            level_name="meaning_integrity",
        )

    # Check 1: bond-graph commitment, observationally pure.
    total_checks += 1
    if not molecule.bond_graph_hash:
        unknowns.append(
            "Bond graph hash absent -- meaning-structure has not been committed"
        )
    else:
        current_hash = molecule.bond_graph_hash_value()
        if current_hash != molecule.bond_graph_hash:
            violations.append(
                "Bond graph hash mismatch -- meaning-structure changed "
                "since finalisation"
            )

    # Check 2: per-atom semantic commitments, observationally pure.
    atoms_with_commitments = 0
    for atom in molecule.atoms.values():
        total_checks += 1
        if not atom.semantic_hash:
            unknowns.append(
                f"Atom '{atom.atom_id}' has no semantic commitment"
            )
            continue
        atoms_with_commitments += 1
        expected = atom.semantic_hash_value()
        if atom.semantic_hash != expected:
            violations.append(
                f"Atom '{atom.atom_id}' semantic hash mismatch -- "
                "content/bonds/shard changed since finalisation"
            )

    if atoms_with_commitments == 0:
        unknowns.append(
            "No atoms have semantic commitments -- finalisation evidence absent"
        )

    # Check 3: rationale coverage.
    total_checks += 1
    bonds_without_rationale = [
        b for b in molecule.bonds.values() if not b.rationale
    ]
    if bonds_without_rationale:
        unknowns.append(
            f"{len(bonds_without_rationale)} bonds lack rationale "
            "(meaning-relationship cannot be independently reviewed)"
        )

    if violations:
        verdict = Verdict.VIOLATED
    elif unknowns:
        verdict = Verdict.UNKNOWN
    else:
        verdict = Verdict.VERIFIED

    notes = tuple(violations + unknowns)
    confidence = (
        1.0 if verdict == Verdict.VERIFIED
        else max(0.0, 1.0 - (len(notes) / max(total_checks, 1)))
    )

    return VerificationReport(
        verdict=verdict,
        level=4,
        confidence=confidence,
        examined=total_checks,
        total=total_checks,
        violations=notes,
        level_name="meaning_integrity",
    )


def is_meaning_integral(molecule: Molecule) -> bool:
    """Quick boolean check for Property 4."""
    report = check_meaning_integrity(molecule)
    return report.verdict == Verdict.VERIFIED
# Bismillah ir-Rahman ir-Rahim
