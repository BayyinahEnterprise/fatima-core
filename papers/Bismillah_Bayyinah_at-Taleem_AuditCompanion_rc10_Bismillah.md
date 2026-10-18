Bismillah ir-Rahman ir-Rahim

Bayyinah at-Taʿlīm -- Audit and Provenance Companion
Companion to: Bayyinah at-Taʿlīm: Structural Honesty Verification for Educational Fairness
Systems, from Primary Schooling to Graduate Research (the reader-facing paper). DOI:
10.5281/zenodo.21436486 . Reader-facing paper: DOI 10.5281/zenodo.21436484 .
Prepared under BayyinahEnterprise audit methodology (PMD v1.2, Audit Framework v3.0).
Mirrors paper state v1.0-rc10 (four rounds recorded; convergence-counting decision pending
owner). Human authorship and copyright to be assigned by project lead (Bilal Syed Arfeen);
Claude (Anthropic) credited as collaborative research tool.

About this companion
This document is the append-only audit trail for the reader-facing paper. It exists so that any
claim in the paper can be traced to how it was established, and so that every error caught and
corrected during development remains on the public record rather than being silently smoothed
away. Preserving this trail is itself load-bearing: it is the demonstration that the paper practices
the structural honesty it proposes.
It contains four parts: the full per-claim Verification Status; the complete findings ledger in three
namespaces (F-ED development findings, F-RV producer-lineage continuity review, F-PR
internal peer review), each in the six-element format the methodology requires; the paper-level
falsifiability criteria; and the append-only version ledger from v0.1 through v1.0-rc6 with its
Next Audit Cycle status.
Section numbers referenced inside the findings and ledger (for example "Section 4.4.6," "Section
3," "Section 4.1") refer to the reader-facing paper. Finding disposition tags (RESOLVED,
PARTIALLY-RESOLVED, ABSORBED, OPEN, RESOLVED-AND-RETAINED) and
severity tokens (CRITICAL, HIGH, MEDIUM, LOW) follow the Audit Framework severity
rubric. Per Bayyinah Audit Framework v3.0 Section 14.5, superseded text is preserved verbatim
in the ledger and corrected by annotation, never edited in place.
Convergence status, stated plainly: the paper is producer-complete, and one of the two required
independent audit rounds has now passed. It carries 0 open CRITICAL findings and nothing
open above LOW. The methodology's convergence criterion -- two consecutive audit rounds by
a Tier 1 auditor outside the authoring lineage, each returning 0 CRITICAL and 0 HIGH -- is not
yet fully met: a first independent, non-lineage audit round (namespace F-XA, performed by a
non-Anthropic auditor) returned PASS at 0 CRITICAL and 0 HIGH with 6 LOW findings, all
now absorbed (see the v1.0-rc7 -> v1.0-rc8 appendix). A second independent round (namespace
F-AT-R2, also a non-Anthropic auditor) then reproduced the results and also returned 0
CRITICAL and 0 HIGH (1 MEDIUM, 1 LOW, absorbed in v1.0-rc9). However, that auditor
expressly attested its round was NOT qualifying for convergence: it shares the OpenAI/GPT
model family with the first-round auditor, and it did not run in a fresh, carryover-free context. By
the Knight-Leveson correlated-blind-spot standard this program applies, two rounds from the
same model family in shared context do not satisfy the independence the gate intends. A third

round (namespace F-AT-R3) then supplied that different family: a Gemini auditor in a fresh
context passed at 0 CRITICAL and 0 HIGH (2 INFO), the first fully-qualifying different-family
round, though its report asserted rather than showed its recomputation. A fourth round
(namespace F-AT-R4-NQ) was requested from the GLM/Zhipu family but was performed by a
Claude/Anthropic instance -- the producing lineage itself -- which honestly self-identified and
declared its own round NON-QUALIFYING; it is a producer-side regression reproduction
(thorough, arithmetic shown, 0 CRITICAL / 0 HIGH, 1 LOW and 2 INFO absorbed into v1.0rc10), not a qualifying round. Authoritative current status: convergence is NOT met. Exactly
one qualifying different-family round (Gemini, F-AT-R3) has occurred; a second qualifying
round -- ideally a genuinely distinct family that shows its arithmetic, on the current artifact -- is
still required, and because v1.0-rc10 changed two reference entries from rc9, that second round
should be run on rc10 (the substance is identical; only the Guryan and Chouldechova reference
entries differ). Any absorption of findings is a producer-lineage revision and does not itself count
as a round. Neither the earlier F-RV continuity review nor the F-PR peer review counted,
because both were producer-lineage (Standing Rule 7); the rc5 and rc6 external passes were nonlineage but targeted, not full severity-scored rounds. The single remaining blocking item to an
unqualified "shipped" status is that second passing independent round.

A. Verification Status
Per Framework Foundations v1.1 discipline, the epistemic provenance of this note's load-bearing
claims is stated explicitly so reviewers do not have to determine which claims are verified.
Read end-to-end by the authoring instance (methodology): SHV: A New Frontier
(20131072); Bayyinah at-Tartīb (20070782); Al-Mutaffifīn (19894724); Bayyinah al-Munāsabāt
(20069654); the bayyinah-audit skill references (findings-format, severity-rubric, em-dashpolicy, producer sub-skill).
Read end-to-end by the authoring instance (worked-example sources), v0.2 baseline: NYC
Independent Budget Office (IBO), "Is It Getting Fairer? Examining Five Years of School
Funding Allocations Under Fair Student Funding," April 2013 (fsf2013); IBO, "FSF Formula
Changes Had Small Impact on School Budgets," May 29, 2025, and the full report. All Section
4.4 figures attributed to these two IBO sources are read end-to-end. Corrected in v1.0-rc2 (FRV-1): v1.0 (now relabeled v1.0-rc1) stated that a re-verification pass confirmed eight of nine
load-bearing IBO claims verbatim and downgraded one claim -- the specific category attribution
of "elementary and high-school ELL students, and high-school special-education CTT students"
as funded significantly below formula weight -- to partially confirmed, on the stated ground that
the attribution "was not located verbatim in the report's main text." A continuity review flagged
this as a retrieval-miss error, and re-fetching the report in this session confirms the review was
right: the report's section "Students Funded Below, Close to, or Above Formula Weight" states
the attribution verbatim, with supporting category-level figures (Section 4.4.2, F-ED-8). All nine
load-bearing IBO claims are now confirmed verbatim; none remain at partially-confirmed status.
This correction is logged rather than smoothed over precisely because the paper's own discipline
requires it, and because a retrieval failure that went undetected in one source is grounds for
lower, not higher, confidence in claims from sources this instance could not independently recheck (see the recompute correction below).

Newly read end-to-end in v1.0: Voloch, Daniel (2015), Children First Reforms, Fair Student
Funding and the Displacement of Accountability in the New York City Department of Education,
CUNY Graduate Center Ph.D. dissertation -- the school-level 81-to-134-percent range, the 8.5
percent (n=38) fully-funded figure, the 86.19 percent median, and the statistically significant
inverse relationship with enrollment size and low-income/ELL share are all now confirmed
verbatim from the dissertation's abstract and corroborated independently by the NYU Steinhardt
Metro Center. This claim is promoted from snippet-level to Tier 2 end-to-end verified. See
Section 4.4.2.
Newly obtained and read end-to-end in v1.0 (primary formula data): NYC DOE Fair
Student Funding Public App FSF Detail Reports, FY2023, for five sample schools (28Q160,
10X085, 30Q258, 14K488, 30Q148) -- the disclosed allocation walkthrough line items (an
aggregate prior-year weighted register, a base per-pupil rate, teacher-salary and register-change
adjustments, the $225,000 foundation, and three collective-bargaining/state-aid terms) plus the
reported total, obtained via direct browser interaction (the app requires JavaScript postbacks and
is not accessible via automated HTTP fetch). Cross-checked against the NYC Comptroller's
FY2023/FY2024 School Budget Allocations Mastersheet and the FY2023 FSF Guide and
weight/per-capita table. Used for the independent recompute in Section 4.4.6 and F-ED-10.
Corrected in v1.0-rc2 (F-RV-2, F-RV-3): two problems with how this recompute was
originally presented are now fixed. First, Tier: v1.0-rc1 labeled the recompute Tier 1; it is Tier 2
(Structural) by this paper's own definition in Section 3, because reproducing the DOE's published
total depends on a disclosed parameter choice (report vintage, Initial versus Final) rather than
being parameter-free. Second, reproducibility: the reviewing instance in the continuity review
attempted to independently re-run this recompute and could not, because the DOE FSF Public
App returned robots-disallowed and the NYC Comptroller mastersheet returned an Incapsula
bot-detection challenge to its automated access attempts. The recompute is therefore tagged
single-instance, not independently reproduced rather than presented as settled. The underlying
five-school extract and mastersheet rows have not yet been archived as a companion dataset;
doing so is the concrete fix and is logged as an open action item (F-ED-11; Next Audit Cycle).
Corrected in v1.0-rc4 (F-PR-2): independent reproduction from the now-archived dataset
showed that the extract contains an aggregate prior-year weighted register and the DOE
walkthrough line items, not category-level weighted-register breakdowns; the earlier phrase "full
category-level weighted-register breakdowns" overstated what was captured and is corrected
above. The recompute is accordingly an internal-consistency check (walkthrough terms sum to
the reported total) plus a cross-source match (DOE total equals the Comptroller "Initial"
column), not a formula reconstruction from weighted registers and per-capita weights; the
original Falsifiability item 2 (formula = foundation + sum of weight times per-capita) remains
not performed. See F-ED-13.
Independent verification pass, absorbed in v1.0-rc5, provenance corrected in v1.0-rc6 (nonlineage; resolves F-ED-13 and F-ED-14 on the merits). After v1.0-rc4 and its companion
dataset were shared, a non-lineage party independently re-derived the F-ED-10 decomposition
(confirmed exact for all five schools, including 28Q160's $1,376 relief against a $94,292 swing)
and supplied two new primary-source results. Provenance is tagged per claim; the two sourceaccess tags below are corrected in v1.0-rc6 from v1.0-rc5's own wording, per the reviewer's own
follow-up report (see Appendix, v1.0-rc5 -> v1.0-rc6 amendments). - Reviewer-verified in this
session: the walkthrough's teacher-salary-change term equals fy22_register times ($4,197.19

minus $4,223.00) to under $1 for all five schools (max deviation $0.78, school 14K488), so
base(FY2022 rate) plus teacher-salary-change equals fy22_register times $4,197.19 (the FY2023
rate on the FY2022 register). This identity independently corroborates that $4,223.00 is the
FY2022 base rate and $4,197.19 the FY2023 rate, because the arithmetic only closes at exactly
those two values. - Reviewer-fetched and confirmed verbatim in this session (corrected in v1.0rc6; v1.0-rc5 tagged this user-supplied-not-reviewer-fetched): the DOE FSF Working Group
Meeting 3 deck (infohub.nyced.org) publishes a year-by-year Base Weight Amount table -FY2021 $4,137.85, FY2022 $4,223.00, FY2023 $4,197.19 -- and attributes FY2023's decrease to
average teacher salary falling for the first time in several years due to increased retirements. The
reviewer fetched this deck directly from the source URL in this session; the full table returned
with no robots block encountered by the reviewer's fetch method. This matches the reviewerverified identity above and closes F-ED-14. - Reviewer-obtained via live browser automation
and independently recomputed in this session (corrected in v1.0-rc6; v1.0-rc5 tagged this userperformed-not-reviewer-reproduced): a category-level Detail Report pull (Grade Weight,
Academic Intervention, ELL, Special Education, Portfolio, with per-category counts and dollars)
for all five schools, obtained by the reviewer directly via live browser automation against the
DOE FSF Public App, from which the reviewer independently confirmed the category dollars
sum to the register-times-rate base and reconstructed the full walkthrough as (FY2022 register
times FY2022 rate) + teacher-salary-change (bridges to the FY2023 rate) + register-change
adjustment (bridges FY2022 to FY2023 register at approximately the base rate) + foundation +
collective-bargaining terms, matching the DOE-reported total to within $2-$18 for all five
schools. The register-change adjustment uses a single blended base rate and carries a $1 to $60
residual, since category-specific per-capitas differ; a fully category-exact reconstruction is the
remaining refinement. This category-level data is browser-obtained and is not yet in the
companion dataset; adding it is the remaining reproducibility step (F-ED-13, Next Audit Cycle).
Newly pinned in v1.0 (F-ED-1 remediation/retention evidence base): the full citation list is
given under mechanism ED-K4 (Section 4.1) and includes, among others, Jacob & Lefgren
(2009), Nomi & Allensworth (2013), Geng & Rockoff (2017), Balu et al. (2015), IES/MDRC
national RTI evaluation, Westall, Utter & Strunk (2023), Michigan Read by Grade Three,
Cook/Guryan et al., "Not Too Late", and Nickow, Oreopoulos & Quan (2024). These replace the
summary-level citations carried in v0.2. Provenance caveat added in v1.0-rc2 (F-RV-4):
"pinned" here means each figure carries a source URL supplied by a dedicated remediationpathway research pass; it does not mean each figure was individually re-verified end-to-end by
the producing instance the way the FSF and Voloch figures were. The negative RTI effect size
(Balu et al. 2015, −0.17 SD, p = 0.002) and the Michigan disparity figures (Westall, Utter &
Strunk 2023) were checked against source abstracts during that research pass; the remaining
figures under ED-K4 (the Nickow/Oreopoulos/Quan pooled effect, the Cook et al. tutoring
effects, the Mississippi program cost and effect-size figures, and the Saga Education per-pupil
cost range) are cited-not-yet-individually-verified pending a dedicated verification pass. See FED-11.
Corrected in v1.0: the FY2023 100-percent-funding-floor announcement ("1,164 schools and
over 700,000 students") is retraced to an April 19, 2021 announcement by Mayor Bill de Blasio,
Council Speaker Corey Johnson, and Chancellor Meisha Porter, committing to fund all schools
at 100 percent of FSF formula starting in the 2021-22 school year -- not a January 2023
Adams/Banks announcement, and not literally "FY2023." The January 2023 Adams/Banks

announcement was a distinct proposal concerning the Students-in-Temporary-Housing and
Concentration-Need weights (the precursor to the FY2024 changes IBO's 2025 report measures).
See Section 4.4.2 and the Appendix ledger.
Public record: NYC Office of the Mayor announcements (April 2021, January 2023); NYC
Public Schools FSF Guide FY2023; Fair Student Funding Working Group Final Report
(November 2022).
Read in abstract and structural-head only (corpus siblings, not load-bearing here): Furqan
thesis (20132214), furqan-lint thesis and white paper (20101645, 20101580), Audit Framework
Application Brief (20031395), Cross-Text Computational Linguistics (19961267), Bayyinah alMaal (19875931), Bayyinah input-layer defense (19802455), Al-Khalifa (19776577), Bilal
(19776576), Predictive Audit Chains (20093407).
Empirical magnitude, stated at corpus-honest level (governs every use of the phrase
"mathematical nature of the Qur'an"): per Bayyinah al-Munāsabāt (20069654), approximately 82
percent of the canonical-versus-random long-range autocorrelation gap is attributable to the
canonical's approximate length-sort; the residual intra-quartile ordering effect is approximately
+0.10 to +0.15, statistically significant after Bonferroni correction at lag 5 but not at lag 10
(empirical p = 0.030). Per Cross-Text Computational Linguistics (19961267) Verification Status,
the earlier claim that Fibonacci growth is Quran-specific, carried in four prior papers, was
falsified and corrected. Consequence for this note: the Qur'an is a source of design primitives and
diagnostic vocabulary, plus one small candidate structural-ordering effect. It is not a validated
quantitative instrument for adjudicating educational outcomes. Any mechanism requiring it to be
one is refused under the Tier discipline (Section 3).
Status, honestly stated: v1.0-rc2 is producer-complete, not cross-instance-converged. v0.2's
"blocking path to v1.0" listed five items. The four that fall within the producing instance's own
authority have been completed: (1) project-lead disposition of F-ED-1 obtained and applied; (2)
Voloch (2015) read end-to-end; (3) an independent formula recompute performed against
published DOE data for a 5-school FY2023 sample; (4) pinned citations supplied for the F-ED-1
education-research claims. Item (5) -- cross-instance audit by a Tier 1 auditor other than the
producing instance, with convergence at two consecutive rounds of 0 CRITICAL and 0 HIGH -has not been performed in this session, because no separate reviewing instance was available.
This version therefore carries 0 open CRITICAL findings and is producer-complete, but the
paper's own convergence criterion for an unqualified "shipped" status is not yet met. This is
logged honestly rather than smoothed over, per the discipline this note itself imposes on the
systems it audits.
Continuity review received and absorbed (v1.0-rc2). After the file above (now relabeled v1.0rc1) was shared, a producer-lineage continuity review (namespace F-RV) was received, reporting
0 CRITICAL, 1 HIGH, 3 MEDIUM, 2 LOW. Per the review's own Provenance Disclosure and
Standing Rule 7, the reviewing instance had authored v0.1 and v0.2 of this paper, so its findings
are advisory and explicitly do not count toward the item-5 convergence criterion -- item 5
remains fully open regardless of this review's outcome. Before absorbing any finding, F-RV-1
(HIGH) was independently re-checked against the primary source in this session by re-fetching
the IBO 2013 report directly; the report does state the disputed attribution verbatim, confirming
the review was correct and v1.0-rc1's downgrade was a genuine retrieval-miss error. All six

findings are absorbed in this version: F-RV-1 (claim restored, Section 4.4.2 and F-ED-8), F-RV2 and F-RV-3 (recompute reclassified Tier 2 and tagged single-instance/not-independentlyreproduced, Section 3, 4.4.3, 4.4.6, and F-ED-10), F-RV-4 (ED-K4 citation provenance tagged
honestly above and in Section 4.1, with new finding F-ED-11), F-RV-5 (version label corrected
to v1.0-rc2; the prior file is v1.0-rc1 in this paper's history), and F-RV-6 (em-dash glyphs, a
rendering artifact of the authoring pipeline, replaced with the double-hyphen throughout). Item 5
-- independent cross-instance audit by a non-lineage Tier 1 auditor, two consecutive rounds of 0
CRITICAL and 0 HIGH -- remains the sole open blocking gate to an unqualified shipped status;
this review, however thorough, does not and cannot discharge it.
Citation verification pass completed (v1.0-rc3; discharges F-ED-11 action item 2). The four
ED-K4 remediation-pathway figures v1.0-rc2 flagged as cited-not-yet-individually-verified have
now been read end-to-end against primary sources; see F-ED-12 for the full disposition. Two
corrections surfaced. First, the Nickow, Oreopoulos & Quan pooled tutoring effect size was cited
as ≈ 0.37 SD; that number belongs to the 2020 NBER working paper draft (w27476) of the same
underlying study and to secondary summaries (J-PAL, the U.S. Department of Education) that
still
repeat
it.
The
peer-reviewed
2024
article
actually
linked
(DOI
10.3102/00028312231208687) reports a revised overall pooled ES of 0.288 SD (SE = 0.029, p
< .001), now the cited figure. Second, the Saga Education per-pupil cost figure was misattributed
to Mahmud (2025); that paper does not mention Saga Education. The correct source is Cook,
Dodge, Farkas, Guryan, Ludwig et al., "Not Too Late" (NBER w28531 / University of Chicago
Education Lab), which reports a defensible per-pupil cost range of $1,800 (current, AmeriCorpssubsidized, blended-learning model) to $4,800 (2013-2015 study period, 2:1 in-person model),
not "$1,900-$4,800." Three figures were confirmed exactly as stated: the Cook et al. pooled TOT
≈ 0.28 SD and 0.23 SD one-year-later persistence figures (matching the University of Chicago
Education Lab's hosted paper text verbatim; the NBER-hosted PDF draft carries marginally
different point estimates, 0.264/0.222 SD, ordinary cross-revision variation between workingpaper drafts of the same study), and the Mississippi Literacy-Based Promotion Act figures (≈$15
million/year; 29 coaches in 2013-14 rising to 74 by 2015-16; bare-mandate effect 0.014 SD, not
significant, versus Mississippi's funded-coaching model reaching 0.322 SD by 2019), all
confirmed verbatim against Mahmud (2025). The intent-to-treat-versus-treatment-on-treated "24x" gap claim is corroborated by the broader scale-up literature (e.g., a University of Chicago
Education Lab 2022-23 scale-up study reporting 0.04 SD ITT versus 0.14 SD TOT, a 3.5x gap)
but is not a statement made in the Nickow et al. 2024 paper itself, whose accessible text does not
discuss ITT/TOT at all; the citation is corrected to attribute this pattern to the scale-up literature
alone. See Section 4.1 and F-ED-12.
FY2023 recompute dataset compiled for archiving (v1.0-rc3; F-ED-11 action item 1, in
progress). The five-school FSF Detail Report walkthrough extract and the corresponding NYC
Comptroller mastersheet rows (F-ED-10) have been compiled into a documented companion
dataset package (CSV extracts, the recompute script, a README stating provenance and
license, and the supporting weight/per-capita reference table) so a second party can reproduce the
recompute without needing a live browser session against the DOE Public App. Publishing this
package to Zenodo (or an equivalent public archive) so it carries a citable DOI, matching this
paper's companion-paper convention, is the final step and had not yet been completed as of this
version; see F-ED-11 and Next Audit Cycle.

B. Findings
Ordered by severity, then locus. F-ED-1 through F-ED-7 were raised against the prior-session
draft; F-ED-8 through F-ED-14 against the worked-example target system and this paper's own
citation and reproducibility practices. Absorption status is annotated per finding (append-only;
original text preserved in the Appendix ledger).
F-ED-1 CRITICAL → ABSORBED [v1.0] -- Tanzīl phased-progression proposed as
fairness-optimizing is, as written, a grade-retention and tracking mechanism Locus: priorsession draft, section "Tanzīl Phased Progression." Substance: Surface claims fairness
optimization and guaranteed intervention; substrate is a hard prerequisite gate that stops
promotion. Grade retention and tracking are tied in the empirical record to disproportionate
pushout and elevated dropout among low-income and minority students. The gate detects nonmastery but did not, as originally proposed, fund remediation, so "guarantees intervention" was a
surface claim with no substrate behind it. Disposition: ABSORBED in v1.0 as ED-K4
(remediation-coupled mastery gate, Section 4.1), per the project lead's explicit disposition
("apply the required couplings"). The gate is refused unless both couplings are present, disclosed,
and logged: (a) an automatically-triggered, dosage-and-funding-disclosed, attendance-logged
remediation pathway; (b) an independent ED-K2 disaggregated subgroup regression gate,
retained as the primary safeguard because (a) has not been shown, anywhere in the literature
reviewed, to eliminate subgroup disparity on its own (Westall, Utter & Strunk 2023). Pinned
citations and honest caveats are given in full under ED-K4. Cross-reference: ED-K4, ED-K2; atTartīb 20070782 Section 6.2; severity-rubric CRITICAL boundary.
F-ED-2 HIGH -- Mizan-calibrated assessment claimed to "remove grading demographic
bias" [ABSORBED v0.2] Locus: prior-session draft, section "Mīzān-Calibrated Assessment."
Substance: Surface claimed bias removal; substrate cannot deliver it (calibration and equalized
error rates mutually exclusive once base rates differ; bias also in rubric, items, training data).
Disposition: ABSORBED as ED-U3 (Mizan-calibrated abstention), restated as three-valued
honest abstention with the bias-removal claim deleted and the impossibility result cited. Crossreference: ED-U3; Section 2.
F-ED-3 HIGH -- Reproducibility conflated with validation in the graduate graduation
trigger [ABSORBED v0.2] Locus: prior-session draft, section "Graduate & Master's Level
Research." Substance: Surface presented byte-deterministic reproduction as a graduationvalidation trigger; reproduction gates provenance (Tier 1), not merit (Tier 3). Disposition:
ABSORBED in ED-G1, reclassified as a necessary Tier 1 precondition, never sufficient; merit
stated as a retained human Tier 3 judgment. Cross-reference: ED-G1; Section 3 Tier falsifiability
rule.
F-ED-4 HIGH -- Immutable transcript ledger collides with the right to rectification
[ABSORBED v0.2] Locus: prior-session draft, sections "Additive-Only Transcript Ledgers" and
"immutable ledger." Substance: Surface claimed immutability as integrity; an immutable student
record conflicts with error correction, FERPA rights, and expungement. Disposition:
ABSORBED in ED-K2 and ED-G3 as append-only-with-correcting-entries (silent deletion
prohibited, logged correction permitted; §14.5). In a deployed system handling protected records
this escalates to CRITICAL (regulatory). Cross-reference: ED-K2, ED-G3; producer sub-skill
Step 5.

F-ED-5 MEDIUM -- Validator-by-Different-Instance claimed to "remove institutional
bias" [ABSORBED v0.2] Locus: prior-session draft, section "Undergraduate Programs."
Substance: Surface claimed bias removal across scope; substrate relocates bias to the validator
surface and applies only to rubric-gradeable outputs (N-version independence-failure).
Disposition: ABSORBED in ED-U2 as bias relocation with disclosed scope limits and the
Knight-Leveson caveat cited. Cross-reference: ED-U2; at-Tartīb 20070782 Section 4.5.
F-ED-6 MEDIUM -- "Al-Mutaffifīn dynamics" implies an analytic mechanism the surah
supplies [ABSORBED v0.2] Locus: prior-session draft, section "The Core Educational
Disconnect." Substance: Surface attributed analytic force to the surah ("dynamics reveals"); the
surah supplies the naming of the asymmetric-measure pattern, not a derivation mechanism.
Disposition: ABSORBED throughout; Al-Mutaffifīn used as canonical name only (Sections 2,
4.1, 4.4). The "dynamics reveals" framing does not appear in this paper. Cross-reference:
Verification Status; Section 2.
F-ED-7 MEDIUM -- "Mathematical nature of the Qur'an" framing risks Tier 3 leakage
relative to the deflated empirical magnitude [ABSORBED v0.2] Locus: research-program
framing carried into the education application. Substance: Surface phrase implies a validated
quantitative instrument; substrate per al-Munāsabāt is a residual +0.10 to +0.15 effect surviving
Bonferroni at lag 5 only, ~82 percent of the headline gap being length-sort, with Fibonaccispecificity falsified per Cross-Text. Disposition: ABSORBED in Verification Status and Section
3: the Qur'an is confined to primitive-source and vocabulary-source plus the one deflated
candidate effect; any mechanism requiring it as a validation instrument is refused. Crossreference: Verification Status; Section 3 Tier discipline.
F-ED-8 HIGH -- ED-K1 fires on the historical allocation-versus-formula divergence with
weight-category regressivity [RESOLVED-AND-RETAINED; magnitude verified v0.2;
corrected v1.0; corrected again v1.0-rc2] Locus: NYC DOE published FSF allocation and
formula amounts, FY2011 to FY2022 (IBO fsf2013); School Allocation Memoranda. Substance:
Surface (need-weighted equity, 100 percent of formula = fully funded) diverged from substrate
(FY2011 median 75.4 percent of formula, about 98 percent of schools below; FY2012 median
86.0 percent, 94.0 percent below). At the weight-category level, the negative implied weight for
below-standards students is confirmed (schools serving more such students received less
funding). Corrected in v1.0: the more specific v0.2 claim naming elementary/high-school ELL
and high-school special-education CTT students as funded significantly below formula weight
was downgraded to unconfirmed, on the ground that the attribution "was not located verbatim" in
the report. Corrected again in v1.0-rc2 (F-RV-1): that v1.0 downgrade was itself wrong. A
producer-lineage continuity review flagged it as a retrieval-miss error, and re-fetching the report
in this session confirms the review: the report's section "Students Funded Below, Close to, or
Above Formula Weight" states the attribution verbatim, naming middle-school students below
academic standards, elementary and high-school ELL students, and high-school specialeducation CTT students as funded below formula weight in 2011-2012 and at least two other
years, with supporting category-level figures (high-school ELL implied weights of 0.30-0.37
against a 0.50 formula weight; special-education CTT students receiving half or less of the 2.52
formula weight in the first two years). The claim is restored to confirmed. The Layer 1 resolution
announcement (April 19, 2021, de Blasio/Porter, 2021-22 school year, not a January 2023
Adams/Banks announcement) and the Voloch (2015) end-to-end verification are unaffected by
this continuity review and stand as corrected in v1.0. Disposition: Layer 1 RESOLVED per the

2021-22-school-year 100-percent floor (date/administration corrected v1.0); retained as the EDK1 demonstration and logged append-only with its resolution. Tier 1 ratio is ship-grade; the
specific ELL/CTT below-weight attribution is restored to confirmed (v1.0-rc2, correcting the
v1.0 error); the Voloch school-level relationship remains merged as an independently verified,
distinct Tier 2 claim. Cross-reference: ED-K1, ED-K2; Al-Mutaffifīn 19894724 Sections 2 and
4.1a; Section 4.4; F-RV-1.
F-ED-9 MEDIUM -- Tier boundary held on the current formula-adequacy layer [refusaldemonstration] Locus: NYC DOE FSF weights FY2024 to FY2025 (STH, Concentration
Need); IBO May 29, 2025. Substance: Current surface (the formula now captures concentrated
need) meets a substrate in which the corrective weights are small per pupil (about 78 dollars per
pupil STH; about 95,000 dollars average across 304 schools) and, per IBO, unlikely to move
system-wide outcomes, with possible budget instability. The framework emits the Tier 2
magnitude and refuses the Tier 3 adequacy verdict; IBO independently drew the same boundary.
Disposition: Emit Tier 2 magnitude and the scan-incomplete declaration; do not emit an
adequacy verdict. No absorption required; the mechanism is behaving correctly. Cross-reference:
F-ED-3, F-ED-7; Section 3 Tier falsifiability rule; Al-Mutaffifīn 19894724 Section 3.1.
F-ED-10 MEDIUM -- Walkthrough arithmetic is internally consistent and matches the
Comptroller Initial column, but the Initial-to-Final divergence is only partially explained
[PARTIALLY-RESOLVED; new in v1.0; Tier-corrected v1.0-rc2; decomposed v1.0-rc4]
Locus: NYC DOE FSF Public App Detail Reports versus NYC Comptroller FY23/FY24 School
Budget Allocations Mastersheet, for five sample schools (28Q160, 10X085, 30Q258, 14K488,
30Q148). Substance: Independently reconstructing each school's Total FY2023 FSF Allocation
from its DOE Detail Report's disclosed walkthrough terms (base allocation at the FY2022
register and $4,223.00 base rate, teacher-salary change, register-change adjustment, $225,000
foundation, and three collective-bargaining/state-aid adjustment terms) reproduced the DOE's
own published total to within $2-$18 (rounding) for all five schools. On first comparison, this
reconstructed total differed from the Comptroller mastersheet's "FY2023 Final" FSF figure for
the identical schools by amounts ranging from −2.2 percent (−$94,292, school 28Q160) to +12.5
percent (+$539,067, school 30Q258), non-uniform across schools -- large enough that citing "the
FY2023 FSF allocation" for a school without specifying report vintage would be a false claim.
Tracing the mastersheet's own columns resolved this rather than leaving it as an open
discrepancy: the recomputed/DOE-reported figure matches the mastersheet's "FY2023 Initial"
column exactly (to the same $2-$18 rounding) for all five schools, and the divergence from
"FY2023 Final" is only partially explained by the mastersheet's disclosed Register Relief
column. Corrected in v1.0-rc4 (F-PR-1): the v1.0-rc3 claim that this divergence is "fully
explained by Register Relief and a mid-year enrollment change" does not survive a per-school
decomposition against the archived data. The correct comparison is Initial FSF versus Final FSF
plus Register Relief, because relief exists to offset enrollment-driven register loss. Residuals
(Final FSF + Register Relief minus Initial FSF): 30Q258 +$1,007 and 14K488 +$10,521 (relief
offsets the enrollment loss; reconciles within about $11k), but 28Q160 +$95,668, 10X085 +
$218,563, and 30Q148 +$224,353 (a net-positive residual that relief and enrollment do not
explain). Most sharply, 28Q160's Final FSF rises $94,292 while its enrollment falls 12 students
and its Final Register Relief is only $1,376, so relief and enrollment cannot be the cause; the
residual for these three schools is consistent with a mid-year rate/collective-bargaining rebenchmark that the archived Initial-vintage walkthrough does not itemize. All five residuals are

positive, so once relief is included every sample school's FSF-side funding held at or above its
Initial level. Corrected in v1.0-rc2 (F-RV-2, F-RV-3): v1.0-rc1 labeled the walkthrougharithmetic result "a genuine Tier 1 byte-determinism result" and its Section 4.4.6 falsifiability
criterion as "Tier 1 valid once report vintage is disclosed." Both statements are corrected.
Because reproducing the DOE's published total depends on disclosing which report vintage
(Initial versus Final) is being matched, a disclosed parameter choice, the result is Tier 2
(Structural) by Section 3's own definition, not Tier 1: a Tier 1 label with a required disclosed
parameter is a contradiction in this paper's own terms. Separately, the reviewing instance in the
continuity review attempted to independently re-run this recompute and could not: the DOE FSF
Public App returned robots-disallowed and the Comptroller mastersheet returned an Incapsula
bot-detection challenge. The recompute is therefore also tagged single-instance, not
independently reproduced, until the underlying five-school extract and mastersheet rows are
archived as a companion dataset (see F-ED-11). Disposition: PARTIALLY-RESOLVED, Tier
reclassified (v1.0-rc4). The recompute is Tier 2 valid once report vintage (Initial versus Final) is
disclosed as a required parameter; Section 4.4.6's falsifiability criterion 2 is amended
accordingly, and the single-instance status is disclosed rather than presented as settled. The
Initial-to-Final divergence is partially, not fully, explained by the archived data: register relief
offsets the enrollment-driven change for two of five schools, and a net-positive rate/CB residual
(roughly $96k to $224k) remains for the other three that the Initial-vintage walkthrough does not
itemize. Scan-incomplete declaration: closing that residual requires the Final-vintage Detail
Report walkthrough per school, which is not in the archive and is logged as an open item at FED-13. The status is downgraded from RESOLVED to PARTIALLY-RESOLVED accordingly;
the v1.0-rc3 "fully explained" wording is preserved in the ledger per §14.5. The Tier mislabeling
in v1.0-rc1 remains recorded. Cross-reference: Section 4.4.6; ED-K1; F-ED-11; F-RV-2; F-RV3; source files: NYC DOE FSF Public App Detail Reports (28Q160, 10X085, 30Q258, 14K488,
30Q148), FY2023; NYC Comptroller FY23/FY24 Mastersheet.
F-ED-11 MEDIUM -- Citation-provenance discipline applied unevenly across the paper;
recompute raw data not archived for independent reproduction [ABSORBED; new in v1.0rc2, from continuity review F-RV-4 and F-RV-2] Locus: Verification Status (ED-K4 citation
paragraph); Section 4.1 mechanism ED-K4; Section 4.4.6 recompute (F-ED-10). Substance: This
paper distinguishes read-end-to-end, snippet-level, and pinned-not-verified provenance for its
worked-example claims (FSF allocation figures, Voloch), but had not applied the same discipline
to the ED-K4 remediation-pathway citations, which were described simply as "pinned" without
stating that pinning a URL is a weaker claim than individually re-verifying the figure end-to-end.
Separately, the FY2023 FSF recompute (F-ED-10) is a genuine result but currently exists only as
this producing instance's own extraction and computation; the underlying DOE Detail Report
extracts and Comptroller mastersheet rows for the five sample schools have not been published
or archived anywhere a second party could retrieve and check them, and two independent
attempts to re-access the same public sources programmatically (DOE FSF Public App,
Comptroller mastersheet) were blocked by robots-disallowed and Incapsula bot-detection
respectively. A result that is correct but reproducible only by re-running the same producing
instance's own browser session is not yet reproducible in the sense this paper's own Tier
discipline cares about. Disposition: ABSORBED, action items updated in v1.0-rc3. The
Verification Status ED-K4 paragraph and Section 4.1 now state explicitly which ED-K4 figures
were checked against source abstracts (Balu et al. 2015; Westall, Utter & Strunk 2023) versus
cited-not-yet-individually-verified (Nickow/Oreopoulos/Quan; Cook et al.; the Mississippi

program figures; Saga Education). The recompute is tagged single-instance, not independently
reproduced in the Verification Status, Section 3, Section 4.4.3, and Section 4.4.6 (F-ED-10).
Two concrete open action items were logged rather than silently deferred: (1) archive and
publish the five schools' raw FSF Detail Report extracts and the relevant Comptroller
mastersheet rows as a companion dataset (Zenodo or equivalent), so a second party can
reproduce the recompute without needing browser access to the same DOE app; (2) individually
verify the remaining ED-K4 citations (Nickow/Oreopoulos/Quan, Cook et al., Mississippi, Saga
Education) end-to-end in a future revision. Item (2) is now COMPLETE (v1.0-rc3): see F-ED12 for the two corrections this pass surfaced. Item (1) is IN PROGRESS: the five-school
extract, mastersheet rows, recompute script, and a documented README/license have
been compiled into an archivable companion package, delivered to the project lead for
manual publication to Zenodo (no API-driven publish was performed in this session); the
resulting DOI is not yet available to cite here and is carried to Next Audit Cycle. Crossreference: F-ED-10; F-ED-12; ED-K3, ED-K4; Section 3; Section 4.4.6; F-RV-2; F-RV-4.
F-ED-12 MEDIUM -- Individual citation verification of the four remaining ED-K4 figures
surfaces a version-mismatch and a mis-attribution [RESOLVED-AND-RETAINED; new
in v1.0-rc3, discharges F-ED-11 action item 2]
Locus: Section 4.1 mechanism ED-K4, dosage-threshold and per-pupil-cost bullets; Verification
Status ED-K4 paragraphs.
Substance: The four ED-K4 figures F-ED-11 logged as cited-not-yet-individually-verified were
each re-read end-to-end against primary sources in this version. Two errors surfaced. (1) Version
mismatch: the Nickow, Oreopoulos & Quan pooled tutoring effect size was cited as ≈ 0.37 SD,
attributed to the linked 2024 peer-reviewed article (DOI 10.3102/00028312231208687). That
article's own abstract states an overall pooled ES of 0.288 SD (SE = 0.029, p < .001). The 0.37
SD figure is real, but belongs to the authors' earlier 2020 NBER working-paper draft of the same
study (w27476) -- a figure still repeated by several secondary sources (J-PAL, the U.S.
Department of Education) that cite the 2020 preprint rather than the 2024 published revision.
Citing 0.37 SD while linking the 2024 DOI conflated the two versions. (2) Mis-attribution: the
Saga Education tutoring-cost figure ("≈$1,900-$4,800/student") was cited to Mahmud (2025,
EdWorkingPaper 25-1352) -- a full-text check confirms that paper never mentions Saga
Education anywhere; it is a Mississippi-retention-policy paper with no tutoring-vendor content.
The correct source is Cook, Dodge, Farkas, Guryan, Ludwig et al., "Not Too Late" (NBER
w28531), specifically the University of Chicago Education Lab's hosted revision of that paper,
which states Saga's cost was $3,200-$4,800 per pupil during the 2013-2015 study period and has
since dropped to $1,800 per pupil via an AmeriCorps subsidy and a blended-learning 4:1 model
-- a $1,800-$4,800 range, not $1,900-$4,800; no source was located for a $1,900 figure
specifically. Two figures were confirmed rather than corrected: the Cook et al. pooled TOT
(≈0.28 SD) and one-year persistence (0.23 SD) figures matched the UChicago Ed Lab hosted
text verbatim (the NBER-hosted PDF draft shows 0.264/0.222 SD, an ordinary cross-revision
variance between working-paper drafts, not an error); and the Mississippi Literacy-Based
Promotion Act cost (≈$15 million/year), coaching-count (29 rising to 74), and effect-size (0.014
SD bare-mandate versus 0.322 SD funded-model by 2019) figures all matched Mahmud (2025)
verbatim. Separately, the "2-4x" ITT/TOT gap claim in the same section, previously coattributed to Nickow et al. (2024), was checked against that paper's accessible text and no
ITT/TOT discussion was found there; the claim is corroborated instead by a University of

Chicago Education Lab 2022-23 scale-up study (0.04 SD ITT versus 0.14 SD TOT, a 3.5x gap),
so the citation is narrowed to that source alone.
Disposition: RESOLVED-AND-RETAINED. Section 4.1's dosage-threshold bullet now cites
0.288 SD for Nickow, Oreopoulos & Quan (2024) with an explicit note distinguishing it from the
2020 preprint's 0.37 SD; the per-pupil-cost bullet now attributes the Saga Education range
($1,800-$4,800) to Cook et al./NBER w28531 rather than Mahmud (2025); the ITT/TOT gap
bullet now cites only the UChicago Ed Lab scale-up study. The Verification Status section and
the Section 4.1 citation-provenance paragraph are both updated to state that all four previouslyunverified ED-K4 figures are now individually verified end-to-end, with these two corrections
logged rather than silently applied. This finding does not, by itself, discharge Item 5 of the
paper's convergence criterion (independent cross-instance audit); it is the producing instance's
own follow-through on an action item it logged against itself in v1.0-rc2, and is subject to the
same non-lineage audit requirement as every other finding in this ledger.
Cross-reference: F-ED-11; ED-K4; Section 4.1; Verification Status.
F-ED-13 MEDIUM -- The recompute was an internal-consistency and cross-source check,
not a formula reconstruction; category-level reconstruction now performed [RESOLVEDAND-RETAINED in v1.0-rc5; provenance corrected v1.0-rc6; raised v1.0-rc4 from peer
review F-PR-2 and F-PR-4]
Locus: Verification Status "primary formula data" paragraph; Section 4.4.6 item 2; Section 4.4.2
(100.00 percent corroboration); Section 4.4.3 emit table; original Falsifiability item 2.
Substance: An independent peer-review pass reproduced the recompute from the archived
companion dataset and found that it sums the DOE Detail Report's own disclosed walkthrough
line items back to the DOE's own reported total (agreement within $2 to $18, rounding) and that
the total matches the Comptroller "FY2023 Initial" FSF column exactly for all five schools. Both
results are genuine and are retained. But this is an internal-consistency check of one DOE
document plus a cross-source match, not the formula reconstruction from weighted registers and
per-capita weights that the paper's original Falsifiability item 2 called for: the only formuladerived term is an aggregate prior-year register times a base rate, and the archived extract
contains no category-level weighted register. The Verification Status phrase "full category-level
weighted-register breakdowns" overstated what was captured, and the Section 4.4.2 "100.00
percent" base-allocation field is browser-viewed and absent from the archive.
Disposition: RESOLVED-AND-RETAINED (v1.0-rc5; provenance corrected v1.0-rc6). In
v1.0-rc4 this was absorbed only by downscoping, with the formula reconstruction left open
because the archive lacked the per-school category register. In v1.0-rc5 an independent nonlineage pass performed the reconstruction: a category-level Detail Report pull (Grade Weight,
Academic Intervention, ELL, Special Education, Portfolio) for all five schools shows the
category dollars sum to the register-times-rate base, and the full walkthrough is mechanistically
reconstructed as (FY2022 register times FY2022 rate) + teacher-salary-change (bridging to the
FY2023 rate; reviewer-verified to under $1, see Verification Status and F-ED-14) + registerchange adjustment (bridging FY2022 to FY2023 register) + foundation + collective-bargaining
terms. This is a genuine mechanistic explanation of the walkthrough (roll last year's register at
last year's rate forward through the salary-rate and register changes), not merely an internalconsistency check, and it discharges the F-PR-2 concern. Corrected in v1.0-rc6: v1.0-rc5

tagged the category-level Detail Report pull "user-performed, not reviewer-reproduced." The
reviewer has since reported that the pull was obtained by the reviewer's own live browser
automation and the reconstruction arithmetic was independently run by the reviewer, not merely
relayed; this is corrected to reviewer-obtained and reviewer-reproduced (see Verification Status).
Two honest residuals remain and are retained, not smoothed: (1) the register-change adjustment
uses a single blended base rate and carries a $1 to $60 residual because category-specific percapitas differ, so a fully category-exact reconstruction is a further refinement; (2) the categorylevel data is browser-obtained and is not yet in the companion dataset, so this specific
reconstruction is not yet independently reproducible by a third party from the archive itself.
Adding the category-level register (and the per-school base-allocation percentage) to the dataset
is carried to Next Audit Cycle as a reproducibility step, not a merits gap.
Cross-reference: F-PR-2; F-PR-4; F-ED-10; F-ED-11; F-ED-14; Section 4.4.6 falsifiability item
2; Al-Mutaffifin 19894724 Section 4.1a (per-case ratio pattern).
F-ED-14 MEDIUM -- Base-rate parameter ($4,223.00) is the rolled-forward FY2022 base
weight amount; resolved with a primary source [RESOLVED in v1.0-rc5; provenance
corrected v1.0-rc6; raised v1.0-rc4 from peer review F-PR-3]
Locus:
companion
dataset
five_school_fsf_fy2023_detail_report_extract.csv
(base_rate_per_pupil_usd = 4223.00) and fsf_recompute.py; F-ED-10 Substance ("$4,223.00
base rate"); companion dataset fsf_fy2023_weights_percapitas.xlsx (K-5 weight 1.0 per-capita =
$4,197.19).
Substance: The recompute's single largest term is the aggregate prior-year weighted register
times a base rate of $4,223.00 (roughly $3M of a roughly $4.1M total). The dataset's own
FY2023 per-capita reference table lists the base (K-5, weight 1.0) per-capita at $4,197.19. The
reviewer confirmed that $4,223.00 is the rate that makes the walkthrough reconcile to within $18
and that $4,197.19 does not (it would leave the recompute roughly $18k short on the base term),
so $4,223.00 is the rate the DOE actually applied. But its provenance and vintage are
undocumented: it is plausibly a prior-year (FY2022) or enrollment-blended system rate
consistent with the roll-forward method, which is not stated anywhere in the extract or the paper.
An undocumented load-bearing rate that disagrees with the paper's own included reference table
is a parameter-integrity gap.
Disposition: RESOLVED (v1.0-rc5; provenance corrected v1.0-rc6). Two independent lines
close this. (1) Reviewer-verified from the archived data: teacher-salary-change equals
fy22_register times ($4,197.19 minus $4,223.00) to under $1 (max deviation $0.78) for all five
schools, so the walkthrough uses the FY2022 rate ($4,223.00) on the FY2022 register and the
teacher-salary-change term bridges to the FY2023 rate ($4,197.19). The arithmetic only closes at
exactly those two values, so the identity itself pins both rates. (2) Primary source, reviewerfetched (corrected in v1.0-rc6; v1.0-rc5 tagged this user-supplied-cited-not-reviewer-fetched,
citing a robots block): the DOE FSF Working Group Meeting 3 deck publishes a year-by-year
Base Weight Amount table -- FY2021 $4,137.85, FY2022 $4,223.00, FY2023 $4,197.19 -- and
attributes the FY2023 decrease to average teacher salary falling for the first time in several years
due to increased retirements, which is why the rolled-forward FY2022 rate exceeds the current
FY2023 rate. The reviewer has since reported fetching this deck directly from its source URL in
the same session, with the full table returned and no robots block encountered by that fetch

method; the tag is corrected accordingly. The $4,223.00 versus $4,197.19 discrepancy flagged by
F-PR-3 is therefore not an error but the expected prior-year-versus-current-year distinction, now
documented from a source the reviewer directly confirmed. The remaining reproducibility step is
to cite the deck in the companion dataset alongside the weights table.
Cross-reference: F-PR-3; F-ED-10; F-ED-13; Verification Status (independent verification pass);
companion dataset fsf_fy2023_weights_percapitas.xlsx.
Accepted without finding (sound mappings): Bismillah scope declarations as competency
bounding; ring-composition syllabus design as opening-closing consistency (a rhetoric-pedagogy
device requiring no metaphysical claim); the additive-only principle against silent record
dropping (retained under F-ED-4 rectification correction).

C. Falsifiability Criteria (paper-level)
1.

2.
3.

4.
5.
6.

7.

If any Tier 1 mechanism in Section 4 requires semantic disambiguation to fire, the label
is false (framework violation). Disambiguating report vintage (Initial versus Final budget
snapshot) is a disclosed-parameter choice, not a semantic one, so requiring it is not itself
a framework violation; but a result that depends on that disclosed choice to reproduce is
Tier 2, not Tier 1, by Section 3's own definition (corrected v1.0-rc2, F-RV-3; F-ED-10).
If ED-K2 gates are applied and reforms with subgroup regressions still report unqualified
aggregate improvement, the gate is not enforced as specified.
If ED-K4's remediation pathway is deployed and its logged attendance/uptake data shows
systematically lower uptake among the same subgroups the disaggregated regression gate
is meant to protect, coupling (a) has failed on its own terms and must be re-designed
before the gate may continue firing.
If ED-U2 cross-instance grading produces correlated errors across instances, the biasrelocation claim degrades to bias-preservation.
If ED-G1 reproduction passes correlate with committee merit judgments beyond chance,
the Tier 1 / Tier 3 separation in F-ED-3 is empirically wrong.
Added v1.0-rc2 (F-RV-2, F-ED-11). A structural or empirical result generated by a single
producing instance and presented as ship-grade must be independently reproducible by a
second party from archived source data, not merely re-describable by the same instance
re-running its own prior session. If the underlying data for a claim in this paper is not
archived in a form a second instance or human reviewer can retrieve and check, that
claim is tagged single-instance, not independently reproduced, and is not counted toward
this paper's convergence criterion until archived.
Worked-example falsifiability: Section 4.4.6 items 1 through 3.

D. Append-Only Ledger and Next Audit Cycle
Appendix: v0.1 initial draft [preserved]
•
Established Tier discipline for education (Section 3)
•
Proposed ED-K1..K3, ED-U1..U2, ED-G1..G3
•
Raised F-ED-1 (CRITICAL) through F-ED-7 (MEDIUM) against prior-session draft
•
Deflated "mathematical nature of the Qur'an" to corpus-honest magnitude

Appendix: v0.1-addendum worked example [preserved]
•
Added Section 4.4 NYC Fair Student Funding (ED-K1/ED-K2)
•
Raised F-ED-8 (HIGH) and F-ED-9 (MEDIUM)
•
Pinned current-layer magnitude to IBO May 29, 2025 (end-to-end)
•
Named two verification debts: IBO fsf2013 end-to-end read; independent formula
recompute
•
v0.1-addendum F-ED-8 substance (superseded, preserved per §14.5): "the divergence
was inversely correlated with student need (higher low-income and ELL share and larger
enrollment associated with lower percent-of-formula funded)." Correction in v0.2 per
end-to-end IBO fsf2013 read: the IBO source supports weight-category regressivity
(ELL, special-ed CTT below formula weight; middle-school-below-standards negative
implied weight) and the 94-98%-below figures; the school-level inverse relationship is
Voloch (2015), a distinct source, now tagged snippet-level and not merged with the IBO
finding.
Appendix: v0.1 -> v0.2 amendments [preserved]
•
F-ED-2 ABSORBED: added ED-U3 (Mizan-calibrated abstention); bias-removal claim
deleted
•
F-ED-3 ABSORBED: ED-G1 reclassified necessary-not-sufficient; merit stated as human
Tier 3
•
F-ED-4 ABSORBED: ED-K2 and ED-G3 stated as append-only-with-correcting-entries;
"immutable" removed for student records
•
F-ED-5 ABSORBED: ED-U2 stated as bias relocation with Knight-Leveson caveat and
rubric-only scope
•
F-ED-6 ABSORBED: "dynamics reveals" framing removed; Al-Mutaffifīn used as name
only
•
F-ED-7 ABSORBED: Qur'an confined to primitive/vocabulary source plus deflated
candidate effect
•
F-ED-8 magnitude VERIFIED end-to-end (IBO fsf2013); directional claim corrected and
re-attributed
•
F-ED-9 corroborated by IBO's own Tier 1 / Tier 3 boundary
•
Section 4.4 worked example integrated into the paper body
•
F-ED-1 remains OPEN (CRITICAL, HALT-and-escalate; project-lead decision)
•
v0.2 F-ED-1 substance and disposition text (superseded, preserved per §14.5):
"Disposition: HALT-and-escalate to project lead. OPEN in v0.2. Not absorbed.
Escalation content: the gate may proceed only if (a) coupled to a resourced, logged
remediation pathway triggered on non-mastery, and (b) instrumented with an ED-K2
disaggregated regression gate. Until both couplings exist, unfit to ship."
•
v0.2 F-ED-8 category-attribution text (superseded, preserved per §14.5): "At the weightcategory level, IBO's regression found specific high-need categories funded significantly
below their formula weight: elementary and high-school ELL students, and high-school
special-education CTT students." Correction in v1.0: re-verification against the retrieved
report text could not confirm this specific attribution verbatim; downgraded to
unconfirmed pending appendix-table verification (see F-ED-8, v1.0).

•

v0.2 Layer 1 resolution attribution (superseded, preserved per §14.5): "Beginning
FY2023 the city committed to funding every school at no less than 100 percent of
formula, an investment it described as reaching 1,164 schools and over 700,000
students." Correction in v1.0: this is an April 19, 2021 de Blasio/Porter announcement,
effective the 2021-22 school year, not a January 2023 Adams/Banks announcement and
not literally "FY2023" (see F-ED-8, v1.0).

Appendix: v0.2 -> v1.0 amendments [new in this artifact]
•
Project lead disposed F-ED-1: "Apply the required couplings." F-ED-1 status changed
from OPEN/HALT-and-escalate to ABSORBED, via new mechanism ED-K4 (Section
4.1): a remediation-coupled mastery gate requiring (a) an automatically-triggered,
dosage-and-funding-disclosed, attendance-logged remediation pathway and (b) an
independent, non-substitutable ED-K2 disaggregated subgroup regression gate, with
pinned citations and honest caveats (Michigan's persistent economic-disadvantage
retention disparity despite comparable remediation infrastructure; NYC's own A-501
causal evidence excluding ELL/SpEd; RTI/MTSS mixed-to-negative national evidence;
no direct experimental test of "gate + remediation" versus "gate + no remediation" on
subgroup outcomes).
•
Voloch (2015) read end-to-end (full dissertation abstract, table of contents, Chapter One,
and cross-corroboration via NYU Steinhardt Metro Center); promoted from snippet-level
to Tier 2 end-to-end verified with added precision (451 high school budgets, SY2013-14,
8.5% n=38 fully funded, median 86.19%).
•
Independent FSF formula recompute performed for a 5-school FY2023 sample (28Q160,
10X085, 30Q258, 14K488, 30Q148), using DOE FSF Public App Detail Reports
obtained via browser automation. Recompute reproduced the DOE's own published Total
FY2023 FSF Allocation to within $2-$18 (rounding) for all five schools. New finding FED-10 logged: this figure matches the Comptroller mastersheet's "FY2023 Initial"
column exactly and diverges from "FY2023 Final" for a fully explained, disclosed reason
(mid-year register relief following an enrollment change) -- resolved, not left open. (v1.0rc4 correction per §14.5, F-PR-1: this "fully explained / resolved" characterization is
superseded; independent decomposition against the archived data shows the divergence is
only partially explained -- relief offsets enrollment for two of five schools, three carry an
unexplained net-positive residual -- and F-ED-10 is now PARTIALLY-RESOLVED.
Historical entry preserved verbatim above.)
•
Pinned citations supplied for the F-ED-1 remediation/retention research base under EDK4 (Section 4.1), replacing summary-level citations.
•
F-ED-8 corrected: (i) the specific ELL/high-school-special-ed-CTT below-formulaweight attribution downgraded to unconfirmed pending appendix-table verification; (ii)
the Layer 1 100-percent-floor announcement retraced to April 19, 2021 (de Blasio/Porter,
2021-22 school year), correcting the v0.2 "beginning FY2023" / January 2023 AdamsBanks misattribution; (iii) the Voloch school-level inverse relationship merged in as an
independently end-to-end-verified Tier 2 claim.
•
F-ED-10 (MEDIUM, RESOLVED-AND-RETAINED) added: documents and resolves
the report-vintage ambiguity discovered during the recompute.
•
Section 4.4 (worked example) and Section 6 (paper-level falsifiability) updated to reflect
the completed recompute and corrected citations.

•

•

Section 7 (Limitations) updated: the "requires pinned citations before full-rigor ship"
limitation is discharged; a new limitation is stated regarding the absence of a direct
experimental "gate + remediation" versus "gate + no remediation" subgroup comparison
in the literature, and regarding the cross-instance audit gap below.
Item 5 of v0.2's blocking path -- cross-instance audit by a Tier 1 auditor other than
the producing instance, with convergence at two consecutive rounds of 0 CRITICAL
and 0 HIGH -- was NOT performed in this session. No separate reviewing instance
was available. This is flagged honestly rather than silently dropped or fabricated; see
Verification Status and Next Audit Cycle below.

Appendix: v1.0(-rc1) -> v1.0-rc2 amendments [new in this artifact]
After v1.0 (retroactively relabeled v1.0-rc1 per F-RV-5) was shared, a producer-lineage
continuity review was received: six findings, namespace F-RV, reporting 0 CRITICAL, 1 HIGH
(F-RV-1), 3 MEDIUM (F-RV-2, F-RV-3, F-RV-4), 2 LOW (F-RV-5, F-RV-6). Per the review's
own Provenance Disclosure and this paper's Standing Rule 7, the reviewing instance had
authored v0.1 and v0.2 of this paper and is therefore excluded from the Tier 1 auditor pool for its
own lineage; its findings are advisory and do not count toward the item-5 convergence criterion.
Before absorbing any finding, F-RV-1 was independently re-checked against the primary source
in this session (direct re-fetch of the IBO 2013 report), which confirmed the review's claim and
confirmed v1.0-rc1's own retrieval-miss error. F-RV-6 was independently re-checked
mechanically (grep count of em-dash glyphs: 32 occurrences found). All six findings are
absorbed:
•

•

•

•

F-RV-1 (HIGH) ABSORBED. v1.0-rc1 stated the specific ELL/high-school-special-edCTT below-formula-weight attribution "was not located verbatim in the report's main
text" and downgraded it to unconfirmed. That statement about the source was false; the
report's section "Students Funded Below, Close to, or Above Formula Weight" states the
attribution verbatim, with supporting category-level figures. The claim is restored to
confirmed in Verification Status, Section 4.4.2, Section 4.4.3, and F-ED-8.
F-RV-2 (MEDIUM) ABSORBED. The FY2023 FSF recompute (F-ED-10) is tagged
single-instance, not independently reproduced, in Verification Status, Section 4.4.3,
Section 4.4.6, and F-ED-10/F-ED-11, because the DOE FSF Public App (robotsdisallowed) and NYC Comptroller mastersheet (Incapsula bot-detection) blocked a
second party's attempt to re-access the same public sources. Archiving the underlying
five-school extract and mastersheet rows as a companion dataset is logged as an open
action item (F-ED-11; Next Audit Cycle), not yet completed.
F-RV-3 (MEDIUM) ABSORBED. The recompute is reclassified from Tier 1 to Tier 2
(Structural) in Section 3, Section 4.4.3, Section 4.4.6, Section 6, F-ED-10, and F-ED-11,
because reproducing the DOE's published total depends on a disclosed parameter choice
(report vintage), which is Tier 2 by Section 3's own definition. The "Tier 2/Tier 1" slash
language in Section 3 is removed.
F-RV-4 (MEDIUM) ABSORBED. Verification Status and Section 4.1 (ED-K4) now
state explicitly which remediation-pathway citations were checked against source
abstracts (Balu et al. 2015; Westall, Utter & Strunk 2023) versus cited-not-yetindividually-verified (Nickow/Oreopoulos/Quan 2024; Cook et al.; Mississippi program
figures; Saga Education). New finding F-ED-11 logs this and the recompute-archiving

•

•

gap together, with individual verification of the remaining citations carried as an open
action item.
F-RV-5 (LOW) ABSORBED. The version label is corrected from an unqualified "v1.0"
to "v1.0-rc2," with the prior file relabeled v1.0-rc1 in this paper's own history (not
renamed on disk; the file previously shared as "v1.0" is left as-is and is superseded by
this artifact). Per the review's own disposition, promotion to an unqualified v1.0 label is
reserved for convergence: two consecutive cross-instance rounds of 0 CRITICAL and 0
HIGH.
F-RV-6 (LOW) ABSORBED. All 32 em-dash glyphs found in v1.0-rc1 are replaced
with the double-hyphen throughout this artifact, restoring the em-dash-clean standard
established in v0.2.

Superseded v1.0(-rc1) text preserved per §14.5, annotated as itself corrected: - v1.0-rc1 Section
4.4.2 downgrade text: "the more specific v0.2 claim that 'elementary and high-school ELL
students, and high-school special-education CTT students' were funded significantly below their
formula weight was re-checked against the report's retrieved text and could not be confirmed
verbatim... This claim is downgraded to unconfirmed pending appendix-table verification."
Corrected in v1.0-rc2 per F-RV-1: this statement about the source was false; the attribution is
verbatim-confirmed and restored (see F-ED-8, v1.0-rc2). - v1.0-rc1 Section 3 Tier language: "it
stays in Tier 2/Tier 1 provided the vintage is stated." Corrected in v1.0-rc2 per F-RV-3: a
disclosed-parameter-dependent result is Tier 2, not a Tier 1/Tier 2 hybrid. - v1.0-rc1 Section
4.4.6 falsifiability item 2 language: "This recompute is Tier 1 valid provided report vintage is
disclosed as a required parameter." Corrected in v1.0-rc2 per F-RV-3: Tier 2 valid, not Tier 1. v1.0-rc1 F-ED-10 disposition: "The independent recompute is Tier 1 valid once report vintage
(Initial versus Final) is disclosed as a required parameter." Corrected in v1.0-rc2 per F-RV-3:
Tier 2 valid, with single-instance status disclosed per F-RV-2. - v1.0-rc1 title block: "Draft
Application Note, Version 1.0." Corrected in v1.0-rc2 per F-RV-5: "Version 1.0-rc2 (producercomplete; cross-instance audit pending)," with the prior file relabeled v1.0-rc1.
Appendix: v1.0-rc2 -> v1.0-rc3 amendments [new in this artifact]
This revision discharges the two open action items v1.0-rc2 logged at F-ED-11, both of which
fall within the producing instance's own authority (no separate reviewing instance was involved
in this round):
•

F-ED-11 action item 2 COMPLETE. The four ED-K4 figures previously cited-not-yetindividually-verified (Nickow, Oreopoulos & Quan 2024; Cook et al. "Not Too Late";
Mahmud 2025 Mississippi figures; Saga Education per-pupil cost) were each read end-toend against primary sources. New finding F-ED-12 (MEDIUM, resolved-and-retained)
logs two corrections: the Nickow et al. pooled effect size is corrected from ≈0.37 SD (a
conflation with the authors' 2020 NBER preprint, w27476) to 0.288 SD (the actual figure
in the 2024 published article linked); and the Saga Education per-pupil cost is reattributed from Mahmud (2025), which does not mention Saga Education, to Cook et
al./NBER w28531, with the range corrected from "$1,900-$4,800" to "$1,800-$4,800."
Two figures were confirmed rather than corrected (Cook et al. pooled TOT/persistence;
Mississippi cost and effect-size figures), and the ITT/TOT "2-4x" gap claim's citation is
narrowed to the UChicago Education Lab scale-up study, removed from Nickow et al.

•

specifically. Section 4.1, the Verification Status section, F-ED-11's disposition, Section
4.4.4, Section 5 header, and Section 7 (Limitations) are all updated accordingly.
F-ED-11 action item 1 IN PROGRESS. The five-school FSF Detail Report extract and
the corresponding NYC Comptroller mastersheet rows (F-ED-10) have been compiled
into a documented, licensed companion dataset package (two CSV extracts, the
recompute script, the supporting weight/per-capita table, a README covering
provenance/methodology/reproduction instructions, and a CC-BY 4.0 license for the
compilation) so a second party can attempt the recompute without a live browser session
against the DOE Public App. Publishing this package to a public archive (Zenodo or
equivalent) so it carries a citable DOI, matching this paper's companion-paper
convention, has not yet been completed as of this version and is carried to Next Audit
Cycle. Section 4.4.6, F-ED-11, and Section 7 (Limitations) are updated to reflect
"compiled, not yet published" rather than "not yet archived."

No prior finding text is edited in place; this section documents new work only, per §14.5.
Appendix: v1.0-rc3 -> v1.0-rc4 amendments [new in this artifact]
After v1.0-rc3 and its companion dataset were shared, a rigorous internal peer review
(namespace F-PR, producer-lineage) was performed. For the first time in this lineage the
FY2023 recompute was reproduced by a second computation from the archived dataset rather
than trusted from the producing pass. The review reported 0 CRITICAL, 2 HIGH (F-PR-1, FPR-2), 1 MEDIUM (F-PR-3), 1 LOW (F-PR-4). Per Standing Rule 7 the reviewing instance is
producer-lineage and its findings, like every prior self-review here, do not discharge Item 5.
Reproduction results retained: the DOE walkthrough line items sum to the reported total within
$2 to $18 for all five schools, and the DOE total matches the Comptroller "FY2023 Initial" FSF
column exactly for all five. All four findings are absorbed:
•

•

•

F-PR-1 (HIGH) ABSORBED. The v1.0-rc3 claim that the Initial-to-Final divergence is
"fully explained by Register Relief and a mid-year enrollment change" is corrected. A
per-school decomposition (Initial FSF versus Final FSF plus Register Relief) shows relief
offsets the enrollment change for only two of five schools (30Q258 +$1,007; 14K488 +
$10,521), leaving a net-positive rate/CB residual for three (28Q160 +$95,668; 10X085 +
$218,563; 30Q148 +$224,353) that the Initial-vintage walkthrough does not itemize;
28Q160's Final FSF actually rises while its enrollment falls, which relief and enrollment
cannot explain. F-ED-10 is downgraded RESOLVED to PARTIALLY-RESOLVED and
Section 4.4.6 item 2 corrected.
F-PR-2 (HIGH) ABSORBED. The recompute is described accurately as an internalconsistency check plus a cross-source match, not a formula reconstruction from weighted
registers and per-capita weights; the overstated Verification Status phrase "full categorylevel weighted-register breakdowns" is corrected, and the Section 4.4.3 emit-table row is
downscoped. New finding F-ED-13 logs this; the true formula reconstruction remains not
performed (the archive lacks the per-school category register) and is carried as an open
item.
F-PR-3 (MEDIUM) ABSORBED, remains OPEN. New finding F-ED-14 documents
that the recompute's base rate ($4,223.00) reconciles the walkthrough but disagrees with
the dataset's own FY2023 K-5 per-capita ($4,197.19) and is of undocumented

•

provenance/vintage; resolving it requires the FSF Guide base-rate definition and is
carried to Next Audit Cycle.
F-PR-4 (LOW) ABSORBED. The Section 4.4.2 "100.00 percent" base-allocation
corroboration is flagged as browser-viewed and absent from the archive; adding that field
(and the category register) to the companion dataset is logged at F-ED-13.

Superseded v1.0-rc3 text preserved per §14.5, annotated as itself corrected: - v1.0-rc3 F-ED-10
substance: "the divergence from 'FY2023 Final' is fully explained by the mastersheet's own
disclosed Register Relief column and a mid-year enrollment change." Corrected in v1.0-rc4 per
F-PR-1: partially explained only; two of five schools reconcile via relief, three carry an
unexplained net-positive residual. - v1.0-rc3 Verification Status: "full category-level weightedregister breakdowns and complete allocation walkthroughs." Corrected in v1.0-rc4 per F-PR-2:
the archive holds an aggregate register and walkthrough line items, not category-level
breakdowns. - v1.0-rc3 F-ED-10 disposition status: "RESOLVED-AND-RETAINED, Tier
reclassified." Corrected in v1.0-rc4 per F-PR-1: PARTIALLY-RESOLVED.
No prior finding text is edited in place; this section documents new work only, per §14.5.
Appendix: v1.0-rc4 -> v1.0-rc5 amendments [new in this artifact]
An independent (non-lineage) verification-plus-analysis pass was received. It reproduced the FED-10 decomposition exactly for all five schools and resolved rc4's two producer-side open
items on the merits. Reviewer re-verification in this session: the teacher-salary-change identity
(fy22_register times ($4,197.19 minus $4,223.00)) was independently confirmed to under $1 for
all five schools, which pins both base rates. The DOE Working Group deck (base-weight table)
and the category-level Detail Report pull could not be re-fetched by the producing instance (both
robots-disallowed to automated access) and are tagged accordingly.
•

•

•

F-ED-14 RESOLVED (was OPEN). The base rate $4,223.00 is the rolled-forward
FY2022 base weight amount; the FY2023 rate is $4,197.19. Primary source: the DOE
FSF Working Group Meeting 3 deck's year-by-year Base Weight Amount table (FY2021
$4,137.85, FY2022 $4,223.00, FY2023 $4,197.19), with the FY2023 decrease attributed
to a teacher-salary drop from increased retirements. The F-PR-3 discrepancy is the
expected prior-year-versus-current-year distinction, not an error. Corroborated reviewerside by the teacher-salary-change identity.
F-ED-13 RESOLVED-AND-RETAINED (was ABSORBED-by-downscoping). A
category-level Detail Report reconstruction was performed: category dollars sum to the
register-times-rate base, and the walkthrough is mechanistically reconstructed as rollforward of the FY2022 register at the FY2022 rate through the salary-rate and register
changes. This discharges F-PR-2's "not a formula reconstruction" concern. Two residuals
retained: a $1 to $60 blended-rate approximation on the register-change adjustment
(category-specific per-capitas differ), and the category-level data not yet being in the
companion dataset.
Verification Status, Section 4.4.3 emit table, Section 4.4.4 index, and Section 4.4.6
falsifiability item 2 updated to reflect the reconstruction and the resolved base rate.

Superseded v1.0-rc4 text preserved per §14.5, annotated as itself corrected: - v1.0-rc4 F-ED-14
disposition: "OPEN. Cannot be resolved from the archived data." Corrected in v1.0-rc5: resolved

with a primary source and a reviewer-verified identity. - v1.0-rc4 F-ED-13 disposition:
"ABSORBED by downscoping; formula reconstruction remains an open item... not by
performing the reconstruction." Corrected in v1.0-rc5: reconstruction performed; RESOLVEDAND-RETAINED with two named residuals.
No prior finding text is edited in place; this section documents new work only, per §14.5.
Appendix: v1.0-rc5 -> v1.0-rc6 amendments [new in this artifact]
After v1.0-rc5 was shared, the same non-lineage reviewer who supplied its F-ED-13/F-ED-14
resolution reported a provenance correction to that resolution's own tagging, based on tooling
used within that reviewer's own session (not new data and not a new numeric finding):
•

•

•

•

v1.0-rc5 tagged the DOE FSF Working Group Meeting 3 deck "user-supplied, cited but
not reviewer-fetched (source is robots-disallowed to automated access)." The reviewer
reports having fetched the deck directly from its source URL in that same session, with
the full Base Weight Amount table returned and no robots block encountered by that
fetch method. Corrected to reviewer-fetched and confirmed verbatim.
v1.0-rc5 tagged the category-level Detail Report pull for all five schools "user-performed,
not reviewer-reproduced (the FSF Detail Report app is robots-disallowed to automated
access)." The reviewer reports having obtained that pull directly via the reviewer's own
live browser automation against the DOE FSF Public App, and having independently run
the reconstruction arithmetic (category dollars summing to the register-times-rate base;
the walkthrough reconstruction matching the DOE total within $2-$18) rather than
accepting it on trust. Corrected to reviewer-obtained and reviewer-reproduced.
No disposition status changes: F-ED-13 remains RESOLVED-AND-RETAINED and FED-14 remains RESOLVED, exactly as v1.0-rc5 stated. This is a strengthening of the
evidentiary basis already claimed, not a new merits finding, and does not discharge Item
5 (the cross-instance-audit convergence gate remains open). Next Audit Cycle item (g)
from v1.0-rc5 ("re-fetch the deck from a non-robots-disallowed mirror to move F-ED14's primary source from user-cited to reviewer-verified") is discharged by this
correction; the deck did not need a mirror, only a different fetch method than the one the
producing instance had available.
Verification Status, F-ED-13, and F-ED-14 are updated with the corrected tags;
superseded v1.0-rc5 wording is preserved below per §14.5.

Superseded v1.0-rc5 text preserved per §14.5, annotated as itself corrected: - v1.0-rc5
Verification Status: "User-supplied, cited but not reviewer-fetched (source is robots-disallowed
to automated access): the DOE FSF Working Group Meeting 3 deck..." Corrected in v1.0-rc6:
reviewer-fetched and confirmed verbatim; no robots block encountered by the reviewer's fetch
method. - v1.0-rc5 Verification Status: "User-performed, not reviewer-reproduced (the FSF
Detail Report app is robots-disallowed to automated access): a category-level Detail Report
pull..." Corrected in v1.0-rc6: reviewer-obtained via live browser automation and independently
recomputed. - v1.0-rc5 F-ED-14 disposition: "(2) User-supplied primary source (cited, not
reviewer-fetched: the DOE deck is robots-disallowed to automated access)..." Corrected in v1.0rc6: reviewer-fetched. - v1.0-rc5 F-ED-13 disposition did not explicitly re-state the userperformed tag inline but relied on the Verification Status tag by cross-reference; that crossreferenced tag is corrected as above.

No prior finding text is edited in place; this section documents new work only, per §14.5.
Next audit cycle: v1.0-rc5 resolved both producer-side open items rc4 carried (F-ED-13 formula
reconstruction performed; F-ED-14 base rate sourced); v1.0-rc6 corrects the provenance tags on
those two resolutions to reviewer-fetched/reviewer-reproduced rather than user-supplied/userperformed, strengthening rather than reopening either finding. No open findings above LOW and
0 CRITICAL. It remains producer-complete, not cross-instance-converged: the independent
verification pass, though non-lineage, was a targeted verification of two findings plus one
provenance correction, not a full audit round producing a severity-scored findings report, so by
the verifier's own Standing Rule 7 note it does not close the convergence gate. The sole
remaining item before an unqualified "shipped" status (and an unqualified "v1.0" label, per FRV-5) is a cross-instance audit by a Tier 1 auditor with no stake in this lineage, achieving two
consecutive rounds of 0 CRITICAL and 0 HIGH findings. Secondary, non-blocking follow-ups
for a future version: (a) pull the Voloch dissertation's Chapter Four/Five regression tables (pp.
106-119) directly to confirm exact coefficients rather than relying on the abstract; (b) publish the
companion dataset (now to include the category-level Detail Report data and a citation to the
FSF Working Group base-weight deck) to a public archive so it carries a citable DOI and the
recompute and reconstruction are independently reproducible by a third party (F-RV-2, F-ED-11,
F-ED-13); (c) if full-text access to Nickow, Oreopoulos & Quan (2024) becomes available,
confirm directly whether that paper states an ITT/TOT ratio (F-ED-12); (d) extend the FY2023
recompute sample beyond five schools for a population-level ED-K1 audit; (e) if ED-K4 is
implemented, instrument its Falsifiability Criterion 3 from day one; (f) complete the fully
category-exact formula reconstruction (each category count times its own per-capita) to remove
the $1 to $60 blended-rate residual (F-ED-13). Item (g) from v1.0-rc5 (re-fetching the DOE deck
to move it from user-cited to reviewer-verified) is now discharged; see the v1.0-rc5 -> v1.0-rc6
amendments above.
Appendix: v1.0-rc6 -> v1.0-rc7 (pre-publication) amendments [new in this artifact]
This round covers the structural and citation changes made in preparing the work for publication.
Per §14.5 no prior finding or ledger text is edited in place; this appendix documents new work
only. All changes are producer-lineage or reviewer-reported editorial and provenance work; none
is a cross-instance audit round, so the convergence gate remains open exactly as stated above.
•

Two-document restructuring. The single rc6 manuscript, in which the audit apparatus
was threaded through the reader-facing argument, was split into two artifacts: a readerfacing paper (settled version-of-record claims, audit machinery removed) and this Audit
and Provenance Companion (the full Verification Status, the F-ED/F-RV/F-PR ledger,
falsifiability criteria, and this append-only version history). The FY2023 worked-example
data remains a separate Companion Dataset. The split relocates the audit trail intact to
this companion as its permanent home; no finding text was destroyed or rewritten. Loadbearing audit-derived facts were retained in the paper as settled statements: the Tier
classification of each mechanism, the five-school Tier 2 scope and partial Initial-versusFinal resolution of the worked example, the deflated Qur'an-structural magnitude, and the
explicit statement that no cross-instance audit has occurred.

•

DOI assignment and cross-reference. DOIs were assigned by the project lead and wired
into both documents: the paper is 10.5281/zenodo.21436484 and cites this companion as

10.5281/zenodo.21436486; this companion is 10.5281/zenodo.21436486 and cites the
paper as 10.5281/zenodo.21436484. These identify the paper and companion themselves
and are distinct from the still-pending public-archive DOI for the Companion Dataset zip
(Next Audit Cycle item (b)), which remains open.
•

Citation-URL restoration (paper References). In the initial split, the paper's
References section had been reduced to author-year entries without URLs, dropping the
verified primary-source links rc6 had carried inline. This was a reader-facing verifiability
regression and is corrected: every empirical source now carries its verified URL (IBO
2013 and 2025, Voloch, Westall/Utter/Strunk, Geng & Rockoff, Balu et al., Cook et al.,
Nickow et al. plus the 2020 draft, Mahmud, the 2021 Mayor announcement, and the NYC
DOE FSF Guide/weights/Public App), and Chancellor's Regulation A-501 and the NYU
Steinhardt corroboration were added as entries. All URLs were taken from rc6's verified
set rather than reconstructed. The reference list was set left-aligned so long URLs wrap
ragged-right without justified-stretch or margin overflow.

•

Three theory-reference URLs added (pre-publication review). Chouldechova (2017),
Kleinberg/Mullainathan/Raghavan (2016), and Knight & Leveson (1986) were the only
paper references still without a URL after the restoration above; canonical
publisher/repository links were added (Big Data via Liebert; arXiv 1609.05807; IEEE
TSE DOI 10.1109/TSE.1986.6312924).

•

Westall/Utter/Strunk citation corrected (pre-publication review; pre-existing error).
The paper cited ERIC document ED672729 as "Estimating the Effects of Michigan's
Read by Grade Three Law," labeled an "EdWorkingPaper." Direct source verification
(fetch of the ED672729 full text, corroborated by AERA and MSU announcements)
established the actual title as "Following the Letter of the Law: 2020-21 Retention
Outcomes Under Michigan's Read by Grade Three Law," published by the Education
Policy Innovation Collaborative (EPIC), Michigan State University. The URL was
already correct; the title and venue label attached to it were not. This error was present in
the rc6-era markdown and in every prior review round, and is caught only now via direct
source verification. The paper's References entry is corrected; the in-text author-year
citation ("Westall, Utter and Strunk 2023") was already correct and is unchanged. The
underlying empirical claims sourced to this document (the persistent economicdisadvantage retention disparity and the below-cutoff retention "bite" figures) are
unaffected; only the document's title and venue were misstated.

Next audit cycle (unchanged in substance): the paper remains producer-complete, not crossinstance-converged. This pre-publication round is editorial and provenance work, not the item-5
cross-instance audit. The sole remaining blocking item to an unqualified "shipped" status and an
unqualified "v1.0" label is a cross-instance audit by a Tier 1 auditor with no stake in this lineage,
achieving two consecutive rounds of 0 CRITICAL and 0 HIGH findings. The secondary nonblocking follow-ups (a) through (f) from the v1.0-rc5 -> v1.0-rc6 entry remain open, most
relevantly (b), publishing the Companion Dataset to a public archive for its own citable DOI.

Appendix: v1.0-rc7 -> v1.0-rc8 amendments (first independent cross-instance audit round)
[new in this artifact]
This appendix records the paper's first independent, non-lineage audit round and the absorption
of its findings. Per Section 14.5 no prior text is edited in place; this documents new work only.
The round. After v1.0-rc7 was published and the audit-request brief was issued, an independent
auditor of a non-Anthropic lineage (attested as GPT-5.5/OpenAI, outside the Claude/Anthropic
producing and reviewing lineage, with no drafting role) executed both recompute scripts against
the archived dataset, independently re-queried the Section 4.3-analogue quantities from the raw
CSV/XLSX, and re-verified every reference against primary sources. Result: PASS at 0
CRITICAL, 0 HIGH, 0 MEDIUM, 6 LOW, 0 INFO. This is the first of the two consecutive
passing rounds the convergence criterion requires; by Standing Rule 7 the producer-lineage
absorption below does not itself count as a round, and a second independent round on the
corrected artifact is still required.
Independent reproduction confirmed (non-defects). The auditor reproduced, from the
archived dataset, the walkthrough-to-DOE-total match (within $2.23 to $18.05), the DOE-totalto-Comptroller-Initial exact match for all five schools, the category-line sums (within $0 to $2),
the Initial-versus-Final decomposition (30Q258 +$1,007; 14K488 +$10,521; 28Q160 +$95,668;
10X085 +$218,563; 30Q148 +$224,353), and the teacher-salary identity (all under $1). It also
independently confirmed, against primary sources, every load-bearing numerical citation
(Nickow 0.288 vs the 2020 draft's 0.37; Guryan/Cook tutoring effects; Balu -0.17; Westall
disparities; Mahmud Mississippi figures; the UChicago 0.04 vs 0.14 ITT/TOT gap; IBO 2013
and 2025; Voloch; the 2021 floor; the FY2024 weights). No Tier-3 leak was found; the adequacy
and discrimination refusals held.
The six LOW findings, all absorbed in v1.0-rc8:
•

•

•

•

F-XA-1 (LOW) ABSORBED. The 2024 AERJ Nickow/Oreopoulos/Quan reference
carried the 2020 NBER draft's title ("The Impressive Effects of Tutoring...") rather than
the published title. Independently re-verified against the AERJ/ERIC/Semantic Scholar
records in this session. Reference corrected to "The Promise of Tutoring for PreK-12
Learning: A Systematic Review and Meta-Analysis of the Experimental Evidence,"
AERJ 61(1) 74-107, with the 2020 draft title noted as such. The 0.288-versus-0.37
distinction was already correct.
F-XA-2 (LOW) ABSORBED. "Not Too Late" was cited as "Cook et al." and the
reference led with Cook; the NBER/AEA record lists Guryan first, Cook fourth.
Independently re-verified (NBER w28531; AER 113(3) 738-765). In-text citations
changed to "Guryan et al. 2021/2023" and the reference reordered to official author order.
The cited effect and cost values were already supported.
F-XA-3 (LOW) ABSORBED. Section 5 invoked Goodhart without a reference entry. A
Goodhart (1975) reference with the Strathern (1997) popular formulation was added, and
the sentence now names Goodhart's law explicitly. The proposition was already
externally supported; this closes the paper's own citation-substrate gap.
F-XA-4 (LOW) ABSORBED [correction appended per F-AT-R2-02]. The companion
dataset README still described the parent paper as "currently v1.0-rc6." This
disposition originally stated the README was "Updated to v1.0-rc8"; in fact the

•

•

README edit set it to v1.0-rc7, not rc8, so this disposition overclaimed the fix and the
distributed README lagged the paper state -- exactly the documented-not-implemented
divergence the method exists to catch, here in this ledger. Corrected in v1.0-rc9: the
README is set to v1.0-rc9 in both its opening description and its citation block, verified
against the repackaged dataset. The original disposition text is preserved here per Section
14.5. The README also carries an explicit note that the dataset's public-archive DOI is
pending and that, until deposited, it is distributed as the file package accompanying this
companion (DOI 10.5281/zenodo.21436486) rather than as a separate DOI. README
em-dash glyphs were also converted to double-hyphens for house-style consistency.
F-XA-5 (LOW) ABSORBED. The Mahmud reference carried a paraphrased title.
Independently re-verified against EdWorkingPaper 25-1352; corrected to "Does StateMandated Third-Grade Reading Retention Policy Improve Achievement? Evidence from
a Staggered-Adoption Difference-in-Differences Design," Annenberg Institute at Brown
University. Author initial corrected to S. (Sakib). The cited Mississippi figures were
already supported.
F-XA-6 (LOW) ABSORBED. The README described the category recompute script
as cross-checking the category file "two ways," but the script's Part 2 reads the
walkthrough bridge terms (teacher-salary-change, register-change adjustment, collectivebargaining terms) from the top-level extract (file 1), not from the category-level rows
(file 3), because file 3 does not carry those top-level terms. The README was narrowed
to state this accurately: Part 1 uses category rows; Part 2 re-runs the top-level
walkthrough; the two files corroborate the reconstruction from different angles rather
than Part 2 being category-derived. This is a documentation-fidelity fix; the numerical
result was and remains correct and independently reproduced.

Refinement recorded (not a finding). The auditor independently recomputed the registerchange blended residual from the archived data and observed a range of about $1 to $37 (direct
residuals +$1.27, -$36.54, -$6.74, -$9.62, +$0.93), confirming the companion's "$1 to $60" as a
conservative envelope rather than the exact observed range. For accuracy, F-ED-13's residual is
characterized going forward as an observed range of approximately $1 to $37 within a disclosed
conservative envelope of $1 to $60; the earlier "$1 to $60" phrasing is preserved per Section 14.5
and annotated here.
Next audit cycle: one further independent, non-lineage audit round on the v1.0-rc8 corrected
artifact, returning 0 CRITICAL and 0 HIGH, closes the convergence gate and permits an
unqualified v1.0 label. Should that round raise any CRITICAL or HIGH finding, it is absorbed
and the two-round count restarts. The publish-the-dataset-DOI item remains open and would
strengthen the independence of that next round.
Appendix: v1.0-rc8 -> v1.0-rc9 amendments (second independent audit round: PASS on
severity, non-qualifying for convergence) [new in this artifact]
Per Section 14.5 no prior text is edited in place; the overclaimed F-XA-4 disposition is corrected
by appended annotation above, and this documents the round.
The round. An independent auditor of a non-Anthropic lineage (attested OpenAI/GPT) audited
v1.0-rc8: it ran both recompute scripts, independently re-derived the worked example, the Initialversus-Final decomposition, the base-rate identity, and the four rc8 citation corrections, and

checked the Tier, scope, deflation, and ED-K4 disciplines. Result: PASS at 0 CRITICAL, 0
HIGH, 1 MEDIUM, 1 LOW. The auditor confirmed the arithmetic, the citation fixes, the Tier-3
refusals, the deflated-magnitude discipline, the evidence-informed ED-K4 characterization, and
the non-extrapolated five-school scope, finding no unsupported empirical, causal, adequacy,
discrimination, or theological-validation claim.
Why it does not close convergence. The auditor expressly attested its execution was nonqualifying: it shares the OpenAI/GPT model family with the first-round (F-XA) auditor, and its
session was not context-independent. It offered the round as a regression audit, not as the second
convergence-counting round. This program accepts that judgment: two same-family rounds in
shared context do not satisfy the independence the gate intends. Convergence remains open
pending a different-lineage, fresh-context round.
Findings, both absorbed in v1.0-rc9:
•

•

F-AT-R2-01 (MEDIUM) ABSORBED. The reader paper's abstract and Section 5 still
stated the work "has not yet undergone independent cross-instance audit," contradicting
this companion's record that the first (F-XA) round had occurred and passed. Both
passages are corrected to state accurately that one independent round passed at 0
CRITICAL and 0 HIGH, that a second reproduced the result but was non-qualifying on
independence, and that the two-round convergence criterion is therefore not yet met and a
genuinely independent round is still required.
F-AT-R2-02 (LOW) ABSORBED. The companion's F-XA-4 disposition claimed the
dataset README was updated to v1.0-rc8, but the packaged README still read v1.0rc7 in both its opening description and its citation block: the recorded fix did not match
the distributed artifact, and additionally targeted the wrong version (rc7, when the paper
state was rc8). Corrected in v1.0-rc9: the README is set to rc9 in both places, the FXA-4 disposition is annotated above to record the overclaim honestly, and the dataset ZIP
is repackaged from the corrected README.

Next audit cycle: the convergence gate remains open. One genuinely independent round is
required -- a different auditor lineage (non-OpenAI, or a qualified human) in a fresh context,
returning 0 CRITICAL and 0 HIGH on v1.0-rc9 -- to stand as the second qualifying consecutive
round. Depositing the companion dataset to a public archive for its own DOI (F-ED-11) remains
open and would strengthen that round's independence.
Appendix: v1.0-rc9 third independent round (F-AT-R3, Gemini, first different-family):
PASS, convergence decision deferred [new in this artifact]
The round. An auditor of the Gemini family (attested outside the Claude/Anthropic producing
lineage and outside the OpenAI/GPT lineage of the F-XA and F-AT-R2 auditors, in a fresh
context) audited v1.0-rc9 and returned PASS at 0 CRITICAL, 0 HIGH, with 2 INFO findings
only (F-AT-R3-01, README bullet-spacing; F-AT-R3-02, a secondary-reference capitalization
variance). Both are INFO/monitor, carry unspecified loci, require no correction, and are not
absorbed as edits; they are logged for monitoring. The auditor deferred the convergence-counting
decision to the methodology owner.
Honest evidentiary note. This report is a valid different-family pass, which is what discharges
the correlated-blind-spot objection that blocked the two prior same-family (GPT) rounds from

counting. It is, however, lighter on shown verification than those rounds: it asserts that the
recompute, decomposition, base-rate identity, and citations confirm, but does not print
independently recomputed residuals, diffs, or values the way the F-XA and F-AT-R2 reports did.
Its independence is strong; its transparency of recomputation is weaker. This is recorded so the
round is not over-credited.
Convergence status: PENDING OWNER DECISION, not unilaterally declared met. Two
readings are on the record. (a) Met: two auditors of two different non-authoring families (GPT
round 1, Gemini round 3) both passed at 0 CRITICAL and 0 HIGH on identical analytical
substance (rc8 and rc9 differ only in provenance-label text, not in any analytical claim), no
failing round ever intervened, and the different-family requirement is now satisfied, so the gate's
purpose is served. (b) Not yet: strict "two consecutive qualifying rounds on the current artifact"
wants two clean passes on the same final artifact; round 1 passed on rc8, round 3 on rc9, and
round 3 is the first fully-qualifying round on rc9, so one further qualifying round on unchanged
rc9 would close the gate without any counting asterisk. The producing lineage's recorded
recommendation: because the substance has now cleared three independent rounds across two
non-authoring families, treat convergence as MET on substance and update the paper's status
language accordingly IF the methodology owner accepts reading (a); otherwise obtain one
further different-family or human round on unchanged rc9 that shows its recomputation, which
removes the last asterisk. Either way, depositing the companion dataset to a public archive (FED-11) remains the outstanding item that would make any such round's reproduction fully arm'slength. ### Appendix: v1.0-rc9 -> v1.0-rc10 amendments (fourth round F-AT-R4-NQ: producerlineage, NON-QUALIFYING; and reader/companion consistency repair) [new in this artifact]
Per Section 14.5 no prior finding text is edited in place; the convergence-status paragraph (a live
status field, not a finding) is updated to current, and this documents the round and the
consistency repair.
The round. A fourth audit was requested from the GLM/Zhipu family. The responding instance
identified itself as Claude/Anthropic -- the producing lineage -- and honestly declared its round
NON-QUALIFYING on that basis, refusing to claim distinct-family independence or to count
itself toward convergence. It performed a thorough show-your-work reproduction from the
archived dataset (walkthrough totals, category sums, DOE-versus-Comptroller-Initial exact
match, the full Initial-versus-Final residual table, the teacher-salary identity with a sensitivity
check confirming the rate pair is uniquely pinned, and base-rate provenance to the DOE deck),
and re-verified the citations against primary sources, all at 0 CRITICAL and 0 HIGH. As
producer lineage its findings are advisory (Standing Rule 7), but a factual citation defect it raised
was independently confirmable and is absorbed.
Findings:
•

•

F-AT-R4-NQ-01 (LOW) ABSORBED. The "Not Too Late" reference listed eleven
authors, ending at Steinberg; the published AER article (113(3), 738-765) and NBER
w28531 list twelve, the twelfth being Greg Stoddard. Independently confirmed against
prior primary-source search evidence. "and Stoddard, G." is appended in v1.0-rc10. The
F-XA-2 lead-author correction (Guryan first, Cook fourth) is unaffected.
F-AT-R4-NQ-03 (INFO) ABSORBED (optional consistency). The Chouldechova
reference truncated the title at the colon; the full title "Fair prediction with disparate

•

impact: A study of bias in recidivism prediction instruments," Big Data 5(2), 153-163, is
restored in v1.0-rc10 for consistency with the exact-title discipline applied elsewhere.
F-AT-R4-NQ-02 (INFO) NOTED, no change. The auditor could not re-extract the
1,164-schools / 700,000-students figures from the 2021 announcement's primary URL (it
redirected under automated fetch); the figures were verified in the F-XA round and
corroborated by Chalkbeat. A verification-access limitation, not a defect.

Consistency repair (the round's most useful contribution). The auditor observed that the
reader paper's abstract and Section 5 described only the F-XA and F-AT-R2 rounds and did not
mention the Gemini (F-AT-R3) round, and that the companion's front-matter convergence-status
paragraph was stale relative to the appended F-AT-R3 record. This is the same stale-frontmatter-status failure mode caught in the allocation note (F-AA-R2-05), here recurring in this
companion. Repaired in v1.0-rc10: the reader paper abstract and Section 5 now state the full
round history including the Gemini different-family pass; the companion convergence-status
paragraph is updated to the authoritative current status above. Standing remedy reaffirmed: a
single authoritative current-status field is updated every round, and no appended round is
considered absorbed until the front-matter status reflects it.
Next audit cycle: convergence remains open with exactly one qualifying different-family round
(Gemini). One further qualifying round -- a genuinely distinct family that shows its arithmetic -on v1.0-rc10 closes the gate under the strict reading. Depositing the companion dataset for its
own DOI (F-ED-11) remains the outstanding item that would make that round's reproduction
fully arm's-length. Note that the requested GLM/Zhipu round was not actually obtained (the
responder was the producing lineage); a real GLM/Zhipu or other distinct-family round is still
available to run.



Bismillah ir-Rahman ir-Rahim
