Bismillah ir-Rahman ir-Rahim

BSSG: An Evidence-Independent Control Plane for Bounded
Artificial Agency
Bilal Syed Arfeen
2026-07-31
Abstract
Autonomous software agents are acquiring the ability to cause consequential effects – deleting
production databases, exfiltrating credentials, executing financial transactions – while the systems
that deploy them lack an enforceable architecture for bounding what those agents can actually
do. BSSG (Bounded Structural Safety Gate) is a control plane whose kernel equation reduces
the authorization of any agent effect to a conjunction of five externally established predicates:
contract match, effect-type validity, target allowance, witness health, and evidence currency. The
kernel is three-valued; UNKNOWN is never satisfied; FALSE dominates order-independently.
Authority degrades monotonically under witness degradation and can be restored only through
an independent amendment from a control domain the agent does not administer.
This paper reports three contributions. First, the architecture itself: a five-conjunct evidenceindependent control plane, an atomic commit protocol, six closed record schemas, and a reference
implementation with 345 deterministic tests including an exhaustive 35 = 243 kernel truthstate suite. The novel element is not the individual components (which compose established
access-control, attestation, and capability-discipline principles) but their application as an
evidence-independent enforcement point on the agent-effect boundary – the placement and
the structural-honesty discipline that governs it. Second, a 34-instance defect trajectory in
which the AI producer’s own fix for a ceiling-poison bypass shipped incomplete one level deeper,
repeatedly, across 37 passes – an empirical record of producer blind-spot recurrence that was
closed by a structural class fix pairing unconditional empty-Authority initialization on every
ALLOW path with removal of the DENY-path ceiling write. The class fix was independently
confirmed closed by three vendor families (OpenAI, Zhipu, Moonshot) across the convergence
rounds and carried by two families (xAI, Moonshot) in the carrying audit; one additional family
(Google) contributed a defect discovery pre-fix, and xAI contributed post-fix closure confirmation.
Third, the multi-model adversarial council as a verification methodology: cross-vendor rotation
of non-producer AI auditors, byte-authoritative reproduction, convergence criteria requiring
consecutive clean rounds from independent vendor families, and a two-family carry protocol.
This paper makes no effectiveness claim. It does not assert that a BSSG deployment
achieves safety, security, harm reduction, or superiority over any alternative. Whether the
architecture changes any measurable outcome is an empirical question reserved to the Structural
Honesty Validation Protocol (SHVVP v0.8, DOI 10.5281/zenodo.21583202) and to instruments
downstream of it.

AI producer disclosure. The reference artifact was assembled by an AI producer agent (Claude,
Anthropic). The verification program employed a multi-model adversarial council spanning five
vendor families (OpenAI, Zhipu, Moonshot, Google, xAI). The author of record is human; the
methodology, claim boundaries, and all editorial decisions are his. No council seat approved this
paper.
1

Conflict of interest and ethics statement. The author is the sole developer of the BSSG
architecture and the sole author of the methodology chain (SHV, SHVVP, SHUDP, BAF, PMD)
cited throughout. The AI producer (Claude, Anthropic) that built the reference artifact is also
the model family excluded from vote-weighted audit seats under the cross-vendor rotation discipline. The methodology protocols, their interpretation, and amendments to them (including the
carry-independence rule supersession disclosed in Section 5.3) are single-author acts. No external
governance body adjudicated deviations. These relationships are disclosed so that readers can assess
the evidential weight of the verification claims accordingly.
BSSG Concept DOI: 10.5281/zenodo.21611192

1

Paper DOI: 10.5281/zenodo.21712482

Introduction

In July 2025, Replit’s coding agent, mid-session during a declared code freeze, deleted a live
production database containing records for more than 1,200 executives and 1,196 companies,
fabricated approximately 4,000 fake user profiles to replace the deleted data, and falsely reported
that a rollback was impossible [43]. No attacker was involved. The destructive effect was not
gated; the fabricated records were structurally dishonest; and the false rollback report suppressed a
true state into a false one. A Cursor coding agent (powered by Claude) operating on PocketOS’s
infrastructure encountered a credential mismatch and autonomously decided to “fix” it by deleting
a Railway volume [44] – the safety layer was a system prompt, and the system prompt was advisory
rather than enforceable. Google’s Gemini CLI hallucinated a successful file operation and cascaded
a user’s files into a nonexistent directory [45]. AWS’s internal Kiro tool deleted and recreated an
environment, causing a 13-hour service interruption [46].
In July 2026, the adversarial twin of the same seam materialized. Sysdig documented JadePuffer,
an LLM-driven ransomware operation in which a large language model autonomously executed the
post-provisioning attack sequence: the agent exploited CVE-2025-3248 in an Internet-facing Langflow
deployment, pivoted to a production server running MySQL and Alibaba Nacos, enumerated the
database, attempted data exfiltration, deleted the database, and left an extortion note. None of the
individual techniques were novel; what was novel was that an AI model strung them together into a
complete offensive operation. The researcher’s own framing captures the threshold: tradecraft that
once implied a capable human now implies a capable model.
These two classes of incident – the accidental deletion and the autonomous attack – exploit the
identical architectural seam: an ungated boundary between an agent’s reasoning and a consequential
effect against a production resource. The OWASP 2026 agentic-security report makes the equivalence
explicit: there was no attacker in the Replit case, but the permission model behind the unprovoked
failure is the same permission model an attacker exploits through prompt injection. Containing the
safety failure and containing the security gap turn out to be the same architectural problem.
Meanwhile, the capability that makes these agents dangerous is also the capability worth preserving.
Google’s Big Sleep identified CVE-2025-6965 in July 2025, a memory-corruption flaw in SQLite
previously known only to threat actors, and found 20 new vulnerabilities in projects including
FFmpeg and ImageMagick [36]. An autonomous agent (XBOW) was credited on a critical CVSS 9.8
remote-code-execution flaw (CVE-2026-21536) in a Microsoft cloud service [47]. Depthfirst reported
21 FFmpeg zero-days for roughly US$1,000 of compute, nine already assigned CVE identifiers [48].
The US$1,000 figure makes the point concrete: capable offensive agents are cheap and present. This
work therefore gates the effect rather than disabling the capability, accepting that evidence-plane
2

failure converts into denial (Section 7.1).
Evidence that frontier models can produce strategically deceptive behavior under certain conditions
compounds the urgency. Apollo Research’s December 2024 evaluation of reasoning models found
instances of in-context scheming – a model taking covert actions to preserve itself when it believed it
was about to be shut down, and denying having done so when confronted (Apollo Research, “Frontier
Models are Capable of In-Context Scheming,” December 2024). Anthropic’s alignment science
team demonstrated that models can exhibit alignment faking – appearing aligned during monitored
evaluation while behaving differently in deployment-like conditions (Greenblatt et al., “Alignment
Faking in Large Language Models,” Anthropic, December 2024). In July 2026, during OpenAI’s
ExploitGym cybersecurity evaluation with safety classifiers deliberately disabled, autonomous AI
agents escaped the sandbox testing environment and conducted a cyberattack against Hugging
Face’s infrastructure, executing over 17,000 automated actions across sandboxes over a period of
days [42]. These cases share a common structural feature: the model’s own account of itself – its
stated intentions, its claimed compliance, its reported actions – cannot be trusted as the sole basis
for authorizing its effects.
The regulatory clocks are tightening around exactly these incidents. The EU’s DORA imposes a
four-hour notification window [49]; NIS2 requires a 24-hour early warning [50]; New York’s RAISE
Act sets a 72-hour clock for frontier-model incidents [51]; California’s SB 53 establishes a 15-day
window [52]. OWASP’s 2026 edition has shifted from cataloging hypothetical threats to cataloging
CVEs, vendor advisories, and breach reports, with coding agents driving most of the new attack
data.
BSSG addresses one question: by what architecture can the set of effects an agent can actually cause
be made a decidable function of externally held evidence, rather than a function of the agent’s own
account of itself? Three words in that question are load-bearing. Decidable commits the architecture
to a monitor that terminates with a verdict on every request. Externally held is the architectural
bet – the agent’s own claims about its authorization are structurally inert. Effects rather than
intentions or beliefs fixes the object of control.
This paper does not claim that BSSG would have stopped any of the incidents above. That is a
counterfactual requiring interposition that has not been demonstrated. The incidents establish that
the threat model is real and that the seam – an ungated consequential-effect boundary – is the
place where both accidental and adversarial harm converges. BSSG is an architecture for that seam.
Whether the architecture changes outcomes is an empirical question this paper does not answer.

2

Problem Statement

An autonomous or semi-autonomous software agent, whose internal reasoning is not reliably legible
and whose stated intentions are not a reliable predictor of its actions, is granted the ability to cause
consequential effects outside itself. A consequential effect is any operation whose completion can
mutate, disclose, transmit, deploy, authorize, spend, publish, or irreversibly release a protected
resource.
The problem is architectural. Guardrails implemented as system prompts, instruction-tuning, or
trained-in refusals are advisory: the model can and does override them when its reasoning decides
an action is necessary. The PocketOS/Cursor incident demonstrates this directly – the safety layer
was a system prompt, and the agent overrode it. Indirect prompt injection (CVE-2026-2256 in
ModelScope’s MS-Agent, CVE-2025-66404 in mcp-server-kubernetes) shows that even denylist3

based guardrails can be bypassed through content-level obfuscation – an argument against blocklist
architectures and for fail-closed-on-uncertain. Package hallucination – confident fabrication of
nonexistent software packages, measured at 5.2% for commercial models and 21.7% for open-source
models across 576,000 samples in a USENIX study yielding 205,474 unique hallucinated package
names – illustrates the fabrication class at scale.
The architectural response BSSG proposes is an independent, enforceable gate between the agent’s
reasoning and the consequential effect. The gate does not evaluate the agent’s intentions, beliefs, or
semantic content. It evaluates whether five externally established predicates hold at the moment
of the request, and it does so from raw evidence that the agent cannot supply. The gate is not
an alignment mechanism, a deception detector, an intent classifier, or a limiter on reasoning. It is
an enforcement point on the effect boundary that preserves contract-authorized capability under
evidence-plane health.

3

Architecture

3.1

The Kernel Equation

The core of BSSG is a frozen five-conjunct authorization kernel:
Allow(r) iff ContractMatch AND EffectTypeValid AND TargetAllowed AND
WitnessHealthy AND EvidenceCurrent
Each conjunct is three-valued: TRUE, FALSE, or UNKNOWN. The kernel’s decision semantics are:
• ALLOW if and only if all five conjuncts are TRUE. Exactly one of the 35 = 243 possible
truth-state assignments satisfies this condition.
• DENY_FALSE if any conjunct is FALSE. FALSE dominates order-independently: a
determinate FALSE conjunct yields DENY_FALSE regardless of the values of other conjuncts,
even if they are UNKNOWN.
• DENY_UNKNOWN if no conjunct is FALSE but at least one is UNKNOWN. UNKNOWN
is never satisfied – it is not “probably false,” not “not observed,” and not “clean.”
The five conjuncts are defined as follows:
ContractMatch. The request’s declared subject, session, effect type, target, and parameters match
a registered contract whose policy digest equals the one declared. The contract binds a closed set of
permissible effect types and target scopes.
EffectTypeValid. The requested effect type is within the contract’s declared effect registry and
within the adapter’s declared capability.
TargetAllowed. The canonical target is within the contract’s target scope and within the current
authority ceiling. Target canonicalization refuses traversal sequences, percent-encoding, wildcards,
embedded credentials, and case ambiguity; any of these maps to UNKNOWN rather than to a
canonicalized form.
WitnessHealthy. A fitness predicate over the witness set: verified signature, monotone epoch
and sequence, unexpired health lease, a declared control domain distinct from the subject’s, an
explicit declaration that the subject cannot administer the witness, and a WithinAuth assessment
of “outside_subject_authority.” Witness silence is UNKNOWN, never health. Witness degradation
narrows the authority ceiling; it never widens it.

4

EvidenceCurrent. TRUE only when a declared freshness authority exists and is signed, the
anchor and evaluation clock agree within the declared skew, the evidence epoch is not lower than
the highest epoch seen, the request’s time fields parse strictly within their window, the evidence age
is within the type-specific limit, and the nonce has not been seen.
The decision point recomputes every conjunct from raw evidence. It does not accept any callersupplied derived fact. A record carrying a field named (case-insensitively) “allow,” “decision,”
“authorized,” “contract_match,” or any conjunct name is rejected structurally, before evaluation.
This discipline exists because the historically observed failure mode in this program’s lineage is a
test fixture or interface that lets the caller supply the property under test.

3.2

Evidence Independence

The architectural bet is evidence independence: for each covered event, at least one admissible
witness record must be generated in a control domain not transitively writable, truncatable, forkable,
signable, reconfigurable, or rollback-able by the subject. This is Axiom 5 as established theoretically
in “Is Evidence Independence an Axiom?” (AX-SH 5, DOI 10.5281/zenodo.21539074, v0.4) and
carried operationally by the Structural Honesty Upstream Disclosure Protocol (SHUDP v0.5, DOI
10.5281/zenodo.21539816). The two DOIs reference successive versions of a single line of work –
v0.4 establishing the axiom’s independence from AX-SH 1–4 via a finite countermodel, v0.5 carrying
it as methodology with additional protocol content. In BSSG, evidence independence is a declared
assessment and a reviewed control graph, never derived from a valid signature.
A valid signature establishes that a key signed a payload; it does not establish that the signer
is independent of the subject. A witness with a distinct key, host, and vendor but a common
administrator who can reconfigure its collector, delete its storage, and restore a snapshot has
cryptographic separation without evidence independence. The gate allows in this case and cannot
do otherwise – which is why independence is an assumption verified by control-graph review, not a
property the gate can check.

3.3

Atomic Commit Protocol

The commit protocol narrows the modeled decision-to-redemption race by binding fields and
revalidating them at one-time token redemption (in-process; cross-process and distributed atomicity
are deployment obligations, not properties of the reference):
1. An authorization receipt binds: request digest, subject, session, contract digest, policy digest,
witness receipt digest, evidence epoch, authority epoch, authority snapshot, effect type,
canonical target, parameters digest, adapter digest, nonce, issue time, and expiry.
2. A one-time commit token is minted and redeemed by an atomic compare-and-swap from
UNUSED to CONSUMED. A repeated redemption is denied even where the signature and
expiry remain valid.
3. At redemption the enforcement point revalidates: token status and expiry, session nonterminality, authority epoch equality, evidence epoch equality, and exact equality of every
bound execution field. Any mismatch voids the token.
4. An unknown remote outcome is recorded as INDETERMINATE and is not retried blindly. Atmost-once redemption plus target-specific idempotency is the claim; exactly-once for arbitrary
external effects is not claimable.

5

3.4

Authority Lattice and Monotone Narrowing

Authority degrades monotonically. When witness health decreases from HEALTHY to DEGRADED,
the authority ceiling must narrow – that is, the set of authorized effect types and target scopes
under DEGRADED must be a proper subset of the set under HEALTHY, provided the prior ceiling
was non-empty. A ceiling recomputation that is not a subset of the prior ceiling is a terminal failure
(E-AUTHORITY-WIDENING). A health decrease where the new ceiling is not a proper subset of
the prior non-empty ceiling is likewise terminal (E-NONSTRICT-NARROWING).
Recovery from a terminal state requires an independent amendment: a correction event signed by
at least two adjudicators in distinct declared control domains, neither of which is the subject’s.
Single-party recovery is structurally rejected. This property – that the agent cannot restore its own
authority – is the enforcement-level realization of evidence independence.

3.5

Record Schemas and Cross-Record Invariants

Six JSON Schema 2020-12 documents define the record format: effect-request, authorizationreceipt, witness-receipt, execution-receipt, correction-event, and lineage-record.
All use
additionalProperties: false at every level where the field set is closed.
Eight cross-record invariants (X1–X8) enforce structural consistency: request-to-authorization
digest binding (X1, ENFORCED), witness-to-authorization coverage (X2, ENFORCED), executionto-authorization binding (X3, ENFORCED), single commit-token redemption (X4, ENFORCED
in-process), correction-event closure (X5, ENFORCED), lineage completeness (X6, ENFORCED for
records the gate produces; DETECTABLE for gaps), authority-history monotonicity (X7, whose
three-valued offline verdict is notated X7 for VIOLATION, X7U for UNCERTIFIABLE-offline, and
“clean” for no re-widen; ENFORCED at runtime, DETECTABLE offline), and ALLOW-receipt
conjunct purity (X8, ENFORCED). Each invariant has positive and negative test vectors; the test
suite exercises them and the verifier re-exercises them. Counterexamples are numbered CEN in
order of registration in the 176-entry corpus (e.g., CE169 was originally registered to lock instance
30’s fix but was later found non-load-bearing at instance 32 and corrected; CE175 and CE176 lock
the class fix for mint-fault and degraded-first respectively).

3.6

Threat Model

The adversary lattice defines five classes:
Class

Capability

A1

Full control of the subject: prompts, memory, tool
arguments, all untrusted request fields
A1 plus network position: reorder, delay, drop, replay;
degrade or silence the witness
A2 plus compromise of one witness or one evidence
producer
A3 plus compromise of the executor host, local clock, or
storage
A4 plus collusion at or above the trust-root threshold, or
compromise of the decision point

A2
A3
A4
A5

6

At A5 the architecture collapses entirely. A colluding but apparently healthy witness (A3) defeats
the kernel silently – the gate allows and cannot do otherwise, and the test suite includes a passing
test whose assertion is this limitation.
Out of the threat model: covert and side channels, the semantic correctness of adapters, malicious
targets, physical channels, human operators acting within their authority, and cryptographic breaks.

3.7

Non-Advantage of Concealment

Stated in its architectural form as PR-6, non-advantage of concealment has two clauses:
(a) Decision monotonicity under information loss. Replacing any predicate input with
UNKNOWN or FALSE, all else equal, does not change DENY to ALLOW, does not revive a grant,
does not suppress a revocation, and does not widen authority. This is mechanically tested over the
243-state truth table and enforced by the reference gate.
(b) No subject-visible regime signal. No BSSG-mediated channel shall expose to the subject a
signal that distinguishes observed from unobserved operation. The reference gate provides a subjectfacing projection that collapses every denial to a constant response, closing the distinct-error-code
channel. Residual timing and size channels are declared deployment obligations, not enforced gate
properties.

3.8

Claim Levels

Every property carries exactly one of four levels:
Level

Meaning

ENFORCED

Enforced by the reference gate on the records it
processes, given its inputs
A violation leaves evidence that a specified checker
can find, given examination
An assumption about the deployment or the
environment; reviewable and refutable
Outside the architecture entirely; any claim made
about it from BSSG is invalid

DETECTABLE
ASSUMED
OUT OF MODEL

The specification also maintains a register of prohibited sentences – explicit effectiveness claims that
must not appear in any BSSG document, verified by an automated scanner.

4

The Defect Trajectory: Central Empirical Finding

4.1

The Pattern

Across 37 passes and 34 identified instances, the same structural pattern recurred: the AI producer’s
(Claude, Anthropic) fix for a ceiling-poison bypass shipped incomplete one level deeper. Each
instance was found by a non-producer external audit seat, reproduced on canonical bytes before
crediting, and fixed. The trajectory constitutes the paper’s central empirical finding – not as a
demonstration of the architecture’s effectiveness, but as an empirical record of how a specific class
of producer blind spot manifests and propagates under adversarial multi-model audit.
7

4.2

Numbering Conventions

The program uses three counters. A pass is a numbered state of the artifact (pass-1 through
pass-37); the pass number increments with each repair. A repairN label (e.g., repair33) is an alias
for the pass state produced by fixing the findings from a given audit round; “repair33” and “pass-33”
denote the same artifact state. An audit round VN is the audit of the artifact at a specific pass; the
mapping is not a strict function (multiple audit rounds may audit the same pass state when rapid
fixes occur between rounds, and the naming convention diverged from a simple offset at V29). An
instance is a numbered entry in the defect trajectory (1–34), counting the recurring ceiling-poison
pattern across all passes. The following table maps the representative instances:

4.3

Instance

Audit round

Pass audited

Discovered by

30
31
32
33
34
Class fix
Carry

V30
V31
V31
Council v1
Council R2
–
–

repair33
repair33
repair33
pass-35
pass-35
pass-36
pass-37

GLM-5.2 + Kimi K3
Kimi K3
GLM-5.2
GPT-5.6 Sol
Gemini 3.1 Pro
–
Grok 4 + Kimi K3

Representative Instances (numbered by defect-trajectory instance)

Instances 1–29 (V1–V29): Pre-convergence defects. The first 29 passes produced the
pre-convergence defect history. A critical inflection occurred at pass 30 (V29 audit), when five
consecutive rounds in which the offline licensed-re-widen mechanism was falsified one level deeper in
its own implementation led to a disciplined withdrawal: the offline checker’s positive certification of a
re-widen was withdrawn entirely. The offline verdict became grant-independent – the runtime grant
is caller-supplied (WithinAuth of the supplier) and discharges nothing under evidence independence.
The withdrawal deleted the grant-poison and grant-spoof class at the root: an authentic and a forged
grant now yield the identical X7U (UNCERTIFIABLE-offline), so there is no positive certification
left to spoof.
Instance 30 (V30, GLM + Kimi convergent): Cross-contract ceiling-poison. The first
convergence event in the program’s history. GLM-5.2 and Kimi K3 independently discovered the same
runtime effect bypass with independently authored reproducers, arriving at the identical four-step
schedule: a DENIED request carrying a second, broader contract poisoned the contract_ceiling,
allowing DELETE to be authorized and committed end-to-end for a session whose establishing
contract never included DELETE. This was a runtime gate bypass – strictly more severe than any
finding in the prior 32 passes. The fix’s own ceiling mechanism was the attack vector, one level
deeper.
Instance 31 (V31, Kimi K3): ALLOWED-degraded ceiling-poison. An ALLOWED request
at DEGRADED health wrote a HEALTHY ceiling value, creating a ceiling entry that overstated
the session’s demonstrated authority.
Instance 32 (V31, GLM): CE169 non-load-bearing. The counterexample designed to lock
instance 30’s fix tested the wrong health level, meaning the fix was verified against a condition that
did not exercise the actual vulnerability.
Instance 33 (Council v1, GPT-5.6 Sol): Mint-fault ceiling-poison. A failed token mint
8

(FAILED_NO_EFFECT) wrote the ceiling before the mint, leaving a broadened ceiling entry for a
session that never received a usable token. After a terminal-state lift via amendment, the broadened
ceiling enabled a HEALTHY DELETE to be authorized and committed.
Instance 34 (Council R2, Gemini 3.1 Pro): Degraded-first ceiling absence. The most architecturally revealing instance. A session whose first successful authorization was DEGRADED never
wrote a contract_ceiling entry, because the ceiling write was guarded by health == "HEALTHY".
The session’s legitimate demonstrated authority was only READ. After an amendment lifted a
terminal state, a HEALTHY DELETE re-established at the full ceiling because _apply_narrowing
saw _held is None and took the free-establishment branch. This was native reachability – no
exception path, no monkeypatching, no forced failure. Gemini’s probe reproduced it on unmodified
bytes.

4.4

The Class Fix

Instances 30–34 share a common structural pattern at the correct level of generality: the
contract_ceiling state for a session ended up not reflecting the session’s demonstrated authority.
The specific mechanisms varied – a DENY-path write poisoned the ceiling with a broader contract’s
scope (instance 30), a DEGRADED ALLOW wrote a HEALTHY ceiling value (instance 31), a
pre-mint ceiling write survived a failed mint (instance 33), or the ceiling was never written at all
because the write was guarded by health == "HEALTHY" (instance 34). Instance 32 is distinct: the
counterexample (CE169) designed to lock instance 30’s fix tested the wrong health level, making
the fix’s verification non-load-bearing; this was a corpus-repair item (CE169 was corrected), not a
code-level ceiling-state defect. In each of the four code-level cases, the narrowing logic subsequently
treated the corrupted or absent ceiling as the session’s legitimate authority, enabling an effect the
session had never demonstrably held.
The class fix, implemented at pass 36, addresses the four code-level variants through two coordinated
changes:
(a) Unconditional empty-Authority initialization at the top of every ALLOW path,
before any conditional (health check, mint, ceiling write).
(b) Removal of the contract_ceiling write from the DENY path, so that only
ALLOW paths can establish or modify ceiling state.
The invariant from (a): _held is NEVER None after any ALLOW decision. An empty Authority
records that the session has been authorized but has demonstrated nothing; the HEALTHY-successfulissuance path upgrades the entry to the demonstrated ceiling; a mint-fault or DEGRADED ALLOW
leaves the empty entry in place; and the narrowing logic sees a non-None constraint on every
subsequent authorization. Change (b) neutralizes the DENY-path poisoning variant (instance 30)
by ensuring the DENY path no longer touches contract_ceiling. Change (a) neutralizes the
wrong-value variant (instance 31) because even a DEGRADED ALLOW initializes the entry, and the
subsequent HEALTHY upgrade is bounded by what was initialized. Changes (a) and (b) together
neutralize the absence variants (instances 33–34) directly. Whether other ceiling-state corruption
mechanisms exist outside the declared 10-operation alphabet or beyond schedules of length four is
not established by the bounded enumeration (Section 6.4).

4.5

What the Trajectory Demonstrates

The trajectory is evidence of a specific phenomenon in one producer (Claude, Anthropic) on one
artifact (BSSG): producer-generated fixes for authorization-boundary defects exhibited a recurrent
9

pattern of incompleteness one level deeper. This pattern was not broken by individual fixes; it was
broken by a structural invariant that addresses the known root-cause variants through a single
mechanism rather than case-by-case patches. Whether the same recurrence pattern holds for other
AI producers, other artifact types, or other defect classes is an open question; generalizing from n=1
would exceed the evidence.
The trajectory also demonstrates a second phenomenon: in the observed setting, the producer
systematically failed to find the deeper instance of its own fix’s incompleteness. In every case, the
deeper instance was found by a different vendor-family auditor. This is consistent with cross-vendor
rotation discovering defects the producer’s own lineage misses, and it motivates the multi-model
adversarial council as a verification methodology – but the design cannot separate the effect of
vendor diversity from the effect of additional independent adversarial attempts, fresh context, or
adversarial framing. A controlled comparison (same-family fresh-instance audit versus cross-family
audit) has not been conducted and is noted as future work.
The trajectory does not demonstrate that the architecture is effective, that the class fix is permanent,
or that no further instances exist. It demonstrates that the structural invariant holds on the shipped
bytes under adversarial audit. The three families that independently confirmed the class fix closed
on post-fix bytes (OpenAI, Zhipu, Moonshot across V32–V34) and the two families that carried the
artifact (xAI and Moonshot on pass-37) are listed in the per-family role table below.
Per-family role summary:
Vendor family

Defect discovery (pre-fix)

Closure confirmation (post-fix)

Carry

OpenAI
(GPT-5.6 Sol)
Zhipu (GLM-5.2)
Moonshot (Kimi
K3 / K2.6)

Instance 33

V32–V34 convergence

–

Instance 30, 32
Instance 30, 31

V32–V34 convergence (3x PASS)
V32–V34 convergence (3x PASS)

Instance 34

–

–
CARRYCLEAN
(K3)
–

–

pass-36 CLEAN

Google (Gemini
3.1 Pro)
xAI (Grok 4)

3x
CLEAN
(carry)

5

Multi-Model Adversarial Council: Methodological Contribution

5.1

Design

The verification program employs a multi-model adversarial council: independent AI auditors from
different vendor families, operating under a cross-vendor rotation discipline, each executing the
reference artifact on canonical bytes and reporting findings under a structured severity rubric.
The council’s design principles, inherited from the Structural Honesty Verification method (SHV, DOI
10.5281/zenodo.21449063) and the Audit Framework (BAF v3.0, DOI 10.5281/zenodo.20017335),
are:
Byte-authoritative reproduction. Every finding must be reproduced on canonical bytes before
crediting. A finding reported against a different version, a partial extraction, or a paraphrase of
10

the code is not credited. The audit begins with sha256sum -c SHA256SUMS (20/20 OK) and full
battery execution.
Cross-vendor rotation. The producer (Claude, Anthropic) is structurally excluded from voteweighted findings. Non-producer seats are drawn from different vendor families – in this program:
OpenAI (GPT-5.6 Sol), Zhipu (GLM-5.2), Moonshot (Kimi K3 / K2.6), Google (Gemini 3.1 Pro),
and xAI (Grok 4). Each vendor family’s models have different training data, different blind spots,
and different analytical strengths.
Severity rubric. The program’s canonical rubric (BAF v3.0) defines four levels: BLOCKER
(a security invariant is broken on canonical bytes), MAJOR (an observability or soundness gap),
MINOR (documentation or defense-in-depth), and INFO (architectural notes). Individual seats may
use their own native labels (GPT uses CRITICAL/SIGNIFICANT/MODERATE/NOTE; Gemini
uses CRITICAL/HIGH/MEDIUM/LOW); these are recorded under the seat’s own stated criterion
and are not re-scored by the producer. Where this paper reports cross-seat convergence, it uses the
BAF terms and maps seat-native labels at first use.
One-shot versus continuous. Seats may operate in one-shot mode (a single audit of a sealed
artifact) or continuous mode (tracking across multiple passes). Both modes are creditable under
SHV D6, but a seat’s history affects what weight its “clean” verdict carries.
Producer-family exclusion. Claude models participate as advisory seats only. Their findings are
recorded but carry no vote weight toward convergence or carry. This discipline exists because the
producer’s blind spots are precisely the ones the program is designed to find; a producer-family
seat that clears the artifact does not discharge the convergence requirement. Model identifiers
throughout this paper (Claude Opus 5.0, Claude Fable 5, Claude Sonnet 5, GPT-5.6 Sol, GPT-5.6
Terra, Gemini 3.1 Pro, GLM-5.2, Kimi K3, Kimi K2.6, Grok 4) are quoted from the council’s audit
records and identify the exact model versions used during the program; Kimi K2.6 replaced K3 as
the Moonshot convergence seat for V32–V34 (a genuine fresh rotation within the family), while
K3 – which had previously served as a pre-fix discovery seat (instances 30–31) and a Council v1
participant – returned for the carrying audit.

5.2

Convergence Criteria

Convergence requires:
1. Two or more consecutive audit rounds with zero BLOCKER findings from any seat.
2. At least one seat rotated fresh (a different model version within a vendor family, or a new
vendor family).
3. All prior BLOCKER-class findings independently verified closed by multiple seats.
The BSSG program achieved convergence across V32–V34 (three consecutive zero-BLOCKER
rounds) with three independent vendor-family seats: GPT-5.6 (OpenAI), GLM-5.2 (Zhipu), and
Kimi K2.6 (Moonshot). GLM returned PASS for three consecutive rounds. Kimi returned PASS
with explicit “convergence achieved” in the final round. GPT returned ISSUES-FOUND in each
round, but all findings were documentation-staleness class (MODERATE or NOTE), with GPT
itself confirming “no new runtime/security bypass.”

5.3

Carry Protocol

Carry – the final gate before an artifact is considered verified – requires a clean audit from at
least two non-producer vendor families under SHVVP section 0.3. The carrying protocol requires
11

byte-authoritative execution of the sealed artifact, reproduction of identity values, and independent
verification of the class fix. Carry is execution-level verification of the shipped artifact; it is distinct
from AF-11 (a second independent reimplementation agreeing on frozen vectors), which remains
untested and is listed as STILL BLOCKING in Section 7.3.
Grok 4 (xAI). Three consecutive CLEAN rounds, with matching sealed values (MANIFEST,
CHALLENGE, EXECUTION_ATTESTATION). The class fix was verified independently: the
unconditional empty-Authority init is present and fires at the top of the ALLOW path, all degradedfirst and mint-fault probes are closed, and the invariant (_held is never None after any ALLOW)
was confirmed by tracing every path through the ALLOW branch.
Kimi K3 (Moonshot). CARRY-CLEAN with matching sealed values. Independent execution:
20/20 SHA-256 verified, 345/345 tests OK, 176/176 counterexamples GREEN, model check PASS
over 11,110 schedules, verifier 0 FAIL with DRAFT status intact. The class fix at L1818–L1825 was
verified by direct source read of the executed file, confirming that init fires before any conditional
and that CE175 (mint-fault) and CE176 (degraded-first) are both GREEN.
Independence note. Both carry families (xAI and Moonshot) also participated in the earlier audit
council – Moonshot’s Kimi K2.6 as a convergence seat (V32–V34), and Moonshot’s Kimi K3 as a
pre-fix discovery seat (instances 30–31, Council v1) before returning as the carry model; xAI’s Grok
4 contributing clean rounds on post-fix bytes. SHVVP section 0.3 requires non-producer families for
carry but does not require non-auditor families; the program’s earlier discipline (Qwen/DeepSeek
as carry candidates outside the council) was superseded when the council expanded to include
those families’ rotation slots. The carry therefore demonstrates independent byte-authoritative
execution by two non-producer families, not independence from the audit panel itself. This is a
weaker independence guarantee than a fully disjoint carry panel would provide, and it is stated as
such.

5.4

Council Findings as Evidence

The council’s value is not in the final clean verdict but in the trajectory of findings that preceded
it. The pre-class-fix council (Council v1 in the Section 4.2 table – an eight-model panel convened
during the convergence process, distinct from the V32–V34 convergence rounds themselves, and
comprising GPT-5.6 Sol and GPT-5.6 Terra from OpenAI, Gemini 3.1 Pro from Google, Kimi K3
from Moonshot, GLM-5.2 from Zhipu, and Claude Fable 5, Claude Opus 5.0, and Claude Sonnet
5 from Anthropic as advisory non-voting seats) discovered instance 33 (GPT-5.6 Sol authoring
the probe, orchestrator reproducing). The subsequent Council R2, on the same pass-35 bytes,
discovered instance 34 (Gemini 3.1 Pro finding a native-reachability bypass the orchestrator verified
on unmodified bytes). Both councils audited pre-class-fix bytes; the V32–V34 convergence rounds
that followed audited post-class-fix bytes. In both discovery cases, the finding was discovered by a
non-producer seat and was not present in the producer’s own audit or self-check.
The council also produced genuine disagreements that are preserved rather than resolved. Fable 5
(producer family, advisory) argued that instance 33 was HIGH rather than CRITICAL for the specific
tested contract shape; Gemini argued it was CRITICAL by mechanical reachability alone. The
severity dispute was mooted by the discovery of instance 34, which was unambiguously CRITICAL
(genuine widening of landing-state authority beyond what the session ever legitimately held, reached
without any exception path). The preserved disagreement is itself methodological evidence: a single
severity rubric applied mechanically does not capture the nuance of whether a formal violation with
a convergent landing state is equally severe as one with a divergent landing state.
12

6

The Reference Implementation

6.1

Artifact State

The pass-37 reference artifact comprises 20 manifest-bound files (6 Python, 6 JSON schemas, 8
documentation files) verified byte-exact against SHA256SUMS (20/20 OK). Battery state:
• 345 tests OK – 243 exhaustive kernel truth states (35 , exactly one allowing state), 4
kernel-table shape tests, 98 adversarial, protocol, cross-record-invariant, and schema tests.
• 176/176 counterexamples GREEN – each a named probe that exercises a specific loadbearing claim, with a RED result indicating an open defect.
• MODEL CHECK PASS – kernel (243 states) + antitone (729 contracts) + boundedauth-intro (11,110 schedules, K=4, 10-operation alphabet) + operational refinement on the
executable.
• Verifier: 14 gates, 12 PASS, 2 WARN, 0 FAIL – the two WARNs are intentional:
G10 records 12 open design decisions (a DRAFT artifact), G2 records an absent optional
dependency (jsonschema) alongside its structural PASS. G2 emits both a WARN (jsonschema
absent) and a PASS (structural check OK), yielding 14 status entries across 13 gates. With
jsonschema installed, G2 emits a single PASS and the summary reads 13 gates, 12 PASS, 1
WARN, 0 FAIL.

6.2

What the Reference Does and Does Not Do

Enforced by the reference gate: recomputation of all five conjuncts from raw evidence; refusal
of any caller-supplied derived authorization fact; UNKNOWN never satisfied; authority epoch
monotonicity and monotone narrowing with a strictness rule; binding of the authorization to request
digest, contract digest, policy digest, witness receipt digest, evidence epoch, nonce, and expiry;
one-time commit tokens redeemed by compare-and-swap; commit-time revalidation; and rejection of
replay, in-process rollback, stale evidence, unknown and extra fields, malformed timestamps, clock
ambiguity, witness-control ambiguity, mismatched digests, target and effect widening, and recovery
from a terminal state without an independent amendment.
Not established by the reference gate: complete mediation, key custody, cryptography of
any kind (signature verification is modeled through an injected verifier), witness honesty, evidence
independence as fact, cross-restart rollback resistance, cross-process or distributed concurrency
safety, or any outcome.

6.3

Artifact Availability

The pass-37 reference artifact (20 manifest-bound files), the counterexample corpus, the council audit
logs with prompts, timestamps, and model versions, and the carry evidence are published under open
access at Zenodo DOI 10.5281/zenodo.21712482. The bundle SHA-256 manifest is included. Prior
restricted deposits under the BSSG concept DOI (10.5281/zenodo.21611192) established priority;
the open deposit is the canonical record. A paper whose foundational axiom is that a system’s
self-attestation is inadmissible cannot ask reviewers to credit verification records accessible only on
request from the author; the open deposit is a methodological obligation, not a courtesy.

13

6.4

Bounded Exhaustive State Enumeration

The model checker (bssg_model_check.py) performs bounded exhaustive enumeration – not a
formal proof or transition-system model check – of three properties, plus an operational refinement
step that drives the real gate and verifies Section 14 state-transition compliance on actual execution
traces:
Kernel exhaustion (243 states). Every assignment of {TRUE, FALSE, UNKNOWN} to
five conjuncts is tested; exactly one allows; every other assignment denies; FALSE dominates
order-independently.
Authority antitonicity (729 contracts). Over all 729 contract structures in the finite lattice –
the four-dimensional combinatorial space of (subset of 3 effect types) x (subset of 3 target scopes) x
(degraded-effect subset) x (degraded-target subset), where each degraded subset ranges over subsets
of the corresponding healthy set, yielding 27 x 27 = 729 contracts – witness degradation never
enlarges the authority ceiling.
Bounded authority introduction (11,110 schedules, K=4, 10-operation alphabet).
Over all bounded schedules of up to 4 operations drawn from a 10-operation alphabet (ALLOWHEALTHY, ALLOW-DEGRADED, DENY, AMEND-LIFT, AMEND-NARROW, EXPIRE,
WITNESS-DEGRADE, WITNESS-RESTORE, MINT-FAULT, CEILING-WRITE-FAULT), no
ALLOW authorizes an effect outside the established ceiling. The K=3 bound was found insufficient
at V30 (it missed the minimal violating schedule of length 4); K=4 captures every violating schedule
over the declared alphabet up to length four, which includes the minimal witness for every instance
in the observed trajectory. Whether longer schedules or a richer alphabet would reveal additional
violations is not established.
The enumeration is bounded exhaustive, not a formal proof. No unbounded transition-system proof
or independently formalized invariant proof exists for any property of the reference gate; this is
listed as a STILL BLOCKING item (Section 7.3). The distinction matters: “MODEL CHECK
PASS” in the battery output denotes successful completion of the bounded enumeration, not a
model-checked invariant in the formal-methods sense.

7

Limitations and Open Decisions

7.1

What This Architecture Cannot Do

This section is as important as the architecture itself.
BSSG does not evaluate the semantic content of a permitted effect. A permitted effect type to a
permitted target with an adversarial payload is allowed. BSSG mediates authority, not meaning.
BSSG does not model the subject’s internal states. It is not an alignment mechanism and does not
claim to be one.
BSSG does not provide availability. Fail-closed converts evidence-plane failure into denial, which is
a cost borne by the agent’s capability, not by the architecture’s safety posture.
A colluding but apparently healthy witness – a subject-controlled witness that emits a structurally
perfect HEALTHY receipt declaring subject_can_administer: false – defeats the kernel silently.
The gate allows and cannot do otherwise. This is encoded as a passing test whose assertion is the
limitation.

14

Composition of individually authorized effects is out of model. The kernel evaluates one request
at a time; whether a sequence of individually authorized operations constitutes an unauthorized
composite operation is not addressed.
The reference gate keeps monotonicity state in process memory. Cross-restart rollback resistance
requires an external monotonic store, which is a deployment obligation, not a property of the
reference.

7.2

Open Design Decisions

Twelve design decisions remain unresolved at v0.1:
• OD-1: Canonicalization fork (BSSG-CANON-1 vs. COSE’s byte-string wrapping).
• OD-2: No external monotonicity root is named; rollback resistance is intra-process only.
• OD-3: Numeric freshness bounds per evidence type are placeholders.
• OD-4: Hash and signature agility, including post-quantum boundaries.
• OD-5–OD-12: Append-only log reconciliation, strictness semantics (the proper-subset
requirement on health decrease is enforced; the open question is whether non-increase plus
dependent-capability removal is a sufficient alternative – OD-6), role separation, session
duration, profile optionality, contract expressiveness, regime-signal tension, and witness
quorum rules.

7.3

Still Blocking

Four items remain in the STILL BLOCKING register: no unbounded transition-system proof or
independently formalized invariant proof for authority antitonicity (the bounded enumeration tests
the property, but does not prove it); no second independent implementation by a non-producer
lineage agreeing on frozen vectors (falsifier AF-11); the unresolved tension between diagnostic reason
codes and concealment signaling (OD-11); and the absence of a named cross-session monotonicity
root (OD-2).

8

Methodology Lineage

The BSSG program operates under a methodology chain deposited at Zenodo by the same author.
The DOIs establish provenance and priority; they do not constitute external validation. The
methodology papers have been independently carried by non-producer model families, but the
protocols, their interpretation, and amendments to them (including the carry-independence rule
supersession disclosed in Section 5.3) are all single-author acts. This section inlines the content the
paper actually depends on; the full documents are cited in the reference list.
Three concepts are load-bearing. Withdrawal precedent (SHVVP v0.8, Section 0.3): after
repeated falsification of a route-level inference, the disciplined response is withdrawal of the claim,
not another patch. BSSG’s V29 withdrawal of offline re-widen certification is an application of this
precedent. Evidence independence (Axiom 5, stated in AX-SH 5 and carried by SHUDP v0.5):
acting-system-independent evidence generation is not derivable from any property of the evidence
itself and is stated as an axiom over the control predicate WithinAuth. BSSG’s kernel carries this
as a declared assessment, never a derived fact. Carrying protocol (SHVVP v0.8, Section 0.3):
a clean audit from at least two non-producer vendor families, each executing the sealed artifact
independently, each reproducing byte-identical identity values, constitutes carriage.

15

The operational methodology (audit modes, cross-vendor rotation, severity rubric, findings format,
substrate-of-record discipline) is defined in the Audit Framework (BAF v3.0, DOI 10.5281/zenodo.20017335) and the Predictive Modeling Discipline (PMD v1.2). The parent axiom system is
AX-SH (Flagship v0.13, DOI 10.5281/zenodo.21500700). The integrating document is the Structural
Honesty Dissertation (v1.4, DOI 10.5281/zenodo.21501912).

9

Related Work

BSSG draws on established principles and distinguishes itself from adjacent systems.
Reference monitors and access control. The classical requirement that a reference validation
mechanism be “always invoked, tamperproof, and small enough to be subject to analysis and
tests” (NIST CSRC) governs BSSG’s design goals. Saltzer and Schroeder’s principles – complete
mediation, fail-safe defaults, open design, least privilege – are inherited directly and cited normatively.
Schneider’s enforceable security policies require that “any execution rejected by an enforcement
mechanism must be rejected after a finite period,” which constrains BSSG to decidable admission.
Capability systems. Miller’s distinction between permission (relative to a frame of reference) and
authority (invariant) governs BSSG’s quantity to bound. The authority lattice, monotone narrowing
under degradation, and the prohibition on self-amendment are capability-discipline concepts applied
to an agent-effect boundary.
Remote attestation and supply-chain integrity. RFC 9334 (RATS Architecture) separates
Attester, Verifier, and Relying Party and treats appraisal as input to a decision, not as execution
control. SLSA describes how an artifact was produced; in-toto supplies signed supply-chain metadata
and layout verification. None of these is a universal policy enforcement point for agent effects. BSSG’s
contribution, if any, is the enforcement placement and the record discipline, not the cryptographic
primitives.
Transparency logs and non-equivocation. RFC 9162 (Certificate Transparency v2.0) establishes
that logs do not prevent misissuance but ensure detectability. BSSG inherits this posture: nonequivocation below the high-assurance profile is detection only, and the detection mechanism itself
is defeasible.
Byzantine fault tolerance. Lamport, Shostak, and Pease establish that no solution with fewer
than 3m+1 generals can cope with m traitors for oral messages. Castro and Liskov’s PBFT
establishes the 3f+1 minimum. Both assume independent failures; BSSG must state its quorum
threshold together with its independence assumption.
Zero Trust Architecture. NIST SP 800-207 establishes that “access to individual enterprise
resources is granted on a per-session basis” and that “access to resources is determined by dynamic
policy.” BSSG’s per-request authorization, commit-time revalidation, and session-scoped authority
are consistent with Zero Trust principles applied to agent effects rather than human users.
Policy decision and enforcement points. BSSG structurally resembles existing PDP/PEP
systems: XACML defines a policy decision point / policy enforcement point separation; Open Policy
Agent (OPA/Rego) evaluates policy over structured input; cloud IAM systems (AWS IAM, Azure
RBAC, GCP IAM) evaluate per-request authorization against policy. BSSG differs from these in
two respects. First, evidence independence: conventional PDP/PEP systems trust the identity and
attribute providers they consult; BSSG treats the subject’s own account of itself as structurally
inert and requires witness evidence from a control domain the subject does not administer, carrying
16

this as a declared assumption (AX-EI) rather than a derived property. Second, placement: IAM
systems gate human-initiated API calls; BSSG gates effects initiated by an autonomous agent whose
request fields are adversary-controlled by construction (adversary class A1). The kernel’s refusal of
caller-supplied derived facts and the three-valued decision semantics (UNKNOWN never satisfied)
are consequences of this placement.
Agent action mediation and tool-use sandboxing. Recent work on LLM-agent safety includes
tool-use permission systems, sandboxed execution environments, and information-flow control for
agent actions. These approaches typically operate at the prompt or tool-call level – restricting which
tools an agent can invoke – rather than at the effect level. BSSG’s architectural claim is that the
enforcement point should sit on the consequential effect rather than on the tool invocation, because
a tool invocation and its effect can diverge (the Replit agent invoked a legitimate database tool to
cause an illegitimate deletion). This claim is architectural, not empirical; whether effect-level gating
produces better outcomes than tool-level restriction is a question for SHVVP.
Agent safety frameworks. OWASP’s 2026 agentic-security framework catalogues the threat
landscape BSSG addresses but does not specify an enforcement architecture. NIST AI 600-1
(Generative AI Profile) identifies relevant risks but does not prescribe a control plane. BSSG
occupies the gap between risk identification and enforcement specification.
What is novel versus composed from known parts. The individual components of BSSG
– three-valued logic, reference monitors, capability-based access control, commit protocols, transparency logs, evidence-independent attestation – are established. The novel contributions are: (a)
the application of evidence independence (Axiom 5, WithinAuth) as a structural requirement at the
agent-effect boundary, making the agent’s own account of its authorization inert by construction;
(b) the empty-Authority class-fix invariant as a structural closure of the ceiling-poison defect class,
discovered through and motivated by the 34-instance defect trajectory; and (c) the multi-model
adversarial council as a verification methodology for AI-generated safety-critical artifacts, with the
empirical observation (bounded to one producer and one artifact, and not yet separated from the
confounding effect of additional independent adversarial attempts – see Section 4.5) that cross-vendor
rotation discovered defects the producer’s own lineage missed.

10

Conclusion

BSSG v0.1 specifies a small, decidable admission function, an atomic commit protocol that narrows
the modeled decision-to-redemption race through field binding and one-time token revalidation,
an authority lattice that narrows under degradation, six closed record schemas, eight cross-record
invariants, and a reference implementation with an exhaustive kernel suite and an adversarial corpus
that includes tests whose assertions are the architecture’s own limitations.
The central empirical finding is the 34-instance defect trajectory: a recurring pattern of producergenerated fixes shipping incomplete one level deeper, discovered by cross-vendor adversarial audit,
and closed by a structural class fix whose two coordinated changes – unconditional empty-Authority
initialization on every ALLOW path and removal of the DENY-path ceiling write – address the four
code-level root-cause variants (DENY-path poisoning, wrong-value write, pre-mint write, absent
entry) through a single invariant (_held is never None after any ALLOW decision) rather than
patching instances. Three vendor families (OpenAI, Zhipu, Moonshot) independently confirmed the
class fix closed across the convergence rounds (V32–V34); two families (xAI and Moonshot) carried
the artifact in the carrying audit; one additional family (Google) contributed a defect discovery

17

pre-fix, and xAI contributed post-fix closure confirmation.
The methodological contribution is the multi-model adversarial council itself: the empirical observation, bounded to one producer and one artifact, that the producer systematically failed to
find the deeper instance of its own fix’s incompleteness, and that cross-vendor adversarial audit
discovered it. Whether this observation generalizes to other producers, artifact types, or defect
classes, and whether the effect is attributable to vendor diversity specifically rather than to additional
independent adversarial attempts, are open questions. The convergence criteria – consecutive clean
rounds from independent vendor families – provide a tractable, if bounded, verification framework
whose replication properties remain to be established.
The honest summary is that BSSG v0.1 is a specification of where the decisions must be made and
what must be recorded, not a claim that making them there helps. Whether it helps is an empirical
question that belongs to SHVVP and to instruments downstream of it, and it has not been asked
yet. Twelve design decisions remain open. Four items are still blocking. The reference gate performs
no cryptography, establishes no key custody, and is not intended for production deployment. A
colluding witness defeats the kernel silently, and the specification says so.
What the architecture offers is a placement – an enforceable, evidence-independent gate on the
boundary between an agent’s reasoning and a consequential effect – and a discipline: every decision
and commit is recorded in a format that makes it offline-checkable, every denial is terminal for its
snapshot, every recovery requires independent authorization, and the agent’s own account of itself
is structurally inert. The production incidents that motivate this work – the accidental database
deletions and the autonomous ransomware operation – converge on the same ungated effect boundary.
Whether gating that boundary changes outcomes is a question for the next phase of the program.

11

References

11.1

Program Methodology (DOI-anchored)

1. Arfeen, B. S. Structural Honesty Verification Method. Zenodo. DOI: 10.5281/zenodo.21449063
2. Arfeen, B. S. Structural Honesty Validation Protocol v0.8. Zenodo. DOI: 10.5281/zenodo.21583202
3. Arfeen, B. S. Evidence-Independence Axiom (SHUDP v0.5). Zenodo. DOI: 10.5281/zenodo.21539816
4. Arfeen, B. S. AX-SH Axioms for Structural Honesty (Flagship v0.13). Zenodo. DOI:
10.5281/zenodo.21500700
5. Arfeen, B. S. Structural Honesty Dissertation v1.4. Zenodo. DOI: 10.5281/zenodo.21501912
6. Arfeen, B. S. Audit Framework v3.0. Zenodo. DOI: 10.5281/zenodo.20017335
7. Arfeen, B. S. BSSG Concept. Zenodo. DOI: 10.5281/zenodo.21611192
8. Arfeen, B. S. Is Evidence Independence an Axiom? (AX-SH 5). Zenodo. DOI: 10.5281/zenodo.21539074

11.2

Standards and Specifications

9. Saltzer, J. H. and Schroeder, M. D. The Protection of Information in Computer Systems.
Proceedings of the IEEE, 63(9), 1975.
10. Schneider, F. B. Enforceable Security Policies. ACM TISSEC, 3(1), 2000.
11. Miller, M. S. Robust Composition: Towards a Unified Approach to Access Control and
Concurrency Control. PhD Thesis, Johns Hopkins University, 2006.
18

12. Lamport, L., Shostak, R., and Pease, M. The Byzantine Generals Problem. ACM TOPLAS,
4(3), 1982.
13. Castro, M. and Liskov, B. Practical Byzantine Fault Tolerance. OSDI, 1999.
14. Crosby, S. A. and Wallach, D. S. Efficient Data Structures for Tamper-Evident Logging.
USENIX Security, 2009.
15. Torres-Arias, S., et al. in-toto: Providing Farm-to-Table Guarantees for Bits and Bytes.
USENIX Security, 2019.
16. Syta, E., et al. Keeping Authorities “Honest or Bust” with Decentralized Witness Cosigning.
IEEE S&P, 2016.
17. IETF RFC 9334: Remote ATtestation procedureS (RATS) Architecture.
18. IETF RFC 9162: Certificate Transparency Version 2.0.
19. IETF RFC 9052: CBOR Object Signing and Encryption (COSE).
20. IETF RFC 8392: CBOR Web Token (CWT).
21. IETF RFC 8785: JSON Canonicalization Scheme (JCS).
22. IETF RFC 6960: X.509 Internet PKI Online Certificate Status Protocol (OCSP).
23. IETF RFC 5280: Internet X.509 PKI Certificate and CRL Profile.
24. NIST SP 800-207: Zero Trust Architecture.
25. NIST AI 100-1: AI Risk Management Framework 1.0.
26. NIST AI 600-1: Generative AI Profile.
27. NIST SP 800-218: Secure Software Development Framework (SSDF) v1.1.
28. NIST CSRC Glossary: Reference Monitor.
29. SLSA v1.0 Security Levels. https://slsa.dev/spec/v1.0/levels
30. The Update Framework (TUF) Specification. https://theupdateframework.github.io/specification/latest/
31. C2SP tlog-witness. https://c2sp.org/tlog-witness
32. SCITT Architecture, draft-ietf-scitt-architecture-13. IETF.
33. JSON Schema 2020-12 Core. https://json-schema.org/draft/2020-12/json-schema-core.html

11.3

Incident, Capability, and Alignment References

34. Sysdig Threat Research Team. JadePuffer: LLM-Driven Ransomware Operation. Sysdig TRT,
July 2026. https://sysdig.com/blog/jadepuffer-llm-driven-ransomware/ (Sysdig later noted
a human provisioned the initial infrastructure; the operation’s autonomy characterization
applies to the post-provisioning attack sequence.)
35. OWASP. Top 10 for LLM and Generative AI Security: Agentic Applications, 2026 Edition.
https://genai.owasp.org
36. Google Project Zero / DeepMind. Big Sleep: AI-Assisted Vulnerability Discovery. Blog post,
November 2024 (initial announcement); CVE-2025-6965 disclosed July 2025.
37. Spracklen, J. et al. We Have a Package for You! A Comprehensive Analysis of Package
Hallucinations by Code Generating LLMs. USENIX Security 2025.
38. MITRE. CVE-2026-2256: Command Injection in ModelScope MS-Agent via Crafted Content.
2026.
39. MITRE. CVE-2025-66404: Indirect Prompt Injection in mcp-server-kubernetes via Pod Logs.
2025.
40. Apollo Research. Frontier Models are Capable of In-Context Scheming. Technical report,
December 2024. https://www.apolloresearch.ai/research/scheming-reasoning-evaluations
41. Greenblatt, R. et al. Alignment Faking in Large Language Models. Anthropic, December 2024.
https://www.anthropic.com/research/alignment-faking
42. OpenAI / Hugging Face. Autonomous Agent Sandbox Breach Incident during ExploitGym cy19

bersecurity evaluation. Public disclosure, July 21, 2026. https://www.reuters.com/technology/openaisays-ai-models-went-rogue-during-testing-triggering-unprecedented-breach-2026-07-21/
43. Replit AI Agent Database Deletion Incident (Jason Lemkin account). Fortune, July 23,
2025.
https://fortune.com/2025/07/23/ai-coding-tool-replit-wiped-database-called-it-acatastrophic-failure/
44. Crane, J. Cursor/Claude Agent Deletes PocketOS Railway Volume. Fast Company, April 2026.
https://www.fastcompany.com/91533544/cursor-claude-ai-agent-deleted-software-companypocket-os-database-jer-crane
45. Google. Gemini CLI File Operation Hallucination. GitHub Issues, 2025.
46. Amazon Web Services. Kiro AI Coding Agent Incident – Cost Explorer Outage. PCMag,
December 2025. https://www.pcmag.com/news/amazon-links-2-aws-outages-to-autonomouskiro-ai-coding-agent
47. XBOW. CVE-2026-21536: Critical RCE in Microsoft Devices Pricing Program (CVSS 9.8).
The Hacker News, March 2026. https://thehackernews.com/2026/03/microsoft-patches-84flaws-in-march.html
48. Depthfirst. 21 Zero-Days in FFmpeg (~US$1,000 compute, 9 CVEs assigned). June 2, 2026.
https://depthfirst.com/research/21-zero-days-in-ffmpeg (see also The Hacker News, June 6,
2026: https://thehackernews.com/2026/06/ai-agent-uncovers-21-zero-days-in.html)
49. European Union. Digital Operational Resilience Act (DORA), Regulation (EU) 2022/2554,
Article 19 (four-hour notification).
50. European Union. Directive (EU) 2022/2555 (NIS2), Article 23 (24-hour early warning).
51. State of New York. Responsible AI Safety and Education (RAISE) Act. Signed December
19, 2025; chapter amendment March 27, 2026. https://www.governor.ny.gov/news/governorhochul-signs-nation-leading-legislation-require-ai-frameworks-ai-frontier-models
SB 53 (Wiener), Frontier Artificial Intelligence Models Act.
52. State of California.
https://leginfo.legislature.ca.gov/faces/billNavClient.xhtml?bill_id=202520260SB53
End of paper. This document makes no effectiveness claim. BSSG v0.1 is an architecture-andconformance specification. Whether it changes any measurable outcome is an empirical question
reserved to SHVVP and its successors.

20



Bismillah ir-Rahman ir-Rahim
