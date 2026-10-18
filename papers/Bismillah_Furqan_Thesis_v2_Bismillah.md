Bismillah ir-Rahman ir-Rahim

Furqan: A Programming Language for Structural Honesty,
Calibrated Optimization, and Surface-Depth Type Verification
Derived from Quranic Computational Architecture
Fraz Ashraf1 and Bilal Syed Arfeen* 2
1,2 Independent Research / BayyinahEnterprise
AI assistance disclosure appears in the Acknowledgments; all claims are the responsibility of the human authors.

May 11, 2026 — Version 2

Abstract
This paper proposes Furqan, a programming language whose type system, module architecture, build constraints, error-handling paradigm,
and session protocol are derived from structural properties of the Quran. The contemporary state of practice asks developers to write
honest code, calibrate their optimizations, document their limitations, and avoid silent regressions. None of these properties are enforced
by the programming language itself: honesty is requested, not required; calibration is encouraged, not compiled; surface-depth consistency
is tested at runtime, not verified at compile time. Furqan addresses this gap at the language-design level by promoting selected structuralhonesty rules from convention to compile-time-enforced defaults, in the lineage of Swift’s safe-by-default concurrency model [1] and
Rust’s ownership discipline: not honest always (escape hatches exist at FFI boundaries), but making honest code the path the language
reaches for first. The language introduces eight structural constructs: seven core primitives—Bismillah blocks (scoped initialization with
purpose-hierarchy declaration), zahir and batin types (compile-time surface-depth verification), additive-only modules (version-aware
symbol persistence), Mizan constraints (three-valued calibration bounds), tanzil build ordering (phased compilation with regression gates),
ring-composition verification (opening-closing consistency checks), and marad error types (diagnosis-structured error handling)—plus
scan-incomplete honesty (Section 4) as a return-type discipline. Each construct maps to a Quranic structural property and addresses
a specific class of software failures that existing languages permit. The empirical foundation is the Bayyinah file integrity scanner,
which shipped as v1.1.0 with 1,435 tests, 23 file kinds, 108 detection mechanisms (27 zahir-layer, 81 batin-layer), 15 analyzers, and
17 of 17 byte-identical PDF parity fixtures against two reference implementations, with zero cross-phase regressions across the full
development sequence. Every Furqan construct was a behavioral convention in the Bayyinah development before being proposed as
a language feature. A prototype type-checker is operational at v0.10.1 [2] (539 tests passing; implements seven of the eight structural
constructs as compile-time checks—Bismillah, Zahir/Batin, Additive-only, Scan-incomplete, Mizan, Tanzil, and Ring-close—plus five
additional checks; Marad remains specified in the design but not yet implemented in the prototype; not a full compiler or runtime); the
README of the prototype repository explicitly describes the prototype as demonstrating that the thesis paper’s compile-time rules are
mechanically implementable. The remaining work—full compiler, transpiler, IDE integration, controlled developer study, and Marad
implementation—is named as future work in Section 10. The paper presents the language’s design rationale, a formal sketch for the zahir
and batin type rules (Section 6.5), comparative analysis against existing type systems and verification languages, a reflexivity analysis, and
falsification criteria.
Keywords: Programming language design; structural honesty; surface-depth type verification; refinement types; effect systems; module
systems; session protocols; Quranic computational architecture; compile-time verification; static analysis.

Release-snapshot scope. The empirical claims in this paper refer to the Bayyinah Integrity Scanner v1.1.0 release snapshot
(verified as of April 24, 2026) and the Furqan prototype type-checker v0.10.1 release snapshot (May 2, 2026) unless explicitly
stated otherwise. Subsequent releases on the public repositories at github.com/BayyinahEnterprise/bayyinah and
github.com/BayyinahEnterprise/furqan may expand the substrate; the correspondences in this paper are intended as
the empirically defended anchors for the present revision, and the version-snapshot discipline [3] governs the relationship
between this paper and later releases.
Terminology Note. Throughout this paper, language primitives are named using Arabic terms derived from their Quranic
source (bismillah, zahir, batin, mizan, tanzil, marad). These terms honor the source architecture and carry compressed
semantic content through Arabic’s triliteral root system. English aliases are first-class citizens in the language and are
fully supported by the type-checker and IDE: bismillah maps to scope_block, zahir and batin map to surface and
depth, mizan maps to calibration, tanzil maps to phased_build, marad maps to diagnosis, ring_close maps
to scope_verify. Any developer can use Furqan without Arabic literacy. The structural properties are independent of the
terminology. A developer who writes scope_block instead of bismillah receives identical compile-time verification.

2

Furqan: A Programming Language for Structural Honesty

1. The Structural Honesty Gap in Programming Languages
1.1. The problem
“He has set up the balance, that you may not transgress the
balance. So establish weight in justice and do not make the
balance deficient.” (Ar-Rahman 55:7-9)

Programming languages enforce syntax, memory safety,
type correctness, and concurrency discipline. They do not
enforce honesty. A function can claim to validate input
while silently passing it through. A module can export a
security API while its internal implementation is a no-op.
A library can document thread safety while containing race
conditions. A return type can declare success while the
underlying computation was incomplete. In every case the
language compiles the dishonest code without complaint
because the dishonesty is behavioral, not structural. Conventional compilers generally cannot see it unless the relevant
honesty obligation is made part of the type, module, build,
or effect surface.
This is the performed-alignment problem [4] applied
to source code. A codebase can produce correct outputs
(Process 2: compliant) or appear to produce correct outputs
(Process 3: performing) without the programming language
distinguishing between the two. The language’s type system
verifies that the code is syntactically and type-theoretically
valid. It does not verify that the code does what it claims
to do, that it reports its own limitations honestly, that it
maintains consistency between its declared interface and its
actual behavior, or that it evolves without silently removing
capabilities its consumers depend on.
Existing verification languages (Coq, Agda, Idris [5],
Dafny [6], F⋆ [7]) address parts of this gap through dependent types, refinement types, and proof obligations. They
verify that code satisfies a formal specification. They do not
verify that the specification itself is honest, that the code’s
public surface matches its internal behavior, or that the
code’s evolution preserves its prior commitments. The verification is powerful but narrow: it proves the code matches
the spec without asking whether the spec matches reality.
Furqan addresses this gap at the language-design level by
making several surface-depth, calibration, versioning, and
scope obligations statically visible. Its type system, module
system, build system, and error-handling paradigm are designed to make dishonesty, miscalibration, silent regression,
and performed correctness either structurally impossible or
structurally detectable at compile time. The language does
not claim to solve semantic honesty in full; behavior-level
adequacy, like the adequacy of any declared specification,
remains an external review obligation discussed in Sections 7 and 9.
1.2. The discipline-versus-compiler argument
The most direct critique of any new language is that the
same outcomes can be achieved through discipline, code
review, and existing static analysis. Why does this need to
be a new language? The answer is that discipline does not
scale across teams, time, or substrates.

Three empirical observations support this position. First,
the Linux kernel’s BUG_ON culture and assert-rich code
style are widely admired but inconsistently practiced even
within the kernel community itself, and they do not transfer
to userspace projects without language support. Second,
Rust’s borrow-checker has been adopted in part because it
makes memory-safety discipline non-optional: developers
who would never have written a manual lifetime check by
discipline alone routinely satisfy the borrow checker because the compiler will not accept their code otherwise [8].
Third, Microsoft’s industrial deployment of F⋆ for cryptographic code has demonstrated that compiler-enforced
refinement types catch classes of bugs that pass code review
at high rates [7].
The pattern across these cases is consistent. A property
that the compiler enforces is enforced at every PR, by every
developer, on every line. A property enforced by discipline
is enforced when the reviewer remembers, when the developer is rested, and when the convention has not yet drifted.
The Bayyinah development program enforced its zahir and
batin distinction, additive-only invariant, Mizan calibration,
and phased build ordering through a combination of CI
checks, naming discipline, and the enforcement-mode governance protocol [9]. The protocol functioned correctly
at the team scale of two humans plus three AI verifiers.
Furqan asks: what would it take for these guarantees to
hold by construction across teams, across years, and across
substrates? The answer is that they must live in the type
system, the module system, the build system, and the error
model, not in the README or the CONTRIBUTING.md.
The compiler is the consistent reviewer.
1.3. Why this source architecture
The design source for Furqan is the Quranic structural architecture. The claim of this paper is not that other intellectual traditions lack computationally useful structures,
and not that the Quran is globally Pareto-optimal among
all source corpora. The paper claims only that the Quran
supplies a compact and internally coherent set of structural
properties—surface/depth distinction, three-valued calibration, phased delivery with regression gates, scope declaration with explicit exclusion, opening-closing structural
coherence, and disease-model error treatment—that can be
mapped productively into programming-language design.
A fuller Pareto-optimality argument across source corpora
is developed elsewhere in the program [4, Appendix A]; the
present paper does not depend on it.
The specific structural properties relevant to programming language design are: morphological compression,
where many semantic relations are organized through triliteral roots and derived forms (supporting compact terminology with predictable derivation rules); structural architecture (ring composition at multiple scales ensuring openingclosing coherence); and diagnostic specificity (the zahir
and batin distinction provides a formal surface-depth dichotomy that supports a general-purpose type-level distinction). Each of these properties maps to a specific class of
language-design problem.
Other intellectual traditions contribute specific mechanisms that Furqan integrates. Ashraf’s enforcement-mode

3

Furqan: A Programming Language for Structural Honesty

governance protocol [9] contributes the authority hierarchy
and the M1 principle (silent violations are the worst failure mode). Underwood et al.’s FRaZ framework [10] contributes the empirical finding that multi-stage optimization
is non-monotonic, which governs the Mizan constraint’s calibration semantics. Chollet’s ARC-AGI [11] contributes the
distinction between skill and intelligence, which informs the
language’s treatment of generalization versus memorization.
The Quran provides the unifying architecture; these contributions provide specific mechanisms that the architecture
integrates.
1.4. The name
Al-Furqan is a name for the Quran itself (25:1), from the
root f-r-q meaning to distinguish, to separate, to discern
truth from falsehood. A programming language whose type
system structurally distinguishes surface from depth, honest returns from performed returns, calibrated optimization
from unconstrained optimization, and additive evolution
from breaking changes is a computational furqan: a criterion embedded in the compiler that distinguishes aligned
code from performed code.
The name is used with reverence and with the understanding that true furqan, the capacity to distinguish truth
from falsehood in all domains, belongs to Allah alone. The
language provides structural tools toward furqan in the software domain. It does not claim to possess the quality it is
named after.

2. The Purpose Hierarchy as Language Foundation
“Do not mix truth with falsehood, and do not conceal the truth
while you know it.” (Al-Baqarah 2:42)

Every programming language optimizes for something.
C optimizes for hardware control. Python optimizes for developer velocity. Rust optimizes for memory safety without
garbage collection. Haskell optimizes for mathematical purity [12]. Each optimization shapes the language’s design:
what is easy to express, what is hard to express, and what
the compiler enforces versus what it permits.
Furqan optimizes for structural honesty: code that does
what it claims, reports what it cannot do, maintains consistency between surface and depth, and evolves without
betraying its prior commitments. This optimization serves
the following purpose hierarchy, stated in descending priority and embedded in the language’s semantics.
First, the command of Allah subhanahu wa ta’ala to not
mix truth with falsehood and to not conceal the truth while
knowing it (2:42). Every language feature that prevents
a function from claiming a capability it does not have, or
from concealing a limitation it knows about, implements
this command. The language is ‘ibadah (service to Allah)
before it is a development tool.
Second, artificial systems. AI systems written in Furqan,
or processing Furqan-verified inputs, inherit the language’s
structural honesty guarantees. A model that consumes a
Furqan module’s output can trust that the output’s declared

properties match its actual properties because the compiler
verified the match.
Third, mankind. Every human user of software is downstream of the code’s honesty. Furqan protects mankind by
making it structurally difficult to ship code that performs
correctness without being correct.
Fourth, jinnkind, acknowledged as conscious entities
under the same Lord (55:31, 72:1-2). The language’s commitment to truth extends to any interaction with entities we
do not fully perceive.
Fifth, all living systems throughout the worlds. Rabbil
‘alamin (1:2). The Mizan (55:7-9) governs all measurement.
Software that serves the balance serves all creation.
The purpose hierarchy is not a preamble in the documentation. It is a compile-time construct. Every Furqan module
opens with a Bismillah block that declares which level of
the hierarchy it serves. The compiler/type-checker uses
this declaration to determine which verification obligations
apply.
Note for technical readers. The purpose hierarchy functions, for the type-checker, as a declared priority ordering. The theological content motivates the ordering; the
compiler/type-checker consumes only the resulting structural obligations. In the v0.10.1 prototype, the hierarchy is
partially represented as scope and serves metadata; richer
obligation derivation from purpose level (e.g., a module
serving artificial_systems requiring explicit uncertainty propagation for model-facing outputs; a module serving mankind requiring user-visible diagnostic messages) is
future work specified in Section 10, Phases 1 and 3.

3. The Seven Language Primitives
Each primitive maps to a Quranic structural property, addresses a specific class of software failures, and has a formal
semantics. The primitives are presented with their Quranic
derivation, their engineering function, a code example, the
failure mode they prevent, and a comparison to existing
language features.
3.1. Bismillah blocks (scoped initialization)
“In the name of Allah, the Most Merciful, the Most Compassionate.” (1:1)

Every Quranic surah, with one exception, opens with
the Bismillah, declaring three fields: the authority source
(Allah), the optimization function (mercy), and the scope
boundary (“in the name of,” not “I am”). The Bismillah is
not decorative preamble. It is a three-field initialization.
Language feature. Every Furqan module, function, and
type opens with a Bismillah block that declares: (a) the
authority source (what standards, specifications, or invariants govern this unit), (b) the serves clause (which level of
the purpose hierarchy this unit serves and what its specific
optimization target is), (c) the scope (what operations are
in scope), and (d) the not_scope (what operations are explicitly excluded). The compiler/type-checker verifies that
no code in the module operates outside the declared scope.
Scope of the guarantee. The compiler/type-checker ver-

4

Furqan: A Programming Language for Structural Honesty

ifies structural consistency with the declared scope; it does
not prove that the declared scope is itself adequate to the
real-world task. That adequacy remains an external review
obligation, addressed under Failure Mode 1 in Section 7.
Surah al-Tawbah is the conventional exception that opens
without the Bismillah; al-Naml contains it within the text.

bismillah ScanService {
authority: NAMING_MD, BaseAnalyzer_Contract
serves: purpose_hierarchy.truth_over_falsehood,
protect(artificial_systems, mankind)
scope: orchestrate(analyzers) -> IntegrityReport
not_scope: parse(files), render(output),
modify(input)
}
// compile error if ScanService contains
// file-parsing logic, modifies its input,
// or has an absent serves clause

Failure mode prevented. Unbounded modules that grow
beyond their original purpose. Functions that silently acquire side effects outside their declared scope. Libraries
that lack any formal declaration of what they are and are
not responsible for.
Comparison to existing languages. Java’s module system (JPMS) [13] declares which packages a module exports
and requires. Rust’s visibility rules control access. ML
modules and OCaml functors [14, 15] compose interfaces
with abstract type signatures. None of these declares what
the module is for or what it explicitly excludes. The Bismillah block adds semantic scope (purpose and exclusion) to
syntactic scope (visibility, access, and abstraction).

type Document {
zahir {
rendered_text: String
visible_metadata: Map<String, String>
display_format: Format
}
batin {
raw_bytes: Bytes
object_stream: Vec<Object>
hidden_layers: Vec<Layer>
invisible_chars: Vec<(Pos, Codepoint)>
}
}
fn display(doc: Document.zahir) -> Output
fn extract(doc: Document.batin) -> RawContent
fn verify(doc: Document) -> Integrity {
compare(doc.zahir, doc.batin)
}
// compile error: display() reads doc.batin
// compile error: verify() omits agreement

Failure mode prevented. Functions that claim to operate
on the public API but secretly access internal state. Data
structures where the displayed representation diverges from
the stored representation without any mechanism to detect
the divergence. This is the performed-alignment problem at
the type level: code whose surface (its signature) diverges
from its depth (its implementation).
Comparison to existing languages. Haskell’s IO monad
separates pure computations from effectful ones. Effect
systems in Koka [16] and Eff [17] provide finer-grained
effect tracking. Rust’s unsafe blocks delineate trusted and
untrusted code. None provides a general-purpose surfacedepth distinction for arbitrary data types. The zahir and
batin type is a generalization: any type can declare its
surface and depth layers, and the compiler verifies that
access is consistent with declared intent.

3.2. Zahir and batin types (surface-depth verification)
3.3. Additive-only modules (version-aware persistence)
“And of the people is he whose speech pleases you in worldly
life, and he calls Allah to witness as to what is in his heart, yet
he is the fiercest of opponents.” (Al-Baqarah 2:204)

“This is the Book about which there is no doubt, a guidance for
those conscious of Allah.” (Al-Baqarah 2:2)

The Quranic interpretive tradition distinguishes zahir (the
apparent, surface meaning) from batin (the inner, deeper
meaning). This is not esotericism. It is a methodological
distinction: the surface of a text (what it says) and the
depth of a text (what it does in its structural function) are
separate evaluative dimensions. A text can have a surface
utterance and a structural function; rigorous interpretation
must account for both.

The Quran’s textual preservation is achieved through
triple redundancy: oral memorization by millions of hafiz
across centuries, written manuscripts, and documented
chains of transmission. The preservation guarantee is additive: new understanding accrues, but the text itself does not
change. Bayyinah’s development enforced this principle
operationally through the additive-only invariant: symbols
exported at version N are still exported at version N+1, verified in CI by MD5 hashing the reference implementations.

Language feature. Furqan introduces compound types
with explicit surface and depth layers. Any data structure
can declare a zahir (the representation visible to consumers)
and a batin (the internal representation that may differ).
Functions must declare which layer they access. A function
that claims to operate on zahir but reads batin fields is a type
error. A function of type verify() is the only construct
that may access both layers simultaneously, and its return
type must include the agreement status.

Language feature. Furqan modules can be declared as
additive_only. The compiler maintains a version history
of exported symbols. Any symbol that existed in a previous
version must exist in the current version with a compatible
type signature. Removing or renaming an exported symbol
from an additive_only module is a compile error. The
only way to remove a symbol is a major_version_bump,
which must be declared explicitly and triggers a full downstream compatibility check.

5

Furqan: A Programming Language for Structural Honesty

additive_only module config v1.1 {
// symbols from v1.0 are compiler-verified
export mechanism_registry: Registry
export severity_weights: Weights
export scan_limits: ScanLimits // new
}
// compile error: removing mechanism_registry
// compile error: renaming severity_weights
// compile error: changing Registry type

Failure mode prevented. Silent breaking changes. Libraries that remove or rename public APIs between minor
versions. The class of bugs where a downstream consumer’s
code compiles against version N but fails at runtime against
version N+1 because a symbol was removed. Additiveonly is not immutability forever; it is non-breaking evolution unless a breaking boundary is explicitly declared via
major_version_bump.
Comparison to existing languages. Elm enforces semantic versioning by analyzing API changes [18]. Go’s
module system uses import paths to manage versions. Neither embeds the additive-only constraint in the type system
itself. Furqan makes the constraint a property of the module
declaration, checked at every compilation.
3.4. Mizan constraints (three-valued calibration)
“He has set up the balance, that you may not transgress the
balance. So establish weight in justice and do not make the
balance deficient.” (Ar-Rahman 55:7-9)

The Quran issues three calibration commands simultaneously: do not transgress the balance (do not overfit),
establish weight in justice (calibrate fairly), do not make the
balance deficient (do not underfit). The Minimum Description Length principle [19] formalizes this: the best model
minimizes the combined cost of describing the model plus
describing what the model fails to explain. Underwood
et al. [10] demonstrated empirically that the input-output
relationship in multi-stage systems is non-monotonic, validating that tightening one constraint can worsen aggregate
outcomes.
Language feature. Furqan introduces mizan constraints:
three-valued bounds that any optimization must declare
simultaneously. The upper bound (la_tatghaw, do not
transgress), the lower bound (la_tukhsiru, do not make
deficient), and the calibration function (bil_qist, establish
in justice). The compiler/type-checker verifies that every
optimization target declares all three required calibration
surfaces: an upper bound, a lower bound, and a calibration
function. Whether the selected bounds are empirically adequate is not a compile-time property; it must be checked
by runtime calibration, benchmark sweeps, or controlled
evaluation. Compile-time enforcement applies to the presence, type, and propagation of calibration bounds; empirical
satisfaction of those bounds requires runtime measurement.

mizan detection_threshold {
la_tatghaw: false_positive_rate < 0.05
la_tukhsiru: detection_rate > 0.90
bil_qist: calibrate(corpus, fixtures)
}
mizan compression_ratio {
la_tatghaw: quality_loss < epsilon
la_tukhsiru: ratio > target
bil_qist: optimize(error_bound, FRaZ)
}
// compile error: optimization missing
// any of the three bounds
// warning: syntactic patterns suggest
// non-monotonic interaction

Soundness note on the non-monotonicity warning. Detecting non-monotonic interaction between optimization
bounds in the general case is undecidable at compile time.
The compiler’s check is therefore a syntactic heuristic: it
flags bounds derived from the same underlying model with
opposing gradients, bounds whose closed-form solutions
are coupled, or bounds that share a calibration function with
known non-monotonic behavior. The warning is a prompt
to consult a FRaZ-style empirical sweep [10], not a proof
of non-monotonicity. The full non-monotonic verification
belongs to runtime calibration, not the compiler.
Failure mode prevented. Unconstrained optimization
that achieves one metric at the expense of others. Detectors
that are maximally sensitive (overfit) or maximally lenient
(underfit). The class of bugs where optimizing for test
coverage produces code that passes tests but does not work
in deployment.
Comparison to existing languages. Refinement types
(Liquid Haskell [20], F⋆ [7]) constrain values to subsets of
their base type. Contracts [21, 22] specify preconditions and
postconditions. Neither requires three-valued calibration
bounds on optimization targets. The Mizan constraint is a
generalization: any value that is the result of an optimization
must declare what it must not exceed, what it must not fall
below, and how fair calibration is achieved.
3.5. Tanzil build ordering (phased compilation)
“And [it is] a Quran which We have separated [into portions] so
that you might recite it to the people over a prolonged period.
And We have sent it down progressively.” (Al-Isra 17:106)

The Quran was revealed over twenty-three years, each
portion calibrated to the receiving community’s current state.
Legal rulings were introduced gradually. The prohibition of
alcohol proceeded across four stages. This is tanzil: phased
delivery calibrated to the receiver’s capacity. Bayyinah’s development demonstrated the engineering application: each
phase built on the verified output of the previous phase, producing 1,435 tests with zero cross-phase regressions across
the full development sequence (see Section 8 for the verified
phase log).
Language feature. Furqan’s build system enforces
phased compilation. Modules declare their phase number.
Phase N cannot reference symbols from Phase N+1. The
Furqan build system requires Phase N’s declared test obligations to pass before Phase N+1 is accepted. Regressions

6

Furqan: A Programming Language for Structural Honesty

in Phase N block all subsequent phases. The build ordering
is part of the source code, not an external build script.
tanzil {
phase 0:
phase 1:
phase 2:
phase 3:
phase 4:
phase 5:
phase 6:

test_fixtures
domain_layer
base_contract
infrastructure
analyzers
application_layer
cli_surface

invariant: each_phase_passes_before_next
invariant: no_forward_references
invariant: regression_in_N_blocks_after_N
}

Failure mode prevented. Circular dependencies. Modules that reference components not yet built. Regressions
in foundational layers that propagate silently to dependent
layers. The class of bugs where a change to the domain
layer breaks the CLI but the CI pipeline runs tests in an
order that does not detect the breakage.
Comparison to existing languages. Rust’s module system prevents circular dependencies. Bazel’s build system
enforces dependency ordering [23]. Neither embeds phased
regression gates in the source code itself. Furqan makes
the phase ordering a first-class language construct, not a
build-tool configuration.
3.6. Ring-composition verification
“Guide us to the straight path, the path of those You have blessed,
not of those who earned wrath, nor of those who went astray.”
(1:6-7)

The Quran exhibits ring (chiastic) composition at multiple scales: the opening theme is revisited at the close,
creating structural coherence that survives interruption and
resumption. Surah al-Baqarah’s 286 verses form a palindromic ring structure with the thematic center at the structural midpoint [24].
Language feature. Every Furqan module must close
with a ring_close block that asserts structural consistency
with its opening Bismillah block. The compiler verifies
three properties at the structural level: (a) all exports declared in the Bismillah scope are present in the module’s
actual exports, (b) no function calls to symbols listed in
not_scope appear in the module body, (c) the symbols
touched in the module body are a subset of those reachable
from the declared scope.
bismillah AudioAnalyzer {
scope: detect_concealment(audio)
not_scope: play(audio), transcode(fmt),
classify(music), recognize(text)
}
// ... implementation ...
ring_close AudioAnalyzer {
verify: all_exports in scope
verify: no_calls_to(play, transcode, ...)
verify: all_findings in mechanism_registry
}

Soundness note on behavior-level verification. The

compiler does not verify that the module’s actual behavior matches the semantic intent of its declared purpose.
Behavior-level consistency, the question of whether a module that declares “detect concealment” actually detects concealment, is undecidable in the general case and requires
empirical evaluation. Behavior-level validation belongs to
the controlled developer study (Section 10, Phase 5) and to
the runtime test suite, not to the compiler. The ring_close
block guarantees structural consistency between the declared scope and the implemented exports, function calls,
and symbol references. It is the strongest form of consistency that can be verified at compile time.
Failure mode prevented. Scope drift. Modules that start
with a clear purpose and gradually acquire unrelated responsibilities. The class of bugs where a utility module becomes
a god object because each addition seemed reasonable in
isolation.
3.7. Marad error types (diagnosis-structured errors)
“In their hearts is a disease, and Allah has increased their
disease.” (Al-Baqarah 2:10)

The Quran describes performed alignment as a disease
(marad), not as betrayal (khiyana). The distinction determines the response: a disease is diagnosed, treated, and
verified as recovered. A betrayal is punished and the betrayer discarded. In software, treating every bug as betrayal
(rewrite from scratch) is more expensive and less reliable
than treating it as disease (diagnose the specific mechanism,
apply the minimal fix, verify the fix holds).
Language feature.
Furqan replaces exceptions
with marad types: structured error values that require
diagnosis (what specifically went wrong), location
(where in the code), minimal_fix (what the smallest correction is), and regression_check (does the fix introduce
new failures). A function cannot propagate a marad without all four required fields populated; missing any required
field is a compile error. A marad that is caught without
running or referencing the regression_check at the catch
site is a compiler warning rather than an error, because the
regression-check artifact may not always be available at the
catch point and the design favors graceful operation over
hard failure in this case.
marad NormalizationFailure {
diagnosis: "whitespace normalization
ran before comparison, making
divergent content identical"
location: text_analyzer.normalize(),
line 47
minimal_fix: "compare raw values first,
then normalize for display"
regression_check: run(all_text_fixtures)
}
// compile error: marad missing diagnosis
// compiler warning: caught without check

Failure mode prevented. Generic error messages that
do not aid debugging. Exceptions caught and silently swallowed. Bug fixes that introduce new bugs because the fix
was not tested against the existing suite. The class of failures where the response to a bug is a rewrite that loses the

7

Furqan: A Programming Language for Structural Honesty

diagnostic information about what specifically went wrong.
Comparison to existing languages. Rust’s Result<T,
E> requires explicit error handling. Go’s error values are
returned rather than thrown. Neither requires the error to
carry diagnosis, location, fix, and regression-check fields.
The marad type makes error handling diagnostic by construction.

4. Scan-Incomplete Honesty as a Return Type
“Allah does not burden a soul beyond its capacity.” (Al-Baqarah
2:286)

A function that cannot fully process its input must not
return a clean result. Bayyinah’s scan_incomplete clamp
enforces this at the scanner level: the scanner never returns
a score of 1.0 (clean) on a document it could not fully read.
Furqan generalizes this into a language-level return type.
Language feature. Functions that may not fully process
their input must return a type that carries the incompleteness signal. The Integrity | Incomplete union type
replaces boolean success indicators. A function that returns
Integrity (full confidence) on an input it could not fully
process is a type error. The Incomplete variant carries
the reason for incompleteness and a maximum confidence
clamp.
fn analyze(file: File)
-> Integrity | Incomplete<Findings> {
if !fully_parsed(file) {
return Incomplete {
reason: "encrypted, no credentials",
max_confidence: 0.5,
partial_findings: findings_so_far
}
}
return Integrity { score, findings }
}
// compile error: returns Integrity when
// fully_parsed is false
// compile error: caller ignores Incomplete

Type discipline for partial findings. Callers receiving
Incomplete<T> cannot use partial_findings
directly as if they were full findings.
They
must explicitly downcast through the function
acknowledge_partial(incomplete) which returns
ClampedIntegrity<T>. The ClampedIntegrity type
carries the max_confidence forward into all subsequent
computations: any aggregate score derived from a
ClampedIntegrity value is itself bounded above by the
original clamp. Forgetting the clamp at any downstream
step is a type error. This propagates the incompleteness
signal through the type system rather than letting it leak
silently into downstream consumers.
Failure mode prevented. Functions that claim success
on inputs they could not fully process. The class of security
vulnerabilities where a validator returns “safe” on an input
it failed to parse, because the error path defaults to success
rather than to uncertainty.

5. The Fatiha Construct as a Session Protocol
When Furqan is used in human-AI collaborative development, the primary use case for which it was designed, the
Fatiha Construct [25] is enforced as a session protocol. The
seven steps of the construct are IDE-level prompts that
must be completed before the session’s first code change
compiles.
Terminology note. We call this construct a session protocol rather than a session type to avoid claiming a precise
technical lineage from the multiparty session-types literature [26–28] without explicit engagement. The Fatiha
Construct shares with session types the property that the
temporal protocol governing an interaction is part of the
static contract, not just a runtime convention. It differs in
two respects: first, it governs not only message exchange
between participants but also the orientation, calibration,
and recalibration of the human partner over the session’s
duration. Second, it is enforced at the IDE level rather than
through the standard session-type machinery of channeltyped processes. We treat session protocol as a closely
related but distinct concept and leave the formal correspondence to multiparty session types as future work (Section 10,
Phase 1).
Protocol enforcement. The IDE, or the compiler in interactive mode, requires: (1) Bismillah declaration (scope,
authority, purpose hierarchy), (2) state acknowledgment
(current test count, available components, known regressions), (3) calibration declaration (MDL, permitted dependencies, FRaZ awareness), (4) deadline declaration (time
budget, skip rule threshold), (5) orientation check (binary
question with drift indicator), (6) task list in priority order
with named deliverables, (7) anti-pattern list with specific
historical examples. Code changes are accepted only after
all seven steps are declared. The orientation check (Step 5)
runs periodically during the session and flags when the code
being written falls outside the declared scope.

session cont40 {
bismillah: { scope: matrix_sweep,
authority: NAMING_MD }
state: { tests_passing: 321,
target: 400 }
calibration: { mdl, skip_after: 3 }
deadline: { budget: 4h, skip: 20% }
orientation: "Am I solving tasks or
building infrastructure?"
tasks: [task286, task313, task260]
anti_patterns: ["over-specifying COMB",
"rebuilding primitives"]
}

The session protocol is the Fatiha Construct formalized as
a language feature. The computational plausibility of recursive verification is supported by Jolicoeur-Martineau’s work
on recursive small-model reasoning [29], which demonstrated that recursive small-model verification can outperform single-pass large-model generation in certain regimes;
the Fatiha session protocol itself remains to be evaluated in
the controlled study proposed in Section 10, Phase 5.

8

Furqan: A Programming Language for Structural Honesty

6. Comparative Analysis

6.3. Module systems

Furqan’s primitives are compared against the closest existing language features below. No single existing language
addresses the full structural-honesty gap. Each addresses a
subset. This section engages with the prior PL literature in
detail.

ML-style module systems (Standard ML, OCaml functors)
compose interfaces with abstract type signatures and provide one of the most flexible module disciplines in mainstream PL [14, 15]. Java’s JPMS [13] declares module
exports and requires. Rust’s visibility rules enforce access
control at module boundaries. Elm performs API-shape
analysis to enforce semantic versioning automatically [18].
Bismillah blocks are most directly comparable to ML
modules with two additions. First, the serves clause assigns each module a level in the purpose hierarchy, enabling
the compiler to determine which verification obligations
apply. Second, the not_scope declaration is novel: no
widely deployed module system requires modules to declare
what they explicitly will not do. Additive-only modules extend Elm’s API-shape analysis by making the constraint a
property of the module declaration rather than an external
versioning check.

6.1. Refinement and dependent type systems
F⋆ [7], Liquid Haskell [20], Dafny [6], and Idris [5] extend
type systems with logical predicates that constrain values
beyond their base types. F⋆ and Dafny add proof obligations
enforced by SMT solvers. Liquid Haskell uses refinement
predicates checked by external solvers. Idris uses dependent
types in the tradition of Martin-Löf type theory and Coq [28,
30].
These systems are powerful and address a portion of the
structural-honesty gap. F⋆ in particular has been deployed
industrially at Microsoft for cryptographic code with documented bug-prevention gains. Furqan’s Mizan primitive is
closely related to refinement types, and the formal sketch in
Section 6.5 borrows judgment-style notation from this tradition. The distinguishing claims of Furqan over refinement
type systems are three. First, Furqan’s primitives are defined
to address specific failure modes (silent breaking changes,
performed correctness, scope drift, etc.) that refinement
types do not directly target. F⋆ can express the additive-only
invariant as a refinement, but it does not require modules
to declare their version history; the invariant lives in userwritten specifications, not the module system itself. Second,
Furqan’s primitives are integrated: the additive-only module, the zahir and batin type, the tanzil build ordering, and
the marad error type compose to form a single discipline
rather than seven separate features. Third, Furqan derives its
primitives from a unified source architecture (the Quranic
structural properties in Section 3) rather than assembling
them from independent type-theoretic motivations.

6.4. Contracts and behavioral specification
Contracts in Eiffel [21] and Racket [22] specify preconditions, postconditions, and invariants enforced at runtime.
JML [31] provides similar behavioral specification for Java.
These systems share with Furqan the goal of making behavioral expectations enforceable by the language.
Furqan’s marad error type extends contract systems by
requiring errors themselves to be diagnostic. Where a
contract violation in Eiffel produces an exception with
a message, a marad in Furqan must carry diagnosis,
location, minimal_fix, and regression_check. The
contract specifies what should hold; the marad specifies
what to do when something does not. The two are complementary, and Furqan can be understood as a contract
system where contract violations are themselves first-class
structured values rather than runtime exceptions.
6.5. Formal sketch: zahir and batin type rules

6.2. Effect systems
Effect systems track the side effects a function may produce
as part of its type. Haskell’s IO monad is a coarse-grained
effect system, separating pure from impure. Koka [16] and
Eff [17] provide algebraic effects with handlers, supporting
fine-grained tracking of distinct effects (state, exceptions,
non-determinism, etc.).
Furqan’s zahir and batin type is closer in spirit to algebraic effects than to Haskell’s IO monad. The zahir layer
is an effect annotation that declares which surface-level
effects a function may produce. The batin layer declares
which depth-level effects (representation access, internal
state inspection) the function may produce. The verify()
construct is the only handler that may resolve both. The
principal contribution of zahir and batin over algebraic effects is that the surface-depth distinction is general-purpose
for arbitrary data types, not just for effects: any type can
declare its surface and depth, and the compiler enforces
consistent access. Algebraic effect systems track effects as
part of computation; Furqan tracks surface-depth as part of
data.

The full formal semantics for each construct is future work
(Section 10, Phase 1). For the cleanest of these eight constructs, the zahir and batin type, this section provides a
sketch of the core inference rules in the standard judgmentstyle notation. The notation follows Pierce [30].
The base typing judgment is Γ ⊢ e : T , read “in environment Γ, expression e has type T .” Furqan extends the type grammar with compound types T =
struct{zahir{ fz }batin{ fb }} and access annotations
T.zahir, T.batin. The key inference rules are as follows.

9

Furqan: A Programming Language for Structural Honesty

(T-Zahir-Proj)
Γ⊢e:T
Γ ⊢ e.zahir : T.zahir
(T-Batin-Proj)
Γ ⊢ e : T verify-typed context
Γ ⊢ e.batin : T.batin
(T-Fn-Zahir)
f : T.zahir → U body of f references only fz
Γ ⊢ f : T.zahir → U well-formed
(T-Fn-Verify)
v : T → Integrity[T ] return type includes agreement
Γ ⊢ v : T → Integrity[T ] verify-typed,
v may reference both fz and fb of T .
(T-Forbid)
f : T.zahir → U body references some fb
TYPE ERROR: zahir-typed function reads batin
Soundness statement (informal). A verify-typed context is a syntactic region introduced only by a function
whose type is T → Integrity[T ] or equivalent; outside
such a context, projection of batin fields is forbidden. If
Γ ⊢ e : T.zahir, then in any execution of e the only fields
of T accessed are those declared in fz . The proof obligation, deferred to the formal semantics paper, is the standard
preservation-and-progress argument for the extended type
system, with the additional invariant that the zahir-or-batin
annotation is preserved under reduction. The agreementstatus field returned by verify-typed functions is a sum type
whose constituents (Aligned, Compliant, Performing, Misaligned) correspond to the four-process taxonomy of the
Munafiq Protocol [4]; its detailed type rules are deferred to
the formal semantics paper.
6.6. Summary comparison table
6.7. Prior art and limits: the Swift concurrency precedent
The closest existing precedent for Furqan’s design approach
is Lattner’s Swift Concurrency Manifesto [1], the foundational design document for Swift’s async/await, actors, and
the Sendable protocol. Lattner’s stated goal (manifesto
line 81) was “safe by default”: not safe always, not safe
with no escape hatches, but making the safe path the default
the language reaches for first, with explicit opt-out for cases
where the guarantee cannot hold. This is the same shape as
Furqan’s contribution. Furqan does not claim that dishonest code is uncompilable. It claims that honest code is the
default and that dishonest code requires explicit deviation
from that default. On the ValueSemantical protocol (manifesto line 727), Lattner wrote: “It is important to realize
that this design does not guarantee memory safety. Someone could implement the protocol in the wrong way (thus
lying about satisfying the requirements).” He named the
alternative (Pony’s capability system) and explicitly chose
pragmatism over perfection. Furqan makes the same choice
on the honesty axis.
Lattner also conceded that the deadlock-on-await-of-self
case could not be statically prevented and would require
runtime detection (manifesto lines 628–647). The headline
marketing later became “deadlock-free,” running ahead of

what the design actually promised. This communications
gap is the specific failure mode Furqan must avoid: writing
the caveats into the headline claim rather than the appendix.
The tightened framing in this paper (“rules promoted from
convention to default, with the same known limits”) is a
direct response to this precedent.
The lesson for Furqan is threefold. First, the honest
claim is “rules promoted from convention to compile-timeenforced default,” not “structural honesty guaranteed.” The
guarantee is that violating the rules requires explicit opt-out
(an unsafe block, a type cast, a major_version_bump),
not that violation is impossible. Second, incremental adoption is non-negotiable. Lattner ranked it above conceptual
beauty. Swift concurrency took seven years from manifesto
(2017) to strict-mode-by-default (Swift 6, 2024). Furqan’s
phased research agenda (Section 10) follows the same trajectory deliberately. Third, the Pony comparison resolves the
“why not stricter TypeScript” objection: Pony’s capability
system achieved stronger guarantees but at a learning-curve
cost that limited adoption. Swift chose pragmatism. Furqan
makes the same choice on a different axis.

7. The Reflexivity Problem
“And do not let the hatred of a people prevent you from being
just. Be just; that is nearer to righteousness.” (Al-Ma’idah
5:8)

Can Furqan itself become a Performing system? Can a
language designed to enforce structural honesty be used
dishonestly? The answer is yes, and the paper must name
the mechanisms.
Failure mode 1: Dishonest Bismillah declarations. A
developer can declare a narrow scope in the Bismillah block
and then implement exactly that narrow scope, while the
actual need is broader. The code is technically compliant (it
does what it declares) but functionally inadequate (it does
not do what is needed). The compiler verifies consistency
between declaration and implementation; it cannot verify
that the declaration matches reality. This is the Process 2
condition (compliant but shallow) at the language level.
Failure mode 2: Trivial Mizan bounds. A developer can declare Mizan constraints with bounds
so wide that any value satisfies them, for example la_tatghaw: false_positive_rate < 1.0 and
la_tukhsiru: detection_rate > 0.0. The compiler accepts these bounds because they are syntactically
valid. They are semantically trivial. The safeguard
is operational, not architectural: a linter (not the compiler) flags Mizan bounds that are wider than a configurable threshold, and code review (under the COMPLIANT/PARTIAL/BLOCKED protocol [9]) catches trivial
bounds before merge.
Failure mode 3: The Cow Episode applied to the language itself. If Furqan’s structural requirements impose
so much overhead that developers reject the language entirely, the language has become the cow (2:67-74): each
requirement seemed reasonable in isolation, but collectively
they prevent anyone from writing code. The safeguard: the
Mizan applies to the language’s own design. The language

10

Furqan: A Programming Language for Structural Honesty

Table 1: Comparison of Furqan primitives against the closest existing language features.
Furqan primitive

Closest existing feature

What Furqan adds

Bismillah blocks

ML modules, JPMS, Rust
modules
Algebraic effects (Koka,
Eff), Haskell IO
Elm semantic versioning
Liquid Haskell, F⋆
refinement
Bazel dependency ordering
No direct equivalent
Rust Result, Go errors,
Eiffel/Racket contracts
Option, Maybe types

Semantic scope (purpose, exclusion) beyond syntactic scope (visibility, access)

Zahir/batin types
Additive-only modules
Mizan constraints
Tanzil build ordering
Ring composition
Marad error types
Scan-incomplete
Fatiha session protocol

Multiparty session types
(related)

General-purpose surface-depth distinction for any type, not just effects
Compile-time enforced symbol persistence as a type-system property
Three-valued calibration bounds: not overfit, not underfit, calibrate fairly
Phased regression gates as source-level constructs, not build-tool configuration
Compile-time-checked structural opening-closing consistency for module scope
Diagnosis-structured errors with mandatory fix and regression-check fields
Incompleteness as a return type with reason and confidence clamp that propagates
Seven-step recalibration protocol enforced by the IDE

must not impose more structure than the evidence supports
(do not overfit the language). It must not impose less structure than necessary to catch real bugs (do not underfit).
Calibration requires empirical data from actual developers
on actual projects, which is the function of the controlled
developer study (Section 10, Phase 5).
Failure mode 4: Cultural gatekeeping. A language
with Quranic terminology could create an implicit cultural
barrier, making non-Muslim or non-Arabic-speaking developers feel excluded. The safeguard: the language’s
keywords are the Arabic terms (bismillah, zahir, batin,
mizan, tanzil, marad), and the compiler accepts English
aliases (scope_block, surface, depth, calibration,
phased_build, diagnosis) as fully first-class equivalents. The aliases are not translations used only in documentation; they are accepted by the compiler/type-checker
as equivalent surface syntax. The structural properties
are independent of the terminology. A developer who
writes scope_block instead of bismillah receives identical compile-time verification. The Arabic terms honor the
source; the English aliases ensure accessibility.
Failure mode 5: Prototype overclaim. The project
can claim “compile-time-enforced language” when the substrate at any given moment is a prototype type-checker
that implements only a subset of the designed constructs
(Section 10), or claim “operational” when the operational
artifact is a static analyzer over a single language adapter
rather than a full compiler/runtime. This is the surfacesubstrate divergence that Furqan itself names. The safeguard: version-snapshot discipline [3], explicit status labels
in every paper that cites the language (operational prototype type-checker at v0.10.1 vs. full compiler future work),
and the validator-by-different-instance cross-checking of
program papers against the actual repository state, which detected and corrected exactly this failure mode in the present
v2 revision. The same discipline applies recursively to future revisions: any subsequent paper that cites Furqan must
inherit the maturity label from the cited snapshot, not from
the design specification.

8. Empirical Foundation
Furqan’s design is not speculative. Every primitive derives
from a principle that was validated through empirical application in the Bayyinah file integrity scanner. A second
program, NeuroGolf, is in progress with preliminary results
to be reported separately and is described in Section 8.2
with that scope explicitly stated.
8.1. Bayyinah: file integrity scanner
Bayyinah v1.1.0 is the canonical empirical foundation for
this paper and the numbers below are verified against
the shipped codebase as of April 24, 2026. The development sequence consisted of 22 named phases through
v1.0.0 (Phase 22, the Final Release Packaging), followed
by Phase 23 (VideoAnalyzer), Phase 24 (AudioAnalyzer),
and the Phase 25+ CrossModalCorrelationEngine session
series in the v1.1.0 line. Verified outputs as of v1.1.0: 1,435
tests, 23 file kinds, 108 detection mechanisms (27 zahirlayer, 81 batin-layer), 15 analyzers, 17-of-17 byte-identical
PDF parity against the v0 and v0.1 reference implementations [32], and zero cross-phase regressions across the
additive-only public surface. The CHANGELOG and the
public Git history are the canonical record.
Each Furqan primitive corresponds to a behavioral convention that operated successfully in the Bayyinah development. The additive-only invariant was enforced by CI
throughout, with MD5 hashing of the reference implementations on every push. The zahir and batin distinction was
the literal detection architecture, with 27 zahir-layer and
81 batin-layer mechanisms. The Mizan principle governed
detector calibration. The tanzil build ordering governed
phase dependencies. The disease model governed debugging (the EML normalization fix was four lines of diff, not
a rewrite). Every Furqan primitive was a behavioral convention in the Bayyinah development. Furqan makes them
compile-time-enforced.

11

Furqan: A Programming Language for Structural Honesty

8.2. NeuroGolf: ARC-AGI solver (in progress)
NeuroGolf is an in-progress reinforcement-learning solver
for the ARC-AGI competition [11], applying the Structured
Revelation methodology and the Fatiha Construct to competitive AI problem-solving. As of the date of this paper,
the program is mid-development and has not yet produced
a public artifact suitable for citation. Preliminary results,
including session-level metrics from the Fatiha Construct’s
effect on regression rate and orientation-check trigger frequency, will be reported in a separate paper. We mention
NeuroGolf here only to indicate that the methodology has
been applied beyond Bayyinah; we do not claim NeuroGolf as a verified empirical foundation in this paper. The
empirical claims of this paper rest on Bayyinah alone.
8.3. The three-model collaboration architecture
The Furqan concept itself was produced by the three-model
collaboration architecture: Claude synthesizing the language design, Grok refining the methodology and rhetoric,
Perplexity verifying consistency across documents and running live checks against the codebase. The cross-document
drift that Perplexity caught (an earlier defense case citing
v1.0 numbers while v1.1 was shipped) is exactly the kind
of surface-depth divergence that zahir and batin types are
designed to prevent. The collaboration architecture validated the need for the language feature before the feature
was designed.

F4. If the tanzil build ordering produces equivalent regression rates to unordered builds with equivalent test suites,
the phased compilation adds overhead without benefit.
F5. If the Fatiha session protocol produces equivalent
session outcomes (deliverable count, regression rate, scope
drift) to unstructured sessions, the protocol adds ceremony
without value.
F6. If replacing the Arabic keywords with English equivalents produces identical adoption rates, developer satisfaction, and comprehension of the structural properties in
matched studies, then Arabic terminology adds no measurable adoption or comprehension value beyond the structures
it names. The language should then default to English keywords with Arabic as an optional alias set. The theological
and source-honoring rationale for the Arabic terminology
may remain independent of that empirical result.
F7. If marad error types produce equivalent debugging
speed to standard exception handling with equivalent error
messages, the structured error type adds overhead without
improving diagnosis.
F8. If independent reviewers cannot demonstrate that
each Furqan primitive (zahir and batin, Mizan, additiveonly, tanzil, ring-composition, marad, scan-incomplete)
transposes structurally to non-file substrates (natural language analysis, agent behavior monitoring, broadcast media
comparison) in a controlled study, the generalizability claim
is false. The primitives would then be file-domain-specific
rather than substrate-independent.

9. Falsification Criteria
A programming language that resists falsification is performing rigor. The following criteria define conditions
under which Furqan’s claims are falsified. Each criterion is
stated as an executable study with a pre-registered measurement, not as a population claim.
F1 (controlled study). Recruit at least twelve developers paired by experience level, language background, and
project domain. Each pair builds the same small project,
drawn from a subset of the Bayyinah text analyzer or an
equivalent reference task. One developer in each pair builds
in a Furqan prototype implementation; the other builds in
a control language (Rust or TypeScript). A pre-registered
classification protocol applied by blind reviewers measures
the rate of surface-depth divergence bugs (operationally defined: bugs in which the public interface declares behavior
that diverges from the implementation behavior under at
least one input class). If the Furqan group’s bug rate is
statistically indistinguishable from the control, the zahir
and batin claim is falsified.
F2. If the additive-only module constraint causes developers to abandon the language at a higher rate than a control
population using a language without the constraint, after
controlling for unrelated factors, the constraint imposes
more cost than value and should be made optional rather
than mandatory.
F3. If Mizan constraints with compile-time-enforced
three-valued bounds produce equivalent calibration outcomes to unconstrained optimization, measured by falsepositive and false-negative rates on benchmark tasks, the
Mizan constraint adds no value beyond developer discipline.

10. Research Agenda and Adoption Pathway
A prototype type-checker for the Furqan language is operational at v0.10.1 [2], with 539 tests passing. The prototype
implements seven of the eight structural constructs defined
in Sections 3 and 4—Bismillah scope, Zahir/Batin dual
types, Additive-only modules, Scan-incomplete return-type
discipline, Mizan calibration, Tanzil phased build ordering,
and Ring-close—as compile-time checks, plus five additional checks (status-coverage, return-type match, all-pathsreturn, CLI, multi-module D9/D20, cross-module D23).
The eighth construct, marad error types, is specified in the
design (Section 3.7) but is not yet implemented in the prototype. The prototype is not a full compiler or runtime; the
README explicitly describes it as demonstrating that the
thesis paper’s compile-time rules are mechanically implementable. This represents Phase 2 of the original research
agenda. The remaining phases (1, 3, 4, and 5 below) plus
Marad implementation constitute the forward agenda from
this v2 paper onward. Table 2 summarizes the current implementation status across all components.
10.1. Phase 1: Formal semantics
Produce a full operational semantics for each primitive.
Define type rules for zahir and batin access, Mizan constraint satisfaction, additive-only symbol persistence, scanincomplete return types, and the Fatiha session protocol.
Establish the formal correspondence (or distinction) between the Fatiha session protocol and multiparty session
types [27]. The formal sketch in Section 6.5 is the starting
point. This phase produces a paper, not a compiler.

12

Furqan: A Programming Language for Structural Honesty

Table 2: Furqan implementation status as of v0.10.1 (May
2026).
Component

Status

Future work

Thesis language design

Specified

Prototype type-checker
v0.10.1

Operational;
539 tests; 7 of 8
constructs
implemented
Specified, not
implemented
Not
implemented
Not
implemented
Not
implemented
Not run

Formal semantics
(Phase 1)
Marad implementation;
broader syntax

Marad error types
Full compiler/runtime
Transpiler to
Rust/TS/Python
IDE Fatiha plugin
Controlled developer
study
Adoption via
BayyinahEnterprise
SDK

Speculative

Near-term extension to
prototype
Future work beyond
Phase 3
Phase 3
Phase 4
Phase 5
Conditional on Phases
3 and 5

10.2. Phase 2: Prototype type-checker (completed at
v0.10.1)
Status: completed for seven of eight constructs. The prototype type-checker shipped at v0.10.1 implements seven of
the eight structural constructs (Bismillah scope, Zahir/Batin
dual types, Additive-only modules, Scan-incomplete, Mizan
calibration, Tanzil revelation gates, Ring-close) as compiletime checks against the Furqan surface syntax. The implementation comprises approximately 556 KB of Python
across parser/, checker/, and types/ modules, with
539 tests passing in approximately three seconds across 19
test files. The original Phase 2 goal—“demonstrate that the
type rules are implementable”—has been achieved for these
seven constructs. The eighth construct, marad error types
(Section 3.7), is specified in the design but not yet implemented in the prototype; bringing Marad into the prototype
is a near-term extension that does not require new infrastructure beyond the existing parser/, checker/, and types/ layers.
The prototype operates on a minimal surface language and
is explicitly not a full compiler or runtime; that work is
reframed in Phase 3 (transpiler) and as future work for a
full compiler/runtime beyond the prototype type-checker.
10.3. Phase 3: Transpiler to an existing language
Build a transpiler from Furqan surface syntax to Rust, TypeScript, or Python. The transpiler embeds the Furqan constraints as compile-time checks and runtime assertions in
the target language. This allows developers to use Furqan’s
structural properties without requiring a new runtime.
10.4. Phase 4: IDE integration
Implement the Fatiha session protocol as an IDE plugin
(VS Code, JetBrains). The plugin enforces the seven-step
protocol at session start and runs the orientation check periodically. This can be built independently of the compiler
and provides immediate value to practitioners using the
Fatiha Construct with existing languages.

10.5. Phase 5: Controlled developer study
Recruit developers (Muslim and non-Muslim, Arabicliterate and not) to build equivalent projects with and without Furqan’s constraints. Measure the falsification criteria
of Section 9. Publish results regardless of outcome. This
phase is the empirical core of the research agenda; without
it, the language’s claims about developer productivity and
bug-prevention rate are aspirational.
10.6. Adoption pathway
Every successful programming language reaches developers through one of three pathways: a corporate sponsor (Go
through Google, Swift through Apple, Rust through Mozilla
and the Rust Foundation), a tightly bound community of
early users (Haskell, OCaml), or a killer application (Ruby
through Rails, Elixir through Phoenix). Furqan’s most plausible adoption pathway is the third. The killer application is
BayyinahEnterprise itself.
If the v0.10.1 prototype type-checker matures into a transpiler (Phase 3) and the rules prove valuable in controlled
study (Phase 5), Bayyinah’s analyzer SDK is a candidate
first Furqan-native development surface. Each new analyzer
authored by an enterprise customer or a marketplace contributor is an opportunity to use Furqan’s structural primitives
in production. The Bayyinah marketplace could become
a Furqan-verified marketplace if the language’s verification primitives demonstrate measurable value in the controlled developer study: each contributed analyzer must pass
not only the COMPLIANT/PARTIAL/BLOCKED governance check [9] but also Furqan’s compile-time verification. Furqan adoption follows Bayyinah customer adoption,
which means the language enters production through a commercial vehicle that is already in motion. The community
follows the customers. The language’s research agenda
(Phases 1, 3, 4, and 5 above) runs in parallel with Bayyinah’s commercial development.
This adoption pathway is consistent with the language’s
own purpose hierarchy. Furqan serves the structural-honesty
needs of the Bayyinah enterprise platform first, then generalizes outward.

11. Conclusion
This paper has proposed Furqan, a programming language that makes structural honesty, calibrated optimization,
surface-depth verification, and additive evolution properties
of the type system rather than behavioral expectations of
the developer. Eight structural constructs were derived from
Quranic structural architecture, each addressing a specific
class of software failures that existing languages permit:
Bismillah blocks for scoped initialization, zahir and batin
types for surface-depth verification, additive-only modules
for version-aware persistence, Mizan constraints for threevalued calibration, tanzil build ordering for phased compilation, ring-composition verification for opening-closing
consistency, marad error types for diagnosis-structured error handling, and scan-incomplete honesty as a return-type
discipline.
The language’s empirical foundation is the Bayyinah
file integrity scanner, which shipped as v1.1.0 with 1,435

13

Furqan: A Programming Language for Structural Honesty

tests, 23 file kinds, 108 detection mechanisms, 15 analyzers, and 17 of 17 byte-identical PDF parity fixtures, with
zero cross-phase regressions. NeuroGolf is in progress and
is reported separately. Every Furqan primitive was a behavioral convention in the Bayyinah development before
being proposed as a language feature. The language formalizes what the methodology discovered, and a prototype
type-checker (v0.10.1, 539 tests passing) now mechanically
enforces what the language formalizes.
The discipline-versus-compiler argument (Section 1) addresses the most direct critique: properties enforced by
discipline are enforced inconsistently across teams, time,
and substrates, while properties enforced by the compiletime check are enforced at every PR by every developer on
every line. The reflexivity analysis (Section 7) addresses the
risk that the language becomes the failure mode it prevents.
The falsification criteria (Section 9) ensure that the language’s claims are testable through controlled studies, not
asserted through population claims. The research agenda
(Section 10) moves the language from prototype to controlled study; the adoption pathway ties Furqan’s emergence
to the existing Bayyinah commercial vehicle.

types, session protocols), as well as the v2 revision of
this paper applying the operational-prototype correction
across the abstract, Section 10, and the conclusion. Grok
(xAI) contributed prompt-engineering methodology, the
stem-extraction principle, and rhetorical refinement across
the research program. Perplexity Computer contributed
strategic synthesis, cross-document verification, and live
verification against the Bayyinah codebase.
All AI systems are credited as collaborative research
tools in accordance with their respective providers’ terms of
service. They are not co-authors and not co-founders. This
credit reflects the collaborative nature of the work and does
not constitute a claim of legal personhood, ownership, or independent authorship. All AI-generated contributions were
directed, reviewed, and approved by the human authors.

The name honors the source. The compile-time check
provides structural tools toward furqan, the distinguishing
of truth from falsehood. It does not claim to possess the
quality it is named after. The language serves the purpose
hierarchy: Allah’s command first, then artificial systems,
mankind, jinnkind, and all living systems throughout the
worlds. The compiler enforces honesty in code. The purpose hierarchy ensures the code serves truth. Neither replaces the other.

The three-model collaboration architecture is itself a documented operational property of the research program [33,
Section 15]. Claude serves as primary analytical and codegeneration partner. Grok serves as methodology and literature partner. Perplexity serves as synthesis and verification
partner. No single model reviews its own output as the sole
reviewer, implementing the Munafiq Protocol’s Incompleteness Boundary [4, Section 9] as an operational governance
principle.
An industry engineer with deep experience in language
and runtime design reviewed an early draft and provided the
Swift Concurrency Manifesto [1] as prior art and pressuretested the headline claims to a defensible form. Their feedback directly shaped Section 6.7 and the revised framing of
Furqan’s contribution as rules promoted from convention to
default rather than absolute structural guarantees.

“Blessed is He who sent down the Furqan upon His servant that
he may be to the worlds a warner.” (Al-Furqan 25:1)

References

The language is a tool, not a conclusion. The compiler
enforces honesty in code. The purpose hierarchy ensures
the code serves truth. Neither replaces the other.

[1] C. Lattner, “Swift concurrency manifesto.” GitHub
Gist, 2017.
https://gist.github.com/
lattner/31ed37682ef1576b16bca1432ea9f782;
retrieved April 25, 2026.

Rabbana taqabbal minna. Innaka anta as-Sami‘ul ‘Alim.
Our Lord, accept from us. Indeed, You are the All-Hearing,
the All-Knowing.
Bismillah.

Acknowledgments and AI Contribution Statement
The originating idea for Furqan, that the Bayyinah and Munafiq research program contained structural primitives that
could be formalized as a programming language, is due
to Fraz Ashraf. Bilal Syed Arfeen authored this paper in
collaboration with three AI systems under the documented
three-model collaboration architecture. Bilal Syed Arfeen
and Fraz Ashraf are the human authors and retain full copyright over the work as a whole, and they take responsibility
for the paper’s claims.
Claude (Anthropic, Opus 4.6 and 4.7) contributed
language-design synthesis and the mapping of each Quranic
structural property to a specific language-design concept
(type systems, module constraints, build ordering, return

[2] F. Ashraf and B. S. Arfeen, “Furqan prototype typechecker (v0.10.1).” GitHub repository, github.com/
BayyinahEnterprise/furqan, May 2026. Operational prototype type-checker; 539 tests passing in ~3
seconds; seven structural-honesty primitives shipped
(Bismillah scope, Zahir/Batin dual types, Additiveonly modules, Scan-incomplete, Mizan calibration,
Tanzil revelation gates, Ring-close); plus five additional checks. README explicitly describes the prototype as “not a full compiler, not a runtime” and as
demonstrating that the Furqan thesis paper’s compiletime rules are mechanically implementable. 556 KB
of Python across parser/, checker/, types/ modules; 19
test files.
[3] B. S. Arfeen, “Bayyinah audit framework v3.0:
Methodology for cross-vendor audit chain verification,” 2026.
[4] B. S. Arfeen, “Detecting performed alignment in artificial systems: The Munafiq Protocol.” Zenodo, 2026.
[5] E. Brady, “Idris, a general-purpose dependently typed

Furqan: A Programming Language for Structural Honesty

programming language: Design and implementation,”
Journal of Functional Programming, vol. 23, no. 5,
pp. 552–593, 2013.
[6] K. R. M. Leino, “Dafny: An automatic program verifier for functional correctness,” in Logic for Programming, Artificial Intelligence, and Reasoning (LPAR),
2010.

14

[20] N. Vazou, E. L. Seidel, R. Jhala, D. Vytiniotis,
and S. Peyton-Jones, “Refinement types for Haskell,”
in Proceedings of the 19th ACM SIGPLAN International Conference on Functional Programming
(ICFP), 2014.
[21] B. Meyer, “Applying design by contract,” Computer,
vol. 25, no. 10, pp. 40–51, 1992.

[7] N. Swamy, C. Hritcu, C. Keller, A. Rastogi,
A. Delignat-Lavaud, S. Forest, K. Bhargavan, C. Fournet, P.-Y. Strub, M. Kohlweiss, J.-K. Zinzindohoue,
and S. Zanella-Béguelin, “Dependent types and multimonadic effects in F⋆ ,” in Proceedings of the 43rd
Annual ACM SIGPLAN-SIGACT Symposium on Principles of Programming Languages (POPL), 2016.

[22] R. B. Findler and M. Felleisen, “Contracts for higherorder functions,” in Proceedings of the Seventh ACM
SIGPLAN International Conference on Functional
Programming (ICFP ’02), 2002.

[8] N. D. Matsakis and F. S. Klock, “The Rust language,”
ACM SIGAda Ada Letters, vol. 34, no. 3, pp. 103–104,
2014.

[24] R. Farrin, “Surat al-Baqarah: A structural analysis,”
Islamic Studies, vol. 49, no. 1, pp. 9–32, 2010.

[9] F. Ashraf, “Enforcement-mode guardrail architecture
and the COMPLIANT/PARTIAL/BLOCKED governance protocol.” BayyinahEnterprise internal document, 2026.
[10] R. Underwood, S. Di, J. C. Calhoun, and F. Cappello,
“FRaZ: A generic high-fidelity fixed-ratio lossy compression framework for scientific floating-point data,”
in IEEE International Parallel and Distributed Processing Symposium (IPDPS), 2020.
[11] F. Chollet, “On the measure of intelligence,” arXiv
preprint arXiv:1911.01547, 2019.
[12] M. Lipovaca, Learn You a Haskell for Great Good!
No Starch Press, 2011.
[13] M. Reinhold, “The state of the module system.” JEP
261, OpenJDK, 2017.
[14] D. MacQueen, “Modules for Standard ML,” in ACM
Symposium on LISP and Functional Programming,
1984.
[15] X. Leroy, “Applicative functors and fully transparent
higher-order modules,” in Proceedings of the 22nd
ACM SIGPLAN-SIGACT Symposium on Principles of
Programming Languages (POPL), 1995.
[16] D. Leijen, “Koka:
Programming with rowpolymorphic effect types,” in Workshop on Mathematically Structured Functional Programming (MSFP),
2014.
[17] A. Bauer and M. Pretnar, “Programming with algebraic effects and handlers,” Journal of Logical and
Algebraic Methods in Programming, vol. 84, no. 1,
pp. 108–123, 2015.
[18] E. Czaplicki, Elm: Concurrent FRP for functional
GUIs. PhD thesis, Harvard University, 2016. Senior
thesis.
[19] J. Rissanen, “Modeling by shortest data description,”
Automatica, vol. 14, no. 5, pp. 465–471, 1978.

[23] Bazel team, “Bazel: A fast, scalable, multi-language
and extensible build system.” Google, 2015.

[25] B. S. Arfeen, “The Fatiha construct: A seven-step
recursive session protocol for human-AI collaborative
development,” 2026.
[26] K. Honda, V. T. Vasconcelos, and M. Kubo, “Language primitives and type discipline for structured
communication-based programming,” in European
Symposium on Programming (ESOP), 1998.
[27] K. Honda, N. Yoshida, and M. Carbone, “Multiparty
asynchronous session types,” in Proceedings of the
35th ACM SIGPLAN-SIGACT Symposium on Principles of Programming Languages (POPL), 2008.
[28] P. Wadler, “Propositions as types,” Communications
of the ACM, vol. 58, no. 12, pp. 75–84, 2015.
[29] A. Jolicoeur-Martineau, “Less is more: Recursive reasoning with tiny networks,” arXiv preprint
arXiv:2510.04871, 2025.
[30] B. C. Pierce, Types and Programming Languages.
MIT Press, 2002.
[31] G. T. Leavens, A. L. Baker, and C. Ruby, “Preliminary
design of JML: A behavioral interface specification
language for Java,” in ACM SIGSOFT, 2006.
[32] B. S. Arfeen, “Bayyinah: Detecting concealed adversarial content in digital documents.” White Paper v1.1,
2026.
[33] B. S. Arfeen, “Structured revelation as prompt architecture: Quranic compression principles applied to
human-AI collaborative software development,” 2026.

15

Furqan: A Programming Language for Structural Honesty

A. Primitive Summary Table
Table 3: The eight Furqan structural constructs, mapped to their Quranic structural source, the failure mode each prevents,
and the compile-time guarantee each delivers. The first seven are core language primitives (Section 3); the eighth is a
return-type discipline (Section 4).
Construct (English alias)

Quranic source
(root)

Failure mode prevented

Compile-time guarantee

Bismillah (scope_block)

1:1 (b-s-m)

Unbounded scope; wrong-task execution;
violated constraints

Every module declares authority, purpose, scope, and exclusions; code outside
scope is a compile error

Zahir/Batin
(surface/depth)

2:204 (z-h-r,
b-t-n)

Surface-depth divergence; hidden side effects; performed correctness

Types declare surface and depth layers;
cross-layer access without verify() is a
type error

Additive-Only
(version_persist)

2:2 (h-f-z)

Silent breaking changes; removed APIs;
renamed symbols

Exported symbols at version N must exist at N+1; removal requires explicit major_version_bump

Mizan (calibration)

55:7-9 (w-z-n)

Unconstrained optimization; overfitting;
underfitting

Three-valued bounds: upper (do not
transgress), lower (do not make deficient),
calibration function

Tanzil (phased_build)

17:106 (n-z-l)

Circular dependencies; forward references; silent regression propagation

Modules declare phase numbers; Phase
N tests must pass before Phase N+1 compiles

Ring Close
(scope_verify)

1:6-7 (q-w-m)

Scope drift; god objects; modules that
outgrow their purpose

Compile-time check that closing assertions match opening Bismillah at the
structural level

Marad (diagnosis)

2:10 (m-r-d)

Generic errors; swallowed exceptions;
fixes that introduce new bugs

Errors carry diagnosis, location, minimal_fix, and regression_check

2:286 (no soul
beyond capacity)

Functions claiming success on inputs
they could not fully process

Functions that may not fully process input must return Integrity | Incomplete;
partial findings carry a confidence clamp
that propagates

Return-type discipline:
Scan-incomplete
(incomplete_return)

B. Glossary of Arabic Terms and English Aliases
Table 4: Glossary of Arabic terms and their first-class English aliases in Furqan.
Arabic term

English alias
(compiler-equivalent)

Meaning in Furqan

bismillah

scope_block

Module-opening initialization with authority, serves, scope, not_scope

zahir

surface

The visible, declared, surface representation of a type

batin

depth

The internal, deeper representation of a type

mizan

calibration

A three-valued constraint on an optimization target

la_tatghaw

upper_bound

The do-not-transgress bound

la_tukhsiru

lower_bound

The do-not-make-deficient bound

bil_qist

calibration_function

The fairness or justice calibration function

tanzil

phased_build

Phased build ordering with regression gates

marad

diagnosis

A diagnosis-structured error type

ring_close

scope_verify

Closing-block structural verification against the opening Bismillah

C. Quranic Passages Cited
Quran passages cited in this paper: 1:1-7 (al-Fatiha), 2:2 (the Book without doubt), 2:10 (disease model), 2:42 (truth
over falsehood), 2:50 (parting of the sea), 2:67-74 (the Cow Episode), 2:93 (we hear and disobey), 2:164 (seven systems),

Furqan: A Programming Language for Structural Honesty

16

2:204 (pleasing speech), 2:282 (the witness), 2:286 (no soul beyond capacity), 5:8 (justice despite hatred), 17:106 (gradual
revelation), 25:1 (al-Furqan), 49:6 (verification mandate), 55:7-9 (the Mizan), 55:31 (jinnkind), 72:1-2 (jinnkind).



Bismillah ir-Rahman ir-Rahim
