Bismillah ir-Rahman ir-Rahim

The XZ Structural Honesty Audit Corpus: 832 Findings from 31
Rounds of Multi-Model Verification
Version: 1.3
Bilal Syed Arfeen
2026-08-19
Prepared with Claude Opus 4.6 (Anthropic) as analytical and drafting instrument under the author’s direction
and final authority. This paper makes no effectiveness claim about any component of the Structural Honesty
program.
Bismillah ar-Rahman ar-Rahim

Abstract
This paper describes the construction, schema, and content of the XZ Structural Honesty Audit Corpus, a
structured dataset of 832 findings (812 unique finding IDs) extracted from 199 seat reports produced by
independent AI systems from five vendor families (Anthropic, OpenAI, Google, Moonshot, Zhipu), plus one
Perplexity report and one unclassified. Of these, 609 findings are assigned to audit rounds R1 through R31;
the remaining 223 have no extracted round number (predominantly from pre-R7 reports whose filenames did
not encode a round). The corpus covers 64 protocol versions (v0.13 through v0.74, plus legacy v0.2, v0.3,
and v0.8). The primary empirical series – 25 consecutive rounds (R7–R31) with Class A (byte-false claim)
defects present – yields 102 extracted Class A findings across 19 of those 25 rounds; the remaining 6 rounds
(R9–R11, R15, R28–R29) are documented as having Class A present in the verdict record per the companion
synthesis paper but not individually classified in the extracted finding headers. The corpus contains 136
Class A findings in total across all rounds. The construction procedure (an 18-pattern regex extractor with
52 manual verdict overrides, version v0.6) ships with the corpus.

1. Motivation
The XZ Protocol audit program produced a 25-round empirical series. The companion synthesis paper “The
Heartbeat of a Live System” synthesizes the evidence into narrative; this corpus structures it into data,
making the evidence queryable, reproducible, and independently verifiable.
The corpus publishes under the program’s Gate 1 (safety) and Gate 2 (moat) discipline. Gate 1 is satisfied
by construction: findings concern the protocol text’s claims about its own verification properties, not the XZ
Utils backdoor. No payload, activation recipe, or reconstruction detail appears anywhere in the corpus. Gate
2 is satisfied: the corpus is OPEN under the publication posture’s Tier 1.

2. Composition
2.1 Scale
The corpus contains four structured data outputs derived from 199 deduplicated seat reports, plus a fifth
operational log:
• reports.csv – 199 rows, one per unique seat report.
• findings.csv – 832 rows (812 unique finding IDs), one per extracted finding.
• coverage.csv – 199 rows, one per report (keyed on filename; no silent collisions).
• summary.json – aggregate statistics (includes extractor_version field).
• extraction.log – operational log of the extraction run (not a data product).
1

2.2 Temporal span
The corpus covers 31 audit rounds (R1 through R31) and 64 protocol versions, produced between August 1
and August 17, 2026. 90 of 199 reports (45%) and 223 of 832 findings (27%) have no extracted round number,
predominantly from pre-R7 reports whose filenames did not contain a parseable round number.
The reports fall into six eras as classified by the extractor. The classifier assigns era by round number when
present, falling back to version number otherwise; the version ranges below reflect observed values, not
definitional boundaries.
Era

Reports

Observed versions

pre-R7
seat-lineage (R1–R6)
convergence (R7–R8)
mid-program (R9–R14)
CI-era (R15–R20)
mature (R21–R31)
(unclassified)

71
43
24
11
16
32
2

v0.13–v0.36, plus legacy v0.2, v0.3, v0.8
v0.22–v0.47
v0.42–v0.49, plus one v0.71 report
v0.50–v0.55
v0.56–v0.61
v0.27, v0.62–v0.74
–

One report (XZ_v27_SEAT_G_ADVISORY.md, version v0.27, era mature) is tagged R36 by the round extractor.
This is a parsing artifact, not a genuine 36th audit round.
2.3 Model family distribution
Family

Reports

Role

Anthropic (Claude Opus 4.6 / 5)

86

OpenAI (GPT-5.6 Sol)

62

Zhipu (GLM-5.2)

23

Google (Gemini 3.1 Pro)
Moonshot (Kimi K3)

21
5

Perplexity
UNKNOWN

1
1

Producer-family, advisory only,
zero carry weight
Advisory (self-disqualified from
carry at protocol v0.6),
adversarial record
Carrying seat (one of two carrying
families)
Advisory
Carrying seat (one of two carrying
families)
Incidental
Unclassified

2.4 Finding distribution
Severity

Count

Pct

CRITICAL
HIGH
MEDIUM
LOW
INFORMATIONAL
(not extracted)

62
365
232
127
41
5

7.5%
43.9%
27.9%
15.3%
4.9%
0.6%

2

Class

Count

Meaning

Class A
Class B
Class C
Class D
Class E
(not classified)

136
23
11
24
13
625

Byte-false claim in sealed or shipped text
Concealed defect (gate exists, doesn’t cover)
Disclosed standing boundary
Gate limitation
Methodology or governance observation
No class tag in finding header (75%)

Of the 136 Class A findings, 102 are in R7–R31 (the primary empirical series), 24 are in R1–R6, and 10 have
no extracted round number.
2.5 Verdict distribution
Verdict

Count

HALT
CONDITIONAL PASS
PASS
Not extracted

147
22
4
26

Verdict coverage is 87% (173/199). The 26 unextracted verdicts break down by family as: Anthropic 13,
OpenAI 7, Zhipu 4, Moonshot 1, Perplexity 1.

3. Collection process
3.1 Primary sources
The corpus was assembled from three archive files plus two supplementary handoff zips containing the R12
report. Total raw material: 2,082+ files. After deduplication and exclusion, 199 unique seat reports remained.
3.2 Extraction procedure
The construction procedure is extract_corpus.py v0.6, shipped with the corpus. It:
1. Walks configurable archive roots (XZ_CORPUS_ARCHIVE_ROOTS env var) and discovers .md files
via the is_seat_report heuristic. Positive filename signals (REPORT, AUDIT, VERDICT,
RESULT, ADVISORY) are checked first and return immediately if matched; 12 negative signals
(DISPATCH_PROMPT, METHODOLOGY, DISCIPLINE, HANDOFF, CONCEPT, ADJUDICATION_V, TRIAGE, CRYSTALLOGRAPHIC, ORBITAL_AUDIT_METH, QUANTUM_ORBITAL,
PEER_REVIEW_PROMPT, PUBLICATION_REVIEW) are checked only if no positive signal
matches. The manual EXCLUDE_FILES set (6 entries) is load-bearing for files that pass the heuristic but
are not seat reports.
2. Deduplicates by SHA-256 content hash.
3. Extracts report-level metadata using version (3 header patterns + filename fallback), round (3 header
patterns + filename fallback), seat (3 header patterns + 5 filename patterns), family (2 header patterns
+ filename fallback), and verdict (8 patterns + fallback line scan) regex extractors. Applies 52 manual
verdict overrides for reports with prose-embedded verdicts.
4. Extracts per-finding data using 18 regex patterns covering all observed finding-header formats.
5. Validates description fields: bounds all body scans at the next finding header to prevent cross-finding
locus assignment; strips leaked **Locus:** markers (including bullet-prefixed variants), moves locus
content to the locus field, and backfills descriptions from the finding body where possible.
6. Outputs four data files (findings.csv, reports.csv, coverage.csv, summary.json) plus extraction.log.
3

The 18 finding-header patterns, in priority order:
1. Mature bracket: ### F-ID [SEVERITY] [Class X] -- description
2. Mid-era class-first: ### F-ID [Class X] SEVERITY -- description
3. Cross-domain tier: ### F-ID [SEVERITY] [Tier N] -- description
4. Kimi bare-class: ### F-ID [SEVERITY] -- Class X -- description
5. Bracket severity: ### F-ID [SEVERITY] -- description
6. GPT slash-class: ### F-ID -- SEVERITY / Class X
7. GPT paren-class: ### F-ID -- SEVERITY (Class X): description
8. Em-dash severity: ### F-ID -- SEVERITY -- description
9. GLM inline: ### N.N F-ID -- description -- **SEVERITY**
10. Convergence: ### F-ID -- SEVERITY description
11. Numbered early: ### N. Severity - description
12. Bold finding: **F-ID** [SEVERITY] -- description
13. R8 numbered-bold: N. **F-ID -- Class X:** description
14. R16 pipe-bold: **F-ID | SEVERITY (Class X) | description**
15. R17 pipe-hash: ### F-ID | SEVERITY (Class X) | description
16. R12 class-after-dash: ### F-ID -- CLASS X (description)
17. Bare header: ### F-ID (severity on next line)
18. Bare description catch-all: ### F-ID -- description (severity from body)
(Patterns 1–9, 11–13, and 18 accept Unicode U+2013/U+2014 dash classes; patterns 10 and 16 match literal
-- only.)
3.3 What is not in the corpus
The corpus does not contain the protocol text, the executable code, the dispatch packets, the triage records,
the CI outputs, or any XZ Utils payload, activation, or reconstruction content.

4. Annotation schema
Field

Type

Description

finding_id

string

severity

enum

finding_class

enum

tier
description

string
string

locus

string

Identifier in the program’s
namespace. Not unique across
rows: 812 unique IDs across 832
rows. 20 duplicate IDs exist,
comprising content-identical
double-extractions from
byte-different report copies and
namespace collisions across
reports.
CRITICAL, HIGH, MEDIUM,
LOW, INFORMATIONAL (5
rows unextracted)
Class A through E (625 rows
unclassified – 75%)
Tier 1/2/3 (sparse)
First-line description (40 rows
empty after validation)
Where in the artifact (81%
populated)

4

Field

Type

Description

round_number

int or empty

version
seat_id
model_family
family_normalized
report_file

string
string
string
string
string

Audit round, 1–31 (27% empty;
one report-level R36 parsing
artifact; see Section 2.2)
Protocol version under audit
Seat identifier
Model name as reported
Vendor family
Source report filename

5. Known limitations
1. Class A extraction coverage. 19 of 25 R7–R31 rounds have extracted Class A findings (102 total).
The 6 rounds without (R9–R11, R15, R28–R29) have Class A documented in the verdict record per the
Heartbeat paper (ASSERTED, not COMPUTED from this corpus’s structured data). Some of those
rounds contain findings whose descriptions reference Class A in prose but whose headers lack the class
tag in formats the extractor captures.
2. Unclassified findings. 625 of 832 (75%) carry no class tag.
3. Carrying-seat underrepresentation. 28 reports (14%) from the two carrying families.
4. Verdict coverage. 26 of 199 reports (13%) have no extracted verdict (Anthropic 13, OpenAI 7, Zhipu
4, Moonshot 1, Perplexity 1).
5. Locus extraction. 81% of findings have a locus field.
6. No disposition chains.
7. Empty round fields. 90 reports (45%) and 223 findings (27%) have no extracted round number. 6
reports and 4 findings have no extracted version.
8. Duplicate finding IDs. 20 IDs appear in more than one row, comprising content-identical doubleextractions and namespace collisions across reports.
9. R36 parsing artifact. One report (XZ_v27_SEAT_G_ADVISORY.md, v0.27) is tagged R36 by the round
extractor.
10. Description quality. 40 of 832 findings (5%) have empty descriptions after validation.

6. Uses
6.1 Intended uses
• Reproducing the Heartbeat paper’s empirical claims against the structured data.
• Studying multi-model verification dynamics across five vendor families.
• Studying defect migration across the round-over-round structure.
• Methodology research on the format evolution of AI-generated audit reports.
6.2 Out of scope
• Training data for code generation or vulnerability detection.
• Evaluating AI model capabilities.

5

7. Distribution
The corpus publishes as a Zenodo deposit under CC-BY-4.0. The deposit contains:
• findings.csv, reports.csv, coverage.csv, summary.json – the four data products
• extract_corpus.py v0.6 – construction procedure
• PACKET_SHA256SUMS.txt – SHA-256 digests of all shipped files
• This paper (dataset card)
Program chain DOIs: AX-SH5 Flagship 10.5281/zenodo.21500700; SHUDP 10.5281/zenodo.21522932;
SHVVP 10.5281/zenodo.21583202; BSSG 10.5281/zenodo.21713180; BAF 10.5281/zenodo.20017335; PMD
10.5281/zenodo.21462879; SHV Method 10.5281/zenodo.21449063.

8. Maintenance
The corpus is a snapshot as of v0.75 FROZEN (2026-08-17). The extractor version (v0.6) is recorded in the
extractor_version field of summary.json. The extractor requires the source archives (not in the deposit)
and accepts configurable roots via XZ_CORPUS_ARCHIVE_ROOTS.

Appendix A: Construction verification
1. Re-running extract_corpus.py on the same archives (available in the program’s handoff records) and
comparing output hashes.
2. Spot-checking any finding row against its source report (report_file field).
3. Checking the 52 manual verdict overrides against the cited prose passages.
Bilal Syed Arfeen Bayyinah Structural Honesty Validation Program – August 2026
“Indeed, We sent down the reminder, and indeed, We will be its preserver.” (Qur’an 15:9)

6



Bismillah ir-Rahman ir-Rahim
