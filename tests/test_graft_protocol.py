"""
Graft protocol regression tests.

Every test begins with a graft whose status is PROPOSED or APPLIED --
not VERIFIED. The honest state of the graft at this turn is: no graft
is VERIFIED. The manifest's aggregate verdict is UNKNOWN.

These tests verify:
  1. A proposed graft is UNKNOWN, not VERIFIED
  2. An author cannot review their own graft
  3. Key collapse falsifies independence
  4. Lineage match yields UNKNOWN, not VERIFIED
  5. NullAnchor yields UNKNOWN
  6. A manifest with unreviewed grafts is UNKNOWN
  7. Test-double anchor verifies when commitment matches
  8. Fixture plumbing correctly propagates reviewer verdicts
  9. Composite gate degrades to weakest sub-molecule
"""

from fatima.graft.manifest import (
    Graft,
    GraftStatus,
    GraftManifest,
    compute_graft_verdict,
)
from fatima.graft.independence import (
    EvidenceParty,
    IndependenceRecord,
    check_independence,
)
from fatima.graft.anchor import (
    AnchorProof,
    NullAnchor,
    TestDoubleAnchor,
    verify_anchor,
)
from fatima.graft.composite import verify_composite_grafts
from fatima.graft.report import GraftReport
from fatima.graft.adversarial.fixtures import (
    PARAPHRASE_PAIRS,
    NEGATION_PAIRS,
    check_fixture_pair,
)
from fatima.verification.verdict import Verdict, VerificationReport


# --- Graft manifest tests ---


def test_proposed_graft_is_unknown_not_verified():
    g = Graft(
        graft_id="g1",
        target_path="fatima/core/atom.py",
        old_symbol="compute_semantic_hash",
        new_module="fatima.graft",
        rationale="F-03 mutating hash",
        canon_ref="F-03",
    )
    r = compute_graft_verdict(g, "author-kid")
    assert r.verdict is Verdict.UNKNOWN


def test_graft_author_cannot_review_own_graft():
    """Even a signed attestation from the author's own key yields UNKNOWN."""
    kid = "same-key-id"
    g = Graft(
        graft_id="g1",
        target_path="p",
        old_symbol="s",
        new_module="m",
        rationale="r",
        canon_ref="F-03",
        status=GraftStatus.APPLIED,
        reviewer_attestation=b"fake-signature",
        reviewer_key_id=kid,
    )
    r = compute_graft_verdict(g, kid)
    assert r.verdict is Verdict.UNKNOWN
    assert "reviewer and author share key identity" in r.notes[0]


# --- Independence tests ---


def test_independence_check_falsifies_key_collapse():
    author = EvidenceParty("author", "k1", "lineageA")
    reviewer = EvidenceParty("semantic_reviewer", "k1", "lineageA")
    rec = IndependenceRecord(author=author, semantic_reviewer=reviewer)
    r = check_independence(rec)
    assert r.verdict is Verdict.VIOLATED


def test_independence_check_lineage_match_is_unknown_not_verified():
    author = EvidenceParty("author", "k1", "lineageA")
    reviewer = EvidenceParty("semantic_reviewer", "k2", "lineageA")
    rec = IndependenceRecord(author=author, semantic_reviewer=reviewer)
    r = check_independence(rec)
    assert r.verdict is Verdict.UNKNOWN


def test_independence_distinct_keys_and_lineage():
    author = EvidenceParty("author", "k1", "lineageA")
    reviewer = EvidenceParty("semantic_reviewer", "k2", "lineageB")
    rec = IndependenceRecord(author=author, semantic_reviewer=reviewer)
    r = check_independence(rec)
    assert r.verdict is Verdict.VERIFIED


def test_independence_anchor_collapse_with_author():
    author = EvidenceParty("author", "k1", "lineageA")
    reviewer = EvidenceParty("semantic_reviewer", "k2", "lineageB")
    anchor = EvidenceParty("anchor", "k1", "lineageA")  # same key as author
    rec = IndependenceRecord(
        author=author, semantic_reviewer=reviewer, anchor=anchor
    )
    r = check_independence(rec)
    assert r.verdict is Verdict.VIOLATED
    assert "anchor key equals author key" in r.notes[0]


# --- Anchor tests ---


def test_null_anchor_yields_unknown():
    r = verify_anchor(None, NullAnchor(), "hash")
    assert r.verdict is Verdict.UNKNOWN


def test_null_anchor_with_proof_still_unknown():
    proof = AnchorProof("rfc3161", b"proof", "2026-01-01T00:00:00Z", "hash")
    r = verify_anchor(proof, NullAnchor(), "hash")
    assert r.verdict is Verdict.UNKNOWN


def test_test_double_anchor_verifies_matching_commitment():
    proof = AnchorProof("test-double", b"proof", "2026-01-01T00:00:00Z", "abc123")
    r = verify_anchor(proof, TestDoubleAnchor(), "abc123")
    assert r.verdict is Verdict.VERIFIED


def test_test_double_anchor_rejects_mismatched_commitment():
    proof = AnchorProof("test-double", b"proof", "2026-01-01T00:00:00Z", "abc123")
    r = verify_anchor(proof, TestDoubleAnchor(), "different-hash")
    assert r.verdict is Verdict.VIOLATED


# --- Manifest tests ---


def test_manifest_with_unreviewed_graft_is_unknown():
    g1 = Graft("g1", "p", "s", "m", "r", "F-03", status=GraftStatus.APPLIED)
    g2 = Graft("g2", "p2", "s2", "m2", "r2", "F-04", status=GraftStatus.PROPOSED)
    manifest = GraftManifest("release-0.2.0", (g1, g2))
    r = manifest.compute("author-kid")
    assert r.verdict is Verdict.UNKNOWN


def test_manifest_with_no_grafts_is_unknown():
    manifest = GraftManifest("empty-release", ())
    r = manifest.compute("author-kid")
    assert r.verdict is Verdict.UNKNOWN


# --- Fixture tests ---


def test_paraphrase_fixture_plumbing():
    for pair in PARAPHRASE_PAIRS:
        passed, reason = check_fixture_pair(pair, reviewer_attested_faithful=True)
        assert passed, f"{pair.fixture_id}: {reason}"


def test_negation_fixture_plumbing():
    for pair in NEGATION_PAIRS:
        passed, reason = check_fixture_pair(pair, reviewer_attested_faithful=False)
        assert passed, f"{pair.fixture_id}: {reason}"


def test_fixture_detects_inverted_reviewer_verdict():
    pair = PARAPHRASE_PAIRS[0]
    passed, reason = check_fixture_pair(pair, reviewer_attested_faithful=False)
    assert not passed
    assert "fixture expects True" in reason


# --- Composite gate tests ---


def test_composite_gate_degrades_to_weakest():
    verified_sub = VerificationReport(
        verdict=Verdict.VERIFIED, level=5, confidence=1.0,
        examined=10, total=10, level_name="sub_a",
    )
    unknown_sub = VerificationReport(
        verdict=Verdict.UNKNOWN, level=5, confidence=0.5,
        examined=5, total=10, level_name="sub_b",
    )
    inter_bond = GraftReport.ok("inter_bond", 1.0, "all bonds consistent")
    result = verify_composite_grafts(
        {"sub_a": verified_sub, "sub_b": unknown_sub},
        inter_bond,
    )
    assert result.overall.verdict is Verdict.UNKNOWN
    assert result.overall.confidence == 0.5


def test_composite_gate_empty_is_unknown():
    inter_bond = GraftReport.absent("inter_bond", "no sub-molecules")
    result = verify_composite_grafts({}, inter_bond)
    assert result.overall.verdict is Verdict.UNKNOWN


def test_composite_gate_all_verified():
    v1 = VerificationReport(
        verdict=Verdict.VERIFIED, level=5, confidence=1.0,
        examined=10, total=10, level_name="sub_a",
    )
    v2 = VerificationReport(
        verdict=Verdict.VERIFIED, level=5, confidence=0.9,
        examined=9, total=10, level_name="sub_b",
    )
    inter_bond = GraftReport.ok("inter_bond", 0.95, "bonds verified")
    result = verify_composite_grafts({"a": v1, "b": v2}, inter_bond)
    assert result.overall.verdict is Verdict.VERIFIED
    assert result.overall.confidence == 0.9
