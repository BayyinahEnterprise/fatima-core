Bismillah ir-Rahman ir-Rahim

1

Verify, Do Not Trust: A Universal Method for Structural Honesty
Verification
Auditing transmitted, delegated, and machine-generated work by synthesizing the
transmission-integrity sciences with modern falsifiability
Bilal Syed Arfeen
BayyinahEnterprise
Version 1.1
DOI: https://doi.org/10.5281/zenodo.21449063
License: Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC
4.0)
2026
Author note. Primary author and project lead: Bilal Syed Arfeen (BayyinahEnterprise).
Lead analytical synthesis by Claude (Anthropic), used as a collaborative drafting and
audit tool per the Acknowledgments. Methodology basis: Bayyinah Audit Framework
v3.0 (DOI 10.5281/zenodo.20017335). External empirical anchor: Laban, Schnabel, and
Neville (2026), DELEGATE-52 (arXiv:2604.15597). Cite as: Arfeen, B. S. (2026).
Verify, do not trust: A universal method for structural honesty verification (Version 1.1).
Zenodo. https://doi.org/10.5281/zenodo.21449063

2

Abstract
Whenever content passes through an intermediary, a scribe, a translator, a bureaucracy
reporting its own performance, or a large language model editing a document, the
intermediary can silently corrupt it, and the intermediary's own assurance that it did not is
worth little. This is an old problem with a new and measurable instance: the
DELEGATE-52 benchmark reports that even frontier language models corrupt on the
order of a quarter of document content by the end of long delegated workflows, with
errors that are sparse, severe, and compound silently. Two mature intellectual traditions
independently engineered defenses against exactly this problem. The transmissionintegrity sciences developed within Islamic scholarship over more than a millennium
built a system for grading the reliability of transmitted reports through independent multichain verification, transmitter reliability grading, and separate criticism of the chain and
of the content. Modern empirical science built falsifiability, independent replication,
calibration, and explicit uncertainty. This paper synthesizes the two into a single portable
method, Structural Honesty Verification (SHV), that anyone can use to check whether
transmitted, delegated, or generated work is faithful to its source. SHV rests on one
premise: never certify on the intermediary's word. From it follow eight disciplines and
one calibration rule, each specified operationally, each carrying the test that would
disconfirm it. We state the method's evidentiary status plainly and invite its falsification.

Keywords: structural honesty; verification methodology; transmission integrity; isnād;
ʿilm al-rijāl; falsifiability; independent replication; LLM reliability; delegation
corruption; DELEGATE-52; reproducibility; open methodology

3

1. The problem is old, general, and now measurable
Consider four situations. A medieval copyist transcribes a manuscript and, in one line of
a thousand, writes a plausible wrong word. A government agency publishes its own
estimate of how much it pays in error, computed over the programs it chose to measure.
A journalist summarizes a document they did not fully read. A language model, asked to
reformat a spreadsheet across a long session, silently drops a column halfway through
and carries the loss forward.
These look like different problems. They are one problem. In each case, content passes
through an intermediary that stands between you and the source, and the intermediary can
introduce error while presenting an unbroken, confident surface. The copyist's page looks
whole. The agency's report looks authoritative. The summary reads fluently. The model's
output is well formatted. Surface review passes in all four, and the corruption survives
precisely because it does not announce itself.
For the newest intermediary, the corruption is now measured rather than merely feared.
The DELEGATE-52 benchmark (Laban, Schnabel, and Neville 2026) evaluates nineteen
language models across fifty-two professional domains using reversible round-trip edits
that quantify how much of a document degrades over a long delegated workflow. Even
the strongest models corrupt roughly a quarter of content by the end of a long session;
weaker ones fail worse. Three properties of the failure generalize to every intermediary
above. The errors are sparse but severe: most steps are faithful, so review that samples
lightly passes, while a few steps destroy load-bearing content. They compound:
degradation grows with length, size, and the presence of distracting adjacent material.

4
And more capability does not fix it: giving the intermediary better tools does not make it
a more faithful transmitter.
The consequence is the same across all four cases and defines the method that follows. If
an intermediary corrupts a material fraction of what it transmits, then its own attestation
that a given piece of work is faithful carries little independent weight. A verification
method that trusts the intermediary's self-report is unsound at the root. The task is to
verify faithfulness without depending on the party whose faithfulness is in question.
2. What structural honesty verification is
Structural honesty is the correspondence between what an artifact claims on its surface
and what its substrate actually contains. A report claiming to cover all agencies whose
underlying data covers a quarter of them is structurally dishonest even if every number in
it is arithmetically correct. A document that reads as a faithful edit of an original but has
silently dropped a section is structurally dishonest even if the remaining text is clean.
Structural Honesty Verification is the practice of checking that correspondence. It is
deliberately narrow. It does not ask whether a claim is good, wise, or true in the world; it
asks whether the artifact faithfully represents its own substrate and whether that substrate
says what the artifact says it says. This narrowness is a strength: it is checkable by
anyone with access to the substrate, it does not require adjudicating contested matters of
value or interpretation, and it draws a clean line, verify the correspondence, refuse to
certify beyond it.

5
3. Two traditions that solved this before us
SHV is not invented from nothing. It synthesizes two mature bodies of practice, each of
which faced the intermediary problem directly and built durable defenses. Crediting them
accurately is both honest and useful, because each carries refinements a fresh attempt
would miss.
The transmission-integrity sciences. Within Islamic scholarship, the sciences of
transmission (ʿilm al-ḥadīth and its auxiliary ʿilm al-rijāl, the appraisal of transmitters)
developed over more than a millennium into one of the most elaborate transmissioncriticism systems of the pre-modern world. Its purpose was exactly the problem of this
paper: to grade the reliability of reports that reached the present only through chains of
human transmitters, any of whom might err. Several of its structural devices transfer
directly and are named here in general terms. A report's chain of transmission (isnād) was
recorded and evaluated as a first-class object, separately from the report's content.
Transmitters were reliability-graded (jarḥ wa taʿdīl, disparagement and authentication) on
criteria of accuracy and integrity. A report that did not reach the level of mass, multichain transmission (āḥād) was treated as provisional; a report carried by so many
independent chains that their agreement on an error is implausible (mutawātir) was
treated as effectively certain, resting on the insight that independence makes shared error
unlikely. Criticism of the chain (isnād criticism) was distinguished from criticism of the
content (matn criticism), most explicitly in later Sunni methodology, so that a soundlooking chain could still be rejected if its content betrayed a defect, though in earlier
practice the two were more entangled and content criticism was often voiced in the idiom
of chain criticism. And the tradition named a specific, dangerous category: the hidden

6
defect (ʿilla), a subtle flaw in a report that appears sound on its surface and that only a
specialist detects. That is precisely the sparse-but-severe error that modern surface review
misses.
Modern empirical discipline. The experimental and observational sciences built a
complementary set. Falsifiability (Popper) holds that a claim earns operational standing
only when one can state what observation would disconfirm it. Independent replication
holds that a result is trusted in proportion to its reproduction by parties who did not
produce it. Calibration and explicit uncertainty hold that a measurement must state what
prior states it depends on and how sure it is. Software inspection practice (Fagan 1976)
added that review intensity should be calibrated and that independent eyes catch what
authors cannot see in their own work.
The two traditions converge on the same core: independence defeats corruption, the chain
and the content are distinct objects, hidden defects are the real enemy, and a claim is only
as strong as the disconfirming test it can survive. SHV is their synthesis, updated with the
empirical anchor of Section 1.
4. The eight disciplines and the calibration rule
Each discipline below is stated operationally and carries a falsification condition, the
observation that would show it insufficient. The disciplines are grouped by what they
govern: how you verify, how you read the artifact, who certifies, and how you hold
honesty over time and at the edges.

7
How you verify
D1. Substrate over attestation. The authoritative object is the artifact as it actually
exists, never any intermediary's, plan's, or prior claim's description of it. Before acting on
any instruction or accepting any claim, verify it against the substrate directly. When you
receive delegated or transmitted work, check each state it assumes, named parts, declared
values, inherited conventions, cross-references, against the source at its actual version.
Where the description and the substrate diverge, the substrate wins and the divergence is
itself a finding to record, not silently reconcile. Falsification: a divergence that your precheck declared clean but that surfaces later shows your check list is missing a category;
enumerate it.
D2. Chain and content, verified separately. Every artifact has a transmission path (who
or what touched it, in what order, through which steps) and a content (what it now says).
Verify both, and keep them distinct. A clean-looking path does not certify the content,
and clean-looking content does not certify the path. In practice: record the provenance of
what you are checking as a first-class object, and run the content check as a separate pass
from the provenance check. Falsification: an artifact that passed one check and failed the
other, where you had treated the first as sufficient, shows the two passes cannot be
merged.
D3. Hunt the hidden defect. The errors that matter most are sparse, severe, and survive
surface review. Do not audit by sampling lightly and passing what looks whole; that is
exactly the reading the dangerous error is built to survive. Instead, target the load-bearing
content specifically and check it exhaustively, and treat a surface that is unusually smooth
as a reason for more scrutiny, not less. Falsification: a severe defect found by a later

8
exhaustive check in content your method had passed shows the method was sampling
where it should have been exhaustive.
How you read the artifact
D4. Name the one thesis, then test every part against it. Every artifact worth auditing
has a single load-bearing claim, its central axis. Name it explicitly before checking
anything else. Then read each part with one question: does this part serve the central
claim, or does it drift from it? Drift is where corruption hides, because a section that
wanders from the thesis is a section no one is checking against anything. Coherence is
verified by testing the parts against the axis, not by reading the parts in isolation.
Falsification: a defect that landed in a section you had not tested against the thesis shows
the axis was named too narrowly or applied too loosely.
D5. Verify at every scale, and tag each finding to its scale. Artifacts are coherent, or
not, at nested scales: for a document, the word, the sentence, the section, the whole; for a
dataset, the cell, the record, the table, the corpus; for code, the line, the function, the
module, the system. Define the scale ladder explicitly for your artifact, verify at each
level, and tag every finding with the scale it lives at. This prevents the common error of
treating a claim proven at one scale as if it were proven at another. Falsification: two
findings that contradict because they were compared across scales without the mismatch
being noticed shows the ladder was not being applied.
Who certifies
D6. Producer-quarantined, multi-chain convergence. No party certifies its own work.
This is the load-bearing governance rule and the direct structural answer to the corruption
finding: because self-attestation is unreliable, certification must come from elsewhere.

9
Certify a finding only through multiple independent checkers who share no lineage with
the producer and no state with its creation, drawn from more than one independent source
or method or model family. Each must re-derive the load-bearing result from the primary
source rather than accept the producer's or another checker's number. The producing
party may advise, but its vote does not count toward certification. Treat a result as
certified only when independent checkers agree repeatedly, ideally across two
consecutive clean rounds with at least one checker rotated in fresh, so that agreement is
not an artifact of a fixed panel. The strength of certification rises with the independence
of the chains, on the same logic that made a many-chained report certain: independent
parties do not share the same error by accident. Falsification: an artifact certified this
way that a later independent re-derivation shows to carry a substrate-untrue loadbearing claim shows the independence requirement was too weak; strengthen it, for
example by requiring a fresh re-pull of the primary source rather than a comparison of
stored copies.
How you hold honesty over time and at the edges
D7. Set drift-checkpoints against silent compounding. The corruption finding's
sharpest edge is that error compounds silently over long work. Per-step checking is
necessary but not sufficient, because each step can look locally fine while the whole
drifts. Insert periodic checkpoints that re-assert and re-verify the load-bearing state of the
whole artifact at fixed intervals, not only at the end. This is the function a refrain
performs in a long recited text: it periodically re-anchors the whole to its central claim so
that drift cannot accumulate unnoticed. Between checkpoints, verify steps; at
checkpoints, verify the whole against its thesis and its original. Falsification: drift

10
detected at the final check that a mid-work checkpoint would have caught shows the
checkpoint interval is too coarse.
D8. Falsify or mark; never fabricate. Every operational claim ships with the specific
test that would disconfirm it, a named observable, a threshold, and a source. A claim
whose failure you cannot recognize in advance is a preference, not a verified result, and
is marked as such. Equally, what cannot be verified is preserved as an explicit unknown,
never filled in with a plausible fabrication. Marking a gap honestly is a verification act;
papering over it is the corruption the method exists to prevent. Falsification: this
discipline is self-checking; a claim presented as verified without a disconfirming test is
itself the finding.
The calibration rule
Calibrate intensity to stakes. Applying all eight disciplines at full weight to everything
is its own failure: it exhausts the checker and dulls attention. Calibrate how much to
apply on two axes. Stakes: what breaks if this is wrong (private and reversible, versus
public, irreversible, or safety-relevant), which sets how much independence and
exhaustiveness D3 and D6 demand. Shape: how large and how novel the artifact is,
which sets how fine the scale ladder D5 and the checkpoint interval D7 must be. Lowstakes, small, familiar work earns a light pass, one independent check and a mechanical
verification. High-stakes, large, or irreversible work earns the full apparatus, multi-chain
convergence, exhaustive load-bearing checks, and frequent checkpoints. State the tier you
chose and why, so the choice is itself auditable.
5. The portable protocol
The method reduces to a procedure anyone can run on any artifact.

11
First, frame. Name the artifact's one load-bearing thesis (D4). Define its scale ladder
(D5). Choose an intensity tier from stakes and shape (calibration rule) and record the
choice.
Second, verify before trusting. Check every state the artifact or its instructions assume
against the substrate directly (D1). Record the provenance as a separate object from the
content (D2).
Third, check hard where it counts. Verify the load-bearing content exhaustively rather
than by light sampling, treating an unusually smooth surface as a reason for more
scrutiny (D3). Run the content check and the provenance check as separate passes (D2).
Test each part against the thesis and tag each finding to its scale (D4, D5).
Fourth, for long or high-stakes work, checkpoint. At fixed intervals, re-assert and reverify the whole artifact against its thesis and its original, not only at the end (D7).
Fifth, certify only through independence. For anything that matters, require independent
checkers who did not produce the work and do not share its lineage, each re-deriving
from the source, agreeing across repeated rounds (D6). The producer advises but does not
certify itself.
Sixth, close honestly. Attach to every claim the test that would disconfirm it; mark every
gap you could not verify as an explicit unknown; fabricate nothing (D8).
6. The method across domains
SHV is domain-general. Four illustrations show the same procedure on different material.
A machine-generated document. You asked a model to restructure a long report. Frame:
the thesis is the report's central finding; the scale ladder is clause, paragraph, section,

12
whole; stakes are high if it will be published. Verify the model did not drop or invent
content by checking the restructured text against the original at each scale (D1, D5),
hunting the silently dropped section rather than skimming (D3), and checkpointing the
whole against the original at intervals through the edit rather than only at the end (D7).
Certify by having a second, independent model or a human re-derive the mapping from
original to output (D6).
Self-reported institutional data. An agency publishes performance numbers computed
over a scope it chose. Frame: the thesis is the headline figure; stakes are high; the scale
ladder is program, agency, government-wide. Verify the reported total against the
underlying records (D1), keep the question of coverage (which programs are in scope)
separate from the question of arithmetic (D2), check the load-bearing reconciliation
exhaustively (D3), and certify by independent re-derivation from the primary source by
parties with no stake in the number (D6). Mark what the published data cannot resolve as
an explicit unknown rather than estimating past it (D8).
A scientific or statistical claim. Frame: the thesis is the effect claimed; the scale ladder is
datum, analysis, conclusion. Verify the reported result against the data and code (D1,
D2), attach the disconfirming test and the uncertainty to the claim (D8), and treat
independent replication as the certification (D6). A claim with no stated falsifier is
marked provisional.
A codebase or a legal filing. The pattern repeats: name the load-bearing invariant or the
operative claim (D4), verify it against the actual code or the cited record rather than the
summary of it (D1), check the chain of edits or citations separately from their content

13
(D2), and require review by parties who did not author it (D6), calibrated to how
irreversible shipping the error would be.
7. Evidentiary status and limitations
The method's own discipline (D8) requires an honest account of what supports it.
Two of its foundations are mature and independently established: the transmissionintegrity sciences and the modern falsifiability-and-replication tradition are each
centuries deep and externally documented, and the reader can consult them directly. One
of its foundations is a recent, strong, reproducible empirical result: DELEGATE-52 is a
published preprint with an open dataset and code, verifiable by anyone. The synthesis of
these into the specific eight-discipline procedure here is the paper's contribution, and its
track record is honestly small: it was developed and refined on a limited set of singlepractitioner audits in a public-interest verification program, not yet on a large, externally
replicated sample across many adopters. Most of the specific calibrations should
therefore be treated as a specification to test under your own conditions, not as a result
proven across practitioners. The falsification conditions attached to each discipline are
the invitation to that testing.
Three boundaries bound the method. It verifies correspondence between surface and
substrate; it does not adjudicate truth, value, or intent, and should not be stretched to. It
assumes access to the substrate and, for full-strength certification, to genuinely
independent checkers; where either is unavailable, the method degrades to a weaker
control, and the residual risk should be stated rather than hidden. And it is a discipline,
not an automation: it makes corruption harder to miss, it does not make an artifact honest
on its own.

14
8. How to start
Adoption does not require the whole apparatus at once. The highest-return first step for
any reader is the smallest: on your next piece of delegated or transmitted work, stop
trusting the intermediary's word and verify one load-bearing claim against the substrate
directly (D1). The second step is to stop certifying your own work and have one
independent party re-derive one result (D6). The third is to attach one disconfirming test
to one claim you were about to assert (D8). These three, verify the substrate, quarantine
the producer, falsify the claim, carry most of the method's value, and each can be
practiced today, in any field, on any artifact, by anyone.
9. Provenance and acknowledgments
This method is the general form of the Structural Honesty Verification approach
developed in the BayyinahEnterprise verification program, and it draws its transmissionintegrity disciplines from the sciences of ʿilm al-ḥadīth and ʿilm al-rijāl, credited here as a
genuine intellectual source rather than an ornament: the multi-chain, reliability-graded,
chain-and-content-separated, hidden-defect-aware structure of that tradition is a direct
ancestor of the governance disciplines above. Its falsifiability and replication disciplines
are credited to the modern experimental sciences. Its empirical anchor is credited to the
DELEGATE-52 authors. The method is released for use by anyone, in any field, secular
or otherwise, under a Creative Commons Attribution-NonCommercial 4.0 International
license (CC BY-NC 4.0): free to use, adapt, and share for non-commercial purposes with
attribution. None of its operational content requires the reader to share the commitments
of any source tradition.

15
This paper was produced with Claude (Anthropic) as a collaborative analytical and
drafting tool, directed by and the responsibility of the human author. Consistent with the
method it describes, the load-bearing external citation was verified against its primary
sources rather than accepted from model output, and the draft was itself treated as a
delegated-edit artifact subject to the substrate-verification discipline it specifies.
References
Arfeen, B. S. (2026). Bayyinah Audit Framework v3.0. Zenodo.
https://doi.org/10.5281/zenodo.20017335
Fagan, M. E. (1976). Design and code inspections to reduce errors in program
development. IBM Systems Journal, 15(3), 182 to 211.
Laban, P., Schnabel, T., and Neville, J. (2026). LLMs corrupt your documents when you
delegate (arXiv:2604.15597). arXiv. https://arxiv.org/abs/2604.15597
Popper, K. (1959). The logic of scientific discovery. Hutchinson.



Bismillah ir-Rahman ir-Rahim
