Bismillah ir-Rahman ir-Rahim

1

Bayyinah at-Taʿlīm
Structural Honesty Verification for Educational Fairness Systems, from Primary Schooling
to Graduate Research
Bilal Syed Arfeen (BayyinahEnterprise), with collaborative analytical assistance from
Claude (Anthropic).
DOI:

10.5281/zenodo.21444497

.

Audit

and

Provenance

Companion:

DOI

10.5281/zenodo.21436486 .
Companion to: Bayyinah at-Tartīb (Arfeen 2026, DOI 10.5281/zenodo.20070782); AlMutaffifīn (Arfeen 2026, DOI 10.5281/zenodo.19894724); Structural Honesty Verification: A
New Frontier (Arfeen and Ashraf 2026, DOI 10.5281/zenodo.20131072).
Audit trail, full version history, finding-by-finding provenance, and cross-vendor
verification discipline for this paper are published separately in the Audit and Provenance
Companion (see Provenance and Verification, Section 6). The FY2023 worked-example data and
recompute scripts are published as a Companion Dataset (see Data Availability, Section 8).
"And establish weight in justice and do not make the mizan deficient." (Ar-Rahman
55:9)

2
Abstract
Structural Honesty Verification (SHV) verifies the correspondence between a system's
surface (what it claims, reports, or certifies) and its substrate (what it actually distributes,
produces, or contains). This paper applies SHV to educational fairness across three tiers: primary
and secondary schooling, undergraduate admissions and assessment, and graduate research. The
central observation is that "fair" and "equitable" are surface claims that usually conceal which
mechanism is running, and that the algorithmic-fairness impossibility results make the choice of
fairness definition consequential rather than cosmetic. SHV does not choose the definition,
remove bias, or adjudicate merit; its contribution is to make an institution declare which fairness
definition its mechanism implements, to make resource and record divergences tamper-evident
and regression-gated, and to separate what is genuinely verifiable (funding, provenance, nondeletion, reproduction) from what is not (merit, equity, understanding). We organize the proposal
with a three-tier classification of what can and cannot be verified, present nine mechanisms
across the three educational tiers, and demonstrate the framework end-to-end on New York
City's Fair Student Funding formula, where a five-school FY2023 recompute reconstructs the
DOE's own allocation walkthrough from public data. The work is theoretical with one
operational worked example; it has undergone several independent cross-instance audit rounds
outside the authoring lineage, which passed with no critical or high-severity findings, including
one by a different model family; but not yet the two consecutive qualifying such rounds the
methodology requires for convergence, and its scope limits are stated explicitly.

3
1. Purpose and Scope
This paper applies Structural Honesty Verification (SHV) to educational fairness across
three tiers: primary and secondary schooling (K-12), undergraduate programs, and graduate and
masters research. SHV is the verification of correspondence between a system's surface (what it
claims, reports, certifies) and its substrate (what it actually distributes, produces, or contains),
across versions, contexts, and populations (Arfeen and Ashraf 2026). It composes with existing
accountability regimes; it does not replace them.
The central claim is deliberately narrow. SHV does not remove bias from education, does
not adjudicate which distribution of educational goods is just, and does not validate competence.
Its contribution is to make three things enforceable: (a) that an institution declare which
definition of fairness its mechanism implements, (b) that resource and record divergences
between surface and substrate be tamper-evident and regression-gated, and (c) that what is
genuinely verifiable (funding, provenance, non-deletion, reproduction) be separated from what is
not (merit, equity, understanding), with the second forbidden from borrowing the surface
language of the first.
2. The Governing Divergence: Declared Fairness versus Operative Fairness
"Fair" and "equitable" are surface claims that usually conceal which mechanism is
running. The algorithmic-fairness impossibility results establish that calibration and equalized
error rates cannot both hold once base rates differ across groups (Kleinberg, Mullainathan and
Raghavan 2016; Chouldechova 2017). Education inherits this as the equity-versus-equality split:
equal inputs and equal outcomes are different substrates and they conflict. An institution that
asserts "fair" without declaring its operative definition has already produced a surface-substrate
divergence.

4
SHV's first move is not to choose the definition -- that is a value judgment outside the
framework's authority -- but to make the declaration mandatory and machine-checkable, then to
verify that the substrate matches the declared definition rather than silently implementing a third
one.
3. Tier Discipline: What Can and Cannot Be Verified
The framework classifies every quantity it touches into one of three tiers, imported from
Al-Mutaffifīn (Arfeen 2026): Tier 1 (Verified) is a byte-deterministic structural address with
zero semantic interference; Tier 2 (Structural) is a bounded hybrid whose underlying data is
structural but whose aggregation introduces disclosed parameter choices; Tier 3 (Interpretive)
requires semantic adjudication and is refused as a verification target. The governing falsifiability
rule is that a mechanism labeled Tier 1 which requires the system to disambiguate semantic
meaning has leaked into Tier 3, and the framework is violated. Disambiguating a disclosed
parameter -- for example, which budget snapshot ("Initial" versus "Final") of a fiscal year is
being read -- is not a semantic disambiguation, but a result that depends on such a parameter to
reproduce is Tier 2, not Tier 1.
Educational quantity

Tier

Justification

Per-district

Tier 1

Structural address on

expenditure by zip code, per-

public ledgers; funding is a

pupil funding

number

Transcript credit

Tier 1

Structural facts with

records, degree conferral,

timestamps; append-only

prerequisite completion

checkable

Thesis artifact

Tier 1

Byte-deterministic

5
Educational quantity

Tier

Justification

reproduction (code plus data

regeneration; provenance, not

regenerate stated results)

merit

Subgroup-

Tier 2

Structural per-record

disaggregated outcome rates

facts, but binning and

(completion, placement)

population definition are
disclosed parameter choices

Enforcement of a

Tier 2

Structural once the

declared fairness definition

definition is fixed; definition

against substrate

choice is exogenous

Competence, merit,

Tier 3

Requires semantic

novelty, "understanding,"

adjudication; refused as a

equity-as-justice, funding

verification target

adequacy
No Tier 3 mechanism is proposed. The recurring failure mode in educational applications
is a Tier 3 quantity presented in Tier 1 surface language.
4. Mechanisms
4.1 Primary and Secondary (K-12)
Surface claim audited: "equal opportunity." Substrate: funding tied to local property tax,
tracking, gifted and AP access, exclusionary discipline, and promotion/retention gating.

6
ED-K1 (Tier 1) -- Cross-section funding audit. Scan expenditure and allocation ledgers
by district or school against the declared fairness definition, and emit a divergence signal where
the funding structure applies short measure relative to the system's own need-weighted formula
(the asymmetric-measure signature of Al-Mutaffifīn). The novelty is not the scan -- equity
dashboards already disaggregate -- but its pairing with ED-K2. Demonstrated end-to-end in
Section 4.4.
ED-K2 (Tier 1 gate over Tier 2 aggregation) -- Disaggregated regression gate. A
reform may not report aggregate improvement if any protected subgroup regressed without a
logged, signed justification. Student records are append-only with correcting entries, never
immutable: silent deletion is prohibited, logged correction is permitted, so the right to
rectification is preserved.
ED-K3 (Tier 1) -- Scan-incomplete rating declaration. An accountability rating must
carry a typed declaration of what it did not measure: students removed pre-test through
disciplinary action, narrowed curriculum, untested domains.
ED-K4 (Tier 2) -- Remediation-coupled mastery gate. A phased-progression or
mastery gate may fire only when both couplings below are present, disclosed, and logged.
Absent either, the gate is refused as unfit to deploy. This is a hard precondition, because a bare
mastery gate is grade retention, which the empirical record ties to disproportionate pushout of
low-income and minority students.
(a) Resourced, automatically-triggered remediation. On a logged non-mastery
determination, a remediation pathway must activate automatically, with no principal-discretion,
referral, or parent-request gap, because discretionary triggering preserves exactly the disparity

7
the mechanism exists to close even where the remediation infrastructure is nominally universal
(Westall, Utter and Strunk 2023). The pathway must disclose at minimum: (1) a dosage threshold
grounded in the tutoring-RCT evidence -- at least three sessions per week, 30 to 50 minutes each,
delivered by trained teachers or well-trained paraprofessionals, sustained for a semester or year
(Nickow, Oreopoulos and Quan 2024 report an overall pooled effect of 0.288 SD across 96
RCTs; the often-cited 0.37 SD figure is from the 2020 working-paper draft; Guryan et al.
2021/2023 report a treatment-on-treated effect of about 0.28 SD, persisting near 0.23 SD one
year later); (2) an itemized funding source and per-pupil cost, so the "resourced" claim is
auditable rather than symbolic, comparable in disclosure to Mississippi's Literacy-Based
Promotion Act (about $15 million per year; 29 to 74 literacy coaches; Mahmud 2025) or the
Saga Education model (about $1,800 to $4,800 per pupil; Guryan et al. 2021/2023); (3) a defined
timeline with a re-assessment checkpoint; and (4) mandatory logging of actual attendance and
uptake, not mere eligibility, since intent-to-treat versus treatment-on-treated gaps of two- to
fourfold are common (a University of Chicago Education Lab scale-up reports 0.04 SD versus
0.14 SD, a 3.5-fold gap).
(b) Independent, non-substitutable disaggregated gate. Coupling (a) does not by itself
discharge the equality requirement. Michigan's Read by Grade Three law paired comparable
remediation and exemption infrastructure with its retention gate; that infrastructure equalized
retention by race once test scores were controlled, but the economic-disadvantage disparity
persisted -- economically disadvantaged students remained 2.4 to 3.3 percentage points more
likely to be retained, unexplained by performance, exemption eligibility, district characteristics,
or mobility, with the retention "bite" from scoring just below the cutoff falling almost entirely on
them (4.5 points versus a statistically insignificant 0.3 for others; Westall, Utter and Strunk

8
2023). The disaggregated subgroup regression gate must therefore run independently and
continuously, regardless of whether coupling (a) is nominally in place.
Honest caveats. The evidence base for ED-K4 is suggestive and triangulated, not a single
clean causal test. NYC's own best causal evidence on test-based retention (Geng and Rockoff
2017) finds large positive test-score effects but explicitly excludes English language learners and
special-education students, so it has no subgroup answer for two of the populations the gate
exists to protect. Response to Intervention, often assumed to be the default remediation vehicle,
is mixed-to-negative in the most rigorous national evaluation, with a statistically significant
negative effect of -0.17 SD for first graders (Balu et al. 2015); if RTI is the chosen vehicle, EDK4 requires the higher-dosage, higher-fidelity variant with independent outcome monitoring.
And no located study directly compares "gate plus mandated remediation" against "gate plus no
remediation" on subgroup-disaggregated outcomes; the supporting evidence is quasiexperimental and policy-comparison-based (Mahmud 2025; Jacob and Lefgren 2002). ED-K4 is
therefore evidence-informed, not evidence-guaranteed, which is why coupling (b) is retained as
the primary safeguard.
4.2 Undergraduate
Surface claim audited: "holistic, merit-based." Substrate: preference structures, testoptional policies that relocate bias, algorithmic screening.
ED-U1 (Tier 2) -- Declared-definition enforcement. The process must publish which
fairness definition it runs and be audited for substrate consistency with it. The framework does
not adjudicate which definition is just; it detects a "race-neutral" surface reintroducing the
variable through proxies, or a "holistic" surface operating substantively as a class filter.

9
ED-U2 (Tier 2, bounded) -- Validator-by-different-instance grading. Route
anonymized, rubric-gradeable outputs to an independent cross-institutional grader to reduce
localized grader effects. This is N-version programming and carries the Knight-Leveson (1986)
independence-failure caveat: it relocates bias to the validator surface rather than removing it, and
applies only to rubric-gradeable work; essay, studio, clinical, and research outputs resist it.
ED-U3 (Tier 2) -- Mizan-calibrated abstention. Three-valued assessment (pass / fail /
insufficient-evidence) that removes some arbitrary curving by permitting explicit abstention
rather than forcing a point estimate. It does not remove demographic bias: calibration and
equalized error rates are mutually exclusive once base rates differ, and bias also resides in the
rubric, the items, and any automated grader's training data. The mechanism buys honest
abstention, not bias removal.
4.3 Graduate and Masters
Surface claim audited: program prestige and marketed placement; mentorship.
ED-G1 (Tier 1 precondition, never sufficient) -- Thesis reproduction gate. Dataset,
code, and text must regenerate the stated results deterministically as a necessary precondition for
defense. This gates provenance (Tier 1), not merit (Tier 3); presenting reproduction as sufficient
for graduation would be a Tier 3 leak. Merit adjudication remains a human Tier 3 judgment the
framework does not perform.
ED-G2 (Tier 2) -- Disaggregated program-outcome disclosure. Completion, funding,
and placement broken out by group and cohort, with a scan-incomplete declaration of what the
marketing surface omits (revenue-driven admits, funded versus unfunded two-tier cohorts).

10
ED-G3 (Tier 1 record over Tier 3 target) -- Advising-obligation ledger. Append-onlywith-correcting-entries logging of committee obligations met or missed. The ledger entry is a
Tier 1 structural fact with a timestamp; any inference about mentorship quality is Tier 3 and is
not emitted. Advising variance falls hardest on first-generation and underrepresented students
who lack informal networks to route around a poor advisor, so making the obligation surfacecheckable is itself an equality intervention.
4.4 Worked Example: NYC Fair Student Funding
This is the paper's one fully worked example, in the spirit of Al-Mutaffifīn's Lehman
Repo 105 case. It does not accuse the NYC Department of Education (DOE) of misconduct; it
measures.
The surface claim. Fair Student Funding (FSF), introduced in 2007, is New York City's
stated equity mechanism: a weighted-pupil model in which dollars follow students, each carrying
a base weight plus additive need weights (grade, academic intervention, English Language
Learner, special education, portfolio; from FY2024 also temporary housing and concentration of
need). FSF is the largest single stream a school receives, historically 60 to 70 percent of a
school's budget and 57 percent on average in FY2024. If implemented as stated, every school's
allocation would equal 100 percent of its formula-generated amount.
The substrate, Layer 1 (allocation versus formula). The DOE publishes, per school,
both the FSF allocation received and the formula amount the weights generate; their ratio is a
Tier 1 structural address. Historically the two diverged system-wide in one direction. Per the
Independent Budget Office (IBO 2013), the FY2011 median school received 75.4 percent of its
formula amount, with about 98 percent of schools below formula; FY2012 rose to an 86.0

11
percent median with 94 percent still below. At the weight-category level, IBO's regression found
that the implied weight for middle-school students below academic standards was negative -schools serving more of those students received less funding, not more -- and that elementary
and high-school ELL students and high-school special-education Collaborative Team Teaching
students were funded below their formula weight across the years studied. This is the
asymmetric-measure signature located precisely in the regression. Separately and at the school
level, Voloch (2015) examined 451 high-school budgets for 2013-14, found FSF ranging from
81 to 134 percent of formula with only 8.5 percent of schools fully funded (median 86.19
percent), and reported a statistically significant inverse relationship between a school's percentof-formula funded and its enrollment size, its share of low-income students, and its share of ELL
students.
Layer 1 resolution. New York City committed to funding every school at no less than
100 percent of formula beginning in the 2021-22 school year (announced April 19, 2021), an
investment described as reaching 1,164 schools and over 700,000 students, corroborated by
IBO's 2025 report. The divergence was closed by adding money while over-formula schools
were held harmless, not by reallocation. A five-school FY2023 recompute (below) independently
confirms the 100-percent floor was still in effect two fiscal years later.
Layer 2 (formula versus need). Closing Layer 1 relocated the honest question to the
formula itself. A 2022 Working Group concluded the formula under-captured concentrated need;
FY2024 added a Students in Temporary Housing weight and a Concentration Need weight.
IBO's May 2025 analysis found their magnitude small: the temporary-housing weight raised
affected budgets by about $78 per pupil, and the concentration-need weight raised 304 schools'

12
budgets by about $95,000 on average, which IBO judged unlikely to produce an observable
system-wide outcome effect, with possible year-to-year budget instability.
What the framework emits, and what it refuses. At Tier 1 it emits the allocation-toformula ratio and its resolution. At Tier 2 it emits the weight-category regressivity, the schoollevel inverse relationship, and the magnitude of the FY2024 corrective weights. At Tier 3 it
refuses to judge whether 100 percent of formula is adequate or whether the weights are the
correct weights -- and, notably, IBO itself drew the same line, confining its 2013 analysis to how
closely the DOE implemented the formula rather than whether the formula distributes funds
appropriately.
Formula reconstruction (Tier 2). From the DOE's published FY2023 FSF Detail
Reports for five sample schools (28Q160, 10X085, 30Q258, 14K488, 30Q148), the allocation
walkthrough was reconstructed independently: for each school the category-level line items sum
to the reported weighted-register total within $2, and the full walkthrough -- prior-year weighted
register at the prior-year base rate ($4,223.00), a teacher-salary-change term bridging to the
current-year rate ($4,197.19), a register-change adjustment, the $225,000 foundation, and three
collective-bargaining terms -- reproduces the DOE's own reported total within $2 to $18
(rounding) for all five schools. The base rates are sourced to the DOE FSF Working Group's
published year-by-year Base Weight Amount table, which also explains why the current-year
rate is lower than the prior-year one (average teacher salary fell for the first time in several years
due to increased retirements). This is a genuine mechanistic account of the walkthrough, not
merely an internal-consistency check. Its result is Tier 2, not Tier 1, because reconciling to the
DOE's published figure requires disclosing which report vintage ("Initial" versus "Final") is
being matched. The reconstructed figure matches the Comptroller mastersheet's FY2023 "Initial"

13
column exactly; the divergence from the "Final" column is only partially explained by the
disclosed register-relief and enrollment columns, with a net-positive rate/collective-bargaining
residual remaining for three of the five schools that the Initial-vintage walkthrough does not
itemize.
Scope of this example. The five-school recompute is a demonstration of reproduction
mechanics on real public data, not a population-level audit, and should not be extrapolated to all
roughly 1,500 FSF-funded schools without further sampling. All figures and the recompute script
are published in the Companion Dataset (Section 8).
5. Limitations
SHV verifies claim-to-mechanism correspondence; it supplies no value judgment about
just distribution, and treating it as a justice oracle would be the exact surface-substrate inflation
the framework exists to catch. Fairness metrics are vulnerable to Goodhart's law -- once a
measure becomes an optimization target it ceases to be a good measure (Goodhart 1975;
Strathern 1997) -- so every fairness key performance indicator requires a calibration bound and a
stated valid range. Auditing carries its own equality cost -- whose data, whose classrooms, whose
behavior is surveilled -- so the audit apparatus itself owes a scan-incomplete declaration.
The ED-K4 evidence base, though pinned to primary sources, does not settle the
underlying causal question: no located study directly compares gated-with-remediation against
gated-without-remediation on subgroup-disaggregated outcomes. The worked example is a fiveschool Tier 2 demonstration, not a system-wide audit. Most consequentially for how this paper
should be read: it has undergone multiple independent cross-instance audit rounds outside the
authoring lineage, all passing at zero critical and zero high-severity findings. The first (an

14
OpenAI/GPT auditor) passed with six low-severity findings absorbed. A second (also GPT)
reproduced the results but its auditor attested it did not satisfy the required independence, being
the same model family as the first, so it does not count. A third, by a different model family
(Gemini) in a fresh context, passed cleanly and is the first fully-qualifying different-family
round. The convergence criterion the broader methodology imposes -- two consecutive
qualifying rounds by an auditor outside the authoring lineage, each finding no critical or highseverity defects -- has therefore not yet been met: one further qualifying round on the current
artifact is required, and no claim in this paper should be read as having cleared that bar.
6. Provenance and Verification
This paper is the version-of-record statement of what is claimed and at what confidence.
The complete audit trail -- the finding-by-finding provenance ledger, the full version history and
its corrections, the per-claim verification tags, and the cross-vendor and convergence discipline
under which the work was produced -- is published separately in the Bayyinah at-Taʿlīm Audit
and Provenance Companion (DOI 10.5281/zenodo.21436486), so that a reader who wishes to
check how any claim was established, or how any earlier error was caught and corrected, can
trace it there. That companion is a load-bearing part of this research program: it is the
demonstration that the paper practices the structural honesty it proposes.
One provenance point is stated here because it governs how the framework may be used.
This research program draws its design vocabulary (the Tier discipline, the surface-substrate
frame, the asymmetric-measure signature) from structural readings of the Qur'an, but it does not
treat the Qur'an as a validated quantitative instrument for adjudicating educational outcomes, and
no mechanism in this paper requires it to be one. The program's own empirical work is explicit
and deflationary about the underlying textual-structure finding: roughly 82 percent of the

15
headline long-range autocorrelation gap it studies is attributable to an approximate length-sort,
the residual effect is small (about +0.10 to +0.15) and survives multiple-comparison correction at
only some lags, and an earlier claim of a Quran-specific Fibonacci growth pattern was falsified
and retracted. The Qur'an is a source of design primitives and diagnostic names, plus one small
candidate structural effect; any use of it as a truth-certifying oracle in another domain would
itself fail the verification the framework exists to perform.
7. AI Contribution Statement
The human author designed the research questions, the tier framework, and the
mechanism set, and takes responsibility for all claims. Claude (Anthropic) contributed analytical
synthesis, the worked-example verification and recompute, and drafting under the author's
direction, and is credited as a collaborative research tool, not a co-author. The verification,
correction, and audit history of this collaboration is documented in the Audit and Provenance
Companion.
8. Data Availability
The FY2023 five-school worked example is published as a Companion Dataset
(BayyinahEnterprise): per-school FSF Detail Report walkthrough extracts, category-level
weighted-register detail, the corresponding NYC Comptroller mastersheet rows, the FY2023
weight and per-capita reference table, and the recompute scripts, with a README stating
provenance and a CC-BY 4.0 license for the compilation. The underlying figures are public
records of the NYC DOE and the NYC Comptroller's Office.

16
References
Arfeen, B. S. (2026). Al-Mutaffifīn: Structural Integrity Verification for Financial Governance
Systems. Zenodo. DOI 10.5281/zenodo.19894724.
https://doi.org/10.5281/zenodo.19894724
Arfeen, B. S. (2026). Bayyinah at-Tartīb: Eight Engineering Strategies for Safety- and JusticeCritical Software, Anchored in Quranic Structural Primitives. Zenodo. DOI
10.5281/zenodo.20070782. https://doi.org/10.5281/zenodo.20070782
Arfeen, B. S. (2026). Bayyinah al-Munāsabāt: A Multi-Corpus, Multi-Pipeline Falsification
Study. Zenodo. DOI 10.5281/zenodo.20069654.
https://doi.org/10.5281/zenodo.20069654
Arfeen, B. S., and Ashraf, F. (2026). Structural Honesty Verification: A New Frontier. Zenodo.
DOI 10.5281/zenodo.20131072. https://doi.org/10.5281/zenodo.20131072
Balu, R., et al. (2015). Evaluation of Response to Intervention Practices for Elementary School
Reading. IES/MDRC (NCEE 2016-4000). https://ies.ed.gov/ncee/2025/01/20164000espdf
Chouldechova, A. (2017). Fair prediction with disparate impact: A study of bias in recidivism
prediction instruments. Big Data, 5(2), 153-163.
https://www.liebertpub.com/doi/abs/10.1089/big.2016.0047
Guryan, J., Ludwig, J., Bhatt, M. P., Cook, P. J., Davis, J. M. V., Dodge, K., Farkas, G., Fryer,
R. G. Jr., Mayer, S., Pollack, H., Steinberg, L., and Stoddard, G. (2021/2023). Not Too
Late: Improving Academic Outcomes Among Adolescents. NBER Working Paper 28531
(2021); American Economic Review 113(3), 738-765 (2023).

17
https://www.nber.org/papers/w28531 (University of Chicago Education Lab revision:
https://educationlab.uchicago.edu/wp-content/uploads/sites/3/2023/10/UChicagoEducation-Lab-Not-Too-Late-Paper_03.23.pdf)
Geng, T., and Rockoff, J. (2017). The Effect of Test-Based Retention on Student Outcomes.
Working paper. https://www.columbia.edu/~tg2430/GengRockoff_Retention.pdf
Goodhart, C. A. E. (1975). Problems of Monetary Management: The U.K. Experience. Papers in
Monetary Economics, Reserve Bank of Australia. (Popular formulation, Strathern, M.
(1997), "Improving ratings: audit in the British university system," European Review
5(3), 305-321: when a measure becomes a target, it ceases to be a good measure.)
Independent Budget Office (2013). Is It Getting Fairer? Examining Five Years of School
Funding Allocations Under Fair Student Funding. NYC IBO.
https://www.ibo.nyc.gov/assets/ibo/downloads/pdf/education/2013/2013-april-is-itgetting-fairer.pdf
Independent Budget Office (2025). What's in a Weight? Budgetary Impacts of FY24 FSF
Formula Changes. NYC IBO.
https://www.ibo.nyc.gov/assets/ibo/downloads/pdf/education/2025/2025-may-whats-in-aweight-budgetary-impacts-of-fy24-fsf-formula-changes.pdf
Jacob, B., and Lefgren, L. (2002). Remedial Education and Student Achievement: A RegressionDiscontinuity Analysis. NBER Working Paper 8918.
https://www.nber.org/system/files/working_papers/w8918/w8918.pdf
Kleinberg, J., Mullainathan, S., and Raghavan, M. (2016). Inherent trade-offs in the fair
determination of risk scores. ITCS 2017. https://arxiv.org/abs/1609.05807

18
Knight, J. C., and Leveson, N. G. (1986). An experimental evaluation of the assumption of
independence in multiversion programming. IEEE Transactions on Software
Engineering. https://doi.org/10.1109/TSE.1986.6312924
Mahmud, S. (2025). Does State-Mandated Third-Grade Reading Retention Policy Improve
Achievement? Evidence from a Staggered-Adoption Difference-in-Differences Design.
EdWorkingPaper 25-1352, Annenberg Institute at Brown University.
https://files.eric.ed.gov/fulltext/ED678324.pdf
New York City Department of Education. Chancellor's Regulation A-501 (Promotion
Standards). https://www.schools.nyc.gov/docs/default-source/default-document-library/
a-501-english.pdf
New York City Department of Education. Fair Student Funding: FY2023 FSF Guide and
Weight/Per-Capita Table; FSF Public App reports. NYC Public Schools. FSF Guide:
https://www.nycenet.edu/offices/finance_schools/budget/DSBPO/allocationmemo/
fy22_23/fy23_docs/FY2023_FSF_Guide.pdf ; Weights:
https://www.nycenet.edu/offices/finance_schools/budget/DSBPO/allocationmemo/
fy22_23/fy23_docs/fy2023_Weights.xlsx ; Public App:
https://www.nycenet.edu/publicapps/Offices/FSF/OverviewReports.aspx
New York City Office of the Mayor (2021, April 19). Historic Investment to Fully Fund Fair
Student Funding. https://www.nyc.gov/office-of-the-mayor/news/277-21/mayor-deblasio-speaker-johnson-schools-chancellor-porter-historic-investment-to

19
New York University Steinhardt, Metropolitan Center for Research on Equity. Revisiting "Does
the Fair Student Funding Formula Live Up to Its Name?"
https://steinhardt.nyu.edu/metrocenter/revisiting-does-fair-student-funding-formula
Nickow, A., Oreopoulos, P., and Quan, V. (2024). The Promise of Tutoring for PreK-12
Learning: A Systematic Review and Meta-Analysis of the Experimental Evidence.
American Educational Research Journal, 61(1), 74-107. DOI
10.3102/00028312231208687.
https://journals.sagepub.com/doi/10.3102/00028312231208687 (earlier NBER draft,
Working Paper 27476, 2020, was titled "The Impressive Effects of Tutoring on PreK-12
Learning"; https://www.nber.org/system/files/working_papers/w27476/w27476.pdf)
Voloch, D. (2015). Children First Reforms, Fair Student Funding and the Displacement of
Accountability in the New York City Department of Education. Ph.D. dissertation, CUNY
Graduate Center. https://academicworks.cuny.edu/cgi/viewcontent.cgi?
article=1633&context=gc_etds
Westall, J., Utter, A., and Strunk, K. O. (2023). Following the Letter of the Law: 2020-21
Retention Outcomes Under Michigan's Read by Grade Three Law. Education Policy
Innovation Collaborative (EPIC), Michigan State University.
https://files.eric.ed.gov/fulltext/ED672729.pdf



Bismillah ir-Rahman ir-Rahim
