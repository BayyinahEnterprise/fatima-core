Bismillah ir-Rahman ir-Rahim

1

Procurement Concentration and Potentially Recoverable
Competitive Savings in New York City Contracting
A Cost-Recovery Proposal and Pilot Design
Bayyinah Civic Integrity Program -- Working Paper (Version 1.0, converged: F-PCR1 NON-PASS, then F-PC-R2 and F-PC-R3 qualifying passes; consecutive qualifyingPASS count TWO; rotation closed) Prepared July 2026. Corresponding: Bilal Arfeen,
BayyinahEnterprise. DOI: 10.5281/zenodo.21447217. Audit and provenance ledger and dataset:
DOI 10.5281/zenodo.21447219.
Audit status notice: This paper was originally synthesized by a single AI instance in a
single research session from primary-source data (NYC Comptroller vendor-level microdata, NY
State MTA procurement data, and academic procurement-savings literature), and at first had not
been through the multi-round independent audit process applied to Bayyinah's other civicintegrity papers (at-Ta'līm and AllocationAsymmetry). Its empirical spine (the concentration
measurement, the savings arithmetic, the MTA cross-check, and the Appendix 1 reconciliation)
has since been independently reproduced and audited across three cross-instance rounds: F-PCR1 returned NON-PASS on one HIGH finding (a false quantitative assurance in the Section 5.0
basis note) plus supporting findings, all absorbed; F-PC-R2 and F-PC-R3 were qualifying passes
(zero CRITICAL and zero HIGH), advancing the consecutive qualifying-PASS count to TWO,
with the rotation closed by a member new to the second pass. Convergence is therefore MET
under Audit Framework v3.0, Standing Rule 7. Convergence here certifies structural honesty -that every figure reproduces from primary sources, that the disclosures (the two bases, the
coverage gap, the intermediary screen) are accurate, and that the refusal boundary holds -- and

2
does NOT certify that the savings estimate is verified recoverable or policy-ready; that remains a
conditional, pilot-gated planning range per Section 5.0. Two honest caveats: the two consecutive
passes rest on materially-identical substance (the audited versions differ only in wording and
tooling, no figure moved); and convergence is met inside this producer-defined governance
framework, while the externally-verifiable core -- every figure reproducing from the public
Comptroller and data.ny.gov sources -- holds independently of the framework.

3

Abstract
New York City registers roughly $42.4 billion in new contracts annually, of which about
$21.6 billion (50.9%) is awarded through Limited-or-Non-Competitive methods rather than open
bidding (FY25 Annual Summary Contracts Report). This paper narrows that headline figure to
an "addressable" base of roughly $5.66 to $6.98 billion per year -- the Sole Source, Negotiated
Acquisition, and (optionally) Emergency subgroups -- after excluding categories that are either
already competitively bid in substance (Innovative Procurement / Design-Build) or structurally
non-competitive by design (Government-to-Government, Intergovernmental). We cross-check
vendor concentration in the two largest addressable subgroups against an independently
reproduced concentration analysis of Metropolitan Transportation Authority (MTA)
procurement, using identical Gini-coefficient and top-N methodology. The comparison shows
NYC's Sole Source subgroup is more concentrated than MTA's entire procurement book (Gini
0.956 vs. 0.931) -- but the concentration is driven overwhelmingly by a single quasigovernmental vehicle (NYCEDC, 82.5% of the subgroup), not by private-market vendor capture.
Applying literature-grounded competitive-savings rates (10 to 20%) to the addressable base
yields a conditional planning range with a headline near $500 million to $1.4 billion per year,
and a sensitivity floor near $434 million once the largest quasi-governmental vehicle (NYCEDC)
is excluded. This range is not a verified recoverable amount: it is gated on a pilot (Section 7) that
tests whether the underlying spend has viable alternative vendors, the assumption the whole
estimate rests on. We propose four concrete policy interventions and a bounded 12 to 18 month
pilot program to test the model's central assumption -- that a meaningful share of Sole Source
spend has viable alternative vendors -- before any citywide claim is made.

4

1. Introduction
New York City's contracting apparatus has two structural tracks: Group 1 (Competitive
Method Contracts, awarded via sealed bid or RFP) and Group 2 (Limited or Non-Competitive
Method Contracts, awarded via one of twelve statutory exceptions to competitive bidding under
Procurement Policy Board rules) (Comptroller's Contract Primer). Group 2 is not inherently
improper -- it exists because some goods and services genuinely cannot be competitively bid
(true single-source technology, legally mandated vendors, emergencies). But at 50.9% of
citywide contract value in FY25, it is also the segment where competitive-pricing pressure is
weakest, and therefore the segment where cost recovery is most plausible if even a fraction of it
could be moved toward genuine competition.
This paper is the fourth research leg in the Bayyinah civic-integrity research program,
alongside the at-Ta'līm Fair Student Funding fidelity verifier (education equity, not cost savings)
and the AllocationAsymmetry paper (MTA procurement/expenditure divergence and vendor
concentration, DOI 10.5281/zenodo.21445552). Where those papers focused on formula fidelity
and data-provenance integrity respectively, this paper asks a narrower and more operational
question: how much of NYC's non-competitive contracting is realistically recoverable, and what
would a city agency need to do to test that recovery in practice.

2. Background: NYC's Two-Group Procurement System
Table 1 shows the FY25 disaggregation of Group 2 into its twelve statutory subgroups,
all figures from Table 7 of the FY25 Annual Summary Contracts Report.
Table 1. FY25 Limited/Non-Competitive Contracts by Subgroup

5
% of
Subgroup

Contracts

Value

Group 2 Value

Innovative

19

$10,976,9

50.85%

Procurement
Negotiate

12,119
962

d Acquisition
Sole

$4,058,85

18.80%

1,691
126

Source

$1,599,15

7.41%

0,768
Emergenc

106

y Procurement
Governme

6.14%

7,939
31

nt-to-Government
Determine

$1,326,03

$891,413,

4.13%

172
138

d by Government

$871,314,

4.04%

665

Mandate
Discretion

1,561

ary (Line Item)
Intergover

Purchase -M/WBE

3.41%

414
280

nmental
Small

$735,384,

$623,037,

2.89%

419
1,144

$376,298,
765

1.74%

6
% of
Subgroup
Small

Contracts

Value

Group 2 Value

3,841

$111,618,

0.52%

Purchase --

847

General
Micropurc

1,572

hase

$15,172,4

0.07%

08
Demonstr

4

ation Project
Total
Group 2

$2,931,25

0.01%

3
9,784

$21,588,1

100.00%

23,459

For comparison, the FY23 subgroup breakdown (FY23 Annual Summary Contracts
Report, Table 7) shows Sole Source at $3,672,247,394 (24.72% of that year's Group 2) and
Innovative Procurement at $3,480,627,013 (23.43%) -- meaning Innovative Procurement's share
roughly doubled and Sole Source's dollar value fell by more than half between FY23 and FY25,
largely a function of which mega-projects (jails vs. other capital work) happened to register in
each fiscal year rather than a change in underlying policy. The full FY23 breakdown spans
thirteen subgroups (the twelve above plus a discontinued "Buy-Against Procurement Contracts"
category, $9,550,554 / 3 contracts, that does not recur in FY25) and is itemized in the companion
dataset.
A separate, unresolved question concerns the Department of Education specifically.
DOE's own Table 96 shows Limited/Non-Competitive contracts falling from a FY2016 baseline

7
of 64% of contract value ($2.7B of $4.29B, ME17_078F) to 29.89% of value in the FY23 to
FY25 cumulative table, while the contract-count share stayed high (83.95%). We believe this
decline in dollar share is substantially a reporting artifact -- large multi-year mega-contracts (e.g.,
NYCSSS custodial services, $2.56B over 4 years or $6.36B over 8 years, NYS OSC audit 2020N-8) register once and then drop out of subsequent years' "new registration" tables -- rather than
genuine improvement. This is corroborated by a live, ongoing dispute: the City Council is
currently auditing approximately $12.9 billion per year in DOE external contracting, of which
DOE has self-classified 352 of 579 requested contracts as "not competitively bid," and DOE has
missed the Council's document deadline, prompting Speaker Menin to cite a "pattern of opacity,
slow-walking, and delay" and threaten a subpoena (NY Post, July 14, 2026). We exclude DOE
from the quantitative addressable-base calculation below because its true non-competitive
footprint cannot currently be reconciled with confidence -- but flag it as the single largest source
of upside uncertainty in either direction.
A related structural blind spot, unconnected to any single agency, is the Comptroller's
own May 2026 finding on "Monty Hall Contracts" -- $625 million in Accelerated Procurement
spend under master agreements since FY22 that has received zero Comptroller review
(Comptroller report, May 2026). This is a distinct category from the ones analyzed below and is
not included in our addressable-base figure, but it is directly relevant to Recommendation 2
(Section 6.2).

8
3. Methodology
3.1 Data sources
•

Contract-level and vendor-level microdata: NYC Comptroller Appendix 1 -- Registered
Contracts by Group, Industry, Agency Type, and Retroactivity Category, 55,224 rows,
FY22 to FY25, with fields including Vendor Legal Name, Subgroup, Award Method,
Registered Amount, and Registering Agency.

•

Aggregate subgroup figures: FY25 Annual Summary Contracts Report and the FY23
Annual Contracts Report.

•

MTA comparison figures: independently reproduced (across nine audit rounds by
multiple model instances) statistics from the Bayyinah AllocationAsymmetry paper,
sourced from the New York State MTA Procurement Report (All) dataset.

•

Competitive-savings literature: a Czech single-bid reform study finding roughly 10%
price reduction after eliminating single-bidder awards (Utrecht working paper); a Slovak
study finding roughly a 19-percentage-point gap between multi-bidder (~19% below
estimate) and single-bidder (~1% below estimate) outcomes (JKU study); and a broader
U.S. federal 10 to 40% range from GAO and OMB reviews of competitive vs. noncompetitive sourcing (GAO-10-833; OMB paper).

3.2 Addressable-base construction and exclusion criteria
We start from the full $21.59B Group 2 total and exclude subgroups on the following
grounds:
•

Innovative Procurement ($10.98B) -- excluded. As detailed in Section 4.3, this
subgroup in FY25 is dominated by Design-Build contracts for the Borough-Based Jails

9
program, which the Comptroller's own report states were competitively bid; the Group 2
classification reflects a PPB rulebook categorization for methods not yet codified, not an
absence of competition (PPB Rule §3-12, American Legal Publishing).
•

Government-to-Government ($891M) and Intergovernmental ($623M) -- excluded.
These are, by definition, transactions between government entities where private-market
competition is not a meaningful counterfactual.

•

Determined by Government Mandate ($871M) -- excluded. Legally mandated vendor
relationships have no competitive alternative by construction.

•

Discretionary (Line Item), Small Purchase, Micropurchase, Demonstration Project
(combined ~$1.24B) -- excluded. These are low-dollar, high-volume categories where
competitive-bid overhead would likely exceed any recoverable savings.

•

Sole Source ($1.60B) and Negotiated Acquisition ($4.06B) -- included as the core
addressable base ($5.66B). These are the two subgroups where a plausible, if imperfect,
competitive counterfactual exists -- a different vendor could conceivably have bid.

•

Emergency Procurement ($1.33B) -- included only in a "wide" sensitivity case
($6.98B). Time-constrained circumstances legitimately limit competition, but emergency
status is also the subgroup most vulnerable to overuse, so we present it as a secondary,
not primary, addressable figure.

3.3 Vendor-concentration cross-check methodology
To test whether NYC's addressable subgroups show the kind of vendor concentration
associated with reduced competitive pressure, we computed vendor-level concentration for Sole
Source and Negotiated Acquisition using the identical method applied and independently
reproduced across nine rounds of adversarial audit in the AllocationAsymmetry paper: aggregate

10
contract value to one positive total per distinct vendor name, drop null/zero/negative amounts,
then compute (a) the share of subgroup value held by the top 1, 5, 10, and 20 vendors, and (b) the
Gini coefficient over the resulting vendor-total distribution. Using the same measurement
convention on both sides of the comparison is what makes the MTA/NYC comparison
meaningful rather than a comparison of arbitrary numbers.
3.4 Reproduction
Every concentration figure in Table 2, the addressable-base and savings arithmetic in
Table 3, and the MTA cross-check are reproducible from a standard-library script and the two
frozen vendor CSVs, published as a companion reproduction package. The script
(reproduce_procurement.py) verifies the SHA-256 of each CSV against a manifest,
recomputes the vendor count, top-N shares, and Gini for each subgroup on the clean vendor rows
(Rank a positive integer; the TOTAL and footnote rows excluded), checks the five Table 3
savings bases, reconciles the Negotiated and Sole Source subgroups against the Comptroller
Appendix 1 microdata, and with --live re-pulls the MTA FY2024 figures from data.ny.gov
and confirms them against the constants carried from the converged AllocationAsymmetry
paper. A --selftest mode perturbs each checked value and confirms the comparator detects
it. All checks reproduce exactly; the one known discrepancy (the Negotiated positive-basis gap
of Section 4.4) is reported by the script rather than hidden.

11
4. Findings
4.1 Citywide landscape
FY25 citywide: $42,446,174,150 across 12,955 new contracts; Group 2 accounts for
50.86% of value and 75.52% of contract count -- meaning most individual contracts, by count,
are small non-competitive purchases, while dollar value is dominated by a small number of very
large awards (megaprojects, master agreements) (FY25 report).
4.2 DOE and the live oversight dispute
See Section 2. We do not include DOE-specific figures in the quantitative model below;
the ongoing Council audit dispute over ~$12.9B/year in DOE contracting means any DOEspecific addressable-base estimate would currently be speculative.
4.3 Innovative Procurement: why it is excluded
The FY25 report states directly: "While these contracts were competitively bid, DesignBuild is still considered an Innovative Procurement method and is classified into group 2
accordingly" (FY25 report). Design-Build is a two-step, qualifications-based Best Value
selection process used for the Borough-Based Jails program. The three highest-value contracts
registered citywide in FY25 are the three BBJ facilities, awarded to three different vendor teams
-- Leon D. DeMatteis Construction Corp (Queens, $3.98B), Tutor Perini O&G Joint Venture
(Manhattan, $3.76B), and Transformative Reform Group LLC (Bronx, $2.97B) -- which is
consistent with a genuine, if limited-field, competitive process rather than single-bidder capture.
We have not independently verified how many bidders competed for each of the three BBJ
awards; this would be a natural extension of this research if the exclusion decision needs to be
defended further.

12
4.4 Vendor concentration: NYC Sole Source and Negotiated Acquisition vs. MTA
Table 2 presents the cross-check.
Table 2. Vendor Concentration Comparison
MTA,
FY2024 (13,718
Metric
Universe

records; data.ny.gov)
$65.19B face

NYC
NYC Sole
Source, FY25

Negotiated
Acquisition, FY25

$1.60B, 115

$3.87B, 935

value (FY2024),

contracts (positive-

contracts (positive-

13,718 records

amount basis), 106

amount basis), 462

(FY2024), 2,656

vendors

vendors

distinct vendors
(FY2024)
Top-1 vendor

--

82.50%

24.03%

Top-5 vendor

22.14%

90.59%

36.92%

Top-10

30.42%

94.06%

46.22%

0.931 (face) /

0.956

0.819

share

share

vendor share
Vendor Gini
coefficient

0.904 (annual
expenditure)

13
Note: our computed positive-amount totals are below the official Table 7 subgroup totals.
Sole Source: 106 vendors / $1,597,506,645 against the official $1,599,150,768 (a 0.10% gap).
Negotiated Acquisition: 462 vendors / $3,865,895,210 against the official $4,058,851,691, a
4.75% gap of about $192.96 million across 27 contracts. This gap has been reconciled directly
against the Comptroller's Appendix 1 parent-contracts microdata (publicly reachable, though the
host intermittently returns HTTP 403 to automated requests). The FY2025 Appendix 1 extract
contains exactly 935 Negotiated rows and 115 Sole Source rows, every one carrying a positive
amount and a named vendor (zero blank or null vendor names), summing to the positive-basis
totals above. Nothing was dropped in the vendor aggregation. The gap is instead between Table
7's aggregate contract counts (962 Negotiated, 126 Sole Source) and the parent-contracts extract
(935 and 115): 27 Negotiated contracts ($192.96M) and 11 Sole Source contracts ($1.64M) are
counted in the summary table but absent from the extract -- a coverage or scope difference
between the Comptroller's summary and its parent-contracts export, not an attribution loss inside
the file. The Negotiated concentration figures should therefore be read as computed on about
95.25% of the official subgroup base; whether the 27 missing contracts would raise or lower the
Gini depends on their own concentration, which the extract does not contain. (An earlier draft
guessed the mechanism was unattributable vendor names and reported the file as access-blocked;
opening the file corrected both.)
Sole Source's top vendor is the New York City Economic Development Corporation, at
$1,317,949,728, which is 82.5% of the entire subgroup -- followed by the Wildlife Conservation
Society ($49.0M), SoundThinking Inc ($43.1M), Curriculum Associates LLC ($19.1M), and
Medical Debt Resolution Inc ($18.0M). By contract count, Sole Source awards are spread across
DOE (22), DEP (14), DOHMH (11), DSS/HRA (7), and NYPD (6).

14
Negotiated Acquisition's top vendor is HANYC Foundation Inc, a nonprofit hotelmanagement intermediary for DHS emergency shelter programs, at $929,104,960 (24.0%),
followed by Samaritan Daytop Village Inc ($157.8M), The Children's Rescue Fund ($138.2M),
Concordance Healthcare Solutions LLC ($106.1M), and Genuine Parts Company ($96.0M). By
contract count, DYCD registers by far the most Negotiated Acquisition contracts (575 of 935),
overwhelmingly tied to the COMPASS NYC after-school program -- but these 575 contracts are
spread across many distinct nonprofit providers, so DYCD's high count does not translate into
high vendor concentration.
4.5 Structural interpretation
Sole Source is nominally more concentrated than MTA's entire procurement book (Gini
0.956 vs. 0.931), and Negotiated Acquisition is less concentrated (Gini 0.819 vs. 0.931). But the
mechanisms differ. MTA's concentration is spread across 2,656 distinct vendors in a genuine
commercial market -- construction, engineering, rolling-stock, and related services -- where a
handful of large firms nonetheless win a disproportionate share, the pattern the
AllocationAsymmetry paper's own audit trail explicitly classified as "a non-culpable structural
explanation" rather than evidence of misconduct. NYC's Sole Source and Negotiated Acquisition
concentration, by contrast, is driven by one or two single-purpose intermediary vehicles per
subgroup -- NYCEDC (a City-created nonprofit instrumentality) and HANYC Foundation (a
nonprofit hotel-shelter management intermediary) -- that function structurally more like the
already-excluded Government-to-Government category than like private-market vendor capture.
This has a direct bearing on the savings model: concentration in a genuine commercial
market (MTA-style) is exactly the kind of pattern where more competitive pressure could
plausibly

recover

money.

Concentration

in

a

designated

single-vehicle

model

15
(NYCEDC/HANYC-style) is much less likely to be recoverable through more competition,
because the City deliberately chose a single delivery vehicle for institutional reasons (control,
accountability, speed) that a competitive rebid would not necessarily change.

5. Savings Estimate Synthesis
5.0 On producing a savings figure at all
This program's other civic papers deliberately refused to attach a dollar-savings number
to their findings, and that refusal was principled, not timid. The Fair Student Funding work (atTa'līm) concerned a fixed redistributive pool, where a divergence moves money between schools
rather than reducing a bill, so "savings" was the wrong frame entirely. The MTA concentration
work (AllocationAsymmetry) measured a descriptive count-versus-dollar asymmetry and
classified vendor concentration explicitly as a non-culpable structural pattern, not recoverable
waste; producing a savings figure there would have manufactured a number the data did not
support. The standing discipline across the program has been that a verification method is not a
savings instrument, and that fabricating a recoverable-dollars figure contradicts the papers' own
measure-do-not-accuse posture.
Non-competitive procurement is genuinely different in one specific way, and that
difference is the only thing that licenses a savings estimate here: unlike a redistributive formula
or a descriptive concentration curve, a non-competitively awarded contract has a real competitive
counterfactual. A different vendor could, in principle, have bid. That is what makes "how much
might competition recover" a coherent question rather than a category error. But the estimate that
follows is conditional in a way the reader must keep in view: it multiplies an addressable base by

16
price-reduction rates drawn from other jurisdictions' procurement systems, and its load-bearing
assumption -- that a meaningful share of this spend actually has viable alternative vendors -- is
precisely the thing this paper has not verified and proposes a pilot to test. The numbers below are
therefore a planning range under stated assumptions, not a measurement of money the City is
losing or a promise of money it will save. No figure here should be cited as recoverable until the
pilot in Section 7 tests the alternative-vendor assumption on real contracts. Presented that way,
the estimate stays inside the program's discipline: it is an explicitly-conditional projection with
its assumptions on the surface, not a verified claim.
A note on which base each figure uses. Two dollar bases appear in this paper and are
not interchangeable. The concentration analysis (Section 4.4) uses the positive-amount vendor
basis the Gini method requires ($1.598B Sole Source, $3.866B Negotiated, $5.463B combined).
The savings model uses the official Table 7 subgroup totals ($1.599B, $4.059B, $5.658B
combined), the authoritative figures, which exceed the positive basis by about $194.6M (chiefly
the $192.96M Negotiated coverage gap of Section 4.4, plus a $1.64M Sole Source gap). Because
the NYCEDC-adjusted row is built on the official Core, it carries that full $194.6M: the officialbasis adjusted figure ($4,340,052,731) is $194.6M above the fully positive-basis adjusted figure
($4,145,452,127), and its 10% and 20% floors ($434.0M / $868.0M) are $19.5M and $38.9M
above the positive-basis floors ($414.5M / $829.1M). Table 3 reports the adjusted row on both
bases so the basis effect is explicit rather than buried. This corrects an earlier draft that described
the adjusted row's basis exposure as about $2M; that figure was the Sole Source gap alone and
wrongly omitted the Negotiated gap the row carries.
Table 3. Addressable Base and Estimated Conditional Savings (all conditional and
pilot-gated; see Section 5.0)

17
Base

Value

10% savings

20% savings

Core,

$5,658,002,459

$565,800,246

$1,131,600,492

$6,984,040,398

$698,404,040

$1,396,808,080

$4,340,052,731

$434,005,273

$868,010,546

$4,145,452,127

$414,545,213

$829,090,425

$3,410,947,771

$341,094,777

$682,189,554

official basis
(Sole Source +
Negotiated
Acquisition),
upper bound
Wide,
official basis
(Core +
Emergency
Procurement),
upper bound
Core,
adjusted, official
basis (excluding
NYCEDC)
Core,
adjusted,
positive basis
(excluding
NYCEDC)
Intermedi

18
Base

Value

10% savings

20% savings

ary-screened
(Core minus
NYCEDC and
HANYC)
The Core and Wide rows apply the literature rate to the entire subgroup base and are
upper bounds: as Section 4.5 shows, large shares of that base are designated single-vehicle
intermediary spend (NYCEDC, HANYC) with little competitive counterfactual, so a screened
estimate is the more defensible figure. The intermediary-screened row removes both named
vehicles; a complete screen of every quasi-governmental or designated-intermediary vendor
would lower it further. The adjusted row is shown on both bases per Section 5.0.
The headline range is approximately $500 million to $1.4 billion per year, down from
an earlier and cruder $1 to 3 billion/year estimate that extrapolated DOE's FY2016 noncompetitive share citywide. The adjusted-core row reflects the concentration cross-check in
Section 4.5: if NYCEDC's contract is treated as structurally non-recoverable (like Governmentto-Government spend), the plausible floor of the range falls to roughly $434 million/year. We
have not performed the equivalent adjustment for Negotiated Acquisition's HANYC-type megacontracts, DYCD's fragmented COMPASS spend, or any other subgroup-specific single-vehicle
exclusions; a complete pass would screen every Sole Source and Negotiated Acquisition vendor
for quasi-governmental or designated-intermediary status before finalizing a number. We present
the adjusted-core and intermediary-screened figures as sensitivity bounds, not revised headlines;
the screened figure (Core minus NYCEDC and HANYC, about $3.41B, or $341M to $682M at
the literature rates) is the most conservative and, given Section 4.5, arguably the most defensible.

19

6. Actionable Proposal
6.1 Recommendation 1 -- Concentration-triggered independent re-review
Require that any Sole Source or Negotiated Acquisition award where a single vendor
holds more than 50% of that agency-subgroup's annual value, or where the subgroup's vendor
Gini coefficient exceeds 0.90, triggers a mandatory sources-sought market check (a public
request for information testing whether alternative vendors exist) before the contract's next
renewal. This targets exactly the pattern identified in Section 4.4 without requiring a full re-bid
of every non-competitive contract.
6.2 Recommendation 2 -- Extend vendor-level transparency to all Group 2 subgroups in
near-real time
The Comptroller already publishes the vendor-level Appendix 1 file used throughout this
paper, but only as part of the annual report cycle. Publishing the same fields (Vendor Legal
Name, Subgroup, Award Method, Registered Amount) on a rolling quarterly basis -- and
explicitly including Accelerated Procurement / master-agreement task orders currently outside
standard review, addressing the $625M "Monty Hall Contracts" gap (Comptroller report, May
2026) -- would let concentration be monitored continuously rather than discovered a year after
the fact.
6.3 Recommendation 3 -- Separate quasi-governmental instrumentality reporting
Create a reporting flag distinguishing awards to City-created or City-affiliated nonprofit
instrumentalities (NYCEDC, HANYC-type intermediaries) from awards to independent private
vendors within the Sole Source and Negotiated Acquisition subgroups. This would let the

20
Council, the Comptroller, and outside researchers separate "genuinely non-competitive private
awards" from "designated single-vehicle government delivery," which the current Table 7
categories conflate -- a distinction this paper had to reconstruct manually from vendor names.
6.4 Recommendation 4 -- Algorithmic integrity scanning of procurement registrations
Bayyinah's core technical competency is automated integrity analysis of structured
records. The same Gini/top-N methodology used in Section 4.4 (and previously validated across
nine independent audit rounds on MTA data) can be run as a standing, automated scan against
the Comptroller's published Appendix 1 data each quarter, flagging any agency-subgroup pair
crossing the Recommendation 1 thresholds without requiring new legislation or new data
infrastructure -- only a scheduled script against data the City already publishes.

7. Pilot Program Design
We propose a bounded, low-risk pilot to test the model's central and least-verified
assumption -- that a meaningful share of Sole Source spend has a viable alternative vendor -before generalizing any savings claim citywide.
Scope. All Sole Source contracts registered by DOE, DEP, DOHMH, DSS/HRA, and
NYPD (the five agencies with the most Sole Source contracts by count in FY25, per Section 4.4)
above a $1 million threshold, excluding any vendor independently flagged as a City-created or
City-affiliated instrumentality under Recommendation 3. This excludes NYCEDC by
construction and targets the roughly $280 million "genuinely private-market" residual of the Sole
Source subgroup identified in Section 5.

21
Mechanism. For each qualifying contract approaching renewal, issue a public sourcessought notice (not a full RFP) asking whether alternative vendors could meet the same
specification. This is a lightweight, non-binding market test -- it does not require re-bidding the
contract, only determining whether re-bidding would be worth the administrative cost.
Duration. 12 to 18 months, aligned to a single fiscal year's renewal cycle, so results can
be compared against the following year's Table 7 figures.
Metrics. - Percentage of tested contracts where at least one credible alternative vendor
responds. - For contracts subsequently rebid, the percentage price change versus the prior Sole
Source registered amount. - Administrative cost of running the sources-sought process, to
establish a true net-savings figure (not just gross).
Success criteria. The pilot should be considered informative (regardless of whether it
confirms or disconfirms the savings model) if it produces a credible-alternative-vendor rate and a
rebid price delta for at least 20 contracts. It should be considered supportive of this paper's thesis
if the observed price delta on rebid contracts falls within or above the 10 to 20% literaturegrounded range from Section 3.1.
Governance and independence safeguard. Consistent with the Bayyinah audit protocol
applied to this program's other papers, the pilot's results should be evaluated by a party
independent of whichever agency ran the sources-sought process, and the underlying data
(contract IDs, vendor responses, price deltas) should be published rather than summarized only
in a top-line report -- mirroring the vendor-level transparency this paper argues for in
Recommendation 2.

22
8. Limitations
•

This paper began as a single-session, single-instance synthesis; its empirical spine has
since been independently reproduced and audited across three cross-instance rounds and
converged under Standing Rule 7 (see the audit-status notice). Convergence certifies
structural honesty and reproducibility, not that the savings estimate is verified
recoverable or policy-ready -- that remains conditional on the Section 7 pilot.

•

The Innovative Procurement exclusion (Section 4.3) relies on the Comptroller's own
characterization of Design-Build as competitively bid; we did not independently verify
bidder counts for the three Borough-Based Jail awards.

•

The vendor-concentration cross-check (Section 4.4) compares one fiscal year of NYC
data (FY25) against one fiscal year of MTA data (FY2024) from a different level of
government (city vs. state authority) with different procurement rules; the comparison is
illustrative of methodology, not a claim that the two systems are equivalent.

•

The DOE-specific non-competitive footprint remains genuinely unresolved pending the
outcome of the ongoing City Council audit; this paper deliberately excludes DOE from
its quantitative model rather than resolving that dispute.

•

The savings literature (Czech, Slovak, GAO/OMB) is drawn from different jurisdictions
and procurement systems than New York City's; the 10 to 20% range is a reasonable
planning assumption, not a NYC-specific estimate.

•

We have not adjusted Negotiated Acquisition for its own designated-intermediary
contracts (e.g., HANYC) the way we did for Sole Source/NYCEDC; the adjusted-core
figure in Table 3 is therefore likely still an overestimate of the truly recoverable amount.

23
9. Conclusion
Narrowing from a citywide $21.6 billion non-competitive headline to a defensible $5.66
to $6.98 billion addressable base, and then cross-checking vendor concentration within that base
against an independently reproduced MTA benchmark, produces a materially smaller and more
defensible planning range than earlier passes in this research program: roughly $500 million to
$1.4 billion per year under the stated literature-grounded assumptions, with a plausible
NYCEDC-excluded floor near $434 million, and an intermediary-screened sensitivity of about
$341 million to $682 million once NYCEDC and HANYC are both excluded. That range is
conditional on the alternative-vendor assumption the Section 7 pilot is designed to test, and
should not be cited as recoverable before it does. Even so, its magnitude relative to the City's
own procurement-reform activity to date and the four recommendations above are designed to be
implementable with data the City already collects, at a bounded pilot scale, before any larger
claim is made or acted upon.

References
•

FY25 Annual Summary Contracts Report for the City of New York

•

FY25 Annual Summary Contracts Report -- landing page

•

Appendix 1 -- Registered Contracts by Group, Industry, Agency Type, and Retroactivity
Category (FY25, .xlsx)

•

FY23 Annual Summary Contracts Report for the City of New York

•

Comptroller's Contract Primer

•

PPB Rule §3-12, American Legal Publishing

•

MOCS Citywide Indicator Reports

24
•

DOE FY2016 procurement report (ME17_078F)

•

NYS Comptroller audit 2020-N-8 (NYCSSS custodial contracts)

•

NY Post, "Mayor Zohran Mamdani stonewalls audit of nearly $13B in no-bid NYC DOE
contracts," July 14, 2026

•

Comptroller report on "Monty Hall Contracts," May 2026

•

MTA Procurement Report (All), data.ny.gov

•

Bayyinah AllocationAsymmetry paper, DOI 10.5281/zenodo.21445552

•

Bayyinah AllocationAsymmetry ledger and dataset, DOI 10.5281/zenodo.21445556

•

Utrecht working paper on Czech single-bid procurement reform

•

JKU study on Slovak multi-bidder vs. single-bidder procurement outcomes

•

GAO-10-833, competitive sourcing

•

OMB paper on competitive sourcing

•

Companion dataset: NYC Procurement Concentration & Savings -- Source Dataset
(XLSX workbook). Contains full vendor-level detail for all 106 FY25 Sole Source
vendors and all 462 FY25 Negotiated Acquisition vendors, the complete FY23 (13subgroup) and FY25 (12-subgroup) Table 7 breakdowns, the MTA cross-check
comparison table, the live Savings Model formulas, and this reference list. Delivered as a
companion workbook artifact alongside this paper; vendor lists are also available as
standalone

CSV

exports

(sole_source_vendors_fy25.csv,

negotiated_acquisition_vendors_fy25.csv). A standard-library reproduction package
(reproduce_procurement.py plus the two hashed CSVs and a manifest) reproduces every
concentration figure, the savings arithmetic, and the live MTA cross-check, and self-tests
its own comparator.



Bismillah ir-Rahman ir-Rahim
