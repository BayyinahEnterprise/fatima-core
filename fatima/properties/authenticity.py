"""
Property 5: Provenance Authenticity -- external trust anchoring.

The 0.1 architecture claimed self-authentication: "the encoding
authenticates itself through its own internal consistency."  Canon
finding F-01 proved this is forgeable: a forged document that passes
L1-L4 scores VERIFIED because it checks its own hashes against itself.

The evolved P5 requires external provenance evidence:
  - An author signature verified against a trust store
  - An external time anchor (RFC 3161, OpenTimestamps, etc.)
  - Optionally, an independent reviewer attestation

Without a provenance envelope, P5 is UNKNOWN.  That is the honest
default.  A deployment that has not configured provenance does not
get to claim authenticity.
"""

from __future__ import annotations

from typing import Optional

from fatima.core.molecule import Molecule
from fatima.verification.provenance import ProvenanceEnvelope, PublicKeyProvider
from fatima.verification.semantic import verify_authenticity
from fatima.verification.verdict import Verdict, VerificationReport


def check_authenticity(
    molecule: Molecule,
    provenance: Optional[ProvenanceEnvelope] = None,
    key_provider: Optional[PublicKeyProvider] = None,
) -> VerificationReport:
    """Check Property 5: Provenance Authenticity.

    Composes L1-L4 internal verification with L5 provenance check.
    Without a provenance envelope, L5 is UNKNOWN -- the honest default.
    """
    return verify_authenticity(
        molecule, provenance=provenance, key_provider=key_provider,
    )


def is_authentic(
    molecule: Molecule,
    provenance: Optional[ProvenanceEnvelope] = None,
    key_provider: Optional[PublicKeyProvider] = None,
) -> bool:
    """Quick boolean check for Property 5.

    Without provenance, this always returns False (UNKNOWN != VERIFIED).
    That is correct: authenticity cannot be claimed without external evidence.
    """
    report = check_authenticity(
        molecule, provenance=provenance, key_provider=key_provider,
    )
    return report.verdict == Verdict.VERIFIED
