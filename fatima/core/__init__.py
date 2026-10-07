"""
fatima.core — Atomic data structures for FATIMA encoding.

Atom  — the indivisible semantic unit
Bond  — typed semantic relationship between atoms
Molecule — document as molecular structure with bond graph
CompositeMolecule — hierarchical decomposition for large documents
InterMoleculeBond — cross-section bond between sub-molecules
"""

from fatima.core.bond import Bond, BondType
from fatima.core.atom import Atom
from fatima.core.molecule import Molecule
from fatima.core.composite import CompositeMolecule, InterMoleculeBond

__all__ = [
    "Atom", "Bond", "BondType", "Molecule",
    "CompositeMolecule", "InterMoleculeBond",
]
