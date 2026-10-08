"""
Molecule — a document as a molecular structure with a bond graph.

A Molecule is the complete FATIMA encoding of a document.  It consists
of Atoms (semantic units) connected by Bonds (typed semantic
relationships).  The bond graph — the complete set of bonds — is the
structure that carries meaning above Shannon's boundary.

The Molecule is the unit at which the five FATIMA properties are
evaluated:

  P1  Holographic Redundancy — any k-of-n atoms reconstruct the
      complete bond graph via their holographic shards.
  P2  Fitrah-Alignment — the bond graph preserves the natural
      structural coherence of the content.
  P3  Tawhidic Unity — removing or altering any atom or bond creates
      detectable structural inconsistency.
  P4  Meaning-Integrity — semantic distortion alters the bond graph,
      which is detectable even when all bits are preserved.
  P5  Authenticity — the structural coherence of the molecule is
      its own authentication mechanism.

Trust degradation (NC-P2): if atoms are lost or their shards cannot
be verified, the Molecule's trust level degrades monotonically — it
never silently increases.
"""

from __future__ import annotations

import hashlib
import json
from collections import defaultdict
from dataclasses import dataclass, field
from typing import Iterator, Optional

from fatima.core.atom import Atom
from fatima.core.bond import Bond, BondType
from fatima.verification.verdict import Verdict, VerificationReport


@dataclass
class Molecule:
    """A FATIMA-encoded document.

    Attributes
    ----------
    molecule_id : str
        Unique identifier for this document encoding.
    title : str
        Human-readable title of the document.
    atoms : dict[str, Atom]
        All atoms in the document, keyed by atom_id.
    bonds : dict[str, Bond]
        All bonds in the document, keyed by bond_id.
    metadata : dict
        Document-level metadata (author, date, version, etc.).
    bond_graph_hash : str
        SHA-256 of the serialised bond graph — the structural
        fingerprint of the document's meaning.
    """

    molecule_id: str
    title: str = ""
    atoms: dict[str, Atom] = field(default_factory=dict)
    bonds: dict[str, Bond] = field(default_factory=dict)
    metadata: dict = field(default_factory=dict)
    bond_graph_hash: str = ""

    # --- Atom operations ---

    def add_atom(self, atom: Atom) -> None:
        """Add an atom to the molecule."""
        if atom.atom_id in self.atoms:
            raise ValueError(f"Atom '{atom.atom_id}' already exists in molecule")
        self.atoms[atom.atom_id] = atom
        self._invalidate_graph_hash()

    def get_atom(self, atom_id: str) -> Atom:
        """Retrieve an atom by ID."""
        if atom_id not in self.atoms:
            raise KeyError(f"No atom with id '{atom_id}' in molecule")
        return self.atoms[atom_id]

    def remove_atom(self, atom_id: str) -> Atom:
        """Remove an atom and all its bonds.

        Returns the removed atom for inspection.  This operation
        is structurally detectable (Property 3, Tawhidic Unity):
        every bond referencing the removed atom becomes dangling.
        """
        atom = self.atoms.pop(atom_id)
        # Remove all bonds involving this atom
        to_remove = [
            bid for bid, bond in self.bonds.items()
            if bond.source_id == atom_id or bond.target_id == atom_id
        ]
        for bid in to_remove:
            del self.bonds[bid]
        # Clean bond_ids from remaining atoms
        for remaining in self.atoms.values():
            remaining.bond_ids = [
                bid for bid in remaining.bond_ids if bid not in to_remove
            ]
        self._invalidate_graph_hash()
        return atom

    # --- Bond operations ---

    def add_bond(self, bond: Bond) -> None:
        """Add a bond between two atoms.

        Both atoms must already exist in the molecule.  The bond's
        ID is registered in both participating atoms' bond_ids lists.
        """
        if bond.source_id not in self.atoms:
            raise KeyError(
                f"Source atom '{bond.source_id}' not in molecule"
            )
        if bond.target_id not in self.atoms:
            raise KeyError(
                f"Target atom '{bond.target_id}' not in molecule"
            )
        if bond.bond_id in self.bonds:
            raise ValueError(
                f"Bond '{bond.bond_id}' already exists "
                f"({bond.source_id} -> {bond.target_id} [{bond.bond_type.value}])"
            )
        self.bonds[bond.bond_id] = bond
        self.atoms[bond.source_id].bond_ids.append(bond.bond_id)
        self.atoms[bond.target_id].bond_ids.append(bond.bond_id)
        self._invalidate_graph_hash()

    def get_bonds_for(self, atom_id: str) -> list[Bond]:
        """All bonds in which an atom participates."""
        return [
            bond for bond in self.bonds.values()
            if bond.source_id == atom_id or bond.target_id == atom_id
        ]

    def get_outgoing_bonds(self, atom_id: str) -> list[Bond]:
        """Bonds where the given atom is the source."""
        return [
            bond for bond in self.bonds.values()
            if bond.source_id == atom_id
        ]

    def get_incoming_bonds(self, atom_id: str) -> list[Bond]:
        """Bonds where the given atom is the target."""
        return [
            bond for bond in self.bonds.values()
            if bond.target_id == atom_id
        ]

    # --- Graph analysis ---

    @property
    def atom_count(self) -> int:
        return len(self.atoms)

    @property
    def bond_count(self) -> int:
        return len(self.bonds)

    @property
    def structural_bond_count(self) -> int:
        """Number of load-bearing (structural) bonds."""
        return sum(1 for b in self.bonds.values() if b.is_structural)

    def adjacency(self) -> dict[str, set[str]]:
        """Undirected adjacency list of the bond graph."""
        adj: dict[str, set[str]] = defaultdict(set)
        for bond in self.bonds.values():
            adj[bond.source_id].add(bond.target_id)
            adj[bond.target_id].add(bond.source_id)
        # Include isolated atoms
        for aid in self.atoms:
            if aid not in adj:
                adj[aid] = set()
        return dict(adj)

    def is_connected(self) -> bool:
        """Whether the bond graph is connected.

        An unconnected molecule violates Property 3 (Tawhidic Unity):
        the encoding has been fragmented into independent parts.
        """
        if not self.atoms:
            return True
        adj = self.adjacency()
        start = next(iter(self.atoms))
        visited: set[str] = set()
        stack = [start]
        while stack:
            node = stack.pop()
            if node in visited:
                continue
            visited.add(node)
            stack.extend(adj.get(node, set()) - visited)
        return len(visited) == len(self.atoms)

    def connected_components(self) -> list[set[str]]:
        """Return the connected components of the bond graph."""
        adj = self.adjacency()
        visited: set[str] = set()
        components: list[set[str]] = []
        for start in self.atoms:
            if start in visited:
                continue
            component: set[str] = set()
            stack = [start]
            while stack:
                node = stack.pop()
                if node in visited:
                    continue
                visited.add(node)
                component.add(node)
                stack.extend(adj.get(node, set()) - visited)
            components.append(component)
        return components

    def dangling_bonds(self) -> list[Bond]:
        """Bonds that reference atoms not in the molecule.

        Any dangling bond is evidence of tampering or data loss —
        a violation of Property 3 (Tawhidic Unity).
        """
        return [
            bond for bond in self.bonds.values()
            if bond.source_id not in self.atoms
            or bond.target_id not in self.atoms
        ]

    def missing_reciprocals(self) -> list[tuple[Bond, BondType]]:
        """Bonds whose type implies a reciprocal that is absent.

        Per Requirement 1 (Chapter 14), structural cross-referencing
        requires that bond relationships be reciprocated where the
        type demands it.  Missing reciprocals are a structural
        inconsistency (Level 2 verification failure).
        """
        missing = []
        for bond in self.bonds.values():
            recip_type = bond.reciprocal_type()
            if recip_type is None:
                continue
            # Check if the reciprocal bond exists
            expected = Bond(
                source_id=bond.target_id,
                target_id=bond.source_id,
                bond_type=recip_type,
            )
            if expected.bond_id not in self.bonds:
                missing.append((bond, recip_type))
        return missing

    # --- Integrity ---

    def bond_graph_hash_value(self) -> str:
        """Return the current bond-graph commitment without mutation.

        Verification-safe: this function observes the graph and returns its
        deterministic SHA-256 commitment.  It does not rewrite the stored
        ``bond_graph_hash``.
        """
        bond_strings = sorted(
            f"{b.source_id}:{b.target_id}:{b.bond_type.value}:{b.weight}"
            for b in self.bonds.values()
        )
        material = "\n".join(bond_strings)
        return hashlib.sha256(material.encode("utf-8")).hexdigest()

    def compute_bond_graph_hash(self) -> str:
        """Finalise and store the current bond-graph commitment.

        BUILD-TIME operation.  Verification must call
        :meth:`bond_graph_hash_value` and compare, never rewrite.
        """
        self.bond_graph_hash = self.bond_graph_hash_value()
        return self.bond_graph_hash

    def compute_all_semantic_hashes(self) -> None:
        """Recompute semantic hashes for all atoms.

        Must be called after all bonds and shards are finalised.
        """
        for atom in self.atoms.values():
            atom.compute_semantic_hash()
        self.compute_bond_graph_hash()

    def _invalidate_graph_hash(self) -> None:
        """Mark the graph hash as stale after structural change."""
        self.bond_graph_hash = ""

    # --- Verification (basic structural checks) ---

    def verify_structural(self) -> VerificationReport:
        """Level 2 structural verification.

        Checks:
        1. No dangling bonds (all referenced atoms exist)
        2. Bond graph is connected (Tawhidic Unity)
        3. All required reciprocal bonds exist
        4. All atom bond_ids lists are consistent with the bond set
        """
        violations: list[str] = []
        total_checks = 0

        # Check 1: dangling bonds
        dangling = self.dangling_bonds()
        total_checks += len(self.bonds)
        if dangling:
            for b in dangling:
                violations.append(
                    f"Dangling bond {b.bond_id}: "
                    f"{b.source_id} -> {b.target_id} [{b.bond_type.value}]"
                )

        # Check 2: connectivity
        total_checks += 1
        if not self.is_connected():
            components = self.connected_components()
            violations.append(
                f"Bond graph is disconnected: {len(components)} components "
                f"(Tawhidic Unity violation)"
            )

        # Check 3: reciprocal bonds
        missing = self.missing_reciprocals()
        total_checks += len(self.bonds)  # each bond checked for reciprocal
        for bond, expected_type in missing:
            violations.append(
                f"Missing reciprocal: {bond.target_id} -> {bond.source_id} "
                f"[{expected_type.value}] expected for "
                f"{bond.source_id} -> {bond.target_id} [{bond.bond_type.value}]"
            )

        # Check 4: bond_id consistency
        total_checks += len(self.atoms)
        for atom in self.atoms.values():
            for bid in atom.bond_ids:
                if bid not in self.bonds:
                    violations.append(
                        f"Atom '{atom.atom_id}' references non-existent "
                        f"bond '{bid}'"
                    )

        examined = total_checks
        if violations:
            verdict = Verdict.VIOLATED
        elif not self.atoms:
            verdict = Verdict.UNKNOWN
        else:
            verdict = Verdict.VERIFIED

        confidence = 1.0 if total_checks > 0 else 0.0
        return VerificationReport(
            verdict=verdict,
            level=2,
            confidence=confidence,
            examined=examined,
            total=total_checks,
            violations=tuple(violations),
            level_name="structural",
        )

    def verify_syntactic(self) -> VerificationReport:
        """Level 1 syntactic verification.

        Checks that every atom's content hash matches its content.
        """
        violations: list[str] = []
        for atom in self.atoms.values():
            if not atom.verify_syntactic():
                violations.append(
                    f"Atom '{atom.atom_id}' content hash mismatch "
                    f"(syntactic integrity violation)"
                )

        total = len(self.atoms)
        if violations:
            verdict = Verdict.VIOLATED
        elif total == 0:
            verdict = Verdict.UNKNOWN
        else:
            verdict = Verdict.VERIFIED

        return VerificationReport(
            verdict=verdict,
            level=1,
            confidence=1.0 if total > 0 else 0.0,
            examined=total,
            total=total,
            violations=tuple(violations),
            level_name="syntactic",
        )

    # --- Iteration ---

    def atoms_by_position(self) -> list[Atom]:
        """Atoms in document order."""
        return sorted(self.atoms.values(), key=lambda a: a.position)

    def __iter__(self) -> Iterator[Atom]:
        """Iterate atoms in document order."""
        return iter(self.atoms_by_position())

    # --- Serialisation ---

    def to_dict(self) -> dict:
        """Serialise the complete molecule to a plain dictionary."""
        return {
            "molecule_id": self.molecule_id,
            "title": self.title,
            "metadata": self.metadata,
            "bond_graph_hash": self.bond_graph_hash,
            "atoms": {aid: a.to_dict() for aid, a in self.atoms.items()},
            "bonds": {bid: b.to_dict() for bid, b in self.bonds.items()},
        }

    @classmethod
    def from_dict(cls, data: dict) -> Molecule:
        """Deserialise from a plain dictionary."""
        mol = cls(
            molecule_id=data["molecule_id"],
            title=data.get("title", ""),
            metadata=data.get("metadata", {}),
            bond_graph_hash=data.get("bond_graph_hash", ""),
        )
        # Reconstruct atoms first
        for aid, adict in data.get("atoms", {}).items():
            mol.atoms[aid] = Atom.from_dict(adict)
        # Then bonds
        for bid, bdict in data.get("bonds", {}).items():
            mol.bonds[bid] = Bond.from_dict(bdict)
        return mol

    def to_json(self, indent: int = 2) -> str:
        """Serialise to JSON."""
        return json.dumps(self.to_dict(), indent=indent, ensure_ascii=False)

    @classmethod
    def from_json(cls, text: str) -> Molecule:
        """Deserialise from JSON."""
        return cls.from_dict(json.loads(text))

    def __repr__(self) -> str:
        return (
            f"Molecule(id={self.molecule_id!r}, title={self.title!r}, "
            f"atoms={self.atom_count}, bonds={self.bond_count})"
        )
