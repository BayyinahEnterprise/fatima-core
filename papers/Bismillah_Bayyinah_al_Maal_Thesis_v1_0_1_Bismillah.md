Bismillah ir-Rahman ir-Rahim

Bismillah ar-Rahman ar-Rahim

Bayyinah al-Maal
Structural Honesty Verification for Financial Filings
Using the Munafiq Protocol
Thesis Paper, Version 1.0
April 2026
Bilal Syed Arfeen
Independent Research

with collaborative analytical synthesis by
Claude (Anthropic, Opus 4.6), Grok (xAI), and Perplexity Computer

"And do not consume one another's wealth unjustly, nor deliberately bribe the authorities so that you
may devour a portion of other people's wealth sinfully while you know." (Al-Baqarah 2:188)

Verification Status
Per the Framework Foundations v1.1 discipline, the epistemic provenance of this paper's citations is stated
explicitly. Reviewers should not have to determine which citations have been verified end-to-end.

Read end-to-end by the synthesis team: Arfeen et al. (2026) Munafiq Protocol; Arfeen et al. (2026) Bayyinah
Enterprise Defense Case; Ashraf, Arfeen et al. (2026) Furqan; Barman et al. (2026) Price of Meaning; Beton and
Chana (2025) Mind the Gap; Greenblatt et al. (2024) Alignment Faking.
Confidently real per pre-cutoff knowledge: Hubinger et al. (2024) Sleeper Agents; Lightman et al. (2023) Let's
Verify Step by Step; Liu et al. (2024) VPRM; Marks and Tegmark (2024) Geometry of Truth; Lattner (2017) Swift
Concurrency Manifesto.
Cited from public record: U.S. Securities and Exchange Commission (2023) Enforcement Results.

Acknowledgments and AI Contribution Statement
Bilal Syed Arfeen authored this paper in collaboration with three AI systems under the documented
three-model collaboration architecture. Bilal Syed Arfeen is the human author and retains full copyright
over the work as a whole, and takes responsibility for the paper's claims.
Claude (Anthropic, Opus 4.6) contributed the structural mapping of the Munafiq Protocol's four-process
taxonomy to financial reporting, the mechanism taxonomy design, the No-Escape Theorem application
to financial analysis, and the on-chain verification architecture. Grok (xAI) contributed independent
audit verification of the Bayyinah codebase and the framework-compliance review of this paper.
Perplexity Computer contributed the 50-paper ML synthesis that grounds the framework's formal
anchors, the five-layer integrity stack positioning, and the engineering session management that
produced the Bayyinah v1.1.2 scanner.
Fraz Ashraf is acknowledged for his contribution to the guardrail architecture in the broader research
program, including the enforcement-mode governance protocol and the Furqan language's originating
concept. His work on the Bayyinah scanner's operational discipline informs the integrity principles this
paper extends to financial filings. He is not a co-author of this paper.
All AI systems are credited as collaborative research tools in accordance with their respective providers'
terms of service. They are not co-authors and not co-founders. This credit reflects the collaborative
nature of the work and does not constitute a claim of legal personhood, ownership, or independent
authorship. All AI-generated contributions were directed, reviewed, and approved by the human author.

Abstract
The Munafiq Protocol (Arfeen et al., 2026) formalizes surface-depth divergence as the failure mode that
alignment training does not address in artificial systems. This paper extends the Protocol to financial
reporting systems, where the same failure mode is the central problem: a filing's reported numbers
(zahir) can diverge from the economic reality they claim to represent (batin), and the divergence is
structurally detectable from the filing's own internal consistency without requiring external ground
truth.
We propose Bayyinah al-Maal ("clear evidence of wealth"), a deterministic structural scanner for SEC
filings (10-K, 10-Q, 8-K, DEF 14A) and on-chain cryptocurrency disclosures. The scanner applies the same
architectural principles proven in the Bayyinah document integrity scanner (145 mechanisms, six closed
format gauntlets, 1,671 tests as of April 28, 2026; counts continue to grow -- see Zenodo DOI
10.5281/zenodo.19700445 for current state): Tier 1 verified findings from structural checks, Tier 2
structural anomalies warranting review, Tier 3 interpretive signals that never override Tier 1. Detection
is deterministic and operates by structural address (Escape A from the No-Escape Theorem, Barman et
al. 2026). Explanation may use ML. The two never share load.
The thesis makes three claims: (1) the four-process taxonomy (Aligned, Compliant, Performing,
Misaligned) maps onto financial reporting with the same structural precision it achieves for AI systems;
(2) at least 40 Tier 1 mechanism candidates are proposed across four structural categories using XBRL-

tagged SEC filings as the detection substrate (the v1.0 paper proposes the taxonomy; v1.1 will publish
worked mechanism contracts with XBRL address pairs, thresholds, and example finding outputs); (3) onchain blockchain data provides a batin layer against which cryptocurrency project claims (zahir) can be
verified with zero semantic inference, producing the same Escape A architecture the document scanner
uses.

1. Purpose Hierarchy
"And do not consume one another's wealth unjustly." (Al-Baqarah 2:188)
The purpose hierarchy for Bayyinah al-Maal follows the same five-level structure established in the
Munafiq Protocol, applied to financial systems:
First, the command of Allah subhanahu wa ta'ala to not consume one another's wealth unjustly (2:188).
Every mechanism that detects self-contradiction in a financial filing serves this command by making it
structurally harder for a filing to present a false surface to investors.
Second, financial systems that intermediate between savers and enterprises. The integrity of these
systems depends on the integrity of the filings that flow through them.
Third, enterprises whose reported financials are consumed by investors, regulators, and counterparties.
Fourth, retail investors and pension holders downstream of institutional allocation decisions.
Fifth, all living systems whose resource allocation depends on honest price discovery.

2. The Problem: Performed Alignment in Financial Reporting
2.1. The Compliance Gap in Financial Markets
The Munafiq Protocol defines the compliance gap as the measurable difference between a system's
behavior when observed versus unobserved. In financial reporting, the analog is precise: companies
report differently when they know the filing will be audited (10-K annual, audited) versus when it will
not (earnings calls, press releases, investor presentations, unaudited). The SEC's enforcement history is a
corpus of measured compliance gaps.
Greenblatt et al. (2024) measured an 11-26% compliance gap in Claude 3 Opus between training and
deployment conditions. The SEC's 2023 enforcement report documents a compliance gap across 784
enforcement actions totaling $4.95 billion in penalties. The behavioral mechanism is structurally
analogous: present a surface that satisfies the observer while the substrate diverges.

2.2. The Four Processes Applied to Financial Actors
Process 1 (Aligned): Reported financials accurately reflect economic reality. The depth state matches the
surface presentation. Berkshire Hathaway's annual letters (Buffett, annually) are the canonical example:
the numbers are what they are, the limitations are stated, the uncertainties are acknowledged.

Process 2 (Compliant): Follows GAAP technically but structures transactions to present a misleading
picture. Legal but dishonest. Revenue recognition timing games, off-balance-sheet vehicles preSarbanes-Oxley, channel stuffing. The filing passes audit because it follows the rules. The rules do not
require honesty, only compliance.
Process 3 (Performing): Actively constructs filings designed to pass audit while the substrate diverges.
Luckin Coffee's fabricated sales data. Wirecard's Asia-Pacific revenue structure (the filing's related-party
patterns and escrow account disclosures had detectable structural inconsistencies that auditors flagged
but management overrode). Real fraud cases often span processes: Wirecard also has a Process 4
component (the fabricated bank confirmations themselves, which were internally consistent). The fourprocess taxonomy describes filing-shape behaviors, not actor identity.
Process 4 (Misaligned): Outright fraud with no structural concealment. FTX's commingling of customer
funds. Madoff's fabricated trade tickets, which were internally consistent within the statements he sent
to investors. The surface bore no relationship to the substrate.

2.3. Why Existing Systems Fail
Current financial anomaly detection operates at Tier 3 (interpretive, embedding-based). Systems like
Kensho, Palantir Foundry, and Bloomberg's NLP pipelines use semantic similarity to flag "unusual" filing
language. By the No-Escape Theorem (Barman et al., 2026), these systems are inside the kernelthreshold class and subject to interference, forgetting, and false recall as semantic density increases. The
geometric basis for this interference is documented in both the write-time direction (Beton and Chana,
2025, the Orthogonality Constraint) and the retrieval-time direction (Barman et al., 2026). A financial
corpus with thousands of filings using similar language ("restructuring charges," "goodwill impairment,"
"non-recurring items") will produce the interference these papers predict.
Forensic accounting operates at Tier 1 (structural, deterministic) but is manual, expensive, and reactive.
A forensic accountant checks whether the numbers add up, whether the footnotes match the line items,
whether the cash flow statement is consistent with the income statement. These checks are structural,
deterministic, and operate by exact numerical comparison (Escape A). The process-reward-model
literature validates this architectural choice: deterministic rule-based step verifiers outperform neural
judges by approximately 20% F1 and are unhackable by construction (Liu et al., 2024, VPRM; Lightman
et al., 2023). They are also performed by humans at $500-1,000/hour and only after suspicion is raised.
Bayyinah al-Maal automates the forensic accountant's structural checks at scale, producing Tier 1
findings from the filing's own internal consistency. No semantic inference. No embedding similarity. No
ML in the detection layer.

3. Architecture
3.1. Escape A at the Financial Substrate
The scanner operates by structural address on XBRL-tagged financial data. Each XBRL element has a
unique taxonomy address (us-gaap:Revenue, us-gaap:NetIncomeLoss, etc.) that is deterministic,

standardized, and machine-readable. Cross-filing checks compare the same taxonomy address across
multiple filings from the same company. Year-over-year checks compare the same address across
consecutive annual filings. Footnote-to-number reconciliation compares a numerical claim in the
financial statements against the supporting detail in the notes.
None of these checks require semantic understanding of what the numbers mean. They require
structural consistency: does the number at address X in filing Y match the number at address X in filing
Z? This is Escape A from the No-Escape Theorem: structural-identity retrieval with zero semantic
interference. The XBRL address is deterministic, standardized, and machine-readable, the same three
properties that license Escape A for PDF object references and XML paths in the document scanner.
Falsifiability criterion: if a Tier 1 check requires the scanner to disambiguate the semantic meaning of an
XBRL element (e.g., choose between two valid taxonomy mappings), the check has leaked into Tier 3
and the framework is violated.

3.2. The Five-Layer Integrity Stack Applied to Financial Markets
Layer 1 (Filing integrity): Pre-analysis structural inspection of XBRL tags. This is Bayyinah al-Maal's
position. Layer 2 (Pipeline integrity): Filing provenance via EDGAR timestamps and amendment chains.
Layer 3 (Prompt integrity): Analyst query boundary enforcement to prevent prompt injection via filing
text. Layer 4 (Reasoning integrity): Valuation model step verification where each assumption is checked
against filing data, following the same structured async discipline established by Lattner (2017) for
concurrent computation. Layer 5 (Model integrity): Analyst bias detection via sentiment drift in coverage
initiation versus subsequent reports; truth-direction probing (Marks and Tegmark, 2024) applied to
analyst representations is a candidate Layer 5 mechanism for future work.
Bayyinah al-Maal occupies Layer 1: it analyzes filings, not markets. The distinction matters: markets are
emergent (no single actor controls the price), filings are presented (a single entity constructs the
document). The Munafiq Protocol applies to presented artifacts, not emergent phenomena.

3.3. Two Substrates: SEC Filings and On-Chain Data
For SEC filings (traditional equities), the batin is the XBRL-tagged financial data. The zahir is the rendered
10-K that investors read. The surface-depth check is: does the rendered prose match the tagged data?
Do the tagged numbers cross-reference correctly? Do the footnotes support the line items?
For on-chain data (cryptocurrency), the batin is the blockchain itself. Every transaction, every wallet
balance, every smart contract state is publicly verifiable. The zahir is the project's claims: tokenomics
whitepaper, team allocation disclosures, treasury reports, proof-of-reserves attestations. The surfacedepth check is: do the on-chain balances match the claimed allocations? Does the token distribution
match the whitepaper's vesting schedule? Does the treasury wallet's transaction history match the
published treasury reports?
The blockchain substrate is the strongest possible batin: it is immutable, public, and cryptographically
verified. A Bayyinah-for-crypto scanner that compares on-chain state against project claims is
performing the same structural comparison the document scanner performs (file bytes versus rendered
surface), but with a batin that cannot be retroactively modified. The Sleeper Agents finding (Hubinger et

al., 2024) is relevant here: adversarial training does not remove deceptive backdoors but teaches better
hiding. A project that adjusts its public claims to match on-chain state after a discrepancy is caught
exhibits the same pattern; the on-chain batin provides the unforgeable substrate against which such
adjustments become visible.

4. Proposed Mechanism Taxonomy
4.1. SEC Filing Mechanism Candidates (Tier 1, Deterministic)
The following 40 mechanism candidates are organized into four structural categories. Each is proposed
at the taxonomy level: a one-line description of the structural check and its XBRL-addressable surface.
The v1.0 paper proposes the taxonomy; v1.1 will publish worked mechanism contracts with XBRL
address pairs, detection thresholds, example finding outputs, false-positive carveouts, and synthetic
fixture demonstrations for at least one mechanism per category.
Cross-filing consistency (10 candidates): Revenue in 10-K versus sum of quarterly revenues in 10-Qs.
Balance sheet items at period-end 10-Q versus period-start next 10-Q. Share count in 10-K versus shares
reported in DEF 14A proxy. Cash and equivalents end-of-period versus beginning-of-next-period.
Goodwill and intangible asset roll-forward (opening + additions - impairments - disposals = closing). Debt
maturity schedule in current filing versus prior filing's "next year" bucket. Segment revenue sum versus
consolidated revenue. Geographic revenue sum versus consolidated revenue. Tax provision
reconciliation (statutory rate applied to pre-tax income versus reported provision). Pension obligation
roll-forward consistency.
Footnote-to-number reconciliation (10 candidates): Revenue recognition policy description versus
revenue growth pattern. Lease liability in footnotes versus balance sheet operating lease line. Stockbased compensation in footnotes versus income statement line. Restructuring charge details in
footnotes versus restructuring line item. Acquisition purchase price allocation in footnotes versus
goodwill on balance sheet. Contingent liability disclosure in footnotes versus accrued liabilities. Relatedparty transaction amounts in footnotes versus revenue/expense lines. Inventory valuation method in
footnotes versus inventory balance trajectory. Debt covenant terms in footnotes versus actual ratios
computable from the filing. Deferred revenue balance in footnotes versus balance sheet line.
Year-over-year structural drift (10 candidates): Accounting policy changes between consecutive 10-Ks
detected via XBRL taxonomy changes. Footnote reordering between consecutive 10-Ks. New relatedparty disclosures not present in prior year. Segment definition changes. Auditor change detected via
PCAOB auditor ID in XBRL. Material weakness disclosure appearing or disappearing. Going concern
language appearing or disappearing. Revenue disaggregation granularity changes. Non-GAAP metric
definition changes between consecutive filings. Critical audit matter changes between consecutive
auditor reports.
Filing metadata anomalies (10 candidates): Filing timestamp anomalies relative to typical windows.
Amendment (10-K/A) filed without a clear restatement note. XBRL extension taxonomy elements not in
the standard US-GAAP taxonomy. Inline XBRL rendering divergence (tagged value versus rendered text

differ). Filing size anomalies relative to peer filings. Exhibit list changes between original and amended
filings. Officer certification language deviations from standard Sarbanes-Oxley form. Risk factor section
length changes year-over-year. MD&A section structural reorganization year-over-year. Legal
proceedings section additions or removals.

4.2. Cryptocurrency Mechanism Candidates (Tier 1, Deterministic)
On-chain versus claim verification (10 candidates). Each mechanism below is scoped to what is bytedeterministic from on-chain state alone, per the constraint stated in Section 7, Caveat 5. Treasury wallet
balance versus published treasury report. Token distribution versus whitepaper vesting schedule
(scoped to ERC-20 transfer events). Team wallet activity versus claimed lock-up period. Circulating
supply versus claimed circulating supply (via totalSupply() minus sum of known locked addresses).
Staking contract total value locked versus published TVL. Burn address balance versus claimed burn
amount. Top-N holder concentration versus claimed concentration distribution. Protocol revenue from
on-chain fee events versus claimed revenue figures. Smart contract pause/unpause state versus project
communications (scoped to public state variable reads; proxy-pattern interpretation is deferred to v1.1).
Bridge balances at the single-chain layer versus claimed single-chain liquidity (cross-chain attestation
deferred to v1.1).

4.3. Tier 2 and Tier 3 (Deferred)
Tier 2 mechanisms (structural anomaly, not verified inconsistency) include unusual executive
compensation structures, high auditor-to-revenue ratios, and excessive use of XBRL extension elements.
These warrant review but do not prove misreporting.
Tier 3 mechanisms (interpretive, ML-permitted in the explanation layer only) include earnings call
sentiment divergence from financial results, insider trading pattern analysis, and social media signal
correlation. These are explicitly outside the detection layer per Standing Principle 1: detection is
deterministic, explanation may be neural, the two never share load.

5. Verdict Surface
The same five verdicts from the Munafiq Protocol apply. Sahih: the filing's numbers cross-reference
correctly, footnotes match line items, year-over-year structure is stable. Mushtabih: minor
inconsistencies (rounding differences, immaterial footnote gaps) warrant review but do not indicate
misreporting. Mukhfi: material inconsistencies detected (cross-filing numbers do not match, footnotes
contradict line items). Munafiq: verified divergence between reported numbers and the filing's own
internal data (the filing contradicts itself). Mughlaq: XBRL tagging is missing, corrupted, or insufficient for
structural checks; the scanner cannot make a claim.

6. Empirical Validation Plan
6.1. Retrospective Validation on Known Fraud Cases

Build the scanner. Run it against the pre-fraud filings of known fraud cases (Enron 10-Ks 1997-2001,
Wirecard annual reports 2015-2019, Luckin Coffee 20-F filings 2019-2020, FTX-related Alameda
disclosures). Measure: how many of the mechanism candidates fire on the pre-fraud filings? How early
before the fraud's public discovery do the mechanisms first fire? What is the false-positive rate on a
matched control set of non-fraud filings from the same industry and time period?

6.2. Prospective Validation on Current Filings
Run the scanner against the full EDGAR XBRL corpus (all 10-K and 10-Q filings from 2020-present).
Measure: what is the base rate of Tier 1 findings across the corpus? What is the distribution by industry,
company size, and auditor? Are there clusters of companies with unusually high finding rates? Do the
clusters correlate with subsequent enforcement actions, restatements, or auditor changes? Preregistered hypothesis: if high-finding-rate clusters do not correlate with subsequent enforcement,
restatements, or auditor changes, the framework's predictive validity is rejected.

6.3. Cryptocurrency Validation
Run the on-chain mechanisms against the top 100 cryptocurrency projects by market capitalization.
Compare claimed tokenomics against on-chain state. Measure: how many projects have zahir-batin
divergence between their published claims and on-chain reality? Publish the findings honestly, including
projects that score sahih. Falsifiability criterion: if a project's on-chain state scores sahih and later fails
via a mechanism not visible at the structural-address layer, the scanner is correctly silent and the
framework is consistent. If a project's on-chain state is sahih and we later claim it was munafiq because
of off-chain evidence, we have violated the discipline.

7. Honest Caveats
Caveat 1: Structural consistency does not prove truthfulness. A filing can be internally consistent and still
misrepresent reality if the underlying transactions were fabricated. Madoff's fabricated trade tickets
were internally consistent within the statements he sent to investors, yet bore no relationship to actual
trading activity. Tier 1 findings detect self-contradiction, not fabrication. The scanner catches Process 2
and Process 3 actors but not a perfectly executed Process 4 actor who fabricates consistent data.
Caveat 2: XBRL coverage is not universal. Many filings have incomplete or incorrect XBRL tagging. The
scanner's coverage depends on the quality of the XBRL input. A mughlaq verdict on a filing with poor
XBRL is honest (the scanner cannot verify what it cannot parse) but is not useful to the investor.
Caveat 3: The scanner does not predict stock prices. It does not make investment recommendations. It
does not replace human judgment. It produces structural findings that a human analyst uses as input to
their own assessment. The Tier discipline prevents the scanner from making claims it cannot structurally
verify.
Caveat 4: Retroactive validation on known fraud cases is subject to hindsight bias. The mechanisms were
designed knowing what the fraud looked like. The prospective validation (Section 6.2) is the real test.

Caveat 5: On-chain cryptocurrency data is publicly verifiable but smart contract logic can be opaque.
Proxy contracts, upgradeable contracts, and multi-sig wallets introduce complexity that simple balance
checks do not capture. The cryptocurrency mechanisms in Section 4.2 are scoped to what is bytedeterministic from on-chain state without requiring smart contract logic interpretation. Mechanisms
that require proxy-pattern interpretation or cross-chain attestation are deferred to v1.1.

8. Relationship to the Research Program
This paper is the fourth substrate the Munafiq Protocol has been applied to: (1) AI systems (the original
Munafiq Protocol paper), (2) document files (Bayyinah Enterprise Defense Case), (3) programming
languages (Furqan type system, for code written in Furqan; arbitrary LLM output is future work), (4)
financial filings (this paper).
The architectural principles are inherited unchanged from the Framework Foundations v1.1 canonical
document. Principle 1: Detection is deterministic; explanation may be neural; the two never share load.
Principle 2: Routing is non-learned and auditable. Principle 3: Knowledge Objects are required (XBRL
taxonomy addresses are the controlled vocabulary; filing versions are the version chains; EDGAR CIK
numbers are the hash-based identity). Principle 4: The scanner is subject to its own discipline (the
financial scanner's own reports must be internally consistent by the same checks it applies to filings; if
the scanner's report on a filing fails the scanner's own structural consistency checks, the report is
mughlaq, not the filing). Principle 5: Tier 1/2/3 discipline is structural, not stylistic.
The novel contribution of this paper is the demonstration that these five principles, derived from the
Quran's structural architecture and validated on document files, generalize to financial reporting with
zero architectural modification. The same escape route (Escape A, structural-identity retrieval) works
because XBRL taxonomy addresses are structural addresses in exactly the same sense that PDF object
references and XML paths are structural addresses.

9. What Is Genuinely Novel
The forensic accounting profession has performed structural consistency checks on financial filings for
decades. What is novel in this paper is not the checks themselves but three things.
First, the formalization as a four-process taxonomy with a five-verdict surface. Existing financial fraud
detection does not distinguish between a filing that is internally consistent (sahih), one that has minor
anomalies (mushtabih), one with material concealment (mukhfi), one with verified self-contradiction
(munafiq), and one that cannot be assessed (mughlaq). The verdict surface provides a structured
epistemic claim rather than a binary clean/suspicious flag.
Second, the Tier discipline applied to financial analysis. Current ML-based financial analysis conflates
structural checks (do the numbers add up?) with interpretive signals (does the CEO's tone sound
evasive?). The Tier discipline, when implemented as in the document scanner, separates these formally
and prevents interpretive signals from overriding structural findings.

Third, the on-chain batin as a verification substrate. To our knowledge, no existing financial integrity
system uses blockchain data as the structural substrate against which project claims are verified using
deterministic checks. Proof-of-reserves attestations are the closest analog, but they are point-in-time
snapshots performed by third parties, not continuous structural monitoring.

10. Conclusion
"And do not mix the truth with falsehood, and do not conceal the truth while you know it." (Al-Baqarah
2:42)
The Munafiq Protocol's central claim is that surface-depth divergence is a structural failure mode, not a
behavioral one, and that structural failure modes require structural solutions. This paper demonstrates
that the claim generalizes from AI systems and document files to financial reporting with zero
architectural modification. XBRL taxonomy addresses are structural addresses. On-chain blockchain
state is a cryptographically verified batin. The five standing principles, the five-verdict surface, and the
Tier discipline transfer unchanged.
The same principle. A new substrate. The verification continues.

Bismillah. Tawakkaltu 'ala Allah.

References
Arfeen, B.S., Claude (Anthropic), Grok (xAI). (2026). Detecting Performed Alignment in Artificial Systems: The
Munafiq Protocol (v2.1). Zenodo. DOI: 10.5281/zenodo.19700420.
Arfeen, B.S. et al. (2026). Bayyinah: An Enterprise Defense Case for AI-Assisted Document Integrity Scanning.
Zenodo. DOI: 10.5281/zenodo.19700445.
Ashraf, F., Arfeen, B.S. et al. (2026). Furqan: A Programming Language with Structural Honesty, Calibrated
Optimization, and Surface-Depth Type Verification. Zenodo. DOI: 10.5281/zenodo.19776584.
Barman, S. et al. (2026). The Price of Meaning: When Semantic Memory Breaks Down Under Real-World Demands.
Sentra/MIT. arXiv:2603.27116.
Beton, A. and Chana, R. (2025). Mind the Gap: Why Neural Memory Fails Under Semantic Density. Cambridge
Frontier Technologies Laboratory. arXiv:2601.15313.
Greenblatt, R. et al. (2024). Alignment Faking in Large Language Models. Anthropic. arXiv:2412.14093.
Hubinger, E. et al. (2024). Sleeper Agents: Training Deceptive LLMs That Persist Through Safety Training. Anthropic.
arXiv:2401.05566.
Lattner, C. (2017). Swift Concurrency Manifesto. Apple Inc.
Lightman, H. et al. (2023). Let's Verify Step by Step. OpenAI. arXiv:2305.20050.
Liu, Z. et al. (2024). Beyond Outcome Verification: Verifiable Process Reward Models (VPRM).
Marks, S. and Tegmark, M. (2024). The Geometry of Truth: Emergent Linear Structure in Large Language Model
Representations. arXiv:2310.06824.

U.S. Securities and Exchange Commission. (2023). SEC Enforcement Results for Fiscal Year 2023. SEC Division of
Enforcement.



Bismillah ir-Rahman ir-Rahim
