"""
Composite Molecule — hierarchical decomposition for large documents.

GF(2^8) limits holographic encoding to 255 evaluation points per
molecule.  Documents exceeding this threshold are decomposed into
sub-molecules at natural structural boundaries (sections, chapters),
each with its own independent holographic encoding.

The composite structure preserves all five FATIMA properties:

  P1  Each sub-molecule is holographically encoded independently.
      Any sufficient cross-section of a sub-molecule reconstructs
      that sub-molecule's bond graph.  The composite bond graph
      is the union of all sub-molecule bond graphs plus the
      inter-molecule bonds.

  P2  Fitrah-alignment is checked per sub-molecule and globally.

  P3  Tawhidic Unity requires that the composite graph be connected
      — sub-molecules must be linked by inter-molecule bonds.

  P4  Meaning-integrity is verified at both levels: within each
      sub-molecule and across the composite.

  P5  Authenticity is the composition of all checks at both levels.

The maximum atoms per sub-molecule defaults to 200, leaving headroom
below the GF(2^8) hard limit of 255.
"""

from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass, field
from typing import Optional

from fatima.core.atom import Atom
from fatima.core.bond import Bond, BondType
from fatima.core.encoding import (
    HolographicParams,
    apply_holographic_encoding,
)
from fatima.core.molecule import Molecule
from fatima.verification.verdict import Verdict, VerificationReport


# Default maximum atoms per sub-molecule.
# Below the GF(2^8) hard limit of 255 to leave headroom
# for structural overhead.
MAX_ATOMS_PER_SUB = 200


@dataclass
class InterMoleculeBond:
    """A bond connecting atoms in different sub-molecules.

    These bonds encode cross-section relationships that would
    otherwise be lost when a document is decomposed.  They are
    not part of any sub-molecule's holographic encoding — they
    exist at the composite level and are verified separately.

    Attributes
    ----------
    source_molecule : str
        molecule_id of the sub-molecule containing the source atom.
    source_atom : str
        atom_id of the source atom.
    target_molecule : str
        molecule_id of the sub-molecule containing the target atom.
    target_atom : str
        atom_id of the target atom.
    bond_type : BondType
        Semantic type of the relationship.
    weight : float
        Strength of the relationship (0.0, 1.0].
    rationale : str
        Why this cross-section bond exists.
    """
    source_molecule: str
    source_atom: str
    target_molecule: str
    target_atom: str
    bond_type: BondType
    weight: float = 0.8
    rationale: str = ""

    @property
    def bond_id(self) -> str:
        """Deterministic ID based on endpoints and type."""
        material = (
            f"{self.source_molecule}:{self.source_atom}:"
            f"{self.target_molecule}:{self.target_atom}:"
            f"{self.bond_type.value}"
        )
        return hashlib.sha256(material.encode()).hexdigest()[:16]

    def to_dict(self) -> dict:
        return {
            "source_molecule": self.source_molecule,
            "source_atom": self.source_atom,
            "target_molecule": self.target_molecule,
            "target_atom": self.target_atom,
            "bond_type": self.bond_type.value,
            "weight": self.weight,
            "rationale": self.rationale,
        }

    @classmethod
    def from_dict(cls, data: dict) -> InterMoleculeBond:
        return cls(
            source_molecule=data["source_molecule"],
            source_atom=data["source_atom"],
            target_molecule=data["target_molecule"],
            target_atom=data["target_atom"],
            bond_type=BondType(data["bond_type"]),
            weight=data.get("weight", 0.8),
            rationale=data.get("rationale", ""),
        )


@dataclass
class CompositeMolecule:
    """A document decomposed into hierarchically encoded sub-molecules.

    Attributes
    ----------
    composite_id : str
        Unique identifier for the composite.
    title : str
        Document title.
    sub_molecules : dict[str, Molecule]
        Sub-molecules keyed by molecule_id.
    inter_bonds : dict[str, InterMoleculeBond]
        Cross-section bonds keyed by bond_id.
    metadata : dict
        Document-level metadata.
    molecule_order : list[str]
        Ordered list of sub-molecule IDs (document order).
    composite_hash : str
        SHA-256 of the entire composite structure.
    """
    composite_id: str
    title: str = ""
    sub_molecules: dict[str, Molecule] = field(default_factory=dict)
    inter_bonds: dict[str, InterMoleculeBond] = field(default_factory=dict)
    metadata: dict = field(default_factory=dict)
    molecule_order: list[str] = field(default_factory=list)
    composite_hash: str = ""

    # --- Sub-molecule operations ---

    def add_sub_molecule(self, mol: Molecule) -> None:
        """Add a sub-molecule to the composite."""
        if mol.molecule_id in self.sub_molecules:
            raise ValueError(
                f"Sub-molecule '{mol.molecule_id}' already exists"
            )
        self.sub_molecules[mol.molecule_id] = mol
        self.molecule_order.append(mol.molecule_id)
        self._invalidate_hash()

    def add_inter_bond(self, bond: InterMoleculeBond) -> None:
        """Add a cross-section bond between sub-molecules."""
        if bond.source_molecule not in self.sub_molecules:
            raise KeyError(
                f"Source sub-molecule '{bond.source_molecule}' not found"
            )
        if bond.target_molecule not in self.sub_molecules:
            raise KeyError(
                f"Target sub-molecule '{bond.target_molecule}' not found"
            )
        src_mol = self.sub_molecules[bond.source_molecule]
        tgt_mol = self.sub_molecules[bond.target_molecule]
        if bond.source_atom not in src_mol.atoms:
            raise KeyError(
                f"Source atom '{bond.source_atom}' not in "
                f"sub-molecule '{bond.source_molecule}'"
            )
        if bond.target_atom not in tgt_mol.atoms:
            raise KeyError(
                f"Target atom '{bond.target_atom}' not in "
                f"sub-molecule '{bond.target_molecule}'"
            )
        self.inter_bonds[bond.bond_id] = bond
        self._invalidate_hash()

    # --- Properties ---

    @property
    def total_atoms(self) -> int:
        return sum(m.atom_count for m in self.sub_molecules.values())

    @property
    def total_bonds(self) -> int:
        intra = sum(m.bond_count for m in self.sub_molecules.values())
        return intra + len(self.inter_bonds)

    @property
    def sub_molecule_count(self) -> int:
        return len(self.sub_molecules)

    # --- Holographic encoding ---

    def apply_holographic_encoding(
        self, ratio: float = 0.5
    ) -> list[HolographicParams]:
        """Apply holographic encoding to each sub-molecule independently.

        Returns the encoding parameters for each sub-molecule.
        """
        params = []
        for mid in self.molecule_order:
            mol = self.sub_molecules[mid]
            if mol.atom_count >= 2:
                p = apply_holographic_encoding(mol, ratio=ratio)
                params.append(p)
        return params

    def finalise(self) -> None:
        """Compute all semantic hashes and the composite hash."""
        for mol in self.sub_molecules.values():
            mol.compute_all_semantic_hashes()
        self.compute_composite_hash()

    # --- Integrity ---

    def compute_composite_hash(self) -> str:
        """SHA-256 of the entire composite structure.

        Covers all sub-molecule bond graph hashes plus all
        inter-molecule bonds.
        """
        parts = []
        for mid in self.molecule_order:
            mol = self.sub_molecules[mid]
            if not mol.bond_graph_hash:
                mol.compute_bond_graph_hash()
            parts.append(f"sub:{mid}:{mol.bond_graph_hash}")
        for bid in sorted(self.inter_bonds.keys()):
            ib = self.inter_bonds[bid]
            parts.append(
                f"inter:{ib.source_molecule}:{ib.source_atom}:"
                f"{ib.target_molecule}:{ib.target_atom}:"
                f"{ib.bond_type.value}:{ib.weight}"
            )
        material = "\n".join(parts)
        self.composite_hash = hashlib.sha256(
            material.encode("utf-8")
        ).hexdigest()
        return self.composite_hash

    def is_connected(self) -> bool:
        """Whether all sub-molecules are linked through inter-bonds.

        A disconnected composite violates Tawhidic Unity at the
        composite level.
        """
        if self.sub_molecule_count <= 1:
            return True

        adj: dict[str, set[str]] = {
            mid: set() for mid in self.sub_molecules
        }
        for ib in self.inter_bonds.values():
            adj[ib.source_molecule].add(ib.target_molecule)
            adj[ib.target_molecule].add(ib.source_molecule)

        visited: set[str] = set()
        stack = [self.molecule_order[0]]
        while stack:
            node = stack.pop()
            if node in visited:
                continue
            visited.add(node)
            stack.extend(adj[node] - visited)

        return len(visited) == self.sub_molecule_count

    def _invalidate_hash(self) -> None:
        self.composite_hash = ""

    # --- Serialisation ---

    def to_dict(self) -> dict:
        return {
            "composite_id": self.composite_id,
            "title": self.title,
            "metadata": self.metadata,
            "molecule_order": self.molecule_order,
            "composite_hash": self.composite_hash,
            "sub_molecules": {
                mid: mol.to_dict()
                for mid, mol in self.sub_molecules.items()
            },
            "inter_bonds": {
                bid: ib.to_dict()
                for bid, ib in self.inter_bonds.items()
            },
        }

    @classmethod
    def from_dict(cls, data: dict) -> CompositeMolecule:
        comp = cls(
            composite_id=data["composite_id"],
            title=data.get("title", ""),
            metadata=data.get("metadata", {}),
            molecule_order=data.get("molecule_order", []),
            composite_hash=data.get("composite_hash", ""),
        )
        for mid, mdict in data.get("sub_molecules", {}).items():
            comp.sub_molecules[mid] = Molecule.from_dict(mdict)
        for bid, ibdict in data.get("inter_bonds", {}).items():
            comp.inter_bonds[bid] = InterMoleculeBond.from_dict(ibdict)
        return comp

    def __repr__(self) -> str:
        return (
            f"CompositeMolecule(id={self.composite_id!r}, "
            f"title={self.title!r}, "
            f"sub_molecules={self.sub_molecule_count}, "
            f"total_atoms={self.total_atoms}, "
            f"total_bonds={self.total_bonds})"
        )
