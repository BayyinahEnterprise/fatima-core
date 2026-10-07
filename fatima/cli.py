"""
FATIMA CLI — encode, verify, and inspect .fatima files.

Usage:
  fatima encode  <input>  [--output <path>] [--title <title>]
  fatima verify  <input>  [--sample-size <n>] [--seed <n>]
  fatima inspect <input>

Commands:
  encode   Encode a markdown/text document to .fatima format
  verify   Run all five verification levels on a .fatima file
  inspect  Print a summary of a .fatima file's structure

The encode command produces a .fatima file (JSON) containing the
molecular encoding with holographic distribution.  For documents
exceeding 200 atoms, a CompositeMolecule is produced with
hierarchical decomposition.

The verify command runs all five FATIMA verification levels:
  L1  Syntactic integrity (SHA-256 hashes)
  L2  Structural consistency (bond graph)
  L3  Holographic redundancy (reconstruction from subsets)
  L4  Fitrah-alignment (structural coherence heuristics)
  L5  Authenticity (composition of L1–L4)

The inspect command shows atom count, bond count, bond type
distribution, holographic parameters, and verification status.
"""

from __future__ import annotations

import argparse
import sys
import time
from pathlib import Path

from fatima.core.composite import CompositeMolecule
from fatima.core.molecule import Molecule
from fatima.formats.document import encode_document
from fatima.formats.serialization import load_fatima, save_fatima
from fatima.verification.composite import verify_composite
from fatima.verification.holographic import verify_holographic
from fatima.verification.semantic import verify_authenticity, verify_fitrah_alignment
from fatima.verification.structural import verify_structural
from fatima.verification.syntactic import verify_syntactic
from fatima.verification.verdict import Verdict


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="fatima",
        description=(
            "FATIMA — Fitrah-Aligned Tawhidic Integrity for "
            "Meaning and Authenticity"
        ),
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    # encode
    enc = subparsers.add_parser(
        "encode",
        help="Encode a document to .fatima format",
    )
    enc.add_argument("input", help="Input file (markdown or text)")
    enc.add_argument(
        "-o", "--output",
        help="Output .fatima file path (default: <input>.fatima)",
    )
    enc.add_argument(
        "-t", "--title",
        help="Document title",
        default="",
    )
    enc.add_argument(
        "--ratio",
        type=float,
        default=0.5,
        help="Holographic reconstruction ratio (default: 0.5)",
    )

    # verify
    ver = subparsers.add_parser(
        "verify",
        help="Verify a .fatima file through all five levels",
    )
    ver.add_argument("input", help="Input .fatima file")
    ver.add_argument(
        "--sample-size",
        type=int,
        default=20,
        help="Holographic verification sample size (default: 20)",
    )
    ver.add_argument(
        "--seed",
        type=int,
        default=None,
        help="Random seed for reproducibility",
    )

    # inspect
    ins = subparsers.add_parser(
        "inspect",
        help="Inspect a .fatima file's structure",
    )
    ins.add_argument("input", help="Input .fatima file")

    args = parser.parse_args(argv)

    if args.command == "encode":
        return cmd_encode(args)
    elif args.command == "verify":
        return cmd_verify(args)
    elif args.command == "inspect":
        return cmd_inspect(args)
    return 1


def cmd_encode(args: argparse.Namespace) -> int:
    """Encode a document to .fatima format."""
    input_path = Path(args.input)
    if not input_path.exists():
        print(f"Error: '{input_path}' not found", file=sys.stderr)
        return 1

    text = input_path.read_text(encoding="utf-8")
    title = args.title or input_path.stem

    output_path = args.output or str(input_path.with_suffix(".fatima"))

    print(f"Encoding: {input_path}")
    print(f"  Title: {title}")
    print(f"  Input: {len(text):,} characters")

    t0 = time.time()
    result = encode_document(
        text,
        title=title,
        holographic_ratio=args.ratio,
    )
    elapsed = time.time() - t0

    if isinstance(result, CompositeMolecule):
        print(f"  Type: CompositeMolecule")
        print(f"  Sub-molecules: {result.sub_molecule_count}")
        print(f"  Total atoms: {result.total_atoms}")
        print(f"  Total bonds: {result.total_bonds}")
        print(f"  Inter-bonds: {len(result.inter_bonds)}")
        print(f"  Connected: {result.is_connected()}")
    else:
        print(f"  Type: Molecule")
        print(f"  Atoms: {result.atom_count}")
        print(f"  Bonds: {result.bond_count}")

    saved = save_fatima(result, output_path)
    print(f"  Time: {elapsed:.2f}s")
    print(f"  Output: {saved} ({saved.stat().st_size:,} bytes)")
    return 0


def cmd_verify(args: argparse.Namespace) -> int:
    """Verify a .fatima file through all five levels."""
    input_path = Path(args.input)
    if not input_path.exists():
        print(f"Error: '{input_path}' not found", file=sys.stderr)
        return 1

    structure, meta = load_fatima(input_path)
    print(f"Verifying: {input_path}")
    print(f"  FATIMA version: {meta['fatima_version']}")

    t0 = time.time()

    if isinstance(structure, CompositeMolecule):
        print(f"  Type: CompositeMolecule")
        print(f"  Sub-molecules: {structure.sub_molecule_count}")
        print(f"  Total atoms: {structure.total_atoms}")
        print()

        result = verify_composite(
            structure,
            holographic_sample_size=args.sample_size,
            holographic_seed=args.seed,
        )
        elapsed = time.time() - t0

        print(result.summary())
        print(f"\n  Verification time: {elapsed:.2f}s")

        return 0 if result.overall.verdict == Verdict.VERIFIED else 1

    else:
        print(f"  Type: Molecule")
        print(f"  Atoms: {structure.atom_count}")
        print(f"  Bonds: {structure.bond_count}")
        print()

        reports = []
        level_names = [
            ("L1 Syntactic", verify_syntactic),
            ("L2 Structural", verify_structural),
        ]

        for name, fn in level_names:
            r = fn(structure)
            reports.append(r)
            _print_level(name, r)

        # L3 Holographic
        r = verify_holographic(
            structure,
            sample_size=args.sample_size,
            seed=args.seed,
        )
        reports.append(r)
        _print_level("L3 Holographic", r)

        # L4 Fitrah
        r = verify_fitrah_alignment(structure)
        reports.append(r)
        _print_level("L4 Fitrah", r)

        # L5 Authenticity (composition)
        r = verify_authenticity(structure)
        reports.append(r)
        _print_level("L5 Authenticity", r)

        elapsed = time.time() - t0
        print(f"\n  Verification time: {elapsed:.2f}s")

        overall = reports[-1]
        return 0 if overall.verdict == Verdict.VERIFIED else 1


def cmd_inspect(args: argparse.Namespace) -> int:
    """Inspect a .fatima file's structure."""
    input_path = Path(args.input)
    if not input_path.exists():
        print(f"Error: '{input_path}' not found", file=sys.stderr)
        return 1

    structure, meta = load_fatima(input_path)

    print(f"File: {input_path}")
    print(f"  Size: {input_path.stat().st_size:,} bytes")
    print(f"  FATIMA version: {meta['fatima_version']}")
    print()

    if isinstance(structure, CompositeMolecule):
        print(f"Type: CompositeMolecule")
        print(f"  Composite ID: {structure.composite_id}")
        print(f"  Title: {structure.title}")
        print(f"  Sub-molecules: {structure.sub_molecule_count}")
        print(f"  Total atoms: {structure.total_atoms}")
        print(f"  Total bonds: {structure.total_bonds}")
        print(f"  Inter-bonds: {len(structure.inter_bonds)}")
        print(f"  Connected: {structure.is_connected()}")
        print(f"  Composite hash: {structure.composite_hash[:32]}...")
        print()

        print("Sub-molecules:")
        for mid in structure.molecule_order:
            mol = structure.sub_molecules[mid]
            print(f"  {mid}:")
            print(f"    Title: {mol.title}")
            print(f"    Atoms: {mol.atom_count}")
            print(f"    Bonds: {mol.bond_count}")
            _print_bond_distribution(mol, indent=4)
    else:
        print(f"Type: Molecule")
        print(f"  Molecule ID: {structure.molecule_id}")
        print(f"  Title: {structure.title}")
        print(f"  Atoms: {structure.atom_count}")
        print(f"  Bonds: {structure.bond_count}")
        print(f"  Bond graph hash: {structure.bond_graph_hash[:32]}..."
              if structure.bond_graph_hash else "  Bond graph hash: (not computed)")
        print()

        # Content type distribution
        from collections import Counter
        type_counts = Counter(
            a.content_type for a in structure.atoms.values()
        )
        print("Content types:")
        for ct, count in type_counts.most_common():
            print(f"  {ct}: {count}")
        print()

        _print_bond_distribution(structure, indent=0)

        # Holographic info
        atoms_with_shards = sum(
            1 for a in structure.atoms.values() if a.has_shard
        )
        if atoms_with_shards:
            first_shard = next(
                a for a in structure.atoms.values() if a.has_shard
            )
            print()
            print("Holographic encoding:")
            print(f"  Atoms with shards: {atoms_with_shards}/{structure.atom_count}")
            print(f"  Threshold (k): {first_shard.shard_threshold}")
            print(f"  Total (n): {atoms_with_shards}")
            print(f"  Redundancy ratio: {first_shard.shard_threshold/atoms_with_shards:.2%}")

    # Verification snapshot
    if meta.get("verification"):
        print()
        print("Last verification:")
        v = meta["verification"]
        print(f"  Timestamp: {v['timestamp']}")
        print(f"  Overall: {v['overall']['verdict']}")
        for lvl in v.get("levels", []):
            print(f"  {lvl['level_name']} (L{lvl['level']}): "
                  f"{lvl['verdict']} ({lvl['confidence']:.0%})")

    return 0


def _print_level(name: str, report) -> None:
    """Print a single verification level result."""
    icon = {
        Verdict.VERIFIED: "VERIFIED",
        Verdict.UNKNOWN: "UNKNOWN ",
        Verdict.VIOLATED: "VIOLATED",
    }[report.verdict]
    print(f"  {name}: {icon}  "
          f"(confidence: {report.confidence:.0%}, "
          f"examined: {report.examined}/{report.total})")
    for v in report.violations:
        print(f"    - {v}")


def _print_bond_distribution(mol: Molecule, indent: int = 0) -> None:
    """Print bond type distribution."""
    from collections import Counter
    prefix = " " * indent
    bond_counts = Counter(
        b.bond_type.value for b in mol.bonds.values()
    )
    if bond_counts:
        print(f"{prefix}Bond types:")
        for bt, count in bond_counts.most_common():
            print(f"{prefix}  {bt}: {count}")


if __name__ == "__main__":
    sys.exit(main())
