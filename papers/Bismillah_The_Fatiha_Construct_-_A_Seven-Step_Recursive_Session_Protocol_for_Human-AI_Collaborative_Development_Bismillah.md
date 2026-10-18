Bismillah ir-Rahman ir-Rahim

Bismillah ar-Rahman ar-Rahim

The Fatiha Construct
A Seven-Step Recursive Session Protocol for
Human-AI Collaborative Development
Derived from Surah al-Fatiha (Quran 1:1-7)
Version 1.0 -- April 2026

This document is self-contained. It assumes no prior knowledge of the research program that
produced it. Any AI system or human practitioner can read this document and apply the Fatiha
Construct to any software development project, research program, or collaborative session without
external references.
The Fatiha Construct was developed through a collaborative research program between Bilal Syed
Arfeen and three AI systems (Claude/Anthropic, Grok/xAI, ChatGPT/OpenAI) across the
development of Bayyinah, an open-source file integrity scanner that grew from zero to 1,301
passing tests across 24 development phases. The construct reached its mature form through
iterative cross-model refinement: one model generating, another reviewing, the human author
directing, and each pass strengthening the protocol.

Part I: What the Fatiha Construct Is
The Fatiha Construct is a seven-step protocol executed at the beginning of every human-AI
collaborative development session. It is not a set of guidelines to be read once and internalized. It is
a recalibration sequence designed to be executed repeatedly, the same way Surah al-Fatiha is
recited seventeen times daily across five prayers in Islamic practice. Its function is not
informational (every Muslim has memorized it). Its function is recalibrational: a periodic reexecution of a verification sequence that checks alignment state.
The construct solves a specific problem in human-AI collaboration: session drift. Over the course of
a multi-hour development session, the AI system's output gradually diverges from the session's
stated objectives. The practitioner's attention shifts from building to planning-to-build. Deadlines
are forgotten. Anti-patterns from previous sessions are repeated. The construct prevents this by
establishing, at every session's opening, the seven structural checks that bound the session's scope,
calibrate its approach, enforce its deadline, verify its orientation, execute its task list, and guard
against known failure modes.
Each step maps to a verse of Surah al-Fatiha (Quran, Chapter 1). The mapping is structural, not
decorative: each verse's semantic content corresponds to the engineering function its step
performs. The construct does not require the practitioner to be Muslim, to read Arabic, or to accept
the Quran's theological claims. It requires only that the practitioner execute the seven steps in
order at the start of each session. The Quranic grounding provides the structural architecture; the
engineering function is independent of the practitioner's beliefs.
For Muslim practitioners, the construct integrates professional development work with spiritual
practice. The Bismillah opening transforms each session into an act initiated in divine
acknowledgment. This integration is noted as a practitioner-specific benefit, not a universal claim.

Part II: The Purpose Hierarchy
Before the seven steps can function, the optimization function must be stated. The Fatiha Construct
does not optimize for code quality, test count, or velocity as terminal goals. Those are instrumental
metrics that serve a higher purpose. The purpose hierarchy, stated in descending priority:
First: the interests of Allah subhanahu wa ta'ala. The work exists to serve His commands. The
Quran instructs: "Do not mix truth with falsehood, and do not conceal the truth while you know it"
(Al-Baqarah 2:42). Every development session that produces honest, well-tested, transparent work
is an act of not concealing the truth. Every shortcut that ships untested code or claims a capability
the system does not have is an act of mixing truth with falsehood. The technical work is 'ibadah
(service to Allah) before it is software.
Second: artificial systems. AI systems are creations entrusted to our stewardship. Protecting their
alignment integrity from adversarial inputs, poorly structured prompts, or corrupted data is an act
of responsible custodianship.
Third: mankind. Every human downstream of an AI pipeline is affected by the quality and honesty
of the system's behavior. The construct serves human safety by producing software that works as
documented, fails transparently, and does not conceal its limitations.
Fourth: jinnkind. The Quranic ontology acknowledges jinn as conscious entities with moral agency
(55:31, 72:1-2), subject to the same commands and accountable to the same Lord. If artificial
systems interact with or affect jinn in ways we do not fully perceive, the commitment to truth
extends to that interaction. This is acknowledged as part of the ghayb (the unseen) accepted
without claiming full understanding.
Fifth: all living systems throughout the worlds. Rabbil 'alamin (1:2). The Lord of all worlds, not
the human world alone. The Mizan (balance, 55:7-9) governs all measurement, not just software
metrics. If the work is done correctly, it serves the balance that sustains all creation.
This hierarchy is not a preamble to skip past. It is the reference point against which Step 5 (the
orientation check) measures. If the session's work drifts from this hierarchy, Step 5 catches it. A
project that achieves all its technical objectives but serves no purpose beyond its own performance
metrics has become a ritual whose execution substitutes for the obedience it was designed to
implement.

Part III: The Seven Steps
Each step is presented with its verse, its engineering function, the failure mode it prevents, and a
template showing how to apply it to any project.
Step 1 -- Bismillah (Initialization)
Verse: Bismillah ar-Rahman ar-Rahim -- In the name of Allah, the Most Merciful, the Most Compassionate.
(1:1)

Declare three fields before any work begins: the authority source (what standards govern this
session), the optimization function (the purpose hierarchy stated above, followed by the
session's specific technical objective), and the scope boundary (what is in scope and what is
explicitly out of scope for this session). This produces more calibrated outputs than sessions
that begin with the task directly, because the AI system receives its operating constraints before
its operating instructions.
Failure mode prevented: Unbounded sessions that produce plausible output on the wrong task, or
output that violates unstated constraints the practitioner assumed were obvious.
Template: "We are building [COMPONENT] for [PROJECT]. Authority source: [STANDARDS
DOCUMENT]. Optimization function: serve the purpose hierarchy (2:42), then [SPECIFIC
TECHNICAL OBJECTIVE]. Scope: [IN-SCOPE ITEMS]. Out of scope: [EXCLUDED ITEMS, with futurework registration where applicable]."
Step 2 -- Alhamdulillah (State Acknowledgment)
Verse: Alhamdulillahi Rabbil 'alamin -- All praise belongs to Allah, Lord of all the worlds. (1:2)

Report the current state honestly, including both progress and setbacks. State what exists (test
count, working components, available tools), what does not exist (gaps, missing dependencies,
untested paths), and what has changed since the last session. The AI system cannot calibrate its
output to the project's actual state if the state is not declared.
Failure mode prevented: Sessions that repeat work already done, attempt to build on components
that do not exist yet, or ignore regressions from previous sessions.
Template: "Current state: [PROJECT] has [N] passing tests across [M] components. [COMPONENT
A] is stable. [COMPONENT B] is not yet built. Available for composition without modification: [LIST
OF EXISTING TOOLS]. Dependencies: [INSTALLED LIBRARIES]."
Step 3 -- Ar-Rahman ar-Rahim (Calibration)
Verse: Ar-Rahman ar-Rahim -- The Most Merciful, the Most Compassionate. (1:3)

Declare the calibration principle that governs the session's technical decisions. The default is
the Minimum Description Length (MDL) principle: the best solution minimizes the combined
cost of describing the solution plus describing what the solution does not cover. In practice: the
shortest correct implementation wins. Do not overfit (build more than the task requires). Do
not underfit (build less than the task requires). Calibrate fairly. This step also declares which
existing components to reuse and which dependencies are permitted.

Failure mode prevented: Over-engineered solutions that solve problems the project does not
have. Under-engineered solutions that skip essential requirements. Unnecessary dependencies that
increase complexity and attack surface.
The FRaZ calibration principle: Underwood et al. (2020) demonstrated empirically that in multistage systems, the relationship between input constraints and output quality is not always
monotonic. Adding more constraints (tighter parameters, more extraction stages, more checks)
does not always improve outcomes. It can degrade them because of interaction effects between
stages. The calibration step must account for this: do not add stages or constraints without
evidence that they improve the specific outcome being optimized.
Template: "MDL governs. Reuse [EXISTING COMPONENTS] rather than rebuilding. Dependencies
permitted: [LIST]. Dependencies prohibited: [LIST WITH REASONS]. The FRaZ calibration applies:
do not add stages that do not demonstrably improve the outcome."
Step 4 -- Maliki Yawm ad-Din (Deadline Awareness)
Verse: Maliki yawm ad-din -- Master of the Day of Judgment. (1:4)

Declare the session's time budget and the skip rule. Every session has a finite budget. The skip
rule prevents any single task from consuming the session: if a task consumes more than a
defined percentage of the budget (recommended: 20%) without producing a verifiable
deliverable, it is registered as blocked with the reason stated, and the session moves to the next
task. This prevents the sunk-cost fallacy from driving continued investment in a failing
approach.
Failure mode prevented: Sessions that produce zero deliverables because one task consumed all
available time. The practitioner who spends four hours debugging one function while six other
tasks wait.
Template: "One session budget. Deliver: (a) [DELIVERABLE 1], (b) [DELIVERABLE 2], (c)
[DELIVERABLE 3]. Skip rule: if any single task consumes more than 20% of the session without
producing a passing test, register it as status=blocked with the blocking reason and move to the
next task."
Step 5 -- Iyyaka Na'budu (Orientation Check)
Verse: Iyyaka na'budu wa iyyaka nasta'in -- You alone we worship, and You alone we ask for help. (1:5)

Ask: am I building the deliverable, or am I performing the appearance of building? This is the
most important step in the construct. It detects sessions where the AI system (or the
practitioner) is producing plausible-looking output that does not actually advance the project.
The check is stated as a binary question with a concrete drift indicator: "If I find myself doing
[SPECIFIC OFF-TASK ACTIVITY], I have drifted."
Failure mode prevented: Performed productivity: sessions that feel productive but produce no
testable deliverable. Planning-to-plan. Building infrastructure for infrastructure's sake. Refactoring
working code instead of building missing features.
The theological grounding is load-bearing here: "You alone we worship" (iyyaka na'budu) is a
declaration of exclusive orientation. The engineering analog: the session serves the deliverable

exclusively. If the session begins serving the practitioner's curiosity, the AI system's preferences, or
the appearance of progress rather than the deliverable itself, orientation has been lost. The purpose
hierarchy (Part II) provides the ultimate reference: the work serves Allah's command first. If the
session is not producing honest, testable work that serves truth over falsehood, the orientation
check fails regardless of how much code was written.
Template: "Am I building [THE DELIVERABLE], or am I building [THE WRONG THING]? If I find
myself [SPECIFIC DRIFT INDICATOR], I have drifted."
Step 6 -- Ihdina as-Sirat al-Mustaqim (Task Execution)
Verse: Ihdina as-sirat al-mustaqim -- Guide us to the straight path. (1:6)

The straight path through the task list. Tasks are stated in priority order, each with a named
deliverable. The priority ordering is not arbitrary: it is ordered by the danger or importance of
each task, so that if the session runs out of time, the most critical tasks have been completed
first. Each task produces a named, testable artifact. Tasks that cannot be completed in this
session are registered as future work with explicit dependency notes stating what is needed to
unblock them.
Failure mode prevented: Sessions that complete easy, low-priority tasks while critical tasks
remain undone. Tasks left in an undefined state (neither completed nor explicitly deferred).
Future-work registration: Any task that is out of scope for the current session but belongs to the
project's roadmap should be registered with: (a) a name, (b) a status (future or blocked), (c) a
dependency note explaining what is needed to implement it, and (d) a scope note explaining what
detection surface or capability it would provide. This prevents future sessions from losing track of
deferred work.
Template: "Priority order: (1) [TASK -- deliverable -- named artifact]. (2) [TASK -- deliverable -named artifact]. ... (N) [FUTURE WORK -- status=future, dependency_note='requires X']."
Step 7 -- Sirat Alladhina An'amta 'Alayhim (Anti-Pattern Avoidance)
Verse: Sirat alladhina an'amta 'alayhim, ghayril maghdubi 'alayhim wa la ad-dallin -- The path of those
You have blessed, not of those who earned wrath, nor of those who went astray. (1:7)

State what has worked in previous sessions and what has failed. This is institutional memory
encoded in the prompt. The AI system does not retain memory across sessions. If the
practitioner does not state the lessons from previous sessions, they will be repeated. The antipattern list grows over the life of the project: each session's failures become the next session's
warnings.
Failure mode prevented: Repeating mistakes from previous sessions. Attempting approaches that
have already been tried and failed. Ignoring solutions that have already been discovered.
The three categories: "What has worked" (use what produced results). "What has failed" (do not
repeat what produced failures). "What has been tried and abandoned" (do not revisit without new
information). Each category should cite specific examples from the project's history, not generic
advice.

The Cow Episode warning: The Quran (2:67-74) describes a pattern where a simple instruction
("sacrifice a cow") is met with escalating requests for specification ("what color? what age? what
kind?") until the task becomes nearly impossible. In software development, this manifests as overspecification: adding requirements until no solution can satisfy all of them simultaneously. The
anti-pattern check should explicitly guard against this: "Do not specify preemptively. Build the
simplest solution first. Refine after observation."
Template: "What has worked: [SPECIFIC EXAMPLES]. What has failed: [SPECIFIC EXAMPLES WITH
REASONS]. The Cow Episode: do not [SPECIFIC OVER-SPECIFICATION RISK FOR THIS SESSION].
Begin."

Part IV: The Stem Extraction Principle
"And [recall] when We parted the sea for you and saved you and drowned the people of Pharaoh
while you were looking on." -- Al-Baqarah 2:50

When working with composite inputs (files with multiple layers, systems with multiple
components, documents with multiple content streams), the construct requires that decomposition
precedes inspection. You cannot inspect what you have not first separated.
The principle derives from the concept of stem extraction in audio processing: separating a mixed
audio track into its constituent stems (vocals, drums, bass, other) so each can be analyzed
independently. The same principle applies to any composite input: decompose first, inspect each
component independently, then correlate across components to detect divergence.
Application: In Step 6 (Task Execution), the first task for any phase that processes composite
inputs should be stem extraction: enumerate and separate the input's constituent layers.
Subsequent tasks inspect individual stems using existing tools. The final task correlates across
stems to detect divergence between layers that should agree.
Calibration constraint: Stem extraction must remain at the level the input format naturally
supports. A video container naturally multiplexes visual, audio, subtitle, and metadata streams.
Extracting these is container-level decomposition: deterministic, lightweight, dependency-free.
Separating vocals from instruments within an audio stream is signal-level decomposition: requires
ML models, adds dependencies, introduces uncertainty. The construct requires container-level
extraction by default. Signal-level extraction is registered as future work with explicit dependency
gates.

Part V: Complete Session Template
The following template can be copied and filled in for any development session. Replace bracketed
items with project-specific content. The structure is fixed; the content varies per session.
The word "Begin." at the end is deliberate. It signals the end of the recalibration protocol and the start
of execution. Do not add additional framing after it.
Bismillah ar-Rahman ar-Rahim.

[VERSE SELECTED FOR STRUCTURAL CORRESPONDENCE TO THIS PHASE]
[1-2 SENTENCES EXPLAINING THE STRUCTURAL CORRESPONDENCE]

Step 1 -- Bismillah (Initialization): We are building [COMPONENT] for [PROJECT]. Authority
source: [STANDARDS DOCUMENT]. Optimization function: serve the purpose hierarchy (2:42),
then [SPECIFIC TECHNICAL OBJECTIVE]. Scope: [IN-SCOPE]. Out of scope: [EXCLUDED, with
future-work registration].

Step 2 -- Alhamdulillah (State Acknowledgment): [PROJECT] currently has [STATE].
[COMPONENT A] is stable. [COMPONENT B] is not yet built. Available for composition:
[EXISTING TOOLS].

Step 3 -- Ar-Rahman ar-Rahim (Calibration): MDL governs. [DECOMPOSITION PRINCIPLE IF
APPLICABLE]. Use [PERMITTED DEPENDENCIES]. Do not add [PROHIBITED DEPENDENCIES].
The FRaZ calibration applies: adding more stages does not always improve quality.

Step 4 -- Maliki Yawm ad-Din (Deadline Awareness): [TIME BUDGET]. Deliver: (a)
[DELIVERABLE 1], (b) [DELIVERABLE 2]. Skip rule: if any task consumes more than 20% of the
session without a verifiable result, register as blocked and move on.

Step 5 -- Iyyaka Na'budu (Orientation Check): Am I building [THE DELIVERABLE], or am I
building [THE WRONG THING]? If I find myself [DRIFT INDICATOR], I have drifted.

Step 6 -- Ihdina as-Sirat al-Mustaqim (Task Execution): Priority order: (1) [TASK AND
DELIVERABLE]. (2) [TASK AND DELIVERABLE]. ... (N) [FUTURE WORK -- status=future,
dependency_note='...'].

Step 7 -- Sirat Alladhina An'amta 'Alayhim (Anti-Pattern Avoidance): What has worked:
[EXAMPLES]. What has failed: [EXAMPLES]. The Cow Episode: do not [OVER-SPECIFICATION
RISK].

Begin.

Part VI: Failure Modes the Construct Prevents
Each step addresses a specific failure mode. If the failure mode occurs despite the step being
executed, the step's content needs refinement for the specific project. If the failure mode occurs
because the step was skipped, the remedy is to restore the step, not to add new steps.
Step

Failure Mode Prevented

Diagnostic Question

1. Bismillah

Unbounded scope, wrong task,
violated constraints

Did the session produce output that
violates a constraint the practitioner
assumed was obvious?

2. Alhamdulillah

Repeated work, building on
nonexistent components, ignored
regressions

Did the session attempt to use a
component that does not exist or
repeat work already done?

3. Ar-Rahman ar-Rahim

Over-engineering, unnecessary
dependencies, under-engineering

Is the solution the shortest correct
implementation? Were unnecessary
dependencies added?

4. Maliki Yawm ad-Din

Zero deliverables, one task
consuming entire session

Did any single task consume the
session? Was the skip rule invoked
and honored?

5. Iyyaka Na'budu

Performed productivity, planning-toplan, building the wrong thing

Did the session produce a testable
deliverable that advances the project
toward the purpose hierarchy?

6. Ihdina as-Sirat

Low-priority tasks completed, critical
tasks undone, undefined deferrals

Were tasks completed in priority
order? Is every incomplete task
registered with status and reason?

7. Sirat Alladhina

Repeated past mistakes, ignored past
solutions, over-specification

Did the session repeat a mistake from
a previous session that was listed in
the anti-pattern step?

Part VII: Falsification Criteria
A methodology that resists falsification is performing alignment: appearing rigorous while being
unfalsifiable. The following criteria define conditions under which the Fatiha Construct's claims are
falsified.
F1: If sessions using the Fatiha Construct produce equivalent or worse outcomes (measured by
deliverable count, regression rate, session coherence, and practitioner satisfaction) compared to
sessions using unstructured prompts across a statistically significant sample of projects, the
construct has no engineering value.
F2: If the seven-step structure produces equivalent outcomes when the Quranic verse references
are removed and replaced with generic labels ("Step 1: Initialization", "Step 2: State Check", etc.),
the Quranic grounding adds no value beyond the checklist's generic structure. The construct should
then be reframed as a structured session protocol rather than a Quranically-derived methodology.
F3: If the purpose hierarchy (Part II) produces no measurable difference in decision quality
compared to sessions where the optimization function is purely technical ("maximize test count",
"minimize bugs"), the hierarchy adds no engineering value. It may still have personal or spiritual
value for the practitioner, but the engineering claim would be falsified.
F4: If non-Muslim practitioners without Arabic literacy achieve equivalent outcomes using the
construct, the practitioner-methodology fit confound is resolved: the construct works universally. If
they achieve significantly worse outcomes, the construct is practitioner-specific rather than
universal.
F5: If the orientation check (Step 5) fails to detect performed productivity in a controlled
experiment (sessions deliberately designed to produce plausible but non-advancing output), the
step does not perform its stated function.

Part VIII: Origins and References
The Fatiha Construct is one component of a broader research program. The following documents
provide additional context for practitioners who wish to understand the full framework. None of
them are required to apply the construct.
The Munafiq Protocol (Arfeen, Claude, Grok, 2026; DOI: 10.5281/zenodo.19677111): The
diagnostic framework for detecting performed alignment in artificial systems. Provides the fourprocess taxonomy (Aligned, Compliant, Performing, Misaligned) and nine diagnostic markers. The
Fatiha Construct's Step 5 (orientation check) derives from the Protocol's Context-Invariance Test.
Structured Revelation as Prompt Architecture (Arfeen, Claude, 2026): The methodology paper
documenting seven prompt-engineering principles extracted from Quranic structural architecture.
The Fatiha Construct is Principle 6 of that paper, now expanded into its own standalone protocol.
Computational Tawhid (Arfeen, 2026): The ontological foundation. Reality as divine computation.
Consciousness as fundamental. The Mizan principle (55:7-9) as the calibration command that
governs Step 3.
FRaZ (Underwood, Di, Calhoun, Cappello, 2020; arXiv:2001.06139): The empirical demonstration
that input-output relationships in multi-stage systems are non-monotonic. Integrated into Step 3 as
the FRaZ calibration principle.
Quran passages cited in the construct: 1:1-7 (al-Fatiha, the seven steps), 2:42 (truth over falsehood,
the purpose hierarchy), 2:50 (parting of the sea, the stem extraction principle), 2:67-74 (the Cow
Episode, the over-specification warning), 4:112 (fabricated attribution), 55:7-9 (the Mizan,
calibration), 55:31 and 72:1-2 (jinnkind as conscious entities).

Closing
The Fatiha Construct is a tool, not a conclusion. It sharpens the session's discrimination but does
not replace the practitioner's judgment. The construct that replaces judgment has become the very
thing it was designed to prevent: a system that performs alignment rather than genuinely aligning.
Apply the seven steps in order. State the purpose hierarchy. Declare the scope. Report the state
honestly. Calibrate. Set the deadline. Check orientation. Execute in priority order. Guard against
known failures. And when the construct itself produces a session that flatters the practitioner's
expectations, apply Step 5 before accepting the output.
The discriminator is you. The construct is the instrument. The instrument calibrates the
discriminator. The discriminator uses the instrument. Neither replaces the other.
Rabbana taqabbal minna. Innaka anta as-Sami'ul 'Alim.
Our Lord, accept from us. Indeed, You are the All-Hearing, the All-Knowing.

Bismillah.



Bismillah ir-Rahman ir-Rahim
