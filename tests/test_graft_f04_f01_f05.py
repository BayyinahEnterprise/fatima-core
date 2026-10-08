"""
F-04 + F-01 + F-05 coupled graft regression tests.

These tests verify the three Canon findings are closed together:

  F-04: check_meaning_integrity() is now wired into verify_authenticity()
        as part of L4.  A molecule with tampered bonds must degrade the
        final verdict -- not silently pass.

  F-01: Self-authentication is eliminated.  A molecule that passes L1-L4
        internally but has no provenance envelope gets UNKNOWN at L5,
        never VERIFIED.

  F-05: External anchoring is required.  Only a provenance envelope with
        a verified author signature, matching commitment, and external
        time anchor can yield VERIFIED at L5.

Every test begins from the honest default: no provenance => UNKNOWN.
"""

import hashlib
from unittest.mock import MagicMock

from fatima.core.atom import Atom
from fatima.core.bond import Bond, BondType
from fatima.core.molecule import Molecule
from fatima.properties.meaning import check_meaning_integrity
from fatima.properties.authenticity import check_authenticity, is_authentic
from fatima.verification.semantic import verify_authenticity, verify_fitrah_alignment
from fatima.verification.provenance import (
    ProvenanceEnvelope,
    PublicKeyProvider,
    NullKeyProvider,
    verify_provenance,
)
from fatima.verification.verdict import Verdict


def _make_finalised_molecule() -> Molecule:
    """Build a small molecule with all commitments finalised."""
    mol = Molecule(molecule_id="test-mol")
    a1 = Atom("a1", "The treaty was sealed.", "claim")
    a2 = Atom("a2", "Historical evidence supports this.", "evidence")
    mol.add_atom(a1)
    mol.add_atom(a2)
    mol.add_bond(Bond(
        source_id="a2",
        target_id="a1",
        bond_type=BondType.SUPPORTS,
        weight=0.9,
        rationale="Evidence supports the claim",
    ))

    # Finalise: commit all hashes (BUILD-TIME)
    mol.compute_all_semantic_hashes()

    return mol


# --- F-04 tests: meaning-integrity is wired into L5 pipeline ---


def test_f04_meaning_integrity_wired_into_verify_authenticity():
    """check_meaning_integrity() must participate in verify_authenticity().

    Build a valid molecule, tamper with an atom's bond_ids, and verify
    that the final verdict reflects the meaning-integrity violation --
    not just the fitrah heuristics.
    """
    mol = _make_finalised_molecule()

    # Tamper: inject a forged bond_id into an atom without recomputing
    mol.atoms["a1"].bond_ids.append("forged-bond-id")

    # Meaning-integrity alone should catch this
    mi = check_meaning_integrity(mol)
    assert mi.verdict is Verdict.VIOLATED

    # The full pipeline must also catch it (F-04 wiring)
    full = verify_authenticity(mol)
    assert full.verdict is Verdict.VIOLATED
    assert any("semantic hash mismatch" in v.lower() for v in full.violations)


def test_f04_missing_commitments_degrade_full_pipeline():
    """A molecule with no commitments gets UNKNOWN from meaning-integrity,
    and this must propagate through the full pipeline."""
    mol = Molecule(molecule_id="no-commits")
    a1 = Atom(
        atom_id="a1",
        content="Uncommitted content",
        content_type="claim",
        holographic_shard=b"\x01" * 32,
    )
    mol.add_atom(a1)

    mi = check_meaning_integrity(mol)
    assert mi.verdict is Verdict.UNKNOWN

    full = verify_authenticity(mol)
    # UNKNOWN from meaning-integrity + UNKNOWN from no provenance
    assert full.verdict is Verdict.UNKNOWN


# --- F-01 tests: self-authentication is eliminated ---


def test_f01_no_provenance_yields_unknown_not_verified():
    """The core F-01 fix: without provenance, L5 is UNKNOWN.

    Under the 0.1 architecture, a molecule passing L1-L4 would score
    VERIFIED at L5 through "self-authentication."  That is now impossible.
    """
    mol = _make_finalised_molecule()

    # Internally valid -- L1-L4 should not find violations
    mi = check_meaning_integrity(mol)
    assert mi.verdict is Verdict.VERIFIED

    # But without provenance, the full pipeline MUST be UNKNOWN
    full = verify_authenticity(mol)
    assert full.verdict is not Verdict.VERIFIED
    assert full.verdict is Verdict.UNKNOWN
    assert any(
        "provenance" in v.lower() or "authenticity" in v.lower()
        for v in full.violations
    )


def test_f01_check_authenticity_wrapper_also_unknown_without_provenance():
    """The Property 5 wrapper must also be UNKNOWN without provenance."""
    mol = _make_finalised_molecule()
    report = check_authenticity(mol)
    assert report.verdict is Verdict.UNKNOWN


def test_f01_is_authentic_false_without_provenance():
    """The boolean convenience must return False without provenance."""
    mol = _make_finalised_molecule()
    assert is_authentic(mol) is False


# --- F-05 tests: external anchoring ---


def test_f05_provenance_with_mismatched_commitment_is_violated():
    """A provenance envelope covering a different hash than the molecule's
    bond-graph hash must yield VIOLATED."""
    mol = _make_finalised_molecule()
    envelope = ProvenanceEnvelope(
        author_key_id="author-key-001",
        signature=b"fake-sig",
        commitment_hash="wrong-hash-not-matching",
    )
    report = verify_provenance(
        envelope=envelope,
        expected_commitment=mol.bond_graph_hash,
    )
    assert report.verdict is Verdict.VIOLATED
    assert any("different commitment" in v.lower() for v in report.violations)


def test_f05_provenance_with_matching_commitment_but_no_key_is_unknown():
    """A provenance envelope with a matching commitment but no key
    in the trust store yields UNKNOWN -- we can't verify the signature."""
    mol = _make_finalised_molecule()
    envelope = ProvenanceEnvelope(
        author_key_id="author-key-001",
        signature=b"some-signature",
        commitment_hash=mol.bond_graph_hash,
    )
    report = verify_provenance(
        envelope=envelope,
        expected_commitment=mol.bond_graph_hash,
        key_provider=NullKeyProvider(),
    )
    assert report.verdict is Verdict.UNKNOWN
    assert any("not found in trust store" in v.lower() for v in report.violations)


def test_f05_provenance_null_anchor_is_unknown():
    """Without an external time anchor, temporal authenticity is UNKNOWN."""
    mol = _make_finalised_molecule()
    envelope = ProvenanceEnvelope(
        author_key_id="author-key-001",
        signature=b"some-signature",
        commitment_hash=mol.bond_graph_hash,
        anchor_provider="null",
    )
    report = verify_provenance(
        envelope=envelope,
        expected_commitment=mol.bond_graph_hash,
    )
    assert report.verdict is Verdict.UNKNOWN
    assert any("time anchor" in v.lower() for v in report.violations)


def test_f05_self_attestation_detected():
    """If reviewer and author share the same key, self-attestation
    must be flagged as VIOLATED."""
    mol = _make_finalised_molecule()
    envelope = ProvenanceEnvelope(
        author_key_id="same-key",
        signature=b"sig",
        commitment_hash=mol.bond_graph_hash,
        reviewer_key_id="same-key",
        reviewer_attestation=b"reviewer-sig",
    )
    report = verify_provenance(
        envelope=envelope,
        expected_commitment=mol.bond_graph_hash,
    )
    assert report.verdict is Verdict.VIOLATED
    assert any("self-attestation" in v.lower() for v in report.violations)


def test_f05_no_provenance_envelope_is_unknown():
    """No envelope at all must yield UNKNOWN -- not VERIFIED."""
    report = verify_provenance(
        envelope=None,
        expected_commitment="some-hash",
    )
    assert report.verdict is Verdict.UNKNOWN
    assert any("no provenance envelope" in v.lower() for v in report.violations)


# --- Integration: full pipeline with provenance ---


def test_full_pipeline_with_provenance_envelope_unknown_key():
    """Full pipeline: valid molecule + provenance envelope with unknown key.

    The molecule passes L1-L4 internally, but the provenance key is
    not in the trust store.  Final verdict: UNKNOWN (not VERIFIED).
    """
    mol = _make_finalised_molecule()
    envelope = ProvenanceEnvelope(
        author_key_id="unknown-author",
        signature=b"unverifiable-sig",
        commitment_hash=mol.bond_graph_hash,
    )
    report = verify_authenticity(
        mol,
        provenance=envelope,
        key_provider=NullKeyProvider(),
    )
    # Must be UNKNOWN because signature can't be verified
    assert report.verdict is Verdict.UNKNOWN
    assert report.level == 5
    assert report.level_name == "authenticity"


def test_full_pipeline_provenance_through_check_authenticity():
    """The P5 wrapper must pass provenance through correctly."""
    mol = _make_finalised_molecule()
    envelope = ProvenanceEnvelope(
        author_key_id="author",
        signature=b"sig",
        commitment_hash=mol.bond_graph_hash,
        reviewer_key_id="different-reviewer",
        reviewer_attestation=b"reviewer-sig",
        anchor_provider="test-double",
        anchor_proof=b"proof",
        anchor_timestamp="2026-01-01T00:00:00Z",
    )
    report = check_authenticity(
        mol, provenance=envelope, key_provider=NullKeyProvider(),
    )
    assert report.level == 5
    # Still UNKNOWN because NullKeyProvider can't verify signature
    assert report.verdict is Verdict.UNKNOWN
