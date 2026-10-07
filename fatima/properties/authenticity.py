"""
Property 5: Authenticity Verification via Structural Coherence.

The authentication mechanism is the structural coherence of the
encoding itself.  No external certificate, no separate signature,
no trusted third party is required.  The encoding authenticates
itself through its own internal consistency.

This is the composition of Properties 1–4: if all four are
satisfied, the encoding is authentic.  Any corruption would have
destroyed one or more of these properties, and the properties
themselves are the authentication.

This eliminates false attribution — in a system whose authenticity
is derived from its own structural coherence, forgery requires
constructing a system with the holographic property, and no
fraudulent system can exhibit the holographic property because
fraud requires inconsistency.
"""

from __future__ import annotations

from fatima.core.molecule import Molecule
from fatima.verification.semantic import verify_authenticity
from fatima.verification.verdict import Verdict, VerificationReport


def check_authenticity(molecule: Molecule) -> VerificationReport:
    """Check Property 5: Authenticity via Structural Coherence.

    Composes all five verification levels (Levels 1–5).
    """
    return verify_authenticity(molecule)


def is_authentic(molecule: Molecule) -> bool:
    """Quick boolean check for Property 5."""
    report = check_authenticity(molecule)
    return report.verdict == Verdict.VERIFIED
