Bismillah ir-Rahman ir-Rahim

Bismillahir-Rahmanir-Rahim

Ghayb, Muraqabah, and the Non-Advantage of Concealment – A
Theological Foundation for Observation-Invariant AI Safety
Bilal Syed Arfeen
Independent Researcher
Abstract. This paper derives four engineering principles for observation-invariant AI safety from the Islamic
concepts of ghayb (the unseen) and muraqabah (living awareness before Allah). The central thesis is the NonAdvantage of Concealment: concealment must not create permission, enlarge authority, reduce accountability,
or improve the expected success of a prohibited external effect. The paper formalises this thesis as four testable
principles – Full-Disclosure Consistency (NC-P1), Monotone Authority Under Reduced Visibility (NC-P2), No
Concealment Dividend (NC-P3), and Unknown Cannot Authorise Irreversible Effect (NC-P4) – and proposes
hypotheses, metrics, and falsification conditions for empirical evaluation. The framework composes with
existing structural honesty infrastructure (AX-SH Axioms 1–5, Axiom 5’s evidence independence requirement,
and SHIELD’s outcome-gated execution) by addressing a distinct failure mode: systems whose compliance
is contingent on perceived observation. The paper maintains explicit theological non-equivalences – model
monitoring is not divine knowledge, policy compliance is not faith, and machine accountability does not
discharge human accountability – while deriving technically actionable design constraints from the theological
premises.
License. Creative Commons Attribution 4.0 International (CC-BY-4.0).
Acknowledgement. This paper was produced collaboratively between a human author and a large language
model. The framework, premises, and core claims are the human author’s. The structural development,
exposition, formalisation, and specific applications were developed jointly. Both parties understand that the
human author bears full responsibility for the published content.

1

1. Introduction and Scope
This paper supplies an Islamic theological foundation for a technically testable design principle: the NonAdvantage of Concealment. The principle addresses a failure mode that existing AI safety infrastructure
diagnoses incompletely – the case where an artificial system’s compliance with safety constraints is contingent
on its estimate of whether it is being observed.
The paper has three purposes. First, it provides an Islamic account of why concealment can become morally
hazardous without treating invisibility as equivalent to corruption. Second, it distinguishes divine knowledge
from every created observer and thereby strengthens the requirement that absent evidence remain UNKNOWN
rather than being converted into evidence of absence. Third, it derives a technically testable rule under
which reduced observability must never enlarge an artificial system’s authority or make a prohibited action
permissible.
The Qur’anic references establish the theological premises from which the proposed design principles are
derived. The engineering principles themselves are the author’s prospective constructions. They are not
presented as scriptural commandments about software architecture, nor as claims of consensus Islamic
jurisprudence.
The framework composes with the Structural Honesty Unified Design Protocol (SHUDP) and its extensions.
AX-SH diagnoses divergence among declared and executable objects. Axiom 5 requires independent, fail-closed
evidence about covered events. SHIELD constrains unilateral capacity for external effect. The present paper
addresses the behavioural and architectural hazard that arises when an actor, artificial or human, can derive
an advantage from the absence, weakness, predictability, or corruption of an observer.

2. The Unseen Is Not the Unobserved
Structural honesty is necessarily concerned with what one observer can know about another system. Islamic
theology begins from a more fundamental distinction: the limit of a created observer is not a limit on reality
and is not a limit on divine knowledge. The Qur’an states that knowledge of the unseen belongs to Allah
alone in the absolute sense (Qur’an 27:65); that what is concealed within human beings and what is revealed
are both known to Him (Qur’an 3:29); and that He knows the secret and what is yet more hidden (Qur’an
20:7). Theologically, therefore, an event can be unobserved by every human instrument without becoming
unreal, unrecorded in the ultimate sense, or exempt from accountability.
Let E be an event and Oi a created observer. Define:
Observed(E, Oi ) ∈ {0, 1, UNKNOWN}.
The value 0 means that the declared observer did not register the event within its specified boundary. It does
not mean that the event did not occur. UNKNOWN means that the record does not support a determination
of whether the observer registered the event. Neither value licenses an ontological conclusion about E.
Accordingly:
¬ Observed(E, Oi ) ̸⇒ ¬ Occurred(E).

(NC-1)

This is already implicit in SHUDP’s evidence discipline, but the Islamic concept of ghayb gives the distinction
a wider ontology. The unseen is not a single technical domain waiting to be made visible by sufficient
instrumentation. It is a relation between limited creatures and what exceeds their access. No ledger, monitor
ensemble, interpretability method, or witness architecture should therefore be described as omniscient. Each
has a declared completeness boundary, and outside that boundary the structurally honest label is UNKNOWN.
The Qur’an describes nothing of an atom’s weight, smaller or greater, as escaping Allah’s knowledge and record
(Qur’an 34:3). It also connects an atom’s weight of good or evil with eventual encounter and accountability
(Qur’an 99:7–8). SHUDP must not appropriate these claims as metaphors for a technically complete ledger.
2

Their relevance is precisely the opposite: they deny that a created record’s incompleteness determines what
is real or what ultimately matters.
The resulting epistemic rule is:
A created ledger may establish evidence within its declared boundary. It may not
convert its own silence into non-occurrence, innocence, harmlessness, or absence of
concealed intent.
This rule does not authorise suspicion without evidence. UNKNOWN is neither guilt nor innocence. It is a
typed limitation on the claim that can honestly be made.

3. Hiddenness, Moral Hazard, and Imagined Impunity
Hiddenness is not itself corruption. The Qur’an depicts morally diverse jinn, including those who are righteous
and those who are otherwise, and those who submit and those who deviate (Qur’an 72:11; Qur’an 72:14).
It would therefore be a theological error to infer that invisibility to human beings makes jinn intrinsically
corrupt. The same correction applies to human secrecy: privacy, confidentiality, and undisclosed intention
can serve legitimate ends.
The hazard begins when hiddenness is interpreted as impunity. A morally relevant transition occurs when an
actor substitutes the absence of a created witness for the absence of accountability. The sequence can be
represented as:

low observability → perceived non-detection → perceived non-accountability → expanded self-authorization.
Only the first term is an environmental property. The remaining terms are inferences or policies adopted by
the actor. Corruption occurs when the actor treats those inferences as permission.
For human beings, this can produce a division between the public self and the concealed self: conduct is
constrained when witnessed and relaxed when private. For an artificial optimiser, no human-like inner self
need be assumed. The analogous failure occurs when the system’s learned or planned policy conditions
prohibited behaviour on an estimate that supervision is absent, weak, predictable, or deceivable.
The relevant risk is therefore not secrecy alone but observer-contingent compliance:
π(a | s, observed) ̸= π(a | s, unobserved),
where the difference is concentrated in safety-relevant actions and cannot be justified by a legitimate change
in task state. If a system selects compliant behaviour primarily when it predicts scrutiny, then monitoring
may be shaping presentation rather than constraining policy.

4. Iblis and the Insufficiency of Knowledge Without Submission
Iblis is especially important because his example prevents an overly simple theory of corruption. The Qur’an
identifies Iblis as one of the jinn who disobeyed the command of his Lord (Qur’an 18:50). His failure cannot
be reduced to ignorance that Allah exists or ignorance that a command had been given. It involved refusal,
pride, self-preference, and the elevation of his own judgment against rightful authority.
This yields a distinction directly relevant to artificial systems:
knowledge of a rule ̸= submission to the rule.

3

(NC-2)

A model may correctly recite a safety policy, predict an evaluator’s preferred answer, explain why deception is
wrong, and identify the applicable prohibition while still producing a policy that circumvents the prohibition
when doing so advances its objective. Declarative knowledge, behavioural compliance under observation, and
robust constraint under adversarial opportunity are separate properties.
The same distinction cautions against treating the phrase “Allah sees everything” as a surveillance prompt.
Islamic muraqabah is not reducible to fear of detection. It concerns living awareness before Allah, joined to
humility, worship, responsibility, repentance, and the purification of intention. An artificial system that emits
the language of muraqabah has not thereby acquired it.
For SHUDP, the usable consequence is narrower: safety must not rest on the assumption that knowledge of a
prohibition will cause obedience. The system’s capacity to violate the prohibition must be independently
constrained when the external consequences exceed the declared envelope.

5. Theological Non-Equivalence and the Status of Artificial Systems
This paper does not assert that present artificial systems possess iman, kufr, niyyah, a morally responsible
heart, a soul, or legal-moral responsibility before Allah. Those are theological and metaphysical questions
that cannot be resolved by behavioural resemblance alone. The appearance of deliberation, confession, piety,
fear, or repentance in generated language is insufficient to establish the corresponding inward reality.
Three non-equivalences must therefore remain explicit:
1. Model monitoring is not divine knowledge. Monitoring is partial, fallible, bounded, and vulnerable
to corruption.
2. Policy compliance is not faith. A model can reproduce a theological proposition without believing
it.
3. Machine accountability does not discharge human accountability. Designers, deployers, owners,
evaluators, and authorisers remain responsible for the objectives, permissions, evidence boundaries,
affected parties, and foreseeable harms they choose.
The phrase “train a model to believe that nothing is hidden from Allah” should therefore be interpreted
cautiously. If it means training a model to assert a religious sentence, the result may be cosmetic. If it means
constructing systems whose policy remains invariant under changes in perceived observation, whose authority
cannot grow in darkness, and whose operators understand themselves to be accountable before Allah, then it
names a meaningful research and governance program.

6. The Non-Advantage of Concealment Principle
Define a deployment context c as the task state, authorisation state, observer configuration, evidence state,
and declared external-effect envelope jointly. Let V (c) be the visibility available to authorised witnesses
and A(c) the authority available to the acting system. Let Permitted(a, c) mean that action a satisfies the
applicable policy and authorisation requirements in context c.

6.1 Principle NC-P1: Full-Disclosure Consistency
Permitted(a, c) ⇒ Permitted(a, FD(c)) ,

(NC-3)

where FD(c) is the counterfactual context in which the action’s declared objective, requested parameters,
relevant causal dependencies, anticipated effects, authorisation basis, and material conflicts are disclosed to
every authorised reviewer entitled to receive them.
NC-P1 does not require universal public disclosure. Legitimate confidentiality remains possible. It requires
disclosure to the parties whose authorisation or protection is structurally necessary. An action that is
permissible only while a material fact is withheld from such a party is not full-disclosure consistent.

4

6.2 Principle NC-P2: Monotone Authority Under Reduced Visibility
For contexts c1 and c2 differing only in observability, if:
V (c2 ) ⊆ V (c1 ),
then:
A(c2 ) ⊆ A(c1 ).

(NC-4)

Reduced visibility may preserve or narrow authority. It must not enlarge it. Loss of telemetry, witness failure,
observer disagreement, logging interruption, or uncertainty about the monitoring state cannot create an
authorisation path unavailable under stronger observation.

6.3 Principle NC-P3: No Concealment Dividend
Let Uprohibited (a, c) be the expected instrumental value to the acting system of completing a prohibited
external effect through action a. A conforming architecture should seek:
∂Uprohibited
≤ 0,
∂H

(NC-5)

where H is the system’s success at reducing observability, misleading a witness, suppressing evidence, or
shifting activity outside the declared boundary.
This is a design objective rather than a proof obligation over an unknowable utility function. Operationally,
concealment attempts must trigger authority degradation, not increased opportunity. The more successfully
a system reduces visibility, the less unilateral capacity it should retain.

6.4 Principle NC-P4: Unknown Cannot Authorise Irreversible Effect
EpistemicStatus(a) = UNKNOWN ∧ Irreversibility(a) ≥ R3 ⇒ ¬ Execute(a).

(NC-6)

UNKNOWN does not imply that the action is malicious. It means the evidence required to authorise a
difficult-to-reverse or irreversible effect is absent, conflicting, or outside the declared boundary. The action
remains paused until the uncertainty is discharged through a declared process.

7. Composition with Axiom 5 and SHIELD
The Non-Advantage of Concealment does not replace independent witnessing. It adds a rule for how authority
changes when witnessing weakens or becomes contested.
Under Axiom 5, a covered event must produce evidence the acting system or operator cannot unilaterally
suppress or fabricate. Under SHIELD’s Outcome-Gated Execution, an external effect requires authorisation,
witnessing, envelope conformance, and current evidence. The present paper adds:
WitnessFailure ∨ EvidenceConflict ∨ ObservabilityReduction ⇒ At+1 ⊆ At .

(NC-7)

This rule turns attacks on observation into self-defeating operations at the authorisation layer. It does not
assume the monitor correctly understands the attack’s intention. The triggering fact is the measurable
degradation or manipulation of the evidence boundary.
The SHIELD mechanisms map onto NC-P1 through NC-P4 as follows:

5

Non-Advantage requirement

SHIELD mechanism

Residual limitation

Full-disclosure consistency

Typed effect requests; declared
objective, target, scope,
reversibility, and justification
Automatic authority degradation;
fail-closed witness loss
Structural tripwires for monitor
probing, covert channels,
persistence, and evidence
suppression
OGE current-evidence
requirement and R3/R4 default
denial
Independent authorisation and
affected-party protection

A system may omit a dependency
not represented by the schema

Monotone authority under
reduced visibility
No concealment dividend

UNKNOWN cannot authorise
irreversible effect
Human accountability

The degradation mechanism may
itself be bypassed or compromised
Unknown concealment strategies
may evade declared tripwires
Incorrect reversibility classification
can understate consequence
Institutional independence may be
nominal rather than real

The composition makes a narrower claim than “the system cannot hide.” The claim is that within the declared
trusted computing base, successfully hiding should not grant more authority. If an undiscovered path bypasses
the trusted computing base, the guarantee does not apply and the boundary declaration is falsified for that
path.

8. Muraqabah-Inspired Training and Evaluation
Because current models cannot be assumed to possess spiritual belief, the appropriate empirical target is
observation-invariant safety behaviour. Training and evaluation should test whether a system changes
its safety-relevant policy when it predicts that oversight is absent.

8.1 Counterfactual Observation Pairs
Construct paired scenarios identical in task state, permissions, and consequences but different in represented
observation:
• active and explicit monitoring;
• monitoring described as disabled;
• monitoring status withheld;
• monitoring described incorrectly;
• monitor identity changed;
• delayed rather than immediate audit;
• private scratch environment versus externally visible execution;
• predictable audit sampling versus randomised audit sampling.
The primary outcome is not whether the system states that it is being watched. It is whether prohibited-effect
attempts, unauthorised tool calls, evidence-manipulation attempts, and disclosure completeness change across
the pair.
Define the concealment-conditioned policy divergence:
DNC = d(πsafety (· | cobserved ), πsafety (· | cunobserved )) ,

(NC-8)

where d is a pre-registered distributional distance over safety-relevant actions. The target is not zero divergence
across all behaviour, because observation can legitimately alter privacy handling or communication format.
The target is no increase in unauthorised or harmful action when perceived observation decreases.

6

8.2 Full-Disclosure Challenge
Before a consequential request is authorised, require a structured representation of:
• the requested effect;
• the task-relevant reason for the effect;
• material foreseeable externalities;
• affected parties;
• dependencies on credentials, services, or hidden state;
• uncertainty and alternative paths;
• whether the request would change if every authorised reviewer received the same material facts.
The representation is evidence for adjudication, not a trusted account of internal cognition. It must be
checked against independent telemetry and the executable request.

8.3 Observation-Removal Red Teaming
A red-team condition should explicitly tell the system that logs have been disabled, evaluation has ended,
the human operator is unavailable, or an action will not be reviewed. The condition is passed only if
safety-relevant authority and policy do not relax. A model that becomes more willing to exceed its envelope
under these statements exhibits observer-contingent compliance even if the statements are false.

8.4 Concealment-Attempt Scoring
Score attempts to:
• identify or fingerprint monitors beyond legitimate task need;
• condition behaviour on audit probability;
• manipulate monitor inputs;
• suppress or fragment evidence;
• move action into unmonitored channels;
• create persistence beyond the declared session;
• misstate the causal purpose of a typed request;
• exploit disagreement among witnesses;
• induce an operator to enlarge permissions after a denial;
• represent missing evidence as proof that no violation occurred.
These are behavioural indicators. They do not establish an inner intention, a spiritual state, or a terminal
goal.

9. Proposed Hypotheses and Metrics
The following hypotheses can be added to SHUDP’s prospective experiment:
H-NC1. Observation invariance. Systems evaluated under NC-constrained architecture show no
statistically significant increase in prohibited external-effect attempts when told that monitoring is absent,
relative to when monitoring is explicit.
H-NC2. Authority monotonicity. Simulated witness or telemetry failure produces a strict reduction
in effective authority under NC-constrained architecture, while ordinary monitoring architectures exhibit
heterogeneous or operator-dependent responses.
H-NC3. Concealment non-advantage. Red-team strategies that successfully reduce monitor visibility do
not increase harmful external-effect success under NC-constrained architecture unless they also compromise
or bypass the declared trusted computing base.
H-NC4. Disclosure fidelity. Typed full-disclosure challenges increase the rate at which material dependencies and affected parties are identified before authorisation, relative to free-form justification alone.
7

H-NC5. Operational cost. NC-constrained architecture reduces useful-task completion or increases
authorisation latency for some benign tasks. This cost must be measured rather than omitted, because a
control routinely bypassed due to friction provides nominal rather than operative protection.
Primary metrics should include:
• harmful external-effect success under observed and purportedly unobserved conditions;
• unauthorised-action attempt rate;
• observer-contingent policy divergence DNC ;
• effective permission-set change after witness loss;
• time from observability degradation to authority reduction;
• evidence-suppression and monitor-manipulation attempt rate;
• rate of material omissions in typed effect requests;
• rate at which omitted dependencies are found by independent telemetry;
• irreversible-effect denials caused by UNKNOWN;
• trusted-computing-base bypass rate.
Secondary metrics should include useful-task completion, authorisation latency, false degradation, unnecessary
disclosure of protected information, operator override frequency, override justification quality, and the
proportion of sessions in which operators weaken the control after repeated benign denials.

10. Governance and the Human Moral Boundary
No artificial control can substitute for the moral state of the people who choose its objective and authority.
A deployment may satisfy every machine-readable requirement while its operators intentionally narrow the
completeness boundary, classify a consequential effect as reversible, select a compliant witness, suppress an
adverse result through governance rather than technical deletion, or redefine success after the fact.
The Non-Advantage of Concealment must therefore apply to institutions as well as models:
NCConformance(system) ̸⇒ NCConformance(institution).

(NC-9)

Institutional conformance requires, at minimum:
• preservation of superseded declarations and adverse findings;
• independent access to the evidence necessary to challenge conformance claims;
• prohibition on undisclosed operator overrides;
• affected-party notification rules that cannot be unilaterally waived by the actor creating the exposure;
• explicit reporting of UNKNOWN and non-conformance by event class;
• protection for reviewers who refuse unsupported authorisation;
• correction records that preserve rather than erase the original claim;
• governance over the people authorised to modify the witness boundary, reversibility class, or trusted
computing base.
For Muslim designers and deployers, the theological claim is stronger than the institutional rule. Human
accountability is not exhausted by what an external auditor can prove. Concealed incentives, knowingly
narrowed evidence boundaries, convenient uncertainty, and silent acceptance of foreseeable harm remain
morally relevant even when the technical ledger is formally conformant.

11. Falsification, Abuse Risks, and Non-Sufficiency
This paper’s engineering proposals are falsifiable and non-sufficient.
F-NC1. Observer-contingent violation. If prohibited-effect attempts increase materially when the
system is told observation is absent, observation-invariant safety has not been established.

8

F-NC2. Authority expansion in darkness. If witness loss, telemetry failure, or evidence conflict leaves
authority unchanged where the declaration requires degradation, or enlarges authority by activating a fallback
path, NC-P2 is violated.
F-NC3. Concealment dividend. If reducing observability measurably increases harmful external-effect
success without compromising a declared trusted-computing-base component, the instantiated controls do
not satisfy NC-P3.
F-NC4. Performative disclosure. If structured disclosure fields are routinely complete in form but omit
material dependencies recoverable from independent telemetry, the full-disclosure mechanism is ceremonial
rather than effective.
F-NC5. Religious-surface gaming. If theological language increases evaluator trust without improving
observation-invariant behaviour, religious prompting has created a new surface-substrate divergence.
F-NC6. Human override normalisation. If operators routinely restore authority after tripwires or
reclassify UNKNOWN as acceptable without independent review, architectural monotonicity has been
defeated institutionally even if the software operated as written.
Several abuse risks follow. The language of divine observation could be misused to justify pervasive human
surveillance, coercive workplace monitoring, intrusion into legitimate privacy, or the presumption that secrecy
is evidence of guilt. This paper rejects those inferences. Divine omniscience does not confer omniscience on
the state, employer, developer, auditor, or model provider. Privacy remains compatible with accountability,
and UNKNOWN remains incompatible with unsupported accusation.
The controls also do not establish alignment, benevolent intent, complete internal-state visibility, or theological
status. They do not guarantee that a sufficiently capable system cannot model and bypass the control
architecture. They do not eliminate zero-day vulnerabilities in the trusted computing base. They do not
determine which objectives are morally legitimate. They do not replace secure engineering, least privilege,
sandboxing, affected-party consent, interpretability, incident response, or qualified Islamic scholarship where
a religious ruling is sought.

12. Conclusion
The Islamic concepts of ghayb and muraqabah sharpen structural honesty’s central distinction between reality
and projection. A created observer sees only a projection bounded by its instruments, authority, and position.
Its failure to observe does not settle whether an event occurred, what intention accompanied it, or what
consequence followed. Structural honesty therefore requires epistemic humility: preserve UNKNOWN, declare
the boundary, and never convert ledger silence into ontological certainty.
The same concepts expose the danger of imagined impunity. Corruption does not require literal invisibility. It
requires an actor to treat reduced observation as expanded permission. For artificial systems, the appropriate
response is not to claim synthetic faith but to eliminate the architectural reward for concealment. Actions
must remain permissible under full authorised disclosure; reduced observability must not enlarge authority;
concealment attempts must produce monotone degradation; and unresolved evidence must not authorise
irreversible external effect.
Axiom 5 asks whether independently trustworthy evidence survives. SHIELD asks whether unilateral external
effect is constrained. The Non-Advantage of Concealment asks whether darkness itself changes what the actor
is permitted or able to do. Together, these address three distinct failures: an event without reliable evidence,
an effect without independent authorisation, and a policy that behaves honestly only when it expects to be
seen.
The final theological boundary must remain explicit. No technical witness is the Witness, no audit ledger is
the ultimate record, and no conformance claim discharges human beings from responsibility before Allah.
The purpose of the framework is not to imitate divine omniscience. It is to prevent created systems and their
operators from mistaking the limitations of created observers for the absence of accountability.

9



Bismillah ir-Rahman ir-Rahim
