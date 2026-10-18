Bismillah ir-Rahman ir-Rahim

Bayyinah al-Amāna: Provenance Integrity for Public Open Data -Audit and Provenance Companion
Companion to: Bayyinah al-Amāna: Provenance Integrity for Public Open Data (the readerfacing note, v1.0; DOI 10.5281/zenodo.21446613). This ledger: DOI 10.5281/zenodo.21446618.
Governed by: Bayyinah, Portable Structural Honesty Verification for Public-Service Institutions
(the framework paper). Prepared under BayyinahEnterprise audit methodology (PMD v1.2,
Audit Framework v3.0). Mirrors note state v1.0, the canonical converged release (three
consecutive qualifying passes, F-AM-R1/R2/R3; the consecutive qualifying-PASS count is
THREE, the gate met and confirmed clean at F-AM-R3 with the rotation gap closed). See the
authoritative Current State block.
Finding namespace: F-AM (al-Amāna). Severities are UPPERCASE (CRITICAL, HIGH,
MEDIUM, LOW, INFO). Findings use the six-element format (identifier, severity, locus,
substance as surface-versus-substrate divergence, disposition, cross-reference).

Current State (authoritative, as of v1.0)
•

•

•

Artifact state: v1.0 canonical converged release. Reader note plus this companion and
the reproduction package (Bayyinah_ProvenanceIntegrity_ReproPackage),
whose frozen capture snapshot/provenance_capture.json has SHA-256
c49488723819d272beb6445435c724dfbf2050a363baf89d09a333a993e18201.
The package verifies its hash, reproduces all four checks offline, re-pulls the live
data.ny.gov endpoints to detect drift, and self-tests its comparator (42 captured values,
zero missed).
Consecutive qualifying-PASS count (single operational counter): THREE. Three
qualifying rounds have occurred (F-AM-R1, F-AM-R2, F-AM-R3), each with at least
two qualifying non-producer members returning zero CRITICAL and zero HIGH; Claude
quarantined throughout. The two-consecutive-pass gate under Standing Rule 7 was MET
at F-AM-R2 and CONFIRMED CLEAN at F-AM-R3 on the corrected artifact. The two
earlier caveats are now resolved: (1) the not-clean converging round -- F-AM-R3 reaudited the corrected artifact and the only finding was a single LOW wording nuance (FAM-R3-001, since absorbed into v1.0); and (2) the weak rotation -- F-AM-R3's passbearing set includes GPT 5.4, a qualifying member new relative to the R1/R2 clean pair,
this time successfully and cleanly isolated, closing the rotation gap. One honest caveat
remains: the gate is met inside this producer-defined governance framework, while the
externally-verifiable result -- every figure reproduces exactly from live data.ny.gov under
the exact fiscal-window filter, and the comparator is tamper-evident under hash-gate
defeat -- holds independently of the framework. Any CRITICAL or HIGH in a future
round resets the count to zero.
Independent audit history: three rounds. F-AM-R1 (GPT 5.5 + Gemini 3.1 Pro
qualifying) QUALIFYING PASS, 0C/0H, 1 MEDIUM + 2 LOW absorbed in v0.2. FAM-R2 (GPT 5.5 + Gemini 3.1 Pro clean pair; GPT 5.4 rotated-in but INCOMPLETE on
isolation) QUALIFYING PASS, 0C/0H, 1 MEDIUM + 2 LOW absorbed in v0.3. F-AMR3 confirming round (clean pass-bearing pair GPT 5.5 + GPT 5.4, the latter new and this

•

•

•

time cleanly isolated; Gemini 3.1 Pro PASS but Step-4 recompute nonconforming via a
broad-date-range filter mismatch, not counted in the clean pair; Claude advisory)
QUALIFYING PASS, 0C/0H, one LOW (F-AM-R3-001) absorbed into v1.0. Counter to
THREE; rotation gap closed.
Verified substantive claims (Tier 1 and Tier 2, reproduced live and frozen):
–
Provenance: gpsc-qqsz declares provenance community ("MTA Procurement
Report (All)"); twsw-2mqa declares provenance official ("MTA Procurements:
Beginning 2018"). Both on data.ny.gov.
–
Community-vs-official divergence by fiscal year: FY2023 identical (both 12,114
records, $63,569,204,049.36); FY2024 divergent by 70 records and
$58,072,427.23 (0.5103% count, 0.0891% face; gpsc 13,718/$65,189,755,228.64,
twsw 13,648/$65,131,682,801.41); FY2022 identical in row count (both 12,156)
but divergent by $0.75 in summed face value ($54,698,007,774.69 vs
$54,698,007,775.44).
–
Freshness (row-level :created_at, uniform per window): community view
created 2025-12-01 (335 / 701 / 1066 days after FY2024 / FY2023 / FY2022
close); official dataset created 2026-04-01 (456 / 822 / 1187 days after close).
Uniform creation timestamps across each closed year indicate the window was
instantiated in a single post-close batch, detectable from a single live pull; this is
consistent with a wholesale republish and equally with a first-time bulk load,
which the single-pull timestamp does not distinguish (F-AM-R1-S-001).
–
Schema: community view 23 fields, official 32; 16 official-only, 7 communityonly.
Refusal (Tier 3): the artifact does not judge whether any divergence, republish, or edit
was legitimate, authorized, or improper; it detects and quantifies and stops. This refusal is
enforced in the reader note (Sections 3 and 5.4) and printed by the reproduction tool on
every run.
Deposit action (CLOSED at v1.0): DOIs assigned -- reader note
10.5281/zenodo.21446613, this ledger 10.5281/zenodo.21446618. The reproduction
package is deposited under an immutable DOI alongside this ledger at
10.5281/zenodo.21446618; the reader note Section 9 points to it there.

Convergence machinery (reused from the converged sibling note)
The audit apparatus is the one that carried the Public-Ledger Allocation and AsymmetricMeasure Audits to convergence: a rotated Perplexity Model Council of fresh, memoryless
instances; the Claude producing lineage quarantined and excluded from the convergence-bearing
verdict; at least two qualifying non-producer members per round; mandatory executed
reproduction against the bundled package (a comparison of stated numbers against a brief is
never a PASS); exact expected values supplied in the brief; and a widened pre-delivery
mechanical check across all current-status loci (version, counter, round count) distinguishing
current status from append-only history. A round is a qualifying PASS only with zero
CRITICAL and zero HIGH from at least two qualifying members with documented executed
reproduction. Any HIGH or CRITICAL resets the counter to zero.

Section 14.5 (append-only immutability)
Superseded text is preserved and annotated, never edited in place. Historical ledger and appendix
references to past states are correct-in-context and are not changed; only the Current State block
above and the running counter reflect the present. Each audit round is recorded as a dated
append-only appendix below.

Pre-audit producer record (v0.1 baseline)
These are producer-side records establishing the v0.1 baseline. None is an independent audit
finding; the counter remains ZERO.
•

•

•

P3-B1 (viability gate, PASSED). Phase 0 confirmed live against both portals: dataset
provenance is exposed in metadata; the dedicated /revisions.json endpoint is NOT
public (HTTP 404); and the SODA API publicly exposes per-row
:created_at/:updated_at system columns, a stronger freshness signal than the
revision endpoint would have been. The primary freshness method is therefore row-level
system timestamps from a single live pull, with dated-snapshot hash comparison retained
as confirmatory. Independently reproduced by the producer against data.ny.gov.
P3-B2 (scope refinement absorbed). An external informal fact-check ran live checks
against the endpoints and confirmed the provenance classifications and the rowtimestamp freshness signal, and recommended promoting the row-timestamp method
from fallback to primary. The producer independently reproduced each claim
(provenance community/official; /revisions.json 404; uniform :created_at)
before absorbing it into the scope and the reproduction package. Recorded as an informal
external confirmation, explicitly non-qualifying and not an audit round.
P3-B3 (value-level divergence surfaced and display corrected). During package
construction the FY2022 face divergence of $0.75 at identical row count was initially
masked by a percentage display rounding to 0.0000% while the comparator correctly
tagged it DIVERGENT. The producer inspected the raw captured values, confirmed the
difference is real and stable (the live re-pull reproduces it), and corrected the display to
show absolute row and dollar deltas. The finding is retained in the reader note Section 5.1
as the sharpest illustration of the method's resolution.

Audit rounds
Appended below as dated append-only appendices: F-AM-R1 (v0.1 -> v0.2) and F-AM-R2 (v0.2
-> v0.3). [Superseded per Section 14.5: the original 'None yet' placeholder is retained here in
spirit only; the round appendices follow.]
Appendix: v0.1 -> v0.2 amendments (first round F-AM-R1, rotated Model Council:
QUALIFYING PASS, count to ONE) [new in this artifact]
The round. First independent cross-instance audit of the v0.1 artifact, package bundled, rotated
membership: qualifying members GPT 5.5 (OpenAI) and Gemini 3.1 Pro (Google); Claude Opus
4.8 (Anthropic) quarantined advisory-only. Both qualifying members executed all six protocol
steps with pasted outputs, independently recomputed with their own code (without importing the
supplied functions), demonstrated the adversarial mutate-and-rehash returning comparator

DRIFT (exit 2), and each returned 0 CRITICAL, 0 HIGH. Synthesized qualifying verdict:
QUALIFYING PASS. Per the counter rule the consecutive qualifying-PASS count moves from
ZERO to ONE; this is the first of the two consecutive passes convergence requires.
Substance reproduced. Provenance gpsc-qqsz community / twsw-2mqa official; FY2023
identical (12,114 / $63,569,204,049.36); FY2024 divergent 70 records / $58,072,427.23
(0.5103% / 0.0891%); FY2022 identical row count with $0.75 face divergence; freshness lags
335/701/1066 (community) and 456/822/1187 (official); schema 23 vs 32 (16 official-only, 7
community-only); revisions endpoint 404; system columns queryable; hash match; self-test
42/42; live no-drift. All three members and the orchestrator sanity check concur.
Findings absorbed in v0.2: - F-AM-R1-S-001 (MEDIUM) ABSORBED. The "wholesale
republish" inference (reader note Abstract, Section 3 Tier-2 definition, Section 5.2; and the
reproduction tool's flag) presupposes a prior publication that a single-pull uniform
:created_at does not establish; the same timestamp is equally consistent with a first-time bulk
load of a view with no prior served instance. Raised MEDIUM by GPT 5.5 and INFO by Claude
Opus 4.8; Gemini assessed the inference as appropriate. Absorbed at the strictest level: the reader
note now claims only the batch-after-close fact and admits the first-bulk-load alternative in-line,
and the tool's flag was relabelled from WHOLESALE-REPUBLISH to POST-CLOSE-BATCH with a
clarifying note. Non-blocking; disturbs no reproduced count, total, timestamp, or lag. - F-AMR1-S-002 (LOW) ABSORBED. "Provenance"/"first-party" wording could read as an
independent chain-of-custody determination; it is the Socrata-declared provenance metadata
field. The reader note now labels it as portal-metadata classification. - F-AM-R1-S-003 (LOW)
ABSORBED. "Stronger signal" for row timestamps was too broad; softened to "an available
freshness signal (row-instantiation timing), not a full change log."
Findings held affirmative (no change required): the refusal boundary holds (no accusation of
tampering or bad faith; the sole "tamper" occurrence is "tamper-evident," a property of the
method); the tier discipline and estimand/framing hygiene hold; cross-dataset
contract_amount comparability is well supported (FY2023 byte-identical, FY2022 differs by
only $0.75 at identical row count); and all numerical and data-interface claims reproduced
exactly.
Next audit cycle. The count is ONE. One further qualifying pass on this v0.2 artifact -- at least
two qualifying members, executed reproduction, 0 CRITICAL and 0 HIGH -- completes the
two-consecutive-pass convergence gate. Keep the package bundled and the membership rotated.
The producer's pre-delivery mechanical check covers version, counter, and round count across all
current-status loci; it was run on this v0.2 revision. The reproduction package's immutable-DOI
deposit remains a future owner action.
Appendix: v0.2 -> v0.3 amendments (second round F-AM-R2, rotated Model Council:
QUALIFYING PASS, count to TWO; gate met with caveats) [new in this artifact]
The round. Second (convergence-closing) cross-instance audit of the v0.2 artifact, package
bundled. Membership: qualifying clean pair GPT 5.5 (OpenAI) and Gemini 3.1 Pro (Google);
GPT 5.4 (OpenAI) rotated in as a third qualifying member; Claude Opus 4.8 (Anthropic)
quarantined advisory. Both clean-pair members executed all six protocol steps with pasted
outputs, independently recomputed without importing the supplied functions, demonstrated the

adversarial mutate-and-rehash returning comparator DRIFT (exit 2), and each returned 0
CRITICAL, 0 HIGH. GPT 5.4 executed genuinely but returned INCOMPLETE: it could not
attest isolation (a workspace-wide grep touched other round directories), so it is excluded from
the convergence-bearing count; its corroborating findings are recorded. Synthesized qualifying
verdict over the clean pair: QUALIFYING PASS. Per the written criterion this is the second
consecutive qualifying pass and moves the counter from ONE to TWO, meeting the Standing
Rule 7 gate on the v0.2 substance.
Substance reproduced (all executing members + orchestrator shadow run): hash match;
provenance community/official; FY2023 identical, FY2024 70 records / $58,072,427.23,
FY2022 $0.75 at identical row count; freshness lags 335/701/1066 and 456/822/1187; schema 23
vs 32 (16/7); revisions endpoint 404; system columns queryable; self-test 42/42; live no-drift;
adversarial DRIFT exit 2 after hash-gate defeat.
Findings absorbed in v0.3 (all below HIGH, non-blocking per the brief): - F-AM-R2-001
(MEDIUM) ABSORBED. The R1 republish over-claim was fixed in the Abstract, Section 3,
Section 5.2, and the tool flag, but survived in Sections 5.4 ("the republish inference"), 6
("republish checks"), and 7 ("reports as a republish"). This is a recurrence of F-AM-R1-S-001 in
loci the primary fix missed -- the producer's own "fix some loci, not all" failure mode. Corrected
in v0.3: those three loci now read "post-close-batch inference / post-close-batch checks / reports
as a post-close batch load (republish or first-time bulk load, indistinguishable from a single
pull)." Raised by GPT 5.5 and GPT 5.4; Gemini and the Claude advisory treated S-001 as fully
resolved. - F-AM-R2-002 (LOW) ABSORBED. Companion header line 3 stale-labelled the
reader note v0.1 while line 5 and the Current State read v0.2. Corrected to v0.3. Raised by GPT
5.5, GPT 5.4, and Claude advisory (three-way); the producer's widened check had missed this
locus. - F-AM-R2-003 (LOW) ABSORBED. The companion "Audit rounds" placeholder still
read "None yet ... v0.1 reader note" after the F-AM-R1 appendix had been appended. Marked
superseded per Section 14.5. Raised by GPT 5.5.
Producer accountability note. Two of the three findings (F-AM-R2-002/003) are statuspropagation stragglers the producer's own widened mechanical check failed to catch, because the
check's locus list omitted the companion header line 3 and the "Audit rounds" placeholder, and
its republish scan matched only "wholesale republish" rather than bare "republish." The check
has been corrected to include those loci and the bare term. This is the same class of failure the
program has repeatedly surfaced in its own producer; it is recorded, not concealed.
Convergence status and recommendation. The written gate is met (count TWO on the v0.2
substance). It is not promoted to a canonical converged v1.0, because (a) the converging round
was not clean (a recurring MEDIUM plus two status stragglers, now absorbed into v0.3), and (b)
the rotation record is weak (same clean pair across both passes; the rotated-in member selfdisqualified). Recommended before promotion: one confirming round (F-AM-R3) on this
corrected v0.3 with a successfully-isolated rotated qualifying member, returning 0 CRITICAL / 0
HIGH on a now-clean artifact. This is a stricter close than the letter of the rule requires, and is
the honest one.

Appendix: v0.3 -> v1.0 promotion (third round F-AM-R3, confirming: QUALIFYING
PASS, count to THREE, rotation gap closed, canonical convergence) [new in this artifact]
The round. Confirming convergence round on the corrected v0.3 artifact, package unchanged
and bundled. Membership: qualifying clean pass-bearing pair GPT 5.5 (OpenAI) and GPT 5.4
(OpenAI, rotated-in and new relative to the R1/R2 clean pair); Gemini 3.1 Pro (Google)
qualifying; Claude Opus 4.8 (Anthropic) quarantined advisory. GPT 5.5 and GPT 5.4 each
executed all six steps with pasted outputs, independently recomputed the live facts with their
own code using the specified exact-match fiscal-window filter, demonstrated the adversarial
hash-gate-defeat DRIFT (exit 2), attested clean isolation, and returned 0 CRITICAL, 0 HIGH.
GPT 5.4 -- which returned INCOMPLETE on isolation in R2 -- this round confined every
operation to its own directory and attested cleanly, closing the rotation gap. Synthesized
qualifying verdict: QUALIFYING PASS. Counter to THREE; the gate met at R2 is confirmed
clean on v0.3.
Substance reproduced (GPT 5.5, GPT 5.4, Claude advisory, and the producer's independent
live re-pull): hash match; provenance community/official; FY2023 identical, FY2024 70
records / $58,072,427.23, FY2022 $0.75 at identical row count; freshness lags 335/701/1066 and
456/822/1187; schema 23 vs 32 (16/7); revisions 404; system columns queryable; self-test 42/42;
live no-drift; adversarial DRIFT exit 2.
Gemini 3.1 Pro Step-4 anomaly (audit-execution defect, not artifact defect; independently
adjudicated). Gemini's independent recompute used a broad date-range filter
(fiscal_year_end_date >= 'YYYY-01-01' AND <= 'YYYY-12-31T23:59:59.999')
instead of the exact-match filter the paper and script use ( = 'YYYY-12-31T00:00:00.000'),
returning slightly higher counts (gpsc FY2022 12,158; FY2023 12,115 with a $49,000-high sum;
FY2024 13,719) and misattributing the difference to "moving data." The producer independently
reproduced both filters live: the exact-match filter still returns the frozen values (12,156 /
12,114 / 13,718), and the broad filter captures extra non-December-31 fiscal-year-end rows -- in
FY2023, a single 2023-03-31 row carrying about $49,000 accounts exactly for Gemini's +1
record and $49,000 sum. The data is not moving (the script's own --live showed no drift);
Gemini's Step 4 was a filter mismatch. It is therefore treated as nonconforming and Gemini is not
counted in the clean pass-bearing pair; convergence rests on GPT 5.5 + GPT 5.4, whose exactmatch recomputes agree with the frozen capture and the producer's ground truth.
Finding absorbed in v1.0: - F-AM-R3-001 (LOW) ABSORBED. Reader Section 1's refusal
sentence read "an observed divergence or republish," a newly-surfaced locus of the republishwording class (outside the R2-specified Sections 5.4/6/7, which were confirmed resolved).
Flagged by GPT 5.5; Gemini, GPT 5.4, and the Claude advisory read it as a refused Tier-3
hypothetical and did not flag it. The producer agrees it is at least imprecise (the method
establishes a post-close batch load, not a republish) and absorbed it: Section 1 now reads "an
observed divergence or post-close batch load." Non-blocking; disturbs no reproduced value.
Convergence status. Convergence is confirmed clean on the v1.0 artifact: three consecutive
qualifying passes, the confirming round clean on the blocking criteria (0 CRITICAL / 0 HIGH)
with the rotation gap closed by a successfully-isolated new qualifying member, and the sole
finding a LOW wording nuance now absorbed. This is a stricter close than the two-consecutive-

pass letter requires. v1.0 is the thrice-passed substance with the one LOW Section 1 fix; no
figure changed across any round.
Remaining owner actions (post-convergence, not audit rounds). (1) Assign DOIs and wire
them into the reader note and this companion. (2) Deposit the reproduction package to an
immutable archive alongside the ledger. (3) Render the reader note and companion (at-Taʿlīm
style, all-black Times New Roman) for publication. No further audit round is required unless the
substance changes.
Appendix: v1.0 DOI assignment and deposit [new in this artifact]
The owner assigned DOIs and deposited the artifacts. No analytic content changed; this records
identifiers and closes the deposit action.
•
•
•

Reader note (paper): DOI 10.5281/zenodo.21446613.
This audit and provenance ledger: DOI 10.5281/zenodo.21446618.
Reproduction and audit dataset: deposited under an immutable DOI alongside this
ledger at 10.5281/zenodo.21446618, closing the deposit action recorded in the Current
State. The frozen capture, its manifest, the reproduction script, and the three rounds'
primary auditor reports now have a citable, arm's-length home.

The convergence caveat recorded in the Current State continues to apply unchanged: the gate is
met inside this producer-defined governance framework, while the externally-verifiable result -every figure reproduces exactly from live data.ny.gov under the exact fiscal-window filter, and
the comparator is tamper-evident under hash-gate defeat -- holds independently. v1.0 records the
converged state with permanent identifiers; no further audit round is required unless the
substance changes.



Bismillah ir-Rahman ir-Rahim
