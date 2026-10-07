"""
Document encoder — converts structured text to a FATIMA Molecule.

This module provides the bridge between human-readable documents
and FATIMA's molecular encoding.  It parses structured text
(markdown sections, paragraphs, sentences) into Atoms, infers
Bonds from structural relationships, applies holographic encoding,
and produces a complete Molecule ready for verification.

The encoder operates in stages:
  1. Atomisation — split the document into semantic units
  2. Bond inference — detect structural relationships between atoms
  3. Holographic encoding — distribute the bond graph across atoms
  4. Finalisation — compute semantic hashes and bond graph hash

For documents exceeding MAX_ATOMS_PER_SUB (200), the encoder
automatically decomposes into a CompositeMolecule, splitting at
section heading boundaries.  Each sub-molecule is independently
holographically encoded, and inter-molecule bonds preserve
cross-section relationships.
"""

from __future__ import annotations

import hashlib
import re
from typing import Optional, Union

from fatima.core.atom import Atom
from fatima.core.bond import Bond, BondType
from fatima.core.composite import (
    CompositeMolecule,
    InterMoleculeBond,
    MAX_ATOMS_PER_SUB,
)
from fatima.core.encoding import apply_holographic_encoding
from fatima.core.molecule import Molecule


def encode_document(
    text: str,
    title: str = "",
    molecule_id: Optional[str] = None,
    metadata: Optional[dict] = None,
    holographic_ratio: float = 0.5,
) -> Union[Molecule, CompositeMolecule]:
    """Encode a structured text document as a FATIMA Molecule.

    For documents with more than MAX_ATOMS_PER_SUB atoms, returns
    a CompositeMolecule with hierarchical decomposition.

    Parameters
    ----------
    text : str
        The document text (markdown or plain text).
    title : str
        Document title.
    molecule_id : str | None
        Unique identifier.  Generated from content hash if not given.
    metadata : dict | None
        Document-level metadata.
    holographic_ratio : float
        Fraction of atoms needed for holographic reconstruction.

    Returns
    -------
    Molecule | CompositeMolecule
        The fully encoded molecular structure.
    """
    if molecule_id is None:
        molecule_id = hashlib.sha256(text.encode("utf-8")).hexdigest()[:16]

    # Stage 1: Atomisation
    atoms = _atomise(text)

    # If within single-molecule limits, encode directly
    if len(atoms) <= MAX_ATOMS_PER_SUB:
        return _encode_single_molecule(
            atoms, text, title, molecule_id,
            metadata or {}, holographic_ratio,
        )

    # Decompose into sub-molecules at section boundaries
    return _encode_composite(
        atoms, text, title, molecule_id,
        metadata or {}, holographic_ratio,
    )


def _encode_single_molecule(
    atoms: list[Atom],
    text: str,
    title: str,
    molecule_id: str,
    metadata: dict,
    holographic_ratio: float,
) -> Molecule:
    """Encode atoms into a single Molecule (original path)."""
    mol = Molecule(
        molecule_id=molecule_id,
        title=title,
        metadata=metadata,
    )

    for atom in atoms:
        mol.add_atom(atom)

    if mol.atom_count < 2:
        mol.compute_all_semantic_hashes()
        return mol

    # Bond inference
    bonds = _infer_bonds(atoms, text)
    for bond in bonds:
        mol.add_bond(bond)

    # Holographic encoding
    if mol.atom_count >= 2:
        apply_holographic_encoding(mol, ratio=holographic_ratio)

    # Finalisation
    mol.compute_all_semantic_hashes()
    return mol


def _encode_composite(
    atoms: list[Atom],
    text: str,
    title: str,
    composite_id: str,
    metadata: dict,
    holographic_ratio: float,
) -> CompositeMolecule:
    """Decompose a large document into a CompositeMolecule.

    Splits at section heading boundaries, respecting MAX_ATOMS_PER_SUB.
    Each sub-molecule is independently holographically encoded.
    Inter-molecule bonds preserve cross-section relationships.
    """
    comp = CompositeMolecule(
        composite_id=composite_id,
        title=title,
        metadata=metadata,
    )

    # Split atoms into groups at section boundaries
    groups = _split_at_sections(atoms)

    # Create sub-molecules
    for idx, group in enumerate(groups):
        sub_id = f"{composite_id}-sub-{idx:03d}"
        # Derive sub-title from first heading in the group
        sub_title = _group_title(group, idx)

        sub_mol = Molecule(
            molecule_id=sub_id,
            title=sub_title,
            metadata={"parent_composite": composite_id, "sub_index": idx},
        )
        for atom in group:
            sub_mol.add_atom(atom)

        if sub_mol.atom_count >= 2:
            # Infer bonds within this group only
            sub_bonds = _infer_bonds(group, text)
            for bond in sub_bonds:
                sub_mol.add_bond(bond)

            # Apply holographic encoding
            apply_holographic_encoding(sub_mol, ratio=holographic_ratio)

        sub_mol.compute_all_semantic_hashes()
        comp.add_sub_molecule(sub_mol)

    # Create inter-molecule bonds between adjacent sub-molecules
    _add_inter_bonds(comp, groups)

    # Finalise composite hash
    comp.compute_composite_hash()
    return comp


def _split_at_sections(atoms: list[Atom]) -> list[list[Atom]]:
    """Split atoms into groups at section heading boundaries.

    Each group is at most MAX_ATOMS_PER_SUB atoms.  If a section
    is itself larger than the limit, it is split at sub-section
    boundaries, or if none exist, at the midpoint.
    """
    if not atoms:
        return []

    # Find section boundary indices (atoms whose content starts with '#')
    boundaries: list[int] = []
    for i, atom in enumerate(atoms):
        if atom.content.startswith("#") and i > 0:
            boundaries.append(i)

    # If no boundaries, split at even intervals
    if not boundaries:
        return _split_evenly(atoms)

    # Split at boundaries
    groups: list[list[Atom]] = []
    prev = 0
    for bnd in boundaries:
        group = atoms[prev:bnd]
        if group:
            groups.append(group)
        prev = bnd
    # Last group
    remainder = atoms[prev:]
    if remainder:
        groups.append(remainder)

    # Enforce MAX_ATOMS_PER_SUB: split any oversized group further
    final_groups: list[list[Atom]] = []
    for group in groups:
        if len(group) <= MAX_ATOMS_PER_SUB:
            final_groups.append(group)
        else:
            # Try to split at sub-headings within this group
            sub_groups = _split_group_at_subheadings(group)
            final_groups.extend(sub_groups)

    # Merge tiny groups (< 5 atoms) with their predecessor
    merged: list[list[Atom]] = []
    for group in final_groups:
        if merged and len(group) < 5 and (
            len(merged[-1]) + len(group) <= MAX_ATOMS_PER_SUB
        ):
            merged[-1].extend(group)
        else:
            merged.append(group)

    return merged if merged else [atoms]


def _split_group_at_subheadings(atoms: list[Atom]) -> list[list[Atom]]:
    """Split an oversized group at sub-heading boundaries."""
    # Look for ## or ### headings within the group
    sub_boundaries: list[int] = []
    for i, atom in enumerate(atoms):
        if atom.content.startswith("##") and i > 0:
            sub_boundaries.append(i)

    if sub_boundaries:
        groups: list[list[Atom]] = []
        prev = 0
        for bnd in sub_boundaries:
            group = atoms[prev:bnd]
            if group:
                groups.append(group)
            prev = bnd
        remainder = atoms[prev:]
        if remainder:
            groups.append(remainder)
        # Recurse if still oversized
        final: list[list[Atom]] = []
        for g in groups:
            if len(g) <= MAX_ATOMS_PER_SUB:
                final.append(g)
            else:
                final.extend(_split_evenly(g))
        return final

    return _split_evenly(atoms)


def _split_evenly(atoms: list[Atom]) -> list[list[Atom]]:
    """Split atoms into even groups of at most MAX_ATOMS_PER_SUB."""
    groups: list[list[Atom]] = []
    for i in range(0, len(atoms), MAX_ATOMS_PER_SUB):
        groups.append(atoms[i:i + MAX_ATOMS_PER_SUB])
    return groups


def _group_title(group: list[Atom], index: int) -> str:
    """Extract a title from the first heading atom in a group."""
    for atom in group:
        if atom.content.startswith("#"):
            # Strip markdown heading markers
            return atom.content.lstrip("#").strip()
    return f"Section {index + 1}"


def _add_inter_bonds(
    comp: CompositeMolecule,
    groups: list[list[Atom]],
) -> None:
    """Add inter-molecule bonds between adjacent sub-molecules.

    Creates bonds linking the last atom of each group to the
    first atom of the next group (sequential continuity), and
    cross-references between groups sharing significant terms.
    """
    mol_ids = comp.molecule_order

    # Sequential continuity bonds between adjacent sub-molecules
    for i in range(len(mol_ids) - 1):
        src_mid = mol_ids[i]
        tgt_mid = mol_ids[i + 1]
        src_mol = comp.sub_molecules[src_mid]
        tgt_mol = comp.sub_molecules[tgt_mid]

        # Last atom of source → first atom of target
        src_atoms = src_mol.atoms_by_position()
        tgt_atoms = tgt_mol.atoms_by_position()
        if src_atoms and tgt_atoms:
            comp.add_inter_bond(InterMoleculeBond(
                source_molecule=src_mid,
                source_atom=src_atoms[-1].atom_id,
                target_molecule=tgt_mid,
                target_atom=tgt_atoms[0].atom_id,
                bond_type=BondType.ELABORATES,
                weight=0.7,
                rationale="Sequential continuity between sections",
            ))

        # If target starts with a heading, the heading DEPENDS_ON
        # the concluding content of the previous section
        if tgt_atoms and tgt_atoms[0].content_type == "definition":
            comp.add_inter_bond(InterMoleculeBond(
                source_molecule=tgt_mid,
                source_atom=tgt_atoms[0].atom_id,
                target_molecule=src_mid,
                target_atom=src_atoms[-1].atom_id,
                bond_type=BondType.DEPENDS_ON,
                weight=0.6,
                rationale="Section heading builds on prior content",
            ))

    # Cross-reference bonds: invocations in any sub-molecule
    # QUALIFY atoms in all other sub-molecules (via their headings)
    for mid in mol_ids:
        mol = comp.sub_molecules[mid]
        for atom in mol.atoms.values():
            if atom.content_type == "invocation":
                # Link to the first heading of every other sub-molecule
                for other_mid in mol_ids:
                    if other_mid == mid:
                        continue
                    other_mol = comp.sub_molecules[other_mid]
                    other_atoms = other_mol.atoms_by_position()
                    if other_atoms:
                        comp.add_inter_bond(InterMoleculeBond(
                            source_molecule=mid,
                            source_atom=atom.atom_id,
                            target_molecule=other_mid,
                            target_atom=other_atoms[0].atom_id,
                            bond_type=BondType.QUALIFIES,
                            weight=0.4,
                            rationale="Invocation frames all sections",
                        ))
                break  # Only the first invocation per sub-molecule


def _atomise(text: str) -> list[Atom]:
    """Split text into semantic atoms.

    Strategy:
    - Lines starting with 'Bismillah' → 'invocation' atoms
    - Lines starting with '#' → 'definition' atoms (section headings
      define topics)
    - Lines starting with '**Definition' or '**Requirement' → 'definition'
    - Lines containing 'because', 'therefore', 'since', 'thus' and
      making a claim → 'evidence' (supporting reasoning)
    - Other substantive paragraphs → 'proposition' atoms
    """
    atoms: list[Atom] = []
    paragraphs = _split_paragraphs(text)

    for i, para in enumerate(paragraphs):
        stripped = para.strip()
        if not stripped:
            continue

        content_type = _classify_content(stripped)
        atom = Atom(
            atom_id=f"atom-{i:04d}",
            content=stripped,
            content_type=content_type,
            position=i,
        )
        atoms.append(atom)

    return atoms


def _split_paragraphs(text: str) -> list[str]:
    """Split text into meaningful paragraphs.

    Treats blank lines as paragraph separators.  Consecutive
    non-blank lines are joined into a single paragraph unless
    they start with '#' (heading) or '*' (Bismillah/emphasis).
    """
    lines = text.split("\n")
    paragraphs: list[str] = []
    current: list[str] = []

    for line in lines:
        stripped = line.strip()
        if not stripped:
            if current:
                paragraphs.append(" ".join(current))
                current = []
        elif stripped.startswith("#") or stripped.startswith("*Bismillah"):
            # Headings and invocations are their own paragraphs
            if current:
                paragraphs.append(" ".join(current))
                current = []
            paragraphs.append(stripped)
        else:
            current.append(stripped)

    if current:
        paragraphs.append(" ".join(current))

    return paragraphs


def _classify_content(text: str) -> str:
    """Classify a paragraph into a content type."""
    lower = text.lower()

    if lower.startswith("bismillah"):
        return "invocation"

    if text.startswith("#"):
        return "definition"

    if text.startswith("**Definition") or text.startswith("**Requirement"):
        return "definition"

    # Evidence indicators
    evidence_markers = [
        "because ", "therefore ", "since ", "thus ",
        "this shows ", "this demonstrates ", "evidence ",
        "for example", "this means ", "as shown ",
    ]
    claim_markers = [
        "must ", "should ", "cannot ", "requires ",
        "is necessary", "is sufficient",
    ]

    has_evidence = any(m in lower for m in evidence_markers)
    has_claim = any(m in lower for m in claim_markers)

    if has_evidence and not has_claim:
        return "evidence"
    if has_claim and not has_evidence:
        return "claim"
    if text.startswith("|") or text.startswith("---"):
        return "metadata"

    return "proposition"


def _infer_bonds(atoms: list[Atom], full_text: str) -> list[Bond]:
    """Infer bonds between atoms from structural relationships.

    Heuristics:
    1. Sequential adjacency → ELABORATES (next paragraph elaborates
       on the previous)
    2. Headings → DEFINES their subsequent content
    3. Evidence → SUPPORTS the nearest preceding claim
    4. References (explicit citations) → REFERENCES
    5. Invocations → QUALIFIES all subsequent content
    """
    bonds: list[Bond] = []
    seen_bond_ids: set[str] = set()

    def add_bond(src: str, tgt: str, btype: BondType,
                 weight: float = 0.8, rationale: str = "") -> None:
        if src == tgt:
            return
        bond = Bond(
            source_id=src,
            target_id=tgt,
            bond_type=btype,
            weight=weight,
            rationale=rationale,
        )
        if bond.bond_id not in seen_bond_ids:
            seen_bond_ids.add(bond.bond_id)
            bonds.append(bond)

    # Index atoms by type for fast lookup
    invocations = [a for a in atoms if a.content_type == "invocation"]
    definitions = [a for a in atoms if a.content_type == "definition"]
    claims = [a for a in atoms if a.content_type == "claim"]
    evidence_atoms = [a for a in atoms if a.content_type == "evidence"]

    # Rule 1: Sequential adjacency
    for i in range(len(atoms) - 1):
        curr = atoms[i]
        nxt = atoms[i + 1]
        if curr.content_type == "definition":
            # Heading defines what follows
            add_bond(curr.atom_id, nxt.atom_id, BondType.DEFINES,
                     weight=0.9, rationale="Section heading defines content")
            add_bond(nxt.atom_id, curr.atom_id, BondType.DEPENDS_ON,
                     weight=0.9, rationale="Content depends on its heading")
        else:
            add_bond(nxt.atom_id, curr.atom_id, BondType.ELABORATES,
                     weight=0.6, rationale="Sequential elaboration")

    # Rule 2: Evidence supports nearest preceding claim
    for ev in evidence_atoms:
        nearest_claim = None
        min_dist = float("inf")
        for cl in claims:
            dist = ev.position - cl.position
            if 0 < dist < min_dist:
                min_dist = dist
                nearest_claim = cl
        if nearest_claim:
            add_bond(ev.atom_id, nearest_claim.atom_id, BondType.SUPPORTS,
                     weight=0.85, rationale="Evidence supports claim")

    # Rule 3: Invocations qualify everything
    for inv in invocations:
        for atom in atoms:
            if atom.atom_id != inv.atom_id:
                add_bond(inv.atom_id, atom.atom_id, BondType.QUALIFIES,
                         weight=0.5, rationale="Invocation frames content")

    # Rule 4: Cross-references — detect shared terminology
    for i, a in enumerate(atoms):
        for j, b in enumerate(atoms):
            if i >= j:
                continue
            # Simple heuristic: shared significant words indicate reference
            words_a = set(re.findall(r'\b[A-Z][a-z]+(?:\s+[A-Z][a-z]+)*\b',
                                     a.content))
            words_b = set(re.findall(r'\b[A-Z][a-z]+(?:\s+[A-Z][a-z]+)*\b',
                                     b.content))
            shared = words_a & words_b
            # Filter out very common words
            shared -= {"The", "This", "That", "These", "Those", "Each",
                       "Every", "Any", "All", "Some", "No", "Not"}
            if len(shared) >= 2:
                add_bond(a.atom_id, b.atom_id, BondType.REFERENCES,
                         weight=0.4,
                         rationale=f"Shared terms: {shared}")

    return bonds
