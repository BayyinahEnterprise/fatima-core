Bismillah ir-Rahman ir-Rahim

Empirical Results from 31 Rounds of Multi-Model Structural Honesty Audit
Version: 1.3.1
Bilal Syed Arfeen
2026-08-19
Prepared with Claude Opus 4.6 (Anthropic) as analytical and drafting instrument under the author’s direction
and final authority. This paper makes no effectiveness claim about any component of the Structural Honesty
program.
Bismillah ar-Rahman ar-Rahim

Abstract
We report the empirical results of 31 audit rounds on the XZ Protocol, a construct-validation preregistration
for structural-decision replay of the XZ Utils supply-chain compromise (CVE-2024-3094). The audit program
produced 199 seat reports from five core vendor families (Anthropic, OpenAI, Google, Moonshot, Zhipu)
plus two incidental entries, yielding 832 structured findings (136 Class A byte-false claims). The primary
result is a 25-round consecutive Class A recurrence series (R7–R31): in every round, at least one byte-false
claim about the instrument’s verification properties was identified. Of the 25 rounds, 19 have individually
extracted Class A findings in the structured corpus (102 findings); 5 have Class A substance identifiable
at description level; 1 (R15) rests on the companion synthesis paper (ASSERTED, not COMPUTED from
this corpus). The recurrence witness table (shipped as recurrence_witness.csv) documents the per-round
evidence. The secondary result is a defect migration trajectory: Class A findings appear across all five
classified locus layers (code/CI, cross-layer consistency, provenance/amendment, methodology/dispatch, and
unclassified) with recurrence at previously cleared layers rather than a one-way architectural ascent. The
row-level migration classification (shipped as migration_classification.csv) documents the per-finding
layer assignment. These results are consistent with a self-referential incompleteness analogy. This paper
publishes the methods, results, and failures; no result is suppressed.

1. Introduction
The Structural Honesty Verification (SHV) program asks whether a software artifact’s claims about its
own properties are testable against independently observable evidence. The program’s instrument – the
XZ Protocol – is a preregistered contract for replaying the structural decisions that enabled the XZ Utils
supply-chain compromise (CVE-2024-3094), under conditions where the payload is excluded and only the
decision structure is examined.
The audit program tests this instrument against itself. Independent AI systems from different vendor families
examine the protocol text, its executable verification code, its amendment record, and its claims about its
own verification properties. Each audit round produces findings classified by severity and, from R7 onward,
by defect class (A through E). The program’s central question is whether the Class A (byte-false claim) count
converges to zero.
It does not. This paper reports what the program found, how it found it, and what the persistent recurrence
suggests about the limits of self-referential verification.

1

2. Methods
2.1 Audit design
Each round follows a seven-phase cycle: tuning, dispatch, performance, filtering, triage, bearer assessment,
and judgment. The methodology is documented in the Structural Honesty Verification Methodology v7
Canonical.
2.2 Seat architecture
The audit program’s governance design assigns seats across five core vendor families. The producer family
(Anthropic, Claude) is barred from carry weight. Two non-producer families (Moonshot Kimi K3 and Zhipu
GLM-5.2) hold carrying authority. OpenAI GPT-5.6 Sol serves as adversarial advisory. Google Gemini 3.1
Pro serves as advisory.
In the R7–R31 series, 68 seat reports were extracted, with 1 to 9 reports per round (median 3). The family
breakdown: Anthropic 24, OpenAI 30, Google 11, Moonshot 3, Zhipu 0. Zhipu contributed zero R7–R31
reports; all 23 Zhipu reports in the corpus fall in earlier eras. Per-report finding rates: Anthropic 12.2,
OpenAI 3.8, Google 1.5, Moonshot 1.3. The Anthropic rate may partly reflect the producer family’s detailed
knowledge of the artifact; the carrying families’ lower rates represent genuinely independent verification.
2.3 Corpus construction
The XZ Structural Honesty Audit Corpus provides the structured evidence. The construction procedure
(extract_corpus.py v0.6) walks 199 seat reports, applies 18 regex patterns, and outputs 832 rows of structured
data. The corpus, its construction procedure, and its dataset card are deposited separately.
2.4 Limitations of the structured evidence
The structured corpus is an extraction, not the full evidence. 75% of findings carry no class tag. 27% have no
extracted round number. Some round-number assignments contain extraction artifacts (notably, 28 findings
from a v0.71 peer-review report are tagged R7 rather than their likely R28 provenance; one report is tagged
R36 due to a version-number parsing artifact). The full evidence base includes the seat reports themselves,
the round triages, and the verdict records, which are available in the program’s handoff archives but not
deposited as structured data.
For the 6 R7–R31 rounds where Class A is not individually classified in the finding headers, the per-round
evidence basis is documented in recurrence_witness.csv:
• R9: Finding F-S01-50-01 description reads “Class A (byte-level error)” (DESCRIPTION-LEVEL).
• R10: Report metadata records class_a_count = 4 (REPORT-METADATA); descriptions include
byte-false substance.
• R11: Report metadata records class_a_count = 3 (REPORT-METADATA); descriptions contain
“Class A” references.
• R15: No in-packet evidence. Class A presence is ASSERTED from the companion Heartbeat paper.
This is the only round whose Class A basis is entirely external to the shipped structured data.
• R28: Descriptions reference byte-false claims (phantom repair, fail-open gate) without using the “Class
A” label. Class A presence is supported at description level and ASSERTED from the Heartbeat paper.
• R29: Descriptions contain “Class A – String N, Position M” with empty class fields (DESCRIPTIONLEVEL).

3. Results
3.1 Primary result: 25-round Class A recurrence
Every round from R7 through R31 contained at least one Class A finding. Of the 25 rounds, 19 have individually
classified Class A findings in the structured corpus (102 findings total); 5 have Class A substance at description
2

level; 1 (R15) rests on an external source. The recurrence witness table (recurrence_witness.csv) documents
the per-round evidence and its type (COMPUTED, DESCRIPTION-LEVEL, REPORT-METADATA, or
ASSERTED).
The Laplace predictive probability of recurrence at R32, treating the 25-round series as 25 successes in
a Bernoulli sequence, is (25 + 1) / (25 + 2) = 0.963. This is an arithmetic convention for expressing
recurrence confidence, not an inferential estimate; the Bernoulli-exchangeability assumption is not satisfied
by an adversarial repair process, and the Laplace rule carries no weight beyond the convention.
3.2 Secondary result: defect migration trajectory
The 102 R7–R31 Class A findings were classified into five locus layers using an algorithmic rule applied to the
locus and description fields. The classification script counts matches against layer-specific keyword sets
(code/CI terms, cross-layer terms, provenance terms, methodology terms); the highest-scoring layer is assigned
as primary; findings matching no layer are classified as Other/unclassified; findings matching multiple layers
are assigned to the highest-scoring layer with the mixed-layer status noted in the rationale column. The rowlevel assignments are shipped as migration_classification.csv, produced by classify_migration.py
(also shipped).
Layer

Description

Findings

Observed rounds

Code/CI

Build.py, register
generator,
extract_findings, CI
gates
Title, status, Section 0.1,
FB-7b, Section 25
No layer-specific
keyword match, opaque
locus, or empty locus
Tagging, audit context,
witness, scribe
Section 27, Section 22,
append-only, sealed
entries

41

R8, R13, R17–R21,
R26–R27, R30–R31

23

R8, R13, R16, R24,
R26–R27, R30–R31
R7, R12–R14, R16–R19,
R30–R31

Cross-layer consistency
Other/unclassified
Methodology/dispatch
Provenance/amendment

21
11

R7, R21–R23, R25, R27,
R30–R31
R7–R8, R30–R31

6

The trajectory shows migration with recurrence. No layer is permanently cleared: Code/CI appears in R8
and R13, peaks at R17–R21, and recurs at R26–R27 and R30–R31. Provenance appears early (R7–R8) and
recurs at R30–R31 with an append-only violation. Cross-layer consistency appears across the entire series.
The trajectory is not a one-way architectural ascent; it is a persistent recurrence across layers, with the
dominant locus shifting over time.
3.3 Severity distribution
The 428 R7–R31 findings distribute as:
Severity

Count

Pct

CRITICAL
HIGH
MEDIUM
LOW
INFORMATIONAL
(not extracted)

15
224
104
67
13
5

3.5%
52.3%
24.3%
15.7%
3.0%
1.2%

3

3.4 Verdict distribution
Of 68 R7–R31 seat reports: 63 HALT (93%), 3 CONDITIONAL PASS (4%), 1 PASS (1%), 1 not extracted
(1%). No round achieved unanimous PASS across all seats.
3.5 Cross-program context
Three programs in the SHV chain produced convergence trajectories. These are historical observations from
the program’s records, not a controlled comparison; the programs differ in units, stopping rules, defect classes,
and governance structures. The instance and round counts are sourced from the respective program deposits
(References 1–4), not re-derived from this packet.
Program

Trajectory

Outcome

BSSG (Ref. 4)

34 instances across 37 passes

SHVVP (Ref. 3)

7 HALTs (v0.1–v0.7)

XZ Protocol

25 rounds (R7–R31)

Defect class emptied; trajectory
ended
Trust-boundary discipline
converged; first carry at v0.8
Class A persisted with layer
migration; did not converge to
zero

4. Failures and negative results
4.1 Class A did not converge to zero
This is the primary negative result. The program interprets this through the self-referential incompleteness
analogy (Section 5.1), while acknowledging alternative explanations.
4.2 Carrying-seat underrepresentation
The two carrying families produced only 3 reports in R7–R31 (4% of 68), all from Moonshot. Zhipu contributed
zero R7–R31 reports. The governance design assigns carrying authority to Moonshot and Zhipu, but the
actual evidence base does not reflect that authority.
4.3 Extraction coverage
75% of findings carry no class tag. 27% have no extracted round number. 5% have empty descriptions.
The migration layer classification (Section 3.2) is algorithmically derived but depends on keyword matching
against locus and description strings, which is sensitive to the extractor’s output quality; 21 of 102 findings
(21%) are classified as Other/unclassified.
4.4 The FROZEN amendment
The XZ Protocol v0.75 froze with Class A still present. The amendment (Section 22 item 8) allows FROZEN
when the remaining Class A is “demonstrated structurally irremediable” and disclosed. This converts a
falsifiable gate (all Class A = 0) into a gate where the acceptance criterion depends partly on the lead’s
judgment that the residual is self-referential. The program discloses this conversion; it does not claim the
original gate is preserved.

4

5. Discussion
5.1 The self-referential incompleteness analogy
The 25-round series is consistent with a self-referential incompleteness analogy. The defect migration trajectory
shows that each verification layer, once secured, does not remain permanently clear; the defect recurs across
layers with the dominant surface shifting. The persistent residual is the instrument’s claims about its own
verification properties.
This observation is analogous to Goedel’s incompleteness theorem (a sufficiently expressive formal system
cannot prove its own consistency from within), but it is not a formal theorem and does not establish that the
non-convergence is structurally unavoidable. The empirical recurrence may have causes other than formal
self-reference: evolving specifications, human edits, extractor limitations, model error, governance rules, or
the specific structure of the artifact under audit. The Sidrat clause – “This instrument cannot verify that it
has no remaining byte-false claims about its own verification properties” – is a disclosed boundary motivated
by the empirical record, not a proved impossibility.
5.2 What the program does not claim
This paper does not claim that SHV prevents, mitigates, detects, or ensures anything. The program’s contribution is the observation that a bounded verification instrument, operated with cross-vendor independence
and append-only governance, produces a specific empirical trajectory. Whether that trajectory is useful for
software security is a question for implementers, not for this paper.

6. Conclusion
The XZ Protocol audit program produced 832 findings across 31 rounds. The primary result – 25 consecutive
rounds with Class A present – is the program’s central empirical contribution. The secondary result – a defect
migration trajectory with recurrence across code/CI, cross-layer, provenance, methodology, and unclassified
surfaces – characterizes the shape of the non-convergence. The self-referential incompleteness analogy provides
the interpretive frame. The Sidrat clause provides the honest disclosure.
The instrument is finite. The verification is bounded. The defect persists. The record is the evidence.

References
1. AX-SH5 Flagship: 10.5281/zenodo.21500700
2. SHUDP: 10.5281/zenodo.21522932
3. SHVVP v0.8: 10.5281/zenodo.21583202
4. BSSG: 10.5281/zenodo.21713180
5. BAF v3.0: 10.5281/zenodo.20017335
6. PMD: 10.5281/zenodo.21462879
7. SHV Method: 10.5281/zenodo.21449063
8. A5 evidence-independence: 10.5281/zenodo.21539074
9. Dissertation v1.4: 10.5281/zenodo.21501912
10. XZ Corpus: 10.5281/zenodo.22007364
11. XZ Protocol v0.75: 10.5281/zenodo.21984212
12. Heartbeat paper: 10.5281/zenodo.21985646
Bilal Syed Arfeen Structural Honesty Validation Program – August 2026
“As for the foam, it vanishes, being cast off. But as for that which benefits the people, it remains in the
earth.” (Qur’an 13:17)
5



Bismillah ir-Rahman ir-Rahim
