Bismillah ir-Rahman ir-Rahim

1

Bayyinah: Public-Ledger Allocation and Asymmetric-Measure
Audits
A Descriptive Count-versus-Dollar Asymmetry in Public-Authority Procurement, with a
Reproducible Worked Example on New York MTA Data
Bilal Syed Arfeen (BayyinahEnterprise), with collaborative analytical assistance from
Claude (Anthropic).
DOI:

10.5281/zenodo.21445552.

Audit

and

provenance

ledger:

DOI

10.5281/zenodo.21445556. Version 1.0, the canonical converged release: the two-consecutivequalifying-pass convergence gate under Audit Framework v3.0 Standing Rule 7 was met on the
identical v0.7 substance (F-AA-R8 and F-AA-R9, three qualifying non-producer members,
executed reproduction, zero critical and zero high in both rounds). The full round history and the
honestly-recorded convergence caveats are in the ledger Current State.
Governed by: Bayyinah, Portable Structural Honesty Verification for Public-Service
Institutions (Arfeen 2026, the framework paper). Companion to: Bayyinah at-Taʿlīm (Arfeen
2026,

DOI

10.5281/zenodo.21436484);

Al-Mutaffifīn

(Arfeen

2026,

10.5281/zenodo.19894724).
"And establish weight in justice and do not make the mizan deficient." (Ar-Rahman
55:9)

DOI

2
Abstract
This method application note applies Structural Honesty Verification to public-authority
procurement. Its worked example is a descriptive, reproducible measurement, deliberately
narrowed after a first independent audit round that found the v0.1 draft attaching interpretive
claims its data could not support. The example measures, for the Metropolitan Transportation
Authority's FY2024 procurement report, the divergence between a participation metric counted
by contract and the same metric weighted by dollars, on two clearly named dollar estimands.
Businesses recorded as Minority- and Women-Owned Business Enterprises (MWBE) as the
prime vendor hold 18.7 percent of FY2024 contract records but 3.95 percent of total reported
contract face value and 7.06 percent of that year's reported annual expenditure; contract face
value is highly concentrated (top-ten vendors 30.4 percent; Gini 0.931). A count-versus-dollar
asymmetry is present on both dollar measures and persists across three report vintages, though its
magnitude differs by measure (a factor of 4.7 on face value, 2.7 on annual expenditure) and the
annual-expenditure gap is narrowing. Crucially, the note reports these as descriptive primevendor statistics; it does not claim they measure attainment of any MWBE goal, does not treat
contract face value as annual spending, and does not conclude that competitive-process
composition demonstrates rule compliance. Those were overreaches in v0.1 and are removed.
The example remains a single-authority demonstration of a portable method, not a finding about
the authority.

3
1. Purpose and Scope
This paper instantiates the framework's allocation-and-asymmetry method on live public
procurement data. The framework (Arfeen 2026) establishes the method core, the two admission
filters, the tier discipline, and the per-jurisdiction adapter pattern; this paper supplies a fully
reproducible worked example.
The method verifies whether an institution's operative behavior, reconstructed from
public data, matches a declared rule, and reports structural divergences and asymmetries. This
version is deliberately conservative about what the available data can establish. It reports
descriptive composition and count-versus-dollar asymmetry. It does not determine whether a
declared rule is wise, whether any divergence is intentional, whether a participation goal was
met, or whether procurement complied with an authority's guidelines. The first three are Tier 3
adjudications; the fourth requires operative-guideline and transaction-documentation data this
dataset does not contain. All four are refused in Section 4.4.
2. The Method: Descriptive Count-versus-Dollar Asymmetry
The governing object of this note is the asymmetric-measure signature, imported from
Al-Mutaffifīn (Arfeen 2026): a metric that reads one way when counted and another when
weighted by the dollars it governs. In procurement, the canonical form is a participation rate that
is one value as a fraction of contract count and a smaller value as a fraction of contract dollars,
because the counted category is concentrated in many small awards while dollar volume pools in
a few large ones.
Two disciplines, both tightened across the audit rounds, govern how this signature is
reported. First, the dollar denominator must be a named estimand. "Contract dollars" is

4
ambiguous between the total face value of a contract (a stock, often spanning many years) and
the amount expended in a given fiscal year (an annual flow); the two differ by nearly an order of
magnitude here, and a count-versus-dollar ratio is meaningless until the denominator is fixed.
Second, the signature is descriptive. Observing that a category holds a larger share of count than
of dollars is a structural fact; concluding that this represents a failure to meet a goal, or a
deficient measure in the normative sense the mizan verse evokes, requires the goal's own
definition, denominator, and eligibility rules, which are exogenous to this dataset. The method
reports the asymmetry and stops there.
Every quantity here is Tier 1 (a contract amount is a number on a public ledger) or Tier 2
(a count-versus-dollar share depends on the disclosed choice of estimand, fiscal year, and
category flag). Nothing is Tier 3.
3. The Data-Interface Contract and the New York Adapter
The method's data-interface contract for procurement is: a public, record-level
procurement ledger exposing, per contract, one or more award-amount fields with defined
semantics, an award-process category, an award date, and any declared-category flags, at a
disclosed fiscal-year boundary.
The reference adapter maps a New York public-authority procurement report onto this
contract. New York public authorities report procurement annually; under Public Authorities
Law they submit through the Authorities Budget Office's PARIS system using standardized
reporting structures, and the ABO in collaboration with the state Open Data program publishes
compiled datasets. The result is a common schema across authorities, which is what makes a
single adapter reusable; the statute mandates the annual reporting, while PARIS and the

5
ABO/Open Data publication pipeline supply the common electronic schema and portal
availability.
Provenance, stated precisely (corrected in v0.2). The dataset queried here, Socrata
resource gpsc-qqsz on data.ny.gov, is a community-created view derived from the
statewide authority-procurement dataset; the portal notes that the state did not review or approve
view modifications. A first-party, MTA-attributed dataset, twsw-2mqa, is separately published.
The two are close but not identical: for the fiscal year ending December 31, 2024, gpsc-qqsz
returns 13,718 records summing to $65.19 billion in contract face value, while twsw-2mqa
returns 13,648 records summing to $65.13 billion. The face-value divergence is about 0.089
percent (under 0.1 percent), but the record counts differ by about 0.5 percent (70 records);
neither affects the qualitative findings, but both must be disclosed separately rather than under a
single sub-0.1-percent label. A production audit should rebase on the first-party or ABO
statewide dataset and reconcile the community view; this draft retains gpsc-qqsz for continuity
with the archived snapshot and describes it accurately as a derived view. The frozen three-year
extract used here (fiscal years ending 2022, 2023, and 2024) contains 37,988 records (12,156,
12,114, and 13,718 respectively); the full gpsc-qqsz resource across all reported periods
contains about 111,879 records, a figure that in v0.1 was incorrectly attributed to the three-year
window.
The adapter also records what the ledger does not directly support: a by-geography
allocation analysis. The MTA capital budget datasets (kizb-nxtu, ehz8-ag3n) are queryable
tabular resources carrying allocation dollars per project, but they lack a borough key; project
location is published only as coordinates in a separate table ( wcsa-vkhf), so borough attribution

6
requires a project-number join followed by a coordinate-to-boundary spatial join, a GIS step
deferred to a dedicated geographic instance.
4. Worked Example: MTA FY2024 Procurement Report
4.0 Naming the estimand, and a stock-versus-flow disclosure
The FY2024 report (fiscal year ending December 31, 2024) contains 13,718 records. It
carries two distinct dollar fields with different meanings. contract_amount is the total face
value of a contract, which for a multi-year contract spans many fiscal years; summed over the
report it is $65.19 billion. amount_expended_for_fiscal_year is the amount actually spent
under those contracts during FY2024; summed it is $8.17 billion. These are not interchangeable,
and neither is "FY2024 spending" without qualification.
A stock-versus-flow disclosure is essential and was absent in v0.1. Award dates in the
FY2024 report range from 1984 to 2025, and 91.7 percent of the summed contract face value
belongs to contracts awarded before 2024; only 8.3 percent was awarded in 2024. The $65.19
billion is therefore the face-value stock of all contracts appearing in the FY2024 report, not a
flow of FY2024 awards or spending. Relatedly, because multi-year contracts recur across annual
reports, the same contract appears in more than one vintage. This must be measured with a
stable-field fingerprint, not an exact all-field one: an exact match on every field finds zero shared
records across vintages, because the fiscal-year field and the annual-state fields (expenditure-forfiscal-year, expenditure-to-date, and outstanding balance) differ by construction between
vintages. Matching instead on all fields except the fiscal-year field and the three annual-state
fields (expenditure-for-fiscal-year, expenditure-to-date, and outstanding balance) -- the
remaining fields being stable contract-identity attributes such as vendor, procurement

7
description, award process, award and term dates, and contract face value -- finds 2,115, 604,
and 1,002 shared records between the FY2022/FY2023, FY2022/FY2024, and FY2023/FY2024
vintages respectively. (Matching on only the five-or-so enumerated identity fields rather than the
full non-excluded set yields larger counts and is not the method used here; the reported figures
come from excluding exactly the four fiscal-year and annual-state fields.) The three annual
snapshots are therefore not independent samples and must never be summed. Where this note
reports figures "across three report vintages," it means exactly that -- repeated observations of an
overlapping contract portfolio -- not three independent annual flows.
Of the 13,718 records, 1,348 carry a missing contract_amount and 48 carry an
explicit zero (1,396 total, 10.2 percent); these are analytically distinct and are separated here.
Notably, the two award-process categories with no contract_amount (state-contract and noncontract purchase orders) do carry annual expenditure, so they vanish from face-value figures but
not from expenditure figures.
4.1 Process composition (descriptive; no compliance claim)
By contract face value, "Authority Contract - Competitive Bid" is $60.12 billion, 92.2
percent, across 10,876 records (79.3 percent by count); "Non-Competitive Bid" is $5.07 billion,
7.8 percent. By annual expenditure, the four categories are competitive 89.65 percent, noncompetitive 4.73 percent, purchased-under-state-contract 3.24 percent, and non-contract
purchase order 2.38 percent.
This is reported as descriptive composition only. v0.1 declared this a "pass" of a
competitive-bidding rule, asserting that substrate matched surface; that claim is withdrawn. A
high competitive share does not demonstrate compliance with the authority's operative

8
procurement rule: testing that would require the MTA's own procurement guidelines, the
permitted exception categories, the waiver and documentation requirements under Public
Authorities Law Section 2879, and a transaction-level or defensibly-sampled check that each
non-competitive award fits a documented exception, together with validation of the authority's
own process coding. None of that is in this dataset, so the method reports the composition and
withholds any rule-compliance conclusion.
4.2 MWBE prime-vendor count-versus-dollar asymmetry (descriptive)
Businesses flagged as MWBE prime vendors hold 2,570 of 13,718 FY2024 records, 18.7
percent by count. The same flag holds 3.95 percent of contract face value and 7.06 percent of
FY2024 annual expenditure. The participation metric measured by count is thus about 4.7 times
its face-value share and about 2.7 times its annual-expenditure share. Across the three report
vintages, the count share is 16.4, 18.6, 18.7 percent; the face-value share is 3.27, 3.51, 3.95
percent (ratio 5.0, 5.3, 4.7); and the annual-expenditure share is 4.25, 6.27, 7.06 percent (ratio
3.9, 3.0, 2.7). A count-versus-dollar asymmetry is present on both dollar measures, but its
magnitude depends on the measure and the annual-expenditure gap is narrowing, not stable.
This is a descriptive prime-vendor statistic, and v0.2 removes the goal-attainment
framing v0.1 attached to it. The vendor_is_a_mwbe flag identifies whether the recorded prime
vendor is an MWBE; it does not capture indirect participation through subcontractors or joint
ventures, the eligible-spend denominator against which a utilization goal is assessed, contractspecific goals tied to available subcontracting opportunities and disparity-study categories, or
waivers and exemptions. New York MWBE utilization goals are defined over those constructs
(Executive Law Article 15-A), not over a binary prime-vendor flag on total contract face value.
Consequently this note does not claim the 3.95 or 7.06 percent figure measures attainment of any

9
goal, does not call the dollar share the "operative substrate" or the count share the "short
measure," and does not infer goal compliance or its absence. What it reports is narrower and still
real: as a prime vendor, the MWBE-flagged share of records is several times its share of either
dollar measure, persistently across vintages.
4.3 Vendor concentration (face-value stock)
Contract face value is highly concentrated: in FY2024 the top five vendors hold 22.1
percent, the top ten 30.4 percent, and the top twenty 41.8 percent, with a Gini of 0.931 across
2,656 distinct vendor strings and no negative amounts. The largest holdings are rolling-stock and
heavy-construction contracts (a rail-car manufacturer at $6.46 billion, a bus manufacturer at
$2.56 billion, and construction joint ventures above $1.5 billion). Annual-expenditure value is
also concentrated, though less extremely: top five 16.9 percent, top ten 26.2 percent, top twenty
37.6 percent, Gini 0.904. Both measures are reproduced in the accompanying script.
The concentration on both dollar measures (face-value Gini 0.931; annual-expenditure
Gini 0.904) supplies a structural explanation for the count-versus-dollar asymmetry on both:
when a large share of dollars is committed to a handful of very large capital contracts not held by
MWBE prime vendors, the dollar-weighted MWBE share is mechanically pulled below the
count share regardless of how many small contracts MWBE vendors hold. Stating this
mechanism is within the method's authority because it is a structural fact about where dollars
concentrate. Concluding from it that the authority steers dollars away from any group, or that it
does not, is a Tier 3 judgment the method refuses. The concentration finding is presented
precisely to forestall that leap.

10
4.4 What the method emits, and what it refuses
The method emits, for the FY2024 MTA procurement report on named estimands: the
process composition by face value and by annual expenditure (Tier 2, descriptive); the MWBE
prime-vendor count share and its face-value and annual-expenditure shares, with three-vintage
figures and the repeat-reporting caveat (Tier 2, descriptive); the face-value vendor concentration
and Gini (Tier 2); and the scan-incomplete declarations (the stock-versus-flow composition, the
missing-versus-zero split, the deferred by-geography analysis, the community-view provenance).
It refuses: any determination of intent, steering, discrimination, favoritism, or fraud (Tier 3); any
claim that a dollar share measures attainment of an MWBE goal (outside the dataset's
constructs); any claim that competitive-process composition demonstrates rule compliance
(untested against operative guidelines); and any characterization of its outputs as fraud findings
or court-admissible evidence. Its outputs are descriptive structural measurements that an
oversight body or advocate may use as one input under its own standards.
5. Portability
The method is demonstrated on one authority. Its portability rests on the data-interface
contract: any jurisdiction publishing a record-level procurement ledger with defined amount
semantics, a process category, and declared-category flags can be audited by writing an adapter.
New York is favorable because many authorities report through the shared PARIS structures, so
the adapter applies with minimal change across authorities publishing to the same compiled
schema, which makes a second-authority instance readily available. That claim remains designed
and single-instance: this paper demonstrates the New York adapter, and cross-jurisdiction
transfer to a differently structured municipal ledger is stated but not yet shown.

11
6. Limitations
Beyond the tier limits, this note carries data-specific limitations made explicit after the
first audit round. The headline dollar figure is a face-value stock spanning awards from 1984 to
2025, not annual spending, and the annual-flow measure is nearly an order of magnitude smaller.
The three report vintages share many of the same multi-year contracts and cannot be summed or
treated as independent. The MWBE figure is a prime-vendor flag only, without indirect
participation, eligible-spend denominators, contract-specific goals, or waivers, and therefore
cannot speak to goal attainment. The competitive-process composition is not a compliance test.
The source is a derived community view that diverges slightly from the first-party dataset. The
MWBE flag and process coding are taken as published and not independently validated. The
paper began producer-side and has now converged. The single operational metric is the
consecutive qualifying-PASS count, which is TWO. Nine audit rounds have occurred: three
NON-PASS (F-AA-R1, F-AA-R2, F-AA-R3); a consistency-only PASS not credited (F-AA-R4);
a findings-bearing NON-PASS (F-AA-R5); the first qualifying pass (F-AA-R6, count to one); a
findings-bearing NON-PASS (F-AA-R7, reset to zero); a qualifying pass (F-AA-R8, count to
one); and a second consecutive qualifying pass (F-AA-R9, count to two). F-AA-R8 and F-AAR9 together are the two consecutive qualifying passes the methodology requires, so the
convergence gate is met on this artifact (released as v1.0). The convergence caveats (both
passing rounds shared the same three-member set, distinguished only by fresh instances; the two
rounds audited materially-identical substance) and the remaining owner-side deposit action are
recorded in the companion.

12
7. Provenance and Verification
The design vocabulary (the mizan as honest measurement, the asymmetric-measure
signature, the tier discipline) is drawn from structural readings of the Qur'an and is inspiration,
not evidence: every figure in Section 4 is justified entirely by public data, arithmetic, and
disclosed parameters. The program's own empirical foundation is explicit that the underlying
textual-structure finding is small and partly a length-sort artifact, with an earlier Fibonaccispecificity claim falsified and retracted (Arfeen 2026, al-Munāsabāt); this paper leans on none of
that. This is version 1.0, the canonical converged release (the convergence gate was met on the
identical v0.7 substance). It has been through nine independent cross-instance audit rounds
recorded in the companion. Three were NON-PASS and absorbed (F-AA-R1, F-AA-R2 by
OpenAI GPT; F-AA-R3 by the Claude producing lineage, non-qualifying). A fourth (F-AA-R4,
Gemini) returned PASS on a consistency review only and is not credited. A fifth (F-AA-R5) was
a findings-bearing NON-PASS. A sixth (F-AA-R6) was the first genuine qualifying pass. A
seventh (F-AA-R7) was a findings-bearing NON-PASS on a producer status-propagation defect
that reset the count to zero. The eighth and ninth (F-AA-R8 and F-AA-R9, rotated Model
Councils) were two consecutive qualifying passes: three qualifying non-producer members (GPT
5.5, GPT 5.4, Gemini 3.1 Pro) each executed the full reproduction and returned zero critical and
zero high in both rounds, with all prior findings confirmed resolved. The single operational
metric, the consecutive qualifying-PASS count, is TWO, so the convergence gate under Standing
Rule 7 is met on this artifact. Two caveats are recorded honestly with the declaration: the two
consecutive passing rounds used the same three-member set (independence between them rests
on fresh, memoryless instances rather than differing model identities), and they audited
materially-identical substance (the only change between the two was one companion wording

13
fix). The reproduction package is deposited under an immutable DOI alongside the audit and
provenance ledger (DOI 10.5281/zenodo.21445556), making the reproduction fully arm's-length.
8. Data Availability and Reproduction
Every figure in Section 4 is reproducible from the New York State open-data portal
without authentication. The source queried is the community view gpsc-qqsz; the first-party
MTA dataset twsw-2mqa and the ABO statewide authority-procurement dataset are the
recommended production sources and should be reconciled against it. FY2024 is selected with
fiscal_year_end_date='2024-12-31T00:00:00.000'. Face-value figures use
contract_amount; annual-flow figures use amount_expended_for_fiscal_year; award-

year composition uses award_date. The frozen three-year snapshot (37,988 records), its
manifest (with a programmatically regenerated field inventory validated against the rows) and
SHA-256, and a reproduction script that verifies the hash and recomputes every figure on both
estimands for all three years accompany this paper as a single reproduction package
(Bayyinah_AllocationAsymmetry_ReproPackage), deposited under an immutable DOI
alongside the audit and provenance ledger at DOI 10.5281/zenodo.21445556; anyone can
retrieve it there and re-run the full reproduction. Missing (1,348) and explicit-zero (48) amounts
are reported separately.
References
Arfeen, B. S. (2026). Bayyinah: Portable Structural Honesty Verification for Public-Service
Institutions. Working draft (the framework paper governing this note).

14
Arfeen, B. S. (2026). Bayyinah at-Taʿlīm: Structural Honesty Verification for Educational
Fairness Systems, from Primary Schooling to Graduate Research. Zenodo. DOI
10.5281/zenodo.21436484. https://zenodo.org/records/21436484
Arfeen, B. S. (2026). Al-Mutaffifīn: Structural Integrity Verification for Financial Governance
Systems. Zenodo. DOI 10.5281/zenodo.19894724. https://zenodo.org/records/19894724
Arfeen, B. S. (2026). Bayyinah al-Munāsabāt: A Multi-Corpus, Multi-Pipeline Falsification
Study. Zenodo. DOI 10.5281/zenodo.20069654. https://zenodo.org/records/20069654
Metropolitan Transportation Authority. Procurement Report (All). New York State Open Data
portal, community view gpsc-qqsz (derived from the statewide authority-procurement
dataset); first-party dataset twsw-2mqa. https://data.ny.gov/resource/gpsc-qqsz
New York State. Executive Law Article 15-A (Minority- and Women-Owned Business
Enterprises); Public Authorities Law Sections 2800 and 2879 (authority reporting and
procurement guidelines).



Bismillah ir-Rahman ir-Rahim
