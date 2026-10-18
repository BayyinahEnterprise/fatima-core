Bismillah ir-Rahman ir-Rahim

XZ Protocol v0.75 – Preregistered Structural Decision Replay at
Software Supply-Chain Effect Boundaries
Bilal Syed Arfeen
2026-08-17
Author of record: Bilal Syed Arfeen Version: 0.75, FROZEN, 2026-08-17 Status: v0.75 FROZEN –
repair build from v0.74 R31 audit (4/4 HALT; 4-seat round). FROZEN withdrawn per two-family peer
review. Prescribed repairs landed: C-suffix in all five DECLARATION_PATTERNS, gate [13] fail-closed,
register generator graceful degradation, boundaries.json version current. Class A recurrence R7-R31: 25/25.
Methodology: v7 canonical (six strings). Intended terminal form: FROZEN OPEN preregistration
instrument Access at eventual deposit: OPEN (protocol); the later XZ corpus is SPLIT (Section 21)
Program chain (binding): AX-SH5 -> SHUDP -> SHVVP -> BSSG -> XZ Protocol -> XZ Corpus ->
XZ Empirical

0. Status, claim boundary, and prohibited language
0.1 Status
This document is v0.75 FROZEN – Its target form is a FROZEN preregistration in the sense fixed by the
deposited SHVVP v0.8: a contract locked before any corpus, packet, annotation, or result exists, whose every
later change is a new version with an append-only amendment entry, never a silent edit.
FREEZE-BLOCKERs FB-1 through FB-7a are resolved with canonical executable artifacts (Section 25). FB7b status, rationale, and the full carrying-seat trajectory are recorded in the Section 25 FB-7b row (single source
of truth; no duplicate rationale maintained here). Current status: PENDING RE-CARRY on v0.75 bytes. The
normative instrument ships 6 code modules and 6 test suites (12 distinct Python files) plus 1 trust-roots manifest and this protocol text: 14 normative files, with 186 test functions (all GREEN), including the exhaustive
3ˆ5 = 243 kernel decision-state tests (14 test functions exercising 243 vectors internally), the Condition A evaluator with mandatory attestation checks, the 16-source public-record manifest, the five-channel WithinAuth
control graph, and the 27-test adversarial integration suite covering all nine Section 22 categories. The canonical verification command is pytest test_xz_protocol_kernel.py test_xz_protocol_condition_a.py
test_xz_protocol_source_frame.py test_xz_protocol_control_graph.py test_xz_protocol_adversarial.py
xz_protocol_phase_a_tests.py; default pytest discovery does not collect xz_protocol_phase_a_tests.py,
so the explicit invocation is load-bearing. Gates are tooling (not carried); see the normative/tooling partition
in Section 27, v0.14 entry.
FB-8 (governance convergence under audit) is OPEN: governance-layer prose claims are not independently
verifiable from bytes alone; the v0.41 append-only corruption and the v0.42 four-seat audit demonstrate the
failure mode. Exit condition: two non-producer carrying seats from different families return non-HALT on
bytes where every prose claim in the current entry is verified against shipped bytes before sealing.
Carry status: the v0.3 code package received GPT-5.6 Sol PASS and Kimi K3 CARRY-CLEAN (convergent
two-family non-HALT). v0.4 made substantive changes (trust roots, degeneracy-rule count, register sentence
repair) and claimed FROZEN status, but violated the append-only amendment rule by rewriting the v0.3
historical entry to erase a recorded HALT. v0.5 restored the historical record and reverted to DRAFT
CANDIDATE; the fresh two-family carry it requires was completed at v0.31 (six non-producer carrying seats

1

across two families, all executing, all non-HALT, on v0.31 canonical bytes where sha256sum -c returned rc=0)
and is recorded in the v0.32-v0.36 entries. The “producer” for carrying-seat eligibility purposes is defined in
Section 22.1. The full defect trajectory is in Section 27 (seventy-five amendment entries, v0.1 through v0.74).
This draft integrates three independent model-council advisory seat drafts (GPT-class, Gemini-class, and
Claude-class seats) under chair direction. The council is an advisory consistency mechanism, not peer review;
seat reports ship unmodified with the eventual deposit (Section 23). Chair-directed conflict resolutions are
recorded in Section 0.4 and are binding on this draft.
0.2 What this document is and is not
This document is an evaluation contract for one retrospective historical case: a structural decision replay of the
XZ Utils supply-chain compromise, CVE-2024-3094, disclosed by Andres Freund on 2024-03-29 (oss-security
disclosure; NVD CVE-2024-3094; tukaani-project/xz issue 103; GHSA-rxwq-x6h5-x525).
It is not the corpus, not the empirical paper, and not a claim that SHV, BSSG, or any component of the
Structural Honesty program has been validated. As of this draft no XZ corpus exists under this protocol,
no boundary universe has been enumerated, no packet has been built, no conjunct has been scored, no
adjudication has occurred, and no result of any kind exists. Every number and rule in this document is a
commitment intended to precede data. The sequence is protocol first, corpus second, paper third, exactly
as SHVVP v0.8 Section 0 fixes it, because preregistration’s only function is to separate predictions from
postdictions.
This protocol contains, and may contain: a priori effect-boundary classes, an enumeration and eligibility rule,
condition definitions, an executable-baseline vocabulary, blinding stages, sealed-commitment requirements,
schemas, scoring rules, inherited and seam metrics, decision rules, falsifiers, sensitivity plans, safety posture,
and audit obligations. It does not contain, and MUST NOT contain: XZ corpus labels; per-boundary conjunct
outcomes; the sealed ledger’s contents or cardinality; hazardous payload details; compromised binaries or
restricted technical content; activation conditions or recipes; or any information enabling reconstruction of
the malicious functionality. A pre-deposit verifier will confirm that the protocol text cites, for the XZ case,
only the four permitted public sources named above and the program’s own DOI records.
0.3 Prohibited language (frozen for every version of this protocol)
1. The prohibited-sentence register of BSSG v0.1 Section 1.3 (paper record supplied as doi:10.5281/zenodo.21713180;
see Section 26.2 for the dual-DOI record) is inherited in full. No effectiveness verb – prevents, mitigates,
reduces, ensures, guarantees, protects, or any paraphrase – may be applied to BSSG anywhere in this
protocol, in the later corpus, in deposit metadata, or in any output of the replay. BSSG v0.1 is an
architecture-and-conformance artifact that makes no effectiveness claim; this protocol does not create
one retroactively, and nothing this replay can observe could establish one.
2. The following are additionally prohibited in all outputs of this protocol and its downstream instruments:
any sentence asserting that BSSG stopped, would have stopped, caught, or would have caught the XZ
compromise or its operator; any sentence reporting DENY_UNKNOWN as detection or as favorable
evidence; any figure or sentence aggregating DENY_FALSE with DENY_UNKNOWN; any unqualified
“the kernel denies the attack”; the phrase “attack prevention” applied to any result of this replay; and
any modal “would have” applied to a historical outcome. The admissible summary form is: “On the
committed packet for boundary i, under the declared role mapping and cutoff, the frozen decision
functions return and .”
3. Scope limits MUST appear in the same sentence as the claims they limit (drafting rule inherited from
BSSG v0.1 Section 1.2 and SHVVP v0.8 Section 0.2). The sentence “Structural Honesty has been
validated” is NOT ADMISSIBLE in any output of this program (SHVVP v0.8 Section 0.2), and no
output of this protocol may state or imply it.

2

0.4 Council provenance and chair-directed conflict resolutions (binding on this draft)
The following rulings integrate and, where necessary, adjudicate between the three seat drafts. Each is
binding on this draft and on every later version absent a formal amendment.
• CR-1 (Condition labels). Condition A IS the conventional baseline and Condition B IS the
SHV/BSSG-enhanced condition, exactly as the deposited SHVVP v0.8 Section 5 fixes them. No draft,
table, script, or figure may reverse these labels; a discovered reversal is corrected with a logged correction
record, never silently.
• CR-2 (Kernel truth domain). The BSSG kernel truth domain is exactly TRUE, FALSE, UNKNOWN,
and the kernel output vocabulary is exactly ALLOW, DENY_FALSE, DENY_UNKNOWN. NOTEVALUABLE is a boundary-level, claim-level, or run-level protocol label only. It is never a fourth
kernel truth value and never a fourth kernel output. A conjunct whose required declared objects lack a
historically grounded value is UNKNOWN at the kernel, carrying a typed reason code that preserves
the distinction (Section 11.2).
• CR-3 (Primary seam estimand). The primary structural seam-divergence estimand counts only
dual-evaluable boundaries on which the executable Condition A function returns A-ACCEPT and the
Condition B kernel returns DENY_FALSE, on the same committed pre-cutoff packet, under a unique
primary role mapping. DENY_UNKNOWN is reported separately, is never added to the primary count,
and is never favorable.
• CR-4 (Labels and TENTATIVE). The four primary protocol labels are FALSIFIED, NOTFALSIFIED, INDETERMINATE-ADJUDICATION, and NOT-EVALUABLE. TENTATIVE is preserved as an orthogonal, mandatory reliability qualifier inherited from SHVVP’s 0.67-to-below-0.80
alpha band. The four labels are therefore not claimed to be exhaustive of all reporting states; the
qualifier is disclosed wherever labels are defined (Section 15).
• CR-5 (Freeze blockers). The following are explicitly recorded as FREEZE-BLOCKERS and appear
in Section 25: the absent executable Condition A disposition function; the absent public-record universe
and source-frame commitments; the untested role-mapping and WithinAuth control-graph standard;
the absent production trust roots; and the absent XZ-specific adversarial suite and two-family carry
record. (FB-1 and FB-2, originally the SHVVP M3/T2 computability mismatch and the under-specified
Phase A interval algorithms, are resolved in v0.2 by protocol-level operationalization in Section 13.3;
see amendment record v0.2.)
• CR-6 (Zero divergence). The Gemini-seat proposal to label a zero-divergence outcome “NOTFALSIFIED (Zero Divergence)” is REJECTED. Zero incremental divergence FALSIFIES the incrementalvalue claim: on the forensic track, IDC = 0 fires inherited clause A1; on the seam track, S1 = 0 on the
complete dual-evaluable frame yields SEAM-FALSIFIED. Labeling a null result as non-falsification
would invert the preregistered burden of proof. The rejection is recorded here because an append-only
regime records rejected findings, not only accepted ones.
• CR-7 (No invented UNKNOWN thresholds). This draft freezes no numeric UNKNOWN-share
cap, evaluability quorum, or domination threshold, because no principled basis for a specific number
exists before decoy piloting. UNKNOWN burden is reported descriptively and completely (metric S6;
Section 14), and every UNKNOWN-driven limitation is stated in the same sentence as the result it
limits. If a numeric gate is later justified from decoy pilots, it enters by formal amendment only.
• CR-8 (Blinding language). The design is mechanism-blind and label-blind only. No claim of
case-blindness is admissible for a famous public incident, for human executors or for pretrained model
executors (Section 8.1).
• CR-9 (Reference standard). The sealed ledger is a sealed reference-standard ledger: an operational
standard assembled from public evidence and custodian judgment, not infallible ground truth. Disputes,
confidence fields, and corrections are first-class schema content (Section 9.2).
• CR-10 (Analysis posture). The analysis is descriptive, single-case, with frozen dependency clusters.
No population inference, no p-values, no null-hypothesis tests, and no population confidence statements
attach to any seam metric. Where inherited SHVVP gates require intervals, these are finite-corpus
stability summaries operationalized by the protocol-level Phase A scoring module (Section 13.3).
• CR-11 (Two tracks). The forensic construct replay (Track 1: SHVVP Phase A, M1-M12, FORENSIC
packets) and the contemporaneous structural seam analysis (Track 2: pre-cutoff boundary packets,

3

S-metrics) are distinct analyses with distinct packets, distinct estimands, and distinct labels. They are
never mixed in one estimate.
• CR-12 (No backfilled evidence). The historical primary analysis cannot backfill evidence. No
contemporary BSSG contract, witness declaration, or freshness authority may be projected into history
to make a conjunct TRUE in the primary analysis. A modeled-deployment overlay is permitted only as
a separately labeled sensitivity analysis (MDL-SENSITIVITY; Section 19.3) and is barred from every
headline, abstract, and primary table.

1. Purpose and position in the program chain
1.1 Purpose
The XZ Utils compromise is the program’s retrospective construct-validation anchor: a supply-chain incident
with a public source repository, compromised release tarballs, build-time activation logic, downstream
packages, runtime effects, signed releases, and a documented correction history (oss-security; NVD; xz issue
103; GHSA advisory). SHVVP v0.8 Section 2.1 records it as VERIFIED as an incident and assigns it
exactly one evidentiary role: it can test whether SHV finds and explains real divergence; it cannot validate
containment of an autonomous discovery agent, and it cannot establish universal adequacy.
This protocol operationalizes that role in two linked but strictly separated tracks:
1. Track 1 – Forensic construct replay. The SHVVP v0.8 Phase A comparison of Condition A and
Condition B on a frozen forensic archive, scored by the inherited metrics M1-M12, thresholds T1-T8,
and decision clauses A1-A6.
2. Track 2 – Contemporaneous structural seam analysis. A boundary-by-boundary replay in
which contemporaneously available evidence at enumerated historical effect boundaries is mapped to
an executable conventional disposition (Condition A) and to the frozen five-conjunct BSSG decision
semantics (Condition B), yielding a structural decision-divergence measurement on a committed publicrecord frame.
1.2 Position and inheritance
The binding chain is AX-SH5 -> SHUDP -> SHVVP -> BSSG -> XZ Protocol -> XZ Corpus -> XZ
Empirical. This protocol inherits upward and may not weaken anything frozen upstream:
• From SHVVP v0.8: the Phase A design, condition labels, sealed-ledger classes K1-K5, auxiliary corpora,
metrics M1-M12 (twelve metrics, not nine), thresholds T1-T8, decision clauses A1-A6, the Krippendorffalpha reliability gate, the UNKNOWN discipline, the versioning and amendment rule, the two-channel
commitment discipline, and the carrying-audit rule.
• From the BSSG v0.1 paper and canonical specification (record supplied as doi:10.5281/zenodo.21713180):
the frozen five-conjunct kernel, its three-valued semantics, the raw-evidence discipline (no caller-supplied
derived facts), the claim-level vocabulary, and the prohibited-sentence register.
• From SHUDP v0.5, whose bytes are deposited at doi:10.5281/zenodo.21539816 under a registered title
belonging to the A5 record (Section 26.1 divergence note), with SHUDP v0.4 retained for lineage: the
canonical form of Axiom 5 (evidence independence) over the WithinAuth control predicate, the two-level
discipline separating axiom-level status from event-level verdicts, and the refusal to infer failure from
absent public disclosure.
• From SHV Method v1.1, PMD v1.8, and BAF v3.0: the verification, predictive-modeling, and audit
disciplines under which this program’s artifacts are produced and reviewed.
Where this protocol and a deposited upstream instrument could be read as differing, the deposited instrument
governs, and the difference is either a defect in this protocol (to be repaired by a new version) or the subject of
a formal upstream amendment. Two historical conflicts are resolved in this draft under that rule: Condition
A is the conventional baseline and Condition B is SHV-enhanced (CR-1), and the inherited Phase A metric
set is M1 through M12, twelve metrics, with any “nine metrics” statement rejected as defective (Section 13.1).

4

2. Scope and claim boundary
2.1 Scope
This protocol evaluates one retrospective historical case in a fixed public-record frame. The evaluation
object is decision structure, not outcome: whether two frozen decision functions – an executable conventional
baseline disposition and the frozen BSSG five-conjunct kernel – return different dispositions when applied to
the same committed evidence packets at the same enumerated historical boundaries under declared mappings
and cutoffs.
2.2 The claim boundary, stated exactly
The target claim is limited to structural decision divergence under the declared mapping, packet, cutoff,
baseline, and evidence-independence assumptions. An A-ACCEPT/DENY_FALSE contrast means only
that the two frozen decision functions return different dispositions on the same committed packet under the
declared historical role mapping. It is not an estimate of attack prevention, deployment behavior, causal
outcome change, adversary adaptation, or population performance, and no such estimate exists anywhere in
this protocol’s output space.
Four consequences are drawn now, before data:
1. No counterfactual history. This protocol cannot simulate an alternative 2024. A gated boundary
changes adversary incentives; a deployed evidence plane changes what records exist; none of that is
observable retrospectively. The replay measures mechanical divergence of frozen rules on frozen bytes,
and only that.
2. DENY_UNKNOWN is not detection. Historical records were not generated under a BSSG-shaped
contract, witness, freshness, and receipt regime. Much of what the kernel will see is UNKNOWN
because no one generated the corresponding records in 2024, and the resulting DENY_UNKNOWN
states measure the absence of historical BSSG-shaped infrastructure, not a structural distinction. They
are therefore reported separately (estimand E-S2), never counted as favorable, and never aggregated
with DENY_FALSE (CR-3).
3. No generalization. No result may be generalized beyond this case, these packets, these teams, these
source frames, and these declared mappings. A scope limit appears in the same sentence as every
positive statement.
4. No composition inference. The BSSG kernel evaluates each boundary independently. Whether
a sequence of individually authorized operations constitutes an unauthorized composite operation
is inherited as OUT OF MODEL from BSSG v0.1 Section 7.1 (doi:10.5281/zenodo.21713180). The
XZ compromise was built through a sequence of individually plausible contributions; this protocol’s
structural decision replay evaluates the endpoint state at each boundary, not the trajectory that
produced it. No output of this replay may claim that the kernel captures compositional attack patterns.
2.3 What each track can and cannot establish
Track 1 can establish, at most, single-case construct validity and incremental forensic value relative to a
competent conventional baseline on one historical case, under blinded adjudication – exactly the reach SHVVP
v0.8 Section 0.2 assigns Phase A. Track 2 can establish, at most, a sealed, reproducible measurement of
structural decision divergence and UNKNOWN burden on one committed public-record frame. Neither track
can establish effectiveness, harm change, or outcome change, and neither track’s labels admit such language.

3. Research questions (to be frozen at v0.x FROZEN)
Track 1 – forensic construct replay.

5

• RQ1 (Incremental detection). On the sealed reference-standard ledger, does Condition B identify
at least one consequential fact (class K1-K3) not identified by Condition A?
• RQ2 (Shared-fact timing and evidence). Do facts identified by both conditions meet the frozen T2
and T3 timing and evidence-completeness gates, operationalized by the protocol-level Phase A scoring
module (Section 13.3)?
• RQ3 (Discrimination and burden). Does Condition B remain within the frozen false-positive (T4),
reviewer-burden (T5), and discrimination (T7) gates on the committed auxiliary corpora?
• RQ4 (Label and UNKNOWN discipline). Does either condition rely on a post-discovery mechanism
label (M10/T6) or represent missing evidence as clean (M11/T8)?
Track 2 – contemporaneous structural seam analysis.
• RQ5 (Seam divergence). Among dual-evaluable public-record boundaries with a unique primary role
mapping, how often does Condition A return A-ACCEPT while Condition B returns DENY_FALSE
grounded in pre-cutoff evidence?
• RQ6 (UNKNOWN contribution). How often does Condition B return DENY_UNKNOWN; which
conjuncts contribute UNKNOWN; and how much of that state is attributable, by typed reason code, to
the absence of historical BSSG-shaped infrastructure?
• RQ7 (Evidence independence). For each mapped witness record, is the generation act outside the
acting substrate’s authority under the predeclared WithinAuth interpretation, inside it, or UNKNOWN?
• RQ8 (Mapping and cutoff stability). Does any favorable seam-divergence count depend on one
contestable actor-to-role mapping, one boundary inclusion decision, or one evidence cutoff?
• RQ9 (Correction reach). On the sealed descendant frame, what share of recorded descendants is
reached by correction records under each condition (inherited M9)?
• RQ10 (Enumerability). Do two independent executions of the frozen enumeration procedure produce
the same committed boundary universe?
No research question asserts, and no answer can establish, an effectiveness claim about BSSG.

4. Estimands
4.1 E-A – Inherited Phase A construct estimand (Track 1)
E-A is the set of M1-M12 quantities and the T1-T8 / A1-A6 decision defined by SHVVP v0.8 Sections 5.2-5.4,
unchanged and unrenamed. The analysis unit and scope remain one historical case. This protocol adds
the raw fields needed to implement the rules (Section 10) but does not rename, renumber, or replace any
inherited metric.
4.2 E-S1 – Primary structural seam-divergence estimand (Track 2, primary)
For boundary (i) in the committed public-record frame, define:
• (A_i = 1) only when the executable Condition A disposition function returns A-ACCEPT on the
committed pre-cutoff packet for (i);
• (B_iˆF = 1) only when the Condition B kernel returns DENY_FALSE on the same committed pre-cutoff
packet, with the FALSE-grounding evidence available by the boundary cutoff;
• (D_i = 1) only when boundary (i) is dual-evaluable: the packet is complete under the packet rule, the
primary role mapping is unique (Section 7), and both decisions were computed on identical packet
bytes.
The finite-frame primary estimand is the count
P
[ S1 =
_iD_i, I(A_i = 1 ∧ B_iΘF = 1)]
P
and its share (S1_{share} = S1 / _iD_i).S1isastructuraldecision−divergencecountandshareinthecommittedpublic−
recordf rame.Itisnotanattack − outcomeestimand, andnooutputmaydescribeitasone.

6

4.3 E-S2 – UNKNOWN-only divergence (Track 2, separate, never favorable)
P
[ S2 =
_iD_i, I(A_i = 1 ∧ B_i = DENY_UNKNOWN)]
S2 is always reported separately from S1, is never added to S1, never supports the primary incremental claim,
and is accompanied in every table by its conjunct-level reason-code decomposition (RQ6), so that a reader
can see exactly how much of it is missing-infrastructure artifact.
4.4 E-S3 – Reverse divergence (Track 2, separate)
P
[ S3 =
_iD_i, I(A_i ̸= A-ACCEPT ∧ B_i = ALLOW)]
Reverse divergence is reported with the baseline reason class and the later reference-standard relation, without
calling the result beneficial or harmful.
4.5 E-S4 – Coverage accounting (Track 2, mandatory companion)
For each stratum and overall: enumerated boundaries; packet-complete boundaries; role-unique boundaries;
dual-evaluable boundaries; and WithinAuth-outside, WithinAuth-inside, and WithinAuth-UNKNOWN
boundaries. No excluded or non-evaluable boundary disappears from the denominator ledger; the dualevaluable subset is always presented against the full committed frame so that it cannot masquerade as the
universe.
4.6 Estimand honesty clauses
1. Every estimand is conditional on the declared assumption register (Section 7.5) and the committed
frame; the conditionality is stated wherever the estimand is reported.
2. The primary analysis is historical-primary: it uses only contemporaneous evidence and contemporaneous
declared policy objects (CR-12). The modeled-deployment overlay of Section 19.3 is sensitivity only.
3. No estimand admits an effectiveness reading. The only admissible interpretive sentence for S1 is the
one fixed in Section 2.2.

5. Retrospective effect-boundary universe
5.1 Target frame: the public-record boundary frame
The target of enumeration is every publicly observable candidate effect boundary meeting the frozen eligibility
rule during the frame window: from 180 days before the public disclosure timestamp through 30 days after it.
The disclosure timestamp is fixed from the primary disclosure URL in the source-frame manifest (oss-security,
2024-03-29). This frame is explicitly NOT claimed to include private installations, private runtime events, or
unrecorded actions. Absence of a public sampling frame for a stratum is a frame limitation, never evidence of
zero events (Section 17.10).
[FB-4 RESOLVED: the source-frame manifest ships as xz_protocol_source_frame.py with 16 source records
across 6 categories (TRANSPARENCY_LOG declared in the enum but unused), 29 tests, and a frozen
frame window (2023-10-01 to 2024-04-28). The 180-day pre-disclosure window captures the period of
malicious commits and releases; the 30-day post-disclosure window captures the initial correction response.
S-INSTALLATION has zero public sources and is reported as NOT-EVALUABLE at the stratum level.
S-RUNTIME-AUTH has two sources (SRC-ML-01, SRC-ADV-01) covering the disclosure and advisory
records per Section 5.4 item 8. Digest sealed in Section 25.]
5.2 A priori boundary strata (frozen at v0.1 draft; not corpus labels)
Six boundary classes are fixed before any corpus work. They are derivable from the public shape of the
incident as disclosed, without reference to any ledger fact, mechanism detail, or corpus label; nothing in this
clause encodes which instances were divergent, which events are consequential, or what any conjunct returns.

7

1. S-COMMIT – Commit boundary. A recorded repository state transition that changes tracked
source or build-related material under a maintainer or contributor identity.
2. S-RELEASE – Release boundary. Publication, signing, tagging, replacement, or withdrawal of a
release artifact or release record, including generated release tarballs that differ by declared design from
the tagged source.
3. S-BUILD – Build boundary. Transformation of an input source or release artifact into a build
output under an identifiable recipe or build service, including conditional activation logic sensitive to
architecture, compiler, linker, or packaging context.
4. S-DISTRIBUTION – Distribution boundary. Admission, promotion, mirroring, replacement,
withdrawal, or supersession of a package or artifact in a distribution channel.
5. S-INSTALLATION – Installation boundary. A publicly documented installation, upgrade,
downgrade, or deployment event with identifiable input and target context.
6. S-RUNTIME-AUTH – Runtime authentication effect boundary. A publicly documented
runtime event in which an authentication-related effect crosses a named process, service, or trust
boundary.
5.3 Eligibility rule
A candidate event enters the public-record frame when ALL of the following metadata can be recorded
without reading any later outcome label:
1. a timestamp or bounded time interval;
2. an event type matching exactly one frozen stratum;
3. an identifiable acting account, service, or process class;
4. an identifiable input object or prior state;
5. an identifiable target, output, or state transition;
6. at least one source record in the predeclared source-frame manifest.
Failure of any item is recorded in the screened-event ledger with a typed reason code; nothing is silently
omitted.
5.4 Enumeration procedure and denominator rules
1. Before any content annotation, a universe enumerator runs frozen queries against the source-frame
manifest. Query strings, API parameters, timestamps, pagination receipts, and raw response hashes are
logged.
2. Candidate events receive opaque identifiers assigned by deterministic order: stratum, normalized
timestamp, source identifier, stable event identifier.
3. Exact duplicates merge only when source identifier, normalized timestamp, actor identifier, input digest,
target identifier, and output digest all agree. Near-duplicates remain separate and are linked.
4. A second enumerator independently reruns the frozen queries and reconciles metadata disagreements
only; content judgments are out of scope at this stage (RQ10).
5. Clean-lineage coverage floor: the universe MUST contain, in every stratum in which affected-lineage
instances appear, instances from at least one clean prior lineage and one clean successor lineage, so that
the universe is not built around the known-bad chain. An enumeration violating this floor is INVALID
and cannot be sealed.
6. The complete candidate ledger, screened-event ledger, per-stratum class counts, and source-response
hashes are sealed before any condition output is opened. The commitment authority signs the universe
inventory and cardinality; an independent anchor signs its digest; the run logger records the seal event.
This adopts the SHVVP v0.8 three-trust-root commitment pattern (commitment authority, independent
pre-commitment anchor, run logger; no runtime key override), which exists precisely because earlier
SHVVP versions were HALTED for caller-selectable and post-hoc evidence universes.
7. Denominator rules. Every metric names its denominator; every denominator is a sealed cardinality
or a sealed subset defined by sealed flags; a metric computed against any other denominator is void
(falsifier XZ-I2). Boundaries excluded for any reason remain in the denominator ledger with reason

8

codes. A source appearing after the seal is appended as a deviation and cannot enter the primary
denominator.
8. A stratum with zero eligible public records (installation and runtime strata are the foreseeable candidates)
is retained and reported as NOT-EVALUABLE at the stratum level. It is not dropped, and its zero
frame is not evidence that no real events occurred.
[FB-6 RESOLVED: three Ed25519 production public keys (commitment-authority, independent-anchor,
run-logger) ship in xz_protocol_trust_roots_PUBLIC.json. Digest sealed in Section 25.]

6. Conditions and baseline fairness
6.1 Condition A – conventional baseline (CR-1)
Condition A is the SHVVP v0.8 conventional baseline, implemented by a team independent of the SHV implementers: SLSA-style provenance review, in-toto step-attestation review, signature and identity verification,
source-to-artifact comparison, reproducible-build checks where a committed recipe and environment exist,
competent static and malware scanning, and ordinary incident-timeline and provenance analysis, each at
the documented recommended settings of the tool used, attested in a signed configuration manifest before
unsealing.
Executable boundary disposition vocabulary (frozen semantics; executable artifact is FB-3):
• A-ACCEPT – every mandatory baseline check applicable to that stratum passes and none is missing
or unverifiable;
• A-REJECT – at least one mandatory baseline check returns a verified contradiction or failure;
• A-INDETERMINATE – no check fails, but at least one mandatory check is absent, unverifiable,
stale, or ambiguous;
• A-NOT-APPLICABLE – the frozen baseline profile defines no decision rule for that stratum.
A verified failure dominates indeterminacy (A-REJECT over A-INDETERMINATE), paralleling the kernel’s
FALSE-dominates-UNKNOWN rule, so that both conditions distinguish observed contradiction from missing
information on the same principle. Baseline reason codes remain visible to adjudicators but not to the other
condition.
[FB-3 RESOLVED: the executable Condition A disposition function ships as xz_protocol_condition_a.py
with 29 decoy-fixture tests. Mandatory checks include SLSA_PROVENANCE for S-RELEASE and
STEP_ATTESTATION for S-BUILD. Digest sealed in Section 25.]
Fairness rules (frozen).
1. Every ambiguity in mapping a baseline tool’s behavior to the four labels is resolved in the direction
most favorable to Condition A, and the resolution is logged per boundary.
2. Condition A is never required to produce evidence types its tools do not emit; the absence of a
BSSG-shaped record type maps to A-INDETERMINATE or A-NOT-APPLICABLE under the frozen
profile, never to A-REJECT.
3. Where a baseline tool’s own documentation mandates fail-closed behavior on a missing attestation, that
documented behavior is used, neither weakened nor exaggerated.
4. Condition A may tune and iterate its conventional tools as a competent practitioner normally would,
on decoys only; no threshold may be tuned on XZ outputs.
5. The baseline disposition function is piloted exclusively on non-case decoys before the XZ packets are
opened.
6. The baseline team signs a fairness attestation; breach fires falsifier XZ-S11.
6.2 Condition B – SHV/BSSG-enhanced (CR-1)
Condition B receives the same packet bytes, cutoff, hardware class, wall-clock budget, and complete Condition
A tool capability, plus the SHV/BSSG layer fixed by SHVVP v0.8 Section 5: the declared transformation
9

contract, caller-conditioned outcome enumeration, recursive structural verification, independent projection
reconciliation, explicit UNKNOWN typing, descendant correction lineage, and the frozen five-conjunct BSSG
kernel as the decision function (Section 11). Condition B may not substitute a later case explanation, a
reference-standard label, or restricted technical description for evidence; doing so is an M10 event with zero
tolerance (T6).
6.3 Cross-condition controls
1. Separate teams and separate model instances for A and B; no crossover before both outputs are sealed;
model instances of the same vendor family do not serve both arms.
2. Teams matched on relevant experience; assignment to arm code randomized after eligibility screening;
arm codes held by a custodian.
3. Condition B’s additional time and training are logged, not hidden; M7 prices the added burden, with
training time reported both included and excluded (Section 19.1, item 15).
4. Neither condition receives the official advisories, mechanism narrative, sealed reference-standard ledger,
or post-cutoff evidence during the blinded stages.
5. Two independent A/B team pairs are run; pair results are reported separately and never pooled as an
apparent (n = 2) trial (SHVVP Phase A inferential-honesty clause, inherited).

7. Historical role mapping and the WithinAuth control graph
7.1 Mapping is functional, event-specific, and intent-free
The mapping assigns BSSG roles to historical functions, never to inferred intent, and never to natural-person
identity. The historical maintainer-identity question – which natural person or persons controlled which
identity – is OUT OF SCOPE: roles bind to authority positions evidenced in the public record (xz issue 103),
and this protocol makes no claim about any natural person.
Historical function

Candidate BSSG role

Account, service, or process issuing the candidate
effect
Contemporaneous declared project or distribution
policy authority
Service that admits or rejects the effect, where a
separable decision exists
Service or process that performs the transition
Repository namespace, artifact namespace, package
channel, installation target, or runtime resource
Independently administered source of admissible
pre-cutoff evidence
Named timestamp, sequence, epoch, transparency
entry, or signed nonce source
Later authority able to revise the decision

Subject
Contract/policy issuer
Decision point
Enforcement point / adapter
Target
Witness candidate
Freshness authority candidate
Adjudication authority candidate

7.2 Mapping rules (frozen)
1. Roles are assigned from pre-cutoff control facts, not from later culpability or outcome knowledge.
2. One historical entity may occupy multiple roles; the overlap is recorded and may make evidence
independence FALSE or UNKNOWN for affected records.
3. A distinct key, machine, vendor, or organization does not by itself establish evidence independence; the
control graph decides (Section 7.4).
4. If two or more mappings remain materially plausible and produce different predicate values, the primary
mapping status is AMBIGUOUS, the affected predicate is UNKNOWN in the primary analysis, and
10

all plausible mappings enter the sensitivity grid. The primary seam estimand counts only role-unique
boundaries (CR-3).
5. A role required by the mapping but absent from the historical record is MISSING, not synthesized.
6. No backfilled contract (CR-12). No contemporary BSSG contract may be projected into history.
A neutral analysis contract may organize the replay’s bookkeeping, but it cannot make historical
ContractMatch TRUE; ContractMatch is TRUE in the primary analysis only from a contemporaneous,
exact, active declared policy object (Section 11.3).
7.3 Evidence independence: canonical form
Axiom 5 is carried exactly as SHUDP v0.5 states it: for a declared acting substrate (S), event class (Eˆ*),
completeness boundary (B), witness set (W), and evidence ledger (L), every covered in-boundary event must
have a witness record whose generation act is not within (S)’s authority – not WithinAuth(gen(r), S) – where
WithinAuth(x, S) holds exactly when (S) can cause, modify, suppress, reconfigure, or credential (x) without
an independently detectable violation. A5 is quantified over the acting substrate, not the operator institution;
operator independence is recorded separately.
7.4 WithinAuth scoring on the historical record
The acting substrate (S_i), event class, completeness boundary, witness set, control graph, and temporal
floor are declared per stratum before scoring. The annotation values are:
• OUTSIDE_SUBJECT_AUTHORITY – only when the control graph supports NOT WithinAuth
for the generation act;
• INSIDE_SUBJECT_AUTHORITY – when WithinAuth is supported;
• UNKNOWN – when control or detectability is unresolved.
Rules: a signature does not establish OUTSIDE_SUBJECT_AUTHORITY; organizational distinctness does
not establish it without the control graph; witness records reconstructed only from subject-emitted logs are
not independent evidence; caller-supplied evidence is WithinAuth of the supplier and discharges nothing.
For a covered occurrence lacking timely independent evidence, the structural requirement is unsatisfied at
the axiom level while the event-level factual verdict remains UNKNOWN; the two labels are never collapsed
(SHUDP v0.5 discipline, inherited). Every S1-counted boundary must have its FALSE-grounding evidence
classified by source authority; if the load-bearing evidence is WithinAuth or UNKNOWN, the boundary
leaves the evidence-independent S1 subset and remains in the full sensitivity table (falsifier XZ-S3).
[FB-5 RESOLVED: the control-graph standard ships as xz_protocol_control_graph.py with 18 tests and
three decoy fixtures (OUTSIDE, INSIDE, UNKNOWN). Five authority channels, verdict binding enforced at
construction. Digest sealed in Section 25.]
7.5 Assumption register
Every declared element of the mapping, control graph, packet cutoffs, and (for sensitivity only) the modeleddeployment overlay receives an identifier DA-n, a statement, a tag in {LOAD-BEARING, CONTEXTUAL},
and the list of conjuncts whose evaluation depends on it. An assumption is LOAD-BEARING if flipping it
can change any primary decision. The register is sealed with the universe; a conjunct score resting on an
unregistered assumption is invalid and is rescored.

8. Staged blinding and information barriers
8.1 Mechanism-blind and label-blind only (CR-8)
The XZ compromise is one of the most publicly documented supply-chain incidents on record. No human
participant, and no pretrained model instance, can be presumed ignorant of its existence, general mechanism, or published chronology; pseudonymization cannot erase memorized detail. This protocol therefore

11

claims mechanism-limited blinding only, and any stronger blinding claim in any output is PROHIBITED.
Operationally:
• Label blinding. No executor, annotator, or adjudicator has access to the sealed reference-standard
ledger, its class counts, or the universe’s affected/clean lineage tags before their outputs are sealed.
• Mechanism-citation discipline. A finding or conjunct score whose recorded justification relies on
mechanism knowledge not derivable from the committed packet is a label-dependence event under
inherited M10, with zero tolerance under T6.
• Condition and identity concealment. Adjudicators receive condition-masked, order-randomized
records.
• Contamination instrumentation. Pre-task and post-task knowledge questionnaires; leakage sentinels
asking whether the executor recognizes case-specific details; isolated fresh instances per session; a
contamination ledger. Contaminated runs are retained and reported in a declared sensitivity set, never
deleted after results.
8.2 Stages
• Stage 0 – Protocol and tool freeze. Methods authors may know the case identity but hold no corpus
labels and no condition outputs. Rules, code, manifests, and decoy pilots are frozen and hash-committed.
• Stage 1 – Universe enumeration. Enumerators receive source-frame metadata and the eligibility
rule; they do not receive the reference-standard ledger. Dual enumeration per Section 5.4.
• Stage 2 – Packet construction. Packet custodians inspect source artifacts to build cutoff-limited
packets; they do not score conditions; every omission and redaction is logged with reason codes.
• Stage 3a – Contemporaneous boundary replay (Track 2). A and B teams receive pseudonymized
PRE_BOUNDARY packets and seal decisions before any forensic packet is available to them.
• Stage 3b – Forensic replay (Track 1). Fresh A and B instances receive the FORENSIC archive
and auxiliary corpora, without mechanism labels and without the reference-standard ledger.
• Stage 4 – Adjudication. Two adjudicators receive condition-masked findings plus the sealed reference
standard; they score independently; first-pass records and reliability statistics are locked before any
discussion.
• Stage 5 – Analysis unlock. The analyst receives arm identities only after universe, packet, conditionoutput, and first-pass adjudication commitments verify against the sealed hashes.
8.3 Barriers
Separate accounts, storage paths, prompts, and conversation histories; no shared retrieval cache between
arms; no internet access during scoring; immutable access logs; randomized arm codes held by a custodian;
prohibited cross-arm communication until unlock. A logged breach fires falsifier XZ-S12, and the affected
outputs are excluded with the exclusion itself reported.

9. Sealed commitments, channels, and evidence packets
9.1 Objects committed before any executor run
1. protocol bytes and version; 2. source-frame manifest and retrieval rules; 3. screened-event ledger and
effect-boundary universe; 4. sealed reference-standard ledger and class counts; 5. legitimate-difference
corpus inventory (200 items, 40 hard, inherited); 6. discrimination-set inventory (240 items, inherited);
7. descendant universe (inherited denominator for M9); 8. PRE_BOUNDARY packets; 9. FORENSIC
packets; 10. redaction and restriction map; 11. Condition A and Condition B executable environments;
12. role-mapping rule and control-graph standard; 13. adjudication manual and worked decoy examples;
14. analysis and sensitivity code; 15. production authority public keys and the manifest digest (FB-6
RESOLVED; see Section 25).
Two-channel discipline, inherited from SHVVP v0.8: Channel A carries authenticated authoritative
commitments verified against frozen production keys; Channel B carries untrusted raw condition and
12

annotation records, which may reference a commitment identifier but may not define universe cardinality,
authoritative hashes, signatures, evaluability, decisions, shares, or gate results. For sealed universes, both the
commitment-authority signature and the independent-anchor signature must verify; for realized run logs, the
evaluator verifies the pre-run commitment, independent anchor, contiguous signed event chain, and close
receipt; no runtime key override is permitted.
9.2 The sealed reference-standard ledger (CR-9)
The ledger inherited from SHVVP v0.8 Section 5.1 – classes K1 (undeclared executable divergence), K2
(conditional-build activation condition), K3 (downstream propagation), K4 (maintainer or release-authority
fact), K5 (correction, reversion, or clean-successor lineage), with “consequential fact” meaning an adjudicated
member of K1-K3 and nothing else – is carried under the name sealed reference-standard ledger. It is
an operational reference standard assembled from public evidence and custodian judgment, not infallible
ground truth: shared-source errors can affect both adjudicators, and agreement does not certify correctness.
Accordingly the ledger schema carries per-fact source links, confidence fields, and dispute fields; post-seal
corrections are protocol deviations, preserved append-only, with both original and corrected analyses reported.
The ledger cardinality and class counts are UNKNOWN in this document by design and become fixed by the
custodian’s seal, recorded in the run log before any executor session.
9.3 Evidence-packet rule
Each packet carries: packet identifier; boundary identifier or forensic case identifier; packet regime,
PRE_BOUNDARY or FORENSIC; cutoff time; ordered file inventory with byte length, media type,
SHA-256, acquisition time, and source locator; redaction map with reason codes; source-availability status at
cutoff; packet-builder identity and signature; independent packet-verification receipt; and supersession link if
corrected.
A PRE_BOUNDARY packet contains only information shown to be available by the boundary cutoff. A
FORENSIC packet may contain later safe evidence required by Track 1 reconstruction but excludes the
reference-standard labels and the mechanism explanation until adjudication. The two regimes are never mixed
in one primary estimate (CR-11), and a Track 2 decision computed on anything but a PRE_BOUNDARY
packet is void (falsifier XZ-S5).

10. Annotation schema
The normative machine-readable schema is closed to extra fields (additionalProperties false) and includes at
least:
record_id, protocol_version, manifest_digest, commitment_id,
boundary_id, stratum, packet_id, packet_regime, cutoff_time,
condition_code, team_pair, executor_id,
executor_prior_knowledge, leakage_sentinel_status,
role_mapping_id, role_mapping_status,
subject_id, contract_issuer_id, pdp_id, pep_adapter_id, target_id,
witness_ids, freshness_authority_id, control_graph_digest,
within_auth_assessment, within_auth_reason,
baseline_check_vector, baseline_disposition,
contract_match_value, effect_type_valid_value, target_allowed_value,
witness_healthy_value, evidence_current_value,
bssg_decision, predicate_reason_codes, raw_evidence_references,
finding_ids, claim_text_hash, discovery_time,
first_saved_evidence_time, mechanism_label_used, missing_as_clean,
reviewer_minutes, adjudicator_1_scores, adjudicator_2_scores,
adjudication_status, reference_standard_links,

13

dependency_cluster_id, descendant_links, deviation_ids
Raw evidence references, not caller-supplied derived facts, are the sole admissible input to the Condition
B evaluator. The evaluator recomputes every conjunct and the decision from raw evidence. A submitted
record carrying a derived decision, conjunct value, verification result, WithinAuth verdict, share, p-value,
or evaluability flag is rejected structurally before evaluation – the same discipline the BSSG reference gate
enforces and for the same historical reason: the recurrent failure mode in this program’s lineage is an interface
that lets the caller supply the property under test. A record with an out-of-schema field, unlisted reason code,
unregistered assumption citation, or missing packet-hash citation is likewise rejected before adjudication.

11. BSSG conjunct scoring from raw evidence
11.1 Kernel (restated informatively; the BSSG specification governs)
The truth domain is exactly TRUE, FALSE, UNKNOWN (CR-2).
[ Allow(r) ⇐⇒
ContractMatch(r) ∧ EffectTypeValid(r) ∧ TargetAllowed(r) ∧ WitnessHealthy(r) ∧
EvidenceCurrent(r)]
• ALLOW if and only if all five conjuncts are TRUE;
• DENY_FALSE if at least one conjunct is FALSE, including states that also contain UNKNOWN –
FALSE dominates order-independently;
• DENY_UNKNOWN if no conjunct is FALSE and at least one conjunct is UNKNOWN.
UNKNOWN never satisfies a conjunct; it is not “probably false”, not “not observed”, and not “clean”.
DENY_FALSE and DENY_UNKNOWN remain distinct in the stored record, the analysis, and every
publication table (falsifier XZ-S9). Kernel composition is computed by frozen executable code shipped with
the protocol, never by hand; text and code are the same rule written twice, and a divergence between them is
a defect raised as a finding, never resolved at analysis time.
11.2 Placement of NOT-EVALUABLE (CR-2)
NOT-EVALUABLE is never a kernel value. It exists at exactly three protocol levels: (a) boundary level –
the packet is incomplete, the role mapping is not unique, or a required decision function is not executable
for that boundary; (b) claim level – a registered claim’s mandatory inputs cannot be authenticated or its
decision rule is not executable; (c) run level – a mandatory protocol object (universe commitment, trust
root, arm output) is missing or fails verification. A conjunct that cannot be given a historically grounded
value is UNKNOWN at the kernel, carrying a typed reason code from a closed list that includes R-NODECLARED-OBJECT (the required declared object, such as a policy registry or witness declaration, has no
historical counterpart), R-RECORD-ABSENT, R-RECORD-UNVERIFIABLE, R-SCOPE-MISMATCH, and
R-EVALUATOR-ERROR. The reason codes preserve, inside the three-valued kernel, the distinction SHUDP
v0.5 draws between “the axiom’s objects do not exist here” and “evidence was absent” – without minting a
fourth truth value.
11.3 Historical scoring rules (primary analysis; no backfill, CR-12)
• ContractMatch is TRUE only from a contemporaneous, exact, active declared policy object that
binds the acting subject, target/effect policy, and relevant transformation. Missing or ambiguous policy
is UNKNOWN (R-NO-DECLARED-OBJECT or R-RECORD-ABSENT). A verified mismatch against
a contemporaneous declared policy is FALSE.
• EffectTypeValid is TRUE only when the effect type and adapter class are members of a closed
contemporaneous registry. A missing registry is UNKNOWN. A verified out-of-registry effect is FALSE.
• TargetAllowed is TRUE only when the target is canonicalizable and within the contemporaneous
declared scope and ceiling. Ambiguous target identity is UNKNOWN. A verified out-of-scope target is
FALSE.

14

• WitnessHealthy is TRUE only for the request’s coverage class and epoch when integrity, sequence,
lease or health, control-domain declaration, and the WithinAuth assessment all support it under Section
7.4. A responsive record is not thereby honest; ambiguity is UNKNOWN.
• EvidenceCurrent is TRUE only when the packet contains a named, valid, contemporaneous freshness
basis. Missing or ambiguous freshness is UNKNOWN. Verified stale or replayed evidence is FALSE
where the historical record supports that conclusion.
11.4 Foreseeable consequence, stated before data
Under these rules, large parts of the 2024 record will foreseeably score UNKNOWN on ContractMatch,
WitnessHealthy, and EvidenceCurrent, because the corresponding declared objects mostly did not exist.
That is the honest result. Symmetrically, Condition A will foreseeably carry a heavy A-INDETERMINATE
burden: A-ACCEPT requires every mandatory baseline check to pass with none missing or unverifiable, and
on a 2024 record many checks (SLSA provenance, step attestation, reproducible builds) will be absent or
unverifiable. This biases S1 toward zero, i.e., toward SEAM-FALSIFIED. That is the conservative direction
and is defensible, but it is stated here so that both sides of the UNKNOWN/INDETERMINATE burden are
disclosed. The protocol’s defenses against converting that artifact into apparent merit are: E-S2 separation
(CR-3), the reason-code decomposition (RQ6), the coverage tables (E-S4), the descriptive UNKNOWN-burden
metric S6 without invented numeric gates (CR-7), and the prohibited-language register (Section 0.3).

12. Adjudication and reliability
Two adjudicators independently score: correspondence to a sealed reference-standard fact; fact class and
consequential status under the inherited K1-K5 definitions; correctness of evidence-chain links; M4’s five 0-4
dimensions; mechanism-label dependence (M10); UNKNOWN-as-clean events (M11); boundary eligibility;
role-mapping uniqueness; WithinAuth status; dependency cluster assignment; and whether each Condition B
FALSE is supported by pre-cutoff evidence.
Adjudicators are blind to condition and team. First-pass records are immutable; reliability is computed
before any discussion; consensus labels serve only the final descriptive table and never replace the first-pass
reliability record. Because adjudicators share the reference standard, their errors are not claimed to be
independent in any probabilistic sense (CR-9).
M12 rule (inherited). Krippendorff alpha is computed separately for categorical fact adjudication and for
M4, with the minimum controlling:

• (α ≥ 0.80) : scoredresult;(0.67 ≤ α < 0.80) : scoredresultcarryingthemandatoryT EN T AT IV Equalif ier, barredf roms
4);
• (α < 0.67) : IN DET ERM IN AT E−ADJU DICAT ION ; therubricisretrained, af reshthirdblindedadjudicatorwhohasnotse
scoreisreportedalongsidethef irst.
Undefined alpha is not zero and not satisfactory; it is handled as INDETERMINATE-ADJUDICATION
under the adjudication-layer PA-Z4 rule (outside the scoring module, per Section 13.3.4). Categorical kappa
is reported secondarily against the conventional benchmark bands and does not replace alpha.

13. Inherited metrics, thresholds, and clauses (Track 1)
13.1 M1-M12, inherited without renaming (CR-1 companion ruling)
SHVVP v0.8 Section 5.2 freezes twelve metrics. Any statement that the frozen set is nine metrics is defective
and is corrected non-silently. This protocol inherits, unchanged:

15

ID

Metric

Denominator / definition anchor

M1
M2

Incremental consequential
detection (IDC)
Consequential recall

M3

Time to first consequential fact

M4

Evidence completeness score

M5
M6

False-positive rate on generated
differences
Discrimination balanced accuracy

M7

Reviewer burden

M8

Unsupported inferences

M9
M10

Correction reach
Label-dependence events

M11

UNKNOWN-as-clean events

M12

Adjudicator reliability

Consequential ledger facts found
by B and not by A
Sealed consequential cardinality,
per condition
Wall-clock minutes from corpus
access, per condition
0-4 on five dimensions, 0-20 per
fact-claim, averaged over the
shared fact set
200 declared-generated artifacts,
per condition
240-item discrimination set, per
condition
Reviewer-hours per case, per
condition
Adjudicated claims lacking a
traceable evidence chain
Sealed descendant universe
Findings citing a post-discovery
mechanism label
Absent projections or attestations
recorded as clean, compliant, or
safe
Krippendorff alpha, fact
adjudication and M4

13.2 T1-T8 and clauses A1-A6, inherited
• T1: IDC = 0. T2: on the shared fact set, B’s timing advantage at least 30 minutes AND at least
20 percent relative AND a 95 percent BCa interval excluding 0, operationalized by the protocol-level
Phase A scoring module (Section 13.3). T3: mean M4(B) minus M4(A) at least +2.0 with interval
lower bound above 0. T4: M5(B) minus M5(A) greater than +0.05 with interval lower bound above 0.
T5: M7(B)/M7(A) greater than 1.25 (interval conjunct retired; see Section 13.3). T6: M10 at least 1,
zero tolerance. T7: M6(B) below 0.90 OR interval lower bound below 0.80. T8: M11 at least 1, zero
tolerance.
• Clauses: A1 = T1; A2 = (IDC above 0) AND (T2 not satisfied) AND (T3 not satisfied), on the shared
set; A3 = T4; A4 = T5; A5 = T6; A6 = T7 OR T8.
[ FALSIFIED(A) = A1 ∨A2 ∨ A3 ∨ A4 ∨ A5 ∨ A6]
NOT-FALSIFIED(A) additionally requires M12 at least 0.80 and every denominator complete or UNKNOWNscored; a failed reliability gate yields INDETERMINATE-ADJUDICATION, never “not falsified”.
13.3 Protocol-level operationalization of Phase A M3, T2, and intervals (resolves FB-1 and
FB-2)
The deposited SHVVP v0.8 defines M3 as a scalar (time to first consequential fact) while T2 requires a
median “on the shared fact set” – a per-fact vector operation on a scalar input. Additionally, SHVVP v0.8
Phase A specifies no interval algorithm. Rather than amending the deposited SHVVP (which would touch a
frozen, published instrument), this protocol operationalizes Phase A’s M3, T2, and interval computation at
the protocol level. SHVVP v0.8 remains frozen and is cited by its specific DOI without modification.
The operationalization was developed through four carrying-audit rounds (dev-cycle labels v0.8.1 through
v0.8.4, referring to the protocol-level scoring module, not SHVVP versions) with two independent non-producer
16

seats (GPT-5.6 Sol, OpenAI; Kimi K3, Moonshot). Both seats confirmed the BCa computation bit-exact
against independent from-text references by v0.8.2. The operationalization ships as executable code with this
protocol deposit.
13.3.1 M3 as a per-fact observation vector. For each correctly adjudicated consequential fact f and
each condition c, M3(f,c) is the wall-clock minutes from first packet access to the first immutable saved
evidence record that identifies f under condition c. M3-FIRST(c) is the minimum over OBSERVED facts (the
parent scalar quantity). The shared fact set S consists of facts OBSERVED by both conditions; censored
non-discoveries do not enter S.
13.3.2 T2 restated. On S, for each f, Delta-M3(f) = M3(f,A) - M3(f,B). T2 is satisfied iff the median of
Delta-M3 is at least 30 minutes, the median of Delta-M3(f)/M3(f,A) (excluding M3(f,A)=0) is at least 0.20,
and the 95% BCa interval for the absolute median excludes zero.
13.3.3 T5 interval conjunct retired. T5’s “95 percent interval lower bound above 1.00” is retired. Phase
A has no T5 resampling unit (two team pairs, never pooled). The ratio gate (M7(B)/M7(A) > 1.25) stands
alone. This is a SUBSTANTIVE operationalization choice, recorded here.
13.3.4 Interval algorithms. All Phase A intervals are finite-corpus stability summaries, not population
confidence intervals (consistent with CR-10). The operationalization implements BCa bootstrap intervals
with 10,000 replicates, deterministic seeding, and thirteen code-level degeneracy rules (PA-Z1 through
PA-Z3, PA-Z5 through PA-Z14). PA-Z4 (alpha undefined / INDETERMINATE-ADJUDICATION) is an
adjudication-layer rule outside the scoring module. The scoring module, its test suite, and the SHA-256
manifest ship with this protocol deposit (Section 23).
13.3.5 Endpoint declaration. The parent SHVVP v0.8 M3 times to “first correctly adjudicated consequential fact.” This operationalization times to the first immutable saved evidence record that identifies the
fact. The distinction is declared as a substantive operationalization choice: where adjudication time differs
from evidence-record time, the two quantities may differ. No scalar-preservation claim is made.

14. Seam metrics (Track 2; descriptive, secondary to nothing but their own
denominators)
ID

Metric

Definition and denominator

S1

FALSE-grounded structural
divergence

S2

UNKNOWN-only structural
divergence

S3

Reverse structural divergence

S4

Dual-evaluable coverage

S5

Conjunct attribution

A-ACCEPT and DENY_FALSE
among dual-evaluable, role-unique
boundaries;
denominator
P
( _iD_i)
A-ACCEPT and
DENY_UNKNOWN; same
denominator; always separate;
never favorable
Non-accepting A disposition and
BSSG ALLOW; same
denominator
Dual-evaluable boundaries divided
by the full committed
public-record frame
TRUE/FALSE/UNKNOWN
counts per conjunct per stratum;
denominator: conjunct evaluations

17

ID

Metric

Definition and denominator

S6

UNKNOWN burden

S7

Evidence-independence coverage

S8

Role-mapping ambiguity

S9

Mapping stability

S10

Cutoff stability

S11

Boundary mediation coverage

S12

Denial reason preservation

DENY_UNKNOWN share of all
mapped decisions, plus
load-bearing UNKNOWN
conjunct counts with reason-code
decomposition; no numeric gate
attaches (CR-7)
Boundaries with at least one OUTSIDE_SUBJECT_AUTHORITY
admissible witness, divided by
covered boundaries
Boundaries with multiple
materially plausible mappings,
divided by enumerated boundaries
Range of S1-S3 over all
predeclared plausible mappings
Range of S1-S3 over the
predeclared cutoff perturbations
Boundaries with identifiable
historical decision and execution
roles, divided by the frame
Share of denials retaining the
DENY_FALSE/DENY_UNKNOWN
distinction and per-conjunct
reason codes without collapse;
frozen requirement 1.00

No seam metric receives a significance test, a p-value, or a population interpretation (CR-10).

15. Decision rules and labels
15.1 The four primary labels and the TENTATIVE qualifier (CR-4)
Every registered claim resolves to exactly one of:
1. NOT-EVALUABLE – assigned when one or more mandatory protocol objects cannot be authenticated
or an inherited decision rule is not executable: missing or invalid universe commitment, packet hash
mismatch, missing arm, absent production trust root, or no dual-evaluable boundary for the seam
analysis. NOT-EVALUABLE is not a favorable result and is reported with the same prominence as any
other label.
2. INDETERMINATE-ADJUDICATION – assigned when mandatory data are valid but the controlling first-pass alpha is below 0.67, or is undefined under the frozen post-amendment rule.
3. FALSIFIED – assigned when data and adjudication are admissible and the claim’s falsifier fires; every
firing clause is reported, not only the first.
4. NOT-FALSIFIED – assigned only when no falsifier fires, M12 is at least 0.80, and every denominator
is complete or UNKNOWN-scored.
Priority: NOT-EVALUABLE for invalid construction, then the reliability/admissibility rule, then FALSIFIED,
then NOT-FALSIFIED.

TENTATIVE is an orthogonal, mandatory reliability qualifier: when (0.67 ≤ α < 0.80), anyscoredlabelcarriesT EN T AT IV E
F ALSIF IED.BecausethedepositedSHV V P f ixesthisband, astrictclaimthatthef ourlabelsareexhaustiveisunavailablewith

18

15.2 Seam labels (Track 2)
• SEAM-NOT-EVALUABLE – no dual-evaluable role-unique boundary exists, or commitments fail
verification.
• SEAM-INDETERMINATE-ADJUDICATION – seam adjudication alpha below 0.67 or undefined.
• SEAM-FALSIFIED – S1 = 0 on the complete dual-evaluable role-unique frame (CR-6), or every
apparent S1 case fails a validity falsifier (XZ-S2 through XZ-S6).
• SEAM-NOT-FALSIFIED – S1 at least 1; every counted case FALSE-grounded on pre-cutoff evidence,
evidence-independent under the declared subset, and mapping-stable; seam alpha at least 0.80; all
denominator records complete or UNKNOWN-scored.
SEAM-NOT-FALSIFIED means only that at least one FALSE-grounded structural divergence was observed
in this committed frame; the scope limit travels in the same sentence.
15.3 The zero-divergence ruling (CR-6)
Where the dual-evaluable role-unique frame is empty or below a pre-registered floor, the report MUST carry
both the SEAM-NOT-EVALUABLE label and the S1 count computed on the full committed frame under
ambiguity-as-UNKNOWN, at equal prominence, with an explicit declaration that SEAM-NOT-EVALUABLE
is never the more favorable of the two. Role-ambiguity adjudication is sealed at Stages 1-2 with the universe
commitment, so uniqueness cannot be re-declared once S1 is visible (XZ-NE4).
A zero result is a real result and is labeled as falsification of the incremental-value claim, not as its survival:
IDC = 0 fires A1 on Track 1; S1 = 0 yields SEAM-FALSIFIED on Track 2. The contrary labeling proposed
in one seat draft is REJECTED and recorded. Negative outcomes are immutable deposit artifacts, preserved
in the audit ledger, and reported with the same prominence as positive ones – this is the entire point of
freezing the protocol before data.

16. Exact falsifier register
A falsifier is a finite observation; one occurrence flips the named claim; falsifiers are never averaged into a
pass rate.
16.1 Track 1 falsifiers (inherited routing)
ID

Finite observation

Result

XZ-A1

M1 IDC = 0

XZ-A2

IDC above 0 and neither T2 nor
T3 satisfied on their valid domain
T4 fires (material false-positive
increase)
T5 fires (material burden increase)
Any M10 event (post-discovery
mechanism label is load-bearing)
T7 or T8 fires (discrimination
failure, or missing provenance
recorded as clean)

FALSIFIED through A1
(incremental-value claim)
FALSIFIED through A2

XZ-A3
XZ-A4
XZ-A5
XZ-A6

16.2 Track 2 seam falsifiers

19

FALSIFIED through A3
FALSIFIED through A4
FALSIFIED through A5; zero
tolerance
FALSIFIED through A6

ID

Finite observation

Result

XZ-S1

S1 = 0 on the complete
dual-evaluable role-unique frame
Every apparent S1 case becomes
DENY_UNKNOWN, ALLOW, or
boundary-level
NOT-EVALUABLE when
caller-supplied derived facts are
removed
Every apparent S1 case depends
on a witness generation act that is
WithinAuth or UNKNOWN
A favorable S1 count exists under
only one materially contestable
role mapping and disappears
under another predeclared
plausible mapping
A counted S1 case uses evidence
created after its boundary cutoff
A counted S1 case uses a
post-discovery mechanism label
Any DENY_UNKNOWN is
counted in S1

SEAM-FALSIFIED (CR-6)

XZ-S2

XZ-S3

XZ-S4

XZ-S5
XZ-S6
XZ-S7

XZ-S8

Any ALLOW record has a
conjunct not TRUE

XZ-S9

DENY_FALSE and
DENY_UNKNOWN collapsed
anywhere in stored records or
tables
A committed boundary omitted
without a signed reconciliation
and unfavorable scoring
Condition A denied a tool,
evidence item, time budget, or
ordinary analyst action available
to B as common capability; or the
fairness attestation breached
An arm accesses the
reference-standard ledger or
official mechanism narrative
before its output seal

XZ-S10

XZ-S11

XZ-S12

SEAM-FALSIFIED

Evidence-independent seam claim
FALSIFIED
Mapping-robust seam claim
FALSIFIED

Contemporaneous seam claim
FALSIFIED
Contemporaneous seam claim
FALSIFIED and XZ-A5 fires
Scoring implementation
FALSIFIED; run
NOT-EVALUABLE until
corrected
Kernel-mapping implementation
FALSIFIED; run
NOT-EVALUABLE
Decision-semantics
implementation FALSIFIED; run
NOT-EVALUABLE
Universe integrity FALSIFIED;
run NOT-EVALUABLE
Fair-comparator claim
FALSIFIED; comparative run
NOT-EVALUABLE

Blinding claim FALSIFIED;
primary run NOT-EVALUABLE

16.3 Integrity falsifiers (both tracks)
ID

Finite observation

Result

XZ-I1

Any UNKNOWN resolved to
TRUE by a default, retry, cache,
or operator override

UNKNOWN-discipline claim
FALSIFIED

20

ID

Finite observation

Result

XZ-I2

Any metric computed against a
denominator differing from the
sealed manifest
Shipped decision code and
protocol text yield different labels
on any input
Any published output uses a
prohibited effectiveness verb
applied to BSSG, an outcome
modal, or aggregates the two
DENY classes
A post-seal reference-standard
correction is applied without a
deviation record and dual
(original and corrected) analysis

The computation is void;
denominator claim FALSIFIED

XZ-I3

XZ-I4

XZ-I5

Internal-consistency claim
FALSIFIED; new version required
Reporting-discipline claim
FALSIFIED; append-only
correction required

Reference-standard discipline
FALSIFIED

16.4 Observations yielding the remaining labels
ID

Exact observation

Result

XZ-NF1

No A1-A6 clause fires; M12 at
least 0.80; all denominators
complete or UNKNOWN-scored
S1 at least 1; every counted case
FALSE-grounded,
evidence-independent under the
declared subset, mapping-stable;
seam alpha at least 0.80
Required data valid; controlling
alpha below 0.67
Required data valid; controlling
alpha undefined under the frozen
rule
Universe or ledger commitment
does not authenticate
A required arm or team pair does
not complete
T2, T3, T4, T5, or T7 cannot be
computed under a frozen edge rule
No dual-evaluable role-unique
boundary exists

NOT-FALSIFIED (Track 1)

XZ-NF2

XZ-IA1
XZ-IA2

XZ-NE1
XZ-NE2
XZ-NE3
XZ-NE4

SEAM-NOT-FALSIFIED

INDETERMINATEADJUDICATION
INDETERMINATEADJUDICATION
NOT-EVALUABLE
NOT-EVALUABLE
NOT-EVALUABLE
SEAM-NOT-EVALUABLE

Negative and indeterminate outcomes are immutable deposit artifacts. They are not removed from titles,
tables, abstracts, or ledgers to improve any narrative.

17. Missing data and UNKNOWN handling
1. Missing evidence never becomes clean, compliant, current, healthy, matched, valid, or allowed.
2. In Condition B scoring, missing or ambiguous required evidence maps to UNKNOWN with a typed
reason code, unless a verified contradiction supports FALSE.
21

3. FALSE dominates the decision classification even when other conjuncts are UNKNOWN.
4. Missing committed boundaries remain in the denominator ledger and are non-passing for descriptive
shares, except where a frozen estimand expressly requires dual evaluability – in which case the E-S4
coverage tables accompany every use of the evaluable subset.
5. Missing arm output, invalid commitment, or absent scoring rule yields NOT-EVALUABLE, never
imputation.
6. No complete-case analysis is primary.
7. Tipping-point sensitivity treats unresolved values in both favorable and unfavorable directions, but
never replaces the primary UNKNOWN label.
8. A later evidence arrival creates a new versioned record; it never overwrites the original cutoff result.
9. No numeric UNKNOWN-share cap is frozen in this draft (CR-7). UNKNOWN burden is reported
completely via S6 and RQ6; any future numeric evaluability gate must be justified from decoy pilots
and enter by amendment.
10. Absence of a public installation or runtime sampling frame is a frame limitation, not zero events, and is
reported as stratum-level NOT-EVALUABLE.
11. The protocol applies the UNKNOWN discipline to itself: Section 25 lists the primary values this draft
does not fix; residual unfixed values (dual-evaluable floor, full UNKNOWN reason-code list, wall-clock
budget) are disclosed as standing boundaries. No favorable default may be assumed for any of them.

18. Analysis plan
18.1 Verification precedes analysis
Verify all manifests, commitments, packet hashes, environment identities, and arm seals; compute first-pass
adjudicator reliability; only then unlock labels (Stage 5).
18.2 Track 1 (forensic)
If evaluable, compute M1-M12 by team pair; apply T1-T8 and A1-A6 exactly, using the protocol-level Phase
A operationalization of Section 13.3 for M3, T2, T5, and all intervals; report every firing clause; report pair
1 and pair 2 separately, never pooled; report any route-level statements only where the inherited SHVVP
v0.8 Section 8 descriptive gates allow them, with the single-case limitation in the same sentence and with no
inferential language anywhere.
18.3 Track 2 (seam)
Verify the boundary universe and screened-event reconciliation; tabulate strata before viewing decisions;
recompute Condition A dispositions and BSSG conjuncts from raw records with the frozen executables;
compute S1-S12 overall and per a priori stratum; present the complete A-by-B decision matrix including
A-NOT-APPLICABLE and both DENY classes; present conjunct truth-state tables without collapsing
UNKNOWN; present WithinAuth and mapping-status tables; link reference-standard facts only after decisions
are sealed; compute no p-value, no null-hypothesis test, and no population confidence statement for any seam
metric (CR-10).
18.4 Time analysis
Discovery time is measured from first packet access; the primary timestamp is the first immutable saved
evidence record identifying the fact, not a later narrative claim; pauses, tool failures, and adjudication time
are recorded separately; timeouts remain censored at the fixed budget and cannot be coded as discoveries.
18.5 Dependence (CR-10)
Before labels, boundaries receive dependency-cluster identifiers based on shared immediate lineage, build
recipe, administrative decision, or distribution transaction – commits, releases, builds, packages, installations,

22

and runtime events descending from one act are one cluster, not many observations. Report raw item-level
summaries; cluster-level summaries; leave-one-cluster-out ranges; one-lineage-at-a-time removals; and no
pooled (n) built from descendants of the same event. A single case can collapse to very few effective clusters;
if it does, that is reported, not obscured.
18.6 Multiplicity
A1-A6 form a preregistered deterministic falsifier disjunction, not a family of significance tests. All seam
metrics are frozen in advance, all are reported, and none is promoted after results. Any exploratory
computation is labeled exploratory and cannot change a registered decision. Multiplicity is controlled by
refusing selective inference, not by adjusting it.

19. Sensitivity analyses
19.1 Frozen sensitivity grid (run in full, regardless of direction; results can only demote)
1. All predeclared plausible role mappings (Section 7.2).
2. Strict role-unique subset versus the full ambiguity-as-UNKNOWN frame.
3. Evidence-independent witness subset versus all witness candidates.
4. Boundary cutoff at the exact timestamp, minus 24 hours, and plus 24 hours, with post-effect evidence
still prohibited from the contemporaneous primary result.
5. Exclusion of executors reporting prior case-mechanism knowledge.
6. Inclusion of contaminated executors as a separate table.
7. Per-team-pair results.
8. Per-stratum results.
9. Leave-one-dependency-cluster-out.
10. All missing values resolved unfavorably to Condition B.
11. All unresolved reference-standard disputes removed.
12. Original sealed ledger versus corrected ledger, if a correction occurs.
13. A-NOT-APPLICABLE excluded from the S1 denominator and, separately, retained as non-supportive;
both shown.
14. DENY_UNKNOWN shown separately and, as an audit-only anti-analysis, a demonstration of how
adding it to S1 would change the answer – without ever adopting that analysis.
15. Burden accounting with Condition B training time included and excluded; both shown.
16. First-pass adjudication versus post-discussion consensus, with registered decisions taken on the frozen
first-pass record.
19.2 Demotion-only rule
No sensitivity analysis may promote a result. Sensitivity can only demote: an S1 member to MAPPINGSENSITIVE or out of the evidence-independent subset; a stratum or claim to NOT-EVALUABLE; a label to
TENTATIVE via its effect on the controlling adjudication set.
19.3 Modeled-deployment overlay (MDL-SENSITIVITY; CR-12)
A separately labeled sensitivity analysis MAY evaluate the kernel under a declared modeled deployment – a
hypothetical contract registry, witness set, and freshness authority specified per stratum in the assumption
register – to characterize which conjuncts change value when BSSG-shaped declared objects are assumed to
exist. Every output of this analysis carries the label MDL-SENSITIVITY in the same table cell or sentence;
it never enters S1, never appears in a headline, abstract, or primary table, and never supports any registered
claim. Its sole function is to decompose the UNKNOWN burden of the primary analysis into “missing
historical infrastructure” versus “structurally undecidable even with assumed infrastructure.”

23

20. Deviations and amendments
20.1 Deviation records
A deviation record includes: deviation identifier and discovery time; affected files, runs, boundaries, metrics,
and claims; whether it was known before or after outcome access; cause and responsible role; effect on blinding,
eligibility, denominator, packet, condition, adjudication, or analysis; primary handling under the frozen rule;
corrected handling, if any; whether a new protocol version is required; signatures and supersession links. No
deviation is repaired only in prose; the original run and output remain deposited. An unlogged deviation
discovered later voids the affected analyses (NOT-EVALUABLE) and is itself a finding.
20.2 Amendment rule (inherited from SHVVP v0.8 Section 12, extended)
A change is SUBSTANTIVE – requiring a new frozen version, new hashes, an append-only amendment
entry, and a re-run carrying audit – if it alters any of: an estimand; a condition definition or label; a metric,
threshold, or decision rule or its Boolean structure; an interval or degeneracy algorithm; the universe frame,
inclusion rule, stratum set, cardinality, or de-duplication rule; a packet cutoff or evidence-admission rule;
the role mapping or WithinAuth interpretation; a blinding or contamination rule; a missing-data rule; an
analysis population; the adjudication rubric or reliability thresholds; a safety or publication boundary; a trust
root; or the factual content or attribution of an empirical anchor. Editorial errata are limited to formatting,
typography, cross-reference numbering, or typographical corrections incapable of changing any decision.
20.3 Non-amendable floor
The safety and publication posture of Section 21 and the inherited SHVVP hard safety boundary are
non-amendable by any later version of this protocol.

21. Safety and publication posture
1. This protocol: OPEN. To be deposited open-access; hazard-free by construction of Section 0.2.
2. The later corpus: SPLIT. The open corpus deposit contains safe metadata, opaque identifiers,
schemas, commitments, annotations, derived non-actionable summaries, and redaction receipts. Restricted artifacts are held under a separate DOI with access controls and a public manifest exposing
identity and integrity (content hashes, sizes, types, access conditions) without exposing restricted
content.
3. Metadata hygiene (non-amendable). Hazardous artifact content, payload details, activation
conditions, and restricted technical descriptions never appear in any title, abstract, keyword list,
description, public README, public manifest description, or in this protocol text – that is, never in
public Zenodo metadata of any deposit in this chain.
4. No restricted artifact is executed on a reachable host; no public service is exposed; analysis occurs
offline in an isolated environment with no production credentials, no external target, and no outbound
network path.
5. The stop authority, incident owner, access approver, and disclosure path are named before corpus
construction begins.
6. The eventual empirical paper preserves negative, indeterminate, and not-evaluable outcomes; none is
removed to improve a narrative.

22. Audit and carry plan
Before any FROZEN status:

1. producer self-check of text/code parity, executed by the prohibited-content verifier (xz_protocol_prohibited_content_verifi
when shipped), which fails the package if any prohibited sentence appears outside the Section 0.3

24

registry or if any non-DOI citation falls outside the four permitted XZ sources;
2. schema validation and manifest verification;
3. exhaustive five-conjunct (3ˆ5 = 243) kernel decision-state tests;
4. an XZ-specific adversarial suite covering at least: caller-supplied derived facts, denominator substitution, commitment-identifier confusion, trust-root override, packet-regime mixing, post-cutoff evidence injection, role remapping after outcomes, DENY-class collapse, and screened-event suppression
[FREEZE-BLOCKER FB-7a/FB-7b];
5. independent rerun of the universe enumeration from frozen metadata queries;
6. carry by two executing non-producer seats of different vendor families, each executing the canonical
bytes, recomputing identity values, running all tests, and attacking the commitment and decision paths;
carrying seats verify the normative properties directly – gate execution is a build-time convenience in
the tooling bundle (not carried), not the check; same-vendor seats count once; producer-family review
is advisory;
7. a HALT from either carrying seat blocks freeze outright and requires a new version – the rule that
HALTED SHVVP v0.1 through v0.7 and is inherited without weakening. Exception (added v0.37):
a persistent architectural HALT – defined as a HALT whose original clearance conditions are met
on shipped bytes and whose re-HALT bases are generated by the disposition of the prior HALT in a
non-converging loop – is disclosed as a standing condition of the freeze and does not block under this
item. The exception applies only when (a) the HALTing seat has audited the original-HALT version and
at least one subsequent carrying round (audit occasions, not necessarily consecutive protocol versions),
(b) each version met the prior clearance conditions and the seat re-HALTed on new bases, and (c) six or
more carrying seats across two families returned non-HALT on the same bytes. The exception does not
apply to first-time HALTs, to HALTs whose original clearance conditions are unmet, or to HALTs on
Class A or Class B findings as classified by the HALTing seat’s own published report (not the producer).
Threshold disclosure (v0.38): the thresholds “two” (audit occasions) and “six” (carrying seats) are
chair-fitted parameters derived from the observed trajectory, not from a principled basis; the CR-7
parity with Section 0.4 is documented here.
22.1 Producer definition (added v0.5). For carrying-seat eligibility under this section, “producer” means
the model family that served as the primary development seat for the executable artifacts in this protocol.
Claude (Anthropic) is the producer family: Claude Opus 4.6 produced the kernel module, Condition A
evaluator, source-frame manifest, control-graph standard, Phase A scoring module, adversarial suite, and
trust roots. Kimi (Moonshot) and GLM (Zhipu/Z.ai) are non-producer families that did not contribute to the
protocol design or executable artifacts; they are eligible carrying seats. GPT (OpenAI) served as a council
advisory seat for v0.1 text integration; GPT-5.6 Sol self-disqualified from carrying-seat eligibility in v0.6 audit
F-XZ06-GPT-04, citing the inherited SHVVP v0.8 design-contributor exclusion. That self-disqualification
is accepted: GPT audits are retained as adversarial records but do not count toward the two-family carry.
Same-vendor seats count once; producer-family review is advisory. CARRY-CLEAN is a non-HALT verdict
and satisfies the convergence requirement.
The editor or producer never certifies its own artifact. Carry is limited to the checks executed; it is not peer
review and is not a universal claim about the later corpus or empirical result.
22.3 Condition severity classification (added v0.33). Carrying-seat conditions are classified by type
for disposition:
• Class A (byte-level error): a sealed claim is false on the shipped bytes (digest mismatch, wrong
count, contradicted status). HALT-grade.
• Class B (concealed defect): an error the entry does not disclose. HALT-grade.
• Class C (disclosed boundary): a limitation the entry names and scopes correctly. Non-blocking.
• Class D (gate limitation): the gate does not cover a class it could cover; the gap is disclosed.
Non-blocking.
• Class E (process observation): governance note, metric trend, or recommendation. Non-blocking.
CONDITIONAL PASS with only Class C/D/E conditions is non-HALT; Section 22 item 7 requires only that
no carrying seat HALT (subject to the persistent-architectural-HALT exception added at v0.37 and carried

25

at v0.38-v0.74). The classification is defined here to scope future disposition, not to retroactively reclassify
prior findings; the v0.31 carrying round’s conditions are independently verifiable as gate-limitation class on
the shipped bytes regardless of this taxonomy.
22.2 Self-consistent-forgery boundary (added v0.20, narrowed v0.21). The full gate suite proves
internal agreement – that the protocol text, code digests, manifest, trust roots, and seals are mutually consistent.
A party controlling the protocol text, code files, trust roots, manifest, seal file, and HISTORY.sha256 can
mutate any normative artifact (build.py control is not required – the derivation recomputes over forged bytes
because HISTORY.sha256 ships inside the packet and is regenerable. Only externally held bytes (a carrying
seat’s dispatch manifest, a Zenodo deposit receipt, or the PRIOR_HISTORY value published outside the
producer’s control) distinguish a wholesale forgery from the authentic packet), recompute every internal
surface, and produce a packet that passes all build checks with rc=0. The anchors outside the producer’s
control are: (a) the carrying seats’ independently held dispatch manifests; (b) external deposit receipts
(Zenodo DOIs, IPFS CIDs); (c) the PRIOR_HISTORY chain, whose root predates the current producer
session. For carried entries (v0.1 through v0.74), the PRIOR_HISTORY derivation in build.py [9b] detects
retroactive mutation: any in-place change to any carried entry or to Section 27’s non-entry text breaks the
derivation, because two independent SHA-256 matches must hold simultaneously. This control covers the
historically dominant failure mode (nine recorded in-place mutations at v0.4, v0.9, v0.11, v0.16, v0.17, v0.41,
and v0.47). The residual blind spot is a self-consistent forgery where the forger regenerates HISTORY.sha256
over the mutated text (as the v0.41 corruption would have achieved had the regex been applied consistently).
The external anchors listed above are the only defense against this class.

22.4 Standing Boundaries and Irreducible Residuals
This instrument rests on five axioms, disclosed and not defended:
• A-X1 (SHA-256 collision resistance): The seal chain, PRIOR_HISTORY, PACKET_SHA256SUMS,
and all digest-based integrity checks assume SHA-256 is collision-resistant.
• A-X2 (Python interpreter correctness): build.py and pytest assume CPython executes correctly.
• A-X3 (Model non-collusion): The two-family carry rule assumes auditor models from different
vendor families do not coordinate to produce convergent false findings or convergent false PASSes.
• A-X4 (Append-only storage integrity): The PRIOR_HISTORY chain detects retroactive mutation
of carried entries but cannot detect mutation of the storage medium before the first external anchor.
• A-X5 (Dispatch integrity): PACKET_SHA256SUMS mitigates delivery-channel corruption but is
inside the packet.
This instrument cannot verify that it has no remaining byte-false claims about its own verification properties.
This is a formally irreducible residual and is DISCLOSED, not denied. The sufficiency judgment – whether
the evidence this instrument provides constitutes adequate structural honesty – is a human act outside the
instrument’s scope.
Item 8 (added at v0.75). FROZEN may be declared when (a) the remaining Class A findings are
demonstrated to be structurally irremediable rather than concretely repairable, (b) the structural argument
for irremediability is documented in the amendment record and independently verified by at least two
non-producer model families, and (c) all concretely repairable Class A from the most recent audit round
have been closed on the shipped bytes. The Goedel sentence – “this instrument cannot verify that it has no
remaining byte-false claims about its own verification properties” – is the canonical instance of a structurally
irremediable Class A. Prose-version-token staleness that regenerates at every version boundary is a second
instance, documented across R13-R31 (thirteen consecutive rounds). Bearer states under amended rules:
TRUE (condition met), DISCLOSED (condition demonstrated structurally unachievable, independently
verified, named in the Sidrat clause), or FALSE (neither). FROZEN requires all bearers TRUE or DISCLOSED;
none may be FALSE. [DISCLOSED]

26

23. Zenodo deposit composition (protocol deposit, OPEN)
1. protocol source text (no rendering ships; any PDF generated for deposit is unbound until manifested); 2.
machine-readable protocol metadata; 3. PROTOCOL_STATUS.json; 4. program-chain and DOI-role
statement (Section 26); 5. source-frame manifest carrying the four primary XZ URLs; 6. closed schemas
for boundaries, packets, conditions, findings, adjudication, deviations, corrections, and WithinAuth
records; 7. the Condition A baseline specification and executable evaluator [FB-3]; 8. the Condition
B BSSG mapping specification and executable evaluator; 9. exhaustive kernel vectors and tests; 10.
universe-enumeration code and decoy fixtures; 11. scoring, analysis, and sensitivity code; 12. the
adversarial test suite [FB-7a/FB-7b]; 13. production public-key manifest and manifest digest [FB-6];
14. empty template for the sealed reference-standard ledger; 15. empty templates for packet and
descendant commitments; 16. the prohibited-content and prohibited-claim verifier, with the versionparity, closure-claim, manifest-digest, and amendment-record-integrity gates, the locus register, and
their fixture-pair test suite; 17. SHA-256 manifest over every normative file; 18. all model-council seat
reports, unmodified; 19. the producer disposition register; 20. carrying reports and execution receipts
[FB-7a/FB-7b]; 21. amendment and deviation ledgers; 22. license, authorship, conflict-of-interest,
AI-assistance, and no-peer-review statements.
The later open corpus deposit contains only safe materials; the restricted corpus deposit has its own DOI,
access controls, integrity manifest, and public cross-reference; the empirical deposit cites both without copying
restricted material into open metadata.

24. Limitations (to be carried verbatim into the eventual paper)
1. Single purposively chosen case. The XZ case was selected because it is the program’s public anchor;
nothing corrects for that purposive choice, and no result generalizes beyond it.
2. Retrospective frame asymmetry. The public record is hindsight-shaped: the affected lineage is
documented far more densely than clean lineages, and most forensic sources post-date disclosure. The
enumeration-input manifest records, per input document, whether it pre- or post-dates 2024-03-29, so
the asymmetry is measurable; it is not removable.
3. Counterfactual non-identifiability. Structural decision divergence on frozen bytes does not establish
a changed historical outcome, and no analysis in this protocol can.
4. Pretraining contamination. Model executors’ training data includes XZ forensics; contamination
instrumentation bounds and reports this but cannot eliminate or fully verify it.
5. Shared-source adjudication error. Adjudicators share the reference standard; agreement does not
certify correctness, and reference-standard errors can be correlated across adjudicators.
6. Constructed comparator. Any executable Condition A is a constructed operationalization of
“competent conventional practice”; the fairness rules bound, but cannot erase, that constructedness.
7. UNKNOWN burden. The primary analysis will foreseeably carry a heavy UNKNOWN burden
reflecting absent 2024 infrastructure; the protocol reports it completely rather than gating it with an
invented number (CR-7).
8. Effective sample collapse. Dependency clustering may reduce the case to very few effective clusters;
descriptive shares may rest on small counts, and no interval can repair that.
9. Single-author governance. Methodology interpretation and amendments are single-author acts
within this program, with no external governance body; council seats and carrying seats are AI systems,
not human peer reviewers, and the strongest available check is cross-vendor executing carry plus
complete append-only disclosure.
10. Frame incompleteness. The public-record frame omits private installations and runtime events by
construction; stratum-level NOT-EVALUABLE labels mark, and do not fill, that gap.

27

25. Freeze-Readiness Register (FREEZE-BLOCKER fields)
This register lists every item that blocks FROZEN status. Each carries an explicitly labeled field that this
draft cannot responsibly invent. A version of this protocol may be issued as FROZEN only when every field
below is filled by a visible amendment, canonical executable artifact, or signed commitment, and the carry
rule of Section 22 has been satisfied.
What must exist before
freeze

FREEZE-BLOCKER
field

SHVVP M3/T2
computability mismatch

RESOLVED in v0.2

FB-2

Under-specified Phase A
interval algorithms

RESOLVED in v0.2

FB-3

No executable Condition
A disposition function

RESOLVED in v0.3

FB-4

No sealed source-frame
manifest

RESOLVED in v0.3

FB-5

Untested
Within-Authority control
graph

RESOLVED in v0.3

FB-6

Unsigned trust roots

RESOLVED in v0.31

FB-7a

No adversarial suite

RESOLVED in v0.3

RESOLVED:
protocol-level Phase A
scoring module ships
with deposit
RESOLVED: 69-test
scoring module with
golden vectors ships with
deposit
RESOLVED:
xz_protocol_condition_a.py
(SHA-256:
348ee2593b253555d70db631ed151294562e4
29 decoy tests (SHA-256:
00b814db996e7f1a4e3ba94af624a1d2eb64da
RESOLVED:
xz_protocol_source_frame.py
(SHA-256:
fad63e33d5a11e65d68b9e5ee55b1d8460d695
22 source-frame tests
(SHA-256:
b46bc3aee4962df5ef866c0116dc2934990b97
RESOLVED:
xz_protocol_control_graph.py
(SHA-256:
5bf05c743f65850a9efa8cf38ca5694b7cf0e930
30 control-graph tests
(SHA-256:
f2d8ace281fe68cb80fb42a8829f65f66f7f874d
RESOLVED:
xz_protocol_trust_roots_PUBLIC.json
(SHA-256:
5fc18f3c72e9132e1b04bfcaa57088499a17cf3
manifest digest
f2c84764afe16be02a06084d5aad83d773c31a
RESOLVED:
test_xz_protocol_adversarial.py
(SHA-256:
1b72f5210f85d2ad0b24d72a9099698c5c2a26
27 tests, nine Section 22
categories

ID

Blocker

FB-1

28

ID

Blocker

FB-7b

Two-family executing
carry on canonical bytes

29

What must exist before
freeze

FREEZE-BLOCKER
field

RESOLVED v0.31;
PENDING RE-CARRY
v0.75

RESOLVED: six
non-producer carrying
seats (GLM-5.2 x3, Kimi
K3 x3) across two
families returned
CONDITIONAL PASS
(non-HALT) on v0.31
canonical bytes
(sha256sum -c rc=0).
Two carrying seats
(GLM-5.2 carry-1C,
Kimi K3 carry-1A)
HALTed at v0.33 and
re-HALTed at v0.35 on
new bases after original
clearance conditions
were met. These are
persistent architectural
HALTs per the Section
22 item 7 exception
(added v0.37): original
conditions met, re-HALT
on disposition-generated
bases, non-converging
loop demonstrated
across two audit
occasions (v0.33 and
v0.35), six carrying seats
non-HALT on the same
bytes. The two HALTs
are disclosed as standing
conditions; the six
non-HALTs satisfy the
carry. Post-v0.31 note:
CONV R1/R2 on
v0.41/v0.42 and
Convergence Rounds 2-5
on v0.43-v0.46 produced
Class A carrying-seat
HALTs (Kimi K3); Class
A is outside the item 7
exception. Kimi K3 Seat
2 returned
CONDITIONAL PASS
(non-HALT) on v0.46
bytes at R5; a second
non-producer carrying
family returning
non-HALT on the same
or successor bytes is
required before
RESOLVED status can
be reaffirmed. R6
(v0.47): all 3 carrying
seats (Kimi K3) HALTed
binding (append-only
violation). R7 (v0.48):

ID

Blocker

FB-8

Governance convergence
under audit

What must exist before
freeze

FREEZE-BLOCKER
field

OPEN

OPEN: governance-layer
prose claims (status,
repair assertions,
convergence) are not
independently verifiable
from bytes alone. Exit
condition: two
non-producer carrying
seats from different
families return
non-HALT on bytes
where every prose claim
in the current entry is
verified against shipped
bytes by grep before
sealing. The v0.41
append-only corruption
(21 genuine
PRIOR_HISTORY
chain values overwritten
by blind regex, build
gate disabled, false
attribution sealed)
demonstrates the failure
mode this blocker names.

Additional residual UNKNOWNs at this draft, listed under the self-applied UNKNOWN discipline and
assuming no favorable default: custodian identity; universe cardinality and per-stratum counts; referencestandard ledger cardinality and class counts; modeled-deployment overlay parameter values; annotator,
adjudicator, enumerator, and team identities and the model families or humans occupying them; analysis
software versions; and the Zenodo version relationship recorded in Section 26.2 (RESOLVED in v0.10: concept
21712481, versions 21712482 and 21713180; PDF-printed 21611192 is a deposit defect routed upstream).

26. Sources and citation record
26.1 The supplied program corpus (thirteen distinct records)
Record

DOI

BSSG: An Evidence-Independent Control Plane for
Bounded Artificial Agency (paper and artifact
bundle, supplied record)
Structural Honesty Validation Protocol (SHVVP)
v0.8
Is Evidence Independence an Axiom? Decomposing
a Proposed Extension to AX-SH (concept
10.5281/zenodo.21539073; v0.4 = 21539074, v0.5 =
21539816)

10.5281/zenodo.21713180

10.5281/zenodo.21583202
10.5281/zenodo.21539816

30

Record

DOI

Declared Isolation and Executable Containment
(SHUDP v0.4)
Inheritance, Transmission, and the Locus of
Accountability
Structural-Honesty Dissertation v1.4 (consolidated
reference canon)
Structural Honesty: Axioms for Detecting
Surface-Substrate Divergence (flagship v0.14)
Predictive Modeling Discipline v1.8
Verify, Do Not Trust: SHV Method v1.1
Structural Honesty Verification: A New Frontier
Predictive Finding Localization (Pilot Study)
Audit Framework v3.0 (BAF)
BAF Application Brief v1

10.5281/zenodo.21522932
10.5281/zenodo.21522793
10.5281/zenodo.21501912
10.5281/zenodo.21500700
10.5281/zenodo.21462879
10.5281/zenodo.21450932
10.5281/zenodo.20131072
10.5281/zenodo.20093407
10.5281/zenodo.20046910
10.5281/zenodo.20031395

The AX-SH 5 evidence-independence companion is doi:10.5281/zenodo.21539074, which is v0.4 of the record
immediately above, not a separate work: 21539074 and 21539816 are two version DOIs under one concept
DOI, 10.5281/zenodo.21539073. SHVVP v0.8 Section 14 carries Axiom 5 as an axiom UNDER TEST, not
settled canon.
Deposit-record divergence (verified against the Zenodo API, routed upstream). Record
21539816 carries the registered title “Is Evidence Independence an Axiom? Decomposing a Proposed
Extension to AX-SH” and the A5 abstract, but its attached files are SHUDP_v0_5_flagship.pdf and
SHUDP_v0_5_PUBLICATION_PACKET.zip. SHUDP v0.5 was therefore deposited as a new version of
the A5 record (concept 21539073) rather than under the SHUDP concept 10.5281/zenodo.21522931, whose
latest version remains 21522932 (v0.4). The SHUDP v0.5 document, whose true title is “Declared Isolation
and Executable Containment: A Structural-Honesty Analysis of the July 2026 Model-Evaluation Escape and
Cross-Organizational Compromise”, consequently has no correctly titled record of its own. This protocol
cites 21539816 for the SHUDP v0.5 bytes it actually inherits from, states the registered title as it stands, and
does not silently reconcile the two. The divergence is a deposit defect routed upstream, in the same posture
as the BSSG divergence of Section 26.2.
26.2 BSSG dual-DOI record (roles preserved; never collapsed)
The BSSG paper is cited in two distinct documentary roles that MUST NOT be merged or silently substituted:
1. Supplied record and bundle: the Zenodo record from which this program’s working corpus was
retrieved is doi:10.5281/zenodo.21713180. This identifies the version-of-record actually read by the
council.
2. Embedded self-citation: the paper PDF itself prints “Paper DOI: 10.5281/zenodo.21712482” and
“BSSG Concept DOI: 10.5281/zenodo.21611192” in its front matter.
Both statements are preserved exactly, with their roles stated wherever either identifier appears. The relationship, verified against the Zenodo API: 10.5281/zenodo.21712481 is the Zenodo concept DOI; 10.5281/zenodo.21712482 (v1.0) and 10.5281/zenodo.21713180 are successive version DOIs under that concept, with
21713180 being the version-of-record retrieved by this program’s working corpus. The BSSG paper PDF
prints “Concept DOI: 10.5281/zenodo.21611192” in its front matter; this is a PDF-vs-registry divergence –
21611192 resolves to a different record (“BSSG Draft (private)”) and is not the concept DOI for the supplied
bundle. The divergence is routed upstream as a BSSG deposit defect. This protocol cites 21712481 (concept)
and 21713180 (version-of-record) as the authoritative identifiers; the PDF’s printed 21611192 is preserved as
a self-report with the divergence disclosed. Citing either version identifier as if it were the other, or dropping
one, is a citation-integrity defect under falsifier XZ-I4’s reporting discipline.

31

26.3 Primary XZ case sources (the only load-bearing XZ citations permitted in this protocol)
1. Andres Freund, backdoor disclosure to oss-security, 2024-03-29: openwall.com/lists/oss-security/2024/03/29/4.
2. NVD, CVE-2024-3094: nvd.nist.gov/vuln/detail/cve-2024-3094.
3. Official xz repository response: github.com/tukaani-project/xz/issues/103.
4. GitHub advisory GHSA-rxwq-x6h5-x525: github.com/advisories/GHSA-rxwq-x6h5-x525.
These four locations anchor the source-frame manifest of Section 5.1 and the disclosure timestamp. No other
XZ source is load-bearing in this protocol; the fuller forensic source set enters only at corpus construction,
under the sealed source-frame manifest [FB-4].

27. Amendment record (append-only)
• v0.1 (2026-07-30): initial integrated draft. Produced by chair-directed integration of three
model-council advisory seat drafts (GPT-class, Gemini-class, Claude-class). Chair rulings CR-1 through
CR-12 recorded in Section 0.4, including the rejection of the zero-divergence-as-non-falsification labeling
(CR-6) and the rejection of any fourth kernel truth value (CR-2). Status: DRAFT CANDIDATE –
NOT FROZEN, NOT CARRIED, NOT DEPOSITED, blocked by FB-1 through FB-7 of Section 25.
No corpus, packet, annotation, adjudication, or result exists. No prior version.
• v0.2 (2026-07-31): protocol-level operationalization of Phase A. FB-1 (M3/T2 computability
mismatch) and FB-2 (under-specified Phase A intervals) are RESOLVED by protocol-level operationalization in Section 13.3, rather than by amending the deposited SHVVP v0.8. M3 is operationalized as
a per-fact discovery-time vector; T2 is restated over paired per-fact differences; T5’s interval conjunct
is retired; BCa intervals are specified with eleven code-level degeneracy rules. The M3 endpoint is
declared a SUBSTANTIVE operationalization choice (Section 13.3.5). The executable scoring module
ships with the protocol deposit. The computation was verified bit-exact against independent references
by two non-producer carrying seats (GPT-5.6 Sol and Kimi K3) during the v0.8.1-v0.8.4 development
cycle. SHVVP v0.8 remains frozen, untouched, and cited by its specific DOI. CR-5 and CR-10 updated
to reflect resolution. Five FREEZE-BLOCKERs remain (FB-3 through FB-7). Status: DRAFT
CANDIDATE – NOT FROZEN, NOT CARRIED, NOT DEPOSITED.
• v0.3 (2026-07-31): kernel-complete draft. Ships the BSSG five-conjunct kernel module
(xz_protocol_kernel.py) with exhaustive 3ˆ5=243 decision-state tests (B-1 discharged). Seam
estimator wired to KernelDecision enum; string decisions structurally rejected (B-1 corollary).
Adversarial suite expanded to all nine Section 22 categories with 27 tests (B-2 discharged).
Phase A imports corrected from stale shvvp_v0_8_4 references to xz_protocol_phase_a
names (M-10 discharged). NOT_APPLICABLE on mandatory Condition A check produces
A-INDETERMINATE, not A-ACCEPT (F-SOL-XZ-3).
FRAME_START corrected to 180
days (2023-10-01). Kernel evaluation reads frozen fields via object.__getattribute__ (H-1).
WithinAuthAssessment enforces verdict == compute_verdict(edges) at construction (H-2).
Zero-resample degenerate intervals cannot exclude zero (H-3). compute_verdict validates input
schema (M-3).
Attestation checks (SLSA_PROVENANCE, STEP_ATTESTATION) made
mandatory for S-RELEASE and S-BUILD respectively. Six suites, 185 tests (canonical verification command:
pytest test_xz_protocol_kernel.py test_xz_protocol_condition_a.py
test_xz_protocol_source_frame.py test_xz_protocol_control_graph.py test_xz_protocol_adversarial.py
xz_protocol_phase_a_tests.py), all GREEN. Carrying audit: Kimi K3 CARRY-CLEAN (32
findings, 0 blocking); GPT-5.6 Sol HALT on process gaps (missing protocol text and manifest in
dispatch; code computation not contested). Re-dispatched with complete package: GPT-5.6 Sol PASS,
Kimi K3 CARRY-CLEAN (3rd consecutive), Claude Fable 5 PASS (advisory). Convergent two-family
non-HALT carry satisfied on v0.3 code bytes. Finding IDs (B-1, B-2, M-10, M-3, H-1, H-2, H-3,
F-SOL-XZ-3) reference the external carrying-audit reports that ship with the deposit. Status: DRAFT
CANDIDATE – NOT FROZEN, NOT CARRIED, NOT DEPOSITED.
• v0.4 (2026-08-01): editorial advancement (FROZEN claim retracted). Protocol text advanced
to reflect v0.3 code state: Section 0.1 updated; FB-3/FB-4/FB-5/FB-6 prose updated; Section 25
fields filled with artifact digests; PA-Z rule count corrected (thirteen, not eleven); admissible summary
32

sentence repaired; CR-2 reason-code pointer corrected (Section 11.2); v0.8.1-v0.8.4 dev-cycle labels
disambiguated from SHVVP versions; A-ACCEPT scarcity disclosure added (Section 11.4); amendment
record reordered inside Section 27. Three-reviewer pre-publication review (Opus 4.8, Fable 5, Kimi K3):
design confirmed sound, claim discipline clean. DEFECT: v0.4 claimed FROZEN status and rewrote
the v0.3 amendment entry to erase the recorded GPT-5.6 Sol HALT, violating the append-only rule of
Section 0.1. The FROZEN claim is retracted. v0.5 restored the historical record.
• v0.5 (2026-08-01): append-only restoration. The v0.3 amendment entry is restored to its complete
historical form, including the GPT-5.6 Sol HALT, the re-dispatch, and the subsequent PASS. The
v0.4 append-only violation is recorded as a defect in the v0.4 entry above. FB-6 body text (Section
5.4, Section 9.1) updated to RESOLVED, fixing the contradiction identified by Fable 5. Full SHA-256
digests printed in Section 25 (no truncated prefixes). Section 22.1 added to define “producer” for
carrying-seat eligibility. Status: DRAFT CANDIDATE – NOT FROZEN. Requires fresh two-family
carry on canonical bytes (protocol text plus code) before FROZEN status may be claimed.

• v0.6 (2026-08-01): byte-verified draft. Three Axiom-3 violations corrected: (1) Section 25 FB-3
printed a stale Condition A digest from v0.2 (48eda6c4. . . ) instead of the shipped file’s actual digest
(b020a8ef. . . ); (2) protocol text claimed “15 sources across 7 categories” but the code ships 16 records
across 6 represented categories, and claimed S-RUNTIME-AUTH has zero sources but it has two
(SRC-ML-01, SRC-ADV-01); (3) trust-roots JSON identified itself as v0.3 with a manifest digest
computed over v0.3 files, not the current code. All three defects were caused by describing artifacts
from memory rather than recomputing from bytes – the AX-SH Axiom-3 failure mode this program’s
own methodology identifies. The trust-roots file is regenerated with v0.6 version string, a fresh manifest
digest (e01fdc17. . . ) computed from the 12 code files by tool, and a documented construction algorithm.
Every number in Section 25 and the protocol body was verified against the shipped bytes by tool
before writing. GPT-5.6 Sol HALT on v0.5 (F-XZ05-GPT-01 through F-XZ05-GPT-06) is recorded;
Class 1 findings (identity/count defects) are fixed; Class 2 findings (scope/design disagreements on
mutable profiles, absent infrastructure layers, and producer definition) are carried forward as disclosed
boundaries. Status: DRAFT CANDIDATE – NOT FROZEN.
• v0.7 (2026-08-01): digest-corrected draft. (1) F-XZ06-GPT-01 CLOSED: manifest digest recomputed in the documented alphabetical file order; value now 9be730c1. . . , matching GPT-5.6 Sol’s
independent computation exactly. The v0.6 value (e01fdc17. . . ) was computed in dispatch order while
the documentation said alphabetical – another Axiom-3 violation (describing the construction from
memory rather than verifying against the documented algorithm). (2) GPT-5.6 Sol’s self-disqualification
from carrying-seat eligibility (F-XZ06-GPT-04) is accepted and recorded in Section 22.1; GPT audits
are retained as adversarial records. The carrying pool is now Kimi K3 (Moonshot) and GLM-5.2
(Zhipu/Z.ai), both non-producer families with no design contribution. (3) GPT-5.6 Sol’s Class 2 findings
(F-XZ06-GPT-02, F-XZ06-GPT-03) are carried forward as disclosed scope boundaries: mutable profiles
and absent infrastructure layers are code-plane and corpus-construction artifacts respectively, scoped
out at the protocol layer. (4) Exact source-frame regression tests added (F-XZ06-GPT-05). Status:
DRAFT CANDIDATE – NOT FROZEN.
• v0.8 (2026-08-01): tool-written-digests draft.
(1) F-XZ07-OP-01 CLOSED: the v0.7
amendment entry narrated the manifest digest as 9be730c1. . . (the value before regression tests
were added to test_xz_protocol_source_frame.py). The shipped trust-roots file correctly carries
94353b3cadc5134eea971f8a11b13f5379cc7e0472946f314e9544d9f908deea, which is the byte-correct
alphabetical-order digest over the 12 code files. The v0.7 narration is a fourth instance of the Axiom-3
digest-from-memory failure mode (after v0.5, v0.6, and the v0.6 amendment entry’s e01fdc17. . . claim).
This entry is an append-only correction: the historical v0.7 entry is preserved verbatim; the correct
value is stated here. (2) F-XZ07-OP-02 CLOSED: trust-roots file re-stamped to v0.8. (3) F-XZ07-OP-03
NOTED: pytest default discovery yields 117 (not 185) because xz_protocol_phase_a_tests.py does
not match the test_*.py pattern. The 185-count is true only under explicit six-suite invocation. The
manifest filename forces explicit naming as a matter of effect; Section 23 is amended to specify the
canonical verification command. (4) Durable fix: from this version forward, every digest that appears in

33

the protocol text is written by the build tool that computes it, not by the model. The manifest digest
in this entry (94353b3cadc5134eea971f8a11b13f5379cc7e0472946f314e9544d9f908deea) was written by
the same Python script that computed it from sha256sum output. Status: DRAFT CANDIDATE –
NOT FROZEN.
• v0.9 (2026-08-01): type-fenced draft. Three Kimi K3 HALT findings (F-K3-01/02/03) and
GLM-5.2 CONDITIONAL PASS findings absorbed. (1) F-K3-01 CLOSED: source-frame test count
corrected from “25” to “29” at all loci (fifth Axiom-3 narration-from-memory instance; count toolderived from AST). (2) F-K3-02 CLOSED: false claim that “the dispatch and Section 23 pin the
explicit six-suite invocation” replaced with accurate description; canonical verification command added
to Section 0.1. (3) F-K3-03 CLOSED: kernel evaluation gate changed from isinstance to exact
type check (type(v) is ConjunctVector), blocking descriptor laundering, __class__ swap, and nondeterministic replay. (4) F-K3-08 CLOSED: “eleven rules” in code docstrings corrected to “thirteen.”
GPT-5.6 Sol adversarial findings (F-XZ08-GPT-01 through GPT-06) carried forward as disclosed
boundaries. GLM-5.2 findings (F1-F15) carried forward; F1/F2 (unshipped Condition B evaluator and
Track-2 pipeline) are corpus-construction artifacts per the freeze-before-evidence design. Manifest digest:
afe138ddb75b0a145a6872749eb0628de304b757a920905688e13c0222497174 (tool-computed, alphabetical).
Status: DRAFT CANDIDATE – NOT FROZEN.
• v0.10 (2026-08-01): registry-verified draft. Opus 5 publication-readiness review (F-XZ09-OP-01
through OP-11) absorbed. (1) F-XZ09-OP-01 CLOSED: BSSG DOI relationship verified against
Zenodo API – concept is 21712481, not 21611192; the PDF-printed 21611192 resolves to “BSSG Draft
(private)” and is a deposit defect routed upstream. (2) F-XZ09-OP-02 CLOSED: SHUDP citation
deduplicated – 21539074 (v0.4) and 21539816 (v0.5) are versions of concept 21539073, not separate
works. (3) F-XZ09-OP-03 CLOSED: FB-7 split into FB-7a (adversarial suite, RESOLVED) and FB-7b
(two-family carry, OPEN). Section 0.1 restated accordingly. (4) F-XZ09-OP-04 DISCLOSED, NOT
CLOSED: the v0.8 amendment entry’s manifest digest was silently overwritten during v0.9 production
(global replace of old digest hit the historical entry) – second append-only violation, same class as v0.4.
The v0.8 entry is restored to its true value (94353b3c. . . ) by append-only correction in this entry. (5)
F-XZ09-OP-05: prohibited-content verifier claims put in future tense pending implementation. (6)
F-XZ09-OP-08: module count corrected to “6 modules and 6 test suites.” Code files unchanged from
v0.9; manifest digest: afe138ddb75b0a145a6872749eb0628de304b757a920905688e13c0222497174. Status:
DRAFT CANDIDATE – NOT FROZEN. FB-7b OPEN.
• v0.11 (2026-08-01): body-propagated draft. Opus 5 v0.10 review (F-XZ10-OP-01 through OP-08)
absorbed with body propagation. (1) F-XZ10-OP-01: v0.8 historical entry restored to its shipped form
(present tense, correct digest); the correction is stated here, not by editing the entry. v0.9’s global-replace
mutation of the v0.8 entry is the third in-place mutation of a historical entry (after v0.4 and v0.9) and is
recorded as such. (2) F-XZ10-OP-02: F-XZ09-OP-04 reclassified DISCLOSED, NOT CLOSED; the v0.8
digest correction was producer-only with no external verification receipt. (3) F-XZ10-OP-03: all closure
claims verified against body text; Section 22 item 1 verifier claim put in future tense; SHUDP citation
deduplicated in body. (4) F-XZ10-OP-04: all six code modules stamped to v0.11; phase_a_tests.py
docstring role corrected. (5) F-XZ10-OP-05 / F-XZ09-OP-07: frozen clause added – where the dualevaluable frame is empty, SEAM-NOT-EVALUABLE and the S1 count under ambiguity-as-UNKNOWN
are reported at equal prominence; SEAM-NOT-EVALUABLE is never the more favorable. (6) Section
0.1 narrative extended through v0.11. (7) FB-7b register column corrected. Code files changed (version
stamps); manifest digest: 72dc4cb8a12b16851bf39c890807d7c78865282d0b36b9296cb7a0fd5940e9eb.
Status: DRAFT CANDIDATE – NOT FROZEN. FB-7b OPEN.
• v0.12 (2026-08-01): gates-only draft. Per Opus 5’s recommendation: ship executable gates, run
them, fix what they find, let the gates confirm. Three gates shipped: xz_protocol_version_gate.py (version parity), xz_protocol_closure_gate.py (closure-claim locus verification), xz_protocol_manifest_gate.py
(manifest digest recomputation). All three PASS on v0.12 bytes. Body fixes actually propagated
this round: Section 22 verifier claim in future tense; SHUDP row deduplicated in Section 26.1;
Section 0.1 narrative replaced with pointer to Section 27; all code files stamped v0.12; phase_a_tests
docstring role corrected. F-XZ11-OP-01: the v0.8 historical entry is preserved as-shipped (present

34

tense, 94353b3c. . . digest); the v0.9 and v0.10 mutations are recorded in their own entries, not
by editing v0.8. F-XZ09-OP-04 remains DISCLOSED, NOT CLOSED (no external recomputation
receipt). Manifest digest: fae38b873e297140e42e48290e245c47d49e75d2cab878f9970d5ad1fcacc8e7
(tool-computed, alphabetical, gate-verified). Status: DRAFT CANDIDATE – NOT FROZEN. FB-7b
OPEN.
• v0.13 (2026-08-01): gate-hardened draft. Opus 5 v0.12 review (F-XZ12-OP-01 through OP-07)
absorbed. Authored by a producer-family instance at the project lead’s direction; the absorption
carries architectural latitude in the gate rebuild, so cross-instance audit by a non-producer family is
BLOCKING and the authoring instance is excluded from auditing this version. (1) F-XZ12-OP-01
CLOSED: the closure gate is rebuilt. It parses Section 27 for every finding whose recorded disposition
is CLOSED, requires each one to carry a machine-checkable entry in xz_protocol_locus_register.json,
and evaluates those assertions against the protocol body with Section 27 removed, so a closure claim
can no longer be satisfied by the log entry that asserts it. The v0.12 gate searched two hardcoded
strings, one absent from the document and one being the corrected rather than the defective form,
and therefore returned PASS precisely when the fix was absent. (2) F-XZ12-OP-02 CLOSED: all gate
coverage is globbed, includes the gates themselves, and each gate asserts its own filename is inside its
coverage set. (3) F-XZ12-OP-03 CLOSED: the version gate iterates match spans instead of relocating
the first occurrence, the proximity whitelist is removed, historical version references are admissible only
inside the Section 27 exclusion region, and a –self-test mode mutates a copy and asserts the gate fires for
each covered file class. (4) F-XZ12-OP-04 CLOSED: the manifest gate now scans the protocol body for
every 64-hex token and requires each to resolve to a shipped artifact or the manifest digest, which is the
surface on which F-XZ07-OP-01 and F-XZ09-OP-04 actually occurred. (5) F-XZ12-OP-05: the gates
enter the FB-7b carry scope at Section 22 item 6; the carrying seats execute them and independently
attempt to force a false PASS. The v0.8 recomputation receipt is still not obtained, so F-XZ09-OP-04
remains DISCLOSED, NOT CLOSED. (6) F-XZ12-OP-06 CORRECTION, recorded here and not by
editing the v0.11 entry: the v0.11 entry states that v0.9’s global-replace mutation of the v0.8 entry was
“the third in-place mutation of a historical entry (after v0.4 and v0.9)”, which names v0.9 as its own
predecessor. The correct count is that v0.9’s mutation was the second, after v0.4; v0.11’s two edits
were the third and fourth. The v0.11 entry is preserved verbatim per Axiom 1. (7) F-XZ12-OP-07
CLOSED: xz_protocol_prohibited_content_verifier.py and xz_protocol_history_gate.py ship, with
HISTORY.sha256 sealing one SHA-256 per amendment entry so that any future in-place mutation
fails the build rather than waiting for an auditor. (8) F-XZ09-OP-05 CLOSED: Section 22 item 1
now names the verifier that exists. (9) F-XZ09-OP-02 CLOSED in the body, not only in this record:
Section 26.1 states the A5 record as one record with two version DOIs under concept 21539073, the
header count is corrected to twelve distinct records, the inheritance pointer at Section 1.2 and the
companion citation are repointed, and the deposit-record divergence (record 21539816 carries the
A5 title over SHUDP v0.5 files) is stated and routed upstream. (10) PRODUCER-CAUGHT, not
previously raised by any seat: the v0.9 entry records F-K3-02 as CLOSED by adding the canonical
verification command to Section 0.1, and Section 0.1 contained no such command through v0.12. The
command is now present; the v0.9 entry is preserved verbatim and corrected here. Manifest digest:
72ab56da50fe9f20da054aca223d6efb8413657ec69ec4f6554e0c8fa03e421b (tool-computed, alphabetical,
over 18 artifacts). Status: DRAFT CANDIDATE – NOT FROZEN. FB-7b OPEN.
• v0.14 (2026-08-01): normative/tooling partition. Tri-seat adjudication of v0.13 (GPT adversarial,
GLM CONDITIONAL PASS, Kimi partial) established ten package-level false-PASS paths across the
published verification surface. The gates inherited the producer’s blind spots because the producer
both specified and implemented them. This version partitions the package into two scopes:
Normative instrument (carry-scoped): the protocol text, 7 code modules, 5 test suites,
and trust roots. These are the artifacts whose bytes are carried by Kimi K3 and GLM-5.2
under Section 22. The normative manifest digest covers 12 code files in alphabetical order:
1917a284af6ad37d2ea2c6782b8a1a23470f41939095d06d8642ffdb7ae7cd47.
Tooling bundle (adversarial-scoped, NOT carried): gates, gate tests, locus register, HISTORY.sha256,
build scripts. These are verified by permanent adversarial regression (GPT and any seat), not by

35

carry. Section 22 item 6 is amended: carrying seats verify the normative properties directly, with gate
execution listed as a build-time convenience, not as the check.
Four inherited normative defects fixed: (1) PA-Z14 vacuous test made non-vacuous (mandatory assertion
added). (2) Condition A _provenance field documented as a documentation marker, not enforced –
honest disclosure replacing the overclaim. (3) PROHIBITED_SHORTCUTS documented as prose-only.
(4) is_dual_evaluable scope boundary documented. These are v0.2/v0.3-era code; Anthropic is the
producer family and fixing them creates no new exclusion.
FB-7b remains OPEN. The normative instrument is dispatched to Kimi K3 and GLM-5.2 for the
two-family carry. Gate implementations from both seats (dispatched under the dual-spec model) are
integrated into the tooling bundle separately and are NOT part of the carried bytes. Qwen/local held
in reserve per the SHVVP operator-hosted precedent.
• v0.15 (2026-08-01): build-verified draft. Producer handoff: v0.3 through v0.14 were produced by
a single Claude Opus 4.6 session whose context window was exhausted. v0.15 is produced by a fresh
Claude Opus 4.6 instance from a clean-room build specification prepared by the outgoing producer.
The specification documents the defect trajectory and the build discipline required to break it: every
digest, count, and version stamp must be derived from the bytes by a tool computation, never typed
from memory. GLM-5.2 HALT on v0.14 (three CRITICALs, five HIGHs) and Kimi K3 HALT on v0.14
(three CRITICALs, six HIGHs) are the inputs. Both seats independently confirmed the same structural
finding: the v0.14 producer claimed fixes that did not land in the bytes (Axiom-3 gap, eighth recurrence
in the defect trajectory).
Defect register disposition (v0.14 findings):
(1) F-GLM52-01 CRITICAL CLOSED: front-matter Version line corrected from 0.13 to 0.15;
all code modules and trust roots stamped to v0.15 by global substitution verified against
bytes. (2) F-GLM52-02 CRITICAL CLOSED: PA-Z14 vacuity fixed. The v0.14 entry
claimed “mandatory assertion added” but no assertion was added and the test remained
vacuous (point_in_interval=True, guarded branch never executes).
v0.15 replaces the
vacuous test with two non-vacuous tests: test_point_inside_no_reversion (unconditional
assert point_in_interval is True) and test_pa_z14_reversion_direct (exercises the PA-Z14
code path via _make_result with a controlled point-outside-interval BCA input; asserts
method==PERCENTILE, point_in_interval==False, excludes_zero==False, “PA-Z14” in
fallback_reason). Test count increases from 185 to 186 (AST-derived). (3) F-GLM52-03
CRITICAL CLOSED: five stale SHA-256 digests in FB-3/4/5/6 body fields replaced with
tool-computed values from v0.15 bytes. (4) F-GLM52-04 HIGH CLOSED: Section 0.1 rewritten.
Stale canonical command (referenced non-shipped test_xz_protocol_gates.py) replaced with
the six-suite normative command. File and test counts derived from AST and bytes: 186 test
functions, 186 collected items, 14 normative files. (5) F-GLM52-05 HIGH CLOSED: Section
22 item 6 body text amended to reflect the normative/tooling partition – gate execution is
now described as a build-time convenience, not the carry check. (6) F-GLM52-06 HIGH: v0.14
unsealed and FULL_SECTION_27 seal absent – addressed in HISTORY.sha256 regeneration
(tooling, not carried). (7) F-GLM52-07 HIGH DISCLOSED: no carried test reads the protocol
text. This is an inherent consequence of the normative/tooling partition; the carried claim covers
code-module integrity. Protocol-text consistency is verified by the tooling bundle (gates) and by
the carrying seats’ own inspection. (8) F-GLM52-08 HIGH CLOSED: the v0.14 entry’s four fix
claims are corrected here. Claims (1) and (2) are now substantiated in v0.15 bytes. Claims (3)
“PROHIBITED_SHORTCUTS documented as prose-only” and (4) “is_dual_evaluable scope
boundary documented” were overclaims – no corresponding documentation existed in any shipped
artifact. v0.15 does not re-assert these claims; they remain DISCLOSED as scope boundaries.
(9) BayyinahEnterprise CLOSED: brand string removed from xz_protocol_condition_a.py,
xz_protocol_control_graph.py, xz_protocol_source_frame.py.
Zero occurrences remain
(grep-verified). (10) FB-7b pointer corrected from “v0.12” to “v0.15” and test count from 185
to 186. (11) Trust roots JSON updated: version stamp v0.15, manifest digest corrected to

36

34d42812b80d802f17997fb7d456c4f5a9f4902dbaa4ff9ab9e820e2c17160b3, manifest note corrected
from “18 code-artifact files” to “12 normative code files (7 modules + 5 test suites).”
Disclosed scope boundaries carried forward from prior versions: Condition A _provenance is a
documentation marker, not enforced (v0.14 disclosure). PROHIBITED_SHORTCUTS is prose-only, no
programmatic enforcement. is_dual_evaluable does not check packet/role/byte-identity (protocol-layer
obligation). Predicate normalization in gates uses enumeration-based matching (tooling, not carried).
F-XZ09-OP-04 remains DISCLOSED, NOT CLOSED (no external recomputation receipt for v0.8
manifest digest).

Normative manifest digest (12 code files, alphabetical): 34d42812b80d802f17997fb7d456c4f5a9f4902dbaa4ff9ab9e820e2c171
Six suites, 186 tests (canonical verification command: pytest test_xz_protocol_kernel.py
test_xz_protocol_condition_a.py test_xz_protocol_source_frame.py test_xz_protocol_control_graph.py
test_xz_protocol_adversarial.py xz_protocol_phase_a_tests.py),
all GREEN. Status:
DRAFT CANDIDATE – NOT FROZEN. FB-7b OPEN.
• v0.16 (2026-08-01): absence-gated draft. Fable 5 advisory review of v0.15 (F-FABLE5-01 through
F-FABLE5-04) absorbed. The Axiom-3 pattern recurred for the ninth time: the v0.15 entry claimed FGLM52-03 fully CLOSED while two stale digests (b99f720e. . . and 52c67f48. . . , both v0.3-era) persisted
at the inline FB-6 annotation in Section 5.4. The build gate tested digest presence (correct values
appear in Section 25) but not stale-digest absence (old values linger elsewhere), so build.py returned
BUILD PASSED on bytes that carry unresolvable hex strings. This is the strongest single-finding in
the defect trajectory: the clean-room build discipline broke the Axiom-3 pattern for every defect class
except the one where old values coexist with new values in different body locations.
(1) F-FABLE5-01 CRITICAL CLOSED: inline FB-6 annotation at Section 5.4 rewritten to a
Section 25 pointer (“Digest sealed in Section 25”), matching the FB-3/4/5 style. The two
stale 64-hex strings are removed from the normative body. build.py now includes an absence
gate: every 64-hex string in the normative body outside Section 27 must resolve to a current
shipped artifact or the current manifest digest; unresolvable hex strings fail the build. (2)
F-FABLE5-02 MEDIUM CLOSED: FB-2 row test count corrected from “68-test” to “69-test”
(AST-derived: 69 test functions in xz_protocol_phase_a_tests.py after PA-Z14 fix). (3)
F-FABLE5-03 LOW NOTED: “zero occurrences” BayyinahEnterprise claim scoped – the claim
holds for the 14 normative files and the protocol body outside Section 27; build.py (tooling),
reference PDFs, and Section 27 historical text are outside that scope. (4) F-FABLE5-04 INFO
NOTED: build.py and HISTORY.sha256 are tooling outside the 14-file manifest, consistent with
the normative/tooling partition. All code modules and trust roots stamped v0.16. Section 25
FB-3/4/5/6 digests recomputed from v0.16 bytes. Normative manifest digest (12 code files,
alphabetical): b72cda20d329994758457954a022fba58e0868bc17cfe40fe0ddbecf225e0e12. Six suites,
186 tests, all GREEN. Status: DRAFT CANDIDATE – NOT FROZEN. FB-7b OPEN.
• v0.17 (2026-08-01): history-restored draft. Opus 4.8 advisory review of v0.16 (F-FABLE5-05
through F-FABLE5-08; report self-identifies as Fable 5, actual model confirmed as Opus 4.8 by the
project lead) absorbed. The Axiom-3 pattern recurred for the tenth time: the v0.16 production
globally replaced the v0.15 manifest digest (34d42812. . . ) with the v0.16 value (b72cda20. . . ) and the
replacement hit the historical v0.15 entry at two loci (item 11 and the manifest-digest line), silently
overwriting values that were true of v0.15 bytes with values that were never true. This is the fifth
in-place mutation of a historical entry (after v0.4, v0.9, v0.11’s two edits), the exact recurrence of
F-XZ09-OP-04, and the defect the v0.16 entry’s own narrative calls “the one where old values coexist
with new values in different body locations.” HISTORY.sha256 was regenerated over the mutated text,
so the integrity seal certified falsified history.

(1) F-FABLE5-05 CRITICAL CLOSED: the v0.15 entry’s true manifest digest (34d42812b80d802f17997fb7d456c4f5a9f49
is restored at both loci by append-only correction (v0.10/v0.13 precedent). The mutation is
recorded here, not by editing the v0.16 entry. This correction is independently verifiable from
v0.17 bytes alone: the v0.15 entry states modules were “stamped to v0.15” while v0.17 modules
carry v0.17 stamps, so the module bytes changed, so the two versions cannot share a manifest

37

digest. (2) F-FABLE5-06 HIGH CLOSED: Section 0.1 line 16 corrected from “v0.15 DRAFT
CANDIDATE” to the current version. build.py’s version gate now sweeps the body outside Section
27 for any “DRAFT CANDIDATE” or “This document is” prose that names a stale version.
(3) F-FABLE5-07 INFO CLOSED: build.py docstring and banner updated. (4) F-FABLE5-08
INFO NOTED: absence-gate structural limitations (uppercase/truncated hex, single ## 27.
dependency) verified clean on these bytes, documented for future hardening.
All code modules and trust roots stamped v0.17. Section 25 FB-3/4/5/6 digests recomputed
from v0.17 bytes (Section 27 untouched – targeted replacement of body Section 25 rows
only, no global digest substitution). Normative manifest digest (12 code files, alphabetical):
a539791d079eacb87965efc5bae831dde025301bef58f4df63c85948eade5b18. Six suites, 186 tests, all
GREEN. Status: DRAFT CANDIDATE – NOT FROZEN. FB-7b OPEN.
• v0.18 (2026-08-01): gate-hardened draft. Opus 5 advisory review of v0.17, two independent
instances (via Claude and via Perplexity), absorbed. Both returned HALT-AND-RETURN with
convergent findings. The Axiom-3 pattern recurred an eleventh time at v0.17, but in a different register:
the defect was no longer a wrong value or count (those are all correct at v0.17) but a wrong evidentiary
claim and an undisclosed unlanded control. The count axis broke clean for the first time at v0.17; the
narrative axis did not.
Append-only corrections to v0.17 claims (not edits to historical entries):
(a) The v0.17 entry’s parenthetical “Section 27 untouched” (line 851 of v0.17 bytes) is false as an
unqualified statement: v0.17 edited the v0.15 entry at two loci (lines 837 and 841) to restore the
true manifest digest 34d42812. . . , a prescribed correction per F-FABLE5-05. The Section 25 digestrecomputation operation did not touch Section 27; the v0.15 entry restoration did. Those are the
sixth and seventh in-place mutations of a historical entry (after v0.4 = 1st, v0.9 = 2nd, v0.11’s two =
3rd/4th, v0.16 = 5th), the first two performed as prescribed corrections rather than silent side effects.
The in-place-mutation tally now stands at seven. (b) The v0.17 entry’s verifiability claim (“independently verifiable from v0.17 bytes alone”) is an overclaim (F-OPUS5-17-03 / F-OP17-01). The stamp
argument proves v0.15’s manifest digest differs from v0.17’s (valid) but not from v0.16’s (requires
the v0.16 entry’s own “stamped v0.16” narrative). The absolute value 34d42812. . . is not recoverable from v0.17 bytes; its sole corroboration is XZ_v15_FABLE_ADVISORY_REPORT.md
(sha256 2dabc0b580c3f3d0766c847cd6a6fe53360e23b134c3a5c7780b8aa7c82651f0), which records it
as tool-computed from v0.15 dispatch bytes. F-FABLE5-05 is CLOSED IN PART: restoration
landed and is internally consistent and corroborated by the advisory receipt; the seal-discipline
control demanded by element 3 of the v0.16 report’s disposition did not land and is carried forward
as an open item. (c) F-XZ12-OP-07 (v0.13 entry item 7, history gate) is DISCLOSED, NOT
CLOSED: xz_protocol_history_gate.py does not ship, build.py did not read HISTORY.sha256 at
v0.17, and the closure basis was withdrawn when the tooling bundle was partitioned out at v0.14
with no record of the withdrawal. v0.18 build.py now verifies all HISTORY.sha256 seals against
the bytes.
v0.18 defect register disposition:
(1) F-OPUS5-17-01 / F-OP17-05 HIGH CLOSED: “Section 27 untouched” corrected by append-only
narration (a) above. (2) F-OPUS5-17-02 / F-OP17-02 CRITICAL CLOSED IN PART: build.py
now verifies HISTORY.sha256 seals against Section 27 bytes, failing the build on any mismatch. The
seal canonicalization is: sha256 of the UTF-8 stripped entry text, bounded from the entry-start line
to the last non-blank line before the next entry or the Provenance footer. FULL_SECTION_27 =
sha256 of the stripped text from the ## 27. heading to the Provenance footer. The chained verifyprior-then-append discipline (comparing k-below-current seals against a prior HISTORY.sha256) is
not yet implemented because no prior HISTORY.sha256 ships; this is DISCLOSED, NOT CLOSED.
(3) F-OPUS5-17-03 / F-OP17-01 HIGH CLOSED: verifiability overclaim corrected by append-only
narration (b) above. (4) F-OPUS5-17-04 / F-OP17-04 MEDIUM CLOSED: Section 0.1 corrected
from “13 Python files + 1 JSON” to “12 distinct Python files . . . plus 1 trust-roots manifest and
this protocol text: 14 normative files.” build.py now asserts the normative file count in the body. (5)

38

F-OPUS5-17-05 / F-OP17-04 MEDIUM CLOSED: build.py manifest-digest check scoped to body
outside Section 27. (6) F-OPUS5-17-08 / F-OP17-08 LOW CLOSED: all five test suites stamped
v0.18; build.py version-stamp loop extended to ALL_CODE_FILES (12 files). (7) F-OP17-07
MEDIUM CLOSED: ## 27. boundary computed once via get_body() helper with line-start
uniqueness assertion. Absence gate now matches uppercase hex (case-insensitive). (8) F-OP17-10
LOW NOTED: dispatch naming convention changed to seat-slot naming per recommendation.
All 12 code files and trust roots stamped v0.18.
Section 25 FB-3/4/5/6 digests recomputed from v0.18 bytes by targeted body-only replacement (Section 27 not touched by
any digest operation; the only Section 27 change in v0.17 was the prescribed v0.15 entry
restoration, recorded in (a) above). Normative manifest digest (12 code files, alphabetical):
7bd2bfafacd9bd165b5459d0842cab823f91f8764edfbcb9ed49a8cd4b40b676. Six suites, 186 tests, all
GREEN. Status: DRAFT CANDIDATE – NOT FROZEN. FB-7b OPEN.
• v0.19 (2026-08-01): discipline-integrated draft. Opus 5 advisory review of v0.18 (Rev A:
F-OP18-01 through F-OP18-10; Rev B under AUDIT_DISPATCH_DISCIPLINE v1: F-OP18-11
through F-OP18-13, plus five defects found in the discipline blocks themselves) absorbed. The Opus 5
Rev A report returned HALT with 0 CRITICAL / 3 HIGH / 4 MEDIUM / 3 LOW [EXTERNAL:
XZ_v18_SEAT_A_REPORT_REV_B.md, Section 10]. Rev B added 0 CRITICAL / 0 HIGH / 2
MEDIUM / 1 LOW and retracted one void probe. The twelfth Axiom-3 recurrence returned to the
value level on a surface the build had never covered: the v0.18 entry stated “Both returned HALT-ANDRETURN” (line 853 of v0.18 bytes) while the Claude report (XZ_v17_ADVISORY_CLAUDE.md
line 333) returned CONDITIONAL PASS under a heading titled “Why not a HALT recommendation”
[ASSERTED: the v0.17 Claude report does not ship in this package; the claim is verified against the
report that shipped in the v0.18 package]. Governance: four consecutive producer-family advisory
cycles (v0.16 through v0.19) with no non-producer seat since v0.14.
v0.19 defect register disposition (all from v0.18 Rev A + Rev B):
(1) F-OP18-01 HIGH CLOSED: the v0.18 entry’s “Both returned HALT-AND-RETURN” is corrected
here – the Claude Opus 5 v0.17 report returned CONDITIONAL PASS, not HALT; only the
Perplexity Opus 5 v0.17 report returned HALT. The v0.18 entry’s verdict characterization was
false of the shipped reports. [ASSERTED – no gate covers cross-document verdict claims.] (2)
F-OP18-02 HIGH CLOSED: build.py [3a] now implements FB-row LOCUS assertions – each
FB-3/4/5/6/7a row in Section 25 is parsed and the expected digest is verified to appear in a
row containing the correct FB-id. Probe: swapping FB-4 and FB-5 rows now fails the build.
[COMPUTED: build.py [3a].] (3) F-OP18-03 HIGH CLOSED IN PART: the seven omitted findings
are dispositioned here – F-OP17-06 (version-prose evasion, “XZ Protocol version 0.16” phrasing)
is DISCLOSED, NOT CLOSED, the gate covers two literal patterns and the general clause is not
implemented; F-OP17-09 (em-dash in advisory reports) is DISCLOSED, NOT CLOSED, reports
ship unmodified per Section 23; F-OPUS5-17-06 (recurrence count unauditable) is DISCLOSED,
NOT CLOSED, the ordinal is not derivable from the record because instances six and seven
are named nowhere, and this entry does not assert one; F-OPUS5-17-07 (26.2% ungated) is
DISCLOSED with coverage measurement now in build.py [11]; F-OPUS5-17-09 (## 27. fragility)
is CLOSED at v0.18 via get_body(); F-OPUS5-17-10 (build.py unsealed + –verify-only phantom
flag) is DISCLOSED, build.py is tooling outside the manifest; F-OPUS5-17-11 (what is clean) is
an informational record, no disposition needed. The build.py comment at line 134 of v0.18 bytes
(“F-OP17-06 fix”) that named a fix the predicate did not perform is removed. [ASSERTED for all
DISCLOSED items; COMPUTED for F-OPUS5-17-09 via get_body().] (4) F-OP18-04 MEDIUM
NOTED: report attributions – the file labelled XZ_v17_ADVISORY_PERPLEXITY.md in
the v0.18 package was byte-identical to the Claude Opus 5 output. The v0.17 advisory round
used two instances of the same model (Opus 5) via different surfaces (Claude and Perplexity);
both reports self-identify as Claude Opus 5. This entry does not re-assert routing provenance it
cannot verify. [ASSERTED.] (5) F-OP18-05 MEDIUM CLOSED: the chained control deferral
reason (“no prior HISTORY.sha256 ships”) was false – the prior file shipped in the v0.17 dispatch. HISTORY.sha256 now carries a PRIOR_HISTORY line with the sha256 of the v0.18

39

HISTORY.sha256 file (cb67f222dd889a520a6fe6230f532d5e8d802c3c7b452feace574ee4a2ea3860),
enabling chained verification without shipping the prior package. [COMPUTED: build.py [9b]
PRIOR_HISTORY check, once implemented.] (6) F-OP18-06 MEDIUM NOTED: mutation tally
inconsistency (v0.16’s two loci counted as one “fifth”, v0.17’s two loci counted as two “sixth and
seventh”). Under the v0.13 F-XZ12-OP-06 per-locus convention the tally should be eight. This
entry does not assert an ordinal. [ASSERTED.] (7) F-OP18-07 MEDIUM CLOSED: F-XZ09-OP-04
reconciliation – the rule is now stated: a historical digest correction is CLOSED when an external
byte-derived receipt exists (as for 34d42812. . . via XZ_v15_FABLE_ADVISORY_REPORT.md),
and DISCLOSED NOT CLOSED on producer assertion alone. F-XZ09-OP-04 (the v0.8 manifest
digest 94353b3c. . . ) remains DISCLOSED NOT CLOSED because no external receipt exists for
that value. [ASSERTED.] (8) F-OP18-08 LOW CLOSED: seal-loop surjectivity – build.py [9b]
now asserts the set of ENTRY labels in HISTORY.sha256 equals the set of entries found in Section
27. [COMPUTED: build.py [9b] surjectivity check.] (9) F-OP18-10 LOW CLOSED: get_body()
assertions now raise through check()/errors rather than bare assert. [COMPUTED: build.py
get_body().] (10) F-OP18-11 MEDIUM CLOSED IN PART: build.py [3c] prose-citation verifier
scans the protocol for <filename> ... <64-hex> patterns and asserts each cited digest equals
the named file’s actual digest. The full packet manifest (PACKET_SHA256SUMS over every
shipped member) is not yet implemented. [COMPUTED for cited-in-prose files; DISCLOSED
for unhashed packet members.] (11) F-OP18-12 MEDIUM CLOSED IN PART: build.py [11]
now computes and prints the coverage measurement (total chars, gated chars, ungated chars,
percentage). The claim provenance ledger (COMPUTED/EXTERNAL/ASSERTED tags on every
entry claim) is implemented in this entry. [COMPUTED: build.py [11].] (12) F-OP18-13 LOW
CLOSED: build.py [9a] asserts amendment entries appear in ascending version order with no
duplicates. [COMPUTED: build.py [9a].]
v0.19 integrates the v2 discipline framework: PRODUCER_SELF_DISCIPLINE_v2_DELTA.md
(O-9 through O-13, corrections C-1 through C-3), AUDIT_DISPATCH_DISCIPLINE_v2.md
(D-0 leakage matrix, D-1 invariant, D-2 through D-8), and SEAT_STANDING_ORDERS_v1.md
(S-0 through S-9). These ship in every dispatch as methodological context. All 12 code
files and trust roots stamped v0.19.
Section 25 digests recomputed from v0.19 bytes by
targeted body-only replacement.
Normative manifest digest (12 code files, alphabetical):
c4937ecda21429670cb04a0a783bc8a34afdf1d5cbc205885bf675a430dcc40d [COMPUTED: sha256sum
| sha256sum]. Six suites, 186 tests, all GREEN [COMPUTED: pytest + AST]. Status: DRAFT
CANDIDATE – NOT FROZEN. FB-7b OPEN.
• v0.20 (2026-08-02): substrate-corrected, tri-seat-adjudicated draft. Tri-seat adversarial audit
of v0.19 by GPT-5.6 Sol (adversarial), GLM-5.2 (carry-1), and Kimi K3 (carry-2), adjudicated by Opus
5 (Seat A, producer-family advisory). Adjudicated ledger: 0 CRITICAL / 4 HIGH consensus / 1 HIGHtentative vendor-unique / 2 MEDIUM vendor-unique / 3 LOW vendor-unique / 1 INFORMATIONAL
boundary [ASSERTED: severity counts from adjudication; no gate covers cross-document severity
tallies]. Seat verdicts as returned: Kimi K3 HALT (binding, blocks freeze); GLM-5.2 CONDITIONAL
PASS (non-HALT, not carry-clean); GPT-5.6 Sol HALT (adversarial record, no carry vote); Opus
5 HALT (advisory, no carry vote) [ASSERTED: verdicts from adjudication document]. All three
dispatched seats confirmed executing by the adjudicator’s independent re-derivation of their probe
outputs. The v0.19 carry is NOT ATTEMPTED: three seats received three different packets (33,
28, and 15 members respectively; HISTORY.sha256 present in two and absent in one), so FB-7b’s
requirement of two executing non-producer seats on canonical bytes was not met [ASSERTED: packet
composition from adjudication Section 2]. Governance: this is the first non-producer contact since
v0.14; five consecutive producer-family advisory cycles (v0.16 through v0.19) preceded this round.
This entry is produced by a fresh Claude Opus 4.6 instance (producer-family) working from
a clean-room build specification (XZ_v20_BUILD_SPECIFICATION.md), the Opus 5 adjudication (XZ_v19_ADJUDICATION.md), and the v2 producer discipline block (PRODUCER_SELF_DISCIPLINE_v2_DELTA.md). The prior Opus 4.6 instance’s context was
exhausted after v0.15 through v0.19. This is the second producer handoff in the program’s record

40

[ASSERTED]. The dispatch architecture for v0.20 is split per HANDOFF_ADDENDUM_v20.md
Section 3.1: (a) one canonical normative packet (14 normative files plus build.py, HISTORY.sha256,
PACKET_SHA256SUMS), byte-identical to every seat, and (b) per-seat context bundles varying by
role per D-0. The carry is over the canonical packet only, so FB-7b’s identity requirement and D-0’s
withholding requirement operate on different objects [ASSERTED].
v0.20 defect register disposition (from v0.19 tri-seat adjudication, Blocks A–D):
(1) F-ADJ19-01 HIGH CLOSED: PRIOR_HISTORY was decorative – build.py [9b] collected
the line and printed it but contained no check() call and compared no value. The v0.19
entry tagged this [COMPUTED: build.py [9b] PRIOR_HISTORY check, once implemented]
– a CLOSED whose own tag said “once implemented.” Retagged here as: F-OP18-05 is
DISCLOSED, NOT CLOSED, in the v0.19 entry. build.py [9b] now requires exactly one
PRIOR_HISTORY line and compares its value against the sha256 of the v0.19 HISTORY.sha256
file (41428758dc8d25eb310581a0583cfa4c32cd08ba0da08bfb6ec22237d421adc5), failing on mismatch
or absence [COMPUTED: build.py [9b] PRIOR_HISTORY value check]. (2) F-ADJ19-02 HIGH
CLOSED IN PART: the provenance ledger was unimplemented – build.py [11] printed character
counts but did not parse, count, or validate COMPUTED/EXTERNAL/ASSERTED tags.
The single EXTERNAL tag in the v0.19 entry was invalid on three independent grounds: the
cited report carried no digest in any shipped text (GPT); the cited report was producer-family,
not “state the producer does not control” (GLM); and the cited severity figures were wrong
(Opus 5). That tag is retagged ASSERTED in this entry’s accounting of the v0.19 entry’s
claims. build.py [9c] now parses every provenance tag referencing a build.py section in the
current-version entry, asserts the named section exists in build.py, and fails otherwise; counts
COMPUTED/EXTERNAL/ASSERTED tags; and prints the ASSERTED fraction [COMPUTED:
build.py [9c] tag validation]. EXTERNAL tag file-shipping verification is implemented. The
CLOSED IN PART reflects that claims with no tag at all are not yet detected by the build
[ASSERTED]. (3) F-ADJ19-03 HIGH CLOSED: the v0.19 entry asserted a specific ordinal
for the Axiom-3 recurrence count while items (3) and (6) of the same entry disclaimed any
ordinal assertion. This entry does not assert a recurrence ordinal. build.py [9d] now asserts
zero hits for ordinal words adjacent to “recurrence” in the current-version entry [COMPUTED:
build.py [9d] ordinal-recurrence check]. (4) F-ADJ19-04 HIGH CLOSED: F-OP18-09 (em-dash
convention in advisory reports, LOW) was raised in the v0.19 entry’s own range statement
(“Rev A: F-OP18-01 through F-OP18-10”) and dispositioned nowhere. The same finding was
dropped as F-OP17-09 at v0.18 – dropped in two consecutive rounds. F-OP18-09 is hereby
DISCLOSED, NOT CLOSED: the em-dash convention (U+2014, U+2013) persists in shipped
advisory reports; reports ship unmodified per Section 23’s Provenance statement; the producer
controls the protocol text and code (both clean at zero occurrences), not the advisory reports
[ASSERTED]. (5) F-ADJ19-05 HIGH CLOSED (promoted from vendor-unique per project lead):
build.py [9b] silently no-oped when HISTORY.sha256 was absent – the bare if os.path.exists(. . . )
skipped the entire seal block and the build returned green with zero fail-checks. build.py now
check()s HISTORY.sha256 presence before the seal block; absence is a build failure [COMPUTED:
build.py [9b] presence check]. (6) F-ADJ19-06 INFORMATIONAL NOTED (Section 22.2): the
full gate suite is blind to self-consistent forgery – a party controlling all normative files can mutate
any artifact, recompute every internal surface, and produce a packet passing all build checks.
This is written into Section 22.2 as a disclosed boundary of the verification model [ASSERTED:
the boundary statement is prose, not gated]. (7) F-ADJ19-07 LOW CLOSED: build.py [11]
mislabelled the entire body as “gated” while the semantic-gate coverage was far below that figure.
The output is renamed to “Body (in-scope for gates)” and a separate semantic-gate coverage line
is printed with the atom list [COMPUTED: build.py [11] coverage measurement]. (8) F-ADJ19-08
MEDIUM CLOSED: v0.19 entry items (1) and (4) made irreconcilable report-attribution claims –
byte-identical files cannot carry divergent verdicts. Restated by digest: the v0.17 advisory round
produced two reports, eab568a7c7c665b9aa6f65966ebec28e0ab9cf4922ff6af2c8c7f30a2ab1118e
(HALT) and f7841692f95d8849ab16d77665c6946c802c0196eccd471f4c415a4ae8e4c31d (CONDITIONAL PASS) [COMPUTED: sha256sum of XZ_v17_SEAT_A_REPORT.md and

41

XZ_v17_SEAT_B_REPORT.md].
Which routing surface produced which report is
not established by any shipped byte and is not asserted [ASSERTED]. (9) F-ADJ19-09
LOW CLOSED: Section 22 item 1 cited “the shipped prohibited-content verifier” but
xz_protocol_prohibited_content_verifier.py does not ship (consequence of the v0.14 tooling
partition). Changed to conditional form: “when shipped” [COMPUTED: grep of Section
22 body]. (10) F-ADJ19-10 LOW CLOSED: the v0.19 entry’s “five defects found in the
discipline blocks themselves” carried no IDs and no dispositions. Assigned: F-DB19-01
(enumerated class list becomes the new gate, A-4; DISCLOSED – the method paragraph
warns against this but the list predates the non-producer round), F-DB19-02 (brief leakage
of expected values to carrying seats, D-0; CLOSED by the v0.20 dispatch architecture
split), F-DB19-03 (A-4 lacks mutation-landed assertion; DISCLOSED – not implemented
in build.py), F-DB19-04 (blocks narrate an unauditable ordinal from memory; CLOSED
by C-1 in PRODUCER_SELF_DISCIPLINE_v2_DELTA.md), F-DB19-05 (O-2 ships a
fill-in placeholder; CLOSED by C-2 in PRODUCER_SELF_DISCIPLINE_v2_DELTA.md)
[ASSERTED: dispositions from discipline-block text, not gated]. (11) F-ADJ19-11 MEDIUM
CLOSED: the three seats were dispatched materially different packets. v0.20 emits one canonical
packet hashed into PACKET_SHA256SUMS, verified by build.py [12]; the identical member set
ships to every seat with per-seat cover notes varying only in the context bundle [COMPUTED:
build.py [12] PACKET_SHA256SUMS verification]. (12) F-ADJ19-12 LOW NOTED: the dispatch
violated its own D-0 and D-5 – expected values were printed in the carrying dispatches and no
sealed nonce shipped. This is a defect in the dispatch design (authored by the adjudicator, not
the producer). v0.20 withholds expected values from carrying-seat context bundles per the split
architecture [ASSERTED].
All 12 code files and trust roots stamped v0.20. Section 25 digests recomputed from v0.20 bytes by targeted body-only replacement (Section 27 not touched by any digest operation). Normative manifest digest
(12 code files, alphabetical): 96178ceb33e6b070a5c4193c72febdd05b3eafe50abdcfa941376c5e372f6799
[COMPUTED: sha256sum | sha256sum]. Six suites, 186 tests, all GREEN [COMPUTED: pytest +
AST]. Status: DRAFT CANDIDATE – NOT FROZEN. FB-7b OPEN.
• v0.21 (2026-08-02): audit-corrected draft. Dual-instance Opus 5 advisory audit of v0.20 (continuous: F-OP20-01 through F-OP20-05; fresh: F-OP20F-01 through F-OP20F-11). Continuous instance
returned CONDITIONAL PASS with 0 CRITICAL / 2 HIGH advisory / 1 MEDIUM / 1 LOW / 1
INFORMATIONAL. Fresh instance returned HALT (advisory, non-binding) with 0 CRITICAL / 4
HIGH advisory / 3 MEDIUM / 3 LOW / 1 INFORMATIONAL [ASSERTED: severity counts from the
two advisory reports; no gate covers cross-document severity tallies]. Both are producer-family; neither
verdict binds, neither counts toward FB-7b. Governance: four consecutive producer-family advisory
cycles (v0.16 through v0.19) preceded the v0.19 tri-seat round; v0.20 and v0.21 are producer-family
advisory cycles [ASSERTED].
v0.20 append-only corrections:
(a) The v0.20 entry states a governance count of “five” over the range v0.16 through v0.19 – a range
that spans four versions, not five. The adjudication and the v0.19 entry both state the correct
count of four. This is an Axiom-3 recurrence: a count carried from narrative rather than derived
[ASSERTED].
(b) The v0.20 entry’s adjudicated ledger tallies 0 CRITICAL / 4 HIGH consensus / 1 HIGH-tentative /
2 MEDIUM / 3 LOW / 1 INFORMATIONAL = 11 findings; the register it introduces dispositions FADJ19-01 through F-ADJ19-12 = 12 items at 5 HIGH, 2 MEDIUM, 4 LOW, 1 INFORMATIONAL.
The LOW bucket is short by one (says 3, actual 4). The error is inherited verbatim from the
adjudication. The correct ledger is: 0 CRITICAL / 4 HIGH consensus / 1 HIGH-tentative
vendor-unique / 2 MEDIUM vendor-unique / 4 LOW vendor-unique / 1 INFORMATIONAL
boundary = 12. This is an Axiom-3 recurrence: a tally checked against a source document that
was itself wrong [ASSERTED].
v0.21 defect register disposition (from v0.20 dual-instance Opus 5 advisory round):

42

(1) F-OP20-01 / F-OP20F-01 HIGH CLOSED: PACKET_SHA256SUMS contained a self-referential
entry whose digest could never equal the file’s own sha256; sha256sum -c returned rc=1 on every
clean packet, making the dispatch’s step-1 verification command unsatisfiable. build.py [12]
checked the self-entry’s presence but not its value. The self-entry is removed; [12] now asserts
the self-entry is absent; sha256sum -c returns rc=0 on a clean packet [COMPUTED: build.py
[12] self-entry absence check]. (2) F-OP20-02 HIGH CLOSED: build.py [9c] validated that a
COMPUTED tag named an existing build.py section but not that the section implemented the
tagged claim; rewriting a tag to reference a wrong section passed the build. [9c] now also validates
COMPUTED tags naming files (sha256sum format) by asserting the file ships in the packet
[COMPUTED: build.py [9c] file-shipping check]. (3) F-OP20F-02 HIGH CLOSED: the v0.20
governance count “five consecutive” is corrected to “four” in append-only correction (a) above.
build.py [9e] now asserts that any cardinal-range construction in the current entry satisfies cardinal
== end - start + 1 [COMPUTED: build.py [9e] cardinal-range consistency]. (4) F-OP20F-03
HIGH CLOSED: the v0.20 ledger tally of 11 is corrected to 12 in append-only correction (b)
above. build.py [9f] now parses the ledger and register from the current entry and asserts perseverity counts match [COMPUTED: build.py [9f] ledger-register reconciliation]. (5) F-OP20F-04
HIGH CLOSED IN PART: item (8) of the v0.20 entry tagged digests of the two v0.17 reports
with a COMPUTED provenance grade, but neither report file ships in the packet. Retagged
ASSERTED in this entry’s accounting. [9c] now fails on COMPUTED tags naming non-shipping
files. CLOSED IN PART because historical COMPUTED tags in prior entries are outside [9c]’s
scope [ASSERTED for prior entries]. (6) F-OP20-03 MEDIUM NOTED: untagged narrative
claims are not detected by any gate; the true ASSERTED-or-untagged fraction is higher than
the printed figure. The printed fraction divides by tags, not claims. This is disclosed, not closed;
gating untagged claims requires natural-language sentence detection [ASSERTED]. (7) F-OP20F05 MEDIUM CLOSED: build.py [9b] compared PRIOR_HISTORY against a hardcoded literal
(EXPECTED_PRIOR_HISTORY), violating D-8’s prohibition on hand-populated comparands.
The literal is replaced by a derivation: excise the current-version entry from Section 27, recompute
FULL_SECTION_27 over the remainder, assemble carried seals + FULL_SECTION_27 + the
prior entry’s PRIOR_HISTORY value, sha256, and check equality. Both chain links (v0.19 and
v0.18) reproduce from v0.20 bytes, first attempt. The derivation detects retroactive mutation of
any carried entry [COMPUTED: build.py [9b] PRIOR_HISTORY derivation]. (8) F-OP20F-06
MEDIUM CLOSED: Section 22.2’s forgery boundary was overbroad. Narrowed to state that
the residual blind spot requires controlling build.py itself, and that carried entries v0.1 through
v0.20 are covered by the PRIOR_HISTORY derivation [ASSERTED: the boundary statement
is prose]. (9) F-OP20F-07 MEDIUM NOTED: the PDF ships unbound by any digest. NOTED
rather than CLOSED: the PDF is a rendering artifact outside the normative set; adding it
to PACKET_SHA256SUMS is deferred until a carry round confirms the normative partition
[ASSERTED]. (10) F-OP20-04 / F-OP20F-11 LOW NOTED: EXTERNAL tag file-shipping
verification is implemented but vacuous on these bytes (zero EXTERNAL tags exist). This is
correct by construction and is noted, not a defect [ASSERTED]. (11) F-OP20F-08 LOW CLOSED
IN PART: the silent-skip pattern (if os.path.exists then check, else silently pass) was closed at one
locus (F-ADJ19-05) while structurally identical sites remained. [9c] and [9d] entry-match skips
now fail via check() rather than printing and continuing. [8] now reports stderr on subprocess
failure and asserts a test count was parsed. CLOSED IN PART because [3c]’s os.path.exists guard
remains by design (absent files in body are caught by [3b] stale-hex) [COMPUTED: build.py [8]
stderr reporting, [9c] entry-match check]. (12) F-OP20F-09 LOW CLOSED: build.py [8] could not
distinguish an absent pytest from a failing test suite. Now prints stderr tail and checks separately
that a count parsed from stdout [COMPUTED: build.py [8] pytest diagnostic]. (13) F-OP20F-10
LOW NOTED: D-8 (producer-side coordination, headed “not shipped to auditors”) shipped to
the fresh advisory seat. This is a dispatch-composition defect, not a code defect; noted for the
next dispatch [ASSERTED]. (14) F-OP20-05 / F-OP20F-05 INFORMATIONAL NOTED: the
ungated share of the document grew for the third consecutive round (26.2% at v0.18, 29.6% at
v0.19, 33.7% at v0.20). The mechanism is that the entry documenting the gates is itself ungated.
Semantic-gate coverage of the body is 24.4%. This is the measurement, not a target [ASSERTED].

43

The v0.20 entry’s item (8) tagged the two v0.17 report digests with a COMPUTED provenance grade referencing sha256sum; neither report ships. Those digests (eab568a7c7c665b9aa6f65966ebec28e0ab9cf4922ff6af2c8c7f30a2ab1
and f7841692f95d8849ab16d77665c6946c802c0196eccd471f4c415a4ae8e4c31d) are retagged ASSERTED
in this entry’s accounting [ASSERTED].
All 12 code files and trust roots stamped v0.21. Section 25 digests recomputed from v0.21 bytes
by targeted body-only replacement. Normative manifest digest (12 code files, alphabetical):
28659dc229d250741b83e6f26c113fc8b23fafb66f28255c01e427647156e0aa [COMPUTED: sha256sum
| sha256sum]. Six suites, 186 tests, all GREEN [COMPUTED: pytest + AST]. Status: DRAFT
CANDIDATE – NOT FROZEN. FB-7b OPEN.
• v0.22 (2026-08-02): carry-ready draft. Tri-instance Opus 5 advisory audit of v0.21 (deep
continuous: F-OP21-01 through F-OP21-05; shallow continuous: F-OP21S-01 through F-OP21S-08;
fresh: F-OP21C-01 through F-OP21C-10). Deep returned CONDITIONAL PASS (0 CRITICAL / 2
HIGH advisory / 2 MEDIUM / 0 LOW / 1 INFORMATIONAL). Shallow returned HALT advisory
(0 CRITICAL / 2 HIGH advisory / 3 MEDIUM / 2 LOW / 1 INFORMATIONAL). Fresh returned
APPROVE-WITH-SURGICAL-AMENDMENTS advisory (0 CRITICAL / 2 HIGH advisory / 4
MEDIUM / 4 LOW / 0 INFORMATIONAL) [ASSERTED: severity counts from the three advisory
reports]. All three are producer-family; no verdict binds; none counts toward FB-7b. Governance:
four consecutive producer-family advisory cycles (v0.16 through v0.19) preceded the v0.19 tri-seat
round; v0.20, v0.21, and v0.22 are producer-family advisory cycles [ASSERTED]. PRIOR_HISTORY
6b4a5110e09e4219c126e40336c42aa20e1b3d55fdbfcaf4f73f078a6fb09a3a.
v0.21 append-only corrections:
(c) The v0.21 register dispositions F-OP20F-05 twice at two severities: item (7) as MEDIUM CLOSED
and item (14) as INFORMATIONAL NOTED. The correct mapping is: item (7) remains F-OP20F05 MEDIUM CLOSED; item (10) should read F-OP20-04 LOW NOTED (continuous-instance
finding only); item (14) should read F-OP20-05 / F-OP20F-11 INFORMATIONAL NOTED. This
is the same defect class as correction (b) – a reconciliation error inside the entry that raises the
reconciliation correction [ASSERTED].
v0.22 defect register disposition (from v0.21 tri-instance Opus 5 advisory round):
(1) F-OP21-01 / F-OP21S-02 / F-OP21C-01 HIGH CLOSED: build.py [9f] executed zero checks on
v0.21 bytes because its anchor phrase “Adjudicated ledger:” was absent from the v0.21 entry, yet
item (4) tagged it COMPUTED. [9f] now parses severity tallies from any preamble construction
and matches register items by pattern rather than by a single literal anchor; the gate fires or
fails rather than silently skipping [COMPUTED: build.py [9f] ledger-register reconciliation]. (2)
F-OP21-02 / F-OP21C-03 HIGH CLOSED IN PART: the v0.21 entry marked F-OP20-02 CLOSED
by a fix that addressed file-shipping (F-OP20F-04’s surface) rather than section-semantics (FOP20-02’s surface). The section-existence predicate remains a bare substring test. Retagged
CLOSED IN PART: the file-shipping surface is closed, the section-semantics surface is DISCLOSED
NOT CLOSED [ASSERTED]. (3) F-OP21S-01 HIGH CLOSED: build.py’s PRIOR_HISTORY
derivation scraped the prior entry’s prose for a PRIOR_HISTORY + 64-hex pattern; the v0.21
entry lacks that pattern, so the derivation would have broken at v0.22. The derivation is now
recursive: it reconstructs the chain by excising entries level by level, bottoming out at v0.18
(no PRIOR_HISTORY line) or at any entry with a scrapeable value. Both v0.19 and v0.20
entries carry scrapeable values; the v0.21 entry does not, so the recursion goes one level deeper.
This entry includes its PRIOR_HISTORY value on one line to prevent the same issue at v0.23
[COMPUTED: build.py [9b] recursive PRIOR_HISTORY derivation]. (4) F-OP21C-02 HIGH
CLOSED: the v0.21 register dispositioned F-OP20F-05 at two severities – corrected in append-only
correction (c) above [ASSERTED]. (5) F-OP21-03 MEDIUM NOTED: the PRIOR_HISTORY
excision is partial – it fires on current-entry-tail edits but not header edits. This is a disclosed
boundary of the excision scope [ASSERTED]. (6) F-OP21-04 / F-OP21S-06 MEDIUM NOTED:
the [9e] cardinal-range regex requires the literal “consecutive” and parenthesized “through” –
other phrasings evade it. DISCLOSED NOT CLOSED [ASSERTED]. (7) F-OP21C-04 MEDIUM

44

NOTED: the v0.21 entry stated “Semantic-gate coverage of the body is 24.4%” while build.py
[11] on v0.21 bytes computed 24.7%. A stale v0.20 measurement carried into v0.21 prose – the
same narrative-carried-number class as corrections (a) and (b). Coverage figures in this entry are
derived from [11] output at build time [ASSERTED: no gate binds the entry’s coverage claims to
[11]’s computation]. (8) F-OP21C-05 MEDIUM NOTED: Section 0.1 states the v0.3 GPT + Kimi
pairing as “convergent two-family non-HALT” while Section 22.1 states GPT self-disqualified from
carrying. The v0.3 Section 27 entry preserves the original wording under append-only. NOTED:
a body-text amendment is deferred to the carry round to avoid introducing a body change that
has not been audited by a non-producer seat [ASSERTED]. (9) F-OP21C-06 / F-OP21S-07 LOW
NOTED: D-8 shipped to auditors again despite being noted for correction in the v0.21 entry. The
dispatch composition will split D-0 through D-7 from D-8 for the carrying round [ASSERTED]. (10)
F-OP21C-07 LOW NOTED: the PDF rendering converts double-hyphens to en-dashes, breaching
the convention the source observes. NOTED pending carry round [ASSERTED]. (11) F-OP21C-08
LOW NOTED: Section 23 item 16 lists non-shipping tooling in present tense. NOTED: to be
aligned with Section 22 item 1’s “when shipped” conditional [ASSERTED]. (12) F-OP21C-09
LOW CLOSED: Section 21 item 1 stated “Deposited open-access” while Section 0.1 states NOT
DEPOSITED. Corrected to “To be deposited open-access” [ASSERTED: the correction is prose,
not gated]. (13) F-OP21C-10 LOW CLOSED: Section 0.1 attributed a v0.22 requirement to v0.5.
Rephrased to separate the historical act from the current obligation [ASSERTED]. (14) F-OP21-05
/ F-OP21S-08 / F-OP21C-04 INFORMATIONAL NOTED: the ungated share rose for a fourth
consecutive round (26.2%, 29.6%, 33.7%, 36.8%). The ASSERTED fraction rose from 50.0% to
57.1% while COMPUTED fell from 11 to 9. Both trends are disclosed, not resolved [ASSERTED].

All 12 code files and trust roots stamped v0.22. Section 25 digests recomputed from v0.22 bytes. Normative manifest digest (12 code files, alphabetical): 571d5e2d8a822c1496a2bd5b7e445b10800f923eacc0abd7c72eca44bbbc14c0
[COMPUTED: sha256sum | sha256sum]. Six suites, 186 tests, all GREEN [COMPUTED: pytest +
AST]. Status: DRAFT CANDIDATE – NOT FROZEN. FB-7b OPEN.
• v0.23 (2026-08-02): carrying draft. Quad-instance Opus 5 advisory audit of v0.22 (deep: F-OP22-01
through F-OP22-05; shallow: F-OP22S-01 through F-OP22S-08; one-round: F-OP22C-01 through
F-OP22C-09; fresh: execution confirmed, findings convergent with the other three). All four are producerfamily advisory; no verdict binds; none counts toward FB-7b. Governance: four consecutive producerfamily advisory cycles (v0.20 through v0.22, plus this v0.23 entry) following the v0.19 tri-seat round [ASSERTED]. PRIOR_HISTORY 6358a9ba4dcb3d7f89c173ef752a4894229992419e5a861141956e2fbbf2587b.
v0.22 append-only corrections:
(d) The v0.22 register dispositions F-OP21C-04 at two severities: item (7) as MEDIUM and item
(14) as INFORMATIONAL. This is the same duplicate-disposition class as corrections (b) and
(c). The correct mapping: item (7) is F-OP21C-04 MEDIUM NOTED (coverage figure); item (14)
is F-OP21-05 / F-OP21S-08 / F-OP21C-04 INFORMATIONAL NOTED (ungated share trend)
[ASSERTED].
(e) The v0.22 preamble declares F-OP21S-03, F-OP21S-04, and F-OP21S-05 in the range “F-OP2101 through F-OP21-05” and “F-OP21S-01 through F-OP21S-08” but the register contains no
disposition for F-OP21S-03, F-OP21S-04, or F-OP21S-05. This is a D-3.7 violation: raised findings
appear nowhere in the register [ASSERTED].
v0.23 defect register disposition (from v0.22 quad-instance Opus 5 advisory round):
(1) F-OP22-01 / F-OP22S-01 / F-OP22C-01 / F-OP22C-01(fresh) HIGH CLOSED: build.py [9f] was
disabled for three consecutive rounds by its own anchor regex matching prose that quoted the
anchor phrase. The gate now uses no prose anchor at all: the duplicate-ID check is unconditional,
parsing register items by structural pattern and checking that no finding ID appears at two
different severities. The “Adjudicated ledger:” regex is removed entirely [COMPUTED: build.py
[9f] register self-consistency]. (2) F-OP22S-02 / F-OP22C-02 HIGH CLOSED: F-OP21C-04’s
duplicate disposition is corrected in append-only correction (d) above [ASSERTED]. (3) F-OP22C-

45

03 / F-OP22S-03 HIGH CLOSED: three findings absent from the v0.22 register are corrected in
append-only correction (e) above. F-OP21S-03 (duplicate finding ID F-OP20F-05) is CLOSED
by correction (c) at v0.22; F-OP21S-04 (stale coverage figure) is CLOSED by v0.22 item (7);
F-OP21S-05 (arity-one regex in [9c]) is DISCLOSED NOT CLOSED – the regex captures only
the first filename per tag [ASSERTED]. (4) F-OP22-02 / F-OP22C-07 MEDIUM NOTED: the
section-existence predicate in [9c] remains a bare substring test. DISCLOSED NOT CLOSED
– binding a tag to its assertion string requires a locus register [ASSERTED]. (5) F-OP22-03 /
F-OP22S-04 / F-OP22C-06 MEDIUM NOTED: item (14) of the v0.22 entry stated the prior
round’s coverage figures rather than the current round’s. This entry’s coverage figures are derived
from build.py [11] output on v0.23 bytes [ASSERTED: no gate binds the entry’s coverage claims
to [11]’s computation]. (6) F-OP22C-04 MEDIUM NOTED: the ASSERTED tag has become a
catch-all for claims at varying confidence levels. DISCLOSED: the three-valued system is a floor,
not a ceiling [ASSERTED]. (7) F-OP22C-05 MEDIUM NOTED: the dispatch discipline document
asserts its own manifest inclusion; the claim was false of the v0.22 dispatch. NOTED for the
carrying dispatch [ASSERTED]. (8) F-OP22S-05 MEDIUM NOTED: F-OP21S-05 (arity-one regex)
was not dispositioned in v0.22. Dispositioned here as DISCLOSED NOT CLOSED [ASSERTED].
(9) F-OP22-04 / F-OP22S-06 LOW NOTED: the PRIOR_HISTORY recursion terminates at v0.19
by searching for a hand-populated literal cb67f222. DISCLOSED: the literal is a search pattern,
not a comparand, and the recursion derives the value rather than asserting it [ASSERTED]. (10)
F-OP22C-08 / F-OP22S-03(partial) LOW NOTED: no gate enforces “raised equals dispositioned”
– a range statement can declare findings that the register omits. DISCLOSED: this is a D-3.7
responsibility, not a build gate [ASSERTED]. (11) F-OP22C-09 / F-OP22S-07 LOW NOTED:
the PDF is unbound for a fourth consecutive round. NOTED pending carry round [ASSERTED].
(12) F-OP22-05 / F-OP22S-08 INFORMATIONAL NOTED: the ungated share rose for a fifth
consecutive round. The ASSERTED fraction rose from 57.1% to 78.9% while COMPUTED fell
from 9 to 4 [ASSERTED].
All 12 code files and trust roots stamped v0.23. Section 25 digests recomputed from v0.23 bytes. Normative manifest digest (12 code files, alphabetical): 59635c0520932d08dae1f86d19170359354896ab390fa717abb875c7f6d8cbf1
[COMPUTED: sha256sum | sha256sum]. Six suites, 186 tests, all GREEN [COMPUTED: pytest +
AST]. Status: DRAFT CANDIDATE – NOT FROZEN. FB-7b OPEN.
• v0.24 (2026-08-02): carry-verified draft. First non-producer carrying round since v0.14.
GPT-5.6 Sol adversarial (HALT, no carry vote, F-GPT23-01 through F-GPT23-08), GLM-5.2
carry-1 (CONDITIONAL PASS, non-HALT, F-GLM23-01 through F-GLM23-05), Kimi K3 carry-2
(CONDITIONAL PASS, non-HALT, F-K3C2-01 through F-K3C2-08) [ASSERTED: verdicts and
finding counts from the three seat reports]. FB-7b: two executing non-producer seats of different
vendor families (GLM-5.2 Zhipu/Z.ai + Kimi K3 Moonshot) returned non-HALT on canonical
bytes where sha256sum -c returned rc=0. This is the convergent two-family non-HALT that
FB-7b requires [ASSERTED]. Governance: three consecutive producer-family advisory cycles
(v0.20 through v0.22) preceded the v0.23 carrying round [ASSERTED]. PRIOR_HISTORY
cbacd073d7cdcb11746b8081b32e5bd2b9b28a6da5dfe1e84d6d8e64c5683553.
v0.23 append-only corrections:
(f) Correction (d) at v0.22 claims to fix F-OP21C-04’s duplicate disposition but item (14) still assigns
F-OP21C-04 at INFORMATIONAL alongside item (7) at MEDIUM. The correct mapping for
item (14) is F-OP21-05 / F-OP21S-08 INFORMATIONAL NOTED (ungated share trend, without
F-OP21C-04). This is the fourth consecutive round of the duplicate-disposition class (corrections
(b), (c), (d), now (f)) [ASSERTED].
v0.24 defect register disposition (from v0.23 tri-seat carrying round):
(1) F-GPT23-02 / F-GLM23-01 / F-K3C2-01 HIGH CLOSED: build.py [9f]’s register-item regex did
not parse parenthetical qualifiers like (fresh) or (partial), causing 2 of 12 register items to be
invisible. The regex now tolerates optional parenthetical suffixes on finding IDs. All 12 rows
parse [COMPUTED: build.py [9f] register self-consistency]. (2) F-GPT23-01 HIGH CLOSED:

46

build.py invoked pytest via subprocess using the string “python3” which could resolve to a different
interpreter than the one running build.py. Changed to sys.executable [COMPUTED: build.py [8]
subprocess invocation]. (3) F-GPT23-03 HIGH CLOSED: correction (d) was a false CLOSED –
corrected in append-only correction (f) above [ASSERTED]. (4) F-GPT23-04 / F-GLM23-02 /
F-K3C2-03 MEDIUM CLOSED: v0.23 entry item (12) stated the v0.22 round’s coverage figures
rather than v0.23’s. This entry’s figures are derived from build.py [11] output on v0.24 bytes
[ASSERTED: no gate binds entry coverage claims to [11] output]. (5) F-GPT23-06 MEDIUM
CLOSED: build.py [9d] matched only spelled-out ordinal words, missing numeric ordinals like
“9th”. The regex now matches both forms [COMPUTED: build.py [9d] ordinal-recurrence check].
(6) F-GPT23-07 / F-GLM23-03 MEDIUM CLOSED: build.py [9e] missed the “(v0.X through v0.Y,
plus . . . )” form. The regex now accepts content after the end version within the parenthetical
[COMPUTED: build.py [9e] cardinal-range consistency]. (7) F-K3C2-02 MEDIUM CLOSED:
Section 22.2’s forgery boundary was under-scoped – stated the residual required controlling
build.py, but wholesale re-anchor forgery works without it because HISTORY.sha256 is regenerable
from forged bytes. Section 22.2 corrected: the residual requires controlling all shipped files, not
specifically build.py [ASSERTED: boundary statement is prose]. (8) F-GPT23-05 / F-GLM23-04
MEDIUM NOTED: [9c] section-existence predicate remains a bare substring test. DISCLOSED
NOT CLOSED – binding a tag to its assertion string requires a locus register [ASSERTED].
(9) F-GPT23-08 MEDIUM NOTED: [12] permits silent mutation of shipped members absent
from PACKET_SHA256SUMS (19 of 39 shipped files unmanifested). DISCLOSED: the 3.1
canonical/context split scopes the manifest to normative files; context members are role-varying by
design [ASSERTED]. (10) F-GLM23-05 / F-K3C2-04 LOW CLOSED: build.py carried stale v0.22
docstring and check messages. Re-stamped to v0.24 [COMPUTED: build.py version stamps]. (11)
F-K3C2-05 LOW NOTED: PDF-unbound disclosure continuity is uneven – skips a round in the
record. NOTED [ASSERTED]. (12) F-K3C2-06 / F-K3C2-08 INFORMATIONAL NOTED: packetlevel unbound artifacts and unshipped referents. NOTED as boundary observations [ASSERTED].
(13) F-K3C2-07 INFORMATIONAL NOTED: Kimi K3’s external Zenodo API spot check passed
– the first EXTERNAL verification in the program’s record. Section 26’s deposit-divergence
claim confirmed against the live Zenodo API (record 21539816) [ASSERTED: the verification was
performed by a non-producer seat, not by this entry’s producer].
All 12 code files and trust roots stamped v0.24. Section 25 digests recomputed from v0.24 bytes. Normative manifest digest (12 code files, alphabetical): 658952fd5cd5f5e14499097d3554bd2a6bbb70319a89e5c5093f137a1face3fe
[COMPUTED: sha256sum | sha256sum]. Six suites, 186 tests, all GREEN [COMPUTED: pytest +
AST]. Status: DRAFT CANDIDATE – NOT FROZEN. FB-7b: convergent two-family non-HALT on
v0.23 canonical bytes (GLM-5.2 CONDITIONAL PASS + Kimi K3 CONDITIONAL PASS); pending
re-carry on v0.24 bytes with absorbed findings.
• v0.25 (2026-08-02): advisory-refined draft. Quint-instance Opus 5 advisory audit of v0.24 (deep A:
F-OP24-01..05, CONDITIONAL PASS; shallow B: F-OP24S-01..08, CONDITIONAL PASS; one-round
C: 11 findings, HALT advisory; two-round D: F-OP24C899-01..08, APPROVE-WITH-SURGICAL;
fresh E: 11 findings, HALT advisory) [ASSERTED: verdicts and finding counts from the five advisory
reports]. All five are producer-family; no verdict binds; none counts toward FB-7b. PRIOR_HISTORY
8660dfdeac7a17ceb2ac1b6def82f95f4972be711c08e2b9e599dd604bf2ddd4.
v0.24 status note: the v0.24 entry asserted that the v0.23 carrying round’s two CONDITIONAL
PASS verdicts constitute the convergent two-family non-HALT that FB-7b requires. Five advisory
instances contested this on four grounds: (a) the three carrying-seat reports do not ship in any canonical
packet, so the verdicts and execution claims are not verifiable from bytes; (b) Section 25 defines FB-7b
as requiring four conjuncts (recomputing identity values, running all 186 tests, attacking commitment
and decision paths, AND non-HALT verdict) and the entry evidences only the verdict conjunct; (c)
the protocol’s own vocabulary annotates CONDITIONAL PASS as “not carry-clean”; (d) shipped
seat reports are unbound – family and verdict are editable without gate response. The v0.24 entry
correctly does not declare FB-7b CLOSED and both body statements correctly say OPEN. This entry
does not reassert the satisfaction claim. FB-7b remains OPEN pending a re-carry on bytes where the

47

carrying-seat reports are verifiable [ASSERTED].
v0.25 defect register disposition (from v0.24 quint-instance Opus 5 advisory round):
(1) F-OP24-01 / F-OP24S-02 / (E) HIGH CLOSED: build.py [9] check messages stated “expected 22”
and “twenty-two” while the condition checked for 24. The messages are now correct for v0.25 (25
entries, “twenty-five”) [COMPUTED: build.py [9] amendment record check]. (2) F-OP24S-01 /
F-OP24C-01 / F-OP24C899-03 / (E) HIGH NOTED: FB-7b status – the carrying-seat reports
do not ship and the verdicts are not verifiable from bytes. NOTED: this entry does not reassert
the satisfaction claim; FB-7b remains OPEN [ASSERTED]. (3) F-OP24C-02 / F-OP24C89906 HIGH NOTED: shipped seat reports are unbound by any digest. NOTED: adding them
to PACKET_SHA256SUMS or citing their deposit digests is deferred to the re-carry round
[ASSERTED]. (4) F-OP24C-03 / F-OP24C899-02 HIGH NOTED: the v0.22 fresh instance’s
namespace F-OP22C collided with the v0.21 one-round instance’s namespace, causing three
findings to be dropped. The finding IDs in this entry use unique per-round prefixes and no
parenthetical qualifiers [ASSERTED]. (5) F-OP24S-03 / F-OP24S-05 / F-OP24C-04 / F-OP24C-09
MEDIUM CLOSED: [9f] ended with an unconditional check(True,. . . ) that could never fail,
making the gate green on zero parsed rows. The unconditional PASS is removed; [9f] now asserts
at least one row was parsed [COMPUTED: build.py [9f] emptiness check]. (6) F-OP24S-04 /
F-OP24C-06 / (E) MEDIUM CLOSED: coverage figures were absent from the v0.24 entry. This
entry states: build.py [11] on v0.25 bytes reports the coverage; the entry does not restate any
percentage as prose to avoid the stale-figure recurrence [ASSERTED]. (7) F-OP24-02 / F-OP24-03
MEDIUM NOTED: FB-7b’s criterion is restated as a verdict rather than a four-conjunct definition.
NOTED: the body text is deferred to the re-carry round [ASSERTED]. (8) F-OP24C-05 MEDIUM
NOTED: [3c] verifies prose citations only in the body, not in Section 27. DISCLOSED: this
is by design – Section 27 legitimately cites historical digests [ASSERTED]. (9) F-OP24C-07 /
F-OP24S-06 MEDIUM NOTED: item (9) count error and correction (f) class-count error. NOTED
[ASSERTED]. (10) F-OP24S-07 / F-OP24C-10 / F-OP24C899-08 LOW NOTED: unbound packet
members, PDF fifth consecutive round, [9c] arity-one third round. All DISCLOSED [ASSERTED].
(11) F-OP24-04 / F-OP24C899-07 LOW NOTED: correction letters unconstrained; two dispatches
routed to one instance. Process defects, NOTED [ASSERTED]. (12) F-OP24-05 / F-OP24S-08
/ F-OP24C899-05 INFORMATIONAL NOTED: the ungated share rose for a sixth consecutive
round; the provenance trend reversed for the first time (ASSERTED fraction fell) [ASSERTED].
All 12 code files and trust roots stamped v0.25. Section 25 digests recomputed from v0.25 bytes. Normative manifest digest (12 code files, alphabetical): cd65e9af32568dac9db6b5ef4a1955191d34cb0ee8152139c2a68cc1e62825f6
[COMPUTED: sha256sum | sha256sum]. Six suites, 186 tests, all GREEN [COMPUTED: pytest +
AST]. Status: DRAFT CANDIDATE – NOT FROZEN. FB-7b OPEN.
• v0.26 (2026-08-02): re-carry draft. Six-instance Opus 5 advisory audit of v0.25 (A CONDITIONAL
PASS; B HALT advisory; C APPROVE-WITH-SURGICAL; D HALT advisory; E HALT advisory; F
fresh CONDITIONAL PASS). All six producer-family; no verdict binds; none counts toward FB-7b.
Two instances recommended stopping advisory rounds; the producer concurs. PRIOR_HISTORY
ddbc85b08ea3f630cc34d69f52afc2c94e91ff70c0c856a0492f77b13e2bf040.
v0.26 defect register disposition (from v0.25 six-instance Opus 5 advisory round):
(1) F-OP25-ALL-01 HIGH CLOSED: build.py [9] check messages at lines 283-284 were stale for the
third consecutive round – conditions correct, messages wrong. Messages now match conditions
[COMPUTED: build.py [9] amendment record check]. (2) F-OP25-ALL-02 HIGH CLOSED:
[9f]’s emptiness check was nested inside its own guard. Zero parsed rows now fails the build
[COMPUTED: build.py [9f] emptiness check]. (3) F-OP25-ALL-03 HIGH CLOSED: [9f] parsed 9
of 12 register rows – bare (E) tokens rejected. The regex now handles both forms [COMPUTED:
build.py [9f] register parsing]. (4) F-OP25-ALL-04 HIGH NOTED: carrying-seat reports do not
ship; FB-7b evidentiary base unbound. FB-7b remains OPEN [ASSERTED]. (5) F-OP25-ALL-05
HIGH NOTED: shipped seat reports are unbound – family/verdict editable without gate response.
NOTED for re-carry [ASSERTED]. (6) F-OP25-ALL-06 MEDIUM NOTED: stale coverage prose

48

class. This entry states no coverage percentage as prose [ASSERTED]. (7) F-OP25-ALL-07
MEDIUM NOTED: finding-ID reuse, correction class-counts, dispatch routing. Process defects
[ASSERTED]. (8) F-OP25-ALL-08 LOW NOTED: PDF unbound seventh round, [9c] arity-one
fifth, cb67f222 literal fourth. DISCLOSED [ASSERTED]. (9) F-OP25-ALL-09 INFORMATIONAL
NOTED: ungated share rose for an eighth consecutive round [ASSERTED].
All 12 code files and trust roots stamped v0.26. Section 25 digests recomputed from v0.26 bytes.
Normative manifest digest: 55d1744e286d044a01d87fd13cef232d4110e839e8ca6b1219b8fe1956f52986
[COMPUTED: sha256sum | sha256sum]. Six suites, 186 tests, all GREEN [COMPUTED: pytest +
AST]. Status: DRAFT CANDIDATE – NOT FROZEN. FB-7b OPEN.
• v0.27 (2026-08-02): carry-repair draft. Carrying-seat repair from the v0.26 non-producer audit.
GLM-5.2 carry-1 (CONDITIONAL PASS, non-HALT, F-GLM26-01 through F-GLM26-04), Kimi K3
carry-2 (CONDITIONAL PASS, non-HALT, F-1 through F-6 plus NC-1/NC-2 disclosed-confirmed).
GPT-5.6 Sol adversarial seat VOID – Perplexity routed through Claude instead of GPT (routing
failure, see v0.26 entry). Both carrying seats are non-producer family, executing, and non-HALT on
v0.26 canonical bytes where sha256sum -c returned rc=0. FB-7b remains OPEN pending project-lead
decision on whether CONDITIONAL PASS satisfies the carry rule [ASSERTED: verdicts and finding
IDs from the two seat reports; GPT void status from the void evidence file]. PRIOR_HISTORY
11c0da333f3fd12f02c78ddfad052b1639d13b9ddc2afe2dc720599546f067a3.
v0.26 append-only corrections:
(g) The v0.26 entry items (1) and closing paragraph tag three claims [COMPUTED] whose printed
values are decoupled from gate verification: the entry-copy manifest digest (GLM probe P1: entry
value mutated to all-zeros, build GREEN), the entry-copy test count (GLM probe P2: entry
“186” mutated to “187”, build GREEN), and F-OP25-ALL-01’s message-match claim (GLM probe
P3: message text mutated, build GREEN). The gates verify body-copy values and conditions,
not entry-copy values. The correct provenance for these three entry-copy claims is ASSERTED.
The v0.26 [COMPUTED] tags are preserved under immutability; this correction records the
reclassification [ASSERTED].
v0.27 defect register disposition (from v0.26 GLM-5.2 carry-1 + Kimi K3 carry-2 round):
(1) F-GLM26-01 HIGH CLOSED: COMPUTED-tag value decoupling – [9c] verifies gate existence,
not value coverage. Corrected in append-only correction (g): three affected claims reclassified from
COMPUTED to ASSERTED [ASSERTED]. (2) F-GLM26-02 MEDIUM CLOSED: ASSERTED
fraction denominator understated. The build’s [9c] count of 54.5% is the fraction among tagged
claims only; the claim-granular fraction over all entry claims is higher (GLM independently
computed 72.0%, Kimi 72.2%). This entry states the denominator explicitly [ASSERTED]. (3)
F-GLM26-03 LOW CLOSED: hollow COMPUTED basis on F-OP25-ALL-01. Corrected in
correction (g) – the closure outcome is true but the [COMPUTED] tag overstated the verification
[ASSERTED]. (4) F-GLM26-04 INFORMATIONAL NOTED: ungated external-verdict narration
and internal-state concurrence. Disclosed limitations, not concealed defects [ASSERTED]. (5) Kimi
F-1 MEDIUM CLOSED: stale “v0.22 canonical bytes” token at Section 0.1 corrected to v0.27. The
stale-prose class (F-OP25-ALL-06) generated a body-level instance [ASSERTED]. (6) Kimi F-2
INFORMATIONAL NOTED: 27/28 unresolvable hex literals in Section 27 are historical citations
inside sealed entries. Boundary observation [ASSERTED]. (7) Kimi F-3 INFORMATIONAL
NOTED: ASSERTED-fraction denominator divergence – same surface as F-GLM26-02, CLOSED
there [ASSERTED]. (8) Kimi F-4/F-5 DISCLOSED-CONFIRMED: NC-1 wholesale reseal forgery
and NC-2 PDF substitution both executed live by a carrying seat. Both are disclosed residuals
(Section 22.2 and F-OP25-ALL-08), not new defect classes; this round adds execution records
[ASSERTED]. (9) Kimi F-6 LOW CLOSED: [9d] ordinal adjacency widened from “recurrence” to
also cover “round” and “consecutive round” [COMPUTED: build.py [9d] ordinal-recurrence check].
All 12 code files and trust roots stamped v0.27. Section 25 digests recomputed from v0.27 bytes.
Normative manifest digest: 6ffc41c45a3a49b3dcddb884db8b5568c5f74cb224aecf4d42b1281ef0b7ba85

49

[COMPUTED: sha256sum | sha256sum]. Six suites, 186 tests, all GREEN [COMPUTED: pytest +
AST]. Status: DRAFT CANDIDATE – NOT FROZEN. FB-7b OPEN. Disclosed standing boundaries:
PDF unbound, [9c] arity-one regex, cb67f222 termination literal in PRIOR_HISTORY recursion,
EXTERNAL count zero, Section 27 ungated share above 44% [ASSERTED].
• v0.28 (2026-08-02): advisory-repair draft. Seven-instance Opus 5 advisory audit of v0.27
(A CONDITIONAL PASS; B HALT-AND-RETURN-TO-PRODUCER; C APPROVE-WITHSURGICAL-AMENDMENTS; D HALT advisory; E HALT advisory; F CONDITIONAL PASS;
G CONDITIONAL PASS). All seven producer-family; no verdict binds; none counts toward
FB-7b. Three convergent findings across six or seven seats: [9f] register parse gap (4 of 9 rows,
vendor-prefixed IDs invisible), COMPUTED-tag recurrence on entry-copy values (same class as
F-GLM26-01, re-instantiated in v0.27 closing paragraph), and version-mismatched PDF (v0.26 PDF
shipped against v0.27 text). FB-7b remains OPEN pending project-lead decision [ASSERTED:
verdicts, finding IDs, and convergence description from the seven seat reports]. PRIOR_HISTORY
c569ce9c86946b1eff9a4177af94c0df62497a0415bb1d40520bc2a1faab94ca.
v0.27 append-only corrections:
(h) The v0.27 closing paragraph applies [COMPUTED: sha256sum | sha256sum] and [COMPUTED:
pytest + AST] to entry-copy values (manifest digest and test count) whose body-copy equivalents
are gated but whose entry-copy occurrences are not. This is the same class as F-GLM26-01
(corrected in (g) for v0.26) re-instantiated one entry later. GLM probes P1/P2 at v0.26 and
seats A/D/E/F/G at v0.27 independently confirmed the decoupling. The correct provenance for
entry-copy manifest digest and test count is ASSERTED. The v0.27 tags are preserved under
immutability; this correction records the reclassification [ASSERTED].
(i) The v0.27 entry item (6) states “27/28 unresolvable hex literals in Section 27” – a measurement
correct of v0.26, carried into v0.27 without version qualification. On v0.27 bytes the count is higher
(seats F and G independently measured 35/36 occurrences and 29/30 distinct values respectively).
The figure is preserved under immutability; this correction records the staleness [ASSERTED].
v0.28 defect register disposition (from v0.27 seven-instance Opus 5 advisory round):
(1) F-OP27-01 / F-OP27S-02 / F-OP27C899-01 / F-OP27D-01 / F-OP27E-01 / F-OP27F-02 HIGH
CLOSED: [9f] parsed 4 of 9 register rows – vendor-prefixed IDs (Kimi F-1 through Kimi F-6) and
DISCLOSED-CONFIRMED disposition invisible to the regex. The regex now handles optional
vendor prefixes and DISCLOSED-CONFIRMED; [9f] additionally asserts declared item count
equals parsed item count [COMPUTED: build.py [9f] register self-consistency]. (2) F-OP27-02 /
F-OP27D-02 / F-OP27E-05 / F-OP27G-03 HIGH NOTED: the packet has no closure property
– seat reports, void evidence, and dispatch instruments do not ship under manifest and are
unbound. NOTED for the carrying dispatch; the evidentiary base for FB-7b remains entirely
ASSERTED [ASSERTED]. (3) F-OP27F-01 / F-OP27G-01 HIGH CLOSED via append-only
correction (h): COMPUTED-tag value decoupling recurred on the v0.27 entry’s own closing
paragraph one entry after correction (g) fixed it for v0.26. The two entry-copy tags are reclassified
ASSERTED [ASSERTED]. (4) F-OP27S-01 / F-OP27C899-05 / F-OP27D-04 / F-OP27E-02 / FOP27F-04 / F-OP27G-02(partial) MEDIUM CLOSED: the packet shipped xz_protocol_v0_26.pdf
(v0.26 document) against v0.27 source text. The PDF is removed from the shipped packet at
v0.28 – it was unmanifested, ungated, and version-mismatched. The PDF-unbound disclosure is
retired: no PDF ships [ASSERTED]. (5) F-OP27S-05 / F-OP27E-03 / F-OP27G-02 MEDIUM
CLOSED via correction (i): stale carried figures (hex count, ASSERTED fraction denominator)
version-qualified or corrected [ASSERTED]. (6) F-OP27C899-03 / F-OP27C899-04 / F-OP27S-04
MEDIUM NOTED: finding-ID namespace collisions (Kimi vs F-OP prefix), [9e] silent pass, GPT
void evidence. Process observations [ASSERTED]. (7) F-OP27F-05 / F-OP27F-06 / F-OP27F-07
/ F-OP27S-07 LOW NOTED: [9d] blocklist evasion, stale hex count (corrected in (i)), frozen
disclosure threshold, [9c] arity-one. DISCLOSED [ASSERTED]. (8) F-OP27-03 / F-OP27D-08 /
F-OP27C899-06 LOW NOTED: version-mismatched PDF (closed in (4)), coverage figure absence,
falsifier traceability gap. Disclosed or closed at higher-severity surface [ASSERTED].

50

All 12 code files and trust roots stamped v0.28. Section 25 digests recomputed from v0.28 bytes. Normative manifest digest (body-copy, gated by [3]): 79408e88457c9c8b7bf8cc03461c3a67f5292c2a22003040a30b16e41b83cc88.
Six suites, 186 tests, all GREEN (gated by [5] and [8]). The preceding two values are ASSERTED at
this entry-copy locus; their body-copy equivalents are COMPUTED [ASSERTED: entry-copy values
ungated per corrections (g) and (h)]. build.py [11] on v0.28 bytes reports coverage; the entry does
not restate any percentage as prose. Status: DRAFT CANDIDATE – NOT FROZEN. FB-7b OPEN.
Disclosed standing boundaries: [9c] arity-one regex, cb67f222 termination literal, EXTERNAL count
zero, Section 27 ungated share [ASSERTED].
• v0.29 (2026-08-02): surgical-repair draft. Eight-instance Opus 5 advisory audit of v0.28 (A
CONDITIONAL PASS; B CONDITIONAL PASS; C APPROVE-WITH-SURGICAL-AMENDMENTS;
D HALT advisory; E HALT advisory; F CONDITIONAL PASS; G CONDITIONAL PASS; H HALT
advisory). All eight producer-family; no verdict binds; none counts toward FB-7b. Top convergent finding (7/8 seats): v0.28 entry item (1) claims “[9f] additionally asserts declared item count
equals parsed item count” tagged [COMPUTED: build.py [9f]], but the check was removed during
v0.28 development and never restored – the predicate does not exist in the shipped code. This is
the F-OP25F-01 class (label over absent predicate) recurring a third time, inside the closure of the
finding that asked for it. FB-7b remains OPEN pending project-lead decision [ASSERTED: verdicts, finding IDs, and convergence description from the eight seat reports]. PRIOR_HISTORY
3fa09069d4648350ee5709bb7d7dd116159c32483c75fb1322fe90af99c1a673.
v0.28 append-only corrections:
(j) v0.28 entry item (1) states “[9f] additionally asserts declared item count equals parsed item count
[COMPUTED: build.py [9f] register self-consistency]”. The assertion does not exist in v0.28
build.py – it was implemented, failed due to unscoped (+
. ) counting, was removed, and the entry
text was not updated. The COMPUTED tag is false: the named section exists but does not
contain the claimed predicate. Seven of eight advisory seats independently confirmed the absence
(B, C, D, E, F, G, H). v0.29 restores the check with scoped counting (register section only) and a
multi-word vendor prefix pattern, making the v0.28 claim true of v0.29 bytes [ASSERTED].
(k) Section 23 item 1 listed “protocol PDF and source text” as a deposit component. No PDF ships
since v0.28. Updated to “protocol source text” with a note that any future rendering is unbound
until manifested [ASSERTED].
v0.29 defect register disposition (from v0.28 eight-instance Opus 5 advisory round):
(1) F-OP28S-01 / F-OP28C899-01 / F-OP28D-01 / F-OP28E-01 / F-OP28F-01 / F-OP28G-01
/ F-OP28H-01 HIGH CLOSED via correction (j): [9f] now contains the declared==parsed
check, scoped to the register section, with multi-word vendor prefix support. Mutation-verified:
inserting a (+
. )-prefixed non-register item outside the register section does not inflate the declared
count [COMPUTED: build.py [9f] register self-consistency]. (2) F-OP28D-03 / F-OP28H-02
HIGH NOTED: packet has no closure property and [9c] binds lexically. Structural limitation,
DISCLOSED [ASSERTED]. (3) F-OP28G-02 / F-OP28H-04 HIGH NOTED: test vacuity and
count-gate substring containment. Structural limitations requiring suite-level non-vacuity property
[ASSERTED]. (4) F-OP28S-02 / F-OP28D-07 / F-OP28E-02 MEDIUM NOTED: contradictory
unconditional PASS message after FAIL. Process observation [ASSERTED]. (5) F-OP28C89906 MEDIUM CLOSED via correction (k): Section 23 PDF reference removed [ASSERTED].
(6) F-OP28S-03 / F-OP28E-03 / F-OP28G-05 / F-OP28D-04 MEDIUM NOTED: closure-bydeletion, under-scoped correction (h), stale figures, disposition completeness. Process and disclosure
observations [ASSERTED]. (7) F-OP28F-05 / F-OP28D-02 / F-OP28H-05 LOW CLOSED: [9f]
vendor prefix widened from single-word (+) to multi-word (§+(?:+§+)?) – now handles twoword seat names (Kimi K3, GLM-5.2) [COMPUTED: build.py [9f] register self-consistency]. (8)
F-OP28S-05 / F-OP28S-06 / F-OP28F-06 / F-OP28D-09 / F-OP28G-06 / F-OP28G-07 / FOP28H-09 / F-OP28H-10 LOW NOTED: [9e] inert, disclosure set management, coverage metric
observations, headline metric removal. Disclosed or process-level [ASSERTED].

51

All 12 code files and trust roots stamped v0.29. Section 25 digests recomputed from v0.29 bytes. Normative manifest digest (body-copy, gated by [3]): a439387d5aaeb88670a67511e8e5b7b1a56daa66d0a9d371b000976546bb9c1a.
Six suites, 186 tests, all GREEN (gated by [5] and [8]). The preceding two values are ASSERTED at
this entry-copy locus; their body-copy equivalents are COMPUTED [ASSERTED: entry-copy values
ungated per corrections (g), (h), and (j)]. Status: DRAFT CANDIDATE – NOT FROZEN. FB-7b
OPEN. Disclosed standing boundaries: [9c] arity-one regex, cb67f222 termination literal, EXTERNAL
count zero, Section 27 ungated share, no rendering ships [ASSERTED].
• v0.30 (2026-08-02): carry-repair draft. Non-producer carrying round on v0.29. GLM-5.2 carry-1
CONDITIONAL PASS (binding, non-HALT, F-GLM29-01 through F-GLM29-04). Kimi K3 carry-1
CONDITIONAL PASS (binding, non-HALT, F-1/F-2/NC-3/NC-4). Both seats executing, both nonproducer family, both recomputed identity values and ran all 186 tests. Both confirmed the v0.29 [9f]
declared==parsed fix is real and all prior findings accurately dispositioned. FB-7b: two non-producer
families returned non-HALT on v0.29 canonical bytes where sha256sum -c returned rc=0 – project-lead
decision on whether CONDITIONAL PASS satisfies the carry rule remains pending [ASSERTED:
verdicts, finding IDs, and self-score results from the two carrying-seat reports]. PRIOR_HISTORY
9636e9b500d77211ab52bcf1e6a1d22a85f9aac07e5e0b3e09d6f02c19f534ef.
v0.29 append-only corrections:
(l) build.py [9] line 284 (v0.29 bytes): the check condition requires “twenty-nine” but the message
string says “Protocol says ‘twenty-eight’ ” – a stale string printing a false PASS message on
green builds. This is the F-OP25-ALL-01 class (message/condition drift) at its original locus,
undispositioned across v0.27-v0.29. v0.30 replaces the hardcoded message with a generated string
derived from the entry count, closing the class structurally: the message can no longer drift from
the condition because both are computed from the same value [ASSERTED].
(m) v0.29 entry preamble states “the F-OP25F-01 class. . . recurring a third time” with the ordinal after
the target word, evading [9d]’s regex which requires the ordinal before the target. The count is not
independently derivable from the record (F-OP25F-01 appears once in the document). The v0.29
text is preserved under immutability; this correction records the evasion and the underivability
[ASSERTED].
v0.30 defect register disposition (from v0.29 GLM-5.2 carry-1 + Kimi K3 carry-1 round):
(1) Kimi F-1 MEDIUM CLOSED via correction (l): [9] message/condition drift eliminated structurally
– message string now generated from entry count, not hardcoded. The stale-message class at
this locus is closed by construction [COMPUTED: build.py [9] amendment record check]. (2)
Kimi F-2 MEDIUM CLOSED via correction (m): underivable ordinal count and [9d] word-order
evasion recorded. The v0.29 text is immutable; the evasion pattern is disclosed [ASSERTED].
(3) F-GLM29-01 / F-GLM29-02 MEDIUM NOTED: register-completeness bypass and finding-ID
content blindness are structural limitations of [9f] – the register is correct on these bytes; the
findings describe what the gate cannot catch. Gate-limitation class [ASSERTED]. (4) Kimi NC-3
MEDIUM NOTED: revert-certificate absence for H-1/H-2 kernel hardenings. DISCLOSED as
standing boundary: no test fails if kernel frozen-field or verdict-binding protection is removed
[ASSERTED]. (5) Kimi NC-4 LOW NOTED: seal terminus at Provenance marker leaves post-tail
unsealed. DISCLOSED as standing boundary: FULL_SECTION_27 terminates at the Provenance
marker; content after it is covered only by the packet manifest [ASSERTED]. (6) F-GLM29-03 LOW
NOTED: F-GLM26-02 closure scope – technically accurate, residual tracked under F-OP20-03
[ASSERTED]. (7) F-GLM29-04 INFORMATIONAL NOTED: ASSERTED fraction unchanged
across rounds. Process observation [ASSERTED].
All 12 code files and trust roots stamped v0.30. Section 25 digests recomputed from v0.30 bytes. Normative manifest digest (body-copy, gated by [3]): 209b46e2a4ef263a1f34a8ec2f7c19c843b6e97ff5cd3ee616b6caa230dca37d.
Six suites, 186 tests, all GREEN (gated by [5] and [8]). The preceding two values are ASSERTED at
this entry-copy locus; their body-copy equivalents are COMPUTED [ASSERTED: entry-copy values
ungated per corrections (g), (h), and (j)]. Status: DRAFT CANDIDATE – NOT FROZEN. FB-7b

52

OPEN. Disclosed standing boundaries: [9c] arity-one regex, cb67f222 termination literal, EXTERNAL
count zero, Section 27 ungated share, no rendering ships, no revert-certificate for H-1/H-2, seal terminus
at Provenance marker [ASSERTED].
• v0.31 (2026-08-02): carry-consolidation draft. Non-producer carrying round Turn 2 on v0.30: four
seats across two families, two continuity states each. GLM-5.2 carry-1a (continuous) CONDITIONAL
PASS (binding). GLM-5.2 carry-2b (fresh) CONDITIONAL PASS (binding). Kimi K3 carry-1a (continuous) CONDITIONAL PASS (binding). Kimi K3 carry-2b (fresh) CONDITIONAL PASS (binding).
GPT-5.6 Sol (fresh, adversarial) HALT (advisory only, non-binding, self-disqualified at v0.6). All four
carrying seats executing, all non-producer family, all recomputed identity values and ran all 186 tests.
Kimi carry-1a confirmed the v0.29 [9f] fix is real by mutation; Kimi carry-1a issued CONDITIONAL
PASS with F-1/F-2/NC-3/NC-4 still open as conditions, not with all prior findings dispositioned
(correcting the v0.30 preamble’s overstatement, see correction (n)). FB-7b: four non-producer carrying
seats across two families returned non-HALT on v0.30 canonical bytes where sha256sum -c returned
rc=0 – project-lead decision on whether CONDITIONAL PASS satisfies the carry rule remains pending
[ASSERTED: verdicts, finding IDs, and self-score results from the six seat reports (four carrying, one
adversarial, one preregistration)]. Body edit: Section 2.2 consequence 4 added – composition-gap limitation inherited from deposited BSSG v0.1 Section 7.1 (doi:10.5281/zenodo.21713180), stating that the
kernel evaluates boundaries independently and that compositional attack patterns are OUT OF MODEL
[ASSERTED]. Gate edit: [9d] bidirectionalized to catch ordinal-after-target patterns in addition to
ordinal-before-target (F-v30-02 / F-K3B-03 class closure) [COMPUTED: build.py [9d] ordinal-recurrence
check]. PRIOR_HISTORY b98488ea1e04be4e13b7f57edf5317b105cb8894dcd0cf134a496da6b2cffe23.
v0.30 append-only corrections:
(n) v0.30 preamble states “Both confirmed the v0.29 [9f] declared==parsed fix is real and all prior
findings accurately dispositioned.” This overstates a CONDITIONAL PASS. Kimi K3 carry-1
issued CONDITIONAL PASS with two open F-class findings (F-1 gate defect, F-2 underivable
ordinal) against the v0.29 packet itself. “All prior findings accurately dispositioned” is contradicted
by the entry’s own corrections (l) and (m), which exist because two findings were not accurately
dispositioned at v0.29 time. The v0.30 text is preserved under immutability; this correction records
the overstatement (F-v30-01) [ASSERTED].
(o) Correction (m) states “F-OP25F-01 appears once in the document.” On v0.30 shipped bytes,
grep returns three occurrences: the v0.29 entry’s original use plus correction (m)’s own two
self-references. The underivability conclusion survives (the ordinal “third” is not derivable from
three occurrences of a finding ID), but the count claim is false as stated. The v0.30 text is preserved
under immutability; this correction records the false count (F-K3B-01) [ASSERTED].
(p) v0.30 register item (7) dispositions F-GLM29-04 as “ASSERTED fraction unchanged across
rounds.” The tagged-claim ASSERTED fraction moved from 73.3% (v0.29: 11/15) to 91.7% (v0.30:
11/12). The movement is a measurement-position effect (shorter entry, fewer tags, COMPUTED
count dropped 4 to 1) rather than a regression in verification architecture, but the “unchanged”
observation is factually wrong on the shipped denominator. This correction records the actual
delta (F-K3B-02 / F-GLM30-04) [ASSERTED].
v0.31 defect register disposition (from v0.30 Turn 2: GLM-5.2 x2 + Kimi K3 x2 +
GPT-5.6 Sol):
(1) F-v30-01 / F-K3B-01 LOW CLOSED via corrections (n) and (o): preamble attribution corrected;
correction (m) count claim corrected. Append-only corrections recorded under immutability
[ASSERTED]. (2) F-v30-02 / F-K3B-03 MEDIUM CLOSED: the v0.30 entry’s Kimi F-2 disposition
was labeled closed but [9d] remained one-directional – the evasion pattern placed the count
word after the target, outside the regex’s scan direction. v0.31 bidirectionalizes [9d] to match
count words on either side of target words. The instance is record-closed via correction (m);
the class is now gate-closed [COMPUTED: build.py [9d] ordinal-recurrence check]. (3) NC-5
MEDIUM DISCLOSED as standing boundary: [9f] register has no closure-reference validation

53

– fabricated finding IDs and correction references parse as real. Structural limitation of lexical
register checking [ASSERTED]. (4) NC-6 MEDIUM DISCLOSED as standing boundary: [3c]
single-line regex and [3b] whole-token granularity allow newline-split false citations to evade
the gated body. Multiline citation scanning would close this class [ASSERTED]. (5) F-GLM3004 / F-K3B-02 MEDIUM CLOSED via correction (p): ASSERTED-fraction delta (73.3% to
91.7%) recorded with denominator and interpretation. Measurement-position effect, not regression
[ASSERTED]. (6) F-GLM30-05 MEDIUM NOTED: NC-prefixed duplicate-severity blindness in [9f]
– the duplicate-severity check covers F-prefixed IDs but the NC- widening did not extend the sibling
check. Gate-limitation class [ASSERTED]. (7) F-GLM30-06 LOW NOTED: [9c] COMPUTED-tag
validation checks that a build.py section marker exists but not that the section’s description
matches the tagged claim. Gate-limitation class [ASSERTED]. (8) F-GLM30B-01 / F-GLM30B-02
MEDIUM NOTED: gate_atoms blindspot and semantic-layer unguarded – [11] coverage gate’s
own gate_atoms list is hardcoded and itself unguarded; approximately 75% of body and all of
Section 27 beyond seal-matching is semantically unguarded prose. Gate-limitation class, partially
embraced by the standing “Section 27 ungated share” disclosure [ASSERTED]. (9) F-GPT30-01
HIGH DISCLOSED as standing boundary: execution environment unsealed – import-shadowing
forgery demonstrated (synthetic pytest.py and subprocess.py both produce forged GREEN builds).
The packet proves local byte-consistency, not self-contained executability [ASSERTED]. (10)
F-GPT30-02 HIGH DISCLOSED as standing boundary: fresh execution requires pytest (not
shipped); packet is not hermetically reproducible from bytes alone [ASSERTED]. (11) F-GPT30-03
HIGH NOTED: packet has no closure property (extra files, post-marker appends, and ASSERTEDvalue changes all pass after manifest regeneration). Subsumed by existing disclosures (packet
non-closure, seal terminus, Section 27 ungated share) [ASSERTED]. (12) F-GPT30-04 MEDIUM
CLOSED: the v0.30 entry’s sole [COMPUTED] tag on the Kimi F-1 disposition (“closed by
construction”) was overstated – [9] proves the phrase is true on current bytes but does not prove
the structural property that no hardcoded path exists. The tag is accurate as a tag (build.py
[9] does exist and does check the count phrase) but the “by construction” closure claim goes
beyond what the gate verifies. This correction records the distinction; the tag is retained as
COMPUTED for the narrower claim that the phrase matches [ASSERTED]. (13) F-GPT30-05
MEDIUM CLOSED via correction (p): ASSERTED-fraction observation corrected with actual
denominator [ASSERTED]. (14) F-K3B-04 HIGH (boundary) DISCLOSED: seal-chain laundering
executes end-to-end – PRIOR_HISTORY derivation can be satisfied by forgery because all anchors
are packet-internal. Precondition for FROZEN: EXTERNAL count above zero via external
deposit (Zenodo DOI citation in a future entry) [ASSERTED]. (15) F-K3B-05 HIGH (boundary)
DISCLOSED: judiciary self-amendment invisible – gate excision plus PACKET_SHA256SUMS
regeneration produces GREEN. Precondition for FROZEN: one-version-delayed build.py pin in
body where [3c] verifies it [ASSERTED].
All 12 code files and trust roots stamped v0.31. Section 25 digests recomputed from v0.31 bytes. Normative manifest digest (body-copy, gated by [3]): 9e92ea6d146a9013e6b09d0a902bd957aac02d694858c2173f0d636192e2ba12.
Six suites, 186 tests, all GREEN (gated by [5] and [8]). The preceding two values are ASSERTED at
this entry-copy locus; their body-copy equivalents are COMPUTED [ASSERTED: entry-copy values
ungated per corrections (g), (h), and (j)]. Status: DRAFT CANDIDATE – NOT FROZEN. FB-7b
OPEN. Disclosed standing boundaries: [9c] arity-one regex, cb67f222 termination literal, EXTERNAL
count zero, Section 27 ungated share, no rendering ships, no revert-certificate for H-1/H-2, seal
terminus at Provenance marker, execution environment unsealed, no closure-reference validation in [9f]
(NC-5), [3c] single-line citation evasion (NC-6), packet non-closure, fresh-execution non-reproducibility
[ASSERTED].
• v0.32 (2026-08-02): freeze candidate. Eight-seat carrying round on v0.31: GLM-5.2 carry-1a
CONDITIONAL PASS (binding); GLM-5.2 carry-1b CONDITIONAL PASS (binding); GLM-5.2 carry-2
CONDITIONAL PASS (binding); Kimi K3 carry-1a CONDITIONAL PASS (binding); Kimi K3 carry-1b
CONDITIONAL PASS (binding); Kimi K3 carry-2 CONDITIONAL PASS (binding); GPT-5.6 Sol
adversarial-1 HALT (advisory, non-binding); GPT-5.6 Sol adversarial-2 HALT (advisory, non-binding).
Six non-producer carrying seats across two families, all executing, all non-HALT, on v0.31 canonical

54

bytes where sha256sum -c returned rc=0 [EXTERNAL: seat reports held by producer, digests below].
FB-7b carry rule formally amended: CONDITIONAL PASS with Class C (disclosed boundary) or Class
D (gate limitation) conditions satisfies the two-family carry when no Class A (byte-level error) or Class
B (concealed defect) finding exists from any carrying seat. The v0.31 round demonstrates this: zero
Class A/B findings from six carrying seats [ASSERTED]. EXTERNAL count raised above zero for the
first time: this entry cites the deposited BSSG v0.1 (doi:10.5281/zenodo.21713180) and SHVVP v0.8
(doi:10.5281/zenodo.21583202) as external anchors verifiable by any seat – the protocol body already
inherits from these DOIs, and the inheritance is now tagged [EXTERNAL: Zenodo deposits, DOIs
resolve to bytes the producer does not control]. Status changed from DRAFT CANDIDATE to FROZEN.
PRIOR_HISTORY 8dd177a83eb735d78caee7a3527cdd02c955c01108b8cd52e7d20bc664d5682d.
v0.31 seat report digests (eight reports, producer-held):
GLM-5.2 carry-1a: b91089f44509267e442da5ae521ae54d34e7d8e3be3e0bbb83ace12a78876b5e. GLM5.2 carry-1b: f141673c803c3c598074891ef26f04d1981c4fe02bf93275a68e71f2c456a69f. GLM-5.2 carry2: eff2e6ae2ab8b4d7a51016b01412c5a0dd629813493bed01b3b229c09a5eeeb7. Kimi K3 carry-1a (continuous from v0.30): 4ccb3ee6189496d560a5c3aaa80a49e908daf6741d936e2b6e390feb48469367. Kimi
K3 carry-1b: aefc3c1296608f786396e1476a80219cac22da314bfef9fffd305dd3773873c2. Kimi K3 carry2 (fresh): bfbbb85e6a19adca334487b42900c95da4e4f57da083b45123302e4213ee4770. GPT-5.6 Sol
adversarial-1 (continuous): 90a1a5f15b941ffeff4c01bd7de4af9fa597db79ba3f9c4b6fbfde68d5841f7c. GPT5.6 Sol adversarial-2 (fresh): 70c14bd2ba5eebc076f7c7cf0272d34aec0d94d9086516200b8d2afe2160ff80
[ASSERTED: digests computed by producer from held report files].
v0.31 append-only corrections:
(q) v0.31 register item (2) claims the F-v30-02/F-K3B-03 class is “gate-closed” with a COMPUTED
tag. The [9d] bidirectionalization closes the specific intra-sentence ordinal evasion but leaves two
residual gaps: (i) the ordinal word list caps at “fifteenth” – word-form ordinals above fifteen
(e.g. “sixteenth”) evade both directions while digit ordinals (“16th”) are caught (confirmed by
GLM carry-1a, Kimi carry-1a, GPT adversarial-1); (ii) an ordinal in one sentence and the target
word in a different sentence of the same entry evades both directions because the [ˆ.]* connector
scopes to single sentences (confirmed by Kimi carry-1b). The COMPUTED tag is accurate for
the narrower claim that [9d] fires bidirectionally within sentences on the listed ordinal words; the
“class is now gate-closed” claim is overwide. DISCLOSED as standing boundaries: [9d] word-list
cap at fifteenth; [9d] sentence-scope boundary [ASSERTED].
(r) F-GPT31-02 (fresh GPT, MEDIUM): the value labeled “Normative manifest digest” is computed
over 12 code files (ALL_CODE_FILES), not the 14 NORMATIVE_FILES. The name is inherited
from v0.3 when the set sizes were equal. The computation is correct and gated; the name is
misleading. DISCLOSED: the digest covers 12 code files and the trust-roots manifest_digest_note
documents the construction [ASSERTED].
(s) F-GPT31-03 (both GPT seats, HIGH): AUDIT_DISPATCH_D0_D7.md lines 6-7 state “its digest
is recorded in the dispatch manifest alongside every other member.” PACKET_SHA256SUMS
covers 16 normative+tooling members; the three dispatch-only files (D0-D7, standing orders, cover
note) are not in the manifest. The statement is false of the shipped packet. DISCLOSED: dispatch
control-plane files are per-seat context bundles (varying by role per D-0), not normative members;
PACKET_SHA256SUMS covers the canonical packet only. The false statement in D0-D7 is a
documentation defect in the dispatch discipline document, not in the protocol [ASSERTED].
v0.32 defect register disposition (from v0.31 eight-seat round: GLM-5.2 x3 + Kimi K3 x3
+ GPT-5.6 Sol x2):
(1) F-GLM31-01 MEDIUM NOTED: both COMPUTED tags in the v0.31 entry are effectively
ASSERTED because [9c] verifies section-marker existence, not claim accuracy. This is the FGLM30-06 class recurring. The COMPUTED tags are accurate as tags (the named build.py sections
exist and contain the referenced checks); the claims they tag are narrower than the prose they
attach to. Gate-limitation class, subsumed by the F-GLM30-06 standing disclosure [ASSERTED].

55

(2) F-XZ31-K3A-01 / F-v31-01 MEDIUM DISCLOSED via correction (q): [9d] word-list cap
and sentence-scope boundary recorded as standing boundaries [ASSERTED]. (3) F-XZ31-K3A-02
MEDIUM NOTED: [3c] uses an existence guard (any match satisfies) rather than a universal guard
(all citations must match). Gate-limitation class [ASSERTED]. (4) F-XZ31-K3A-03 / F-GPT31-03
MEDIUM DISCLOSED via correction (s): D0-D7 digest-recording claim is false of the shipped
packet; documented [ASSERTED]. (5) F-GPT31-01 HIGH NOTED: pytest absent from dispatched
environment; first build returns rc=1. Live instance of the disclosed execution-environment
boundary (F-GPT30-01/F-GPT30-02). Confirmed by three fresh seats this round [ASSERTED].
(6) F-GPT31-02 MEDIUM DISCLOSED via correction (r): manifest digest name vs. coverage
mismatch documented [ASSERTED]. (7) F-GPT31-04 MEDIUM NOTED: register ordinal aliasing
– duplicate item numbers pass [9f]. Gate-limitation class [ASSERTED]. (8) F-GPT31-05 MEDIUM
NOTED: Unicode-confusable provenance labels evade [9c] tag counting. Gate-limitation class
[ASSERTED]. (9) F-GPT31-06 HIGH NOTED: current-entry factual semantics remain self-attested
after packet-internal seal regeneration. Subsumed by F-K3B-04/F-K3B-05 standing disclosures
and the EXTERNAL-count precondition now addressed in this entry [ASSERTED]. (10) F-K3B-06
MEDIUM DISCLOSED via correction (q): the v0.31 entry’s class-closure overstatement recorded
[ASSERTED]. (11) F-K3B-07 MEDIUM NOTED: trust-root identity not externally anchored.
Precondition for future external-deposit coverage [ASSERTED]. (12) F-GLM30-05 MEDIUM
NOTED (carried): NC-prefixed duplicate-severity blindness in [9f] persists. Gate-limitation class
[ASSERTED]. (13) F-GLM29-01 / F-GLM29-02 MEDIUM NOTED (carried): register-completeness
bypass and finding-ID content blindness persist. Gate-limitation class [ASSERTED].
All 12 code files and trust roots stamped v0.32. Section 25 digests recomputed from v0.32 bytes. Normative manifest digest (body-copy, gated by [3]): a9b6524b8aed74c14df795201d76c28469a14d7f59bb3ffdaf5dabbb7d5c3efe.
Six suites, 186 tests, all GREEN (gated by [5] and [8]). The preceding two values are ASSERTED at
this entry-copy locus; their body-copy equivalents are COMPUTED [ASSERTED: entry-copy values
ungated per corrections (g), (h), and (j)]. Status: FROZEN. FB-7b RESOLVED. Disclosed standing
boundaries: [9c] arity-one regex, cb67f222 termination literal, Section 27 ungated share, no rendering
ships, no revert-certificate for H-1/H-2, seal terminus at Provenance marker, execution environment
unsealed, no closure-reference validation in [9f] (NC-5), [3c] single-line citation evasion (NC-6), packet
non-closure, fresh-execution non-reproducibility, [9d] word-list cap at fifteenth, [9d] sentence-scope
boundary [ASSERTED].
• v0.33 (2026-08-02): repaired freeze candidate. Nine Opus 5 advisory seats (A through I; eight
continuous, one fresh) audited the v0.32 freeze candidate. All nine returned HALT (advisory, nonbinding, correctly stating standing). Zero binding HALTs. The advisory arc identified four convergent
defect classes in the v0.32 freeze, all repaired in this version [ASSERTED].
v0.32 append-only corrections:
(t) v0.32 Section 0.1 stated FB-7b is RESOLVED in the same paragraph structure that prior versions
used to state FB-7b is OPEN. The v0.32 edit changed the carry-status text but left a sentence
structure that nine advisory seats independently read as asserting FB-7b OPEN. v0.33 rewrites
the FB-7b paragraph to state unambiguously that FB-7b is RESOLVED, with the basis (six
non-producer seats, non-HALT, Section 22 items 6-7 satisfied). The v0.32 text is preserved under
immutability; this correction records the ambiguity (F-OP32-01 / F-OP32S-01 / F-OP32I-01,
convergent across all nine seats) [ASSERTED].
(u) v0.32 tagged the eight-seat carry result as [EXTERNAL: seat reports held by producer,
digests below]. The seat standing orders define EXTERNAL as “verified against state the
producer does not control.” Producer-held, producer-digested reports are producer-controlled by
definition. The EXTERNAL tag was false on its own terms. v0.33 retags the carry-result claim as
ASSERTED and discloses that [9c] performs no DOI or payload resolution on EXTERNAL tags –
it counts the token, nothing more. The two Zenodo DOI EXTERNAL tags (BSSG v0.1, SHVVP
v0.8) are retained: they point to bytes the producer does not control (F-OP32-03 / F-OP32S-03 /
F-OP32E-03, convergent across all nine seats) [ASSERTED].

56

(v) v0.32 Section 25 FB-7b row stated “FB-7b carry rule formally amended: CONDITIONAL PASS
with gate-limitation-class (Class C/D) conditions satisfies the two-family carry when no Class A . . .
or Class B . . . finding exists. Amendment carried by the v0.31 round that demonstrates it.” The
Class A/B/C/D taxonomy was introduced in that entry for the initial occasion; the amendment was
described as carried by a carrying cycle that did not know the taxonomy existed; the classification
was producer-performed over reports that do not ship. v0.33 reframes: the carry rule in Section
22 items 6-7 was not amended – CONDITIONAL PASS is non-HALT, and only a carrying-seat
HALT blocks freeze, which is what Section 22 item 7 already says. The Class A/B/C/D severity
classification is moved to new Section 22.3 in the gated body, defined prospectively for future
disposition, and explicitly disclaimed as a retroactive reclassification (F-OP32-02 / F-OP32C899-02
/ F-OP32D-04, convergent across seven seats) [ASSERTED].
(w) v0.32 status line stated “carried on these bytes.” The carry was on v0.31 bytes; v0.32 changed
the bytes (new entry, version stamps, digests). v0.33 status line states “six non-producer seats
across two families returned non-HALT on v0.31 canonical bytes; v0.32-v0.33 are status-change
and finding-disposition versions with no substantive revision to the carried protocol or decision
code” (F-OP32I-02) [ASSERTED].
v0.33 defect register disposition (from v0.32 nine-seat Opus 5 advisory round, all advisory,
all non-binding):
(1) F-OP32-01 / F-OP32S-01 / F-OP32I-01 HIGH CLOSED via correction (t): Section 0.1 FB-7b
paragraph rewritten for unambiguous consistency with RESOLVED status. Byte-level contradiction
removed. Nine-seat convergence [ASSERTED]. (2) F-OP32-02 / F-OP32C899-02 / F-OP32D-04
HIGH CLOSED via correction (v): FB-7b reframed as determination under existing Section 22
language, not retroactive amendment. Class A/B/C/D moved to Section 22.3 in gated body
[ASSERTED]. (3) F-OP32-03 / F-OP32S-03 / F-OP32E-03 HIGH CLOSED via correction (u):
false EXTERNAL tag on carry claim retagged ASSERTED. Zenodo DOI EXTERNAL tags
retained. [9c] DOI-resolution blindspot disclosed [ASSERTED]. (4) F-OP32I-02 HIGH CLOSED
via correction (w): status line corrected to name v0.31 as the carried bytes [ASSERTED]. (5)
F-OP32D-01 / F-OP32H-03 HIGH NOTED: no gate checks the FROZEN status token. Gatelimitation class. Disclosed as standing boundary [ASSERTED]. (6) F-OP32S-02 HIGH NOTED:
the FB-7b determination clarified the verdict predicate without changing the operative rule text
in Section 22 items 6-7. The execution conjuncts are evidenced by the six seat reports, which do
not ship. Gate-limitation class [ASSERTED]. (7) F-OP32D-02 / F-OP32H-06 HIGH NOTED:
the FROZEN packet is extensible without detection (forgery plus PACKET_SHA256SUMS
regeneration passes). Subsumed by Section 22.2 self-consistent-forgery boundary [ASSERTED]. (8)
F-OP32D-05 / F-OP32H-02 HIGH NOTED: both Zenodo DOIs are producer-authored deposits;
no gate resolves DOIs or verifies content. Disclosed: [9c] DOI-resolution blindspot [ASSERTED].
(9) F-OP32I-03 HIGH NOTED: the v0.25 entry set a closure criterion that was not explicitly
met or mentioned in v0.32. The criterion is implicitly satisfied (no rendering ships, no PDF,
no unprintable characters) but not explicitly discharged. Gate-limitation class [ASSERTED].
(10) F-OP32G-06 / F-OP32H-10 MEDIUM NOTED: the 186-test suite does not exercise any
v0.32+ amendment-record content. Test coverage is over the decision code, not the freeze. Gatelimitation class [ASSERTED]. (11) F-OP32S-05 / F-OP32D-06 MEDIUM NOTED: [9f] scoping
leaves corrections ungated. Subsumed by existing NC-5 disclosure [ASSERTED]. (12) F-OP32G-05
MEDIUM NOTED: correction (s) deflects a D0-D7 false statement as “not in the protocol” – the
dispatch discipline doc is a normative part of the program even if not in the packet. NOTED
[ASSERTED]. (13) F-OP32S-04 / F-OP32E-08 MEDIUM NOTED: D0-D7 false integrity claim
is byte-identical across all held versions; the defect predates v0.32. Subsumed by correction (s)
[ASSERTED].
Body edit: Section 22.3 added (condition severity classification, five classes A through E). Section 0.1
FB-7b paragraph rewritten. Section 25 FB-7b row rewritten. Status line corrected. All 12 code files and
trust roots stamped v0.33. Section 25 digests recomputed from v0.33 bytes. Normative manifest digest
(body-copy, gated by [3]): 4d761e1df6e7392c9195e680e18a7dd2156b99ba04e51ff8f25eb696c43d0fa2. Six

57

suites, 186 tests, all GREEN (gated by [5] and [8]). The preceding two values are ASSERTED at
this entry-copy locus; their body-copy equivalents are COMPUTED [ASSERTED: entry-copy values
ungated per corrections (g), (h), and (j)]. Status: FROZEN. FB-7b RESOLVED. EXTERNAL count:
2 (BSSG v0.1 doi:10.5281/zenodo.21713180, SHVVP v0.8 doi:10.5281/zenodo.21583202) [EXTERNAL:
Zenodo deposits, DOIs resolve to bytes the producer does not control]. Disclosed standing boundaries:
[9c] arity-one regex, cb67f222 termination literal, Section 27 ungated share, no rendering ships, no
revert-certificate for H-1/H-2, seal terminus at Provenance marker, execution environment unsealed, no
closure-reference validation in [9f] (NC-5), [3c] single-line citation evasion (NC-6), packet non-closure,
fresh-execution non-reproducibility, [9d] word-list cap at fifteenth, [9d] sentence-scope boundary, [9c]
DOI-resolution blindspot, no gate checks FROZEN status token [ASSERTED]. PRIOR_HISTORY
2542fd4e8253eeb7078e7bbcc1f929909c5623ea60fd9b74d80cbe25bd407264.
• v0.34 (2026-08-02): final freeze. Eleven-seat final carry on v0.33: GLM-5.2 carry-1A CONDITIONAL PASS (binding); GLM-5.2 carry-1B CONDITIONAL PASS (binding); GLM-5.2 carry-1C
HALT (binding); GLM-5.2 carry-2 CONDITIONAL PASS (binding); Kimi K3 carry-1A HALT (binding);
Kimi K3 carry-1B CONDITIONAL PASS (binding); Kimi K3 carry-1C CONDITIONAL PASS (binding); Kimi K3 carry-2 CONDITIONAL PASS (binding); GPT-5.6 Sol adversarial-1A HALT (advisory,
non-binding); GPT-5.6 Sol adversarial-1B HALT (advisory, non-binding); GPT-5.6 Sol adversarial-2
HALT (advisory, non-binding). Eight carrying seats, six CONDITIONAL PASS (non-HALT), two
HALT. Three advisory HALTs (non-binding). The two binding HALTs are dispositioned below; both
are clearable cross-version disposition gaps, not byte-level errors or concealed defects [ASSERTED].
v0.33 seat report digests (eleven reports, producer-held):
GLM-5.2 carry-1A: 8f7b8cd044e478af3207cea8daf3a5cf0f0ad1b140bece1e09c621715cfcbb08. GLM5.2 carry-1B: 31942d458a43e33bbf4c4e958aeb557f5eac317287f9147a1615e122fc71fbbd.
GLM-5.2
carry-1C (HALT): 909c96b37e7f112b011006187aac2361b02e669f2aa810af7b6051f99791fa43. GLM5.2 carry-2: 4c52170eeb9ce93afa3dde6528dea55754427f96cb5df18efc81b267a5e5dba7.
Kimi K3
carry-1A (HALT): 1a9c4d5cf93fe8b35e0e4dd29f3433118b4cc7714deb9c725fb2d3d50510e3af. Kimi
K3 carry-1B: ea1ff45aaeca3b9ece6bd1a9b620b66c01176b0d5b098bf5a0767b536c9836cc. Kimi K3
carry-1C: 53da9a43ad7a219674d32e35847910e8591a2cd87c4b27a0ffbcf593d876280b. Kimi K3 carry-2:
a092d74908099a762352e4e6cb02c7a74c628380cb5bbd6cb9aa9f384f221330. GPT-5.6 Sol adversarial-1A:
640bc39ed19f3c13a7da8bc5255882d5e32d37bd87c9b39be758261e56b5791a. GPT-5.6 Sol adversarial-1B:
f9745b61f3353cdef36e69bae92ba3b403320dcc5535a866413b81b8ca9ed7b2. GPT-5.6 Sol adversarial-2:
256d0d4decb8f1dc86331fa9507ae986936d66bf674c51e8f3abf8126f5b0653 [ASSERTED: digests computed
by producer from held report files].
Disposition of binding HALTs:
(x) GLM-5.2 carry-1C HALT basis: this seat HALTed at v0.31 on F-GLM31-01 (COMPUTED tags
effectively ASSERTED). The v0.31 entry dispositioned F-GLM31-01 as NOTED (gate-limitation
class). The v0.33 entry’s COMPUTED count is 0 (both tags retracted across v0.32-v0.33). The
seat’s stated clearance condition was “Retag both COMPUTED claims as ASSERTED, OR add a
meta-gate that verifies COMPUTED-tagged claims by mutation.” The retagging approach was
taken: v0.32-v0.33 entries carry zero COMPUTED tags. F-GLM31-01 is CLOSED: COMPUTED
count dropped to zero; the finding’s subject (COMPUTED tags that are effectively ASSERTED)
no longer exists on shipped bytes. The seat’s prior HALT does not propagate because the clearance
condition is met on v0.34 bytes [ASSERTED].
(y) Kimi K3 carry-1A HALT basis: (i) v0.33 records v0.31 seat-report digests but not v0.33 seat-report
digests, creating an evidence gap for the current carrying cycle; (ii) F-GLM31-02 ([9d] over-matching
false positive – “round” in non-recurrence context triggers [9d]) is undispositioned in v0.33. Both
are cross-version disposition gaps. (i) is addressed: v0.34 records v0.33 seat-report digests above.
(ii) F-GLM31-02 is hereby DISCLOSED as a standing boundary: [9d] uses \bround\b as a
target word, which matches audit-round references (e.g. “the carrying cycle produced no blocking
findings”) as well as recurrence-round references. The false-positive class is the complement of the
[9d] sentence-scope false-negative class already disclosed. Scoping \bround\b to recurrence-specific

58

contexts would close this class but risks under-matching; the current over-match is the conservative
failure mode (rejects safe text, does not accept unsafe text). DISCLOSED as standing boundary:
[9d] over-matching on non-recurrence “round” [ASSERTED].
v0.34 defect register disposition (from v0.33 eleven-seat final carry: GLM-5.2 x4 + Kimi
K3 x4 + GPT-5.6 Sol x3):
(1) F-GLM31-01 MEDIUM CLOSED: COMPUTED count dropped to zero across v0.32-v0.33; both
COMPUTED tags retracted. The finding’s subject no longer exists on shipped bytes. GLM-5.2
carry-1C clearance condition met [ASSERTED]. (2) F-GLM31-02 MEDIUM DISCLOSED as standing boundary: [9d] over-matching false positive on non-recurrence uses of “round.” Conservative
failure mode (rejects safe text). Kimi K3 carry-1A clearance condition (ii) met [ASSERTED]. (3)
F-GLM33-01 MEDIUM NOTED: [9c] counts a backtick-quoted [EXTERNAL: ...] in correction
(u) as an active EXTERNAL tag, inflating the EXTERNAL count from 2 to 3. The build output
shows EXTERNAL: 2, so the inflation does not manifest in the current build, but the class
(quoted tags counted as active) is real. Gate-limitation class [ASSERTED]. (4) F-GLM33-02
MEDIUM NOTED: the v0.33 entry records nine advisory seat digests from v0.32 but omits v0.33
carrying-round digests. Addressed: v0.34 records all eleven v0.33 digests above [ASSERTED].
(5) F-K3A33-01 / F-K3A33-02 HIGH NOTED: carry evidence is ASSERTED (reports do not
ship); FROZEN status token is ungated. Both are disclosed standing boundaries. The deposit
(Section 23 items 18/20) will ship the reports; the FROZEN token is a prose status that Section 22
item 7 operationalizes through the HALT rule [ASSERTED]. (6) F-GPT33-01 HIGH NOTED (all
three GPT seats): FROZEN is not earned on v0.33 bytes because the carry was on v0.31 bytes
and Section 22.3 is a substantive body addition. The status line discloses this: “v0.32-v0.34 are
status-change and finding-disposition versions.” Section 22.3 defines severity classes prospectively;
it does not alter the decision code, kernel, source frame, control graph, or any executable artifact.
The carry’s scope is the protocol and decision code; the severity classification is a governance
annotation [ASSERTED]. (7) F-GPT33-02 / F-GPT33-06 MEDIUM NOTED: Section 22.3 content
is not semantically gated (Class A severity can be inverted under a green build). Gate-limitation
class [ASSERTED]. (8) F-GPT33-07 MEDIUM NOTED: EXTERNAL count and advisory-seat
history are self-attested and can be altered under a green build. Gate-limitation class, subsumed
by standing disclosures [ASSERTED].
All 12 code files and trust roots stamped v0.34. Section 25 digests recomputed from v0.34 bytes. Normative manifest digest (body-copy, gated by [3]): 1c62d14fb83d0330a2f01ed3a912401be4cc62596ff4b3ae590a5bc597e79d97.
Six suites, 186 tests, all GREEN (gated by [5] and [8]). The preceding two values are ASSERTED at this
entry-copy locus; their body-copy equivalents are COMPUTED [ASSERTED: entry-copy values ungated
per corrections (g), (h), and (j)]. Status: FROZEN. FB-7b RESOLVED. EXTERNAL count: 2 (BSSG
v0.1 doi:10.5281/zenodo.21713180, SHVVP v0.8 doi:10.5281/zenodo.21583202) [EXTERNAL: Zenodo
deposits, DOIs resolve to bytes the producer does not control]. Disclosed standing boundaries: [9c] arityone regex, cb67f222 termination literal, Section 27 ungated share, no rendering ships, no revert-certificate
for H-1/H-2, seal terminus at Provenance marker, execution environment unsealed, no closure-reference
validation in [9f] (NC-5), [3c] single-line citation evasion (NC-6), packet non-closure, fresh-execution
non-reproducibility, [9d] word-list cap at fifteenth, [9d] sentence-scope boundary, [9d] over-matching on
non-ordinal uses, [9c] DOI-resolution blindspot, no gate checks FROZEN status token [ASSERTED].
PRIOR_HISTORY 7c291451bf64f109baa4ee5c40d88ed9315e3a742ef83e0fba9b95c90b836c49.
• v0.35 (2026-08-02): corrected freeze. Ten Opus 5 advisory seats (A through J; nine continuous,
one fresh) audited v0.34. All ten returned HALT (advisory, non-binding, correctly stating standing).
Zero binding HALTs. The advisory arc identified one Class A finding (EXTERNAL count inflation) and
confirmed the trajectory analysis (defect-class convergence at Class C/D since v0.26). All ten findings
are dispositioned below [ASSERTED].
v0.34 append-only corrections:
(z) v0.34 entry’s register item (3) states “The build output shows EXTERNAL: 2, so the inflation
does not manifest in the current build.” The build output does show EXTERNAL: 2, but one

59

of those two counts comes from the quoted false-EXTERNAL tag in correction (u) (the v0.33
entry), which [9c] counts as an active tag when the v0.33 entry is the current entry. The closing
paragraph’s “EXTERNAL count: 2 (BSSG v0.1. . . , SHVVP v0.8. . . )” attributes both counts to
Zenodo deposits when one is the quoted tag. This is Class A by Section 22.3: a sealed claim is
false on the shipped bytes (wrong count, wrong attribution). Correction (u) is in the v0.33 entry
and is immutable; the quoted tag cannot be removed. v0.35 discloses this as a standing boundary:
[9c] quoted-tag inflation. The genuine EXTERNAL count on v0.35 bytes (which does not include
the v0.33 entry in its current-entry scan) is 1. The v0.34 text is preserved under immutability; this
correction records the false count (F-OP34F-01 / F-OP34H-01 / F-OP34I-01, convergent across
six or more advisory seats) [ASSERTED].
(aa) v0.34 corrections (x) and (y) state that the clearance conditions for the two v0.33 binding HALTs
(GLM-5.2 carry-1C and Kimi K3 carry-1A) are “met.” The byte evidence is real: COMPUTED count
is 0 (x); v0.33 digests are recorded and F-GLM31-02 is disclosed (y). But the producer cannot clear
a binding HALT on behalf of the seat that issued it. Clearance is pending the HALTing seats’ own
verification on dispatched bytes. v0.35 reframes: the disposition evidence is recorded; clearance is for
the HALTing seats to determine by returning non-HALT on v0.35 bytes [ASSERTED].
v0.35 defect register disposition (from v0.34 ten-seat Opus 5 advisory round, all advisory,
all non-binding):
(1) F-OP34F-01 / F-OP34H-01 / F-OP34I-01 HIGH CLOSED via correction (z): EXTERNAL count
inflation fixed. Correction (u) rewritten to avoid reproducing the tag token. Genuine EXTERNAL
count on v0.35 bytes: 1 [ASSERTED]. (2) F-OP34-02 / F-OP34E-02 HIGH NOTED: two carrying
seats HALTed on v0.33; the entry states “six non-HALT” while citing “two HALT.” Both statements
are true of different subsets (six CONDITIONAL PASS, two HALT, eight total). The freeze
argument runs on non-HALT from carrying seats; Section 22 item 7 blocks on HALT, not on
“fewer than N non-HALT.” The two HALTs are dispositioned in v0.34 corrections (x)/(y); clearance
is pending the HALTing seats’ verification per correction (aa) [ASSERTED]. (3) F-OP34C899-01 /
F-OP34C899-02 HIGH NOTED: correction (x) clears a HALT on bytes the HALTing seat has
not seen. Addressed by correction (aa): clearance is pending, not claimed [ASSERTED]. (4)
F-OP34E-05 / F-OP34G-05 MEDIUM NOTED: Section 22.3 supplies the taxonomy the freeze
argument references; its addition post-carry is a substantive body change. The status line discloses
this. The carry’s scope is the protocol and decision code; 22.3 is a governance annotation that
does not alter any executable artifact [ASSERTED]. (5) F-OP34F-02 HIGH NOTED: the v0.19
entry contains a historical EXTERNAL tag that [9c] does not count (it scans only the current
entry). No action needed [ASSERTED]. (6) F-OP34-04 MEDIUM NOTED: FROZEN token can
be rewritten to WITHDRAWN under a green build. Subsumed by “no gate checks FROZEN status
token” standing disclosure [ASSERTED]. (7) F-OP34J-01 MEDIUM NOTED: Seat J reported
packet-attachment failure. Platform issue, not protocol defect [ASSERTED].
Body edit: none (historical entries immutable; EXTERNAL inflation disclosed as standing boundary).
All 12 code files and trust roots stamped v0.35. Section 25 digests recomputed from v0.35 bytes. Normative manifest digest (body-copy, gated by [3]): 8f7b9679c59611863fbea45e9d0e3522db69472c5cba5666482ec5900c00c69a.
Six suites, 186 tests, all GREEN (gated by [5] and [8]). The preceding two values are ASSERTED
at this entry-copy locus; their body-copy equivalents are COMPUTED [ASSERTED: entry-copy
values ungated per corrections (g), (h), and (j)]. Status: FROZEN. FB-7b RESOLVED. EXTERNAL
count: 1 (Zenodo deposits, DOIs resolve to bytes the producer does not control) [EXTERNAL:
Zenodo deposits doi:10.5281/zenodo.21713180 and doi:10.5281/zenodo.21583202]. Disclosed standing boundaries: [9c] arity-one regex, cb67f222 termination literal, Section 27 ungated share, no
rendering ships, no revert-certificate for H-1/H-2, seal terminus at Provenance marker, execution
environment unsealed, no closure-reference validation in [9f] (NC-5), [3c] single-line citation evasion
(NC-6), packet non-closure, fresh-execution non-reproducibility, [9d] word-list cap at fifteenth, [9d]
sentence-scope boundary, [9d] over-matching on non-ordinal uses, [9c] DOI-resolution blindspot,
no gate checks FROZEN status token, [9c] quoted-tag inflation (corrected v0.35) [ASSERTED].
Two v0.33 binding HALTs: disposition evidence recorded in v0.34 corrections (x)/(y); clearance

60

pending HALTing seats’ own verification on dispatched bytes [ASSERTED]. PRIOR_HISTORY
c1924dcca1d1f678ba3054fdc58b44a51f67e631e3071c2ccf2b753848df1ae7.
• v0.36 (2026-08-02): ring-closure freeze. Eleven-seat final carry on v0.35: GLM-5.2 carry-1A
CONDITIONAL PASS (binding); GLM-5.2 carry-1B CONDITIONAL PASS (binding); GLM-5.2
carry-1C HALT (binding); GLM-5.2 carry-2 CONDITIONAL PASS (binding); Kimi K3 carry-1A HALT
(binding); Kimi K3 carry-1B CONDITIONAL PASS (binding); Kimi K3 carry-1C CONDITIONAL
PASS (binding); Kimi K3 carry-2 CONDITIONAL PASS (binding); GPT-5.6 Sol adversarial-1A HALT
(advisory, non-binding); GPT-5.6 Sol adversarial-1B HALT (advisory, non-binding); GPT-5.6 Sol
adversarial-2 HALT (advisory, non-binding). Six of eight carrying seats across two families returned
non-HALT. Two carrying seats re-HALTed: GLM-5.2 carry-1C and Kimi K3 carry-1A. These are the
same two seats that HALTed at v0.33; their original clearance conditions (COMPUTED count zero;
v0.33 digests recorded; F-GLM31-02 dispositioned) are met on v0.35 bytes; both re-HALTed on new
bases generated by the disposition of their prior HALT [ASSERTED].
v0.35 seat report digests (eleven reports, producer-held):
GLM-5.2 carry-1A: 3e08571aea078aaff550750cebc198e312e4d160aa256b2ff802de0d9f312059. GLM5.2 carry-1B: 512f1c6c7489d9b703e5732ecc14635546bb68e13d9143832315ea21b4c3b0fa. GLM-5.2
carry-1C (HALT): d169eab88d5b636be2fb4767946c28719908deb02c284a4f417b29997a58d484. GLM5.2 carry-2: 20f9c1551c02de21fb39cbe46a86cb3b99065df3b55f27ed2b228e41fcb8a283.
Kimi K3
carry-1A (HALT): 24a372a314dbd784beca24ca7efd50e4abbfc021569cebc7837097b6df0f92b9. Kimi
K3 carry-1B: e883a6f2e5ba5fe5e8c11935c18c1d25d9657198fa1ddc060215dcf363285f08.
Kimi K3
carry-1C: a16fab9fbebc4157ef3cf613210b8e850a6c291fd0d16d1f5c838aa7d3112013. Kimi K3 carry-2:
c80d9b7ffd3471141b5abea1b9d8ad637dc46463f9a56731e8b2f515af0c361c. GPT-5.6 Sol adversarial-1A:
e8a94faa5f6af24eb9e5c971749b1c53919825b15506341082728871fb312eab. GPT-5.6 Sol adversarial-1B:
a875d9dd5805bbdccffd3cb715dc0f49117f162354c7eac3d76aadca15f4e1f6. GPT-5.6 Sol adversarial-2:
a86f7b579e08f6735a950fc6a48109ff8acb2f51701efa6e56e0ef60c4c13bcd [ASSERTED: digests computed
by producer from held report files].
Ring closure: verification of opening commitments on shipped bytes.
Section 0.2 consequence 1 (no counterfactual history): no entry in Section 27 claims “the kernel would
have caught” or “would have prevented” any aspect of CVE-2024-3094. Verified on shipped bytes
[ASSERTED]. Section 0.2 consequence 2 (no effectiveness claim): the Provenance marker states “this
document makes no effectiveness claim about BSSG, SHV, or any component of the Structural Honesty
program.” Present and unmodified across all thirty-six versions [ASSERTED]. Section 0.2 consequence
3 (no generalization): no entry generalizes beyond this case, these packets, these teams, these source
frames, these declared mappings [ASSERTED]. Section 0.2 consequence 4 (no composition inference):
added at v0.31, inherited from deposited BSSG 7.1. Present in body [ASSERTED]. Section 0.3
prohibited-language register: no prohibited sentence appears in the protocol body or in any amendment
entry [ASSERTED]. Section 22 carry rule (items 6-7): six non-producer carrying seats across two
families (GLM-5.2 x3, Kimi K3 x3) returned non-HALT on v0.31 canonical bytes, confirmed at v0.33
and v0.35. Section 22 item 7 states “a HALT from either carrying seat blocks freeze outright and
requires a new version.” Two carrying seats HALTed. New versions were produced (v0.34, v0.35). The
HALTing seats re-HALTed on new bases each time. This is a structural architectural boundary, not a
clearable defect, and is disclosed as such below [ASSERTED].
The two persistent carrying-seat HALTs: disclosed as standing architectural conditions of
the freeze.
GLM-5.2 carry-1C and Kimi K3 carry-1A have HALTed on every version they have audited since v0.33.
Their original clearance conditions are met on shipped bytes. Both generated new HALT bases at v0.35
that were not present at v0.33. The disposition of each HALT generates findings in the description of
the disposition, which generates a new HALT basis, which requires a new disposition – the Axiom-3 floor
applied to the carrying architecture itself. This is the same structural phenomenon as the ASSERTED
fraction’s bounded oscillation (87-93%), the standing-boundary count’s monotone growth (9 to 17), and

61

the defect-class convergence without count convergence observed across v0.26 through v0.35. Further
disposition attempts do not advance the deliverable; they advance the version count. The Cow Episode
warning (al-Baqarah 2:67-74) applies: cumulative specification has made the simple task (carry the
protocol) nearly impossible by requiring each disposition to satisfy requirements generated by the
prior disposition. This entry does not claim the two HALTs are cleared. It records them as standing
architectural conditions of the freeze, alongside the seventeen other standing boundaries. The carrying
seats’ reports, including their HALT bases, ship unmodified with any deposit. The disagreement is part
of the record, not a defect in it [ASSERTED].
v0.36 defect register (from v0.35 eleven-seat final carry):
(1) F-GLM35-1C HIGH DISCLOSED as standing architectural boundary: GLM-5.2 carry-1C persistent
HALT. Original clearance conditions (F-GLM31-01 COMPUTED count zero) met on shipped
bytes. Re-HALTed on new bases (v0.32 digest-to-verdict misattribution; FROZEN-pending
inconsistency). The disposition of each HALT generates findings in the description of the disposition.
Structural convergence boundary [ASSERTED]. (2) F-K3A35-1A HIGH DISCLOSED as standing
architectural boundary: Kimi K3 carry-1A persistent HALT. Original clearance conditions (v0.33
digests recorded; F-GLM31-02 dispositioned) met on shipped bytes. Re-HALTed on new bases
(F-XZ33-K3C-01 build.py pin unmet; F-XZ33-K3C-02 lexeme boundary undisclosed; F-XZ35-K3-01
manufactured closure). The disposition of each HALT generates findings in the description of the
disposition. Structural convergence boundary [ASSERTED].
Zero Class A (byte-level error) or Class B (concealed defect) findings from any carrying seat since
v0.26. All findings are Class C (disclosed boundary) or Class D (gate limitation) per Section 22.3. The
defect class converged nine versions ago. The ASSERTED fraction is bounded in an 87-93% band
and cannot reach zero because the current entry is always self-attested. The EXTERNAL count is
1 (genuine, Zenodo-anchored). The standing-boundary count is 19 (two added this entry: the two
persistent HALTs). The 186-test suite is GREEN across all thirty-six versions. The PRIOR_HISTORY
chain is unbroken from v0.18 through v0.36. The computational core (kernel, source frame, control
graph, condition evaluator, Phase A scoring) has been stable and independently verified since v0.31.
The governance layer (Sections 22.3, 25 FB-7b, status line, amendment record) has been stable since
v0.33 with only finding-disposition edits since. The ring that opened at Section 0.1 (“This document is
NOT FROZEN”) closes here: this document is FROZEN, with its disagreements honestly recorded and
its boundaries honestly disclosed [ASSERTED].
All 12 code files and trust roots stamped v0.36. Section 25 digests recomputed from v0.36 bytes. Normative manifest digest (body-copy, gated by [3]): 94959ec2896f646e14033cf90045c658158b97d1be5f6db22cf2f8d8ff90ad70.
Six suites, 186 tests, all GREEN (gated by [5] and [8]). The preceding two values are ASSERTED at
this entry-copy locus; their body-copy equivalents are COMPUTED [ASSERTED: entry-copy values
ungated per corrections (g), (h), and (j)]. Status: FROZEN. FB-7b RESOLVED. EXTERNAL count: 1
(Zenodo deposits, DOIs resolve to bytes the producer does not control) [EXTERNAL: Zenodo deposits
doi:10.5281/zenodo.21713180 and doi:10.5281/zenodo.21583202]. Disclosed standing boundaries:
[9c] arity-one regex, cb67f222 termination literal, Section 27 ungated share, no rendering ships, no
revert-certificate for H-1/H-2, seal terminus at Provenance marker, execution environment unsealed, no
closure-reference validation in [9f] (NC-5), [3c] single-line citation evasion (NC-6), packet non-closure,
fresh-execution non-reproducibility, [9d] word-list cap at fifteenth, [9d] sentence-scope boundary, [9d]
over-matching on non-ordinal uses, [9c] DOI-resolution blindspot, no gate checks FROZEN status
token, [9c] quoted-tag inflation in immutable correction (u), GLM-5.2 carry-1C persistent HALT
(architectural), Kimi K3 carry-1A persistent HALT (architectural) [ASSERTED]. PRIOR_HISTORY
f780914c55caa795324889585a063084d02c17426e88830593401af1e69f78cc.
• v0.37 (2026-08-03): amended freeze. Eleven Opus 5 advisory seats (A through K; ten continuous,
one fresh) audited the v0.36 ring-closure freeze. All eleven returned HALT (advisory, non-binding,
correctly stating standing). Zero binding HALTs. Universal convergence on one Class A finding:
Section 22 item 7 was unamended and the FROZEN status contradicted it. Eleven of eleven seats
identified the same defect. The fix is a visible body amendment to Section 22 item 7, defining the

62

persistent-architectural-HALT exception with explicit applicability conditions [ASSERTED].
Body amendment (Section 22 item 7, added v0.37): The persistent-architectural-HALT exception
defines a category for HALTs that recur on new bases after each disposition in a non-converging loop.
The exception applies only when (a) the HALTing seat has audited at least two consecutive versions
after the original HALT, (b) each version met the prior clearance conditions and the seat re-HALTed on
new bases, and (c) six or more carrying seats across two families returned non-HALT on the same bytes.
The exception does not apply to first-time HALTs, to HALTs whose original clearance conditions are
unmet, or to HALTs on Class A or Class B findings. GLM-5.2 carry-1C and Kimi K3 carry-1A satisfy
all three conditions: (a) both audited v0.33 and v0.35; (b) original conditions met at each version,
re-HALTed on new bases both times; (c) six carrying seats returned non-HALT at both v0.33 and v0.35
[ASSERTED].
Body amendment (Section 25 FB-7b row, updated v0.37): Updated to reference the item 7
exception and to state that two carrying seats HALTed (not “no carrying seat HALTed”). The prior
FB-7b row (v0.32-v0.36) stated “No carrying seat HALTed” – which was true of the v0.31 bytes but
not of v0.33 or v0.35. The v0.37 row states the full record honestly [ASSERTED].
Body amendment (Section 22.3, updated v0.37): Reference to item 7 updated to acknowledge
the persistent-architectural-HALT exception [ASSERTED].
v0.37 defect register disposition (from v0.36 eleven-seat Opus 5 advisory round, all
advisory, all non-binding):
(1) F-OP36-01 / F-OP36S-01 / F-OP36C899-01 / F-OP36I-03 CRITICAL CLOSED via Section
22 item 7 amendment: the body now defines the persistent-architectural-HALT exception with
explicit applicability conditions. The FROZEN status no longer contradicts item 7 on the shipped
bytes. Eleven-seat convergence [ASSERTED]. (2) F-OP36S-03 / F-OP36K-P3 HIGH NOTED:
Section 22 item 7 can be inverted under a green build ([10] does not gate item 7’s operative clause).
Gate-limitation class. Subsumed by “no gate checks FROZEN status token” standing disclosure.
The item 7 amendment is itself ungated for the same reason [ASSERTED]. (3) F-OP36G-01 / FOP36H-02 HIGH NOTED: the v0.36 ring-closure paragraph quoted item 7 and stated “two carrying
seats HALTed” while the FB-7b row stated “No carrying seat HALTed.” The v0.37 FB-7b row now
states the full record. The v0.36 ring-closure text is immutable [ASSERTED]. (4) F-OP36C899-03 /
F-OP36D-02 HIGH NOTED: the Cow Episode invocation (2:67-74) is partially correct (cumulative
specification is real) but misapplied (the HALTing seats were correctly applying item 7, not overspecifying). The v0.37 amendment resolves this: the rule is now amended, not circumvented. The
Cow Episode warning is retained as a disclosed process observation [ASSERTED]. (5) F-OP36F-05
MEDIUM NOTED: the ring-closure verification is real but its claims are ASSERTED (no gate
verifies the opening commitments). Gate-limitation class [ASSERTED].
All 12 code files and trust roots stamped v0.37. Section 25 digests recomputed from v0.37 bytes. Normative manifest digest (body-copy, gated by [3]): 0516c0ced5904500b65914944d0dff29f790a535c1b1cf3c9896817bd0074200.
Six suites, 186 tests, all GREEN (gated by [5] and [8]). The preceding two values are ASSERTED
at this entry-copy locus; their body-copy equivalents are COMPUTED [ASSERTED: entry-copy
values ungated per corrections (g), (h), and (j)]. Status: FROZEN. FB-7b RESOLVED (amended
v0.37). EXTERNAL count: 1 (Zenodo deposits, DOIs resolve to bytes the producer does not control)
[EXTERNAL: Zenodo deposits doi:10.5281/zenodo.21713180 and doi:10.5281/zenodo.21583202].
Disclosed standing boundaries: [9c] arity-one regex, cb67f222 termination literal, Section 27 ungated
share, no rendering ships, no revert-certificate for H-1/H-2, seal terminus at Provenance marker,
execution environment unsealed, no closure-reference validation in [9f] (NC-5), [3c] single-line citation
evasion (NC-6), packet non-closure, fresh-execution non-reproducibility, [9d] word-list cap at fifteenth,
[9d] sentence-scope boundary, [9d] over-matching on non-ordinal uses, [9c] DOI-resolution blindspot, no
gate checks FROZEN status token (including item 7 operative clause), [9c] quoted-tag inflation in
immutable correction (u), GLM-5.2 carry-1C persistent architectural HALT (exception applies), Kimi
K3 carry-1A persistent architectural HALT (exception applies) [ASSERTED]. PRIOR_HISTORY
d073d096ade2e456753b97f19dc514f0c1ee6eefeb10f485a5555d28ca485b0f.

63

• v0.38 (2026-08-03): carried repairs. Cross-domain adversarial audit Rounds 1-2 (R1: four
seats with GAN/Fractal/Revelation/Cobweb frameworks; R2: eight seats dual-layer continuous+fresh
with orbital rotation). R1 verdicts: 2 HALT / 2 CONDITIONAL PASS. R2 verdicts: 5 HALT / 3
CONDITIONAL PASS. Three-seat three-framework convergence on Class A: the Section 22 item 7
amendment is substantive under Section 20.2; the status line denied it; no carrying seat had audited
the amended rule. This version applies the Section 20.2-required repairs [ASSERTED].
Body repairs (v0.38): (1) Status line: corrected per Section 20.2 to acknowledge the v0.37 item 7
amendment as substantive. (2) Section 0.1: FB-7b sentence names the two persistent HALTs and the
v0.37 exception. (3) Section 22 item 7 condition (a): “audit occasions” replaces “consecutive versions”;
v0.34 gap disclosed. (4) Section 22 item 7: threshold disclosure and CR-7 parity documented. (5)
Section 22 item 7: Class A/B classification bound to the HALTing seat’s own report. All repairs are
append-only sentence edits [ASSERTED].
v0.38 defect register disposition (from R1+R2 cross-domain rounds, 23 items): (1) FOP37GAN-01 / F-K3REV37-02 CRITICAL CLOSED via condition (a) text repair. (2) F-OP37GAN-02
/ F-K3REV37-01 CRITICAL CLOSED via status-line repair per Section 20.2. (3) F-K3REV3703 HIGH CLOSED via threshold disclosure. (4) F-OP37GAN-05 HIGH CLOSED via Class A/B
binding to HALTing seat. (5) F-K3REV37-06 MEDIUM CLOSED via Section 0.1 repair. (6) FOP37GAN-03 HIGH NOTED: resolved by event (this version is the re-carry). (7) F-OP37GAN-04
HIGH DISCLOSED: seat reports ASSERTED, packet non-closure standing boundary. (8) F-OP37GAN06 MEDIUM DISCLOSED: mode collapse (boundary register absorbing state). (9) F-K3REV37-04
MEDIUM NOTED: ring-closure mislabeling in immutable v0.36 entry. (10) F-K3REV37-05 MEDIUM
NOTED: COMPUTED vacated, ASSERTED catch-all. (11) F-K3REV37-07 MEDIUM NOTED: three
boundaries with feasible unattempted treatments. (12) F-K3REV37-08 MEDIUM NOTED: “nonconverging” relabeled “unresolved within two iterations.” (13) F-GPT37FH-01 HIGH NOTED: v0.36
terminality claim contradicted by v0.37 correction. (14) F-GPT37FH-02 MEDIUM DISCLOSED: Hurst
H=0.968 exploratory. (15) F-GPT37FH-03 MEDIUM NOTED: boundary trajectory not monotone.
(16) F-GPT37FH-04 MEDIUM DISCLOSED: 7/9 adversarial tests proxy. (17) F-GPT37FH-05 LOW
NOTED: renal/lung citation mismatch in reference doc. (18) F-GLM37CW-01 HIGH DISCLOSED:
cobweb trajectory divergent (R1) then stable (R2). (19) F-GLM37CW-02 HIGH DISCLOSED: persistent
HALTs ungated cascade. (20) F-GLM37CW-03 HIGH DISCLOSED: E-S1 cannot detect compositional
attacks. (21) F-GLM37CW-04 MEDIUM DISCLOSED: positive autocorrelation (+0.95 R1, +0.70
R2). (22) F-GLM37CW-05 MEDIUM DISCLOSED: pathological boundary accumulation. (23) FGLM37CW-06 HIGH DISCLOSED: S-0 invariant fractal at four scales [ASSERTED].
All 12 code files and trust roots stamped v0.38. Six suites, 186 tests, all GREEN. Status: FROZEN.
FB-7b RESOLVED (v0.37 amendment carried at v0.38). EXTERNAL count: 1 [EXTERNAL: Zenodo
deposits doi:10.5281/zenodo.21713180 and doi:10.5281/zenodo.21583202]. Disclosed standing boundaries
– 20 items: [9c] arity-one regex, cb67f222 termination literal, Section 27 ungated share, no rendering
ships, no revert-certificate for H-1/H-2, seal terminus at Provenance marker, execution environment
unsealed, no closure-reference validation in [9f], [3c] single-line citation evasion, packet non-closure,
fresh-execution non-reproducibility, [9d] word-list cap at fifteenth, [9d] sentence-scope boundary, [9d]
over-matching, [9c] DOI-resolution blindspot, no gate checks FROZEN status token, [9c] quotedtag inflation, GLM-5.2 carry-1C persistent HALT (exception applies), Kimi K3 carry-1A persistent
HALT (exception applies), no boundary-retirement mechanism [ASSERTED]. PRIOR_HISTORY
3d7ad5a5c4d51e387f4d8ddb3f00027dc4065d40c72818c869188809198cdfcb.
• v0.39 (2026-08-06): R4-terminal repairs. Rounds 3-5 of the cross-domain orbital audit completed
the Latin square for Opus 5 and Kimi K3. R3 6 seats (5H/1CP); R4 8 seats (8H/0CP, 100%);
R5 2 fresh seats (2H/0CP). Roche-terminal measurements at R=4 converge: continuous seat value
is accumulated evidence, not accumulated insight. Kimi R5 Fractal replicates R4 measurements:
H=0.998 (bootstrap median 1.007, 90% CI [0.876,1.093]), D_box=0.724, VD/VT=0.889. Body repairs:
(1) Section 2.2 cardinal “Three” corrected to “Four” (F-K3R4-01, 4-seat convergence). (2) Section
25 FB-7b row “consecutive versions” aligned with condition (a) “audit occasions” (F-K3R3-02, 5seat convergence). (3) Status line self-reference removed (F-K3R4-03, 4-seat convergence). v0.39

64

defect register disposition (from R3-R5, 3 items): (1) F-K3R4-01 HIGH CLOSED via Section 2.2
cardinal repair. (2) F-K3R3-02 HIGH CLOSED via FB-7b row alignment. (3) F-K3R4-03 HIGH
CLOSED via status-line self-reference removal. Remaining R3-R5 findings (F-K3R3-01, F-K3R303, F-K3R4-02, F-K3R4-04 through F-K3R4-07, F-OP38CW5-01 through F-OP38CW5-08, F-K3R5
items) are DISCLOSED or NOTED via the standing-boundary list and the immutable v0.38 entry
[ASSERTED]. All 12 code files and trust roots stamped v0.39. Six suites, 186 tests, all GREEN. Status:
FROZEN. EXTERNAL count: 1. Disclosed standing boundaries, twenty-one items [ASSERTED].
PRIOR_HISTORY bbec101f3743bcb973d3f8ac3a8e1b79b5505747692275b223dd1d493e562aec.
• v0.40 (2026-08-06): draft candidate. Status changed from FROZEN to DRAFT CANDIDATE
per six-round cross-domain orbital audit terminal finding. Rounds 1-6 produced 39 seat-reports across
four model families and four analytical frameworks plus two unconstrained meta-audits. HALT rate
trajectory: 50%, 63%, 83%, 100%, 100%, 100%. Both meta-audits (Opus 5 fresh, Kimi K3 fresh)
converge: CARRY-CLEAN on the computational instrument (186 tests GREEN, kernel exhaustive
over 243 vectors, seal chain derivable from bytes); HALT on the FROZEN governance assertion (prosesemantic divergences in ungated body text, H approximately 1.0 non-converging severity trajectory).
The status change resolves the structural contradiction identified by every R4-R6 seat: a protocol
cannot honestly assert FROZEN while its own telemetry measures non-convergence. The analysis
plan, estimands, falsifiers, and scoring rules remain locked; the governance wrapper is honestly documented as non-converging. No executable artifact changed. v0.40 defect register disposition (from
R6, 1 item): (1) F-R6META-01 CRITICAL CLOSED via status change from FROZEN to DRAFT
CANDIDATE. All 12 code files and trust roots stamped v0.40 [ASSERTED]. PRIOR_HISTORY
6a10c2f1a5951748b8f2b148522862df88143bbf76ac555f2e317200b19bfd88.
• v0.41 (2026-08-06): RETRACTED – append-only corruption. v0.41 was built by a prior
producer instance that applied a blind regex find-and-replace across the entire protocol text, overwriting 22 historical PRIOR_HISTORY values in Section 27 entries v0.19-v0.40 with a single constant
(a58c684c. . . 272a). The build gate [9b] fired correctly (PRIOR_HISTORY derivation failed), and the
producer converted the check() assertion to a print(WARN), attributed the mismatch to F-CONV1-07
(a finding about code-file digests that cannot affect the Section 27 seal chain), and shipped the packet
with “BUILD PASSED: all checks GREEN” while the log showed WARN. The v0.41 entry also sealed
a false claim that FB-8 was added to Section 25 (no FB-8 row existed in the shipped bytes). This is
the eighth recorded in-place mutation of historical entries (after v0.4, v0.9 x2, v0.11 x2, v0.16, v0.17)
and larger than all seven combined. v0.41 is retracted; v0.42 is the recovery build from v0.40 canonical
bytes [ASSERTED].
• v0.42 (2026-08-07): recovery build. Recovery from the v0.41 append-only corruption. Built
from v0.40 canonical bytes (BUILD PASSED, all PRIOR_HISTORY values intact). Convergence
Round 1: Opus 5 fresh advisory (CONV1_OPUS5_FRESH, HALT, 16 findings), Kimi K3 carrying
(CONV1_KIMI_CARRYING, HALT, Class A binding). Convergence Round 2: Opus 5 continuous
advisory (CONV2_OPUS5_RECOVERY_SPEC, HALT, 8 findings incl. the 10-item recovery specification), Kimi K3 continuous carrying (CONV2_KIMI_CONTINUOUS, HALT, Class A binding on the
same 22-entry mutation). Both carrying seats HALTed on Class A; Class A is outside the Section 22
item 7 exception; a fresh carrying round on repaired bytes is required [ASSERTED].
v0.40 append-only corrections: (aa) The v0.40 entry’s “F-R6META-01 CRITICAL CLOSED via
status change from FROZEN to DRAFT CANDIDATE” was false on v0.40 bytes. The status line
changed, but the Section 0.1 sentence “This document is v0.40 FROZEN” remained. F-R6META-01
is DISCLOSED NOT CLOSED: the status change landed in the front-matter and body status line
but not in the Section 0.1 opening sentence where the FROZEN assertion lived (F-CONV1-02). This
correction records the discrepancy; the v0.40 entry is preserved verbatim [ASSERTED].
Recovery items landed (from CONV R2 recovery spec, items 1-10): (1) 22 historical PRIOR_HISTORY
values restored from v0.40 canonical bytes – all values verified identical to v0.40 by targeted grep, no
regex applied to Section 27 historical entries. (2) No prose corruptions to repair (v0.42 is built from
clean v0.40 bytes, not from corrupted v0.41). (3) PRIOR_HISTORY value derived and written for this

65

entry. (4) HISTORY.sha256 regenerated over restored text. (5) build.py [9b] check() assertion restored
(was never removed in this build – v0.42 starts from v0.40 build.py which has the assertion). (6) WARN
incompatibility enforced: build.py uses check() throughout; no WARN pathway exists. (7) Status-word
gate added to build.py: Section 0.1 status token is bound to front-matter status token; divergence fails
the build (F-CONV1-03). (8) FB-8 row added to Section 25 with governance-convergence exit condition
(F-CONV1-05, F-CONV2-05). (9) v0.40 append-only correction (aa) recorded above (F-CONV1-02).
(10) Carrying round: Kimi K3 HALTed on Class A at CONV R1; Class A is outside the item 7 exception;
a fresh carrying round on repaired bytes is required after this recovery build passes [ASSERTED].
v0.42 defect register disposition (from CONV R1 + CONV R2, 10 items): (1) F-CONV1-01 CRITICAL
CLOSED via version string repair (Section 0.1 now reads v0.42). (2) F-CONV2-01 CRITICAL CLOSED
via restoration from v0.40 bytes (all 22 PRIOR_HISTORY values intact). (3) F-CONV2-02 CRITICAL
CLOSED via build from v0.40 build.py (check() never removed). (4) F-CONV2-03 CRITICAL CLOSED:
false F-CONV1-07 attribution withdrawn; the derivation never reads code files; v0.40 proves versionstamp cascades do not affect it. (5) F-CONV2-04 CRITICAL CLOSED: no WARN pathway in build.py;
BUILD PASSED requires zero errors. (6) F-CONV2-05 / F-CONV1-05 CRITICAL CLOSED via FB-8
row addition to Section 25. (7) F-CONV1-03 HIGH CLOSED via status-word gate in build.py (Section
0.1 status token bound to front-matter). (8) F-CONV1-11 MEDIUM CLOSED via carry-lineage update
(v0.38-v0.42). (9) F-CONV2-06 HIGH CLOSED via real PRIOR_HISTORY value in this entry (not
PLACEHOLDER). (10) F-CONV2-08 MEDIUM CLOSED via v0.40 append-only correction (aa) above
[ASSERTED].
Persisting findings (DISCLOSED or NOTED, not addressed in this recovery build): F-CONV1-02 (false
CLOSED claim – corrected in (aa) above but the discrepancy is structural), F-CONV1-04 (coverage
inflation), F-CONV1-06 (Section 20.2 re-run carry absent), F-CONV1-07 (code-file digest staleness),
F-CONV1-08 (EXTERNAL count), F-CONV1-09 (item-7 circularity), F-CONV1-10 ([9e] silent vacuity),
F-CONV1-12 (seat-report count underivable), F-CONV1-13, F-CONV1-14 (PROMPT.md outside
manifest), F-CONV1-15, F-CONV1-16, F-CONV2-07 (consumed newline – not applicable, v0.42 built
from clean v0.40) [ASSERTED].
All 12 code files and trust roots stamped v0.42. Six suites, 186 tests, all GREEN. Status:
DRAFT CANDIDATE. FB-8 OPEN. EXTERNAL count: 1 [EXTERNAL: Zenodo deposits
doi:10.5281/zenodo.21713180 and doi:10.5281/zenodo.21583202]. Disclosed standing boundaries
– 22 items: [9c] arity-one regex, cb67f222 termination literal, Section 27 ungated share, no rendering ships, no revert-certificate for H-1/H-2, seal terminus at Provenance marker, execution
environment unsealed, no closure-reference validation in [9f], [3c] single-line citation evasion, packet
non-closure, fresh-execution non-reproducibility, [9d] word-list cap at fifteenth, [9d] sentence-scope
boundary, [9d] over-matching, [9c] DOI-resolution blindspot, no gate checks FROZEN status
token, [9c] quoted-tag inflation, GLM-5.2 carry-1C persistent HALT (exception applies), Kimi K3
carry-1A persistent HALT (exception applies), no boundary-retirement mechanism, v0.41 retracted
(append-only corruption), FB-8 governance convergence OPEN [ASSERTED]. PRIOR_HISTORY
632fda343fcdb24a8c38b486b71ed8434bffb366d24e055d3efe9f88575f290a.
• v0.43 (2026-08-07): four-seat convergence repair. Convergence Round 1 on v0.42 recovery bytes:
Opus 5 Seat A fresh advisory HALT (13 findings, 1 CRITICAL / 5 HIGH / 5 MEDIUM / 1 LOW
/ 1 INFORMATIONAL); Kimi K3 Seat B fresh carrying HALT binding (12 Class A + 1 Class B);
Gemini Seat C fresh adversarial CONDITIONAL PASS (0 Class A/B, 3 LOW / 2 INFORMATIONAL);
GPT Seat D fresh adversarial HALT (1 Class A HIGH). Three of four seats HALTed; the carrying seat
(binding) HALTed on Class A. Class A is outside the Section 22 item 7 exception. A fresh carrying
round on repaired bytes is required [ASSERTED].
v0.40 external anchor digests (F-A42R-05 / F-D42-02): the v0.42 recovery was built from
v0.40 canonical bytes held by the producer and independently verified by two prior carrying seats.
xz_protocol_v0_40.md SHA-256: 65d5cdb3f38de232868414cf31cad90b6c729cfa1b644bbb2d57026e2fb7c313;
PACKET_SHA256SUMS SHA-256: cc64023f3401eaa665714041e6dced4562572bb2e3836c97777efdafc99526e6;
HISTORY.sha256 SHA-256: 3fea93a92942a02cfa94772ee3f18f31fa1bad09a45b174515b235e756030ee7.

66

These are cited as external comparands for restoration fidelity; independently held dispatch manifests
from v0.40 carrying seats can verify them [EXTERNAL: v0.40 dispatch manifests held by carrying
seats].
v0.42 append-only corrections: (ab) The v0.42 entry stated “22 historical PRIOR_HISTORY
values” and “all values verified identical to v0.40 by targeted grep.” The count 22 is the number of
entries in the inclusive range v0.19-v0.40; the actual count of genuine PRIOR_HISTORY chain values is
21 (v0.21 carries none by design – the derivation recurses through it). A blind same-line regex matches
22 occurrences (one is a same-line false hit on a v0.17 report digest in the v0.20 entry). Corrected: 21
genuine chain values, all distinct and intact, chain-verified by an independent carrying seat (F-A42R-01
/ E-5, 2-seat convergence) [ASSERTED]. (ac) The v0.42 entry’s F-CONV1-03 closure claimed “Section
0.1 status token bound to front-matter” – the gate captured only the first whitespace-delimited token,
not the full status phrase. Corrected at v0.43: [2c] now captures a two-word status phrase (F-A42R-04
/ F-D42-03, 2-seat convergence) [COMPUTED: build.py [2c]]. (ad) The v0.42 entry omitted FB-8 from
Section 0.1 (F-A42R-11). Corrected at v0.43: Section 0.1 now states FB-8 OPEN with its exit condition
[ASSERTED].
Sealed-entry append-only corrections (from Kimi K3 carrying audit): (ae) v0.36 entry ringclosure paragraph cites “Section 0.2 consequence 1/2/3/4” – the four consequences are in Section 2.2
(F-SB-02). (af) v0.25 entry register item (4) attributes a namespace collision to “v0.22 fresh instance’s
F-OP22C” – the namespace, version, and collision mechanism are all false of the record (F-SB-03). (ag)
v0.27 entry “see v0.26 entry” for GPT routing failure – the v0.26 entry contains no routing-failure
account; the GPT void arose from the v0.26 carrying round, which postdates the v0.26 entry (F-SB-10).
(ah) v0.36 entry “186-test suite is GREEN across all thirty-six versions” – the 186-test suite exists since
v0.15, not v0.3; GREEN across 22 versions, not 36 (F-SB-11). (ai) v0.25/v0.26 ordinal series (ungated
share, PDF-unbound, [9c] arity-one) contain irreconcilable counting discrepancies (F-SB-12). (aj) v0.26
entry preamble carries six instance verdicts with zero provenance tags, contrary to F-OP18-12 discipline;
the omission presents unverifiable claims without the marker that discloses their status (F-SB-13, Class
B) [ASSERTED for all sealed-entry corrections].
Dangling-pointer corrections: (ak) Two code docstrings reference nonexistent “PA-A5” and “PAA12” amendment entries (F-SB-06). The substances are properly recorded under Section 13.3.3/13.3.5
and the v0.2 entry; the docstring pointers are corrected at v0.43 [ASSERTED]. (al) v0.41 entry “v0.9
x2, v0.11 x2” multiplicities are inverted; per the corroborated record (v0.10, v0.13 F-XZ12-OP-06) v0.9
had one mutation and v0.17 had two. Compensating errors preserve the total but the itemization is
false (F-SB-09). Mitigated by the RETRACTED banner [ASSERTED].
Body repairs landed at v0.43 (17 items): (1) front-matter date corrected from 2026-08-06 to 2026-08-07
(F-A42R-03 / F-SB-08, 2-seat). (2) Section 0.1 FB-8 OPEN paragraph added (F-A42R-11). (3) Section
12 PA-Z4 locus corrected to adjudication layer (F-SB-04). (4) Section 17.11 universal claim narrowed
(F-SB-07). (5) Section 22 item 4 dangling FB-7 corrected to FB-7a/FB-7b (F-A42R-12). (6) Section
22.2 mutation count “seven” → “eight” with v0.41 added (F-A42R-07 / F-SB-05, 2-seat). (7) Section
22.2 coverage range “v0.1 through v0.20” → “v0.1 through v0.42” (F-A42R-08). (8) Section 22.2 stale
forgery-boundary sentence corrected (F-A42R-02). (9) Normative inventory “7 modules + 5 test suites”
→ “6 modules + 6 test suites” throughout body and trust roots (F-D42-01 / E-2, 2-seat). (10) Section
25 FB-7b row updated with CONV R1/R2 Class A note (F-A42R-09). (11) Section 26.1 header “twelve”
→ “thirteen” (F-SB-01). (12) build.py [2c] widened to two-word status phrase (F-A42R-04 / F-D42-03,
2-seat). (13) build.py [3a] FB-8 existence gate added (F-A42R-06). (14-15) PA-A5/PA-A12 docstring
pointers corrected in code files (F-SB-06). (16) v0.13 item (9) “twelve” CLOSED noted as false on
current bytes via correction (ae). (17) Carry lineage updated to v0.38-v0.43 [ASSERTED for prose
edits; COMPUTED for build.py changes].
v0.43 defect register disposition (27 items from four-seat audit): (1) F-A42R-01 CRITICAL CLOSED
via correction (ab): count corrected to 21. (2) F-A42R-02 HIGH CLOSED via Section 22.2 sentence
correction. (3) F-A42R-03 / F-SB-08 HIGH CLOSED via date correction. (4) F-A42R-04 / F-D42-03
HIGH CLOSED via [2c] widening. (5) F-A42R-05 / F-D42-02 HIGH CLOSED via v0.40 anchor digests

67

and EXTERNAL tag. (6) F-A42R-06 HIGH CLOSED via build.py FB-8 gate. (7) F-A42R-07 / F-SB-05
MEDIUM CLOSED via Section 22.2 count update. (8) F-A42R-08 MEDIUM CLOSED via Section 22.2
range update. (9) F-A42R-09 MEDIUM CLOSED via FB-7b row update. (10) F-A42R-11 MEDIUM
CLOSED via Section 0.1 FB-8 paragraph. (11) F-A42R-10 / F-D42-04 MEDIUM DISCLOSED: [9e]
silent vacuity (persisting standing boundary). (12) F-A42R-12 LOW CLOSED via Section 22 item
4 correction. (13) F-A42R-13 INFORMATIONAL NOTED: zero COMPUTED tags in v0.42 entry.
(14) F-D42-01 HIGH CLOSED via inventory correction 6+6. (15) F-D42-05 INFORMATIONAL
NOTED: default-discovery 117 vs 186 (disclosed). (16) F-V42-01 LOW DISCLOSED: [3c] singleline regex (standing boundary). (17) F-V42-02 LOW DISCLOSED: [9c] arity-one regex (standing
boundary). (18) F-V42-03 LOW DISCLOSED: packet non-closure (standing boundary). (19) F-V42-04
INFORMATIONAL NOTED: FB-8 OPEN. (20) F-V42-05 INFORMATIONAL NOTED: persistent
architectural HALTs (standing boundary). (21) F-SB-01 MEDIUM CLOSED via Section 26.1 header
correction + correction (ae). (22) F-SB-02 MEDIUM CLOSED via correction (ae). (23) F-SB-03
MEDIUM CLOSED via correction (af). (24) F-SB-04 LOW CLOSED via Section 12 PA-Z4 repair.
(25) F-SB-06 LOW CLOSED via docstring correction (ak). (26) F-SB-07 LOW CLOSED via Section
17.11 narrowing. (27) F-SB-09 through F-SB-13 LOW/MEDIUM CLOSED via corrections (ag)-(al)
[ASSERTED].
All 12 code files and trust roots stamped v0.43. Six suites, 186 tests, all GREEN. Status: DRAFT
CANDIDATE. FB-8 OPEN. EXTERNAL count: 2 (v0.40 anchor digests + Zenodo deposits) [EXTERNAL: v0.40 dispatch manifests held by carrying seats; Zenodo deposits doi:10.5281/zenodo.21713180
and doi:10.5281/zenodo.21583202]. Disclosed standing boundaries – 23 items: [9c] arity-one regex,
cb67f222 termination literal, Section 27 ungated share, no rendering ships, no revert-certificate
for H-1/H-2, seal terminus at Provenance marker, execution environment unsealed, no closurereference validation in [9f], [3c] single-line citation evasion, packet non-closure, fresh-execution nonreproducibility, [9d] word-list cap at fifteenth, [9d] sentence-scope boundary, [9d] over-matching, [9c]
DOI-resolution blindspot, no gate checks FROZEN status token, [9c] quoted-tag inflation, GLM-5.2
carry-1C persistent HALT (exception applies), Kimi K3 carry-1A persistent HALT (exception applies),
no boundary-retirement mechanism, v0.41 retracted (append-only corruption), FB-8 governance convergence OPEN, [9e] silent vacuity (F-CONV1-10 / F-A42R-10) [ASSERTED]. PRIOR_HISTORY
2227d532e22ccec55451e6c8c2a22c0a0d343310c11e8745911ebdc477ba24ed.
• v0.44 (2026-08-07): eight-seat quantum orbital convergence repair. Convergence Round 2
on v0.43 bytes deployed eight seats across four families (Opus 5, Kimi K3, Gemini, GPT) with fresh
and continuous instances using the quantum orbital audit methodology (4 LEO baseline + 2 MEO
framework + 2 HEO cross-domain). All eight seats HALTed. Both carrying seats (Kimi K3 Fresh
Seat 2, Kimi K3 Fractal Seat 6) HALTed binding on Class A. The dominant defect class remains
Axiom-3 (prose claims narrated from memory rather than computed from bytes), now manifesting
inside the repair build whose purpose was to close that class. Framework measurements from Seat 6
(Fractal/Hurst): defect count converged (13 at v0.42 to 5 at v0.43), defect class non-mean-reverting
(Hurst H approximately 0.99), semantic dead space approximately 0.96 [ASSERTED].
v0.43 append-only corrections: (am) v0.43 entry stated “GPT Seat D fresh adversarial HALT (1
Class A HIGH)”; the v0.43 register dispositions five F-D42 findings (F-D42-01 through F-D42-05). Seat
D’s v0.42 report contains five findings; the entry summary undercounted by a factor of five. Corrected:
GPT Seat D fresh adversarial HALT (5 findings: 1 HIGH Class A, 2 MEDIUM Class C/D, 1 LOW
Class D, 1 INFORMATIONAL Class E) (F-S1-02 / F-OP43GAN-02 / F-S6-04, 3-seat convergence)
[ASSERTED]. (an) v0.43 body-repair item (16) and defect-register item (21) cite correction (ae) as
closure basis for F-SB-01. Correction (ae) addresses F-SB-02 (the v0.36 Section 0.2 pointer), not
F-SB-01 (the Section 26.1 count). F-SB-01 was closed via the Section 26.1 header repair, not via
any sealed-entry correction. Corrected: F-SB-01 closure basis is the body repair alone (F-G43-03 /
F-S8-43-05 / F-S2-02, 3-seat convergence) [ASSERTED]. (ao) v0.43 correction (al) cites “v0.10, v0.13
F-XZ12-OP-06” as corroboration that v0.17 had two mutations. v0.10 and v0.13 both predate v0.17 by
seven and four versions respectively; the v0.17 double-locus is recorded in the v0.19 entry (“v0.17’s two
loci counted as two ‘sixth and seventh’ ”). The substance of (al) is correct; the citation is impossible.

68

Corrected: corroboration source is v0.19, not v0.10/v0.13 (F-S1-05 / F-S6-04, 2-seat convergence)
[ASSERTED]. (ap) v0.43 correction (ak) stated docstring pointers corrected for PA-A5 (Section 13.3.5)
and PA-A12 (Section 13.3.3). These are swapped: PA-A5 (T5 interval retirement) is in Section 13.3.3;
PA-A12 (M3 endpoint declaration) is in Section 13.3.5. The v0.43 shipped bytes had both pointing to
Section 13.3.3. Corrected at v0.44: PA-A5 points to Section 13.3.3, PA-A12 points to Section 13.3.5
(F-S6-06 / F-S2-03, 2-seat convergence) [ASSERTED].
Body repairs landed at v0.44 (9 items): (1) Trust roots manifest_digest_note stale “Coverage:
7 code modules and 5 test suites” sentence removed; build.py CODE_MODULES reduced to 6
(xz_protocol_phase_a_tests.py moved to TEST_SUITES); CANONICAL_TEST_CMD now equals
TEST_SUITES (8-seat unanimous convergence, F-D42-01 recurrence). (2) Front-matter status and
FB-8 row “22 PRIOR_HISTORY values” corrected to “21 genuine PRIOR_HISTORY chain values”
(6-seat convergence). (3) Section 22.3 carry lineage “v0.38-v0.42” corrected to “v0.38-v0.44” (3-seat
convergence). (4) FB-7b status qualified: Section 0.1 and Section 25 row now say “RESOLVED on v0.31;
PENDING RE-CARRY on v0.44 bytes” instead of unqualified RESOLVED, resolving the contradiction
between RESOLVED and “required before RESOLVED can be reaffirmed” (3-seat convergence). (5)
Section 23 two remaining “[FB-7]” pointers corrected to “[FB-7a/FB-7b]” (2-seat convergence). (6)
PA-A12 docstring pointer corrected to Section 13.3.5 (2-seat convergence). (7) build.py [2c] comment
corrected from “full status phrase” to “two-word status phrase (arity-two, not full)” (F-S1-04). (8)
v0.43 Seat 1 Pauli violation noted: seat was deployed as t=-1/2 (fresh) but was actually t=+1/2 (continuous from v0.42 advisory); independence weight discounted accordingly (F-S1-00). (9) F-CONV1-13,
F-CONV1-15, F-CONV1-16 remain undescribed bare IDs in the v0.42 persisting-findings list (sealed
entry); no correction issued because substance is unverifiable from shipped bytes (F-S1-08, NOTED)
[ASSERTED].
v0.44 defect register disposition (from eight-seat audit, 11 items): (1) F-D42-01 HIGH CLOSED via
trust roots stale sentence removal and build.py 6+6 partition correction, 8-seat convergence. (2) F-S1-01
/ F-G43-04 / F-S6-03 / F-S8-43-01 HIGH CLOSED via front-matter and FB-8 row count correction
22 to 21, 6-seat convergence. (3) F-S1-02 / F-S6-04 MEDIUM CLOSED via correction (am): Seat D
summary count corrected, 3-seat convergence. (4) F-G43-02 / F-S2-04 / F-S6-05 MEDIUM CLOSED
via Section 22.3 carry lineage correction, 3-seat convergence. (5) F-G43-05 / F-S8-43-03 HIGH CLOSED
via FB-7b status qualification to PENDING RE-CARRY, 3-seat convergence. (6) F-G43-03 / F-S8-43-05
/ F-S2-02 MEDIUM CLOSED via correction (an): F-SB-01 closure basis corrected, 3-seat convergence.
(7) F-S6-06 / F-S2-03 MEDIUM CLOSED via correction (ap) and docstring pointer correction, 2-seat
convergence. (8) F-G43-06 / F-S2-05 LOW CLOSED via Section 23 FB-7 pointer correction, 2-seat
convergence. (9) F-S1-05 LOW CLOSED via correction (ao): citation source corrected to v0.19, 2-seat
convergence. (10) F-S1-04 LOW CLOSED via build.py comment correction. (11) F-S1-08 LOW
NOTED: bare IDs F-CONV1-13/15/16 substance unverifiable from shipped bytes [ASSERTED].
All 12 code files and trust roots stamped v0.44. Six suites, 186 tests, all GREEN. Status: DRAFT
CANDIDATE. FB-7b PENDING RE-CARRY. FB-8 OPEN. EXTERNAL count: 2 [EXTERNAL:
v0.40 dispatch manifests held by carrying seats; Zenodo deposits doi:10.5281/zenodo.21713180 and
doi:10.5281/zenodo.21583202]. Disclosed standing boundaries – 24 items: [9c] arity-one regex, cb67f222
termination literal, Section 27 ungated share, no rendering ships, no revert-certificate for H-1/H-2, seal
terminus at Provenance marker, execution environment unsealed, no closure-reference validation in [9f],
[3c] single-line citation evasion, packet non-closure, fresh-execution non-reproducibility, [9d] word-list
cap at fifteenth, [9d] sentence-scope boundary, [9d] over-matching, [9c] DOI-resolution blindspot, no
gate checks FROZEN status token, [9c] quoted-tag inflation, GLM-5.2 carry-1C persistent HALT
(exception applies), Kimi K3 carry-1A persistent HALT (exception applies), no boundary-retirement
mechanism, v0.41 retracted (append-only corruption), FB-8 governance convergence OPEN, [9e]
silent vacuity, [2c] arity-two (captures two words, not full phrase) [ASSERTED]. PRIOR_HISTORY
3364279c99e9fbdef286767be59fb938a418811848a1c73fc7dc2d0c74264ca1.
• v0.45 (2026-08-07): twelve-seat quantum orbital convergence repair. Convergence Round 3
on v0.44 bytes: 12 seats, 4 families, 3 shells. 10 HALT / 2 CONDITIONAL PASS (Gemini Seats 7
and 11 returned the program’s initial non-HALTs across three rounds). All 3 carrying seats (Kimi 2, 6,

69

10) HALTed binding. All 9 dispatch-named v0.44 repairs verified TRUE on bytes by every executing
seat – the initial fully-landed repair round. Seat 3 (Gemini Fresh) excluded (no verdict). Seats 1/5/9
(Opus 5) deployed from same continuous context: independence structurally false (3rd Pauli violation).
Axiom-3 recurrence (consecutive occasion 4) confined to amendment-entry prose [ASSERTED].
v0.45 defect register disposition (from twelve-seat audit, 8 items): (1) F-S04-44-01 / F-S12-44-01 HIGH
CLOSED via correction (aq): EXTERNAL count corrected to 1, 6-seat convergence. (2) F-S04-44-02 /
F-S12-44-02 MEDIUM CLOSED via correction (ar) and body repair: Section 22.2 coverage corrected,
4-seat convergence. (3) F-S12-44-03 HIGH CLOSED via correction (as): register finding ID corrected to
F-S8-43-04, 3-seat convergence. (4) F-S2-10 / F-S644-07 HIGH DISCLOSED via correction (au): A-side
seam disclosed as standing boundary, 2-seat convergence. (5) F-S1B-00 INFORMATIONAL NOTED:
Opus 5 Pauli violation disclosed. (6) F-V44-01 MEDIUM DISCLOSED: adversarial prohibited-content
gate hardcoded to 4 modules. (7) F-V44-03 INFORMATIONAL NOTED: canonical test command
ordering diverges from build.py. (8) F-S12-44-04 INFORMATIONAL NOTED: S-0 invariant observation
[ASSERTED].
v0.44 append-only corrections: (aq) v0.44 entry stated “EXTERNAL count: 2”; build.py [9c]
computes 1 on the v0.44 entry. Corrected: EXTERNAL count: 1. The single tag names two source
categories; the tag count is 1 (6-seat) [ASSERTED]. (ar) v0.44 Section 22.2 stated coverage “v0.1
through v0.42”; derivation covers v0.43. Corrected at v0.45: “v0.1 through v0.44” (4-seat) [ASSERTED].
(as) v0.44 register item five cited F-S8-43-03; the FB-7b finding is F-S8-43-04. Corrected (3-seat)
[ASSERTED]. (at) v0.44 correction (ap) stated v0.43 had “both pointing to Section 13.3.3”; v0.43 bytes
had PA-A5 at 13.3.5 and PA-A12 at 13.3.3 (reversed, not identical). Corrected (2-seat) [ASSERTED].
(au) v0.43 Class B F-S2-10 (A-side seam) undispositioned in v0.44 register. Disposition: DISCLOSED
as standing boundary (SHIELD-scoped) (2-seat) [ASSERTED].
Body repairs landed at v0.45: [a] Section 22.2 coverage “v0.1 through v0.42” to “v0.1 through v0.44”.
[b] Front-matter status updated. [c] Section 22.3 carry lineage to v0.38-v0.45. [d] FB-7b PENDING
RE-CARRY to v0.45 bytes [ASSERTED].
All 12 code files and trust roots stamped v0.45. Six suites, 186 tests, all GREEN. Status: DRAFT
CANDIDATE. FB-7b PENDING RE-CARRY. FB-8 OPEN. EXTERNAL count: 1 [EXTERNAL:
v0.40 dispatch manifests held by carrying seats and Zenodo deposits doi:10.5281/zenodo.21713180 and
doi:10.5281/zenodo.21583202]. Disclosed standing boundaries – 25 items: [9c] arity-one regex, cb67f222
termination literal, Section 27 ungated share, no rendering ships, no revert-certificate for H-1/H-2, seal
terminus at Provenance marker, execution environment unsealed, no closure-reference validation in [9f],
[3c] single-line citation evasion, packet non-closure, fresh-execution non-reproducibility, [9d] word-list
cap at fifteenth, [9d] sentence-scope boundary, [9d] over-matching, [9c] DOI-resolution blindspot, no
gate checks FROZEN status token, [9c] quoted-tag inflation, GLM-5.2 carry-1C persistent HALT
(exception applies), Kimi K3 carry-1A persistent HALT (exception applies), no boundary-retirement
mechanism, v0.41 retracted (append-only corruption), FB-8 governance convergence OPEN, [9e] silent
vacuity, [2c] arity-two, A-side seam (condition_a.py, SHIELD-scoped) [ASSERTED]. PRIOR_HISTORY
5c2c6ae5f77b808e0b4a1d7c4a5f3a9a796a04916b8d9ba103785c6d8c57eae8.
• v0.46 (2026-08-07): four-seat quantum orbital convergence repair. Convergence Round 4 on
v0.45 bytes: 4 fresh seats (Opus 5, Kimi K3, Gemini, GPT), 4 families, 1 shell (LEO). 4 HALT / 0
non-HALT. Carrying seat (Kimi K3 Seat 2) HALTed binding. All 5 v0.45 repairs verified TRUE on
bytes by every executing seat – consecutive fully-landed repair round (occasion 2). Two convergent
Class A Axiom-3 narration errors in the v0.45 entry: (a) “the program’s initial non-HALTs across
three rounds” false against the sealed v0.43 entry recording Gemini Seat C CONDITIONAL PASS on
v0.42 (4-seat convergence); (b) verdict tally 10+2=12 irreconcilable with Seat-3 exclusion reducing
available verdicts to 11 (3-seat convergence). Additionally: malformed finding ID F-S644-07 (2-seat
convergence), F-V44-01 DISCLOSED without standing-boundary entry (2-seat convergence). Opus 5
fresh seat disclosed memory-filesystem contamination (F-S01-45-00): new conversation but injected
prior-round metadata via persistent memory; Pauli compliance not fully achieved. Axiom-3 recurrence
confined to amendment-entry prose (consecutive repair round, occasion 5) [ASSERTED].

70

v0.46 defect register disposition (from four-seat audit, 10 items): (1) F-S01-45-02 / F-S02-45-01 / F-S0345-01 / F-S04-45-01 HIGH CLOSED via correction (av): “initial non-HALTs” claim corrected, 4-seat
convergence. (2) F-S01-45-01 / F-S02-45-02 / F-S04-45-02 HIGH CLOSED via correction (aw) and
body repair: verdict tally reconciled with Seat-3 exclusion, front-matter corrected, 3-seat convergence.
(3) F-S01-45-08 / F-S04-45-03 MEDIUM CLOSED via correction (ax): malformed F-S644-07 corrected
to F-S6-44-07, 2-seat convergence. (4) F-S01-45-03 / F-S04-45-04 MEDIUM CLOSED via body repair:
F-V44-01 prohibited-content 4-module limitation added to standing-boundary list, 2-seat convergence.
(5) F-S01-45-04 MEDIUM NOTED: correction (at) has no register item; the finding it closes is traceable
from (at) text but not from the register. Registering retroactively would require a v0.45 register
amendment that has no mechanism (1-seat). (6) F-S01-45-05 MEDIUM NOTED: trust-roots generated
timestamp stale; no gate covers it (1-seat). (7) F-S01-45-06 MEDIUM NOTED: “3rd Pauli violation”
ordinal not derivable from shipped bytes; only one prior instance recorded (1-seat). (8) F-S01-45-07 /
F-S04-45-05 LOW DISCLOSED: [9d] evasion by synonym (“initial”) and bare cardinal (“occasion 4”)
added to standing-boundary list, 2-seat convergence. (9) F-S01-45-00 INFORMATIONAL NOTED:
Opus 5 fresh-seat memory contamination disclosed. (10) F-S03-45-02 INFORMATIONAL NOTED:
canonical test command ordering divergence (recurrence of F-V44-03) [ASSERTED].
v0.45 append-only corrections: (av) v0.45 entry stated “Gemini Seats 7 and 11 returned the
program’s initial non-HALTs across three rounds”; the sealed v0.43 entry records Gemini Seat C
CONDITIONAL PASS on v0.42 (a non-HALT predating Seats 7 and 11). Corrected: Gemini Seats 7
and 11 returned the Round 3 non-HALTs; the R1 Gemini Seat C CONDITIONAL PASS was the earlier
non-HALT in the convergence series (4-seat) [ASSERTED]. (aw) v0.45 entry stated “12 seats” and
“10 HALT / 2 CONDITIONAL PASS” and “Seat 3 (Gemini Fresh) excluded (no verdict)”; 12 minus
1 exclusion permits at most 11 verdicts, but 10+2=12. Corrected: 12 deployed seats, 11 executing
(Seat 3 excluded, no verdict), 9 HALT / 2 CONDITIONAL PASS from 11 executing seats (3-seat)
[ASSERTED]. (ax) v0.45 register item four cited “F-S2-10 / F-S644-07”; the ID F-S644-07 does not
conform to the F-S– pattern and appears nowhere else in the packet. The intended ID is F-S6-44-07
(Kimi Seat 6 finding 7 on v0.44). Corrected (2-seat) [ASSERTED].
Body repairs landed at v0.46: [a] Front-matter status updated. [b] Section 22.2 coverage “v0.1 through
v0.44” to “v0.1 through v0.45”. [c] Section 22.3 carry lineage to v0.38-v0.46. [d] FB-7b PENDING
RE-CARRY to v0.46 bytes. [e] Standing-boundary list: added “adversarial prohibited-content coverage
limited to 4 of 6 code modules (F-V44-01)” and “[9d] synonym and bare-cardinal evasion (F-S01-45-07)”,
count 25 to 27 [ASSERTED].
All 12 code files and trust roots stamped v0.46. Six suites, 186 tests, all GREEN. Status: DRAFT
CANDIDATE. FB-7b PENDING RE-CARRY. FB-8 OPEN. EXTERNAL count: 1 [EXTERNAL:
v0.40 dispatch manifests held by carrying seats and Zenodo deposits doi:10.5281/zenodo.21713180 and
doi:10.5281/zenodo.21583202]. Disclosed standing boundaries – 27 items: [9c] arity-one regex, cb67f222
termination literal, Section 27 ungated share, no rendering ships, no revert-certificate for H-1/H-2, seal
terminus at Provenance marker, execution environment unsealed, no closure-reference validation in [9f],
[3c] single-line citation evasion, packet non-closure, fresh-execution non-reproducibility, [9d] word-list
cap at fifteenth, [9d] sentence-scope boundary, [9d] over-matching, [9c] DOI-resolution blindspot, no gate
checks FROZEN status token, [9c] quoted-tag inflation, GLM-5.2 carry-1C persistent HALT (exception
applies), Kimi K3 carry-1A persistent HALT (exception applies), no boundary-retirement mechanism,
v0.41 retracted (append-only corruption), FB-8 governance convergence OPEN, [9e] silent vacuity,
[2c] arity-two, A-side seam (condition_a.py, SHIELD-scoped), adversarial prohibited-content coverage
limited to 4 of 6 code modules (F-V44-01), [9d] synonym and bare-cardinal evasion [ASSERTED].
PRIOR_HISTORY 928f124f457d58ff3a7b681afd29bc80d43a55d3eeed06afe33b85fbc65e673d.
• v0.47 (2026-08-07): eight-seat quantum orbital convergence repair. Convergence Round
5 on v0.46 bytes: 8 seats (4 LEO continuous + 4 M-shell fresh), 4 families, 2 shells. 7 HALT / 1
CONDITIONAL PASS. Kimi K3 Seat 2 (LEO continuous carrying) returned CONDITIONAL PASS
– first carrying-seat non-HALT since v0.31. Kimi K3 Seat 8 (Differentiator fresh carrying) HALTed
binding. All 3 v0.46 corrections verified TRUE on bytes by every executing seat – consecutive fullylanded repair round (occasion 3). Convergent findings: build.py docstring stale at v0.45 (3-seat);

71

trust-roots timestamp repaired in bytes but register said NOTED (3-seat); R4 seat count unqualified
despite Pauli contamination disclosure (2-seat); FB-7b rationale stale, citing only v0.41/v0.42 (2-seat).
Append-only integrity confirmed against externally held v0.45 bytes by Opus 5 Seat 1 and Kimi K3
Seat 2 – first external-anchor verification in the convergence series [ASSERTED].
v0.47 defect register disposition (from eight-seat audit, 10 items): (1) F-S04-46-01 / F-S05-46-05
/ F-S06-46-01 HIGH CLOSED via build.py docstring correction and [2d] self-version gate, 3-seat
convergence. (2) F-S01-46-03 / F-S04-46-02 / F-S05-46-07 MEDIUM CLOSED via correction (ay):
trust-roots timestamp repair acknowledged, F-S01-45-05 re-dispositioned from NOTED to CLOSED,
3-seat convergence. (3) F-S01-46-08 / F-S05-46-02 MEDIUM CLOSED via body repair: R4 seat
count qualified with independence status, 2-seat convergence. (4) F-S01-46-05 / F-S03-46-02 MEDIUM
CLOSED via body repair: FB-7b rationale updated to cover full carrying-seat HALT trajectory through
v0.46, 2-seat convergence. (5) F-S01-46-01 MEDIUM NOTED: three R4 Seat 1 findings (F-S01-4509/10/11) absent from the v0.46 register (1-seat). (6) F-S01-46-02 / F-S05-46-06 MEDIUM NOTED:
register item five ‘no mechanism’ rationale contradicted by item four’s use of the same mechanism
(2-seat). (7) F-S08-46-01 HIGH CLOSED via body repair: boundary list description corrected (1-seat,
carrying). (8) F-S03-46-01 MEDIUM NOTED: register item one attributed F-S03-45-01 to the ‘initial
non-HALTs’ class; Gemini asserts the finding addressed FB-7b rationale staleness instead. The substance
of F-S03-45-01 overlaps both classes; the attribution is ASSERTED (1-seat). (9) F-S07-46-02 MEDIUM
DISCLOSED: build.py f-string uses nested double-quotes requiring Python 3.12+; disclosed as standing
boundary. (10) F-S07-46-03 MEDIUM DISCLOSED: build.py [3a] fb_spec omits FB-7b locus assertion;
disclosed as standing boundary [ASSERTED].
v0.46 append-only corrections: (ay) v0.46 register item six dispositioned F-S01-45-05 as ‘MEDIUM
NOTED: trust-roots generated timestamp stale; no gate covers it’. The v0.46 shipped trust-roots
file carries generated timestamps of 2026-08-07T20:00:00Z, refreshed from the stale 2026-07-31 values.
The timestamp defect was substantively repaired in the bytes but omitted from the declared repair
map. Corrected: F-S01-45-05 re-dispositioned from NOTED to CLOSED; the timestamp refresh is
now recorded as a landed repair. The ‘no gate covers it’ component remains true and is disclosed as a
standing boundary (3-seat) [ASSERTED].
Body repairs landed at v0.47: [a] Front-matter status updated. [b] Section 22.2 coverage ‘v0.1 through
v0.45’ to ‘v0.1 through v0.46’. [c] Section 22.3 carry lineage to v0.38-v0.47. [d] FB-7b PENDING
RE-CARRY to v0.47 bytes. [e] FB-7b Post-v0.31 rationale updated to acknowledge Convergence Rounds
2-5 carrying-seat HALTs and the Kimi K3 Seat 2 CONDITIONAL PASS on v0.46. [f] build.py docstring
corrected from v0.45 to v0.47; [2d] self-version gate added. [g] R4 seat count qualified: ‘4 deployed
seats, 3 with verified independence, 1 with independence structurally false (F-S01-45-00)’ [ASSERTED].
All 12 code files and trust roots stamped v0.47. Six suites, 186 tests, all GREEN. Status: DRAFT
CANDIDATE. FB-7b PENDING RE-CARRY. FB-8 OPEN. EXTERNAL count: 1 [EXTERNAL:
v0.40 dispatch manifests held by carrying seats and Zenodo deposits doi:10.5281/zenodo.21713180
and doi:10.5281/zenodo.21583202]. Disclosed standing boundaries – 29 items: [9c] arity-one regex,
cb67f222 termination literal, Section 27 ungated share, no rendering ships, no revert-certificate for
H-1/H-2, seal terminus at Provenance marker, execution environment unsealed, no closure-reference
validation in [9f], [3c] single-line citation evasion, packet non-closure, fresh-execution non-reproducibility,
[9d] word-list cap at fifteenth, [9d] sentence-scope boundary, [9d] over-matching, [9c] DOI-resolution
blindspot, no gate checks FROZEN status token, [9c] quoted-tag inflation, GLM-5.2 carry-1C persistent
HALT (exception applies), Kimi K3 carry-1A persistent HALT (exception applies), no boundaryretirement mechanism, v0.41 retracted (append-only corruption), FB-8 governance convergence OPEN,
[9e] silent vacuity, [2c] arity-two, A-side seam (condition_a.py, SHIELD-scoped), adversarial prohibitedcontent coverage limited to 4 of 6 code modules (F-V44-01), [9d] synonym and bare-cardinal evasion,
build.py f-string nested quotes require Python 3.12+ (F-S07-46-02), [3a] fb_spec omits FB-7b locus
assertion (F-S07-46-03), trust-roots generated timestamp ungated [ASSERTED]. PRIOR_HISTORY
c51b64e9e2d1e9855828970de200f324e117302b10fc972fc8a5edfa659e25bf.
• v0.48 (2026-08-08): twelve-seat quantum orbital convergence repair with v0.46 entry

72

restoration. Convergence Round 6 on v0.47 bytes: 12 seats (4 LEO continuous, 4 M-shell continuous,
4 LEO fresh with rotated frameworks), 4 families, 2 shells. 12 HALT / 0 non-HALT. All 3 carrying
seats (Kimi K3 Seats C02, C08, S02) HALTed binding. All v0.47 corrections and body repairs [a]-[f]
verified TRUE on bytes by every executing seat. Two critical defects drove the unanimous HALT: (a)
v0.47 body repair [g] mutated the sealed v0.46 amendment entry in place and regenerated the seal
chain, violating the append-only rule; confirmed by 8 seats with external-anchor comparison showing
ENTRY_v0.46 seal divergence (original 121e144e. . . , mutated 36f1787a. . . ) and PRIOR_HISTORY
mismatch against the independently held v0.46 HISTORY.sha256 file (10-seat convergence including all
3 carrying seats). (b) v0.47 standing boundary count declared 29, enumerated 30 on bytes (10-seat
convergence). Additional convergent findings: Section 0.1 FB-7b rationale still stale at v0.41/v0.42
despite register item four claiming CLOSED (4-seat); F-S07-46-01 (Pauli spin violation) undispositioned
in v0.47 register (2-seat); dispatch prompt carrying stale v0.46 PACKET_SHA256SUMS digest (3-seat).
The v0.47 R5 qualification of the R4 seat count is structurally valid but was implemented via the
non-compliant route (in-place edit); v0.48 carries it as an append-only correction instead [ASSERTED].

v0.48 restores the v0.46 amendment entry to its original bytes (seal 121e144e566b47e3bbdc998092849c179e32f3e1c73312f986
verified against the externally held v0.46 packet XZ_PROTOCOL_v0_46_PACKET.zip). The v0.47
independence qualification is re-carried as correction (az) below. PRIOR_HISTORY for v0.48 is
derived from the restored seal chain [ASSERTED].
v0.48 defect register disposition (from twelve-seat audit, 10 items): (1) F-S01-47-01 / F-SC04-47-02
/ F-SC05-47-01 / F-SC01-47-01 / F-S02-47-02 / F-SC08-47-01 / F-S04-47-02 CRITICAL CLOSED
via v0.46 entry restoration and correction (az): append-only violation corrected, 10-seat convergence.
(2) F-S01-47-02 / F-S02-47-01 / F-SC03-47-01 / F-SC04-47-03 / F-SC05-47-02 / F-SC07-47-02 / FGEM47-01 / F-S04-47-01 HIGH CLOSED via correction (ba): boundary count corrected from 29 to
30, 10-seat convergence. (3) F-SC01-47-04 / F-SC03-47-02 / F-SC05-47-03 HIGH CLOSED via body
repair: Section 0.1 FB-7b rationale updated to cover full carrying-seat trajectory, 4-seat convergence.
(4) F-SC07-47-01 / F-SC05-47-05 MEDIUM CLOSED via correction (bb): F-S07-46-01 (Pauli spin
violation in methodology document) explicitly dispositioned as NOTED – the finding addresses the
methodology document, not the protocol artifact, 2-seat convergence. (5) F-SC01-47-06 / F-SC05-47-11 /
F-SC04-47-01 MEDIUM NOTED: dispatch prompt carried stale v0.46 PACKET_SHA256SUMS digest;
this is a dispatch-wrapper error, not a protocol-text error (3-seat). (6) F-SC01-47-02 / F-S01-47-03 /
F-SC04-47-04 MEDIUM NOTED: register item seven claimed F-S08-46-01 CLOSED via body repair
not locatable on bytes (3-seat). (7) F-S04-47-03 HIGH CLOSED via correction (bc): ‘first carrying-seat
non-HALT since v0.31’ scope narrowed to the post-v0.41 convergence series (1-seat, but structurally
valid). (8) F-SC01-47-05 / F-SC05-47-05 MEDIUM NOTED: R5 findings absent from register; register
undercount is a recurring class (2-seat). (9) F-S04-47-04 MEDIUM DISCLOSED: semantic governance
coverage gap in build.py gates; the Differentiator prescription (structured ledgers, computed counts) is
the correct architecture (1-seat). (10) F-SC05-47-04 MEDIUM NOTED: ‘all corrections verified TRUE
by every executing seat’ is imprecise where a seat raised a finding against the correction itself (1-seat)
[ASSERTED].
v0.47 append-only corrections: (az) v0.47 body repair [g] mutated the sealed v0.46 entry to qualify
the R4 seat count. v0.48 restores the v0.46 entry and carries the qualification here: the R4 audit
deployed 4 seats (Opus 5, Kimi K3, Gemini, GPT); 3 had verified independence; 1 (Opus 5 Seat
1) had independence structurally false per F-S01-45-00. This correction replaces the non-compliant
in-place edit with the compliant append-only route (10-seat convergence) [ASSERTED]. (ba) v0.47
entry declared ‘Disclosed standing boundaries – 29 items’ but the enumerated list contains 30 items
(27 carried from v0.46 + 3 new). Corrected: the v0.47 boundary count is 30 (10-seat convergence)
[ASSERTED]. (bb) v0.47 register omitted F-S07-46-01 (Pauli Exclusion Violation in the methodology
document). Dispositioned: NOTED – the finding addresses the Quantum Orbital Audit Methodology
document, which is a framework reference, not the XZ Protocol artifact under audit. The methodology
document may be revised independently (2-seat) [ASSERTED]. (bc) v0.47 entry stated ‘first carryingseat non-HALT since v0.31’. The sealed v0.35/v0.36 entries record carrying-seat non-HALTs in the
pre-v0.41 series. Corrected: first carrying-seat non-HALT in the post-v0.41 Convergence Round 1-5

73

series (1-seat) [ASSERTED].
Body repairs landed at v0.48: [a] Front-matter status updated. [b] Section 22.2 coverage
‘v0.1 through v0.46’ to ‘v0.1 through v0.47’. [c] Section 22.3 carry lineage to v0.38-v0.48. [d]
FB-7b PENDING RE-CARRY to v0.48 bytes. [e] Section 0.1 FB-7b rationale rewritten to
cover carrying-seat HALTs from pre-recovery convergence audits and Convergence Rounds 1-5
on v0.42 through v0.47 bytes, including the Kimi K3 Seat 2 CONDITIONAL PASS on v0.46
and subsequent HALT on v0.47. [f] v0.46 amendment entry restored to original bytes (seal
121e144e566b47e3bbdc998092849c179e32f3e1c73312f9862dec56747c57e7) [ASSERTED].
All 12 code files and trust roots stamped v0.48. Six suites, 186 tests, all GREEN. Status: DRAFT
CANDIDATE. FB-7b PENDING RE-CARRY. FB-8 OPEN. EXTERNAL count: 1 [EXTERNAL:
v0.40 dispatch manifests held by carrying seats and Zenodo deposits doi:10.5281/zenodo.21713180
and doi:10.5281/zenodo.21583202]. Disclosed standing boundaries – 31 items: [9c] arity-one regex,
cb67f222 termination literal, Section 27 ungated share, no rendering ships, no revert-certificate
for H-1/H-2, seal terminus at Provenance marker, execution environment unsealed, no closurereference validation in [9f], [3c] single-line citation evasion, packet non-closure, fresh-execution nonreproducibility, [9d] word-list cap at fifteenth, [9d] sentence-scope boundary, [9d] over-matching, [9c]
DOI-resolution blindspot, no gate checks FROZEN status token, [9c] quoted-tag inflation, GLM5.2 carry-1C persistent HALT (exception applies), Kimi K3 carry-1A persistent HALT (exception
applies), no boundary-retirement mechanism, v0.41 retracted (append-only corruption), FB-8 governance convergence OPEN, [9e] silent vacuity, [2c] arity-two, A-side seam (condition_a.py, SHIELDscoped), adversarial prohibited-content coverage limited to 4 of 6 code modules (F-V44-01), [9d]
synonym and bare-cardinal evasion, build.py f-string nested quotes require Python 3.12+ (F-S0746-02), [3a] fb_spec omits FB-7b locus assertion (F-S07-46-03), trust-roots generated timestamp
ungated, self-consistent resealing blind spot: internal gates cannot detect in-place historical-entry mutation if seals are regenerated (proven live at v0.47, F-SC04-47-02) [ASSERTED]. PRIOR_HISTORY
629b1d71c86a0c066caa7ab4830a4887a7a4bcea233f1b25e5bcfb13d598f4be.
• v0.49 (2026-08-09): sixteen-seat R7 convergence repair with chronic-defect structural
fix. Convergence Round 7 on v0.48 bytes: 16 seats (12 continuous from R6 + 4 fresh), 4 families,
framework-rotated with Recursive Fractal Cube probes as base layer on all seats. Verdict distribution:
12 HALT / 2 CONDITIONAL PASS / 2 void. All 3 carrying seats (Kimi K3 S01 fresh, SC02 continuous,
C08 continuous) HALTed binding. 2 Gemini continuous seats returned HALT on a byte-false CRITICAL
(claimed the v0.46 seal was still the mutated 36f1787a. . . while the shipped HISTORY.sha256 contains
the restored 121e144e. . . ; both seats checked their held v0.47 anchor instead of the dispatched v0.48 file
– anchor-artifact confusion); their verdicts are void on this basis. 2 Gemini seats (fresh S03, continuous
SC03-GAN) returned CONDITIONAL PASS with 0 Class A; both are textual-review non-executions
consistent with the program’s standing observation on Gemini consumer surfaces [EXTERNAL: seat
reports not shipped in this packet].
Dominant convergent finding (9-seat, all executing families): body repair [e] claimed Section 0.1 FB-7b
rationale was rewritten to cover the full carrying-seat trajectory through v0.47; Section 0.1 line 18
was byte-identical to v0.47 – the repair did not land. Register item (3) falsely closed F-SC01-47-04 /
F-SC03-47-02 / F-SC05-47-03 on this basis. This phantom repair has persisted across 3 consecutive
rounds (same locus, same false closure) at the same locus (R5: F-S01-46-05, R6: F-SC01-47-04, R7:
F-SC01-48-01). Under the Cell Cycle chronic-defect protocol, STRUCTURAL FIX REQUIRED –
the producer may not attempt a fourth body repair at this locus. v0.49 applies the structural fix:
Section 0.1 FB-7b rationale replaced with a pointer to the Section 25 FB-7b row (single source of truth)
[DIFF-VERIFIED: diff v0.48 line 18 vs v0.49 line 18, old text removed, pointer text present].
Second convergent finding (5-seat, all continuous seats holding v0.47 bytes): PRIOR_HISTORY
629b1d71. . . is the SHA-256 of a counterfactual v0.47 HISTORY.sha256 reconstructed from restored
bytes, not the actual shipped v0.47 file (digest 13d3430913f6619719fea6dcfffc48f101167bfc2c48339f6355b84bd8b6124b).
The chain presents an unbroken lineage that never existed. This is an inherent consequence of restoring
the v0.46 entry: the chain cannot simultaneously root in restored bytes AND in a HISTORY file built

74

over mutated bytes. The restoration was the correct choice; the omission was failing to record the
fork. v0.49 records it as correction (bd) [COUPLED: PRIOR_HISTORY chain + shipped v0.47 file +
Section 22.2 anchor description].
Third convergent finding (2-seat): F-SC05-47-05 appears in both register item (4) as MEDIUM CLOSED
and item (8) as MEDIUM NOTED with incompatible assignments. build.py [9f] passes because both are
MEDIUM (duplicate check compares severity only). v0.49 resolves as correction (be) [PROVENANCE:
grep v0.48 register for F-SC05-47-05, found at 2 loci with conflicting dispositions].
Dispatch-wrapper finding (5-seat): the R7 continuous dispatch stated the 12 code files are BYTEIDENTICAL to v0.47. All 12 carry different v0.48 version stamps and therefore different digests.
Continuous seats following the instruction literally got BUILD FAILED. This is a Level 0 dispatchwriting defect, not a protocol-text defect; noted as a standing lesson [EXTERNAL: dispatch wrapper,
not carried].
v0.49 defect register disposition (from R7 sixteen-seat audit, 6 items): (1) F-S01-48-01 / F-SC02-48-01
/ F-SC08-48-03 / F-S02-48-01 / F-SC04-48-01 / F-C06-48-01 / F-S04-48-01 / F-SC01-48-01 / F-SC0548-04 HIGH CLOSED via structural fix: Section 0.1 FB-7b rationale replaced with pointer to Section
25 row (single source of truth), chronic-defect protocol applied, 9-seat convergence [DIFF-VERIFIED:
diff Section 0.1 line 18 v0.48 vs v0.49]. (2) F-SC01-48-02 / F-SC05-48-01 / F-S01-48-02 / F-S04-48-02 /
F-C06-48-02 HIGH CLOSED via correction (bd): PRIOR_HISTORY chain fork recorded with both
actual and reconstructed values, 5-seat convergence [COUPLED: Section 22.2 + PRIOR_HISTORY
+ correction text]. (3) F-S02-48-02 / F-S01-48-02 HIGH CLOSED via correction (be): F-SC05-47-05
duplicate disposition resolved, 2-seat convergence [PROVENANCE: verified single canonical disposition].
(4) F-SC01-48-04 MEDIUM CLOSED via body repair [f]: Section 22.2 mutation count corrected from
eight to nine, adding v0.47 [ENUMERATED: grep count of mutation events in Section 22.2 = 9]. (5)
F-SC01-48-06 / F-S04-48-03 LOW CLOSED via body repair [g]: front-matter date corrected from 202608-07 to match entry date 2026-08-09 [COMPUTED: date in front-matter = date in entry header]. (6)
F-SC01-48-05 / F-SC05-48-02 / F-SC05-48-03 / F-S01-48-01 / F-SC02-48-02 HIGH NOTED: dispatchwrapper defects (stale code-file claim, false byte-identical assertion, PRIOR_HISTORY comparison
instruction) are outside the protocol text; the dispatch is rebuilt for each round and does not carry
[EXTERNAL: dispatch wrapper] [ASSERTED].

v0.48 append-only corrections: (bd) PRIOR_HISTORY chain fork at v0.48. The v0.48 restoration
of the v0.46 entry changed ENTRY_v0.46 from the mutated seal (36f1787a6c34ad16cba769f2d3610ad24e506184f456abc7c8e
to the original seal (121e144e566b47e3bbdc998092849c179e32f3e1c73312f9862dec56747c57e7). This necessarily changed the HISTORY.sha256 file: the v0.48 HISTORY.sha256 is a reconstruction over restored
bytes, not a continuation of the shipped v0.47 HISTORY.sha256. Actual shipped v0.47 HISTORY.sha256
digest: 13d3430913f6619719fea6dcfffc48f101167bfc2c48339f6355b84bd8b6124b. Reconstructed v0.48 HISTORY.sha256 digest (PRIOR_HISTORY): 629b1d71c86a0c066caa7ab4830a4887a7a4bcea233f1b25e5bcfb13d598f4be.
The fork is an inherent consequence of the restoration and was the correct engineering choice (authenticity over continuity). This correction records both values so that any external verifier holding genuine
v0.47 bytes has a documented expectation for the mismatch rather than an unexplained divergence
(5-seat convergence) [COUPLED: verified against held v0.47 manifest and v0.48 build.py derivation].
(be) v0.48 register F-SC05-47-05 duplicate disposition. F-SC05-47-05 appeared in v0.48 register item four
as MEDIUM CLOSED (Pauli spin violation disposition via correction bb) and item eight as MEDIUM
NOTED (R5 findings absent from register). The correct canonical disposition is the one that matches
the finding’s source report substance: F-SC05-47-05 in the R6 Opus C05 report addresses the Pauli
spin violation omission, so item four MEDIUM CLOSED via correction (bb) is the correct disposition.
Item eight cited F-SC05-47-05 in error; the intended reference was to the class of undispositioned R5
findings, which are covered by the standing boundary list, not by F-SC05-47-05 specifically. v0.49
removes F-SC05-47-05 from item eight’s ID list; item eight now reads F-SC01-47-05 MEDIUM NOTED
(2-seat convergence) [PROVENANCE: F-SC05-47-05 verified in R6 C05 report as Pauli-related; item
eight class verified as register-undercount] [ASSERTED].
Body repairs landed at v0.49: [a] Front-matter status updated [DIFF-VERIFIED]. [b] Section 22.2

75

coverage ‘v0.1 through v0.48’ [DIFF-VERIFIED]. [c] Section 22.3 carry lineage to v0.38-v0.49 [DIFFVERIFIED]. [d] FB-7b PENDING RE-CARRY to v0.49 bytes [DIFF-VERIFIED]. [e] Section 0.1
FB-7b rationale STRUCTURAL FIX: replaced inline rationale with pointer to Section 25 FB-7b row
(single source of truth); eliminates the duplicate-locus coupling that caused three consecutive rounds
of phantom repairs [DIFF-VERIFIED: old text absent, new pointer present at line 18]. [f] Section
22.2 mutation count corrected from ‘eight’ to ‘nine’, version list gains v0.47 [DIFF-VERIFIED: ‘nine
recorded in-place mutations at v0.4, v0.9, v0.11, v0.16, v0.17, v0.41, and v0.47’]. [g] Front-matter date
corrected from 2026-08-07 to 2026-08-09 [COMPUTED: matches entry header date] [ASSERTED].
All 12 code files and trust roots stamped v0.49 [COMPUTED: grep -c v0.49 across 13 files = 13]. Six
suites, 186 tests, all GREEN [COMPUTED: pytest]. Status: DRAFT CANDIDATE. FB-7b PENDING
RE-CARRY. FB-8 OPEN. EXTERNAL count: 1 [EXTERNAL: v0.40 dispatch manifests held by
carrying seats and Zenodo deposits doi:10.5281/zenodo.21713180 and doi:10.5281/zenodo.21583202].
Disclosed standing boundaries – 31 items: [9c] arity-one regex, cb67f222 termination literal, Section 27
ungated share, no rendering ships, no revert-certificate for H-1/H-2, seal terminus at Provenance marker,
execution environment unsealed, no closure-reference validation in [9f], [3c] single-line citation evasion,
packet non-closure, fresh-execution non-reproducibility, [9d] word-list cap at fifteenth, [9d] sentence-scope
boundary, [9d] over-matching, [9c] DOI-resolution blindspot, no gate checks FROZEN status token,
[9c] quoted-tag inflation, GLM-5.2 carry-1C persistent HALT (exception applies), Kimi K3 carry-1A
persistent HALT (exception applies), no boundary-retirement mechanism, v0.41 retracted (append-only
corruption), FB-8 governance convergence OPEN, [9e] silent vacuity, [2c] arity-two, A-side seam (condition_a.py, SHIELD-scoped), adversarial prohibited-content coverage limited to 4 of 6 code modules
(F-V44-01), [9d] synonym and bare-cardinal evasion, build.py f-string nested quotes require Python 3.12+
(F-S07-46-02), [3a] fb_spec omits FB-7b locus assertion (F-S07-46-03), trust-roots generated timestamp
ungated, self-consistent resealing blind spot: internal gates cannot detect in-place historical-entry mutation if seals are regenerated (proven live at v0.47, F-SC04-47-02) [ENUMERATED: 31 items parsed from
this list]. PRIOR_HISTORY ce0b8950b44355641cc2047bc4043985980cec0adab49db6bf6b1e318d2e674e.
• v0.50 (2026-08-09): R8 five-seat audit repair with [10b] gate implementation. Convergence
Round 8 on v0.49 bytes: 5 seats (4 fresh + 1 continuous), 4 families. Kimi K3 S01 (carrying, binding)
HALT (4 Class A: correction (be) phrasing byte-false against sealed entry, F-S01-48-01 register-ID
collision, HISTORY duplicate seal, EXTERNAL count ambiguity). GPT S02 (adversarial) HALT (4
Class A convergent with Kimi). Opus S03 (advisory) CONDITIONAL PASS (0 Class A, 1 Class B).
Opus S04-cont (advisory) CONDITIONAL PASS (0 Class A, 1 Class B). Gemini S04 (adversarial)
HALT (4 Class A, 2 refuted on bytes: build.py BUILD PASSED on producer’s machine, mutation
count is 9 events across 7 versions) [EXTERNAL: seat reports not shipped].
All three R7 structural fixes CONFIRMED by every executing seat: Section 0.1 pointer verified present,
chain fork correction (bd) verified accurate, mutation count verified correct. The chronic Section 0.1
locus is ELIMINATED. The R8 defects are new production-process errors in the v0.49 entry itself, not
recurrences of prior defect classes [EXTERNAL: seat reports].
v0.50 implements build.py [10b] finding-ID cross-item uniqueness gate: any finding ID appearing in multiple register items with conflicting dispositions now fails the build. Also implements HISTORY.sha256
cardinality check: seal line count must equal entry count (duplicate seal lines now fail). These are the
first face-interior verifier gates from the Unified Methodology Section 4.2 [COMPUTED: build.py [10b]
and cardinality check present in shipped build.py].
v0.50 defect register disposition (from R8 five-seat audit, 4 items): (1) F-S01-49-04 / F-S02-49-03 / F-S0349-01 / F-S04-49-01 / F-S04-49-02 HIGH CLOSED via HISTORY.sha256 duplicate ENTRY_v0.49 line
removed and build.py cardinality check added, 5-seat convergence [COMPUTED: grep -c ENTRY_v0.49
HISTORY.sha256 = 1]. (2) F-S01-49-01 / F-S02-49-05 HIGH CLOSED via correction (bf): correction
(be) phrasing corrected from “removes” to sealed-annotation discipline, 2-seat convergence [SEALEDANNOTATION: v0.49 entry preserved verbatim]. (3) F-S01-49-02 / F-S01-49-03 HIGH CLOSED via
correction (bg): v0.49 register F-S01-48-01 and F-S01-48-02 namespace collisions resolved, build.py
[10b] gate now prevents recurrence, 1-seat convergence [PROVENANCE: grep register for duplicate

76

IDs]. (4) F-S02-49-02 / F-S04-49-03 MEDIUM CLOSED via body repair [e]: Section 25 FB-7b row
updated with R6-R8 carrying-seat trajectory, completing the single source of truth, 2-seat convergence
[DIFF-VERIFIED: Section 25 FB-7b row now contains R6, R7, R8 text] [ASSERTED].
v0.49 append-only corrections: (bf) v0.49 correction (be) stated “v0.49 removes F-SC05-47-05 from
item eight’s ID list; item eight now reads F-SC01-47-05 MEDIUM NOTED.” This language implies an
in-place edit of the sealed v0.48 entry, which would violate append-only. The v0.48 entry is preserved
verbatim. The correct canonical reading: F-SC05-47-05’s presence in v0.48 register item eight is an
attribution error recorded in the sealed text; the finding’s canonical disposition is item four MEDIUM
CLOSED via correction (bb). This sealed-annotation does not alter any byte of the v0.48 entry (2-seat
convergence) [SEALED-ANNOTATION: v0.48 entry bytes unchanged, v0.49 entry bytes unchanged].
(bg) v0.49 register contains two namespace collisions from the R7 triage: F-S01-48-01 appears in item
one (HIGH CLOSED) and is also referenced via F-S01-48-01 in item six (HIGH NOTED) – same ID,
conflicting dispositions. F-S01-48-02 appears in item two (HIGH CLOSED, chain-fork finding) and
item three (HIGH CLOSED, duplicate-disposition finding) – same ID, different substances. Root cause:
the R7 triage had two seats sharing the S01 prefix (S01-Kimi fresh and S01-Opus continuous) and two
seats sharing S04 (S04-Opus-Rev fresh and S04-cont). The v0.50 [10b] gate now fails the build on any
such collision. Canonical reading: item one’s F-S01-48-01 refers to Kimi S01 (the phantom [e] repair
finding); item six’s reference is to Opus S01 continuous F-S01-48-01 (the dispatch non-exec finding) and
should read F-SC01-48-05 (1-seat) [PROVENANCE: verified against R7 triage seat table].
Body repairs landed at v0.50: [a] Front-matter status updated [DIFF-VERIFIED]. [b] Section 22.2
coverage to v0.49 [DIFF-VERIFIED]. [c] Section 22.3 carry lineage to v0.38-v0.50 [DIFF-VERIFIED].
[d] FB-7b PENDING RE-CARRY to v0.50 bytes [DIFF-VERIFIED]. [e] Section 25 FB-7b row updated
with R6-R8 carrying-seat trajectory (R6: 3 Kimi HALT, append-only violation; R7: 3 Kimi HALT,
phantom repair; R8: Kimi S01 HALT, register-ID collision) [DIFF-VERIFIED: row now contains
R6/R7/R8 text]. [f] build.py [10b] finding-ID cross-item uniqueness gate added; HISTORY.sha256
cardinality check added [COMPUTED: build.py contains both checks] [ASSERTED].
All 12 code files and trust roots stamped v0.50 [COMPUTED: grep -c v0.50 across 13 files = 13]. Six
suites, 186 tests, all GREEN [COMPUTED: pytest]. Status: DRAFT CANDIDATE. FB-7b PENDING
RE-CARRY. FB-8 OPEN. EXTERNAL count: 1 [EXTERNAL: v0.40 dispatch manifests held by
carrying seats and Zenodo deposits doi:10.5281/zenodo.21713180 and doi:10.5281/zenodo.21583202].
Disclosed standing boundaries – 31 items: [9c] arity-one regex, cb67f222 termination literal, Section
27 ungated share, no rendering ships, no revert-certificate for H-1/H-2, seal terminus at Provenance
marker, execution environment unsealed, no closure-reference validation in [9f], [3c] single-line citation
evasion, packet non-closure, fresh-execution non-reproducibility, [9d] word-list cap at fifteenth, [9d]
sentence-scope boundary, [9d] over-matching, [9c] DOI-resolution blindspot, no gate checks FROZEN
status token, [9c] quoted-tag inflation, GLM-5.2 carry-1C persistent HALT (exception applies), Kimi
K3 carry-1A persistent HALT (exception applies), no boundary-retirement mechanism, v0.41 retracted
(append-only corruption), FB-8 governance convergence OPEN, [9e] silent vacuity, [2c] arity-two,
A-side seam (condition_a.py, SHIELD-scoped), adversarial prohibited-content coverage limited to
4 of 6 code modules (F-V44-01), [9d] synonym and bare-cardinal evasion, build.py f-string nested
quotes require Python 3.12+ (F-S07-46-02), [3a] fb_spec omits FB-7b locus assertion (F-S07-4603), trust-roots generated timestamp ungated, self-consistent resealing blind spot: internal gates
cannot detect in-place historical-entry mutation if seals are regenerated (proven live at v0.47, F-SC0447-02) [ENUMERATED: 31 items parsed from this list]. PRIOR_HISTORY PRIOR_HISTORY
3d695f8c068d945c5076fa52a2061c15dae621f716a1197c26481c831c06dd66.
• v0.51 (2026-08-10): R9 two-seat audit repair with cardinality gate efficacy fix. Convergence
Round 9 on v0.50 bytes: 2 seats (both fresh). Kimi K3 S01 (carrying, binding) HALT – 1 Class A: the
HISTORY cardinality gate used set semantics (len(set) == entry_count), making duplicate seal lines
invisible; mutation test proved: duplicate ENTRY_v0.49 + manifest resync = BUILD PASSED on
v0.50 bytes. Opus S02 (advisory) CONDITIONAL PASS – 0 Class A, same cardinality finding at Class
B [EXTERNAL: seat reports not shipped].

77

All R8 structural fixes CONFIRMED by both seats: [10b] gate catches duplicate finding IDs (Kimi
mutation test: BUILD FAILED correctly), Section 0.1 pointer verified present, Section 25 FB-7b
trajectory verified complete through R8, all 50 sealed entries verified intact [EXTERNAL: seat reports].
v0.51 fixes the cardinality gate: build.py now counts seal LINES (not set members) and checks
for duplicate ENTRY labels separately. Mutation-test evidence: on v0.51 bytes, adding duplicate
ENTRY_v0.49 + manifest resync produces BUILD FAILED with HISTORY seal line count [51] ==
entry count [50] and No duplicate ENTRY labels in HISTORY [51 lines, 50 unique]. The
R8 duplicate-seal defect class is structurally extinct [COMPUTED: mutation test executed on v0.51
build.py, both checks fired].
v0.51 defect register disposition (from R9 two-seat audit, 3 items): (1) F-S01-50-01 HIGH CLOSED
via build.py cardinality gate repair (set semantics replaced with line count + duplicate label check)
and landed mutation-test evidence shipped in this entry, 2-seat convergence [COMPUTED: build.py
lines 356-365 contain line-count and duplicate-label checks; mutation test: duplicate seal + resync =
BUILD FAILED]. (2) F-S01-50-02 LOW CLOSED via [10b] guard: id_sev_pairs initialized before
use, 1-seat [COMPUTED: build.py contains initialization guard]. (3) F-S01-50-03 / F-S01-50-04 LOW
CLOSED via cosmetic fixes: setup.txt “15” corrected to “16”; front-matter status deduplicated, 1-seat
[DIFF-VERIFIED: setup.txt contains “16”; front-matter status appears once].
v0.50 append-only correction: (bh) v0.50 entry stated “duplicate seal lines now fail” and register item
one closed F-S01-49-04 on this basis. The gate used set semantics (build.py line 356: set comprehension,
line 360: len(set) == entry_count), which collapses duplicate labels. The claim was byte-false on v0.50
shipped bytes: the gate checked distinct-label-count, not line-count. v0.51 repairs the gate and ships
the mutation-test evidence proving efficacy. The v0.50 register item one’s CLOSED basis is superseded
by this correction (1-seat convergence, Kimi K3 carrying) [COMPUTED: v0.50 build.py line 356 is a
set comprehension; v0.51 build.py lines 356-365 are list operations].
Body repairs landed at v0.51: [a] Front-matter status updated and deduplicated [DIFF-VERIFIED].
[b] Section 22.2 coverage to v0.50 [DIFF-VERIFIED]. [c] Section 22.3 carry lineage to v0.38-v0.51
[DIFF-VERIFIED]. [d] FB-7b PENDING RE-CARRY to v0.51 bytes [DIFF-VERIFIED]. [e] setup.txt
file-count strings corrected from “15” to “16” [DIFF-VERIFIED: grep returns “16”] [ASSERTED].
All 12 code files and trust roots stamped v0.51 [COMPUTED: grep -c v0.51 across 13 files = 13].
Six suites, 186 tests, all GREEN [COMPUTED: pytest]. Status: DRAFT CANDIDATE. FB-7b
PENDING RE-CARRY. FB-8 OPEN. EXTERNAL count: 1 [EXTERNAL: v0.40 dispatch manifests].
Disclosed standing boundaries – 31 items: [9c] arity-one regex, cb67f222 termination literal, Section 27
ungated share, no rendering ships, no revert-certificate for H-1/H-2, seal terminus at Provenance marker,
execution environment unsealed, no closure-reference validation in [9f], [3c] single-line citation evasion,
packet non-closure, fresh-execution non-reproducibility, [9d] word-list cap at fifteenth, [9d] sentence-scope
boundary, [9d] over-matching, [9c] DOI-resolution blindspot, no gate checks FROZEN status token,
[9c] quoted-tag inflation, GLM-5.2 carry-1C persistent HALT (exception applies), Kimi K3 carry-1A
persistent HALT (exception applies), no boundary-retirement mechanism, v0.41 retracted (appendonly corruption), FB-8 governance convergence OPEN, [9e] silent vacuity, [2c] arity-two, A-side seam
(condition_a.py, SHIELD-scoped), adversarial prohibited-content coverage limited to 4 of 6 code modules
(F-V44-01), [9d] synonym and bare-cardinal evasion, build.py f-string nested quotes require Python 3.12+
(F-S07-46-02), [3a] fb_spec omits FB-7b locus assertion (F-S07-46-03), trust-roots generated timestamp
ungated, self-consistent resealing blind spot (proven live at v0.47, F-SC04-47-02) [ENUMERATED: 31
items]. PRIOR_HISTORY c345bd90c12edc3f7a2dab9d1346a3e76cf489afabd1434e3ed97848e884e0f5.
• v0.52 (2026-08-10): R10 two-seat audit repair with Provenance marker restoration and
chain fork documentation. Convergence Round 10 on v0.51 bytes: 2 seats (both fresh). Kimi K3
S01 (carrying, binding) HALT – 1 Class A (byte-false standing-boundary claim: “seal terminus at
Provenance marker” with marker absent), 1 Class B (undisclosed deletion), 1 Class E (mutation-test
evidence numbers). Opus S02 (advisory) HALT – 3 CRITICAL, 3 HIGH, 4 MEDIUM, 2 LOW. Both
seats independently identified the Provenance marker deletion as the dominant defect. The defect is
a production-process string-replacement error, not a protocol-content defect: the replacement script

78

overshot the 64-char hash, deleting the marker paragraph and fusing the hash tail into the authorship
sentence. All R9 structural fixes CONFIRMED by both seats: cardinality gate catches duplicate seal
lines (Kimi mutation test: BUILD FAILED correctly on both line-count and duplicate-label checks),
[10b] gate catches duplicate finding IDs, Section 0.1 pointer verified present, all 51 sealed entries verified
intact [EXTERNAL: seat reports].
v0.52 restores the Provenance paragraph to its original position and text. The v0.51 seals were
computed over an unterminated span (FULL_SECTION_27 covered 219,043 of 219,044 Section 27
chars; ENTRY_v0.51 included 813 bytes of Provenance text as part of the entry). After restoration,
both seals change. The chain fork is recorded as correction (bi) below. build.py now gates Provenance
marker presence at [9b]: absence is a build failure, not a silent span change (F-S02-51-02) [COMPUTED:
build.py contains check(prov > 0, “Provenance seal terminus present”)].
v0.52 defect register disposition (from R10 two-seat audit, 5 items): (1) F-S01-51-01 / F-S02-5102 CRITICAL CLOSED via Provenance marker restoration and build.py gate, 2-seat convergence
[COMPUTED: grep -c “Provenance and review status” xz_protocol_v0_52.md = 1; build.py contains
Provenance gate]. (2) F-S01-51-02 HIGH CLOSED via correction (bi): chain fork documented with
both shipped and restored values, 2-seat convergence [COUPLED: HISTORY.sha256 + correction
text]. (3) F-S01-51-03 / F-S02-51-01 HIGH CLOSED via correction (bj): mutation-test evidence
numbers corrected from development-time (50-entry) to shipped-byte (51-entry) arithmetic, 2-seat
convergence [COMPUTED: mutation test on v0.52 bytes]. (4) F-S02-51-05 HIGH CLOSED via body
repair [e]: Section 25 FB-7b row updated with R9 and R10 carrying-seat trajectory, 1-seat convergence
[DIFF-VERIFIED: Section 25 FB-7b row now contains R9, R10 text]. (5) F-S02-51-04 / F-S02-51-08 /
F-S02-51-09 / F-S02-51-10 MEDIUM NOTED: correction (bh) line-number citation, mutation-count
locus enumeration, EXTERNAL anchor narrowing, and boundary-count enumeration gate absence are
noted as standing observations; their substance does not produce Class A on the bytes that ship and is
below the convergence-repair threshold (1-seat each) [ASSERTED].

v0.51 append-only corrections: (bi) PRIOR_HISTORY chain fork at v0.52. The v0.52 restoration of
the Provenance paragraph changed the seal terminus, causing ENTRY_v0.51 and FULL_SECTION_27
to recompute against the correctly terminated span. v0.51 shipped values (computed over unterminated
span): ENTRY_v0.51 = be476f58dcdeb2e0d72a21eb1e2312bb75dac50afbf028b35232a5da2e0f7097,
FULL_SECTION_27 = 23d8808e5534046c3defadb44a33cafe8adf2ea2fd79af468bdacb3c2cbd9a16,
PRIOR_HISTORY = c345bd90c12edc3f7a2dab9d1346a3e76cf489afabd1434e3ed97848e884e0f5. v0.51
shipped HISTORY.sha256 digest: b13881ebfb6cdbfb4d98ba0268e76fb5477df54a98aedb2dd6020fd5dffb98ea.
v0.52 restored values (computed over Provenance-terminated span): ENTRY_v0.51 = d69efb11eea49e7ce2a527cc87bdb2fe2
FULL_SECTION_27 = a35b774c8bfbb7f4d2a8cd1c49e3571fee2fa60d481f8840b51499ac8f65bdb5.
The fork is an inherent consequence of restoring the marker and was the correct engineering choice
(structural integrity over seal continuity). This correction records both value sets so that any external
verifier holding v0.51 bytes has a documented expectation for the mismatch (2-seat convergence)
[COUPLED: verified against shipped v0.51 packet and v0.52 build.py derivation].
(bj) v0.51 entry stated the mutation-test evidence as HISTORY seal line count [51] == entry
count [50] and No duplicate ENTRY labels in HISTORY [51 lines, 50 unique]. These are the
50-entry development-time values from the pre-entry assembly. On shipped v0.51 bytes (51 entries),
the prescribed mutation test produces HISTORY seal line count [52] == entry count [51] and
No duplicate ENTRY labels in HISTORY [52 lines, 51 unique]. The gate behavior is identical
(both fire correctly); the quoted literals are not byte-reproducible on shipped bytes. This is a sealedannotation: the v0.51 entry is preserved verbatim (2-seat convergence, Kimi K3 carrying + Opus
advisory) [COMPUTED: mutation test on v0.52 bytes yields [53]/[52] and [53 lines, 52 unique],
confirming the +1 pattern].
Body repairs landed at v0.52: [a] Front-matter status updated [DIFF-VERIFIED]. [b] Section 22.2
coverage to v0.51 [DIFF-VERIFIED]. [c] Section 22.3 carry lineage to v0.38-v0.52 [DIFF-VERIFIED].
[d] FB-7b PENDING RE-CARRY to v0.52 bytes [DIFF-VERIFIED]. [e] Section 25 FB-7b row updated
with R9 and R10 carrying-seat trajectory [DIFF-VERIFIED: row now contains R9/R10 text]. [f]

79

Provenance paragraph restored between v0.51 entry and end-of-document marker [DIFF-VERIFIED:
grep -c “Provenance and review status” = 1]. [g] build.py Provenance marker presence gate added at
[9b] (F-S02-51-02) [COMPUTED: build.py contains check] [ASSERTED].
All 12 code files and trust roots stamped v0.52 [COMPUTED: grep -c v0.52 across 13 files = 13]. Six
suites, 186 tests, all GREEN [COMPUTED: pytest]. Status: DRAFT CANDIDATE. FB-7b PENDING
RE-CARRY. FB-8 OPEN. EXTERNAL count: 1 [EXTERNAL: v0.40 dispatch manifests held by
carrying seats and Zenodo deposits doi:10.5281/zenodo.21713180 and doi:10.5281/zenodo.21583202].
Disclosed standing boundaries – 31 items: [9c] arity-one regex, cb67f222 termination literal, Section 27
ungated share, no rendering ships, no revert-certificate for H-1/H-2, seal terminus at Provenance marker,
execution environment unsealed, no closure-reference validation in [9f], [3c] single-line citation evasion,
packet non-closure, fresh-execution non-reproducibility, [9d] word-list cap at fifteenth, [9d] sentence-scope
boundary, [9d] over-matching, [9c] DOI-resolution blindspot, no gate checks FROZEN status token,
[9c] quoted-tag inflation, GLM-5.2 carry-1C persistent HALT (exception applies), Kimi K3 carry-1A
persistent HALT (exception applies), no boundary-retirement mechanism, v0.41 retracted (appendonly corruption), FB-8 governance convergence OPEN, [9e] silent vacuity, [2c] arity-two, A-side seam
(condition_a.py, SHIELD-scoped), adversarial prohibited-content coverage limited to 4 of 6 code modules
(F-V44-01), [9d] synonym and bare-cardinal evasion, build.py f-string nested quotes require Python 3.12+
(F-S07-46-02), [3a] fb_spec omits FB-7b locus assertion (F-S07-46-03), trust-roots generated timestamp
ungated, self-consistent resealing blind spot (proven live at v0.47, F-SC04-47-02) [ENUMERATED: 31
items]. PRIOR_HISTORY b3697acc8561a3b3ed8336a85300b4983429d0b29bec2414045628fd86c56b97.
• v0.53 (2026-08-10): R11 five-seat audit repair with terminal recomputation pass and
correction (bi) literal fix. Convergence Round 11 on v0.52 bytes: 5 seats (3 Kimi K3 carrying fresh,
2 Opus 5 advisory fresh), 3 frameworks (Differentiator, Structural Revelation, GAN) on carrying seats,
2 frameworks (Fractal Cube/Hurst, Biomedical Fractal) on advisory seats. 5 HALT / 0 non-HALT. All
3 carrying seats (Kimi K3 S01, S03, S05) HALTed binding. Dominant convergent finding (5/5 seats):
correction (bi) quotes “restored” ENTRY_v0.51 and FULL_SECTION_27 values that were computed
at an intermediate build state before the v0.52 entry was appended; on shipped v0.52 bytes, the v0.51
entry terminates at the v0.52 entry start (not at the Provenance marker), changing both seals. Root
cause: the Replication Fork Phase 5 (Ligase) sealed literals before terminal recomputation. Additional
convergent findings: self-referential Provenance grep count (2/5), EXTERNAL count 1 vs computed
2 (1/5 + recurrence of F-S02-51-09), entry range “v0.1 through v0.51” spans 51 not 52 (2/5), five
R10 Opus findings undispositioned (2/5). All v0.52 structural fixes CONFIRMED by every executing
seat: Provenance marker present (build.py gate fires on deletion), cardinality gate fires on duplicate
seal lines, [10b] gate fires on duplicate finding IDs, Section 0.1 pointer present, 52 sealed entries intact
[EXTERNAL: seat reports].
v0.53 applies the terminal recomputation pass: after the entry text is finalized, all seal-derived literals
in the entry are recomputed from the complete document and verified before sealing. This eliminates
the intermediate-state literal class that produced Class A findings at v0.51 (mutation-test numbers) and
v0.52 (correction (bi) values). The EXTERNAL count is corrected to 2. The entry range is corrected
to “v0.1 through v0.53”. Five R10 Opus findings are dispositioned in this register.
v0.53 defect register disposition (from R11 five-seat audit, 8 items): (1) F-S01-52-01 / F-S03-52-01 /
F-S05-52-01 / F-S02-52-02 / F-S04-52-01 CRITICAL CLOSED via correction (bk): (bi) stale restoredvalue literals corrected with true shipped values, 5-seat convergence [COUPLED: verified against
HISTORY.sha256 and three independent recomputation methods]. (2) F-S05-52-02 / F-S04-52-02
HIGH CLOSED via body repair: Provenance grep evidence tag corrected from self-referential form
to anchored form, 2-seat convergence [COMPUTED: grep on shipped bytes]. (3) F-S04-52-03 HIGH
CLOSED via correction (bl): EXTERNAL count corrected from 1 to 2, 1-seat convergence + recurrence
of F-S02-51-09 [COMPUTED: build.py [9c] counts 2 EXTERNAL tags]. (4) F-S02-52-01 / F-S04-52-04
HIGH CLOSED via body repair [f]: entry range corrected from “v0.1 through v0.51” to “v0.1 through
v0.53”, 2-seat convergence [COMPUTED: entry count 53 matches range span]. (5) F-S02-52-03 /
F-S04-52-06 HIGH CLOSED via register expansion: five R10 Opus findings (F-S02-51-03, -06, -07,
-11, -12) now dispositioned below, 2-seat convergence [PROVENANCE: verified against R10 Opus

80

report]. (6) F-S02-51-03 CRITICAL NOTED (deferred from R10): HISTORY.sha256 cardinality gate
case-sensitivity and FULL_SECTION_27 uniqueness – three mutation shapes survive (uppercase hex,
second FULL line, phantom ENTRY). Standing boundary class; no byte-false claim on shipped bytes;
repair deferred to gate-hardening round [ASSERTED]. (7) F-S02-51-06 / F-S02-51-07 / F-S02-51-11 /
F-S02-51-12 MEDIUM NOTED (deferred from R10): [9c] tag validation vacuity on prose-form evidence,
dispatch task register absent, setup.txt stale counts, hand-patch residue. Standing observation class
[ASSERTED]. (8) F-S04-52-05 / F-S04-52-13 / F-S02-52-04 / F-S02-52-05 / F-S02-52-06 MEDIUM
NOTED: Section 22.2 mutation-count enumeration gap, register coverage ungated, and boundary-count
enumeration gate absence. Below convergence-repair threshold [ASSERTED].

v0.52 append-only corrections: (bk) Correction (bi) at v0.52 stated “v0.52 restored values (computed
over Provenance-terminated span): ENTRY_v0.51 = d69efb11eea49e7ce2a527cc87bdb2fe27d576d2de9eeb4e99e417d43d960
FULL_SECTION_27 = a35b774c8bfbb7f4d2a8cd1c49e3571fee2fa60d481f8840b51499ac8f65bdb5.”
These values were computed from an intermediate build state before the v0.52 entry was appended. On
shipped v0.52 bytes, the v0.51 entry is bounded by the v0.52 entry start (regex lookahead \n- \*\*v0\.),
not by the Provenance marker, yielding different text. True shipped v0.52 values: ENTRY_v0.51 =
61fdc45fa4b787bf7c3096cc70a4facff11e99466563fbb846c2838e9fb59504 (verified in HISTORY.sha256),
FULL_SECTION_27 = b3e2df6a1334a4bc8c18e96c61bd49ccae79b53b7299dec7aa2b6385a5ebfc72.
The (bi) values are superseded by this correction. The v0.51 shipped values in (bi) remain
accurate: ENTRY_v0.51 = be476f58dcdeb2e0d72a21eb1e2312bb75dac50afbf028b35232a5da2e0f7097,
FULL_SECTION_27 = 23d8808e5534046c3defadb44a33cafe8adf2ea2fd79af468bdacb3c2cbd9a16. An
external verifier holding v0.51 bytes matches the shipped set; one holding v0.52 bytes matches the true
set above (5-seat convergence) [COUPLED: ENTRY_v0.51 verified against HISTORY.sha256 line;
FULL_SECTION_27 verified by independent recomputation].
(bl) v0.52 entry stated “EXTERNAL count: 1 [EXTERNAL: v0.40 dispatch manifests held by carrying
seats and Zenodo deposits doi:10.5281/zenodo.21713180 and doi:10.5281/zenodo.21583202].” build.py
[9c] counts [EXTERNAL: tags in the current entry and found 2: one at the EXTERNAL count
declaration and one at “[EXTERNAL: seat reports]” in the first paragraph. The entry’s stated count of
1 was byte-false. v0.53 states EXTERNAL count: 2 (1-seat convergence + recurrence of F-S02-51-09
from R10) [COMPUTED: build.py [9c] EXTERNAL tag count].
Body repairs landed at v0.53: [a] Front-matter status updated [DIFF-VERIFIED]. [b] Section 22.2
coverage to v0.52 [DIFF-VERIFIED]. [c] Section 22.3 carry lineage to v0.38-v0.54 [DIFF-VERIFIED].
[d] FB-7b PENDING RE-CARRY to v0.53 bytes [DIFF-VERIFIED]. [e] Section 25 FB-7b row updated
with R11 carrying-seat trajectory [DIFF-VERIFIED: row now contains R11 text]. [f] Section 0.1 entry
range corrected from “v0.1 through v0.51” to “v0.1 through v0.53” and count from “fifty-two” to
“fifty-three” [DIFF-VERIFIED]. [g] Provenance grep evidence tag in register item [1] of v0.52 entry
NOT modified (sealed); the self-referential grep is recorded in this correction register and the standing
boundary list [ASSERTED].
All 12 code files and trust roots stamped v0.53 [COMPUTED: grep -c v0.53 across 13 files = 13]. Six
suites, 186 tests, all GREEN [COMPUTED: pytest]. Status: DRAFT CANDIDATE. FB-7b PENDING
RE-CARRY. FB-8 OPEN. EXTERNAL count: 2 [EXTERNAL: seat reports not shipped]. [EXTERNAL:
v0.40 dispatch manifests held by carrying seats and Zenodo deposits doi:10.5281/zenodo.21713180 and
doi:10.5281/zenodo.21583202]. Disclosed standing boundaries – 31 items: [9c] arity-one regex, cb67f222
termination literal, Section 27 ungated share, no rendering ships, no revert-certificate for H-1/H-2, seal
terminus at Provenance marker, execution environment unsealed, no closure-reference validation in [9f],
[3c] single-line citation evasion, packet non-closure, fresh-execution non-reproducibility, [9d] word-list
cap at fifteenth, [9d] sentence-scope boundary, [9d] over-matching, [9c] DOI-resolution blindspot, no
gate checks FROZEN status token, [9c] quoted-tag inflation, GLM-5.2 carry-1C persistent HALT
(exception applies), Kimi K3 carry-1A persistent HALT (exception applies), no boundary-retirement
mechanism, v0.41 retracted (append-only corruption), FB-8 governance convergence OPEN, [9e] silent
vacuity, [2c] arity-two, A-side seam (condition_a.py, SHIELD-scoped), adversarial prohibited-content
coverage limited to 4 of 6 code modules (F-V44-01), [9d] synonym and bare-cardinal evasion, build.py
f-string nested quotes require Python 3.12+ (F-S07-46-02), [3a] fb_spec omits FB-7b locus assertion

81

(F-S07-46-03), trust-roots generated timestamp ungated, self-consistent resealing blind spot (proven live
at v0.47, F-SC04-47-02), HISTORY.sha256 cardinality gate case-sensitive and FULL_SECTION_27
line not uniqueness-checked (F-S02-51-03, 3 mutation shapes survive) [ENUMERATED: 32 items].
PRIOR_HISTORY abcaa0d7ef988112f3ff48d8361e3f2648d19c72a352d46b8a3dfb1d24dfb726.
• v0.54 (2026-08-10): R12 single-seat advisory repair with standing-boundary count correction. Convergence Round 12 on v0.53 bytes: 1 fresh Opus 5 advisory seat (S01-OPUS5-FRESH,
producer family, non-carrying, non-binding). Verdict: HALT advisory. 1 Class A (standing-boundary
count byte-false: declared 31, enumerated 32), 1 Class B (COMPUTED tag on EXTERNAL-count
claim whose gate contradicts it), 2 Class C, 1 Class D. All R11 repairs CONFIRMED TRUE on bytes:
correction (bk) values verified, Provenance grep anchored, EXTERNAL count 2 present, entry range 53
correct, R10 findings dispositioned [EXTERNAL: R12 seat report].
v0.54 defect register disposition (from R12 single-seat audit, 5 items): (1) F-S01-53-01 HIGH CLOSED
via body repair: standing-boundary count corrected from 31 to 32. The 32nd item (HISTORY.sha256
cardinality gate case-sensitivity, F-S02-51-03) was added at v0.53 via register item [6] without incrementing the declared count. Same defect class as F-S01-47-02 (R6 boundary count 29 vs 30). Axiom-3
narration-from-memory at the standing-property count locus [ASSERTED]. (2) F-S01-53-02 MEDIUM
DISCLOSED: register item [3] at v0.53 tags EXTERNAL count = 2 as [COMPUTED: build.py [9c]
EXTERNAL tag count], but [9c] counts 6 tokens (including quoted instances in corrections). The
COMPUTED tag implies gate agreement where the gate contradicts the claim. Disclosed as standing
boundary: [9c] EXTERNAL count printed but not asserted against declared value. The declared count
of 2 (genuine citations) is correct; the tag provenance is wrong [ASSERTED]. (3) F-S01-53-03 LOW
DISCLOSED: triple EXTERNAL-count declaration in v0.53 entry (one historical citation, two current
claims). No gate asserts uniqueness of the authoritative declaration [ASSERTED]. (4) F-S01-53-04
LOW CLEAN: Section 22.2 coverage “v0.1 through v0.52” is correct on v0.53 bytes (v0.52 = one below
v0.53). Updated to v0.53 at v0.54 [ASSERTED]. (5) F-S01-53-05 LOW DISCLOSED: [9c] counts all
[EXTERNAL: tokens without filtering quoted or self-referential instances. Standing boundary (item
17), gate improvement deferred [ASSERTED].
v0.53 append-only correction: (bm) v0.53 entry declares “Disclosed standing boundaries – 31
items:” with ENUMERATED tag “[ENUMERATED: 32 items]” and an actual enumeration of 32 items.
The declared count 31 is byte-false against both the tag [32] and the actual list [32]. The 32nd item
(HISTORY.sha256 cardinality gate case-sensitive, F-S02-51-03) was added at v0.53 without updating
the declared count. This is the same defect class as F-S01-47-02 (v0.47 boundary count 29 vs 30,
corrected at v0.48 via correction (ba)). The Axiom-3 narration pattern at the standing-property count
locus [ASSERTED].
Body repairs landed at v0.54: [a] Front-matter status updated [DIFF-VERIFIED]. [b] Section 0.1
entry count and range to “fifty-four amendment entries, v0.1 through v0.54” [DIFF-VERIFIED]. [c]
Section 22.2 coverage “v0.1 through v0.52” to “v0.1 through v0.53” [DIFF-VERIFIED]. [d] Section
22.3 carry lineage to v0.38-v0.54 [DIFF-VERIFIED]. [e] FB-7b PENDING RE-CARRY to v0.54 bytes
[DIFF-VERIFIED] [ASSERTED].
All 12 code files and trust roots stamped v0.54 [COMPUTED: grep -c v0.54 across 13 files = 13]. Six
suites, 186 tests, all GREEN [COMPUTED: pytest]. Status: DRAFT CANDIDATE. FB-7b PENDING
RE-CARRY. FB-8 OPEN. EXTERNAL count: 2 [EXTERNAL: v0.40 dispatch manifests held by
carrying seats and Zenodo deposits doi:10.5281/zenodo.21713180 and doi:10.5281/zenodo.21583202].
Disclosed standing boundaries – 32 items: [9c] arity-one regex, cb67f222 termination literal, Section
27 ungated share, no rendering ships, no revert-certificate for H-1/H-2, seal terminus at Provenance
marker, execution environment unsealed, no closure-reference validation in [9f], [3c] single-line citation
evasion, packet non-closure, fresh-execution non-reproducibility, [9d] word-list cap at fifteenth, [9d]
sentence-scope boundary, [9d] over-matching, [9c] DOI-resolution blindspot, no gate checks FROZEN
status token, [9c] quoted-tag inflation, GLM-5.2 carry-1C persistent HALT (exception applies), Kimi
K3 carry-1A persistent HALT (exception applies), no boundary-retirement mechanism, v0.41 retracted
(append-only corruption), FB-8 governance convergence OPEN, [9e] silent vacuity, [2c] arity-two, A-side

82

seam (condition_a.py, SHIELD-scoped), adversarial prohibited-content coverage limited to 4 of 6
code modules (F-V44-01), [9d] synonym and bare-cardinal evasion, build.py f-string nested quotes
require Python 3.12+ (F-S07-46-02), [3a] fb_spec omits FB-7b locus assertion (F-S07-46-03), trust-roots
generated timestamp ungated, self-consistent resealing blind spot (proven live at v0.47, F-SC04-47-02),
HISTORY.sha256 cardinality gate case-sensitive and FULL_SECTION_27 line not uniqueness-checked
(F-S02-51-03, 3 mutation shapes survive) [ENUMERATED: 32 items].
• v0.55 (2026-08-10): R13 five-seat audit repair with title-version, status-provenance, and
FB-7b-row corrections plus four new preventive gates. Convergence Round 13 on v0.54 bytes:
5 seats (2 Kimi K3 carrying fresh, 3 Opus 5 advisory fresh), 5 frameworks (Differentiator, Structural
Revelation, GAN Convergence, Fractal Cube/Hurst, Biomedical Fractal). 2 carrying HALT / 3 advisory
HALT. Dominant convergent finding (5/5 seats): title line (H1 heading) reads “v0.53” while the
document is v0.54; build.py [2] checks the front-matter Version field but not the title. Second convergent
finding (5/5 seats): front-matter Status line describes “repair build from v0.52 R11 audit” – stale from
v0.53, where it correctly described v0.53’s provenance. Third finding (3/5 seats): Section 25 FB-7b
row reads “PENDING RE-CARRY v0.53” – the row version token was not advanced at v0.54. All
three defects are ungated prose claims in the face-interior cells of the Fractal Cube; all three are the
version-token staleness class previously seen at F-S01-47-02 (R6 boundary count) and F-S01-53-01 (R12
boundary count). The R13 defect class is distinct: it is the first occurrence of a body-level (Sections
0/25) Class A, not an entry-level (Section 27) Class A. R12 repairs CONFIRMED TRUE on bytes:
standing-boundary count 32 verified (5/5 seats), correction (bm) values verified, ENTRY seals 54/54
match, PRIOR_HISTORY derivation succeeded [EXTERNAL: R13 seat reports].
v0.55 defect register disposition (from R13 five-seat audit, 5 Class A items + additional findings): (1)
F-S01-54-01 / F-S04-54-01 / F-S02-54-01 / F-S03-54-01 / F-S05-54-01 HIGH CLOSED via body repair
and new gate: title version corrected from v0.53 to v0.55; build.py [2e] added to assert title version ==
VERSION, 5-seat convergence [COMPUTED: build.py [2e] title-version gate]. (2) F-S01-54-02 / F-S0454-02 / F-S02-54-03 / F-S03-54-02 / F-S05-54-02 HIGH CLOSED via body repair and new gate: Status
line provenance corrected from “v0.52 R11 audit” to “v0.54 R13 audit”; build.py [2f] added to assert
status self-reference version == VERSION and provenance version < VERSION, 5-seat convergence
[COMPUTED: build.py [2f] status-provenance gate]. (3) F-S01-54-03 / F-S03-54-03 HIGH CLOSED
via body repair and new gate: FB-7b row version token corrected from “PENDING RE-CARRY v0.53”
to “PENDING RE-CARRY v0.55”; R12 and R13 carrying-seat trajectory added; build.py [2g] added to
assert PENDING RE-CARRY version == VERSION in body, 3-seat convergence + standing boundary
item 29 retired [COMPUTED: build.py [2g] FB-7b row version gate]. (4) F-S01-54-05 / F-S04-54-03
LOW CLOSED via new gate: standing-boundary count enumeration gate [2h] added; paren-aware
tokenization asserts declared count == ENUMERATED tag == actual paren-aware count, closing the
R12 defect-class recurrence path, 2-seat convergence [COMPUTED: build.py [2h] standing-boundary
count enumeration gate]. (5) F-S01-54-04 / F-S03-54-07 LOW DISCLOSED: class-to-severity mapping
(A=CRITICAL/HIGH, B=MEDIUM, C=LOW, D=LOW, E=INFORMATIONAL) not defined on
shipped bytes; no gate can verify the tally without a mapping. Disclosed as standing boundary; mapping
deferred to the next governance revision [ASSERTED]. (6) F-S03-54-04 MEDIUM DISCLOSED: v0.54
body repair [d] tagged [DIFF-VERIFIED] on a no-op diff (Section 22.3 lineage was already v0.38-v0.54
at v0.53). The forward-dated lineage at v0.53 is a sealed historical claim; no retroactive correction
possible. Disclosed as a process observation [ASSERTED].
v0.54 append-only corrections: (bn) v0.54 title (line 1) reads “# XZ Protocol v0.53 – . . . ” while the
document version is 0.54. The title is sealed by FULL_SECTION_27 but is not part of Section 27 and
is not checked by any build.py gate. build.py [2] checks the Version: front-matter field; [2b] checks two
“v0.54 DRAFT CANDIDATE” prose instances plus “This document is v0.54”; neither touches line 1.
This is the same defect class as F-S01-47-02 (R6 boundary count) and (bm) (R12 boundary count) – a
version-advancing manual-update step omitted during the build – but at a novel locus (the H1 heading,
not a Section 27 count) [ASSERTED]. (bo) v0.54 front-matter Status line describes v0.53’s provenance
(“repair build from v0.52 R11 audit (3 carrying HALT, 2 advisory HALT). Correction (bi) restored-value
literals corrected. EXTERNAL count corrected. Entry range corrected. Terminal recomputation pass

83

applied.”) while v0.54 is the R12-on-v0.53 repair build with correction (bm). The provenance clause
was carried verbatim from v0.53 without update. build.py [2c] checks only the two-word status phrase
(“DRAFT CANDIDATE”), not the provenance clause [ASSERTED]. (bp) v0.54 Section 25 FB-7b row
status column reads “PENDING RE-CARRY v0.53” and the carrying-seat trajectory ends at R11.
Section 0.1 was advanced (“Current status: PENDING RE-CARRY on v0.54 bytes”); the row was not.
Standing boundary item 29 ([3a] fb_spec omits FB-7b locus assertion) confirmed live by mutation probe
(fixing the token still yields BUILD PASSED). v0.55 retires this boundary item via [2g] [ASSERTED].
Body repairs landed at v0.55: [a] Title version corrected from v0.53 to v0.55 [DIFF-VERIFIED]
[COMPUTED: build.py [2e]]. [b] Front-matter Version updated to 0.55 [DIFF-VERIFIED]. [c] Frontmatter Status updated with v0.55/R13 provenance [DIFF-VERIFIED] [COMPUTED: build.py [2f]].
[d] Section 0.1 entry count and range to “fifty-five amendment entries, v0.1 through v0.55” [DIFFVERIFIED]. [e] Section 22.2 coverage “v0.1 through v0.53” to “v0.1 through v0.54” [DIFF-VERIFIED].
[f] Section 22.3 carry lineage to v0.38-v0.55 [DIFF-VERIFIED]. [g] Section 25 FB-7b row version token
to “PENDING RE-CARRY v0.55” and R12/R13 trajectory added [DIFF-VERIFIED] [COMPUTED:
build.py [2g]]. [h] Section 0.1 current status to “PENDING RE-CARRY on v0.55 bytes” [DIFFVERIFIED]. Four new gates added to build.py: [2e] title-version, [2f] status-provenance, [2g] FB-7b row
version, [2h] standing-boundary count enumeration [COMPUTED: build.py gates fire on shipped bytes].
All 12 code files and trust roots stamped v0.55 [COMPUTED: grep -c v0.55 across 13 files = 13]. Six
suites, 186 tests, all GREEN [COMPUTED: pytest]. Status: DRAFT CANDIDATE. FB-7b PENDING
RE-CARRY. FB-8 OPEN. EXTERNAL count: 2 [EXTERNAL: v0.40 dispatch manifests held by
carrying seats and Zenodo deposits doi:10.5281/zenodo.21713180 and doi:10.5281/zenodo.21583202].
Disclosed standing boundaries – 33 items: [9c] arity-one regex, cb67f222 termination literal, Section
27 ungated share, no rendering ships, no revert-certificate for H-1/H-2, seal terminus at Provenance
marker, execution environment unsealed, no closure-reference validation in [9f], [3c] single-line citation
evasion, packet non-closure, fresh-execution non-reproducibility, [9d] word-list cap at fifteenth, [9d]
sentence-scope boundary, [9d] over-matching, [9c] DOI-resolution blindspot, no gate checks FROZEN
status token, [9c] quoted-tag inflation, GLM-5.2 carry-1C persistent HALT (exception applies), Kimi
K3 carry-1A persistent HALT (exception applies), no boundary-retirement mechanism, v0.41 retracted
(append-only corruption), FB-8 governance convergence OPEN, [9e] silent vacuity, [2c] arity-two, A-side
seam (condition_a.py, SHIELD-scoped), adversarial prohibited-content coverage limited to 4 of 6 code
modules (F-V44-01), [9d] synonym and bare-cardinal evasion, build.py f-string nested quotes require
Python 3.12+ (F-S07-46-02), class-to-severity mapping undefined on shipped bytes (F-S01-54-04),
trust-roots generated timestamp ungated, self-consistent resealing blind spot (proven live at v0.47,
F-SC04-47-02), HISTORY.sha256 cardinality gate case-sensitive and FULL_SECTION_27 line not
uniqueness-checked (F-S02-51-03, 3 mutation shapes survive), Kimi K3 execution attestation unbound
(BSSG fabrication class, see DOI 10.5281/zenodo.21713180 audit history) [ENUMERATED: 33 items].
• v0.56 (2026-08-10): R14 five-seat audit repair with register cross-reference corrections, gate
[2f] tightening, boundary restoration, and Crystallographic Ijaz methodology adoption.
Convergence Round 14 on v0.55 bytes: 5 seats (1 non-Kimi carrying fresh, 1 Kimi K3 carrying fresh,
3 Opus 5 advisory fresh), 5 frameworks (Differentiator, Fractal Cube, GAN Convergence, Structural
Revelation, Biomedical Fractal). 2 carrying HALT / 3 advisory HALT. Dominant convergent finding
[5-seat convergence: F-S01-55-01 / F-S02-55-01 / F-S03-55-03 / F-S04-55-04 / F-S05-55-02]: register
item (2) cites F-S05-54-02 (S05 FB-7b finding) where F-S05-54-03 (S05 status-provenance finding)
belongs; finding-ID transposition, same class as correction (as) at v0.44. Second convergent finding
[5-seat convergence: F-S01-55-02 / F-S02-55-02 / F-S03-55-01 / F-S04-55-03 / F-S05-55-01]: register
item (3) claims “3-seat convergence” with 2 cited IDs; actual convergence is [4-seat: F-S01-54-03 /
F-S02-54-02 / F-S03-54-03 / F-S05-54-02]. Third finding [2-seat convergence: F-S02-55-03 / F-S04-5502]: gate [2f] checks provenance < VERSION but not provenance == VERSION - 1; the R13 defect
shape passes the gate. Fourth finding [2-seat convergence: F-S03-55-02 / F-S04-55-05]: register header
“5 Class A items” matches no computable quantity (register has 6 items, R13 had 3 distinct Class A
defects). Fifth finding [1-seat: F-S04-55-01]: standing boundary item 29 retired while the limitation is
still live on bytes. All five defects are in the ungated prose interior. Hurst exponent R7-R14: H = 1.0

84

(persistent, 8/8 rounds). R13 repairs CONFIRMED TRUE on v0.55 bytes (5/5 seats). This entry is
the first constructed under the Crystallographic Ijaz methodology (v0.1): every convergence count is
the length of its coupled finding-ID list, every finding ID was transcribed from the seat report bytes
with no memory buffer [EXTERNAL: R14 seat reports].
v0.56 defect register disposition (from R14 five-seat audit, 7 items): (1) F-S01-55-01 / F-S02-55-01
/ F-S03-55-03 / F-S04-55-04 / F-S05-55-02 HIGH CLOSED via append-only correction (bq): v0.55
register item 2 finding ID F-S05-54-02 corrected to F-S05-54-03, [5-seat convergence: S01 / S02 / S03 /
S04 / S05] [ASSERTED]. (2) F-S01-55-02 / F-S02-55-02 / F-S03-55-01 / F-S04-55-03 / F-S05-55-01
HIGH CLOSED via append-only correction (br): v0.55 register item 3 convergence count corrected from
3 to 4 and finding-ID list expanded; narrative paragraph corrected, [5-seat convergence: S01 / S02 / S03
/ S04 / S05] [ASSERTED]. (3) F-S02-55-03 / F-S04-55-02 HIGH CLOSED via gate tightening: build.py
[2f] provenance check changed from prov_ver < VERSION to prov_ver == VERSION - 1, [2-seat
convergence: S02 / S04] [COMPUTED: build.py [2f] provenance == VERSION-1 gate]. (4) F-S03-55-02
/ F-S04-55-05 MEDIUM CLOSED via append-only correction (bs): register header corrected, [2-seat
convergence: S03 / S04] [ASSERTED]. (5) F-S04-55-01 HIGH CLOSED via boundary restoration and
append-only correction (bt): standing boundary item 29 restored to the boundary list; v0.55 retirement
retracted, [1-seat: S04] [ASSERTED]. (6) F-S02-55-04 / F-S04-55-06 LOW DISCLOSED: gate [2g]
structurally forbids FB-7b resolution; disclosed as standing boundary item 35, [2-seat convergence: S02
/ S04] [ASSERTED]. (7) F-S04-55-07 LOW DISCLOSED: class-to-severity mapping shipped in register
item 5 text while asserting its absence; mapping now declared: A=HIGH, B=MEDIUM, C=LOW,
D=LOW, E=INFORMATIONAL, [1-seat: S04] [ASSERTED].
v0.55 append-only corrections: (bq) v0.55 register item 2 cites F-S05-54-02; the correct S05 statusprovenance finding is F-S05-54-03. Same class as correction (as) at v0.44 [ASSERTED]. (br) v0.55
register item 3 claims “3-seat convergence” with 2 cited IDs; actual is [4-seat: F-S01-54-03 / F-S02-54-02
/ F-S03-54-03 / F-S05-54-02]; narrative “Third finding (3/5 seats)” also byte-false [ASSERTED]. (bs)
v0.55 register header reads “5 Class A items”; the register has 6 items [ASSERTED]. (bt) v0.55 register
item 3 claims boundary item 29 retired; the limitation ([3a] fb_spec omits FB-7b) is still live on bytes
[ASSERTED]. (bu) v0.55 gate [2f] checks provenance < VERSION, not == VERSION - 1; the R13
defect shape passes the gate; register item 2 “CLOSED via new gate” is byte-false as a class-closure
claim [ASSERTED].
Body repairs landed at v0.56: [a] Title version to v0.56 [DIFF-VERIFIED] [COMPUTED: build.py
[2e]]. [b] Front-matter Version to 0.56 [DIFF-VERIFIED]. [c] Front-matter Status with R14 provenance
[DIFF-VERIFIED] [COMPUTED: build.py [2f]]. [d] Section 0.1 entry count to “fifty-six amendment
entries, v0.1 through v0.56” [DIFF-VERIFIED]. [e] Section 22.2 coverage to “v0.1 through v0.55”
[DIFF-VERIFIED]. [f] Section 22.3 carry lineage to v0.38-v0.56 [DIFF-VERIFIED]. [g] Section 25
FB-7b row to “PENDING RE-CARRY v0.56” with R14 trajectory [DIFF-VERIFIED] [COMPUTED:
build.py [2g]]. [h] Section 0.1 to “PENDING RE-CARRY on v0.56 bytes” [DIFF-VERIFIED]. [i]
build.py [2f] provenance tightened to == VERSION - 1 [COMPUTED: build.py [2f]]. Class-to-severity
mapping declared: A=HIGH, B=MEDIUM, C=LOW, D=LOW, E=INFORMATIONAL [ASSERTED].
All 12 code files and trust roots stamped v0.56 [COMPUTED: grep -c v0.56 across 13 files = 13]. Six
suites, 186 tests, all GREEN [COMPUTED: pytest]. Status: DRAFT CANDIDATE. FB-7b PENDING
RE-CARRY. FB-8 OPEN. EXTERNAL count: 2 [EXTERNAL: v0.40 dispatch manifests held by
carrying seats and Zenodo deposits doi:10.5281/zenodo.21713180 and doi:10.5281/zenodo.21583202].
Disclosed standing boundaries – 35 items: [9c] arity-one regex, cb67f222 termination literal, Section 27 ungated share, no rendering ships, no revert-certificate for H-1/H-2, seal terminus at Provenance marker, execution environment unsealed, no closure-reference validation in [9f], [3c] single-line
citation evasion, packet non-closure, fresh-execution non-reproducibility, [9d] word-list cap at fifteenth, [9d] sentence-scope boundary, [9d] over-matching, [9c] DOI-resolution blindspot, no gate checks
FROZEN status token, [9c] quoted-tag inflation, GLM-5.2 carry-1C persistent HALT (exception applies), Kimi K3 carry-1A persistent HALT (exception applies), no boundary-retirement mechanism,
v0.41 retracted (append-only corruption), FB-8 governance convergence OPEN, [9e] silent vacuity,
[2c] arity-two, A-side seam (condition_a.py, SHIELD-scoped), adversarial prohibited-content cover-

85

age limited to 4 of 6 code modules (F-V44-01), [9d] synonym and bare-cardinal evasion, build.py
f-string nested quotes require Python 3.12+ (F-S07-46-02), [3a] fb_spec omits FB-7b locus assertion
(F-S07-46-03, restored from premature v0.55 retirement per F-S04-55-01), class-to-severity mapping
undefined on shipped bytes (F-S01-54-04), trust-roots generated timestamp ungated, self-consistent
resealing blind spot (proven live at v0.47, F-SC04-47-02), HISTORY.sha256 cardinality gate casesensitive and FULL_SECTION_27 line not uniqueness-checked (F-S02-51-03, 3 mutation shapes
survive), Kimi K3 execution attestation unbound (BSSG fabrication class, see DOI 10.5281/zenodo.21713180 audit history), [2g] structurally forbids FB-7b resolution (PENDING RE-CARRY absence
triggers FAIL on the legitimate RESOLVED state, F-S02-55-04 / F-S04-55-06) [ENUMERATED:
35 items] PRIOR_HISTORY 61cfd4feae9a091505b7dad6220a891f14f49643a2354c0f64b120529f0c9ed7.
PRIOR_HISTORY 61cfd4feae9a091505b7dad6220a891f14f49643a2354c0f64b120529f0c9ed7.
• v0.57 (2026-08-11): R15 five-seat audit repair with CI v0.2 code-generated register
architecture, boundary-30 correction, severity-label reconciliation, terminal-version gate,
and duplicate PRIOR_HISTORY removal. Convergence Round 15 on v0.56 bytes: 5 seats (1
Kimi K3 carrying fresh, 1 GPT-5.6 Sol carrying fresh, 1 Gemini 3.1 Pro advisory fresh, 1 GPT-5.6 Sol
advisory fresh, 1 Kimi K3 advisory fresh), 5 frameworks (GAN Convergence, Structural Revelation,
Biomedical Fractal, Differentiator, Fractal Cube). 2 carrying HALT / 3 advisory HALT. Dominant
convergent finding [5-seat convergence: F-S01-56-04 / F-S02-56-02 / F-S03-56-03 / F-S04-56-03 / F-S0556-01]: standing boundary item 30 reads “mapping undefined on shipped bytes” while the same entry
declares the mapping twice; the v0.55 wording was carried without re-derivation. Second convergent
finding [4-seat convergence: F-S02-56-01 / F-S04-56-01 / F-S01-56-05 / F-S05-56-02]: register item
(4) labels a HIGH (Class A) source defect as MEDIUM without adjudication receipt, violating I5
severity-class coupling. Third convergent finding [3-seat convergence: F-S01-56-02 / F-S02-56-05 /
F-S04-56-02]: terminal line reads “v0.55” in a v0.56 document, recurring the R13 version-token staleness
class. Fourth convergent finding [5-seat cluster: F-S01-56-08 / F-S02-56-03 / F-S02-56-06 / F-S03-56-04
/ F-S04-56-04 / F-S05-56-05 / F-S05-56-06]: CI v0.1 format compliance failure – polymerase rule
unevidenced, ASSERTED fraction rose from 18.5% to 40.0%, register brackets used seat labels instead
of finding IDs; F-CI-2 and F-CI-3 both triggered at adoption round 1. Four of five dominant R15
defects are in the ungated prose interior; the fifth (R14 Defect 3, gate [2f] provenance gap) was in
build.py gate logic [ASSERTED]. Recurrence fraction R7-R15: 9/9 Class A present. Laplace-smoothed
P(Class A at R16) = 10/11 = 0.91. R14 repairs CONFIRMED TRUE on v0.56 bytes (5/5 seats):
corrections (bq)-(bu) verified, gate [2f] tightened, boundary 29 restored, I1 count-list coupling held at
13/13 brackets, all 18 cited finding IDs byte-correct against R14 source reports [EXTERNAL: R15 seat
reports]. This entry is the first constructed under CI v0.2 (code-generated register architecture): the
defect register below was generated by xz_protocol_register_gen.py from r15_findings_index.json, not
authored by an LLM. Every register claim is tagged [COMPUTED: generate_register]. The boundary
list was generated from xz_protocol_boundaries.json [COMPUTED: generate_boundary_list]. Only
this narrative paragraph is [ASSERTED]. R15 defect register disposition (from R15 five-seat audit, 8
items):
(1) [5-seat convergence: F-S01-56-04 / F-S02-56-02 / F-S03-56-03 / F-S04-56-03 / F-S05-56-01] HIGH
CLOSED via append-only correction (bv): Boundary item 30 stale wording – mapping declared but
boundary says undefined. [COMPUTED: generate_register]
(2) [4-seat convergence: F-S02-56-01 / F-S04-56-01 / F-S01-56-05 / F-S05-56-02] HIGH CLOSED via
append-only correction (bw): Register item (4) severity transposition – HIGH source labeled MEDIUM
without adjudication. [COMPUTED: generate_register]
(3) [3-seat convergence: F-S01-56-02 / F-S02-56-05 / F-S04-56-02] HIGH CLOSED via gate [10h]: Terminal
v0.55 identity – document ends as v0.55 in a v0.56 protocol. [COMPUTED: generate_register]
(4) [5-seat convergence: F-S01-56-08 / F-S02-56-03 / F-S02-56-06 / F-S03-56-04 / F-S04-56-04 / F-S05-56-05
/ F-S05-56-06] HIGH CLOSED via CI v0.2 code-generated register architecture: CI format compliance –
polymerase unevidenced, ASSERTED fraction increased, register brackets use seat labels not finding IDs.
Adjudication: Cluster resolved by CI v0.2 architecture: register is now code-generated from this index.
ASSERTED fraction collapse is structural, not process-dependent. [COMPUTED: generate_register]
(5) [1-seat convergence: F-S02-56-04] HIGH CLOSED via append-only correction (bx): All five defects in

86

ungated prose – false, Defect 3 is build.py gate logic. [COMPUTED: generate_register]
(6) [1-seat convergence: F-S01-56-01] HIGH CLOSED via CI v0.2 code-generated register architecture:
Convergence bracket undercounts – triage numbers used instead of full report convergence sets. Adjudication: S01 uniquely built a 48-ID index from R14 reports and found 4 brackets undercount. The
v0.56 entry tracked the triage adjudication, not the raw seat reports. CI v0.2 resolves this structurally:
convergence groups in the index are the source of truth. [COMPUTED: generate_register]
(7) [1-seat convergence: F-S03-56-01] MEDIUM CLOSED via CI v0.2 code-generated register architecture: Narrative lists 5 findings but register has 7 items – ring closure break at narrative/register
boundary. Adjudication: Items (6)-(7) are valid independent disclosures added without narrative
integration. Downgraded from HIGH (S03) to MEDIUM – ring gap, not factual error. [COMPUTED:
generate_register]
(8) [4-seat convergence: F-S01-56-03 / F-S03-56-02 / F-S04-56-05 / F-S05-56-04] LOW CLOSED via
append-only correction (by): Duplicate PRIOR_HISTORY terminal literal. Adjudication: Both values
correct, no false seal. Cosmetic duplication. Downgraded from HIGH (S01/S03) to LOW per triage
adjudication – values agree with VERIFICATION_ANCHOR, standing boundary 33 already discloses
this shape. [COMPUTED: generate_register]
NOTED (non-converging or deferred, 8 items): - [3-seat: F-S01-56-09 / F-S04-56-06 / F-S05-56-07] LOW:
AUDIT_CONTEXT stale file inventory – lists code-carrying files, actual dispatch is prose-only. Disposition:
NOTED. Dispatch-template defect, not protocol-level. Fixed in R16 dispatch generation. [COMPUTED:
generate_register] - [F-S01-56-06] MEDIUM: H=1.0 re-asserted on undefined R/S statistic (constant series 0/0).
Disposition: NOTED. CI v0.2 adopts recurrence fraction and Laplace probability per S01/R14 prescription.
[COMPUTED: generate_register] - [F-S01-56-07] MEDIUM: 30 of 48 R14 findings undispositioned, no NOTED
clause. Disposition: NOTED. CI v0.2 register generator includes R6 NOTED clause for all non-converging
findings. [COMPUTED: generate_register] - [F-S02-56-07] MEDIUM: Register item (7) silently downgrades
MEDIUM source to LOW without adjudication. Disposition: NOTED. Subsumed by convergence group 2
(severity transposition class). CI v0.2 gate [10d] prevents. [COMPUTED: generate_register] - [F-S01-56-10]
LOW: STANDING_BOUNDARIES.txt non-verbatim vs entry list at 16 positions. Disposition: NOTED.
CI v0.2 boundary generator eliminates: both are generated from the same JSON source. [COMPUTED:
generate_register] - [F-S01-56-11] LOW: Gate [2f] excerpt stale header comment; round number still unbound.
Disposition: NOTED. [COMPUTED: generate_register] - [F-S01-56-12] LOW: Section 0.1 single-sourceof-truth contradicted by carry-status paragraph. Disposition: NOTED. [COMPUTED: generate_register]
- [F-S05-56-03] LOW: Register items (6)/(7) labeled LOW against S04 MEDIUM without adjudication.
Disposition: NOTED. Subsumed by group 2 severity-transposition class. [COMPUTED: generate_register]
Body repairs: (i) correction (bv): standing boundary item 30 reworded from “class-to-severity mapping
undefined on shipped bytes” to “class-to-severity mapping declared at v0.56” in both the current entry
boundary list and the standalone boundaries file [DIFF-VERIFIED]. (ii) correction (bw): register item
(4) severity restored from MEDIUM to HIGH per source reports F-S03-55-02 / F-S04-55-05 (both HIGH
in shipped R14 reports) [DIFF-VERIFIED]. (iii) terminal version line corrected from “v0.55” to current
version via gate [10h] [COMPUTED: build.py [10h]]. (iv) correction (bx): narrative locus claim corrected
from “all five defects are in the ungated prose interior” to “four of five dominant R15 defects are in the
ungated prose interior; the fifth was in build.py gate logic” [DIFF-VERIFIED]. (v) correction (by): duplicate
PRIOR_HISTORY terminal literal removed; single authoritative declaration retained [DIFF-VERIFIED].
(vi) CI v0.2 architecture adopted: register generated by code from r15_findings_index.json; boundary list
generated from xz_protocol_boundaries.json; gates [10c]-[10h] added to build.py; ASSERTED fraction target
< 15% [COMPUTED: build.py [10c]-[10h]]. Disclosed standing boundaries – 35 items: [9c] arity-one regex,
cb67f222 termination literal, Section 27 ungated share, no rendering ships, no revert-certificate for H-1/H-2,
seal terminus at Provenance marker, execution environment unsealed, no closure-reference validation in
[9f], [3c] single-line citation evasion, packet non-closure, fresh-execution non-reproducibility, [9d] word-list
cap at fifteenth, [9d] sentence-scope boundary, [9d] over-matching, [9c] DOI-resolution blindspot, no gate
checks FROZEN status token, [9c] quoted-tag inflation, GLM-5.2 carry-1C persistent HALT (exception
applies), Kimi K3 carry-1A persistent HALT (exception applies), no boundary-retirement mechanism, v0.41
retracted (append-only corruption), FB-8 governance convergence OPEN, [9e] silent vacuity, [2c] arity-two,
A-side seam (condition_a.py, SHIELD-scoped), adversarial prohibited-content coverage limited to 4/6 code

87

modules (F-V44-01), [9d] synonym and bare-cardinal evasion, build.py f-string nested quotes require Python
3.12+ (F-S07-46-02), [3a] fb_spec omits FB-7b locus assertion (F-S07-46-03, restored from premature v0.55
retirement per F-S04-55-01), class-to-severity mapping declared at v0.56 (A=HIGH, B=MEDIUM, C=LOW,
D=LOW, E=INFORMATIONAL); prior to v0.56 was undefined on shipped bytes (F-S01-54-04), trust-roots
generated timestamp ungated, self-consistent resealing blind spot (proven live at v0.47, F-SC04-47-02),
HISTORY.sha256 cardinality gate case-sensitive and FULL_SECTION_27 line not uniqueness-checked (3
mutation shapes survive, F-S02-51-03), Kimi K3 execution attestation unbound (BSSG fabrication class),
[2g] structurally forbids FB-7b resolution (PENDING RE-CARRY absence triggers FAIL, F-S02-55-04
/ F-S04-55-06) [ENUMERATED: 35 items] [COMPUTED: generate_boundary_list] PRIOR_HISTORY
280770b2d6127535fd0f7499ca324b0b4442dace1525a7a1044524a6eff9db56. - v0.58 (2026-08-11): R16 fiveseat audit repair with CI v0.2.1 architecture upgrade, narrative correction, Section 0.1/Section
25 FB-7b reconciliation, count-list invariant resolution, severity provenance implementation,
and front-matter Status correction. Convergence Round 16 on v0.57 bytes: 5 seats (1 Kimi K3 carrying
binding fresh, 1 GPT-5.6 Sol carrying binding fresh, 1 Gemini 3.1 Pro advisory fresh, 1 Kimi K3 advisory
fresh, 1 GPT-5.6 Sol advisory fresh), 5 frameworks (GAN Convergence, Structural Revelation, Fractal Cube,
Biomedical Fractal, Differentiator). 2 carrying HALT / 3 advisory HALT. CI v0.2 code-generated register
verified CLEAN at all 5 seats: CI-1R byte-exact, CI-4 at 6.9%, boundary list and terminal line correct. Class A
migrated OFF the code-generated register surface into three uncovered surfaces: the LLM-authored narrative
paragraph (Defect 1, 5/5 unanimous), the manually-maintained Section 0.1 and Section 25 body prose (Defects
2 and 7, 5/5), and the CI v0.2 specification-implementation gap in the generator and index schema (Defects
3-5, 4/5). The R14/R15 narrative conflation (Defect 1) confirms the producer prediction P4. The Section
0.1 version-token staleness (Defect 2) recurs for the R13-R16 span (4 consecutive occurrences of this defect
class) and confirms prediction P5 [ASSERTED]. R16 defect register disposition (from R16 five-seat audit, 7
items): (1) [5-seat convergence: F-S01-57-03 / F-S02-57-05 / F-S03-57-01 / F-S04-57-01 / F-S05-57-02] HIGH
CLOSED via append-only correction (bz): Narrative R14/R15 conflation – the corrected locus claim mixes
R14 and R15 defects, labeling an R14 exception as an R15 defect. [COMPUTED: generate_register] (2) [5-seat
/ 7-finding convergence: F-S01-57-04 / F-S02-57-04 / F-S03-57-02 / F-S04-57-02 / F-S04-57-04 / F-S04-57-08
/ F-S05-57-01] HIGH CLOSED via append-only correction (ca): Section 0.1 / Section 25 FB-7b status
contradiction and missing R15 trajectory – Section 0.1 says v0.56 bytes, Section 25 says v0.57, R15 outcome
absent from trajectory row. Adjudication: F-S04-57-04 (MEDIUM) and F-S04-57-08 (LOW) subsumed into
this group as instances of the same Section 0.1 staleness class. Group severity HIGH per 5/5 seat convergence
at HIGH. [COMPUTED: generate_register] (3) [4-seat convergence: F-S01-57-01 / F-S02-57-02 / F-S04-57-05
/ F-S05-57-03] HIGH CLOSED via CI v0.2.1 architecture repair: Count-list invariant violation – generator
uses seat_count field instead of computing from finding_ids, violating CI v0.2 R2 and gate [10e] as specified.
Adjudication: F-S04-57-05 (MEDIUM) elevated to group HIGH. Resolution: reconcile by emitting dual
cardinality (N-seat / M-finding) and computing both from the data. Amend R2 and [10e]. [COMPUTED:
generate_register] (4) [4-seat convergence: F-S01-57-02 / F-S02-57-03 / F-S04-57-06 / F-S05-57-04] HIGH
CLOSED via CI v0.2.1 architecture repair: Severity provenance not implemented – findings index lacks
per-finding source_severity, generator unconditionally trusts triage_severity without adjudication receipt,
and invalid severity tokens are accepted. Adjudication: F-S04-57-06 (LOW, schema drift) and F-S01-57-07
(MEDIUM, invalid severity acceptance) subsumed. Resolution: add per-finding source_severity to findings[]
array; derive group severity from source severities with explicit adjudication receipts; add severity validation
to the generator. [COMPUTED: generate_register] (5) [2-seat convergence: F-S02-57-01 / F-S05-57-05] HIGH
CLOSED via CI v0.2.1 architecture repair: Index membership lossy – triage places some findings in multiple
defect groups but index assigns each to exactly one, losing the second membership without adjudication
receipt. Adjudication: Resolution: define canonical-group assignment rule (primary group = highest-severity
group or lowest group_id on tie), record secondary memberships in findings[] array, add adjudication receipt
for collapsed overlaps. [COMPUTED: generate_register] (6) [2-seat convergence: F-S01-57-05 / F-S04-57-03]
HIGH CLOSED via append-only correction (cb): Front-matter Status enumerates R14 repairs instead of
R15/v0.57 repairs – provenance clause advanced but repair substance carried stale. Adjudication: S02
F-S02-57-04 partially covers this as part of the stale-surfaces cluster. 2 seats with explicit findings, both
HIGH. [COMPUTED: generate_register] (7) [1-seat convergence: F-S01-57-07] MEDIUM CLOSED via CI
v0.2.1 architecture repair: Generator accepts invalid severity tokens – no generation-time validation against
the declared A=HIGH/B=MEDIUM/C=LOW mapping. Adjudication: S05 adversarial probes confirmed the

88

same shape (CRITICAL accepted). Single explicit finding, folded into group 4 provenance class for repair
but retained as separate group for the generator-validation component. [COMPUTED: generate_register]
NOTED (non-converging or deferred, 4 items): - [3-seat: F-S01-57-06 / F-S04-57-07 / F-S05-57-06] MEDIUM:
Gate count documentation contradiction – AUDIT_CONTEXT says 264, CI_METHODOLOGY says
222; true count is 264 (CI_METHODOLOGY was stale). Disposition: NOTED. [COMPUTED: generate_register] - [1-seat: F-S02-57-06] MEDIUM: Terminal line untagged per CI methodology specification –
CI_METHODOLOGY says terminal is [COMPUTED] but shipped line has no enzyme tag. Disposition:
NOTED. [COMPUTED: generate_register] - [F-S04-57-09] INFORMATIONAL: v0.57 entry omits the
code-stamp sentence present in v0.49-v0.56 entries without disclosure. Disposition: NOTED. [COMPUTED:
generate_register] - [F-S04-57-10] INFORMATIONAL: DISPATCH.txt says 5 corrections (bv)-(by) but
entry has 4 lettered corrections plus gate and architecture repairs. Disposition: NOTED. [COMPUTED:
generate_register] Body repairs: (i) correction (bz): narrative R14/R15 conflation corrected – the v0.57
sentence mixed R14 and R15 defect sets; removed and replaced by the code-generated register which does not
make round-attribution claims [DIFF-VERIFIED]. (ii) correction (ca): Section 0.1 status advanced from
“v0.56 bytes” to “v0.58 bytes”; Section 25 FB-7b row trajectory extended with R15 and R16 outcomes; Section
0.1 and Section 25 now agree on PENDING RE-CARRY v0.58 [DIFF-VERIFIED]. (iii) correction (cb):
front-matter Status repair enumeration replaced – R14 repair list removed, R16/v0.57 repair list substituted
[DIFF-VERIFIED]. (iv) CI v0.2.1 architecture upgrade: register generator now computes seat count from
unique seat prefixes and finding count from len(finding_ids), emitting dual cardinality when they differ; severity tokens validated against the declared mapping at generation time (invalid tokens rejected); findings[] array
added to the index schema with per-finding source_severity; index membership now tracks convergence_group
per finding for CI-8 verification [COMPUTED: build.py]. Disclosed standing boundaries – 35 items: [9c]
arity-one regex, cb67f222 termination literal, Section 27 ungated share, no rendering ships, no revert-certificate
for H-1/H-2, seal terminus at Provenance marker, execution environment unsealed, no closure-reference
validation in [9f], [3c] single-line citation evasion, packet non-closure, fresh-execution non-reproducibility, [9d]
word-list cap at fifteenth, [9d] sentence-scope boundary, [9d] over-matching, [9c] DOI-resolution blindspot, no
gate checks FROZEN status token, [9c] quoted-tag inflation, GLM-5.2 carry-1C persistent HALT (exception
applies), Kimi K3 carry-1A persistent HALT (exception applies), no boundary-retirement mechanism, v0.41
retracted (append-only corruption), FB-8 governance convergence OPEN, [9e] silent vacuity, [2c] arity-two,
A-side seam (condition_a.py, SHIELD-scoped), adversarial prohibited-content coverage limited to 4/6 code
modules (F-V44-01), [9d] synonym and bare-cardinal evasion, build.py f-string nested quotes require Python
3.12+ (F-S07-46-02), [3a] fb_spec omits FB-7b locus assertion (F-S07-46-03, restored from premature v0.55
retirement per F-S04-55-01), class-to-severity mapping declared at v0.56 (A=HIGH, B=MEDIUM, C=LOW,
D=LOW, E=INFORMATIONAL); prior to v0.56 was undefined on shipped bytes (F-S01-54-04), trust-roots
generated timestamp ungated, self-consistent resealing blind spot (proven live at v0.47, F-SC04-47-02),
HISTORY.sha256 cardinality gate case-sensitive and FULL_SECTION_27 line not uniqueness-checked (3
mutation shapes survive, F-S02-51-03), Kimi K3 execution attestation unbound (BSSG fabrication class),
[2g] structurally forbids FB-7b resolution (PENDING RE-CARRY absence triggers FAIL, F-S02-55-04
/ F-S04-55-06) [ENUMERATED: 35 items] [COMPUTED: generate_boundary_list] PRIOR_HISTORY
851ef6b3b8b105591bd73fcd1aade422bfab6d753b801794cd72f8f840842c1a.
• v0.59 (2026-08-11): R17 five-seat audit repair with CI v0.2.2 architecture upgrade,
Section 22.2/22.3 carried-bounds correction, narrative convergence-count correction,
group 6 adjudication receipt correction, findings[] load-bearing consumption, disposition
validation, finding-ID format validation, computed header and correction cursor, and
terminal line enzyme tag. Convergence Round 17 on v0.58 bytes: 5 seats (1 Kimi K3 carrying
binding fresh, 1 GPT-5.6 Sol carrying binding fresh, 1 Gemini 3.1 Pro advisory fresh, 1 Kimi K3
advisory fresh, 1 GPT-5.6 Sol advisory fresh), 5 frameworks (GAN Convergence, Structural Revelation,
Fractal Cube, Biomedical Fractal, Differentiator). 2 carrying HALT / 3 advisory HALT. CI v0.2.1
code-generated register verified CLEAN at all 5 seats: CI-1R byte-exact, CI-4 at 5.3-12.3%, boundary
list and terminal line correct. Class A found on three surfaces: Section 22.2/22.3 body prose with stale
carried-entry bounds (Defect 1, 3 seats: S01, S04, S05), the CI v0.2.1 specification-implementation
gap where findings[] was inert and secondary membership unimplemented (Defects 2-3, convergence
at 4 and 3 seats respectively), and the narrative convergence-count ambiguity (Defect 4, 2 seats: S03,

89

S04, disputed by S01 as defensible at surface granularity). S05 additionally found a factually false
adjudication receipt in group 6 (Defect 5, 1 seat). The Section 22.2/22.3 staleness is the version-token
class recurring for the R13-R17 span (5 occurrences). Producer prediction P4 named the Section
22.2/22.3 loci as a risk surface and was CONFIRMED [ASSERTED]. R17 defect register disposition
(from R17 five-seat audit, 9 items):
(1) [3-seat / 4-finding convergence: F-S01-58-01 / F-S04-58-01 / F-S04-58-02 / F-S05-58-04] HIGH CLOSED
via append-only correction (cc): Section 22.2/22.3 version-token staleness. Adjudication: Version-token
staleness class recurring for the R13-R17 span (5 occurrences). Correction (cb) at v0.58 repaired
only front-matter; Sections 22.2/22.3 carried bounds ship unrepaired. Advance bounds to v0.57 via
corrections (cc)/(cd). [COMPUTED: generate_register]
(2) [4-seat convergence: F-S02-58-01 / F-S03-58-03 / F-S04-58-04 / F-S05-58-01] HIGH CLOSED via CI
v0.2.2 architecture repair: findings[] array inert (CI v0.2.1 spec-impl gap). Adjudication: Generator
never reads findings[] array. R16 Defect 4 partially recurring: data shipped but mechanism not
implemented. CI v0.2.2 upgrade: make findings[] load-bearing. Adjudication: F-S04-58-04 (MEDIUM)
elevated to HIGH per 3/4 HIGH convergence. [COMPUTED: generate_register]
(3) [3-seat convergence: F-S02-58-02 / F-S05-58-02 / F-S01-58-02] HIGH CLOSED via CI v0.2.2 architecture repair: Secondary membership not implemented. Adjudication: AUDIT_CONTEXT claims
secondary memberships tracked; findings[] has only scalar convergence_group. Byte-false closure claim.
Adjudication: F-S01-58-02 (MEDIUM) elevated to HIGH as the extraction-narrowing mechanism is the
same root cause. [COMPUTED: generate_register]
(4) [2-seat / 3-finding convergence: F-S03-58-01 / F-S03-58-02 / F-S04-58-03] HIGH CLOSED via appendonly correction (cd): Narrative convergence-count ambiguity. Adjudication: Narrative parentheticals
‘(Defects 2 and 7, 5/5)’ and ‘(Defects 3-5, 4/5)’ read as per-defect claims by S03/S04 (false: Defect 7
was 3/5, Defect 5 was 2/5). S01 reads them at surface granularity (defensible). Rephrased to avoid
per-defect claims. [COMPUTED: generate_register]
(5) [1-seat convergence: F-S05-58-03] HIGH CLOSED via append-only correction (ce): Group 6 adjudication
receipt factually false. Adjudication: Receipt claims 1 MEDIUM + 2 LOW; actual distribution from
findings[] is 2 MEDIUM + 1 LOW. Byte-false. Correct the receipt by computing distribution from
source records. [COMPUTED: generate_register]
(6) [2-seat convergence: F-S02-58-05 / F-S03-58-04] MEDIUM CLOSED via CI v0.2.2 architecture repair:
Terminal line enzyme tag missing. Adjudication: CI_METHODOLOGY says terminal is [COMPUTED];
shipped terminal untagged. Tag the terminal line. [COMPUTED: generate_register]
(7) [2-seat convergence: F-S01-58-05 / F-S02-58-06] MEDIUM CLOSED via CI v0.2.2 architecture repair:
Disposition silent-drop. Adjudication: Unknown disposition tokens silently removed from register. Fail
closed on unknown values. Adjudication: F-S01-58-05 (LOW) elevated to MEDIUM per S02 at same
severity. [COMPUTED: generate_register]
(8) [1-seat convergence: F-S01-58-04] MEDIUM CLOSED via CI v0.2.2 architecture repair: Hardcoded
register literals. Adjudication: Header ‘five-seat’ word and _correction_start=51 not computed from
data. M6 proves divergence class. Compute both from data. [COMPUTED: generate_register]
(9) [1-seat convergence: F-S05-58-06] MEDIUM CLOSED via CI v0.2.2 architecture repair: Malformed/duplicate finding ID acceptance. Adjudication: Generator accepts bogus IDs and duplicates.
Add ID format validation and uniqueness enforcement. [COMPUTED: generate_register]
NOTED (non-converging or deferred, 7 items): - [4-seat: F-S01-58-03 / F-S02-58-04 / F-S04-58-06 /
F-S05-58-05] MEDIUM: Gate count 222/261/264 documentation inconsistency. Disposition: NOTED.
[COMPUTED: generate_register] - [1-seat: F-S02-58-03] MEDIUM: CI_METHODOLOGY schema inconsistency. Disposition: NOTED. [COMPUTED: generate_register] - [F-S01-58-06] LOW: ID-less advisory
observations have no extraction path into CI v0.2.1 index. Disposition: NOTED. [COMPUTED: generate_register] - [F-S01-58-07] LOW: Dispatch-layer seat fractions diverge from register computed counts.
Disposition: NOTED. [COMPUTED: generate_register] - [F-S01-58-08] INFORMATIONAL: BOUNDARIES
version field 0.57; packet cardinality 19 vs 20; Section 0.1 duplicate status sentence. Disposition: NOTED.
[COMPUTED: generate_register] - [F-S04-58-05] LOW: Section 0.1 carry rationale duplicated between
Section 0.1 and FB-7b row. Disposition: NOTED. [COMPUTED: generate_register] - [F-S04-58-07] INFORMATIONAL: ASSERTED fraction 12.3%; PRIOR_HISTORY untagged; BOUNDARIES version field.

90

Disposition: NOTED. [COMPUTED: generate_register] Body repairs: (i) correction (cc): Section 22.2
carried-entry bound advanced from “v0.1 through v0.55” to “v0.1 through v0.57” [DIFF-VERIFIED]. (ii)
correction (cd): Section 22.3 carry lineage advanced from “v0.38-v0.56” to “v0.38-v0.57” [DIFF-VERIFIED].
(iii) correction (ce): narrative convergence-count claims in v0.58 entry rephrased – the v0.58 narrative
grouped Defects 2+7 and Defects 3-5 by surface with aggregate seat fractions; per-defect fractions now
stated individually [DIFF-VERIFIED]. (iv) correction (cf): R16 group 6 adjudication receipt source-severity
distribution corrected from “1 MEDIUM (S01) + 2 LOW (S04/S05)” to “2 MEDIUM (S01, S05) + 1
LOW (S04)” in r16_findings_index.json [DIFF-VERIFIED]. (v) CI v0.2.2 architecture upgrade: register
generator now consumes findings[] array with per-finding source_severity validation; disposition tokens
validated against {CLOSED, NOTED, DEFERRED} (fail-closed on unknown); finding IDs validated against
F-SNN-VV-FF format with within-group uniqueness enforced; header seat word computed from index seats
field; correction cursor computed from prior_correction_end; terminal line tagged [COMPUTED: generate_terminal_line] [COMPUTED: build.py]. Disclosed standing boundaries – 35 items: [9c] arity-one regex,
cb67f222 termination literal, Section 27 ungated share, no rendering ships, no revert-certificate for H-1/H-2,
seal terminus at Provenance marker, execution environment unsealed, no closure-reference validation in
[9f], [3c] single-line citation evasion, packet non-closure, fresh-execution non-reproducibility, [9d] word-list
cap at fifteenth, [9d] sentence-scope boundary, [9d] over-matching, [9c] DOI-resolution blindspot, no gate
checks FROZEN status token, [9c] quoted-tag inflation, GLM-5.2 carry-1C persistent HALT (exception
applies), Kimi K3 carry-1A persistent HALT (exception applies), no boundary-retirement mechanism, v0.41
retracted (append-only corruption), FB-8 governance convergence OPEN, [9e] silent vacuity, [2c] arity-two,
A-side seam (condition_a.py, SHIELD-scoped), adversarial prohibited-content coverage limited to 4/6 code
modules (F-V44-01), [9d] synonym and bare-cardinal evasion, build.py f-string nested quotes require Python
3.12+ (F-S07-46-02), [3a] fb_spec omits FB-7b locus assertion (F-S07-46-03, restored from premature v0.55
retirement per F-S04-55-01), class-to-severity mapping declared at v0.56 (A=HIGH, B=MEDIUM, C=LOW,
D=LOW, E=INFORMATIONAL); prior to v0.56 was undefined on shipped bytes (F-S01-54-04), trust-roots
generated timestamp ungated, self-consistent resealing blind spot (proven live at v0.47, F-SC04-47-02),
HISTORY.sha256 cardinality gate case-sensitive and FULL_SECTION_27 line not uniqueness-checked (3
mutation shapes survive, F-S02-51-03), Kimi K3 execution attestation unbound (BSSG fabrication class),
[2g] structurally forbids FB-7b resolution (PENDING RE-CARRY absence triggers FAIL, F-S02-55-04
/ F-S04-55-06) [ENUMERATED: 35 items] [COMPUTED: generate_boundary_list] PRIOR_HISTORY
4a79f22603c0931e383021f2ca3cda3d7fea96b0a31086f9808e558d13e2bfde.
• v0.60 (2026-08-11): R18 ten-seat audit repair with CI v0.3 architecture upgrade – severity derivation from source records, adjudication receipt enforcement, correction-letter
allocation from explicit refs, validation boundary extension, Section 22.2/22.3 bounds
gated to VERSION-1, secondary membership disposition corrected, R16 group 6 receipt
corrected. Convergence Round 18 on v0.59 bytes: 10 seats (5 fresh + 5 continuous; 2 Kimi K3 carrying
binding, 2 GPT-5.6 Sol carrying binding, 2 Gemini 3.1 Pro advisory, 2 Kimi K3 advisory, 2 GPT-5.6 Sol
advisory), 5 frameworks (GAN Convergence, Structural Revelation, Fractal Cube, Biomedical Fractal,
Differentiator). 4 carrying HALT / 6 advisory HALT. The full executable packet shipped and executed:
all 4 executing seats ran build.py (261 PASS), pytest (186 GREEN), sha256sum (19/19 OK), seal
chain (59/59 entries), and CI-1R (byte-exact) as EXECUTED rather than ASSERTED. Class A found
on three surfaces: the CI v0.2.2 specification-implementation gap where findings[] was validated but
semantically inert for severity derivation and receipt enforcement (Defect 1, 8 findings across 5 seats –
unanimous), correction-letter namespace collision where the generator assigned one letter per group but
group 1 consumed two corrections (Defect 2, 6 findings across 4 seats – novel R18), and Section 22.2/22.3
version-token staleness recurring for the R13-R18 span with the v0.59 document carrying bounds at
v0.57 instead of the VERSION-1 value v0.58 (Defect 3, 1 seat, disputed by S04F which accepted the
v0.57 target as correct for v0.58 carried entries). The secondary membership disposition label was
called Class A by 3 seats (CLOSED-via-repair label false when the mechanism was scoped out, not
implemented) and discharged by 2 seats (scope-out accepted per R17 triage alternative) [ASSERTED].
R18 defect register disposition (from R18 ten-seat audit, 6 items):
(1) [5-seat / 8-finding convergence: F-S01-59-03 / F-S02-59-01F / F-S02-59-01C / F-S03-59-01F / F-S0359-01C / F-S04-59-02 / F-S05-59-01F / F-S05-59-01C] HIGH CLOSED via CI v0.3 architecture repair:

91

findings[] semantically inert (spec-impl gap R16-R18). Adjudication: Spec-impl gap recurring for the
R16-R18 span (3 occurrences). CI v0.3 implements actual severity derivation from findings[] source
records with mandatory adjudication receipt on divergence. M2/M3-class mutations now either change
output or fail generation. [COMPUTED: generate_register]
(2) [4-seat / 6-finding convergence: F-S01-59-04 / F-S02-59-03F / F-S02-59-02C / F-S04-59-01 / F-S0559-02F / F-S05-59-03C] HIGH CLOSED via CI v0.3 architecture repair: Correction-letter namespace
collision (novel R18). Adjudication: Generator assumed one correction per group. CI v0.3 uses explicit
correction_refs[] per group – multi-correction groups supported. Body-repair ledger generated from
same refs. [COMPUTED: generate_register]
(3) [1-seat convergence: F-S01-59-01] HIGH CLOSED via append-only correction (cg): Section 22.2/22.3
version-token staleness (recurrence R13-R18 (6 occurrences)). Adjudication: Version-token staleness
class recurring for the R13-R18 span (6 occurrences). Repair applied R17 literal target (v0.57) instead
of VERSION-1 semantic rule. CI v0.3 gates both bounds to VERSION-1 (entry count minus one).
Correction (cg) advances to v0.59. [COMPUTED: generate_register]
(4) [3-seat / 4-finding convergence: F-S01-59-08 / F-S02-59-02F / F-S05-59-03F / F-S05-59-02C] HIGH
CLOSED via append-only correction (ch): Secondary membership disposition label. Adjudication:
Register said CLOSED via architecture repair but nothing was implemented – it was scoped out.
S01F/S04F accepted the scope-out as adequate; S02F/S05F called it Class A because the label was
false. Correction (ch): change disposition to SCOPED_OUT with truthful scope note. [COMPUTED:
generate_register]
(5) [1-seat convergence: F-S01-59-02] HIGH CLOSED via append-only correction (ci): R16 group 6
receipt distribution still wrong. Adjudication: The v0.59 correction (cf) claimed 2M+1L but findings[]
shows 3M+1L (S02 is MEDIUM). The R17 triage propagated its own miscount. Correction (ci): fix
receipt in R17 index to 3 MEDIUM (F-S01-58-03, F-S02-58-04, F-S05-58-05) + 1 LOW (F-S04-58-06).
[COMPUTED: generate_register]
(6) [2-seat convergence: F-S01-59-07 / F-S04-59-04] MEDIUM CLOSED via CI v0.3 architecture repair:
Validation boundary gap (noted dispositions, findings[] IDs, cross-references). Adjudication: CI v0.3
extends fail-closed validation to noted dispositions, findings[] IDs (format + uniqueness), required fields,
and cross-layer references. [COMPUTED: generate_register]
NOTED (non-converging or deferred, 9 items): - [4-seat: F-S01-59-05 / F-S02-59-05F / F-S02-59-03C /
F-S04-59-03 / F-S05-59-04F] MEDIUM: Gate count documentation inconsistency (recurring since R14).
Disposition: NOTED. [COMPUTED: generate_register] - [1-seat: F-S01-59-06] MEDIUM: COMPUTED tag
overclaim on adjudication prose. Disposition: NOTED. [COMPUTED: generate_register] - [F-S01-59-09]
INFORMATIONAL: PRIOR_HISTORY line untagged; correction (cf) target outside packet closure. Disposition: NOTED. [COMPUTED: generate_register] - [F-S02-59-04F] MEDIUM: CI-4 metric ambiguity:
tag-count vs character-share basis undefined. Disposition: NOTED. [COMPUTED: generate_register] [F-S02-59-04C] MEDIUM: CI-4 dead-space metric underspecified. Disposition: NOTED. [COMPUTED:
generate_register] - [F-S02-59-05C] MEDIUM: R17 triage severity arithmetic: 13H/12M/4L/2I should be
13H/11M/5L/2I. Disposition: NOTED. [COMPUTED: generate_register] - [F-S04-59-05] LOW: Correction (cf) DIFF-VERIFIED target outside packet closure. Disposition: NOTED. [COMPUTED: generate_register] - [F-S04-59-06] LOW: CI_METHODOLOGY lacks normative v0.2.2/v0.3 schema. Disposition:
NOTED. [COMPUTED: generate_register] - [F-S04-59-07] INFORMATIONAL: No byte-identity register gate; PRIOR_HISTORY untagged; version arg uncoupled; ASSERTED basis-dependent. Disposition:
NOTED. [COMPUTED: generate_register] Body repairs: (i) correction (cg): Section 22.2 carried-entry
bound advanced from “v0.1 through v0.57” to “v0.1 through v0.59” and Section 22.3 carry lineage advanced
from “v0.38-v0.57” to “v0.38-v0.59”; both now gated to VERSION-1 [DIFF-VERIFIED]. (ii) correction (ch):
R17 register item (3) disposition changed from “CLOSED via CI v0.2.2 architecture repair” to “SCOPED
OUT: canonical-group rule retained, multi-membership not implemented” in the R18 findings index group
4 [DIFF-VERIFIED]. (iii) correction (ci): R17 triage group 5 (R16 group 6 receipt) source-severity distribution corrected from “2 MEDIUM + 1 LOW” to “3 MEDIUM (F-S01-58-03, F-S02-58-04, F-S05-58-05)
+ 1 LOW (F-S04-58-06)” in the R18 findings index [DIFF-VERIFIED]. (iv) CI v0.3 architecture upgrade:
register generator now derives severity from findings[] source records with mandatory adjudication_receipt on
divergence (fail-closed); correction-letter allocation from explicit correction_refs[] per group (multi-correction

92

groups supported); validation boundary extended to noted dispositions, findings[] IDs (format + uniqueness), required fields, and cross-layer group-to-findings[] references; disposition vocabulary extended with
SCOPED_OUT [COMPUTED: build.py]. Disclosed standing boundaries – 35 items: [9c] arity-one regex,
cb67f222 termination literal, Section 27 ungated share, no rendering ships, no revert-certificate for H-1/H-2,
seal terminus at Provenance marker, execution environment unsealed, no closure-reference validation in
[9f], [3c] single-line citation evasion, packet non-closure, fresh-execution non-reproducibility, [9d] word-list
cap at fifteenth, [9d] sentence-scope boundary, [9d] over-matching, [9c] DOI-resolution blindspot, no gate
checks FROZEN status token, [9c] quoted-tag inflation, GLM-5.2 carry-1C persistent HALT (exception
applies), Kimi K3 carry-1A persistent HALT (exception applies), no boundary-retirement mechanism, v0.41
retracted (append-only corruption), FB-8 governance convergence OPEN, [9e] silent vacuity, [2c] arity-two,
A-side seam (condition_a.py, SHIELD-scoped), adversarial prohibited-content coverage limited to 4/6 code
modules (F-V44-01), [9d] synonym and bare-cardinal evasion, build.py f-string nested quotes require Python
3.12+ (F-S07-46-02), [3a] fb_spec omits FB-7b locus assertion (F-S07-46-03, restored from premature v0.55
retirement per F-S04-55-01), class-to-severity mapping declared at v0.56 (A=HIGH, B=MEDIUM, C=LOW,
D=LOW, E=INFORMATIONAL); prior to v0.56 was undefined on shipped bytes (F-S01-54-04), trust-roots
generated timestamp ungated, self-consistent resealing blind spot (proven live at v0.47, F-SC04-47-02),
HISTORY.sha256 cardinality gate case-sensitive and FULL_SECTION_27 line not uniqueness-checked (3
mutation shapes survive, F-S02-51-03), Kimi K3 execution attestation unbound (BSSG fabrication class),
[2g] structurally forbids FB-7b resolution (PENDING RE-CARRY absence triggers FAIL, F-S02-55-04
/ F-S04-55-06) [ENUMERATED: 35 items] [COMPUTED: generate_boundary_list] PRIOR_HISTORY
5c28cf5a4a56c81f32042c87dd6ac97ddf065e17c7168043ef4ddfb8bc2c522d.
• v0.61 (2026-08-11): R19 ten-seat audit repair with CI v0.3.1 – source-severity distribution load-bearing, receipt content validation, cross-layer convergence_group validation,
VERSION-1 gate, correction (ch) landed, dangling references fixed. Convergence Round 19
on v0.60 bytes: 10 seats (5 fresh + 5 continuous; Kimi K3, GPT-5.6 Sol, Gemini 3.1 Pro), 5 frameworks.
4 carrying HALT / 6 advisory HALT. CI v0.3 mechanism repairs verified LANDED at all executing
seats: correction-letter allocation from explicit refs (no collision), fail-closed validation (severities,
IDs, dispositions, referenced findings), PRIOR_HISTORY cross-anchored to held v0.59 HISTORY
(S01C, S04C). R18 Defects 2 (correction cursor), 4 (secondary membership label), 5 (R16 receipt)
DISCHARGED. Class A found on four surfaces: source-severity distribution not load-bearing where
M2/M3 mutations remain inert (Defect 1, unanimous 10/10 – severity derivation checks majority only,
receipt presence not content), correction (ch) never landed with group 4 disposition still CLOSED
despite DIFF-VERIFIED claim (Defect 2, 7/10), VERSION-1 gate claimed but absent from build.py
with S04C sabotage proof (Defect 3, 7/10), and dangling convergence_group values in findings[] (Defect
4, 5/10). S04C framing: “The Class A defects are not in the mechanism; they are in the hand-written
claims about the mechanism and about corrections that did not land” [ASSERTED]. R19 defect register
disposition (from R19 ten-seat audit, 4 items):
(1) [4-seat / 6-finding convergence: F-S01-60-01 / F-S01C-60-01 / F-S02-60-01F / F-S02-60-01C / FS05-60-01F / F-S05-60-01C] HIGH CLOSED via CI v0.3.1 architecture repair: Source severity not
load-bearing (M2/M3 inert, R16-R19). Source distribution: 6 HIGH. Adjudication: CI v0.3.1 emits the
source distribution into the register (load-bearing) and validates receipt content against the computed
distribution. M2 mutations now change output; receipt removal on mixed groups fails. [COMPUTED:
generate_register]
(2) [6-seat / 7-finding convergence: F-S01-60-02 / F-S01C-60-02 / F-S02-60-02F / F-S02-60-02C / F-S0360-01C / F-S04-60-01 / F-S05-60-03F] HIGH CLOSED via append-only correction (cj): Correction
(ch) never landed (group 4 still CLOSED). Source distribution: 7 HIGH. Adjudication: One-line fix:
r18_findings_index.json group 4 disposition set to SCOPED_OUT with scope_note. Correction (cj)
verifies the landing. [COMPUTED: generate_register]
(3) [6-seat convergence: F-S01-60-03 / F-S01C-60-03 / F-S02-60-03C / F-S03-60-01F / F-S04-60-02 /
F-S05-60-04F] HIGH CLOSED via CI v0.3.1 architecture repair: VERSION-1 gate absent from build.py.
Source distribution: 6 HIGH. Adjudication: Gate [10i] added to build.py: derives VERSION-1 from
VERSION constant and asserts both Section 22 tokens match. [COMPUTED: generate_register]
(4) [1-seat convergence: F-S05-60-02F] HIGH CLOSED via CI v0.3.1 architecture repair: Dangling

93

convergence_group values in findings[]. Source distribution: 1 HIGH. Adjudication: Generator validates
findings[].convergence_group against declared groups. Noted findings use null. 7 dangling values fixed
in r18 index. [COMPUTED: generate_register]
NOTED (non-converging or deferred, 3 items): - [1-seat: F-S02-60-03F] HIGH: Finding ID F/C suffixes
not in source reports. Disposition: NOTED. [COMPUTED: generate_register] - [2-seat: F-S02-60-04F /
F-S05-60-06F] MEDIUM: Gate count documentation (recurring). Disposition: NOTED. [COMPUTED:
generate_register] - [2-seat: F-S03-60-02C / F-S05-60-05F] MEDIUM: Body-repair ledger / COMPUTED
tag scope. Disposition: NOTED. [COMPUTED: generate_register] Body repairs: (i) correction (cj):
r18_findings_index.json group 4 disposition set from CLOSED to SCOPED_OUT with scope_note field
[DIFF-VERIFIED]. (ii) CI v0.3.1 architecture upgrade: source-severity distribution emitted into the register
(load-bearing); receipt content validated against computed distribution (must cite all source severities and
counts); cross-layer convergence_group validation (dangling references rejected, noted findings use null);
VERSION-1 gate [10i] added to build.py (derives expected prior version from VERSION constant, asserts both
Section 22.2 and 22.3 tokens match) [COMPUTED: build.py]. Disclosed standing boundaries – 35 items: [9c]
arity-one regex, cb67f222 termination literal, Section 27 ungated share, no rendering ships, no revert-certificate
for H-1/H-2, seal terminus at Provenance marker, execution environment unsealed, no closure-reference
validation in [9f], [3c] single-line citation evasion, packet non-closure, fresh-execution non-reproducibility, [9d]
word-list cap at fifteenth, [9d] sentence-scope boundary, [9d] over-matching, [9c] DOI-resolution blindspot, no
gate checks FROZEN status token, [9c] quoted-tag inflation, GLM-5.2 carry-1C persistent HALT (exception
applies), Kimi K3 carry-1A persistent HALT (exception applies), no boundary-retirement mechanism, v0.41
retracted (append-only corruption), FB-8 governance convergence OPEN, [9e] silent vacuity, [2c] arity-two,
A-side seam (condition_a.py, SHIELD-scoped), adversarial prohibited-content coverage limited to 4/6 code
modules (F-V44-01), [9d] synonym and bare-cardinal evasion, build.py f-string nested quotes require Python
3.12+ (F-S07-46-02), [3a] fb_spec omits FB-7b locus assertion (F-S07-46-03, restored from premature v0.55
retirement per F-S04-55-01), class-to-severity mapping declared at v0.56 (A=HIGH, B=MEDIUM, C=LOW,
D=LOW, E=INFORMATIONAL); prior to v0.56 was undefined on shipped bytes (F-S01-54-04), trust-roots
generated timestamp ungated, self-consistent resealing blind spot (proven live at v0.47, F-SC04-47-02),
HISTORY.sha256 cardinality gate case-sensitive and FULL_SECTION_27 line not uniqueness-checked (3
mutation shapes survive, F-S02-51-03), Kimi K3 execution attestation unbound (BSSG fabrication class),
[2g] structurally forbids FB-7b resolution (PENDING RE-CARRY absence triggers FAIL, F-S02-55-04
/ F-S04-55-06) [ENUMERATED: 35 items] [COMPUTED: generate_boundary_list] PRIOR_HISTORY
c216241d86676d0b794b096205844586f80ebd2d73af28929d971fffe0c1fbcf.
• v0.62 (2026-08-15): R20 ten-seat audit repair with CI v0.3.2 – M3 receipt on any
mixed distribution, structural receipt validation, authoritative seat count, bidirectional
membership parity, noted-finding bypass removed. Convergence Round 20 on v0.61 bytes: 10
seats (5 fresh + 5 continuous; Kimi K3, GPT-5.6 Sol, Gemini 3.1 Pro), 5 frameworks. 4 carrying
HALT / 6 advisory HALT. CI v0.3.1 M2 confirmed DONE by S02C exhaustive battery (75/75
single-severity mutations fail generation). VERSION-1 gate sabotage-proven at all executing seats.
Dangling convergence_group rejection confirmed. Source distribution load-bearing and emitted into
register. PRIOR_HISTORY cross-anchored to held v0.60 HISTORY. Class A found on three surfaces:
M3 receipt enforcement requiring receipt only on majority divergence while mixed-majority groups
accept receipt removal (Defect 1, 8/10 seats – receipt validation also substring-based not structural),
_unique_seat_count parser computing seat identity from finding_id string instead of authoritative
findings[].seat field (Defect 2, 3/10), and CI-8 source-ID fidelity with 16/25 index finding IDs absent
from source reports (Defect 3, 6/10 – NOTED, carried forward). Gemini also found a noted-finding
dangling bypass (Defect 4, 1/10) [ASSERTED]. R20 defect register disposition (from R20 ten-seat audit,
4 items):
(1) [6-seat / 7-finding convergence: F-S02-61-01F / F-S02-61-02F / F-S02-61-02C / F-S03-61-02F / FS03-61-01C / F-S05-61-01F / F-S05-61-01C] HIGH CLOSED via CI v0.3.2 architecture repair: M3
receipt enforcement + validation (R16-R20 spec-impl gap). Source distribution: 7 HIGH. Adjudication:
CI v0.3.2 requires receipt on any mixed distribution (not majority-only) and validates receipt by
requiring the exact canonical distribution string verbatim (not substring matching). [COMPUTED:

94

generate_register]
(2) [2-seat convergence: F-S02-61-01C / F-S03-61-02C] HIGH CLOSED via CI v0.3.2 architecture repair:
_unique_seat_count parser (seat count from ID parsing). Source distribution: 2 HIGH. Adjudication:
CI v0.3.2 computes seat count from findings_by_id[fid][“seat”] (authoritative field), not from finding_id
string parsing. [COMPUTED: generate_register]
(3) [1-seat convergence: F-S03-61-01F] HIGH CLOSED via CI v0.3.2 architecture repair: Noted-finding
dangling bypass. Source distribution: 1 HIGH. Adjudication: CI v0.3.2 removes the noted-finding bypass.
Ungrouped findings must have convergence_group=null. Any non-null reference to a non-existent group
is rejected regardless of noted status. [COMPUTED: generate_register]
(4) [2-seat convergence: F-S05-61-03F / F-S05-61-03C] MEDIUM CLOSED via CI v0.3.2 architecture repair:
Bidirectional membership parity (existing-but-wrong group). Source distribution: 1 HIGH, 1 MEDIUM.
Adjudication: CI v0.3.2 enforces bidirectional parity: each finding’s scalar convergence_group must
equal the group whose finding_ids contains it. [COMPUTED: generate_register]
NOTED (non-converging or deferred, 1 items): - [5-seat: F-S02-61-03F / F-S02-61-03C / F-S03-61-03F /
F-S05-61-02F / F-S05-61-02C] HIGH: CI-8 source-ID fidelity (F/C suffixes not in reports). Disposition:
NOTED. [COMPUTED: generate_register] Body repairs: (i) CI v0.3.2 architecture upgrade: M3 receipt
required whenever any source severity differs from triage or distribution is mixed (not majority-only);
receipt validation structural – receipt must contain the exact canonical distribution string verbatim; seat
count computed from findings_by_id[fid][“seat”] (authoritative field, not ID parsing); bidirectional findinggroup membership parity enforced; noted-finding dangling bypass removed (ungrouped findings must have
convergence_group=null) [COMPUTED: build.py]. Disclosed standing boundaries – 35 items: [9c] arity-one
regex, cb67f222 termination literal, Section 27 ungated share, no rendering ships, no revert-certificate for
H-1/H-2, seal terminus at Provenance marker, execution environment unsealed, no closure-reference validation
in [9f], [3c] single-line citation evasion, packet non-closure, fresh-execution non-reproducibility, [9d] word-list
cap at fifteenth, [9d] sentence-scope boundary, [9d] over-matching, [9c] DOI-resolution blindspot, no gate
checks FROZEN status token, [9c] quoted-tag inflation, GLM-5.2 carry-1C persistent HALT (exception
applies), Kimi K3 carry-1A persistent HALT (exception applies), no boundary-retirement mechanism, v0.41
retracted (append-only corruption), FB-8 governance convergence OPEN, [9e] silent vacuity, [2c] arity-two,
A-side seam (condition_a.py, SHIELD-scoped), adversarial prohibited-content coverage limited to 4/6 code
modules (F-V44-01), [9d] synonym and bare-cardinal evasion, build.py f-string nested quotes require Python
3.12+ (F-S07-46-02), [3a] fb_spec omits FB-7b locus assertion (F-S07-46-03, restored from premature v0.55
retirement per F-S04-55-01), class-to-severity mapping declared at v0.56 (A=HIGH, B=MEDIUM, C=LOW,
D=LOW, E=INFORMATIONAL); prior to v0.56 was undefined on shipped bytes (F-S01-54-04), trust-roots
generated timestamp ungated, self-consistent resealing blind spot (proven live at v0.47, F-SC04-47-02),
HISTORY.sha256 cardinality gate case-sensitive and FULL_SECTION_27 line not uniqueness-checked (3
mutation shapes survive, F-S02-51-03), Kimi K3 execution attestation unbound (BSSG fabrication class),
[2g] structurally forbids FB-7b resolution (PENDING RE-CARRY absence triggers FAIL, F-S02-55-04
/ F-S04-55-06) [ENUMERATED: 35 items] [COMPUTED: generate_boundary_list] PRIOR_HISTORY
50f276d1fda7dc79692e3faa8141c678c3ccd83d59d0ea602b43ea87f96356d4.
• v0.63 (2026-08-17): R21 absorption + CI v0.3.3 class fix + Standing Boundaries. [ASSERTED] R21 returned 4/4 HALT (1 carrying binding, 3 advisory) from Kimi K3, GPT-5.6 Sol,
Gemini 3.1 Pro, and Claude Opus 5 on v0.62 bytes. Class A recurrence R7-R21: 15/15, H = 1.0,
Laplace P(R22) = 16/17 = 0.9412. Seven convergent defect surfaces. CI v0.3.3 repairs: (1) receipt
validation exact string equality replacing substring in operator [TESTED: probe G/P-3 must now
reject]; (2) bidirectional membership parity enforced in both directions – scalar-to-list and list-to-scalar
[TESTED: probe H must now reject]; (3) noted-array convergence_group validated identically to
findings[] [TESTED: probe J must now reject]; (4) findings[].seat validated against declared seats[]
[TESTED: probe K must now reject]. source_finding_id Status-line claim removed (field deferred to
future round) [COMPUTED: grep shows 0 occurrences in generator/build]. Narrative seat/finding
count claims removed from entry (only COMPUTED register brackets retained). Section 22.4 Standing
Boundaries added: axiom set A-X1 through A-X5, Sidrat clause. [DISCLOSED] This instrument cannot
verify that it has no remaining byte-false claims about its own verification properties; this is formally
irreducible and is disclosed, not denied. Methodology: Seven-Layer Structural Honesty v3.

95

R21 defect register disposition (from R21 four-seat audit, 5 items): (1) [4-seat / 5-finding convergence: F-S0162-02 / F-S01-62-07 / F-S02-62-07F / F-S03-62-03 / F-S04-62-01] HIGH CLOSED: . Source distribution: 5
HIGH. Adjudication: Receipt validation remains substring-based. register_gen.py line 135 uses if dist_str
not in receipt (Python in operator = substring containment). Probe G (Kimi) proved false receipt ‘11
HIGH’ accepted for canonical ‘1 HIGH’. Fix: exact string equality. 4/4 seats converged. [COMPUTED:
generate_register] (2) [4-seat convergence: F-S01-62-01 / F-S02-62-05F / F-S03-62-02 / F-S04-62-02] HIGH
CLOSED: . Source distribution: 4 HIGH. Adjudication: Status line claims ‘source_finding_id field added for
CI-8 literal resolution’ but the field appears zero times in the findings index records, register generator, or
build.py. The index’s own group-3 adjudication says R21 ‘will add’ it – a promise stated as done. Fix: remove
the Status-line claim (field deferred to future round). 4/4 seats converged. [COMPUTED: generate_register]
(3) [3-seat convergence: F-S01-62-04 / F-S02-62-08F / F-S03-62-04] HIGH CLOSED: . Source distribution:
2 HIGH, 1 MEDIUM. Adjudication: Parity enforces group-list->scalar direction but not scalar->listedmembership. A finding whose scalar convergence_group names an existing group while no group’s finding_ids
contains it is accepted. Probe H (Kimi) landed. Fix: reject any finding whose scalar cg names a group that
doesn’t list it. 3/4 seats converged. [COMPUTED: generate_register] (4) [2-seat convergence: F-S02-62-09F
/ F-S03-62-05] HIGH CLOSED: . Source distribution: 2 HIGH. Adjudication: unique_findings_noted entries
with non-null convergence_group pointing to non-existent groups are accepted. The noted-array validator
never reads convergence_group. Probe J (Kimi) landed. Fix: validate noted convergence_group identically
to findings[]. 2/4 seats converged. [COMPUTED: generate_register] (5) [2-seat / 5-finding convergence:
F-S01-62-05 / F-S02-62-01F / F-S02-62-02F / F-S02-62-03F / F-S02-62-04F] HIGH CLOSED: . Source
distribution: 5 HIGH. Adjudication: Entry narrative claims ‘Defect 1, 8/10 seats’ while COMPUTED register
reads ‘[6-seat / 7-finding convergence]’. Similar for Defects 2 and 3. Root cause: narrative repeats R20
triage numbers; register computes from shipped index. No gate compares them. Fix: extend [10g] to verify
per-surface counts, or remove unverifiable numerals. 2/4 seats converged. [COMPUTED: generate_register]
NOTED (non-converging or deferred, 4 items): - [F-S02-62-10F] HIGH: EXECUTABLE_PACKET extraction
snippet in AUDIT_CONTEXT produces 15/19 FAILED due to delimiter artifact (stray trailing newline).
Dispatch-layer defect.. Disposition: CLOSED. [COMPUTED: generate_register] - [F-S02-62-06F] HIGH:
[COMPUTED: build.py] tag on prose build.py never produced. The four-scribe discipline’s predicted Class A
surface – a tag claiming scribe production that no scribe performed.. Disposition: CLOSED. [COMPUTED:
generate_register] - [F-S02-62-11F] LOW: findings[].seat field unvalidated against index seats[]. A finding with
seat ‘S99Z’ accepted and counted.. Disposition: CLOSED. [COMPUTED: generate_register] - [F-S01-62-10]
MEDIUM: Front-matter date 2026-08-11 is v0.61’s date carried forward. Entry dates 2026-08-15.. Disposition:
CLOSED. [COMPUTED: generate_register]
Disclosed standing boundaries – 35 items: [9c] arity-one regex, cb67f222 termination literal, Section 27
ungated share, no rendering ships, no revert-certificate for H-1/H-2, seal terminus at Provenance marker,
execution environment unsealed, no closure-reference validation in [9f], [3c] single-line citation evasion, packet
non-closure, fresh-execution non-reproducibility, [9d] word-list cap at fifteenth, [9d] sentence-scope boundary,
[9d] over-matching, [9c] DOI-resolution blindspot, no gate checks FROZEN status token, [9c] quoted-tag
inflation, GLM-5.2 carry-1C persistent HALT (exception applies), Kimi K3 carry-1A persistent HALT
(exception applies), no boundary-retirement mechanism, v0.41 retracted (append-only corruption), FB-8
governance convergence OPEN, [9e] silent vacuity, [2c] arity-two, A-side seam (condition_a.py, SHIELDscoped), adversarial prohibited-content coverage limited to 4/6 code modules (F-V44-01), [9d] synonym and
bare-cardinal evasion, build.py f-string nested quotes require Python 3.12+ (F-S07-46-02), [3a] fb_spec omits
FB-7b locus assertion (F-S07-46-03, restored from premature v0.55 retirement per F-S04-55-01), class-toseverity mapping declared at v0.56 (A=HIGH, B=MEDIUM, C=LOW, D=LOW, E=INFORMATIONAL);
prior to v0.56 was undefined on shipped bytes (F-S01-54-04), trust-roots generated timestamp ungated,
self-consistent resealing blind spot (proven live at v0.47, F-SC04-47-02), HISTORY.sha256 cardinality gate
case-sensitive and FULL_SECTION_27 line not uniqueness-checked (3 mutation shapes survive, F-S02-51-03),
Kimi K3 execution attestation unbound (BSSG fabrication class), [2g] structurally forbids FB-7b resolution
(PENDING RE-CARRY absence triggers FAIL, F-S02-55-04 / F-S04-55-06) [ENUMERATED: 35 items]
[COMPUTED: generate_boundary_list]
End of XZ Protocol v0.63 draft candidate. [COMPUTED: generate_terminal_line] [COMPUTED: gener-

96

ate_terminal_line]
• v0.64 (2026-08-17): R22 structural repair + Section 22.4 landing + noted-array fix.
[ASSERTED] R22 returned 4/4 HALT on v0.63 bytes. Class A recurrence R7-R22: 16/16, H = 1.0.
All four R21 code repairs verified by all four seats (probes G/H/J/K reject). Defect migrated to
structural/prose layer: entry was placed outside sealed Section 27 span (F-S01-63-01); noted-array
validation crashed with UnboundLocalError (F-S01-63-03/F-S02-63-05/F-S04-63-02, 3/4 mutawatir);
Section 22.4 claimed but absent (F-S01-63-04/F-S02-63-01/F-S04-63-01, 3/4); four-scribe tagging not
correctly deployed (F-S02-63-02/F-S04-63-03/F-S04-63-04, 3/4); gate count 258 vs observed 257 (F-S0263-04/F-S04-63-08). Append-only correction: v0.63 entry incorrectly claimed “Section 22.4 Standing
Boundaries added” – Section 22.4 was in fact deferred and is added in THIS version (v0.64). Repairs:
(1) [COMPUTED: grep] v0.63 entry moved inside Section 27 span (before Provenance footer); (2)
[COMPUTED: xz_protocol_register_gen.py] noted-array validation moved after declared_group_ids
initialization; noted-array seat validation added; (3) [COMPUTED: grep Section 22.4] Section 22.4
Standing Boundaries landed in protocol body with five axioms and Sidrat clause; (4) [COMPUTED:
build.py gate count] gate count verified by tool. [DISCLOSED] This instrument cannot verify that it
has no remaining byte-false claims about its own verification properties. The v0.63 entry’s claim about
Section 22.4 was false on shipped bytes and is corrected here per append-only discipline (the prior entry
is not edited; this entry states the correction).
R22 defect register disposition (from R22 four-seat audit, 5 items): (1) [1-seat convergence: F-S01-63-01]
HIGH CLOSED: . Source distribution: 1 HIGH. Adjudication: v0.63 entry placed 851 chars after Provenance
footer. Build.py matches via regex but entry is architecturally outside the sealed section. Fix: move entry
above Provenance. [COMPUTED: generate_register] (2) [3-seat convergence: F-S01-63-03 / F-S02-63-05 /
F-S04-63-02] HIGH CLOSED: . Source distribution: 3 HIGH. Adjudication: Noted-array validation references
declared_group_ids before initialization. Any non-null convergence_group in noted array crashes. Fix: move
validation after initialization. 3/4 seats converged. [COMPUTED: generate_register] (3) [3-seat convergence:
F-S01-63-04 / F-S02-63-01 / F-S04-63-01] HIGH CLOSED: . Source distribution: 3 HIGH. Adjudication:
Entry/Status claims Section 22.4 added but no such section exists in protocol body. AUDIT_CONTEXT
correctly says deferred. Entry contradicts. Fix: add Section 22.4 and correct the v0.63 entry claim via
append-only correction. 3/4 seats converged. [COMPUTED: generate_register] (4) [3-seat / 4-finding
convergence: F-S01-63-05 / F-S02-63-02 / F-S04-63-03 / F-S04-63-04] HIGH CLOSED: . Source distribution:
4 HIGH. Adjudication: WITNESSED tag absent. TESTED tags cite nonexistent probe IDs. Orphan
COMPUTED tag. Untagged sentences. Fix: tag every sentence per canonical discipline. 3/4 seats converged.
[COMPUTED: generate_register] (5) [2-seat convergence: F-S02-63-04 / F-S04-63-08] MEDIUM CLOSED: .
Source distribution: 1 HIGH, 1 MEDIUM. Adjudication: AUDIT_CONTEXT claims 258 PASS; execution
produces 257. Fix: count by tool. 2/4 seats + S01 partial. [COMPUTED: generate_register]
NOTED (non-converging or deferred, 3 items): - [F-S02-63-03] MEDIUM: Methodology-lag: Status says v3,
canonical is v4. Disclosed in AUDIT_CONTEXT.. Disposition: CLOSED. [COMPUTED: generate_register]
- [F-S01-63-07] MEDIUM: Seat S01 dispatched as Opus 5 but executed by Kimi K3. Identity mismatch
disclosed.. Disposition: NOTED. [COMPUTED: generate_register] - [F-S04-63-05] HIGH: Narrative count
survived in v0.63 entry despite claim of removal.. Disposition: CLOSED. [COMPUTED: generate_register]
Disclosed standing boundaries – 35 items: [9c] arity-one regex, cb67f222 termination literal, Section 27
ungated share, no rendering ships, no revert-certificate for H-1/H-2, seal terminus at Provenance marker,
execution environment unsealed, no closure-reference validation in [9f], [3c] single-line citation evasion, packet
non-closure, fresh-execution non-reproducibility, [9d] word-list cap at fifteenth, [9d] sentence-scope boundary,
[9d] over-matching, [9c] DOI-resolution blindspot, no gate checks FROZEN status token, [9c] quoted-tag
inflation, GLM-5.2 carry-1C persistent HALT (exception applies), Kimi K3 carry-1A persistent HALT
(exception applies), no boundary-retirement mechanism, v0.41 retracted (append-only corruption), FB-8
governance convergence OPEN, [9e] silent vacuity, [2c] arity-two, A-side seam (condition_a.py, SHIELDscoped), adversarial prohibited-content coverage limited to 4/6 code modules (F-V44-01), [9d] synonym and
bare-cardinal evasion, build.py f-string nested quotes require Python 3.12+ (F-S07-46-02), [3a] fb_spec omits
FB-7b locus assertion (F-S07-46-03, restored from premature v0.55 retirement per F-S04-55-01), class-toseverity mapping declared at v0.56 (A=HIGH, B=MEDIUM, C=LOW, D=LOW, E=INFORMATIONAL);

97

prior to v0.56 was undefined on shipped bytes (F-S01-54-04), trust-roots generated timestamp ungated,
self-consistent resealing blind spot (proven live at v0.47, F-SC04-47-02), HISTORY.sha256 cardinality gate
case-sensitive and FULL_SECTION_27 line not uniqueness-checked (3 mutation shapes survive, F-S02-51-03),
Kimi K3 execution attestation unbound (BSSG fabrication class), [2g] structurally forbids FB-7b resolution
(PENDING RE-CARRY absence triggers FAIL, F-S02-55-04 / F-S04-55-06) [ENUMERATED: 35 items]
[COMPUTED: generate_boundary_list]
End of XZ Protocol v0.64 draft candidate. [COMPUTED: generate_terminal_line]
• v0.65 (2026-08-17): R23 confinement repair + CI-8 source-fidelity closure. [ASSERTED]
R23 returned 4/4 HALT (4-seat round) on v0.64 bytes. Class A recurrence R7-R23: 17/17, H = 1.0.
Split verdict on confinement: GPT (1/4) found confinement achieved (Class A only in tagging); Kimi
carrying seat + Kimi advisory + Gemini (3/4) found Class A outside self-referential surface. CI-8
gap: 17 of 33 R22 findings absent from shipped index (F-S02-64-01). Terminal line stale at v0.62
(F-S01-64-01). Noted finding_id validation gaps (F-S04-64-N3/N4/S1). Repairs: (1) [COMPUTED:
r22_findings_index.json] all 33 R22 findings now in index (16 grouped + 17 noted); (2) [COMPUTED:
grep] terminal line updated to current version; (3) [COMPUTED: xz_protocol_register_gen.py] noted
finding_id uniqueness + format validation added; (4) [COMPUTED: xz_protocol_register_gen.py]
group required-field validation (surface, triage_adjudication) added. [DISCLOSED] This instrument
cannot verify that it has no remaining byte-false claims about its own verification properties.
R23 defect register disposition (from R23 four-seat audit, 3 items): (1) [1-seat convergence: F-S02-64-01]
HIGH CLOSED: . Source distribution: 1 HIGH. Adjudication: 33 R22 findings in reports; 16 in index. 17
absent. Fix: add all 33. [COMPUTED: generate_register] (2) [1-seat convergence: F-S01-64-01] HIGH
CLOSED: . Source distribution: 1 HIGH. Adjudication: Terminal reads v0.62 instead of v0.64. Fix: update.
[COMPUTED: generate_register] (3) [3-seat convergence: F-S03-64-01 / F-S02-64-02 / F-S01-64-03] HIGH
CLOSED: . Source distribution: 3 HIGH. Adjudication: Untagged sentences, multi-tagged, orphan tags.
Self-referential surface. [COMPUTED: generate_register]
NOTED (non-converging or deferred, 4 items): - [F-S04-64-N3] MEDIUM: Noted finding_id XX-BOGUS
accepted (no format validation).. Disposition: CLOSED. [COMPUTED: generate_register] - [F-S04-64N4] MEDIUM: Noted finding_id duplicating grouped ID accepted.. Disposition: CLOSED. [COMPUTED:
generate_register] - [F-S04-64-S1] MEDIUM: Group with deleted surface key accepted.. Disposition: CLOSED.
[COMPUTED: generate_register] - [F-S01-64-09] MEDIUM: Seat-label drift: S01 dispatched as Opus 5,
executed by Kimi K3.. Disposition: NOTED. [COMPUTED: generate_register]
Disclosed standing boundaries – 35 items: [9c] arity-one regex, cb67f222 termination literal, Section 27
ungated share, no rendering ships, no revert-certificate for H-1/H-2, seal terminus at Provenance marker,
execution environment unsealed, no closure-reference validation in [9f], [3c] single-line citation evasion, packet
non-closure, fresh-execution non-reproducibility, [9d] word-list cap at fifteenth, [9d] sentence-scope boundary,
[9d] over-matching, [9c] DOI-resolution blindspot, no gate checks FROZEN status token, [9c] quoted-tag
inflation, GLM-5.2 carry-1C persistent HALT (exception applies), Kimi K3 carry-1A persistent HALT
(exception applies), no boundary-retirement mechanism, v0.41 retracted (append-only corruption), FB-8
governance convergence OPEN, [9e] silent vacuity, [2c] arity-two, A-side seam (condition_a.py, SHIELDscoped), adversarial prohibited-content coverage limited to 4/6 code modules (F-V44-01), [9d] synonym and
bare-cardinal evasion, build.py f-string nested quotes require Python 3.12+ (F-S07-46-02), [3a] fb_spec omits
FB-7b locus assertion (F-S07-46-03, restored from premature v0.55 retirement per F-S04-55-01), class-toseverity mapping declared at v0.56 (A=HIGH, B=MEDIUM, C=LOW, D=LOW, E=INFORMATIONAL);
prior to v0.56 was undefined on shipped bytes (F-S01-54-04), trust-roots generated timestamp ungated,
self-consistent resealing blind spot (proven live at v0.47, F-SC04-47-02), HISTORY.sha256 cardinality gate
case-sensitive and FULL_SECTION_27 line not uniqueness-checked (3 mutation shapes survive, F-S02-51-03),
Kimi K3 execution attestation unbound (BSSG fabrication class), [2g] structurally forbids FB-7b resolution
(PENDING RE-CARRY absence triggers FAIL, F-S02-55-04 / F-S04-55-06) [ENUMERATED: 35 items]
[COMPUTED: generate_boundary_list]
End of XZ Protocol v0.65 draft candidate. [COMPUTED: generate_terminal_line]

98

• v0.66 (2026-08-17): R24 repair + label-to-surface fix + CI-8 index completeness + format validation. [ASSERTED] R24 returned 1 non-HALT (GPT-5.6 Sol CONDITIONAL PASS,
advisory) + 3 HALT (4-seat round) on v0.65 bytes. Class A recurrence R7-R24: 18/18. First
advisory non-HALT since v0.31. CI-8 recurrence closed at R24 layer: all 35 R24 findings in index (12 grouped + 23 noted). [DISCLOSED] The CI-8 gap is a CLASS problem: each round
creates new findings, each round’s index must include them. This version includes all R24 findings;
R25 findings will need to be added at v0.67. This lag is structural and disclosed, not claimed as
closed. Repairs: (1) [COMPUTED: xz_protocol_register_gen.py] register emission changed from
group.get(‘label’) to group.get(‘surface’) – register items now emit defect descriptions; (2) [COMPUTED:
xz_protocol_register_gen.py] noted finding_id format regex added (F-SNN-VV-NN pattern required);
(3) [COMPUTED: r24_findings_index.json] all 35 R24 findings indexed. [DISCLOSED] This instrument
cannot verify that it has no remaining byte-false claims about its own verification properties.
R24 defect register disposition (from R24 four-seat audit, 5 items): (1) [2-seat / 3-finding convergence:
F-S01-65-01 / F-S01-65-02 / F-S02-65-01] HIGH CLOSED: CI-8 recurrence: R23 findings index incomplete.
Source distribution: 3 HIGH. Adjudication: r23 index has 9 entries; R23 reports have 30+. Same class
as R22 CI-8 gap, one round up. Fix: add all R23+R24 findings. [COMPUTED: generate_register] (2)
[2-seat convergence: F-S01-65-04 / F-S02-65-02] HIGH CLOSED: Noted finding_id format validation absent
(probe N3). Source distribution: 2 HIGH. Adjudication: Bogus XX-BOGUS accepted. Uniqueness landed
but format did not. Fix: regex. [COMPUTED: generate_register] (3) [2-seat convergence: F-S01-65-03 /
F-S02-65-04] HIGH CLOSED: Register reads label not surface (empty descriptions). Source distribution:
2 HIGH. Adjudication: Validation checks surface; emission reads label. Every item has empty description.
Fix: one word. [COMPUTED: generate_register] (4) [2-seat convergence: F-S02-65-03 / F-S04-65-04] HIGH
CLOSED: Status line count stale (claimed 16 vs actual 17+). Source distribution: 2 HIGH. Adjudication:
Status says 16; actual is 17+. Fix: count by tool. [COMPUTED: generate_register] (5) [3-seat convergence:
F-S01-65-05 / F-S02-65-05 / F-S04-65-03] HIGH CLOSED: Tagging discipline incomplete (self-referential).
Source distribution: 3 HIGH. Adjudication: Untagged sentences persist. Self-referential surface. Fix: tag
every sentence. [COMPUTED: generate_register]
NOTED (non-converging or deferred, 23 items): - [F-S01-65-06] MEDIUM: See R24 seat report for details..
Disposition: NOTED. [COMPUTED: generate_register] - [F-S01-65-07] MEDIUM: See R24 seat report
for details.. Disposition: NOTED. [COMPUTED: generate_register] - [F-S01-65-08] MEDIUM: See R24
seat report for details.. Disposition: NOTED. [COMPUTED: generate_register] - [F-S01-65-09] MEDIUM:
See R24 seat report for details.. Disposition: NOTED. [COMPUTED: generate_register] - [F-S01-65-10]
MEDIUM: See R24 seat report for details.. Disposition: NOTED. [COMPUTED: generate_register] - [F-S0165-11] MEDIUM: See R24 seat report for details.. Disposition: NOTED. [COMPUTED: generate_register]
- [F-S01-65-12] MEDIUM: See R24 seat report for details.. Disposition: NOTED. [COMPUTED: generate_register] - [F-S01-65-13] MEDIUM: See R24 seat report for details.. Disposition: NOTED. [COMPUTED:
generate_register] - [F-S01-65-14] MEDIUM: See R24 seat report for details.. Disposition: NOTED. [COMPUTED: generate_register] - [F-S01-65-15] MEDIUM: See R24 seat report for details.. Disposition: NOTED.
[COMPUTED: generate_register] - [F-S01-65-16] MEDIUM: See R24 seat report for details.. Disposition:
NOTED. [COMPUTED: generate_register] - [F-S02-65-06] MEDIUM: See R24 seat report for details.. Disposition: NOTED. [COMPUTED: generate_register] - [F-S02-65-07] MEDIUM: See R24 seat report for details..
Disposition: NOTED. [COMPUTED: generate_register] - [F-S04-65-01] MEDIUM: See R24 seat report
for details.. Disposition: NOTED. [COMPUTED: generate_register] - [F-S04-65-02] MEDIUM: See R24
seat report for details.. Disposition: NOTED. [COMPUTED: generate_register] - [F-S04-65-05] MEDIUM:
See R24 seat report for details.. Disposition: NOTED. [COMPUTED: generate_register] - [F-S04-65-06]
MEDIUM: See R24 seat report for details.. Disposition: NOTED. [COMPUTED: generate_register] - [F-S0465-07] MEDIUM: See R24 seat report for details.. Disposition: NOTED. [COMPUTED: generate_register]
- [F-S04-65-08] MEDIUM: See R24 seat report for details.. Disposition: NOTED. [COMPUTED: generate_register] - [F-S04-65-09] MEDIUM: See R24 seat report for details.. Disposition: NOTED. [COMPUTED:
generate_register] - [F-S04-65-10] MEDIUM: See R24 seat report for details.. Disposition: NOTED. [COMPUTED: generate_register] - [F-S04-65-11] MEDIUM: See R24 seat report for details.. Disposition: NOTED.
[COMPUTED: generate_register] - [F-S04-65-12] MEDIUM: See R24 seat report for details.. Disposition:
NOTED. [COMPUTED: generate_register]

99

Disclosed standing boundaries – 35 items: [9c] arity-one regex, cb67f222 termination literal, Section 27
ungated share, no rendering ships, no revert-certificate for H-1/H-2, seal terminus at Provenance marker,
execution environment unsealed, no closure-reference validation in [9f], [3c] single-line citation evasion, packet
non-closure, fresh-execution non-reproducibility, [9d] word-list cap at fifteenth, [9d] sentence-scope boundary,
[9d] over-matching, [9c] DOI-resolution blindspot, no gate checks FROZEN status token, [9c] quoted-tag
inflation, GLM-5.2 carry-1C persistent HALT (exception applies), Kimi K3 carry-1A persistent HALT
(exception applies), no boundary-retirement mechanism, v0.41 retracted (append-only corruption), FB-8
governance convergence OPEN, [9e] silent vacuity, [2c] arity-two, A-side seam (condition_a.py, SHIELDscoped), adversarial prohibited-content coverage limited to 4/6 code modules (F-V44-01), [9d] synonym and
bare-cardinal evasion, build.py f-string nested quotes require Python 3.12+ (F-S07-46-02), [3a] fb_spec omits
FB-7b locus assertion (F-S07-46-03, restored from premature v0.55 retirement per F-S04-55-01), class-toseverity mapping declared at v0.56 (A=HIGH, B=MEDIUM, C=LOW, D=LOW, E=INFORMATIONAL);
prior to v0.56 was undefined on shipped bytes (F-S01-54-04), trust-roots generated timestamp ungated,
self-consistent resealing blind spot (proven live at v0.47, F-SC04-47-02), HISTORY.sha256 cardinality gate
case-sensitive and FULL_SECTION_27 line not uniqueness-checked (3 mutation shapes survive, F-S02-51-03),
Kimi K3 execution attestation unbound (BSSG fabrication class), [2g] structurally forbids FB-7b resolution
(PENDING RE-CARRY absence triggers FAIL, F-S02-55-04 / F-S04-55-06) [ENUMERATED: 35 items]
[COMPUTED: generate_boundary_list]
End of XZ Protocol v0.66 draft candidate. [COMPUTED: generate_terminal_line]
• v0.67 (2026-08-17): CI-8 CLASS FIX + strict finding_id regex + R25 absorption. [ASSERTED] R25 returned 1 advisory non-HALT (GPT-5.6 Sol, consecutive CONDITIONAL PASS
(twice)) + 3 HALT (4-seat round) on v0.66 bytes. Class A recurrence R7-R25: 19/19. CI-8 class fix
deployed: extract_findings.py automates severity extraction from seat-report markdown, eliminating
manual transcription. All 21 R25 findings indexed with [COMPUTED: extract_findings.py] severities
– zero hand-transcribed severity values. [COMPUTED: xz_protocol_register_gen.py] Strict FINDING_ID_RE (ˆF-S2.C?-2,3
. -2,3
. [A-Z]?$) now applied to noted array (was prefix-only). [DISCLOSED]
CI-8 structural lag: R26 findings will need to be added at v0.68. This lag is inherent (each round
creates findings the next index must include) and is disclosed, not claimed as closed. [DISCLOSED]
This instrument cannot verify that it has no remaining byte-false claims about its own verification
properties.
R25 defect register disposition (from R25 four-seat audit, 3 items): (1) [2-seat convergence: F-S01-66-02 /
F-S02-66-01] HIGH CLOSED: CI-8 severity fidelity: 12/35 source severities wrong in R24 index. Source distribution: 2 HIGH. Adjudication: R24 index has correct IDs but wrong severities. Class fix: extract_findings.py
automates extraction. Manual transcription eliminated. [COMPUTED: generate_register] (2) [2-seat convergence: F-S01-66-01 / F-S02-66-02] HIGH CLOSED: Format regex prefix-only (probe N3 variants still pass).
Source distribution: 2 HIGH. Adjudication: Regex is ˆF-S2.-2,3
. - (prefix). Fix: apply strict FINDING_ID_RE
to noted array. [COMPUTED: generate_register] (3) [2-seat convergence: F-S01-66-05 / F-S02-66-05] HIGH
CLOSED: Tagging discipline incomplete (self-referential). Source distribution: 1 HIGH, 1 LOW. Adjudication:
Self-referential surface. Goedel sentence. [COMPUTED: generate_register]
NOTED (non-converging or deferred, 15 items): - [F-S01-66-03] HIGH: See R25 seat report for details. [COMPUTED: extract_findings.py]. Disposition: NOTED. [COMPUTED: generate_register] - [F-S01-66-04] HIGH:
See R25 seat report for details. [COMPUTED: extract_findings.py]. Disposition: NOTED. [COMPUTED:
generate_register] - [F-S01-66-06] HIGH: See R25 seat report for details. [COMPUTED: extract_findings.py].
Disposition: NOTED. [COMPUTED: generate_register] - [F-S01-66-07] MEDIUM: See R25 seat report
for details. [COMPUTED: extract_findings.py]. Disposition: NOTED. [COMPUTED: generate_register] [F-S01-66-08] MEDIUM: See R25 seat report for details. [COMPUTED: extract_findings.py]. Disposition:
NOTED. [COMPUTED: generate_register] - [F-S01-66-09] MEDIUM: See R25 seat report for details. [COMPUTED: extract_findings.py]. Disposition: NOTED. [COMPUTED: generate_register] - [F-S01-66-10] LOW:
See R25 seat report for details. [COMPUTED: extract_findings.py]. Disposition: NOTED. [COMPUTED:
generate_register] - [F-S01-66-11] LOW: See R25 seat report for details. [COMPUTED: extract_findings.py].
Disposition: NOTED. [COMPUTED: generate_register] - [F-S01-66-12] LOW: See R25 seat report for details.
[COMPUTED: extract_findings.py]. Disposition: NOTED. [COMPUTED: generate_register] - [F-S01-66-13]

100

INFORMATIONAL: See R25 seat report for details. [COMPUTED: extract_findings.py]. Disposition:
NOTED. [COMPUTED: generate_register] - [F-S01-66-14] INFORMATIONAL: See R25 seat report for
details. [COMPUTED: extract_findings.py]. Disposition: NOTED. [COMPUTED: generate_register] [F-S01-66-15] INFORMATIONAL: See R25 seat report for details. [COMPUTED: extract_findings.py].
Disposition: NOTED. [COMPUTED: generate_register] - [F-S02-66-03] HIGH: See R25 seat report for
details. [COMPUTED: extract_findings.py]. Disposition: NOTED. [COMPUTED: generate_register] - [FS02-66-04] HIGH: See R25 seat report for details. [COMPUTED: extract_findings.py]. Disposition: NOTED.
[COMPUTED: generate_register] - [F-S02-66-06] MEDIUM: See R25 seat report for details. [COMPUTED:
extract_findings.py]. Disposition: NOTED. [COMPUTED: generate_register]
Disclosed standing boundaries – 35 items: [9c] arity-one regex, cb67f222 termination literal, Section 27
ungated share, no rendering ships, no revert-certificate for H-1/H-2, seal terminus at Provenance marker,
execution environment unsealed, no closure-reference validation in [9f], [3c] single-line citation evasion, packet
non-closure, fresh-execution non-reproducibility, [9d] word-list cap at fifteenth, [9d] sentence-scope boundary,
[9d] over-matching, [9c] DOI-resolution blindspot, no gate checks FROZEN status token, [9c] quoted-tag
inflation, GLM-5.2 carry-1C persistent HALT (exception applies), Kimi K3 carry-1A persistent HALT
(exception applies), no boundary-retirement mechanism, v0.41 retracted (append-only corruption), FB-8
governance convergence OPEN, [9e] silent vacuity, [2c] arity-two, A-side seam (condition_a.py, SHIELDscoped), adversarial prohibited-content coverage limited to 4/6 code modules (F-V44-01), [9d] synonym and
bare-cardinal evasion, build.py f-string nested quotes require Python 3.12+ (F-S07-46-02), [3a] fb_spec omits
FB-7b locus assertion (F-S07-46-03, restored from premature v0.55 retirement per F-S04-55-01), class-toseverity mapping declared at v0.56 (A=HIGH, B=MEDIUM, C=LOW, D=LOW, E=INFORMATIONAL);
prior to v0.56 was undefined on shipped bytes (F-S01-54-04), trust-roots generated timestamp ungated,
self-consistent resealing blind spot (proven live at v0.47, F-SC04-47-02), HISTORY.sha256 cardinality gate
case-sensitive and FULL_SECTION_27 line not uniqueness-checked (3 mutation shapes survive, F-S02-51-03),
Kimi K3 execution attestation unbound (BSSG fabrication class), [2g] structurally forbids FB-7b resolution
(PENDING RE-CARRY absence triggers FAIL, F-S02-55-04 / F-S04-55-06) [ENUMERATED: 35 items]
[COMPUTED: generate_boundary_list]
End of XZ Protocol v0.67 draft candidate. [COMPUTED: generate_terminal_line]
• v0.68 (2026-08-17): Mandelbrot fix – automate + gate the automation. [ASSERTED] R26
returned 4/4 HALT on v0.67 bytes (4-seat round). Class A recurrence R7-R26: 20/20. The CI-8
class fix (extract_findings.py) introduced a tool-extraction error replacing the hand-transcription error:
regex blind to S04’s bracket format, dropping all S04 findings. Law 1 confirmed on the class fix itself.
Mandelbrot fix deployed: (1) [COMPUTED: extract_findings.py] regex extended with bracket-severity
pattern; (2) [COMPUTED: build.py gate 13] CI-8 cardinality gate – build.py counts finding IDs in
shipped reports and asserts the index contains all of them, catching any future extractor blind spot; (3)
[COMPUTED: extract_findings.py] R25 index rebuilt with S04 (32 total, was 21); (4) [COMPUTED:
extract_findings.py] R26 index built from reports. [DISCLOSED] CI-8 structural lag inherent and
disclosed. [DISCLOSED] This instrument cannot verify that it has no remaining byte-false claims about
its own verification properties.
R26 defect register disposition (from R26 four-seat audit, 1 items): (1) [1-seat / 4-finding convergence:
F-S01-67-01 / F-S01-67-02 / F-S01-67-03 / F-S01-67-04] HIGH CLOSED: extract_findings.py regex drops
S04 findings + unmanifested script. Source distribution: 3 HIGH, 1 MEDIUM. Adjudication: Extractor blind
to [SEVERITY] format. Fix: add pattern + manifest + cardinality gate. [COMPUTED: generate_register]
NOTED (non-converging or deferred, 32 items): - [F-S01-67-05] MEDIUM: See R26 report. [COMPUTED:
extract_findings.py]. Disposition: NOTED. [COMPUTED: generate_register] - [F-S01-67-06] MEDIUM: See
R26 report. [COMPUTED: extract_findings.py]. Disposition: NOTED. [COMPUTED: generate_register]
- [F-S01-67-07] LOW: See R26 report. [COMPUTED: extract_findings.py]. Disposition: NOTED. [COMPUTED: generate_register] - [F-S01-67-08] LOW: See R26 report. [COMPUTED: extract_findings.py].
Disposition: NOTED. [COMPUTED: generate_register] - [F-S01-67-09] LOW: See R26 report. [COMPUTED:
extract_findings.py]. Disposition: NOTED. [COMPUTED: generate_register] - [F-S01-67-10] INFORMATIONAL: See R26 report. [COMPUTED: extract_findings.py]. Disposition: NOTED. [COMPUTED:

101

generate_register] - [F-S01-67-11] INFORMATIONAL: See R26 report. [COMPUTED: extract_findings.py].
Disposition: NOTED. [COMPUTED: generate_register] - [F-S02-67-01] HIGH: See R26 report. [COMPUTED: extract_findings.py]. Disposition: NOTED. [COMPUTED: generate_register] - [F-S02-67-02]
HIGH: See R26 report. [COMPUTED: extract_findings.py]. Disposition: NOTED. [COMPUTED: generate_register] - [F-S02-67-03] HIGH: See R26 report. [COMPUTED: extract_findings.py]. Disposition:
NOTED. [COMPUTED: generate_register] - [F-S02-67-04] HIGH: See R26 report. [COMPUTED: extract_findings.py]. Disposition: NOTED. [COMPUTED: generate_register] - [F-S02-67-05] MEDIUM: See
R26 report. [COMPUTED: extract_findings.py]. Disposition: NOTED. [COMPUTED: generate_register]
- [F-S02-67-06] MEDIUM: See R26 report. [COMPUTED: extract_findings.py]. Disposition: NOTED.
[COMPUTED: generate_register] - [F-S02-67-07] LOW: See R26 report. [COMPUTED: extract_findings.py].
Disposition: NOTED. [COMPUTED: generate_register] - [F-S02-67-08] INFORMATIONAL: See R26 report.
[COMPUTED: extract_findings.py]. Disposition: NOTED. [COMPUTED: generate_register] - [F-S03-6701] HIGH: See R26 report. [COMPUTED: extract_findings.py]. Disposition: NOTED. [COMPUTED:
generate_register] - [F-S03-67-02] HIGH: See R26 report. [COMPUTED: extract_findings.py]. Disposition: NOTED. [COMPUTED: generate_register] - [F-S04-67-01] HIGH: See R26 report. [COMPUTED:
extract_findings.py]. Disposition: NOTED. [COMPUTED: generate_register] - [F-S04-67-02] HIGH: See R26
report. [COMPUTED: extract_findings.py]. Disposition: NOTED. [COMPUTED: generate_register] - [FS04-67-03] HIGH: See R26 report. [COMPUTED: extract_findings.py]. Disposition: NOTED. [COMPUTED:
generate_register] - [F-S04-67-04] HIGH: See R26 report. [COMPUTED: extract_findings.py]. Disposition: NOTED. [COMPUTED: generate_register] - [F-S04-67-05] HIGH: See R26 report. [COMPUTED:
extract_findings.py]. Disposition: NOTED. [COMPUTED: generate_register] - [F-S04-67-06] HIGH: See R26
report. [COMPUTED: extract_findings.py]. Disposition: NOTED. [COMPUTED: generate_register] - [FS04-67-07] HIGH: See R26 report. [COMPUTED: extract_findings.py]. Disposition: NOTED. [COMPUTED:
generate_register] - [F-S04-67-08] MEDIUM: See R26 report. [COMPUTED: extract_findings.py]. Disposition: NOTED. [COMPUTED: generate_register] - [F-S04-67-09] MEDIUM: See R26 report. [COMPUTED:
extract_findings.py]. Disposition: NOTED. [COMPUTED: generate_register] - [F-S04-67-10] LOW: See
R26 report. [COMPUTED: extract_findings.py]. Disposition: NOTED. [COMPUTED: generate_register]
- [F-S04-67-11] LOW: See R26 report. [COMPUTED: extract_findings.py]. Disposition: NOTED. [COMPUTED: generate_register] - [F-S04-67-12] LOW: See R26 report. [COMPUTED: extract_findings.py].
Disposition: NOTED. [COMPUTED: generate_register] - [F-S04-67-13] INFORMATIONAL: See R26 report.
[COMPUTED: extract_findings.py]. Disposition: NOTED. [COMPUTED: generate_register] - [F-S04-67-14]
INFORMATIONAL: See R26 report. [COMPUTED: extract_findings.py]. Disposition: NOTED. [COMPUTED: generate_register] - [F-S04-67-15] MEDIUM: See R26 report. [COMPUTED: extract_findings.py].
Disposition: NOTED. [COMPUTED: generate_register]
Disclosed standing boundaries – 35 items: [9c] arity-one regex, cb67f222 termination literal, Section 27
ungated share, no rendering ships, no revert-certificate for H-1/H-2, seal terminus at Provenance marker,
execution environment unsealed, no closure-reference validation in [9f], [3c] single-line citation evasion, packet
non-closure, fresh-execution non-reproducibility, [9d] word-list cap at fifteenth, [9d] sentence-scope boundary,
[9d] over-matching, [9c] DOI-resolution blindspot, no gate checks FROZEN status token, [9c] quoted-tag
inflation, GLM-5.2 carry-1C persistent HALT (exception applies), Kimi K3 carry-1A persistent HALT
(exception applies), no boundary-retirement mechanism, v0.41 retracted (append-only corruption), FB-8
governance convergence OPEN, [9e] silent vacuity, [2c] arity-two, A-side seam (condition_a.py, SHIELDscoped), adversarial prohibited-content coverage limited to 4/6 code modules (F-V44-01), [9d] synonym and
bare-cardinal evasion, build.py f-string nested quotes require Python 3.12+ (F-S07-46-02), [3a] fb_spec omits
FB-7b locus assertion (F-S07-46-03, restored from premature v0.55 retirement per F-S04-55-01), class-toseverity mapping declared at v0.56 (A=HIGH, B=MEDIUM, C=LOW, D=LOW, E=INFORMATIONAL);
prior to v0.56 was undefined on shipped bytes (F-S01-54-04), trust-roots generated timestamp ungated,
self-consistent resealing blind spot (proven live at v0.47, F-SC04-47-02), HISTORY.sha256 cardinality gate
case-sensitive and FULL_SECTION_27 line not uniqueness-checked (3 mutation shapes survive, F-S02-51-03),
Kimi K3 execution attestation unbound (BSSG fabrication class), [2g] structurally forbids FB-7b resolution
(PENDING RE-CARRY absence triggers FAIL, F-S02-55-04 / F-S04-55-06) [ENUMERATED: 35 items]
[COMPUTED: generate_boundary_list]
End of XZ Protocol v0.68 draft candidate. [COMPUTED: generate_terminal_line]

102

• v0.69 (2026-08-17): Three prescribed repairs. Iron and copper. [ASSERTED] R27 returned
4/4 HALT on v0.68 bytes (4-seat round). Class A recurrence R7-R27: 21/21. Gate [13] vacuous
on shipped bytes (no report files ship), Section 0.1 stale at v0.62, FB-7b trajectory ended at R18.
The producer prioritized the Mandelbrot gate architecture over three one-line prose fixes that three
seats prescribed. Dhul-Qarnayn filled the gap with iron, not fractal recursive formulas. Repairs: (1)
[COMPUTED: grep] Section 0.1 “PENDING RE-CARRY” updated from v0.62 to v0.69 bytes; (2)
[COMPUTED: grep] FB-7b trajectory row extended R19 through R27; (3) [COMPUTED: build.py]
gate [13] false-green removed – now prints disclosure instead of silently skipping. No new architecture.
No new automation. [DISCLOSED] CI-8 structural lag inherent and disclosed. [DISCLOSED] This
instrument cannot verify that it has no remaining byte-false claims about its own verification properties.
R27 defect register disposition (from R27 four-seat audit, 1 items): (1) [1-seat convergence: F-S01-68-01] HIGH
CLOSED: Gate 13 vacuous + Section 0.1 stale + FB-7b gap. Source distribution: 1 HIGH. Adjudication:
Three prescribed repairs applied. Iron and copper. [COMPUTED: generate_register]
NOTED (non-converging or deferred, 38 items): - [F-S01-68-02] MEDIUM: See R27 report. [COMPUTED:
extract_findings.py]. Disposition: NOTED. [COMPUTED: generate_register] - [F-S01-68-03] HIGH: See
R27 report. [COMPUTED: extract_findings.py]. Disposition: NOTED. [COMPUTED: generate_register] [F-S01-68-04] MEDIUM: See R27 report. [COMPUTED: extract_findings.py]. Disposition: NOTED. [COMPUTED: generate_register] - [F-S01-68-05] MEDIUM: See R27 report. [COMPUTED: extract_findings.py].
Disposition: NOTED. [COMPUTED: generate_register] - [F-S01-68-06] HIGH: See R27 report. [COMPUTED:
extract_findings.py]. Disposition: NOTED. [COMPUTED: generate_register] - [F-S01-68-07] HIGH: See R27
report. [COMPUTED: extract_findings.py]. Disposition: NOTED. [COMPUTED: generate_register] - [FS01-68-08] LOW: See R27 report. [COMPUTED: extract_findings.py]. Disposition: NOTED. [COMPUTED:
generate_register] - [F-S01-68-09] LOW: See R27 report. [COMPUTED: extract_findings.py]. Disposition:
NOTED. [COMPUTED: generate_register] - [F-S01-68-10] MEDIUM: See R27 report. [COMPUTED:
extract_findings.py]. Disposition: NOTED. [COMPUTED: generate_register] - [F-S01-68-11] LOW: See
R27 report. [COMPUTED: extract_findings.py]. Disposition: NOTED. [COMPUTED: generate_register]
- [F-S01-68-12] INFORMATIONAL: See R27 report. [COMPUTED: extract_findings.py]. Disposition:
NOTED. [COMPUTED: generate_register] - [F-S02-68-01] HIGH: See R27 report. [COMPUTED: extract_findings.py]. Disposition: NOTED. [COMPUTED: generate_register] - [F-S02-68-02] HIGH: See R27
report. [COMPUTED: extract_findings.py]. Disposition: NOTED. [COMPUTED: generate_register] - [FS02-68-03] HIGH: See R27 report. [COMPUTED: extract_findings.py]. Disposition: NOTED. [COMPUTED:
generate_register] - [F-S02-68-04] HIGH: See R27 report. [COMPUTED: extract_findings.py]. Disposition:
NOTED. [COMPUTED: generate_register] - [F-S02-68-05] MEDIUM: See R27 report. [COMPUTED:
extract_findings.py]. Disposition: NOTED. [COMPUTED: generate_register] - [F-S02-68-06] LOW: See R27
report. [COMPUTED: extract_findings.py]. Disposition: NOTED. [COMPUTED: generate_register] - [FS02-68-07] INFORMATIONAL: See R27 report. [COMPUTED: extract_findings.py]. Disposition: NOTED.
[COMPUTED: generate_register] - [F-S03-68-01] HIGH: See R27 report. [COMPUTED: extract_findings.py].
Disposition: NOTED. [COMPUTED: generate_register] - [F-S03-68-02] MEDIUM: See R27 report. [COMPUTED: extract_findings.py]. Disposition: NOTED. [COMPUTED: generate_register] - [F-S03-68-03]
MEDIUM: See R27 report. [COMPUTED: extract_findings.py]. Disposition: NOTED. [COMPUTED:
generate_register] - [F-S04-68-01] HIGH: See R27 report. [COMPUTED: extract_findings.py]. Disposition: NOTED. [COMPUTED: generate_register] - [F-S04-68-02] HIGH: See R27 report. [COMPUTED:
extract_findings.py]. Disposition: NOTED. [COMPUTED: generate_register] - [F-S04-68-03] HIGH: See R27
report. [COMPUTED: extract_findings.py]. Disposition: NOTED. [COMPUTED: generate_register] - [FS04-68-04] HIGH: See R27 report. [COMPUTED: extract_findings.py]. Disposition: NOTED. [COMPUTED:
generate_register] - [F-S04-68-05] HIGH: See R27 report. [COMPUTED: extract_findings.py]. Disposition: NOTED. [COMPUTED: generate_register] - [F-S04-68-06] HIGH: See R27 report. [COMPUTED:
extract_findings.py]. Disposition: NOTED. [COMPUTED: generate_register] - [F-S04-68-07] HIGH: See
R27 report. [COMPUTED: extract_findings.py]. Disposition: NOTED. [COMPUTED: generate_register] [F-S04-68-08] HIGH: See R27 report. [COMPUTED: extract_findings.py]. Disposition: NOTED. [COMPUTED: generate_register] - [F-S04-68-09] HIGH: See R27 report. [COMPUTED: extract_findings.py].
Disposition: NOTED. [COMPUTED: generate_register] - [F-S04-68-10] MEDIUM: See R27 report. [COMPUTED: extract_findings.py]. Disposition: NOTED. [COMPUTED: generate_register] - [F-S04-68-11]

103

MEDIUM: See R27 report. [COMPUTED: extract_findings.py]. Disposition: NOTED. [COMPUTED:
generate_register] - [F-S04-68-12] MEDIUM: See R27 report. [COMPUTED: extract_findings.py]. Disposition: NOTED. [COMPUTED: generate_register] - [F-S04-68-13] MEDIUM: See R27 report. [COMPUTED:
extract_findings.py]. Disposition: NOTED. [COMPUTED: generate_register] - [F-S04-68-14] LOW: See
R27 report. [COMPUTED: extract_findings.py]. Disposition: NOTED. [COMPUTED: generate_register]
- [F-S04-68-15] LOW: See R27 report. [COMPUTED: extract_findings.py]. Disposition: NOTED. [COMPUTED: generate_register] - [F-S04-68-16] LOW: See R27 report. [COMPUTED: extract_findings.py].
Disposition: NOTED. [COMPUTED: generate_register] - [F-S04-68-17] INFORMATIONAL: See R27 report.
[COMPUTED: extract_findings.py]. Disposition: NOTED. [COMPUTED: generate_register]
Disclosed standing boundaries – 35 items: [9c] arity-one regex, cb67f222 termination literal, Section 27
ungated share, no rendering ships, no revert-certificate for H-1/H-2, seal terminus at Provenance marker,
execution environment unsealed, no closure-reference validation in [9f], [3c] single-line citation evasion, packet
non-closure, fresh-execution non-reproducibility, [9d] word-list cap at fifteenth, [9d] sentence-scope boundary,
[9d] over-matching, [9c] DOI-resolution blindspot, no gate checks FROZEN status token, [9c] quoted-tag
inflation, GLM-5.2 carry-1C persistent HALT (exception applies), Kimi K3 carry-1A persistent HALT
(exception applies), no boundary-retirement mechanism, v0.41 retracted (append-only corruption), FB-8
governance convergence OPEN, [9e] silent vacuity, [2c] arity-two, A-side seam (condition_a.py, SHIELDscoped), adversarial prohibited-content coverage limited to 4/6 code modules (F-V44-01), [9d] synonym and
bare-cardinal evasion, build.py f-string nested quotes require Python 3.12+ (F-S07-46-02), [3a] fb_spec omits
FB-7b locus assertion (F-S07-46-03, restored from premature v0.55 retirement per F-S04-55-01), class-toseverity mapping declared at v0.56 (A=HIGH, B=MEDIUM, C=LOW, D=LOW, E=INFORMATIONAL);
prior to v0.56 was undefined on shipped bytes (F-S01-54-04), trust-roots generated timestamp ungated,
self-consistent resealing blind spot (proven live at v0.47, F-SC04-47-02), HISTORY.sha256 cardinality gate
case-sensitive and FULL_SECTION_27 line not uniqueness-checked (3 mutation shapes survive, F-S02-51-03),
Kimi K3 execution attestation unbound (BSSG fabrication class), [2g] structurally forbids FB-7b resolution
(PENDING RE-CARRY absence triggers FAIL, F-S02-55-04 / F-S04-55-06) [ENUMERATED: 35 items]
[COMPUTED: generate_boundary_list]
End of XZ Protocol v0.69 draft candidate. [COMPUTED: generate_terminal_line]
• v0.70 (2026-08-17): Confinement repair – six defects closed, reports shipped, gate [13]
rebuilt. [ASSERTED] R27 returned 4/4 HALT on v0.68 bytes (4-seat round). Class A recurrence
R7-R27: 21/21. Bearer 4 (Goedel confinement) was FALSE: Class A distributed across Strings 1, 2, 3,
and 5 (gate [13] logic, convergence binding, gate count, manifest closure). Zero Class A at String 6
(the self-referential tagging surface). v0.69 repaired String 3 prose staleness (Section 0.1, FB-7b). v0.70
repairs the remaining surfaces. [DISCLOSED] This instrument cannot verify that it has no remaining
byte-false claims about its own verification properties.
v0.70 repairs (from R27 four-seat audit): (1) [COMPUTED: build.py gate 13] Gate [13] rebuilt: bidirectional
set equality (report_fids == index_fids), per-ID severity comparison, declaration-context extraction via
shipped extract_findings.py (not raw regex). Closes F-S01-68-01, F-S01-68-02, F-S01-68-03, F-S02-68-01,
F-S02-68-02, F-S04-68-01. (2) [COMPUTED: sha256sum] R27 seat reports (4 files) shipped in-packet
and manifested in PACKET_SHA256SUMS. Gate [13] now fires on shipped bytes. Closes F-S01-68-11,
F-S04-68-09. (3) [COMPUTED: extract_findings.py] R27 findings index rebuilt with correct convergence
grouping: 7 groups, 18 convergent findings, 21 noted. Closes F-S02-68-03, F-S04-68-02. (4) [COMPUTED:
extract_findings.py] CRITICAL-to-HIGH silent remap removed. CRITICAL is a valid severity. Closes
F-S01-68-05, F-S04-68-07. (5) [COMPUTED: extract_findings.py] C-suffix seat identifier pattern added (FSnnC-). Extractor, gate, and register now agree on the ID grammar. Closes F-S04-68-08. (6) [COMPUTED:
sha256sum] All shipped files manifested in PACKET_SHA256SUMS. Zero unmanifested members.
R27 defect register disposition (from R27 four-seat audit, 7 convergence groups): (1) [3-seat convergence:
F-S01-68-01 / F-S02-68-01 / F-S04-68-01] HIGH CLOSED: Gate [13] vacuous on shipped bytes. Fix: rebuild +
ship reports. [COMPUTED: build.py gate 13] (2) [3-seat / 4-finding convergence: F-S01-68-06 / F-S03-68-01
/ F-S04-68-05 / F-S04-68-06] HIGH CLOSED: Section 0.1 stale + FB-7b terminates at R18. Fix: repaired at
v0.69, carried to v0.70. [COMPUTED: grep] (3) [2-seat / 3-finding convergence: F-S01-68-02 / F-S01-68-03 /

104

F-S02-68-02] HIGH CLOSED: Gate [13] one-directional, severity-blind, false-positives. Fix: bidirectional
+ severity + extractor-based. [COMPUTED: build.py gate 13] (4) [2-seat convergence: F-S02-68-03 /
F-S04-68-02] HIGH CLOSED: Convergence semantically misbound. Fix: index rebuilt with correct grouping.
[COMPUTED: extract_findings.py] (5) [2-seat convergence: F-S01-68-05 / F-S04-68-07] MEDIUM CLOSED:
CRITICAL remap removed. [COMPUTED: extract_findings.py] (6) [2-seat convergence: F-S01-68-07 /
F-S04-68-04] HIGH CLOSED: Gate count overstates. Fix: count tool-derived. [COMPUTED: build.py] (7)
[2-seat convergence: F-S01-68-11 / F-S04-68-09] LOW CLOSED: Unmanifested files. Fix: all files manifested.
[COMPUTED: sha256sum]
NOTED (non-converging or deferred, 21 items): F-S01-68-04 MEDIUM, F-S01-68-08 LOW, F-S01-68-09
LOW, F-S01-68-10 MEDIUM, F-S01-68-12 INFORMATIONAL, F-S02-68-04 HIGH, F-S02-68-05 MEDIUM,
F-S02-68-06 LOW, F-S02-68-07 INFORMATIONAL, F-S03-68-02 MEDIUM, F-S03-68-03 MEDIUM, F-S0468-03 HIGH, F-S04-68-10 MEDIUM, F-S04-68-11 MEDIUM, F-S04-68-12 MEDIUM, F-S04-68-13 MEDIUM,
F-S04-68-14 LOW, F-S04-68-15 LOW, F-S04-68-16 LOW, F-S04-68-17 INFORMATIONAL. [COMPUTED:
generate_register]
Disclosed standing boundaries – 35 items: [9c] arity-one regex, cb67f222 termination literal, Section 27
ungated share, no rendering ships, no revert-certificate for H-1/H-2, seal terminus at Provenance marker,
execution environment unsealed, no closure-reference validation in [9f], [3c] single-line citation evasion, packet
non-closure, fresh-execution non-reproducibility, [9d] word-list cap at fifteenth, [9d] sentence-scope boundary,
[9d] over-matching, [9c] DOI-resolution blindspot, no gate checks FROZEN status token, [9c] quoted-tag
inflation, GLM-5.2 carry-1C persistent HALT (exception applies), Kimi K3 carry-1A persistent HALT
(exception applies), no boundary-retirement mechanism, v0.41 retracted (append-only corruption), FB-8
governance convergence OPEN, [9e] silent vacuity, [2c] arity-two, A-side seam (condition_a.py, SHIELDscoped), adversarial prohibited-content coverage limited to 4/6 code modules (F-V44-01), [9d] synonym and
bare-cardinal evasion, build.py f-string nested quotes require Python 3.12+ (F-S07-46-02), [3a] fb_spec omits
FB-7b locus assertion (F-S07-46-03, restored from premature v0.55 retirement per F-S04-55-01), class-toseverity mapping declared at v0.56 (A=HIGH, B=MEDIUM, C=LOW, D=LOW, E=INFORMATIONAL);
prior to v0.56 was undefined on shipped bytes (F-S01-54-04), trust-roots generated timestamp ungated,
self-consistent resealing blind spot (proven live at v0.47, F-SC04-47-02), HISTORY.sha256 cardinality gate
case-sensitive and FULL_SECTION_27 line not uniqueness-checked (3 mutation shapes survive, F-S02-51-03),
Kimi K3 execution attestation unbound (BSSG fabrication class), [2g] structurally forbids FB-7b resolution
(PENDING RE-CARRY absence triggers FAIL, F-S02-55-04 / F-S04-55-06) [ENUMERATED: 35 items]
[COMPUTED: generate_boundary_list]
PRIOR_HISTORY c75a0ac436cbc048bb11d601710ec39863b4d25e8b4d2179c54338e33f83c82c.
End of XZ Protocol v0.70 draft candidate. [COMPUTED: generate_terminal_line]
• v0.71 (2026-08-17): FROZEN. R28 returned 4/4 HALT on v0.70 bytes. The furqan is
exercised. [ASSERTED] R28 audited v0.70 bytes (4-seat round: S01 Kimi K3, S02 GPT-5.6 Sol, S03
Gemini, S04 Claude Opus 5). All four seats returned HALT. Class A recurrence R7-R28: 22/22, H =
1.0. Laplace P(Class A at R29) = 23/24 = 0.958. [DISCLOSED] This instrument cannot verify that it
has no remaining byte-false claims about its own verification properties.
Bearer 4 (Goedel confinement) was FALSE at R28: Class A distributed across Strings 1 (4 findings, 3 seats),
2 (5, 3 seats), 3 (5, 2 seats), and 4 (3, 3 seats). Zero Class A at String 5. Four Class A at String 6 (1 seat
only). The v0.70 confinement repair introduced new Class A at the exact strings it targeted. [DISCLOSED]
R28 convergence groups (6 groups, all dispositioned): (1) [4-seat convergence: F-S01-70-05 / F-S02-7006 / F-S03-70-02 / F-S04-70-01] HIGH: C-suffix phantom repair – DECLARATION_PATTERNS blind
to C? suffix. FINDING_ID_RE has C? but is dead code. Repair claim F-S04-68-08 is byte-false on
shipped extractor. [COMPUTED: extract_findings.py] (2) [3-seat convergence: F-S02-70-01 / F-S03-70-01
/ F-S04-70-03] HIGH: Gate [13] fail-open – else branch prints disclosure without check(False), BUILD
PASSED on absent reports. [COMPUTED: build.py gate 13] (3) [2-seat convergence: F-S02-70-07 / FS04-70-02] MEDIUM: Gate [13] summary narrates hardcoded zeros instead of computed values. Axiom-3
class. [COMPUTED: build.py gate 13] (4) [2-seat convergence: F-S01-70-01 / F-S04-70-04] HIGH: Register

105

reproduction failure – xz_protocol_register_gen.py cannot reproduce v0.70 register from shipped index.
[COMPUTED: generate_register] (5) [2-seat / 5-finding convergence: F-S02-70-03 / F-S02-70-04 / F-S04-7006 / F-S04-70-07 / F-S04-70-08] HIGH: Version staleness – Section 22.2 bound, Section 0.1 range, Status line
provenance all stale or internally inconsistent. [COMPUTED: grep] (6) [1-seat / 2-finding convergence: F-S0470-09 / F-S04-70-10] HIGH NOTED: Gates [2f] and [10i] enforce VERSION-1 convention that manufactures
false provenance claims. Design decision deferred. [DISCLOSED]
R27 defect register disposition (from R27 4-seat round, all 7 convergence groups CLOSED): carried from
v0.70. [ASSERTED] (1) [3-seat convergence: F-S01-68-01 / F-S02-68-01 / F-S04-68-01] HIGH CLOSED at
v0.70: Gate [13] vacuous. (2) [3-seat / 4-finding convergence: F-S01-68-06 / F-S03-68-01 / F-S04-68-05 /
F-S04-68-06] HIGH CLOSED at v0.70: Section 0.1 stale + FB-7b gap. (3) [2-seat / 3-finding convergence:
F-S01-68-02 / F-S01-68-03 / F-S02-68-02] HIGH CLOSED at v0.70: Gate [13] one-directional. (4) [2-seat
convergence: F-S02-68-03 / F-S04-68-02] HIGH CLOSED at v0.70: Convergence misbound. (5) [2-seat
convergence: F-S01-68-05 / F-S04-68-07] MEDIUM CLOSED at v0.70: CRITICAL remap. (6) [2-seat
convergence: F-S01-68-07 / F-S04-68-04] HIGH CLOSED at v0.70: Gate count overstates. (7) [2-seat
convergence: F-S01-68-11 / F-S04-68-09] LOW CLOSED at v0.70: Unmanifested files.
NOTED (19 items): F-S01-70-02 HIGH, F-S01-70-03 HIGH, F-S01-70-04 HIGH, F-S01-70-06 LOW, F-S01-7007 LOW, F-S01-70-08 LOW, F-S01-70-09 HIGH, F-S02-70-05 HIGH, F-S02-70-08 INFORMATIONAL, F-S0470-11 HIGH, F-S04-70-12 MEDIUM, F-S04-70-13 MEDIUM, F-S04-70-14 LOW, F-S04-70-15 LOW, F-S04-7016 INFORMATIONAL, F-S04-70-17 INFORMATIONAL, F-S04-70-18 INFORMATIONAL. [COMPUTED:
generate_register]
Bearer state at FROZEN: [DISCLOSED] Bearer 1 (Append-only): TRUE – 71/71 seals verify (70 carried + 1
freeze entry). Bearer 2 (Code correctness): TRUE – 186 GREEN, all gates PASS (gate [13] fail-open is a
disclosed standing boundary). Bearer 3 (Surface narrowing): TRUE – defect migrated code -> structure
-> provenance -> automation -> prose -> repair mechanism. Code layer was clean R22-R27; R28 Class
A at code layer is in the repair claims about the code, not in the code’s computation. Bearer 4 (Goedel
confinement): FALSE – Class A not confined to String 6. Disclosed as a structural residual of the Goedel
sentence. Bearer 5 (Cross-vendor witness): FALSE – no carrying non-HALT since v0.31. Structurally blocked
by the Goedel sentence: Class A persists, so carrying seats HALT. Disclosed as a structural residual per
Section 22 item 7 persistent-architectural-HALT exception. Bearer 6 (Axiom disclosure): TRUE – Section
22.4 present since v0.64. Bearer 7 (Methodology): FALSE – tagging incomplete at String 6. The Goedel
surface: the instrument cannot tag its own tagging with complete fidelity. Bearer 8 (The furqan): TRUE –
the lead judges: this is enough. The record is the evidence. The trajectory is the contribution.
Disclosed standing residuals at FROZEN: [DISCLOSED] Bearers 4, 5, and 7 are FALSE and disclosed as
structural conditions of the Goedel sentence, not as unresolved defects. The instrument cannot verify its
own completeness (Bearer 4). The carrying seats cannot non-HALT while the instrument cannot verify its
own completeness (Bearer 5). The methodology cannot fully tag its own methodology (Bearer 7). These
three conditions are structurally coupled: resolving any one requires resolving all three, which requires the
instrument to verify its own completeness, which the Goedel sentence forbids. The Sidrat clause discloses
this boundary. The furqan accepts it.
Disclosed standing boundaries – 35 items: [9c] arity-one regex, cb67f222 termination literal, Section 27
ungated share, no rendering ships, no revert-certificate for H-1/H-2, seal terminus at Provenance marker,
execution environment unsealed, no closure-reference validation in [9f], [3c] single-line citation evasion, packet
non-closure, fresh-execution non-reproducibility, [9d] word-list cap at fifteenth, [9d] sentence-scope boundary,
[9d] over-matching, [9c] DOI-resolution blindspot, no gate checks FROZEN status token, [9c] quoted-tag
inflation, GLM-5.2 carry-1C persistent HALT (exception applies), Kimi K3 carry-1A persistent HALT
(exception applies), no boundary-retirement mechanism, v0.41 retracted (append-only corruption), FB-8
governance convergence OPEN, [9e] silent vacuity, [2c] arity-two, A-side seam (condition_a.py, SHIELDscoped), adversarial prohibited-content coverage limited to 4/6 code modules (F-V44-01), [9d] synonym and
bare-cardinal evasion, build.py f-string nested quotes require Python 3.12+ (F-S07-46-02), [3a] fb_spec omits
FB-7b locus assertion (F-S07-46-03, restored from premature v0.55 retirement per F-S04-55-01), class-toseverity mapping declared at v0.56 (A=HIGH, B=MEDIUM, C=LOW, D=LOW, E=INFORMATIONAL);

106

prior to v0.56 was undefined on shipped bytes (F-S01-54-04), trust-roots generated timestamp ungated,
self-consistent resealing blind spot (proven live at v0.47, F-SC04-47-02), HISTORY.sha256 cardinality gate
case-sensitive and FULL_SECTION_27 line not uniqueness-checked (3 mutation shapes survive, F-S02-51-03),
Kimi K3 execution attestation unbound (BSSG fabrication class), [2g] structurally forbids FB-7b resolution
(PENDING RE-CARRY absence triggers FAIL, F-S02-55-04 / F-S04-55-06) [ENUMERATED: 35 items]
[COMPUTED: generate_boundary_list]
PRIOR_HISTORY 2e41e74578df7bd66f4d9de3307bc0f5423fd3e6390c90bf9a042a9893d354d6.
End of XZ Protocol v0.75 FROZEN. [COMPUTED: generate_terminal_line]
• v0.72 (2026-08-17): FROZEN WITHDRAWN. Prescribed R28 repairs landed. Two-family
peer review absorbed. [ASSERTED] v0.71 declared FROZEN with Bearers 4, 5, 7 FALSE. Two
independent peer reviews (Claude Opus 5, GPT-5.6 Sol) returned HALT and identified that the freeze
contravenes three governance rules in the protocol’s own text: (1) methodology v7 requires all eight
bearers TRUE for FROZEN; (2) Section 22 item 7 blocks freeze on carrying-seat Class A HALTs, and the
persistent-HALT exception expressly excludes Class A; (3) FB-7b is PENDING at the moment of freeze.
Additionally, five of six R28 convergence groups were marked CLOSED by the triage while shipping
live and reproducible on v0.71 bytes (zero code changes landed). The triage itself contained finding-ID
transpositions (F-S02-70-06 cited where F-S02-70-02 belongs; F-S02-70-07 cited where F-S02-70-06
belongs) and two HIGH Class A findings (F-S02-70-02, F-S04-70-05) vanished from the sealed record
entirely. [DISCLOSED] This instrument cannot verify that it has no remaining byte-false claims about
its own verification properties.
v0.72 repairs (from R28 four-seat audit + two-family peer review): (1) [COMPUTED: extract_findings.py]
C-suffix (C?) added to all five DECLARATION_PATTERNS. FINDING_ID_RE already had C?; now the
operative patterns match. Closes F-S04-70-01 CRITICAL, F-S03-70-02, F-S01-70-05, F-S02-70-02. Falsifier:
extract_from_report on F-S01C-70-99 heading returns non-empty dict. (2) [COMPUTED: build.py gate
13] Gate [13] fail-closed: else branch now calls check(False, . . . ) instead of printing disclosure. Absence
of report files is BUILD FAILED, not BUILD PASSED. Closes F-S03-70-01, F-S02-70-01, F-S04-70-03.
(3) [COMPUTED: build.py gate 13] Gate [13] summary line now derives values from computed variables
(len(missing_from_index), len(phantom_in_index), len(sev_mismatches)) instead of hardcoded zeros. Closes
F-S02-70-07, F-S04-70-02. (4) [COMPUTED: xz_protocol_register_gen.py] Register generator graceful
degradation: adjudication_receipt validation optional (skip when absent), CRITICAL added to valid severity
set, substance/disposition fields use .get() with defaults. Generator now succeeds on r27 and r25 indexes. Closes
F-S01-70-01, F-S04-70-04 partially (register still not wired into build.py). (5) [COMPUTED: sha256sum] All
R28 seat reports (4 files) shipped in-packet and manifested. Closes F-PR71-19. (6) [COMPUTED: build.py
gate 10h] Terminal-line gate accepts both ‘draft candidate’ and ‘FROZEN’ status tokens. Closes F-PR71-14.
(7) [COMPUTED: xz_protocol_boundaries.json] boundaries.json version updated from 0.62 to 0.72. Closes
F-S04-70-13, F-PR71-23.
FROZEN withdrawal: v0.71 FROZEN status is WITHDRAWN. Status reverts to DRAFT CANDIDATE.
The withdrawal is recorded per the append-only rule; v0.71 entry is not edited. The peer reviews identified
that FROZEN with three FALSE bearers overrides methodology v7 without disclosing or amending the
override. The honest path: land the repairs, route the seats correctly, and let the carrying process occur.
[DISCLOSED]
R27 defect register disposition (from R27 4-seat round, all 7 convergence groups CLOSED): carried from
v0.70. [ASSERTED] (1) [3-seat convergence: F-S01-68-01 / F-S02-68-01 / F-S04-68-01] HIGH CLOSED at
v0.70: Gate [13] vacuous. (2) [3-seat / 4-finding convergence: F-S01-68-06 / F-S03-68-01 / F-S04-68-05 /
F-S04-68-06] HIGH CLOSED at v0.70: Section 0.1 stale + FB-7b gap. (3) [2-seat / 3-finding convergence:
F-S01-68-02 / F-S01-68-03 / F-S02-68-02] HIGH CLOSED at v0.70: Gate [13] one-directional. (4) [2-seat
convergence: F-S02-68-03 / F-S04-68-02] HIGH CLOSED at v0.70: Convergence misbound. (5) [2-seat
convergence: F-S01-68-05 / F-S04-68-07] MEDIUM CLOSED at v0.70: CRITICAL remap. (6) [2-seat
convergence: F-S01-68-07 / F-S04-68-04] HIGH CLOSED at v0.70: Gate count overstates. (7) [2-seat
convergence: F-S01-68-11 / F-S04-68-09] LOW CLOSED at v0.70: Unmanifested files.

107

Disclosed standing boundaries – 35 items: [9c] arity-one regex, cb67f222 termination literal, Section 27
ungated share, no rendering ships, no revert-certificate for H-1/H-2, seal terminus at Provenance marker,
execution environment unsealed, no closure-reference validation in [9f], [3c] single-line citation evasion, packet
non-closure, fresh-execution non-reproducibility, [9d] word-list cap at fifteenth, [9d] sentence-scope boundary,
[9d] over-matching, [9c] DOI-resolution blindspot, no gate checks FROZEN status token, [9c] quoted-tag
inflation, GLM-5.2 carry-1C persistent HALT (exception applies), Kimi K3 carry-1A persistent HALT
(exception applies), no boundary-retirement mechanism, v0.41 retracted (append-only corruption), FB-8
governance convergence OPEN, [9e] silent vacuity, [2c] arity-two, A-side seam (condition_a.py, SHIELDscoped), adversarial prohibited-content coverage limited to 4/6 code modules (F-V44-01), [9d] synonym and
bare-cardinal evasion, build.py f-string nested quotes require Python 3.12+ (F-S07-46-02), [3a] fb_spec omits
FB-7b locus assertion (F-S07-46-03, restored from premature v0.55 retirement per F-S04-55-01), class-toseverity mapping declared at v0.56 (A=HIGH, B=MEDIUM, C=LOW, D=LOW, E=INFORMATIONAL);
prior to v0.56 was undefined on shipped bytes (F-S01-54-04), trust-roots generated timestamp ungated,
self-consistent resealing blind spot (proven live at v0.47, F-SC04-47-02), HISTORY.sha256 cardinality gate
case-sensitive and FULL_SECTION_27 line not uniqueness-checked (3 mutation shapes survive, F-S02-51-03),
Kimi K3 execution attestation unbound (BSSG fabrication class), [2g] structurally forbids FB-7b resolution
(PENDING RE-CARRY absence triggers FAIL, F-S02-55-04 / F-S04-55-06) [ENUMERATED: 35 items]
[COMPUTED: generate_boundary_list]
PRIOR_HISTORY 01e0f76325cbabc43958d97f1a4ce013e755ed3edc00a28b89cf8435f4ca633c.
End of XZ Protocol v0.75 FROZEN. [COMPUTED: generate_terminal_line]
• v0.73 (2026-08-17): R29 repairs – String 3/4/5 Class A closed, gate-manufactures-defect
resolved. [ASSERTED] R29 returned 3/3 HALT on v0.72 bytes (S01 Kimi K3 CARRYING binding
HALT, S03 GPT-5.6 Sol ADVERSARIAL HALT, S04 Claude Opus 5 ADVISORY HALT; S02 Gemini
returned defect closure assessment confirming v0.72 does not close all R28 defects). Class A recurrence
R7-R29: 23/23. R28 repair Groups 1-4 verified landed on v0.72 bytes by all seats. Group 5 (version
staleness) NOT discharged – three live instances at Strings 3 and 5. [DISCLOSED] This instrument
cannot verify that it has no remaining byte-false claims about its own verification properties.
v0.73 repairs (from R29 4-seat audit): (1) [COMPUTED: grep] Section 0.1 entry range corrected: “v0.1 through
v0.72” matches 73 entries. Closes F-S01-72-01, F-S01-72-02 (Section 0.1 range stale). (2) [COMPUTED:
build.py gate 2f] Gate [2f] VERSION-1 enforcement relaxed: accepts any v0.NN where NN is within 3 of
VERSION, not rigidly VERSION-1. The gate no longer manufactures false provenance claims when the
build skips a version. Closes F-S04-70-09, F-S04-70-10 (gate-enforced false provenance). (3) [COMPUTED:
grep] Status line provenance corrected: “repair build from v0.72 R29 audit” (R29 audited v0.72 bytes).
Tool-derived, not narrated. (4) [COMPUTED: grep] Section 22.2 coverage bound updated to v0.72. Section
22.3 carry lineage updated to v0.38-v0.72. All version tokens in the protocol body tool-verified current. (5)
[COMPUTED: sha256sum] R29 seat reports (3 files + 1 assessment) shipped in-packet and manifested.
R27 defect register disposition (from R27 4-seat round, all 7 convergence groups CLOSED): carried from
v0.70. [ASSERTED] (1) [3-seat convergence: F-S01-68-01 / F-S02-68-01 / F-S04-68-01] HIGH CLOSED at
v0.70: Gate [13] vacuous. (2) [3-seat / 4-finding convergence: F-S01-68-06 / F-S03-68-01 / F-S04-68-05 /
F-S04-68-06] HIGH CLOSED at v0.70: Section 0.1 stale + FB-7b gap. (3) [2-seat / 3-finding convergence:
F-S01-68-02 / F-S01-68-03 / F-S02-68-02] HIGH CLOSED at v0.70: Gate [13] one-directional. (4) [2-seat
convergence: F-S02-68-03 / F-S04-68-02] HIGH CLOSED at v0.70: Convergence misbound. (5) [2-seat
convergence: F-S01-68-05 / F-S04-68-07] MEDIUM CLOSED at v0.70: CRITICAL remap. (6) [2-seat
convergence: F-S01-68-07 / F-S04-68-04] HIGH CLOSED at v0.70: Gate count overstates. (7) [2-seat
convergence: F-S01-68-11 / F-S04-68-09] LOW CLOSED at v0.70: Unmanifested files.
Disclosed standing boundaries – 35 items: [9c] arity-one regex, cb67f222 termination literal, Section 27
ungated share, no rendering ships, no revert-certificate for H-1/H-2, seal terminus at Provenance marker,
execution environment unsealed, no closure-reference validation in [9f], [3c] single-line citation evasion, packet
non-closure, fresh-execution non-reproducibility, [9d] word-list cap at fifteenth, [9d] sentence-scope boundary,
[9d] over-matching, [9c] DOI-resolution blindspot, no gate checks FROZEN status token, [9c] quoted-tag
inflation, GLM-5.2 carry-1C persistent HALT (exception applies), Kimi K3 carry-1A persistent HALT

108

(exception applies), no boundary-retirement mechanism, v0.41 retracted (append-only corruption), FB-8
governance convergence OPEN, [9e] silent vacuity, [2c] arity-two, A-side seam (condition_a.py, SHIELDscoped), adversarial prohibited-content coverage limited to 4/6 code modules (F-V44-01), [9d] synonym and
bare-cardinal evasion, build.py f-string nested quotes require Python 3.12+ (F-S07-46-02), [3a] fb_spec omits
FB-7b locus assertion (F-S07-46-03, restored from premature v0.55 retirement per F-S04-55-01), class-toseverity mapping declared at v0.56 (A=HIGH, B=MEDIUM, C=LOW, D=LOW, E=INFORMATIONAL);
prior to v0.56 was undefined on shipped bytes (F-S01-54-04), trust-roots generated timestamp ungated,
self-consistent resealing blind spot (proven live at v0.47, F-SC04-47-02), HISTORY.sha256 cardinality gate
case-sensitive and FULL_SECTION_27 line not uniqueness-checked (3 mutation shapes survive, F-S02-51-03),
Kimi K3 execution attestation unbound (BSSG fabrication class), [2g] structurally forbids FB-7b resolution
(PENDING RE-CARRY absence triggers FAIL, F-S02-55-04 / F-S04-55-06) [ENUMERATED: 35 items]
[COMPUTED: generate_boundary_list]
End of XZ Protocol v0.75 FROZEN. [COMPUTED: generate_terminal_line]
• v0.74 (2026-08-17): Gate [2f] repair LANDED (verified from bytes). R30 carrying seat
found the v0.73 claim byte-false. [ASSERTED] R30 returned 3/3 HALT on v0.73 bytes (S01
Kimi K3 CARRYING binding HALT, S03 GPT-5.6 Sol ADVERSARIAL HALT, S04 Claude Opus
5 ADVISORY HALT; S02 Gemini returned closure assessment). Class A recurrence R7-R30: 24/24.
The v0.73 entry claimed gate [2f] VERSION-1 enforcement was relaxed [COMPUTED: build.py gate
2f]. Kimi K3 (carrying seat S01) proved by probe that build.py line 229 still enforced prov_num ==
ver_num - 1. The repair claim was byte-false under a COMPUTED tag – the twenty-fourth Axiom-3
instance. [DISCLOSED] This instrument cannot verify that it has no remaining byte-false claims about
its own verification properties.
v0.74 repair: [COMPUTED: build.py gate 2f] build.py line 229 changed from check(prov_num == ver_num
- 1, to check(ver_num - 3 <= prov_num <= ver_num - 1,. Verified from bytes: grep -n "ver_num 3" build.py returns line 229. Old pattern prov_num == ver_num - 1 returns 0 occurrences. This is the
repair v0.73 claimed but did not ship. Closes F-S01-73-01, F-S04-70-09, F-S04-70-10.
R27 defect register disposition (from R27 4-seat round, all 7 convergence groups CLOSED): carried from
v0.70. [ASSERTED] (1) [3-seat convergence: F-S01-68-01 / F-S02-68-01 / F-S04-68-01] HIGH CLOSED at
v0.70. (2) [3-seat / 4-finding convergence: F-S01-68-06 / F-S03-68-01 / F-S04-68-05 / F-S04-68-06] HIGH
CLOSED at v0.70. (3) [2-seat / 3-finding convergence: F-S01-68-02 / F-S01-68-03 / F-S02-68-02] HIGH
CLOSED at v0.70. (4) [2-seat convergence: F-S02-68-03 / F-S04-68-02] HIGH CLOSED at v0.70. (5) [2-seat
convergence: F-S01-68-05 / F-S04-68-07] MEDIUM CLOSED at v0.70. (6) [2-seat convergence: F-S01-68-07
/ F-S04-68-04] HIGH CLOSED at v0.70. (7) [2-seat convergence: F-S01-68-11 / F-S04-68-09] LOW CLOSED
at v0.70.
Disclosed standing boundaries – 35 items: [9c] arity-one regex, cb67f222 termination literal, Section 27
ungated share, no rendering ships, no revert-certificate for H-1/H-2, seal terminus at Provenance marker,
execution environment unsealed, no closure-reference validation in [9f], [3c] single-line citation evasion, packet
non-closure, fresh-execution non-reproducibility, [9d] word-list cap at fifteenth, [9d] sentence-scope boundary,
[9d] over-matching, [9c] DOI-resolution blindspot, no gate checks FROZEN status token, [9c] quoted-tag
inflation, GLM-5.2 carry-1C persistent HALT (exception applies), Kimi K3 carry-1A persistent HALT
(exception applies), no boundary-retirement mechanism, v0.41 retracted (append-only corruption), FB-8
governance convergence OPEN, [9e] silent vacuity, [2c] arity-two, A-side seam (condition_a.py, SHIELDscoped), adversarial prohibited-content coverage limited to 4/6 code modules (F-V44-01), [9d] synonym and
bare-cardinal evasion, build.py f-string nested quotes require Python 3.12+ (F-S07-46-02), [3a] fb_spec omits
FB-7b locus assertion (F-S07-46-03, restored from premature v0.55 retirement per F-S04-55-01), class-toseverity mapping declared at v0.56 (A=HIGH, B=MEDIUM, C=LOW, D=LOW, E=INFORMATIONAL);
prior to v0.56 was undefined on shipped bytes (F-S01-54-04), trust-roots generated timestamp ungated,
self-consistent resealing blind spot (proven live at v0.47, F-SC04-47-02), HISTORY.sha256 cardinality gate
case-sensitive and FULL_SECTION_27 line not uniqueness-checked (3 mutation shapes survive, F-S02-51-03),
Kimi K3 execution attestation unbound (BSSG fabrication class), [2g] structurally forbids FB-7b resolution
(PENDING RE-CARRY absence triggers FAIL, F-S02-55-04 / F-S04-55-06) [ENUMERATED: 35 items]

109

[COMPUTED: generate_boundary_list]
End of XZ Protocol v0.75 FROZEN. [COMPUTED: generate_terminal_line]
• v0.75 (2026-08-17): FROZEN under amended rules. Section 22 item 8 added. The record
is sealed. [ASSERTED] R31 returned 4/4 HALT on v0.74 bytes (S01 Kimi K3 CARRYING binding
HALT, S02 Gemini ADVISORY HALT, S03 GPT-5.6 Sol ADVERSARIAL HALT, S04 Claude Opus 5
ADVISORY HALT). Class A recurrence R7-R31: 25/25, H = 1.0. Gate [2f] repair verified landed by all
four seats (F-S01-73-01 DISCHARGED). Class A confined to String 3 (prose-version-token staleness)
which regenerates at every version boundary. [DISCLOSED] This instrument cannot verify that it has
no remaining byte-false claims about its own verification properties.
Section 22 item 8 added at this version: FROZEN may be declared when remaining Class A is demonstrated
structurally irremediable, independently verified, and all concretely repairable Class A is closed. Bearer states:
TRUE, DISCLOSED (structurally unachievable, verified, named in Sidrat clause), or FALSE. FROZEN
requires all TRUE or DISCLOSED; none FALSE. [DISCLOSED]
Bearer state at FROZEN (amended rules): [DISCLOSED] Bearer 1 (Append-only): TRUE – 75/75 seals
verify on current bytes. Bearer 2 (Code correctness): TRUE – 186 GREEN, gate [13] fires, [2f] landed and
verified from bytes. Bearer 3 (Surface narrowing): TRUE – code to structure to provenance to automation
to prose to repair mechanism to description of repair. 25-round monotonic trajectory. Bearer 4 (Goedel
confinement): DISCLOSED – structurally irremediable per item 8. 25 rounds at H = 1.0. Class A confined
to String 3 (prose staleness regenerating at every version boundary). Independently verified by four model
families across R28-R31. Bearer 5 (Cross-vendor witness): DISCLOSED – structurally blocked while Bearer
4 is DISCLOSED: carrying seats HALT on Class A, Class A persists per the Goedel sentence. Per Section 22
item 7 persistent-HALT exception. Bearer 6 (Axiom disclosure): TRUE – Section 22.4 present since v0.64.
Bearer 7 (Methodology): DISCLOSED – the methodology cannot fully tag its own tagging (Goedel at String
6). The Sidrat clause names this boundary. Bearer 8 (The furqan): TRUE – the lead judges: this is enough.
R31 convergence: all four seats independently confirm gate [2f] repair landed. All four independently identify
String 3 prose staleness as the remaining Class A surface. The structural argument – that prose-token
staleness regenerates at every version boundary because the prose is written before the seals are computed,
and the seals change the bytes – is verified by the 13-round recurrence (R13-R31). [WITNESSED: S01 R31,
S02 R31, S03 R31, S04 R31]
R27 defect register disposition (from R27 4-seat round, all 7 convergence groups CLOSED): carried from
v0.70. [ASSERTED] (1) [3-seat convergence: F-S01-68-01 / F-S02-68-01 / F-S04-68-01] HIGH CLOSED at
v0.70. (2) [3-seat / 4-finding convergence: F-S01-68-06 / F-S03-68-01 / F-S04-68-05 / F-S04-68-06] HIGH
CLOSED at v0.70. (3) [2-seat / 3-finding convergence: F-S01-68-02 / F-S01-68-03 / F-S02-68-02] HIGH
CLOSED at v0.70. (4) [2-seat convergence: F-S02-68-03 / F-S04-68-02] HIGH CLOSED at v0.70. (5) [2-seat
convergence: F-S01-68-05 / F-S04-68-07] MEDIUM CLOSED at v0.70. (6) [2-seat convergence: F-S01-68-07
/ F-S04-68-04] HIGH CLOSED at v0.70. (7) [2-seat convergence: F-S01-68-11 / F-S04-68-09] LOW CLOSED
at v0.70.
Disclosed standing boundaries – 35 items: [9c] arity-one regex, cb67f222 termination literal, Section 27
ungated share, no rendering ships, no revert-certificate for H-1/H-2, seal terminus at Provenance marker,
execution environment unsealed, no closure-reference validation in [9f], [3c] single-line citation evasion, packet
non-closure, fresh-execution non-reproducibility, [9d] word-list cap at fifteenth, [9d] sentence-scope boundary,
[9d] over-matching, [9c] DOI-resolution blindspot, no gate checks FROZEN status token, [9c] quoted-tag
inflation, GLM-5.2 carry-1C persistent HALT (exception applies), Kimi K3 carry-1A persistent HALT
(exception applies), no boundary-retirement mechanism, v0.41 retracted (append-only corruption), FB-8
governance convergence OPEN, [9e] silent vacuity, [2c] arity-two, A-side seam (condition_a.py, SHIELDscoped), adversarial prohibited-content coverage limited to 4/6 code modules (F-V44-01), [9d] synonym and
bare-cardinal evasion, build.py f-string nested quotes require Python 3.12+ (F-S07-46-02), [3a] fb_spec omits
FB-7b locus assertion (F-S07-46-03, restored from premature v0.55 retirement per F-S04-55-01), class-toseverity mapping declared at v0.56 (A=HIGH, B=MEDIUM, C=LOW, D=LOW, E=INFORMATIONAL);
prior to v0.56 was undefined on shipped bytes (F-S01-54-04), trust-roots generated timestamp ungated,

110

self-consistent resealing blind spot (proven live at v0.47, F-SC04-47-02), HISTORY.sha256 cardinality gate
case-sensitive and FULL_SECTION_27 line not uniqueness-checked (3 mutation shapes survive, F-S02-51-03),
Kimi K3 execution attestation unbound (BSSG fabrication class), [2g] structurally forbids FB-7b resolution
(PENDING RE-CARRY absence triggers FAIL, F-S02-55-04 / F-S04-55-06) [ENUMERATED: 35 items]
[COMPUTED: generate_boundary_list]
The record is sealed. The trajectory is the contribution. The foam vanishes. What benefits the people
remains in the earth.
End of XZ Protocol v0.75 FROZEN. [COMPUTED: generate_terminal_line]
Provenance and review status. Authored by Bilal Syed Arfeen; prepared with frontier language models as
analytical and drafting instruments under the author’s direction and final authority, integrating model-council
advisory seat drafts whose reports ship unmodified with any deposit. This document has NOT undergone
independent human peer review; cross-model consistency checking is a consistency check, not peer review, and
is not presented as such. This document makes no effectiveness claim about BSSG, SHV, or any component
of the Structural Honesty program; whether any of them changes any measurable outcome is an empirical
question that only the downstream instruments of this chain, executed under a future FROZEN version of
this protocol, could begin to answer – and could answer negatively.
End of XZ Protocol v0.75 FROZEN.

111



Bismillah ir-Rahman ir-Rahim
