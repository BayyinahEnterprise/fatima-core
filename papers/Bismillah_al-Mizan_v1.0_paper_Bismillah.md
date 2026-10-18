Bismillah ir-Rahman ir-Rahim

Bayyinah al-Mīzān
An Audit of the Audit: Reproducibility, Coverage, and Tamper-Evidence in Federal ImproperPayment Reporting
Governed by: "Bayyinah, Portable Structural Honesty Verification for Public-Service
Institutions" (Arfeen 2026, the framework paper), which imports Tier discipline from "AlMutaffifīn" (Arfeen 2026, DOI 10.5281/zenodo.19894724). Companion to "Bayyinah at-Taʿlīm"
(Arfeen 2026, DOI 10.5281/zenodo.21436484; formula-fidelity domain), "Bayyinah al-Amāna:
Provenance Integrity for Public Open Data" (Arfeen 2026, DOI 10.5281/zenodo.21446613;
paper) with its audit and provenance ledger (DOI 10.5281/zenodo.21446618; provenanceintegrity domain, converged after three cross-instance audit passes), and "AllocationAsymmetry"
(Arfeen 2026, DOI 10.5281/zenodo.21445552; MTA procurement/expenditure divergence and
vendor-concentration analysis), the sixth leg of the Bayyinah civic-integrity research program
alongside the NYC and DC procurement papers.
Prepared under BayyinahEnterprise audit methodology. Human authorship and copyright to be
assigned by project lead (Bilal Syed Arfeen); the AI system used as a collaborative research and
drafting tool.
"And establish weight in justice and do not make the mīzān deficient." (Ar-Raḥmān 55:9)

Verification Status (read this before citing any number below)
This note follows the Structural Honesty Verification (SHV) discipline used across the Bayyinah
corpus: Tier 1 = byte-deterministic, reproducible from a frozen public snapshot, zero semantic
interference; Tier 2 = structural but dependent on a disclosed classification or judgment call;
Tier 3 = requires semantic adjudication and is refused as a verification target. Every loadbearing number in this paper is tagged with its tier and its source in-line, not just in a
bibliography.
Provenance disclosure. This paper's occasion was a design sketch produced in a separate, prior
AI session (relayed to the author as three screenshots) proposing a federal-improper-payments
audit under the working title "Bayyinah al-Mīzān." Per this project's own standing discipline -never absorb a forwarded document's claims at face value -- every quantitative claim in that
sketch has been independently re-derived in this session against live or archived primary sources
before being used here. Where the sketch's numbers held up, they are re-cited to the primary
source, not to the sketch. Where they didn't hold up exactly, or where terminology in the sketch
could not be matched to this project's actual established vocabulary, that is stated explicitly
below rather than silently absorbed or silently dropped.
Component mapping. The prior sketch proposed mapping this paper onto named Bayyinah
"components" it called at-Taʿlīm ("formula fidelity") and al-Amāna ("provenance integrity").
Both mappings are confirmed against primary sources. On at-Taʿlīm: the corpus's own
"Procurement Concentration and Recoverable Savings in NYC Contracting" paper states, of its
companions, "the at-Ta'līm Fair Student Funding fidelity verifier (education equity, not cost
savings) and the AllocationAsymmetry paper... Where those papers focused on formula fidelity

and data-provenance integrity respectively," so at-Taʿlīm maps to formula fidelity. On al-Amāna:
it is a real published Bayyinah paper, "Bayyinah al-Amāna: Provenance Integrity for Public
Open Data" (DOI 10.5281/zenodo.21446613, published 2026-07-19, author Arfeen; Bilal Syed),
with a companion audit/provenance ledger and reproduction dataset (DOI
10.5281/zenodo.21446618) stating the artifact "converged after three consecutive independent
cross-instance audit passes" under Audit Framework v3.0 Standing Rule 7; both links were
independently fetched and confirmed in this session. The correction history behind both
mappings -- itself a small case study in why nothing here is absorbed without direct verification
-- is recorded in the append-only ledger.
al-Amāna's actual scope, read directly from its own abstract, is a meta-layer method: verifying a
dataset's declared provenance, freshness, and schema against its substrate, demonstrated on two
New York State Socrata datasets reporting the same MTA procurement records (a community
view, gpsc-qqsz, and the first-party official dataset, twsw-2mqa). This is a different paper, with a
different scope, from AllocationAsymmetry (MTA procurement/expenditure divergence and
vendor concentration) -- the NYC procurement paper's description of AllocationAsymmetry as
covering "data-provenance integrity" describes a thematic concern within that substantive
analysis, not a claim that AllocationAsymmetry and al-Amāna are the same artifact. Both are
companions to this paper; neither is a substitute for the other. This note now uses the confirmed
three-part mapping -- at-Taʿlīm as formula fidelity, al-Amāna as provenance integrity -alongside the general surface-versus-substrate divergence concept and the Tier 1 / Tier 2 /
Tier 3 discipline, both drawn from Bayyinah at-Taʿlīm §1 to 3, which in turn imports them from
Al-Mutaffifīn.

What has and has not happened to this note:
Step

Status

Live re-fetch of primary sources
(paymentaccuracy.gov, GAO, Treasury,
CBO)

Done -- this session, dated 2026-07-19/20

Independent computation of Tier 1 figures
from a frozen, hashed snapshot

Done -- see companion reproduction package

Producer's own re-check of the prior sketch's
claims against those sources

Done -- disposition stated per claim, Section 4

Cross-instance audit by a non-lineage Tier 1
auditor (Standing Rule 7)

Seven rounds completed (F-MZ-R1
through F-MZ-R7). The content converged
at F-MZ-R6 and F-MZ-R7 (two consecutive
qualifying passes, zero CRITICAL and zero
HIGH, on the byte-identical predecessor).
This v1.0 release re-versions the converged
content and is under confirming re-audit from
F-MZ-R8.

Two consecutive convergence rounds of 0
CRITICAL / 0 HIGH

Met by the predecessor content at F-MZR6 and F-MZ-R7. The v1.0 release form is
under confirming re-audit (F-MZ-R8
onward).

Per Standing Rule 7 of this project's audit methodology: a producer instance is excluded from
auditing its own lineage, and any self-review this note contains of its own numbers is advisory
only and does not count toward convergence. Every load-bearing figure below has been
independently reproduced to the digit by qualifying non-lineage auditors across the convergence
rounds; the v1.0 release form is under confirming re-audit.

1. Why This Paper Exists
The U.S. federal government publishes its own estimate of how much it pays incorrectly every
year. For fiscal year 2024 that estimate was about $162 billion; for fiscal year 2025 it rose to
about $186 billion (GAO-25-108172; GAO-26-108694, cited in the Treasury FY2025

Independent Auditor's Report). Cumulative estimates since fiscal year 2003, when the Improper
Payments Information Act first required this reporting, stood at about $2.8 trillion as of the
FY2024 reporting cycle and about $3.0 trillion as of the FY2025 cycle -- both figures taken
directly from GAO's own report text for each respective year, not from a secondary paraphrase
(GAO-25-108172: "cumulative improper payment estimates by executive branch agencies have
totaled about $2.8 trillion"; GAO-26-108694 (the direct GAO source for the FY2025-cycle
wording), also carried in the Treasury FY2025 Independent Auditor's Report and corroborated
by CRS Report R48296: "agencies have reported just under $3.0 trillion in improper payments").
CRS further reports that of that $3.0 trillion lifetime total, about $2.3 trillion (77%) is
concentrated in the same five program areas discussed in Section 4.3.
Two questions look identical at first glance but are not:
1.

How much money is actually being paid incorrectly? -- This requires access to
protected claims-level data (individual Medicare claims, individual SNAP eligibility
records, individual tax filings) that a public-data audit method has no lawful or practical
way to reach. GAO, agency Offices of Inspector General, and Congress have exactly this
access and exactly this mandate. This paper does not attempt to answer question 1, and
readers should not treat anything below as a re-estimate of the true improper-payment
total.

2.

Is the government's own published measurement of that total independently
reproducible, tamper-evident, and honest about what it does and does not cover? -This is a question about public data: the government's own website, the government's
own compliance-review determinations, and the government's own outlay totals. It

requires no access anyone lacks. And, as far as this paper can determine, no one has
published an independent, reproducible answer to it before this draft.
Bayyinah al-Mīzān is scoped entirely to question 2. It audits the audit.

2. Two Hard Truths, Stated Before Any Finding
Hard truth 1: this paper recovers zero dollars. Making a number measurable, reproducible,
and tamper-evident is a precondition for someone else (an appropriator, an inspector general, a
program manager) to act on it. It is not itself recovery, savings, or fraud detection. Any dollar
figure that appears below is diagnostic -- it describes what the government's own reporting says
or what a specific reproducible computation on public data yields -- never a claim about money
that could or should be recovered.
Hard truth 2: this paper's method is weakest exactly where the money is largest. Medicare
and Medicaid together account for roughly half of the entire government-wide improperpayment total (Section 4.3). Auditing those programs at the claims level -- the level at which
fraud and error actually happen -- requires protected data this method cannot touch. This paper
therefore does not audit Medicare's or Medicaid's underlying claims. It audits one layer up: the
rules under which those programs report, the outlay denominators they report against, and
whether the government's own summary of its own numbers reconciles with the government's
own underlying agency-level data. That is a real and previously-unaudited gap, but it is a
narrower gap than "how much fraud is in Medicare," and this paper does not pretend otherwise.

3. The Substrate: What Is Actually Public
Three federal data surfaces make this audit possible, and each has a specific role.
PaymentAccuracy.gov is the statutory public reporting site required under the Payment
Integrity Information Act of 2019 (PIIA, P.L. 116-117) and OMB Circular A-123 Appendix C
(PaymentAccuracy.gov, Resources). It is a JavaScript-rendered site with no visible bulk CSV
download link in its rendered HTML, but its pages embed the underlying data directly as HTML
attributes (data-series, data-sort-value, data-years) that any HTTP client can read without
executing JavaScript. Two pages carry the entire Tier 1 substrate for this paper:
•
•

/the-numbers/ -- three five-year chart series (payment accuracy rate, improper payment
rate, unknown payment rate), FY2021 to FY2025, government-wide.
/agencies-and-programs -- a single consolidated table covering all 83 reporting agencies'
FY2025 outlays, program counts, and rates. This is a materially more efficient substrate
than the per-agency-per-year page pattern (/agency/{CODE}/{YEAR}.html, confirmed
present in the site's sitemap for dozens of agency codes across 2021 to 2025+) that a
naive extraction approach would otherwise have to crawl one page at a time.

Individual agency pages (e.g. /agency/HHS/2024.html) carry program-level detail the rollup
table omits, including -- critically -- each agency's own stated PIIA compliance determination
and the specific list of programs found non-compliant (Section 4.4).
GAO reports and the Treasury Bureau of the Fiscal Service's annual Financial Report /
Independent Auditor's Report carry the headline dollar totals, the program-level concentration
breakdown, and cross-year comparisons that PaymentAccuracy.gov's current-cycle-only pages
do not directly expose. These are used here as an external comparison layer, cited to their own
URLs, never blended into the Tier 1 computed figures without the resulting divergence being
reported as a finding (Section 4.2).

CBO and Treasury fiscal reporting (Monthly Treasury Statement, Combined Statement of
Receipts, Outlays & Balances, CBO Monthly Budget Review) supply the total-federal-outlay
denominator needed for the coverage-ratio computation in Section 4.2.
A frozen, SHA-256-hashed snapshot of every file this paper's Tier 1 numbers are computed
from, plus the extraction script that recomputes them, ships as a companion reproduction
package (Section 8).

4. Tier 1 Findings -- Byte-Reproducible From a Frozen Public Snapshot
4.1 The government-wide rate series reproduces exactly
the-numbers.html's three chart blocks carry, verbatim, in data-series HTML attributes:

Year

Payment accuracy
rate

Improper payment
rate

Unknown payment
rate

2021

92.837%

7.052%

0.112%

2022

94.878%

4.443%

0.679%

2023

94.579%

4.396%

1.025%

2024

96.033%

3.659%

0.309%

2025

95.846%

3.835%

0.319%

(Source: PaymentAccuracy.gov, The Numbers, extracted from the page's own data-series/datayears attributes; reproduced by reproduce_mizan.py in the companion package. Tier 1.)
Each year's three series sum to essentially 100%, confirming they are complementary shares of
total spending in programs classified as susceptible to improper payments. The FY2024 (3.66%)
and FY2025 (3.83%) figures match the commonly cited headline rates exactly, independently

confirmed here directly from the government's own chart data rather than from any secondary
retelling.
4.2 The coverage ratio is real, and so is a reconciliation gap the government's own public
data does not fully resolve
Coverage ratio. Summing the "FY 2025 susceptible program outlays" column across all 83
agencies in the /agencies-and-programs rollup table yields $4,473.7 billion in outlays reported
inside programs classified as susceptible to improper payments (Tier 1, computed directly from
PaymentAccuracy.gov). Total federal government outlays for FY2025 were $7,010.0 billion
(Treasury Bureau of the Fiscal Service, FY2025 Combined Statement); net interest on the public
debt was approximately $1,030 billion, the first time it exceeded $1 trillion (CBO, Monthly
Budget Review: Summary for Fiscal Year 2025). Non-interest outlays were therefore
approximately $5,980 billion, and:
[ %]
This independently confirms, from primary sources computed directly rather than quoted from a
secondary summary, the widely repeated claim that the government's improper-payment
reporting regime covers roughly three-quarters of non-interest federal spending. (Denominator
basis, disclosed per F-MZ-R1: the non-interest figure subtracts CBO's net interest on the public
debt of about $1,028B -- the basis this paper uses -- from $7,010B total outlays. Treasury's net
interest outlays by function is about $970.4B; because it is smaller, it leaves a larger non-interest
denominator and therefore lowers the ratio, to about 74.07% ($4,473.7B / $6,039.6B), versus
about 74.79% ($4,473.7B / $5,982B) on the CBO basis. The coverage ratio is therefore methodsensitive to the net-interest definition -- both computed values are shown, and this paper uses the

CBO basis explicitly rather than leaving it implicit. Tier 2.) (The ~75% coverage figure is also
stated by GAO/CRFB analyses of the same GAO reports; this paper computes it directly from
the primary Treasury/CBO denominators above rather than relying on any secondary
restatement.)
The reconciliation gap (the actual novel finding of this section). The /agencies-and-programs
rollup table is the richest single public page for reconstructing the government-wide dollar total
independently. Multiplying each agency's reported outlays by its reported improper-payment rate
and summing across all 83 agencies yields an implied total of $171.7 billion for FY2025.
GAO's own headline FY2025 total, reported in the same reporting cycle, is $186 billion
(Treasury FY2025 Independent Auditor's Report, citing GAO-26-108694). The gap is $14.3
billion, or about 7.7% of the official total.
This gap is reported as a finding, not resolved. Plausible explanations include: rounding in the
two-decimal-place rate figures displayed on the public rollup table, compounded across agencies
with trillion-dollar outlay bases (a 0.01-percentage-point rounding error on HHS's $1.67 trillion
base alone moves the implied dollar total by about $167 million); the rollup table's rate column
being a program-count-weighted or otherwise-aggregated average that does not multiply cleanly
against the outlay column; or a genuine scope difference between "susceptible program outlays"
as displayed on the public table and the denominator GAO uses internally. This paper does not
adjudicate which explanation is correct -- that is exactly the kind of determination Tier 3
discipline reserves to the agencies, GAO, and IGs. What Tier 1 discipline requires is stating
plainly that the public rollup table alone does not reproduce the headline dollar total to the
last billion, which is itself a coverage/tamper-evidence finding: a citizen or researcher trying to
verify the $186 billion figure from the single richest page PaymentAccuracy.gov publishes

cannot do so exactly, and no supplementary reconciliation file explaining the gap was found on
the public site.
(Sanity check: dividing the implied $171.7B by the $4,473.7B outlay base yields 3.838%,
matching the 3.835% government-wide rate from Section 4.1 to three significant figures -- so the
rollup table is at least internally self-consistent, even though it doesn't fully match GAO's
separately reported headline dollar figure. Tier 1, reproduce_mizan.py.)
4.3 Program concentration, confirmed directly from GAO's own reports for both years
The commonly repeated "top-5-programs" concentration claim is confirmed here directly from
GAO's primary reports, not from any secondary paraphrase, and turns out to differ meaningfully
between the two years:
FY2024 (GAO-25-108172): "About 75 percent ($121 billion) of the government-wide total of
estimated improper payments that agencies reported for fiscal year 2024 is concentrated in five
program areas":
Program area

FY2024 improper payments

HHS -- Medicare

$54 billion

HHS -- Medicaid

$31 billion

Treasury -- Earned Income Tax Credit

$16 billion

USDA -- Supplemental Nutrition
Assistance Program

$11 billion

SBA -- Restaurant Revitalization Fund

$9 billion

Top 5 total

$121 billion (≈75%)

FY2025 (GAO-26-108694, cited in Treasury's FY2025 Independent Auditor's Report;
corroborated by a separate mirror of the same underlying GAO report text): "about 73 percent

(approximately $136 billion) of the government-wide total... is concentrated in five program
areas":
Program area

FY2025 improper payments

HHS -- Medicare (3 programs)

$57 billion

HHS -- Medicaid

$37 billion

Treasury -- Earned Income Tax Credit

$21 billion

USDA -- Supplemental Nutrition
Assistance Program

$10 billion

SBA -- Shuttered Venue Operators
Grant program

$10 billion

Top 5 total

$136 billion (≈73%)

Note the composition shift: the fifth-largest FY2025 contributor (SBA's Shuttered Venue
Operators Grant program) is a COVID-era program, while the FY2024 fifth-largest contributor
(SBA's Restaurant Revitalization Fund) is a "different" COVID-era program. This is Tier 1 in the
narrow sense that both tables are transcribed verbatim from GAO's own published figures; it
becomes a Tier 2 finding once combined with the reporting-universe question taken up in
Section 5.1.
Separately confirmed from the agency-level rollup table computed in Section 4.2: of the implied
$171.7B FY2025 total, HHS alone (Medicare + Medicaid + all other HHS susceptible programs
combined) accounts for an implied $97.4 billion, or 56.7% -- a higher single-agency
concentration than the "top 5 programs" framing alone conveys, because Medicare and Medicaid
are both housed at HHS (Tier 1, reproduce_mizan.py).

4.4 HHS's PIIA non-compliance, confirmed directly from the government's own
compliance-determination text
This is the strongest and most directly sourced Tier 1 finding in this paper, because it required no
computation at all -- only reading text the government itself published.
The PaymentAccuracy.gov HHS agency page carries a "Compliance with the Payment Integrity
Information Act of 2019" section stating, verbatim:
"HHS was found non-compliant during the most recent PIIA compliance review."
"Number of consecutive years HHS has been non-compliant: 3"
Immediately following is a list of 195 specific HHS programs the same page identifies as noncompliant, of which 189 cite, verbatim, the specific criterion: "Conducted Improper Payment risk
assessments for each program with annual outlays greater than $10,000,000 at least once in the
last three years in the most recent OIG PIIA Compliance report."
This directly and precisely confirms -- with an exact count, not an approximation -- the widely
repeated but rarely sourced claim that HHS has "hundreds" of unassessed risk assessments and
has been non-compliant for multiple consecutive years. The precise figures (195 programs; 189
specifically on the $10M risk-assessment criterion; 3 consecutive years) are new to this paper
relative to secondary coverage this author is aware of, and are reproducible by anyone who
fetches the same page (Tier 1, reproduce_mizan.py).
One caveat stated honestly: this page attributes the underlying determination to "the most recent
OIG PIIA Compliance report" without naming or linking that report directly. This paper did not
separately locate and independently confirm the underlying HHS OIG report itself -- the claim
above is confirmed as the government's own public restatement of that determination, not as an

independent re-derivation from the OIG source document. That distinction matters and is not
glossed over.
4.5 HHS's non-compliance is not an outlier -- it sits inside a government-wide pattern,
confirmed from Treasury's own audit report
The HHS-specific finding above understates how structural the compliance problem is.
Treasury's FY2025 Independent Auditor's Report states directly that Inspectors General
"reported noncompliance with PIIA for 12 of the 24 agencies covered by the Chief Financial
Officers Act of 1990 (CFO Act) for fiscal year 2024, the latest year available for the compliance
reports" (Treasury FY2025 Independent Auditor's Report) -- almost exactly half. The
Congressional Research Service's own synthesis states this more sharply still: "about half of the
24 largest federal agencies -- which account for 99% of improper payments -- are noncompliant
with PIIA in most years" (CRS Report R48296). Read together with Section 5.3's finding that
only 15 of 83 reporting agencies contribute any measured dollar at all, this means the entire
measured universe is concentrated in a small set of large agencies, roughly half of which are, in
most years, out of compliance with the very statute that requires the measurement in the first
place. This is Tier 1 in the sense that the 12-of-24 and "about half" figures are transcribed
verbatim from primary/first-party sources, but Tier 2 in the sense that "most years" and the 99%
attribution are CRS's own synthesis across years rather than a single reproducible computation
this paper performed itself.

5. Tier 2 Findings -- Disclosed Classification and Judgment
5.1 The reporting universe is not stable year to year, and the direction of that instability
does not cleanly support a single story
The prior design sketch that occasioned this paper proposed that FY2025's rise from FY2024
was explained by "better reporting" -- programs that failed to report in FY2024 reporting for the
first time in FY2025. Checking this directly against GAO's own topline counts complicates
rather than confirms that story: FY2024 had 16 agencies and 68 programs reporting; FY2025
had 15 agencies and 64 programs (GAO-25-108172; Treasury FY2025 Independent Auditor's
Report citing GAO-26-108694) -- fewer agencies and programs reported in the year the total
rose, not more.
At the same time, the specific composition of reporting programs did shift: SBA's Shuttered
Venue Operators Grant program appears in the FY2025 top-5 concentration table (Section 4.3)
but not the FY2024 one, and separate GAO testimony describes SBA's Shuttered Venue
Operators Grant program, along with HHS's Temporary Assistance for Needy Families and
HUD's Tenant-Based Rental Assistance, as risk-susceptible programs that did not report a
required estimate in at least one recent year (GAO written testimony, oversight.house.gov).
This paper's honest conclusion: the reporting universe visibly churns program-by-program from
year to year -- programs enter and exit the reported set -- but the net topline count moved in the
opposite direction from what a simple "more reporting explains the rise" story would predict.
Whatever explains the $24 billion FY2024→FY2025 increase, it is not simply "the universe of
reporting programs got bigger." This is exactly the kind of coverage-instability finding the
surface-versus-substrate framework exists to surface, and exactly the kind of claim this paper

declines to resolve further, because doing so would require attributing a cause to a $24 billion
change GAO itself has not, as far as this paper's sources show, decomposed publicly by programentry-and-exit effects. (Tier 2: structural facts -- agency/program counts, specific named
programs -- combined with a disclosed judgment that the "better reporting" causal story is not
well supported by those facts as they stand.)
5.2 The FY2023→FY2024 decline is explained by the government's own text, and that
explanation is about composition, not integrity
GAO's own FY2024 report states the $74 billion decrease from FY2023 to FY2024 "is largely
attributable to the completion or winding down of certain COVID-19 programs" (GAO-25108172). This is Tier 2 rather than Tier 1 because it requires accepting GAO's own attribution of
causation rather than an independently reproducible computation, but it is worth stating plainly
because the distinction it draws matters: a headline total falling because a temporary program
ended is a composition change, not evidence that ongoing programs became more accurately
administered. This paper takes no further position on how much of the $74 billion decline
reflects genuine improvement in ongoing programs versus mechanical COVID-program winddown, because doing so would require program-by-program before/after decomposition this
paper has not performed.
5.3 Most reporting agencies contribute nothing measurable, by their own declaration
Of the 83 agencies listed in the FY2025 rollup table, 68 report zero programs classified as
susceptible to improper payments -- meaning only 15 of 83 agencies (18%) contribute any
nonzero figure to the $171.7 to 186 billion total at all (Tier 1, reproduce_mizan.py, crosschecked against GAO's own count of "15 agencies reported" for FY2025). This is not evidence

that those 68 agencies have no improper payments -- susceptibility classification is itself a
disclosed agency determination under OMB Circular A-123 Appendix C, and this paper does not
audit whether any individual agency's "not susceptible" determination is correct. It is stated here
as a structural fact about the shape of the reporting universe: the entire measured system rests on
a small number of agencies' self-classifications, and the vast majority of federal agencies are, by
their own account, entirely outside the measured universe.
5.4 "Unknown payments" are a distinct, non-trivial category the headline number quietly
folds in
Section 4.1's table carries a third series most retellings of the headline number drop entirely: the
unknown payments rate -- payments a reviewer could not determine to be proper or improper,
most often for lack of sufficient documentation, rather than a determination that the payment was
wrong. That rate ran from 0.11% (FY2021) up to 1.03% (FY2023) before falling back to 0.31%
(FY2024) and 0.32% (FY2025) (Tier 1, PaymentAccuracy.gov, The Numbers, Section 4.1 table).
At FY2025's roughly $4.47 trillion susceptible-outlay base, 0.32% is on the order of $14 billion
-- a figure of the same rough magnitude as this paper's own reconciliation gap in Section 4.2, and
one worth naming precisely because "unknown" is a fundamentally different epistemic category
from "improper": it is a statement about the limits of what the measurement process could
determine, not a finding that money was misspent. GAO's own FY2025 breakdown of the $186
billion headline corroborates that most of the total is affirmatively classified rather than left
unknown: about 82% (~$153 billion) is categorized as overpayments, with the remainder split
across underpayments, unknown payments, and technically improper payments (GAO-26108694). This paper does not attempt to reconcile the government-wide "unknown payments
rate" series in Section 4.1 against that program-level overpayment/underpayment/unknown

breakdown -- doing so would require the same kind of program-by-program mapping this paper's
Limitations section (7) flags as unresolved elsewhere -- but records both facts side by side as a
Tier 2 finding: the headline total is not purely "money paid wrongly," and the government's own
reporting does not make it trivial to see how much of it is that versus simply undocumented.

6. Tier 3 -- What This Paper Explicitly Refuses to Claim
Per the SHV Tier discipline, the following are refused as verification targets in this paper,
regardless of how the underlying numbers might tempt a reader toward them:
•

•
•

•

No "true" improper-payment total. This paper does not estimate, imply, or gesture
toward what the correct figure "really" is, for any program, agency, or the government as
a whole. The $162B/$186B figures are audited as the government's own claim, not
treated as either confirmed or as a floor on some larger true number.
No recoverable-savings figure. Nothing in this paper should be read as "$X billion
could be recovered." See Hard Truth 1.
No adjudication of any individual agency's susceptibility or compliance
determination. Whether HHS's 195 flagged programs, or any other agency's
determination, is correct -- as opposed to accurately reported by the agency itself, as this
paper confirms it is -- is a question for GAO, the relevant Inspector General, and
Congress, not for a public-data audit.
No fraud accusation, implied or explicit, against any agency, program, or
individual. This paper's findings are about the reproducibility and internal consistency of
a public measurement system, not about wrongdoing.

7. Limitations, Stated Plainly
•

This paper is a v1.0 release whose content converged under Standing Rule 7 across
F-MZ-R6 and F-MZ-R7 (two consecutive qualifying cross-instance passes, zero
CRITICAL and zero HIGH); the release form is under confirming re-audit from FMZ-R8. The Tier-1 numeric core (the rate series, the FY2025 rollup reconciliation, the
$14.3B / 7.7% gap, the HHS facts) was reproduced to the digit from the live source by
every qualifying member in every round; the NON-PASS verdicts rest on packetcompleteness and documentation defects, not on any disputed figure. Per Standing Rule
7, the author's own review remains advisory and does not substitute for the two
consecutive zero-CRITICAL/zero-HIGH rounds convergence requires.

•

•
•
•
•

The FY2025 agency rollup table has no FY2024 equivalent on the same page
structure, so the agency-level reconciliation-gap computation in Section 4.2 could only
be performed for FY2025, not FY2024. Whether the same ~7.7% gap recurs in FY2024
or other years is untested.
The HHS PIIA non-compliance determination (Section 4.4) is confirmed as the
government's own public restatement, not independently re-derived from the
underlying OIG report, which was not separately located and read in this session.
The reconciliation gap in Section 4.2 is reported, not explained. Three plausible
mechanical explanations are offered; none is confirmed, and this paper does not claim to
know which (if any) is correct.
This paper's method structurally cannot reach the largest-dollar programs'
underlying claims data (Hard Truth 2). Everything here operates one layer up from
where the actual improper payments occur.
No USAspending.gov API pull was ultimately needed or performed; the FY2025
outlay denominator came directly from the PaymentAccuracy.gov rollup table itself,
cross-checked against Treasury/CBO government-wide totals, which proved sufficient
and more directly traceable than a separate USAspending.gov reconciliation would have
been. This is noted because an earlier version of this project's own plan called for a
USAspending.gov pull specifically; that step was superseded, not skipped by oversight.

8. Companion Reproduction Package
A companion package ships alongside this draft containing:
•
•
•

•

MANIFEST.json -- every source file's exact URL, its role in this paper's Tier 1 claims,
and its SHA-256 hash.
reproduce_mizan.py -- a script that parses the frozen snapshot and reproduces every Tier
1 number in Sections 4.1, 4.2, and 4.4 from scratch, with no hand-typed intermediate
figures.
snapshot/ -- the frozen source pages (the-numbers, agencies-and-programs, HHS/2024)
that the Tier 1 numbers are computed from. The canonical rollup URL is the no-slash
form https://paymentaccuracy.gov/agencies-and-programs; the trailing-slash form
redirects to the site home page, so re-derivations should use the no-slash form, which the
MANIFEST pins.
data/ -- the parsed seed snapshot (values + hashes + sitemap map) and README.md.
(The package ships reproduce_mizan.py, MANIFEST.json, snapshot/, and data/; there is
no separate output/ directory -- the script prints its results to stdout and returns a nonzero
exit on any mismatch.)

Anyone can re-fetch the live URLs listed in MANIFEST.json and diff the resulting hash against
the frozen snapshot. A mismatch means the government has changed the underlying page since

this snapshot was taken -- which is, under this paper's own tamper-evidence standard, a finding
to be logged in a future version, not a reason to silently update this version's numbers without a
record of what changed.

Append-Only Ledger
Appendix: v0.1 initial draft [superseded text preserved below]
First draft, written in a single session. Occasioned by a design sketch (three screenshots) from a
separate prior AI session proposing this paper's scope and structure. Every quantitative claim in
that sketch was independently re-derived against primary sources before use here. v0.1 stated the
following, since corrected: (a) it rejected the sketch's "at-Taʿlīm = formula fidelity" mapping
outright as an invented generic-component name; (b) it cited the lifetime cumulative improperpayment total as "roughly $3 trillion" via a secondary source (ANCOR) without distinguishing
which reporting-cycle vintage that figure belonged to; (c) it did not include a government-wide
PIIA compliance finding beyond the HHS-specific one, nor a dedicated treatment of the
"unknown payments" category. No audit round had occurred as of v0.1.
Appendix: v0.2 corrections [superseded text preserved below]
Triggered by a second, independently produced comparison draft of this same paper (a separate
AI system, forwarded by the author for comparison) that used the same original design sketch as
its occasion. Per this project's standing discipline, the comparison draft's claims were not
absorbed on the comparison draft's authority; each was checked against primary sources before
any change was made here. Three corrections and two additions resulted:

1.

2.

3.

4.

5.

Terminology, corrected (not merely re-flagged). v0.1's rejection of "at-Taʿlīm =
formula fidelity" was itself wrong. The corpus's own "Procurement Concentration and
Recoverable Savings in NYC Contracting" paper (already present in this workspace, not
newly introduced) states directly that at-Taʿlīm and AllocationAsymmetry "focused on
formula fidelity and data-provenance integrity respectively." So at-Taʿlīm = formula
fidelity is confirmed corpus usage. What v0.1 got right, and what v0.2 retains: no paper
or component named "al-Amāna" was found anywhere in the accessible corpus; the paper
that actually occupies the provenance-integrity role is AllocationAsymmetry. The
comparison draft repeated "al-Amāna" from the same original sketch without
independently checking it either -- this appears to be an error that originated in the design
sketch and was carried forward uncritically by more than one AI system, which is itself a
useful illustration of why this project's standing discipline requires independent reverification rather than trusting a forwarded document, however confidently it is written.
Cumulative total, corrected. "Roughly $3 trillion" (v0.1, via ANCOR) is replaced with
vintage-specific figures taken directly from GAO's own report text: about $2.8 trillion as
of the FY2024 cycle, about $3.0 trillion as of the FY2025 cycle (Section 1), plus CRS's
corroborating breakdown that ~77% of the $3.0 trillion lifetime total sits in the same five
program areas as the current-year concentration finding.
New Tier 1/2 finding added (Section 4.5). Treasury's FY2025 Independent Auditor's
Report states 12 of the 24 CFO Act agencies were found non-compliant with PIIA for
FY2024 -- almost exactly half -- corroborated by a CRS synthesis describing this as a
persistent, most-years pattern across the agencies that account for 99% of improper
payments. This generalizes the HHS-specific compliance finding (Section 4.4) into a
government-wide structural finding, independently confirmed from Treasury's and CRS's
own report text, not adopted from the comparison draft's wording.
New Tier 2 finding added (Section 5.4). The "unknown payments" rate series (already
present in this paper's own Section 4.1 table, drawn from the same primary source) is
given its own dedicated treatment distinguishing it from "improper," cross-checked
against GAO's own overpayment/underpayment/unknown breakdown for FY2025.
One comparison-draft claim explicitly not incorporated. The comparison draft
asserted that, among programs reporting in both FY2023 and FY2024, "a little over half
reported a lower rate, but only about a third reduced the actual dollar amount." This is a
plausible and interesting claim, but this paper could not locate a primary-source table
stating it directly within the time available for this revision, and declines to include it
without that confirmation. It is recorded here, unincorporated, rather than silently
dropped, so a future revision can pick it up if the underlying program-level rate/dollar
table is located and independently checked.

No audit round has occurred as of v0.2. Item 5 of this project's standard convergence criterion
(independent cross-instance audit by a non-lineage Tier 1 auditor, two consecutive rounds of 0
CRITICAL/0 HIGH) remains fully open. Per Standing Rule 7, the corrections above are the
producer's own advisory self-review and do not themselves count as audit convergence.

Appendix: v0.3 correction [this artifact]
Triggered by the author directly supplying two live Zenodo links in this session:
zenodo.org/records/21446613 and zenodo.org/records/21446618. Both were independently
fetched and read in this session before this correction was made -- the links were not accepted on
the author's authority alone, consistent with this project's standing discipline applying equally to
author-supplied evidence as to AI-produced comparison drafts.
The error being corrected. v0.2's Appendix (above) states: "no paper or component named 'alAmāna' was found anywhere in the accessible corpus." This was wrong. "Bayyinah al-Amāna:
Provenance Integrity for Public Open Data" is a real, separately published paper (DOI
10.5281/zenodo.21446613, published 2026-07-19, author Arfeen; Bilal Syed), with its own
converged audit and provenance ledger (DOI 10.5281/zenodo.21446618, "converged after three
consecutive independent cross-instance audit passes" under Audit Framework v3.0 Standing
Rule 7).
Root cause of the error, stated plainly. v0.2's search for "al-Amāna" was a grep across this
session's local workspace attachments -- the uploaded corpus files listed at the start of this
session -- not a search of the author's full published output. Absence from that local corpus was
reported as if it were absence from existence. This is a narrower version of the same failure mode
this project's discipline exists to prevent (accepting an unverified claim), just committed in the
negative direction: concluding a thing does not exist because it was not found in an incomplete
search space, rather than concluding a thing is true because a forwarded document said so. Both
are the same underlying error -- treating the boundary of what was checked as the boundary of
what is real.

What changed as a result. (1) The document header now lists al-Amāna as a named companion
paper with its DOI and its ledger's DOI. (2) The Verification Status terminology-correction
paragraph now states the confirmed three-part mapping: at-Taʿlīm = formula fidelity, al-Amāna
= provenance integrity (verifying a dataset's declared provenance, freshness, and schema against
its substrate -- read directly from al-Amāna's own abstract, not inferred), and
AllocationAsymmetry as a distinct substantive-analysis paper (MTA procurement/expenditure
divergence and vendor concentration) that is thematically adjacent to but not identical with alAmāna. (3) Section 7's Limitations entry and the Version header are updated to v0.3. No Tier
1/2/3 quantitative finding in Sections 4 to 5 of this paper changes as a result of this correction -it is confined to the terminology/attribution framing in the header and Verification Status section.
No audit round has occurred as of v0.3. Item 5 of this project's standard convergence criterion
(independent cross-instance audit by a non-lineage Tier 1 auditor, two consecutive rounds of 0
CRITICAL/0 HIGH) remains fully open. Per Standing Rule 7, this correction is the producer's
own advisory self-review, prompted by author-supplied evidence, and does not itself count as
audit convergence.
Appendix: v0.4 absorption [superseded by v0.5 corrections below]
Produced by Claude (Anthropic) as collaborative tool, folding in the two refinements the F-MZR1 council surfaced: (a) the coverage-ratio denominator basis was disclosed explicitly in Section
4.2 (which net-interest figure is subtracted); (b) the Federal News Network "183b" URL and the
civicintelligence.news corroboration were replaced with primary GAO sources; and the prior
draft's 81 em/en-dashes were normalized to house style. v0.4 also updated the version header to
reflect that F-MZ-R1 had completed. It did not, however, update the Verification Status table or

the Limitations section to match (they still read "v0.3 / no round has occurred"), and it
introduced a directional error in the new denominator-basis sentence (stating the Treasury basis
would raise the coverage ratio when it lowers it). Both defects were caught in F-MZ-R2 and are
corrected in v0.5.
Appendix: v0.5 correction [this artifact]
Triggered by the F-MZ-R2 cross-instance round (three qualifying non-lineage members: GPT
5.5, Gemini 3.1 Pro, GPT 5.4; findings-bearing NON-PASS; count ZERO). Execution was clean:
all three members genuinely executed the live re-pull with three distinct correct hashes and
completed the whole-paper Tier-3 scan, and the $14.3B / 7.7% reconciliation gap was tripleconfirmed from the live source with rounding bounded at about 1/64 of the gap. The NON-PASS
rested on documentation and packet defects, several of them introduced by the v0.4 absorption
itself. v0.5 corrects them: (1) the Verification Status table and Limitations section are updated to
v0.5 / two-rounds-completed / count ZERO, resolving the header-versus-body contradiction (FMZ-R2-002); (2) the Section 4.2 denominator-basis direction is corrected -- the Treasury basis
lowers the ratio to about 74.07% versus 74.79% on the CBO basis, both now shown (F-MZ-R2003); (3) the direct GAO-26-108694 page is cited for the $3.0T-cycle wording (F-MZ-R2-004);
(4) Section 8's documented package layout is aligned with the actual artifact, and stale
reproduce.py references are corrected to reproduce_mizan.py (F-MZ-R2-005); (5) the CRS
citation is moved from the everycrsreport.com mirror to the official crsreports.congress.gov
endpoint (F-MZ-R2-006); and (6) a standalone citation ledger is now shipped as a separate
artifact, resolving the packet-completeness finding (F-MZ-R2-001). No Tier-1 figure changed.
Per Standing Rule 7, this correction is advisory producer self-review prompted by the round's
findings, and does not itself count as audit convergence; the count remains ZERO.

Appendix: v0.6 correction [this artifact]
Triggered by the F-MZ-R3 cross-instance round (three qualifying non-lineage members: GPT
5.5, GPT 5.4, Gemini 3.1 Pro; findings-bearing NON-PASS; count ZERO). The Tier-1 numeric
core reproduced exactly for the third consecutive round, including a hash-validated independent
live re-pull by all three members, and the $14.3B / 7.7% gap was triple-confirmed with rounding
bounded at about 1/64 of the gap; the refusal boundary held across three whole-paper scans. The
NON-PASS rested on three documentation defects, two of them regressions or partial-lands of
R2 fixes. v0.6 corrects them: (1) the Verification Status table's second status row, which still
read "no audit round has occurred" one row below the row correctly stating rounds had
completed, is rewritten so every row of the current-status body agrees that three rounds have
completed and the count is ZERO (F-MZ-R3-001, a regression of F-MZ-R2-002; the R2 fix had
updated one table row but not its sibling, and the producer's verification search had used too
narrow a phrase to catch the second row); (2) the standalone citation ledger's FY2024 row is
realigned to the same GAO source the paper's Section 1 cites, restoring ledger-to-paper URL
agreement (F-MZ-R3-002); and (3) Section 8's duplicated directory bullet is removed so the
described package layout matches the shipped artifact (F-MZ-R3-003). No Tier-1 figure
changed. The producer verified each edit landed and ran a widened whole-document check
across every status row, every version locus, the ledger-to-paper citation alignment, and the
Section 8 bullets, rather than a single-phrase search, to avoid repeating the partial-absorption
pattern that produced F-MZ-R3-001. Per Standing Rule 7 this correction is advisory producer
self-review; the count remains ZERO.

Appendix: v0.7 correction [this artifact]
Triggered by the F-MZ-R4 cross-instance round (three qualifying non-lineage members: GPT
5.5, GPT 5.4, Gemini 3.1 Pro; findings-bearing NON-PASS; count ZERO, fourth consecutive).
The Tier-1 numeric core is now quadruple-confirmed: across four rounds, ten independent
qualifying-member executions reproduced the $14.3B / 7.7% reconciliation gap to the digit from
the live source, with the same hash and byte count every time; the coverage-ratio direction, the
HHS concentration, the susceptibility structure, and the refusal boundary held in every round.
Nothing in the arithmetic is in dispute. The NON-PASS rested on three defects, two of them the
producer's recurring partial-absorption pattern. v0.7 corrects them: (1) a Section 7 Limitations
bullet that opened with "three independent cross-instance audit rounds" but four clauses later still
read "in both rounds" is corrected so no clause in the current-status body references any round
count other than the current one (F-MZ-R4-002, the same one-clause-away sibling drift as FMZ-R3-001, a fourth instance; the producer's prior widened checks searched too narrow a set of
round-count strings); (2) the standalone citation ledger is realigned to the paper by URL set
reconciliation rather than row by row: the www and non-www PaymentAccuracy forms are
unified to the paper's form (rows 11, 12, 20), the FY2025 rows that cite the Treasury
Independent Auditor's Report in the paper now cite it in the ledger too (rows 18, 21), the
reporting-universe row is aligned to the GAO-25-108172 source the paper leads with (row 22),
and the paper's load-bearing GAO oversight-testimony source is added as a ledger row (F-MZR4-003, the sibling-row residual of F-MZ-R3-002; row 6 alone had been fixed in v0.6); and (3)
the reproduction package, which was omitted from the R4 dispatch packet and left three
members unable to run the mandatory execution steps, is a packet-assembly correction rather
than a paper edit: the package exists and must be included in the R5 packet and diffed against

Section 8 before dispatch (F-MZ-R4-001). No Tier-1 figure changed. This time the producer
verified the citation class by extracting every URL from both files and computing the set
difference, not by inspecting the named rows, to break the four-round pattern of fixing the
flagged locus and missing its siblings.
Appendix: v0.8 correction [this artifact]
Triggered by the F-MZ-R5 cross-instance round (three qualifying non-lineage members: GPT
5.5, GPT 5.4, Gemini 3.1 Pro; findings-bearing NON-PASS; count ZERO, fifth consecutive).
The Tier-1 numeric core is now quintuple-confirmed: all three members reproduced the hashes,
the $4,473.7B coverage, the $171.7B implied total, the $14.3B / 7.7% gap, and HHS $97.4B /
56.7% to the digit from an independent live re-pull of the canonical rollup URL, and the refusal
boundary held for the fifth time. All three R4 regression targets landed on their strings (package
present, round-count sweep zero, URL set clean). The NON-PASS rested on one HIGH finding
and one INFO.
F-MZ-R5-001 (HIGH): older version labels (v0.1 through v0.5) still appeared in the currentstatus body at three loci -- the terminology-correction narrative and the coverage-ratio directioncorrection parenthetical -- violating the D7 invariant that version labels appear only in the
appendix. This is the third instance of the same drift-hygiene family as F-MZ-R3-001 (siblingrow) and F-MZ-R4-002 (sibling-clause), and the pointed part is that the producer wrote that
exact invariant into the R5 brief and then failed it in the paper. v0.8 corrects it structurally: the
terminology paragraph now states only the corrected conclusions (at-Taʿlīm maps to formula
fidelity; al-Amāna is a real published Bayyinah paper, cited to its two Zenodo records), and the
coverage paragraph states only that the Treasury basis lowers the ratio; the version-labeled

correction history is carried here in the append-only ledger, where it belongs. Verification was
widened to the exact regex the synthesizer prescribed, case-insensitive \bv0\.[1-6]\b across the
entire current-status body, returning zero body matches; this regex is now a standing pre-dispatch
gate for this paper.
The correction history moved out of the body, preserved: an earlier draft first rejected the atTaʿlīm mapping (wrongly, on the ground that at-Taʿlīm names a specific education paper rather
than a generic component), then corrected it against the NYC procurement paper's own statement
that at-Taʿlīm is a Fair Student Funding fidelity verifier; and an earlier draft concluded no alAmāna paper existed, from an incomplete workspace search space, before the author supplied
the two live Zenodo records that confirm al-Amāna is real. Both are small case studies in why
nothing here is absorbed without direct verification against the actual universe of published
work.
F-MZ-R5-002 (INFO): Gemini filed a HIGH claiming the live rollup URL now redirects and the
gap zeroed to 100%, but GPT 5.5 and GPT 5.4 showed on re-derivation that Gemini had fetched
only the trailing-slash form; the canonical no-slash URL the paper and MANIFEST cite still
returns the correct rollup exactly. The finding was downgraded to INFO. v0.8 pins the canonical
no-slash URL in Section 8 and notes that the trailing-slash form redirects, so future rounds do
not re-file this on the wrong variant. No Tier-1 figure changed. Per Standing Rule 7 this
correction is advisory producer self-review; the count remains ZERO.
Appendix: v1.0 release [this artifact]
The predecessor draft converged under Standing Rule 7 across F-MZ-R6 and F-MZ-R7: two
consecutive qualifying cross-instance rounds, conducted by fresh non-Claude auditors (GPT 5.5,

GPT 5.4, Gemini 3.1 Pro) on byte-identical bytes, each returning zero CRITICAL and zero
HIGH after documented independent execution (reproduction package run, hash-validated live
re-pull from the canonical no-slash rollup URL, and the three drift-hygiene gates all returning
zero). The numeric core is septuple-confirmed across the seven-round arc. This v1.0 release reversions that converged content unchanged in substance: only the version label and the
verification-status framing are updated to record the convergence. Because the release carries
new bytes, it is placed under confirming re-audit (F-MZ-R8, F-MZ-R9); a second consecutive
qualifying pass on the release form completes its convergence. No Tier-1 figure, citation, or
refusal changed in the promotion. The full round-by-round absorption history (v0.1 through
v0.8) is preserved above in this append-only ledger; the standalone convergence record
documents the R6 and R7 certification.



Bismillah ir-Rahman ir-Rahim
