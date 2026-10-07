"""
.fatima file format — serialisation and deserialisation.

A .fatima file is a JSON document with one of two structures:

Single molecule (documents ≤ 200 atoms):

    {
      "fatima_version": "0.1.0",
      "type": "molecule",
      "molecule": { ... },       // Molecule.to_dict()
      "verification": { ... },   // optional verification snapshot
      "encoding": { ... }        // optional holographic params
    }

Composite molecule (documents > 200 atoms):

    {
      "fatima_version": "0.1.0",
      "type": "composite",
      "composite": { ... },      // CompositeMolecule.to_dict()
      "verification": { ... },   // optional verification snapshot
      "encoding": { ... }        // optional holographic params
    }

The file extension is `.fatima`.  The format is human-readable JSON
with 2-space indentation by default.

Backward compatibility: files without a "type" field are assumed
to be single-molecule files (pre-composite format).
"""

from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional, Union

from fatima.core.composite import CompositeMolecule
from fatima.core.molecule import Molecule
from fatima.verification.verdict import Verdict, VerificationReport


def save_fatima(
    structure: Union[Molecule, CompositeMolecule],
    path: Union[str, Path],
    verification_reports: Optional[list[VerificationReport]] = None,
    encoding_params: Optional[dict] = None,
    indent: int = 2,
) -> Path:
    """Save a Molecule or CompositeMolecule to a .fatima file.

    Parameters
    ----------
    structure : Molecule | CompositeMolecule
        The molecular structure to save.
    path : str | Path
        File path.  '.fatima' extension is added if missing.
    verification_reports : list[VerificationReport] | None
        Optional verification snapshot to include.
    encoding_params : dict | None
        Optional holographic encoding parameters.
    indent : int
        JSON indentation (default 2).

    Returns
    -------
    Path
        The path the file was written to.
    """
    path = Path(path)
    if path.suffix != ".fatima":
        path = path.with_suffix(".fatima")

    is_composite = isinstance(structure, CompositeMolecule)

    doc: dict = {
        "fatima_version": "0.1.0",
        "type": "composite" if is_composite else "molecule",
    }

    if is_composite:
        doc["composite"] = structure.to_dict()
    else:
        doc["molecule"] = structure.to_dict()

    if verification_reports:
        doc["verification"] = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "levels": [
                {
                    "level": r.level,
                    "level_name": r.level_name,
                    "verdict": r.verdict.value,
                    "confidence": r.confidence,
                    "examined": r.examined,
                    "total": r.total,
                    "violations": list(r.violations),
                }
                for r in verification_reports
            ],
            "overall": {
                "verdict": VerificationReport.compose(
                    *verification_reports
                ).verdict.value,
            },
        }

    if encoding_params:
        doc["encoding"] = encoding_params

    path.write_text(
        json.dumps(doc, indent=indent, ensure_ascii=False),
        encoding="utf-8",
    )
    return path


def load_fatima(
    path: Union[str, Path],
) -> tuple[Union[Molecule, CompositeMolecule], dict]:
    """Load a Molecule or CompositeMolecule from a .fatima file.

    Parameters
    ----------
    path : str | Path
        Path to the .fatima file.

    Returns
    -------
    tuple[Molecule | CompositeMolecule, dict]
        The loaded structure and the full document metadata
        (verification snapshot, encoding params, version).
    """
    path = Path(path)
    text = path.read_text(encoding="utf-8")
    doc = json.loads(text)

    file_type = doc.get("type", "molecule")

    if file_type == "composite":
        structure = CompositeMolecule.from_dict(doc["composite"])
    else:
        # Backward compatible: "molecule" or missing type field
        structure = Molecule.from_dict(doc["molecule"])

    meta = {
        "fatima_version": doc.get("fatima_version", "unknown"),
        "type": file_type,
        "verification": doc.get("verification"),
        "encoding": doc.get("encoding"),
    }

    return structure, meta
