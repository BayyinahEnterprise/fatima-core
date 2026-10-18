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
Level 3: Holographic Verification — reconstruction from cross-sections.

Checks whether the holographic encoding (Property 1) is intact:
any sufficient cross-section of k-of-n atoms must reconstruct
the complete bond graph.

This level tests the *redundancy* of the encoding — whether the
document's meaning-structure survives partial loss.  If reconstruction
fails from any valid k-size subset, the holographic property has been
compromised.

The verification is sampling-based for large molecules: rather than
testing all C(n,k) subsets, it tests a configurable number of random
subsets and reports the success rate.

Trust degradation (NC-P2): if some atoms have lost their shards,
the confidence is reduced proportionally.  If the number of atoms
with intact shards drops below the threshold k, the verdict is
UNKNOWN (insufficient evidence to confirm or deny), not VIOLATED
(we cannot prove violation without evidence of what was lost).
"""

from __future__ import annotations

import random
from itertools import combinations

from fatima.core.encoding import verify_holographic_reconstruction
from fatima.core.molecule import Molecule
from fatima.verification.verdict import Verdict, VerificationReport


def verify_holographic(
    molecule: Molecule,
    sample_size: int = 20,
    seed: int | None = None,
) -> VerificationReport:
    """Level 3: verify holographic redundancy.

    Parameters
    ----------
    molecule : Molecule
        The molecule to verify.
    sample_size : int
        Number of random k-size subsets to test.  If C(n,k) is
        smaller than sample_size, all subsets are tested.
    seed : int | None
        Random seed for reproducibility.

    Returns
    -------
    VerificationReport
        Level 3 report with confidence based on the fraction of
        successful reconstructions.
    """
    violations: list[str] = []
    all_ids = [a.atom_id for a in molecule.atoms_by_position()]
    n = len(all_ids)

    if n < 2:
        return VerificationReport(
            verdict=Verdict.VERIFIED if n == 1 else Verdict.UNKNOWN,
            level=3,
            confidence=1.0 if n == 1 else 0.0,
            examined=n,
            total=n,
            level_name="holographic",
        )

    # Check that atoms have shards
    atoms_with_shards = [
        aid for aid in all_ids if molecule.atoms[aid].has_shard
    ]
    if not atoms_with_shards:
        return VerificationReport(
            verdict=Verdict.UNKNOWN,
            level=3,
            confidence=0.0,
            examined=0,
            total=n,
            violations=("No holographic shards found — encoding not applied",),
            level_name="holographic",
        )

    threshold = molecule.atoms[atoms_with_shards[0]].shard_threshold

    if len(atoms_with_shards) < threshold:
        # NC-P2: insufficient atoms → UNKNOWN, not VIOLATED
        return VerificationReport(
            verdict=Verdict.UNKNOWN,
            level=3,
            confidence=len(atoms_with_shards) / n,
            examined=len(atoms_with_shards),
            total=n,
            violations=(
                f"Only {len(atoms_with_shards)} atoms have shards, "
                f"but threshold is {threshold}",
            ),
            level_name="holographic",
        )

    # Full reconstruction first
    ok, msg = verify_holographic_reconstruction(molecule)
    if not ok:
        violations.append(f"Full reconstruction failed: {msg}")
        return VerificationReport(
            verdict=Verdict.VIOLATED,
            level=3,
            confidence=1.0,
            examined=n,
            total=n,
            violations=tuple(violations),
            level_name="holographic",
        )

    # Sample k-size subsets
    # For small molecules, test all C(n,k) subsets exhaustively.
    # For large molecules, generate random k-size subsets directly —
    # enumerating C(250,125) ≈ 10^73 subsets is impossible.
    rng = random.Random(seed)
    n_with_shards = len(atoms_with_shards)

    # Compute C(n,k) to decide exhaustive vs. sampling
    from math import comb
    total_subsets = comb(n_with_shards, threshold)
    exhaustive = total_subsets <= sample_size

    if exhaustive:
        subsets_to_test = [
            list(s) for s in combinations(atoms_with_shards, threshold)
        ]
    else:
        # Generate random subsets without enumerating
        subsets_to_test = [
            rng.sample(atoms_with_shards, threshold)
            for _ in range(sample_size)
        ]

    successes = 0
    for subset in subsets_to_test:
        ok, msg = verify_holographic_reconstruction(molecule, subset)
        if ok:
            successes += 1
        else:
            violations.append(
                f"Subset reconstruction failed: {msg}"
            )

    tested = len(subsets_to_test)
    if successes == tested:
        verdict = Verdict.VERIFIED
    elif successes == 0:
        verdict = Verdict.VIOLATED
    else:
        # Partial success: some subsets work, some don't
        # This shouldn't happen with correct encoding — it indicates
        # selective corruption
        verdict = Verdict.VIOLATED
        violations.append(
            f"Partial reconstruction: {successes}/{tested} subsets succeeded "
            f"(indicates selective corruption)"
        )

    confidence = successes / tested if tested > 0 else 0.0
    return VerificationReport(
        verdict=verdict,
        level=3,
        confidence=confidence,
        examined=tested,
        total=total_subsets,
        violations=tuple(violations),
        level_name="holographic",
    )
# Bismillah ir-Rahman ir-Rahim
