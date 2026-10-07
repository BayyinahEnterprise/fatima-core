"""
Property 2: Fitrah-Alignment.

The encoding must preserve the natural structural coherence of the
content — the coherence that the fitrah recognises as truth.

A FATIMA-compliant encoding must encode content in a form that
preserves the relationships, dependencies, and internal consistency
that the content inherently possesses.

Fitrah-alignment distinguishes FATIMA from mere redundancy: a message
can be holographically redundant and still be corrupt if the
redundancy encodes a distorted version of the original.
"""

from __future__ import annotations

from fatima.core.molecule import Molecule
from fatima.verification.semantic import verify_fitrah_alignment
from fatima.verification.verdict import Verdict, VerificationReport


def check_fitrah_alignment(molecule: Molecule) -> VerificationReport:
    """Check Property 2: Fitrah-Alignment.

    Returns a Level 4 verification report with heuristic checks
    for structural coherence.
    """
    return verify_fitrah_alignment(molecule)


def is_fitrah_aligned(molecule: Molecule) -> bool:
    """Quick boolean check for Property 2."""
    report = check_fitrah_alignment(molecule)
    return report.verdict == Verdict.VERIFIED
