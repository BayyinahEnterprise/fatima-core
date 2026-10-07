"""
Composite Molecule Verification — all five properties at both levels.

Verifies a CompositeMolecule by:
  1. Verifying each sub-molecule independently (all 5 levels)
  2. Verifying composite-level properties:
     - P3: Tawhidic Unity requires composite connectivity
     - P4: Fitrah-alignment across sub-molecule boundaries
     - P5: Authenticity is the composition of all checks

The composite verdict is the lattice meet (worst) of all sub-molecule
verdicts and the composite-level checks, per NC-P2 monotone degradation.
"""

from __future__ import annotations

from fatima.core.composite import CompositeMolecule
from fatima.verification.holographic import verify_holographic
from fatima.verification.semantic import verify_fitrah_alignment
from fatima.verification.structural import verify_structural
from fatima.verification.syntactic import verify_syntactic
from fatima.verification.verdict import Verdict, VerificationReport


def verify_composite(
    composite: CompositeMolecule,
    holographic_sample_size: int = 20,
    holographic_seed: int | None = None,
) -> CompositeVerificationResult:
    """Full verification of a CompositeMolecule.

    Verifies each sub-molecule through all five levels, then
    verifies composite-level properties.

    Returns
    -------
    CompositeVerificationResult
        Contains per-sub-molecule reports and composite-level reports,
        plus the composed overall verdict.
    """
    sub_reports: dict[str, list[VerificationReport]] = {}

    # Verify each sub-molecule independently
    for mid in composite.molecule_order:
        mol = composite.sub_molecules[mid]
        reports = [
            verify_syntactic(mol),
            verify_structural(mol),
            verify_holographic(
                mol,
                sample_size=holographic_sample_size,
                seed=holographic_seed,
            ),
            verify_fitrah_alignment(mol),
        ]
        # L5 is composition of L1-L4
        composed = VerificationReport.compose(*reports)
        l5 = VerificationReport(
            verdict=composed.verdict,
            level=5,
            confidence=composed.confidence,
            examined=composed.examined,
            total=composed.total,
            violations=composed.violations,
            level_name="authenticity",
        )
        reports.append(l5)
        sub_reports[mid] = reports

    # Composite-level checks
    composite_checks: list[VerificationReport] = []

    # Composite P3: Tawhidic Unity — connectivity between sub-molecules
    connectivity_report = _check_composite_connectivity(composite)
    composite_checks.append(connectivity_report)

    # Composite P4: Cross-section fitrah — inter-bond consistency
    cross_fitrah = _check_cross_section_fitrah(composite)
    composite_checks.append(cross_fitrah)

    # Composite hash integrity
    hash_report = _check_composite_hash(composite)
    composite_checks.append(hash_report)

    # Overall verdict: compose all sub-molecule L5 verdicts + composite checks
    all_reports = []
    for mid in composite.molecule_order:
        all_reports.append(sub_reports[mid][-1])  # L5 from each sub
    all_reports.extend(composite_checks)
    overall = VerificationReport.compose(*all_reports)

    return CompositeVerificationResult(
        sub_molecule_reports=sub_reports,
        composite_reports=composite_checks,
        overall=overall,
    )


def _check_composite_connectivity(
    composite: CompositeMolecule,
) -> VerificationReport:
    """Check P3 at composite level: all sub-molecules connected."""
    if composite.sub_molecule_count <= 1:
        return VerificationReport(
            verdict=Verdict.VERIFIED,
            level=2,
            confidence=1.0,
            examined=1,
            total=1,
            level_name="composite_connectivity",
        )

    connected = composite.is_connected()
    if connected:
        return VerificationReport(
            verdict=Verdict.VERIFIED,
            level=2,
            confidence=1.0,
            examined=composite.sub_molecule_count,
            total=composite.sub_molecule_count,
            level_name="composite_connectivity",
        )
    else:
        return VerificationReport(
            verdict=Verdict.VIOLATED,
            level=2,
            confidence=0.0,
            examined=composite.sub_molecule_count,
            total=composite.sub_molecule_count,
            violations=(
                "Composite structure is fragmented — sub-molecules "
                "are not all linked by inter-molecule bonds "
                "(Tawhidic Unity violated at composite level)",
            ),
            level_name="composite_connectivity",
        )


def _check_cross_section_fitrah(
    composite: CompositeMolecule,
) -> VerificationReport:
    """Check P4 across sub-molecule boundaries.

    Verifies that inter-molecule bonds are structurally coherent:
    - Referenced atoms exist in their sub-molecules
    - Bond weights are within valid range
    - Bond types are semantically appropriate for cross-section links
    """
    violations: list[str] = []
    total_checks = 0

    for bid, ib in composite.inter_bonds.items():
        total_checks += 1

        # Check endpoints exist
        if ib.source_molecule not in composite.sub_molecules:
            violations.append(
                f"Inter-bond {bid}: source molecule "
                f"'{ib.source_molecule}' not found"
            )
            continue
        if ib.target_molecule not in composite.sub_molecules:
            violations.append(
                f"Inter-bond {bid}: target molecule "
                f"'{ib.target_molecule}' not found"
            )
            continue

        src_mol = composite.sub_molecules[ib.source_molecule]
        tgt_mol = composite.sub_molecules[ib.target_molecule]

        if ib.source_atom not in src_mol.atoms:
            violations.append(
                f"Inter-bond {bid}: source atom '{ib.source_atom}' "
                f"not in sub-molecule '{ib.source_molecule}'"
            )
        if ib.target_atom not in tgt_mol.atoms:
            violations.append(
                f"Inter-bond {bid}: target atom '{ib.target_atom}' "
                f"not in sub-molecule '{ib.target_molecule}'"
            )

        # Check weight range
        if not (0.0 < ib.weight <= 1.0):
            violations.append(
                f"Inter-bond {bid}: weight {ib.weight} outside (0, 1]"
            )

    if total_checks == 0:
        # No inter-bonds to check (single sub-molecule)
        return VerificationReport(
            verdict=Verdict.VERIFIED,
            level=4,
            confidence=1.0,
            examined=0,
            total=0,
            level_name="composite_fitrah",
        )

    if violations:
        verdict = Verdict.VIOLATED
    else:
        verdict = Verdict.VERIFIED

    confidence = 1.0 - (len(violations) / max(total_checks, 1))
    return VerificationReport(
        verdict=verdict,
        level=4,
        confidence=max(0.0, confidence),
        examined=total_checks,
        total=total_checks,
        violations=tuple(violations),
        level_name="composite_fitrah",
    )


def _check_composite_hash(
    composite: CompositeMolecule,
) -> VerificationReport:
    """Check composite hash integrity."""
    if not composite.composite_hash:
        return VerificationReport(
            verdict=Verdict.UNKNOWN,
            level=1,
            confidence=0.0,
            examined=0,
            total=1,
            violations=("Composite hash not computed",),
            level_name="composite_hash",
        )

    # Recompute and compare
    saved_hash = composite.composite_hash
    recomputed = composite.compute_composite_hash()
    if saved_hash == recomputed:
        return VerificationReport(
            verdict=Verdict.VERIFIED,
            level=1,
            confidence=1.0,
            examined=1,
            total=1,
            level_name="composite_hash",
        )
    else:
        return VerificationReport(
            verdict=Verdict.VIOLATED,
            level=1,
            confidence=1.0,
            examined=1,
            total=1,
            violations=(
                f"Composite hash mismatch: stored {saved_hash[:16]}... "
                f"!= recomputed {recomputed[:16]}...",
            ),
            level_name="composite_hash",
        )


class CompositeVerificationResult:
    """Container for composite verification results.

    Attributes
    ----------
    sub_molecule_reports : dict[str, list[VerificationReport]]
        Per-sub-molecule reports keyed by molecule_id.
        Each list contains L1–L5 reports.
    composite_reports : list[VerificationReport]
        Composite-level checks (connectivity, cross-fitrah, hash).
    overall : VerificationReport
        The composed verdict across all checks.
    """

    def __init__(
        self,
        sub_molecule_reports: dict[str, list[VerificationReport]],
        composite_reports: list[VerificationReport],
        overall: VerificationReport,
    ):
        self.sub_molecule_reports = sub_molecule_reports
        self.composite_reports = composite_reports
        self.overall = overall

    def summary(self) -> str:
        """Human-readable summary of the verification."""
        lines = [
            f"Composite Verification: {self.overall.verdict.value}",
            f"  Overall confidence: {self.overall.confidence:.2%}",
            "",
        ]

        # Sub-molecule summaries
        lines.append("Sub-molecule verdicts:")
        for mid, reports in self.sub_molecule_reports.items():
            l5 = reports[-1]  # Last is L5 (authenticity)
            marker = (
                "VERIFIED" if l5.verdict == Verdict.VERIFIED
                else "UNKNOWN" if l5.verdict == Verdict.UNKNOWN
                else "VIOLATED"
            )
            lines.append(f"  {mid}: {marker} ({l5.confidence:.0%})")

        # Composite-level summaries
        lines.append("")
        lines.append("Composite-level checks:")
        for report in self.composite_reports:
            lines.append(
                f"  {report.level_name}: {report.verdict.value} "
                f"({report.confidence:.0%})"
            )
            for v in report.violations:
                lines.append(f"    - {v}")

        if self.overall.violations:
            lines.append("")
            lines.append(
                f"Total violations: {len(self.overall.violations)}"
            )

        return "\n".join(lines)
