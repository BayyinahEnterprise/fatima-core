"""
Property 3: Tawhidic Unity.

The encoding cannot be fragmented without detection.  The removal
or alteration of any component creates structural inconsistencies
detectable from the remaining components.

This is stronger than error detection: it requires that the
meaning-structure of the encoding be internally cross-referencing
to such a degree that any local distortion propagates into globally
detectable inconsistency.

Tawhidic unity mirrors tawhid itself: the encoding is one, and any
attempt to divide it reveals the division.
"""

from __future__ import annotations

from fatima.core.molecule import Molecule
from fatima.verification.verdict import Verdict, VerificationReport


def check_tawhidic_unity(molecule: Molecule) -> VerificationReport:
    """Check Property 3: Tawhidic Unity.

    Verifies:
    1. Bond graph is connected (no fragmentation)
    2. No dangling bonds (no phantom references)
    3. Structural bond density is sufficient (every atom participates
       in at least one structural bond)
    4. Removing any single atom would create detectable inconsistency
       (measured by checking for dangling bonds after simulated removal)
    """
    violations: list[str] = []
    total_checks = 0

    if molecule.atom_count == 0:
        return VerificationReport(
            verdict=Verdict.UNKNOWN,
            level=2,
            confidence=0.0,
            examined=0,
            total=0,
            level_name="tawhidic_unity",
        )

    # Check 1: Connectivity
    total_checks += 1
    if not molecule.is_connected():
        components = molecule.connected_components()
        violations.append(
            f"Bond graph fragmented into {len(components)} components "
            f"(sizes: {[len(c) for c in components]})"
        )

    # Check 2: Dangling bonds
    total_checks += 1
    dangling = molecule.dangling_bonds()
    if dangling:
        violations.append(
            f"{len(dangling)} dangling bonds (reference non-existent atoms)"
        )

    # Check 3: Every atom has at least one bond
    total_checks += 1
    isolated = [
        aid for aid, atom in molecule.atoms.items()
        if len(atom.bond_ids) == 0
    ]
    if isolated:
        violations.append(
            f"Isolated atoms (no bonds): {isolated} — "
            f"these atoms are not part of the meaning-structure"
        )

    # Check 4: Removal detectability — for each atom, check that
    # removing it would create at least one dangling bond in the
    # remaining structure
    total_checks += molecule.atom_count
    undetectable_removals = []
    for atom_id in molecule.atoms:
        # Count bonds that would become dangling if this atom were removed
        bonds_affected = len(molecule.get_bonds_for(atom_id))
        if bonds_affected == 0:
            undetectable_removals.append(atom_id)

    if undetectable_removals:
        violations.append(
            f"Atoms whose removal would be undetectable: "
            f"{undetectable_removals}"
        )

    # Check 5: Structural bond minimum — the document needs enough
    # load-bearing bonds (DEFINES, DEPENDS_ON, IMPLIES, CONTRADICTS)
    # to form a structural skeleton.  The minimum is:
    #   - At least (n-1) / 4 for small documents (every ~4 atoms
    #     has at least one structural relationship)
    #   - For large documents, the ratio naturally decreases because
    #     more meaning is carried through ELABORATES/REFERENCES bonds
    # The floor is n/4 rounded down, minimum 1.
    total_checks += 1
    min_structural = max(1, molecule.atom_count // 4)
    actual_structural = molecule.structural_bond_count
    if actual_structural < min_structural:
        violations.append(
            f"Insufficient structural bonds: {actual_structural} "
            f"(minimum {min_structural} for {molecule.atom_count} atoms)"
        )

    # Verdict
    examined = total_checks
    if violations:
        verdict = Verdict.VIOLATED
    else:
        verdict = Verdict.VERIFIED

    confidence = 1.0 - (len(violations) / max(total_checks, 1))
    confidence = max(0.0, confidence)

    return VerificationReport(
        verdict=verdict,
        level=2,
        confidence=confidence,
        examined=examined,
        total=total_checks,
        violations=tuple(violations),
        level_name="tawhidic_unity",
    )


def is_tawhidically_unified(molecule: Molecule) -> bool:
    """Quick boolean check for Property 3."""
    report = check_tawhidic_unity(molecule)
    return report.verdict == Verdict.VERIFIED
