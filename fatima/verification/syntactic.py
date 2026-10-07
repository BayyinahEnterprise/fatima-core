"""
Level 1: Syntactic Verification — bit-level integrity.

This is the baseline FATIMA inherits from Shannon's tradition.
Standard integrity checks (SHA-256 content hashes) verify that
the bits have not been altered.  This level operates *below*
Shannon's boundary — it can detect bit-level corruption but
cannot detect semantic distortion that preserves all bits.
"""

from __future__ import annotations

from fatima.core.molecule import Molecule
from fatima.verification.verdict import Verdict, VerificationReport


def verify_syntactic(molecule: Molecule) -> VerificationReport:
    """Level 1: verify that every atom's content hash matches.

    Delegates to Molecule.verify_syntactic() but provides the
    canonical entry point for the verification architecture.
    """
    return molecule.verify_syntactic()
