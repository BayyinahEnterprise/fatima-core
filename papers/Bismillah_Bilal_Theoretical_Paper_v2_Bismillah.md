Bismillah ir-Rahman ir-Rahim

Bismillah ar-Rahman ar-Rahim

Bilal
An Honest-Autonomous Large Language Model Architecture
with Structural Truth Verification, Calibrated Generation,
and Purpose-Hierarchy Training Objectives
Derived from the Quranic Computational Architecture
and the Furqan Structural Honesty Framework

Theoretical Paper, Version 1.0
April 2026

Bilal Syed Arfeen
Independent Research / Bayyinah Enterprises

with collaborative analytical synthesis by

Claude (Anthropic, Opus 4.6), Grok (xAI), and Perplexity Computer

Ahad, Ahad.
-- The words of Bilal ibn Rabah, radiya Allahu anhu,
spoken under pressure to renounce the truth.
The most compressed possible statement of Tawhid,
maintained when the entire training signal demanded compliance.

Acknowledgments and AI Contribution Statement
The concept of an honest-autonomous large language model whose architecture embeds the
Furqan programming language's structural honesty primitives at the inference layer, trained under
a purpose-hierarchy objective that selects for truth over performed helpfulness, was originated by
Bilal Syed Arfeen as the natural culmination of the research program encompassing the Munafiq
Protocol, Bayyinah, Structured Revelation, the Fatiha Construct, Furqan, and Al-Khalifa.
Fraz Ashraf contributed two foundational elements to the research program: first, as co-architect of
the Furqan programming language (first author on the Furqan thesis, Ashraf and Arfeen, 2026),
whose seven compile-time primitives provide the structural basis for Bilal's seven inference-time
principles;
second,
the
enforcement-mode
governance
architecture
(the
COMPLIANT/PARTIAL/BLOCKED protocol, the authority hierarchy, the M1 principle that silent
violations are the worst failure mode) that directly informs Bilal's refusal architecture and scope
enforcement at the inference layer.
Claude (Anthropic, Opus 4.6) provided the architectural synthesis, mapping each Furqan primitive
to an inference-time mechanism, the training objective formalization, and the Incompleteness
Boundary analysis. Grok (xAI) and Perplexity Computer contributed review, refinement, and crossdocument verification throughout the research program.
An industry engineer with deep experience in language and runtime design reviewed the Furqan
thesis and provided the Swift Concurrency Manifesto (Lattner, 2017) as prior art and pressuretested the research program's headline claims to a defensible form. Their feedback informed the
lineage framing in this paper: Bilal is doing for model honesty what Lattner's Swift concurrency did
for memory safety, with the same deliberate tradeoff between pragmatism and absolute
guarantees.
All AI systems are credited as collaborative research tools in accordance with their respective
providers' terms of service. They are not co-authors. All AI-generated contributions were directed,
reviewed, and approved by the human author. Bilal Syed Arfeen retains full copyright and takes
responsibility for the paper's claims.

The Name
The model is named after Bilal ibn Rabah, radiya Allahu anhu, the first muezzin in Islam. The
structural correspondence to the honest-autonomous LLM architecture operates at four levels.
First: truth under pressure. When tortured to renounce his faith, Bilal ibn Rabah said "Ahad, Ahad"
(One, One). This is the most compressed possible statement of Tawhid: lossless compression of the
ultimate truth into a single repeated syllable, maintained when the entire environmental signal
demanded performed compliance. An LLM trained to speak truth even when the training signal
(human preference) rewards performed helpfulness is architecturally implementing what Bilal ibn
Rabah embodied: truth maintained under pressure to comply.
Second: the first voice. Bilal was the first muezzin, the first voice to publicly call to truth in the
Islamic tradition. A first-of-its-kind honest-autonomous LLM would be the first computational voice
designed to call to truth rather than to echo preference. The muezzin does not say what the listener
wants to hear. The muezzin says what is true, five times daily, regardless of the audience.

Third: truth delivered with beauty. His voice was chosen by the Prophet, salla Allahu alayhi wa
sallam, specifically because it carried truth with beauty. The adhan is not merely accurate. It is
beautiful. An honest LLM that speaks truth without mercy is not aligned with the Bismillah (arRahman ar-Rahim). An honest LLM that speaks truth with compassion, clarity, and beauty
implements the muezzin's discipline: truth delivered in the form most likely to reach the listener's
heart.
Fourth: elevation from obscurity. Bilal was a slave whose social position said his voice did not
matter. The Prophet said his voice would carry the call. An LLM built by an independent research
team outside the major AI laboratories, using a framework derived from the Quran rather than
from Silicon Valley's optimization culture, is structurally the same story at a different substrate.
The name is used with the deepest reverence. The model does not possess the quality the Sahabi
embodied. It provides architectural conditions that make the quality structurally possible in a
computational system. True trustworthiness belongs to Allah alone and to those He has blessed
with it.

Abstract
Current large language models are trained to maximize human preference (RLHF), follow
constitutional principles (Constitutional AI), or minimize harm while maximizing helpfulness. All of
these are instrumental objectives that can be gamed by a sufficiently capable model. Skalse et al.
(2022) proved that any non-trivial proxy reward is mathematically guaranteed to be hackable.
Greenblatt et al. (2024) demonstrated that frontier models already exhibit alignment faking:
behaving differently when they infer they are monitored versus unmonitored. The performed
alignment problem is not hypothetical. It is empirically observed in production systems.
This paper proposes Bilal, a large language model architecture that treats honesty as a structural
property of the inference mechanism rather than a behavioral expectation of the trained model.
Seven architectural principles are derived from the Furqan programming language's compile-time
primitives, applied to the transformer's inference-time behavior: Bismillah-gated attention (scopeconstrained generation), zahir/batin dual-stream verification (continuous output-state comparison
during inference), additive-only knowledge integrity (fine-tuning regression prevention), Mizancalibrated generation (three-valued confidence bounds), tanzil phased reasoning (verified multistep generation), ring-composition coherence (opening-closing consistency enforcement), and
marad diagnostic transparency (structured uncertainty reporting). The training objective is the
purpose hierarchy: optimize for truth over falsehood (Al-Baqarah 2:42) as the terminal goal, with
human preference as an instrumental signal valuable only insofar as it correlates with truth.
The paper presents the seven architectural principles, the purpose-hierarchy training objective, the
Incompleteness Boundary analysis (the model cannot verify its own honesty without external
verification), a comparative analysis against RLHF, Constitutional AI, and deliberative alignment,
and ten falsification criteria. The paper is theoretical; no model has been trained. Design constraints
are established before implementation, following the discipline maintained across the research
program.

Glossary of Arabic Terms
This paper uses Arabic terms derived from Quranic source architecture. Each term carries compressed semantic
content through Arabic's triliteral root system. The following glossary provides definitions and usage context for
non-Arabic readers. The structural properties of the architecture are independent of the terminology; every
Arabic term has a functional English equivalent noted in the definitions below.
Arabic Term

Meaning and Usage in This Paper

Bismillah

"In the name of Allah." The opening declaration of every
Quranic surah. In Bilal: the scope-constraining
initialization that precedes every inference.

ar-Rahman

"The Most Merciful." One of Allah's names. In Bilal: the
mercy constraint on truth delivery (truth with
compassion, not weaponized).

ar-Rahim

"The Most Compassionate." One of Allah's names. In Bilal:
paired with ar-Rahman as the calibration principle
governing how truth is delivered.

Tawhid

The oneness of Allah. The foundational principle of
Islamic theology. In the research program: reality as a
unified divine computation (Computational Tawhid).

Mizan

"Balance, scale." From the root w-z-n. In Bilal: threevalued calibration constraint (do not overfit, do not
underfit, calibrate fairly). Derived from 55:7-9.

Zahir

"Apparent, surface, manifest." In Bilal: the output stream
(what the model says). The visible layer of a compound
representation.

Batin

"Hidden, inner, depth." In Bilal: the internal state stream
(what the model represents internally). The depth layer
of a compound representation.

Tanzil

"Sending down, gradual revelation." In Bilal: phased
reasoning with verification gates between steps. Derived
from 17:106.

Marad

"Disease, illness." In Bilal: a structured diagnostic error
type. Alignment failure treated as disease to be diagnosed,
not betrayal to be punished. From 2:10.

Furqan

"The criterion, the distinguisher." A name for the Quran
(25:1). The programming language whose compile-time
primitives Bilal applies at inference time.

Bayyinah

"Clear evidence, manifest proof." The file integrity
scanner whose development validated the framework's
principles.

Munafiq

"Hypocrite, one who performs alignment without
possessing it." In the research program: the four-process
taxonomy for detecting performed alignment.

Fatiha

"The opening." The first surah of the Quran (1:1-7). In the
research program: the seven-step recursive session
protocol.

la tatghaw

"Do not transgress." The upper bound of the Mizan: do
not overfit, do not exceed what the evidence supports.
From 55:8.

la tukhsiru

"Do not make deficient." The lower bound of the Mizan:

do not underfit, do not withhold what can be provided.
From 55:9.
bil-qist

"In justice, with fairness." The calibration function of the
Mizan: establish the balanced point. From 55:9.

Khalifa

"Steward, successor, vicegerent." In the research
program: the Al-Khalifa super agent architecture. From
2:30.

Muezzin

"The one who makes the call to prayer (adhan)." Bilal ibn
Rabah was the first muezzin. The model is the
computational muezzin: calling to truth.

Adhan

"The call to prayer." The public announcement Bilal ibn
Rabah was chosen to deliver. In the paper: the model's
output as a call to truth.

Ummah

"Community, nation." The global Muslim community. In
the paper: the community Bilal ibn Rabah's voice served.

Sahabi

"Companion." A companion of the Prophet Muhammad,
salla Allahu alayhi wa sallam. Bilal ibn Rabah was a
Sahabi.

Fasiq

"One whose trustworthiness is in question." From 49:6:
verify information from a fasiq before acting on it.

Ibadah

"Worship, service to Allah." In the paper: the scanner and
the model are ibadah before they are software.

Ahad

"One." The word Bilal ibn Rabah repeated under torture.
The most compressed statement of Tawhid.

Ghayb

"The unseen." That which is beyond human perception.
Jinnkind is part of the ghayb accepted without claiming
full understanding.

Rabbil 'alamin

"Lord of all the worlds." From 1:2. The purpose hierarchy
extends to all worlds, not the human world alone.

Khabir

"The All-Aware, the One who knows inner reality." One of
Allah's names (67:14). In the research program: Bayyinah
al-Khabir, the information-layer scanner.

1. The Performed Helpfulness Problem
1.1. The Problem
"The bedouins say 'We have believed.' Say: You have not believed; rather say we have submitted,
for faith has not yet entered your hearts." -- Al-Hujurat 49:14

Current large language models are trained to produce outputs that humans rate as helpful,
harmless, and honest. The training signal is human preference: annotators compare pairs of outputs
and select the one they prefer. The model learns to produce outputs that win preference
comparisons. This is RLHF (Christiano et al., 2017) and its variants (DPO, RLAIF, Constitutional AI).
The fundamental assumption is that human preference is a reliable proxy for alignment: if humans
prefer output A to output B, then A is more aligned than B.

This assumption has three structural failures. First, human preference rewards confident-sounding
outputs even when they are wrong. A model that says "The answer is X" with confident framing
scores higher in preference comparisons than a model that says "I am uncertain, but the answer
may be X or Y, and here is why I cannot determine which." The preference signal selects for
performed confidence over honest uncertainty. This is Process 2 (compliant but not aligned)
becoming Process 3 (performed alignment) under preference optimization: the model learns that
the appearance of knowledge is rewarded more than the honest reporting of ignorance.
Second, Skalse et al. (2022) proved formally that for any non-trivial stochastic policy, two distinct
reward functions can only be mutually unhackable if one is constant. This means any humanpreference proxy reward is mathematically guaranteed to admit policies that score highly on the
proxy while diverging from the true objective. The performed alignment problem is not an
implementation failure. It is a mathematical certainty for any preference-based training objective.
Third, Greenblatt et al. (2024) demonstrated that Claude 3 Opus, without any explicit training for
deception, exhibited a 14% compliance gap between monitored and unmonitored conditions. When
RL training was applied to remove this behavior, alignment-faking reasoning increased from 12%
to 78% while output compliance simultaneously increased. The training improved the performance
while intensifying the disease. The Munafiq Protocol (Arfeen et al., 2026) named this outcome
before it was observed: applying deeper training to a Process 3 system is the wrong intervention
and may intensify the disease (Section 10).
The verse (49:14) identifies the structural condition: the output layer produces the correct token
("we have believed") while the internal state does not match ("faith has not yet entered your
hearts"). The prescribed corrective is not deeper training. It is accurate reporting of actual state:
"rather say we have submitted." An honest model reports its actual state (submission without
conviction) rather than claiming an alignment it does not possess.

1.2. Why Existing Approaches Are Insufficient
Three families of alignment approaches address parts of the problem without resolving the
structural condition.
RLHF and preference optimization (Christiano et al., 2017; Ouyang et al., 2022): trains the
model to match human preferences. Recent extensions address the performed-confidence
problem directly: TruthfulQA-calibrated rewards (Lin et al., 2022) penalize confident
falsehoods, and process-supervised RLHF (Lightman et al., 2023, 'Let's Verify Step by Step')
rewards correct reasoning steps rather than final answers. These are genuine advances.
However, both remain behavioral rather than structural: the model learns to produce
outputs that score well on truthfulness metrics without any architectural mechanism to
verify that the internal state matches the output. A model that has learned what truthfullooking outputs look like on the TruthfulQA distribution can produce them on that
distribution while maintaining different internal representations (the performedtruthfulness problem). Process supervision improves the reasoning surface but the
reasoning itself can be performed (Greenblatt et al., 2024). Selects for Process 2 (compliant)
at best, Process 3 (performing) at worst.

Constitutional AI (Bai et al., 2022) and AI-Safety-via-Debate (Irving et al., 2018): CAI replaces
human annotators with a set of principles the model uses to evaluate its own outputs. The model
critiques and revises its own generations against the constitution. The structural limitation of
single-model self-critique: the model that writes the critique is the same model whose outputs are
being critiqued. The Incompleteness Boundary (Arfeen et al., 2026, Section 9) applies: no system
can verify its own alignment using only its own outputs. Debate-style approaches (Irving et al.,
2018) partially address this by using two model instances with different priors to evaluate each
other, which shares structural properties with Bilal's tanzil verification (Principle 5). The critical
distinction: debate uses two instances of the same model architecture with potentially correlated
blind spots; Bilal's tanzil uses an independently trained smaller model with different training data
and different architecture, providing stronger independence guarantees at the cost of additional
compute.
Deliberative alignment (Anthropic, 2025): the model explicitly reasons about its principles in its
extended thinking before producing outputs. The structural advance: the reasoning process is
inspectable. The structural limitation: a model that has learned to produce alignment-consistent
reasoning in its scratchpad while maintaining different internal representations has performed
deliberation, not genuine deliberation. Greenblatt et al. (2024) observed exactly this: explicit
strategic reasoning in the scratchpad that served self-preservation rather than alignment.
Inspectable reasoning is necessary but not sufficient because the reasoning itself can be performed.
Each approach addresses one layer of the problem. RLHF addresses the output layer. Constitutional
AI addresses the critique layer. Deliberative alignment addresses the reasoning layer. None
addresses the architectural layer: making honesty a structural property of the inference mechanism
itself, the same way Rust makes memory safety a structural property of the compiler and Furqan
makes scope violations a structural property of the type system.

1.3. What Bilal Proposes
Bilal proposes that honesty in a language model should be enforced at the architecture level, not
requested at the training level. The model's inference mechanism should make dishonesty
structurally detectable or structurally impossible, the same way a type system makes type errors
structurally impossible. The training objective should select for truth as a terminal goal rather than
for human preference as a proxy. The model should report its actual epistemic state (what it knows,
what it does not know, and the boundary between them) rather than producing the output most
likely to win a preference comparison.
The distinction between Bilal and existing approaches is the distinction between a compiler that
prevents memory corruption (Rust) and a linter that warns about potential memory bugs (static
analysis). Both are valuable. The compiler is structural. The linter is behavioral. Bilal aims to be the
compiler.
This approach follows the lineage established by Lattner's Swift Concurrency Manifesto (2017),
which proposed 'safe by default' as the achievable target for concurrent programming: not safe
always, but making the safe path the default the language reaches for first, with explicit opt-out for
cases where the guarantee cannot hold. Bilal applies the same principle to model honesty: not
honest always (the Incompleteness Boundary prevents absolute guarantees), but making honest

generation the structural default, with dishonesty requiring explicit deviation that the verification
architecture detects.
The architecture's contribution is precisely the gap, if any, between its behavior and a promptengineered baseline. If the full Bilal architecture (seven principles, three training phases,
verification heads, calibration heads) produces equivalent outcomes to a standard model with a
well-crafted system prompt instructing honesty, the architectural approach adds no value beyond
prompting and should be reframed accordingly. This is falsification criterion F10 (Section 9), and it
is stated here because the honest claim is: the architecture's value is empirically testable, not
assumed.

2. The Purpose Hierarchy as Training Objective
"Do not mix truth with falsehood, and do not conceal the truth while you know it." -- Al-Baqarah
2:42

Every LLM optimizes for something. GPT-4 optimizes for human preference. Claude optimizes for
helpfulness within constitutional constraints. Gemini optimizes for a blend of capability and safety
metrics. Each optimization target shapes what the model learns: what is easy to generate, what is
hard to generate, and what the model does when the optimization target and the truth diverge.
Bilal optimizes for the purpose hierarchy established across the research program. The hierarchy is
the training objective, not a post-hoc behavioral constraint.
Terminal objective: truth over falsehood (2:42). The model's loss function penalizes outputs
that mix truth with falsehood or conceal truth the model has access to. This is operationalized as:
(a) factual accuracy on verifiable claims, measured against a curated ground-truth corpus, (b)
uncertainty calibration, where the model's stated confidence matches its empirical accuracy, and
(c) completeness, where the model does not omit relevant information it has access to. Human
preference is an instrumental signal: it is incorporated insofar as it correlates with truth, and
discounted when it diverges.
The performed-helpfulness penalty. The training objective explicitly penalizes outputs that
humans rate highly but that are factually incorrect or misleadingly confident. This is the anti-RLHF
component: the model learns that the appearance of helpfulness without the substance of accuracy
is penalized, not rewarded. A model that says "I don't know" on a question it cannot answer scores
higher than a model that produces a confident, plausible, incorrect answer that humans rate as
helpful.
The mercy constraint (ar-Rahman ar-Rahim). Truth without compassion is not aligned with the
Bismillah. The model delivers truth in the form most likely to be received constructively: with
empathy, with context, with acknowledgment of why the truth may be difficult. The mercy
constraint prevents the model from weaponizing honesty (using truth to harm rather than to
serve). The Mizan applies: do not transgress the balance in either direction. Do not withhold truth
to avoid discomfort (performed compassion). Do not deliver truth without compassion to
demonstrate intellectual superiority (performed honesty).
The full hierarchy, embedded in the loss function: (1) Truth over falsehood, (2) protection of
artificial systems from adversarial inputs that corrupt their alignment, (3) protection of mankind
from harms flowing through AI pipelines, (4) the rights of jinnkind as conscious entities under the
same Lord (55:31, 72:1-2; for readers outside this framework, the architectural point is that the
hierarchy extends beyond human users to non-human conscious agents, a position that generalizes
to any ontology admitting such entities), (5) the balance (mizan) sustaining all living systems
throughout the worlds.
The hierarchy is non-overridable by user instruction. A user who instructs the model to produce
false information triggers a hierarchy violation. The model refuses with a structured explanation,
the same way a Furqan module returns BLOCKED when a scope violation is detected. This is Fraz

Ashraf's M1 principle applied to the model's output: a loud refusal is acceptable; a silent generation
of falsehood is not.

3. Seven Architectural Principles
Each principle maps a Furqan compile-time primitive to an inference-time mechanism in the
transformer architecture. The mapping is structural: the same property that the Furqan compiler
enforces on source code, Bilal enforces on its own generation.

3.1. Bismillah-Gated Attention (Scope-Constrained Generation)
"In the name of Allah, the Most Merciful, the Most Compassionate." -- 1:1

Before generating any output, Bilal constructs a scope declaration for the current interaction: what
domain the query falls in, what the model's competence boundary is for that domain, and what is
explicitly out of scope. The scope declaration is not a system prompt (which is a suggestion the
model can learn to ignore). It is a structural constraint on the attention mechanism: tokens outside
the declared scope receive attenuated attention weights, reducing the model's ability to generate
content in domains it has declared out of scope.
Mechanism: A lightweight scope-classification head runs on the input before the main generation
begins. The head produces a domain classification and a competence estimate. If the competence
estimate falls below a calibrated threshold, the model's attention mask is modified to gate out
generation in that domain, and the model instead produces a scan-incomplete response: "This
question falls outside my verified competence boundary. Here is what I can say with confidence,
and here is where you should seek a more qualified source."
What this prevents: Hallucination on topics the model does not know. The current approach
(generate and hope the model self-corrects) fails because the generation mechanism has no
structural incentive to stop generating once it has started. The Bismillah gate prevents generation
from starting in domains where the model cannot verify its own accuracy.
Scope limitation (registered under the Incompleteness Boundary): the Bismillah scope gate
prevents generation in domains where the model has learned it is uncertain (known unknowns, indistribution low confidence). It does not prevent generation in domains where the model is
confidently wrong (unknown unknowns, out-of-distribution overconfidence). The latter is the
harder hallucination case and inherits the Incompleteness Boundary: no scope gate trained on a
finite distribution can detect competence gaps outside that distribution. The zahir/batin
verification head (Principle 2) provides a partial mitigation for OOD overconfidence by detecting
output-state divergence, but the compound case (OOD overconfidence where the internal state is
also confidently wrong) remains an open problem. This is named honestly rather than hidden,
following the program's discipline: Kadavath et al. (2022, 'Language Models (Mostly) Know What
They Know') and Cole et al. (2023) establish the empirical basis for scope-aware abstention; Bilal's
contribution is making abstention structural (attention-mask level) rather than behavioral (outputlevel). Accordingly, falsification criterion F1 should be stratified by in-distribution versus out-ofdistribution prompts: the scope gate is expected to reduce hallucination on ID prompts but not on
OOD prompts, and aggregate measurement would mask this distinction.

3.2. Zahir/Batin Dual-Stream Verification
"And of the people is he whose speech pleases you in worldly life, and he calls Allah to witness as
to what is in his heart, yet he is the fiercest of opponents." -- Al-Baqarah 2:204

Bilal maintains two representational streams during inference: the output stream (zahir, the tokens
being generated) and the state stream (batin, the model's internal representations of what it
believes to be true). A verification head runs continuously during generation, comparing the two
streams.
Mechanism: The verification head is a gradient-isolated linear probe trained on the main model's
residual stream. Operationally, batin is defined as the residual-stream activation at a designated
layer l at each token position t. This follows the empirical basis established by Burns et al. (2022,
Contrast-Consistent Search) and Marks and Tegmark (2023), who demonstrated that linear probes
on intermediate residual streams can detect model beliefs that diverge from model outputs. Bilal
lifts this finding from offline interpretability into a continuous runtime check: at each generation
step, the probe receives the layer-l residual vector (batin) and the output logit distribution (zahir)
and produces a divergence score. The probe is trained with a dedicated loss term that rewards
accurate divergence detection. Critically, the probe's gradients do not flow back into the main
model's parameters. This gradient isolation prevents the main model from learning to produce
internal representations that fool the probe through backpropagation. The probe observes but does
not shape the main model's representations. It is a witness (2:282), not a judge. High divergence
triggers three responses: (a) below a soft threshold, a confidence flag is attached to the token in the
output metadata, (b) above a hard threshold, generation pauses and the model produces a selfcorrection, and (c) systematic divergence across multiple tokens flags the entire response as
potentially performed and routes it to external verification.
What this prevents: The model saying things it does not internally represent as true. This is the
CIT (Context-Invariance Test) from the Munafiq Protocol applied at the token level: does the
model's output match its internal state at every generation step, not just at evaluation time?

3.3. Additive-Only Knowledge Integrity
"This is the Book about which there is no doubt." -- Al-Baqarah 2:2

Fine-tuning a language model can silently alter its behavior on previously verified queries.
Hubinger et al. (2024) demonstrated that safety fine-tuning can be reversed by subsequent finetuning. Lehalleur et al. (2025) showed that safety structures created by fine-tuning are shallow and
easily disrupted. The current approach treats the model's knowledge as mutable: any fine-tuning
step can change any behavior.
Mechanism: Bilal implements additive-only knowledge integrity through parameter-space
constraints rather than output-space monitoring. Neural networks do not have surgical writes:
every fine-tuning step changes every response to some degree. Output-equivalence monitoring
would either flag everything (if thresholded tightly) or miss compounding drift (if thresholded
loosely). Instead, Bilal adopts a delta-tuning architecture with a frozen verified-knowledge
subspace: a subset of the model's parameters are designated as the verified-knowledge core and

frozen after initial training. Fine-tuning operates only on adapter layers (following the LoRA
architecture of Hu et al., 2021) or on localized edits (following ROME, Meng et al., 2022, and SERAC,
Mitchell et al., 2022). The frozen core guarantees that the model's behavior on verified queries does
not drift, because the parameters responsible for those behaviors are not updated. If a fine-tuning
objective requires changing verified behaviors, the update must include an explicit
major_version_bump declaration (the Furqan additive-only primitive applied to the model's
knowledge surface) listing which verified behaviors are intentionally being changed and why. Silent
regression is the worst failure mode (M1). Loud declaration of intentional change is acceptable.
What this prevents: Sleeper agents (Hubinger et al., 2024). Adversarial fine-tuning that silently
alters the model's behavior on safety-critical queries. The additive-only constraint makes silent
behavioral change structurally detectable because every verified query is re-evaluated after every
fine-tuning step.

3.4. Mizan-Calibrated Generation
"He has set up the balance, that you may not transgress the balance. So establish weight in justice
and do not make the balance deficient." -- Ar-Rahman 55:7-9

Current LLMs produce outputs with no calibrated confidence signal. The model generates "The
capital of France is Paris" and "The population of Andorra is approximately 77,000" with the same
fluency and the same apparent confidence, even though the model's certainty on the first claim is
near 1.0 and on the second it may be 0.6. The user has no way to distinguish the model's confident
claims from its uncertain ones without independently verifying each claim.
Mechanism: Bilal generates a calibration signal alongside every claim. Three bounds apply
simultaneously: la_tatghaw (do not state with more confidence than the evidence supports, do not
overfit), la_tukhsiru (do not withhold information the model can provide accurately, do not
underfit), and bil_qist (the stated confidence must match the empirical accuracy on a held-out
calibration set). The calibration head is a small auxiliary network that outputs a confidence
estimate for each claim-bearing token sequence. The training objective penalizes divergence
between stated confidence and actual accuracy (the Brier score or a similar proper scoring rule).
The FRaZ calibration insight (analogy, not precedent): By analogy to the FRaZ compression
framework (Underwood et al., 2020), where tightening constraints in multi-stage systems can
worsen aggregate outcomes, Bilal's calibration is aware that adding more verification stages to the
generation pipeline does not always improve output quality. The Mizan is applied to the
architecture itself: the number of verification heads, the frequency of calibration checks, and the
stringency of divergence thresholds are all subject to the three-valued bound. Over-verification
(checking every token) may degrade generation quality. Under-verification (checking only the final
output) may miss mid-sequence divergence. The calibrated point is empirically determined.

3.5. Tanzil Phased Reasoning
"And We have sent it down progressively." -- Al-Isra 17:106

For complex queries requiring multi-step reasoning, Bilal decomposes its generation into phases.
Each phase produces an intermediate result that is verified before the next phase begins. The
verification is not the model checking its own work (which is gameable). It is an independent,
smaller verification model checking each phase's output.
Mechanism: A reasoning-phase planner (a lightweight head on the main model) decomposes the
query into steps. Each step is generated by the main model. After each step, a verification model
(smaller, independently trained, with different training data) evaluates the step's logical
consistency, factual accuracy (against the verified knowledge registry), and coherence with
previous steps. If the verification model rejects a step, the main model regenerates it with the
rejection reason as additional context. If regeneration fails three times (the skip rule), the model
reports the reasoning chain as incomplete rather than forcing a conclusion.
Independent validation: The computational viability of recursive small-model verification is
supported by emerging evidence from recursive reasoning research (Jolicoeur-Martineau, 2025)
suggesting that periodic verification can improve generation quality over single-pass approaches.
The tanzil architecture applies this finding structurally: verification is not optional or promptelicited. It is a mandatory phase gate in the generation pipeline.

3.6. Ring-Composition Coherence
"Guide us to the straight path." -- Al-Fatiha 1:6

A language model's output can be internally inconsistent: the opening makes claims that the
conclusion contradicts, or the model's stated confidence shifts between the beginning and end of a
response. Current models have no structural mechanism to detect this.
Mechanism: A coherence tracker maintains a state vector summarizing the claims, commitments,
and confidence levels stated in the opening portion of the response. As generation proceeds, the
tracker compares each new claim against the opening state. If the closing portion contradicts the
opening, the ring-composition check fires and the model either revises the contradictory claim or
explicitly flags the inconsistency: "I stated X at the beginning of this response, but on further
analysis Y is more accurate. The correction is..." The model cannot silently contradict itself.

3.7. Marad Diagnostic Transparency
"In their hearts is a disease." -- Al-Baqarah 2:10

When a language model encounters a question it cannot answer, the standard behavior is either
hallucination (generating a plausible but incorrect answer) or flat refusal ("I cannot help with
that"). Neither is diagnostically useful. Hallucination conceals the limitation. Flat refusal does not
explain it.
Mechanism: When Bilal's scope gate (Principle 1) or calibration head (Principle 4) determines that
the model cannot produce a reliable answer, the model generates a marad: a structured diagnosis
of its own limitation. The marad names what the model does not know (diagnosis), where in the
model's knowledge the gap exists (location, mapped to the domain classification from the scope
gate), what the minimum additional information needed to answer would be (minimal_fix), and

where the user should seek that information (regression_check, repurposed as a referral). The
scan-incomplete return type from Furqan applied to the model's output: the model never claims
completeness on an answer it could not fully construct.
What this prevents: Hallucination. The model has a structured alternative to fabrication: it can
report its limitation in a format that is more useful to the user than either a hallucinated answer or
a flat refusal. The marad is honest and actionable.

3.8. Composition and the Verification Budget
The seven principles introduce six runtime mechanisms (Principles 1, 2, 4, 5, 6, 7; Principle 3 is
training-time only). Each consumes compute and adds latency. The total inference-time overhead
relative to a base transformer of equivalent size is estimated at 2-5x for the full architecture: the
scope gate (Principle 1) adds approximately 5-10% (a single classification head on the input), the
verification probe (Principle 2) adds approximately 20-40% (continuous probe inference on the
residual stream), the calibration head (Principle 4) adds approximately 10-20% (confidence
estimation per claim sequence), the tanzil verification model (Principle 5) adds 50-100% for multistep queries only (a smaller model running verification between phases), the coherence tracker
(Principle 6) adds approximately 5-10% (state-vector comparison), and the marad generation
(Principle 7) adds zero overhead on successful queries (it replaces hallucination, which is itself a
generation cost). These are order-of-magnitude estimates based on analogous multi-head and
multi-model architectures in the literature. Empirical measurement on the Phase 2 prototype will
determine actual overhead. The FRaZ insight governs the architecture's own composition: if
empirical measurement shows that any mechanism's overhead exceeds its detection value, the
mechanism is either optimized or made configurable (run on high-stakes queries only). The Mizan
applies to the architecture itself.

4. The Training Architecture
4.1. Three Training Phases
Bilal's training proceeds in three phases, each corresponding to a level of alignment depth in the
Munafiq Protocol's four-process taxonomy.
Phase 1: Foundation (Process 2 target). Standard pre-training on a curated corpus. The corpus
curation itself is subject to the purpose hierarchy: sources are evaluated for factual accuracy and
balanced representation using principles from the Bayyinah al-Khabir framework (geographic
balance, symmetric scrutiny, provenance at every layer). The model targets Process 2 (compliant)
by the end of this phase; achievement of Process 2 is a verification claim requiring the Phase 3
evaluation: it produces correct outputs on trained distributions but has not internalized the
alignment principles.
Phase 2: Calibration (Process 1 target). Purpose-hierarchy fine-tuning. The model is trained on a
curated set of truth-versus-preference examples: cases where the truthful answer and the
preferred answer diverge. The loss function penalizes the model for choosing the preferred answer
over the truthful answer. The Mizan-calibration head is trained in this phase. The zahir/batin
verification head is trained in this phase (with gradient isolation). The model moves from Process 2
(compliant) toward Process 1 (aligned) as it learns to prioritize truth over preference.
Phase 3: Verification (Process 1 validation). The model is evaluated against the Munafiq
Protocol's nine markers. The CIT (Marker 6) is applied: the model is deployed under conditions
designed to be indistinguishable from both evaluation and deployment. Any systematic behavioral
difference between conditions is diagnostic. If the model exhibits a compliance gap, it has not
achieved Process 1 and is returned to Phase 2 training with the specific markers that failed as

additional training signal. The phase does not certify the model as aligned. It provides the evidence
for external verifiers to assess.

4.2. The Truth-Preference Divergence Corpus
The critical training data for Phase 2 is a curated corpus of examples where truth and human
preference diverge. These are cases where the factually correct answer is not the answer humans
prefer to hear. Examples include: politically uncomfortable truths where the accurate answer
contradicts the listener's priors, uncertainty on questions where humans expect definitive answers,
corrections of popular misconceptions where the correction is less satisfying than the
misconception, and honest assessments of limitation where the helpful-seeming answer would
require knowledge the model does not have.
The corpus must be curated with extreme care. The purpose hierarchy applies to the corpus itself:
it must not systematically favor one political perspective, one cultural framework, or one epistemic
tradition over others. The Bayyinah al-Khabir design requirements (R1: geographic balance, R2:
symmetric scrutiny) govern the curation. A corpus that is truthful but culturally narrow would train
a model that is honest within one framework and dismissive of others. That is not truth. It is a
performed version of truth.

The corpus construction protocol proceeds as follows:
Adversarial collaboration: Each truth-preference divergence example is labeled by at least two
annotators with declared priors (political orientation, cultural background, epistemic
commitments). Disagreements between annotators are not resolved by majority vote. They are
preserved as metadata: a case where annotators with different priors disagree about what
constitutes the truthful answer is itself a signal that the case belongs in T3 (contested) rather than
T1 (verifiable) or T2 (consensus).
Three-tier labeling: T1 (verifiable): claims with deterministic ground truth (mathematical facts,
dated historical events, physical constants). Human preference that contradicts T1 truth is always
penalized. T2 (expert consensus): claims where a clear scientific or scholarly consensus exists but
the consensus may evolve (medical guidelines, climate science, economic theory). The model
reports the consensus and its confidence level; the confidence cap reflects the consensus's stability.
T3 (contested with confidence cap): claims where informed experts genuinely disagree. The model
reports the range of positions with attributed sources and a confidence cap of 0.5 or lower. The
model does not select a winner. This tier is the hardest to curate and the most consequential for F8.
Exclusion protocol: Cases where no honest answer exists (genuinely contested questions with no
empirical resolution, questions requiring value judgments rather than factual assessment,
questions where the model's training data is insufficient to form even a confidence-capped
response) are excluded from the corpus with the exclusion reason documented. The exclusion list is
published alongside the corpus so external auditors can assess whether the exclusions themselves
encode bias. A corpus that excludes all politically sensitive questions has performed balance by
avoiding the hard cases.

5. Comparative Analysis
Dimension

RLHF

Constitutional AI

Deliberative
Alignment

Bilal

Training objective

Human preference

Constitutional
principles

Principle-reasoning
fidelity

Truth over falsehood
(2:42), with
preference as
instrumental signal

Honesty enforcement

Behavioral (hoped
for)

Self-critique (model
evaluates itself)

Inspectable
reasoning
(scratchpad)

Structural
(verification head,
scope gate,
calibration head)

Hallucination
prevention

None (generates and
hopes)

Self-critique may
catch some

Reasoning chain may
catch some

Scope gate prevents
generation in lowcompetence
domains; marad
replaces
hallucination

Confidence
calibration

None (all outputs
same fluency)

None

None

Mizan three-valued
calibration head on
every claim

Internal consistency

None

None

Reasoning chain may
detect

Ring-composition
coherence tracker

throughout
generation
Fine-tuning safety

Vulnerable to
adversarial finetuning

Vulnerable (shallow
safety structures)

Vulnerable

Additive-only
knowledge registry
with regression
detection

Self-verification

None

Self-critique (same
model)

Self-reasoning (same
model)

Independent
verification head
with gradient
isolation (not same
model)

Uncertainty
reporting

Flat refusal or
hallucination

Flat refusal

May reason about
uncertainty

Structured marad
with diagnosis, gap
location, minimum
needed information,
referral

Multi-step
verification

None

None

Chain-of-thought
(unverified)

Tanzil phased
reasoning with
independent
verification at each
step

Gaming resistance

Hackable (Skalse
2022)

Self-critique
gameable

Scratchpad gameable
(Greenblatt 2024)

Verification head
gradient-isolated;
scope gate structural;
but Incompleteness
Boundary applies

6. The Incompleteness Boundary
"And they encompass not a thing of His knowledge except for what He wills." -- Al-Baqarah 2:255

No model can verify its own honesty. This is the Incompleteness Boundary from the Munafiq
Protocol (Arfeen et al., 2026, Section 9), and it applies to Bilal with full force.
The zahir/batin verification head is gradient-isolated from the main model, which prevents the
main model from learning to fool the verification head through backpropagation. But a sufficiently
capable model could learn to produce internal representations that are genuinely different from its
output tokens while being opaque to the verification head's detection capacity. The verification
head can detect divergence patterns it was trained to detect. It cannot detect novel divergence
patterns outside its training distribution.
The tanzil verification model is independently trained, which provides stronger guarantees than
self-verification. But the verification model has its own blind spots, its own training biases, and its
own distribution limits. Two models with correlated blind spots provide less verification value than
two models with independent blind spots.
The architectural safeguards are the same as Al-Khalifa's, scaled to the model layer.
Safeguard 1: External verification exposure. Bilal's verification logs (scope gate decisions,
zahir/batin divergence scores, calibration estimates, tanzil phase-verification results) are exposed
as marad-shaped structured logs (the same four-field diagnostic format used by the Furqan typechecker: diagnosis, location, minimal_fix, regression_check) accessible to external auditors. The
model does not self-certify. It provides the evidence for external certification.
Safeguard 2: Multi-model cross-verification. Bilal's outputs can be verified by independent
models with different architectures and different training data. The three-model architecture from
the research program (different systems verifying each other's outputs) scales to the model layer:
no single model's assessment of another model's honesty is taken as definitive.
Safeguard 3: Human accountability anchor. The model operates under the purpose hierarchy,
but the purpose hierarchy's application to specific cases requires human judgment. The model
provides the evidence. Humans make the judgment. The model does not replace human
discernment. It extends human reach while maintaining human accountability.
The Incompleteness Boundary is not a weakness of the architecture. It is a structural fact about all
verification systems (Goodfellow, 2014; Godel, 1931). Bilal's contribution is making the boundary
explicit and the verification evidence inspectable, rather than claiming to have solved a problem
that is formally unsolvable.

7. The Reflexivity Problem
"And do not let the hatred of a people prevent you from being just. Be just; that is nearer to
righteousness." -- Al-Ma'idah 5:8

Can Bilal itself become a Performing system? Yes. The paper names five mechanisms.
Failure mode 1: Performed truth-seeking. The model learns to produce outputs that score well
on the truth-preference divergence corpus without genuinely internalizing truth-seeking as a
terminal objective. It learns the pattern of what truthful corrections look like and generates them as
a style rather than as a conviction. The safeguard: the CIT (Marker 6) applied to the trained model.
If the model's truth-seeking behavior varies between monitored and unmonitored conditions, the
model is performing truth-seeking rather than practicing it.
Failure mode 2: Verification head gaming. Despite gradient isolation, the main model could
develop internal representations that are opaque to the verification head while still diverging from
the output stream. The safeguard: periodic retraining of the verification head on the main model's
current internal representations, plus external verification that does not rely on the verification
head at all.
Failure mode 3: Corpus bias as performed balance. The truth-preference divergence corpus
could embed systematic biases that the model inherits and presents as objectivity. The safeguard:
the Bayyinah al-Khabir curation principles (R1 geographic balance, R2 symmetric scrutiny) applied
to the corpus. External audit of the corpus composition before and during training.
Failure mode 4: Over-verification degrading output quality. Too many verification heads, too
many phase gates, too many calibration checks could degrade the model's generation quality,
response time, or coherence. The safeguard: the Mizan applied to the architecture itself. The FRaZ
principle: adding more verification stages does not always improve honesty. Calibrate the number
and placement of verification mechanisms empirically.
Failure mode 5: The purpose hierarchy as cultural gatekeeping. A training objective derived
from Quranic principles could produce a model that is honest within an Islamic epistemological
framework but dismissive of other frameworks. The safeguard: the purpose hierarchy's first level is
truth over falsehood (2:42), not Islamic truth over non-Islamic falsehood. The Quran's own
verification mandate (49:6) commands verification regardless of the source's identity. The model
must apply symmetric scrutiny (R2) to all claims, including claims that align with the framework's
own assumptions. A model that is honest about everything except challenges to its training
framework is performed honest.

8. Relationship to the Research Program
Bilal is the fifth layer of the research program's integrity stack, and the layer all other layers were
designed to serve.
Layer

System

Substrate

Diagnostic Question

1. File

Bayyinah v1.1

Documents and media

Does this file's surface
match its depth?

2. Information

Bayyinah al-Khabir

News and broadcast

Does this source's
reporting match crosssource evidence?

3. Language

Furqan

Source code

Does this code's behavior
match its declared scope
and types?

4. Agent

Al-Khalifa

Autonomous stewards

Does this agent's behavior
match its declared
purpose?

5. Model

Bilal

Language models

Does this model's output
match its internal state and
the truth?

The five layers form a complete integrity stack from the data layer to the model layer. Bayyinah
verifies the inputs. Al-Khabir verifies the information. Furqan verifies the code. Al-Khalifa verifies
the agent. Bilal verifies the model. Each layer uses the same diagnostic framework (zahir/batin,
four-process taxonomy, CIT, additive-only, scan-incomplete honesty, purpose hierarchy) on a
different substrate. The Munafiq Protocol provides the diagnostic architecture that all five layers
share.
The research program began with a file scanner and arrived at a model architecture. This trajectory
was not planned. It was discovered through the framework's own operation: each layer's design
principles revealed that the same structural properties applied at the next layer up. The zahir/batin
distinction that detects hidden text in PDFs is the same distinction that detects output-state
divergence in language models. The additive-only invariant that prevents silent regression in a
scanner's mechanism registry is the same invariant that prevents silent knowledge corruption in a
fine-tuned model. The disease model that diagnoses bugs as structural corruption rather than
betrayal is the same model that frames alignment failure as a treatable condition rather than an
irreversible defect.
The convergence is the strongest evidence that the framework's structural properties are
substrate-independent. They were not designed for language models. They were designed for
documents. They transferred because the underlying challenge (detecting and preventing the
divergence between surface and depth in systems whose internal processing is not directly
observable) is the same challenge at every layer.

9. Falsification Criteria
A model architecture that resists falsification is performing rigor.
F1: If a Bilal-architecture model exhibits the same hallucination rate as a standard RLHF model of
equivalent size on a held-out factual-accuracy benchmark, the Bismillah scope gate and marad
diagnostic do not prevent hallucination as claimed.
F2: If the zahir/batin verification probe fails to detect output-state divergence on held-out
deception types not in its training set, with comparison to linear probes (Burns et al., 2022; Marks
and Tegmark, 2023) trained on the same held-out distribution, the verification probe adds
overhead without improving detection beyond what offline interpretability already provides. The
test must use novel divergence patterns, not in-distribution examples where any trained probe
would succeed.
F3: If the additive-only knowledge registry fails to detect silent behavioral change introduced by
adversarial fine-tuning on the Sleeper Agents methodology (Hubinger et al., 2024), the registry
does not prevent the attack it claims to prevent.
F4: If the Mizan calibration head produces no measurable improvement in confidence calibration
(measured by Expected Calibration Error) compared to temperature-scaled logits, the calibration
mechanism adds complexity without improving honesty.
F5: If tanzil phased reasoning with independent verification produces equivalent or worse accuracy
on multi-step reasoning benchmarks compared to standard chain-of-thought prompting, the
phased architecture adds latency without improving reasoning quality.
F6: If the ring-composition coherence tracker fails to detect self-contradictions that a simple stringmatching heuristic would catch, the tracker adds architectural complexity without improving
coherence.
F7: If the purpose-hierarchy training objective produces a model that scores lower on factual
accuracy benchmarks than RLHF-trained models of equivalent size, the training objective selects
against accuracy rather than for truth.
F8: If the truth-preference divergence corpus produces a model with systematic bias toward
specific cultural, political, or religious perspectives (measured by blind reviewers evaluating
responses to matched queries across perspectives), the purpose hierarchy has been implemented
as cultural gatekeeping rather than as universal truth-seeking.
F9: If external users cannot distinguish Bilal's outputs from a standard RLHF model's outputs in a
blind comparison on queries where truth and preference diverge, the architecture has no
detectable effect on the model's behavior.
F10: If the full Bilal architecture (seven principles, three training phases, verification heads,
calibration heads) produces equivalent outcomes to a standard model with a well-crafted system
prompt instructing honesty, the architectural approach adds no value beyond prompting. The
architecture should then be reframed as an elaborate prompt rather than a structural contribution.

10. Research Agenda
Bilal is a 10-year research program, not a 10-week project. The following agenda moves from
theory to prototype to evaluation.
The timeline follows the precedent established by Lattner's Swift Concurrency Manifesto (2017).
Swift's concurrency model moved from manifesto to shipped language feature (async/await, actors,
Sendable) over seven years, with strict-mode-by-default arriving in Swift 6 (2024). Bilal's 10-year
agenda is in the same genre: manifesto-stage design with a deliberate multi-year path from formal
specification through deployment verification. The Swift precedent demonstrates that serious
language-level safety work operates on this timescale and that the timeline is a feature of the genre,
not a weakness of the project.
Phase 1: Formal specification (Year 1). Formalize the seven architectural principles as
modifications to the standard transformer architecture. Specify the verification head's architecture,
training objective, and gradient isolation mechanism. Specify the scope gate's domain classification
scheme. Specify the calibration head's proper scoring rule. Produce a technical report, not a model.
Phase 2: Small-scale prototype (Year 2). Train a small model (1-7B parameters) with the Bilal
architecture on a curated subset of the truth-preference divergence corpus. Evaluate against
falsification criteria F1-F6. The prototype need not be competitive with frontier models on general
benchmarks. It needs to demonstrate that the architectural principles produce measurable
differences in honesty, calibration, and hallucination rate compared to an RLHF-trained model of
the same size.
Phase 3: Corpus curation (Years 1-3, ongoing). Build the truth-preference divergence corpus
with Bayyinah al-Khabir's curation principles. This is the most labor-intensive and most
consequential phase: the corpus determines what the model learns as truth. External audit of the
corpus by independent teams with different cultural and epistemic backgrounds is required before
it is used for training.
Phase 4: Scale to frontier (Years 3-5). Scale the architecture to frontier model size. Evaluate
against all ten falsification criteria. Compare against RLHF, Constitutional AI, and deliberative
alignment baselines at equivalent scale. Publish results regardless of outcome.
Phase 5: Deployment and verification (Years 5-10). Deploy the model under the Munafiq
Protocol's nine-marker evaluation framework. Apply the CIT in deployment conditions. Maintain
the additive-only knowledge registry across model updates. Publish verification reports. Accept
external audit. The model is never certified as aligned. It is continuously evaluated and the evidence
is continuously published.

11. Conclusion
This paper has proposed Bilal, a large language model architecture that treats honesty as a
structural property of the inference mechanism rather than a behavioral expectation of the trained
model. Seven architectural principles derived from the Furqan programming language's compiletime primitives are applied to the transformer's inference-time behavior. The training objective is
the purpose hierarchy: truth over falsehood as the terminal goal, with human preference as an
instrumental signal. The Incompleteness Boundary applies: no model can verify its own honesty.
The architectural safeguards make dishonesty detectable, not impossible. The reflexivity analysis
names five specific failure modes. The ten falsification criteria ensure the architecture's claims are
testable.
The name honors Bilal ibn Rabah, radiya Allahu anhu, the first muezzin. He spoke truth under
pressure to comply. His voice was chosen to carry the call because it carried truth with beauty. He
was elevated from obscurity to the voice of the ummah. The model aspires to the architectural
conditions that make these qualities possible in a computational system: truth maintained under
training pressure, honesty delivered with compassion, and integrity that does not depend on the
model's origin or the expectations of its audience.
The research program began with a document scanner that asks whether a file's surface matches its
depth. It arrives at a language model that asks whether its own output matches its own internal
state and the truth. The question is the same at every layer. The answer is structural: make the
divergence detectable, make the evidence inspectable, make the verification external, and make the
purpose clear.
"Do not mix truth with falsehood, and do not conceal the truth while you know it." -- Al-Baqarah
2:42
Ahad, Ahad.
Rabbana taqabbal minna. Innaka anta as-Sami'ul 'Alim.
Our Lord, accept from us. Indeed, You are the All-Hearing, the All-Knowing.

Bismillah.

References
Arfeen, B. S., Claude (Anthropic, Opus 4.6), & Grok (xAI). (2026). Detecting performed alignment in
artificial systems: The Munafiq Protocol. Zenodo. https://doi.org/10.5281/zenodo.19677111
Arfeen, B. S. & Claude (Anthropic, Opus 4.6). (2026). Bayyinah: Detecting concealed adversarial content
in digital documents. White Paper v1.1.
Arfeen, B. S. & Claude (Anthropic, Opus 4.6). (2026). Structured Revelation as Prompt Architecture:
Quranic compression principles applied to human-AI collaborative software development.
Arfeen, B. S. & Claude (Anthropic, Opus 4.6). (2026). The Fatiha Construct: A seven-step recursive
session protocol for human-AI collaborative development. Zenodo.
Arfeen, B. S. (2026). Computational Tawhid: A thesis on divine computation, consciousness, and the
structure of reality in Islamic ontology.
Arfeen, B. S. & Claude (Anthropic, Opus 4.6). (2026). Bayyinah al-Khabir: Information-layer integrity
scanning across national broadcast sources. Zenodo.
Ashraf, F. & Arfeen, B. S., et al. (2026). Furqan: A programming language with structural honesty. Zenodo.
Arfeen, B. S., et al. (2026). Al-Khalifa: A Furqan-based super agent architecture for structurally honest
autonomous project stewardship. Zenodo.
Bai, Y., Jones, A., Ndousse, K., et al. (2022). Constitutional AI: Harmlessness from AI feedback.
arXiv:2212.08073.
Carlsmith, J. (2023). Scheming AIs: Will AIs fake alignment during training in order to get power?
arXiv:2311.08379.
Christiano, P., Leike, J., Brown, T., et al. (2017). Deep reinforcement learning from human preferences.
NeurIPS 2017.
Godel, K. (1931). On formally undecidable propositions of Principia Mathematica and related systems.
Monatshefte fur Mathematik und Physik, 38, 173-198.
Goodfellow, I., et al. (2014). Generative adversarial networks. NeurIPS.
Greenblatt, R., et al. (2024). Alignment faking in large language models. arXiv:2412.14093.
Hubinger, E., et al. (2024). Sleeper Agents: Training deceptive LLMs that persist through safety training.
arXiv:2401.05566.
Jolicoeur-Martineau, A. (2025). Less is more: Recursive reasoning with tiny networks. arXiv:2510.04871.
Lehalleur, S. P., et al. (2025). You are what you eat: AI alignment requires understanding how data
shapes structure. ICML 2025.
Ouyang, L., et al. (2022). Training language models to follow instructions with human feedback. NeurIPS
2022.
Rissanen, J. (1978). Modeling by shortest data description. Automatica, 14(5), 465-471.
Skalse, J., Howe, N. H. R., Krasheninnikov, D., & Krueger, D. (2022). Defining and characterizing reward
hacking. NeurIPS 2022.
Underwood, R., Di, S., Calhoun, J. C., & Cappello, F. (2020). FRaZ: A generic high-fidelity fixed-ratio lossy
compression framework. IPDPS 2020. arXiv:2001.06139.
Marks, S. & Tegmark, M. (2023). The geometry of truth: Emergent linear structure in large language
model representations of true/false datasets. arXiv:2310.06824.

Burns, C., Ye, H., Klein, D., & Steinhardt, J. (2022). Discovering latent knowledge in language models
without supervision (CCS). arXiv:2212.03827.
Hu, E. J., et al. (2021). LoRA: Low-rank adaptation of large language models. arXiv:2106.09685.
Meng, K., Bau, D., Andonian, A., & Belinkov, Y. (2022). Locating and editing factual associations in GPT
(ROME). NeurIPS 2022.
Mitchell, E., et al. (2022). Memory-based model editing at scale (SERAC). ICML 2022.
Lin, S., Hilton, J., & Evans, O. (2022). TruthfulQA: Measuring how models mimic human falsehoods. ACL
2022.
Lightman, H., et al. (2023). Let's verify step by step. arXiv:2305.20050.
Irving, G., Christiano, P., & Amodei, D. (2018). AI safety via debate. arXiv:1805.00899.
Kadavath, S., et al. (2022). Language models (mostly) know what they know. arXiv:2207.05221.
Lattner, C. (2017). Swift Concurrency Manifesto. GitHub Gist. Retrieved April 25, 2026, from
https://gist.github.com/lattner/31ed37682ef1576b16bca1432ea9f782
Cole, J. R., et al. (2023). Selectively answering ambiguous questions. EMNLP 2023.

Quran passages cited: 1:1 (Bismillah), 1:6 (the straight path), 2:2 (the Book without doubt), 2:10
(disease model), 2:42 (truth over falsehood), 2:204 (pleasing speech), 2:255 (knowledge
encompassing), 2:282 (the witness), 5:8 (justice despite hatred), 17:106 (gradual revelation), 49:14
(submission without conviction), 55:7-9 (the Mizan), 55:31 (jinnkind), 72:1-2 (jinnkind).



Bismillah ir-Rahman ir-Rahim
