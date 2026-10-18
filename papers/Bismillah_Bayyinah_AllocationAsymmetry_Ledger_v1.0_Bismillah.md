Bismillah ir-Rahman ir-Rahim

Bayyinah: Public-Ledger Allocation and Asymmetric-Measure
Audits -- Audit and Provenance Companion
Companion to: Bayyinah: Public-Ledger Allocation and Asymmetric-Measure Audits (the
reader-facing note, v1.0; DOI 10.5281/zenodo.21445552). This ledger: DOI
10.5281/zenodo.21445556. Governed by: Bayyinah, Portable Structural Honesty Verification for
Public-Service Institutions (the framework paper). Prepared under BayyinahEnterprise audit
methodology (PMD v1.2, Audit Framework v3.0). Mirrors note state v1.0, the canonical
converged release (nine audit rounds; F-AA-R8 and F-AA-R9 are two consecutive qualifying
passes, so the convergence gate is met on the identical v0.7 substance now released as v1.0). See
the authoritative Current State block below.
DOI: [to be assigned on deposit]. Reader-facing note: DOI [to be assigned on deposit].

About this companion
This document is the append-only audit trail for the allocation-and-asymmetry note. It exists so
that any figure in the note can be traced to the exact rows it came from, and so that every error
caught and corrected during development stays on the public record rather than being silently
revised away. For a note whose method is verifying claims against a substrate, preserving how
its own claims were checked and corrected is not optional; it is the method applied to the note
itself.
It contains four parts: the per-claim Verification Status, including the frozen data snapshot and
its integrity hash and the two independent external reproduction passes; the findings ledger
(namespace F-AA) in the six-element format; the paper-level falsifiability criteria; and the
append-only version ledger with the one substantive correction made to date. Section numbers
refer to the reader-facing note. Per Bayyinah Audit Framework v3.0 Section 14.5, superseded
text is preserved and corrected by annotation, never edited in place.
Convergence status [historical, as written at the F-AA-R1 absorption; superseded by the
authoritative Current State block below, retained per Section 14.5]: the note is producer-side
and NOT converged, and its first independent audit round was a NON-PASS. That round
(namespace F-AA-R1, an OpenAI GPT-5.6 instance outside the authoring lineage) reproduced
the arithmetic exactly but returned 0 CRITICAL, 3 HIGH, 3 MEDIUM, 3 LOW: the v0.1 draft
attached interpretive claims its data did not support (contract face value presented as annual
spending; a prime-vendor flag presented as MWBE-goal attainment; competitive-process
composition declared a compliance pass). All nine findings are absorbed in v0.2 (see the F-AAR1 appendix). Because a HIGH-bearing round does not pass, the two-consecutive-passing-round
convergence count is at zero and restarts: v0.2 must undergo a fresh independent round. The
absorption below is producer-side and does not itself count as a round.

Current State (authoritative, as of v1.0)
This block is the single authoritative statement of current status; where any present-tense
language in the historical Sections A through D below conflicts with it, this block governs and
that language is superseded historical text preserved per Section 14.5.
•

•

•

•
•

•

Artifact state: v1.0 canonical converged release. Reader note DOI
10.5281/zenodo.21445552; this ledger DOI 10.5281/zenodo.21445556; the reproduction
package (content unchanged since v0.3; validated in F-AA-R3 and executed against in FAA-R5, R6, R7, R8, R9) is deposited under an immutable DOI alongside this ledger at
DOI 10.5281/zenodo.21445556. v1.0 is the identical converged v0.7 substance with
DOIs assigned and the package deposited; no analytic content changed.
Independent audit history (rounds 1-3; see the counter bullet for the full eightround sequence): the first three independent cross-instance rounds were attempted, all
NON-PASS. Round 1 (F-AA-R1, OpenAI GPT): 0 CRITICAL, 3 HIGH, 3 MEDIUM, 3
LOW, absorbed in v0.2. Round 2 (F-AA-R2, OpenAI GPT, self-attested non-qualifying
on same-family/context grounds): 0 CRITICAL, 2 HIGH, 3 MEDIUM, 1 LOW, absorbed
in v0.3. Round 3 (F-AA-R3, Claude/Anthropic -- the producing lineage, self-attested
non-qualifying on independence): 0 CRITICAL, 1 HIGH, 2 MEDIUM, 1 LOW, 1 INFO,
absorbed in v0.4. The round-2 and round-3 HIGH findings were both the producer's
failure to propagate a version/round-status update across all parts of the artifact; round 3
also completed, for the first time, the two mandatory legs (full --live comparison and
the row-level capital join) no prior auditor could finish, confirming the data,
implementation, and provenance are sound.
Fourth round (F-AA-R4, Gemini -- genuinely independent, fresh context): PASS at 0
CRITICAL, 0 HIGH, 2 INFO. This is the first properly-independent passing round.
Critical caveat: the auditor explicitly did not execute the reproduction scripts or query
the data; it validated the artifact's internal consistency against the expected outputs stated
in the audit brief (a logic-and-consistency review), not an independent data reproduction.
Every figure it cited matches the producer's verified computations, but it added no
independent-reproduction evidence and could not have caught a data-level error. Its two
INFO findings (fingerprint exact-match=0 confirmed; version propagation now complete)
require no action.
Open findings above INFO, as of v0.4: none.
Fifth round (F-AA-R5, Perplexity Model Council): findings-bearing NON-PASS.
Qualifying members GPT 5.5 and Gemini 3.1 Pro (Claude Opus 4.8 quarantined,
advisory-only); both qualifying members declined PASS. The frozen reproduction
package was not in the audit packet, so the mandatory offline/self-test/live-comparator
steps could not run; but the qualifying members independently reproduced every
principal figure via live queries (37,988 rows; $65.19B face; $8.17B expenditure; MWBE
18.73/3.95/7.06 percent; top-10 30.42 percent; Gini 0.931; pre-2024 91.69 percent;
1,348/48 missing/zero; 18-field overlaps 2,115/604/1,002; exact all-field 0). Two HIGH
findings (missing package; convergence-counter contradiction) and one MEDIUM
(provenance wording) are absorbed in v0.5.
Deposit action (F-AA-R5-C-01, CLOSED at v1.0): the reproduction package is
deposited under an immutable DOI alongside this ledger at DOI

•

•

•

•

•

•

10.5281/zenodo.21445556; Section 8 of the reader note points to it there. The package
now has a citable, arm's-length home, closing the last open item.
Sixth round (F-AA-R6, Perplexity Model Council): QUALIFYING PASS. Qualifying
members GPT 5.5 and Gemini 3.1 Pro (Claude Opus 4.8 quarantined) both executed the
full seven-step protocol against the attached package -- hash and field-inventory OK,
self-test 45/45, live no-drift exit 0, adversarial mutation flagged, provenance separated,
capital join demonstrated -- and both returned 0 CRITICAL, 0 HIGH. First genuinelyindependent executed-reproduction passing round in the series. One MEDIUM (F-AAR6-01, companion line-3 stale v0.4) absorbed; non-blocking.
Seventh round (F-AA-R7, Perplexity Model Council with rotated membership):
findings-bearing NON-PASS. Qualifying members GPT 5.5, GPT 5.4 (rotation member,
new vs R6), and Gemini 3.1 Pro; Claude quarantined. Two qualifying members (GPT
5.5, GPT 5.4) independently executed the full protocol and returned the same HIGH
finding F-AA-R7-01; Gemini returned 0/0 but with execution defects (off-by-one
provenance count; adversarial step confirmed the hash abort but not the comparatornonzero requirement) and is non-decisive. The rotation worked as intended: the surviving
blind spot was a MISSED defect (Gemini), caught by the rotated GPT members.
Substance reproduced exactly across all members.
Eighth round (F-AA-R8, rotated Perplexity Model Council): QUALIFYING PASS.
Three qualifying members -- GPT 5.5, GPT 5.4 (rotation), Gemini 3.1 Pro -- each
executed all seven protocol steps against the attached package and returned 0 CRITICAL,
0 HIGH; Claude quarantined. The R7-01 status-propagation defect was confirmed
resolved by all members (version, counter, and round count consistent across all loci),
and Gemini corrected its two R7 execution defects. One MEDIUM (F-AA-R8-01, a
companion history-lead-in wording nuance) absorbed; non-blocking.
Ninth round (F-AA-R9, rotated Perplexity Model Council -- FINAL convergence
round): QUALIFYING PASS. The same three qualifying members -- GPT 5.5, GPT 5.4,
Gemini 3.1 Pro -- each executed all seven protocol steps against the attached package and
returned 0 CRITICAL, 0 HIGH; Claude quarantined. All prior findings, including the
R7-01/R8-01 status-propagation family, confirmed resolved across all loci. One LOW (FAA-R9-01) was a defect in the BRIEF's wording, not the artifact (see below); nonblocking.
Consecutive qualifying-PASS count (single operational counter, per F-AA-R5-C02): TWO. F-AA-R8 and F-AA-R9 are two consecutive qualifying passes (each: at least
two qualifying non-producer members, executed reproduction, 0 CRITICAL / 0 HIGH).
The two-consecutive-qualifying-pass convergence gate under Audit Framework v3.0
Standing Rule 7 is MET on the converged v0.7 substance, released as v1.0. Round
history: three NON-PASS (R1, R2, R3), one non-reproducing consistency-only PASS not
credited (R4), one findings-bearing NON-PASS (R5), one qualifying pass (R6, count to
one), one findings-bearing NON-PASS (R7, reset to zero), two consecutive qualifying
passes (R8 count to one, R9 count to two).
Convergence caveats (recorded honestly with the declaration): (1) F-AA-R8 and FAA-R9 used the same three-member qualifying set (GPT 5.5, GPT 5.4, Gemini 3.1 Pro);
independence between the two consecutive passes rests on fresh, memoryless instances in
clean sessions, not on differing model identities. The set spans two providers and two
GPT versions, and across the nine-round history the substance has been independently

•

•

reproduced by four distinct non-producer models, but the two decisive consecutive passes
are not from disjoint membership. (2) R8 audited v0.6 and R9 audited v0.7; the substance
is materially identical (the only change was the F-AA-R8-01 wording fix), not byteidentical. (3) F-AA-R5-C-01 (deposit of the reproduction package to an immutable DOI)
is now CLOSED at v1.0: the package is deposited alongside this ledger at DOI
10.5281/zenodo.21445556, making the reproduction fully arm's-length.
Brief-level note (F-AA-R9-01, LOW): the Round-9 brief's spec line "No three-way
intersection or identity-only subset" was imprecise -- the stable 18-field three-way
intersection is 265 (independently confirmed by GPT 5.4, Gemini, and the producer); the
exact all-field three-way intersection is 0 and all pairwise figures (2,115 / 604 / 1,002)
reproduce exactly. The v0.7 artifact makes no "no three-way intersection" claim, so this
is a correction to future briefs, not an artifact defect.
Superseded status phrases to disregard as current: in Section B, "One substantive
finding to date"; in Section D, "this state," "the note is producer-complete and carries 0
open findings above INFO"; in Section A, the corroboration that the 3.95 percent share is
the MWBE "operative substrate"; in Section C, the fourth falsifiability criterion referring
to a Section 4.1 "pass." Each is annotated in place below.

A. Verification Status
Primary data. All figures derive from the New York State Open Data portal, Socrata resource
gpsc-qqsz (MTA Procurement Report, All), retrieved without authentication. Unlike the
education worked example, whose sources were browser-gated, this endpoint is directly
queryable, so the recompute is reproducible by any second party from the primary source.
Frozen snapshot (reviewer-reproducible). Because the live resource may be updated by the
authority, the exact rows underlying the note's figures are frozen as a companion artifact:
snapshot/gpsc-qqsz_FY2022-2024.json, 37,988 records across the three fiscal years
ending 2022, 2023, and 2024, with a MANIFEST.json recording the retrieval timestamp, the
field list, and a SHA-256 of the canonical JSON. The reproduction script
reproduce_paper2.py verifies this hash before computing, so a reader is told immediately if
the snapshot has been altered, and can compute the note's figures deterministically offline and,
with --live, check for drift against the current endpoint.
Reproduction record. - Producer-lineage: every Section 4 figure was computed from the
snapshot by reproduce_paper2.py and matches the note exactly (FY2024 totals; competitive
92.22 percent of dollars; MWBE 18.7 percent count and 3.95 percent dollar; three-year
persistence 5.0, 5.3, 4.7; top-5/10/20 concentration 22.1/30.4/41.8 percent; Gini 0.931; 2,656
vendors). - External verification EV-1 (informal, non-lineage): an independent party executed
the reproduction script against the live endpoint and independently re-queried the Section 4.3
quantities (zero-amount exclusion, vendor concentration, Gini, largest vendors by name and
amount), reporting exact matches on all figures including individual vendor dollar amounts
(Kawasaki Rail Car $6.46B, New Flyer $2.56B, and construction joint ventures above $1.5B). External verification EV-2 (informal, non-lineage): the same party empirically tested the crosstable join asserted in Section 3, resolving a real project_number (D501CB08) from the
locations table wcsa-vkhf against live allocation records in kizb-nxtu, confirming the join is
functional, not merely plausible.

Framing-claim corroboration (external, informal). EV corroborated two interpretive claims:
that New York MWBE goals are dollar-denominated (9 NYCRR Section 435.6, "percent of the
total dollar value of contracts"), which was originally stated as supporting a reading that the 3.95
percent dollar share is the operative substrate. [Corrected in v0.3 per F-AA-R2-01, Section
14.5:] that reading is withdrawn and does not match the reader note. Dollar-denomination of a
goal does not establish that total prime-contract face value (or any single supplied ledger
amount) is the legally operative MWBE-goal denominator; eligible expenditures, subcontracting
opportunities, participation tiers, exclusions, and waivers remain absent. The 3.95 percent figure
is a descriptive prime-vendor statistic only. EV also corroborated that a shared procurementreporting schema is mandated for New York public authorities (Public Authorities Law and
Executive Law Article 15-A, via the Authorities Budget Office PARIS system), which supports
Section 3's common-schema claim underpinning portability.

B. Findings
Namespace F-AA (allocation-asymmetry development findings). [Superseded per F-AA-R205: 'one substantive finding' was true only at the original writing; the current finding set
spans F-AA-1, F-AA-2, F-AA-R1-01..09, and F-AA-R2-01..06. See Current State block.]
F-AA-1 MEDIUM -- Incorrect data-infrastructure claim: capital budget data described as
not queryable/tabular [RESOLVED-BY-CORRECTION in v0.1 (corrected); raised by
external verification]
Locus: Section 3 (data-interface adapter), with follow-through in Section 4.4 and Section 6.
Substance: The first v0.1 text stated that the MTA capital budget data "is published as a derived
dashboard view rather than a queryable tabular resource, so a borough-level capital-dollar
analysis is not reproducible through this endpoint." This was false as a claim about the data
infrastructure. The producing lineage had observed that one dashboard resource ( mn7w-32rv)
would not serve rows and generalized "not queryable" to the entire capital dataset family without
testing the others. In fact kizb-nxtu and ehz8-ag3n are queryable tabular Socrata resources
carrying allocation dollars per project. The surface claim ("not queryable") diverged from the
substrate (the data is queryable), which is precisely the failure mode the note's own method
exists to detect, here committed by the note about its own data source.
Disposition: RESOLVED-BY-CORRECTION. The reason was corrected while the conclusion
was preserved, because the conclusion was independently sound: the budget tables carry
allocation dollars but no borough key, so a borough-level rollup requires joining to the locations
table (wcsa-vkhf) on the shared project number and then a coordinate-to-boundary spatial join,
a nontrivial GIS step rather than a single query, and is deferred rather than blocked. The
corrected text names the queryable resources explicitly and states the accurate reason. The
correction was itself externally re-verified (EV-2), including the functional join test. Root cause
recorded for future notes: an infrastructure claim was asserted from a single failed endpoint
without enumerating the dataset family; the standing remedy is that any "data not available"
claim in this series must enumerate and test the candidate resources before assertion.
Cross-reference: external verification EV-1, EV-2; Section 3; carried detail F-AA-2.

F-AA-2 INFO -- Column-name divergence across capital tables, carried for the geographic
instance [CARRIED; not an error in this note]
Locus: not in the reader-facing note; recorded here for the forthcoming by-geography capital
instance.
Substance: The capital tables do not share a column name for the project key: wcsa-vkhf and
kizb-nxtu use project_number, while ehz8-ag3n uses proj_num (same underlying
identifier). This does not affect any claim in the present note, which asserts a shared project
number only as a concept, not identical column names. It is logged because a future geographic
instance that joins these tables must handle the name divergence or silently produce empty joins.
Disposition: CARRIED to the by-geography capital instance. No action in this note.
Cross-reference: F-AA-1; external verification EV-2.

C. Falsifiability Criteria (note-level)
The worked example would be falsified, in whole or part, by any of the following, each
checkable from the frozen snapshot or the live endpoint. First, if the snapshot SHA-256 does not
match the manifest, the figures must not be trusted and the reproduction is void. Second, if the
MWBE count-versus-dollar divergence did not hold across all three fiscal years, the persistence
claim would fail; it is therefore stated with all three years exposed, not one. Third, if the vendor
dollar concentration were low (a flat distribution), the structural explanation offered in Section
4.3 for the MWBE dollar gap would lose its basis; the Gini of 0.931 and the top-ten share of 30.4
percent are the load-bearing evidence for that explanation and are reproducible. Fourth
[Corrected in v0.3 per F-AA-R2-04, Section 14.5]: the original criterion referred to a Section
4.1 "pass," which v0.2 withdrew. The corrected criterion is: if recomputation does not reproduce
the reported process-composition percentages, the descriptive Section 4.1 figures are falsified.
Separately and independently of any share being dominant, no composition result establishes
rule compliance, which requires the operative guidelines and exception documentation absent
from this dataset. Each of these is a specific number a second party can recompute and disagree
with.

D. Append-Only Ledger
v0.1 (initial draft). Note drafted from live gpsc-qqsz data; all Section 4 figures computed by
the producing lineage and by an initial reproduction script.
v0.1 (corrected) [this state]. One substantive correction absorbed (F-AA-1): the incorrect "not a
queryable tabular resource" claim in Section 3, with matching follow-through in Sections 4.4 and
6, replaced by the accurate "queryable, carries dollars, lacks a borough key, needs a spatial join"
reason. Superseded text preserved per Section 14.5: - v0.1 Section 3: "is published as a derived
dashboard view rather than a queryable tabular resource, so a borough-level capital-dollar
analysis is not reproducible through this endpoint." Corrected in v0.1 (corrected) per F-AA-1: the
data is queryable and carries dollars; the barrier is a missing borough key, requiring a spatial
join. No numerical figure in Section 4 was altered by the correction; the external reproduction of
those figures (EV-1) therefore still stands against the corrected note.

Producer-complete package added [this state]. Frozen snapshot with integrity hash and
manifest; hardened reproduction script verifying the hash and reproducing all Section 4 figures
offline; this audit companion; and an accompanying audit-request brief for an external auditor.
Next audit cycle [superseded status per F-AA-R2-05; see Current State block for
authoritative status]: at the original writing this said the note was producer-complete with 0
open findings above INFO; that predates both audit rounds. The remaining item is unchanged in
substance: two consecutive passing rounds by an auditor outside the authoring lineage. The
consecutive-pass count is zero after two NON-PASS rounds. The external verification passes
recorded here, however thorough, do not discharge that gate by Standing Rule 7. Secondary
follow-ups, non-blocking: (a) run a second New York authority's procurement report through the
same gpsc-qqsz-schema adapter to begin discharging the framework's portability claim; (b)
build the by-geography capital instance using the join proven in EV-2, handling the proj_num
name divergence recorded in F-AA-2.
Appendix: v0.1 -> v0.2 amendments (first independent cross-instance audit round: NONPASS) [new in this artifact]
Per Section 14.5 no prior text is edited in place; this documents new work only.
The round. After v0.1 (corrected) and the reproduction package were issued, an independent
auditor of a non-Anthropic lineage (attested OpenAI GPT-5.6, no drafting role) verified the
snapshot hash and row count, ran the supplied script, independently recomputed every Section 4
statistic from the frozen rows without importing the supplied functions, additionally recomputed
on amount_expended_for_fiscal_year, and tested award-year composition, cross-year
repeat fingerprints, missing/zero splits, vendor aggregation, and the Gini implementation. Result:
reproduction exact on the selected estimand, but NON-PASS at 0 CRITICAL, 3 HIGH, 3
MEDIUM, 3 LOW. Two audit legs did not complete in the auditor's environment (the --live
call hit DNS resolution failure; the row-level capital join was not re-executed) and are carried to
the resubmission round. The producing lineage independently re-verified all nine findings
against the frozen snapshot before absorbing them.
HIGH findings, all absorbed in v0.2:
•

•

F-AA-R1-01 (HIGH) ABSORBED. contract_amount is total contract face value, not
FY2024 spending; 91.7 percent of the FY2024 sum is from contracts awarded before
2024 (award years 1984-2025), and multi-year contracts recur across report vintages.
v0.1's annual-flow framing was a stock-versus-flow error. v0.2 names two estimands
(face value $65.19B; annual expenditure $8.17B), adds the stock-versus-flow disclosure
and the repeat-reporting caveat, recomputes on both measures, and narrows "persistence"
to repeated observations of an overlapping portfolio (Sections 4.0, 4.2, 6).
F-AA-R1-02 (HIGH) ABSORBED. The 18.7-versus-3.95 percent figure was framed as
the operative MWBE-goal substrate and "short measure." A binary prime-vendor flag
cannot capture indirect/subcontract participation, eligible-spend denominators, contractspecific goals, or waivers (Executive Law Article 15-A), and on annual expenditure the
share is 7.06 percent, not 3.95. v0.2 recasts this as a descriptive prime-vendor countversus-dollar statistic on both measures, removes "operative substrate," "short measure,"

•

"honest measure," and "four cents on the dollar," and adds the
prime-only/indirect/eligibility/waiver limitations (Sections 2, 4.2, 6).
F-AA-R1-03 (HIGH) ABSORBED. v0.1 declared the competitive-bidding rule a "pass"
(substrate matches surface) from award-process composition alone. Composition is not
compliance: testing it needs the MTA's operative guidelines, exception categories,
waiver/documentation requirements (Public Authorities Law Section 2879), and a
transaction-level or sampled check. v0.2 reports composition as a descriptive Tier-2
statistic and withdraws the "pass" and "substrate matches surface" language (Sections 4.1,
4.4).

MEDIUM findings, absorbed:
•

•
•

F-AA-R1-04 (MEDIUM) ABSORBED. gpsc-qqsz is a community-created view, not
first-party. The producing lineage independently confirmed the first-party twsw-2mqa
differs (13,648 rows / $65.13B vs 13,718 / $65.19B, under 0.1 percent). v0.2 describes
gpsc-qqsz accurately as a derived view, names twsw-2mqa and the ABO statewide
dataset as recommended production sources, and discloses the divergence (Sections 3, 8).
F-AA-R1-05 (MEDIUM) ABSORBED. v0.1 stated 111,879 records for the three fiscal
years; the frozen three-year extract is 37,988 (111,879 is the full resource across all
periods). Corrected in Section 3.
F-AA-R1-06 (MEDIUM) ABSORBED. v0.1 said state law requires publishing to a
common portal schema. v0.2 states the accurate chain: Public Authorities Law mandates
annual reporting; authorities submit via PARIS using standardized structures; ABO with
Open Data NY publishes compiled datasets (Sections 3, 5).

LOW findings, absorbed:
•
•

•

F-AA-R1-07 (LOW) ABSORBED. Missing and explicit-zero amounts merged in v0.1;
v0.2 separates 1,348 missing and 48 explicit-zero (Sections 4.0, 8).
F-AA-R1-08 (LOW) ABSORBED. The manifest field inventory (derived from row 0)
omitted vendor_province_region, which Socrata had suppressed as null in that row.
The manifest is regenerated from the union of all rows and validated equal to the actual
field set; the reproduction script now aborts on any field-inventory mismatch. Snapshot
bytes and hash are unchanged.
F-AA-R1-09 (LOW) ABSORBED. --live checked only FY2024 count and sum. The
script now pulls all three years live and compares every emitted statistic (both estimands,
all vintages) against the frozen baseline, exiting nonzero on material drift.

Next audit cycle: v0.2 requires a fresh independent round, because a NON-PASS resets the twoconsecutive-passing-round count to zero. The resubmission round must additionally complete the
two legs the first auditor could not (a full --live comparison and a functional row-level capital
join), and should rebase provenance on the first-party or ABO dataset. The portability and bygeography follow-ups remain open.

Appendix: v0.2 -> v0.3 amendments (second independent audit round: NON-PASS) [new in
this artifact]
Per Section 14.5 no prior text is edited in place; substantive stale claims are annotated in place
above (F-AA-R2-01, F-AA-R2-04, F-AA-R2-05), and this documents the round.
The round. An independent auditor of a non-Anthropic lineage (attested OpenAI GPT) audited
v0.2. It reproduced every frozen statistic exactly (including the annual-expenditure asymmetry
and the face-value concentration and Gini) and confirmed the field-inventory abort works. It
returned NON-PASS at 0 CRITICAL, 2 HIGH, 3 MEDIUM, 1 LOW. The auditor explicitly
attested this round was NOT the preferred independence: it shares the OpenAI family with round
1 and did not run in a strictly fresh context. Two mandatory legs did not complete in its
environment (its Python DNS resolver failed the live pull; the row-level capital join was not
executed). The producing lineage independently re-verified every finding against the frozen
snapshot before absorbing.
The pattern this round exposed. Both HIGH findings are the producing lineage's own failures
of propagation and honesty, not new data problems: round 1's corrections were applied to the
reader note but not carried into this companion or the reproduction script, and the round-1 script
fix was documented more broadly than implemented. This is recorded plainly because it is the
exact failure this program exists to catch, committed by the producer against its own artifacts.
HIGH findings, absorbed in v0.3:
•

•

F-AA-R2-01 (HIGH) ABSORBED. This companion's Section A still asserted the 3.95
percent share is the MWBE "operative substrate," the precise claim round 1 required the
reader note to remove. It is corrected in place above: dollar-denomination of a goal does
not make total prime-contract face value the operative denominator, and the figure is
descriptive only. This also discharges the round-1 residual (overbroad corroboration) the
auditor noted under F-AA-R1-06.
F-AA-R2-02 (HIGH) ABSORBED. The reproduction script's --live claimed to
compare "every emitted statistic, schema, and row/hash summary" but compared only
three MWBE percentages; the companion repeated the overbroad claim. v0.3 rebuilds the
script around a single complete statistics object: --live now recomputes and compares
every published statistic (both estimands, all vintages: totals, missing/zero, process
shares, face and annual-expenditure concentration and Gini, pre-2024 share), the field
inventory, and row counts, with explicit tolerances and nonzero exit on any mismatch. A
--selftest mode perturbs each of the 45 statistics plus the schema and confirms the
comparator detects every one; it passes. The full --live comparison was also executed
end-to-end and reported no drift.

MEDIUM/LOW findings, absorbed in v0.3:
•

F-AA-R2-03 (MEDIUM) ABSORBED. The reader's "exact full-field fingerprint finds
several thousand" was false: an exact all-field match finds zero (fiscal-year and annualstate fields differ). v0.3 reader Section 4.0 describes a stable-field fingerprint (excluding
fiscal-year and expenditure/balance fields) and reports the actual pairwise counts 2,115 /
604 / 1,002, independently confirmed against the snapshot.

•

•

•

F-AA-R2-04 (MEDIUM) ABSORBED. This companion's Section C fourth falsifiability
criterion referred to a withdrawn Section 4.1 "pass" and preserved the invalid inference.
Corrected in place above to a process-composition-reproducibility criterion, with the
explicit statement that no composition result establishes compliance.
F-AA-R2-05 (MEDIUM) ABSORBED. This companion mixed present-tense status
labels ("one substantive finding to date," "0 open findings above INFO," "this state") with
append-only history, so current status was unreadable. v0.3 adds the authoritative Current
State block at the top and annotates the stale labels in place as superseded.
F-AA-R2-06 (LOW) ABSORBED. Reader Section 4.3 claimed the concentration
explains the asymmetry "on both measures" while reporting only face-value
concentration. v0.3 adds the annual-expenditure concentration (top five 16.9 percent,
Gini 0.904) to the reader note and reproduces it in the script, so the both-measures claim
is demonstrated in-package.

Next audit cycle: the consecutive-passing-round count is ZERO after two NON-PASS rounds
and v0.3 requires a fresh round. That round must be the preferred independence (a non-OpenAI
auditor in a fresh context) and must complete the two mandatory legs no auditor has yet
executed: a full live comparison (now genuinely implemented) and a functional row-level
capital-table join. It should also reproduce against the first-party twsw-2mqa or the ABO
statewide dataset. Until two consecutive passing rounds occur, nothing here is convergenceverified.
Appendix: v0.3 -> v0.4 amendments (third independent round F-AA-R3: NON-PASS, nonqualifying on independence) [new in this artifact]
Per Section 14.5 no prior finding text is edited in place; stale status labels in the header and the
line-17 convergence paragraph are annotated/updated as noted above, and this documents the
round.
The round. A third audit was requested from a different family (Gemini). The responding
instance identified itself as Claude/Anthropic -- the producing lineage -- and honestly declared
its round non-qualifying on the independence requirement (a producer-lineage round cannot
discharge the gate), while noting its technical work remained valid. Run in a fresh context, it rederived every statistic from the frozen snapshot and a live pull and returned NON-PASS at 0
CRITICAL, 1 HIGH, 2 MEDIUM, 1 LOW, 1 INFO. For the first time in the three-round
history it completed both mandatory legs: a full --live comparison across all three years (no
drift, exit 0) and a functional row-level capital-table join (120/120 project_number matches in
kizb-nxtu; 120/120 in ehz8-ag3n via proj_num; wcsa-vkhf confirmed to carry no
borough key; worked example D701HH89 joining to a $92,827 kizb-nxtu allocation). It also
adversarially perturbed a non-MWBE statistic and confirmed --live flags it (exit 2), and
reconciled gpsc-qqsz against first-party twsw-2mqa. The producing lineage independently reverified every finding, including recomputing the fingerprint field-set variants, before absorbing.
Findings, absorbed in v0.4:
•

F-AA-R3-01 (HIGH) ABSORBED. The reader note's Section 7 still self-described as
"v0.2" and referenced only the first audit round, and Section 6 referenced only the "first
audit round" -- contradicting the note's own v0.3 header and the companion's Current

•

•

•

•

State block. The v0.2-to-v0.3 (R2) absorption was propagated into the header and
companion but not into the reader note's own provenance and limitations sections: the
same propagation failure mode as F-AA-R2 and the at-Taʿlīm F-AT-R4-NQ, now
committed a third time against the reader note's self-status. Corrected in v0.4: Sections 6
and 7 (and the Section 2 narrative) now state the artifact is v0.4, reference all three
rounds, and state the consecutive-passing-round count is zero. To prevent recurrence, the
standing rule is reaffirmed and widened: on any version bump, every self-referential
version/round-status statement -- reader header, abstract, limitations, provenance,
companion header, companion Current State -- is updated in the same edit, and the
version is not considered bumped until all are consistent.
F-AA-R3-02 (MEDIUM) ABSORBED. The companion header (lines 3, 5) still read
"v0.1" and "Mirrors note state v0.2," un-annotated, contradicting the Current State block
-- a residual of the F-AA-R2-05 fix that updated Sections A-D but not the header.
Corrected in v0.4: the header now reads v0.4 and points to the Current State block.
F-AA-R3-03 (MEDIUM) ABSORBED. The reader note's Section 4.0 fingerprint prose
foregrounded a five-to-seven-field "contract-identity" enumeration, but the published
overlaps (2,115 / 604 / 1,002) reproduce only under the 18-field method (all fields except
the fiscal-year and three annual-state fields); the enumerated-field reading yields 3,674 /
690 / 1,892, independently confirmed. A second party following the prose would not
reproduce. Corrected in v0.4: the prose now describes the method as matching on all
fields except the fiscal-year and annual-state fields, with the identity fields named as
examples, and explicitly notes the enumerated-only reading is not the method used. The
qualitative conclusion (vintages overlap; never sum) is unchanged.
F-AA-R3-04 (LOW) ABSORBED (cosmetic). A sentence-boundary artifact from the FAA-R2-01 in-place correction ("...statistic only. and that a shared...") is repaired. The
surviving literal "operative substrate" strings occur only in negations, the supersededphrases list, and the append-only ledger, which is Section 14.5-compliant preservation;
no further action, the round-2 HIGH (F-AA-R2-01) remains substantively resolved.
F-AA-R3-05 (INFO) NOTED. Both mandatory legs completed; all figures reproduce;
script --live/--selftest do what they document and were adversarially confirmed;
provenance reconciled; no negative amounts; MWBE framing consistent across note,
companion, and script; no withdrawn "pass" or annual-flow language survives as a
current claim. No defect.

Next audit cycle: the consecutive-passing-round count is ZERO after three NON-PASS rounds
and v0.4 requires a fresh round. The data, implementation, and provenance are now confirmed
sound (F-AA-R3 completed the two previously-unfinished legs), so a properly-independent
round -- a genuinely different family (non-OpenAI, non-Claude) in a fresh context -- has a clean
artifact to audit and need only confirm the F-AA-R3-01/02/03 status/prose fixes landed. Two
consecutive such passing rounds close the gate.
Appendix: F-AA-R4 fourth round (Gemini, genuinely independent): PASS on severity;
consistency review, not a reproduction [new in this artifact]
Content is unchanged from the v0.4 that F-AA-R3 produced; this records the round only. No
findings above INFO were raised, so no correction was absorbed.

The round. A fourth audit was requested from Gemini. The responding instance attested it is
Gemini (Google), in a fresh context, distinct from the OpenAI lineage (rounds 1-2) and the
Claude/Anthropic producing lineage (round 3). This is the first request in the series confirmed to
reach a genuinely different family. It returned PASS at 0 CRITICAL, 0 HIGH, 2 INFO.
The limitation, in the auditor's own words. Gemini stated it does not have an environment to
execute reproduce_paper2.py or query data.ny.gov, and that it "validated the logical,
arithmetic, and structural claims presented against the strict falsifiability criteria and expected
programmatic outputs outlined in this audit request." That is a consistency-and-logic review of
the artifact against the brief's stated expected outputs -- both of which originate from the
producer -- not an independent reproduction from the data. It therefore confirms internal
consistency and correct handling of the disclosed method, but it did not and could not surface a
data-level discrepancy; it added no independent-reproduction evidence. The producing lineage
separately re-verified every figure Gemini cited against the frozen snapshot (37,988 rows;
$65.19B; 18.7/3.95/7.06; 1,348/48; concentration and fingerprint figures) and all match -- but
that verification is the producer's, not Gemini's.
Findings (both INFO, no action): - F-AA-R4-01 (INFO). Fingerprint exact all-field match
returns zero, confirming the required divergence on the four excluded fiscal-year/annual-state
fields; surface matches substrate. Cross-ref F-AA-R3-03. - F-AA-R4-02 (INFO). Version/status
propagation is now complete: all components uniformly reflect v0.4 and the zero-consecutivepass state (as of the audited artifact), resolving the recurring lagging-version defect. Cross-ref FAA-R3-01/02.
Convergence assessment. F-AA-R4 satisfies independence (genuinely Gemini, fresh context)
and severity (0 CRITICAL, 0 HIGH), so on the letter of the criterion it is the first of the two
consecutive passing rounds. But the gate exists to obtain independent reproduction, and this
round did not reproduce. To date no single round has been simultaneously independent, a real
reproduction, and passing. Accordingly, convergence must not be declared on this round plus
another non-reproducing consistency review; the closing round must genuinely reproduce the
figures from the data (scripts executed or recomputed, arithmetic shown). The producer records
the count as one of two on the letter, with this reproduction gap as the binding condition on the
closing round. [Superseded per F-AA-R5-C-02: the dual-counter framing is withdrawn as
launder-prone; the single operational counter is the consecutive qualifying-PASS count,
which is ZERO. See the F-AA-R5 appendix.]
Appendix: v0.4 -> v0.5 amendments (fifth round F-AA-R5, Perplexity Model Council:
findings-bearing NON-PASS) [new in this artifact]
Per Section 14.5 no prior finding text is edited in place; the superseded R4 dual-counter
conclusion is annotated above, and this documents the round.
The round. The closing round was run as a Perplexity Model Council of three members in clean,
independent instances: GPT 5.5 (OpenAI) and Gemini 3.1 Pro (Google), both qualifying, and
Claude Opus 4.8 (Anthropic -- the producing lineage), quarantined as advisory-only under
Standing Rule 7. The council was the first vehicle in this series to (a) confirm genuinely multifamily independence with per-member attribution and (b) execute live data reproduction.
Synthesized
qualifying-member
verdict:
FINDINGS-BEARING
NON-PASS
/

INCOMPLETE (GPT 5.5: NON-PASS, 0 CRITICAL / 2 HIGH; Gemini 3.1 Pro:
INCOMPLETE-NON-PASS, 0 CRITICAL / 1 HIGH). The consecutive qualifying-PASS streak
is therefore ZERO.
What reproduced (the substantive win). Despite the missing package, the qualifying members
independently reproduced the substance from live New York Open Data, and it all matched the
producer's verified figures and each other: 37,988 rows across the three vintages; FY2024 face
$65,189,755,228.64 and annual expenditure $8,170,228,558.54; MWBE 18.7345 / 3.9532 /
7.0612 percent; top-10 face concentration 30.4151 percent; positive-face-vendor Gini 0.93117
and annual-expenditure Gini 0.90435; pre-2024 face share 91.6876 percent; 1,348 missing / 48
explicit-zero; 18-field pairwise vintage overlaps 2,115 / 604 / 1,002 with exact all-field overlap
0; and the capital join resolving through project_number / proj_num with wcsa-vkhf
carrying no borough key. This is the first genuinely-independent executed reproduction of the
numbers in the five-round history; the estimand, stock/flow, descriptive-MWBE, structuralconcentration, and vintage-overlap framing are confirmed sound by two non-producer families.
(Gemini reported an alternate 0.937 Gini and a mixed overlap triplet; the council and the
producer both find this a member-level method variance -- a different denominator and mixed
pairwise/three-way intersection -- not data drift, since GPT, Claude, and the producer all
independently obtain 0.93117 and 2,115/604/1,002.)
Findings absorbed in v0.5:
•

•

•

•

F-AA-R5-C-01 (HIGH) -- ABSORBED (producer part); deposit OPEN. The reader
note and companion describe an accompanying frozen reproduction package, but it was
not in the audit packet and is not recoverable from the artifact's cited DOIs (which are
related works). This blocked the mandatory offline/self-test/live-comparator steps.
Producer part: Section 8 now states the package is a single named file that must be
handed directly to auditors, that its own DOI is pending deposit, and that the cited
Zenodo DOIs are not this package; the package file is included in the deliverables. Full
closure requires the owner to deposit the package to an immutable archive with its own
DOI.
F-AA-R5-C-02 (HIGH) -- ABSORBED. The artifact carried two convergence counters
("one of two on the letter" beside "ZERO"), which the council flagged as unstable and
launder-prone (it could promote the non-reproducing R4 into a convergence claim).
Collapsed to a single operational counter -- the consecutive qualifying-PASS count,
which is ZERO -- in the reader Sections 6 and 7 and the companion Current State; the R4
dual-counter conclusion is annotated as superseded. This also corrects the over-generous
R4 crediting from the prior turn.
F-AA-R5-C-03 (MEDIUM) -- ABSORBED. The provenance sentence attached "under
0.1 percent" to a claim reporting both record count and dollar sum; the face-value
divergence is about 0.089 percent but the record-count divergence is about 0.51 percent.
Section 3 now states the two separately.
F-AA-R5-C-04 (INFO) -- NOTED. Principal totals, MWBE shares, stock/flow
distinction, concentration, pre-2024 share, missing/zero split, and 18-field fingerprint all
reproduce; substantive framing preserved.

Next audit cycle. The single most valuable outcome of R5 is that the substance is now
independently reproduced by two non-producer families -- the data, implementation, and framing
are sound. What blocks convergence is no longer substance but process: (1) deposit the
reproduction package to an immutable DOI and include it in the packet; (2) then run a fresh nonClaude qualifying council (or two consecutive qualifying auditors) with the package present, so
the mandatory executed-reproduction steps run against the frozen artifact and return, twice
consecutively, 0 CRITICAL and 0 HIGH. The consecutive qualifying-PASS count is ZERO and
both passes remain to be earned.
Appendix: v0.5 F-AA-R6 sixth round (Perplexity Model Council): QUALIFYING PASS
(first of two required) [new in this artifact]
The round. Rerun of the closing Model Council with the reproduction package now bundled in
the packet. Three members in fresh, memoryless, isolated instances: GPT 5.5 (OpenAI) and
Gemini 3.1 Pro (Google), both qualifying, and Claude Opus 4.8 (producing lineage),
quarantined advisory-only. Both qualifying members completed all seven mandatory execution
steps against the attached package, with pasted tool outputs, and both returned 0 CRITICAL, 0
HIGH. Synthesized qualifying verdict: PASS. This is the first round in the six-round history that
is simultaneously (a) genuinely independent (two non-producer families), (b) an actual executed
reproduction (scripts run, data queried, outputs shown), and (c) passing.
Executed evidence (both qualifying members, independently). Snapshot hash and 22-field
inventory validated; 37,988 rows; FY2024 face $65,189,755,228.64, annual expenditure
$8,170,228,558.54; MWBE 18.7345 / 3.9532 / 7.0612 percent; top-10 face concentration
30.4151 percent; positive-face-vendor Gini 0.93117, annual-expenditure Gini 0.90435; pairwise
18-field vintage overlaps 2,115 / 604 / 1,002 with exact all-field overlap 0; self-test detecting all
45 perturbations; live comparator no-drift exit 0; adversarial one-cell mutation producing
nonzero exit; provenance separated (face divergence about 0.089 percent, count divergence
about 0.51 percent); capital join demonstrated with wcsa-vkhf carrying no borough key. The
method specifications in the brief eliminated the prior round's member-level Gini/fingerprint
variance: all members obtained 0.931 and 2,115/604/1,002.
Finding absorbed in this correction: - F-AA-R6-01 (MEDIUM) ABSORBED. The
companion header (line 3) still described the reader note as v0.4 while the reader, companion
line 5, and Current State block said v0.5 -- a recurrence of the version-propagation defect (the
same family as F-AA-R2-05, F-AA-R3-01/02, F-AA-R5-C-02), and one the producer had twice
written a standing rule against and still committed. Corrected: line 3 now reads v0.5. To make
the standing rule enforceable rather than aspirational, the producer now runs a mechanical check
that every version string across the reader note and companion is identical before delivery, rather
than relying on manual propagation.
Non-blocking member observations (no artifact defect): GPT 5.5 noted a LOW that the
packet ZIP bundles artifacts rather than a separate brief file (a packet-assembly observation, not
an artifact defect) and an INFO refining capital-key coverage to near-complete (a full-key query
matched 2,608 of 2,609 wcsa-vkhf project numbers, with L50502SX absent from both
allocation views). The reader note claims join feasibility and defers the by-geography analysis; it
does not claim universal key coverage, so no correction is required, though the near-completenot-universal nuance is recorded here.

Next audit cycle. The consecutive qualifying-PASS count is ONE. One further qualifying pass
-- two qualifying members, executed reproduction, 0 CRITICAL and 0 HIGH -- on this corrected
v0.5 artifact completes the two-consecutive-pass convergence gate. The reproduction package
must again be bundled in the packet. The immutable-DOI deposit of the package (F-AA-R5-C01) remains the owner's open action and would make the reproduction fully arm's-length; it is not
required for the pass but strengthens it.
Appendix: v0.5 -> v0.6 amendments (seventh round F-AA-R7, rotated Model Council:
findings-bearing NON-PASS, count reset to ZERO) [new in this artifact]
The round. The closing round was rerun with the package bundled and, per the brief's
recommendation, rotated membership: qualifying members GPT 5.5, GPT 5.4 (new relative to
R6), and Gemini 3.1 Pro, with Claude Opus 4.8 quarantined. All qualifying members executed
the reproduction and reproduced every figure exactly. Verdict: findings-bearing NON-PASS.
Two qualifying members (GPT 5.5 and the rotation member GPT 5.4) independently returned
the same HIGH finding; Gemini returned 0/0 but non-decisively (execution defects). A
qualifying PASS requires at least two qualifying members at 0 CRITICAL / 0 HIGH; that was
not met. Per the reset rule, the consecutive qualifying-PASS count returns from ONE to ZERO.
F-AA-R7-01 (HIGH) ABSORBED. The round-status and convergence-counter prose was not
propagated when F-AA-R6 was absorbed: the reader note header and Sections 6 and 7, and the
companion header line 5, still stated the pre-R6 state ("consecutive qualifying-PASS count
ZERO; five audit rounds; none has occurred"), directly contradicting the companion's
authoritative Current State block ("F-AA-R6 QUALIFYING PASS; count ONE"). The same
single operational counter thus read ZERO in the reader note and ONE in the companion -- the
dual-counter contradiction the brief's own regression checklist requires be absent -- and "none
has occurred" was false. This is the sixth appearance of the version/status-propagation failure
family (F-AA-R2-05, F-AA-R3-01/02, F-AA-R5-C-02, F-AA-R6-01), and the producer's prior
mechanical fix was too narrow: it checked version-label strings (which did stay consistent at
v0.5, so F-AA-R6-01's version-label target passes) but not the round-count/counter prose, where
the contradiction lived. Corrected in v0.6: the reader header, Sections 6 and 7, and companion
header are all updated to the authoritative post-R7 status (seven rounds; R6 first qualifying pass;
R7 NON-PASS; counter ZERO), and the mechanical pre-delivery check is widened to compare,
across every current-status locus, the version string AND the counter value AND the round
count.
Substance (unchanged, re-confirmed). All members reproduced 37,988 rows; FY2024 face
$65,189,755,228.64, expenditure $8,170,228,558.54; MWBE 18.7345 / 3.9532 / 7.0612 percent;
top-10 30.4151 percent; Gini 0.93117 / 0.90435; pre-2024 91.6876 percent; 1,348 / 48; pairwise
overlaps 2,115 / 604 / 1,002, exact all-field 0; self-test 45/45; live no-drift exit 0. GPT 5.5
executed the adversarial step to spec (re-hash manifest, --live returns DRIFT exit 2); Gemini
stopped at the hash abort, confirming integrity-hash detection but not the comparator
requirement. Capital join 40/40 with no borough key. The data, implementation, and framing
remain sound; the NON-PASS is entirely the producer's status-propagation defect.
Next audit cycle. Count is ZERO; two consecutive qualifying passes are again required. The
substance has now been independently executed and reproduced by three non-producer members
across two rounds (R6, R7), so the analytic content is as verified as the program can make it;

what has twice broken a closing pass is the producer's own status propagation. The immediate
producer obligation is to hold the round-status/counter prose consistent across all loci (now
mechanically checked on both version and counter). The package-DOI deposit (F-AA-R5-C-01)
remains the owner's open action.
Appendix: v0.6 -> v0.7 amendments (eighth round F-AA-R8, rotated Model Council:
QUALIFYING PASS, count to ONE) [new in this artifact]
The round. Rerun of the closing round on the R7-corrected v0.6 artifact with the package
bundled and rotated membership. Qualifying members GPT 5.5, GPT 5.4 (rotation, new relative
to R6), and Gemini 3.1 Pro; Claude Opus 4.8 quarantined advisory-only. All three qualifying
members executed all seven mandatory steps against the attached package with pasted outputs
and each returned 0 CRITICAL, 0 HIGH. Synthesized qualifying verdict: QUALIFYING
PASS. Per the counter rule this moves the consecutive qualifying-PASS count from ZERO to
ONE; it is the first of the two consecutive qualifying passes convergence requires, not the
second.
Regressions confirmed clean. The F-AA-R7-01 status-propagation defect is resolved: all
qualifying members confirmed the version string (v0.6 at audit time), the consecutive qualifyingPASS counter (ZERO entering the round), and the round count (seven) were mutually consistent
across the reader header, reader Sections 6 and 7, companion header, and Current State block.
The R7 execution defects are not repeated: all three qualifying members demonstrated
comparator-nonzero (exit 2, DRIFT) after mutating a non-MWBE amount and re-hashing the
manifest, and Gemini returned the exact 13,718 provenance count with no off-by-one. Substance
reproduced exactly by all members and the synthesizer's independent ground-truth pre-execution:
37,988 rows; FY2024 face $65,189,755,228.64 and expenditure $8,170,228,558.54; MWBE
18.7345 / 3.9532 / 7.0612 percent; top-10 30.4151 percent; Gini 0.93117 / 0.90435; pre-2024
91.6876 percent; 1,348 / 48; pairwise overlaps 2,115 / 604 / 1,002, exact 0; self-test 45/45; live
no-drift; capital join with no borough key.
Finding absorbed: - F-AA-R8-01 (MEDIUM) ABSORBED. The Current State "Independent
audit history" bullet led with "three independent cross-instance rounds attempted, all NONPASS" as a scoped lead-in to its rounds 1-3 sub-paragraph; one qualifying member (GPT 5.5)
flagged that it can be misread as a total-round-count claim against the actual eight-round history.
The other members read it as correctly scoped and did not flag it. Non-blocking (MEDIUM; the
operational counter and the full round sequence are stated correctly in the same block). Corrected
in v0.7: the lead-in is now explicitly scoped to rounds 1-3 and points to the counter bullet for the
full sequence. Recorded as another member of the version/round-status wording family, though a
much milder one than the count-contradiction of F-AA-R7-01.
Next audit cycle. The count is ONE. One further qualifying pass -- at least two qualifying
members, executed reproduction, 0 CRITICAL and 0 HIGH -- on this corrected v0.7 artifact
completes the two-consecutive-pass convergence gate. Keep the package bundled and the
membership rotated. The producer's pre-delivery mechanical check now covers version, counter,
and round count across all current-status loci; it was run on this v0.7 revision. The package-DOI
deposit (F-AA-R5-C-01) remains the owner's open action and would make the reproduction fully
arm's-length.

Appendix: v0.7 F-AA-R9 ninth round (rotated Model Council, FINAL): QUALIFYING
PASS -- convergence MET [new in this artifact]
The round. The convergence-closing round on the v0.7 artifact, package bundled, rotated
membership retained: qualifying members GPT 5.5, GPT 5.4, Gemini 3.1 Pro, with Claude Opus
4.8 quarantined. All three qualifying members executed all seven mandatory steps against their
own isolated copy of the attached package, pasted real outputs, and each returned 0 CRITICAL,
0 HIGH. Synthesized qualifying verdict: QUALIFYING PASS. Together with F-AA-R8 this is
the second consecutive qualifying pass, so the two-consecutive-qualifying-pass convergence
gate under Standing Rule 7 is MET on the v0.7 artifact.
Regressions confirmed clean. The status-propagation family (F-AA-R7-01, F-AA-R8-01) is
resolved: all qualifying members independently confirmed the version (v0.7), the counter (ONE
entering the round), and the round count (eight) were mutually consistent across the reader
header, reader Sections 6 and 7, the companion header, and the Current State block, and that the
audit-history lead-in is scoped to rounds 1-3. The R7 execution defects were not repeated; the
adversarial step returned comparator DRIFT (exit 2) for all members. Substance reproduced
exactly by all three members and the producer's own independent recompute: 37,988 rows;
FY2024 face $65,189,755,228.64, expenditure $8,170,228,558.54; MWBE 18.7345 / 3.9532 /
7.0612 percent; top-10 30.4151 percent; Gini 0.93117 / 0.90435; pre-2024 91.6876 percent;
1,348 / 48; pairwise overlaps 2,115 / 604 / 1,002; exact all-field 0; three-way 18-field
intersection 265 (a real, non-claimed value; see F-AA-R9-01).
Sole finding (non-blocking, brief-level). F-AA-R9-01 (LOW): the Round-9 brief mis-described
the fingerprint by implying no three-way intersection exists; the 18-field three-way intersection
is 265. The artifact itself never makes that claim and reproduces every published figure exactly,
so there is no artifact defect; the correction applies to future briefs.
Convergence declaration and its honest limits. Convergence under Audit Framework v3.0,
Standing Rule 7 is met on the v0.7 artifact: two consecutive qualifying passes (F-AA-R8, F-AAR9), each with at least two qualifying non-producer members, executed reproduction, and 0
CRITICAL / 0 HIGH. Recorded limits, so the claim is not read as more than it is: the two
decisive passes used the same three-member set (independence between them rests on fresh
instances, not disjoint membership); they audited materially-identical rather than byte-identical
substance; and the reproduction package's immutable-DOI deposit (F-AA-R5-C-01) remains an
owner-side action [updated at v1.0 per Section 14.5: F-AA-R5-C-01 is now CLOSED; the
package is deposited alongside this ledger at DOI 10.5281/zenodo.21445556]. The broader
evidentiary record is stronger than the two-pass minimum: across nine rounds, four distinct nonproducer models (GPT 5.6, GPT 5.5, GPT 5.4, Gemini 3.1 Pro) independently reproduced every
published figure from the frozen snapshot and the live endpoint, and the descriptive framing
survived adversarial review throughout.
Remaining owner actions (post-convergence, not audit rounds). (1) Deposit the reproduction
package to an immutable archive with its own DOI and wire that DOI into Section 8, closing FAA-R5-C-01. (2) If desired, promote the version label from v0.7 to an unqualified v1.0 to mark
the converged state (the label promotion is an owner decision; convergence itself is met on v0.7).
(3) Final render/deposit of the reader note and companion. No further audit round is required
unless the substance changes.

Appendix: v0.7 -> v1.0 canonical promotion and deposit [new in this artifact]
Following convergence (F-AA-R8 and F-AA-R9, two consecutive qualifying passes on
materially-identical v0.7 substance), the owner promoted the artifact to its canonical v1.0 release
and assigned DOIs. No analytic content changed between converged v0.7 and v1.0; the
promotion assigns identifiers and deposits the reproduction package.
•
•
•

Reader note (paper): DOI 10.5281/zenodo.21445552.
This audit and provenance ledger: DOI 10.5281/zenodo.21445556.
Reproduction package: deposited under an immutable DOI alongside this ledger at DOI
10.5281/zenodo.21445556. This closes F-AA-R5-C-01, the last open item: the frozen
snapshot, manifest, and reproduce_paper2.py now have a citable, arm's-length
home, so any party can retrieve and re-run the reproduction without being handed the
files.

The convergence caveats recorded in the Current State block continue to apply unchanged: the
two decisive passes shared the same three-member qualifying set (independence between them
rests on fresh instances, not disjoint membership), and they audited materially-identical rather
than byte-identical substance. v1.0 does not alter or strengthen those; it records the converged
state with permanent identifiers. No further audit round is required unless the substance changes.



Bismillah ir-Rahman ir-Rahim
