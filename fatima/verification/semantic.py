"""
Level 4: Meaning-Integrity and Fitrah-Alignment Verification.
Level 5: Provenance Authenticity -- external trust anchoring.

The 0.1 architecture treated L4 as fitrah heuristics alone, and L5 as
"self-authentication through structural coherence."  Two Canon findings
drove the repair:

  F-04: check_meaning_integrity() was never wired into the verification
        pipeline.  P4 was orphaned -- its checks existed but were never
        called by verify_authenticity() or any downstream consumer.

  F-01: "Self-authentication" is forgeable.  A forged document that
        passes L1-L4 scores VERIFIED at L5 because L5 merely composed
        L1-L4 with no external evidence.

The evolved architecture:

  L4 = compose(check_meaning_integrity, verify_fitrah_alignment)
       Meaning-integrity checks (F-03 purity graft) are composed with
       fitrah heuristics.  Both are P4 concerns.

  L5 = verify_provenance(envelope, expected_commitment, key_provider)
       External trust anchoring.  Without a provenance envelope, L5 is
       UNKNOWN -- the honest default.  Self-authentication is eliminated.

This module also closes F-05 (no external anchoring): the provenance
envelope carries author signature, external time anchor, and optional
independent reviewer attestation.
"""

from __future__ import annotations

from collections import Counter
from typing import Optional

from fatima.core.bond import BondType
from fatima.core.molecule import Molecule
from fatima.properties.meaning import check_meaning_integrity
from fatima.verification.provenance import (
    ProvenanceEnvelope,
    PublicKeyProvider,
    verify_provenance,
)
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


def verify_authenticity(
    molecule: Molecule,
    provenance: Optional[ProvenanceEnvelope] = None,
    key_provider: Optional[PublicKeyProvider] = None,
) -> VerificationReport:
    """Level 5: provenance authenticity -- external trust anchoring.

    The 0.1 architecture composed L1-L4 and called the result
    "self-authentication."  Canon finding F-01 proved this is forgeable:
    a forged document scores VERIFIED because it checks its own hashes
    against itself.

    The evolved L5:
      1. Runs L1-L3 (syntactic, structural, holographic) as before.
      2. Runs L4 as the composition of meaning-integrity (F-03 purity)
         and fitrah-alignment heuristics.  This closes F-04.
      3. Composes L1-L4 into an internal-verification composite.
      4. Runs L5 as verify_provenance() -- external signature, time
         anchor, and optional reviewer attestation.  Without a
         provenance envelope, L5 is UNKNOWN.  This closes F-01 and F-05.

    The final verdict is the meet of internal verification and
    provenance.  A document cannot be VERIFIED without external evidence.
    """
    from fatima.verification.syntactic import verify_syntactic
    from fatima.verification.structural import verify_structural
    from fatima.verification.holographic import verify_holographic

    # L1-L3: unchanged
    l1 = verify_syntactic(molecule)
    l2 = verify_structural(molecule)
    l3 = verify_holographic(molecule)

    # L4: meaning-integrity (F-03 purity) composed with fitrah heuristics.
    # This closes F-04: check_meaning_integrity() is now wired in.
    l4_meaning = check_meaning_integrity(molecule)
    l4_fitrah = verify_fitrah_alignment(molecule)
    l4 = VerificationReport.compose(l4_meaning, l4_fitrah)

    # Internal verification composite (L1-L4).
    internal = VerificationReport.compose(l1, l2, l3, l4)

    # L5: provenance authenticity -- external trust anchoring.
    # The expected commitment is the molecule's bond-graph hash,
    # which is what L4 meaning-integrity just verified.
    expected_commitment = molecule.bond_graph_hash or ""
    l5_provenance = verify_provenance(
        envelope=provenance,
        expected_commitment=expected_commitment,
        key_provider=key_provider,
    )

    # Final verdict: meet of internal verification and provenance.
    all_violations = internal.violations + l5_provenance.violations
    final_verdict = internal.verdict & l5_provenance.verdict
    final_confidence = min(internal.confidence, l5_provenance.confidence)

    return VerificationReport(
        verdict=final_verdict,
        level=5,
        confidence=final_confidence,
        examined=internal.examined + l5_provenance.examined,
        total=internal.total + l5_provenance.total,
        violations=all_violations,
        level_name="authenticity",
    )
