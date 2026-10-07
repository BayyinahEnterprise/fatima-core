"""
Holographic encoding — threshold distribution of the bond graph.

This module implements FATIMA Property 1 (Holographic Redundancy):
any sufficient cross-section of k-of-n atoms reconstructs the complete
bond graph.  The mechanism is adapted from Shamir's Secret Sharing
(1979), but the "secret" is the serialised bond graph rather than a
scalar value.

How it works:

1. The complete bond graph is serialised to bytes.
2. The bytes are split into blocks that fit within a finite field.
3. For each block, a random polynomial of degree (k-1) is constructed
   with the block as the constant term.
4. Each atom receives one evaluation point from each polynomial —
   these evaluation points collectively form that atom's "shard".
5. Given any k atoms with their shards, Lagrange interpolation
   recovers the constant terms and thus the complete bond graph.

This is not encryption — it is structural redundancy.  The bond graph
is not hidden; it is *distributed* so that loss of up to (n-k) atoms
does not destroy the document's meaning-structure.

The threshold k is chosen so that the minimum sufficient cross-section
preserves structural coherence:
  - k = ceil(n * 0.5) for typical documents (50% redundancy)
  - k = ceil(n * 0.33) for high-redundancy (any third suffices)
  - k = n for no redundancy (every atom required)

The field is GF(2^8) for simplicity and compatibility — each byte of
the bond graph is an element of GF(256).  This is the same field used
by Reed-Solomon codes and AES, making the implementation well-studied.
"""

from __future__ import annotations

import json
import os
import zlib
from dataclasses import dataclass
from typing import Optional

import numpy as np

from fatima.core.atom import Atom
from fatima.core.bond import Bond


# --- GF(2^8) arithmetic ---
# Irreducible polynomial: x^8 + x^4 + x^3 + x + 1 = 0x11B (AES/Rijndael)
# Generator element: 3 (x+1), which is primitive — generates all 255 nonzero elements.
# Generator 2 (x) only generates a subgroup of order 51 with this polynomial.

_GF_EXP = [0] * 512  # anti-log table: _GF_EXP[i] = 3^i mod p(x)
_GF_LOG = [0] * 256  # log table: _GF_LOG[x] = i such that 3^i = x


def _gf_mul_raw(a: int, b: int) -> int:
    """Multiply two elements in GF(2^8) using shift-and-XOR.

    Used only during table initialisation (before the log/exp tables
    are available).
    """
    result = 0
    while b:
        if b & 1:
            result ^= a
        a <<= 1
        if a & 0x100:
            a ^= 0x11B
        b >>= 1
    return result


def _init_gf_tables() -> None:
    """Precompute GF(2^8) log and anti-log tables using generator 3."""
    x = 1
    for i in range(255):
        _GF_EXP[i] = x
        _GF_LOG[x] = i
        x = _gf_mul_raw(x, 3)  # multiply by generator 3
    # Wrap the exp table for convenience in modular arithmetic
    for i in range(255, 512):
        _GF_EXP[i] = _GF_EXP[i - 255]


_init_gf_tables()

# NumPy lookup tables for vectorised GF(2^8) arithmetic
_NP_GF_EXP = np.array(_GF_EXP, dtype=np.uint16)  # uint16 for safe addition
_NP_GF_LOG = np.array(_GF_LOG, dtype=np.uint16)

# Full 256×256 multiplication table for vectorised GF dot products.
# _GF_MUL_TABLE[a, b] = gf_mul(a, b).  256 KB — fits comfortably in L2 cache.
_GF_MUL_TABLE = np.zeros((256, 256), dtype=np.uint8)
for _a in range(256):
    for _b in range(256):
        if _a == 0 or _b == 0:
            _GF_MUL_TABLE[_a, _b] = 0
        else:
            _GF_MUL_TABLE[_a, _b] = _GF_EXP[_GF_LOG[_a] + _GF_LOG[_b]]


def gf_mul(a: int, b: int) -> int:
    """Multiply two elements in GF(2^8)."""
    if a == 0 or b == 0:
        return 0
    return _GF_EXP[_GF_LOG[a] + _GF_LOG[b]]


def gf_div(a: int, b: int) -> int:
    """Divide two elements in GF(2^8).  b must be nonzero."""
    if b == 0:
        raise ZeroDivisionError("Division by zero in GF(2^8)")
    if a == 0:
        return 0
    return _GF_EXP[(_GF_LOG[a] - _GF_LOG[b]) % 255]


def gf_pow(a: int, n: int) -> int:
    """Raise a to the nth power in GF(2^8)."""
    if n == 0:
        return 1
    if a == 0:
        return 0
    return _GF_EXP[(_GF_LOG[a] * n) % 255]


def gf_add(a: int, b: int) -> int:
    """Add two elements in GF(2^8) — XOR."""
    return a ^ b


# --- Shamir-style share generation and reconstruction ---

def _make_polynomial(secret_byte: int, degree: int) -> list[int]:
    """Create a random polynomial with the given constant term.

    coefficients[0] = secret_byte
    coefficients[1..degree] = random nonzero elements of GF(2^8)
    """
    coeffs = [secret_byte]
    for _ in range(degree):
        # Random nonzero coefficient
        r = 0
        while r == 0:
            r = int.from_bytes(os.urandom(1), "big")
        coeffs.append(r)
    return coeffs


def _eval_polynomial(coeffs: list[int], x: int) -> int:
    """Evaluate a polynomial at point x in GF(2^8).

    Uses Horner's method: p(x) = c0 + x*(c1 + x*(c2 + ...))
    """
    result = 0
    for c in reversed(coeffs):
        result = gf_add(gf_mul(result, x), c)
    return result


def _lagrange_interpolate(points: list[tuple[int, int]]) -> int:
    """Recover the constant term (secret) from k points via Lagrange.

    points = [(x1, y1), (x2, y2), ..., (xk, yk)]
    Returns p(0), which is the secret byte.
    """
    k = len(points)
    secret = 0
    for i in range(k):
        xi, yi = points[i]
        # Compute the Lagrange basis polynomial evaluated at x=0
        numerator = 1
        denominator = 1
        for j in range(k):
            if i == j:
                continue
            xj = points[j][0]
            # At x=0: numerator *= (0 - xj) = xj (in GF(2^8), -x = x)
            numerator = gf_mul(numerator, xj)
            # denominator *= (xi - xj) = xi ^ xj (in GF(2^8))
            denominator = gf_mul(denominator, gf_add(xi, xj))
        # basis_i(0) = numerator / denominator
        basis = gf_div(numerator, denominator)
        secret = gf_add(secret, gf_mul(yi, basis))
    return secret


def _compute_lagrange_basis(x_coords: np.ndarray) -> np.ndarray:
    """Precompute Lagrange basis coefficients L_i(0) for given x-coords.

    These depend only on the evaluation points, not on the y-values,
    so they can be computed once and reused for every byte position.

    Parameters
    ----------
    x_coords : np.ndarray, shape (k,), dtype uint8
        The evaluation points (1-indexed atom positions).

    Returns
    -------
    np.ndarray, shape (k,), dtype uint8
        The basis coefficients: basis[i] = L_i(0).
    """
    k = len(x_coords)
    basis = np.zeros(k, dtype=np.uint8)

    for i in range(k):
        xi = int(x_coords[i])
        numerator = 1
        denominator = 1
        for j in range(k):
            if i == j:
                continue
            xj = int(x_coords[j])
            numerator = gf_mul(numerator, xj)
            denominator = gf_mul(denominator, xi ^ xj)
        basis[i] = gf_div(numerator, denominator)

    return basis


def _vectorised_lagrange_decode(
    shard_matrix: np.ndarray,
    basis: np.ndarray,
) -> np.ndarray:
    """Recover all secret bytes at once via vectorised GF(2^8) dot product.

    The secret for each byte position is:
        secret[pos] = XOR_i( GF_MUL(basis[i], shard_matrix[i, pos]) )

    Using the precomputed 256×256 multiplication table turns this into
    array indexing + XOR reduction — no Python-level loops over bytes.

    Parameters
    ----------
    shard_matrix : np.ndarray, shape (k, num_bytes), dtype uint8
        Row i holds shard bytes for the i-th selected atom.
    basis : np.ndarray, shape (k,), dtype uint8
        Precomputed Lagrange basis coefficients.

    Returns
    -------
    np.ndarray, shape (num_bytes,), dtype uint8
        The recovered secret bytes.
    """
    k, num_bytes = shard_matrix.shape
    result = np.zeros(num_bytes, dtype=np.uint8)

    for i in range(k):
        b = int(basis[i])
        if b == 0:
            continue
        # _GF_MUL_TABLE[b] is a 256-element lookup: element e → gf_mul(b, e)
        # Fancy-index the entire row of shard bytes through it at once
        products = _GF_MUL_TABLE[b][shard_matrix[i]]
        result ^= products  # GF(2^8) addition is XOR

    return result


# --- Public API ---

@dataclass
class HolographicParams:
    """Parameters for holographic encoding.

    Attributes
    ----------
    threshold : int
        k — minimum number of atoms needed to reconstruct.
    total : int
        n — total number of atoms receiving shards.
    redundancy_ratio : float
        k/n — the fraction of atoms needed.
    """
    threshold: int
    total: int

    @property
    def redundancy_ratio(self) -> float:
        return self.threshold / self.total if self.total > 0 else 1.0

    @classmethod
    def for_document(cls, n_atoms: int, ratio: float = 0.5) -> HolographicParams:
        """Compute parameters for a document with n atoms.

        ratio : float
            Fraction of atoms needed for reconstruction.
            0.5 = any half suffices (default).
            0.33 = any third suffices (high redundancy).
            1.0 = all atoms required (no redundancy).
        """
        if n_atoms < 2:
            return cls(threshold=n_atoms, total=n_atoms)
        if n_atoms > 255:
            raise ValueError(
                f"GF(2^8) supports at most 255 evaluation points, "
                f"got {n_atoms} atoms.  Split into sub-molecules."
            )
        import math
        k = max(2, math.ceil(n_atoms * ratio))
        return cls(threshold=k, total=n_atoms)


def encode_holographic(
    bond_graph_json: str,
    atom_ids: list[str],
    threshold: int,
) -> dict[str, bytes]:
    """Distribute the bond graph across atoms as holographic shards.

    Parameters
    ----------
    bond_graph_json : str
        JSON-serialised bond graph (the "secret" to distribute).
    atom_ids : list[str]
        Identifiers of the atoms that will receive shards.
        Order determines the evaluation point (1-indexed).
    threshold : int
        k — minimum number of shards needed for reconstruction.

    Returns
    -------
    dict[str, bytes]
        Mapping from atom_id to its holographic shard.
        Each shard is a byte string of the same length as the
        compressed bond graph.
    """
    n = len(atom_ids)
    if threshold < 2:
        raise ValueError("Threshold must be >= 2")
    if threshold > n:
        raise ValueError(f"Threshold ({threshold}) > atom count ({n})")
    if n > 255:
        raise ValueError("GF(2^8) supports at most 255 shares")

    # Compress the bond graph to reduce shard size
    data = zlib.compress(bond_graph_json.encode("utf-8"), level=9)

    # For each byte in the compressed data, create a polynomial and
    # evaluate at each atom's point
    degree = threshold - 1
    shards: dict[str, bytearray] = {aid: bytearray() for aid in atom_ids}

    for byte_val in data:
        poly = _make_polynomial(byte_val, degree)
        for i, aid in enumerate(atom_ids):
            x = i + 1  # evaluation points are 1, 2, ..., n (never 0)
            shards[aid].append(_eval_polynomial(poly, x))

    return {aid: bytes(shard) for aid, shard in shards.items()}


def decode_holographic(
    shards: dict[str, bytes],
    atom_ids_used: list[str],
    threshold: int,
    all_atom_ids: list[str],
) -> str:
    """Reconstruct the bond graph from k-of-n holographic shards.

    Uses vectorised NumPy operations for large molecules (k >= 8):
    precomputes Lagrange basis coefficients once, then recovers all
    bytes simultaneously via the GF(2^8) multiplication table.

    For a 250-atom molecule with k=125 and ~13 KB compressed bond
    graph, this reduces ~200M Python-level GF operations to ~125
    NumPy vectorised table lookups + XOR reductions.

    Parameters
    ----------
    shards : dict[str, bytes]
        Mapping from atom_id to shard bytes.  At least k shards
        are needed.
    atom_ids_used : list[str]
        Which atom_ids from shards to use for reconstruction.
        Must have length >= threshold.
    threshold : int
        k — the threshold used during encoding.
    all_atom_ids : list[str]
        The original ordered list of all atom_ids (to determine
        evaluation points).

    Returns
    -------
    str
        The reconstructed bond graph as JSON.

    Raises
    ------
    ValueError
        If fewer than k shards are provided.
    """
    if len(atom_ids_used) < threshold:
        raise ValueError(
            f"Need at least {threshold} shards, got {len(atom_ids_used)}"
        )

    # Build the index mapping: atom_id -> evaluation point (1-indexed)
    point_map = {aid: i + 1 for i, aid in enumerate(all_atom_ids)}

    # Use the first `threshold` available shards
    selected = atom_ids_used[:threshold]
    shard_length = len(shards[selected[0]])

    # Vectorised path: precompute basis once, then batch-recover all bytes
    x_coords = np.array([point_map[aid] for aid in selected], dtype=np.uint8)
    basis = _compute_lagrange_basis(x_coords)

    # Stack all selected shards into a (k × num_bytes) matrix
    shard_matrix = np.array(
        [np.frombuffer(shards[aid], dtype=np.uint8) for aid in selected],
        dtype=np.uint8,
    )

    # Recover all secret bytes at once
    recovered_array = _vectorised_lagrange_decode(shard_matrix, basis)
    recovered = bytes(recovered_array)

    # Decompress
    data = zlib.decompress(recovered)
    return data.decode("utf-8")


def apply_holographic_encoding(
    molecule: "Molecule",
    ratio: float = 0.5,
) -> HolographicParams:
    """Apply holographic encoding to a molecule in place.

    Serialises the bond graph, distributes shards across all atoms,
    and updates each atom's holographic_shard and shard_threshold.

    Parameters
    ----------
    molecule : Molecule
        The molecule to encode.  Modified in place.
    ratio : float
        Fraction of atoms needed for reconstruction (default 0.5).

    Returns
    -------
    HolographicParams
        The encoding parameters used.
    """
    from fatima.core.molecule import Molecule

    atom_ids = [a.atom_id for a in molecule.atoms_by_position()]
    params = HolographicParams.for_document(len(atom_ids), ratio)

    if params.total < 2:
        # Single atom: no distribution possible
        for atom in molecule.atoms.values():
            atom.holographic_shard = b""
            atom.shard_threshold = params.total
        return params

    # Serialise the bond graph
    bond_data = {
        bid: bond.to_dict() for bid, bond in molecule.bonds.items()
    }
    bond_json = json.dumps(bond_data, sort_keys=True, ensure_ascii=False)

    # Distribute
    shards = encode_holographic(bond_json, atom_ids, params.threshold)

    # Apply to atoms
    for aid, shard in shards.items():
        atom = molecule.atoms[aid]
        atom.holographic_shard = shard
        atom.shard_threshold = params.threshold

    return params


def verify_holographic_reconstruction(
    molecule: "Molecule",
    subset_ids: Optional[list[str]] = None,
) -> tuple[bool, str]:
    """Verify that a subset of atoms can reconstruct the bond graph.

    If subset_ids is None, uses all atoms (should always succeed if
    the encoding is intact).

    Returns (success, reconstructed_or_error_message).
    """
    from fatima.core.molecule import Molecule

    all_ids = [a.atom_id for a in molecule.atoms_by_position()]
    use_ids = subset_ids or all_ids

    # Gather shards
    shards = {}
    for aid in use_ids:
        atom = molecule.atoms[aid]
        if atom.has_shard:
            shards[aid] = atom.holographic_shard

    if not shards:
        return False, "No holographic shards found"

    threshold = next(iter(molecule.atoms.values())).shard_threshold
    if len(shards) < threshold:
        return False, (
            f"Insufficient shards: {len(shards)} available, "
            f"{threshold} needed"
        )

    try:
        recovered_json = decode_holographic(
            shards, list(shards.keys()), threshold, all_ids
        )
        # Verify the recovered graph matches the current graph
        current_bonds = {
            bid: bond.to_dict() for bid, bond in molecule.bonds.items()
        }
        current_json = json.dumps(
            current_bonds, sort_keys=True, ensure_ascii=False
        )
        if recovered_json == current_json:
            return True, "Bond graph reconstruction verified"
        else:
            return False, "Reconstructed bond graph differs from current"
    except Exception as e:
        return False, f"Reconstruction failed: {e}"
