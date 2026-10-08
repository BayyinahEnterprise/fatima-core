"""
Atom — the indivisible semantic unit of a FATIMA document.

An Atom is to FATIMA what a byte is to Shannon: the smallest unit
that carries meaning.  But unlike a byte, an Atom is not defined by
its bits alone.  It is defined by its content, its structural
relationships (bonds) to other atoms, and its holographic shard —
a compressed encoding of a sufficient cross-section of the entire
bond graph, so that the meaning of the whole document can be
reconstructed from any k-of-n atoms.

This mirrors the architecture of the Names: each Name is a
self-contained unit, but each Name also *contains the whole*
(the holographic property established in The Most Beautiful Names).
"""

from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Atom:
    """A semantic unit in a FATIMA document.

    Attributes
    ----------
    atom_id : str
        Unique identifier within the molecule.  Deterministic where
        possible (derived from position and content hash).
    content : str
        The semantic content of this atom — the actual text, claim,
        proposition, or data that this unit carries.
    content_type : str
        What kind of semantic unit this is: 'proposition', 'definition',
        'evidence', 'claim', 'reference', 'metadata', 'invocation'.
    content_hash : str
        SHA-256 of the content, computed on creation.  This is the
        Level 1 (syntactic) integrity marker.
    semantic_hash : str
        SHA-256 of the content + all bond identifiers + holographic
        shard.  This is the Level 2+ (structural) integrity marker.
        Empty until the atom is embedded in a molecule and its bonds
        and shard are finalised.
    bond_ids : list[str]
        Identifiers of all bonds in which this atom participates
        (as source or target).  Populated when the atom is embedded
        in a molecule.
    holographic_shard : bytes
        Compressed encoding of sufficient bond-graph structure to
        allow reconstruction of the complete molecule from any
        k-of-n atoms.  Empty until holographic encoding is applied.
    shard_threshold : int
        The k in the k-of-n threshold scheme: how many atoms (with
        their shards) are needed to reconstruct the complete bond
        graph.  Zero until holographic encoding is applied.
    position : int
        Linear position in the document (for ordering).  Semantic
        relationships are in the bonds; position is metadata.
    """

    atom_id: str
    content: str
    content_type: str = "proposition"
    content_hash: str = ""
    semantic_hash: str = ""
    bond_ids: list[str] = field(default_factory=list)
    holographic_shard: bytes = b""
    shard_threshold: int = 0
    position: int = 0

    _VALID_TYPES = frozenset({
        "proposition",   # a claim or statement
        "definition",    # defines a term or concept
        "evidence",      # supports or demonstrates a claim
        "claim",         # an assertion to be supported
        "reference",     # points to an external source
        "metadata",      # structural/bibliographic information
        "invocation",    # Bismillah or similar sacred opening
    })

    def __post_init__(self) -> None:
        if self.content_type not in self._VALID_TYPES:
            raise ValueError(
                f"Invalid content_type '{self.content_type}'. "
                f"Must be one of: {sorted(self._VALID_TYPES)}"
            )
        if not self.content_hash:
            self.content_hash = self._compute_content_hash()

    def _compute_content_hash(self) -> str:
        """SHA-256 of the content — Level 1 syntactic integrity."""
        return hashlib.sha256(self.content.encode("utf-8")).hexdigest()

    def semantic_hash_value(self) -> str:
        """Return the semantic commitment without mutating this atom.

        This is the verification-safe form.  Verification MUST call this
        method and compare the returned value with the stored commitment;
        it must never rewrite ``semantic_hash`` while deciding whether the
        stored commitment is still valid.
        """
        material = (
            self.content
            + "|"
            + ",".join(sorted(self.bond_ids))
            + "|"
            + self.holographic_shard.hex()
        )
        return hashlib.sha256(material.encode("utf-8")).hexdigest()

    def compute_semantic_hash(self) -> str:
        """Finalise and store the semantic commitment.

        This method is intentionally mutating and is therefore a BUILD-TIME
        operation only.  Verification uses :meth:`semantic_hash_value`.
        Separating commit from compare closes Canon finding F-03.
        """
        h = self.semantic_hash_value()
        self.semantic_hash = h
        return h

    def verify_syntactic(self) -> bool:
        """Level 1 verification: has the content been altered?"""
        return self.content_hash == self._compute_content_hash()

    @property
    def has_shard(self) -> bool:
        """Whether this atom carries a holographic shard."""
        return len(self.holographic_shard) > 0

    @property
    def structural_weight(self) -> int:
        """Number of bonds this atom participates in.

        Higher structural weight means the atom is more deeply
        embedded in the meaning-structure.  Per NC-P2 (Monotone
        Authority), losing a high-weight atom degrades confidence
        more than losing a low-weight atom.
        """
        return len(self.bond_ids)

    def to_dict(self) -> dict:
        """Serialise to a plain dictionary."""
        return {
            "atom_id": self.atom_id,
            "content": self.content,
            "content_type": self.content_type,
            "content_hash": self.content_hash,
            "semantic_hash": self.semantic_hash,
            "bond_ids": list(self.bond_ids),
            "holographic_shard": self.holographic_shard.hex(),
            "shard_threshold": self.shard_threshold,
            "position": self.position,
        }

    @classmethod
    def from_dict(cls, data: dict) -> Atom:
        """Deserialise from a plain dictionary."""
        atom = cls(
            atom_id=data["atom_id"],
            content=data["content"],
            content_type=data.get("content_type", "proposition"),
            content_hash=data.get("content_hash", ""),
            semantic_hash=data.get("semantic_hash", ""),
            bond_ids=data.get("bond_ids", []),
            holographic_shard=bytes.fromhex(data.get("holographic_shard", "")),
            shard_threshold=data.get("shard_threshold", 0),
            position=data.get("position", 0),
        )
        return atom

    def __repr__(self) -> str:
        preview = self.content[:60] + "..." if len(self.content) > 60 else self.content
        return (
            f"Atom(id={self.atom_id!r}, type={self.content_type!r}, "
            f"bonds={len(self.bond_ids)}, content={preview!r})"
        )
