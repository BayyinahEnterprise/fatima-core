Bismillah ir-Rahman ir-Rahim

Structural Regularities in AI-Assisted Audit Chains:
A Pilot Study in Predictive Finding Localization
Bilal Syed Arfeen
BayyinahEnterprise
bayyinahenterprises@tuta.com
ABSTRACT
When AI-generated code is audited iteratively across multiple releases, the sequence of findings
exhibits structural regularities that are not visible in any single audit round but emerge from
the longitudinal chain. We extract eleven such regularities (R1–R11) from a five-finding pilot
chain (F22–F26) drawn from a 43-round audit corpus spanning three repositories and four
primary language substrates. In a pre-registered retrospective experiment, a predictor
conditioned on the structured audit-chain log achieved 10/10 hits across five dimensions (failing
step, error code, substrate layer, fix-size class, and root cause) on two held-out findings. We
report this result with three explicit caveats: the predictor shared context with the chain's
producing instance, the scoring dimensions are coarse (P4 has only four classes; P5 scores
mechanism presence without requiring exclusion of alternatives), and the ablation control
separating chain-derived prediction from general LLM priors was designed but not yet
executed. We also frame the five-dimension prediction as a Hamming-distance scoring
problem on a fixed-length codeword, which clarifies why coarse categorical hits accumulate
easily and motivates stricter dimension-weighted analysis. The contribution is not the hit rate
but the regularities themselves: failure-mode shift, step monotonicity, error-code locality,
cross-language seam recurrence, and seven others. These are properties of the corpus, not of
the predictor, and are independently verifiable from the published dataset. We release the
structured audit-chain log as a Zenodo dataset and pre-register a cross-instance ablation study
as the Phase 2 follow-up.
Keywords: software audit, AI-assisted development, defect prediction, audit methodology, structural
honesty, predictive prompting, mining software repositories, Hamming-distance scoring

1 INTRODUCTION
AI-assisted software development produces code at unprecedented speed. GitHub Copilot alone
serves over one million paid subscribers (Nadella 2023). Claude Code, Cursor, and Codex are used
daily by engineering teams across industries. The code these tools produce is syntactically correct,
passes tests, and reads cleanly to human reviewers. It also ships with structural defects that
existing static analyzers, type checkers, and security scanners do not detect (Arfeen 2026a).
The gap is categorical. Existing tools ask whether code is correct – does it type-check, does it
satisfy the specification, does it have known vulnerability patterns. None ask whether code is
honest – does it keep the promises it makes? A function that claims to return patient allergy data
but silently returns nothing on database-connection failure is type-correct, passes tests against a
mocked database, and reads cleanly to a reviewer. It is also structurally dishonest: its surface claim
(returns allergies) diverges from its substrate behavior (sometimes returns nothing without
notice). This divergence class – the surface–substrate gap – is the target of the structural-honesty

1

Structural Regularities in AI-Assisted Audit Chains

Arfeen · Pilot Study

discipline formalized in the Bayyinah Audit Framework (Arfeen 2026a, 2026b).
The Bayyinah Audit Framework has been applied across 43 documented rounds on three
repositories, producing a longitudinal record: each round documents what was checked, what was
found, what severity was assigned, what fix was applied, and what the next round subsequently
surfaced. This record – the audit chain – is the dataset this paper examines.
1.1 Motivating Observation
The motivating observation is empirical. When a new diagnostic class is added to a static analyzer's
internal registry but the command-line printer's dispatch table is not updated, the diagnostic
silently fails to display. This happened in round 34 of the furqan-lint audit chain. It had also
happened, in structurally isomorphic form, in rounds 29 and 35. The pattern – adding a member to
a structural group without updating all co-members – recurred three times before an automated
gate was introduced to prevent it. A predictor with access to the chain's history would have flagged
the omission at round 29, before the first instance shipped.
A second example from a different sub-chain: findings F22 through F26 trace a single
failure-mode sequence through an 8-step verifier pipeline. Each finding surfaces as the direct
consequence of the prior finding's fix: fixing the dispatch layer (F22, step 2–3) unblocks execution
to the install layer (F23, step 4); fixing the install layer unblocks the import layer (F24, step 4);
fixing the import layer unblocks the identity policy layer (F25, step 6); fixing the identity layer
unblocks the surface-extraction layer (F26, step 8). The step numbers are monotonically
non-decreasing: 2–3, 4, 4, 6, 8. This monotonicity is not a coincidence. It is a structural regularity of
how fixes propagate through a sequential pipeline.
This paper asks: are such patterns extractable from audit-chain data, and do they localize future
findings?
1.2 Scope and Claims
This paper makes one claim: audit-chain structure contains extractable regularities that localize
future findings. It does not claim that an LLM conditioned on audit-chain history outperforms an
unconditioned LLM – that is the Phase 2 ablation study, pre-registered in Section 8. It does not
claim that the regularities generalize beyond this corpus – that is the cross-project validation using
the two sibling repositories. It does not claim that predictive audit prompting prevents findings –
that raises a self-referential measurement problem discussed in Section 7.3.

2 BACKGROUND AND RELATED WORK
2.1 Defect Prediction in Software Engineering
The use of historical data to predict future software defects has a 20-year research history. Hassan
and Holt (2005) demonstrated that code-change history predicts defect locations. The PROMISE
dataset (Menzies et al. 2007) established shared corpora for defect-prediction studies. Recent
SZZ-based approaches (Rosa et al. 2021) link bug-fixing commits to bug-introducing commits.
Kamei et al. (2013) introduced just-in-time defect prediction at the commit level.
All of these approaches operate on code metrics: churn, complexity, coupling, developer
experience, file age. The predictor variables are properties of the code artifact. Our approach
operates one meta-level up: the predictor variables are properties of the audit chain, not of the
code. We predict audit findings from audit-chain structure, not from code structure.

2

Structural Regularities in AI-Assisted Audit Chains

Arfeen · Pilot Study

The distinction matters because audit-chain regularities capture process dynamics –
failure-mode shift across releases, step progression through a multi-stage verifier, cross-language
seam recurrence – that code metrics do not encode. A file's cyclomatic complexity does not change
when the audit round number increments; the audit chain's step-coverage vector does.
2.2 Process Mining
Process mining (van der Aalst 2016) discovers process models from event logs. Our structured
audit-chain log is an event log: each row is an event (a finding), with a timestamp (round number),
an activity (the substrate layer), and a case (the failure-mode chain). Association-rule mining
(Agrawal and Srikant 1994) discovers co-occurrence patterns in transactional data. Our regularities
(R1–R11) are association rules extracted manually from a small corpus; the registered report
(Section 8) will apply algorithmic mining via R's arules package to the full normalized corpus.
2.3 AI-Assisted Code Audit
The Bayyinah Audit Framework (Arfeen 2026a) is, to our knowledge, the first published
methodology for auditing AI-generated code using multiple AI instances in distinct roles. The
framework's validator-by-different-instance protocol uses a fresh AI instance with no access to the
producing instance's conversation to review artifacts independently. The framework has been
applied across 43 documented rounds on three repositories under framework versions 1 through 4
(v1–v3 published; v4 private operational edition). The complete audit chain has monotonically
increasing round numbers, a four-level severity rubric (CRITICAL, HIGH, MEDIUM, LOW),
reproducers for each finding, and closure ledgers documenting the response at each round
transition.
2.4 Coding-Theoretic Framing
Each prediction in this study is a fixed-length codeword over five dimensions (P1–P5). The
validator-by-different-instance protocol can be read as a (3,1) repetition code: the same audit
artifact is checked by independent instances, and agreement is required for closure. The
five-dimension scoring vector is a Hamming-distance comparison between the predicted
codeword and the ground-truth codeword: distance zero means 5/5 HIT, distance one means 4/5,
and so on. This framing is interpretive, not generative – it does not produce predictions, it
organizes how we score and weight them. Section 6.5 presents the Hamming-distance summary
alongside the per-dimension breakdown.

3 THE AUDIT-CHAIN CORPUS
3.1 Corpus Overview
The full corpus comprises 43 documented rounds across three repositories. Two parallel
numbering systems exist, reflecting different scoping conventions adopted at different project
phases:
Counter A (global, framework-mandated). Rounds 1–37, monotonically numbered. Rounds 1–22
span three sibling repositories (furqan-lint, Furqan language, Bayyinah Integrity Scanner) during
initial development (May 2–3, 2026) under Framework v1–v3. Rounds 23–37 span furqan-lint v0.8.5
through v0.9.4 (441 tests at checkpoint, four primary substrates: Python, Rust, Go, ONNX) under
Framework v3.

3

Structural Regularities in AI-Assisted Audit Chains

Arfeen · Pilot Study

Counter B (phase-scoped). Rounds 28–33, scoped to a corrective-ship sequence within the Gate 11
Sigstore-CASM verifier pipeline (furqan-lint v0.11.1 through v0.11.6, 452 tests at v0.11.0). Counter B
maps to global Counter A rounds approximately 38–43. Counter B uses its own finding-ID
namespace (F1–F26).
Table 1. Corpus structure across counters.
Counter

Rounds

Repositories

Substrate

Framework

A (global)

1–37

3 (furqan-lint, Furqan, Bayyinah Scanner)

441 tests at v0.9.4

v1–v3

B (phase)

28–33

furqan-lint (Gate 11)

452 tests at v0.11.0

v3–v4

Combined

~43

3

–

v1–v4

3.2 Finding Inventory
The corpus contains an estimated 50–80 distinct findings across all 43 rounds. The estimation
reflects two documentation conventions:
In Counter A, findings are classified under the C/H/M/L severity scheme without sequential IDs.
A single round (the v0.10.0 audit, round ~38) contains 17 findings: 1 CRITICAL, 6 HIGH, 7
MEDIUM, 3 LOW. Earlier rounds contain 5–12 findings per round in recommendation form
(labeled Rec-1 through Rec-12 in the original memos; the Rec-prefix is used here to avoid collision
with the regularity codes R1–R11 introduced in Section 4).
In Counter B, findings carry sequential IDs (F1–F26) with full structured documentation. Of
these, five (F22–F26) have complete six-element documentation suitable for the predictive-analysis
schema.
The gap between 5 fully structured findings and ~50–80 total findings is a normalization effort,
not a data-collection effort. The pre-round-28 findings exist in audit memos and require 2–3 hours
per round to transcribe to the 18-column schema. This normalization yields the 50–80 finding
target for the registered report without requiring any new audit rounds.
3.3 The Pilot Sub-Chain (F22–F26)
The pilot uses the five-finding chain from the Gate 11 Sigstore-CASM verifier pipeline. Selection
criteria: (1) single failure-mode sequence with unambiguous causal chain, (2) complete
six-element structured documentation with ground-truth closure proofs, (3) multi-stage pipeline
providing a natural categorical target variable.
Table 2. Pilot sub-chain F22–F26.
ID

Rd

Stp

Error Code

Substrate Layer

Scope

Fix

Location

F22

29

2–3

CASM-V-001

verifier_dispatch

whitelist_alignme
nt

21 LOC Py

verification.py

F23

30

4

CASM-V-021

ci_install_matrix

extras_gap

1 LOC
YAML

ci.yml

F24

31

4

CASM-V-021

sigstore_api_drift

api_path_drift

3 LOC Py

verification.py

F25

32

6

CASM-V-032

policy_construction

literal_vs_regex

1 LOC
YAML

ci.yml

F26

33

8

SyntaxError

extractor_dispatch

wrong_lang_dispa
tch

~30 LOC
Py

surface_extraction.p
y

4

Structural Regularities in AI-Assisted Audit Chains

Arfeen · Pilot Study

The verifier pipeline has 8 steps. Findings progress through steps 2–3, 4, 4, 6, 8 – non-contiguous
but monotonically non-decreasing. Steps 5 (bytes-IO) and 7 (signature verification) are not visited.
3.4 Dataset Availability
The structured log (audit_chain_log_F22_F26.csv, 5 rows, 18 columns) is published on Zenodo.
Experiment protocol, committed predictions, and scoring documents are supplementary
materials. The full 43-round corpus will be normalized and released with the registered report.

4 STRUCTURAL REGULARITIES (R1–R11)
Eleven regularities extracted by manual inspection of the F22–F26 chain and audit memos from
rounds 29–33. Each is a propositional rule testable against future findings.
4.1 Failure-Mode Dynamics
R1 (Failure-mode shift). Closing a finding at layer L surfaces the next finding at structurally
adjacent layer L'. Adjacency follows pipeline step order. Each fix unblocks execution to the next
step where the next latent failure becomes observable.
R2 (Step monotonicity). Step numbers are monotonically non-decreasing within a single
failure-mode chain: 2–3, 4, 4, 6, 8. No finding regresses to a previously-passed step. A consequence
of R1: each fix advances the execution frontier.
R3 (Error-code locality). Consecutive findings at the same step share error-code prefixes. F23 and
F24, both at step 4, share CASM-V-021. Step change implies code change.
4.2 Substrate Properties
R4 (Fix-size bimodality). Fixes cluster at small (1–3 LOC, CI YAML configuration) or medium
(20–30 LOC, Python dispatch tables). No large fixes (100+ LOC). Corrective-ship discipline
constrains size.
R5 (External-library persistence). Three of five findings involve sigstore-python semantics. A
rapidly evolving external dependency is a persistent finding source.
R6 (Step exhaustion). Two consecutive findings at step 4 (F23, F24) preceded a jump to step 6
(F25). Double-occupancy at a step exhausts its finding surface; the predictor should look ahead.
4.3 Cross-Cutting Patterns
R7 (Step-coverage tracking). After F22–F25, visited steps are {2–3, 4, 6}; unvisited are {1, 5, 7, 8}.
Unvisited steps narrow the prediction space. Steps 1, 5, 7 are structurally less likely to fail
(initialization, bytes-IO, signature verification). Step 8 (surface extraction, language-dependent
parsing) is the next substantive step.
R8 (CI-vs-substrate alternation). Findings alternate between CI YAML (F23, F25) and Python code
(F22, F24, F26). The smoke-test workflow is itself a finding surface.
R9 (File locality). When a Python file implements step-specific logic, findings at that step localize
to that file. F22 to verification.py (step 2–3). F24 to verification.py (step 4). F26 to
surface_extraction.py (step 8).
R10 (Severity bounding). All five findings are LOW/LOW-MEDIUM. Corrective-ship discipline
(one finding per release) constrains severity.

5

Structural Regularities in AI-Assisted Audit Chains

Arfeen · Pilot Study

R11 (Cross-language seam recurrence). F22: Rust module through Python-only verifier. F26:
ast.parse applied to Rust source. The cross-language seam – language-agnostic interface with
language-specific implementation – recurs at every layer where the abstraction exists.

5 EXPERIMENT DESIGN
5.1 Protocol
Retrospective predict-then-reveal on the pilot sub-chain:
(1) Input: structured log for F22 through F(N-1). (2) Predict: commit predictions on 5 dimensions
before ground-truth is read. (3) Score: compare predictions to ground truth per dimension. (4)
Threshold: TIGHT if at least 3/5 dimensions HIT (pre-registered).
Two tests: Test 1 predicts F25 from F22–F24. Test 2 predicts F26 from F22–F25.
5.2 Scoring Dimensions
Table 3. Scoring dimensions and random baselines.
Dim

Name

Classes

Random Baseline

P1

Failing step

8

12.5%

P2

Error code

Open set

–

P3

Substrate layer

Open set

–

P4

Fix-size class

4

25%

P5

Root cause (mechanism)

Free text

–

P4's four-class granularity and P5's mechanism-presence scoring are acknowledged as generous
(Section 7.4). The Hamming-distance framing in Section 2.4 lets us treat the 5-tuple (P1, P2, P3, P4,
P5) as a single codeword and report distance d in {0, 1, …, 5}, with d = 0 corresponding to a 5/5 HIT.
More formally, the five-dimension prediction is a fixed-length codeword (P1, P2, P3, P4, P5) where
each dimension is a symbol drawn from its respective alphabet. The Hamming distance d between
the predicted codeword and the ground-truth codeword is the number of mismatching
dimensions, so d = 0 corresponds to 5/5 HIT. This framing makes alphabet asymmetry explicit: P4
has alphabet size 4 (random Pr[d_P4 = 0] = 0.25), P1 has alphabet size 8 (random Pr[d_P1 = 0] =
0.125), while P2, P3, and P5 are open alphabets where random agreement is much rarer. A
dimension-weighted analysis would weight hits on open-alphabet dimensions more heavily than
hits on small-alphabet dimensions; we defer this weighted scheme to the Phase 2 registered report
(Section 8) so that the pilot hit-rate is reported on the simplest, most generous metric.
5.3 Predictor and Contamination
The predictor was the same Claude instance (Anthropic Claude Opus 4) participating in the audit
chain. Predictions were committed before scoring documents were read, but the predictor's
context included audit memos describing the findings. This shared context is the primary
limitation; the Phase 2 ablation (Section 8) isolates the chain's independent contribution.
5.4 Positionality and Disclosure
The author is the sole human practitioner who produced the audit chain, developed the framework
(Arfeen 2026a), built the tools (furqan-lint; Arfeen 2026c), and directed the AI collaborators

6

Structural Regularities in AI-Assisted Audit Chains

Arfeen · Pilot Study

(Claude, Perplexity, Grok) throughout the 43-round chain. The methodology co-developer, Fraz
Ashraf, contributed engineering-discipline practices to the framework design but did not
participate in the specific rounds (29–33) from which the pilot sub-chain F22–F26 is drawn. This is
a self-study design: the researcher is studying their own process. We acknowledge two
consequences. First, the researcher's familiarity with the corpus may inflate regularity extraction
beyond what an independent analyst would observe. Second, predictor and corpus producer are
the same agent at the meta level even when LLM instances differ. The Phase 2 registered report
(Section 8) addresses both consequences by requiring a different LLM vendor with no shared
context, and by pre-registering the regularity definitions before any new predictions are made. The
framework's structural-honesty discipline (Arfeen 2026a) requires this disclosure as a load-bearing
precondition for any claim made from self-produced data.

6 RESULTS
6.1 Test 1: Predict F25 from F22–F24
Table 4. Test 1 per-dimension results.
Dim Predicted

Actual

Score Attribution

P1

step 6

step_6_identity

HIT

R2 (monotonicity), R6
(exhaustion)

P2

CASM-V-032 or -035

CASM-V-032

HIT

R3 (code locality)

P3

policy_construction

policy_construction

HIT

R5 (sigstore substrate)

P4

one_word or
few_lines

1 LOC YAML

HIT

R4 (bimodality)

P5

literal vs regex
mismatch

regex method when
literal expected

HIT

R5 + LLM prior (ambiguous)

Test 1: 5/5 HIT. TIGHT. Hamming distance d = 0.
R2 and R6 localized the step (step 4 exhausted after double-occupancy; next substantive step is 6).
R3 localized the error-code prefix. R5 localized the layer. P5's literal-vs-regex prediction is the
dimension where LLM priors on ambient-OIDC failure modes may contribute independently of the
chain. The honest interim verdict: the chain contributes to localization (P1, P2, P3) but cannot be
definitively credited with the specific root-cause mechanism (P5) without the cross-instance
ablation.
6.2 Test 2: Predict F26 from F22–F25
Table 5. Test 2 per-dimension results.
Dim Predicted

Actual

Score Attribution

P1

step 8

step_8_surface

HIT

R2 (monotonicity), R7
(coverage)

P2

SyntaxError from
ast.parse

unhandled SyntaxError

HIT

R11 (cross-language seam)

P3

extractor_dispatch

extractor_dispatch

HIT

R11, R9 (file locality)

P4

~30 LOC dispatch table

~30 LOC dispatch table

HIT

R4 (bimodality)

7

Structural Regularities in AI-Assisted Audit Chains

Arfeen · Pilot Study

Dim Predicted

Actual

Score Attribution

P5

dispatches all to
ast.parse, no routing

HIT

dispatches all files to
ast.parse without routing

R11 (cross-language)

Test 2: 5/5 HIT. TIGHT. Hamming distance d = 0.
Test 2 is the stronger result. R7 localizes the step (unvisited set {1, 5, 7, 8}; step 8 is the next with
substantive language-dependent logic). R11 localizes the mechanism (cross-language seam:
ast.parse applied to Rust source). Cold-start analysis: without the chain, a predictor would not
localize to step 8, would not predict ast.parse as the mechanism, and would not name the dispatch
gap. The chain does the load-bearing work for P1, P2, P3, P5 in Test 2.
6.3 Combined Results
Table 6. Combined results across tests.
P1

P2

P3

P4

P5

Verdict

Test 1 (F25 from F22–24)

HIT

HIT

HIT

HIT

HIT

TIGHT

Test 2 (F26 from F22–25)

HIT

HIT

HIT

HIT

HIT

TIGHT

Combined

2/2

2/2

2/2

2/2

2/2

10/10

6.4 Regularity Attribution
Table 7. Which regularities drive which dimensions.
Regularity

Dimensions Driven

Tests

R2 (step monotonicity)

P1

T1, T2

R3 (error-code locality)

P2

T1

R4 (fix-size bimodality)

P4

T1, T2

R5 (external-library persistence)

P3, P5 (partial)

T1

R6 (step exhaustion)

P1

T1

R7 (step-coverage tracking)

P1

T2

R9 (file locality)

P3

T2

R11 (cross-language seam)

P2, P3, P5

T2

LLM prior (non-chain)

P5 (partial)

T1

R2 and R11 are the most broadly predictive. R4 benefits from coarse granularity. The chain's
contribution is ambiguous only for P5 in Test 1.
6.5 Hamming-Distance Summary
Treating the 5-tuple (P1, P2, P3, P4, P5) as a codeword of length 5, both tests yield Hamming
distance d = 0 against ground truth. Dimensions P4 and P5 are the dimensions most vulnerable to
coarse-grain inflation (4-class P4, mechanism-presence P5). Under a stricter weighting scheme
that down-weights P4 and P5, the effective per-test score is 3/3 on the discriminating dimensions
(P1, P2, P3), still d = 0. The Hamming framing is therefore robust to the most plausible critique of
the scoring rubric: even if P4 and P5 are excluded, the predictor remains at perfect
Hamming-distance on the remaining dimensions for both tests. We treat this as suggestive rather

8

Structural Regularities in AI-Assisted Audit Chains

Arfeen · Pilot Study

than confirmatory until Phase 2 reduces same-instance contamination.

7 DISCUSSION
7.1 Nature of the Regularities
R1–R11 are empirical laws of this specific audit chain. They describe how findings in a multi-stage
verifier pipeline relate to each other under the Bayyinah Audit Framework. They are not universal
laws of software auditing. Whether they transfer to other methodologies, substrates, or tool chains
is an open question addressed in the registered report's cross-project validation.
The regularities are independently verifiable. Any researcher with the published dataset can
confirm step monotonicity (R2), error-code locality (R3), fix-size bimodality (R4), cross-language
seam recurrence (R11), and the other properties. The regularities are properties of the data, not of
the predictor.
7.2 Relationship to Defect Prediction
Classical defect prediction uses code-level metrics (churn, complexity, coupling) to predict
defect-prone modules (Hassan and Holt 2005; Menzies et al. 2007; Kamei et al. 2013). Our approach
uses audit-chain-level metrics to predict the next audit finding. The two are complementary: code
metrics predict where bugs live (spatial); audit-chain metrics predict what the next finding will be
(temporal).
The meta-level distinction has a methodological consequence. Code metrics are static at a point
in time. Audit-chain metrics are dynamic across time. This dynamic character enables temporal
prediction.
7.3 The Self-Referential Problem
If predictive prompting pre-empts findings operationally, the predicted finding classes stop
appearing. The training data for those classes dries up. The loss optimizes to zero in a way that
hides whether the optimization was correct. The standard solution (hold out a non-intervention
control) conflicts with the framework's discipline that every ship is a real ship. We note this as a
constraint on Phase 3 deployment and defer it.
7.4 Limitations
Small sample (N = 5). The pilot generates R1–R11 in propositional form but cannot validate them
statistically. Association-rule mining requires N of at least 50, achievable through corpus
normalization (Section 3.2) without new audit rounds.
Same-instance predictor. The predictor shared context with audit memos. The Phase 2 ablation
uses a different vendor with no shared context.
Coarse scoring. P4 has 4 classes (25% random baseline). P5 scores mechanism presence without
requiring alternative exclusion. A stricter protocol would produce lower hit rates. The
Hamming-distance summary in Section 6.5 partially mitigates this critique by reporting d = 0 even
after P4 and P5 are dropped.
Single failure-mode chain. F22–F26 are causally linked. Whether R1–R11 transfer to independent
findings is tested in the registered report.

9

Structural Regularities in AI-Assisted Audit Chains

Arfeen · Pilot Study

No cross-project validation. All findings from furqan-lint. The Bayyinah Scanner and Furqan
language chains (Counter A rounds 1–22) test cross-project transfer. Deferred to the registered
report.
Compressed timeline. The entire 43-round audit corpus, three repositories, 452 tests, and the
supporting publications were produced in a six-to-seven day window (May 2–8, 2026) by a single
practitioner directing AI collaborators. This compression raises the question of whether
regularities observed in a rapid-development context transfer to longer-lived projects with slower
release cadences. The Phase 2 registered report's cross-project corpus (Counter A rounds 1–22
across furqan-lint, the Furqan language, and the Bayyinah Scanner) partially addresses this by
spanning repositories with different release cadences. A fully independent replication on a
multi-month audit chain from an unrelated project would strengthen the generalizability claim
further; we flag this as the primary external-validity threat.

8 PHASE 2 PRE-REGISTRATION
8.1 Corpus Expansion
Normalize Counter A rounds 1–37 and Counter B rounds 28–33 to the 18-column schema.
Estimated
yield:
50–80
findings
across
three
repositories.
The
existing
validator-by-different-instance practice (Counter A audit-2 and audit-3 are both v0.9.4 audits by
different instances) provides a native cross-instance data point.
8.2 Ablation Design
Condition A (chain-conditioned). Fresh LLM instance (different vendor) receives structured CSV
for F1 through F(N-1), predicts F(N).
Condition B (unconditioned). Same LLM receives repository skeleton only (file names, signatures,
test names), no audit-chain log, predicts next finding.
Hypothesis. Condition A achieves higher hit rate than Condition B, equivalently lower mean
Hamming distance over the test set.
Analysis. McNemar's test on paired nominal scores. Association-rule mining (R arules).
Severity-slope control charts. Reproducible from a single R Quarto document.
Pre-registration. OSF, before predictions are made.

9 CONCLUSION
Audit chains produced under structured methodologies contain regularities that localize future
findings. We extracted eleven such regularities from a five-finding pilot chain in the furqan-lint
Sigstore-CASM verifier pipeline. A retrospective prediction experiment achieved 10/10 hits on two
held-out findings across five dimensions – Hamming distance d = 0 – with caveats about predictor
contamination, scoring granularity, and the absence of a cross-instance ablation.
The contribution is the regularities, not the hit rate. R1–R11 are properties of the corpus,
independently verifiable from the published dataset, and testable on future audit chains. The
practical implication: audit prompts can be conditioned on chain history to anticipate predictable
findings. The methodological implication: audit-chain data is a predictor-variable class distinct
from code metrics, operating one meta-level above the code and encoding process dynamics that

10

Structural Regularities in AI-Assisted Audit Chains

Arfeen · Pilot Study

code-level analysis does not capture.
The dataset, experiment protocol, committed predictions, and scoring documents are available
on Zenodo.

ACKNOWLEDGMENTS
Fraz Ashraf co-developed the Bayyinah Audit Framework's engineering-discipline components
(root-cause analysis, lifecycle management, mughlaq-trap detection) that govern the audit chain
studied here. The experiment design benefited from editorial review by a Perplexity instance that
identified three methodological weaknesses prior to execution: small-sample framing, the
requirement for a cross-instance ablation control, and a self-referential failure mode in the
originally proposed Phase 3 deployment study. The audit chain was produced using Claude
(Anthropic), Perplexity, and Grok (xAI) as AI collaborators in distinct roles — producer, validator,
and calibrator respectively. No external funding was received. All errors and interpretations
remain the author's responsibility.

REFERENCES
Agrawal, R. and Srikant, R. (1994). Fast algorithms for mining association rules. Proc. VLDB, pp. 487–499.
Arfeen, B.S. (2026a). Bayyinah Audit Framework v3.0. Zenodo. DOI: 10.5281/zenodo.20017335.
Arfeen, B.S. (2026b). Bayyinah Audit Framework: Application Brief. Zenodo. DOI: 10.5281/zenodo.20031395.
Arfeen, B.S. (2026c). furqan-lint: Structural-honesty checks for Python, Rust, Go, and ONNX [Computer software].
https://pypi.org/project/furqan-lint/.
Nadella, S. (2023, October 24). Quoted in: Microsoft has over a million paying GitHub Copilot users. ZDNET.
https://www.zdnet.com/article/microsoft-has-over-a-million-paying-github-copilot-users-ceo-nadella/.
Hassan, A.E. and Holt, R.C. (2005). The top ten list: Dynamic fault prediction. ICSM, pp. 263–272.
Kamei, Y. et al. (2013). A large-scale empirical study of just-in-time quality assurance. IEEE TSE, 39(6), pp.
757–773.
Menzies, T., Greenwald, J., and Frank, A. (2007). Data mining static code attributes to learn defect predictors.
IEEE TSE, 33(1), pp. 2–13.
Rosa, G., Pascarella, L., Scalabrino, S., Tufano, R., Bavota, G., Lanza, M., and Oliveto, R. (2021). Evaluating
SZZ implementations through a developer-informed oracle. Proc. 43rd Int. Conf. on Software Engineering
(ICSE), pp. 436–447.
van der Aalst, W.M.P. (2016). Process Mining: Data Science in Action. Springer.

APPENDIX A DATASET SCHEMA (18 COLUMNS)
The published CSV (audit_chain_log_F22_F26.csv) contains the columns below. Types: str =
free-text string, enum = controlled vocabulary, int = integer, ts = ISO-8601 timestamp.
Table A1. Dataset schema for the audit-chain log.
#

Column

Type

Description

1

finding_id

str

Stable identifier (e.g. F22).

2

counter

enum

Audit counter: A (global) or B (phase).

3

global_round

int

Round index across the full corpus.

11

Structural Regularities in AI-Assisted Audit Chains

Arfeen · Pilot Study

#

Column

Type

Description

4

phase_round

int

Round index within the current phase.

5

timestamp

ts

Closure timestamp (ISO-8601, UTC).

6

repository

str

Repository slug (e.g. furqan-lint).

7

version

str

Semver tag at closure.

8

step

int

Pipeline step number where the failure surfaced.

9

error_code

str

Canonical error code (e.g. CASM-V-032).

10

substrate_layer

str

Substrate layer where the defect lives.

11

scope_class

str

Scope categorization (e.g. literal_vs_regex).

12

severity

enum

CRITICAL, HIGH, MEDIUM, LOW, ADVISORY.

13

fix_size_loc

int

Lines-of-code in the closure patch.

14

fix_size_class

enum

one_word, few_lines, table, refactor.

15

fix_location

str

File or files modified by the patch.

16

root_cause

str

Mechanism statement (free text).

17

closure_shape

str

Patch shape: substrate, CI, schema, etc.

18

regularities

str

Pipe-separated list of attributed regularities.

APPENDIX B REGULARITIES REFERENCE
Code

Name

Proposition

R1

Failure-mode shift

Closing layer L surfaces adjacent L'

R2

Step monotonicity

Steps non-decreasing within a chain

R3

Error-code locality

Same step implies same code prefix

R4

Fix-size bimodality

1–3 LOC or 20–30 LOC clusters

R5

External-library persistence

Evolving deps are persistent sources

R6

Step exhaustion

Double-occupancy predicts step change

R7

Step-coverage tracking

Unvisited steps narrow prediction space

R8

CI-vs-substrate alternation

Findings alternate CI YAML and code

R9

File locality

Step-specific files localize findings

R10

Severity bounding

Corrective discipline bounds severity

R11

Cross-language seam

Language-agnostic names, language-specific impls recur

APPENDIX C SUPPLEMENTARY MATERIALS
Available on Zenodo: experiment_protocol.md, test1_F25_predictions.md, test1_F25_scoring.md,
test2_F26_predictions.md,
test2_F26_scoring.md,
corpus_accounting.md,
audit_chain_log_F22_F26.csv.

12



Bismillah ir-Rahman ir-Rahim
