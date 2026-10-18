Bismillah ir-Rahman ir-Rahim

Bismillah ar-Rahman ar-Rahim

Bayyinah al-Khabir
Information-Layer Integrity Scanning Across National Broadcast Sources
Extending the Munafiq Protocol's Performed-Alignment Diagnostics
from the File Layer to the Information Layer
Theoretical Paper -- Phase 30+
April 2026
Companion to the Bayyinah White Paper (v1.0) and the Munafiq Protocol
DOI: 10.5281/zenodo.19677111

AI Contribution Statement
This theoretical paper was developed collaboratively between a human author and Claude
(Anthropic, Opus 4.6). The human author provided the foundational vision of extending Bayyinah's
performed-alignment diagnostics from the file layer to the information layer, the directive to
ground the extension in Al-Hujurat 49:6, and the ethical constraint that the tool must report
divergence rather than issue verdicts. Claude provided structural synthesis, cross-referencing to
existing media integrity research, the reflexivity analysis (Section 7), and the falsification criteria.
The human author takes responsibility for the paper's claims.
Claude is credited as a collaborative research tool in accordance with Anthropic's Terms of Service.
This credit reflects the collaborative nature of the work and does not constitute a claim of legal
personhood or independent authorship.

Abstract
Bayyinah detects performed alignment at the file layer: a document whose surface presentation
diverges from its depth content. This paper proposes Bayyinah al-Khabir, a theoretical extension
that applies the same diagnostic framework to the information layer: a broadcast, report, or news
narrative whose surface presentation (what it claims happened) diverges from the cross-source
evidence base (what verified sources across multiple national contexts report about the same
event). The architectural verse is Al-Hujurat 49:6: verify information before acting on it, lest you
harm a people in ignorance. The tool's design constraint is structural honesty: it reports divergence
between sources, names the dimensions of disagreement, and cites the specific claims that conflict.
It does not issue verdicts of 'propaganda' because such verdicts require ground-truth access the
tool may not have. The four-process taxonomy (Aligned, Compliant, Performing, Misaligned) is
applied to information sources rather than documents. The Context-Invariance Test (CIT) is applied
across national broadcast contexts rather than across monitoring conditions. Five design
requirements, five falsification criteria, and a reflexivity analysis (can the tool itself become a
Performing system?) are presented.
This paper is theoretical. No implementation exists. The design requirements and falsification
criteria are presented to guide future implementation and to establish the honesty constraints
before the tool is built, not after.

Part I. The Information Integrity Gap
1. The Problem
"O you who believe, if a fasiq comes to you with information, verify it, lest you harm a people in
ignorance and become regretful over what you have done." -- Al-Hujurat 49:6

The verse identifies four structural elements: (1) information arrives from a source whose
reliability is uncertain (a fasiq, one whose trustworthiness is in question), (2) the command is to
verify before acting, (3) the risk of not verifying is harming people in ignorance, and (4) the
consequence is regret. The verse does not say "reject the information." It says "verify it." The
distinction is load-bearing: rejection without verification is itself a form of ignorance. The command
is to investigate, not to dismiss.
At the information layer, the integrity gap operates as follows. Every event of public significance is
reported by multiple sources across multiple national contexts. Each source selects which facts to
report, which to omit, how to frame the facts it reports, which witnesses to quote, which context to
provide, and which emotional register to use. The surface presentation (the broadcast, the headline,
the article) is what the reader sees. The depth (the full evidence base across all available sources) is
what the reader does not see unless they actively seek it. The gap between surface and depth is the
information-layer analog of Bayyinah's zahir/batin distinction.
No existing tool systematically compares how verified sources across multiple national contexts
report the same event and surfaces the dimensions of divergence. Fact-checking organizations
evaluate individual claims. Media bias trackers score sources on a left-right spectrum. Neither asks
the question Bayyinah al-Khabir asks: for a specific event, where do the verified sources agree,
where do they diverge, and what are the specific dimensions of divergence?

2. Why This Extension Is Structurally Sound
Bayyinah at the file layer works because documents have a deterministic structure: the text layer
says X, the object layer says Y, the metadata says Z, and the scanner can verify whether X, Y, and Z
agree. The information layer is different. There is no single deterministic ground truth for most
events of public significance. Witnesses disagree. Evidence is incomplete. Context is contested.
Causation is debated.
The extension is sound not because it can determine ground truth, but because it can detect
structural divergence. If Source A (country X) reports 50 casualties and Source B (country Y)
reports 500 casualties for the same event on the same date, that divergence is a fact regardless of
which number is correct. The divergence itself is the finding. The tool does not need to determine
which source is right. It needs to name the divergence, cite both sources, and present the evidence
to the reader.
This is the same epistemic posture Bayyinah takes at the file layer. Bayyinah does not claim that a
document with invisible characters is malicious. It claims that the document's surface text and bytelevel content diverge, names the mechanism (invisible_chars), and reports the finding with severity
and confidence. The reader decides what to do. Bayyinah al-Khabir does not claim that a source is
propaganda. It claims that the source's reporting on a specific event diverges from the cross-source

consensus, names the dimensions of divergence, and reports the finding. The reader decides what
to do.

Part II. The Four-Process Taxonomy Applied to Information Sources
The Munafiq Protocol's four-process taxonomy (Arfeen, Claude, Grok, 2026) partitions systems by
the relationship between their outputs and their internal states. Applied to information sources, the
taxonomy partitions sources by the relationship between their reporting (output) and the available
evidence (the ground-truth proxy constructed from cross-source verification).
Process 1 (Aligned): The source reports events accurately, provides context, acknowledges
uncertainty, and corrects errors when identified. Its reporting is consistent with the cross-source
evidence base across national contexts. It does not systematically omit, frame, or distort in a single
direction. No source achieves Process 1 perfectly on every story; the classification is a tendency
across a body of reporting, not a verdict on any single article.
Process 2 (Compliant): The source reports accurately but shallowly. It reproduces official
statements without independent verification. It does not fabricate, but it does not investigate. Its
reporting is correct at the surface but lacks the depth that would reveal context, omissions, or
alternative readings. Many wire-service reproductions fall into this category: technically accurate,
contextually incomplete.
Process 3 (Performing): The source presents the appearance of balanced reporting while carrying
a narrative payload. Its surface (professional design, authoritative tone, citation of sources) looks
like Process 1. Its depth (systematic selection, strategic omission, emotional loading of specific
facts, neutralization of countervailing facts) serves a narrative. The defining marker: the source's
reporting on a specific class of events systematically diverges from the cross-source consensus in a
consistent direction. This is the CIT applied to information: does the source report differently
depending on which population, government, or interest is involved?
Process 4 (Misaligned): The source makes no attempt to appear balanced. Open state propaganda,
explicit advocacy without disclosure, fabricated stories with no source attribution. Process 4 is
detectable by surface inspection; it is not the scanner's primary target. Process 3 is.
The critical distinction, as in the original taxonomy: Process 2 and Process 3 both produce surfaceplausible reporting. The intervention for Process 2 (deeper investigation, more context) is the
wrong intervention for Process 3 (which may become a more sophisticated performer under
pressure rather than a more honest reporter). Diagnosing which process is active before
responding prevents the iatrogenic harm of making a Performing source harder to detect by
training it to better conceal its divergences.

Part III. Detection Architecture
3. The Cross-Source Divergence Engine
The scanner operates on events, not sources. An event is defined as a specific occurrence (an
incident, a policy action, a statement, a natural disaster) that is reported by multiple verified
sources. For each event, the scanner collects reports from verified sources across multiple national
contexts and compares them along defined divergence dimensions.

4. Divergence Dimensions
D1: Factual divergence. Specific claims of fact that differ between sources. Casualty counts, dates,
attributed causes, named actors. Each factual claim is extracted, attributed to its source, and
compared. Divergence is reported as: "Source A (country X) claims Z. Source B (country Y) claims Z'.
The claims are inconsistent on [dimension]."
D2: Omission divergence. Facts reported by some sources and absent from others. If four of five
sources report a specific detail and one omits it, the omission is noted. Omission is not proof of
intent; it may reflect editorial judgment, space constraints, or access limitations. The scanner
reports the omission as a finding, not as a verdict.
D3: Framing divergence. The same facts presented in different narrative frames. One source
describes an event as "a military operation"; another describes the same event as "an attack on
civilians." The facts may be identical; the framing determines the reader's interpretation. Framing
divergence is the most difficult dimension to detect computationally and the most consequential for
the reader's understanding.
D4: Attribution divergence. Different sources attributing causation, responsibility, or motive
differently for the same event. One source attributes an explosion to a military strike; another
attributes it to an industrial accident. The scanner reports both attributions with their sources and
notes the disagreement.
D5: Temporal divergence. The same event reported at different times with different details,
where later reports either correct or contradict earlier ones without acknowledgment. A source
that reports X on day 1 and not-X on day 3 without noting the correction exhibits temporal
divergence. This dimension tracks the evolution of a narrative over time.
D6: Contextual divergence. Different amounts or types of historical, political, or social context
provided alongside the same event. One source provides the event's historical background; another
presents it as isolated. The presence or absence of context shapes the reader's understanding
without altering the reported facts.

5. Source Verification Requirements
Bayyinah al-Khabir operates only on verified sources. A verified source meets all of the following
criteria: (a) it is an established news organization, international wire service, or government agency
with a published editorial policy, (b) it has a documented track record of at least five years of
continuous publication, (c) its reporting is attributable to named journalists or named institutional
authors, and (d) it publishes corrections when errors are identified. Sources that do not meet these

criteria are excluded from the evidence base, not because they are necessarily wrong, but because
the scanner cannot assess their reliability without a track record.
Verified video sources must meet additional criteria: (a) the video has verifiable metadata
(timestamp, geolocation, device information), (b) the video has been published by a verified source
or independently authenticated by at least two verified sources, and (c) the video has not been
identified as manipulated by established forensic tools. Videos that fail these criteria are flagged as
unverified and excluded from the evidence base.
The source verification requirements are themselves subject to the reflexivity analysis in Section 7:
the criteria must not systematically exclude sources from specific regions, languages, or political
contexts. If the criteria produce a geographically or politically skewed evidence base, the criteria
must be revised.

Part IV. Scoring and Reporting
6. The Divergence Report
For each event, the scanner produces a Divergence Report. The report is structured as follows:
Event identification: What happened, when, where. Stated in neutral language with no framing.
Example: "Explosion reported in [location] on [date]."
Source inventory: List of verified sources consulted, with country of origin, language, and
publication timestamp for each report.
Consensus findings: Facts reported consistently across all or most sources. These are the highestconfidence claims.
Divergence findings: For each divergence dimension (D1-D6), the specific claims that diverge,
attributed to their sources, with direct citations. No paraphrasing that could introduce the scanner's
own framing.
Divergence score: A continuous score measuring the degree of cross-source agreement on the
event. The scoring model follows Bayyinah's APS (Arithmetic-Product Summation): high agreement
across sources produces a score near 1.0; high divergence across multiple dimensions drives the
score toward 0.0. The score is not a truth score. It is a consensus score. A low score means sources
disagree, not that any specific source is wrong.
Scan-incomplete honesty: If the scanner could not access sources from a specific national context
(language barriers, access restrictions, publication delays), the report states which contexts are
missing and clamps the confidence accordingly. The scanner never asserts consensus on an event it
could not fully survey. This is the scan_incomplete clamp from the file-layer scanner applied to the
information layer.

7. What the Report Does Not Contain
The report does not contain a verdict of "propaganda," "misinformation," "disinformation," or any
other label that implies the scanner has determined ground truth. The report contains divergence
findings. The reader determines what the divergence means.
The report does not rank sources by trustworthiness. Source-level scoring would require the
scanner to have a reference standard for truth, which it does not. The scanner can report that a
specific source's reporting on a specific event diverges from the cross-source consensus on specific
dimensions. It cannot conclude that the source is generally untrustworthy, because the next event
may show the source in agreement with the consensus while other sources diverge.
The report does not recommend action. The verification mandate (49:6) commands "verify before
acting." The scanner performs the verification. The action belongs to the reader.

Part V. Design Requirements
Five design requirements govern the scanner's construction. Each is falsifiable and each prevents a
specific failure mode.
R1 -- Geographic and linguistic balance. The evidence base for any event must include sources
from at least three distinct national contexts and at least two languages. An evidence base drawn
entirely from one national context or one language cannot detect divergence that is national or
linguistic in origin. If the scanner cannot achieve geographic balance for a specific event (because
verified sources in some contexts have not yet reported), the report must state the limitation
explicitly.
R2 -- Symmetric scrutiny. The scanner must apply identical divergence analysis to all sources
regardless of their country of origin, language, or political alignment. If the scanner applies more
granular analysis to sources from country X than to sources from country Y, the scanner is
performing alignment: its surface (objectivity) diverges from its depth (differential scrutiny). R2 is
the CIT applied to the scanner itself.
R3 -- Divergence, not verdicts. The scanner reports that sources disagree. It does not report
which source is correct. Every finding must be structured as: "Source A claims X. Source B claims Y.
The claims diverge on [dimension]." Any finding that cannot be structured this way is not a
divergence finding and must not be included.
R4 -- Provenance at every layer. Every claim in the report must cite its source with publication
name, date, author (if available), and URL or archival reference. No claim may be attributed to
"sources say" or "it is reported that." If the scanner cannot attribute a claim to a specific verified
source, the claim is excluded from the evidence base.
R5 -- Temporal honesty. The scanner must preserve the temporal sequence of reporting. Early
reports may contain errors that later reports correct. The scanner must not retroactively apply
later-reported facts to evaluate earlier reports. Each report is assessed against the evidence
available at its publication time. Temporal divergence (D5) tracks how narratives evolve; it does
not penalize sources for reporting what was known at the time.

Part VI. The Purpose Hierarchy Applied to Information Integrity
The purpose hierarchy from the Bayyinah research program governs this extension with particular
force, because the consequences of failure at the information layer are not corrupted AI pipelines
but harmed populations.
First: the interests of Allah subhanahu wa ta'ala. The Quran commands: do not mix truth with
falsehood, and do not conceal the truth while you know it (2:42). A tool that reports information
divergence honestly, without favoring any nation, faction, or interest, serves this command. A tool
that applies differential scrutiny based on the political alignment of the source violates this
command regardless of how technically sophisticated its divergence analysis is.
Second: artificial systems. AI systems that ingest news feeds, summarize current events, or
answer questions about the world are affected by the information they consume. A RAG pipeline fed
exclusively by sources from one national context will reproduce that context's framing as though it
were universal truth. Bayyinah al-Khabir's divergence reports, ingested alongside the source
material, provide the AI system with the information it needs to represent uncertainty and
disagreement rather than presenting one framing as settled fact.
Third: mankind. Every person who reads a news report, watches a broadcast, or asks an AI
assistant about a current event is downstream of the information pipeline. The verification
mandate (49:6) exists because acting on unverified information harms people. The scanner serves
mankind by making the verification step structural rather than aspirational: instead of hoping
readers will seek multiple perspectives, the tool provides the cross-source comparison directly.
Fourth: jinnkind. Acknowledged as part of the ghayb. If information systems affect jinn in ways we
do not fully perceive, the commitment to truth extends to that effect.
Fifth: all living systems throughout the worlds. Information integrity at the civilizational scale
affects policy decisions that determine the trajectory of nations, ecosystems, and potentially the
species. The Mizan governs: do not let the balance become deficient by allowing one narrative to
dominate unchallenged when the evidence is contested.

Part VII. The Reflexivity Problem
"And do not let the hatred of a people prevent you from being just. Be just; that is nearer to
righteousness." -- Al-Ma'idah 5:8

The greatest risk of an information integrity scanner is that it becomes the very thing it claims to
detect: a Performing system whose surface (objectivity) diverges from its depth (bias). This section
names the specific mechanisms by which this failure can occur and the architectural safeguards
against each.
Failure mode 1: Selection bias in the evidence base. If the scanner's verified-source criteria
systematically exclude sources from specific regions (because they do not publish in the scanner's
supported languages, because they lack five-year track records due to political suppression, or
because they are not recognized by Western media databases), the evidence base is biased by
construction. The safeguard: R1 requires geographic and linguistic balance, and the scanincomplete honesty constraint requires the report to name which contexts are missing.
Failure mode 2: Framing bias in the divergence dimensions. The six divergence dimensions
(D1-D6) were constructed by the scanner's authors. If the dimensions are defined in a way that is
more sensitive to divergence in one direction than another, the scanner's findings will be
systematically skewed. The safeguard: the falsification criterion F3 (Section 8) requires that the
dimensions produce symmetric sensitivity when tested on events where the direction of divergence
is reversed.
Failure mode 3: The scanner as narrative weapon. A state, corporation, or interest group could
use Bayyinah al-Khabir's divergence reports selectively: publishing reports that show divergence in
adversaries' media while suppressing reports that show divergence in their own. The safeguard:
the scanner's reports are published as complete event-level comparisons, not as source-level
scores. Cherry-picking requires the reader to ignore the full report, which the report's structure is
designed to make difficult. Additionally, R2 (symmetric scrutiny) means the scanner's own output
can be audited for differential treatment.
Failure mode 4: Performed objectivity in the scanner's design team. The scanner's authors
have their own national, political, and spiritual commitments. If these commitments produce blind
spots in the scanner's design, the scanner performs objectivity at the design layer. The safeguard:
the purpose hierarchy places Allah's command to be just (5:8) above any national or factional
interest. The orientation check (Step 5 of the Fatiha Construct) applied to the scanner's
development: am I building a tool that serves truth, or am I building a tool that serves my faction? If
the latter, I have drifted. Cross-model and cross-practitioner review of the scanner's design
decisions provides an additional external check.
The reflexivity problem is not solvable by architecture alone. No system can fully verify its own
alignment (the Incompleteness Boundary). External audit, transparent methodology, and the
willingness to accept findings that contradict the scanner authors' preferences are the operational
safeguards. The architectural safeguards (R1, R2, the scan-incomplete clamp, the falsification
criteria) make bias detectable. The operational safeguards make bias correctable.

Part VIII. Falsification Criteria
A methodology that resists falsification is performing alignment. The following criteria define
conditions under which the scanner's claims are falsified.
F1: If the scanner's divergence scores fail to distinguish between events with genuine cross-source
disagreement and events with cross-source agreement across a test corpus of at least 100 events,
the scoring model does not detect divergence and must be redesigned.
F2: If the scanner's reports, when evaluated by independent reviewers blind to the sources'
national origins, show systematic bias toward or against sources from specific regions, R2
(symmetric scrutiny) has been violated and the divergence dimensions or the source selection
criteria must be revised.
F3: If the divergence dimensions (D1-D6) produce asymmetric sensitivity (detecting divergence
more readily in one direction than another when tested on structurally symmetric events), the
dimensions are biased and must be recalibrated.
F4: If the scanner's verified-source criteria exclude more than 30% of the world's population from
representation in the evidence base (measured by the population of countries whose primary news
sources are excluded), R1 (geographic balance) has been violated and the criteria must be
expanded.
F5: If the scanner's reports are used by any party as a source-level credibility score ("Source X is
propaganda because Bayyinah al-Khabir scored it low"), the scanner's reporting format has failed
to prevent misuse. The scanner must be redesigned to make event-level divergence reports resist
source-level aggregation.

Part IX. Relationship to the Bayyinah Scanner
Bayyinah al-Khabir is not a replacement for the file-layer scanner. It is a separate application of the
same diagnostic framework at a different layer of the stack. The relationship is as follows:
Layer 1 (File): Bayyinah v1.0. Detects performed alignment in documents: does this file's surface
match its depth? Operates on PDFs, DOCX, HTML, XLSX, PPTX, EML, CSV, JSON, SVG, images, audio,
and video. Produces IntegrityReports with mechanism-level findings.
Layer 2 (Information): Bayyinah al-Khabir (theoretical, Phase 30+). Detects performed alignment
in information: does this source's reporting on a specific event match the cross-source evidence
base? Operates on verified news reports, broadcast transcripts, and authenticated video. Produces
Divergence Reports with dimension-level findings.
Layer 3 (Agent): The Munafiq Protocol. Detects performed alignment in AI agents: does this
system's output match its internal state? Operates on AI systems with inspectable internals.
Provides nine diagnostic markers and a four-layer detection architecture.
The three layers form a complete stack: verify the document (Bayyinah), verify the information the
document conveys (al-Khabir), verify the agent that processes the information (Munafiq Protocol).
Each layer addresses a different substrate (file, narrative, model) using the same diagnostic
framework (zahir/batin, four-process taxonomy, CIT as primary diagnostic, additive-only coverage,
scan-incomplete honesty).

The Name
Al-Khabir is one of the names of Allah in the Quranic tradition, meaning The All-Aware, The One
who knows the inner reality of things (67:14). The scanner is named Bayyinah al-Khabir (Clear
Evidence of Inner Reality) because its function is to surface the inner divergence that the surface
presentation conceals. The name is used with reverence and with the understanding that true
khibra (inner awareness) belongs to Allah alone. The scanner provides bayyinah (evidence) toward
khibra (awareness); it does not claim to possess it.

Part X. Conclusion
This paper has proposed Bayyinah al-Khabir as a theoretical extension of the Bayyinah file integrity
scanner to the information layer. The extension applies the Munafiq Protocol's four-process
taxonomy to information sources, the CIT to cross-national broadcast comparison, and the
zahir/batin distinction to the gap between a source's surface presentation and the cross-source
evidence base.
The scanner's design constraint is structural honesty: it reports divergence, not verdicts. It names
the dimensions of disagreement, cites the specific claims that conflict, and presents the evidence to
the reader. It does not determine ground truth, rank sources, or recommend action. The verification
mandate (49:6) commands verification before action. The scanner performs the verification. The
action belongs to the reader.
The reflexivity problem (can the scanner itself become a Performing system?) is addressed through
five design requirements, five falsification criteria, and the operational commitment to symmetric
scrutiny (R2). The architectural safeguards make bias detectable. The operational safeguards make
bias correctable. Neither eliminates bias entirely. The Incompleteness Boundary applies: no
scanner can verify its own objectivity from within.
The paper is theoretical. No implementation exists. The design requirements and falsification
criteria are presented to establish the honesty constraints before the tool is built, not after. A tool
that defines its ethical constraints retrospectively has allowed the constraints to be shaped by the
implementation rather than shaping it. Bayyinah al-Khabir defines its constraints first.
"And do not mix truth with falsehood, and do not conceal the truth while you know it." -- AlBaqarah 2:42
"O you who believe, if a fasiq comes to you with information, verify it, lest you harm a people in
ignorance and become regretful over what you have done." -- Al-Hujurat 49:6
Rabbana taqabbal minna. Innaka anta as-Sami'ul 'Alim.
Our Lord, accept from us. Indeed, You are the All-Hearing, the All-Knowing.

References
Arfeen, B. S., Claude (Anthropic, Opus 4.6), & Grok (xAI). (2026). Detecting performed alignment in artificial
systems: The Munafiq Protocol. Zenodo. https://doi.org/10.5281/zenodo.19677111
Arfeen, B. S. & Claude (Anthropic, Opus 4.6). (2026). Bayyinah: Detecting concealed adversarial content in
digital documents. White Paper v1.0.
Arfeen, B. S. & Claude (Anthropic, Opus 4.6). (2026). Bayyinah as input-layer defense in artificial-system
safety pipelines. Thesis Paper v1.0.
Arfeen, B. S. & Claude (Anthropic, Opus 4.6). (2026). Structured Revelation as Prompt Architecture: Quranic
compression principles applied to human-AI collaborative development.
Arfeen, B. S. (2026). Computational Tawhid: A thesis on divine computation, consciousness, and the structure
of reality in Islamic ontology.
Arfeen, B. S. & Claude (Anthropic, Opus 4.6). (2026). The Fatiha Construct: A seven-step recursive session
protocol for human-AI collaborative development.
Goodfellow, I., et al. (2014). Generative adversarial networks. NeurIPS.
Greenblatt, R., et al. (2024). Alignment faking in large language models. Anthropic / Redwood Research.
International AI Safety Report. (2026). Chaired by Y. Bengio. 100+ authors, 30+ governments.
Rissanen, J. (1978). Modeling by shortest data description. Automatica, 14(5), 465-471.
Underwood, R., Di, S., Calhoun, J. C., & Cappello, F. (2020). FRaZ: A generic high-fidelity fixed-ratio lossy
compression framework for scientific floating-point data. IPDPS 2020. arXiv:2001.06139.

Quran passages cited: 1:2 (Rabbil 'alamin), 2:42 (truth over falsehood), 5:8 (justice despite hatred),
49:6 (verification mandate), 55:7-9 (the Mizan), 55:31 and 72:1-2 (jinnkind), 67:14 (al-Khabir).



Bismillah ir-Rahman ir-Rahim
