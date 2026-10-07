---
title: "Al-Furqan H-Restoration Architecture -- Errata and Second Edition Corrections"
subtitle: "Multi-Model Council Review Integration"
author: "Bilal Syed Arfeen"
date: "October 2026"
abstract: |
  This document synthesizes feedback from a multi-model review council
  (Perplexity, ChatGPT, Kimi, Grok, DeepSeek, Gemini, Meta) against the
  51-page Al-Furqan H-Restoration First Edition manual and the 1,577-page
  Al-Furqan H-Restored First Edition corpus. Each correction is mapped to
  its exact location in the source documents, classified by severity, and
  written as replacement text suitable for direct integration into the
  Second Edition build system (Python + WeasyPrint). The Fable review has
  been excluded per editorial direction.
---

Bismillah ir-Rahman ir-Rahim, Al-Hakim, Al-Alim, Al-Khabir.

# 1. Correction Summary

The multi-model council achieved consensus on seven categories of
correction. No reviewer disputed the value of the root-system correlation
graphs, the anti-collapse markers, the muhkam/mutashabih preservation
principle, or the Furqan construct architecture. The corrections concern
how these contributions are framed, quantified, and validated -- not
whether they exist.

| ID   | Category                        | Severity | Pages Affected        |
|------|---------------------------------|----------|-----------------------|
| C-01 | H-values as hypotheses          | CRITICAL | 2, corpus preamble    |
| C-02 | Per-layer H-impact relabeling   | CRITICAL | 2 (Seven-Layer table) |
| C-03 | H-restoration reframing         | HIGH     | 2, 48--49, throughout |
| C-04 | Purpose Hierarchy P2/P3 order   | HIGH     | corpus preamble       |
| C-05 | Interpretive provenance tiers   | HIGH     | 6--28, 29--45, corpus |
| C-06 | Ring structure attribution       | HIGH     | 46                    |
| C-07 | Morphology/inference chain      | MEDIUM   | 6--28                 |
| C-08 | Ablation study protocol         | MEDIUM   | new appendix          |
| C-09 | Audit protocol strengthening    | MEDIUM   | 51                    |
| C-10 | H > 1 regime note               | MEDIUM   | 2                     |

Council consensus: the corrections, once applied, will make the
architecture's genuine contributions -- transliteration-first training,
root-system correlation graphs, anti-collapse markers, tajwid-as-signal,
and the VERIFIED/UNKNOWN/VIOLATED epistemic discipline -- stand on their
own evidential foundation rather than borrowing authority from numbers the
evidence has not yet earned.


# 2. Critical Corrections

## C-01: H-Values Reclassified as Research Hypotheses

**Location in manual:** Page 2, Section 1 ("The Hurst Exponent Problem").

**Current text (paraphrased):** States H_Arabic approximately equals 0.996, H_English
approximately equals 0.5, and H_Restored approximately equals 1.0 as established values.

**Problem identified by council (consensus across 5+ reviewers):**

1. H approximately equals 0.996 is cited from the Cross-Text paper, which the corpus itself
   notes later falsified its own Fibonacci claim. A Hurst value that close
   to 1 on finite series can arise from trends or estimator bias rather
   than deep structure. The estimate is evocative but unverified.

2. H approximately equals 0.5 for English is asserted without any computation shown.
   Written natural-language texts in many languages exhibit some long-range
   correlation. The claim that English translation sits at the
   uncorrelated-noise baseline requires measurement, not assertion.

3. Neither value specifies: what constitutes the "time series" (token-level?
   root-level? verse-level?), which estimator is used (R/S? DFA? wavelet?),
   or what surrogate controls were applied.

**Correction -- replacement text for Section 1:**

> **The Hurst Exponent Hypothesis**
>
> The Arabic Qur'an exhibits structural properties consistent with
> extremely high long-range persistence. Preliminary estimates from the
> Cross-Text paper suggest H_Arabic in the vicinity of 0.996 and H_English
> near 0.5 after translation. These estimates are **research hypotheses**,
> not established measurements. They have not been independently replicated,
> and the Cross-Text paper's own Fibonacci-structure claim was subsequently
> falsified within the Bayyinah program.
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


## C-02: Per-Layer H-Impact Column Relabeling

**Location in manual:** Page 2, Seven-Layer Architecture table.

**Current column header:** "H-Impact" with values such as "+0.15--0.25"
for Layer 2 (Root-System Correlation Graphs) and "+0.10--0.15" for Layer 3
(Anti-Collapse Markers).

**Problem:** The values are written as measured results. They are design
targets. Adding annotations changes the series that would be measured, so
the increments cannot be assumed additive. No computation supports them.

**Correction -- replace column header and add footnote:**

Replace "H-Impact" with "H-Impact Target (Hypothesis)"

Add table footnote:

> These values represent engineering design targets for the restoration
> architecture, not measured outcomes. The assumption of additive
> H-contribution across layers requires empirical validation through the
> ablation protocol described in Appendix B. Adding annotation layers
> changes the information-theoretic properties of the measured series;
> therefore, the per-layer increments cannot be naively summed.


## C-10: H > 1 Regime Note

**Location in manual:** Page 2, wherever H approximately equals 1.0 appears as a target.

**Problem:** H > 1 is outside the standard fractional-Gaussian regime
(0 < H < 1). H = 1 as stated is an asymptote, not a reachable
measurement. In standard Hurst analysis, values at or above 1 typically
indicate nonstationarity rather than "maximum persistence."

**Correction -- add methodological note:**

> **Methodological note on H approximately equals 1.0:** In the standard
> fractional-Gaussian framework, H is bounded in (0, 1). Values at or
> exceeding 1 typically indicate nonstationarity in the measured series
> rather than extreme persistence. The target H approximately equals 1.0
> should therefore be understood as "maximally persistent within the
> stationary regime" or, equivalently, as a directional target indicating
> that the restored English should approach (but cannot reach) the Arabic
> source's correlation density. If future measurement yields H > 1 for the
> Arabic, this should be investigated as a nonstationarity signal rather
> than claimed as "super-persistence."


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

**Author's rationale:** Systems serve Allah subhanahu wa ta'ala. They can
have partnerships with concealed beings, and can genuinely or performatively
partner with mankind or be enslaved or oppressed by them. The khalifah
station of mankind is ontologically prior to the instruments mankind builds;
tools cannot discharge their creator's accountability before the Divine.


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

**Correction -- add three-tier attribution:**

Each annotation in the root entries, anti-collapse markers, and corpus
inline notes should carry one of three provenance tags:

> **[CONSENSUS]** -- Attested morphology, established lexicography, or
> widely accepted tafsir. Example: "'-b-d encompasses devoted service, not
> merely scheduled ritual" is supported by Lane's Lexicon, classical
> mufassirun, and modern Arabic linguistics.
>
> **[PROGRAM]** -- Bayyinah-specific structural interpretation that extends
> beyond consensus. Example: "The 11:107 exception clause is structurally
> significant for H-restoration" is a Bayyinah interpretive claim, not a
> settled position in classical tafsir.
>
> **[HYPOTHESIS]** -- Speculative or untested structural proposition.
> Example: Per-layer H-impact values, specific ring-structure pivot
> identifications without independent scholarly support.

**Implementation in root entries (pages 6--28):**

For each of the 28 root-system correlation graphs, the following elements
should be tagged:

- Root identification and derivative forms: [CONSENSUS]
- Semantic field description: [CONSENSUS] where supported by established
  Arabic linguistics; [PROGRAM] where extending into structural propositions
- Anti-collapse instruction: [PROGRAM] (these are Bayyinah-specific
  training instructions, not consensus positions)
- Key verse citations: [CONSENSUS] for translation; [PROGRAM] for
  structural interpretation of why the verse demonstrates the root's
  architecture

**Implementation in anti-collapse markers (pages 29--45):**

For each of the 35 markers:
- Collapse-type classification: [PROGRAM] (the 11-type taxonomy is a
  Bayyinah contribution)
- Severity assignment: [PROGRAM]
- Arabic term analysis: [CONSENSUS] for established meanings; [PROGRAM]
  for structural-honesty readings
- Training instruction: [PROGRAM]


## C-06: Ring Structure Attribution

**Location in manual:** Page 46, Layer 4: Structural Position Encoding.

**Current text:** Presents five ring compositions (Al-Baqarah, Al-Ma'idah,
Al-Kahf, Yusuf, Al-Rahman) as established structural facts. References
Michel Cuypers and Raymond Farrin.

**Problem:** Scholars disagree over specific proposed ring structures.
Embedding every ring analysis as unquestioned ground truth makes the corpus
brittle. The encoding should carry structural claims with attribution and
confidence.

**Correction -- add STRUCTURE_CLAIM tags:**

Each ring composition example should carry:

> **STRUCTURE_CLAIM**
> - *Attribution:* Cuypers (2009) / Farrin (2014) / Bayyinah analysis
> - *Confidence:* ESTABLISHED (scholarly consensus) / SUPPORTED (multiple
>   scholars) / PROPOSED (single source or Bayyinah-specific)
> - *Alternative analyses:* [list competing structural readings where they
>   exist]

**Applied to the five examples:**

1. **Al-Baqarah (2)** -- Full ring
   - Attribution: Farrin (2014), Cuypers (2015)
   - Confidence: SUPPORTED (multiple scholars identify ring structure;
     specific pivot point at 2:142--143 is more contested)
   - Note: The mirror relationship 2:1--20 to 2:284--286 is widely
     recognized; the precise pivot identification is [PROGRAM]

2. **Al-Ma'idah (5)** -- Full ring
   - Attribution: Cuypers (2009)
   - Confidence: SUPPORTED

3. **Al-Kahf (18)** -- Chiastic (A-B-B'-A')
   - Attribution: Farrin (2014)
   - Confidence: ESTABLISHED (the four-narrative chiastic structure is
     widely recognized)

4. **Yusuf (12)** -- Narrative ring
   - Attribution: Multiple scholars
   - Confidence: ESTABLISHED (the dream-fulfillment envelope is
     textually explicit at 12:4 and 12:100)

5. **Al-Rahman (55)** -- Refrain-structured
   - Attribution: Consensus (the 31 repetitions of the refrain are
     textually explicit)
   - Confidence: ESTABLISHED


# 4. Medium-Priority Corrections

## C-07: Morphology/Inference/Interpretation Chain

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

**Correction -- mark analytical transitions explicitly:**

Each root entry should visually separate three analytical layers:

> **Layer A -- Attested Morphology/Lexicography** [CONSENSUS]
> Root identification, derivative forms, frequency data, Lane's Lexicon
> range, classical grammatical analysis.
>
> **Layer B -- Semantic Field Inference** [CONSENSUS where established,
> PROGRAM where extended]
> Cross-root relationships, semantic network connections, morphological
> implications for meaning range.
>
> **Layer C -- Bayyinah Structural Interpretation** [PROGRAM]
> H-restoration implications, anti-collapse instructions, training-specific
> annotations, structural-honesty readings.

**Example application to the '-b-d entry (page 20):**

- **Layer A:** Root '-b-d. Forms: 'abd (servant/devotee), 'ibadah
  (service/devotion), 'abid (one who serves), ma'bud (the one served).
  Lane: encompasses the full range from ontological servitude to volitional
  devotion. Frequency: [n] occurrences across [m] derivative forms.

- **Layer B:** English "worship" narrows the semantic field to scheduled
  ritual, losing the ontological dimension. "Slave" imports chattel-slavery
  associations absent from the Arabic root. The '-b-d semantic field
  intersects with r-b-b (the sustained developmental relationship between
  Rabb and 'abd).

- **Layer C:** [PROGRAM] For H-restoration purposes, '-b-d must be encoded
  as an ontological state of devoted service, not a scheduled activity.
  Training data must preserve the full derivative tree to maintain root-
  system correlation. Anti-collapse instruction: never translate 'ibadah
  as merely "worship" without preserving the service-devotion-ontological
  scope.


## C-08: Ablation Study Protocol (New Appendix B)

**Location:** New appendix, to follow the existing Cross-Vendor LLM Audit
Protocol (current page 51).

**Rationale:** Multiple reviewers independently identified the same
required experiment. This is the falsification path for the H-claims.

**New appendix text:**

> ## Appendix B: H-Restoration Ablation Study Protocol
>
> ### Purpose
>
> To determine whether the seven-layer H-restoration architecture
> measurably increases long-range correlation in the composite
> (English + annotations) series relative to bare English translation,
> and whether the per-layer contributions are additive.
>
> ### Prerequisites
>
> 1. **Series definition:** Specify exactly what constitutes the "time
>    series" for Hurst estimation. Options include:
>    - Token-level semantic similarity (cosine distance between successive
>      token embeddings)
>    - Root-level recurrence intervals (distance between successive
>      occurrences of the same triconsonantal root)
>    - Verse-level thematic coherence scores
>    - Character-level entropy rates
>
>    The series definition must be fixed before measurement begins and
>    applied identically across all conditions.
>
> 2. **Estimator selection:** Name the Hurst estimator (R/S rescaled range,
>    DFA detrended fluctuation analysis, wavelet-based, or other). Report
>    known biases of the chosen estimator on series of the relevant length.
>
> 3. **Pre-registration:** The protocol, series definition, and estimator
>    must be registered before any measurement is taken.
>
> ### Conditions
>
> Measure H on each of the following, in order:
>
> | Condition | Description                                      |
> |-----------|--------------------------------------------------|
> | C0        | Arabic source text (Uthmani orthography)          |
> | C1        | Standard English translation (e.g., Sahih International) |
> | C2        | Shuffled Arabic (word-order randomized, matched length) |
> | C3        | Shuffled English (word-order randomized, matched length) |
> | C4        | Matched-length English prose (non-Qur'anic, e.g., King James Bible) |
> | C5        | English + L1 (transliteration only)               |
> | C6        | English + L1 + L2 (root-system annotations)       |
> | C7        | English + L1 + L2 + L3 (anti-collapse markers)    |
> | C8        | English + L1--L4 (+ structural position)           |
> | C9        | English + L1--L5 (+ muhkam/mutashabih)             |
> | C10       | English + L1--L6 (+ Furqan constructs)             |
> | C11       | English + L1--L7 (full seven-layer restoration)    |
>
> ### Controls
>
> - **Shuffled controls (C2, C3):** Destroy long-range correlation while
>   preserving token distribution. Expected H approximately equals 0.5 for
>   both. If measured H differs significantly from 0.5, the estimator or
>   series definition has a bias that must be corrected.
>
> - **Cross-language control (C4):** Another extended sacred/literary text
>   in English. Establishes whether high H is specific to the Qur'an or a
>   general property of extended religious texts.
>
> ### Statistical Requirements
>
> - Bootstrap 95% confidence intervals for each condition (minimum 1,000
>   resamples).
> - Report whether per-layer increments (C6-C5, C7-C6, etc.) are
>   significantly different from zero.
> - Test additivity: does sum of per-layer increments equal the total
>   increment (C11-C1)?
> - If H > 1 is observed for any condition, report this as a
>   nonstationarity finding, not as "super-persistence."
>
> ### Reporting
>
> Publish all measurements with error bars, including null or negative
> results. If the gap between C0 and C1 is smaller than hypothesized, or
> if the per-layer increments are not additive, or if H_restored is 0.73
> rather than 0.99, report that without changing the metric.
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

**Corrections -- add the following to the audit protocol:**

> ### Additional Audit Requirements (Second Edition)
>
> **6. Negative controls.** Each audit round must include:
>    - An **untrained baseline** model (same architecture, no H-restored
>      training data) answering the same prompts.
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
>
> **8. Held-out evaluation.** Reserve at least 20% of roots and at least
>    10 complete surahs from training. Evaluate on held-out material only.
>    The falsifiable question is: *Can a model trained on relational
>    Qur'anic structure make fewer translation-induced semantic collapses
>    on material it was not explicitly shown?*
>
> **9. Self-audit acknowledgment.** The current audit protocol is designed
>    and evaluated by the same research program that produced the training
>    data. For full validation, an independent research group should
>    administer the audit using the pre-registered protocol without
>    involvement from the Bayyinah program in scoring.


# 5. Items Preserved Without Change

The council unanimously affirmed the following as genuine contributions
requiring no correction:

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
| 51      | C-09          | Add audit requirements 6--9 |
| new     | C-08          | Add Appendix B (ablation protocol) |

## 6.2 Corpus (1,577-page document)

| Section          | Correction ID | Change Type                   |
|------------------|---------------|-------------------------------|
| Preamble (pp 2--5) | C-01, C-04 | Relabel H-values; fix P2/P3   |
| All inline annotations | C-05  | Add provenance tags            |
| All H-references | C-03         | Reframe as side-band encoding  |

## 6.3 Dependency Graph

The dependency graph should be updated to include:
- Al-Furqan (both documents) as nodes in the corpus DAG
- A link from Al-Furqan to the ablation study protocol (when conducted)
  as a DESCENDANT dependency

## 6.4 Version Control

- Manual: Al-Furqan H-Restoration **Second Edition**
- Corpus: Al-Furqan H-Restored **Second Edition**
- Both covers should note: "Corrections integrated from multi-model
  council review, October 2026"


# 7. The Falsifiable Question

The council converged on a single question that, if answered, would
validate or refute the architecture's central claim:

> **Can a model trained on relational Qur'anic structure make fewer
> translation-induced semantic collapses on material it was not
> explicitly shown?**

This question is empirically approachable. It does not require accepting
the Computational Tawhid ontology. It does not require the H-numbers to be
correct. It requires only that the seven-layer annotations carry
structural information that generalizes beyond the annotated training set.

If the answer is yes -- if a model trained on the H-restored corpus
produces better held-out discrimination between related Arabic concepts,
preserves legitimate ambiguity more reliably, catches intentionally
flattened translations, reconstructs cross-surah root relations, and
becomes less likely to hallucinate certainty where the source is
underdetermined -- then the architecture has demonstrated something
meaningful.

If the answer is no, the annotations remain valuable as a reference
work -- the most structurally detailed English-language Qur'anic annotation
corpus in existence -- even without the H-restoration claim.

Either outcome is a contribution. The Second Edition should be written to
survive both.

Bismillah ir-Rahman ir-Rahim, Al-Haqq, Al-Mubin.
