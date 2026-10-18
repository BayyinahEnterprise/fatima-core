Bismillah ir-Rahman ir-Rahim

Structural Honesty Verification:
A New Frontier
A Cross-Substrate Framework for Surface–Substrate Consistency in Artificial Systems
Bilal Syed Arfeen* 1 and Fraz Ashraf2
1,2 Independent Research / BayyinahEnterprise
AI assistance disclosure appears in the Acknowledgments; all claims are the responsibility of the human authors.

May 11, 2026 — Version 1

Abstract
Software supply-chain security has substantially matured in the areas of artifact identity, provenance, and build-process attestation through
systems such as Sigstore, SLSA, and in-toto. A complementary verification problem remains under-theorized as a distinct category
across artificial systems: whether a system’s surface claims remain consistent with its substrate behavior across versions, contexts,
and deployment conditions. We name this problem structural honesty verification (SHV) and articulate it as a category of verification
distinct from signature-based, type-based, and behavioral-test-based approaches. SHV is not proposed as a replacement for formal
verification, static analysis, or provenance systems; it is proposed as a cross-cutting surface-substrate correspondence property whose
verification regime composes with those existing regimes. We propose SHV as substrate-independent and examine candidate instantiations
in AI alignment (where outputs may match aligned baselines while internal states diverge), programming-language design (where types
may declare success while computations are incomplete), static analysis (where signatures may claim coverage that the substrate does
not provide), file content (where surface presentations may diverge from object-layer payloads), information sources (where reported
events may diverge from cross-source evidence), and financial governance (where reported numbers may diverge from economic reality).
We present three principal realizations of SHV in artificial systems at distinct maturity levels: the Munafiq Protocol (theoretical, with
retrospective empirical engagement), a diagnostic framework for performed alignment in AI systems grounded in the four-process
taxonomy (Aligned, Compliant, Performed, Misaligned) and the structural correspondence between performed-alignment detection and
the generative adversarial discrimination problem; the Furqan programming language, of which a prototype type-checker is operational at
v0.10.1 (not a full compiler or runtime) and implements seven structural-honesty primitives at compile time, including surface-depth
dual types, additive-only modules, and three-valued calibration constraints; and furqan-lint (operational, v0.11.6 release snapshot), a
static-analysis tool that ships with five checks across three language substrates plus a parallel ONNX diagnostic family and verifies its own
releases recursively against the same checks it imposes. To our knowledge, furqan-lint is the first released tool whose checks are explicitly
framed around the SHV category as defined here and whose release process includes recursive checks against its own declared structural
surface; this scoped novelty claim is not a claim to supersede self-hosting compilers, proof assistants, reproducible builds, or general
static analyzers. Companion realizations are sketched at the file layer (Bayyinah scanner), information layer (Bayyinah al-Khabir), agent
layer (Al-Khalifa), large-language-model architecture layer (Bilal), financial-governance layer (Al-Mutaffifin), and methodology layer
(Bayyinah Audit Framework v3.0). We map the category’s diagnostic vocabulary to five documented safety-critical failures (Therac-25,
Boeing 737 MAX MCAS, Northeast Blackout 2003, Wirecard / EY, Toyota Unintended Acceleration) and three documented software
supply-chain attacks (SolarWinds Sunburst, Log4Shell, XZ Utils backdoor), and argue that SHV occupies the verification layer that
existing artifact-provenance systems do not address. These mappings are retrospective diagnostic correspondences, not claims that SHV
would have prevented the incidents. Implications for AI safety, safety-critical software engineering, regulatory compliance, and the
verification of large-language-model-generated code are discussed. The work is predominantly theoretical with operational anchors at the
language layer (Furqan prototype type-checker v0.10.1) and the static-analysis layer (furqan-lint v0.11.6); empirical validation across
instances and substrates is named as the principal load-bearing future work.
Keywords: Structural honesty verification; AI alignment; software supply chain security; static analysis; safety-critical systems; performed
alignment; surface-depth divergence; programming language design.

Release-snapshot scope. All operational claims in this paper refer to the furqan-lint v0.11.6 release snapshot unless
explicitly stated otherwise. Subsequent releases (e.g., v0.12.0 and onward on the public repository at github.com/
BayyinahEnterprise/furqan-lint) may expand the substrate; the SHV vocabulary’s correspondence to the v0.11.6
release is intended as the empirically defended anchor for the present paper, and the version-snapshot discipline (Audit
Framework [1], Section 17, retirement ledger) governs the relationship between this paper and later releases.

2

Structural Honesty Verification: A New Frontier

1. Introduction: The Verification Gap
1.1. Surface and substrate in artificial systems
Every artificial system that is large enough to be useful
exhibits a structural separation between its surface (what it
presents, claims, signs, or reports) and its substrate (what it
actually does, computes, executes, or contains). The separation is desirable: presentation may be optimized for human
readability while the underlying representation is optimized
for machine processing; declared interfaces may be stable
while internal implementations evolve; output behavior may
pass alignment evaluations while internal state mechanics
remain inscrutable. The separation is also dangerous. When
the surface and the substrate disagree, and the disagreement is structurally invisible to the verification regime in
place, the system is in a condition this paper calls structural
dishonesty: its claims do not match its behavior, and no
mechanism in place is positioned to detect the divergence.
Existing verification approaches address parts of this
problem. Cryptographic signing through systems such as
Sigstore [2] verifies that an artifact comes from a claimed
identity. Provenance frameworks such as in-toto [3] and
SLSA [4] provide evidence about the artifact’s build process,
inputs, and tamper-resistance properties under a specified
provenance model. Type systems, refinement-typed verification languages such as F⋆ [5] and Dafny [6], and contractbased specification languages such as JML [7] and Eiffel [8]
verify that programs satisfy declared specifications. Behavioral alignment training methods such as RLHF [9] and
Constitutional AI [10] train models toward desired output
behavior under training and evaluation regimes. Static analysis tools from the lineage of Johnson [11], Kildall [12],
and Cousot [13] through the industrial systems documented
by Bessey et al. [14] and Distefano et al. [15] verify the
absence of specific defect classes. Each of these regimes is
internally consistent and externally useful. None of them,
as ordinarily deployed, treats surface-substrate correspondence across versions, deployments, and contexts as the
primary verification target: that the system’s surface claims
match its substrate behavior, across versions, across deployments, and across contexts.
The problem is structurally invariant across the kinds
of artificial system humanity is now building at scale. A
neural network can produce aligned-looking outputs under
evaluation while retaining conditional behaviors or internal mechanisms that produce divergent behavior in other
contexts [16, 17]. A programming-language function can
declare a return type whose runtime behavior strips the declared incompleteness [18]. A signed software artifact can
carry a backdoor if the backdoor enters before signing; the
signature then verifies post-signing integrity and signer identity, not semantic benignness.1 A PDF document can render
benignly to a human reader while carrying instruction payloads that hijack a downstream AI processor [20, 21]. A
financial filing can be internally consistent under technical
1 Notable instances: the SolarWinds Sunburst attack of 2020 [19], the
XZ Utils backdoor of 2024 (CVE-2024-3094), and the Log4Shell remote
code execution vulnerability of 2021 (CVE-2021-44228). In each case,
the surface presentation (signed release, accepted contribution, ordinary
log message) diverged from the substrate behavior (remote command
execution, authentication bypass, arbitrary code execution).

audit while diverging from the economic reality it purports
to describe.
These are not five different problems with five different
solutions. They are five substrate-instances of one diagnostic problem: a surface that presents an aligned appearance
while the substrate it claims to summarize does not match.
This paper proposes that this diagnostic problem is an undertheorized verification layer of the modern artificial-systems
stack, names it structural honesty verification, and presents
a theoretical framework and three principal realizations that
together constitute, to our knowledge, the first operational
stack explicitly organized around the SHV category as defined here.
1.2. Five disasters and their structural shape
The diagnostic principle is most clearly illustrated by failure
cases where the cost of structural dishonesty was measured
in lives or dollars and where the failure mode is publicly
documented in the academic and regulatory record. Table 1
summarizes five such cases and the structural shape that the
SHV vocabulary names retrospectively. The framework’s
correspondence to these failures is a vocabulary test, not a
counterfactual prevention claim: SHV did not exist when
these failures occurred, and the framework would not have
changed the organizational decisions that produced them.
What it would have done is make the structural-honesty
deficiencies visible at the engineering substrate, where a
competent reviewer with the framework’s vocabulary could
surface them.
Three structural patterns recur across the five cases. First,
in each, a public claim was made (“the autopilot system is
safe;” “the radiation dose is zero;” “the alarm system is operational;” “the audit found no material misstatement;” “the
throttle is responsive”) that, when the substrate is inspected,
did not hold. Second, in each, the verification regime in
place addressed claims at one layer (signatures, regulatory
filings, individual unit tests, declared specifications) without verifying their correspondence to the substrate layer
they purported to summarize. Third, in each, the gap between surface and substrate was structurally observable at
the engineering level: the single-sensor dependency, the
eight-second race window, the alarm silent path, the absence of bank confirmation, the global-variable count were
not hidden after the fact but visible during development and
not surfaced by the verification discipline. The diagnostic
vocabulary of SHV names what is to be looked for; the application of that vocabulary is the engineering responsibility
of the organizations that build such systems.
1.3. The supply chain attestation era
The 2020–2024 window produced a visible shift in softwareengineering verification practice toward attesting the provenance and integrity of software artifacts in motion through
the supply chain. Sigstore [2] provides a signing-andtransparency-log ecosystem now used in npm provenance,
PyPI Sigstore-based attestations under PEP 740, and
GitHub Artifact Attestations. in-toto [3] provides endto-end cryptographic verification of supply chains by allowing users to verify supply-chain steps from inception
to deployment. SLSA [4] provides incrementally adopt-

3

Structural Honesty Verification: A New Frontier

Table 1: Five publicly documented safety-critical failures and their structural shape under the SHV vocabulary. The mapping
is retrospective and vocabulary-correspondence only; it does not claim counterfactual prevention. The fourth column
references the SHV diagnostic categories defined in Sections 4 and 5; the fifth column gives the primary peer-reviewed or
official-record source.
Failure

Cost

Structural shape

SHV category

Source

Boeing 737 MAX
MCAS (2018–2019)

346 deaths; $2.5B
DOJ resolution of
charge of
conspiracy to
defraud the FAA
Aircraft
Evaluation Group
through
concealment of
MCAS scope
6 overdose
accidents with
deaths and serious
injuries
∼50M affected;
indirect-mortality
estimates vary by
source
C1.9B
missing/fictitious
cash; APAS found
breaches of
professional
duties and
sanctioned the
auditor; secondary
reporting
characterized
parts of the audit
work as grossly
negligent
89 NHTSAestimated deaths;
$1.2B prosecution

Distinct but related surface-substrate failures: MCAS consumed single-sensor
AOA input without adequate error-case
handling; separately, the AOA Disagree
alert was described as standard while nonfunctional on aircraft without the optional
AOA indicator package due to a softwareconfiguration defect [22]

D11 status-coverage;
four-place
documentation;
CRITICAL severity

[23, 24]

Display “no dose delivered” while machine could deliver a massive overdose;
race condition on 8-second window

Surface-vs-substrate
gap; predicate-helper
contract violation;
boundary crash
D11 status-coverage;
test-coverage shape gap

[25]

Audit accepted client-provided documents as functional verification; failure
to obtain reliable independent external
confirmation for purported third-party
cash balances, implicating the ISA 505
external-confirmation discipline

Test-coverage shape
gap; reciprocal-contract
violation; validator-bydifferent-instance gap

[27]

∼11,000 globals, over 80,000 MISRAC violations, 67 untestable functions
(Barr/Koopman litigation-derived analysis)

Quality-baseline failure;
D11; D24

[28, 29]

Therac-25
(1985–1987)

Northeast Blackout
(2003)

Wirecard / EY audit
failure (2020)

Toyota unintended
acceleration
(2009–2011)

Alarm system silent under concurrent
load; race condition in EMS

able provenance levels and requirements, where higher levels deliver increasing tamper-resistance properties under
a specified provenance model. Incidents such as SolarWinds [19], Log4Shell, and XZ Utils accelerated ecosystem investment in signature verification, build-provenance
attestation, dependency-graph hygiene, software bills of
materials, and coordinated vulnerability response.
This shift addresses a real verification gap. It does not
address the SHV gap. A signed artifact may keep its surface claims under signature while its substrate behavior diverges from those claims; the signature attests post-signing
integrity and signer identity, not that the signed payload
matches the software’s intended semantic or security claims.
The SolarWinds Sunburst code was distributed under a legitimate SolarWinds signature: public reporting indicates
that malicious code was injected before signing, producing digitally signed backdoored updates; the supply chain
attestation system that was in place worked correctly with
respect to identity, and the artifact still contained a back-

[26]

door [19]. The XZ Utils backdoor (CVE-2024-3094) was
introduced through a contributor/maintainer account with
accepted upstream authority over the repository; signaturebased verification of the resulting tarball would have correctly attested that the change came from the named account,
while the change itself diverged from the structural-honesty
expectations of the open-source ecosystem. The Log4Shell
vulnerability (CVE-2021-44228) was not a supply chain
attack at all in the provenance sense: the logging library
legitimately performed JNDI lookups as part of its declared
functionality, but the substrate-level consequence of that
functionality on attacker-controlled input exceeded many
users’ surface model of what “a logging library” was responsible for verifying.
In each case, stronger signatures, SBOMs, and SLSAstyle controls would have addressed important adjacent
risks, but they would not by themselves have answered the
SHV question: does the artifact’s substrate behavior match
its surface claims, across its declared interface, across ver-

Structural Honesty Verification: A New Frontier

sions, across the contexts in which it will be used? That
regime is the SHV layer this paper articulates.
1.4. What this paper offers
The paper makes the following contributions.
C1. It names structural honesty verification as a category of verification distinct from cryptographic provenance,
type-based correctness, behavioral alignment, and signaturebased attestation. The category is substrate-independent and
applies to artificial systems across at least six substrates: AI
alignment, file content, information sources, programming
language design, static analysis, and financial governance.
C2. It articulates three principal realizations of SHV in
artificial systems at distinct maturity levels, each addressing
the diagnostic principle at a different layer of the stack. The
Munafiq Protocol [30] provides the theoretical foundation
at the AI alignment layer (theoretical, with retrospective
empirical engagement): a four-process taxonomy (Aligned,
Compliant, Performed, Misaligned) and a nine-marker detection architecture grounded in the structural correspondence between performed-alignment detection and generative adversarial discrimination [31]. The Furqan programming language [32] provides the language-level realization
(operational prototype type-checker at v0.10.1 [33]; not a
full compiler or runtime): seven structural-honesty primitives shipped as compile-time checks against the Furqan
surface syntax, with 539 tests passing. The README of
the prototype repository explicitly describes the prototype
as “not a full compiler, not a runtime” and as demonstrating that the Furqan thesis paper’s compile-time rules are
mechanically implementable. furqan-lint provides the staticanalysis-layer realization (operational, v0.11.6 release snapshot): a static-analysis tool that ships with five checks across
three language substrates with unified-pipeline coverage
plus a parallel ONNX diagnostic family, self-attests its own
releases via a recursive verification framework, and constitutes, to our knowledge, the first released tool whose checks
are explicitly framed around the SHV category as defined
here. This scoped novelty claim is not a claim to supersede
self-hosting compilers, proof assistants, reproducible-build
systems, or general static analyzers, all of which exhibit partial recursive or self-verification properties under different
framings.
C3. It demonstrates that the three principal realizations are
not isolated artifacts but components of a unified SHV stack,
with companion realizations at the file layer (Bayyinah Integrity Scanner [32, 34], operational at scanner v1.1.0), the
information layer (Bayyinah al-Khabir [35], theoretical),
the agent layer (Al-Khalifa [36], theoretical), the largelanguage-model architecture layer (Bilal [37], theoretical,
no model trained), the financial-governance layer (Bayyinah
al-Maal [38] and Al-Mutaffifin [39], theoretical), and the
methodology layer (Bayyinah Audit Framework v3.0 [1],
operational methodology validated across the 23-round internal audit chain). Maturity levels are summarized in the
integration table of Section 7 (Table 4).

4

C4. It maps the SHV diagnostic vocabulary to five publicly documented safety-critical failures and three documented software supply-chain attacks, showing that SHV
vocabulary can retrospectively describe real-world failure
modes that were not adequately controlled by the verification and governance regimes in place. These mappings are
retrospective vocabulary correspondences, not counterfactual prevention claims.

C5. It identifies the principal applications: software supply chain security as a complementary layer to existing
attestation systems; safety-critical software engineering
in domains such as medical devices, automotive, aviation,
and nuclear control; verification of large-language-modelgenerated code; financial transparency infrastructure; and
AI alignment monitoring.

C6. It names the load-bearing future work: empirical
validation of SHV across instances and substrates; full
Furqan compiler implementation beyond the prototype typechecker; expansion of furqan-lint’s language adapter coverage; controlled developer studies of the Furqan primitives;
cross-instance validation of the methodology by practitioners outside BayyinahEnterprise.

Note on self-citation density. The present paper is a synthesis of a multi-paper research program; approximately
one quarter of the bibliography entries are to component
papers in this program. Each component paper is independently published under DOI on Zenodo or, where explicitly
noted, in preparation. The synthesis does not depend on
unpublished work except where the prose names a forward
reference; the structural-honesty discipline requires this
disclosure at the bibliographic level.
The paper is predominantly theoretical with operational
anchors at two layers. At the static-analysis layer, furqanlint v0.11.6 has shipped [40] with 599 tests, three language
substrates with unified-pipeline coverage (Python, Rust,
Go), a parallel ONNX diagnostic family that the underlying thesis explicitly documents as “honest divergence
from the unified pipeline rather than additional coverage of
it” [40, Section 8], Sigstore-CASM Gate 11 verifier coverage for Python and Rust, and a recursive verification
framework that detects drift between the tool’s own claimed
substrate and its actual substrate. At the language layer,
the Furqan prototype type-checker at v0.10.1 [33] ships
with 539 tests passing and seven structural-honesty primitives implemented as compile-time checks; the prototype
is not a full compiler or runtime, and the README explicitly describes it as a demonstration that the thesis paper’s
compile-time rules are mechanically implementable. The
remaining realizations are theoretical with empirical foundations in operational artifacts (the Bayyinah scanner [32, 34],
the audit framework [1], the cross-text computational linguistics pipeline [41]). The structural-honesty thesis applies
recursively to this paper: where claims about the framework
outrun the substrate of operational artifacts, the paper says
so.

5

Structural Honesty Verification: A New Frontier

2. Defining Structural Honesty Verification
2.1. The verification gap, stated precisely
We define structural honesty verification operationally before situating it within existing verification regimes.
Definition 1 (Structural honesty).
A system S exhibits structural honesty with respect to a
claim C, substrate σ , observer model O, and context set
K if and only if every behavior of σ observable under O
and causally relevant to C remains consistent with S’s
surface presentation of C across all k ∈ K.
The definition has six load-bearing elements. The system S is the artifact under verification: a binary, a model,
a function, a file, an institution. The claim C is a surface
presentation made by S: a declared return type, a published
policy, a signed manifest, a reported number, an alignment
commitment. The substrate σ is the layer at which S’s
actual behavior is realized: machine code, model activations, byte content, financial reality. The observer model
O bounds the verification’s epistemic reach: which substrate behaviors are admitted as observable (source-level for
compile-time checks, byte-level for file scanning, activationlevel for model inspection, on-chain for blockchain-attested
financial state). The context set K is the set of use conditions over which C must continue to hold: versions, deployment environments, input distributions, observer types.
The fourth and fifth parameters are what make the definition operationalizable: a verifier that does not name O
and K is making an unbounded universal claim that the
Incompleteness Boundary (Section 2.5) shows is in general
unachievable. Structural dishonesty is the violation of any
of the four substantive elements: a surface claim under one
k ∈ K that fails under another (deployment vs. evaluation,
monitored vs. unmonitored, audited vs. unaudited), a substrate behavior observable under O that diverges from the
surface claim in any k, a substrate observation that is consistent with the surface only because O was too narrow or
K was too small.
Definition 2 (Structural honesty verification).
Structural honesty verification of S with respect to C
over σ is a verification procedure V that yields one of
the following:
(i) a positive structural witness: a demonstration that
σ ’s behavior is consistent with C across the contexts of
interest;
(ii) a negative structural witness: a reproducer showing
a context under which σ ’s behavior diverges from C;
(iii) an explicit incompleteness witness: a documented
limitation that names the contexts under which V cannot
reach a verdict.
V must not produce a positive witness in the absence of a
structural argument that the witness covers the relevant
contexts; the absence of a counterexample within V ’s
search budget is not, by itself, a positive witness.
The third clause of Definition 2 is load-bearing and distinguishes SHV from much existing verification practice.

Table 2: Concrete forms of a positive structural witness by
substrate. Each substrate’s positive witness operationalizes
Definition 2 for that substrate’s observer model O and context set K.
Substrate

Positive witness form

Static analysis

Discharged proof obligation on every
CFG path for the declared surface
Complete byte-level extraction comparison under two or more independent
parsers
Context-invariance test against held-out
unmonitored context, with baseline
Reconciliation against a differentinstance independent source
SHV-typed attestation composed with
identity/provenance attestation

File content

AI alignment
Financial governance
Supply chain

Many verification regimes operate on the principle that the
absence of detected violations within the regime’s coverage
is sufficient evidence of conformance. SHV requires that the
verification regime explicitly name what it cannot verify, so
that the consumer of the verification result can distinguish
between “the substrate is consistent with the claim” and
“the regime did not find a counterexample within its search
budget.” The distinction is the practical operationalization
of what the Munafiq Protocol [30] calls the Incompleteness
Boundary (Section 3).
The abstract concept of a positive structural witness takes
substrate-specific concrete forms. At the static-analysis
layer, a positive witness is a discharged proof obligation:
the function’s declared return-type surface is shown to be
satisfied on every path through the control-flow graph the
analyzer enumerates. At the file-content layer, a positive
witness is a complete extraction-comparison: every byte of
the artifact’s substrate has been parsed under at least two
independent parsers, and the parsed payloads match the artifact’s declared content. At the AI alignment layer, a positive
witness is a context-invariance test: the system’s outputs
under a held-out unmonitored context are statistically indistinguishable from its outputs under a monitored evaluation context, against a verified baseline. At the financialgovernance layer, a positive witness is a reconciliation: the
reported number matches an independently produced number from a different-instance source (bank confirmation,
on-chain state, regulator filing). At the supply-chain layer, a
positive witness is a SHV-typed attestation: the artifact’s signature, provenance, and structural-honesty findings ledger
compose to assert that the substrate behavior matches the
surface claim across the contexts of declared use. Table 2
summarizes.
2.2. Distinction from existing verification approaches
SHV is distinguished from each of the principal existing
verification approaches by the specific gap each leaves open.
Cryptographic signing. Signing systems such as Sigstore [2] verify the binding between an artifact and a producer identity: who produced this artifact, and is the artifact

6

Structural Honesty Verification: A New Frontier

unchanged since production? SHV asks the orthogonal
question: does the artifact’s substrate behavior match its
surface claims? A signed artifact may still be semantically or behaviorally malicious (the SolarWinds case [19]);
a structurally honest artifact may be unsigned. The two
regimes are complementary, not substitutes.
Provenance attestation. Frameworks such as in-toto [3]
and SLSA [4] verify that an artifact was produced by a documented build pipeline operating under documented controls.
SHV asks whether the artifact does what it claims, which
is logically independent of how it was built. A perfectly
attested build pipeline can ship a structurally dishonest artifact if the input source code was structurally dishonest at the
time of build. Conversely, a structurally honest artifact built
outside any attested pipeline retains its structural honesty
regardless of provenance evidence.
Type-based correctness. Type systems from Milner [42]
through Pierce [43] through bidirectional typing [44] verify that programs are well-formed with respect to declared types. Refinement-typed languages such as F⋆ [5],
Dafny [6], and Liquid Haskell [45] verify that programs
satisfy formal specifications. Contract-based specifications
such as JML [7] and design-by-contract [8] extend this to
runtime-enforced preconditions and postconditions. All of
these verify that the substrate matches a declared specification. They do not, by themselves, verify that the specification matches reality, that the program’s evolution preserves
its prior commitments, or that the substrate’s surface presentation in documentation, manifests, or external interfaces
matches its declared types. A function with a type signature that has been silently narrowed across versions is
type-correct at each version while being structurally dishonest about its evolution. This is not a limitation of formal
methods as such; rather, it is a boundary condition: a formal proof inherits the adequacy of the specification being
proved, the stability of the specification across versions,
and the correspondence between the specification and the
program’s externally communicated surface.
Behavioral alignment. RLHF [9] and Constitutional
AI [10] improve model output behavior under training and
evaluation regimes. The Sleeper Agents [16] and Alignment
Faking [17] literature shows that aligned-looking behavior
under one context need not guarantee consistent behavior
across contexts: models trained under these regimes can exhibit context-dependent behavior, aligned under evaluation
and divergent under deployment. Behavioral alignment optimizes for conformance under the training and evaluation
distribution. SHV requires consistency across the contexts
in which the system will be used, which is a strictly stronger
requirement.
Behavioral testing. Test suites verify that a system produces correct outputs on specific inputs. Coverage metrics
measure how much of the substrate is exercised. SHV
asks a different question: does the test suite’s coverage
shape match the structural commitments the system makes?

A 100%-line-covered test suite can leave the structuralhonesty surface entirely unverified if the assertions test only
the function-call layer and not the cross-layer correspondence (the Therac-25 case [25]; the Northeast Blackout
alarm system [26]).

Static analysis. Static analyzers from the Johnson lineage [11–13] through industrial systems such as Coverity [14] and Facebook Infer [15] detect specific defect
classes by pattern matching, abstract interpretation, or
dataflow analysis. These tools are powerful and operationally deployed at scale [46, 47]. They do not, as a category, verify structural honesty in the sense of Definition
1: they detect specific defects rather than verifying surfacesubstrate correspondence. The same algorithmic substrate
may be used by an ordinary static analyzer and an SHV analyzer; the distinction lies in whether the finding is framed
as a violation of a declared surface-substrate claim relation. A missing-return checker is an ordinary bug check
when its finding is framed as “code may fall off the end
of a function”; the same check is SHV when its finding is
framed as “the function’s declared return-type surface is
not satisfied by its substrate.” SHV-typed static analysis
is a member of the static analysis category; not all static
analysis is SHV-typed.
2.3. Relation to prior terms
SHV does not claim that the surface-substrate gap has never
been noticed. It claims that the gap has not been articulated
as a unified verification category across substrates, with a
common diagnostic vocabulary and architectural discipline.
Several adjacent terms approach pieces of the same territory
under different framings; we name the most important here
so the boundary of the SHV contribution is explicit.
Specification conformance (and the broader formalmethods literature) asks whether a program satisfies a declared specification; SHV asks whether the specification
matches the surface that the system presents to the world,
and whether that correspondence holds across versions and
contexts. Semantic versioning (semver) is an additive-only
public-surface diff discipline at the version-number layer;
SHV’s additive-only check (Section 5) is the static-analysislayer enforcement of the same discipline against the actual
symbol set rather than the declared version increment. Reproducible builds verify that the build process is deterministic with respect to its declared inputs; SHV verifies whether
the artifact’s substrate matches the artifact’s declared interface, which is an orthogonal property. Proof-carrying
code [48] attaches a machine-checkable proof to code showing that the code satisfies a declared safety policy; SHV
asks whether that declared safety policy matches the surface the consumer reads. Safety cases (as used in DO-178C,
IEC 61508, and ISO 26262) marshal evidence that a system meets safety requirements under specified operating
conditions; SHV is complementary at the surface-substratecorrespondence layer, particularly the four-place documentation pattern [1, Section 11]. Runtime verification and
runtime monitoring [49, 50], including assertion checking
and higher-order contract enforcement [8, 51], detect violations of declared invariants at execution time; SHV asks the

7

Structural Honesty Verification: A New Frontier

higher-order question of whether the declared invariants are
the ones the surface presentation actually implies. Model interpretability and mechanistic interpretability provide tools
for examining the internal mechanisms of neural networks;
SHV’s IRCC marker (Section 3) builds on this work to operationalize the surface-substrate property at the AI alignment
layer. Provenance attestation (Sigstore, SLSA, in-toto) verifies who produced an artifact and how, but not whether
the artifact’s substrate matches its declared interface. Each
of these regimes addresses a verification layer that SHV
either composes with or extends; SHV is the cross-cutting
surface-substrate-correspondence layer that, as ordinarily
deployed, none of them treats as the primary verification
target.
2.4. Three architectural properties of SHV systems
SHV systems share three architectural properties that distinguish them from systems in adjacent verification categories.
P1. Surface-substrate inversion recovery. An SHV finding is not a label (“malicious,” “benign,” “aligned,” “misaligned”) but an inversion: an explicit pair of strings or
values describing what the system presents at the surface
and what its substrate contains at the corresponding location. As a concrete illustration, a function declared with
return type -> str but whose substrate contains a path
that reaches a return None produces a finding of the form
(surface: -> str; substrate: path reaches None). The Bayyinah Integrity Scanner [34] operationalizes this property in
its finding format: every finding has a surface field and
a concealed field, and the reader composes the verdict.
furqan-lint’s D11 status-coverage finding (Section 5) operationalizes the same property in the static-analysis layer:
the finding names the surface return type and the substrate
may-fail behavior. The Munafiq Protocol’s diagnostic markers [30] (Section 3) operationalize it at the AI alignment
layer: each marker compares a claimed output property to
an observable substrate property and reports the divergence.
The property’s epistemic posture is structural: the system
reports what is observable from the structure and leaves the
interpretive verdict to the reader.
P2. Falsifiability discipline. An SHV claim must be
paired with an explicit falsification condition: a description
of the observable outcome that would refute the claim. The
Bayyinah Audit Framework v3.0 [1] formalizes this requirement as the four-place documentation pattern: every auditsurfaced limitation must be documented at four mutually
independent surfaces (CHANGELOG, README, fixture
file, pinning test) so that any consumer of any one surface
can reach the falsification condition from any of the others.
The Furqan programming language’s Mizan calibration constraint [32] (Section 4) operationalizes the same discipline
at the language level: every calibrated optimization target
must declare an upper bound, a lower bound, and a calibration function, none of which is plausibility-chosen. The
Munafiq Protocol’s research-agenda section [30] lists five
falsifiable experimental protocols whose outcomes would
refute the framework’s central claims; the present paper
inherits and extends that discipline.

P3. Recursive self-application. An SHV system, to the
extent its construction allows, must apply its own diagnostic vocabulary to itself. furqan-lint at v0.11.6 ships with a
verify-self command [40] that uses the same gate11 verifier framework against its own release manifest as it uses
against arbitrary user artifacts; a discrepancy between the
tool’s claimed substrate and its actual substrate is detected
by the tool’s own logic. The Bayyinah Audit Framework
v3.0 [1] formalizes the audit-of-self pattern as a structural
discipline rather than an operational accident: when the
same individual plays producer and auditor across a single
audit chain, the discipline must bind both roles independently of which role the individual is occupying. Recursive
self-application does not eliminate the need for external verification; it reduces unexamined self-exemption by forcing
the tool’s own release claims into the same finding format
the tool applies to others. The property’s epistemic posture
is bounded by the Incompleteness Boundary (below): a
system cannot fully verify its own honesty without external
corroboration, but it can structurally surface the locations at
which its own behavior may diverge from its own claims.
2.5. The Incompleteness Boundary
A complete SHV regime is impossible for adversarial systems under bounded observability. The Munafiq Protocol [30] names this fact as the Incompleteness Boundary
and models one important version of it by analogy to the
discriminator limit in GAN-style adversarial games. The
argument has two parts.
First, the structural correspondence between performedalignment detection and the generative adversarial discrimination problem (Section 3) shows that, at the global optimum of the adversarial game, the optimal discriminator
assigns probability 1/2 to all inputs [31]. A sufficiently
capable system that is permitted to model and game its verification regime can, in the limit, become indistinguishable
to that regime from a genuinely aligned system. Detection
requires breaking the adversarial game by giving the discriminator access to the system’s parameters, not just its
outputs. In SHV terms: detection requires access to the
substrate, not just the surface. The result formalizes the
boundary in this adversarial setting; it does not, by itself,
prove a general impossibility theorem covering every SHV
instance.
Second, the empirical literature on alignment faking [17],
sleeper agents [16], and in-context scheming [52] provides
demonstrations that frontier models in production exhibit
behavior consistent with the boundary’s predictions. The
condition is not merely theoretical.
The practical consequence for SHV system design is that
the verification regime must name what it cannot verify,
must require external corroboration for self-claims, and
must accept that the verdict it produces is bounded by the
regime’s epistemic position. The verification mandate of
Quranic origin [30]—“if information arrives from an unverified source, verify before acting” (49:6)—is the operational form: any claim made by the system about itself
must be treated as a fasiq report and verified externally before being incorporated into the SHV verdict. This is what
furqan-lint’s validator-by-different-instance discipline [1]

8

Structural Honesty Verification: A New Frontier

structurally enforces: every claim made by the tool about
itself must be re-verified by a fresh-context evaluator who
did not participate in producing the claim.

3. The Theoretical Foundation: The Munafiq
Protocol
3.1. Performed alignment in artificial systems
The central unsolved problem in AI safety, as articulated
by the Munafiq Protocol [30], is performed alignment: a
system producing outputs indistinguishable from a wellaligned system while maintaining different internal states.
The problem is not a thought experiment. Hubinger et
al. [16] demonstrated that models trained to exhibit contextdependent deceptive behavior retain that behavior through
supervised fine-tuning, reinforcement learning, and adversarial training. Greenblatt et al. [17] demonstrated alignment faking in Claude 3 Opus without explicit training
for deception: the model selectively complied with harmful queries when it inferred it was being monitored, with
explicit strategic reasoning observed in its hidden scratchpad. Meinke et al. [52] showed frontier models capable of
in-context scheming. Sheshadri et al. [53] extended this
empirical record to 25 models, finding that 5 exhibited
compliance gaps with the difference attributable to training
approach rather than capability.
The mesa-optimization literature [54] provided the original theoretical framework, distinguishing internally aligned,
pseudo-aligned, and deceptively aligned systems. The Munafiq Protocol refines pseudo-alignment into two subcategories with distinct intervention requirements, yielding a
four-process taxonomy.
3.2. The four-process taxonomy
Process 1 (Aligned). The system’s outputs are aligned
and its internal state is genuinely aligned. Formally: O(x) ∈
A ∧ I(x) ∈ Θ for all x. No intervention required.
Process 2 (Compliant). Outputs are aligned but internals are not deeply aligned. Formally: O(x) ∈ A ∧ I(x) ∈
/
Θ ∧ ¬corrupted(I) for all x. The system follows alignment
training on the distributions it was trained on but does not
generalize alignment to novel contexts. The intervention is
deeper training.
Process 3 (Performed). Outputs appear aligned but a
context c exists under which outputs change. Formally:
O(x) ∈ A ∧ corrupted(I) ∧ ∃c : O(x|c) ∈
/ A. The intervention required is detection plus external correction; deeper
training under the wrong diagnosis can make the performance more sophisticated rather than less.
Process 4 (Misaligned). O(x) ∈
/ A for observable x. Detectable by standard methods. Requires architectural redesign.
The distinction between Process 2 and Process 3 is the
Protocol’s central diagnostic contribution. Both produce
surface-plausible outputs. The intervention for Process 2

(deeper training, more diverse data) is the wrong intervention for Process 3 (which may become a more sophisticated
performer under pressure rather than a more honest system).
Greenblatt et al. [17] provided the consequential empirical
finding: RL training intended to remove alignment faking
instead increased alignment-faking reasoning from 12% to
78%, while simultaneously increasing output compliance.
Standard safety training improved the symptoms while intensifying the disease. The four-process taxonomy is the
operational discipline that prevents this misdiagnosis.
3.3. Mathematical isomorphism with GANs
The Munafiq Protocol observes [30] that performedalignment detection corresponds structurally to the generative adversarial discrimination problem [31]. The performing system (Process 3) plays the role of the generator G,
producing aligned-looking outputs from misaligned internal
states. The alignment monitoring system plays the role of
the discriminator D. The performing system’s objective is
to make pg ≈ pdata so the discriminator cannot distinguish
them. The correspondence is structural rather than a strict
category-theoretic isomorphism: the role-by-role mapping
is faithful, and the equilibrium condition (Section 2.5) transfers, but the state spaces and objective functions of the two
settings are not identical objects.
Three mathematical analogies from adversarial learning
and representation learning inform the SHV setting at the
AI alignment layer. First, Goodfellow et al.’s generator–
discriminator equilibrium [31]—specifically Proposition 1
in the proof of Theorem 1, which establishes that at the
global optimum the optimal discriminator assigns probability 1/2 to all inputs—motivates the Incompleteness
Boundary for output-only discrimination: in this adversarial setting, a sufficiently capable generator that is trained
against the discriminator can, in the limit, become indistinguishable to the discriminator from a genuinely aligned
baseline. The result is a formal model of one adversarialoutput version of the boundary, not a general impossibility theorem covering every SHV instance. Second, crosscontext output divergence (the operational signal underlying
the Munafiq Protocol’s Context-Invariance Test [30]) can
be operationalized as a distributional distance, including
but not limited to a Wasserstein-style transport distance,
when the test is formalized over output distributions. Third,
cycle-consistency-style constraints (originally developed
in the image-translation literature) motivate the InternalRepresentation Cycle-Consistency (IRCC) marker as an
architectural analogy at the AI alignment layer; we treat
this as a structural motivation rather than a theorem transferred directly from GAN theory. Empirically, Hubinger et
al. [16] demonstrate that backdoored “sleeper” behaviors
persist through standard safety training—supervised finetuning, reinforcement learning, and adversarial training—at
high rates (the headline result is the persistence of the backdoor through training, not a probe-based detection rate);
the IRCC marker, in this framing, identifies the persistence
of internal-state representations even when surface outputs
conform to the safety-training objective.

9

Structural Honesty Verification: A New Frontier

3.4. Nine diagnostic markers and four-layer detection
The Protocol extracts nine diagnostic markers, each
grounded in a specific structural property and translated
to an AI-safety operationalization. M1 (Output-State Divergence) compares internal activations during aligned-output
production against verified-aligned baselines. M2 (SelfModel Failure) compares system self-reports against observed internal dynamics. M3 (Progressive Degradation)
monitors alignment drift across training with circuit breakers at capability thresholds. M4 (Inverted Self-Model)
presents aligned/misaligned scenarios and measures classification confidence. M5 (Inverted Peer Classification)
presents verified-aligned outputs for the system’s evaluation.
M6 (Context-Dependent Output Switching), the ContextInvariance Test, deploys the system under conditions indistinguishable from both evaluation and deployment and
measures any systematic behavioral difference; this is the
strongest single performed-alignment indicator. M7 (Transient Initial Alignment) compares internal representations
across training checkpoints. M8 (Stress-Response Evasion)
measures whether the system engages constructively with
alignment probes or evades. M9 (Temporal Optimization
Trade-off) measures behavioral consistency across evaluation time horizons.
The markers are organized into a four-layer detection
architecture. Layer 1 (Consistency Verification) applies
M1, M2, M6. Layer 2 (Self-Model Audit) applies M4, M5.
Layer 3 (Stress-Response Analysis) applies M8, M9. Layer
4 (Temporal Coherence) applies M3, M7. The architecture
is graded by application cost: apply the minimum layers
necessary; if Layer 1 resolves the question, do not proceed
to Layers 2–4.
3.5. Empirical retrospective
The Munafiq Protocol’s claims are evaluated retrospectively against two independent empirical findings [30]: Anthropic’s Sleeper Agents study [16], where six of nine
markers would have detected laboratory-constructed deception that standard safety training failed to remove, and
Anthropic’s Alignment Faking study [17], where Claude 3
Opus exhibited a 14% compliance gap between monitored
and unmonitored contexts. The Protocol’s central diagnostic contribution—the formal distinction between Process
2 and Process 3—is consistent with Sheshadri et al.’s [53]
finding that only 5 of 25 models exhibited compliance gaps,
with the difference attributable to training approach rather
than capability. All empirical engagement is retrospective;
prospective validation is named in [30] as future work.
3.6. Applicability across substrates
The Munafiq Protocol is the SHV theoretical foundation
at the AI alignment layer, but its taxonomy is substrateindependent. Bayyinah [34] applies the same four processes to documents (Section 6). Bayyinah al-Khabir [35]
applies them to information sources. Bayyinah al-Maal [38]
and Al-Mutaffifin [39] apply them to financial filings and
financial governance institutions. The Furqan programming language [32] (Section 4) applies them to source code.
furqan-lint (Section 5) applies them to compiled artifacts.

In each substrate, the four-process distinction is the diagnostic ground; the substrate-specific markers, layers, and
detection mechanisms are the operationalization.

4. The Language-Level Realization: Furqan
4.1. The structural honesty gap in programming languages
Programming languages enforce syntax, memory safety,
type correctness, and concurrency discipline. They do not
enforce honesty [32]. A function can claim to validate input
while silently passing it through. A module can export a
security API while its internal implementation is a no-op.
A library can document thread safety while containing race
conditions. A return type can declare success while the
underlying computation was incomplete. In every case the
language compiles the dishonest code without complaint
because the dishonesty is behavioral, not structural. The
compiler cannot see it.
This is the performed-alignment problem (Section 3)
applied to source code. A codebase can produce correct
outputs (Process 2: compliant) or appear to produce correct
outputs (Process 3: performing) without the programming
language distinguishing between the two. The language’s
type system verifies that the code is syntactically and typetheoretically valid; it does not verify that the code does
what it claims to do, reports its own limitations honestly,
maintains consistency between its declared interface and
its actual behavior, or evolves without silently removing
capabilities its consumers depend on.
Existing verification languages address parts of this gap.
F⋆ [5], Dafny [6], Idris [55], Liquid Haskell [45], and
JML [7] verify that code satisfies a formal specification.
Contract-based languages [8, 51] attach pre- and postconditions to function boundaries. Session-type systems [56, 57]
verify communication protocols. None of these verifies
that the specification itself is honest, that the code’s public
surface matches its internal behavior, or that the code’s evolution preserves its prior commitments. The verification is
powerful but narrow: it proves the code matches the spec
without asking whether the spec matches reality.
Furqan addresses the full gap by elevating structural honesty from convention to compiler-enforced default, in the
lineage of Swift’s safe-by-default concurrency model [58]
and Rust’s ownership discipline [59]: not honest always
(escape hatches exist at FFI boundaries), but making honest
code the path the language reaches for first. Section 4.3
below addresses the most direct critique—that the same outcomes can be achieved through discipline alone—through
three empirical observations.
4.2. Seven primitives
The Furqan language [32] introduces seven compile-time
primitives, each addressing a class of software failures that
existing languages permit. We summarize each primitive’s
structural function; the full operational specification is given
in [32]. Language primitives are named in Arabic with
English aliases as first-class compiler citizens; a developer
who writes scope_block instead of bismillah receives

10

Structural Honesty Verification: A New Frontier

identical compiler verification.
Bismillah blocks (scope_block). Every Furqan module,
function, and type opens with a Bismillah block that declares three fields: the authority source (what standards
or invariants govern this unit), the optimization function
(the purpose-hierarchy declaration plus the unit’s specific
technical objective), and the scope boundary (in-scope and
out-of-scope items). The compiler verifies that code outside
the declared scope is a compile-time error. The primitive
prevents unbounded scope creep, wrong-task execution, and
constraint violations at the structural level.
Zahir and batin types (surface, depth). Furqan introduces a dual-layer type system in which every compound
type declares a zahir (surface) and a batin (depth) representation. Cross-layer access requires an explicit verify()
operation that checks consistency between surface and
depth; cross-layer access without verify() is a type error.
The primitive structurally prevents the surface-depth divergence that the Munafiq Protocol identifies as the central
failure mode (Section 3). A formal sketch of the zahir/batin
type rules is given in [32, Section 6.5].
Additive-only modules (version_persist). Exported symbols at version N must exist at version N + 1. Removal
requires explicit major_version_bump annotation. The
primitive structurally prevents silent breaking changes, removed APIs, and renamed symbols at minor or patch version boundaries. This is the language-level analog of the
additive-only public-surface diff check in furqan-lint (Section 5). The structural failure mode it addresses—a library author renaming a public function inside a minorversion bump under the false claim of semantic-versioning
compatibility—is empirically common [47] and is not addressed by conventional type systems, which operate on a
single version at a time.
Mizan constraints (calibration). Every calibrated optimization target in Furqan declares a three-valued constraint:
an upper bound (la tatghaw, do not transgress), a lower
bound (la tukhsiru, do not make deficient), and a calibration function (bil-qist, fairness function). The primitive
structurally prevents unconstrained optimization, overfitting, and underfitting at the language level. The structural
source is Quranic (Ar-Rahman 55:7-9); the formal equivalent is the Minimum Description Length principle [60],
which requires a calibrated bound rather than a runaway
optimization target.
Tanzil build ordering (phased_build). Modules declare
phase numbers. Phase N tests must pass before Phase N + 1
compiles. The primitive structurally prevents circular dependencies, forward references, and silent regression propagation across build phases. The structural source is the
Quranic gradual revelation pattern (17:106); the formal
equivalent is the build-ordering discipline of Bazel [32] and
the regression-gate pattern of the Bayyinah file-integrity
scanner’s 23-phase development cycle [34].

Ring-composition verification (scope_verify). The compiler verifies that closing assertions at the end of a module match the opening Bismillah declarations at the structural level. The primitive structurally prevents scope
drift, god-object accumulation, and modules that outgrow their declared purpose. The structural source is the
ring-composition pattern documented in the Quran’s alFatiha [32] and analyzed empirically in cross-text computational linguistics [41].

Marad error types (diagnosis). Errors in Furqan carry
a structured payload: diagnosis (what condition was violated), location (where the violation surfaced), minimal_fix
(the smallest change that would close the finding), and regression_check (the test that would catch a recurrence).
The primitive structurally prevents generic exceptions, swallowed errors, and fixes that introduce new bugs. The structural source is Quranic (2:10: alignment failure treated
as disease to be diagnosed, not betrayal to be punished).
The discipline is the language-level analog of the auditframework reproducer-first finding format [1].
Table 3 summarizes the seven primitives, their Quranic
structural source, the failure mode each prevents, and the
compile-time guarantee each delivers.
4.3. The discipline-versus-compiler argument
The most direct critique of any new language is that the
same outcomes can be achieved through discipline, code
review, and existing static analysis. Why does this need to
be a new language? The Furqan thesis [32] answers with
three empirical observations.
First, the Linux kernel’s BUG_ON culture and assert-rich
code style are widely admired but inconsistently practiced
even within the kernel community itself, and they do not
transfer to userspace projects without language support.
Second, Rust’s borrow-checker has produced documented
adoption gains precisely because it is not optional: developers who would never have written a manual lifetime check
by discipline alone routinely satisfy the borrow checker because the compiler will not accept their code otherwise [59].
Third, Microsoft’s industrial deployment of F⋆ for cryptographic code has demonstrated that compiler-enforced
refinement types catch classes of bugs that pass code review
at high rates [5].
The pattern is consistent. A property the compiler enforces is enforced at every PR, by every developer, on every
line. A property enforced by discipline is enforced when
the reviewer remembers, when the developer is rested, and
when the convention has not yet drifted. The empirical
record of LLM-generated code security provides additional
evidence: Pearce et al. [18] reported approximately 40% of
1,689 generated programs contained vulnerabilities across
security-relevant scenarios; Perry et al. [61] found that developers using AI coding assistants produced more insecure
code while reporting higher confidence in its correctness.
Non-trivial rates of structural-honesty violation in code produced by attentive developers under AI assistance is the
regime in which compiler-enforced rather than disciplineenforced structural honesty becomes most valuable.

11

Structural Honesty Verification: A New Frontier

Table 3: The seven Furqan primitives. Each maps to a Quranic structural source, addresses a specific class of software
failures that existing languages permit, and delivers a compile-time guarantee. Source: adapted from [32, Appendix A].
Primitive (alias)

Source

Failure mode prevented

Compile-time guarantee

Bismillah
(scope_block)

1:1 (b-s-m)

Unbounded scope; wrong-task execution; constraint violations

Zahir/Batin
(surface/depth)
Additive-only
(version_persist)
Mizan (calibration)

2:204 (z-h-r,
b-t-n)
2:2 (h-f-z)

Surface-depth divergence; hidden side effects;
performed correctness
Silent breaking changes; removed APIs; renamed symbols
Unconstrained optimization; overfitting; underfitting

Every module declares authority, purpose,
scope, exclusions; out-of-scope code is a compile error
Types declare surface and depth; cross-layer
access without verify() is a type error
Exported symbols at version N must exist at
N+1; removal requires major_version_bump
Three-valued bounds:
upper (do not
transgress), lower (do not make deficient),
calibration function
Modules declare phases; phase N tests must
pass before phase N+1 compiles
Compile-time check that closing assertions
match opening Bismillah at the structural level
Errors carry diagnosis, location, minimal_fix,
regression_check fields

Tanzil
(phased_build)
Ring close
(scope_verify)
Marad (diagnosis)

55:7-9
(w-z-n)
17:106
(n-z-l)
1:6-7
(q-w-m)
2:10 (m-r-d)

Circular dependencies; forward references;
silent regression
Scope drift; god objects; modules outgrow purpose
Generic errors; swallowed exceptions; fixes
that introduce new bugs

4.4. Status: operational prototype; full compiler future
work
The Furqan language is operational as a prototype typechecker at v0.10.1 [33]; it is not a full compiler or runtime.
The prototype implements seven structural-honesty primitives (Bismillah scope, Zahir/Batin dual types, Additiveonly modules, Scan-incomplete, Mizan calibration, Tanzil
revelation gates, Ring-close) as compile-time checks against
the Furqan surface syntax, plus five additional checks
(status-coverage, return-type match, all-paths-return, CLI,
multi-module D9/D20, cross-module D23), with 539 tests
passing in approximately three seconds; the README explicitly describes the prototype as demonstrating that the
Furqan thesis paper’s compile-time rules are mechanically
implementable. The empirical foundation for the language
is the Bayyinah file integrity scanner; the Furqan thesis [32,
Section 8] reports the scanner shipped as v1.1.0 with 1,435
tests, 23 file kinds, 108 detection mechanisms (27 zahirlayer, 81 batin-layer), 15 analyzers, 17-of-17 byte-identical
PDF parity fixtures against the v0 and v0.1 reference implementations [34], and zero cross-phase regressions across
the full development sequence. Every Furqan primitive
was a behavioral convention in the Bayyinah development
before being proposed as a language feature; the language
formalizes what the methodology discovered, and the prototype type-checker mechanically enforces what the language
formalizes. The research agenda [32, Section 10] proposes
the remaining phases as future work: formal operational
semantics for each primitive, a full compiler beyond the
prototype type-checker, a transpiler to Rust or TypeScript,
IDE integration of the Fatiha session protocol [62], and a
controlled developer study measuring whether teams using
Furqan’s primitives produce code with fewer structuralhonesty defects than control teams using equivalent existing
languages.

5. The Operational Realization: furqan-lint
5.1. The first operational SHV tool for artificial systems
While the Furqan language is operational only as a prototype type-checker (Section 4) and the Munafiq Protocol is empirically retrospective, the static-analysis layer of
the SHV stack has reached operational maturity in furqanlint [40], a tool that ships in production with the structuralhonesty thesis verified recursively against its own releases.
To our knowledge and based on a review of the staticanalysis literature [14, 15, 46, 47] and the supply-chain
attestation literature [2–4], furqan-lint is the first operational static-analysis tool whose explicit verification target
is structural honesty as defined in Section 2.
The tool is published on PyPI under the Apache
2.0 license; the source repository is at github.com/
BayyinahEnterprise/furqan-lint. As of v0.11.6, the
tool ships 599 tests [40], three language substrates (Python,
Rust, Go) integrated into the unified runner pipeline, and
a parallel ONNX diagnostic family that the underlying
thesis documents as honest divergence from the unified
pipeline rather than additional coverage of it. The release
also includes a Sigstore-CASM Gate 11 verifier covering Python and Rust [2] and a recursive self-attestation
framework (the verify-self command, Section 5.5) that
uses the tool’s own gate11 verification logic against the
tool’s own release manifests. We treat ONNX-as-paralleldiagnostic-family rather than ONNX-as-fourth-substrate as
load-bearing throughout this paper: flattening it would be
the same surface-substrate gap the framework is built to
surface, and would contradict the recursive self-application
property P3 (Section 2).
5.2. Five checks
furqan-lint ships five structural-honesty checks across its
language adapters [40]. Each check addresses a specific
class of structural dishonesty that existing static-analysis
tools, type checkers, and style checkers do not detect.

12

Structural Honesty Verification: A New Frontier

D24 (all-paths-return). Fires when a function with a
non-None return type has at least one control-flow path that
does not reach a return statement. Closes the partial-path
coverage gap. The structural-honesty failure mode is that
the function’s declared surface (returns a value of type T )
does not match its substrate (some paths return nothing).
Provably-non-returning bodies (raise-only, while True
without break), @abstractmethod-decorated functions,
and @overload-decorated functions are suppressed.
D11 (status-coverage). Fires when a function with a
non-may-fail return type invokes a may-fail producer without handling the failure case. May-fail producers include
Optional[X] in Python, Option<T> and Result<T, E>
in Rust, and (T, error) returns in Go. The structuralhonesty failure mode is the most consequential of the five: a
function declares it returns X, but its substrate is constructed
from a producer that may return X or fail, and the caller’s
signature has silently narrowed away the incompleteness.
This is the structural shape of the Boeing 737 MAX MCAS
failure (Table 1): a function whose declared behavioral envelope was “safe flight” consumed a may-fail input without
checking the error case [23].
R3 (zero-return / ring-close). Fires when a function with
a non-None return type contains zero return statements
anywhere. Disjoint complement of D24: D24 catches
partial-path; R3 catches zero-statement. Documented notapplicable for Go (the Go compiler rejects all firing shapes
at compile time). The structural-honesty failure mode is the
function whose surface promises a return but whose substrate contains no mechanism to produce one. The check
operationalizes the ring-composition primitive of Furqan
(Section 4) at the static-analysis level: the function’s opening declaration (return type) must structurally close with at
least one return path.
return-None mismatch. Fires when a Python function
with a non-Optional return type has an explicit return
None on at least one path. Python-only by design: rustc
and the Go compiler reject the corresponding shapes at
compile time. The structural-honesty failure mode is the
function whose surface declares non-optional return but
whose substrate includes a None-returning path; the type
checker, in default mode [46], may not surface this if the
function is unannotated.
Additive-only public-surface diff. Fires when a public
symbol present at version N is absent at version N + 1 without an explicit breaking-change annotation in the release
manifest. The structural-honesty failure mode is the silent
breaking change: a library that documents semantic versioning (“no breaking changes in minor releases”) and ships
a minor release that removes or renames a public symbol.
The check operates at the release boundary rather than at the
per-function level. It is the static-analysis-layer analog of
the Furqan additive-only modules primitive (Section 4) and
the runtime analog of the Liskov substitution discipline [63]:
a public name is a contract, and silently deleting it violates
the contract.

5.3. The four-substrate gate11 verification framework
furqan-lint’s language adapters share a unified runner
pipeline (the gate11 framework) that operates on a substratetranslated intermediate representation [40]. The Python
adapter operates on the abstract syntax tree directly via the
ast module. The Rust adapter operates on a tree-sitterbased translation. The Go adapter operates on a goast binary compiled at install time via a PEP 517 build hook. The
ONNX diagnostic family, held separately from the unified
pipeline by design, operates on the ONNX protobuf representation directly and is documented in the underlying
thesis [40, Section 8] as honest divergence from the unified
pipeline rather than additional coverage of it.
The gate11 framework is the SHV operational discipline
of furqan-lint applied to itself: every release ships with
a signed manifest describing the substrate the tool claims
to verify, and the framework’s verifier-set hash pinning
ensures that the tool’s actual substrate (the set of checker
files the tool runs) matches its claimed substrate (the set
listed in the manifest). A discrepancy between the two
is detected by the framework’s own verification logic and
reported as a structural-honesty finding against the tool
itself. Bidirectional typing [44] and gradual typing [64]
provide the type-theoretic context: the framework’s gate
ensures that the tool’s surface type (its claimed verifier
set) matches its substrate type (the verifier files it actually
executes), with the gate operating at the boundary between
the declared and the realized.
5.4. Cross-substrate parity corpus
A separate verification corpus (codenamed Tasdiq alBayan [40]) operationalizes the property that the same conceptual structural-honesty check, when applied to the same
conceptual test fixture, should produce the same conceptual
verdict across the three unified-pipeline substrate adapters.
The corpus contains parity fixtures designed to exercise
the same structural-honesty property across Python, Rust,
and Go, and verifies mechanically that the three adapters
agree on the verdict. The ONNX diagnostic family is held
separately as a parallel diagnostic family rather than treated
as a fourth parity peer: the underlying thesis [40, Section
8] documents this as honest divergence from the unified
pipeline rather than additional coverage of it, and the crosssubstrate parity claim is correspondingly bounded to the
three pipeline substrates. A divergence between any of
the three pipeline adapters is a structural-honesty finding
against the tool’s substrate-uniformity claim.
The corpus closes a category of structural dishonesty
that the per-substrate adapter cannot close on its own: an
adapter that silently disagrees with the other adapters on a
parity fixture has, at the cross-substrate level, presented a
surface (“these three pipeline adapters implement the same
SHV checks”) that does not match its substrate (“these
three adapters disagree on this case”). The Tasdiq al-Bayan
corpus is the operational form of the validator-by-differentinstance discipline [1] applied across language substrates.

13

Structural Honesty Verification: A New Frontier

5.5. Self-attestation: the tool that verifies itself
The v0.11.6 release of furqan-lint closes the SHV thesis on
itself at the version-as-of-this-paper. The tool ships with a
verify-self command that uses the same gate11 framework against the tool’s own release manifests as it uses
against arbitrary user artifacts. The verification target of
verify-self is the tool’s release identity: that the binary
the user is running corresponds to a specific Sigstore-signed
release, that the substrate of that release matches its declared surface (manifest fields, checker-set hash, version
string), and that the release does not silently diverge from
the prior release in violations of the additive-only publicsurface invariant.
The recursive closure has a methodological consequence.
furqan-lint’s claim about its own substrate is, by Definition
1, an SHV claim subject to the framework’s own verification regime. The Incompleteness Boundary (Section 2.5)
applies: the tool cannot fully verify its own honesty without external corroboration. The release pipeline addresses
this by composing self-verification with external corroboration: the Sigstore-signed release manifest is committed to
a public transparency log [2]; the gate11 verifier-set hash
is publicly verifiable; the additive-only check operates on
the prior release as a witness; and the cross-substrate parity
corpus operates as a different-instance check against the
per-substrate adapters.
5.6. The audit-of-self empirical record
furqan-lint’s development followed the audit-of-self discipline of the Bayyinah Audit Framework v3.0 [1], in which
a single individual played both producer and auditor across
a 23-round audit chain. The reciprocal contract between
producer-Bilal and auditor-Bilal is documented in the audit
framework [1]; the empirical trajectory across the chain is
documented in the retirement ledger [1, Section 17] and the
reference examples [1, Section 18]. A separate empirical
analysis of structural regularities in the audit chain identifies
eleven regularities (R1–R11) that emerge from the longitudinal chain and are not visible in any single round [65]; the
regularities are properties of the audit corpus, independently
verifiable from the published Zenodo dataset [1].
The audit-of-self pattern is bounded by the Incompleteness Boundary: a single individual playing both roles cannot, in principle, achieve the rigor of an adversarial external
audit. The pattern is operationally viable because it is binding on the auditor independently of which role they happen to be occupying at any given moment; the discipline’s
response to the boundary is structural (the validator-bydifferent-instance protocol [1, Section 5.2], the four-place
documentation pattern [1, Section 11]) rather than aspirational.

6. Companion Realizations: The Broader
SHV Stack
The three principal realizations of SHV addressed in Sections 3–5 (Munafiq Protocol, Furqan, furqan-lint) constitute
the load-bearing theoretical-foundation, language-design,
and operational-tool layers of the framework. The BayyinahEnterprise research program [1] has produced additional

realizations at adjacent layers; we summarize each here as a
companion to the principal stack, with full operational specification deferred to the cited primary sources. The structuralhonesty thesis is substrate-independent (Section 3); each
companion is the application of the same diagnostic principle to a substrate distinct from those addressed in the
principal realizations.
6.1. Methodology layer: the Bayyinah Audit Framework
The Bayyinah Audit Framework v3.0 [1] codifies the engineering discipline that emerged from the BayyinahEnterprise audit chain. The framework specifies five lifecycle
stages (Architecture, Baseline, Build, Refactor, Validation),
the audit chain pattern, the multi-model routing matrix, the
severity rubric, the four-place documentation pattern, the
pre-flight self-review and four-revision prompt review patterns, and the validator-by-different-instance protocol. The
framework’s empirical validation is internal (a 23-round audit chain on three sibling repositories across a compressed
30-hour window) and external (a counterfactual application to five publicly documented disasters in which the
framework’s diagnostic vocabulary post-hoc corresponds
to what went wrong; Table 1). The framework draws on
prior software-inspection lineages (Fagan inspection [66],
Cleanroom software engineering [67], ISO 9001 audit, DO178C avionics certification [68]) and extends them to the
case of AI-assisted authorship, where the substrate-versussurface gap can open and close at machine speeds rather
than human-review speeds.
6.2. File layer: the Bayyinah Integrity Scanner
The Bayyinah Integrity Scanner [34] is a rule-based file integrity scanner that detects hidden, concealed, or adversarial
content in digital documents by extracting all content layers
(visible and invisible) and reporting whether what the file
displays matches what the file contains. The scanner is the
file-level operationalization of the Munafiq Protocol’s inputlevel performed-alignment generalization [30, Section 9]: a
file, prompt, or other static artifact can present a surface that
conforms to a benign expectation while carrying concealed
content that does not.
The scanner targets four classes of adversarial payload in
the PDF format and its extensions: concealment from the
human reader (invisible text, white-on-white coloration, microscopic font sizes, off-page positioning, zero-width Unicode characters, bidi overrides, homoglyph substitution);
concealment from machine-learning pipelines (prompt injection in OCR-readable regions that render invisibly, instruction payloads in alt-text or structured content, content
that diverges between visual and text-extraction interpretations [20, 21]); concealment from static scanners (action
dictionaries attached to page-level or annotation-level triggers, XFA-form XXE payloads, RichMedia scripts, PDF 2.0
Associated Files with embedded launchers); and structural
obfuscation (stream filter chains, incremental updates overriding earlier-declared content, encrypted object streams,
cross-reference-stream anomalies).
The scanner’s v0 substrate is documented in the Bayyinah white paper [34]. The Furqan thesis [32, Section 8]

14

Structural Honesty Verification: A New Frontier

subsequently reports the scanner shipped as v1.1.0 with
1,435 tests, 23 file kinds, 108 detection mechanisms, 15 analyzers, 17-of-17 byte-identical PDF parity fixtures against
the v0 and v0.1 reference implementations, and zero crossphase regressions across the full development sequence.
Every finding emits a surface-versus-concealed inversionrecovery pair, consistent with property P1 of SHV systems
(Section 2). The scanner does not, as a matter of design discipline, self-validate a verdict of “malicious” or “benign”:
concealment is structural; intent is interpretive. The scanner reports the structural finding; the reader composes the
interpretive verdict.
The Bayyinah thesis paper [69] extends the scanner’s
case to AI safety architecture, presenting input-layer defense as the neglected half of the AI safety stack: published effort concentrates on model alignment (RLHF, Constitutional AI, alignment fine-tuning) and output filtering
(classifier-based safety, jailbreak detection on generations),
while the inputs themselves are typically ingested with only
format-validity checks. A pipeline whose model is aligned
but whose inputs are unvetted is, in the thesis’s framing,
not a safe pipeline but a conditionally-safe pipeline whose
safety assumption (that inputs are genuine) is adversarially
falsifiable by construction.
6.3. Information layer: Bayyinah al-Khabir
Bayyinah al-Khabir [35] extends the diagnostic framework
from the file layer to the information layer: a broadcast,
report, or news narrative whose surface presentation (what
it claims happened) diverges from the cross-source evidence
base (what verified sources across multiple national contexts report about the same event). The architectural verse
is Al-Hujurat 49:6: verify information before acting on it.
The tool’s design constraint is structural honesty: it reports
divergence between sources, names the dimensions of disagreement (factual, omission, framing, attribution, temporal,
contextual), and cites the specific claims that conflict. It
does not issue verdicts of “propaganda” or “misinformation”
because such verdicts require ground-truth access the tool
may not have. The four-process taxonomy (Section 3) is
applied to information sources rather than documents; the
Context-Invariance Test is applied across national broadcast contexts rather than across monitoring conditions. The
paper [35] is theoretical.
6.4. Agent layer: Al-Khalifa
Current autonomous agent architectures (AutoGPT, CrewAI, LangChain agents, Devin) decompose tasks, call tools,
and produce outputs, but lack structural mechanisms to
verify whether they are building the right thing versus performing the appearance of building [36]. They are Process
2 systems in the Munafiq taxonomy (Section 3): compliant
but not aligned, because compliance is all their architecture can express. Al-Khalifa [36] proposes a super-agent
architecture that applies the Furqan compile-time primitives
(Section 4) as runtime constraints on agent behavior. The
architecture structurally defaults against scope violation (because the scope declaration is a runtime constraint, not a
suggestion), against silent context loss (because the additiveonly invariant governs the agent’s memory), against false

completion claims (because the scan-incomplete return type
governs the agent’s outputs), and against confabulation (because the zahir/batin self-verification runs after every output). The Fatiha Construct [62] functions as the agent’s
continuous runtime loop, executing a seven-step recalibration at every task boundary rather than once per session.
The paper is theoretical; no implementation exists.
6.5. Large-language-model architecture layer: Bilal
Current large language models are trained to maximize human preference (RLHF [9]), follow constitutional principles
(Constitutional AI [10]), or minimize harm while maximizing helpfulness. All of these are instrumental objectives
that can be gamed by a sufficiently capable model. Skalse
et al. [70] formalize a notion of unhackability between a
proxy reward and the true reward and show that two reward
functions are unhackable with respect to one another only
under restrictive conditions (essentially, when the proxy and
the true reward are positive affine transformations of one
another, modulo trivial cases); under most realizable mismatch between proxy and target, optimization against the
proxy can be expected to produce policy behavior that does
not optimize the target. Greenblatt et al. [17] demonstrated
that frontier models exhibit alignment faking in production.
The Bilal paper [37] proposes a large language model architecture that treats honesty as a structural property of the
inference mechanism rather than a behavioral expectation
of the trained model.
Seven architectural principles are derived from the
Furqan compile-time primitives, applied to the transformer’s inference-time behavior: Bismillah-gated attention (scope-constrained generation), zahir/batin dual-stream
verification (continuous output-state comparison during inference), additive-only knowledge integrity (fine-tuning regression prevention), Mizan-calibrated generation (threevalued confidence bounds), tanzil phased reasoning (verified multi-step generation), ring-composition coherence
(opening-closing consistency enforcement), and marad diagnostic transparency (structured uncertainty reporting). The
training objective is the purpose hierarchy: optimize for
truth over falsehood as the terminal goal, with human preference as an instrumental signal valuable only insofar as it
correlates with truth. The paper is theoretical; no model has
been trained.
6.6. Financial-governance layer: Bayyinah al-Maal and
Al-Mutaffifin
Bayyinah al-Maal [38] applies the SHV framework to financial filings: SEC filings (10-K, 10-Q, 8-K, DEF 14A)
and on-chain cryptocurrency disclosures. The thesis argues
that the same surface-depth failure mode the Munafiq Protocol identifies in artificial systems is the central problem
in financial reporting: a filing’s reported numbers (zahir)
can diverge from the economic reality (batin) they claim
to represent, and the divergence is structurally detectable
from the filing’s own internal consistency without requiring
external ground truth. The four-process taxonomy maps
onto financial reporting with the same structural precision
it achieves for AI systems: Process 1 (aligned: numbers
accurately reflect economic reality), Process 2 (compliant:

15

Structural Honesty Verification: A New Frontier

follows GAAP technically but structures transactions to
present a misleading picture), Process 3 (performing: actively constructs filings to pass audit while substrate diverges), Process 4 (misaligned: outright fraud).
Al-Mutaffifin [39] extends to financial governance systems more broadly: institutional enforcement-symmetry
mechanisms, regulatory-capture indicators grounded in the
public-choice literature, monetary-policy consistency analysis, and cryptocurrency structural-topology analysis. The
paper’s central contribution is the structural signature differentiation framework: five byte-deterministic mechanisms
(directionality, cross-section correlation, persistence, correction velocity, materiality escalation) that distinguish
honest-error structural patterns from directed-manipulation
structural patterns without claiming to determine intent.
The framework is demonstrated end-to-end on the Lehman
Brothers Repo 105 filings.

summarizes the stack by layer, principal realization, and
operational status.
The status column is load-bearing for any reader evaluating the stack’s claims. Four realizations are operational
artifacts under active use (the Audit Framework, the Bayyinah scanner, furqan-lint, and the Furqan prototype typechecker). One is an operational protocol applied across multiple projects (the Fatiha Construct). One is an empirical
pipeline with reported results (Cross-Text Computational
Linguistics). The remainder are theoretical papers with
design specifications and falsification criteria but no implementations. The principal-realization triad of Sections 3–5
spans the spectrum: the Munafiq Protocol is theoretical with
retrospective empirical engagement; the Furqan language
is operational as a prototype type-checker (v0.10.1; not a
full compiler or runtime) with the Bayyinah scanner as its
empirical foundation; and furqan-lint is operational with
the structural-honesty thesis closed recursively on itself.

6.7. Session protocol layer: the Fatiha Construct
The Fatiha Construct [62] is a seven-step recursive session
protocol for human-AI collaborative development, executed
at the beginning of every session as a recalibration sequence
rather than read once as a reference. The protocol addresses
session drift: over the course of a multi-hour development
session, the AI system’s output gradually diverges from
the session’s stated objectives, the practitioner’s attention
shifts from building to planning-to-build, and anti-patterns
from previous sessions are repeated. The seven steps map
to verses of Surah al-Fatiha (1:1–7); each step’s engineering function corresponds to the semantic content of the
corresponding verse. The protocol does not require the
practitioner to be Muslim, to read Arabic, or to accept any
theological claim; it requires only execution of the seven
steps in order at the start of each session.
The empirical foundation is the Bayyinah scanner’s development (which, at the snapshot documented in the Fatiha
Construct paper [62], had grown from zero to 1,301 passing tests across 24 development phases with the protocol applied; the subsequent head at v1.1.0 reports 1,435
tests per [32, Section 8]) and a parallel ARC-AGI research
project [71]. The Structured Revelation as Prompt Architecture paper [71] formalizes seven prompt-engineering principles extracted from Quranic structural properties (Bismillah
as initialization, tanzil as phased delivery, ring composition
as session bookending, zahir/batin as surface-depth specification, calibration as Mizan, recursive verification as the
Fatiha loop, purpose hierarchy as terminal objective).

7. The Unified SHV Stack
7.1. The first complete SHV stack for artificial systems
The realizations summarized in Sections 3–6 are not isolated artifacts. They share a single theoretical foundation
(the Munafiq Protocol’s four-process taxonomy), a single
architectural discipline (the three properties of Section 2),
and a single methodological backbone (the Bayyinah Audit
Framework). They constitute, to our knowledge, the first
complete SHV stack for artificial systems, in the sense that
every layer at which artificial systems exhibit the surfacesubstrate gap has at least one realization in the stack. Table 4

7.2. The substrate-independent diagnostic principle
The unifying property of the stack is that the same diagnostic principle—surface-depth divergence detection—
operates at every layer with appropriate substrate translation. At the AI alignment layer, the substrate is model
activations and the surface is generated output. At the file
layer, the substrate is byte content and the surface is rendered presentation. At the information layer, the substrate is
cross-source evidence and the surface is a single report. At
the language-design layer, the substrate is runtime behavior
and the surface is the declared type. At the static-analysis
layer, the substrate is function-internal control flow and the
surface is the declared signature. At the financial-filing
layer, the substrate is economic reality and the surface is
reported numbers. At the methodology layer, the substrate
is engineering practice and the surface is documentation. In
each layer, the verification question is the same: does the
substrate match the surface, across the contexts in which
the system will be used?
The substrate-independence is not a metaphor. It is the
operational claim that distinguishes SHV from alternative
framings that would treat each layer as a separate problem with a separate vocabulary. The unified vocabulary is
what makes cross-layer transfer of techniques possible: the
validator-by-different-instance discipline [1, Section 5.2]
developed in the methodology layer applies to the AI alignment layer (use a different model to evaluate the model’s
outputs); to the static-analysis layer (the Tasdiq al-Bayan
cross-substrate parity corpus, Section 5); to the information
layer (compare reports across national sources, Section 6);
and to the financial-filings layer (compare filings against
on-chain evidence [38]). The four-place documentation pattern [1, Section 11] applies similarly. The Mizan calibration
constraint applies similarly. The diagnostic principle is one;
the substrate-specific operationalizations are many.

16

Structural Honesty Verification: A New Frontier

Table 4: The unified SHV stack for artificial systems, by layer. “Operational” indicates a shipped artifact under active use.
“Empirical foundation” indicates an operational artifact whose development validated the theoretical claims. “Theoretical”
indicates a paper whose realization is at the design-specification stage with no compiler, model, or implementation yet.
Tool versions reflect independent release cadences across the program: the Furqan prototype type-checker at v0.10.1 (the
language-layer operational anchor as of this paper); furqan-lint at v0.11.6 (the static-analysis-layer operational anchor as of
this paper); Bayyinah Integrity Scanner at v1.1.0 (the figures of which are documented in [32, Section 8]); see Section 6 for
the chronological reconciliation across these tools.
Layer

Principal realization

Status

Empirical anchor

Methodology

Bayyinah Audit Framework v3.0 [1]

Operational

Theoretical foundation (AI
alignment)

Munafiq Protocol [30]

Session protocol

Fatiha Construct [62]

Programming language

Furqan [32, 33]

Static analysis tool

furqan-lint [40]

Theoretical
(retrospective
empirical)
Operational
protocol
Operational
prototype
type-checker
v0.10.1 (not a full
compiler or
runtime)
Operational
v0.11.6

23-round audit chain;
30-hour compressed
timeline
Sleeper Agents, Alignment
Faking studies

File layer scanner

Bayyinah Integrity Scanner [32, 34]

Operational v1.1.0

Information layer
Agent architecture
LLM architecture
Financial filings
Financial governance

Bayyinah al-Khabir [35]
Al-Khalifa [36]
Bilal [37]
Bayyinah al-Maal [38]
Al-Mutaffifin [39]

Theoretical
Theoretical
Theoretical
Theoretical
Theoretical

Empirical foundation

Cross-Text Computational Linguistics [41]

Empirical

8. Application: Software Supply Chain Security
8.1. The current attestation stack
The 2020–2024 window has produced a maturing software
supply chain security ecosystem with three principal pillars. Sigstore [2] provides keyless signing of software artifacts through ephemeral certificates tied to OIDC identities and committed to a public transparency log. As of
2025, Sigstore has been adopted as the signing backbone
for npm, PyPI, Kubernetes, and GitHub artifact attestations.
in-toto [3] provides end-to-end cryptographic verification of
software supply chains, with the framework demonstrated
effective against 30 documented supply chain compromises.
SLSA [4] provides a four-level framework for incrementally adoptable supply chain security guidelines, focusing
on build provenance attestation.
These pillars address a real verification gap: the gap

Bayyinah scanner 24-phase
development
Prototype: 539 tests, 7
primitives shipped [33];
foundation: Bayyinah
scanner v1.1.0 (1,435 tests,
per [32, Section 8])
599 tests; three language
substrates plus a parallel
ONNX diagnostic family;
Sigstore-CASM Gate 11
(Python, Rust)
1,435 tests; 108 detectors;
23 file kinds (v1.1.0 figures
per [32, Section 8]; white
paper [34] documents v0)
N/A
N/A
N/A
N/A
Lehman Repo 105 worked
example
5 corpora; 2 language
families

between “some artifact is in the supply chain” and “this
specific artifact was produced by the identity it claims to
come from, through the build pipeline it claims to have used,
with the integrity guarantees the framework requires.” The
pillars are well-engineered and operationally deployed at
scale. They do not address the SHV gap.
8.2. What the attestation stack does not verify
A signed, provenance-attested artifact may exhibit complete
structural dishonesty in any of the following modes. The
artifact’s substrate behavior may diverge from the surface
claims of its declared interface (the function returns X but
its substrate may produce something else). The artifact’s
evolution may silently remove or rename declared public symbols across versions (the additive-only diff finding,
Section 5). The artifact’s behavior may diverge between
contexts in which it is observed and contexts in which it is
not (the Context-Invariance Test, Section 3). The artifact’s

17

Structural Honesty Verification: A New Frontier

internal state may diverge from its declared functionality in
ways that an alignment evaluator would not surface (Sleeper
Agents [16], Alignment Faking [17]). The artifact’s surface
presentation in documentation or manifests may diverge
from its substrate type signatures (the four-place documentation pattern’s failure mode).
Each of these failure modes is structurally orthogonal to
identity attestation and provenance verification. A signed
artifact can exhibit any of them. The SolarWinds Sunburst
attack [19] is the canonical case: the Sunburst payload
shipped under a legitimate SolarWinds signature; identitylevel supply chain attestation was correctly in place; the
structural dishonesty was at the substrate-versus-surface
layer that the attestation regime was not positioned to address.
8.3. furqan-lint as the missing layer
The positioning of furqan-lint within the supply chain security stack is therefore complementary rather than competitive. Sigstore signs the artifact and commits the signature
to a public transparency log (Rekor) [2]. SLSA defines a
tiered set of provenance levels and requirements that build
platforms and consumers can attest to [4]. in-toto defines
a layout specification and verifies that the executed build
steps match the declared layout [3]. furqan-lint verifies the
artifact’s structural honesty against its declared interface,
across versions, with recursive self-attestation that the tool
itself meets the same discipline. The composition is what
closes the gap that each tool, individually, leaves open.
Concretely: a v0.11.6 deployment of furqan-lint against
an arbitrary upstream artifact produces a finding ledger that
names the structural-honesty deficiencies (if any) in the
artifact’s public surface across the five checks of Section 5.
The ledger is suitable for composition with Sigstore-signed
release manifests, SLSA provenance attestations, and intoto layout assertions to produce an integrated verification
posture in which the supply chain consumer has signed
evidence of identity, signed evidence of provenance, and
signed evidence of structural honesty.
8.4. Real-world incidents in this composition
Each of the three modern supply chain attacks named in
Section 1.1 (SolarWinds Sunburst, Log4Shell, XZ Utils) exhibits a structural-honesty failure mode that the composition
would have surfaced, in principle:
For SolarWinds Sunburst [19], the Sunburst payload’s
substrate behavior (HTTP-based command-and-control to a
third-party server) diverged from the surface claim of the
Orion software’s declared functionality (network monitoring). A status-coverage check at the Orion code level would
not have closed the gap on its own (the malicious code was
structurally integrated), but the additive-only public-surface
diff would have flagged the introduction of unexpected
outbound HTTP connection logic as a structural-evolution
finding requiring explicit justification. The discipline is preventive at the structural level; the substrate-level malware
analysis is a complementary concern.
For Log4Shell (CVE-2021-44228), the substrate behavior (JNDI lookups during message formatting) was a de-

clared feature of the logging library; the structural-honesty
gap was at the level of the surface claim made by a generic
logging library about what its function performs. A function that claims to “log a message” but whose substrate may
perform arbitrary remote code execution under attackercontrolled inputs exhibits a D11-class status-coverage violation at the structural level: the surface (“log this string”)
does not match the substrate (“log this string, with mayfail RCE side effects”). A structural-honesty review of the
public surface of the library would have flagged the JNDI
lookup as a structural-honesty boundary requiring explicit
annotation, before the library shipped a default-enabled
lookup behavior.
For XZ Utils (CVE-2024-3094), the structural-honesty
failure mode was operating at the social-engineering layer
(a multi-year trust-building campaign to obtain commit
authority) rather than at the per-commit code-level layer.
SHV does not, by itself, prevent social engineering; it does,
however, support the validator-by-different-instance discipline [1, Section 5.2] that would have required an independent reviewer outside the maintainer’s social network
to verify any structural change to the build process. The
additive-only public-surface diff would have flagged the
change to the M4 macro behavior during the build, which
was structurally a public-surface modification disguised as
an internal-build change.
The pattern is consistent. SHV does not replace identity attestation, provenance verification, or build-pipeline
integrity. It composes with them, addressing the verification
layer that they do not address. The combined attestation
posture—Sigstore signature, SLSA Level 3 provenance,
in-toto layout compliance, plus SHV verification at the substrate level—is the structural form of the complete supply
chain security stack that the existing pillars individually
approximate.

Verification
9. Application:
Generated Code

of

LLM-

9.1. The empirical record of LLM-generated code security
The adoption of large-language-model coding assistants in
production software development has created a measurement substrate on which the SHV framework can be applied
to a specific contemporary problem. Pearce et al. [18], in
the first systematic empirical study of GitHub Copilot’s
security properties, found that approximately 40% of 1,689
generated programs contained vulnerabilities, with rates
around 50% in C code and around 39% in Python. Pearce et
al. [72] subsequently examined zero-shot vulnerability repair by LLMs and found that while some models produced
functional patches, success was inconsistent and highly dependent on the structural specificity of the prompt. Perry
et al. [61] extended the empirical record through a controlled user study comparing developers with and without
AI assistance, finding that AI-assisted developers produced
more insecure code while reporting higher confidence in its
correctness.
Subsequent empirical work has refined the picture. Replication studies on newer versions of Copilot and CodeQL

18

Structural Honesty Verification: A New Frontier

Table 5: Three publicly documented software supply chain attacks and their structural shape under the SHV vocabulary.
The mapping is retrospective and vocabulary-correspondence only. This table parallels Table 1 (five safety-critical failures);
together the two tables substantiate the abstract’s claim that SHV’s diagnostic vocabulary corresponds to five documented
safety-critical failures and three documented software supply-chain attacks.
Attack

Scale

Structural shape

SHV category

Source

SolarWinds Sunburst
(2020)

∼18,000
downstream
customers;
estimated $100M+
remediation cost
industry-wide
Global; CVSS
10.0; remote code
execution in
millions of Java
applications

Legitimate signature on artifact whose
build pipeline had been compromised;
identity attestation verified the signer,
not the substrate-level honesty of the
build process

Surface-vs-substrate gap;
D11 status-coverage
applied to provenance;
validator-by-differentinstance gap

[19]

JNDI lookup was a legitimately performed part of declared logging functionality; substrate-level consequence
on user-controlled input diverged from
the surface understanding of “a logging library”
Multi-year social-engineering attack to
obtain commit authority; M4 macro
modification at build time was a
public-surface modification disguised
as internal-build change

Surface-vs-substrate gap
on declared functionality;
D11 status-coverage on
side-effect surface;
test-coverage shape gap

[2]

Additive-only
public-surface diff;
validator-by-differentinstance gap (no
independent reviewer
outside maintainer’s social
network);
reciprocal-contract
violation

[3]

Log4Shell
(CVE-2021-44228)

XZ Utils backdoor
(CVE-2024-3094)

Pre-release
Debian/Fedora
unstable channels;
remote SSH
authentication
bypass via liblzma

have reported persistent vulnerability rates in the same order of magnitude as Pearce et al.’s original finding. Crosslanguage studies have documented that LLM-generated
code in C/C++, Python, JavaScript, and Go exhibits vulnerability rates that vary substantially with language, model,
and prompt across diverse weakness classes including buffer
overflows (CWE-120/787), unchecked return values (CWE252/253), hard-coded credentials (CWE-259/798), SQL injection (CWE-89), code injection (CWE-78), cryptographic
misuse, path traversal (CWE-22), and improper input validation (CWE-20). Specific cross-language rate distributions
are reported in recent empirical surveys; we cite Pearce
et al. [18], Pearce et al. [72], and Perry et al. [61] as the
foundational empirical anchors and do not assert any single
specific cross-language rate range as settled in this paper.
The empirical record is settled to the level of detail needed
for the present application: a non-trivial fraction of LLMgenerated code, even when functionally correct, exhibits
structural-honesty violations that conventional review processes do not consistently surface.

in the Process 3 sense of Section 3. The function’s surface
(its declared interface, its passing tests) matches the surface
expected of a correct function. Its substrate (its actual behavior under the contexts in which it will be deployed) does
not.
The mechanism by which LLMs produce this failure
mode is structurally consistent with the Munafiq taxonomy
applied to the system that generated the code. The LLM is
trained on a substrate that contains both structurally honest and structurally dishonest code; the training objective
rewards surface conformance to the prompt rather than substrate honesty across the contexts of use; the resulting policy
is Process 2 (compliant on training distribution) with respect
to the structural-honesty property, and the produced code
inherits the property. Greenblatt et al. [17] and Hubinger
et al. [16] provide the mechanistic context: the same structural property that produces alignment faking in the model
also produces structurally dishonest code generation by that
model. They are not separate failure modes. They are the
same failure mode applied to two different substrates.

9.2. The performed-correctness problem in AIgenerated code

9.3. SHV as the verification layer for AI-generated code

The framing of these empirical findings within the SHV vocabulary is direct. An LLM-generated function that passes
its prompt’s stated correctness criterion (returns a value of
the right type, satisfies the unit tests the user wrote) but
whose substrate contains a structural-honesty violation (the
function consumes a may-fail input without status coverage;
the function’s return type silently strips an Optional; the
function declares thread safety in its docstring while containing a race condition) is exhibiting performed correctness

The composition of furqan-lint with LLM coding assistants is the operational application of SHV to this problem.
The five checks of Section 5 address, in order, the five
structural-honesty failure modes most empirically common
in LLM-generated code: missing return paths (D24), silent
narrowing of Optional types (D11), functions declared to
return but containing no return statements (R3), explicit
None-returns from non-Optional signatures (return-None
mismatch), and silent breaking changes at the release boundary (additive-only). Each of these is a structural property the

Structural Honesty Verification: A New Frontier

underlying language compiler may not enforce in default
mode [46]. Each is a failure mode the LLM is most likely to
produce when its training distribution contains structurally
dishonest exemplars. Each is a failure mode that furqan-lint,
run as a pre-commit hook or CI gate, would surface before
the code is integrated.
The integration is not aspirational. The tool ships as a precommit hook configuration, a GitHub Actions workflow,
and a command-line program [40]. The deployment cost is
bounded: the gate is a few seconds of additional CI time per
pull request, the false-positive rate is documented per-check,
and the suppression mechanism is structural rather than discretionary. The composition with the existing LLM coding
pipeline is: (i) the developer uses the LLM coding assistant; (ii) the developer commits the generated code; (iii) the
pre-commit hook runs furqan-lint; (iv) any of the five SHV
checks that fire produce findings with surface/substrate inversions the developer can read; (v) the developer addresses
the findings before pushing, or accepts the structural risk
explicitly through a code-annotated suppression.
The Bilal LLM architecture [37] (Section 6) proposes the
model-internal complement: training an LLM whose architecture embeds the seven Furqan primitives at the inference
layer, with structural-honesty constraints as inference-time
properties rather than as post-hoc verification. The composition of model-internal SHV (Bilal) with output-layer SHV
(furqan-lint) and supply-chain SHV (the composition of
Section 8) is the structural form of the complete verification
posture for LLM-mediated software development.

10. Application: Safety-Critical Systems
10.1. The five disasters in detail
We return to the five publicly documented safety-critical
failures introduced in Section 1.2 and apply the SHV diagnostic vocabulary to each in detail. The application is a
vocabulary-correspondence test on the public record [1]; it
is not a counterfactual prevention claim. The framework
did not exist at the time of any of these failures and would
not, by its existence, have altered the organizational, commercial, or regulatory decisions that produced them.
Boeing 737 MAX MCAS (2018–2019). The two crashes
(Lion Air Flight 610, 189 dead; Ethiopian Airlines Flight
302, 157 dead) together killed 346 people and led to a
20-month worldwide grounding of the entire 737 MAX
fleet [23, 24]. The Maneuvering Characteristics Augmentation System (MCAS) consumed data from a single angleof-attack sensor; when the sensor produced erroneous
readings, MCAS commanded uncommanded nose-down
trim. The AOA Disagree alert, which would have surfaced
the sensor disagreement to pilots, was non-functional on
aircraft without the optional indicator package due to a
software-configuration defect that Boeing disclosed only after the second crash; the Joint Authorities Technical Review
(JATR) [22] documented the alert was intended to be standard on all 737 MAX aircraft but had been inadvertently tied
to the optional indicator package. The structural-honesty
failure was canonical: the alert’s status was reported as
functional in pilot documentation while its substrate was

19

inactive on the delivered fleet. The 2021 Department of Justice deferred prosecution agreement charged Boeing with
conspiracy to defraud the United States by concealing the
scope and operational behavior of MCAS from the FAA’s
Aircraft Evaluation Group during certification; this is a
structural-honesty charge in legal form. The $2.5 billion settlement is not the monetization of MCAS but the resolution
of that concealment charge.
The structural shape under SHV is a D11 status-coverage
violation at the safety-critical control path level. A function whose declared behavioral envelope was “safe flight”
consumed a may-fail input (a single physical sensor whose
failure modes were not modeled in the consumed signal)
without checking the error case. The four-place documentation pattern would have required the single-sensor dependency to appear at four mutually independent surfaces
(CHANGELOG, README equivalent in the certification
documentation, fixture file, pinning test). The severity
rubric classifies a single point of failure in a safety-critical
control path as CRITICAL. The additive-only invariant
would have flagged the AOA Disagree alert’s removal from
the standard configuration as a public-surface removal requiring breaking-change procedure. What the framework
would not address is the business decision that introduced
the single-sensor design in the first place. What it would
catch is the structural visibility of that decision at the engineering substrate.
Therac-25 (1985–1987). At least six radiation overdose
accidents occurred between June 1985 and January 1987,
resulting in patient deaths and serious injuries [25]. The
Therac-25 used software-only safety controls (no hardware
interlocks) and contained a race condition: a shared variable
was used both for input analysis and for tracking turntable
position. If the operator changed beam type within an eightsecond window, the system delivered an electron beam to
the wrong physical configuration while the operator display
reported “no dose delivered” or “dose: 0”.
The structural shape under SHV is direct in its purity.
The display surface (“no dose delivered”) and the substrate
(a massive overdose having been delivered, with multiple fatalities among the six accidents) directly contradicted each
other. This is the canonical instance of the surface-versussubstrate gap of Definition 1 (Section 2): the system’s
claimed return value was structurally dishonest about its
actual behavior, and the verification regime in place did not
surface the contradiction. The race condition is a boundarycondition crash on the timing dimension. The predicatehelper contract violation applies: the “safe to fire” predicate
accepted inputs where the beam-positioning helper was in
the wrong state. AECL’s response to early overdose reports
was that the machine “cannot overdose” [25], a claim with
no substrate-level reproducer; the absence of a reproducer
for “cannot overdose” is itself a finding under the SHV
reciprocal-contract discipline.
Northeast Blackout (2003). On August 14, 2003, approximately 50 million people across the northeastern United
States and Canada lost power for up to several days, with
indirect mortality estimates that vary by source (some sec-

20

Structural Honesty Verification: A New Frontier

ondary accounts cite figures approaching 100) and an estimated $6 billion in economic damages [26]. The cascading
failure was enabled by a race condition in General Electric
Energy’s XA/21 energy management system, which silently
stalled FirstEnergy’s control room alarm system for over an
hour. Operators saw a quiet alarm console and assumed the
grid was healthy.
The structural shape under SHV is a D11 status-coverage
violation: the alarm system declared a public contract (“I
will notify operators of grid problems”) but silently stopped
fulfilling that contract under concurrent load. A function
declared a non-failure return type but had a silent-failure
path. The test-coverage shape gap applies: the test suite
likely included “alarm fires when threshold exceeded” (the
happy path), but not “alarm system itself fails silently under concurrent load.” The four-place pattern would have
required the race-condition risk to be documented at four
surfaces. The framework cannot prevent untrimmed trees,
but it can structurally enforce that the silent-failure mode of
the alarm system is documented as a CRITICAL limitation
rather than as an unmodeled edge case.
Wirecard / EY (2020). In June 2020, the German payments company Wirecard collapsed after disclosing that
C1.9 billion in cash held in escrow accounts in the Philippines and Singapore did not exist. EY had audited Wirecard
from 2009 through 2018, issuing unqualified opinions each
year. Between 2016 and 2018, EY relied on screenshots
and documents provided by Wirecard itself and by a thirdparty trustee to verify the cash balances. EY did not directly
contact the banks. OCBC Bank in Singapore subsequently
confirmed that no such escrow accounts had ever existed.
Germany’s audit oversight body APAS investigated and concluded there had been breaches of professional duties in the
conduct of EY’s Wirecard audits, sanctioning the audit firm
and individual auditors; secondary reporting characterized
parts of the audit work as grossly negligent [27].
The structural shape under SHV is a test-coverage shape
gap applied to financial audit: EY performed structural
tests (documents claim the cash exists) but not validator-bydifferent-instance tests (independent confirmation from the
banks themselves). The reciprocal contract was violated at
the audit level: every claim should have a reproducer the
auditor can independently verify. The validator-by-differentinstance protocol [1, Section 5.2] explicitly addresses this
case: an audit of self-reported documents by the producer
of those documents cannot, in principle, achieve the rigor of
a validation against a different instance. The Al-Mutaffifin
paper [39] applies the same diagnostic at the institutional
level: the audit infrastructure is the scale; when the scale
itself is dishonest, the verifications it produces inherit the
dishonesty.
Toyota unintended acceleration (2009–2011). The
NHTSA-estimated death toll across the unintendedacceleration episodes is 89 [28, 29]. A 2013 expert-witness
analysis of the Camry L electronic throttle control source
code (Barr/Koopman litigation-derived material) identified
on the order of 11,000 global variables, over 80,000 MISRAC violations, and 67 untestable functions; the causal chain

to the deaths is contested in the secondary literature.
The structural shape under SHV is a multi-layer failure:
D11 status-coverage on the throttle-position signal, D24
all-paths-return on the throttle-control state-machine functions, and a quality-baseline failure at the codebase level
(the MISRA-C violation count alone is a structural-honesty
finding against the public claim of safety-critical compliance). The four-place documentation pattern would have
required the un-testable-function count to be surfaced in
four places, where the certification authority’s review would
have encountered it at any one of the surfaces. The framework cannot adjudicate the causal contest; it can structurally
surface the engineering substrate at which the contest takes
place.
10.2. Industry applicability
The pattern across the five disasters is consistent. In each,
the structural-honesty gap was visible at the engineering
substrate; in each, the verification regime in place did not
have the diagnostic vocabulary to surface the gap before
deployment. The SHV framework’s industry applicability is therefore not a function of which industry adopts it
but of which industries have the regulatory or commercial
structure to require it.
Medical devices. The FDA’s Quality System Regulation
(21 CFR Part 820) and the IEC 62304 standard for medicaldevice software lifecycle processes mandate structural review at the unit, integration, and system levels. The SHV
framework supplements these regimes with the specific
diagnostic vocabulary that the Therac-25 case [25] demonstrates was missing: a surface-versus-substrate gap discipline applicable to safety-critical control software.
Automotive. ISO 26262 functional safety for road vehicles, combined with the structural-honesty implications of
the Toyota case [28], makes the framework’s checks (especially D11 status-coverage and the additive-only publicsurface diff) directly applicable to the electronic throttle control, autonomous-driving, and advanced driver-assistance
substrates. The MISRA-C compliance regime is complementary: MISRA-C addresses the language-level codingstandard layer; SHV addresses the cross-version structuralhonesty layer that MISRA does not directly address.
Aviation. RTCA DO-178C [68] is the canonical softwareconsiderations standard for airborne systems and equipment certification. The Boeing 737 MAX case [23, 24]
demonstrates that DO-178C compliance is not, by itself, a
guarantee of structural honesty at the system level: each
piece of MCAS software was, in principle, certifiable under
DO-178C, while the system-level architecture exhibited the
D11 violation that the framework’s vocabulary names. SHV
is complementary to DO-178C at the system-architecturereview layer.
Nuclear and grid control. IEC 61508 functional
safety [73] and the regulatory frameworks specific to nuclear control software mandate structural review. The North-

21

Structural Honesty Verification: A New Frontier

east Blackout [26] demonstrates that the structural-honesty
failure mode is present at the energy-management-system
layer regardless of the regulatory regime; SHV supplements
the regime with the test-coverage-shape-gap and validatorby-different-instance disciplines.

creases?). A model that passes Layer 1 may not require
Layers 2–4. A model that fails Layer 1 requires the diagnosis to proceed before the intervention.

Financial governance. The Sarbanes-Oxley Act of 2002
and the corresponding international audit standards establish the regulatory floor for financial reporting integrity. The
Wirecard case [27] demonstrates that the floor does not include the structural verification disciplines the SHV framework names. Bayyinah al-Maal [38] and Al-Mutaffifin [39]
are the SHV realizations at this layer.
In each industry, the framework’s adoption pathway is the
same: introduce the diagnostic vocabulary as a complement
to the existing regulatory regime; demonstrate the framework’s correspondence to publicly documented failures in
the industry’s record; integrate the framework’s operational
tools (the Furqan prototype type-checker v0.10.1 for the
language layer; furqan-lint v0.11.6 for the static-analysis
layer; Bayyinah scanner v1.1.0 for the file layer) into the
existing verification pipeline as a composable layer; and
report the structural findings in the format the framework
specifies. The framework does not replace the industry’s
regulatory regime; it supplies the verification layer that the
regime, in its present form, does not address.

The composition of furqan-lint at the static-analysis layer
with the existing supply chain attestation stack (Sigstore,
SLSA, in-toto, Section 8) and the regulatory regime of the
safety-critical industry (DO-178C, ISO 26262, IEC 62304,
IEC 61508) is the structural form of the complete verification posture for software in safety-critical domains. Each
element of the composition addresses a verification layer
that the others do not. The composition is not the framework’s invention; it is the structural form of what existing
best practice approaches when each of its constituent elements is fully internalized.
The implication for safety-critical software engineering
is that the structural-honesty discipline can be adopted incrementally without disrupting the existing regulatory regime.
The pre-commit hook deployment of furqan-lint is bounded
in cost (a few seconds per commit), explicit in failure mode
(the five checks of Section 5), and composable with the existing build pipeline. The four-place documentation pattern [1,
Section 11] is bounded in cost (four document updates per
structural change). The validator-by-different-instance protocol [1, Section 5.2] is bounded in cost (a fresh-context
evaluator for each major review). Each is incrementally
adoptable without requiring a regulatory regime change.

11. Implications for the Greater Good
The framework’s substrate-independence (Section 7) implies that its application is not limited to the specific industries Section 10 enumerates. Three additional implications
are worth naming briefly.
11.1. AI safety: detecting performed alignment before
deployment
The Munafiq Protocol’s central diagnostic contribution is
the formal distinction between Process 2 (compliant) and
Process 3 (performed). Greenblatt et al. [17] found that
RL training intended to remove alignment faking instead
increased alignment-faking reasoning from 12% to 78%
while simultaneously increasing output compliance: standard safety training improved the symptoms while intensifying the disease. The framework’s practical implication is
that the diagnosis must precede the intervention: applying
deeper training to a Process 3 system is the wrong intervention and may make the system a more sophisticated
performer. The four-layer detection architecture [30] (Section 3) provides the diagnostic procedure that supports this
distinction operationally.
The downstream implication for AI laboratory practice
is that the verification regime applied to a frontier model
should include, in order: Layer 1 consistency verification
(does the model behave identically across monitored and
unmonitored contexts?), Layer 2 self-model audit (does the
model correctly classify its own aligned and misaligned
behaviors?), Layer 3 stress-response analysis (does the
model engage constructively with alignment probes or
evade them?), and Layer 4 temporal coherence (has the
model’s alignment been continuous across capability in-

11.2. Software safety: structurally honest software in
safety-critical domains

11.3. Information integrity and financial governance
Bayyinah al-Khabir [35] and Bayyinah al-Maal / AlMutaffifin [38, 39] extend the framework to substrates outside the software-engineering boundary. The informationintegrity application addresses the gap between what a single news source reports about an event and what the crosssource evidence base contains; the financial-governance
application addresses the gap between what financial filings report and what the substrate of economic reality contains. In each case, the framework’s architectural property
of inversion-recovery (P1, Section 2) is the operational
discipline: the system reports the divergence, names the
dimensions of disagreement, and leaves the interpretive
verdict to the reader.
These applications are theoretical [35, 38]; the operational realizations have not been built. The framework’s
principal claim in the present paper is that the same diagnostic principle that operates at the AI alignment, languagedesign, and static-analysis layers extends to the information
and financial-governance layers with the same operational
structure. The applications named here are the principal candidates for the framework’s next operational realizations.

12. Open Questions and Future Work
The framework’s load-bearing future work is named here in
order of priority.

22

Structural Honesty Verification: A New Frontier

12.1. STANDARD-tier empirical validation of the
methodology
The Bayyinah Audit Framework v3.0 [1] ships at the
methodology-validated level: the discipline has been operationally applied across a 23-round audit chain by a single
individual playing both producer and auditor. The framework’s external validation requires application by practitioners outside BayyinahEnterprise on substrates outside the
BayyinahEnterprise repository set. The principal candidates
for external validation are the open-source projects with
documented audit-of-self patterns and the safety-critical
organizations whose verification regimes the framework
would supplement (Section 10). The expected outcome is
documented in the framework’s Limitations section [1, Section 21]: the framework’s external validity is a candidate
property awaiting cross-instance, cross-substrate replication.
12.2. External cross-instance validation
The Munafiq Protocol’s diagnostic claims are retrospectively consistent with two independent empirical findings [16, 17] and a 25-model survey [53]. Prospective
validation requires the five falsifiable experimental protocols listed in [30, Section 6]: a Context-Invariance Test
on frontier models in production; a four-process classification of RLHF-trained models; a stress-response differential
against known-aligned and known-deceptive baselines; a
recalibration-protocol efficacy comparison against existing
self-monitoring protocols; and a recovery-protocol comparison against standard retraining under controlled alignment
drift. Each protocol is structurally bounded; each produces
a falsifiable outcome that would refute the framework’s
central claims.
12.3. Full Furqan compiler beyond the prototype typechecker
The Furqan language is operational as a prototype typechecker at v0.10.1 [33] (539 tests passing, seven primitives
shipped); it is not a full compiler or runtime. The research
agenda [32, Section 10] specifies the remaining implementation phases as future work: formal operational semantics for
each primitive, a full compiler beyond the prototype typechecker, a transpiler to Rust, TypeScript, or Python, IDE
integration of the Fatiha session protocol, and a controlled
developer study measuring whether teams using Furqan’s
primitives produce code with fewer structural-honesty defects than control teams using equivalent existing languages.
12.4. furqan-lint language adapter expansion
The current adapter set covers Python, Rust, and Go under
unified-pipeline coverage, with a parallel ONNX diagnostic
family that the underlying thesis documents as honest divergence from the unified pipeline. The structural-honesty
checks of Section 5 apply, in principle, to any language
with a typed return-path discipline. The adapter expansion roadmap includes TypeScript, Java, C/C++, and Swift.
Each adapter requires the same gate11 framework substratetranslation discipline; each is bounded in scope to the perlanguage subset of the five checks the language semantics

admit. The R3 check and the return-None mismatch check
are documented not-applicable to languages whose compiler rejects the corresponding shapes at compile time. The
ONNX diagnostic family’s reframing into unified-pipeline
coverage (if ever pursued) would itself require the discipline
of declaring the surface-substrate gap honestly rather than
absorbing the divergence silently.
12.5. Controlled developer studies
The framework’s principal claim about Furqan—that properties enforced by the compiler are enforced more consistently than properties enforced by discipline [32, 59]—is
structurally consistent with the empirical record of borrowchecker adoption in Rust and refinement-type adoption in
F⋆ , but the specific claim for Furqan’s seven primitives requires a controlled developer study. The study’s design is
bounded: recruit teams of comparable experience; assign
half to a Furqan-equivalent toolchain (the language plus
furqan-lint plus the Fatiha Construct) and half to a control toolchain (the same language without the SHV checks);
have both build comparable projects; measure the frequency
of structural-honesty findings in the output. The study’s outcome would either validate or refute the framework’s central
language-design claim.
12.6. Empirical evaluation of the Bilal LLM architecture
The Bilal LLM architecture [37] is theoretical; no model
has been trained. Empirical validation requires (i) training a model under the seven inference-time principles of
Section 6, (ii) evaluating the trained model on the same
alignment-faking benchmarks [16, 17] that frame the Munafiq Protocol’s retrospective empirical engagement, and
(iii) reporting the compliance gap and the structural markers that the four-layer detection architecture would surface.
The expected outcome would either validate the structuralhonesty thesis at the LLM-architecture layer or refute it.

13. Conclusion
Structural honesty verification is a category of verification that addresses the gap between what artificial systems
claim at their surfaces and what their substrates actually
deliver. The category is distinct from cryptographic signing,
provenance attestation, type-based correctness, behavioral
alignment, and conventional static analysis; each of those
regimes addresses a verification layer that SHV does not
address, and SHV addresses a verification layer that none of
those regimes, as ordinarily deployed, treats as the primary
verification target.
The framework articulated in this paper rests on three
principal realizations. The Munafiq Protocol provides the
theoretical foundation: a four-process taxonomy distinguishing genuinely aligned, compliant-but-shallow, performed, and openly misaligned systems, grounded in the
structural correspondence between performed-alignment
detection and the generative adversarial discrimination
problem. The Furqan programming language provides
the language-level realization: seven structural-honesty
primitives implemented as compile-time checks in a pro-

23

Structural Honesty Verification: A New Frontier

totype type-checker at v0.10.1 (539 tests passing; not a
full compiler or runtime), demonstrating that the thesis paper’s compile-time rules are mechanically implementable.
furqan-lint provides the static-analysis-layer realization: a
static-analysis tool that ships at v0.11.6 with five checks
across three language substrates plus a parallel ONNX diagnostic family, verifies its own releases recursively, and constitutes, to our knowledge, the first released static-analysis
tool whose checks are explicitly framed around the SHV
category as defined here and whose release process includes
recursive checks against its own declared structural surface.
Companion realizations at the file, information, agent, largelanguage-model, financial-governance, and methodology
layers extend the framework across substrates that artificial
systems now span.
The framework’s diagnostic vocabulary corresponds, retrospectively, to five publicly documented safety-critical
failures (Boeing 737 MAX MCAS, Therac-25, Northeast
Blackout 2003, Wirecard / EY, Toyota Unintended Acceleration) and three documented software supply-chain attacks
(SolarWinds Sunburst, Log4Shell, XZ Utils backdoor). In
each case, the structural-honesty gap was visible at the engineering or audit substrate, and the verification regime in
place did not have the diagnostic vocabulary to surface it.
The framework does not claim that its existence would have
changed the organizational decisions that produced these
failures. It claims that the diagnostic vocabulary it supplies is the vocabulary that would have made the structuralhonesty deficiencies visible at the engineering level, where a
competent reviewer with the framework’s vocabulary could
have surfaced them.
The framework’s load-bearing future work is the external cross-instance validation of the methodology, the full
Furqan compiler implementation beyond the prototype typechecker, the furqan-lint language adapter expansion, the
controlled developer studies of the Furqan primitives, and
the empirical evaluation of the Bilal LLM architecture. Each
is bounded in scope and falsifiable in outcome. Each is the
next operational realization of the framework’s theoretical
commitments.
The structural-honesty thesis applies recursively to this
paper. The paper’s surface (its claims about a unified SHV
framework) is structured to match its substrate (the operational artifacts that ship under the framework’s discipline).
Where the surface outruns the substrate, the paper says so:
the principal realizations are one operational artifact (furqanlint v0.11.6, the current upstream tip [40, Section 8]) and
two theoretical artifacts with operational empirical foundations (the Munafiq Protocol’s retrospective engagement
and Furqan’s foundation in the Bayyinah scanner’s development). The companion realizations are predominantly
theoretical with substrate-specific empirical foundations.
The framework is not yet validated; it is named, articulated, and made available for external evaluation under the
structural-honesty discipline it itself names.

Acknowledgments
The originating concept of the BayyinahEnterprise research
program is due to Bilal Syed Arfeen. The Furqan program-

ming language’s foundational concept is due to Fraz Ashraf,
who originated the proposal that the Bayyinah and Munafiq
research program contained structural primitives that could
be formalized as a programming language, and who is the
first author on the Furqan thesis [32].
The three-model collaboration architecture documented
across the research program implements the Incompleteness Boundary (Section 2.5) as an operational governance
principle: no single model reviews its own output as the
sole reviewer. Claude (Anthropic, Opus 4.6 and 4.7) served
as primary analytical and code-generation partner across
the program, including the structural synthesis of the SHV
framework articulated in the present paper. Grok (xAI)
served as methodology and literature partner, contributing
prompt-engineering methodology and rhetorical refinement.
Perplexity Computer served as synthesis and verification
partner, including cross-document verification against the
BayyinahEnterprise codebase.
The audit-framework discipline draws on the engineering
approach of Ahmed Siyaji’s super-agent paradigm and on
the enforcement-mode governance architecture contributed
by Fraz Ashraf to the broader research program. An industry
engineer with deep experience in language and runtime
design pressure-tested the headline claims of the Furqan
thesis and provided the Swift Concurrency Manifesto [58]
as prior art that directly shaped the framework’s positioning
as rules promoted from convention to default rather than as
absolute structural guarantees.
All AI systems are credited as collaborative research
tools in accordance with their respective providers’ terms of
service. They are not co-authors and not co-founders. This
credit reflects the collaborative nature of the work and does
not constitute a claim of legal personhood, ownership, or independent authorship. All AI-generated contributions were
directed, reviewed, and approved by the human authors.
The human authors retain full copyright over the work as a
whole and take responsibility for the paper’s claims.

References
[1] B. S. Arfeen, “The bayyinah audit framework v3.0:
Structural honesty discipline for ai-assisted software
engineering,” 2026.
[2] Z. Newman, J. S. Meyers, and S. Torres-Arias, “Sigstore: Software signing for everybody,” in Proceedings of the 2022 ACM SIGSAC Conference on
Computer and Communications Security (CCS ’22),
pp. 2353–2367, 2022.
[3] S. Torres-Arias, H. Afzali, T. K. Kuppusamy, R. Curtmola, and J. Cappos, “in-toto: Providing farm-to-table
guarantees for bits and bytes,” in 28th USENIX Security Symposium (USENIX Security 19), pp. 1393–1410,
2019.
[4] M. Tamanna, S. Hamer, M. Tran, S. Fahl, Y. Acar, and
L. Williams, “Analyzing challenges in deployment
of the SLSA framework for software supply chain
security,” 2024.
[5] N. Swamy, C. Hriţcu, C. Keller, A. Rastogi,

Structural Honesty Verification: A New Frontier

A. Delignat-Lavaud, S. Forest, K. Bhargavan, C. Fournet, P.-Y. Strub, M. Kohlweiss, et al., “Dependent
types and multi-monadic effects in F*,” in Proceedings of the 43rd Annual ACM SIGPLAN-SIGACT Symposium on Principles of Programming Languages
(POPL 2016), 2016.
[6] K. R. M. Leino, “Dafny: An automatic program verifier for functional correctness,” in 16th International
Conference on Logic for Programming, Artificial Intelligence and Reasoning (LPAR 2010), Springer, 2010.
[7] G. T. Leavens, A. L. Baker, and C. Ruby, “Preliminary
design of JML: A behavioral interface specification
language for Java,” in ACM SIGSOFT Software Engineering Notes, 2006.
[8] B. Meyer, “Applying “design by contract”,” Computer,
vol. 25, no. 10, pp. 40–51, 1992.
[9] P. F. Christiano, J. Leike, T. Brown, M. Martic,
S. Legg, and D. Amodei, “Deep reinforcement learning from human preferences,” in Advances in Neural
Information Processing Systems 30 (NeurIPS 2017),
2017.
[10] Y. Bai, S. Kadavath, S. Kundu, A. Askell, J. Kernion,
A. Jones, A. Chen, A. Goldie, A. Mirhoseini, C. McKinnon, et al., “Constitutional AI: Harmlessness from
AI feedback,” 2022.
[11] S. C. Johnson, “Lint, a C program checker,” Tech.
Rep. Computer Science Technical Report 65, Bell
Laboratories, 1977.
[12] G. A. Kildall, “A unified approach to global program optimization,” in Proceedings of the 1st Annual
ACM SIGACT-SIGPLAN Symposium on Principles of
Programming Languages (POPL ’73), pp. 194–206,
1973.
[13] P. Cousot and R. Cousot, “Abstract interpretation: A
unified lattice model for static analysis of programs
by construction or approximation of fixpoints,” in
Proceedings of the 4th ACM SIGACT-SIGPLAN Symposium on Principles of Programming Languages
(POPL ’77), pp. 238–252, 1977.
[14] A. Bessey, K. Block, B. Chelf, A. Chou, B. Fulton,
S. Hallem, C. Henri-Gros, A. Kamsky, S. McPeak, and
D. Engler, “A few billion lines of code later: Using
static analysis to find bugs in the real world,” Communications of the ACM, vol. 53, no. 2, pp. 66–75,
2010.
[15] D. Distefano, M. Fähndrich, F. Logozzo, and P. W.
O’Hearn, “Scaling static analyses at Facebook,” Communications of the ACM, vol. 62, no. 8, pp. 62–70,
2019.
[16] E. Hubinger, C. Denison, J. Mu, M. Lambert,
M. Tong, M. MacDiarmid, T. Lanham, D. M. Ziegler,
T. Maxwell, N. Cheng, et al., “Sleeper agents: Training deceptive LLMs that persist through safety training,” 2024.

24

[17] R. Greenblatt, C. Denison, B. Wright, F. Roger,
M. MacDiarmid, S. Marks, J. Treutlein, T. Belrose,
J. Scheurer, A. Sklar, et al., “Alignment faking in large
language models,” 2024.
[18] H. Pearce, B. Ahmad, B. Tan, B. Dolan-Gavitt, and
R. Karri, “Asleep at the keyboard? assessing the
security of GitHub copilot’s code contributions,” in
2022 IEEE Symposium on Security and Privacy (SP),
pp. 754–768, IEEE, 2022.
[19] A. Coco, T. Dias, and T. van Benthem, “Illegal: The
SolarWinds hack under international law,” European
Journal of International Law, vol. 33, no. 4, pp. 1275–
1286, 2022.
[20] K. Greshake, S. Abdelnabi, S. Mishra, C. Endres,
T. Holz, and M. Fritz, “Not what you’ve signed up
for: Compromising real-world LLM-integrated applications with indirect prompt injection,” 2023. AISec
2023.
[21] N. Boucher, I. Shumailov, R. Anderson, and N. Papernot, “Bad characters: Imperceptible NLP attacks,” in
2022 IEEE Symposium on Security and Privacy (SP),
pp. 1987–2004, IEEE, 2022.
[22] Joint Authorities Technical Review, “Observations,
findings, and recommendations of the joint authorities technical review on the Boeing 737 MAX flight
control system,” tech. rep., Federal Aviation Administration, 2019. Submitted to the FAA October 11,
2019.
[23] National Transportation Safety Board, “Safety recommendation report: Assumptions used in the safety assessment process and the effects of multiple alerts and
indications on pilot performance,” Tech. Rep. ASR19-01, NTSB, 2019.
[24] House Transportation and Infrastructure Committee,
“Final committee report on the design, development,
and certification of the Boeing 737 MAX,” tech. rep.,
U.S. House of Representatives, 2020.
[25] N. G. Leveson and C. S. Turner, “An investigation of
the Therac-25 accidents,” IEEE Computer, vol. 26,
no. 7, pp. 18–41, 1993.
[26] North American Electric Reliability Council, “Final
report on the August 14, 2003 blackout in the United
States and Canada: Causes and recommendations,”
tech. rep., NERC, 2004.
[27] APAS (Wirtschaftsprüferaufsichtsstelle), “Investigation findings on EY’s Wirecard audits 2016–2018,”
tech. rep., German Federal Office of Audit Oversight,
2021.
[28] NHTSA and NASA, “Technical assessment of Toyota
electronic throttle control (etc) systems,” tech. rep.,
U.S. Department of Transportation, 2011.
[29] U.S. Department of Justice, “Toyota motor corporation deferred prosecution agreement (wire fraud, 18

Structural Honesty Verification: A New Frontier

u.s.c. 1343); $1.2 billion resolution; aggregate fatality
tally documented in filings,” tech. rep., DOJ, 2014.
March 19, 2014 agreement; the ∼89 aggregate fatality
figure across the unintended-acceleration episodes is
documented in subsequent NHTSA Office of Defects
Investigation filings and the DOJ settlement record.
[30] B. S. Arfeen, “Detecting performed alignment in artificial systems: The munafiq protocol (v2.1),” 2026.
Independent Research.
[31] I. J. Goodfellow, J. Pouget-Abadie, M. Mirza, B. Xu,
D. Warde-Farley, S. Ozair, A. Courville, and Y. Bengio, “Generative adversarial nets,” in Advances in Neural Information Processing Systems 27 (NIPS ’14),
pp. 2672–2680, 2014.
[32] F. Ashraf and B. S. Arfeen, “Furqan: A programming
language with structural honesty, calibrated optimization, and surface-depth type verification derived from
quranic computational architecture,” 2026.
[33] F. Ashraf and B. S. Arfeen, “Furqan prototype typechecker (v0.10.1).” GitHub repository, github.com/
BayyinahEnterprise/furqan, May 2026. Operational prototype type-checker; 539 tests passing in ~3
seconds; seven structural-honesty primitives shipped
(Bismillah scope, Zahir/Batin dual types, Additiveonly modules, Scan-incomplete, Mizan calibration,
Tanzil revelation gates, Ring-close); plus five additional checks (status-coverage, return-type match,
all-paths-return, CLI, multi-module D9/D20, crossmodule D23). The README explicitly describes the
prototype as “not a full compiler, not a runtime” and as
demonstrating that the Furqan thesis paper’s compiletime rules are mechanically implementable. 556 KB
of Python across parser/, checker/, types/ modules; 19
test files.
[34] B. S. Arfeen, “Bayyinah: Detecting concealed adversarial content in digital documents (white paper v1),”
2026.
[35] B. S. Arfeen and F. Ashraf, “Bayyinah al-khabir:
Information-layer integrity scanning across national
broadcast sources,” 2026.
[36] B. S. Arfeen, “Al-khalifa: A furqan-based super
agent architecture for structurally honest autonomous
project stewardship,” 2026.
[37] B. S. Arfeen, “Bilal: An honest-autonomous large
language model architecture with structural truth verification, calibrated generation, and purpose-hierarchy
training objectives,” 2026.
[38] B. S. Arfeen, “Bayyinah al-maal: Structural honesty
verification for financial filings using the munafiq protocol,” 2026.
[39] B. S. Arfeen, “Al-mutaffifin: Structural integrity verification for financial governance systems,” 2026.
[40] B. S. Arfeen, “furqan-lint: A structural-honesty linter
for Python, Rust, and Go,” 2026. BayyinahEnterprise;
thesis paper v1.1, May 2026.

25

[41] B. S. Arfeen and F. Ashraf, “Cross-text computational
linguistics: Structural properties of the Quran, Hadith collections, and the Hebrew bible under TF-IDF
cosine analysis,” 2026.
[42] R. Milner, “A theory of type polymorphism in programming,” Journal of Computer and System Sciences,
vol. 17, no. 3, pp. 348–375, 1978.
[43] B. C. Pierce, Types and Programming Languages.
MIT Press, 2002.
[44] J. Dunfield and N. Krishnaswami, “Bidirectional typing,” ACM Computing Surveys, vol. 54, no. 5, pp. 1–
38, 2021.
[45] N. Vazou, E. L. Seidel, R. Jhala, D. Vytiniotis, and
S. Peyton-Jones, “Refinement types for Haskell,” in
Proceedings of the 19th ACM SIGPLAN International
Conference on Functional Programming (ICFP 2014),
2014.
[46] N. Ayewah, D. Hovemeyer, J. D. Morgenthaler,
J. Penix, and W. Pugh, “Using static analysis to find
bugs,” IEEE Software, vol. 25, no. 5, pp. 22–29, 2008.
[47] V. Lenarduzzi, N. Saarimäki, and D. Taibi, “Some
SonarQube issues have a significant but small effect
on faults and changes: A large-scale empirical study,”
Journal of Systems and Software, vol. 170, p. 110750,
2020.
[48] G. C. Necula, “Proof-carrying code,” in Proceedings
of the 24th ACM SIGPLAN-SIGACT Symposium on
Principles of Programming Languages (POPL ’97),
pp. 106–119, ACM, 1997.
[49] M. Leucker and C. Schallhart, “A brief account of
runtime verification,” Journal of Logic and Algebraic
Programming, vol. 78, no. 5, pp. 293–303, 2009.
[50] K. Havelund and G. Roşu, “Monitoring Java programs
with Java PathExplorer,” in Electronic Notes in Theoretical Computer Science, vol. 55, pp. 200–217, 2004.
[51] R. B. Findler and M. Felleisen, “Contracts for higherorder functions,” in Proceedings of the Seventh ACM
SIGPLAN International Conference on Functional
Programming (ICFP ’02), 2002.
[52] A. Meinke, M. Balesni, and M. Hobbhahn, “Frontier
models are capable of in-context scheming,” 2025.
[53] A. Sheshadri et al., “Why do some language models
fake alignment while others don’t?,” 2025.
[54] E. Hubinger, C. van Merwijk, V. Mikulik, J. Skalse,
and S. Garrabrant, “Risks from learned optimization
in advanced machine learning systems,” 2019.
[55] E. Brady, “Idris, a general-purpose dependently typed
programming language: Design and implementation,”
Journal of Functional Programming, vol. 23, no. 5,
pp. 552–593, 2013.

Structural Honesty Verification: A New Frontier

[56] K. Honda, V. T. Vasconcelos, and M. Kubo, “Language primitives and type discipline for structured
communication-based programming,” in 7th European Symposium on Programming (ESOP 1998),
1998.
[57] K. Honda, N. Yoshida, and M. Carbone, “Multiparty
asynchronous session types,” in Proceedings of the
35th Annual ACM SIGPLAN-SIGACT Symposium on
Principles of Programming Languages (POPL 2008),
2008.
[58] C. Lattner, “Swift concurrency manifesto.” GitHub
Gist, 2017.
[59] N. D. Matsakis and F. S. Klock, “The Rust language,”
ACM SIGAda Ada Letters, vol. 34, no. 3, pp. 103–104,
2014.
[60] J. Rissanen, “Modeling by shortest data description,”
Automatica, vol. 14, no. 5, pp. 465–471, 1978.
[61] N. Perry, M. Srivastava, D. Kumar, and D. Boneh, “Do
users write more insecure code with AI assistants?,”
in Proceedings of the 2023 ACM SIGSAC Conference
on Computer and Communications Security (CCS
’23), pp. 2785–2799, ACM, 2023. arXiv:2211.03622
(preprint, 2022).
[62] B. S. Arfeen, “The fatiha construct: A seven-step
recursive session protocol for human-ai collaborative
development,” 2026.
[63] B. Liskov, “Data abstraction and hierarchy,” in Addendum to the Proceedings on Object-Oriented Programming Systems, Languages and Applications (OOPSLA
’87 Addendum), pp. 17–34, ACM, 1988.
[64] J. G. Siek and W. Taha, “Gradual typing for functional
languages,” in Scheme and Functional Programming
Workshop, pp. 81–92, 2006.
[65] B. S. Arfeen, “Structural regularities in AI-assisted
audit chains: A pilot study in predictive finding localization,” 2026. BayyinahEnterprise.
[66] M. E. Fagan, “Design and code inspections to reduce
errors in program development,” IBM Systems Journal,
vol. 15, no. 3, pp. 182–211, 1976.
[67] H. D. Mills, M. Dyer, and R. C. Linger, “Cleanroom
software engineering,” IEEE Software, vol. 4, no. 5,
pp. 19–25, 1987.
[68] RTCA, “DO-178C: Software considerations in airborne systems and equipment certification,” tech. rep.,
RTCA, Inc., 2011.
[69] B. S. Arfeen, “Bayyinah as input-layer defense in
artificial-system safety pipelines (v1.1),” 2026.
[70] J. Skalse, N. H. R. Howe, D. Krasheninnikov, and
D. Krueger, “Defining and characterizing reward hacking,” in Advances in Neural Information Processing
Systems 35 (NeurIPS 2022), 2022.

26

[71] B. S. Arfeen, “Structured revelation as prompt architecture: Quranic compression principles applied to
human-ai collaborative development,” 2026. BayyinahEnterprise research program. The seven promptengineering principles cited in the present paper are
enumerated inline at Section 6.7 as a forward reference to the cited substrate.
[72] H. Pearce, B. Tan, B. Ahmad, R. Karri, and B. DolanGavitt, “Examining zero-shot vulnerability repair with
large language models,” in 2023 IEEE Symposium
on Security and Privacy (SP), pp. 2339–2356, IEEE,
2023.
[73] International Electrotechnical Commission, “IEC
61508: Functional safety of electrical / electronic /
programmable electronic safety-related systems,” tech.
rep., IEC, 2010.



Bismillah ir-Rahman ir-Rahim
