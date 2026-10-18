Bismillah ir-Rahman ir-Rahim

Unified Structural Audit Methodology
v1.0
Five-Model Architecture for Construct Validation

A systematic methodology for auditing preregistered instruments, integrating five complementary analytical
models derived from fractal geometry, molecular biology, atomic physics, enzymology, and cell-cycle
regulation.

Author: Bilal Syed Arfeen
Program: Bayyinah Structural Honesty Validation
Date: 2026-08-09
Status: DRAFT

Prepared with frontier language models as analytical and drafting instruments under the author's direction and final authority.
This methodology document makes no effectiveness claim; whether it improves any measurable outcome is an empirical
question.

Contents
1. Introduction: The Five Questions
2. Dependency Graph and Operational Sequence
3. Model I -- Recursive Fractal Cube (WHERE)
4. Model II -- Enzyme-Substrate System (WHAT)
5. Model III -- Replication Fork (HOW)
6. Model IV -- Quantum Orbital (WHO)
7. Model V -- Cell Cycle Checkpoint (WHEN)
8. The Composed Architecture
9. Operational Annexes

1. Introduction: The Five Questions
Every audit of a preregistered instrument must answer five questions. Each question requires a different
analytical tool. No single model reaches all five. The failure to answer any one of them creates a specific,
predictable class of defect.
Questi
on

Domain

Failure if unanswered

Natural basis

WHER
E

Which recursion level generated
the defect? Which analytical cells
are gated vs ungated?

Repairs patch outputs (Level N)
while the generator (Level N-1)
continues producing them

Fractal
geometry

WHAT

What kind of claim is this? What
verification method does its type
require?

All claims treated identically;
type-specific mismatches escape
detection

Enzymology

HOW

How does the producer synthesize
the entry? Where in the pipeline
are claims verified?

Verification deferred to post-hoc
audit; mismatches sealed into
the record before checking

DNA replication

WHO

Who should audit this artifact?
What anchoring does each seat
need?

Fresh seats cannot verify
cross-version claims; continuous
seats may confuse anchor for
artifact

Atomic physics

WHEN

When in the lifecycle should this
defect be caught? How should
chronic defects escalate?

Same defect falsely closed for N
consecutive rounds; no
escalation, no structural fix
trigger

Cell cycle

The five models composing this methodology were derived empirically from seven convergence rounds
(R1 through R7) of the XZ Protocol audit series, totaling 68 seat-reports across four model families. Each
model addresses a failure class that was observed, diagnosed, and -- in some cases -- reproduced
multiple times before the correct analytical frame was identified. The models are not speculative; they are
post-hoc formalizations of patterns that emerged from the data.
Empirical basis. The standing defect class throughout the series is Axiom-3: governance claims narrated
from memory rather than verified against bytes. This defect appeared at every recursion level (entry prose,
corrections, register dispositions, standing properties, dispatch wrappers), persisted across at least 12
consecutive rounds despite targeted repair, and was only partially attenuated by a Level 0 process
intervention at v0.48. The five models formalize the five dimensions along which this single defect class
was analyzed, and along which it must be constrained.

2. Dependency Graph and Operational Sequence
2.1 Why order matters
The five models are not independent modules that can be applied in arbitrary order. They form a directed
acyclic dependency graph in which each model's output is consumed by one or more downstream models.
Applying them out of order produces either redundant work (re-deriving what an upstream model already
computed) or unsound work (acting on classifications not yet established).
The dependency ordering is derived from a single principle: each model depends on the models whose
outputs it consumes as inputs.

2.2 The dependency structure
Model

Depends on

Provides to

Rationale

I. Fractal Cube
(WHERE)

None (found
ational)

All others

The recursion-level taxonomy and
face-interior/edge distinction are consumed by
every downstream model

II. Enzyme
System (WHAT)

I (WHERE)

III (HOW)

Claim classification requires knowing which
cells are gated (WHERE) to determine which
claims need enzymatic verification

III. Replication
Fork (HOW)

I (WHERE),
II (WHAT)

IV (WHO), V
(WHEN)

The build pipeline uses the claim types (WHAT)
as enzyme substrates and the gate topology
(WHERE) to route verification

IV. Orbital
(WHO)

I (WHERE),
III (HOW)

V (WHEN)

Seat deployment requires the gate topology
(WHERE) to assign continuous vs fresh, and
the built artifact (HOW) to dispatch

V. Cell Cycle
(WHEN)

All others

I (next round)

Lifecycle governance consumes findings from
all models and feeds the diagnostic for the next
round's WHERE analysis

2.3 Operational sequence within a single round
Within a single audit-repair-dispatch cycle, the five models are applied in the following sequence. Each
phase produces an artifact consumed by the next phase. The sequence is not optional; skipping a phase
means the downstream phases operate without their required inputs.
1. Diagnosis (Fractal Cube / WHERE). Analyze the prior round's findings. Classify each by recursion
level (0-4). Identify which cells are face-interior (ungated). Determine whether the defect generator is
at Level 0 or lower. Output: a defect map and a gate-coverage topology.
2. Classification (Enzyme System / WHAT). For each claim that will appear in the new entry, classify
it by type: COMPUTED, DIFF-VERIFIED, ENUMERATED, PROVENANCE, EXTERNAL, COUPLED.
Assign the type-specific verification enzyme. Output: a typed claim manifest with enzyme
assignments.
3. Synthesis (Replication Fork / HOW). Build the new version. For each claim, apply the assigned
enzyme inline (the exonuclease). For each repair, unwind coupled constraints (the helicase). Seal

only after the face-interior verifier passes. Output: a sealed artifact.
4. Deployment (Orbital / WHO). Dispatch the sealed artifact to audit seats. Assign fresh vs continuous
based on the gate topology. Assign frameworks based on rotation. Ship the claim manifest so seats
can verify enzyme coverage. Output: dispatched audit packages.
5. Governance (Cell Cycle / WHEN). Receive audit results. Apply phase-gate checks. Escalate
chronic findings. Trigger structural-fix requirements for 3-round persistent defects. Feed the
diagnosis into the next round's WHERE analysis. Output: a triage driving the next round.
The cycle then returns to Phase 1. The Cell Cycle's output (the triage) becomes the Fractal Cube's input
(the defect map). This is the round-to-round feedback loop.

3. Model I -- Recursive Fractal Cube (WHERE)
Mathematical basis: the Menger sponge construction, Hausdorff dimension, self-similarity, rescaled-range
analysis.
The Recursive Fractal Cube is the diagnostic foundation of the methodology. It answers WHERE defects
live by classifying every verifiable property of the artifact into one of two categories: edge (checked by a
gate) or face-interior (ungated prose in the analytical void). It answers WHERE defects come from by
identifying the recursion level at which the defect-generating process operates.

3.1 The five recursion levels
Level

Scope

Content

Generator

0

Entry-writing
process

How the producer creates
amendment entries

The producer's methodology: read
findings, write prose, compute values

1

Amendment entry

The v0.N entry text: claims,
counts, corrections

Level 0 applied to the current round's
findings

2

Corrections

Individual corrections and
their claimed substances

Level 1's description of what each
correction does

3

Register

Finding IDs, severities,
dispositions

Level 2's cross-references to specific
findings

4

Standing
properties

Boundary count, EXTERNAL
count, test count

Level 3's aggregation of dispositions
into standing state

3.2 The generator identification principle
A defect at Level N is generated by the process at Level N-1. To correct it permanently, you must
modify the generator at Level N-1, not the output at Level N. This is the central operational insight of the
fractal cube model. Patching outputs without changing the generator produces the same defect at the next
iteration -- the fractal self-similarity property.
Self-similarity diagnostic (FC-1): If the same defect class appears at Levels 1, 2, 3, and 4
simultaneously, the generator is at Level 0. No Level 1-4 patch will extinguish it. The v0.42 through v0.47
series confirmed this: every correction that fixed a narration error introduced a new narration error in its
own prose.

3.3 Edge vs face-interior classification
The Menger sponge construction removes face-center sub-cubes at every iteration, leaving a structure of
infinite surface area and zero volume -- all edges and corners, no interior. The protocol's gate structure
exhibits the same topology:
• Edge properties (gated): file digests, version stamps, tag counts, register cardinality, seal chain
integrity, manifest concordance. These are checked by build.py and produce a binary PASS/FAIL
result.

• Face-interior properties (ungated): prose narration, finding-ID attribution, correction substance
accuracy, body-repair landing verification, convergence-count provenance. These sit in the analytical
void between edge checks and are verified only by auditor inspection.
The fractal dimension of gate coverage (FC-2) measures the ratio of gated to total verifiable properties. At
v0.48, D is approximately 0.51 -- closer to a Cantor-like dust than to a surface-covering verification mesh.
Every Class A finding in the convergence series has occurred in the face-interior.

3.4 Operational probes
The fractal cube model prescribes seven probes, executed by every seat:
Probe

Name

Question

FC-1

Self-similarity test

Does the defect class recur across 3+ recursion levels?

FC-2

Fractal dimension

D = log(N_gated) / log(N_total) for the current entry. Track across
versions.

FC-3

Hurst exponent

H from the Class A series via R/S analysis. H > 0.5 = persistent
generator.

FC-4

Generator level

For each Class A: which recursion level? What Level N-1 process
produced it?

FC-5

Face-interior
enumeration

List every ungated prose claim. Count them. Compute ungated
fraction.

FC-6

Cross-topology

Map which cells are edge-checked and which are face-interior.
Connected or fragmented?

FC-7

Recursion rule diff

Did the producer modify the Level 0 rule between versions?

3.5 Methodological limitations
FC-2 counting convention. D depends on whether property classes or instances are counted. A
property-class count yields D ~ 0.79; an instance count yields D ~ 0.60 on the same artifact. The
specification must fix a convention and publish the enumeration rule so that D is comparable across seats
and versions.
FC-3 sample-size constraint. R/S estimators require approximately 50+ observations before variance
falls below the signal. At N=7 (seven audit rounds), the estimator is algebraically determined rather than
statistically informative. FC-3 should be treated as directional rather than criterial until the series reaches
sufficient length. Alternative: a simple sign test on consecutive Class A deltas, or the fraction of findings
that are recurrences.
The model's load-bearing core is the recursion-level taxonomy, the generator identification principle, and
the face-interior/edge distinction. The Menger sponge mapping, the 19-object correspondence, and the
Hausdorff dimension are illustrative but not operationally required. Strip the decorative geometry and the
model loses nothing analytically.

4. Model II -- Enzyme-Substrate System (WHAT)
Natural basis: enzyme-substrate specificity, the lock-and-key model, induced-fit catalysis.
The Enzyme-Substrate System answers WHAT kind of claim is being verified. It provides the claim
taxonomy that the Replication Fork's exonuclease (Model III) requires to operate. Without it, the
exonuclease has no way to distinguish a count-claim from a diff-claim from a provenance-claim, and
therefore cannot select the correct verification method.

4.1 The problem: undifferentiated claims
A protocol amendment entry contains claims of fundamentally different kinds. Each kind has a different
verification recipe, a different failure mode, and a different gate requirement. Treating all claims as generic
prose -- as the current [ASSERTED] tag does -- means that type-specific mismatches escape detection.
The enzyme system replaces the single [ASSERTED] tag with a typed vocabulary.

4.2 The six claim types
Type

Shape
(substrate)

Enzyme
(verification)

Example

Gate

COMPU
TED

A value derivable
by running a
command on
shipped bytes

Execute the
command, compare
output to claimed
value

"186 tests, all
GREEN"

[10e]

DIFF-VE
RIFIED

A declared
change at a
named locus
between two
versions

Diff the locus
between prior and
current version,
confirm declared
substance appears
in diff

"Section 0.1
FB-7b rationale
rewritten"

[10c]

ENUME
RATED

A count of items in
a parseable list

Parse the list, count
items, compare to
declared count

"Disclosed
standing
boundaries -- 31
items"

[10a]

PROVEN
ANCE

A finding ID's
existence,
uniqueness, and
disposition

Grep source reports
for the ID, verify
single occurrence
per ID per register,
verify disposition
consistency

"F-SC05-47-05
MEDIUM
CLOSED"

[10b]

EXTERN
AL

A fact about
events outside the
shipped packet

CANNOT be
verified from bytes;
tag honestly as
EXTERNAL

"10-seat
convergence"

None
(hone
st
tag)

COUPLE
D

A property linked
to one or more
other properties
by a structural
constraint

Enumerate the full
coupling set, verify
ALL members after
modifying ANY one

"v0.46 entry
restored"
(coupled to seal,
PRIOR_HISTO
RY, Section
22.2 count)

[10f]

4.3 Enzyme assignment protocol
Before writing the amendment entry, the producer constructs a typed claim manifest: a list of every claim
that will appear in the entry, each annotated with its type and the specific verification command that will be
used to check it.
1. Extract claims. For each sentence in the draft entry, determine whether it makes a verifiable
assertion about the artifact's bytes, its history, or external events.
2. Classify each claim into one of the six types by examining its substrate shape. If it asserts a count, it
is ENUMERATED. If it asserts a change, it is DIFF-VERIFIED. If it cites a finding ID, it is
PROVENANCE. If it depends on running a tool, it is COMPUTED. If it cannot be checked from bytes
alone, it is EXTERNAL. If modifying it would necessarily change another property, it is COUPLED.

3. Assign the enzyme. Write the specific command or check for each claim. For COMPUTED: the tool
invocation. For DIFF-VERIFIED: the two loci and the expected diff content. For ENUMERATED: the
parse target and count method. For PROVENANCE: the grep pattern and uniqueness assertion. For
COUPLED: the full dependency set.
4. Tag the claim in the entry text with its type: [COMPUTED: ], [DIFF-VERIFIED: ], [ENUMERATED: ],
[PROVENANCE: ], [EXTERNAL: ], [COUPLED: ]. These tags replace [ASSERTED].

4.4 The EXTERNAL type and honest tagging
Not all claims can be enzymatically processed. Claims about seat verdicts, convergence counts, and
events that occurred outside the shipped packet are EXTERNAL by nature. The enzyme system does not
pretend to verify them. Instead, it enforces honest tagging: an EXTERNAL claim must carry an
[EXTERNAL: ] tag that names the source (e.g., 'seat reports not shipped in this packet'). This tag is itself a
verifiable property -- an auditor can check whether the named basis exists and whether the claim could
plausibly be verified from it.
The critical discipline: a claim that is tagged [ASSERTED] when it could be tagged [COMPUTED] or
[DIFF-VERIFIED] is a methodology violation. The producer must use the most specific tag available.
[ASSERTED] survives only as a legacy compatibility marker for entries written before the enzyme system
was adopted; new entries must not use it.

4.5 Coupling sets and the helicase function
The COUPLED type requires special treatment because modifying one member of a coupling set
necessarily affects the others. The enzyme for COUPLED claims is the helicase function (borrowed from
Model III): before modifying any property, enumerate every other property coupled to it, and verify ALL
members after the modification.
Known coupling sets in the XZ Protocol:
• Entry restoration set: ENTRY_v0.N seal, HISTORY.sha256 content, PRIOR_HISTORY value,
Section 22.2 mutation count, any external anchor that holds the prior HISTORY.sha256 file.
• FB-7b rationale set: Section 0.1 paragraph, Section 25 FB-7b row, front-matter status line, v0.N entry
body-repair list.
• Version-stamp set: all 12 code files, trust-roots JSON, front-matter version line, build.py docstring,
PACKET_SHA256SUMS digests, dispatch prose claims about file identity.

5. Model III -- Replication Fork (HOW)
Natural basis: DNA replication with three proofreading layers -- polymerase fidelity, 3'-to-5' exonuclease
proofreading, and mismatch repair.
The Replication Fork governs HOW the producer builds each version. It prescribes a synthesis pipeline
with inline verification at every step, so that mismatches between claims and bytes are caught BEFORE
sealing rather than three rounds later by an audit seat.

5.1 The biological analogy
Biological
component

Protocol analogue

Function

Template strand

Body text (the actual state
of the artifact)

The authoritative source; claims must match it,
never the reverse

New strand

Amendment entry (the
producer's description of
what changed)

The synthesized product; every nucleotide
(claim) must complement the template

Polymerase

Level 0 entry-writing
process

Reads the template and synthesizes the new
strand; byte-driven = high fidelity

3'-5' exonuclease

Inline claim verifier
(enzyme from Model II)

Operates immediately behind the polymerase;
removes mismatches at point of synthesis

Helicase

Coupled-constraint
unwinder

Unwinds (enumerates) coupled properties
ahead of the polymerase so all are visible

Ligase

Seal operation (build.py +
HISTORY.sha256)

Joins fragments into a continuous strand;
operates ONLY after proofreading

Mismatch repair

Audit round (Model IV
seats)

Post-synthesis scanning for remaining errors;
operates on the completed product

Strand
discrimination

Bytes-are-authoritative
principle

When a mismatch is found, fix the CLAIM to
match the BYTES, never the reverse

5.2 The strand discrimination principle
In E. coli, mismatch repair distinguishes the template strand from the new strand by methylation status: the
template is methylated, the new strand is not yet. Errors are always corrected on the new strand. If the
system operated on the wrong strand, it would convert correct bases to incorrect ones -- mutagenesis
rather than repair.
The protocol equivalent: bytes are the template strand; claims are the new strand. When a mismatch
between a claim and the bytes is detected, the claim is corrected. Never the bytes. The v0.47 append-only
violation was literally a case of editing the template strand to match an incorrect claim -- the biological
equivalent of mismatch repair operating on the wrong strand, producing mutagenesis rather than repair.
Strand discrimination rule (non-negotiable): if a prose claim and a byte-verified property disagree, the
prose claim is wrong. No exception. The producer may not edit historical entries, sealed records, or body
text to match a claim that was written from memory. The claim is amended; the bytes are authoritative.

5.3 The six-phase build pipeline
Each version is built through six phases. The phases are strictly sequential: the output of each phase is the
input to the next. Skipping a phase or reordering them produces an unsound build.
Phase

Description

Phase 1:
Polymerase
(corrections)

Write corrections (az, ba, ...). For each correction, formulate a byte query, execute
it, write the query output. The correction layer is the first to be synthesized because
corrections are the simplest claims (short, specific, byte-checkable) and because
their substances affect the body text that subsequent phases will reference.

Phase 2:
Helicase +
Polymerase
(body repairs)

Apply body repairs. For EACH declared repair: (a) name the target locus by line
number; (b) extract the before-text from the prior version; (c) write the after-text; (d)
apply the change to the body; (e) invoke the DIFF-VERIFIED enzyme: diff the locus,
verify the declared substance appears; (f) if verification fails, REMOVE the repair
claim from the entry and retry. The helicase step: before modifying any locus,
enumerate every other property coupled to it.

Phase 3:
Polymerase +
Exonuclease
(register)

Compose the register. For each item: (a) list the finding IDs; (b) invoke the
PROVENANCE enzyme: verify each ID exists in a source report; (c) verify the ID
count equals declared convergence; (d) verify no ID appears in more than one item
with conflicting dispositions. The exonuclease step: if any check fails, remove the
item and recompose.

Phase 4:
Polymerase +
Exonuclease
(standing
properties)

Update standing properties. For each count or status claim: (a) invoke the
ENUMERATED or COMPUTED enzyme; (b) derive from bytes; (c) compare to the
declared value; (d) if mismatch, fix the declaration. This phase also handles the
COUPLED enzyme for properties in a coupling set.

Phase 5:
Ligase (seal)

Seal the entry. Run build.py (edge gates). Run the face-interior verifier [10a-f] (the
exonuclease operating post-synthesis as a final check). Compute and write
HISTORY.sha256 seals. SEAL ONLY IF BOTH PASS. A seal over unverified claims
is a seal over potential mismatches.

Phase 6:
Mismatch
repair (audit)

Dispatch to audit seats (Model IV). The seats find what the exonuclease missed.
Because the exonuclease caught the easy mismatches, seats focus on structural
issues (chain forks, coupled constraints, gate-bypass paths) rather than on phantom
repairs that a diff would have caught.

5.4 The exonuclease as inline quality gate
The critical innovation of the replication fork model is the exonuclease: a verification step that operates
DURING synthesis, immediately after each claim is written, rather than after the entire entry is sealed. The
exonuclease uses the enzyme assigned by Model II to check the claim against the bytes. If the check fails,
the claim is removed and rewritten.
This changes the error-correction dynamics fundamentally. Without the exonuclease, mismatches are
discovered by audit seats (Model IV) one round later and repaired by the producer one round after that -- a
minimum two-round latency. With the exonuclease, mismatches are caught at the point of synthesis and
never enter the sealed record.
The phantom [e] repair -- body repair declared CLOSED for three consecutive rounds while the named
locus was byte-identical across all three versions -- is the exact failure mode the exonuclease prevents. A

single diff of Section 0.1 between v0.47 and v0.48 would have revealed that the repair did not land. The
exonuclease step is that diff, applied inline before sealing.

5.5 The helicase and coupled constraints
The helicase function operates AHEAD of the polymerase, unwinding coupled constraints before the
producer modifies any property. The v0.48 chain fork is the canonical example: restoring the v0.46 entry
changes the ENTRY_v0.46 seal, which changes HISTORY.sha256, which changes PRIOR_HISTORY,
which creates a divergence from the shipped v0.47 file that every continuous seat holds. Without the
helicase step, this cascade was discovered by audit seats at R7 rather than anticipated by the producer at
build time.
The helicase protocol: before modifying property P, (1) look up P's coupling set in the registry; (2) for each
coupled property Q, record Q's current value; (3) apply the modification to P; (4) verify each Q and update
as needed; (5) if any Q creates a fork or divergence, record both values (before and after) as an
append-only correction.

6. Model IV -- Quantum Orbital (WHO)
Natural basis: atomic orbital structure, Pauli exclusion, Aufbau filling order, electron shell energy levels.
The Quantum Orbital model governs WHO audits the artifact and what anchoring each seat carries. Its two
load-bearing contributions are the continuous/fresh distinction and the multi-family deployment
requirement. Everything beyond these -- shell designations, spin states, framework rotation as structural
necessity -- is organizational overhead whose analytical return at R7 was not distinguishable from simpler
alternatives.

6.1 The two operational principles
6.1.1 Continuous vs fresh seats
Fresh seats encounter the artifact without prior context. They measure the current state cleanly,
uncontaminated by knowledge of prior rounds. Their strength: they cannot be biased by expectations
about what should have changed. Their limitation: they cannot verify cross-version claims (restorations,
append-only preservation, chain continuity).
Continuous seats carry context from prior rounds and hold prior-version bytes as external anchors. Their
strength: they can verify claims that reference prior state (e.g., 'the v0.46 entry was restored to its original
bytes'). Their limitation: they may confuse the anchor for the artifact under test -- checking their held copy
of a file rather than the shipped copy.
R7 evidence: the v0.46 restoration verification was possible only by continuous seats holding prior bytes
(C01 Opus confirmed byte-identity across 47 entries). Simultaneously, two Gemini continuous seats
confused their v0.47 anchor for the v0.48 artifact and filed a CRITICAL finding that was byte-false on the
shipped bytes. The same mechanism that enables temporal anchoring creates the anchor-artifact
confusion failure mode.
Mitigation: continuous seats must explicitly distinguish 'reading from my held file' from 'reading from the
dispatched file' in their report, and must re-read the dispatched file for every claim rather than relying on
in-context memory of it.

6.1.2 Multi-family deployment
No single model family should constitute the entire audit panel. Different families have different blind spots.
The program's standing observations:
• Gemini consumer surfaces consistently produce textual reviews rather than executing code. Their
PASS verdicts are not substrate-verified. Two Gemini seats at R7 returned CONDITIONAL PASS with
0 Class A while every other executing seat found 1+ Class A on the same bytes.
• GPT has historically been the strongest executing auditor (runs code, checks outputs, catches what
others describe). Self-disqualified from carrying at v0.6.
• Kimi K3 executes genuinely in its sandbox (confirmed by sealed-nonce challenges). Currently the only
carrying family.
• Claude/Opus is the producer family. Advisory only, non-carrying, non-binding.

6.2 Recommended deployment architecture
Based on R7 evidence, the recommended minimum deployment is 6 seats:
Coun
t

Type

Family

Role

Rationale

2

Fresh

Kimi K3 (carrying)

Binding

Clean measurement of the artifact,
unbiased by prior rounds

1

Fresh

GPT (adversarial)

Executing,
non-carrying

Strongest code-execution capability for
build-tool attacks

1

Continuo
us

Kimi K3 (carrying)

Binding +
anchor

Cross-version verification, restoration
confirmation

1

Continuo
us

Opus 5 (advisory)

Non-carrying +
anchor

Deepest analytical reports; holds prior
bytes

1

Fresh

Gemini or other

Adversarial

Second-family coverage; findings
recorded even if execution unverified

6.3 Framework rotation: flavor, not structure
The four analytical frameworks (GAN Convergence, Fractal/Hurst, Structural Revelation,
Differentiator/Pharmacological) produce different language for describing findings but did not produce
different findings at R7. The phantom [e] repair was identified by seats using every framework. Framework
rotation is retained as analytical diversity -- different lenses may surface different insights on different
artifacts -- but is downgraded from a structural requirement to an optional enrichment.
The Recursive Fractal Cube probes (FC-1 through FC-7) remain required for all seats as the common
diagnostic baseline. Framework-specific probes are assigned per seat and executed in addition to the FC
probes, not instead of them.

7. Model V -- Cell Cycle Checkpoint (WHEN)
Natural basis: the eukaryotic cell cycle (G1/S/G2/M phases), checkpoint-mediated arrest, tumor
suppressor regulation, and checkpoint adaptation in cancer biology.
The Cell Cycle Checkpoint model governs WHEN defects should be caught and how chronic defects
escalate across rounds. It is the outermost governance loop, consuming findings from all other models and
feeding the diagnostic for the next round.

7.1 The four phases within a round
Phase

Cell cycle
analogue

Protocol operation

Checkpoint condition

G1
(Gap 1)

Cell assesses
growth signals

Diagnosis: analyze prior-round
triage, classify findings by
recursion level, assess chronic
status

All prior-round findings
dispositioned. Any 3-round
chronic defect triggers
structural-fix protocol

S (Synt
hesis)

DNA replication

Build: Phases 1-4 of the
Replication Fork (corrections,
body repairs, register, standing
properties)

Exonuclease passes on every
claim. No DIFF-VERIFIED claim
without a matching diff

G2
(Gap 2)

Cell checks
replication product

Verification: build.py +
face-interior verifier [10a-f] +
COUPLED constraint sweep

BUILD PASSED. Face-interior
verifier [10a-f] PASSED. All
COUPLED sets verified

M (Mito
sis)

Cell divides

Dispatch: deploy to audit seats
per the Orbital model

All G2 checks passed. Claim
manifest ships with the dispatch

The checkpoints are hard gates: the cycle does not proceed past a checkpoint unless the condition is met.
A build that fails the G2 face-interior verifier is not dispatched. A round whose G1 chronic-defect check
fires must apply the structural-fix protocol before entering S.

7.2 Checkpoint adaptation and the chronic defect protocol
In cancer biology, checkpoint adaptation occurs when a cell sits at a checkpoint too long with
unresolvable damage. The cell eventually overrides the checkpoint and proceeds, carrying the damage
forward. This is how tumors accumulate mutations.
The protocol's analogue: the phantom [e] repair. The audit checkpoint (mismatch repair) fires correctly
every round. The producer acknowledges the finding. Then the producer proceeds to the next version with
a CLOSED disposition that is byte-false -- overriding the checkpoint. The damage carries forward. Three
rounds of adaptation.
The chronic defect protocol prevents checkpoint adaptation:

7.2.1 Trigger condition
A finding is CHRONIC if it persists across 3 consecutive rounds at the same locus. Persistence means:
the finding was raised by an auditor, the producer declared it CLOSED, and a subsequent auditor re-raised
it on the same or equivalent bytes.

7.2.2 Automatic consequences
When a finding reaches CHRONIC status, three consequences trigger automatically:
1. Repair pathway change. The locus gets a STRUCTURAL FIX rather than another body repair.
Either the locus is eliminated (e.g., Section 0.1 rationale replaced with a pointer to Section 25,
creating a single source of truth), or a new gate is added that mechanically enforces the property.
The producer does not get a fourth attempt at the same repair.
2. Producer CLOSED exemption. The finding can only be closed by a carrying seat confirming the
structural fix landed on bytes. The producer's CLOSED declaration for this finding is void -analogous to a tumor suppressor that can no longer be overridden by the cell's own signals.
3. Persistence chain recording. The entry must record the full persistence chain: 'This finding was
filed at Rn (F-XXX), falsely closed at Rn+1 (register item Y), re-raised (F-YYY), falsely closed at
Rn+2, re-raised (F-ZZZ). Chronic status: STRUCTURAL FIX REQUIRED.' This chain is itself a
PROVENANCE-type claim subject to enzymatic verification.

7.3 Inter-round feedback: the cell cycle as the outermost loop
The Cell Cycle model wraps around all four other models. At the end of each round, it:
• Receives the triage (output of Model IV's mismatch repair)
• Updates the chronic-defect registry
• Computes the Hurst-like persistence metric (fraction of findings that are recurrences)
• Checks for structural-fix triggers
• Feeds the updated defect map into Model I (Fractal Cube) for the next round's WHERE analysis
This feedback loop is the mechanism by which the methodology learns across rounds. Without it, each
round treats every finding as novel, even if it is the seventh recurrence of the same defect at the same
locus.

7.4 The WATCHED locus mechanism
Any locus that has been the site of a Class A finding is marked WATCHED. WATCHED loci receive
automatic re-verification at the G2 checkpoint of every subsequent round, even if no finding was raised
against them in the current round. A WATCHED locus is never un-watched; it can only be eliminated (by
the structural-fix protocol) or permanently gated (by a new build.py check that mechanically verifies the
property).
WATCHED loci at the end of R7: Section 0.1 FB-7b rationale (3-round chronic); PRIOR_HISTORY
derivation (chain fork class); register finding-ID uniqueness (duplicate disposition class); dispatch code-file
identity claims (2-round stale-claim class).

8. The Composed Architecture
8.1 The five models as a single pipeline
The five models are not five separate methodologies applied in parallel. They are five stages of a single
pipeline, where each stage's output is the next stage's input. The pipeline operates at two timescales:
within a round (Phases 1-5 of Section 2.3) and across rounds (the Cell Cycle feedback loop).

8.1.1 Within a round
Fractal Cube (WHERE) diagnoses the prior round's findings and produces a defect map. The Enzyme
System (WHAT) classifies each claim in the new entry and assigns verification methods. The Replication
Fork (HOW) builds the entry with inline verification using those methods. The Orbital (WHO) deploys the
artifact to appropriately selected seats. The seats return findings. The Cell Cycle (WHEN) triages the
findings, updates the chronic registry, and feeds the next round's diagnosis.

8.1.2 Across rounds
The Cell Cycle's output (the triage with chronic status and WATCHED loci) becomes the Fractal Cube's
input (which cells to examine, which recursion levels to probe). Over multiple rounds, the WATCHED locus
list grows, the chronic registry accumulates, and structural fixes replace repeated body repairs. The
pipeline converges when no new Class A findings are produced and no chronic defects remain un-fixed.

8.2 Convergence criterion
The methodology defines convergence as the conjunction of four conditions:
1. Zero Class A findings from at least 2 non-producer carrying seats of different families (the
FB-7b/FB-8 exit condition).
2. Zero CHRONIC defects in the chronic registry (all have received structural fixes confirmed by
carrying seats).
3. All WATCHED loci either eliminated or permanently gated.
4. Recurrence fraction below threshold: fewer than 20% of the current round's findings are
recurrences of prior-round findings at the same locus. (This replaces the under-specified Hurst
criterion with a directly measurable metric.)

8.3 The v0.48 test case
Applied retrospectively to v0.48 R7:
• Fractal Cube: correctly diagnosed the partial Level 0 intervention (corrections byte-driven,
body-repairs memory-driven). FC-1 correctly identified the generator at Level 0.
• Enzyme System: would have classified body repair [e] as DIFF-VERIFIED and assigned the diff
enzyme. The enzyme would have reported: locus unchanged.
• Replication Fork: the exonuclease at Phase 2 would have caught the phantom [e] before sealing.
The helicase at Phase 2 would have enumerated the PRIOR_HISTORY coupling set before restoring
the v0.46 entry.

• Orbital: correctly deployed continuous seats that verified the v0.46 restoration. Also demonstrated the
anchor-artifact confusion failure mode (Gemini continuous seats).
• Cell Cycle: would have flagged the Section 0.1 FB-7b rationale as CHRONIC (3 consecutive rounds)
and triggered the structural-fix protocol, preventing a fourth false closure.
Under this methodology, v0.48's two highest-convergence findings (phantom [e] and chain fork) would
have been caught before dispatch. The remaining findings (duplicate register ID, dispatch code-file claim,
mutation count, date mismatch) are lower-severity items that the face-interior verifier [10a-b] and the
COUPLED enzyme would likely have caught at G2.

9. Operational Annexes
9.1 Claim manifest template
Each entry ships a claim manifest. Example for a hypothetical v0.49 entry:
#

Claim text

Type

Enzyme

Result

1

186 tests, all GREEN

COMPUTE
D

pytest + wc

2

Section 0.1 FB-7b rationale
replaced with pointer

DIFF-VERI
FIED

diff line 18 v0.48 vs
v0.49

3

31 standing boundaries

ENUMERA
TED

parse + count

4

F-SC01-48-01 CLOSED via
structural fix

PROVENA
NCE

grep source reports +
dedup

5

PRIOR_HISTORY 629b...

COUPLED

helicase: check seal
chain + prior file

6

9-seat convergence

EXTERNA
L

seat reports (not
shipped)

The Result column is filled by the exonuclease during synthesis and verified by auditors during mismatch
repair.

9.2 Chronic defect registry template
Locus

Finding chain

Rounds

Status

Structural fix

Section 0.1
FB-7b rationale

F-S01-46-05 ->
F-SC01-47-04 ->
F-SC01-48-01

R5-R6-R
7 (3)

CHRONI
C

Replace with pointer to
Section 25 row (single source
of truth)

Register F-ID
uniqueness

F-SC05-47-05 dup at
R7

R7 (1)

WATCH
ED

Pending: [10b] dedup gate in
build.py

Dispatch
code-file identity

R6 stale digest -> R7
false byte-identical
claim

R6-R7
(2)

WATCH
ED

Pending: manifest-diff-based
claim generation

9.3 Coupling set registry
The producer maintains a registry of known coupling sets. Before modifying any property, the helicase
function consults this registry.
Set name
Entry
restoration

Members

Trigger condition

ENTRY_v0.N seal, HISTORY.sha256,
PRIOR_HISTORY, Section 22.2 mutation count,
external anchors holding prior HISTORY file

Any modification to a
historical amendment entry

Set name

Members

Trigger condition

FB-7b
rationale

Section 0.1 paragraph, Section 25 FB-7b row,
front-matter status line

Any change to FB-7b status
or rationale

Version stamp

12 code files, trust-roots JSON, front-matter
version line, build.py docstring,
PACKET_SHA256SUMS, dispatch claims about
file identity

Any version increment

Boundary list

Boundary list items, declared count, [ASSERTED]
tag

Any addition, removal, or
rewording of a boundary

9.4 Face-interior verifier specification
The face-interior verifier implements six sub-checks corresponding to the six claim types. It runs at the G2
checkpoint, after build.py (edge gates) and before sealing.
Gate

Claim type

Check

Catches

[10a]

ENUMERAT
ED

For each (count, noun) pair in the
entry, derive count from bytes

Boundary count errors, register
undercount

[10b]

PROVENAN
CE

For each F-XXX-NN in the register,
verify existence + uniqueness +
disposition consistency

Duplicate finding IDs, dropped
findings, conflicting dispositions

[10c]

DIFF-VERIFI
ED

For each body repair, diff the named
locus and verify the declared
substance appears

Phantom repairs, false CLOSED
dispositions

[10d]

COUPLED

For each member of each coupling
set, verify consistency after
modifications

Chain forks, locus splits, stale
counts

[10e]

COMPUTED

For each tool-derivable claim, re-run
the tool and compare

Stale test counts, wrong manifest
digests

[10f]

EXTERNAL

Verify every EXTERNAL claim
carries an [EXTERNAL: basis] tag

Untagged assertions about
unverifiable events

This methodology is a living document. Its own prose claims are subject to the same enzyme-substrate verification it
prescribes: if this document narrates from memory what the protocol contains, it has reproduced the defect class it
was designed to extinguish. Every factual claim about the XZ Protocol audit series in this document was verified
against the shipped v0.48 bytes and the R7 cross-seat triage before inclusion.

End of Unified Structural Audit Methodology v1.0.



Bismillah ir-Rahman ir-Rahim
