Bismillah ir-Rahman ir-Rahim

Procurement Concentration and Potentially Recoverable
Competitive Savings in New York City Contracting -- Audit and
Provenance Ledger
Companion to: Procurement Concentration and Potentially Recoverable Competitive Savings in
New York City Contracting (the paper, v1.0; DOI 10.5281/zenodo.21447217). This ledger and
dataset: DOI 10.5281/zenodo.21447219. Prepared under BayyinahEnterprise audit methodology
(PMD v1.2, Audit Framework v3.0). Namespace F-PC. Mirrors paper state v1.0, converged.

Current State (authoritative, as of v1.0)
•
•

•

•

•

Artifact state: v1.0, canonical converged release. Paper plus this ledger and the
reproduction and audit dataset.
Consecutive qualifying-PASS count (single operational counter): TWO. Three
qualifying rounds occurred: F-PC-R1 (NON-PASS on one HIGH), then F-PC-R2 and FPC-R3 (qualifying passes, zero CRITICAL and zero HIGH). The two-consecutive-pass
gate under Standing Rule 7 was met at F-PC-R3 and the rotation was closed by a member
new to the second pass (GPT 5.4). Any CRITICAL or HIGH in a future round resets the
count to zero.
Convergence scope (read this carefully). Convergence certifies structural honesty: that
every figure reproduces from primary sources, that the disclosures (the two dollar bases,
the Table-7-vs-Appendix-1 coverage gap, the intermediary screen) are accurate, and that
the refusal boundary holds. It does NOT certify that the savings estimate is verified
recoverable or policy-ready. The savings figures remain a conditional, pilot-gated
planning range per the paper's Section 5.0.
Honest caveats. The two consecutive passes rest on materially-identical substance (the
audited versions differ only in wording and tooling; no figure moved). Convergence is
met inside this producer-defined governance framework, while the externally-verifiable
core -- every figure reproducing from the public NYC Comptroller and data.ny.gov
sources, and the comparator being tamper-evident under the adversarial trap -- holds
independently of the framework.
Reproduction: the paper's concentration figures, all five Table 3 savings bases, the
Section 5.0 basis effect, the Appendix 1 reconciliation, and the MTA cross-check
reproduce from the bundled dataset (reproduce_procurement.py plus two hashed
CSVs and a manifest; default, --live, and --selftest modes). Deposited at DOI
10.5281/zenodo.21447219.

Verified figures (reproduced independently every round)
•
•

Sole Source (positive-amount vendor basis): 106 vendors, $1,597,506,644.98, top-1
82.5004%, top-5 90.5858%, top-10 94.0642%, top-20 97.2606%, Gini 0.95557; top
vendor NYCEDC $1,317,949,728.
Negotiated Acquisition: 462 vendors, $3,865,895,209.67, top-1 24.0334%, top-5
36.9178%, top-10 46.2163%, top-20 55.3833%, Gini 0.81855; top vendor HANYC
$929,104,960.

•
•

•
•

•

Official FY25 Table 7: Sole Source 126 / $1,599,150,768; Negotiated 962 /
$4,058,851,691; Emergency 106 / $1,326,037,939.
Five Table 3 savings bases: Core (official) $5,658,002,459; Wide (official)
$6,984,040,398; NYCEDC-adjusted official $4,340,052,731; NYCEDC-adjusted positive
$4,145,452,127; Intermediary-screened $3,410,947,771. Savings at 10% and 20% are
simple products.
Section 5.0 basis effect: official-adjusted minus positive-adjusted = $194,600,604.35;
floor deltas $19,460,060.44 (10%) / $38,920,120.87 (20%); decomposition
$192,956,481.32 (Negotiated) + $1,644,123.02 (Sole Source).
Appendix 1 reconciliation (FY2025 parent-contracts extract): Negotiated 935 rows /
$3,865,895,209.68 / 462 vendors, all positive, zero blank vendor names; Sole Source 115
rows / $1,597,506,644.98 / 106 vendors, all positive, zero blank. Coverage gaps vs Table
7: Negotiated 27 / $192,956,481.32; Sole Source 11 / $1,644,123.02. This is a coverage
difference between the summary and the extract, not intra-file attribution loss.
MTA
FY2024
cross-check
(converged
AllocationAsymmetry,
DOI
10.5281/zenodo.21445552): 13,718 records, 2,656 vendors, $65,189,755,228.64 face,
top-5 22.14%, top-10 30.4151%, Gini 0.93117.

Tier discipline
Tier 1 (byte-deterministic): hashes, concentration, the five savings bases, the basis effect, the
Appendix 1 reconciliation, the MTA constants. Tier 2 (disclosed method and judgment): the
addressable-base construction and exclusions, the positive-vs-official basis handling, the
intermediary screen, the literature-rate selection. Tier 3 (refused): whether any award should
have been competed, whether any vendor relationship is improper, whether concentration is
culpable, whether savings are truly recoverable. The paper measures; it does not accuse.

Audit history
F-PC-R1 (on v0.3) -- NON-PASS; count held at ZERO. Rotated Model Council: GPT 5.5,
GPT 5.4, Gemini 3.1 Pro qualifying; Claude Opus 4.8 advisory. Tier-1 reproduction was
unanimously clean, but GPT 5.4 raised a verified HIGH (F-PC-R1-001): the Section 5.0 basis
note claimed the NYCEDC-adjusted row "mixes the two bases by about $2M -- immaterial,"
which is false; the true cross-basis effect is $194.6M. Two qualifying members passed but did
not rebut the point (one did not examine it, one repeated the false figure at face value); under
logical adjudication a verified, unrebutted HIGH held the round NON-PASS. Supporting
findings: F-PC-R1-002 (the reconciliation mechanism and a not-reproducible HTTP-403 claim),
F-PC-R1-003 (savings breadth), F-PC-R1-004 (abstract vs body headline), F-PC-R1-005
(unqualified "Recoverable" label). All absorbed in v0.4.
F-PC-R2 (on v0.4) -- qualifying PASS; count ZERO to ONE. GPT 5.5 and Gemini 3.1 Pro
qualifying (both zero CRITICAL and zero HIGH); Claude advisory. All three independently
recomputed the Section 5.0 basis effect at $194,600,604.35, confirming the R1 HIGH was fixed,
and independently reconciled Appendix 1 (935 / 115 rows, zero blank vendors), confirming the
corrected coverage-difference mechanism. Non-blocking findings absorbed in v0.5: F-PC-R2001 (MEDIUM, conclusion floor wording conflated the NYCEDC-only floor with the

intermediary-screened sensitivity), F-PC-R2-009 (LOW, the reproduction script's note still read
"open reconciliation item"), F-PC-R2-006 (INFO, a one-cent rounding artifact).
F-PC-R3 (on v0.5) -- qualifying PASS; count ONE to TWO; CONVERGENCE MET;
rotation closed. GPT 5.5, Gemini 3.1 Pro, and GPT 5.4 qualifying (all zero CRITICAL and zero
HIGH). GPT 5.4 is new relative to the R2 clean pair and is load-bearing in the pass set, so the
two consecutive passes do not rest on an identical pair. All three confirmed the R2 fixes landed
in the shipped artifact and package, and re-derived the basis effect and Appendix 1 reconciliation
from scratch. Two non-blocking findings absorbed in v1.0: F-PC-R3-001 (LOW, a stale Section
8 limitations sentence), F-PC-R3-002 (INFO, Section 3.4 said "three savings bases" when the
tool checks five).

Producer accountability note
Several of the substantive findings across the three rounds were producer errors introduced
during revision, each caught by the audit: the false "$2M -- immaterial" basis note (F-PC-R1001, HIGH); the wrong HTTP-403 and unattributable-vendor mechanism, corrected only by
opening the file the draft claimed was blocked (F-PC-R1-002); a script-note fix that silently
failed to ship and had to be caught a second time (F-PC-R2-009); and two documentationpropagation lags (F-PC-R3-001/002). The recurring failure mode is "update some loci, not all,"
and its recurring fix is to verify every edit actually landed rather than assume. Recorded here, not
concealed. That the audit caught these on its own author is the reason a convergence claim from
it carries weight.

Refusal boundary
No divergence, batch load, award, or vendor relationship is asserted or implied to be illegitimate,
unauthorized, improper, or culpable. The concentration is framed as non-culpable structural
pattern; NYCEDC and HANYC are described as designated single-vehicle government delivery,
not private-market capture. Every savings figure is conditional and pilot-gated. Whether any
award should have been competitively bid is a Tier-3 legitimacy question, reserved for the
publisher and for oversight, and is refused here.

DOI assignment and deposit
•
•

Paper: DOI 10.5281/zenodo.21447217.
This ledger and the reproduction and audit dataset: DOI 10.5281/zenodo.21447219.
The dataset contains reproduce_procurement.py, the two hashed vendor CSVs, a
manifest, and the primary auditor reports and syntheses for all three rounds ( auditreports/). No further audit round is required unless the substance changes.



Bismillah ir-Rahman ir-Rahim
