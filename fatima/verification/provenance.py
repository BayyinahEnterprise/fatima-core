"""
Level 5: Provenance Authenticity -- external trust anchor for FATIMA documents.

The 0.1 architecture defined L5 as self-authentication: "if L1-L4 pass, the
encoding authenticates itself through its own structural coherence." The Canon
(F-01) proved this is forgeable: a forged document scores VERIFIED because it
checks its own hashes against itself.

The evolved L5 replaces self-authentication with provenance authenticity:
a document is authentic only when an external trust root -- a signature from
a declared author verified against a trust store, plus an external time anchor
-- certifies the commitment hash that L1-L4 verified.

Without a provenance envelope, L5 is UNKNOWN. That is the honest default.
A deployment that has not configured provenance does not get to claim
authenticity.
"""

from __future__ import annotations

import hashlib
from dataclasses import dataclass
from typing import Optional, Protocol

from fatima.verification.verdict import Verdict, VerificationReport


@dataclass(frozen=True)
class ProvenanceEnvelope:
    """External provenance evidence for a FATIMA document.

    Attributes
    ----------
    author_key_id : str
        Identifier of the author's signing key.
    signature : bytes
        Ed25519 (or equivalent) signature over commitment_hash.
    commitment_hash : str
        The hash this envelope certifies -- must match the molecule's
        composite commitment (bond_graph_hash or equivalent).
    anchor_provider : str
        Name of the external time-anchor provider ("rfc3161",
        "opentimestamps", "test-double", "null").
    anchor_proof : bytes
        Provider-specific proof payload.
    anchor_timestamp : str
        ISO-8601 timestamp as claimed by the anchor provider.
    reviewer_key_id : str or None
        If an independent reviewer has attested, their key ID.
    reviewer_attestation : bytes or None
        The reviewer's signature over the commitment_hash.
    """

    author_key_id: str
    signature: bytes
    commitment_hash: str
    anchor_provider: str = "null"
    anchor_proof: bytes = b""
    anchor_timestamp: str = ""
    reviewer_key_id: Optional[str] = None
    reviewer_attestation: Optional[bytes] = None


class PublicKeyProvider(Protocol):
    """Interface for retrieving public keys by key_id."""

    def get_public_key(self, key_id: str) -> object | None:
        """Return the public key for a key_id, or None if unknown."""
        ...


class NullKeyProvider:
    """Default key provider. Returns None for all lookups.

    Yields UNKNOWN. This is the honest default when no trust store
    is configured.
    """

    def get_public_key(self, key_id: str) -> None:
        return None


def verify_provenance(
    envelope: Optional[ProvenanceEnvelope],
    expected_commitment: str,
    key_provider: PublicKeyProvider | None = None,
) -> VerificationReport:
    """Verify Level 5 provenance authenticity.

    Returns
    -------
    VerificationReport
        VERIFIED only when:
          - envelope is present
          - commitment_hash matches expected
          - author signature verifies against a known public key
          - author and reviewer keys are distinct (if reviewer present)
        UNKNOWN when evidence is absent (no envelope, no key provider,
          reviewer not present).
        VIOLATED when evidence is present but invalid (signature fails,
          commitment mismatch, key collapse).
    """
    violations: list[str] = []
    unknowns: list[str] = []
    total_checks = 0

    if envelope is None:
        return VerificationReport(
            verdict=Verdict.UNKNOWN,
            level=5,
            confidence=0.0,
            examined=0,
            total=1,
            violations=(
                "No provenance envelope supplied -- authenticity "
                "cannot be established without external evidence",
            ),
            level_name="provenance",
        )

    # Check 1: commitment hash matches what L1-L4 verified
    total_checks += 1
    if envelope.commitment_hash != expected_commitment:
        violations.append(
            "Provenance envelope covers a different commitment hash "
            "than the one L1-L4 verified"
        )

    # Check 2: author signature verification
    total_checks += 1
    if key_provider is None:
        key_provider = NullKeyProvider()

    author_pub = key_provider.get_public_key(envelope.author_key_id)
    if author_pub is None:
        unknowns.append(
            f"Author key '{envelope.author_key_id}' not found in "
            "trust store -- cannot verify signature"
        )
    else:
        try:
            from cryptography.exceptions import InvalidSignature
            author_pub.verify(  # type: ignore[union-attr]
                envelope.signature,
                envelope.commitment_hash.encode("utf-8"),
            )
        except ImportError:
            unknowns.append(
                "cryptography library not available for signature verification"
            )
        except Exception:
            violations.append(
                "Author signature verification failed"
            )

    # Check 3: external anchor
    total_checks += 1
    if envelope.anchor_provider == "null" or not envelope.anchor_proof:
        unknowns.append(
            "No external time anchor -- temporal authenticity "
            "cannot be established"
        )

    # Check 4: independence -- reviewer key != author key
    total_checks += 1
    if envelope.reviewer_key_id is None:
        unknowns.append(
            "No independent reviewer attestation on provenance"
        )
    elif envelope.reviewer_key_id == envelope.author_key_id:
        violations.append(
            "Reviewer and author share key identity -- "
            "self-attestation detected"
        )

    # Determine verdict
    if violations:
        verdict = Verdict.VIOLATED
    elif unknowns:
        verdict = Verdict.UNKNOWN
    else:
        verdict = Verdict.VERIFIED

    all_notes = tuple(violations + unknowns)
    confidence = (
        1.0 if verdict is Verdict.VERIFIED
        else max(0.0, 1.0 - len(all_notes) / max(total_checks, 1))
    )

    return VerificationReport(
        verdict=verdict,
        level=5,
        confidence=confidence,
        examined=total_checks,
        total=total_checks,
        violations=all_notes,
        level_name="provenance",
    )
