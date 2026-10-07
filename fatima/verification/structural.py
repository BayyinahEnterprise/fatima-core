"""
Level 2: Structural Verification — cross-reference consistency.

Checks the bond graph for internal consistency:
  - All bonds reference existing atoms (no dangling bonds)
  - The bond graph is connected (Tawhidic Unity — Property 3)
  - Required reciprocal bonds exist (structural cross-referencing)
  - Atom bond_ids lists are consistent with the bond set

A failure at this level indicates either syntactic corruption
(which Level 1 should have caught) or semantic distortion
(which Level 1 *cannot* catch — this is where FATIMA begins
to cross Shannon's boundary).
"""

from __future__ import annotations

from fatima.core.molecule import Molecule
from fatima.verification.verdict import Verdict, VerificationReport


def verify_structural(molecule: Molecule) -> VerificationReport:
    """Level 2: verify bond graph internal consistency.

    Delegates to Molecule.verify_structural() but provides the
    canonical entry point for the verification architecture.
    """
    return molecule.verify_structural()
