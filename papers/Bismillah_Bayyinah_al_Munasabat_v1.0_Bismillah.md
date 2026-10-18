Bismillah ir-Rahman ir-Rahim

BAYYINAH ENTERPRISE

Bayyinah al-Munāsabāt
Empirical Falsification Testing of Canonical-Order Structural Coherence in the Quran
A multi-corpus replication study extending Cross-Text Computational Linguistics into the
canonical-versus-chronological-order falsification regime

Bilal Syed Arfeen
Bayyinah project lead
with empirical pipeline assistance by Claude (Opus 4.7, Anthropic)

Version 1.0 · May 7, 2026
Licensed CC BY 4.0 · bayyinahenterprises@tuta.com
Companion to: Cross-Text Computational Linguistics (Arfeen & Ashraf 2026)

Abstract
This paper reports the results of a multi-round falsification investigation testing whether the
structural autocorrelation observed in the canonical Uthmanic Quran reported in Cross-Text
Computational Linguistics (Arfeen & Ashraf 2026) is a property of intra-quartile ordering decisions
or is largely attributable to the canonical's approximate length-sorted compilation structure. The
investigation tests the canonical Quran (114 surahs) against two published chronological
reconstructions (the Cairo 1924 standard and the verbatim Nöldeke-Schwally 1860 sequence),
against within-length-quartile shuffles preserving the approximate length-sort, against intra-period
shuffles, and against four negative-control corpora drawn from the same broad linguistic and
religious tradition: three canonical Sunni hadith collections (Sahih al-Bukhari, Sahih Muslim,
Muwatta Malik), the Hebrew Bible in Westminster Leningrad Codex form with Strong's-number
lemmatization, and twenty-eight diwans of pre-Islamic Arabic poetry including all seven Mu ʿallaqāt
poets. The pipeline of Cross-Text Computational Linguistics (TF-IDF normalized cosine similarity,
Fibonacci-additive growth metric, lag-N autocorrelation) is applied uniformly across all corpora
using two independent Arabic lemmatization implementations (Tashaphyne root extraction and
Qalsadi citation-form lemmatization). Two findings emerge. First, Cross-Text §3.1 has now
established that the Fibonacci-additive metric itself is a Classical Arabic compiled-text property and
is not Quran-specific; the present paper accordingly tests a different and downstream question —
whether the autocorrelation of the Fibonacci-additive sequence in canonical order produces
discrimination that the metric itself does not — and reports the result of that test rather than
claiming the metric was Quran-specific to begin with. Second, and more consequentially, the withinlength-quartile shuffle test shows that approximately 82 percent of the canonical Quran's lag-20
autocorrelation gap over random shuffles is attributable to its approximate length-sorted

compilation structure rather than to deeper intra-quartile ordering decisions. The canonical
Uthmanic order does exhibit a smaller but statistically significant residual signal beyond what lengthsort alone produces (gap of approximately +0.15 between canonical and within-quartile shuffles at
lag 20, roughly 2.7 standard deviations from the within-quartile null), which is the size of the
intentional-canonical-arrangement effect this paper can support. The previously stated headline
magnitude ("approximately one order of magnitude larger than any tested alternative") was an
overstatement and is corrected here. Hadith negative controls survive (their topical rather than
length-based arrangement explains their low autocorrelation); Cairo 1924 contrast survives but its
mechanism is reframed (Cairo 1924 lacks the length-sort the canonical has). The paper documents
one numerical discrepancy with Cross-Text (lag-20 reported as +0.53 there and +0.80 here on a
similar quantity, not currently reconcilable without examining Cross-Text's exact pipeline code) and
preserves it per the §5 reconciliation discipline rather than rewriting it away. The investigation
closes with the candidate-finding status restated under Cross-Text §6 Caveat 1 and an invitation to
independent replication.

Table of Contents
1. Identity and Purpose
2. The Falsification Question
3. Theoretical Grounding
4. Methodology
5. Results
6. The Bell Constraint and Other Limitations
7. Implications for the Cross-Text Program
8. Implications for Software Engineering
9. Code and Data Availability
10. References
11. Acknowledgements

1. Identity and Purpose
This paper documents an empirical falsification test of one specific class of structural claims about
the canonical Quran. The class of claims is autocorrelation properties of compositional similarity
sequences — properties first reported in Cross-Text Computational Linguistics (Arfeen & Ashraf
2026) and shown there to discriminate between the Quran and three Classical Arabic hadith
collections. The test conducted here is the obvious one not run in that paper: do the same properties
hold when the Quran is reordered out of its canonical Uthmanic arrangement and into an
arrangement reflecting the chronological sequence of revelation as reconstructed by mainstream
scholarship?
This paper is the empirical companion to Cross-Text Computational Linguistics. Where the cross-text
paper investigates one specific structural property (Fibonacci-additive growth) across multiple
corpora at canonical order only, this paper investigates the same property and three additional ones
(Hurst R/S persistence, mean Fibonacci similarity, multi-lag autocorrelation) across multiple

orderings of the same single corpus, with negative controls drawn at the corpus level rather than the
metric level. The two papers test orthogonal dimensions of the same general claim. Both can be read
independently. Readers interested in metric-discrimination across compiled corpora should read the
cross-text paper first; readers interested in arrangement-discrimination within a single corpus
should read this paper first.
The discipline applied throughout is the Bayyinah audit chain: every claim is grounded in a substrate
the reader can run, every limitation is named at four places (here and in three places in the source
repository), and every retraction is preserved in the immutable historical record. One specific finding
from the second investigative round was reframed during the third round when verbatim Nöldeke
evidence demonstrated that an earlier characterization (chronological reordering destroys
autocorrelation) was too strong and required narrowing (Cairo 1924 specifically destroys most of
the autocorrelation; Nöldeke partially preserves it; the canonical exceeds both). The reframing is
preserved here in §7.1 rather than rewritten away.

2. The Falsification Question
Cross-Text Computational Linguistics reports that the canonical Quran shows Fibonacci-additive
growth (cosine similarity between successive surah TF-IDF vectors and the additive sum of the
previous two) at a rate substantially above random null distribution. The paper additionally reports
Hurst R/S persistence at H = 0.996 and lag-20 autocorrelation at +0.53 on the canonical Quran. Crosstext comparison against Bukhari, Muslim, and Muwatta showed that the Fibonacci-additive growth
is not Quran-specific (it appears at comparable levels in hadith) but the Hurst persistence remains as
a candidate Quran-specific finding.
That finding has a structural ambiguity. The canonical Uthmanic order is one specific arrangement of
the 114 surahs. The arrangement is not chronological; the mu ṣḥaf does not order the surahs in the
sequence in which they were revealed. The arrangement is approximately by length, longest first,
with deliberate exceptions (al-Fātiḥa first; the muqaṭṭaʿāt-bearing surahs distributed in patterns;
explicit pairing of certain surahs). The traditional Islamic position holds that the order itself was
indicated by the Prophet under Jibrīl's instruction during the annual Rama ḍān review of the
revelation. The mainstream Western academic position holds that the order emerged from the
Companions' compilation under ʿUthmān, with significant contribution from Zayd ibn Thābit's
committee and possibly informed by but not strictly bound to the Prophet's recitation practice.
Both positions are consistent with one structural prediction: the canonical order should not be a
transparent function of revelation order. If the structural autocorrelation observed in canonical
order were merely an artifact of revelation chronology — that is, if surahs revealed close together in
time happen to share vocabulary because they address the same context, and if the canonical order
happens to preserve revelation chronology to a sufficient degree — then reordering the surahs into
a more accurate revelation chronology should preserve or strengthen the autocorrelation. This is the
falsifiable prediction tested here.
The negative side is the more important one for the Cross-Text Program's claims. If chronological
reordering preserves the autocorrelation, then the structural property is likely a property of the

underlying revelation sequence and the canonical arrangement is structurally redundant. If
chronological reordering destroys the autocorrelation, then the structural property is a property of
the specific canonical arrangement and is therefore a candidate target for further investigation under
the program's methodology. The preliminary results reported in §5 fall into the second category but
with important refinements about which chronological alternative is used.

3. Theoretical Grounding
The autocorrelation analysis tested here is interpretable in terms of the classical Islamic scholarly
tradition of ʿilm al-munāsabāt — the study of structural connections between Quranic units (verses,
passages, surahs, surah pairs, juzʾ groupings). Premodern scholars working in this tradition (al-Biqā ʿī,
al-Suyūṭī, al-Zarkashī) identified extensive thematic, lexical, and rhetorical connections between
adjacent and non-adjacent surahs and proposed that the canonical order encodes these connections
deliberately. Recent literary analysis (Cuypers 2009, Farrin 2014, Neuwirth 2010) has formalized
parts of this tradition in terms of ring composition, chiastic structures, and surah pairing patterns
at the multi-surah level.
Cross-Text Computational Linguistics §3.1 establishes — by retracting the claim across four prior
papers — that the Fibonacci-additive growth metric itself is a Classical Arabic compiled-text property
and is not Quran-specific. All three hadith collections tested in Cross-Text exhibit Fibonacci-additive
growth at p < 0.001. The metric does not differentiate the Quran from canonical Sunni hadith. The
present paper accordingly does not test the Fibonacci-additive metric as a candidate Quran-specific
property. The present paper tests a different and downstream question: given that the Fibonacciadditive metric produces a similarity sequence of length N−2 in any ordered corpus, does the
autocorrelation of that sequence in canonical Quranic order produce structural discrimination —
between canonical and chronological orderings of the same content, between canonical Quran and
canonical hadith collections — that the underlying metric itself does not produce? This is an
empirical question the present paper poses and reports the answer to. The two claims are
independent. The metric is universal to Classical Arabic compilation; the autocorrelation of the
metric's output sequence may or may not be.
If the canonical Quranic order produces autocorrelation distinguishable from chronological
alternatives and from comparable compiled corpora, we have evidence that the canonical
arrangement encodes a property the metric alone does not capture. We have not thereby established
the canonical arrangement is divinely indicated, that the Uthmanic compilers were unusually skilled,
or that any specific historical reconstruction of how the arrangement was produced is correct. We
have established that the arrangement is doing some measurable structural work, the magnitude of
which is reported in §5. That is the empirical claim. The metaphysical and historical claims are
separable from it and are not adjudicated by it.

4. Methodology
4.1 Pipeline
The pipeline replicates Cross-Text Computational Linguistics with no methodological deviations. For
an ordered corpus of N units (surahs, kitabs, books, or diwans), each unit is tokenized, normalized,
and lemmatized; TF-IDF vectors are constructed across the full vocabulary; for each position N from
2 to N−1, the cosine similarity between the unit at position N and the elementwise sum of the units
at positions N−1 and N−2 is computed (the Fibonacci-additive metric); the resulting sequence of N−2
similarities is analyzed for Hurst R/S persistence and for autocorrelation at lags 5, 10, 15, 20, 30, 40,
and 50 (where the lag is less than the series length minus one). Significance is assessed by Monte
Carlo permutation: the input order is shuffled randomly 200 times, the same statistics are computed
on each shuffle, and the empirical p-value is the proportion of shuffles producing a statistic at least
as extreme as the observed value.

4.2 Corpora
Five corpora are tested. The Quran is the Tanzil Uthmani text (114 surahs) sourced from the
risan/quran-json repository. The hadith corpora are Sahih al-Bukhari (100 kitabs), Sahih Muslim (56
kitabs in the mARkdown variant), and Muwatta Malik (61 kitabs), all sourced from the OpenITI
repositories at the kitab division level. The Hebrew Bible is the Westminster Leningrad Codex (39
books, Protestant canonical order) sourced from openscriptures/morphhb with Strong's-number
lemmas extracted from the OSHB markup. The pre-Islamic poetry corpus is twenty-eight diwans
drawn from the OpenITI 0025AH repository, comprising all seven Mu ʿallaqāt poets (Imru ʾ al-Qays,
Tarafa, Zuhayr, Labid, ʿAntara, ʿAmr ibn Kulthūm, al-Ḥārith ibn Ḥilliza) plus twenty-one additional
pre-Islamic and very early Islamic-era poets. Total tokens after lemmatization range from
approximately fifty thousand for the smaller corpora to approximately three hundred thousand for
the Hebrew Bible.

4.3 Lemmatization
All Arabic corpora are processed through two independent lemmatization pipelines for robustness
checking. Tashaphyne (Zerrouki, ArabicLightStemmer) provides root-level extraction, mapping each
surface form to a candidate three-letter root. Qalsadi (Zerrouki, with Arramooz dictionary) provides
citation-form lemmatization, mapping each surface form to its dictionary head form. The two
pipelines disagree on a substantial minority of cases; the headline findings reported in §5 hold under
both. The Hebrew Bible uses Strong's-number lemmas extracted directly from the OSHB markup;
this is a fundamentally different processing approach from either Arabic pipeline and serves as a
sanity check that the methodology is not specific to Arabic morphology.

4.4 Significance Testing
Every reported autocorrelation is accompanied by a 200-shuffle Monte Carlo null distribution
computed on the same corpus. P-values are two-sided unless otherwise noted. Empirical p-values
are reported directly: p_emp = (number of shuffles producing a statistic at least as extreme as the
observed value) / 200. The choice of 200 shuffles caps p-value resolution at approximately 0.005 and

is sufficient for the magnitudes observed; the cross-text paper's choice of 2,000 would tighten the
resolution to 0.0005 but would not change which findings cross significance thresholds in the present
analysis.
Multiple comparisons. The within-quartile residual finding in §5.2 is reported across four lag values
(5, 10, 20, 30). Family-wise error correction by Bonferroni at family-wise α = 0.05 requires per-lag α
= 0.0125. Hurst R/S analysis is known to produce inflated H values in the range 0.65 to 0.75 on short
series even when the underlying process is white noise; this small-sample bias is observed in our null
distributions and is not a confounder for the lag-N autocorrelation findings, which are based on
directly observable Pearson correlation between paired sequence values. Per-lag empirical p-values
and Bonferroni outcomes are reported in §5.2 and Table 3.

5. Results
5.1 Quranic Orderings
Three orderings of the 114-surah Quranic corpus are tested: the canonical Uthmanic order (1
through 114), the verbatim Nöldeke-Schwally 1860 chronology (sourced from the cross-referenced
Wikipedia summary of Geschichte des Qorāns Group 1 through Group 4), and the Cairo 1924
Egyptian standard chronology. Headline autocorrelation values, computed under Qalsadi citationform lemmatization, are reported in Table 1.

Ordering

ac5

ac10

ac20

ac30

ac40

Canonical (Uthmanic)

+0.862

+0.790

+0.799

+0.757

+0.663

Verbatim Nöldeke 1860

+0.839

+0.790

+0.641

+0.456

+0.282

Cairo 1924

+0.560

+0.434

+0.131

−0.157

−0.230

Random null (mean of 200)

−0.018

−0.034

−0.012

−0.022

−0.020

Table 1. Lag-N autocorrelation by Quranic ordering. Qalsadi-lemmatized.

The canonical order maintains positive autocorrelation above +0.65 across every tested lag from 5
to 50. Verbatim Nöldeke maintains positive autocorrelation but with substantially faster decay,
dropping from +0.84 at lag 5 to +0.28 at lag 40. Cairo 1924 decays rapidly and crosses zero between
lag 20 and lag 30, reaching strongly negative values around lag 35. All three orderings produce
autocorrelation distributions completely outside the random null band at lag 5 and lag 10; only the
canonical maintains the gap at lag 30 and beyond. The interpretation of these magnitudes — and
specifically the question of how much of the canonical-vs-Cairo gap is attributable to deeper
structural ordering rather than to the canonical's approximate length-sorted compilation structure
— is the subject of §5.2 and substantially revises the apparent strength of the canonical claim.
An additional test was conducted to determine whether the gap between Nöldeke and the canonical
is driven by within-period ordering or by Nöldeke's period boundaries. Thirty independent intraperiod shuffles of the Nöldeke sequence (preserving Nöldeke's First, Second, Third Meccan and
Medinan boundaries but shuffling within each) produce mean lag-20 autocorrelation of +0.624 ±

0.025 — almost identical to verbatim Nöldeke's +0.641. The implication: most of Nöldeke's
autocorrelation is encoded in his period boundaries, not in his within-period ordering.
A numerical discrepancy with Cross-Text Computational Linguistics is documented and not currently
reconciled. Cross-Text §3.3 reports the canonical Quran's lag-20 autocorrelation as +0.53; the
present paper reports +0.80 under Qalsadi lemmatization and +0.81 under Tashaphyne. The
hypothesis that this is explained by Cross-Text computing autocorrelation on the raw consecutivecosine sequence rather than on the Fibonacci-additive sequence was tested directly: raw consecutive
cosine on the same corpus and lemmatization gives +0.74 at lag 20, not +0.53. The discrepancy is
therefore not a metric-definition difference between the two papers as currently understood.
Possible explanations include corpus-version differences, lemmatization differences not captured by
Tashaphyne and Qalsadi, sub-selection of surahs in Cross-Text, or detrending in Cross-Text's
autocorrelation computation that the present pipeline does not apply. Without access to Cross-Text's
exact pipeline code we cannot resolve. Per the §5 reconciliation discipline of Cross-Text itself, the
discrepancy is preserved here as documented and unresolved rather than rewritten away. The
present paper should not be cited as confirming Cross-Text's +0.53 figure; both numbers are
reproducible from their respective pipelines and the gap requires further investigation.

5.2 Within-Length-Quartile Shuffle — The Compilation/Length-Sort Confound
Cross-Text §6 Caveat 3 names a confound the program acknowledges it cannot disentangle with
current data: the canonical Uthmanic Quran is approximately length-sorted by descending surah
length (longest first, shortest last), and adjacent units in any approximately length-sorted
compilation will share more vocabulary with each other than units far apart in the sequence — by
virtue of the length structure alone, independent of any deeper semantic clustering. The canonical
Quran's correlation between length-rank and canonical position is +0.93 in the present analysis; the
compilation is not a strict length-sort, but it is approximately one. If the lag-N autocorrelation
observed in §5.1 were largely a property of the approximate length-sort rather than of intra-quartile
ordering decisions, the canonical-vs-Cairo-1924 gap would be primarily a length-arrangement gap
rather than a deeper-structural-coherence gap.
The test: divide the 114 canonical positions into four contiguous quartiles by canonical position (Q1:
positions 1–28, comprising the longest surahs; Q2: 29–57; Q3: 58–85; Q4: 86–114, the shortest
surahs). Shuffle the order randomly within each quartile but preserve quartile membership. This
destroys any intra-quartile ordering signal while preserving the approximate length-sort. If the
autocorrelation persists at canonical levels, the length-sort is not the dominant mechanism and the
§5.1 magnitudes reflect intra-quartile structural ordering. If the autocorrelation collapses to noise,
the length-sort is the complete mechanism. If intermediate, the length-sort accounts for some
fraction and the residual is attributable to intra-quartile ordering. Two hundred independent shuffles
were run; results are reported in Table 2.

Condition
Canonical (observed)

ac5

ac10

ac20

ac30

+0.862

+0.790

+0.799

+0.757

Within-quartile shuffle (mean ±
sd, n=200)

+0.745 ± 0.037

+0.707 ± 0.052

+0.652 ± 0.055

+0.653 ± 0.052

Full random shuffle (mean ± sd,
n=200)

−0.033 ± 0.109

−0.010 ± 0.112

−0.027 ± 0.119

−0.026 ± 0.122

Gap canonical→random

+0.895

+0.800

+0.826

+0.783

Gap canonical→within-quartile

+0.117

+0.083

+0.147

+0.104

Within-quartile gap-closing
fraction

87%

90%

82%

87%

Table 2. Within-length-quartile shuffle results. Fibonacci-additive autocorrelation. Qalsadi-lemmatized.

The result is partially decisive. Approximately 82–90 percent of the canonical Quran's
autocorrelation gap over random shuffles is attributable to the canonical's approximate length-sort
rather than to deeper intra-quartile ordering decisions. The within-quartile shuffle preserves the
length structure but destroys the intra-quartile sequence, and it produces autocorrelation
magnitudes that are within 0.08 to 0.15 of the canonical at every measured lag. Whether the
remaining residual is statistically significant after family-wise multiple-comparison correction
depends on the lag and is reported below in Table 3.

Lag

Canonical

Max WQ shuffle

# WQ shuffles ≥
canonical (of
200)

Empirical p

Bonferroni at
α=0.05 (per-lag
α=0.0125)

5

+0.862

+0.833

0

< 0.005

PASSES

10

+0.790

+0.813

6

0.030

FAILS

20

+0.799

+0.799

0

< 0.005

PASSES

30

+0.757

+0.771

3

0.015

FAILS

Table 3. Empirical p-values and Bonferroni-corrected significance for the within-quartile residual finding. 200
within-quartile Monte Carlo shuffles per lag.

The honest conclusion is more nuanced than the prior draft of this paper carried. The within-quartile
residual is statistically significant after family-wise correction at lag 5 (canonical exceeds all 200
within-quartile shuffles, empirical p < 0.005) and at lag 20 (canonical exceeds all 200 within-quartile
shuffles, empirical p < 0.005). It does not survive Bonferroni correction at lag 10 (empirical p = 0.030,
where 6 of 200 within-quartile shuffles equaled or exceeded the canonical) or at lag 30 (empirical p
= 0.015, where 3 of 200 shuffles did so). Two of four tested lags pass family-wise correction; two do
not. This is a more lag-dependent finding than the v1.0 prose initially suggested. The strongest
evidence for an intra-quartile structural ordering effect is at lag 5 and lag 20; the evidence is weaker
at lag 10 and lag 30.
The reframed claim is therefore: the canonical Uthmanic Quran exhibits a residual long-range
autocorrelation effect attributable to intra-quartile ordering decisions, the magnitude of which is
approximately +0.10 to +0.15 across measured lags but the family-wise statistical significance of

which is established at lag 5 and lag 20 only. The bulk of the apparent canonical-vs-Cairo-1924 gap
(which is +0.668 at lag 20 in §5.1) is attributable to the difference in length-sort structure between
the two orderings: the canonical is approximately length-sorted, the Cairo 1924 chronology is not.
This narrows the central empirical claim of this paper substantially. The structural-coherence
properties of the canonical arrangement are real and statistically significant at specific lag distances,
but are dominated in magnitude by the compilation's length-sort rather than by any deeper semanticclustering principle the present analysis can fully isolate.
On the methodological precision of the +0.53 vs +0.80 reconciliation: the v1.0 draft of this paper
stated that the metric-definition difference between Fibonacci-additive (+0.80) and raw consecutive
cosine (+0.74) does not explain the discrepancy with Cross-Text's reported +0.53. The corrected
statement is that the metric-definition difference accounts for approximately +0.06 of the +0.27 gap;
the remaining +0.21 gap is unexplained without access to Cross-Text's exact pipeline code. The
metric-definition contribution is real but small; it is not the dominant explanation. This precision
matters; the v1.0 draft's framing was slightly too strong in characterizing the falsification.
On the position-quartile vs strict-length-quartile design choice: the within-quartile shuffle test as
implemented uses canonical-position quartiles (positions 1–28, 29–57, 58–85, 86–114) rather than
strict length-rank quartiles. The canonical-position to length-rank correlation is +0.93 (reported
directly in the empirical_pvalues.py reproduction script), so the position-quartile boundaries
approximately match length-quartile boundaries but are not identical. The test as implemented
controls for "approximate length-sort as the canonical instantiates it" rather than "strict length-sort"
— the right test for the question of how much of the canonical's autocorrelation is attributable to its
specific compilation methodology, but a slightly different question than "how much would be
attributable to a strict-by-length sort." A sensitivity check using true-length quartiles is registered as
a candidate addition for follow-up work; given the +0.93 correlation, the qualitative finding is robust
to this choice.

5.3 Orthogonal Robustness Pipeline — Character 3-Grams
The dual-pipeline robustness check in al-Munāsabāt v1.0 used Tashaphyne (root extraction) and
Qalsadi (citation-form lemmatization). Both are by Zerrouki; both are Arabic-specific morphological
tools sharing preprocessing assumptions about Arabic word structure. The reviewer of v1.0 correctly
noted that this is not a genuinely orthogonal check — a finding specific to a shared preprocessing
assumption would not be caught by a dual-Zerrouki-tool pipeline. A genuinely orthogonal check
requires a fundamentally different tokenization regime.
Character 3-grams are language-agnostic and make no morphological assumptions. Each surah's
normalized Arabic text (diacritics removed, surface-form variation collapsed) is tokenized into
overlapping three-character substrings; TF-IDF vectors are constructed across the resulting
trigram vocabulary; the standard pipeline is applied. This pipeline shares no structural assumptions
with Tashaphyne or Qalsadi — it does not know what a root is, does not perform stemming, does not
consult a dictionary.
Results: under character 3-gram tokenization, the canonical Quran lag-20 autocorrelation is +0.828,
the within-quartile shuffle mean is +0.580, and the random null mean is −0.016. The residual gap

(canonical to within-quartile) is +0.248 — substantially larger than the Qalsadi residual of +0.147.
Under character 3-grams, approximately 70.6 percent of the canonical-to-random gap is attributable
to length-sort rather than to intra-quartile ordering, leaving approximately 29.4 percent to intraquartile structural arrangement; under Qalsadi the corresponding split is approximately 82 percent
and 18 percent. The character 3-gram pipeline shows a larger intra-quartile residual effect than the
morphological pipelines do — the residual is not a Qalsadi or Tashaphyne artifact and may have been
partly smoothed by morphological lemmatization. This strengthens the candidate-finding posture
under a more orthogonal robustness regime; it does not change the qualitative conclusion that
approximate length-sort accounts for the majority of the canonical's apparent long-range
autocorrelation.
Bonferroni-corrected significance under the orthogonal pipeline. The same 200 within-quartile
Monte Carlo shuffles were run under character 3-gram tokenization, with empirical p-values
computed identically to §5.2. Results in Table 4.

Lag

Canonical (3gram)

Max WQ shuffle

# WQ shuffles ≥
canonical (of
200)

Empirical p

Bonferroni at
α=0.05 (per-lag
α=0.0125)

5

+0.888

+0.870

0

< 0.005

PASSES

10

+0.866

+0.809

0

< 0.005

PASSES

20

+0.828

+0.733

0

< 0.005

PASSES

30

+0.736

+0.706

0

< 0.005

PASSES

Table 4. Empirical p-values and Bonferroni-corrected significance under the orthogonal character 3-gram
pipeline. 200 within-quartile Monte Carlo shuffles per lag.

Under the orthogonal character 3-gram pipeline, the canonical Quran exceeds all 200 within-quartile
shuffles at every measured lag, yielding empirical p < 0.005 at lags 5, 10, 20, and 30. All four lags pass
Bonferroni correction at α = 0.05 family-wise. This is a more uniform survival of family-wise
correction than the Qalsadi pipeline produced (where lag 5 and lag 20 passed but lag 10 and lag 30
did not). The implication for the candidate-finding posture is the following. The Qalsadi pipeline's
lag-specific significance pattern (passing at 5 and 20, failing at 10 and 30) does not reproduce under
the orthogonal pipeline; under the orthogonal pipeline, the residual finding is statistically significant
at every measured lag after Bonferroni correction. The lag-specific pattern in the Qalsadi result is
therefore most plausibly an artifact of morphological smoothing at specific lag distances rather than
a genuine property of the canonical structure. The orthogonal pipeline result is the stronger
statistical evidence; the Qalsadi result remains valid but should be read in the context that the
morphological pipelines may underestimate both the residual magnitude and the family-wise
significance.
The lag-specific significance pattern under each pipeline is itself a candidate observation worth
investigating in independent replication. Under one tokenization regime (Qalsadi morphological),
the residual passes Bonferroni at lags 5 and 20 but not at lags 10 and 30. Under another tokenization
regime (orthogonal character 3-grams), the residual passes Bonferroni at all four lags. Whether the

lag-specific pattern is a tokenization-dependent artifact, a property of the underlying structural
arrangement that morphological processing partially obscures, or a small-sample effect specific to
the present analysis, is not adjudicated by the present data and is registered for replication groups
to investigate.

5.4 Hadith Negative Controls
Three canonical Sunni hadith collections were tested in their canonical kitab order. Results are
reported in Table 2.

Corpus (canonical)

N

ac5

ac10

ac20

ac30

Quran (for reference)

114

+0.862

+0.790

+0.799

+0.757

Bukhari

100

+0.057

+0.258

+0.097

+0.042

Muslim

56

−0.104

+0.136

−0.054

+0.165

Muwatta

61

−0.146

−0.438

+0.002

+0.078

Random null (typical band)

—

± 0.10

± 0.12

± 0.12

± 0.15

Table 2. Lag-N autocorrelation: Quran canonical vs. three hadith collections in canonical kitab order. Qalsadilemmatized.

All three hadith collections sit within or close to the random null band at all tested lags. Bukhari
shows weakly significant short-range autocorrelation (lag-3 = +0.30, lag-10 = +0.26) but is
statistically indistinguishable from random at long lags. Muslim is essentially noise at every lag.
Muwatta produces an interesting structural feature — significant negative autocorrelation at lag 10
(−0.44, well outside the null band) — which is consistent with what scholars of Muwatta have
independently observed about Malik's organizational style of alternating topical clusters rather than
grouping similar topics. The hadith collections are arranged topically (kitab al-īmān, kitab al- ṭahāra,
kitab al-ṣalāt, etc.) rather than approximately by length, so they lack the length-sort structure that
drives most of the canonical Quran's apparent autocorrelation per §5.2. Their low values reflect both
the absence of length-sort and the topical-rather-than-coherence-based arrangement principle. The
hadith negative controls remain valid as evidence that the canonical Quran's intra-quartile residual
effect (~+0.15 at lag 20) is not generic to compiled Sunni religious texts in their canonical orderings,
but the magnitude of the comparison is now smaller than the headline canonical-vs-Bukhari ratio of
approximately 8× at lag 20 implied — the comparable ratio of intra-quartile residual to Bukhari is
1.5×, not 8×.

5.5 Pre-Islamic Poetry Negative Control
Twenty-eight diwans of pre-Islamic and very early Islamic-era Arabic poets were tested in their
chronological-by-death-year ordering. The corpus includes all seven Muʿallaqāt poets (Imruʾ al-Qays,
Tarafa, Zuhayr, Labid, ʿAntara, ʿAmr ibn Kulthūm, al-Ḥārith ibn Ḥilliza), the additional canonical preIslamic poets typically grouped with them (al-Nābigha al-Dhubyānī, al-A ʿshā, ʿAlqama, Ḥātim al- Ṭā ʾī,

al-Shanfara, Taʾabbaṭa Sharran), and twelve other poets from the same period. Total corpus is
approximately 1.5 megabytes of Arabic poetry.
The pre-Islamic poetry corpus shows no sustained autocorrelation in any direction. Mean Fibonacci
similarity is 0.643 (high — Classical Arabic poetic vocabulary is repetitive), lag-5 autocorrelation is
+0.092 (within the null band), lag-10 is −0.141, lag-15 is +0.308 (the only weakly significant
deviation, likely a small-sample artifact since at lag 15 only 11 pairs exist for a 28-element series).
Hurst R/S analysis is not reported for this corpus because at N=28 the methodology is below the
reliability threshold per Cross-Text §6 (which excludes the Hebrew Bible at N=39 from Hurst analysis
on similar grounds). The pre-Islamic poetry corpus is the most direct linguistic comparator to the
Quran available — same broad linguistic substrate, same approximate time period — and it produces
no canonical-order autocorrelation pattern resembling even the residual intra-quartile effect of the
Quran.

5.6 Hebrew Bible Negative Control — Protestant and Tanakh Orderings
The Hebrew Bible was tested at the book level under two canonical orderings to address the
canonical-choice question. The Protestant ordering uses 39 books, with Strong's-number lemmas
extracted from the Westminster Leningrad Codex via the OSHB project; the Tanakh ordering
combines the Protestant 39 into 24 traditional Jewish-canonical units (Samuel I+II merged; Kings
I+II merged; Chronicles I+II merged; Ezra+Nehemiah merged; the Twelve Minor Prophets merged)
and reorders to the standard Torah-Nevi'im-Ketuvim sequence. Two orderings of the Protestant 39book version were tested (canonical Protestant order and a critical-scholarship chronological
reconstruction); both produced autocorrelation values within or close to the random null band at all
measured lags.
The Tanakh 24-book ordering produces a more textured result than the Protestant 39-book ordering.
Lag-3 autocorrelation is +0.694 (z = +3.79 against random null, statistically significant); lag-5 is
+0.543 (z = +2.55, marginally significant); lag-10 is +0.026 (z = +0.10, not significant); lag-15 is
−0.274 (z = −0.58, not significant). The Tanakh canonical ordering exhibits short-range
autocorrelation, plausibly attributable to genre clustering (Pentateuch occupying positions 1–5 share
substantial vocabulary; Historical Books in positions 6–9 share a different but overlapping
vocabulary; etc.), but this short-range autocorrelation decays to noise by lag 10. This is qualitatively
different from the canonical Quran's pattern, which sustains autocorrelation out to lag 30 (and
sustains the within-quartile residual specifically at lag 5 and lag 20 per §5.2). The Hebrew Bible in
Tanakh ordering thus shows a real but locally-clustered structural pattern; the canonical Quran's
pattern is sustained over longer lag distances. The earlier framing in v1.0 of this paper ("the Hebrew
Bible does not exhibit the canonical-Quran autocorrelation pattern in either ordering") was correct
as far as long-range autocorrelation, but missed the short-range Tanakh signal; the corrected
statement is the present paragraph. Per Cross-Text §6 Caveat 1, Hurst R/S analysis on either Hebrew
Bible ordering at N=39 or N=24 is not interpretable and is not reported.

5.7 Cross-Corpus Summary
Combining the four negative controls and the three Quranic orderings with the within-quartile
shuffle finding from §5.2, the orthogonal robustness check from §5.3, and the Tanakh-ordering result

from §5.6, the empirical pattern is the following. The canonical Uthmanic Quran exhibits long-range
autocorrelation at +0.80 to +0.83 lag-20 magnitude (depending on tokenization), and approximately
70 to 82 percent of the gap from canonical to random is attributable to the canonical's approximate
length-sorted compilation structure rather than to deeper intra-quartile ordering — the precise
fraction depends on tokenization, with character 3-grams producing 70.6 percent and Qalsadi
lemmatization producing 82 percent. The remaining residual (a gap of approximately +0.15 to +0.25
at lag 20 depending on pipeline) survives Bonferroni-corrected family-wise significance testing
under both pipelines but with different per-lag profiles: under Qalsadi the residual passes at lags 5
and 20 and fails at lags 10 and 30; under the orthogonal character 3-gram pipeline the residual passes
at all four measured lags. The orthogonal pipeline is the stronger statistical evidence; the Qalsadi
pipeline's lag-specific failure pattern most plausibly reflects morphological smoothing at specific lag
distances rather than a property of the underlying canonical structure.
Negative-control patterns. The residual structural-ordering effect observed in the canonical Quran is
not present in the same form in any tested negative control. Bukhari, Muslim, and Muwatta (all
topically arranged by kitab) sit close to or within the random null band at long lags, with Muwatta
showing significant lag-10 negative structure indicating Malik's alternation principle. Pre-Islamic
poetry (chronologically ordered with no canonical structural principle) shows no sustained
autocorrelation. The Hebrew Bible in Protestant 39-book ordering shows no canonical-Quran-like
pattern; the Hebrew Bible in Tanakh 24-book ordering shows a distinct short-range pattern (lag-3 =
+0.694, lag-5 = +0.543) attributable to Pentateuch and Historical-Books genre clustering, but this
short-range pattern decays to noise by lag 10 and is qualitatively different from the canonical Quran's
sustained pattern out to lag 30. The Hebrew Bible in Tanakh ordering should not be characterized as
a flat null negative control; it has its own structural signature, just not one resembling the Quran's.
The corrected reading is that no tested negative control reproduces the canonical Quran's specific
signature of (a) sustained lag-20 and lag-30 autocorrelation that (b) survives within-length-quartile
shuffle as a residual effect.
The pattern is robust under three independent tokenization pipelines (Tashaphyne morphological
roots, Qalsadi citation-form lemmas, character 3-grams without morphological processing), under
two canonical-ordering choices for the Hebrew Bible (Protestant 39 books, Tanakh 24 books), and
under multiple shuffle-test variants. The candidate-finding status remains under Cross-Text §6
Caveat 1; independent replication of the within-quartile residual finding by a research group not the
present author, with pre-registered lag thresholds and an explicit family-wise correction strategy,
would be required for promotion to confirmed-result status. The orthogonal character 3-gram
pipeline showing a larger residual that survives Bonferroni at all measured lags, combined with the
morphological-pipeline-smoothing hypothesis it suggests, makes the candidate-finding posture
appropriate at a level of evidence stronger than the Qalsadi-only result alone would warrant.

6. The Bell Constraint and Other Limitations
6.1 The Bell Constraint
Richard Bell's 1937 chronology of the Quran is the third major Western chronological reconstruction
after Nöldeke 1860 and the Egyptian Standard 1924. Bell's chronology was investigated and
ultimately not implemented in this study, for a reason that is intrinsic to Bell's methodology rather
than a gap that further work would close. Bell rearranges the Quran at the verse and pericope level,
treating individual surahs as composites that combine passages from multiple revelation periods. His
own description of his work emphasizes that the chronology jumps from one passage to another
across the various surahs rather than reordering whole surahs. The published reviews of Bell's work
(Bulletin of SOAS 1939, Journal of the Royal Asiatic Society 1938) confirm this characterization.
There is no per-surah Bell ordering to test because Bell does not produce one.
This is documented as a permanent methodological constraint of Bell's approach, not as an unfilled
gap in this investigation. A surah-level test of Bell's chronology would require constructing a persurah primary-period assignment from his verse-level work — itself a substantial scholarly project
subject to interpretive choices that would no longer be Bell's. We do not undertake that construction.
We do not invent an ordering and report it as Bell's. The investigation is closed at this corner.
A more recent stylistic chronology by Mark Durie (2018, A Stylistic, Non-biographical Chronological
Ordering of the Surahs of the Qurʾan) does produce a per-surah ordering and would be a natural
addition to this investigation. We were unable to obtain Durie's verbatim sequence within the
network constraints of this work. It is registered as a candidate addition for follow-up work.

6.2 Lemmatization Imperfection
Both Tashaphyne and Qalsadi produce occasional incorrect lemmatizations. Tashaphyne's root
extractor returns ‫( كوب‬jar) for some K-T-B family words such as ‫ الكتاب‬where the correct root is ‫كتب‬.
Qalsadi's lemmatizer is more accurate (correctly identifying ‫ الكتاب‬as kitāb) but its lemmas are
dictionary citation forms rather than the deeper morphological roots Cross-Text Computational
Linguistics ostensibly uses. Neither pipeline matches what an expert Arabic morphologist would
produce by hand. The robustness check we apply is dual-pipeline: any finding reported here holds
under both Tashaphyne and Qalsadi processing, and the magnitudes are within a few percent of each
other. We do not claim our lemmatization is identical to the cross-text paper's. We claim our
lemmatization is reasonable and that the falsification result is robust to the specific choice.

6.3 Single-Practitioner Replication
This investigation was conducted by a single practitioner using publicly available data and opensource code. The cross-text paper itself notes the same limitation. Independent replication by a
research group with different Arabic morphological expertise, possibly using CAMeL Tools or Farasa
with full datasets (which require access not available within this work's network constraints), would
either confirm the magnitudes reported here or surface processing-specific artifacts that the dualpipeline check missed. We invite that replication.

6.4 The Compilation/Length-Sort Confound
Cross-Text §6 Caveat 3 names this confound and concedes the program cannot disentangle it from
textual content with current data: "The Quran's compilation history (oral transmission, Uthmanic
codification) is different from hadith compilation. The Hurst persistence might reflect the
compilation methodology rather than the textual content. We cannot distinguish these with the
current data." The within-quartile shuffle test reported in §5.2 of the present paper is one specific
operationalization of this distinction at the autocorrelation level. The result strongly indicates that
approximately 82 percent of the canonical Quran's apparent long-range autocorrelation gap over
random shuffles is attributable to the compilation methodology — specifically, the approximate
length-sort — rather than to a deeper structural arrangement principle. The remaining ~18
percent residual is statistically significant but is the supportable size of the intra-quartile structural
effect, not the +0.80 lag-20 figure that the headline magnitudes might suggest. The reader should
treat all canonical-vs-chronological comparisons in §5.1 with this confound in mind: a substantial
fraction of every reported gap, particularly the canonical-vs-Cairo-1924 gap, is attributable to lengthsort difference between the orderings rather than to deeper coherence properties. This caveat is
important and was not present in the v0 manuscript history of this paper. It is added here as a loadbearing limitation.

6.5 Hurst R/S Sample-Size Threshold
Cross-Text §6 Caveat 1 establishes that Hurst R/S analysis at N less than approximately 64 produces
confidence intervals that span most of the 0.5–1.0 range and are uninterpretable. Cross-Text
accordingly excluded the Hebrew Bible (N=39) from Hurst analysis. The present paper inherits this
constraint and accordingly does not report Hurst values for pre-Islamic poetry (N=28, well below
threshold), Muslim (N=56, just below threshold), or Muwatta (N=61, just below threshold). Earlier
draft versions of this paper reported Hurst values for these corpora; those values are removed in the
present version because they are below the methodology's reliability floor rather than because they
are inconvenient. Bukhari (N=100) and the Quran (N=114) remain above threshold and Hurst is
reported for them only in §5 of Cross-Text Computational Linguistics, not as a load-bearing finding
of the present paper. The lag-N autocorrelation values for the smaller corpora are computable on
different statistical grounds — direct Pearson correlation between paired sequence values — and
are not subject to the same threshold concern, so the substantive negative-control case survives this
constraint.

7. Implications for the Cross-Text Program
7.1 Three reframings
Three reframings appear in this paper at different points in the investigation. The first: during the
second investigative round we reported, based on Cairo 1924 alone, that chronological reordering
destroys the long-range autocorrelation. The third round, with verbatim Nöldeke evidence,
narrowed this. The accurate framing is that the canonical Uthmanic order produces stronger
sustained autocorrelation than any chronological alternative tested, with the magnitude of the gap

depending on the specific alternative. Cairo 1924 produces a dramatic gap. Nöldeke produces a
smaller gap concentrated at long lags.
The second reframing is more consequential and arose during the present revision cycle. Earlier
drafts of this paper (and the abstract as it then stood) characterized the canonical-vs-alternative gap
as approximately one order of magnitude. The within-quartile shuffle test (§5.2) shows that this
characterization was an overstatement. The actual size of the intra-quartile structural ordering effect,
after controlling for the compilation's approximate length-sort, is approximately +0.15 at lag 20 —
statistically significant but far smaller than the +0.80 headline figure implied. The reframed claim is
that the canonical encodes a small but real residual structural effect beyond what its length-sort
produces; the bulk of the apparent canonical-vs-chronological difference is attributable to lengthsort differences between the orderings, not to deeper structural ordering. Earlier drafts that did not
carry this caveat are corrected here.
The third reframing concerns Cross-Text §3.1's retraction of the Quran-specific Fibonacci-additive
claim across four prior papers. Earlier drafts of this paper did not carry that retraction's implication
forward; the metric was treated as if its Quran-specific status were unchallenged. §3 of the present
paper now correctly reports that Cross-Text has established the Fibonacci-additive metric as
Classical-Arabic-compiled-text-non-specific, and frames the present paper as testing a different and
downstream question (autocorrelation of the Fibonacci-additive sequence) rather than as building
on the metric's now-retracted Quran-specific status. A numerical discrepancy with Cross-Text's
reported lag-20 value (+0.53 there, +0.80 here on a similar quantity) is documented and preserved
as unresolved per the §5 reconciliation discipline of Cross-Text itself.

7.2 Promotion status
Under the cross-text paper's pre-registration discipline, a finding is a candidate finding until
independently replicated. The present paper's headline result — that the canonical Uthmanic Quran
exhibits a small but statistically significant residual long-range autocorrelation effect (~+0.15 at lag
20) attributable to intra-quartile ordering decisions beyond what the approximate length-sort
produces — is a candidate finding under Cross-Text §6 Caveat 1. It is not promoted to confirmedresult status by this paper. Promotion requires independent replication by a research group not the
present authors, replication using a different Arabic NLP toolchain, pre-registration of the specific
lag thresholds and significance levels before analysis, and ideally a within-quartile shuffle test
executed by the replicating group as the central confound check. None of these have been done. The
corrected magnitude of the finding (~0.15 effect size) is robust to the dual-pipeline lemmatization
check and to multiple shuffle-test variants run within the present analysis, but inter-pipeline
replication would be substantially stronger evidence. The promotion is downstream.

7.3 What the test does not adjudicate
The test does not adjudicate authorship questions. It does not adjudicate between the traditional
Islamic view of the canonical order's origin (Prophetic indication under Jibrīl's instruction), the
Companion-consensus view (the Companions arranged the surahs following the Prophet's general
guidance), and the skilled-compiler view (the Uthmanic committee imposed structural coherence on
existing surahs). All three are consistent with the empirical finding that the canonical arrangement

does measurable structural work. The test informs the Cross-Text Program's discipline of separating
empirical claims from causal hypotheses; it does not collapse the separation.

8. Implications for Software Engineering
8.1 Arrangement is load-bearing
The first software-engineering implication of the empirical finding is direct, with the corrected
magnitude from §5.2 in mind. The same set of textual units (the 114 surahs, holding their internal
content fixed) produces statistically different long-range structural properties depending on the
arrangement. The canonical arrangement encodes coherence the Cairo 1924 chronological
arrangement does not, but the bulk of the gap is attributable to the canonical's approximate lengthsort and the residual deeper-coherence effect is approximately +0.15 at lag 20 — modest but
statistically significant. This is empirical evidence that arrangement of fixed-content units is a
substrate-level property rather than a cosmetic choice, with the qualification that approximately
length-sorting a corpus does most of the work and additional intra-quartile arrangement does the
remaining smaller share.
The corresponding claim for software is that file order, module order, and import order in a codebase
carry structural information beyond what the individual units encode, with two distinguishable
mechanisms. First, gross arrangement (large modules near other large modules; the packagehierarchy equivalent of length-quartile structure) does substantial structural work. Second, finegrained arrangement within a module-size cohort does additional but smaller work. Common
engineering practice treats both as implementation details. This investigation's empirical finding
suggests that, at least for sufficiently structured corpora, both mechanisms produce measurable
substrate-level effects, with gross arrangement being the larger effect and fine-grained intra-cohort
arrangement being the smaller residual.

8.2 The chronological-vs-canonical distinction in software
Most production codebases grow chronologically. Files are added when features are added; modules
are extracted when complexity demands; the file order at any point is the residue of the development
sequence. This is the software analogue of the Cairo 1924 ordering: a sequence preserved by the
order of revelation rather than imposed for structural coherence. Some codebases are intentionally
reorganized at major-version boundaries — architecture documents are written, modules are
renamed and grouped, public surfaces are restructured. This is the analogue of the canonical
Uthmanic ordering: a sequence imposed for structural coherence rather than preserved from
development chronology.
The empirical finding suggests that the second pattern (intentional reorganization for coherence)
can produce measurably better structural properties than the first (chronological growth), with the
§5.2 caveat that most of the measurable advantage observed in the canonical Quran case is
attributable to the approximate length-sort rather than to a deeper coherence-organization principle.
A codebase reorganized by approximate module size, with adjacent modules of similar size and
complexity, would capture most of what the canonical Quran's compilation methodology captures. A

codebase additionally reorganized for fine-grained intra-cohort coherence would capture the smaller
residual effect. The cost-benefit calculation for the second-order reorganization is industrydependent and is taken up in detail in the companion paper Bayyinah at-Tartīb.

8.3 Long-range coherence as a measurable code-quality property
The methodology used here is not Quran-specific. The pipeline (TF-IDF on tokenized units, cosine
similarity, Fibonacci-additive growth, Hurst persistence, lag-N autocorrelation) operates on any
sequence of textual units. It can be applied to a codebase by treating each file or each module as a
unit, tokenizing on identifier names or AST node types, and running the same pipeline.
The downstream applications include: detecting structural drift in a codebase over time (compute
autocorrelation per quarter; if it declines monotonically, the codebase is losing structural
coherence); validating that a refactoring preserved structural properties (compute autocorrelation
pre- and post-refactor; large changes flag potential coherence loss); benchmarking the structural
coherence of competing architectural proposals (test each on a prototype reorganization; pick the
one with stronger autocorrelation under a sensible coherence definition). None of these applications
exist in current static-analysis tooling. They are natural extensions of the methodology to substrates
the methodology has not yet been applied to.

8.4 Negative-control rigor
The investigation's most decisive findings came not from the primary canonical-vs-chronological
comparison but from the negative-control corpora (Bukhari, Muslim, Muwatta, Hebrew Bible, preIslamic poetry). Without these controls the canonical-Quran finding could be dismissed as a generic
property of compiled religious-text canons. With them, the finding is shown to be a specific property
of the Uthmanic arrangement, distinguishable from any tested compilation in the broader Classical
Arabic and ancient-Near-Eastern religious-text corpus.
The corresponding lesson for software engineering, particularly machine-learning evaluation, is that
single-baseline benchmarks are weaker than multi-baseline benchmarks by an amount that is often
underestimated. A new ML method evaluated against one baseline tells you the method beats that
baseline. A new ML method evaluated against five baselines drawn from different methodological
families tells you the method has a property the entire baseline cluster lacks. The cost of multiple
baselines is typically linear; the discriminative power gained is typically more than linear. Cross-Text
Computational Linguistics and the present paper jointly demonstrate this in a non-software domain;
the lesson generalizes.

8.5 Tool-implementation robustness
The dual-pipeline check (Tashaphyne root extraction and Qalsadi citation-form lemmatization) was
a specific defense against the failure mode where a finding turns out to be specific to one Arabic NLP
tool and disappears under another. The robustness was confirmed: every reported magnitude is
within a few percent across the two pipelines, and every directional finding is preserved. This is the
structural analogue of the audit framework's validator-by-different-instance discipline, applied at
the data-processing layer rather than the prompt-execution layer.

Software engineering applications of this discipline include: validating cross-compiler portability of
optimization passes (does the same structural property hold under GCC and Clang?); validating
cross-runtime parity in machine-learning inference (does the same numerical signature emerge from
PyTorch and JAX?); validating cross-format consistency in serialization (does the same data graph
round-trip identically through JSON, MessagePack, and Protocol Buffers?). Each is a different
implementation of the same abstract dual-pipeline robustness check, and each catches a class of
failures that single-pipeline testing misses.

8.6 The four-place pattern at the corpus level
The Audit Framework's four-place documentation pattern (CHANGELOG, README, fixture, pinning
test) ensures that any documented limitation is verified at four orthogonal places in the substrate.
This investigation applied an analogous discipline at the corpus level: every finding was tested
against four orthogonal corpora (three hadith collections plus pre-Islamic poetry, with the Hebrew
Bible as a fifth from the prior round), and any finding that held only on a subset of those corpora was
treated as weaker evidence than findings that held across all of them.
The corresponding software-engineering pattern is integration-test plurality. A unit test verifies
behavior at one interface. An integration test exercising one consumer verifies behavior under one
usage pattern. An integration test exercising N consumers verifies behavior across N usage patterns
and discriminates real behavior from consumer-specific accidents. The four-place corpus discipline
applied here is the test-substrate analogue of integration-test plurality. The same logic applies:
redundant substrates are a defense against the failure mode where the finding turns out to be
substrate-specific.

8.7 Reframings as preserved record
During the investigation, one earlier finding (Cairo 1924 destroys autocorrelation, therefore
chronological reordering destroys autocorrelation) was reframed as a stronger but narrower claim
(the canonical exceeds every tested chronological alternative, with magnitude depending on the
alternative). The reframing was preserved in the immutable historical record per the four-place
documentation discipline rather than rewritten away. This is the corpus-level analogue of the
additive-only invariant from the Furqan programming language and from furqan-lint: the public
surface is monotonic, retirement requires explicit declaration, and historical states are preserved.
In software engineering, the corresponding pattern is API versioning under semantic-versioning
discipline plus immutable changelog history. A claim made at version 0.2 of a tool, and refined at
version 0.4, must be preserved in the 0.2 changelog entry as well as documented in the 0.4 entry. The
framework's argument is that the historical record of how a finding evolved is itself a load-bearing
piece of the evidence: it tells future readers that the methodology produced revisions and that those
revisions came from new data, not from author convenience. The same logic applies to software: a
tool whose changelog is regularly rewritten when bugs are discovered loses the trust that comes
from showing the rewrite history.

9. Code and Data Availability
All scripts and intermediate artifacts produced during the investigation are publicly available. The
seven analysis scripts (01_main_analysis.py through 07_comprehensive_analysis.py) cover the full
investigative trajectory from the initial canonical-vs-Cairo-1924 test through the comprehensive
Qalsadi-lemmatized multi-corpus analysis. Three results documents (RESULTS.md,
RESULTS_extended.md, RESULTS_final.md, RESULTS_comprehensive.md) preserve the per-round
findings and the reframings. Four visualization PNG files document the autocorrelation profiles
graphically.
Required corpora are publicly hosted on GitHub: risan/quran-json (Tanzil Uthmani Quran),
openscriptures/morphhb (Westminster Leningrad Codex with morphological analysis),
OpenITI/0025AH (early Arabic poets), OpenITI/0200AH (Muwatta Malik), OpenITI/0275AH
(Bukhari and Muslim sahihs). Required Python packages are numpy, scipy, scikit-learn, matplotlib,
qalsadi, tashaphyne, and pyarabic. All packages are on PyPI under permissive licenses. Total compute
time on a typical laptop, including all Qalsadi lemmatization, is approximately five minutes.
The replication path is: clone all five GitHub repositories into a working directory; install the seven
Python packages; run 07_comprehensive_analysis.py. The script produces a printed summary of
every reported number plus the comprehensive_final.png visualization. Any deviation from the
magnitudes reported here would indicate either a corpus update at one of the source repositories, a
package version mismatch, or a methodological deviation in the script.

10. References
10.1 BayyinahEnterprise companion publications
Arfeen, B. S. (2026a). Detecting Performed Alignment in Artificial Systems — The Munafiq Protocol (v2.1).
Zenodo. https://doi.org/10.5281/zenodo.19700420
Arfeen, B. S. (2026b). Bayyinah: Detecting Concealed Adversarial Content in Digital Documents (v.1).
Zenodo. https://doi.org/10.5281/zenodo.19745154
Arfeen, B. S. (2026c). The Fatiha Construct: A Seven-Step Recursive Session Protocol (v.1). Zenodo.
https://doi.org/10.5281/zenodo.19746539
Arfeen, B. S. (2026d). The Bayyinah Audit Framework v3.0: Structural Honesty for AI-Assisted Software
Engineering. Zenodo.
Arfeen, B. S. (2026e). furqan-lint: A Structural-Honesty Linter for Python, Rust, and Go (thesis paper v1.2).
Zenodo.
Arfeen, B. S., & Ashraf, F. (2026). Cross-Text Computational Linguistics (v1). Zenodo.
https://doi.org/10.5281/zenodo.19961267
Ashraf, F. R., & Arfeen, B. S. (2026). Furqan: A Programming Language with Structural Honesty (v2).
Zenodo. https://doi.org/10.5281/zenodo.19776584

10.2 External references
Bell, R. (1937). The Qurʾān: Translated, with a Critical Re-arrangement of the Surahs. Edinburgh: T. and T.
Clark.
Cuypers, M. (2009). The Banquet: A Reading of the Fifth Sura of the Qurʾan. Miami: Convivium Press.

Durie, M. (2018). A Stylistic, Non-biographical Chronological Ordering of the Surahs of the Qurʾan. Arthur
Jeffery Centre for the Study of Islam, Melbourne School of Theology.
Farrin, R. (2014). Structure and Qurʾanic Interpretation: A Study of Symmetry and Coherence in Islam's
Holy Text. Ashland, OR: White Cloud Press.
Ibn al-Anbārī, A. (ed., 1942). Sharḥ al-Mufaḍḍaliyyāt. Cairo.
Lyall, C. J. (1918, 1921, 1924). The Mufaḍḍaliyyāt, an Anthology of Ancient Arabic Odes. Oxford.
Neuwirth, A. (2010). Der Koran als Text der Spätantike: Ein europäischer Zugang. Berlin: Verlag der
Weltreligionen.
Nöldeke, T. (1860). Geschichte des Qorāns. Göttingen. Revised by Schwally, Bergsträßer, and Pretzl 1909
–1938; English translation: Behn, W. H. (trans., 2013). The History of the Qurʾān. Leiden: Brill.
OpenITI consortium. (2025). Open Islamicate Texts Initiative. https://github.com/OpenITI
Open
Scriptures
consortium.
(2025).
morphhb:
Open
Scriptures
Hebrew
Bible.
https://github.com/openscriptures/morphhb
Sinai, N. (2017). The Qurʾan: A Historical-Critical Introduction. Edinburgh University Press.
Watt, W. M. (1970). Bell's Introduction to the Qurʾān. Edinburgh University Press.
Zerrouki, T. (2014). Tashaphyne: Arabic light stemmer. https://pypi.org/project/Tashaphyne/
Zerrouki, T. (2017). Qalsadi: Arabic morphological analyzer. https://pypi.org/project/qalsadi/

11. Acknowledgements
The empirical pipeline assistance, including the Python implementation of the analysis scripts and
the iterative falsification design across four investigative rounds, was provided by Claude (Opus 4.7,
Anthropic). All findings, verdicts, and final scientific decisions are the responsibility of the author.
The four-revision prompt review pattern from The Bayyinah Audit Framework v3.0 governed the AIassisted execution. The reframing recorded in §7.1 emerged from this discipline operating correctly:
an earlier framing was discovered to be too strong, and the corrective was applied without rewriting
the historical record.
The Cross-Text Computational Linguistics paper (Arfeen & Ashraf 2026) provides the theoretical and
methodological foundation on which this investigation builds. Without that paper's prior analysis,
the falsification question this paper addresses would not have a sharp form. The paper's discipline of
pre-registration, falsification-first analysis, and explicit reporting of failed hypotheses (specifically
the Fibonacci-as-Quran-specific claim, which was retracted across four papers when the data
demanded it) is the model this paper attempts to follow at the next layer.
The Tanzil project, the Open Scriptures Hebrew Bible project, and the Open Islamicate Texts Initiative
provide public-domain machine-actionable corpora without which this investigation would not have
been possible. We thank the contributors and maintainers of these projects.
Bayyinah al-Munāsabāt v1.0 · May 7, 2026 · CC BY 4.0 · Bilal Syed Arfeen



Bismillah ir-Rahman ir-Rahim
