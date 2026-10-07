"""
Level 4: Fitrah-Alignment Verification — structural coherence of meaning.

This is the most subtle level of verification and the one that most
directly crosses Shannon's boundary.  It checks whether the
reconstructed meaning exhibits the natural structural coherence
that a correctly-functioning agent would recognise as true.

In the reference implementation, fitrah-alignment is approximated by
structural heuristics:
  - Bond-weight distribution: are the weights consistent with the
    content types? (Definitions should have high-weight bonds, etc.)
  - Content-type coverage: does the molecule cover the expected
    semantic range? (A document with only 'claim' atoms and no
    'evidence' atoms is structurally suspect.)
  - Dependency completeness: do claims have supporting evidence?
    Do definitions have elaborations?

These heuristics are *approximations* of the fitrah — the natural
capacity to recognise structural coherence.  A full implementation
would require a verification agent with genuine comprehension.

Level 5 (Authenticity) follows from Levels 1–4: if all four levels
are VERIFIED, the encoding authenticates itself through its own
structural coherence (Property 5).
"""

from __future__ import annotations

from collections import Counter

from fatima.core.bond import BondType
from fatima.core.molecule import Molecule
from fatima.verification.verdict import Verdict, VerificationReport


def verify_fitrah_alignment(molecule: Molecule) -> VerificationReport:
    """Level 4: verify structural coherence of meaning.

    Checks heuristic indicators of fitrah-alignment.
    """
    violations: list[str] = []
    total_checks = 0

    if molecule.atom_count == 0:
        return VerificationReport(
            verdict=Verdict.UNKNOWN,
            level=4,
            confidence=0.0,
            examined=0,
            total=0,
            level_name="fitrah",
        )

    # Check 1: Content-type distribution
    total_checks += 1
    type_counts = Counter(a.content_type for a in molecule.atoms.values())
    claims = type_counts.get("claim", 0)
    evidence = type_counts.get("evidence", 0)
    definitions = type_counts.get("definition", 0)
    propositions = type_counts.get("proposition", 0)

    # A document with claims but no supporting evidence is structurally
    # suspect — it resembles selective emphasis (suppression of support)
    if claims > 0 and evidence == 0 and propositions == 0:
        violations.append(
            f"Fitrah warning: {claims} claims with no supporting "
            f"evidence or propositions (possible selective emphasis)"
        )

    # Check 2: Structural bond coverage
    total_checks += 1
    structural_bonds = [b for b in molecule.bonds.values() if b.is_structural]
    if molecule.bond_count > 0 and len(structural_bonds) == 0:
        violations.append(
            "No structural (load-bearing) bonds in the bond graph — "
            "the meaning-structure has no skeleton"
        )

    # Check 3: Isolated claims — claims with no incoming SUPPORTS bonds
    total_checks += 1
    unsupported_claims = []
    for atom in molecule.atoms.values():
        if atom.content_type in ("claim",):
            incoming = molecule.get_incoming_bonds(atom.atom_id)
            has_support = any(
                b.bond_type in (BondType.SUPPORTS, BondType.IMPLIES)
                for b in incoming
            )
            if not has_support:
                unsupported_claims.append(atom.atom_id)
    if unsupported_claims:
        violations.append(
            f"Unsupported claims (no SUPPORTS/IMPLIES bond): "
            f"{unsupported_claims}"
        )

    # Check 4: Definitions without elaboration
    total_checks += 1
    unelaborated_defs = []
    for atom in molecule.atoms.values():
        if atom.content_type == "definition":
            outgoing = molecule.get_outgoing_bonds(atom.atom_id)
            has_elaboration = any(
                b.bond_type == BondType.ELABORATES for b in outgoing
            )
            incoming_elab = molecule.get_incoming_bonds(atom.atom_id)
            is_elaborated = any(
                b.bond_type == BondType.ELABORATES for b in incoming_elab
            )
            if not has_elaboration and not is_elaborated:
                unelaborated_defs.append(atom.atom_id)
    if unelaborated_defs:
        violations.append(
            f"Definitions without elaboration: {unelaborated_defs}"
        )

    # Check 5: Contradictions — any CONTRADICTS bonds indicate
    # internal inconsistency (which may be intentional in a
    # dialectical document, but must be flagged)
    total_checks += 1
    contradictions = [
        b for b in molecule.bonds.values()
        if b.bond_type == BondType.CONTRADICTS
    ]
    if contradictions:
        for b in contradictions:
            violations.append(
                f"Internal contradiction: {b.source_id} CONTRADICTS "
                f"{b.target_id} — {b.rationale or '(no rationale)'}"
            )

    # Determine verdict
    examined = total_checks
    if violations:
        # Fitrah violations are warnings, not hard failures — the
        # document may be structurally incomplete rather than corrupted
        verdict = Verdict.UNKNOWN
    else:
        verdict = Verdict.VERIFIED

    confidence = 1.0 - (len(violations) / (total_checks * 2))
    confidence = max(0.0, min(1.0, confidence))

    return VerificationReport(
        verdict=verdict,
        level=4,
        confidence=confidence,
        examined=examined,
        total=total_checks,
        violations=tuple(violations),
        level_name="fitrah",
    )


def verify_authenticity(molecule: Molecule) -> VerificationReport:
    """Level 5: self-authentication through structural coherence.

    This is the composition of Levels 1–4: if all levels are
    VERIFIED, the encoding authenticates itself.  No external
    certificate is required (Property 5).

    This function does not re-run Levels 1–4.  It takes their
    results and composes them.
    """
    from fatima.verification.syntactic import verify_syntactic
    from fatima.verification.structural import verify_structural
    from fatima.verification.holographic import verify_holographic

    reports = [
        verify_syntactic(molecule),
        verify_structural(molecule),
        verify_holographic(molecule),
        verify_fitrah_alignment(molecule),
    ]

    composed = VerificationReport.compose(*reports)

    # Re-wrap as Level 5
    return VerificationReport(
        verdict=composed.verdict,
        level=5,
        confidence=composed.confidence,
        examined=composed.examined,
        total=composed.total,
        violations=composed.violations,
        level_name="authenticity",
    )
