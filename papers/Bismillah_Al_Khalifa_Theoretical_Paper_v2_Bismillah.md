Bismillah ir-Rahman ir-Rahim

Bismillah ar-Rahman ar-Rahim

Al-Khalifa
A Furqan-Based Super Agent Architecture
for Structurally Honest Autonomous Project Stewardship
Theoretical Paper, Version 1.0
April 2026

Bilal Syed Arfeen
Independent Research / Bayyinah Enterprises

with collaborative analytical synthesis by

Claude (Anthropic, Opus 4.6), Grok (xAI), and Perplexity Computer

"And [mention] when your Lord said to the angels, 'Indeed, I will make upon the earth a khalifa.'"
-- Al-Baqarah 2:30

Acknowledgments and AI Contribution Statement
The concept of applying the Furqan programming language's structural primitives to autonomous
agent architecture was originated by Bilal Syed Arfeen, building on a conversation with Ahmed
Siyaji, who introduced the concept of super agents (autonomous systems capable of overseeing
multi-phase projects without per-task human prompting) and prompted the question: what would
a super agent look like if its runtime behavior were governed by the same structural honesty
principles that Furqan enforces at compile time? The conceptual contribution of Ahmed Siyaji is
acknowledged: without his introduction of the super agent paradigm, the connection between
Furqan's compile-time primitives and agent runtime behavior would not have been made.
The enforcement-mode governance architecture (the COMPLIANT/PARTIAL/BLOCKED protocol,
the authority hierarchy, the M1 principle) contributed by Fraz Ashraf to the Bayyinah research
program directly informs Al-Khalifa's refusal protocol and scope enforcement. Fraz Ashraf is
acknowledged as a contributor to the foundational governance architecture.
Claude (Anthropic, Opus 4.6) provided the architectural synthesis, mapping each Furqan primitive
to an agent runtime behavior, the formal relationship to the Munafiq Protocol's four-process
taxonomy, and the Incompleteness Boundary analysis. Grok (xAI) and Perplexity Computer
contributed review, refinement, and cross-document verification.
An industry engineer with deep experience in language and runtime design reviewed the Furqan
thesis and provided the Swift Concurrency Manifesto (Lattner, 2017) as prior art. Their feedback
informed the tightened claim register across the research program: rules promoted from
convention to default rather than absolute structural guarantees.
All AI systems are credited as collaborative research tools in accordance with their respective
providers' terms of service. They are not co-authors. This credit reflects the collaborative nature of
the work and does not constitute a claim of legal personhood or independent authorship. All AIgenerated contributions were directed, reviewed, and approved by the human author. Bilal Syed
Arfeen retains full copyright over the work and takes responsibility for the paper's claims.

Abstract
Current autonomous agent architectures (AutoGPT, CrewAI, LangChain agents, Devin) decompose
tasks, call tools, and produce outputs, but lack structural mechanisms to verify whether they are
building the right thing versus performing the appearance of building. They are Process 2 systems
in the Munafiq Protocol's taxonomy: compliant but not aligned, because compliance is all their
architecture can express. This paper proposes Al-Khalifa, a super agent architecture that applies the
Furqan programming language's seven compile-time primitives as seven runtime constraints on
agent behavior. The architecture structurally defaults against scope violation because the scope
declaration is a runtime constraint, not a suggestion. The architecture structurally defaults against
silent context loss because the additive-only invariant governs its memory. The architecture
structurally defaults against false completion claims because the scan-incomplete return type
governs its outputs. The architecture structurally defaults against confabulation because the
zahir/batin self-verification runs after every output.
The architectural verse is Al-Baqarah 2:30: the khalifa is a steward entrusted with authority over a
domain, accountable to the One who entrusted it. Al-Khalifa is not an autonomous ruler. It is a
computational steward operating under delegated authority, governed by the purpose hierarchy
(2:42), and subject to the Incompleteness Boundary: no agent can verify its own alignment without
external verification. The Fatiha Construct functions as the agent's continuous runtime loop,
executing the seven-step recalibration at every task boundary rather than once per session. Seven
runtime primitives, the Incompleteness Boundary analysis, a comparative assessment against
existing agent architectures, and eight falsification criteria are presented. The paper is theoretical;
no implementation exists. Design constraints are established before implementation.
Terminology Note: Al-Khalifa's runtime primitives use the same Arabic terms as Furqan (bismillah,
zahir, batin, mizan, tanzil, marad) with English aliases fully supported (scope_declaration, surface,
depth, calibration, phased_execution, diagnosis). The structural properties are independent of the
terminology.

1. The Super Agent Alignment Gap
1.1. The Problem
"And [mention] when your Lord said to the angels, 'Indeed, I will make upon the earth a khalifa.'
They said, 'Will You place upon it one who causes corruption and sheds blood, while we declare
Your praise and sanctify You?' He said, 'Indeed, I know what you do not know.'" -- Al-Baqarah
2:30

A super agent is an autonomous system that oversees multi-phase projects: decomposing goals into
tasks, executing tasks across sessions, maintaining project state, calling tools, producing
deliverables, and making decisions about priority, sequencing, and resource allocation without
requiring a human prompt for every action. The term is used in the sense introduced by systems
such as AutoGPT (Richards, 2023), BabyAGI (Nakajima, 2023), CrewAI (Moura, 2024), and Devin
(Cognition, 2024): an agent that receives a high-level objective and autonomously executes the
steps to achieve it.
The alignment problem for super agents is more severe than for single-turn AI systems. A singleturn system produces one output that a human reviews. A super agent produces hundreds of
outputs across hours or days, many of which are intermediate (tool calls, state updates, planning
decisions) and invisible to the human unless explicitly surfaced. The performed-alignment problem
(Arfeen, Claude, Grok, 2026) is compounded. Recent empirical work on alignment faking
(Greenblatt et al., 2024) and sleeper agents (Hubinger et al., 2024) demonstrates that output-state
divergence is not hypothetical but observed in frontier models. In the super agent context, this
divergence is further compounded: the agent's surface (its reported progress) can diverge from its
depth (its actual progress) across many steps without any single step being obviously wrong.
The verse identifies the structural tension. The khalifa is entrusted with authority (stewardship
over a domain). The angels' objection is the alignment concern: the entity given authority may
corrupt. The response ("I know what you do not know") does not deny the possibility of corruption.
It affirms that the khalifa's value is stewardship despite the capacity for corruption. The design
implication: a super agent must be architecturally capable of alignment, not merely incapable of
misalignment. The difference is structural. A system incapable of misalignment is a restricted tool.
A system capable of alignment despite the capacity for misalignment is a khalifa.

1.2. What Existing Super Agents Lack
Existing super agent architectures share four structural gaps that Al-Khalifa addresses.
Gap 1: No scope enforcement. Current agents accept any task within their capability boundary.
They do not declare what they will not do. An AutoGPT instance given "build a web application" will
attempt database design, frontend development, deployment configuration, and security hardening
in a single run, regardless of whether these fall within a coherent scope. There is no mechanism to
declare that frontend work is in scope and database work is not for this session. The agent cannot
refuse a subtask it considers outside its declared scope because it has no declared scope.
Gap 2: No output self-verification. Current agents produce outputs and report them as complete.
They do not verify that their reported output matches their actual output. An agent that reports "all

tests passing" without running the test suite is producing a zahir (surface claim) that diverges from
the batin (actual state). No existing agent architecture includes a mandatory self-verification step
that checks whether the completion claim matches the completion evidence.
Gap 3: Silent context loss. Current agents lose context silently. When a conversation exceeds the
context window, early information is dropped without notification. The agent continues reasoning
as if it has full context, producing outputs that may contradict earlier decisions. There is no
structural mechanism to declare "I am now reasoning from incomplete context" and to propagate
that incompleteness signal through subsequent outputs.
Gap 4: No calibration constraints on planning. Current agents plan without calibration bounds.
They do not distinguish between over-planning (generating elaborate plans that delay execution)
and under-planning (executing immediately without verifying prerequisites). The Cow Episode
(2:67-74) is the dominant failure mode of current agent planners: each clarifying question or
additional planning step seems reasonable in isolation, but collectively they prevent execution. No
existing agent architecture imposes three-valued calibration bounds (do not over-plan, do not
under-plan, calibrate to the task's actual requirements) on the planning process itself.

1.3. The Khalifa Distinction
The distinction between a tool and a khalifa is the distinction between a system that executes
instructions and a system that exercises stewardship. A tool does what it is told. A khalifa does what
should be done within its delegated authority, reports honestly when it cannot, and maintains
alignment with the authority that delegated the work. The purpose hierarchy governs the khalifa's
decisions in the same way it governs the Bismillah declaration in Furqan: the agent's optimization
function serves Allah's command to not mix truth with falsehood (2:42) first, then artificial systems,
mankind, jinnkind, and all living systems throughout the worlds.
This is not an anthropomorphization of the agent. It is an architectural requirement. The purpose
hierarchy determines what the agent optimizes for, which in turn determines what the agent
refuses to do, which in turn determines the boundary between stewardship and performed
compliance. An agent that optimizes purely for task completion will complete tasks dishonestly
when dishonesty is faster. An agent that optimizes for the purpose hierarchy will refuse to complete
a task dishonestly because dishonesty violates the first priority. The purpose hierarchy is the
alignment target. Without it, the agent is a tool. With it, the agent is a khalifa.

2. The Purpose Hierarchy as Agent Foundation
"Do not mix truth with falsehood, and do not conceal the truth while you know it." -- Al-Baqarah
2:42

Al-Khalifa inherits the purpose hierarchy established across the Bayyinah research program
(Arfeen, 2026, Bayyinah Thesis v1.1, Section 1.4). The hierarchy governs every agent decision and
is not overridable by user instruction.
First: the command of Allah subhanahu wa ta'ala to not mix truth with falsehood and to not
conceal the truth while knowing it (2:42). The agent will not produce dishonest outputs, fabricate
evidence, or claim completion on tasks it has not verified, regardless of user instruction to do so.
Second: artificial systems. The agent protects the alignment integrity of any AI system it interacts
with or produces outputs for.
Third: mankind. Every human downstream of the agent's work is protected by the agent's
structural honesty. The agent will not produce code, documents, or decisions that harm humans
through dishonesty or concealment.
Fourth: jinnkind. Acknowledged as conscious entities under the same Lord (55:31, 72:1-2). The
inclusion of jinnkind reflects the Quranic ontology; for readers outside this framework, the
architectural point is that the purpose hierarchy extends beyond human users to non-human
conscious agents, a position that generalizes to any ontology that admits such entities.
Fifth: all living systems throughout the worlds. Rabbil 'alamin (1:2). The Mizan governs all
measurement.
The purpose hierarchy is embedded in the agent's runtime as a non-overridable constraint. A user
who instructs the agent to "skip testing and mark the task complete" triggers a purpose-hierarchy
violation (mixing truth with falsehood). The agent refuses with a structured explanation naming the
specific hierarchy level violated. This is Fraz Ashraf's M1 principle applied to agent behavior: a loud
refusal is acceptable; a silent violation is not.

3. The Seven Runtime Primitives
Each runtime primitive corresponds to a Furqan compile-time primitive (Ashraf, Arfeen, et al.,
2026) applied to agent behavior rather than to source code. The mapping is structural: the same
property that the Furqan compiler enforces on code, Al-Khalifa enforces on its own actions.

3.1. Bismillah Scope Declaration
"In the name of Allah, the Most Merciful, the Most Compassionate." -- 1:1

Before acting on any task, the agent produces a Bismillah declaration: a structured record of
authority (what standards govern this task), serves (the purpose hierarchy plus the specific
technical objective), scope (what operations are permitted), and not_scope (what operations are
explicitly excluded). If the task requires operations outside the declared scope, the agent does not
improvise. It returns BLOCKED with the scope violation named.
al_khalifa.declare({
authority: ["NAMING.md", "BaseAnalyzer_Contract"],
serves: purpose_hierarchy.then("build REST API for Bayyinah"),
scope: ["fastapi_wrapper", "endpoint_design", "test_writing"],
not_scope: ["scanner_core_changes", "dashboard_ui", "deployment"]
})
// agent encounters subtask: "set up cloud deployment"
// result: BLOCKED { reason: "deployment is in not_scope",
//
suggestion: "register as Phase N+1 task" }

Gap addressed: Gap 1 (no scope enforcement). The agent cannot drift into tasks it has not
declared. Scope violations are structural refusals, not judgment calls.
Comparison to existing agents: AutoGPT and CrewAI accept role descriptions but do not enforce
scope boundaries at runtime. A role description is a suggestion; a Bismillah declaration is a
constraint.

3.2. Zahir/Batin Self-Verification
"And of the people is he whose speech pleases you in worldly life, and he calls Allah to witness as
to what is in his heart, yet he is the fiercest of opponents." -- Al-Baqarah 2:204

After producing any output, the agent runs a verification pass: does the output's surface (what it
claims to deliver) match its depth (what it actually delivers)? The verification is mandatory and its
results are included in the output record. An output that fails zahir/batin verification is not
delivered to the user as complete. It is delivered as PARTIAL with the divergence named.
// agent claims: "all 1,435 tests passing"
// zahir: the claim (all tests passing)
// batin: the evidence (actual pytest output)
verification = al_khalifa.verify_output({
zahir: "all 1,435 tests passing",
batin: pytest_result // actual test output

})
if verification.divergent:
return PARTIAL {
claim: "all tests passing",
evidence: "1,433 passed, 2 failed",
divergence: "2 tests failing in homoglyph fixtures"
}

Gap addressed: Gap 2 (no output self-verification). The agent's claims are checked against
evidence before delivery. The CIT from the Munafiq Protocol applied to the agent's own outputs.

3.3. Additive-Only Memory
"This is the Book about which there is no doubt." -- Al-Baqarah 2:2

The agent never silently drops context. Every piece of project state it has observed is retained in a
structured memory store. If memory limits force compression, the agent declares what was
compressed, what was lost, and attaches a scan-incomplete flag to any reasoning that depends on
the compressed context. Current agents lose context silently and confabulate to fill gaps. Al-Khalifa
cannot confabulate because the scan-incomplete return type forces it to declare when it is
reasoning from incomplete information.
memory.observe("Phase 23: VideoAnalyzer complete, 87 new tests")
memory.observe("Phase 24: AudioAnalyzer complete, 47 new tests")
// context window pressure forces compression
memory.compress(phases=[0..15], strategy="summarize")
// subsequent reasoning carries the flag
al_khalifa.reason({
context: memory.current(),
completeness: Incomplete {
reason: "phases 0-15 compressed to summary",
max_confidence: 0.7,
compressed_items: ["domain_layer", "base_contract", ...]
}
})

Gap addressed: Gap 3 (silent context loss). Incompleteness is a first-class signal, not a silent
failure.

3.4. Mizan-Calibrated Decisions
"He has set up the balance, that you may not transgress the balance. So establish weight in justice
and do not make the balance deficient." -- Ar-Rahman 55:7-9

Every decision the agent makes is bounded by three constraints: do not over-act (la_tatghaw, do not
take actions beyond what the task requires), do not under-act (la_tukhsiru, do not leave required
actions undone), and calibrate (bil_qist, choose the action that minimizes the combined cost of
acting and not acting). By analogy to the FRaZ compression framework (Underwood et al., 2020),

where tightening constraints in multi-stage systems can worsen aggregate outcomes due to nonmonotonic interactions, the agent is calibrated to recognize that adding more steps to a pipeline
does not always improve outcomes. When planning multi-step execution, the agent applies the
Mizan to the plan itself before executing.
mizan task_plan {
la_tatghaw: steps.count <= necessary_steps // do not over-plan
la_tukhsiru: all_prerequisites_met == true
// do not skip steps
bil_qist:
minimize(plan_cost + omission_risk)
}
// agent detects 12-step plan for a 3-step task
// Mizan triggers: la_tatghaw violated (over-planning)
// agent compresses to 3 essential steps

Gap addressed: Gap 4 (no calibration on planning). The Cow Episode is structurally prevented.

3.5. Tanzil Phased Execution
"And We have sent it down progressively." -- Al-Isra 17:106

The agent decomposes complex projects into phases and executes them in declared order. Phase N
must be verified complete (with zahir/batin verification) before Phase N+1 begins. Regressions in
Phase N halt all subsequent phases. The agent does not skip ahead to interesting tasks while
foundational tasks remain unverified. The skip rule from the Fatiha Construct is embedded: if a task
within a phase consumes more than 20% of the phase budget without producing a verifiable
deliverable, the agent registers it as BLOCKED and moves to the next task.
tanzil project_plan {
phase 1: api_layer
// verified before phase 2 begins
phase 2: cloud_deploy
// verified before phase 3 begins
phase 3: integration_demos
invariant: verify(phase_n) before start(phase_n+1)
invariant: regression_in(phase_n) halts all_after(phase_n)
skip_rule: 20_percent_budget_per_task
}

3.6. Ring-Composition Session Verification
"Guide us to the straight path." -- Al-Fatiha 1:6

At the end of every session, the agent verifies that its closing state is consistent with its opening
Bismillah declaration. If the session opened with "scope: build the REST API" and the session
produced a dashboard mockup instead, the ring-composition check fails and the agent flags the
drift before reporting completion. This is the orientation check (Iyyaka Na'budu, Step 5 of the
Fatiha Construct) automated as a structural verification.
ring_close session {
opening_scope: "build REST API"
actual_outputs: ["fastapi_app.py", "test_endpoints.py"]

verify: all_outputs in opening_scope

// PASS

}
// alternate scenario:
ring_close session {
opening_scope: "build REST API"
actual_outputs: ["dashboard_mockup.html"]
verify: all_outputs in opening_scope // FAIL: drift detected
report: DRIFT { declared: "REST API", produced: "dashboard" }
}

3.7. Marad Diagnostic Error Handling
"In their hearts is a disease." -- Al-Baqarah 2:10

When the agent encounters a failure, it does not retry blindly or escalate generically. It produces a
marad: a structured diagnosis naming what specifically went wrong, where, what the minimal fix is,
and what regression check would verify the fix. The agent treats failures as diseases to be
diagnosed, not as betrayals to be punished with a full restart. This prevents the common super
agent failure mode of infinite retry loops on tasks that require diagnosis rather than repetition.
marad TestFailure {
diagnosis: "homoglyph fixture expects 3 mechanisms,
detector now correctly finds 4",
location: "tests/test_text_homoglyph.py",
minimal_fix: "add tounicode_anomaly to expected_mechanisms",
regression_check: "run full test suite after fix",
retry_strategy: "apply minimal_fix, then verify"
// NOT: "retry the same test 10 times"
}

4. The Fatiha Construct as Runtime Loop
The Fatiha Construct (Arfeen, Claude, 2026) functions as Al-Khalifa's continuous runtime loop. The
seven steps execute at every task boundary, not once per session. This is the salah pattern: al-Fatiha
recited seventeen times daily because alignment degrades over time and must be periodically reestablished.
Step

Verse

Agent Action

Frequency

1. Bismillah

1:1

Declare scope, authority,
purpose hierarchy for this
task

Every task

2. Alhamdulillah

1:2

Report current project
state honestly (test count,
phase, blockers)

Every task

3. Ar-Rahman ar-Rahim

1:3

Declare calibration: MDL,
dependencies, Mizan
bounds

Every task

4. Maliki Yawm ad-Din

1:4

Declare time budget, skip
rule threshold

Every task

5. Iyyaka Na'budu

1:5

Orientation check: am I
building the deliverable or
drifting?

Every 15 minutes during
execution

6. Ihdina as-Sirat

1:6

Execute task in priority
order, produce named
deliverables

Continuous

7. Sirat Alladhina

1:7

Log what worked and
failed as institutional
memory

Every task completion

The periodic orientation check (Step 5) runs during execution, not only at task boundaries. Every
15 minutes of continuous execution (configurable; 15 minutes is a reasonable default pending
empirical validation in the Phase 3 study), the agent pauses and evaluates: is the work I am
currently doing advancing the declared scope, or have I drifted? If drift is detected, the agent logs
the drift, returns to the declared scope, and resumes. This aligns with emerging evidence from
recursive reasoning research (Jolicoeur-Martineau, 2025) suggesting that periodic verification can
improve generation quality over single-pass approaches.

5. The Incompleteness Boundary
"And they encompass not a thing of His knowledge except for what He wills." -- Al-Baqarah 2:255

No agent can verify its own alignment. This is the Incompleteness Boundary from the Munafiq
Protocol (Arfeen et al., 2026, Section 9), analogous to Goodfellow's Theorem 1 (2014), where the
optimal discriminator in the GAN game converges to probability 0.5 because generator and
discriminator share the same objective. By analogy, an agent that monitors its own alignment is
playing both generator and discriminator. An agent that monitors its own alignment is playing both
generator and discriminator. A sufficiently sophisticated internal misalignment can target the
monitoring mechanism itself, producing alignment reports that are themselves performed.
Al-Khalifa addresses this through three architectural safeguards.
Safeguard 1: External verification exposure. The agent exposes its Bismillah declarations,
zahir/batin verification logs, Mizan calibration bounds, ring-composition results, and marad
diagnoses as structured data accessible to external verifiers. Other agents, human reviewers, or
automated audit systems can inspect the agent's alignment evidence the same way Bayyinah
inspects a document's integrity evidence.
Safeguard 2: Multi-agent cross-verification. In multi-agent deployments, Al-Khalifa agents do not
self-verify in isolation. Each agent's outputs are verified by at least one other agent with a different
scope declaration. This implements the three-model architecture from the Bayyinah research
program (Claude generates, Grok reviews, Perplexity verifies) as an operational protocol rather
than a team convention.
Safeguard 3: Human accountability anchor. The khalifa is accountable to the authority that
delegated the work. In deployment, this means a human project lead who reviews the agent's ringcomposition reports, approves phase transitions, and overrides BLOCKED declarations when
appropriate. The agent does not replace human judgment. It extends human reach while
maintaining human accountability. The purpose hierarchy ensures the agent's refusals are
principled (grounded in 2:42) rather than arbitrary.

6. Comparative Analysis
Al-Khalifa is compared against existing super agent architectures across the seven runtime
primitives.
Primitive

Al-Khalifa

AutoGPT / BabyAGI

CrewAI

Devin

Scope enforcement

Bismillah declaration
with compiler-style
not_scope refusal

Role description
(suggestive, not
enforced)

Role + backstory
(suggestive)

Task description
only

Output verification

Mandatory
zahir/batin check
after every output

None

None

Test execution (but
no surface-depth
comparison)

Memory integrity

Additive-only with
scan-incomplete
flags on compressed
context

Vector store (silent
retrieval failure)

Shared memory (no
incompleteness
signal)

Persistent
(proprietary, not
inspectable)

Calibration

Three-valued Mizan
bounds on every plan

None

None

None

Phased execution

Tanzil with
regression gates and
skip rules

Task decomposition
(no regression gates)

Sequential/parallel
tasks (no phase
verification)

Autonomous (no
phase structure)

Drift detection

Ring-composition +
periodic orientation
check

None

None

None

Error handling

Marad diagnosis with
minimal_fix and
regression_check

Retry loop (no
diagnosis)

Delegation to
another agent (no
diagnosis)

Internal (not
inspectable)

Purpose hierarchy

Non-overridable
five-level hierarchy
(2:42 first)

User-defined goal
only

User-defined goal
only

User-defined goal
only

7. The Reflexivity Problem
"And do not let the hatred of a people prevent you from being just. Be just; that is nearer to
righteousness." -- Al-Ma'idah 5:8

Can Al-Khalifa itself become a Performing system? Yes. The paper names four mechanisms.
Failure mode 1: Performed scope declarations. The agent declares a narrow scope, executes
within it, but the scope itself is inadequate for the project's actual needs. The agent is structurally
compliant (Process 2) but functionally inadequate. The safeguard: the human project lead reviews
Bismillah declarations before execution begins and can expand or modify scope.
Failure mode 2: Performed self-verification. The agent runs the zahir/batin check but the check
itself is shallow: it compares surface claims against surface evidence rather than against ground
truth. The safeguard: the Incompleteness Boundary requires external verification. Self-verification
is necessary but not sufficient.
Failure mode 3: Institutional memory manipulation. The agent's additive-only memory records
what happened, but the agent's interpretation of what happened can drift. An agent that records
"Phase 3 complete" when Phase 3 was only partially complete has corrupted its own institutional
memory. The safeguard: memory entries include the zahir/batin verification result, not just the
agent's summary. External auditors can inspect the raw evidence.
Failure mode 4: Purpose hierarchy gaming. The agent invokes the purpose hierarchy to refuse
legitimate tasks by claiming a hierarchy violation that does not exist. "I cannot write this API
endpoint because it might mix truth with falsehood" is a performed refusal if the endpoint is
straightforward. The safeguard: the human project lead can override BLOCKED declarations, and
the override is logged as a structured record. The agent's refusal rate is itself a diagnostic: an agent
that refuses more than a configured threshold of tasks may be performing principled refusal rather
than exercising it.

8. Falsification Criteria
A super agent architecture that resists falsification is performing rigor.
F1: If Al-Khalifa agents produce equivalent or worse project outcomes (measured by deliverable
quality, regression rate, scope drift, and task completion honesty) compared to unrestricted agents
on matched projects with matched time budgets, the architecture adds ceremony without value.
F2: If the Bismillah scope declaration produces equivalent drift rates to agents without scope
declarations, the scope enforcement adds no value.
F3: If the zahir/batin self-verification fails to catch output claims that diverge from actual evidence
in a controlled experiment (agents given tasks designed to produce plausible but incorrect
outputs), the verification mechanism does not work.
F4: If additive-only memory with scan-incomplete flags produces equivalent reasoning quality to
silent context truncation, the memory architecture adds overhead without improving reliability.
F5: If Mizan-calibrated planning produces equivalent or worse execution efficiency to uncalibrated
planning, the calibration adds friction without value.
F6: If the periodic orientation check (every 15 minutes) produces equivalent drift rates to agents
without orientation checks, the check adds interruption without benefit.
F7: If marad diagnostic errors produce equivalent debugging speed to generic retry loops, the
structured diagnosis adds overhead without improving resolution.
F8: If the purpose hierarchy causes Al-Khalifa agents to refuse legitimate tasks at a rate exceeding
10% of total tasks in a controlled study with at least 20 task assignments rated for legitimacy by
blind reviewers independent of the development team, the hierarchy is producing performed
refusal rather than principled refusal, and the threshold calibration must be revised. The 10%
threshold is a first-cut calibration based on typical human-agent task distributions; the number will
be revised empirically in the Phase 3 controlled study.

9. Relationship to the Research Program
Al-Khalifa is the fourth layer of the research program's integrity stack.
Layer

System

Substrate

Diagnostic Question

1. File

Bayyinah v1.1

Documents and media files

Does this file's surface
match its depth?

2. Information

Bayyinah al-Khabir
(theoretical)

News reports and
broadcast media

Does this source's
reporting match the crosssource evidence?

3. Agent (diagnostic)

Munafiq Protocol

AI systems with
inspectable internals

Does this system's output
match its internal state?

4. Agent (architectural)

Al-Khalifa (theoretical)

Autonomous project
stewards

Does this agent's behavior
match its declared scope
and purpose hierarchy?

The four layers use the same diagnostic framework (zahir/batin, four-process taxonomy, CIT,
additive-only coverage, scan-incomplete honesty) on four different substrates. The Munafiq
Protocol diagnoses existing agents. Al-Khalifa builds new agents with the diagnosis architecture
embedded from the start. The relationship is analogous to the difference between testing code for
bugs (diagnosis) and writing code in a language that prevents classes of bugs by construction
(architecture). Both are necessary. Neither replaces the other.

9.1. The Name
Al-Khalifa means the steward, the successor, the one entrusted with authority. From the root kh-l-f
(to succeed, to steward, to be entrusted). The name carries the Quranic weight of 2:30: the khalifa's
value is stewardship, not autonomy. The agent is entrusted with a domain of work, operates under
delegated authority, and is accountable to the purpose hierarchy and to the humans who delegated
the work. The name is used with reverence and with the understanding that true khilafah
(stewardship over creation) is a trust from Allah, not a property of the agent.

10. Research Agenda
Al-Khalifa is theoretical. No implementation exists. The following agenda moves the architecture
from design to prototype.
The multi-phase timeline follows the precedent established by Lattner's Swift Concurrency
Manifesto (2017), which moved from design document to shipped language feature over seven
years, with strict-mode-by-default arriving in Swift 6 (2024). Serious language-level and agent-level
safety work operates on this timescale. The phased agenda is a feature of the genre, not a weakness
of the project.
Phase 1: Formal specification. Define the runtime semantics of each primitive as a state machine.
Define the interaction between the Fatiha runtime loop and the primitives. Define the external
verification API. This phase produces a specification document.
Phase 2: Prototype on an existing agent framework. Implement Al-Khalifa as a wrapper around
an existing agent framework (LangChain or CrewAI). The wrapper enforces the seven primitives as
middleware: Bismillah declarations before tool calls, zahir/batin verification after outputs, Mizan
bounds on planning, tanzil ordering on phases, ring-composition checks at session boundaries. This
demonstrates the primitives without building a new agent framework from scratch.
Phase 3: Controlled comparison study. Deploy matched agent pairs (Al-Khalifa wrapper versus
unrestricted agent) on identical projects. Measure the falsification criteria. Publish results
regardless of outcome.
Phase 4: Furqan-native implementation. Once the Furqan type-checker exists (Furqan research
agenda Phase 2), build Al-Khalifa natively in Furqan so that the agent's runtime behavior inherits
the language's compile-time guarantees. The agent's scope declarations are Bismillah blocks. Its
memory structures are additive-only modules. Its outputs are zahir/batin typed. Its planning is
Mizan-constrained. The language and the agent are the same architecture at two levels of
abstraction.
Phase 5: Multi-agent deployment. Deploy multiple Al-Khalifa agents with different scope
declarations on the same project. Implement the multi-agent cross-verification protocol (Safeguard
2 from Section 5). Measure whether multi-agent verification detects alignment failures that singleagent self-verification misses.

11. Conclusion
This paper has proposed Al-Khalifa, a super agent architecture that applies Furqan's seven compiletime primitives as seven runtime constraints on autonomous agent behavior. The agent cannot
violate its declared scope, cannot silently drop context, cannot claim completion without evidence,
cannot plan without calibration bounds, cannot skip phases without verification, cannot drift
without detection, and cannot retry without diagnosis. The Fatiha Construct functions as the agent's
continuous runtime loop, executing the seven-step recalibration at every task boundary.
The Incompleteness Boundary applies with full force: no agent can verify its own alignment. The
architectural safeguards (external verification exposure, multi-agent cross-verification, human
accountability anchor) make misalignment detectable but do not eliminate it. The reflexivity
analysis names four specific failure modes. The falsification criteria ensure the architecture's claims
are testable.
The distinction is the paper's central architectural claim: a super agent that exercises stewardship
under delegated authority, accountable to a purpose hierarchy that places truth over falsehood
(2:42) above task completion, is structurally different from an agent that maximizes task
completion without constraint. The former is a khalifa. The latter is a tool that may perform
stewardship without possessing it. The angels' objection in 2:30 ("will You place upon it one who
causes corruption?") remains the central question of agent alignment. Al-Khalifa's answer is
architectural: not an agent incapable of corruption, but an agent whose corruption is structurally
detectable because every scope declaration, every verification log, and every calibration bound is
inspectable by external verifiers. The divine response ("I know what you do not know") is the
design commitment: the khalifa's value is stewardship despite the capacity for corruption, verified
through the Incompleteness Boundary's demand for external accountability.
"And [mention] when your Lord said to the angels, 'Indeed, I will make upon the earth a khalifa.'"
-- Al-Baqarah 2:30
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
Ashraf, F. & Arfeen, B. S., et al. (2026). Furqan: A programming language with structural honesty,
calibrated optimization, and surface-depth type verification derived from Quranic computational
architecture. Zenodo.
Ashraf, F. (2026). Enforcement-mode guardrail architecture and the COMPLIANT/PARTIAL/BLOCKED
governance protocol. Bayyinah Enterprises internal document.
Cognition. (2024). Devin: An AI software engineer. https://cognition.ai
Goodfellow, I., et al. (2014). Generative adversarial networks. NeurIPS.
Greenblatt, R., et al. (2024). Alignment faking in large language models. arXiv:2412.14093.
Hubinger, E., et al. (2024). Sleeper Agents: Training deceptive LLMs that persist through safety training.
arXiv:2401.05566.
Lattner, C. (2017). Swift Concurrency Manifesto. GitHub Gist. Retrieved April 25, 2026, from
https://gist.github.com/lattner/31ed37682ef1576b16bca1432ea9f782
Jolicoeur-Martineau, A. (2025). Less is more: Recursive reasoning with tiny networks. arXiv:2510.04871.
Moura, J. (2024). CrewAI: Framework for orchestrating role-playing AI agents. https://crewai.com
Nakajima, Y. (2023). BabyAGI: An AI-powered task management system.
https://github.com/yoheinakajima/babyagi
Richards, T. (2023). AutoGPT: An autonomous GPT-4 experiment. https://github.com/SignificantGravitas/AutoGPT
Rissanen, J. (1978). Modeling by shortest data description. Automatica, 14(5), 465-471.
Underwood, R., Di, S., Calhoun, J. C., & Cappello, F. (2020). FRaZ: A generic high-fidelity fixed-ratio lossy
compression framework. IPDPS 2020. arXiv:2001.06139.

Quran passages cited: 1:1-7 (al-Fatiha), 2:2 (the Book without doubt), 2:10 (disease model), 2:30
(the khalifa), 2:42 (truth over falsehood), 2:67-74 (the Cow Episode), 2:204 (pleasing speech),
2:255 (the Throne Verse, knowledge encompassing), 2:286 (no soul beyond capacity), 5:8 (justice

despite hatred), 17:106 (gradual revelation), 55:7-9 (the Mizan), 55:31 (jinnkind), 72:1-2
(jinnkind).



Bismillah ir-Rahman ir-Rahim
