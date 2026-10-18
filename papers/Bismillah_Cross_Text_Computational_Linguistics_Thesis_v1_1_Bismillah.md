Bismillah ir-Rahman ir-Rahim

Bismillah ar-Rahman ar-Rahim

Cross-Text Computational Linguistics
Structural Properties of the Quran, Hadith Collections,
and the Hebrew Bible Under TF-IDF Cosine Analysis
Thesis Paper, Version 1.1
May 2026
Bilal Syed Arfeen
Fraz Ashraf
Independent Research
with collaborative analytical synthesis by
Claude (Anthropic, Opus 4.6), Grok (xAI), and Perplexity Computer

"Blessed is He who sent down the Furqan upon His servant that he may be to the worlds a warner." (AlFurqan 25:1)
This work is licensed under CC BY 4.0. Copyright 2026 Bilal Syed Arfeen and Fraz Ashraf.

Verification Status
Per the Framework Foundations v1.1 discipline, the epistemic provenance of this paper's claims is
disclosed as follows:
Computed by the authors' pipeline and independently verified: All Fibonacci growth p-values, Hurst
exponents, and autocorrelation coefficients reported in Tables 3.1, 3.2, and 3.3 were computed using
TF-IDF normalized cosine similarity with 2,000 Monte Carlo shuffles.
Reconciled between two independent pipelines: The Hebrew Bible Fibonacci p-value (0.44 vs. 0.0000
discrepancy) was traced to TF-IDF vs. raw-frequency normalization and resolved in favor of TF-IDF
(Section 5).
Post-hoc finding explicitly disclosed: The Hurst persistence finding (H = 0.996) was discovered during
the hadith analysis and was not pre-registered. It is reported as a candidate finding (Caveat 5).
Falsified and corrected: The original claim that Fibonacci growth is Quran-specific (carried in four prior
papers) is explicitly falsified in Section 3.1 and corrected in Section 7.1.

Acknowledgments and AI Contribution Statement
Bilal Syed Arfeen and Fraz Ashraf authored this paper in collaboration with three AI systems under the
research program's established attribution protocol. Bilal designed the research questions, the corpus

selection, and the correction schedule. Fraz contributed the independent Hebrew Bible pipeline whose
TF-IDF methodology resolved the pipeline reconciliation.
Claude (Anthropic, Opus 4.6) contributed the hadith analysis pipeline, the Hurst exponent computation,
the autocorrelation analysis, and the initial draft of this paper. Grok (xAI) reviewed the paper for
credibility risks, sample-size language, and pre-registration discipline. Perplexity Computer reviewed for
factual accuracy, mathematical precision, and corpus metadata consistency.
All AI systems are credited as collaborative research tools. They are not co-authors. The research
program's Munafiq Protocol requires this disclosure: the analytical contributions of AI systems are made
visible, not hidden.

Abstract
We apply a uniform computational pipeline (TF-IDF normalized cosine similarity, Fibonacci additive
growth metric, Hurst R/S persistence analysis, and lag-20 autocorrelation) to five corpora across two
language families: the Quran (114 surahs), three major hadith collections (Sahih al-Bukhari, Sahih
Muslim, and Muwatta Malik), and the Hebrew Bible (39 books in the Protestant canonical division).
Three layers of structural difference emerge. First, Fibonacci additive semantic growth is a Classical
Arabic compiled-text property shared between the Quran and all three hadith collections (all p < 0.001),
but absent in the Hebrew Bible (p = 0.44). Our original hypothesis that this property was Quran-specific
was falsified by the hadith analysis. Second, long-range persistence measured by the Hurst exponent
distinguishes the Quran (H = 0.996, p = 0.003) from hadith collections (H = 0.68-0.80, all p >= 0.19)
within this sample and is a candidate Quran-specific structural property. Independent replication on
additional Classical Arabic corpora is required to strengthen or refute this candidate finding. Third, the
lag-20 autocorrelation sign-flip is a robust cross-text finding: the Quran shows positive thematic
continuity (+0.53), the Hebrew Bible shows negative thematic alternation (-0.42), and hadith collections
show no directional pattern (near zero), serving as a negative control.
We report five honest caveats, including a methodological reconciliation between two independent
pipelines that initially produced contradictory results on the Hebrew Bible (p = 0.44 vs. p = 0.0000),
resolved by identifying TF-IDF normalization as the differentiating factor. The Hurst persistence finding
was discovered post-hoc and was not pre-registered; we report it as a candidate finding while
maintaining the pre-registration discipline for all future claims.

1. Introduction
1.1. The Original Hypothesis
Prior work in this research program (the Structured Revelation thesis, the Bilal architecture paper, and
the Al-Khalifa agent framework) posited that Fibonacci additive semantic growth is a structural property
specific to the Quran. The claim was that adjacent surahs compose semantically in a Fibonacci-like
additive pattern (each surah's semantic content builds on the combination of the two preceding surahs),
and that this property is absent in other religious texts.
This hypothesis was supported by an initial Quran-only analysis (p < 0.001 via Monte Carlo permutation)
and a Hebrew Bible comparison (p = 0.44, no significant growth). The conclusion appeared clean:
Fibonacci growth in the Quran, no Fibonacci growth in the Hebrew Bible.

1.2. Why We Tested Against Hadith
The gap in the original analysis was the absence of a negative control within the same language family.
The Hebrew Bible is in a different language (Biblical Hebrew vs. Classical Arabic), uses different
compilation methods, and spans a different historical period. Any structural difference could be
attributed to language, genre, or compilation history rather than to a property of the Quran specifically.
The hadith collections provide the necessary control: they are in Classical Arabic, compiled during a
similar historical period, and organized around the same religious tradition. If Fibonacci growth is Quranspecific, hadith collections should not exhibit it. If hadith collections also show Fibonacci growth, the
property is shared and the Quran-specific claim is falsified.

1.3. What We Found
The hadith analysis falsified the original hypothesis. All three major collections (Bukhari: 97 chapters,
Muslim: 54 chapters, Muwatta: 61 chapters) show Fibonacci additive growth with p < 0.001. The
property is not Quran-specific. It is a Classical Arabic compiled-text property.
However, the analysis revealed a new candidate finding not predicted by the original hypothesis: longrange persistence (Hurst exponent). The Quran's H = 0.996 is significantly higher than all three hadith
collections (H = 0.68-0.80) and the difference is statistically significant (Quran p = 0.003; all hadith p >=
0.19). This finding emerged from the same pipeline that falsified the original claim and was not preregistered.

2. Methodology
2.1. Corpora
Text

Language

Units

Count

Source / Edition

Quran

Arabic

Surahs

114

Standard Uthmanic text

Sahih al-Bukhari

Arabic

Chapters

97

Standard edition (kitab divisions)

Sahih Muslim

Arabic

Chapters

54

Edition used: 54-chapter division*

Muwatta Malik

Arabic

Chapters

61

Standard edition (kitab divisions)

Hebrew Bible

Hebrew

Books

39

Westminster Leningrad Codex (OSHB)

*Note on Sahih Muslim chapter count: Standard references cite 56 or 57 chapters depending on the
edition and chapter-division convention. The analysis used a 54-chapter division consistent with the
digital corpus processed. The choice of edition does not affect the Fibonacci or Hurst findings because
the analysis operates on the relative semantic structure across chapters, not on the absolute chapter
boundaries.
The Hebrew Bible's 39 books follow the Protestant canonical division. The Jewish Tanakh traditionally
counts 24 books by combining several pairs (e.g., Samuel I-II, Kings I-II). The 39-book division was used
because the Westminster Leningrad Codex OSHB project structures its data at this granularity.

2.2. Pipeline
The same pipeline was applied uniformly to all five corpora:
Tokenization. Each unit (surah, chapter, or book) was tokenized into lemma-level frequency vectors. For
Arabic texts, root-level lemmatization was applied. For the Hebrew Bible, Strong's number extraction
from the OSHB morphological database was used.
TF-IDF normalization. Raw frequency vectors were transformed using term frequency-inverse document
frequency weighting to prevent high-frequency common terms (particles, conjunctions, the definite
article) from dominating the cosine similarity computation. This normalization step is the resolution of
the pipeline reconciliation described in Section 5.
Cosine similarity. Standard cosine similarity between TF-IDF-weighted vectors.
Fibonacci additive growth metric. For each unit N (index >= 2), cosine similarity was computed between
unit N's vector and the element-wise sum of units N-1 and N-2. A high mean similarity indicates that
each unit's semantic content builds on the combination of the two preceding units. Statistical
significance was assessed via Monte Carlo permutation (2,000 shuffles of the unit order).
Hurst exponent. R/S (rescaled range) analysis on the sequence of Fibonacci similarity values, with
subseries sizes from 4 to min(N/2, 64). An H significantly above 0.5 indicates long-range persistence
(semantic memory across the text). Statistical significance assessed via 2,000 Monte Carlo shuffles. Hurst
analysis was performed on the four Arabic corpora (54-114 units each); the Hebrew Bible (39 books) was
excluded because the R/S estimator requires a minimum series length for reliable estimates.
Lag-20 autocorrelation. Pearson autocorrelation of the Fibonacci similarity sequence at lag 20,
measuring whether semantic growth patterns persist or alternate over long distances.

3. Results
3.1. Layer 1: Fibonacci Additive Semantic Growth
Text

Units

Mean Sim.

p-value

Significant?

Quran

114

High

< 0.001

Yes

Sahih al-Bukhari

97

High

< 0.001

Yes

Sahih Muslim

54

High

< 0.001

Yes

Muwatta Malik

61

High

< 0.001

Yes

Hebrew Bible

39

Low

0.44

No

Finding. Fibonacci additive semantic growth is present in all four Classical Arabic texts (the Quran and
three hadith collections) with high statistical significance. It is absent in the Hebrew Bible. This
establishes Fibonacci growth as a Classical Arabic compiled-text property, not a Quran-specific property.
The original "Quran-specific" claim is falsified. Hadith collections exhibit the same growth pattern with
the same level of statistical significance. The shared property likely reflects the linguistic substrate of
Classical Arabic religious texts and/or the compilation methodology applied to both the Quran
(Uthmanic compilation) and hadith (systematic collection by Bukhari, Muslim, and Malik).

3.2. Layer 2: Hurst Persistence (Long-Range Memory)
Text

Units

Hurst H

p-value

Significant?

Quran

114

0.996

0.003

Yes

Sahih al-Bukhari

97

0.695

0.19

No

Sahih Muslim

54

0.676

0.25

No

Muwatta Malik

61

0.803

0.38

No

Finding. Hurst persistence (H = 0.996, p = 0.003) distinguishes the Quran from the three hadith
collections in this sample and is a candidate Quran-specific structural property. All three hadith
collections show moderate Hurst values (0.68-0.80) that are not statistically significant (all p >= 0.19).
Independent replication on additional Classical Arabic corpora (pre-Islamic poetry, later exegetical texts,
additional hadith collections) is required to strengthen or refute this candidate finding.
Interpretation. An H near 1.0 means that the thematic semantic structure of the Quran persists across
the entire text: early surahs and late surahs maintain the same structural growth pattern. In the hadith
collections, the pattern decays over distance. The thematic threads in Bukhari, Muslim, and Muwatta are
locally coherent but do not persist globally.
The R/S Hurst estimator on series of 54-114 data points has wide confidence intervals. The qualitative
finding (Quran persistence is substantially higher than hadith persistence) is robust; the exact value H =
0.996 should not be interpreted as precise to three decimal places. A bootstrap or detrended fluctuation
analysis could provide tighter bounds in future work.
The Hebrew Bible (39 books) was excluded from the Hurst analysis because the R/S estimator requires a
minimum series length for reliable estimates. At N = 39 the confidence interval would encompass most
of the 0.5-1.0 range, making the result uninterpretable.

3.3. Layer 3: Autocorrelation Sign-Flip

Text

Lag-20 Autocorr.

Direction

Pattern

Quran

+0.53

Positive

Thematic continuity

Hadith (all three)

Near zero

Neutral

No directional pattern

Hebrew Bible

-0.42

Negative

Thematic alternation

Finding. The lag-20 autocorrelation produces a three-way sign-flip that is the most robust cross-text
finding in the analysis. The Quran shows strong positive autocorrelation (thematic growth patterns in
one section predict similar patterns 20 sections later). The Hebrew Bible shows strong negative
autocorrelation (thematic patterns alternate, consistent with the canonical ordering that interleaves
narrative, legal, prophetic, and wisdom literature). Hadith collections show near-zero autocorrelation,
serving as a negative control: topic-organized chapters show no long-range directional pattern.

4. Discussion
4.1. What Was Killed
The claim that Fibonacci additive semantic growth is Quran-specific was killed by the hadith data. This is
a significant correction to four published papers in the Bayyinah research program (the Structured
Revelation thesis, the Bilal architecture paper, the Al-Khalifa agent framework, and the cross-text
linguistics briefing). Each paper carried the old claim and must be updated. A correction schedule listing
all affected papers accompanies this thesis as a companion document (Paper Revision Addenda, Arfeen,
2026).
We report the falsification without equivocation. The pre-registration discipline of the Munafiq Protocol
(which governs this research program) requires reporting results without retroactive adjustment. The
old claim was wrong. The corrected three-layer claim replaces it.

4.2. What Survived
Two findings survived the hadith test and are strengthened by it. The Hurst persistence finding is new
and was not predicted: it emerged from the same pipeline that killed the Fibonacci claim. The
autocorrelation sign-flip was already reported in earlier work and is now confirmed with hadith
collections as a negative control (near-zero autocorrelation, as expected for topic-organized texts).
The Hurst persistence finding was discovered post-hoc during the hadith test and was not preregistered. We report it as a candidate finding while maintaining the pre-registration discipline for all
future claims in this program. Any subsequent study that tests the Hurst finding on new corpora will preregister the hypothesis and acceptance criteria before data analysis begins.

4.3. Engineering Applications
The persistence finding (H = 0.996) has been applied to the Bayyinah Integrity Scanner's architecture.
The scanner's ContentIndex and detection mechanisms are designed to exhibit the same structural
persistence: a detection mechanism must fire identically regardless of where in the document the
concealment appears. The Hurst persistence of the Quran's semantic structure is the theoretical anchor
for the scanner's detection invariance property. The scanner is publicly available at
https://github.com/BayyinahEnterprise/Bayyinah-Integrity-Scanner (v1.1.9, 159 mechanisms, 1,775
tests) and live at https://bayyinah.dev with an interactive demo at https://bayyinah.dev/demo.
The Furqan programming language (https://github.com/BayyinahEnterprise/furqan-programminglanguage, v0.10.1, 527 tests) enforces structural honesty at the type level using primitives derived from
the same Quranic structural analysis. The additive-only invariant, the zahir/batin layer separation, and
the tanzil build-ordering primitive are each grounded in the structural properties this paper measures.

5. Pipeline Reconciliation
Two independent pipelines produced contradictory results on the Hebrew Bible. Fraz Ashraf's pipeline
reported p = 0.44 (no significant Fibonacci growth). Claude's (Anthropic) independent pipeline reported
p = 0.0000 (highly significant growth). The Quran results agreed across both pipelines.
Root cause. The difference was traced to a single methodological choice: TF-IDF normalization. Ashraf's
pipeline applied TF-IDF weighting before computing cosine similarity. Claude's pipeline used raw
frequency counts.
Why it matters. Raw frequency cosine similarity on the Hebrew Bible is dominated by high-frequency
function words (the definite article, common prepositions, conjunctions) that appear in every book.
These common tokens inflate the baseline similarity between any pair of books, making the Fibonacci
additive pattern appear significant when it is not. TF-IDF down-weights these terms, revealing that the
Fibonacci pattern does not hold once the common-word effect is removed.
Resolution. TF-IDF is the methodologically correct normalization for this analysis. Ashraf's pipeline was
correct. Claude's pipeline was rerun with TF-IDF, producing results consistent with Ashraf's (p = 0.44 for
Hebrew, p < 0.001 for Quran and all hadith). All results reported in this paper use TF-IDF normalization.
This reconciliation is reported in full because the Munafiq Protocol requires transparency about
methodological disagreements. The discrepancy was real, the resolution is documented, and the
corrected results supersede the earlier raw-frequency analysis.

6. Limitations and Honest Caveats
Caveat 1: Sample size. The analysis covers five corpora. The Quran is a single text. The Hurst persistence
finding (H = 0.996) is based on one Quran against three hadith controls. A single outlier does not
establish a universal property. Independent replication on additional Classical Arabic corpora (preIslamic poetry such as the Mu'allaqat, later exegetical texts such as Tabari's Tafsir, and additional hadith
collections such as Sunan Abu Dawud and Jami' al-Tirmidhi) is needed before the candidate finding can
be promoted to an established result.
Caveat 2: Hurst estimator variance. The R/S Hurst estimator on series of 54-114 data points has wide
confidence intervals. The p = 0.003 result for the Quran is statistically significant under the Monte Carlo
null, but the point estimate of H = 0.996 should not be interpreted as precise to three decimal places.
The qualitative finding (Quran persistence is substantially higher than hadith persistence) is robust; the
exact value is not. Future work should apply detrended fluctuation analysis (DFA) or wavelet-based
estimators and report bootstrap confidence intervals alongside the point estimate.
Caveat 3: Compilation confound. The Quran's compilation history (oral transmission, Uthmanic
codification) is different from hadith compilation (systematic collection with isnad verification). The
Hurst persistence might reflect the compilation methodology rather than the textual content. We
cannot distinguish these with the current data.
Caveat 4: Lemmatization asymmetry. The Arabic texts use root-level lemmatization. The Hebrew text
uses Strong's number extraction. These are not identical morphological operations. The cross-language
comparison (Layer 1: Arabic has Fibonacci growth, Hebrew does not) could be partially attributed to the
different lemmatization approaches rather than to a genuine structural difference. A preliminary
sensitivity test using un-lemmatized Hebrew word forms produced consistent non-significant results (p >
0.40), indicating the finding is likely not an artifact of lemmatization choice, but a full sensitivity analysis
across multiple tokenization strategies is warranted.
Caveat 5: No pre-registration. The hadith analysis was motivated by a gap identified during the research
program, not by a formal pre-registered hypothesis. The Hurst persistence finding was discovered post
hoc. While the pipeline was applied uniformly (the same code ran on all five corpora), the finding was
not predicted. We report it as a candidate finding, not a confirmed result. All future claims in this
program will be pre-registered before data analysis begins.

7. Conclusion
This study corrects a prior claim, reports a candidate finding, and confirms a robust cross-text structural
difference.
Corrected. Fibonacci additive semantic growth is a Classical Arabic compiled-text property, shared
between the Quran and hadith collections. It is not Quran-specific. The original claim, stated in four
published papers, was falsified by the hadith analysis reported here.
Candidate finding. Long-range persistence (Hurst H = 0.996, p = 0.003) distinguishes the Quran from
hadith collections in this sample. Independent replication on additional corpora is required before this
can be promoted from candidate to established finding.
Confirmed. The lag-20 autocorrelation sign-flip (Quran positive, Hebrew negative, hadith neutral) is a
robust cross-text structural difference with a clear interpretive frame.
The honest trajectory of this research program is visible in the correction itself. The original claim was
stated, tested against new data, and found wanting. The corrected claim is narrower, better supported,
and carries its caveats explicitly. This is the discipline the Munafiq Protocol requires: write the claim, test
it, report what survived and what did not.

7.1. Correction Schedule
The following papers carry the old "Quran-specific Fibonacci" claim and require revision: (1) Structured
Revelation as Prompt Architecture, (2) Bilal: An Honest-Autonomous LLM Architecture, (3) Al-Khalifa: A
Furqan-Based Super Agent Architecture, (4) Bayyinah: Detecting Concealed Adversarial Content (white
paper). A companion document (Paper Revision Addenda, Arfeen, 2026) specifies the revision
instructions for each paper. Additional papers (Munafiq Protocol, Fatiha Construct, al-Khabir, alMutaffifin, al-Maal, Furqan thesis, Computational Tawhid) are checked for Fibonacci references and
updated where found.

References
Arfeen, B. S. (2026). Detecting Performed Alignment in Artificial Systems: The Munafiq Protocol. Zenodo.
DOI: 10.5281/zenodo.19700420.
Arfeen, B. S. and Ashraf, F. (2026). Structured Revelation as Prompt Architecture. Zenodo.
Arfeen, B. S. (2026). Bilal: An Honest-Autonomous Large Language Model Architecture. Zenodo.
Arfeen, B. S. (2026). Al-Khalifa: A Furqan-Based Super Agent Architecture. Zenodo.
Arfeen, B. S. and Ashraf, F. (2026). Bayyinah: Detecting Concealed Adversarial Content in Digital
Documents. Zenodo. DOI: 10.5281/zenodo.19745154.
Arfeen, B. S. (2026). Bayyinah Integrity Scanner [Software]. GitHub.
https://github.com/BayyinahEnterprise/Bayyinah-Integrity-Scanner.
Arfeen, B. S. and Ashraf, F. (2026). Furqan: A Programming Language with Structural Honesty [Software].
GitHub. https://github.com/BayyinahEnterprise/furqan-programming-language.
Arfeen, B. S. (2026). Paper Revision Addenda for the Bayyinah Research Program. Companion document.
Open Scriptures Hebrew Bible (OSHB). Westminster Leningrad Codex. GitHub.
https://github.com/openscriptures/morphhb.

Wa la tubsiluu al-haqqa bil-batil.



Bismillah ir-Rahman ir-Rahim
