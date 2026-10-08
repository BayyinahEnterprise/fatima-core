"""
External anchor interface -- pluggable external time reference.

The prototype's anchor_ref as a free string was a placeholder, not an
interface. A real anchor requires a service that produces a verifiable
timestamp the author cannot forge.

Absent a configured anchor provider, the anchor level is UNKNOWN --
never assumed satisfied by a string.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol

from fatima.graft.report import GraftReport


@dataclass(frozen=True)
class AnchorProof:
    """A verifiable external timestamp proof.

    Attributes
    ----------
    provider : str
        Provider type ("rfc3161", "opentimestamps", "test-double").
    payload : bytes
        Provider-specific proof bytes.
    anchored_at : str
        ISO-8601 timestamp as claimed by provider.
    commitment_hash : str
        The hash the anchor covers.
    """

    provider: str
    payload: bytes
    anchored_at: str
    commitment_hash: str


class AnchorProvider(Protocol):
    """Interface every anchor provider must satisfy.

    A provider that cannot verify its own proofs is not a provider;
    it is a second author. The independence check at the anchor layer
    requires that the provider's verification code path is not the
    author's.
    """

    name: str

    def verify(self, proof: AnchorProof, expected_hash: str) -> bool:
        """Verify an anchor proof against an expected commitment hash."""
        ...


class NullAnchor:
    """Default provider. Returns False. Yields UNKNOWN.

    This is not a failure mode; it is the honest default. A deployment
    that has not configured an anchor does not get to claim one.
    """

    name = "null"

    def verify(self, proof: AnchorProof, expected_hash: str) -> bool:
        return False


class TestDoubleAnchor:
    """Test-only provider. Verifies if commitment_hash matches expected.

    For regression tests only. This provider does not contact an external
    service and therefore does not provide real external anchoring.
    """

    name = "test-double"

    def verify(self, proof: AnchorProof, expected_hash: str) -> bool:
        return proof.commitment_hash == expected_hash


def verify_anchor(
    proof: AnchorProof | None,
    provider: AnchorProvider,
    expected_commitment_hash: str,
) -> GraftReport:
    """Verify an external anchor proof.

    Returns
    -------
    GraftReport
        VERIFIED only if a real provider confirms the proof covers
        the expected commitment. UNKNOWN if no proof or null provider.
        VIOLATED if proof covers a different commitment or provider rejects.
    """
    if proof is None:
        return GraftReport.absent(
            "anchor", "no external anchor proof supplied"
        )
    if provider.name == "null":
        return GraftReport.absent(
            "anchor",
            "no anchor provider configured; default is null",
        )
    if proof.commitment_hash != expected_commitment_hash:
        return GraftReport.invalid(
            "anchor", "anchor covers a different commitment"
        )
    if not provider.verify(proof, expected_commitment_hash):
        return GraftReport.invalid(
            "anchor", "provider rejected its own proof"
        )
    return GraftReport.ok(
        "anchor", 1.0, f"verified by {provider.name}"
    )
