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
