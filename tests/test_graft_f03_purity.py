"""
GRAFT-F03-PURITY-001 regression tests.

These tests verify that the commit/compare separation in F-03 holds:
verification observes but never writes to the object being verified.
"""

from copy import deepcopy

from fatima.core.atom import Atom
from fatima.core.bond import Bond, BondType
from fatima.core.molecule import Molecule
from fatima.properties.meaning import check_meaning_integrity
from fatima.verification.verdict import Verdict


def specimen() -> Molecule:
    m = Molecule(molecule_id="graft-f03", title="F-03 specimen")
    a1 = Atom("a1", "A proposition", "proposition")
    a2 = Atom("a2", "Supporting evidence", "evidence")
    m.add_atom(a1)
    m.add_atom(a2)
    # SUPPORTS does not require automatic reciprocal in v0.1 bond rules.
    m.add_bond(Bond(
        source_id="a2",
        target_id="a1",
        bond_type=BondType.SUPPORTS,
        weight=0.9,
        rationale="a2 supplies evidence for a1",
    ))
    m.compute_all_semantic_hashes()
    return m


def test_valid_finalised_molecule_verifies_without_mutation():
    m = specimen()
    before = deepcopy(m.to_dict())
    r = check_meaning_integrity(m)
    after = m.to_dict()
    assert r.verdict is Verdict.VERIFIED
    assert before == after


def test_bond_id_tamper_is_detected_and_not_repaired():
    m = specimen()
    stored = m.atoms["a1"].semantic_hash
    m.atoms["a1"].bond_ids.append("forged-bond-id")
    before = deepcopy(m.to_dict())

    r = check_meaning_integrity(m)

    assert r.verdict is Verdict.VIOLATED
    assert m.atoms["a1"].semantic_hash == stored
    assert m.to_dict() == before
    assert any("semantic hash mismatch" in v for v in r.violations)


def test_direct_graph_tamper_detects_stale_graph_commitment_without_rewrite():
    m = specimen()
    stored_graph_hash = m.bond_graph_hash

    forged = Bond(
        source_id="a1",
        target_id="a2",
        bond_type=BondType.REFERENCES,
        weight=0.4,
        rationale="forged direct insertion",
    )
    # Direct dict insertion deliberately bypasses add_bond() invalidation.
    m.bonds[forged.bond_id] = forged
    before = deepcopy(m.to_dict())

    r = check_meaning_integrity(m)

    assert r.verdict is Verdict.VIOLATED
    assert m.bond_graph_hash == stored_graph_hash
    assert m.to_dict() == before
    assert any("Bond graph hash mismatch" in v for v in r.violations)


def test_missing_commitments_is_unknown_not_verified():
    m = Molecule(molecule_id="unfinalised", title="Unfinalised")
    m.add_atom(Atom("a1", "Uncommitted proposition", "proposition"))
    r = check_meaning_integrity(m)
    assert r.verdict is Verdict.UNKNOWN
