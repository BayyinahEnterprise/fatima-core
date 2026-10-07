"""
Property 1: Holographic Redundancy.

Any sufficient cross-section of a FATIMA-compliant encoding must
reconstruct the complete message — not merely the symbols but the
meaning of the complete message.

The "sufficient cross-section" is defined structurally: any subset
that preserves the structural relationships among the message's
components.

This module provides the property check as a boolean predicate
and a detailed report.
"""

from __future__ import annotations

from fatima.core.molecule import Molecule
from fatima.verification.holographic import verify_holographic
from fatima.verification.verdict import Verdict, VerificationReport


def check_holographic_redundancy(
    molecule: Molecule,
    sample_size: int = 20,
) -> VerificationReport:
    """Check Property 1: Holographic Redundancy.

    Returns a Level 3 verification report.
    """
    return verify_holographic(molecule, sample_size=sample_size)


def is_holographically_redundant(molecule: Molecule) -> bool:
    """Quick boolean check for Property 1."""
    report = check_holographic_redundancy(molecule)
    return report.verdict == Verdict.VERIFIED
