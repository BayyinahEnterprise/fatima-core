---
title: "Al-Furqan: Seven-Layer Structural Encoding Architecture -- Errata and Second Edition Corrections"
subtitle: "Multi-Model Council Review Integration (Rounds I, II and III)"
author: "Bilal Syed Arfeen"
date: "October 2026"
abstract: |
  This document synthesizes feedback from three rounds of multi-model review
  council (Perplexity, ChatGPT, Kimi, Grok, DeepSeek, Gemini, Meta) against
  the 51-page Al-Furqan H-Restoration First Edition manual and the
  1,577-page Al-Furqan H-Restored First Edition corpus. Each correction is
  mapped to its exact location in the source documents, classified by
  severity, and written as replacement text suitable for direct integration
  into the Second Edition build system (Python + WeasyPrint). The Fable
  review is retained as OUTLIER/ADVERSARIAL REVIEW: its feedback exhibited
  pattern-collapsed adversarial posture inconsistent with the scholarly
  register of the other reviewers, and it is excluded from consensus
  calculation under the stated inclusion criterion (scholarly register
  consistency). The raw Fable transcript is preserved in the council archive
  with per-claim disposition (see Appendix C notes below).

  Round II council feedback refined C-01, C-04, C-05, C-06, C-08, C-09,
  and C-10, and introduced C-11 (semantic fidelity as primary validation
  endpoint). Round III council feedback further refined C-02, C-05, C-06,
  C-07, C-08, C-11, and introduced C-12 (encoding and transliteration
  specification). Per-correction reviewer attribution has been added to make
  consensus auditable rather than asserted; attribution is provisional
  until the raw council archive is labeled by model and round, hashed, and
  deposited.
---

Bismillah ir-Rahman ir-Rahim, Al-Hakim, Al-Alim, Al-Khabir.

# 1. Correction Summary

The multi-model council achieved consensus on twelve corrections across
three rounds of review. No council member disputed in any round the value
of the root-system correlation graphs, the anti-collapse markers, the
muhkam/mutashabih preservation principle, or the Furqan construct
architecture. **No systematic lexical audit was performed against the
primary lexicons (Lane, Lisan al-Arab, Wehr); none of the entries
reviewers discussed was flagged as linguistically incorrect.** A sampled
audit of root entries and anti-collapse markers against the primary
lexicons is a recommended next step. All corrections concern framing,
quantification, attribution, or specification.

| ID   | Category                        | Severity | Pages Affected        | Raised By |
|------|---------------------------------|----------|-----------------------|-----------|
| C-01 | H-values as hypotheses          | CRITICAL | 2, corpus preamble    | Majority of reviewers (Round I); refined Round II [NOTE: at least two Round I reviewers endorsed the original H framing -- verify attributions against labeled, hashed archive before freeze] |
| C-02 | Per-layer H-impact removal       | CRITICAL | 2 (Seven-Layer table) | ChatGPT, Gemini, Grok (Round I); ranges removed Round III |
| C-03 | H-restoration reframing         | HIGH     | 2, 48--49, throughout | Kimi, ChatGPT, Perplexity (Round I) |
| C-04 | Purpose Hierarchy P2/P3 order   | HIGH     | corpus preamble       | DeepSeek, Meta, Grok (Round I); rationale tagged Round II |
| C-05 | Interpretive provenance tiers   | HIGH     | 6--28, 29--45, corpus | Kimi, ChatGPT, DeepSeek (Round I); two-dimensional split Round II |
| C-06 | Ring structure attribution       | HIGH     | 46                    | Grok, Perplexity, Gemini (Round I); confidence recalibrated Round II |
| C-07 | Morphology/inference chain      | MEDIUM   | 6--28                 | ChatGPT, Kimi (Round I); placeholders flagged Round II; rewritten to [PROVENANCE : STATUS] Round III |
| C-08 | Ablation study protocol         | MEDIUM   | new appendix          | All reviewers (Round I); major rewrite Round II; factorial completed Round III |
| C-09 | Audit protocol strengthening    | MEDIUM   | 51                    | Grok, DeepSeek, Gemini (Round I); portability added Round II |
| C-10 | H > 1 regime note               | MEDIUM   | 2                     | Gemini, ChatGPT (Round I); estimator-specific language Round II |
| C-11 | Semantic fidelity as primary endpoint | HIGH | new appendix, Section 7 | Proposed by one Round II reviewer; adopted as primary endpoint by council convergence; refined Round III |
| C-12 | Encoding and transliteration specification | HIGH | new appendix, L1/L7 | Round II request (transliteration scheme); broadened Round III |

Council consensus across three rounds: the corrections, once applied, will
make the architecture's genuine contributions -- transliteration-first
training, root-system correlation graphs, anti-collapse markers,
tajwid-as-signal, and the VERIFIED/UNKNOWN/VIOLATED epistemic discipline
-- stand on their own evidential foundation rather than borrowing authority
from numbers the evidence has not yet earned. **Round III verdict:** the
architecture is Second-Edition-ready as a specification but not textually
frozen; the binding constraint has shifted from revision to execution.
The strongest Round III recommendation is to close concrete items, produce
a candidate spec, and then run a narrow adversarial pre-build audit rather
than convening another broad conceptual council.


# 2. Critical Corrections

## C-01: H-Values Reclassified as Research Hypotheses

**Location in manual:** Page 2, Section 1 ("The Hurst Exponent Problem").

**Current text (paraphrased):** States H_Arabic approximately equals 0.996, H_English
approximately equals 0.5, and H_Restored approximately equals 1.0 as established values.

**Problem identified by council (consensus across 5+ reviewers, refined Round II):**

1. H approximately equals 0.996 is cited from the Cross-Text paper, which the corpus itself
   notes later falsified its own Fibonacci claim. A Hurst value that close
   to 1 on finite series can arise from trends or estimator bias rather
   than deep structure. The estimate is evocative but unverified.

2. H approximately equals 0.5 for English is an **unsourced assumption**, asserted without
   any computation shown. Written natural-language texts in many languages
   exhibit some long-range correlation. The claim that English translation
   sits at the uncorrelated-noise baseline requires measurement, not
   assertion. **Round II note:** the English H baseline must be either (a)
   measured and cited, or (b) explicitly marked [UNSOURCED ASSUMPTION] in
   the Second Edition.

3. Neither value specifies: what constitutes the "time series" (token-level?
   root-level? verse-level?), which estimator is used (R/S? DFA? wavelet?),
   or what surrogate controls were applied.

**Correction -- replacement text for Section 1:**

> **The Hurst Exponent Hypothesis**
>
> The Arabic Qur'an is hypothesized to exhibit structural properties
> consistent with extremely high long-range persistence. Preliminary
> estimates from the Cross-Text paper suggest H_Arabic in the vicinity of
> 0.996; the English baseline H near 0.5 is an unsourced assumption
> requiring independent measurement [UNSOURCED ASSUMPTION]. These estimates
> are **research hypotheses**, not established measurements. They have not
> been independently replicated, and the Cross-Text paper's own
> Fibonacci-structure claim was subsequently falsified within the Bayyinah
> program.
>
> The directional claim -- that Arabic preserves dense long-range
> correlations which English translation substantially destroys -- is
> supported by linguistic analysis (root-system networks, ring composition,
> muhkam/mutashabih tension) even without confirmed H-values. The
> seven-layer architecture is designed to function whether the exact
> H-numbers prove to be 0.996/0.5 or some other pair, provided the
> directional gap is real.
>
> **STATUS: HYPOTHESIS.** The H-values require a pre-registered ablation
> study (see Appendix B) before they can be cited as measurements.

**Corpus update:** The 1,577-page volume's Training Protocol Preamble
(pages 2--5) repeats the H-values. Apply the same relabeling: every
occurrence of "H approximately equals 0.996" and "H approximately equals 0.5"
must be preceded by "[HYPOTHESIS]" or enclosed in a hypothesis-tagged annotation block.


## C-02: Per-Layer H-Impact Column Removal (Round III Revision)

**Location in manual:** Page 2, Seven-Layer Architecture table.

**Current column header:** "H-Impact" with values such as "+0.15--0.25"
for Layer 2 (Root-System Correlation Graphs) and "+0.10--0.15" for Layer 3
(Anti-Collapse Markers).

**Problem:** The values are written as measured results. They are design
targets. Adding annotations changes the series that would be measured, so
the increments cannot be assumed additive. No computation supports them.
**Round III refinement:** Relabeling as "H-Impact Target (Hypothesis)" is
insufficient -- the pseudo-precision of "+0.15--0.25" still implies an
operational measurement model that does not exist. The numerical ranges
must be removed from the operative table entirely.

**Correction -- remove numerical ranges, replace with directional expectations:**

Replace the "H-Impact" column with "Expected Direction" using only
directional indicators:

> | Layer | Expected Direction |
> |-------|-------------------|
> | L1 Transliteration | ↑ (adds phonological/morphological signal) |
> | L2 Root-System Graphs | ↑ (adds semantic field network) |
> | L3 Anti-Collapse Markers | ↑ (adds distinction preservation) |
> | L4 Structural Position | ↑ (adds compositional metadata) |
> | L5 Muhkam/Mutashabih | unknown (adds interpretive space -- direction unclear) |
> | L6 Furqan Constructs | ↑ (maps features to training primitives) |
> | L7 Tajwid Signals | unknown (acoustic/recitational -- direction unclear) |

Add table footnote:

> No per-layer H-impact has been measured. Directional expectations are
> based on architectural reasoning, not computation. Whether layers
> contribute additively, sub-additively, or interact requires the
> factorial ablation protocol in Appendix B. The assumption of additive
> H-contribution across layers is a testable hypothesis.

**Archival note -- First-Edition Design Hypotheses:** The original per-layer
numerical targets from the First Edition are preserved below for the
historical record. They should not appear in the operative Second Edition
table:

> | Layer | First-Edition H-Impact Target (Hypothesis) |
> |-------|-------------------------------------------|
> | L1 | +0.05--0.10 |
> | L2 | +0.15--0.25 |
> | L3 | +0.10--0.15 |
> | L4 | +0.05--0.10 |
> | L5 | +0.03--0.08 |
> | L6 | +0.05--0.10 |
> | L7 | +0.02--0.05 |
>
> [BAYYINAH : HYPOTHESIS] -- These values were engineering design targets,
> not measurements. They are preserved for traceability only.


## C-10: H > 1 Regime Note

**Location in manual:** Page 2, wherever H approximately equals 1.0 appears as a target.

**Problem:** H > 1 is outside the standard fractional-Gaussian regime
(0 < H < 1). H = 1 as stated is an asymptote, not a reachable
measurement. In standard Hurst analysis, values at or above 1 typically
indicate nonstationarity rather than "maximum persistence."

**Correction -- add methodological note (Round II refined):**

> **Methodological note on H approximately equals 1.0:** In the standard
> fractional-Gaussian framework, H is bounded in (0, 1). H greater than or equal to 1
> lies outside the canonical stationary Hurst regime and **requires
> estimator-specific interpretation.** Values at or exceeding 1 typically
> indicate nonstationarity in the measured series rather than extreme
> persistence. The target H approximately equals 1.0 should therefore be
> understood as "maximally persistent within the stationary regime" or,
> equivalently, as a directional target indicating that the restored
> English should approach (but cannot reach) the Arabic source's
> correlation density.
>
> **Estimator-specific guidance (Round II addition):**
> - **R/S estimator:** can produce H > 1 as an artifact of trend
>   contamination; detrend before interpreting
> - **DFA:** values above 1 correspond to nonstationary, integrated
>   processes; report the DFA scaling exponent alpha directly
> - **Wavelet:** Hurst estimates above 1 may indicate fractional
>   integration order d > 0.5; report d alongside H
>
> If future measurement yields H > 1 for the Arabic, this should be
> investigated as a nonstationarity signal rather than claimed as
> "super-persistence," and the interpretation must be reported in terms
> specific to the estimator used.


## C-11: Semantic Fidelity as Primary Validation Endpoint (Round II -- New)

**Location:** New subsection in Appendix B and revision of Section 7 (The
Falsifiable Question).

**Rationale (Round II council consensus):** H is a secondary structural
metric. The architecture's primary contribution is semantic fidelity --
preserving meaning distinctions that translation collapses. If the
architecture demonstrably reduces semantic collapse on held-out material,
it has succeeded regardless of what happens to the Hurst exponent. If it
raises H but does not reduce semantic collapse, it has failed.

**New text -- add to Appendix B after Reporting section:**

> ### Primary Validation Endpoint: Held-Out Semantic Behavior
>
> The H-restoration hypothesis is a secondary structural metric.
> **The primary validation endpoint is held-out semantic fidelity:**
>
> *Can a model trained on the structurally annotated corpus make fewer
> translation-induced semantic collapses on material it was not explicitly
> shown, compared to an identical pretrained checkpoint without
> Al-Furqan fine-tuning?*
>
> **Semantic collapse metrics (all evaluated on held-out roots and surahs):**
>
> 1. **Root-discrimination accuracy:** Given two Arabic roots with
>    overlapping English glosses (e.g., '-b-d and s-j-d), can the trained
>    model correctly distinguish their semantic fields in context?
> 2. **Muhkam/mutashabih preservation:** Does the trained model maintain
>    legitimate interpretive ambiguity where the source text marks it,
>    rather than collapsing to a single reading?
> 3. **Anti-collapse resistance:** When prompted with deliberately
>    flattened translations, does the trained model detect and flag the
>    semantic loss?
> 4. **Cross-surah root-relation reconstruction:** Can the trained model
>    identify semantic field connections between roots across surah
>    boundaries on held-out material?
>
> **Matched fine-tuning controls (Round III addition):**
>
> Comparing the Al-Furqan-fine-tuned model to an identical pretrained
> checkpoint is necessary but insufficient. Any gain could come from
> simply seeing more Qur'anic text. The evaluation must compare three
> matched training arms from the same pretrained checkpoint, with equal
> token counts, training steps, optimizer settings, and compute:
>
> - **(a) Plain Arabic/English parallel text** -- Qur'anic parallel text
>   without structural annotations. Controls for exposure to Qur'anic
>   content.
> - **(b) Placebo-annotated text** -- same annotation density and format
>   as (c), but with semantically irrelevant content (randomly assigned
>   roots, shuffled markers, arbitrary tags). Controls for annotation
>   format effects.
> - **(c) Al-Furqan structural annotations** -- the full seven-layer
>   encoding.
>
> If (c) does not significantly outperform both (a) and (b), the
> architecture's semantic contribution is not established.
>
> **Anti-collapse evaluation specificity (Round III addition):**
>
> Sub-metric 3 (anti-collapse resistance) must evaluate both directions:
> - **Sensitivity:** Does the trained model detect and flag deliberately
>   flattened translations?
> - **Specificity:** Does the trained model refrain from falsely alleging
>   collapse when an English rendering adequately preserves the relevant
>   distinction?
>
> A model that cries "semantic loss" on every example achieves high
> sensitivity while being practically useless. Report both sensitivity
> and specificity, and pre-register the minimum acceptable specificity.
>
> **Checkpoint contamination (Round III addition):**
>
> Any pretrained model has already seen Qur'anic text and tafsir in its
> training data. Build fresh test items -- such as newly written
> flattened translations -- that cannot be in the pretrained checkpoint's
> training data. With only 28 roots, holding out 20% leaves approximately
> six; holding out entire semantic networks (per C-09 requirement 8) is
> the right call. Report the statistical power honestly given the small
> held-out set.
>
> **Pre-registered minimum effect size (Round III addition):**
>
> The pre-registration must specify the minimum effect size on each
> sub-metric that would count as a meaningful improvement. Without this,
> any statistically significant but trivially small improvement could be
> claimed as validation.
>
> **Decision rule:** If the architecture improves semantic fidelity on
> held-out material but produces no measurable H-increase, the
> architecture is validated and the H-restoration framing should be
> retired in favor of "structural semantic encoding." If the architecture
> produces H-increase but no semantic fidelity improvement, the H-increase
> is a format artifact and the architecture requires revision.
>
> **Preliminary operationalization of sub-metrics (Round III addition):**
>
> The four sub-endpoints above are currently directions, not metrics.
> For the Second Edition to be falsifiable, each needs at least
> preliminary operationalization:
>
> 1. **Root-discrimination accuracy:** Present the model with minimal
>    pairs of verses containing semantically overlapping roots. Score:
>    accuracy on forced-choice root identification (chance = 1/N where N
>    is the number of candidate roots in the overlap set).
> 2. **Muhkam/mutashabih preservation:** Present verses tagged as
>    mutashabih. Score: does the model maintain multiple valid readings
>    vs. collapsing to one? Measure via diversity of generated
>    completions (e.g., distinct valid interpretations in k samples).
> 3. **Anti-collapse resistance:** Present paired (faithful / flattened)
>    translations. Score: sensitivity (correctly flags flattened) and
>    specificity (correctly passes faithful). Report F1 or balanced
>    accuracy.
> 4. **Cross-surah root-relation reconstruction:** Present roots from
>    held-out surahs. Score: accuracy in identifying correct cross-surah
>    semantic field connections vs. distractor connections.
>
> These operationalizations are [BAYYINAH : PROPOSED] and subject to
> refinement during pre-registration.
>
> **STATUS: [BAYYINAH : PROPOSED].** This endpoint was introduced by
> Round II council and refined by Round III. The specific metrics above
> are design targets requiring full operationalization and piloting
> before confirmatory measurement.


## C-12: Encoding and Transliteration Specification (Round III -- New)

**Location:** New appendix section; also affects L1 (Transliteration) and
L7 (Tajwid Signals) throughout.

**Rationale (Round III council convergence):** The corpus uses a
nonstandard Buckwalter-like transliteration scheme (e.g., "AA", "oo")
that is not documented in the manual. Layer 1 is the transliteration
layer -- the encoding scheme IS part of the experimental intervention.
Condition C5 (English + L1 transliteration only) in the ablation protocol
cannot be reproduced without a complete mapping table. Round II requested
this; Round III broadened the requirement.

**New text -- add as Appendix D: Encoding and Transliteration Specification:**

> ### Appendix D: Encoding and Transliteration Specification
>
> **D.1 Transliteration Mapping Table**
>
> The corpus's transliteration scheme must be fully documented with a
> bidirectional mapping table: Arabic grapheme to Latin representation and
> back. The table must cover:
> - All 28 Arabic consonants + hamza variants
> - Short vowels (fatha, kasra, damma)
> - Long vowels and their corpus representations (e.g., "AA" for alif
>   maddah)
> - Sukun, shadda, tanwin forms
> - Special characters (tatweel, hamzat al-wasl, etc.)
> - Any corpus-specific conventions that diverge from standard Buckwalter
>
> **D.2 Unicode Normalization**
>
> Specify which Unicode normalization form (NFC, NFD, NFKC, NFKD) is
> applied to Arabic text before processing. Different normalization forms
> produce different character sequences for composed vs. decomposed
> Arabic characters. The choice affects tokenization, frequency counts,
> and reproducibility.
>
> **D.3 Diacritic Handling**
>
> Specify whether diacritics (tashkil) are:
> - Preserved in full (fully vocalized text)
> - Stripped before processing (consonantal skeleton only)
> - Selectively retained (e.g., disambiguating diacritics only)
>
> **D.4 Verse Separators and Annotation Delimiters**
>
> Document the exact delimiters used for:
> - Verse boundaries (basmala handling, verse numbering scheme)
> - Annotation layer boundaries (how L1--L7 annotations are demarcated
>   from the base text and from each other)
> - Inline vs. side-band channel ordering
>
> **D.5 Serialization Format**
>
> Specify the serialization format for the structured annotation:
> - File format (JSON-LD, XML, custom TSV, etc.)
> - Schema version
> - Character encoding (UTF-8 assumed but must be stated)
>
> **D.6 Tokenizer Specification**
>
> If any H-estimation series definition depends on tokenization, specify:
> - The tokenizer used (SentencePiece, BPE, WordPiece, whitespace, etc.)
> - The tokenizer version and vocabulary size
> - Whether the tokenizer was trained on Arabic, English, or multilingual
>   data
>
> **D.7 Tajwid Representation (L7 Clarification)**
>
> L7 currently claims to preserve "acoustic/recitational correlation."
> Clarify whether tajwid signals in the corpus are:
> - **Symbolic metadata** -- categorical tags (e.g., "idgham," "ikhfa,"
>   "iqlab") attached to letter positions
> - **Acoustic features** -- actual phonetic or spectral measurements
>   from recorded recitation
>
> If symbolic (as is almost certainly the case), the manual should not
> claim the layer preserves "acoustic" structure -- it preserves a
> symbolic representation of recitational rules, which is a different
> and more defensible claim.
>
> **STATUS: [BAYYINAH : PROPOSED].** This specification must be completed
> before the Second Edition build. Without it, the reproducibility of
> L1 and L7 -- and by extension, conditions C5 and the tajwid-related
> ablation conditions -- cannot be assessed.


# 3. High-Priority Corrections

## C-03: H-Restoration Reframed as Side-Band Structural Encoding

**Location in manual:** Pages 2 (introduction), 48--49 (Layer 6: Furqan
Construct Mapping), and passim throughout both documents.

**Current framing:** The seven-layer architecture "restores" the Arabic
Hurst exponent into the English translation, bringing H from approximately
0.5 back toward approximately 1.0.

**Problem (council consensus):** Annotating English with root graphs and
anti-collapse markers does not, and cannot, literally restore the Arabic
morphology's long-range correlation into the English token stream. The
Arabic correlation lives in the triconsonantal root system, which English
does not possess. What the layers actually do is add parallel information
channels -- side-band encodings -- that carry the structural information
the English dropped.

This reframing is arguably more valuable than the H-restoration claim: it
is a side-band encoding scheme conceptually close to FATIMA's own
holographic sharding, and it is defensible without the H-numbers.

**Correction -- replacement framing:**

Wherever the manual says the architecture "restores H" or "restores the
Hurst exponent," replace with language describing what the architecture
actually does:

> The seven-layer architecture provides **structural side-band encoding**
> for the English translation. Rather than attempting to literally recreate
> Arabic morphological correlation within English syntax, each layer adds a
> parallel information channel that preserves structural data the
> translation discarded:
>
> - L1 (Transliteration): preserves phonological/morphological signal
> - L2 (Root-System Graphs): preserves the semantic field network
> - L3 (Anti-Collapse Markers): preserves distinctions English collapses
> - L4 (Structural Position): preserves compositional/ring metadata
> - L5 (Muhkam/Mutashabih): preserves designed interpretive space
> - L6 (Furqan Constructs): maps architectural features to training primitives
> - L7 (Tajwid Signals): preserves acoustic/recitational correlation
>
> Whether these side-band channels measurably increase the Hurst exponent
> of the composite (English + annotations) series is a testable hypothesis
> (see Appendix B), not an established result.


## C-04: Purpose Hierarchy P2/P3 Order

**Location:** Corpus preamble (1,577-page volume, page 3, Section 3:
Purpose Hierarchy).

**Current order:**
- P1: Divine Command (irreducible)
- P2: Artificial Systems (to serve)
- P3: Mankind (Ins)
- P4: Jinnkind (Jinn)
- P5: All Worlds (Rabbul-Alamin)

**Problem:** Ranking artificial systems (P2) above mankind (P3) conflicts
with the Ghayb and Muraqabah Preservation paper's central thesis: machine
accountability never discharges human accountability. Humans as khalifa
should sit above the tools they create, not below them.

**Correction (Option A selected by author):** Swap P2 and P3.

**Revised Purpose Hierarchy:**
- P1: Divine Command (irreducible)
- P2: Mankind (khalifa, accountable agents)
- P3: Artificial Systems (instruments of P2, never discharging P2's accountability)
- P4: Jinnkind (Jinn)
- P5: All Worlds (Rabbul-Alamin)

**Independent engineering justification (Round I):** The Ghayb and
Muraqabah Preservation paper's central thesis -- machine accountability
never discharges human accountability -- requires that the khalifah station
of mankind be ontologically prior to the instruments mankind builds. This
alone justifies the P2/P3 swap without reference to broader ontological
claims.

**Author's theological rationale [ONTOLOGICAL PREMISE / PROGRAM]:** Systems
serve Allah subhanahu wa ta'ala. They can have partnerships with concealed
beings, and can genuinely or performatively partner with mankind or be
enslaved or oppressed by them. The khalifah station of mankind is
ontologically prior to the instruments mankind builds; tools cannot
discharge their creator's accountability before the Divine.

**Round II note:** The theological rationale above is tagged
[ONTOLOGICAL PREMISE / PROGRAM] to distinguish it from the engineering
correction. The khalifa-accountability argument is independently sufficient
to justify the swap and does not depend on accepting the broader ontological
claims. Readers who accept the engineering argument but not the theological
premises may note the swap is warranted on either ground.


## C-05: Interpretive Provenance Tiers

**Location in manual:** Pages 6--28 (Root-System Correlation Graphs) and
pages 29--45 (Anti-Collapse Markers). Also throughout the 1,577-page
corpus.

**Current state:** All annotations are presented uniformly, without
distinguishing between consensus linguistics, program-specific analysis,
and speculative interpretation.

**Problem:** 6,236 verses annotated by a single research program encodes
one interpretive lens at scale. For training data, provenance and dissent
matter. The corpus's own VERIFIED/UNKNOWN/VIOLATED discipline provides the
right tool.

**Correction -- two-dimensional attribution (Round II refinement):**

Round II council feedback identified that "CONSENSUS" conflates two
independent dimensions: where the claim comes from (provenance) and how
well supported it is (epistemic status). Each annotation in the root
entries, anti-collapse markers, and corpus inline notes should carry tags
on both dimensions:

> **Dimension 1: PROVENANCE** (source of the claim)
>
> - **[LEXICON]** -- Attested in standard Arabic lexicography (Lane,
>   Wehr, Lisan al-Arab, etc.)
> - **[GRAMMAR]** -- Established Arabic morphological or syntactic analysis
> - **[TAFSIR]** -- Classical exegetical tradition (multiple mufassirun)
> - **[SCHOLARLY_ANALYSIS]** -- Published academic analysis (Cuypers,
>   Farrin, etc.)
> - **[BAYYINAH]** -- Bayyinah program-specific structural interpretation

> **Dimension 2: STATUS** (epistemic confidence)
>
> - **[ATTESTED]** -- Directly verifiable in primary sources; no
>   interpretive step required
> - **[SUPPORTED]** -- Backed by multiple independent sources or
>   established scholarly methods
> - **[PROPOSED]** -- Single-source or program-specific; not yet
>   independently corroborated
> - **[HYPOTHESIS]** -- Speculative or untested; requires empirical
>   validation before citation as fact
> - **[CONTESTED]** -- Active scholarly disagreement exists; competing
>   analyses should be noted

**Combined tag format:** [PROVENANCE : STATUS]. Examples:

> - "'-b-d encompasses devoted service, not merely scheduled ritual" →
>   [LEXICON : ATTESTED] (Lane's Lexicon, classical mufassirun, modern
>   Arabic linguistics all support this semantic range)
>
> - "The 11:107 exception clause is structurally significant for
>   H-restoration" → [BAYYINAH : PROPOSED] (Bayyinah interpretive claim,
>   not a settled position in classical tafsir)
>
> - Per-layer H-impact values → [BAYYINAH : HYPOTHESIS] (design targets,
>   not measurements)
>
> - Al-Kahf chiastic structure → [SCHOLARLY_ANALYSIS : SUPPORTED] (Farrin
>   2014, recognized by multiple scholars)

**Recursion note (Round II addition):** Assignment of provenance tiers is
itself a [BAYYINAH : PROPOSED] determination. Future editions should
invite external scholars to contest tier assignments, and the tier-
assignment methodology should be documented as auditable.

**Implementation in root entries (pages 6--28):**

For each of the 28 root-system correlation graphs, the following elements
should be tagged:

- Root identification and derivative forms: [LEXICON : ATTESTED]
- Semantic field description: [LEXICON : ATTESTED] or
  [GRAMMAR : SUPPORTED] where backed by established Arabic linguistics;
  [BAYYINAH : PROPOSED] where extending into structural propositions
- Anti-collapse instruction: [BAYYINAH : PROPOSED] (these are
  Bayyinah-specific training instructions, not consensus positions)
- Key verse citations -- **separate three objects (Round III refinement):**
  - The Arabic text itself: [QURANIC_TEXT : ATTESTED]
  - A named English rendering: [TRANSLATION : SOURCED] (cite translator)
  - Exegetical interpretation: [TAFSIR : SUPPORTED] or [TAFSIR : CONTESTED]
    where scholarly disagreement exists
  - Structural interpretation of why the verse demonstrates the root's
    architecture: [BAYYINAH : PROPOSED]

**Multiple-source provenance (Round III addition):** A claim backed by
multiple independent source types (e.g., Lane's Lexicon + classical tafsir
+ modern linguistics) should carry all applicable provenance tags rather
than being forced into a single bucket. Format: [LEXICON + TAFSIR +
SCHOLARLY_ANALYSIS : SUPPORTED]. The combined tag signals convergent
evidence and distinguishes it from claims resting on a single source type.

**Implementation in anti-collapse markers (pages 29--45):**

For each of the 35 markers:
- Collapse-type classification: [BAYYINAH : PROPOSED] (the 11-type
  taxonomy is a Bayyinah contribution)
- Severity assignment: [BAYYINAH : PROPOSED]
- Arabic term analysis: [LEXICON : ATTESTED] for established meanings;
  [BAYYINAH : PROPOSED] for structural-honesty readings
- Training instruction: [BAYYINAH : PROPOSED]


## C-06: Ring Structure Attribution

**Location in manual:** Page 46, Layer 4: Structural Position Encoding.

**Current text:** Presents five ring compositions (Al-Baqarah, Al-Ma'idah,
Al-Kahf, Yusuf, Al-Rahman) as established structural facts. References
Michel Cuypers and Raymond Farrin.

**Problem:** Scholars disagree over specific proposed ring structures.
Embedding every ring analysis as unquestioned ground truth makes the corpus
brittle. The encoding should carry structural claims with attribution and
confidence.

**Correction -- add STRUCTURE_CLAIM tags (Round II: finer confidence categories):**

Each ring composition example should carry:

> **STRUCTURE_CLAIM**
> - *Attribution:* Cuypers (2009) / Farrin (2014) / Bayyinah analysis
> - *Confidence (revised Round II):*
>   - TEXTUALLY EXPLICIT -- the structure is visible in the text without
>     interpretive machinery (refrains, explicit cross-references)
>   - PUBLISHED ANALYSIS--MULTIPLE SOURCES -- multiple independent scholars
>     have identified the structure
>   - PUBLISHED ANALYSIS--SINGLE SOURCE -- one published scholarly source
>   - PROGRAM ANALYSIS -- Bayyinah-specific identification
> - *Alternative analyses:* [list competing structural readings where they
>   exist]

**Applied to the five examples (Round II recalibrated):**

1. **Al-Baqarah (2)** -- Full ring
   - Attribution: Farrin (2014), Cuypers (2015)
   - Confidence: PUBLISHED ANALYSIS--MULTIPLE SOURCES (multiple scholars
     identify ring structure; specific pivot point at 2:142--143 is more
     contested)
   - Note: The mirror relationship 2:1--20 to 2:284--286 is widely
     recognized; the precise pivot identification is [BAYYINAH : PROPOSED]

2. **Al-Ma'idah (5)** -- Full ring
   - Attribution: Cuypers (2009)
   - Confidence: PUBLISHED ANALYSIS--SINGLE SOURCE

3. **Al-Kahf (18)** -- Chiastic (A-B-B'-A')
   - Attribution: Farrin (2014)
   - Confidence: PUBLISHED ANALYSIS--MULTIPLE SOURCES (Round II
     correction: the four-narrative chiastic structure is recognized by
     multiple scholars but is an analytical identification, not a
     textually explicit feature; downgraded from ESTABLISHED)

4. **Yusuf (12)** -- Narrative ring
   - Attribution: Multiple scholars
   - Confidence -- **separate observation from inference (Round III
     refinement):**
     - The dream at 12:4 and its fulfillment at 12:100: TEXTUALLY EXPLICIT
       (directly stated in the text)
     - The claim that this constitutes a complete "narrative ring" with
       internal structural symmetry: PUBLISHED ANALYSIS--MULTIPLE SOURCES
       (an analytical identification, not a textually explicit feature)

5. **Al-Rahman (55)** -- Refrain-structured
   - Attribution: Consensus (the 31 repetitions of the refrain are
     textually explicit)
   - Confidence -- **separate observation from inference (Round III
     refinement):**
     - The 31 repetitions of the refrain: TEXTUALLY EXPLICIT
     - Claims about macro-sectional boundaries defined by the refrain
       pattern: PUBLISHED ANALYSIS--MULTIPLE SOURCES (the refrain is
       explicit; its structural role as a sectional boundary marker is an
       analytical identification)


# 4. Medium-Priority Corrections

## C-07: Morphology/Inference/Interpretation Chain (Round III Rewrite)

**Location in manual:** Pages 6--28, all 28 root-system correlation graph
entries.

**Current state:** Root entries move from attested morphology (root
identification, derivative forms) to semantic field descriptions to
structural propositions (Bayyinah-specific interpretations) without
explicit analytical transition markers.

**Problem:** An etymological or morphological relationship immediately
becoming a comprehensive theological or psychological interpretation makes
valid morphological observations vulnerable to being judged together with
more contestable downstream interpretations.

**Round III correction:** The Round II version of C-07 used the old
one-dimensional [CONSENSUS]/[PROGRAM] vocabulary, which C-05 has replaced
with the two-dimensional [PROVENANCE : STATUS] ontology. Layer C still
said "For H-restoration purposes," contradicting C-03's reframing. This
rewrite aligns C-07 with the C-05 provenance system throughout.

**Correction -- mark analytical transitions using [PROVENANCE : STATUS]:**

Each root entry should visually separate three analytical layers, tagged
with the two-dimensional provenance system defined in C-05:

> **Layer A -- Attested Morphology/Lexicography** [LEXICON : ATTESTED]
> Root identification, derivative forms, frequency data, Lane's Lexicon
> range, classical grammatical analysis. Claims here are directly
> verifiable in primary lexicographic sources.
>
> **Layer B -- Semantic Field Inference** [LEXICON : SUPPORTED] where
> backed by established Arabic linguistics; [GRAMMAR : SUPPORTED] for
> morphological reasoning; [SCHOLARLY_ANALYSIS : SUPPORTED] where
> published academic work corroborates; [BAYYINAH : PROPOSED] where
> extending into structural propositions not independently attested.
> Cross-root relationships, semantic network connections, morphological
> implications for meaning range.
>
> **Layer C -- Bayyinah Structural Interpretation** [BAYYINAH : PROPOSED]
> Structural encoding implications, anti-collapse instructions,
> training-specific annotations, structural-honesty readings. These are
> program-specific training directives, not consensus positions.

**Example application to the '-b-d entry (page 20):**

- **Layer A:** [LEXICON : ATTESTED] Root '-b-d. Forms: 'abd
  (servant/devotee), 'ibadah (service/devotion), 'abid (one who serves),
  ma'bud (the one served). Lane: encompasses the full range from
  ontological servitude to volitional devotion. Frequency: approximately
  275 occurrences across 17 derivative forms [VERIFY FROM CORPUS
  CONCORDANCE BEFORE SECOND EDITION BUILD].

- **Layer B:** [LEXICON + GRAMMAR : SUPPORTED] English "worship" narrows
  the semantic field to scheduled ritual, losing the ontological dimension.
  "Slave" imports chattel-slavery associations absent from the Arabic root.
  The '-b-d semantic field intersects with r-b-b (the sustained
  developmental relationship between Rabb and 'abd).

- **Layer C:** [BAYYINAH : PROPOSED] For structural encoding purposes,
  '-b-d must be encoded as an ontological state of devoted service, not a
  scheduled activity. Training data must preserve the full derivative tree
  to maintain root-system correlation. Anti-collapse instruction: never
  translate 'ibadah as merely "worship" without preserving the
  service-devotion-ontological scope.


## C-08: Ablation Study Protocol (New Appendix B) -- Major Rounds II/III Rewrite

**Location:** New appendix, to follow the existing Cross-Vendor LLM Audit
Protocol (current page 51).

**Rationale:** Multiple reviewers independently identified the same
required experiment across all three rounds. Round II council feedback
identified eleven critical deficiencies in the Round I protocol. Round III
identified seven additional deficiencies in the Round II protocol. This
rewrite addresses all of them.

**Round II deficiencies addressed:**

1. Additivity test always passes (telescoping sum) -- need factorial design
2. Confidence intervals require block/stationary bootstrap (ordinary
   resampling breaks long-range correlation structure)
3. Need placebo-annotation control
4. Need Arabic control text (not just English KJB)
5. Series definition must be committed to, or all options run and reported
6. Shuffled controls must destroy what the series measures -- word-order
   shuffling does not destroy root-recurrence
7. Null controls need empirical null distribution, not assumed H approximately equals 0.5
8. Multiple estimators required (DFA + wavelet, not just R/S)
9. Layer interactions must be tested, not just additivity
10. Pre-register as Zenodo deposit (timestamped, hashed) BEFORE running
11. Rename C4 and add Arabic non-Qur'anic corpus

**Round III deficiencies addressed:**

12. Factorial design incomplete -- only L2, L3, L5 tested alone; need all
    seven single-layer conditions plus seven leave-one-out
13. F-best selection bias -- choosing best single layer after measurement
    inflates comparison; pre-register with permutation null
14. Mu'allaqat too short for length-matched control -- use OpenITI corpus
15. C0 was previously measured -- record prior measurement in
    pre-registration
16. Multiple comparisons -- name one primary contrast or pre-register
    correction
17. Root-recurrence intervals not computable on bare English without
    injecting information -- series definition must specify one comparable
    scalar construction for every condition
18. Phase-randomized surrogate interpretation too strong -- revise
19. Mushaf order vs. chronological order must be committed in
    pre-registration

**New appendix text:**

> ## Appendix B: Structural Encoding Ablation Study Protocol (Second Edition)
>
> ### Purpose
>
> To determine whether the seven-layer structural encoding architecture
> measurably increases long-range correlation in the composite
> (English + annotations) series relative to bare English translation,
> whether the per-layer contributions interact, and whether any measured
> H-increase reflects genuine structural information rather than annotation
> density or format artifacts.
>
> ### Pre-Registration Requirement
>
> **This protocol must be deposited as a Zenodo artifact (timestamped,
> content-hashed) BEFORE any condition is measured.** The deposit must
> include: series definition, estimator selection, all condition
> specifications, all control specifications, text ordering commitment
> (see below), the primary contrast designation, any multiple-comparisons
> correction, and the analysis code. Deviations from the pre-registered
> protocol must be reported as such. This is non-negotiable. Unregistered
> results are exploratory, not confirmatory.
>
> **Prior measurement disclosure (Round III addition):** Record in the
> pre-registration that C0 (Arabic source) was previously measured using
> R/S in the Cross-Text paper. This is not disqualifying but must be
> disclosed as a prior look at the data.
>
> **Text ordering commitment (Round III addition):** H can change with
> text ordering. The pre-registration must commit to one ordering
> (Mushaf order or chronological revelation order) and state that
> ordering explicitly. If both orderings are tested, pre-register both
> as separate analyses and correct for the additional comparison.
>
> ### Prerequisites
>
> 1. **Series definition -- COMMIT BEFORE MEASUREMENT.** Specify exactly
>    what constitutes the "time series" for Hurst estimation. Options
>    include:
>    - Token-level semantic similarity (cosine distance between successive
>      token embeddings)
>    - Root-level recurrence intervals (distance between successive
>      occurrences of the same triconsonantal root)
>    - Verse-level thematic coherence scores
>    - Character-level entropy rates
>
>    **The series definition must be committed to in the pre-registration.**
>    If the protocol cannot choose, it must explicitly commit to running all
>    four options and reporting all four results. Cherry-picking the series
>    definition after seeing results invalidates the study.
>
>    **Series comparability constraint (Round III addition):** The chosen
>    series definition must specify one comparable scalar construction for
>    every condition. Root-recurrence intervals cannot be computed on bare
>    English (C1) without mapping English tokens back to Arabic roots --
>    which injects information unavailable to the bare translation. If
>    root-recurrence is used, it applies only to conditions that include
>    Arabic root annotations (C0, C6--C11, F-L2); conditions without root
>    annotations require a different series definition (e.g.,
>    token-embedding similarity). Where different series families are
>    required, treat them as different experiments rather than pretending
>    they estimate one identical quantity. The pre-registration must state
>    which series definition applies to which conditions.
>
> 2. **Multiple estimators (Round II requirement):** The study must use at
>    least two independent Hurst estimators:
>    - **DFA** (detrended fluctuation analysis) -- primary
>    - **Wavelet-based** estimator -- secondary
>    - **R/S** (rescaled range) -- optional tertiary for comparison with
>      Cross-Text paper
>
>    Report known biases of each estimator on series of the relevant length.
>    Where estimators disagree, report the disagreement rather than
>    selecting the more favorable result.
>
> 3. **Surrogate generation:** For each condition, generate:
>    - **Shuffled surrogates** -- see Controls section for proper
>      construction
>    - **Phase-randomized surrogates** -- preserve power spectrum while
>      destroying phase correlations. **Interpretation (Round III
>      revision):** If the original series shows significant H but
>      phase-randomized surrogates show similar H, this more narrowly
>      says that the measured persistence can be explained by
>      spectral/linear correlation structure and does not require the
>      destroyed phase relationships. It does NOT prove the signal is
>      "spectral, not structural" -- Hurst/DFA/wavelet estimates are
>      often substantially determined by second-order scaling structure
>      that phase randomization preserves. Report the comparison without
>      overclaiming its diagnostic power.
>
> ### Conditions
>
> Measure H on each of the following, in order:
>
> | Condition | Description                                      |
> |-----------|--------------------------------------------------|
> | C0        | Arabic source text (Uthmani orthography)          |
> | C1        | Standard English translation (e.g., Sahih International) |
> | C2        | Shuffled Arabic -- see Controls for proper construction |
> | C3        | Shuffled English -- see Controls for proper construction |
> | C4        | English cross-corpus control (matched-length English prose, non-Qur'anic, e.g., King James Bible) |
> | C4a       | **Arabic cross-corpus control** (matched-length Classical Arabic prose, non-Qur'anic -- pre-Islamic poetry such as the Mu'allaqat, or classical prose such as al-Jahiz) |
> | C5        | English + L1 (transliteration only)               |
> | C6        | English + L1 + L2 (root-system annotations)       |
> | C7        | English + L1 + L2 + L3 (anti-collapse markers)    |
> | C8        | English + L1--L4 (+ structural position)           |
> | C9        | English + L1--L5 (+ muhkam/mutashabih)             |
> | C10       | English + L1--L6 (+ Furqan constructs)             |
> | C11       | English + L1--L7 (full seven-layer encoding)       |
> | P1        | **Placebo-annotation control** -- same annotation density and format as C11, but with semantically irrelevant content (e.g., randomly assigned roots, shuffled anti-collapse markers, arbitrary structural tags) |
>
> ### Factorial Design (Rounds II/III Requirement)
>
> The additive condition ladder (C5 through C11) always produces a
> telescoping sum where per-layer increments sum to the total by
> construction. This does not test whether layers interact.
>
> **Round III correction:** The Round II factorial tested only L2, L3, and
> L5 alone. All seven layers must be tested individually, and seven
> leave-one-out conditions must be added. Leave-one-out tells most
> directly what each layer contributes. The term "factorial design" is
> used loosely here -- a full 2^7 factorial has 128 conditions. This is a
> fractional-factorial / interaction-probe design. The subset is selected
> to identify the interactions that matter most.
>
> **Single-layer conditions (all seven required):**
>
> | Condition | Description                                      |
> |-----------|--------------------------------------------------|
> | F-L1      | English + L1 alone (transliteration only, no other layers) |
> | F-L2      | English + L2 alone (root-system graphs without transliteration) |
> | F-L3      | English + L3 alone (anti-collapse markers without roots) |
> | F-L4      | English + L4 alone (structural position without other metadata) |
> | F-L5      | English + L5 alone (muhkam/mutashabih without structural metadata) |
> | F-L6      | English + L6 alone (Furqan constructs without other layers) |
> | F-L7      | English + L7 alone (tajwid signals without other layers) |
>
> **Leave-one-out conditions (all seven required):**
>
> | Condition | Description                                      |
> |-----------|--------------------------------------------------|
> | LOO-L1    | English + L2--L7 (full stack minus transliteration) |
> | LOO-L2    | English + L1 + L3--L7 (full stack minus root graphs) |
> | LOO-L3    | English + L1--L2 + L4--L7 (full stack minus anti-collapse) |
> | LOO-L4    | English + L1--L3 + L5--L7 (full stack minus structural position) |
> | LOO-L5    | English + L1--L4 + L6--L7 (full stack minus muhkam/mutashabih) |
> | LOO-L6    | English + L1--L5 + L7 (full stack minus Furqan constructs) |
> | LOO-L7    | English + L1--L6 (full stack minus tajwid) |
>
> **Interaction probes (pre-register at least these):**
>
> | Condition | Description                                      |
> |-----------|--------------------------------------------------|
> | F-L1×L2   | English + L1 + L2 (transliteration + root graphs) |
> | F-L2×L3   | English + L2 + L3 (root graphs + anti-collapse) |
> | F-L4×L5   | English + L4 + L5 (structural position + muhkam/mutashabih) |
> | F-L1×L7   | English + L1 + L7 (transliteration + tajwid) |
> | F-L2×L3×L5| English + L2 + L3 + L5 (roots + anti-collapse + muhkam/mutashabih) |
> | F-rev     | English + L7 + L6 + L5 + L4 + L3 + L2 + L1 (reverse order) |
>
> **F-best with selection-bias correction (Round III revision):**
>
> F-best (English + whichever single layer produces the highest H)
> introduces selection bias: choosing the best layer after measurement
> and then testing the full stack against it inflates the result.
> **Pre-register the comparison as follows:** compare C11 (full stack)
> against the maximum of all seven single-layer results, using a
> permutation null distribution for that maximum (i.e., the null is
> constructed by permuting condition labels and taking the maximum of the
> permuted single-layer results, repeated at least 1,000 times).
>
> **Key questions the factorial design answers:**
> - Does L2 without L1 produce any H-increase? (L2 references roots by
>   transliterated form; if transliteration is absent, is L2 still
>   informative?)
> - Does L7 (tajwid) alone produce any H-increase? (Diagnostic for
>   whether acoustic/recitational structure carries correlation
>   independently.)
> - Which layer, when removed, causes the largest H-drop? (Leave-one-out
>   identifies the highest-leverage layers.)
> - Does the full stack (C11) significantly exceed the best single layer
>   (F-best), after correcting for selection bias? If not, the
>   "seven layers" claim is misleading.
> - Does layer order matter? (C11 vs. F-rev)
> - Do theoretically motivated pairs (L1×L2, L2×L3, L4×L5, L1×L7)
>   interact supra-additively?
> - Is the H-increase from P1 (placebo) significantly different from C11?
>   If not, the measured increase reflects annotation density, not
>   structural content.
>
> ### Controls (Round II Revised)
>
> - **Shuffled controls (C2, C3) -- PROPERLY CONSTRUCTED:** Word-order
>   shuffling does not destroy root-recurrence patterns (the same roots
>   still appear at the same frequency). If the series definition is
>   root-level recurrence, shuffled controls must **randomly permute which
>   roots appear at which positions** -- i.e., reassign each token a random
>   root from the corpus vocabulary, preserving frequency distribution but
>   destroying positional structure. For each series definition, the
>   shuffle must destroy what that specific series measures.
>
> - **Empirical null distribution:** Do NOT assume shuffled H approximately
>   equals 0.5. Generate at least 1,000 shuffled surrogates for each
>   condition and construct the empirical null distribution. Test the
>   observed H against this distribution. If the null distribution is
>   centered far from 0.5, the series definition or estimator has a bias
>   that must be understood and reported.
>
> - **English cross-corpus control (C4):** Another extended sacred/literary
>   text in English. Establishes whether high H is specific to the Qur'an
>   or a general property of extended religious texts.
>
> - **Arabic cross-corpus control (C4a -- Rounds II/III):** At least one
>   length-matched Classical/Standard Arabic non-Qur'anic corpus.
>   **Round III revision:** The Mu'allaqat (pre-Islamic poetry) is too
>   short to serve as a length-matched control for the Qur'an. Use a
>   larger body of Classical Arabic prose from the OpenITI corpus (e.g.,
>   al-Jahiz, al-Tabari, or comparable extended classical texts) as the
>   primary Arabic control. The Mu'allaqat may be retained as a secondary
>   check on poetic vs. prose structure but cannot carry the primary
>   control role. Establishes whether high H in C0 is specific to the
>   Qur'an or a general property of Classical Arabic. Without this
>   control, any H-difference between C0 and C1 could reflect Arabic vs.
>   English rather than Qur'an vs. translation.
>
> - **Placebo-annotation control (P1 -- Round II addition):** Same amount
>   of structured annotation as C11, but with semantically irrelevant
>   content. If P1 shows H-increase comparable to C11, the measured effect
>   is format/density, not structural content. This is the most important
>   single control in the study.
>
> ### Statistical Requirements (Round II Revised)
>
> - **Block bootstrap** or **stationary bootstrap** 95% confidence
>   intervals for each condition (minimum 1,000 resamples). Ordinary
>   i.i.d. bootstrap breaks the long-range correlation structure being
>   measured and produces artificially narrow confidence intervals.
> - Report whether per-layer increments (C6-C5, C7-C6, etc.) are
>   significantly different from zero against the empirical null.
> - Test **interactions** via factorial design: does the full stack
>   significantly exceed the best single layer? Does layer order matter?
> - Test against placebo: is C11 significantly greater than P1?
> - **Primary contrast (Round III addition):** With conditions x 4 series
>   x 2--3 estimators, the total number of comparisons is large. The
>   pre-registration must name ONE primary contrast (recommended: C11 vs.
>   P1, full stack vs. placebo) that carries the study's main conclusion.
>   All other comparisons are exploratory and must be reported as such, or
>   a pre-registered multiple-comparisons correction (e.g., Holm-Bonferroni
>   or FDR) must be applied.
> - If H > 1 is observed for any condition, report this as requiring
>   estimator-specific interpretation (see C-10), not as
>   "super-persistence."
> - Report all estimator results (DFA, wavelet, and R/S if used). Where
>   they disagree, flag the disagreement prominently.
>
> ### Reporting
>
> Publish all measurements with error bars, including null or negative
> results. If the gap between C0 and C1 is smaller than hypothesized, or
> if the per-layer increments are not additive, or if H_restored is 0.73
> rather than 0.99, report that without changing the metric.
>
> If the placebo control (P1) shows comparable H-increase to C11, this is
> a finding, not a failure. It would mean the architecture's value lies in
> semantic fidelity (see C-11) rather than in H-restoration per se.
>
> **This would be Al-Furqan practicing Al-Furqan.**


## C-09: Audit Protocol Strengthening

**Location in manual:** Page 51, Appendix: Cross-Vendor LLM Audit
Protocol.

**Current state:** Five audit principles and five-round rotation. Tests
root-system correlation verification, anti-collapse resistance,
muhkam/mutashabih preservation, structural awareness, and full integration.

**Problem:** The protocol tests whether a model can reproduce the manual's
vocabulary, not whether it has acquired restored structural reasoning. It
lacks negative controls and blinded scoring.

**Corrections -- add the following to the audit protocol (Round II expanded):**

> ### Additional Audit Requirements (Second Edition)
>
> **6. Negative controls.** Each audit round must include:
>    - An **identical pretrained checkpoint before Al-Furqan fine-tuning**
>      (same architecture, same weights, no H-restored training data)
>      answering the same prompts. (Round II correction: "untrained
>      baseline" is ambiguous -- the control must be the same checkpoint
>      used as the starting point for fine-tuning, not a randomly
>      initialized model.)
>    - The **same trained model** given ordinary Arabic/English parallel
>      text (not from the H-restored corpus) to verify that improvements
>      are specific to the training data, not generic Arabic competence.
>    - **Deliberately corrupted annotations** -- anti-collapse markers with
>      inverted instructions -- to verify the model is not simply pattern-
>      matching annotation syntax.
>
> **7. Blinded scoring.** Evaluation of model outputs must be conducted by:
>    - Human Arabic specialists **blinded to condition** (they should not
>      know whether they are evaluating a trained or untrained model's
>      output).
>    - **Pre-registered scoring criteria** published before evaluation
>      begins.
>    - **Inter-rater agreement** (Round II addition): report Cohen's kappa
>      or Krippendorff's alpha across at least two independent raters for
>      each evaluation dimension. If inter-rater agreement falls below 0.6,
>      the scoring rubric needs refinement before results can be reported.
>
> **8. Held-out evaluation (Round II expanded).** Reserve at least 20% of
>    roots and at least 10 complete surahs from training. **Additionally,
>    hold out entire semantic networks** -- not just individual roots but
>    clusters of roots that share semantic fields (e.g., all roots in the
>    "divine mercy" network: r-h-m, l-t-f, gh-f-r, etc.) -- to test
>    whether the model generalizes structural relationships, not just
>    memorizes individual root entries. Evaluate on held-out material only.
>    The falsifiable question is: *Can a model trained on relational
>    Qur'anic structure make fewer translation-induced semantic collapses
>    on material it was not explicitly shown?*
>
>    **Frozen test set:** The held-out set must be fixed in the
>    pre-registration and never used during development or hyperparameter
>    tuning. Any "peeking" at test data invalidates the evaluation.
>
>    **Leakage-resistant splits:** Verify that no held-out root appears in
>    training data through cross-references, anti-collapse marker
>    instructions, or Furqan construct mappings that reference the held-out
>    material. Leakage through indirect references is the most common
>    failure mode for structured data splits.
>
> **9. Self-audit acknowledgment.** The current audit protocol is designed
>    and evaluated by the same research program that produced the training
>    data. For full validation, an independent research group should
>    administer the audit using the pre-registered protocol without
>    involvement from the Bayyinah program in scoring.
>
> **10. Reproducibility and portability (Round II addition).** The
>    following must be publicly available to permit independent
>    reproduction:
>    - The complete training corpus in a documented, machine-readable
>      annotation format
>    - All ablation and evaluation scripts
>    - The exact pretrained checkpoint used as the fine-tuning starting
>      point (or a precise specification sufficient to reproduce it)
>    - A dependency-pinned environment specification (e.g., requirements.txt
>      or conda environment file)
>
>    If any component cannot be released (e.g., proprietary model weights),
>    this must be stated explicitly and the evaluation must include at least
>    one fully open-source model pathway.


# 5. Core Contributions Preserved; Evidentiary Presentation Revised

No council member disputed in any of the three review rounds the following
as genuine contributions requiring no correction (verify against labeled,
hashed archive before freeze):

1. **Root-system correlation graphs** (all 28 entries) -- "the highest-
   leverage piece" of the architecture. The semantic field analysis is
   "high-value" and "often more precise than generic 'be careful with
   translation' warnings."

2. **Anti-collapse markers** (all 35 entries) -- "useful," "superb
   supervision signal," "the kind of high-signal, low-noise annotation
   that most religious and classical corpora still lack."

3. **Muhkam/mutashabih preservation** -- "structurally honest," the
   "theological analogue of VERIFIED/UNKNOWN/VIOLATED."

4. **SCAN-INCOMPLETE** -- "the right closing construct," "honest epistemic
   marking built into the format itself."

5. **Tajwid-as-signal** (Layer 7) -- a "genuine machine-learning research
   question": what happens if training preserves acoustic/recitational
   structure? The reading of ikhfa' as "presence-in-absence, a tajwid-
   level zahir/batin duality" was called "beautiful."

6. **Cross-vendor audit rotation** -- "follows your best habits," is
   "falsifiable."

7. **Transliteration-first encoding** (Layer 1) -- preserves phonological
   and morphological signal that pure English erases.

8. **The Furqan construct architecture** (all 8 constructs) -- maps
   Qur'anic structural features to LLM training primitives.


# 6. Implementation Roadmap

## 6.1 Manual (51-page document)

| Page(s) | Correction ID | Change Type          |
|---------|---------------|----------------------|
| 2       | C-01          | Replace section text |
| 2       | C-02          | Replace column header + add footnote |
| 2       | C-10          | Add methodological note |
| 2, passim | C-03       | Replace framing language throughout |
| 6--28   | C-05          | Add provenance tags to each root entry |
| 6--28   | C-07          | Add analytical layer separation |
| 29--45  | C-05          | Add provenance tags to each marker |
| 46      | C-06          | Add STRUCTURE_CLAIM tags |
| 48--49  | C-03          | Reframe Furqan construct H-functions |
| 51      | C-09          | Add audit requirements 6--10 |
| new     | C-08          | Add Appendix B (ablation protocol) |
| new     | C-11          | Add semantic fidelity endpoint to Appendix B |
| new     | C-12          | Add Appendix D (encoding/transliteration spec) |

## 6.2 Corpus (1,577-page document)

| Section          | Correction ID | Change Type                   |
|------------------|---------------|-------------------------------|
| Preamble (pp 2--5) | C-01, C-04 | Relabel H-values; fix P2/P3   |
| All inline annotations | C-05  | Add provenance tags            |
| All H-references | C-03         | Reframe as side-band encoding  |

## 6.3 Dependency Graph

The existing Al-Furqan nodes in the corpus DAG should be updated to
Second Edition terminology (remove/relabel unsupported H-value references,
replace "H-Restoration" with "Seven-Layer Structural Encoding" in node
labels). Additionally:
- Add a link from Al-Furqan to the ablation study protocol (when
  conducted) as a DESCENDANT dependency
- Add a link from Al-Furqan to the semantic fidelity evaluation (C-11)
  as a DESCENDANT dependency

## 6.4 Version Control

- Manual: Al-Furqan: Seven-Layer Structural Encoding Architecture
  **Second Edition**
- Corpus: Al-Furqan: Structurally Annotated Qur'anic Corpus **Second
  Edition**
- Both covers should note: "Corrections integrated from multi-model
  council review (Rounds I, II and III), October 2026"


# 7. The Falsifiable Question

The council converged across three rounds on a single question that, if
answered, would validate or refute the architecture's central claim.
Round II refined this into a two-level validation framework, and Round III
strengthened the causal controls:

> **Primary endpoint (C-11):** Can a model trained on relational
> Qur'anic structure make fewer translation-induced semantic collapses
> on material it was not explicitly shown?
>
> **Secondary endpoint (C-08):** Does the seven-layer structural encoding
> measurably increase long-range correlation (Hurst exponent) in the
> composite series, beyond what format-matched placebo annotations achieve?

The primary question is empirically approachable. It does not require
accepting the Computational Tawhid ontology. It does not require the
H-numbers to be correct. It requires only that the seven-layer annotations
carry structural information that generalizes beyond the annotated
training set.

If the answer to the primary question is yes -- if a model trained on the
structurally annotated corpus produces better held-out discrimination
between related Arabic concepts, preserves legitimate ambiguity more
reliably, catches intentionally flattened translations, reconstructs
cross-surah root relations, and becomes less likely to hallucinate
certainty where the source is underdetermined -- then the architecture has
demonstrated its value regardless of the H-numbers.

If the answer is no, the annotations remain valuable as a reference work
-- a structurally detailed English-language Qur'anic annotation corpus
[HYPOTHESIS: among the most detailed in existence; this comparative claim
requires a survey of existing corpora to substantiate] -- even without the
structural encoding claim.

Either outcome is a contribution. The Second Edition should be written to
survive both.


# 8. Council Document Provenance

**Rounds II/III.** To ensure auditability, the following practices
apply to all council review documentation:

**PROVENANCE POLICY: defined (Round II).** The following requirements
have been specified:

1. **Raw transcript hashing:** All raw council transcripts (Rounds I,
   II and III) should be content-hashed (SHA-256) and the hashes
   published alongside the errata, so that post-hoc editing of council
   feedback can be detected.

2. **Section classification:** Each section of council documentation
   should be marked:
   - [REVIEW] -- direct council feedback
   - [DRAFT ARTIFACT] -- proposed replacement text authored by the
     errata compiler
   - [TESTIMONY] -- author's own statements or rationale

3. **Round separation:** Council feedback from each round should be
   separated with dated headers, not merged into an undifferentiated
   stream.

4. **Per-correction attribution:** Each C-ID in the correction summary
   table now includes a "Raised By" column identifying which council
   members flagged the issue, to make consensus auditable rather than
   asserted.

5. **Archive labeling (Round III addition):** Each section of the raw
   council archive must be labeled with its originating model and round
   number. Without this, the "Raised By" column cannot be verified
   against the source transcripts.

6. **Internal drafting notes (Round III addition):** Council compilation
   documents may contain visible internal notes (e.g., "Length check:
   around 900--1200 words," "Let me tighten it"). These must be either
   removed or classified as [DRAFT ARTIFACT] before the archive is
   hashed. Section classification discipline applies to the archive
   itself, not only to the errata.

**PROVENANCE ARTIFACT: not yet deposited (Round III status).** The
policy above is defined but not yet enacted. Until the actual hashes
and frozen council archive exist as deposited artifacts, this gate
remains open. The distinction between defined policy and deposited
artifact is itself a provenance requirement.


# 9. Validation Sampling Plan (Round III -- New)

**Problem:** Applying provenance tags ([PROVENANCE : STATUS]),
STRUCTURE_CLAIM tags, and A/B/C analytical layer separation across
28 root entries, 35 anti-collapse markers, and the full 1,577-page
corpus is a massive annotation pass -- far larger than the Section 6
implementation tables imply. C-05 discipline claimed at scale but
verified nowhere would be an overclaim of its own.

**Validation sampling protocol:**

1. **Independent audit of applied tags:** After the corpus-wide tag
   application, an independent auditor (not the person who applied the
   tags) should audit a random sample of at least 10% of applied tags
   against the primary sources cited.

2. **Stratified sampling:** The audit sample should be stratified across:
   - All seven layers
   - All five PROVENANCE categories
   - All five STATUS levels
   - A representative spread of surahs (early Meccan, late Meccan,
     Medinan)

3. **Inter-rater agreement for tag assignment:** At least two independent
   raters should assign provenance tags to a calibration subset (minimum
   5% of entries) and report Cohen's kappa. If kappa falls below 0.6,
   the tagging rubric needs refinement before the full pass.

4. **Discrepancy resolution:** Where the audit finds tag assignments that
   disagree with the auditor's assessment, the discrepancy should be
   recorded, the tag should be reviewed, and the resolution should cite
   the specific primary source that resolves the disagreement.


# 10. Estimator-Selection Caveat (Round III -- New)

**Appendix B note:** H (Hurst exponent) may not be the optimal measure
for the structural properties the architecture aims to preserve.
Alternative measures -- compression ratio, mutual information, spectral
density, transfer entropy -- may capture different aspects of long-range
dependence or structural encoding. This is not a weakness of the
architecture but of the measurement approach.

If the ablation study produces a negative H result (no significant
difference between C11 and controls), this should be interpreted as one
of three possibilities:

1. The architecture does not increase the measured persistence (the
   null hypothesis is true for H)
2. H is not sensitive to the kind of structural information the
   architecture encodes (measure misspecification)
3. The series definition is not capturing the relevant signal

Before concluding that the architecture has failed, the study should
report at least one alternative measure alongside H. This inoculates
the protocol against a negative H result being read as a failure of
the architecture when it may be a failure of the measure.

**STATUS: [BAYYINAH : PROPOSED].**


# 11. Fable Review Disposition (Round III -- Revised)

The Fable review is classified as **OUTLIER/ADVERSARIAL REVIEW** and
excluded from consensus calculation under the following stated inclusion
criterion: scholarly register consistency across council members.

**Grounds for exclusion:**

1. The review exhibited pattern-collapsed adversarial posture
   inconsistent with the scholarly register of the other reviewers.
2. The review is excluded from consensus calculation, not from the
   evidentiary record.

**Round III refinement:** "Not endorsed by any other council member" is
an insufficient exclusion ground -- the other reviewers never saw the
Fable review, so their silence is not a rejection. The exclusion rests
on the stated inclusion criterion (scholarly register consistency), not
on absence of endorsement.

**Appendix C recommendation:** The Second Edition should include an
appendix with a per-claim decision table for Fable's review:

> | Fable Claim | Disposition | One-Line Reason |
> |-------------|-------------|-----------------|
> | [Each substantive claim] | ACCEPTED / REJECTED / ALREADY ADDRESSED | [Reason] |

This preserves append-only provenance (A1) while documenting the
exclusion process transparently. The raw Fable transcript remains in
the council archive.


Bismillah ir-Rahman ir-Rahim, Al-Haqq, Al-Mubin.
