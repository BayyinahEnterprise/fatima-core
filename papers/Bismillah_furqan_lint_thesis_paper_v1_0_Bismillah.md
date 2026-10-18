Bismillah ir-Rahman ir-Rahim

furqan-lint: A Structural-Honesty Linter for Python,
Rust, and Go
Theoretical foundations, three-language implementation,
twenty-seven-version empirical record, and the audit-of-self
pattern
Bilal Syed Arfeen
BayyinahEnterprise
bayyinahenterprises@tuta.com

ABSTRACT
This thesis paper documents furqan-lint, a structural-honesty linter for Python, Rust, and Go.
The tool implements five checks derived from the Furqan programming language's
structural-honesty primitives: D24 (all-paths-return), D11 (status-coverage), R3 (zero-return /
ring-close), return-None mismatch, and additive-only public-surface diff. The empirical gap
relative to ruff and mypy is specific: where mypy in default mode catches the direct
return-type mismatches when annotations are present and complete, furqan-lint catches the
structural cases mypy does not. These include status-coverage propagation through
narrowing return-type annotations (where each function passes mypy individually but the
chain across functions strips the original incompleteness), public-surface deletion across
versions (mypy operates on one version at a time and has no cross-version awareness), and
zero-return ring-close on unannotated or dynamically constructed functions (mypy in default
mode passes silently on unannotated code, which comprises the majority of production
Python). Equivalent shapes apply on Rust (Option/Result) and Go ((T, error)) where the
language compilers reject some but not all firing conditions.
Three implementation surfaces are documented: a Python adapter built on the standard ast
module via the upstream Furqan translation, a Rust adapter built on tree-sitter behind the
[rust] optional dependency extra, and a Go adapter built on a custom goast binary compiled at
install time behind the [go] optional dependency extra. The three adapters feed a common
runner pipeline; the same checker functions execute against the unified Furqan intermediate
representation regardless of source language. Coverage is asymmetric and documented:
some checks (D24, D11, additive-only) apply to all three languages; others (R3 in Go,
return-None in Rust and Go) are documented as not-applicable because the firing condition is
unreachable on any source the language compiler accepts. This v1.0 release includes an
explicit currently-shipping-adapters section (§5.0) and a theorization of additional adaptable
languages (§5.4) covering TypeScript, Kotlin, Swift, Scala, C#, C++23, OCaml/F#, Zig, Java,
and Elixir.
The empirical record covers twenty-seven releases shipped over two days (May 2 to May
3, 2026), beginning at v0.1.0 with forty-one tests and reaching v0.8.5 with three hundred and
forty-seven tests. Each release was governed by an audit chain applying the Bayyinah Audit
Framework's discipline: every behavioral change required an empirical reproducer, severity
classification, four-place documentation across CHANGELOG, README, fixture, and pinning

1

furqan-lint: A Structural-Honesty Linter

Arfeen, Thesis v1.0

test, and adherence to the additive-only invariant on the project's own public surface. Notable
structural decisions documented in this paper include the v0.4.1 retirement of the v0.1.0 D11
monkey-patch through an upstream Furqan parameter, the v0.7.2 prompt-grounding
self-check that scope-narrowed the planned Rust analogue of return-None mismatch to
nothing because the firing condition was unreachable on rustc-accepted source, and the
v0.8.5 attribution corrective preserving immutable historical CHANGELOG sections while
sweeping going-forward attribution conventions.
furqan-lint is the reference implementation of the audit framework's discipline applied to a
tool that audits structural honesty: it is the case where the tool that catches drift in other
people's code must not have drift in its own. The audit-of-self pattern is documented
architecturally; the pre-commit hook runs furqan-lint on src/ as part of every commit, and the
same checks that surface findings in consumer codebases gate the project's own substrate.
Keywords: structural honesty, static analysis, linter, multi-language, Python, Rust, Go,
tree-sitter, AI-assisted code, audit-of-self, additive-only public surface, status coverage,
ring-close, may-fail unions, BayyinahEnterprise
Note on version currency. This paper documents the substrate as of v0.8.5 (May 3, 2026),
the release at which the twenty-seven-version empirical record concludes. The substrate has
continued advancing in the six days between v0.8.5 and this paper's publication date: the
latest release at the time of writing is v0.11.6 (May 9, 2026), and the test count has grown from
three hundred and forty-seven at v0.8.5 to five hundred and ninety-nine at v0.11.6. The
intervening releases add a fourth language adapter (ONNX, v0.9.0) and a Sigstore-CASM Gate
11 verifier for Python (v0.10.0) and Rust (v0.11.0). §5.5 of this paper summarises these
post-v0.8.5 developments without analysing them at the per-version depth applied to v0.1.0
through v0.8.5; the analysis-grade record terminates at v0.8.5 by deliberate scope. Readers
seeking the current substrate state should consult CHANGELOG.md at the repository head:
https://github.com/BayyinahEnterprise/furqan-lint.

1 IDENTITY AND PURPOSE
furqan-lint is a structural-honesty linter for Python, Rust, and Go. It is the reference
implementation of a particular kind of static check: a check that catches the gap between
what a function declares it returns and what its substrate actually does. The tool runs as a
command-line program, as a pre-commit hook, and as a continuous-integration GitHub
Action. It is published at github.com/BayyinahEnterprise/furqan-lint and on the Python
Package Index as furqan-lint.
This paper is the technical specification of the tool. Its companion is The Bayyinah Audit
Framework v3.0 (Arfeen 2026i), which documents the engineering discipline under which
furqan-lint was built. The framework names the methodology; this paper documents the
artifact. Both can be read independently; readers interested in the discipline should read the
framework first, readers interested in the tool's internals should read this paper first, and
readers interested in deploying furqan-lint into a continuous-integration pipeline can read the
Application Brief (Arfeen 2026j) before either.
1.1 What furqan-lint is

2

furqan-lint: A Structural-Honesty Linter

Arfeen, Thesis v1.0

Five checks ship in the v0.8.5 release documented in this paper. Four are static checks
invoked through the check subcommand: D24 (all-paths-return), D11 (status-coverage), R3
(zero-return / ring-close), and return-None mismatch. The fifth, additive-only public-surface
diff, is invoked through a separate diff subcommand and compares two versions of a
module's public surface, firing on any name removed without an explicit retirement procedure.
The five checks are derived from the Furqan programming language's structural-honesty
primitives. Furqan's type system rejects code shapes that lie about what they do: a function
declaring an integer return type cannot have a path that produces None; a function consuming
an integrity-or-incomplete union must handle both arms; a public module's exported name set
is monotonically additive across releases unless a name is explicitly retired. These primitives
are compile-time rejections in Furqan; furqan-lint translates the same structural rules into
static-analysis findings on existing Python, Rust, and Go source code without requiring the
codebase to be rewritten in Furqan.
1.2 What furqan-lint is not
furqan-lint is not a replacement for ruff, mypy, or any general-purpose linter. The five checks
are deliberately narrow; they cover a class of defects that mypy in default mode does not
catch, and that mypy in --strict mode catches only when annotations are complete enough to
surface them. The specific empirical gap (case-illustrated by running both tools on the same
fixtures; the systematic comparator-analysis successor study is named in §9.6) covers four
shapes: status-coverage propagation through narrowing return-type annotations (where
every individual function passes mypy but the chain across functions strips the original
incompleteness), public-surface deletion across versions (where mypy operates on one
version at a time and has no cross-version awareness), zero-return ring-close on unannotated
or dynamically-constructed functions (where mypy in default mode passes silently), and the
equivalent shapes on Rust and Go where the language compilers reject some but not all firing
conditions. For all other static-analysis needs (style violations, unused imports, complexity
metrics, type-soundness checks on annotated code, formatting), users should run ruff and
mypy alongside furqan-lint. The recommended pre-commit configuration runs ruff first (lint
and format), then mypy (types), then furqan-lint (structural honesty); each layer catches what
the previous layers do not.
furqan-lint is also not a security scanner, a dependency-vulnerability checker, a
license-compliance tool, or a code-coverage measurement tool. The structural-honesty class
of defects it covers is a specific class of latent correctness issues, not a general-purpose
code-quality measurement. The tool's value scales with the cost of a structurally-dishonest
defect; in low-stakes domains, the overhead may not pay rent.
1.3 Why this paper exists
The Bayyinah Audit Framework v3.0 references furqan-lint twenty-five times as the reference
implementation of the framework's discipline. Those references describe the framework's
relationship to furqan-lint, not the technical specification of furqan-lint itself. This paper closes
the gap. It documents the tool's architecture, the theoretical grounding of the five checks, the
implementation strategy across three substrates, the empirical trajectory of the
twenty-seven-version development, the audit-of-self pattern under which the tool was built,
the validation methodology, and the limitations.
3

furqan-lint: A Structural-Honesty Linter

Arfeen, Thesis v1.0

Throughout the paper the audit framework's discipline is applied to the prose itself: every
claim has a substrate, every limitation is named, every empirical assertion is reproducible
against the public repository at github.com/BayyinahEnterprise/furqan-lint. Where the
framework documents the discipline of audit, this paper documents the artifact built under that
discipline; the relationship between the two is the relationship between methodology and
instance.

2 THE STRUCTURAL-HONESTY GAP
Existing static-analysis tools for Python, Rust, and Go cover three broad categories: style and
formatting (ruff in Python, rustfmt and gofmt for the other languages), type-soundness (mypy
in Python, the language compilers themselves for the other languages), and security and
dependency analysis (Snyk, Veracode, and similar tooling at the supply-chain layer). A
specific class of defects falls outside all three categories. This paper calls that class
"structural-honesty defects," and the rest of this section names the four shapes that
constitute the class.
2.1 The Optional-collapse pattern
In Python, a function declaring a return type of Optional[X] (equivalent to Union[X, None]) is
permitted to return either X or None. A caller consuming the function's return value must
handle both arms; failing to do so is a latent defect. mypy's behavior here divides into two
cases. The direct-misuse case (a caller annotated as returning X invokes f returning
Optional[X] and propagates the result without handling None) is caught by mypy in default
mode when both annotations are present and complete; mypy reports an Incompatible return
value type error. The propagation case is the empirical gap: a caller correctly handles the
None arm locally (checking for None, returning a default on the None path) but its return-type
annotation is X (non-Optional), so the original incompleteness is silently narrowed away in the
type signature. Two function calls down the chain, a consumer reads the value as if the
Optional had never existed. mypy passes because every individual function body is internally
consistent; the structural drift is across the chain, not within any single function. The defect
ships when the upstream input causes the original Optional source to return None, the local
handler returns its default, and the downstream consumer treats the default as a real value.
furqan-lint's D11 (status-coverage) check catches this propagation case directly. It
compares the producer's declared incompleteness against the consumer's declared
completeness, even when both producer and consumer pass mypy individually. The check is
the executable form of the Furqan type system's Integrity-or-Incomplete union: a producer of
Optional[X] must be consumed by a caller whose declared return type also propagates the
Incomplete arm, or by a caller that explicitly raises or otherwise non-locally exits on the None
arm before propagating an X. Silent collapse via a degenerate-default narrowing is a finding.
2.2 The silently-removed public name
API stability is a contract between a library author and the library's downstream consumers. A
semantic-versioning major-version bump is the discipline by which an author signals
"breaking changes are present." Most tooling enforces semantic versioning at the
version-string layer; very little tooling enforces it at the substrate layer. A library author can
4

furqan-lint: A Structural-Honesty Linter

Arfeen, Thesis v1.0

rename a public function inside a minor-version bump (or even a patch-version bump) and the
version string says nothing happened. The downstream consumer learns of the breakage at
runtime, when their import fails or their function call hits an attribute error.
furqan-lint's additive-only check is the executable form of the Furqan
additive-only-modules primitive. Invoked via furqan-lint
diff
old_module.py
new_module.py, the check extracts the set of public names (top-level functions, classes,
constants, and re-exports) from each version and fires on any name present in old that is
absent in new. Adding a public name is silent. Renaming a public name (which is structurally a
deletion plus an addition) is a finding. The check is supplemented by language-aware
diagnostic prose: Python users see suggestions like "re-export the old name as an alias", Go
users see "var Name = <new>" re-export hints, and Rust users see analogous
module-re-export suggestions.
2.3 The zero-return ring-close
A function declaring a non-None return type that contains zero return statements anywhere in
its body is structurally dishonest in a specific way: the declared return type is a contract, and
falling off the end of the function in Python yields None, which is not a valid value of the
declared type. When the function is fully annotated, mypy in default mode catches this as
"Missing return statement." The empirical gap is on unannotated code: mypy in default mode
passes silently on functions without return-type annotations (and most production Python
codebases are not under --strict). furqan-lint's R3 check enforces the structural shape
regardless of annotation completeness. R3's name comes from the Furqan ring-close
primitive: a function is a ring whose entry and exit points must close on the declared (or, in
unannotated cases, expected) type.
R3 is the fourth Python check, added in v0.6.0. It supplements D24 (all-paths-return) by
catching the shape D24 cannot: D24 fires on partial-path coverage (some paths return, others
fall through), but a function with zero return statements has no path coverage to analyze. R3
catches that shape directly. The implementation is conservative: functions decorated with
@abstractmethod
or
@overload
(or
aliased
forms
documented
in
tests/fixtures/documented_limits/aliased_optional_import.py)
are
skipped.
Provably-non-returning bodies (raise-only, while True without break) are also skipped.
2.4 The return-None mismatch
The return-None mismatch is the specific case where a function declares a non-Optional
return type (for example, -> str) but contains an explicit return None statement on some
path. This is a stronger shape than the D24 partial-path case (where the path falls off the end
implicitly) and a stronger shape than R3 (where there are no return statements). The function
explicitly returns None where the declared type cannot accommodate None. furqan-lint's
return_none_mismatch check fires on this shape and is wired into the Python adapter.
A planned Rust analogue of return-None mismatch was investigated during v0.7.2
development and dropped. The empirical demonstration that Rust's compiler rejects all
firing-condition shapes (rustc rejects fn f() -> i32 { None } at compile time before
furqan-lint sees the file) is documented in §7.4 below; the v0.7.2 release notes document the
scope-narrowing decision in detail. The same shape applies to Go: the Go compiler rejects
similar shapes at compile time. return_none_mismatch is therefore Python-only by design, not
5

furqan-lint: A Structural-Honesty Linter

Arfeen, Thesis v1.0

by oversight.

3 THEORETICAL GROUNDING
The five checks documented in §2 are not arbitrary engineering choices. They are
operationalizations of structural-honesty primitives from the Furqan programming language
(Ashraf and Arfeen 2026). This section traces each check to its theoretical origin and names
the design choices that translate compile-time language semantics into static-analysis
findings on languages that lack those semantics.
3.1 Furqan's structural-honesty primitives
Furqan defines several primitives that constrain the shape of well-formed code. Three apply
directly to the checks in furqan-lint. The first is the Integrity-or-Incomplete union: a function
may return Integrity[X] or Incomplete, but a consumer must handle both arms. The Furqan
compiler rejects code that consumes an Integrity-or-Incomplete return value as if it were a
bare Integrity. This primitive is the theoretical origin of D11.
The second is the additive-only modules primitive: a Furqan module's public name set is
monotonically additive across releases. Removing a public name requires an explicit
retirement-block declaration, which the compiler enforces and which downstream consumers
can detect. The primitive is the theoretical origin of the additive-only check.
The third is ring-close: a function declared with a non-empty return type is a ring whose
every path must close on a value of that type. The Furqan compiler rejects functions whose
paths do not close. The primitive is the theoretical origin of D24 (which catches partial-path
closure failures) and R3 (which catches the degenerate case of zero return statements).
3.2 Translation from compile-time to static analysis
Python, Rust, and Go each accept some shapes that Furqan rejects. Translation choices are
documented per-check. For D24, Python's interpreter does not enforce all-paths-return; the
function is permitted to fall off the end and yield None. mypy in default mode enforces it on
functions with explicit return-type annotations (reporting "Missing return statement"); the
empirical gap is on unannotated code, where mypy passes silently. furqan-lint's D24 fires on
the structural shape regardless of annotation completeness. Rust's compiler does enforce
all-paths-return at the type-system level, which is why D24 in the Rust adapter only fires on a
structurally-different shape: explicit branches that some return-typed and some panic-typed.
Go's compiler also enforces it, with similar implications.
For D11, mypy catches the direct-misuse case (a caller returning X invokes f returning
Optional[X] and propagates the result without handling None) in default mode when
annotations are present. The empirical gap is the propagation case: a caller correctly handles
the None arm locally with a degenerate default but its return-type annotation strips the original
incompleteness, so two function calls down the chain a consumer reads the value as if the
Optional had never existed. mypy passes this because every function body is internally
consistent; the structural drift is across the chain. furqan-lint catches this directly via the
producer-predicate parameter, which compares the producer's declared incompleteness
against the consumer's declared completeness regardless of whether mypy's per-function

6

furqan-lint: A Structural-Honesty Linter

Arfeen, Thesis v1.0

checks pass. For Rust, the equivalent shape is a caller declaring -> T while invoking a helper
returning Option<T> or Result<T, E> without using the ?-operator or explicit match;
furqan-lint's Rust adapter recognizes both the Option and the Result shapes through the same
producer-predicate mechanism. For Go, the equivalent shape is a caller declaring (T) (single
return) while invoking a helper returning (T, error); furqan-lint's Go adapter recognizes the
(T, error) convention as the may-fail-producer pattern.
For additive-only, the enforcement is deliberately external to the language: it operates on
two snapshots of public names extracted from the source. The check is therefore identical in
shape across all three languages; only the public-name extraction differs (Python's ast
module yields top-level def, class, and assigned-name shapes; Rust's tree-sitter walker yields
pub items; Go's goast binary yields uppercase-initial top-level names). The checker code is
shared; the language adapters supply only the extraction.
For R3, the firing condition is the disjoint complement of D24: D24 fires on partial-path
coverage where at least one path returns, R3 fires on zero-return-statement coverage where
no path returns. The two checks together cover the full ring-close shape. R3 in the Go adapter
is documented not-applicable because Go's compiler rejects all firing shapes at compile time;
the adapter does not implement R3 for Go.
3.3 The producer-predicate parameter
The translation from Furqan's compile-time Integrity-or-Incomplete to runtime D11
enforcement is mediated by a single function: the producer predicate. Given a return-type
annotation, the producer predicate returns true if the annotation describes a may-fail producer
(Optional in Python, Option<T> or Result<T, E> in Rust, (T, error) in Go) and false
otherwise. The producer predicate is the only language-specific component of D11; the rest of
the check is shared via the upstream Furqan check_status_coverage function and its
producer_predicate keyword parameter, available since Furqan v0.11.0.
The history of D11 wiring is documented in §7.2 below. v0.1.0 used a context-managed
monkey-patch on the upstream furqan.checker module's _is_integrity_incomplete_union
predicate, a stopgap measure documented at the time as deferred work. v0.3.0 added
thread-safety to the monkey-patch via a global lock. v0.4.1 retired the monkey-patch entirely
by passing the producer predicate via the upstream producer_predicate keyword, which had
landed in Furqan v0.11.0 in the interim. The retirement closed the full lifecycle of a round-1
audit finding across four versions. The final implementation has zero shared mutable state, no
global locks, and no monkey-patches; the v0.4.1 release notes describe the change as "retires
the patch entirely" in the documented sense of §11 four-place pattern (Arfeen 2026i).

4 THE FIVE CHECKERS
This section documents each checker in detail: the firing condition, the diagnostic prose, the
false-positive avoidance strategy, and the documented limitations. All five checkers are
implemented in src/furqan_lint/ and exercised by the test suite in tests/.
4.1 D24: all-paths-return

7

furqan-lint: A Structural-Honesty Linter

Arfeen, Thesis v1.0

D24 fires when a function declared with a non-None return type has at least one path through
its control-flow graph that does not reach a return statement. The check operates on the
Furqan intermediate representation produced by the language adapter; the underlying CFG
analysis is delegated to upstream Furqan. The Python adapter translates ast.FunctionDef and
ast.AsyncFunctionDef nodes; the Rust adapter translates fn items and impl methods via
tree-sitter; the Go adapter translates FuncDecl and method declarations via the goast binary.
False-positive avoidance covers three shapes. First, functions whose return type is None or
Optional[None] do not fire (the implicit fall-through is consistent with the declared type).
Second, functions whose body provably never returns (raise-only bodies, infinite loops
without break) do not fire. Third, functions decorated with @abstractmethod or @overload (and
the
aliased
forms
documented
in
tests/fixtures/documented_limits/aliased_optional_import.py) are skipped.
The diagnostic prose names the line of the function declaration and the path that fails to
close. For a function with multiple uncovered paths, only the first is reported; the user is
expected to fix one path at a time and re-run. This is a deliberate trade-off: fewer cascading
diagnostics in exchange for a less complete report.
4.2 D11: status-coverage
D11 fires when a function declared with a non-may-fail return type invokes a may-fail producer
without handling the failure case. The producer predicate is language-specific (§3.3); the rest
of the check is shared. In Python, a may-fail producer is any function whose return type is
Optional[X] or Union[X, None] (or the PEP 604 X | None form, supported since v0.3.4). In
Rust, a may-fail producer is any function whose return type is Option<T> or Result<T, E>. In
Go, a may-fail producer is any function whose return type is (T, error) for some T.
False-positive avoidance covers two shapes. First, a caller whose declared return type is
itself a may-fail producer (propagation case) does not fire. Second, a caller that explicitly
handles the failure case before propagating the success arm does not fire; in Python this is
detected via if-let-style matching, in Rust via the ?-operator or match expression, in Go via the
standard if err != nil { return ..., err } convention.
The check has the deepest empirical history of the five. The v0.1.0 release implemented D11
via a context-managed monkey-patch on furqan.checker._is_integrity_incomplete_union.
v0.3.0 added thread-safety to the patch via a global _predicate_lock. v0.4.1 retired the patch
entirely
by
passing
producer_predicate=_is_optional_union
to
upstream
check_status_coverage. The history is documented in CHANGELOG entries v0.1.0, v0.3.0,
and v0.4.1; the four-place pattern is satisfied by the corresponding fixture, pinning test,
README entry, and CHANGELOG entry.
4.3 R3: zero-return / ring-close
R3 fires when a function declared with a non-None return type contains zero return
statements anywhere in its body. The check is the disjoint complement of D24: D24 fires on
partial-path coverage with at least one return statement somewhere; R3 fires on zero return
statements. Together the two checks cover the full ring-close shape.
R3 was added in v0.6.0 as the fourth Python checker, retiring two earlier documented
limitations: the v0.4.x "Zero-return functions" limit and the v0.3.5 "Exception-driven
8

furqan-lint: A Structural-Honesty Linter

Arfeen, Thesis v1.0

fall-through" limit (R3 catches the try-body-only-raise shape that D24 cannot). One new
documented limitation was introduced and closed in v0.6.1: aliased decorator imports for R3's
skip-list (e.g., from abc import abstractmethod as abstract) were not yet resolved through
symbol tables; v0.6.1 added the symbol table.
R3 in the Rust adapter (added in v0.7.2) has the same firing condition. R3 in the Go adapter
is documented not-applicable: the Go compiler rejects all firing-condition shapes at compile
time before furqan-lint sees the file.
4.4 return-None mismatch
return_none_mismatch fires on a specific Python shape: a function declares a non-Optional
return type (for example, -> str or -> int) but contains an explicit return None statement on

at least one path. The check closes the D24 return-None blind spot: D24 fires on implicit
fall-through, but a function that explicitly returns None on a path needs a separate diagnostic
to surface the structural mismatch.
return_none_mismatch is Python-only. The planned Rust analogue was investigated during

v0.7.2 development and dropped; the §7.4 prompt-grounding self-check in v0.7.2 empirically
demonstrated that the firing condition (a function declaring a non-Option return type with an
explicit None expression) is unreachable on any source rustc accepts. rustc rejects fn f() ->
i32 { None } at compile time before furqan-lint sees the file. The Go compiler exhibits
analogous behavior. The Rust translator delta and the check_return_none wiring would have
shipped infrastructure for a check with no job; the v0.7.2 release defers re-introduction to
whichever later phase introduces an actual consumer for __none__ in Rust IR.
4.5 additive-only diff
additive_only is invoked through a separate CLI subcommand: furqan-lint diff
old_module.py new_module.py. The check extracts the set of public names from each version

and reports any name present in old that is absent in new. Adding a public name is silent.
Renaming a public name (structurally a deletion plus an addition) is a finding.
Public-name extraction is language-specific. In Python, a public name is any top-level
function, class, or assigned name not prefixed with an underscore, plus any name listed in
__all__ if __all__ is present. In Rust, a public name is any top-level item declared with pub or
pub(crate); the public_names module of the rust_adapter walks the tree-sitter AST and
produces a frozenset. In Go, a public name is any top-level identifier whose initial letter is
uppercase; the public_names module of the go_adapter invokes the goast binary which emits
qualified names (including method receivers as of v0.8.2) and returns a frozenset.
Cross-language diff is not supported: furqan-lint diff foo.py bar.go returns exit code
2 with a "Cross-language diff not supported" message. The check is intended for comparing
two versions of the same module's public surface across releases, which is the boundary at
which API stability is meaningful; cross-language comparison is a category error. Diagnostic
prose is language-aware. Python users see suggestions like "re-export the old name as
old_name = new_name." Go users see "var OldName = NewName" re-export hints. Rust users
see analogous module-re-export suggestions. The shared diagnostic skeleton is supplied by
the common runner; the language-specific suffix is supplied by the adapter.

9

furqan-lint: A Structural-Honesty Linter

Arfeen, Thesis v1.0

5 THREE-LANGUAGE IMPLEMENTATION
furqan-lint supports Python, Rust, and Go through three language adapters that share a
common runner pipeline. Each adapter is responsible for translating source code into the
Furqan intermediate representation; the same checker functions then operate on the IR
regardless of the source language. §5.0 summarizes the shipping adapters at a glance; §5.1
through §5.3 document each adapter in depth; §5.4 theorizes additional languages that share
the structural-honesty preconditions and could be adapted in subsequent phases.
5.0 Adapters shipping in v0.8.5
Three adapters ship in the v0.8.5 release. Table 1 summarizes each adapter at a glance. The
Python adapter is the foundational implementation and ships in the standard wheel without
optional extras. The Rust adapter ships behind the [rust] optional dependency extra and pulls
tree-sitter and tree-sitter-rust as runtime dependencies. The Go adapter ships behind the [go]
optional dependency extra and compiles a custom goast binary at install time via a PEP 517
build hook, which requires Go 1.21 or later on PATH at install time but not at runtime.
Adapter

Install command

Parser

Checks

Toolchain at install

Python

pip install
furqan-lint

ast (stdlib)

D24, D11, R3,
return-None,
additive

Python 3.10+

Rust

pip install "fu tree-sitter +
rqan-lint[rust] tree-sitter-rust
"

D24, D11, R3,
additive

Python 3.10+
(wheels prebuilt)

Go

pip install "fu goast (Go stdlib
rqan-lint[go]" go/ast)

D24, D11, additive

Python 3.10+ and
Go 1.21+

Table 1. The three currently-shipping adapters in v0.8.5. Coverage is asymmetric and
documented; cells marked not-applicable in subsequent text reflect language-compiler-side
rejection of firing conditions, not adapter omission.
Coverage matrix (Table 2) names which checks fire on which language. D24, D11, and
additive-only apply to all three languages. R3 applies to Python and Rust; the Go compiler
rejects R3's firing condition, so the check is not-applicable on Go source. return-None
mismatch is Python-only; both rustc and the Go compiler reject the firing condition at compile
time, as documented in §4.4 and §7.4.
Check

Python

Rust

Go

D24 (all-paths-return)

Yes

Yes

Yes

D11 (status-coverage)

Yes (Optional)

Yes (Option, Result)

Yes ((T, error))

R3 (zero-return /
ring-close)

Yes

Yes

N/A (compiler rejects)

return-None mismatch

Yes

N/A (compiler rejects)

N/A (compiler rejects)

additive-only diff

Yes

Yes

Yes

10

furqan-lint: A Structural-Honesty Linter

Arfeen, Thesis v1.0

Table 2. Per-check, per-language coverage. "N/A (compiler rejects)" denotes that the firing
condition is unreachable on source the language compiler accepts; the adapter deliberately
does not implement the check.
5.1 Python adapter
The Python adapter is the foundational implementation. It uses the standard library's ast
module to parse Python source and translates the resulting ast.Module into a Furqan Module
via the upstream furqan.adapter.translate_tree function. The translation is a
node-by-node walk producing the Furqan IR; behavioral fidelity is verified by the upstream
Furqan test suite plus furqan-lint's own integration tests.
The Python adapter ships in the wheel without optional extras. Installation via pip install
furqan-lint is sufficient to run all four Python checks (D24, D11, R3, return_none_mismatch)
and the Python additive-only diff. The adapter also exposes the public function
adapter.translate_tree(tree, filename) so the CLI can parse source once and feed both
the Furqan Module (for D24, D11, return-none) and the raw ast.Module (for R3, which needs
decorator information that the Furqan translation does not preserve). This single-parse path
was added in v0.6.0.
Public-name extraction for Python is implemented in additive.py and walks the
ast.Module looking for FunctionDef, AsyncFunctionDef, ClassDef, Assign, and AnnAssign
nodes at module scope. Names beginning with an underscore are considered private and
excluded. If __all__ is present and contains a list of strings, only those names are considered
public; this honors the standard Python convention for explicit public-surface declaration.
5.2 Rust adapter
The Rust adapter ships behind the [rust] optional dependency extra: pip install
furqan-lint[rust]. The extra installs tree-sitter and tree-sitter-rust; both ship pre-built
wheels for ARM64 and x86_64, so installation does not require a source build. The version pin
tree-sitter>=0.23,<1 reflects an empirical break between tree-sitter 0.20 and 0.21 that
motivated the explicit upper bound.
The

Rust

adapter

translates

tree-sitter

ASTs

into

Furqan

IR

through

src/furqan_lint/rust_adapter/translator.py (819 lines, the largest single source file in the

repository). The translation handles Rust functions, methods, impl blocks, traits (with trait
method declarations), pub and pub(crate) visibility modifiers, Option<T> and Result<T, E>
return types, and the ?-operator. Lifetimes, generics with bounds, macro expansion, closure
return-type inference, and Cargo workspace traversal remain out of scope; these limitations
are documented in the README and pinned by tests/fixtures/rust/documented_limits/.
Edition handling: the Rust edition (one of "2018", "2021", "2024") is read from the nearest
ancestor Cargo.toml's [package].edition field. If no Cargo.toml is found or the field is
malformed, the edition defaults to "2021." The current implementation does not branch on
edition; the field is read for forward compatibility with edition-specific syntax that may diverge
in future Rust releases.
Three

checkers

run

on

Rust

files:

D24

(all-paths-return,

via

upstream

furqan.checker.check_d24), D11 (status-coverage with the producer predicate recognizing
both Option<T> and Result<T, E>), and R3 (zero-return / ring-close, via upstream

11

furqan-lint: A Structural-Honesty Linter

Arfeen, Thesis v1.0

check_ring_close). The rust_adapter/runner.py module wires the checkers; the
rust_adapter/parser.py module handles the lazy import of tree-sitter so the broader

furqan_lint package remains importable on installs without the [rust] extra.
5.3 Go adapter
The Go adapter ships behind the [go] optional dependency extra: pip install
furqan-lint[go]. The extra is a marker-only PyPI dependency (no Python packages); the
actual translation is performed by a Go binary called goast that is compiled from
go_adapter/cmd/goast/ at install time via a PEP 517 build hook. The Go toolchain (1.21 or later)
is therefore required at install time, but not at runtime; the compiled binary ships in the wheel.
The goast binary parses Go source via the Go standard library's go/ast package, emits a
JSON representation of the function declarations and types, and exits. The Python-side
go_adapter/translator.py reads the JSON and translates into Furqan IR. The split between
the binary and the Python adapter is deliberate: parsing Go in Python is structurally awkward
(the goast representation depends on Go's evolving language specification), and reusing the
Go standard library's parser ensures compatibility with the language as actually defined by the
toolchain.
Two checkers run on Go files: D24 (all-paths-return) and D11 (status-coverage with the
producer predicate recognizing the (T, error) convention). R3 is documented
not-applicable: the Go compiler rejects all firing-condition shapes at compile time before
furqan-lint sees the file. return_none_mismatch is similarly not-applicable.
Public-name extraction for Go: the goast binary emits uppercase-initial top-level names. As
of v0.8.2, qualified method names (including the receiver type) are also emitted. The
go_adapter/public_names.py module reads the JSON and constructs a frozenset for the
additive-only check. The diff diagnostic prose is Go-aware: users see var Name = <new>
re-export hints rather than Python alias syntax.
5.4 Theorized future adapters
The five checks generalize beyond Python, Rust, and Go. The structural-honesty primitives
they encode (Integrity-or-Incomplete unions, additive-only public surface, ring-close) are
language-agnostic; the per-language adapter supplies only the parser, the may-fail-producer
predicate, and the public-name extractor. This section enumerates ten candidate languages
by structural fit, names the parser library that would do the heavy lifting for each, and
indicates which of the five checks would fire on accepted source. The theorization is
engineering-grounded rather than speculative; for each language the parser and convention
exist today, so an adapter is shovel-ready work rather than research.
Three categories organize the candidates. The first category is languages whose may-fail
convention closely mirrors Rust's Option/Result and which would benefit from the full
five-check suite (modulo R3's compiler-rejection caveat per language). The second category
is languages whose may-fail convention is partial, where D11 firing requires extra translation
effort. The third category is languages whose compiler enforces ring-close and may-fail
handling at the type-system level, making most checks structurally redundant; additive-only
and a residual D24 on panic-or-return shapes remain valuable.
5.4.1 Strong-fit candidates
12

furqan-lint: A Structural-Honesty Linter

Arfeen, Thesis v1.0

TypeScript and JavaScript are the highest-fit candidates by adoption volume. TypeScript's
structural type system supports Optional via T | undefined and T | null union types, which
are direct analogues of Rust's Option<T>. The TypeScript Compiler API (ts-morph or the
official typescript package) and tree-sitter-typescript both supply parsers that could feed a
TypeScript adapter; the producer predicate would fire on T | undefined, T | null, and the
strict-null-checks Optional shapes. JavaScript without TypeScript annotations is the
no-annotation case where R3 and D24 still fire on the structural shape regardless of
annotation completeness, similar to the Python no-annotation case. additive-only on .ts and .js
modules would extract export and module.exports names. Effort estimate: comparable to the
Rust adapter (~800 lines of translator), with the TypeScript-specific complexity concentrated
in conditional types and intersection types that the producer predicate would need to handle
conservatively.
Kotlin maps cleanly onto the existing producer-predicate machinery. T? denotes nullable
types (direct Optional analogue), Result<T> is part of the standard library, and pub-style
visibility modifiers (public, internal, private) translate directly to the additive-only extraction.
Either tree-sitter-kotlin or kotlinc's PSI library could supply the parser. Effort estimate: lower
than Rust because the type system is more uniform; expected ~600 lines of translator.
Swift's may-fail conventions are stronger than Kotlin's: Optional<T> (Wrapped or nil),
Failure: Error>, and the throws keyword for throwing functions all
constitute may-fail-producer shapes. The producer predicate would fire on all three.
SwiftSyntax or tree-sitter-swift would supply the parser. additive-only on Swift modules would
extract public, open, and internal declarations (per Swift's access-level model). Effort
estimate: comparable to Rust, with throws handling adding a separate translator path.
Result<Success,

Scala combines functional and object-oriented structures and ships Option, Either, and Try
as standard-library may-fail producers. For Scala 3 (formerly Dotty), the official compiler
provides a parser API; for Scala 2, scalameta is the standard parser library. The producer
predicate would recognize all three may-fail shapes. additive-only on Scala modules requires
handling implicit conversions and given/using clauses, which would benefit from a phase-2
extension after the baseline adapter ships. Effort estimate: comparable to Rust for the
baseline, with significant additional work for implicit-resolution handling.
C# (.NET) ships Nullable<T> as the canonical Optional, and the third-party OneOf package
plus the standard Result patterns from libraries such as LanguageExt and
CSharpFunctionalExtensions supply Result-style may-fail producers. Roslyn (the official .NET
compiler platform) provides a first-class C# parser API. additive-only on C# assemblies would
extract public types and members; the access-modifier handling is straightforward. Effort
estimate: comparable to Kotlin if scoped to Nullable<T> only; comparable to Scala if
Result-pattern recognition is in scope.
C++23 ships std::optional (since C++17) and std::expected (since C++23) as
standard-library may-fail producers. Tree-sitter-cpp or libclang would supply the parser;
libclang is preferred for production-grade adapters because it understands the preprocessor.
The producer predicate would fire on std::optional<T> and std::expected<T, E>.
additive-only on C++ headers requires handling extern "C", namespace boundaries, and
template instantiations; the baseline could ignore templates and ship a useful additive-only
check on non-template public surface. Effort estimate: higher than Rust due to preprocessor
complexity, with libclang doing most of the heavy lifting.
13

furqan-lint: A Structural-Honesty Linter

Arfeen, Thesis v1.0

OCaml and F# share the option and Result types from the ML family. Their compilers
enforce exhaustiveness on pattern matches over options, which means the D11 firing condition
is structurally narrower than in Python or Rust: the compiler rejects most D11 firing shapes at
compile time, leaving only the propagation case where a function returns the bare type rather
than option/Result and discards the failure information. Additive-only on .ml and .fs modules
would extract the .mli/.fsi signature files' export sets. Effort estimate: lower than Rust because
the compiler does most of the work; baseline adapter expected ~400 lines.
Zig ships error unions (!T) and optional types (?T) as first-class language features, and the
compiler enforces handling at the call site. The producer predicate would recognize !T and ?T
return types; D11's residual firing condition is the same as OCaml's: the propagation case
where a caller declares a bare T and silently discards the error or optional. tree-sitter-zig
supplies a parser. Effort estimate: comparable to OCaml; the tighter language specification
makes the producer predicate simpler.
5.4.2 Partial-fit candidates

Java has Optional<T> (since Java 8) and checked exceptions as the may-fail-producer
shapes. The Optional case maps cleanly; the checked-exception case requires the producer
predicate to recognize the throws clause as a may-fail signal, and the consumer-side check to
recognize either a try/catch block or a propagating throws clause as adequate handling.
JavaParser or the Eclipse JDT supply parsers; tree-sitter-java is also available. additive-only
on Java modules would extract public class and interface members. The structural-honesty
value of Java is mainly in the Optional collapse case (modern Java often wraps null-returning
legacy APIs in Optional, then strips the wrapping inconsistently); the checked-exception case
is interesting but less commonly the source of latent defects. Effort estimate: comparable to
Rust, with the dual may-fail conventions splitting the producer predicate into two paths.
Elixir uses a pervasive convention rather than a type-system feature: functions that may fail
return {:ok, result} | {:error, reason} tuples, and pattern-matching with case or with is
the canonical handling. The producer predicate would need to recognize the convention
rather than a static type, which is structurally analogous to Go's (T, error) recognition but
more dynamic because Elixir is untyped at compile time. Tree-sitter-elixir supplies a parser.
additive-only on Elixir modules would extract def and defp declarations and the
@behaviour-implemented callbacks. Effort estimate: comparable to Go due to
convention-based recognition, with the additional complexity that Elixir's macro system
rewrites code at compile time, so the source-level check is necessarily incomplete.
5.4.3 Compiler-enforced families

Haskell, OCaml, F#, and the broader ML-family compilers enforce exhaustiveness on Maybe
and Either pattern-matches at compile time. D11's firing condition (consuming a may-fail
producer without handling the failure case) is structurally rejected by the compiler before
furqan-lint sees the file, the same way Rust's compiler rejects D24's firing condition for
missing returns. R3 is similarly compiler-rejected (functions must close their return type).
What remains valuable: additive-only on .hs and .ml modules' export lists, and a residual D24
on panic-or-return shapes (using error or undefined to escape the type system). The
five-check suite collapses to two checks on these languages, and the engineering effort shifts
toward additive-only as the primary value. Effort estimate: very low for additive-only alone;
not-applicable for the other four checks.
14

furqan-lint: A Structural-Honesty Linter

Arfeen, Thesis v1.0

Ruby is the inverse case: no static types, no compiler enforcement, and a culture of
duck-typing rather than may-fail conventions. Sentinel returns (nil, false) are common, but
they are convention rather than declared type. furqan-lint's value on Ruby would be limited to
additive-only on public methods, where the structural-honesty layer overlaps with rubocop
and similar tools. Not recommended as a near-term adapter target; the structural-honesty
preconditions are weakly satisfied.
Table 3 summarizes the adapter theorization. The table is the reference for adoption
decisions: a project considering furqan-lint can match its language against the strong-fit,
partial-fit, or compiler-enforced category and read the parser and effort estimate accordingly.

guage

Category

Parser

Producer predicate Effort vs. Rust

eScript /
aScript

Strong-fit

TypeScript
Compiler API or tre
e-sitter-typescript

`T \

undefined, T \

in

Strong-fit

tree-sitter-kotlin or
kotlinc PSI

T?, Result

Lower

ft

Strong-fit

SwiftSyntax or
tree-sitter-swift

Optional, Result,
throws

Comparable

la

Strong-fit

scalameta or Scala
3 compiler API

Option, Either, Try

Comparable

(.NET)

Strong-fit

Roslyn

Nullable, OneOf,
Result patterns

Lower (Nullable
only) / Comparable
(with Result)

+23

Strong-fit

libclang or
tree-sitter-cpp

std::optional,
std::expected

Higher

aml / F#

Strong-fit (compiler
-narrowed)

ocaml-compiler-libs option, Result
/ FSharp.Compiler.S
ervice

Strong-fit (compiler
-narrowed)

tree-sitter-zig

?T, !T

Lower

a

Partial-fit

JavaParser or
Eclipse JDT

Optional, throws

Comparable

r

Partial-fit

tree-sitter-elixir

`{:ok, ...} \

{:error, ...}`
convention

kell

Compiler-enforced

haskell-src-exts or
GHC API

Maybe, Either
(mostly
compiler-rejected)

Lower
(additive-only only)

y

Weak-fit

tree-sitter-ruby or
parser gem

Convention only
(nil, false sentinels)

Not recommended

null`

Lower

Comparable to Go

Table 3. Theorized future adapters by structural fit. Strong-fit candidates can adopt the full
five-check suite (modulo per-language compiler rejection of specific firing conditions).
Partial-fit candidates require additional translation work in the producer predicate.
Compiler-enforced families collapse the suite to additive-only as the primary value. The

15

Comparable

furqan-lint: A Structural-Honesty Linter

Arfeen, Thesis v1.0

weak-fit case (Ruby) is named explicitly to delimit the framework's applicability rather than to
suggest adoption.
None of the theorized adapters are committed to a release schedule. The v0.8.5 release
ships with Python, Rust, and Go; subsequent adapters are deferred to whichever phase
introduces an explicit consumer demand or a partner project willing to fund the engineering
work. The theorization documents the addressable surface, not a promise to ship.
5.5 Substrate advances since v0.8.5 (currency addendum)
The analysis-grade record in this paper terminates at v0.8.5 (May 3, 2026) by deliberate
scope. Six days separate that release from this paper's publication date, and the substrate has
continued advancing in those six days. This subsection summarises the post-v0.8.5
developments at the executive level so a reader of v1.0 of this paper is not misled into
believing the substrate is frozen at v0.8.5; it does not extend the per-version analytic depth
applied to v0.1.0 through v0.8.5. Future revisions of this paper may absorb these
developments into the analytic record, or may leave them to a successor paper. The
immutability discipline that governs the v0.1.0-through-v0.8.5 record is preserved: this
subsection adds context, it does not retract or rewrite earlier sections.
Fourth language adapter (ONNX, v0.9.0, May 4, 2026). furqan-lint extended
structural-honesty diagnostics to ONNX computational graph files (.onnx) as a parallel
diagnostic family, not as an instance of the existing checkers operating on a unified
intermediate representation. The three ONNX-family checks are D24-onnx (all-paths-emit on
graph outputs), opset-compliance (against a pinned opset registry), and D11-onnx (shape and
type coverage). Two further checks ship behind sub-extras: numpy_divergence under
[onnx-runtime] (v0.9.3+) and a score_validity ADVISORY under [onnx-profile] (v0.9.4+). The
ONNX adapter is documented as honest divergence from the unified pipeline rather than
additional coverage of it; the thesis-level analysis of why this divergence is acceptable is
deferred to a successor paper.
Sigstore-CASM Gate 11 verifier (v0.10.0 + v0.11.0, May 7, 2026). Phase G11.A (al-Fatiha)
introduced SAFETY_INVARIANTS.md as the foundational document for Sigstore-CASM Gate
11; phase G11.0 shipped the Python verifier behind [gate11]; phase G11.1 (as-Saffat) shipped the
Rust extension behind [gate11-rust]. The gate is a cryptographically-witnessed additive-only
contract on the public surface, signed via Sigstore Rekor at release time and verifiable by
downstream consumers. The thesis-level treatment of how the gate composes with the
existing additive-only diff check is also deferred to a successor paper; this subsection records
its existence so the v0.8.5 substrate documentation is not read as a complete description of
the current public-surface discipline.
Test count and release cadence. The test count progressed from three hundred and
forty-seven (v0.8.5) to five hundred and ninety-nine (v0.11.6) over the post-v0.8.5 window, a
+252 delta across thirteen releases (v0.9.0 through v0.11.6 inclusive). The cadence continues
to satisfy the framework's CHANGELOG-math gate: every release entry documents its
test-count delta and the gate verifies the arithmetic against pytest --collect-only at release
time. The post-v0.8.5 releases include several closure cycles for Round 28 through Round 32
audit findings (F22 through F25), the latest of which is the al-Furqan corrective in v0.11.6
closing a workflow identity-pattern literal-vs-regex distinction failure. The reader is referred to
CHANGELOG.md at the repository head for per-release detail.
16

furqan-lint: A Structural-Honesty Linter

Arfeen, Thesis v1.0

Toolchain currency. The Go adapter's documented install-time toolchain requirement has
shifted from Go 1.21 (the v0.8.5 baseline) to Go 1.21+ in the README's headline section and Go
1.22+ in the active install-line guidance; the runtime requirement remains a compiled binary
with no Go toolchain dependency. The Rust adapter now reads the Cargo.toml
[package].edition field (one of "2018", "2021", "2024") with a 2021 default; the current
implementation does not branch on edition. The upstream Furqan dependency floor is
furqan>=0.11.0 (v0.11.6 is the current upstream tip). These are operational currency notes
rather than thesis-level changes.

6 THE AUDIT-OF-SELF PATTERN
furqan-lint is a structural-honesty linter. It catches a class of latent defects in code authored
by humans and AI assistants. The tool itself is also code authored by humans and AI
assistants. The reciprocal contract documented in The Bayyinah Audit Framework v3.0
(Arfeen 2026i) is therefore directly applicable to furqan-lint's own substrate. This section
documents how the audit-of-self pattern is operationalized in the project: the pre-commit
hook configuration, the continuous-integration self-check, and the empirical record of
findings the tool has surfaced on its own code.
6.1 The pre-commit configuration
The project's .pre-commit-config.yaml runs four hooks on every commit: ruff (lint and
format), mypy (strict type checking), pytest (the full test suite), and furqan-lint check src/.
The fourth hook is the audit-of-self in operational form: the same furqan-lint binary that
consumers install from PyPI runs against the project's own source tree, and a finding blocks
the commit. The hook configuration is committed to the repository; any contributor running
pre-commit install picks up the same enforcement.
The README documents the pattern explicitly: "The furqan-lint check src/ self-check
runs as part of pre-commit; the tool that catches drift in other people's code must not have
drift in its own." This is not a stylistic flourish but a structural requirement. A linter whose own
substrate fails the linter's checks would be unable to ship without flagging itself; the inability
to ship a clean release would surface immediately during continuous integration.
6.2 The continuous-integration self-check
The .github/workflows/ci.yml continuous-integration workflow runs the same gates as
pre-commit, plus expanded coverage. The matrix exercises Python 3.10, 3.11, 3.12, and 3.13
against three optional-dependency configurations (no extras, [rust] extra, [go] extra),
producing a fourteen-job matrix as of v0.8.4 (up from a five-job matrix in v0.8.3). The matrix
expansion is the empirical answer to a v0.8.3 round-21 audit finding documented in §7.5: a CI
matrix that does not exercise every adapter is structurally equivalent to having no CI for the
unexercised adapters.
The tests/ directory includes several gate-level tests that validate the project's own
discipline rather than the tool's behavior on consumer code. test_changelog_math_gate.py
parses CHANGELOG entries and verifies that documented test-count deltas match the actual
pytest
--collect-only
count. test_extras_matrix_gate.py verifies that every

17

furqan-lint: A Structural-Honesty Linter

Arfeen, Thesis v1.0

optional-dependency configuration in pyproject.toml is exercised by at least one CI job.
test_four_place_completeness_gate.py walks the documented-limits directory and verifies
each limit has a fixture, a pinning test, a README entry, and a CHANGELOG mention.
test_release_sweep_gate.py verifies version-string consistency across pyproject.toml,
src/furqan_lint/__init__.py, and the latest CHANGELOG entry. These gates are the
operational form of the framework's audit chain (Arfeen 2026i, §4).
6.3 Findings the tool has surfaced on itself
The empirical record is documented in §7 below. Several rounds of the audit chain surfaced
findings via furqan-lint check src/ on the project's own source tree. Notable examples
include: (a) v0.4.1's CRITICAL pre-commit hook installation finding, where the v0.4.0 hook
shipped with empty additional_dependencies and silently failed at install time (surfaced not
by furqan-lint itself but by the audit chain's discipline of "surface vs substrate" verification);
(b) v0.7.2's prompt-grounding self-check that empirically demonstrated the planned Rust
return-None analogue would have shipped infrastructure for a check with no job; and (c)
v0.8.5's attribution-discipline corrective, where the audit chain's own historical record
violated the four-place pattern by attributing findings to a specific named auditor in inline
comments while the going-forward convention attributes them to round-N audit.
None of these findings are dramatic. The empirical claim is the modesty: the audit-of-self
pattern surfaces small structural deficits early and continuously, before they compound. The
retirement ledger documents the full set of failure-mode shapes retired across the chain; each
is structurally prevented in all subsequent versions until the gate is explicitly removed. The
discipline is the substrate; the releases are the surface.

7 EMPIRICAL TRAJECTORY: TWENTY-SEVEN VERSIONS
furqan-lint shipped twenty-seven releases between May 2 and May 3, 2026: v0.1.0 through
v0.8.5, with one absorbed version (v0.7.4 was rolled into v0.8.0). This section documents the
trajectory as an empirical record. Each release has a CHANGELOG entry naming the round of
the audit chain it corresponds to, the severity-classified findings it closed, and the test-count
delta. The trajectory is the substrate against which the framework's claims of disciplined
development are falsifiable.
7.1 Genesis: v0.1.0 through v0.3.5
v0.1.0 (May 2) shipped the foundational implementation: D24 and D11 on Python, the CLI with
check and version subcommands, and 41 tests. D11 was implemented via a context-managed
monkey-patch on the upstream furqan.checker._is_integrity_incomplete_union predicate,
a stopgap measure documented at the time as deferred work. The v0.1.0 release is the audit
chain's round-1 baseline.
v0.2.0 added the additive-only diff subcommand and Python public-name extraction.
v0.3.0 added thread-safety to the D11 monkey-patch via a global _predicate_lock; the
threading hazard had been surfaced by the round-2 audit. v0.3.1 through v0.3.5 closed a
series of HIGH and MEDIUM findings on diagnostic prose, PEP 604 (X | None) syntax
recognition, and Bare-Union vs Optional disambiguation. v0.3.5 documented the
"Exception-driven fall-through" limitation as a deferred fix; the limitation was retired in v0.6.0
18

furqan-lint: A Structural-Honesty Linter

Arfeen, Thesis v1.0

by the R3 checker.
7.2 The CI integration pivot: v0.4.0 and v0.4.1
v0.4.0 (May 2) introduced the GitHub Action and the pre-commit hook configuration. The
release was substantial: 158 tests, the action.yml composite workflow definition, and the
.pre-commit-hooks.yaml entry. v0.4.0 also seeded the audit chain's most consequential
structural discipline: the four-revision prompt review pattern documented in The Bayyinah
Audit Framework v3.0 (Arfeen 2026i, §12.3). The pattern emerged from a round-8 finding in
which a corrective-action prompt was discovered to contain five errors including a CRITICAL:
removing a symbol would have broken fourteen tests via ImportError cascade. The prompt
was revised before execution; the discovery seeded the framework's prompt-review
discipline.
v0.4.1 closed seven findings from the round-8 review: one CRITICAL (the pre-commit hook
installation defect, described in §6.3), two HIGH, two MEDIUM, and two LOW. The CRITICAL
was particularly consequential: v0.4.0 had shipped a pre-commit hook configuration that
declared furqan as a dependency via pyproject.toml, but pyproject.toml's furqan>=0.11.0
specification would resolve to PyPI (which only hosted furqan==0.10.1 at the time), causing
pip to fail dependency resolution. The hook shipped in v0.4.0 in a non-functional state; v0.4.1
fixed it by declaring furqan as an additional_dependency via the canonical GitHub URL. The
structural lesson: structural tests (YAML schema validation) passed in v0.4.0; functional install
tests would have caught the failure. v0.4.1 added the functional tests as a four-place-pattern
pinning.
v0.4.1

also

retired

the

v0.1.0
D11
monkey-patch
by
passing
producer_predicate=_is_optional_union to the upstream check_status_coverage function
(the parameter had landed in furqan v0.11.0 in the interim). The retirement closed the full
lifecycle of a round-1 finding across four versions, removing import threading, the
contextmanager import, the _predicate_lock global, and the entire _python_optional_mode
context manager. The _is_optional_union helper survived with its body unchanged, only the
docstring was updated to reference the upstream parameter.
7.3 The R3 round: v0.6.0 and v0.6.1
v0.6.0 (May 2) added the R3 (zero-return / ring-close) checker, the fourth Python checker.
The implementation is in src/furqan_lint/zero_return.py (~407 lines as of v0.8.5, per
pyproject's source-line audit). R3 closed two earlier documented limitations simultaneously:
the v0.4.x "Zero-return functions" limit and the v0.3.5 "Exception-driven fall-through" limit.
One new documented limitation was introduced (aliased decorator imports such as from abc
import abstractmethod as abstract were not yet resolved through symbol tables) and was
closed in v0.6.1 by adding the symbol table.
v0.6.0 also surfaced an architectural decision: R3 needs decorator information that the
Furqan translation does not preserve. The CLI was modified to parse Python source once via
ast.parse and feed both the Furqan Module (for D24, D11, return-none) and the raw
ast.Module (for R3) to the runner. The single-parse path was added via the new public
adapter.translate_tree(tree, filename) function. The change is minor in terms of lines but
structurally important: it preserved the layered separation between the Furqan IR (which
checkers depend on) and the language-specific AST (which a small subset of checkers also
19

furqan-lint: A Structural-Honesty Linter

Arfeen, Thesis v1.0

need).
7.4 The Rust adapter phases: v0.7.0 through v0.7.4
v0.7.0 (May 3) added the Rust adapter behind the [rust] optional dependency extra. The
implementation
is
the
largest
single
source
addition
in
the
project:
rust_adapter/translator.py at 819 lines, plus rust_adapter/runner.py (165 lines),
public_names.py (153 lines), edition.py (87 lines), parser.py (60 lines), and __init__.py (117
lines). The phase landed D24 on Rust files using upstream furqan.checker.check_d24; D11
and R3 followed in subsequent v0.7 releases.
v0.7.2 documents the most consequential scope-narrowing decision in the audit chain: the
prompt-grounding self-check that empirically demonstrated the planned Rust analogue of
return_none_mismatch is unreachable. The round-15 prompt specified return-None mismatch
as the third Rust checker for v0.7.2. The round-16 pre-implementation critique (the
four-revision prompt review pattern in operation) constructed a battery of test cases
attempting to write Rust source that would trigger the firing condition, and discovered that
rustc rejects all such shapes at compile time before furqan-lint sees the file. fn f() -> i32 {
None } does not parse; rustc rejects it as a type mismatch before any AST processing occurs.
The translator delta and the check_return_none wiring would have shipped infrastructure for a
check with no job. v0.7.2 dropped the planned analogue and shipped Result-aware D11
instead, which had been a stretch goal in the original round-15 prompt.
v0.7.3 added the dead-code retirement pin: a forward-compatibility regression test
asserting that _d24_diagnostic_in_r3_set (a function that had been removed in v0.6.1
commit b0a4b18) does not exist anywhere under src/. The pin prevents accidental
re-introduction. v0.7.4 was absorbed into v0.8.0; the version number is preserved in the
CHANGELOG as a placeholder for the absorbed work, per the framework's immutability
discipline.
7.5 The Go adapter and CI matrix expansion: v0.8.0 through v0.8.4
v0.8.0 (May 3) added the Go adapter behind the [go] optional dependency extra. The
implementation includes a Go binary (go_adapter/cmd/goast/) compiled at install time via a
PEP 517 build hook in setup.py, plus Python-side translator (291 lines), parser (108), runner
(61), public_names (52), build hooks (43), and exceptions (29). v0.8.0 landed D24 and D11 on
Go files; R3 and return_none_mismatch are documented not-applicable for the reasons in
§3.2. v0.8.1 added the Go diff subcommand; v0.8.2 extended public-name extraction to
include qualified method names with receiver types.
v0.8.3 expanded the continuous-integration matrix from five jobs to fourteen. The
pre-v0.8.3 matrix exercised only the Python adapter under the no-extras configuration; the
Rust and Go adapters compiled in dev-loop but were not exercised under CI's partial-extras
configurations. The round-21 audit surfaced this as a HIGH-severity finding: a CI matrix that
does not exercise every adapter is structurally equivalent to having no CI for the unexercised
adapters. v0.8.3's expansion covers Python 3.10, 3.11, 3.12, and 3.13 across three
optional-dependency configurations (no extras, [rust] extra, [go] extra), producing the
fourteen-job grid (with two combinations excluded as redundant).

20

furqan-lint: A Structural-Honesty Linter

Arfeen, Thesis v1.0

v0.8.4 swept several findings from the round-22 GitHub repository audit:
branch-protection configuration alignment, the eight-minor-version PyPI drift (v0.1.0 had been
the most recent PyPI release while the substrate had advanced through eight minor versions),
per-version public-surface baseline pins, and a multi-commit corrective sequence executed
under the four-revision prompt review pattern. The PyPI drift finding closed via PyPI Trusted
Publishing with OIDC, atomically; wall-clock time from tag push to PyPI publication was 52
seconds. Test count rose from 325 (v0.8.3) to 344 (v0.8.4).
7.6 The attribution corrective: v0.8.5
v0.8.5 (May 3) is a documentation-only release that closes a single round-23 finding: the audit
chain's CHANGELOG and source-code attribution to "Fraz" as the auditor was imprecise. The
framework documented in The Bayyinah Audit Framework v3.0 (Arfeen 2026i) is jointly
developed by Bilal Syed Arfeen and Fraz Ashraf as framework methodology; the auditor role
across all twenty-three rounds has been Bilal, applying the framework to his own substrate.
This is a single-person audit-of-self pattern, and earlier CHANGELOG entries that attributed
findings to a specific named auditor inline are imprecise.
v0.8.5 closed the finding via a four-part discipline. First, the going-forward convention
attributes findings to round-N audit without naming the auditor inline. Second, source-code
inline comments attributing rounds to a specific name were swept (eight references in
src/furqan_lint/adapter.py, one in src/furqan_lint/return_none.py, plus test-file module
docstrings in five test files). Third, an Attribution discipline note was added at the top of
CHANGELOG.md, above all release sections, explaining the framework's provenance and the
auditor role. Fourth, historical CHANGELOG sections were preserved verbatim per the
immutability discipline; commit subjects and bodies that mention the named auditor were
similarly preserved on origin.
Test count rose from 344 (v0.8.4) to 347 (v0.8.5). The +3 delta is structural: the
per-version cadence in the framework requires every minor and patch version to ship a
per-version public-surface baseline pin in each of the three additive-only surface snapshots.
v0.8.5 introduces no Python public surface change, so each baseline aliases v0.8.4. The three
new pin tests assert that the corresponding __all__ remains a superset of its v0.8.5 baseline.
The CHANGELOG-math gate verifies 347 - 344 = 3.
The v0.8.5 release is also the empirical demonstration of the audit-of-self pattern's
recursive applicability: the audit framework's own historical record was found to violate the
four-place pattern (the auditor name was load-bearing in source comments but not in test
fixtures or pinning tests), and the corrective release fixed the substrate without rewriting
history. The discipline applies to itself.

8 THE THIRTEEN QUALITY GATES
furqan-lint's continuous-integration pipeline runs thirteen quality gates against every pull
request. The gates are the operational form of the audit framework's quality baselines (Arfeen
2026i, §8); each gate is a falsifiable assertion about the project's substrate, enforced
mechanically rather than relied upon as author vigilance. This section documents the thirteen
gates, the test files that implement them, and the structural property each gate prevents from
drifting.
21

furqan-lint: A Structural-Honesty Linter

Arfeen, Thesis v1.0

8.1 The five tool-on-itself gates
The first five gates run furqan-lint against the project's own substrate. The pre-commit hook
configuration runs furqan-lint check src/ on every commit, and the same configuration is
invoked from the .github/workflows/ci.yml file under each Python-version row of the CI matrix.
The five tool-on-itself gates are: D24 (no Python file in src/ has a function with partial-path
return coverage failure), D11 (no Python file in src/ has a caller that consumes an Optional
producer without handling the None arm), R3 (no Python file in src/ has a function with zero
return statements declared with a non-None return type), return_none_mismatch (no Python
file in src/ has an explicit return None on a path declared with a non-Optional return type),
and additive-only on src/furqan_lint/__init__.py (no public name has been removed
without an explicit retirement procedure).
8.2 The CHANGELOG-math gate
test_changelog_math_gate.py parses the CHANGELOG entries for the current and previous

releases, extracts the documented test-count delta ("Test count: X (vN) -> Y (vN+1). Net
delta: +K"), and verifies that the actual pytest --collect-only count equals X for the
previous release and Y for the current release, and that Y - X equals K. The gate prevents
documentation drift between the CHANGELOG's test-count claim and the substrate's actual
test count.
8.3 The four-place completeness gate
walks the tests/fixtures/documented_limits/
directory and verifies that every documented limit has all four surfaces: a fixture file
demonstrating the limit, a pinning test asserting the current behavior on the fixture, a README
entry documenting the limit, and a CHANGELOG entry naming the version in which the limit
was documented or retired. The gate is the operational form of the framework's four-place
pattern (Arfeen 2026i, §11); a documented limit that exists in only three of the four places is a
finding that fails CI.
test_four_place_completeness_gate.py

8.4 The release-sweep gate
test_release_sweep_gate.py verifies version-string consistency across pyproject.toml's
project.version field, src/furqan_lint/__init__.py's __version__ string, and the

most-recent CHANGELOG entry's version header. The gate prevents the class of release-time
defects in which the substrate version is updated in one place but not the others. The gate
also verifies that the CHANGELOG entry's date matches the current date when the version is
bumped, preventing back-dated entries.
8.5 The extras-matrix gate
test_extras_matrix_gate.py reads the optional-dependencies section of pyproject.toml
([project.optional-dependencies] with rust and go entries) and verifies that the

.github/workflows/ci.yml file declares CI jobs exercising each optional-dependency
configuration. The gate prevents the failure mode surfaced in v0.8.3's round-21 audit, in
which the Rust and Go adapters compiled in dev-loop but were not exercised under CI.

22

furqan-lint: A Structural-Honesty Linter

Arfeen, Thesis v1.0

8.6 The README-drift gate
test_readme_drift.py
(furqan-lint check,

verifies

that

public

commands

documented

in

README.md

furqan-lint diff, furqan-lint version) match the actual
subcommands registered in src/furqan_lint/cli.py's argument parser. The gate prevents

the failure mode in which a CLI subcommand is renamed in the substrate but the README
continues to advertise the old name.
8.7 The origin-tag-presence smoke gate
test_origin_tag_presence_smoke.py is a smoke test that verifies the origin remote has a tag
matching the current substrate's version. The gate runs only when CHECK_ORIGIN_TAGS=1 is

set, so it does not fail local development; the CI configuration sets the variable on
release-bump commits. The gate prevents the failure mode in which a release tag is
committed locally but not pushed to origin, leading to a PyPI publication without a
corresponding GitHub tag.
8.8 The Go-specific gates
Three additional gates run only on the [go] extra: test_go_documented_limits.py mirrors the
four-place
completeness
gate
for
Go-specific
limits
in
tests/fixtures/go/documented_limits/; test_goast_qualified_methods.py verifies the
v0.8.2
qualified-method-name
behavior
of
the
goast
binary;
and
test_go_public_surface_additive.py applies the additive-only check to Go fixtures.
8.9 What the gates do not enforce
The thirteen gates are deliberately narrow. They enforce structural properties of the project's
substrate, not subjective code-quality judgments. Cyclomatic complexity is monitored by ruff
(the Python linter, configured via pyproject.toml's [tool.ruff.lint] section); type soundness
is enforced by mypy --strict; test coverage is reported by pytest-cov but not gated. The
gates documented here are specifically the structural-honesty layer; they complement rather
than replace the conventional gates that ruff, mypy, and pytest already supply.

9 VALIDATION METHODOLOGY
The validation methodology for furqan-lint operates at three layers: unit-test validation of
individual checker behavior, integration-test validation of the CLI and adapter pipelines, and
gate-test validation of the project's own discipline. This section documents each layer, the
test markers used to organize them, and the empirical claims the methodology supports.
9.1 Unit-test layer
Unit tests exercise individual checker functions against fixtures. The fixtures live in
tests/fixtures/ and are organized into clean/, failing/, and documented_limits/
subdirectories per language. clean/ fixtures are valid source code that should not trigger any
check; failing/ fixtures are source code crafted to trigger exactly one check;
documented_limits/ fixtures demonstrate known limitations of the current implementation. Unit
tests are marked with the unit pytest marker (registered in pyproject.toml's

23

furqan-lint: A Structural-Honesty Linter

Arfeen, Thesis v1.0

[tool.pytest.ini_options] markers list) and run in-process, in single-digit milliseconds.

The fixture-driven pattern is deliberate: every checker has a clean/ companion that
demonstrates the false-negative case (a true positive in the source language that the checker
correctly does not flag) and a failing/ companion that demonstrates the true-positive case.
The two together pin the checker's firing condition; a regression that introduces a false
positive on the clean/ fixture or a false negative on the failing/ fixture surfaces immediately. As
of v0.8.5 the project ships eleven Python failing fixtures, ten Python clean fixtures, four
Python documented-limits fixtures, plus parallel sets for Rust and Go.
9.2 Integration-test layer
Integration tests exercise the CLI end-to-end via subprocess invocation. The integration
pytest marker organizes them; tests in this layer take seconds rather than milliseconds.
Integration tests verify that furqan-lint check exits with the correct code (0 on clean, 1 on
findings, 2 on argument errors), that diagnostic prose matches expected patterns, and that file
and directory inputs are handled correctly. The integration layer is what the GitHub Action
exercises in the wild.
Three additional integration markers organize specialized tests: network (tests requiring
network access, used for the v0.8.4 PyPI Trusted Publishing verification), slow (tests taking
several seconds), and mock (tests using unittest.mock or pytest-mock). The markers allow
developers to skip slow or network-dependent tests during fast feedback loops while
ensuring CI exercises the full set.
9.3 Gate-test layer
Gate tests are the audit-of-self layer documented in §8. They validate properties of the
project's own substrate rather than of the checker behavior on consumer code. A gate test
failing means the project itself has drifted, not that the tool has a bug. The thirteen gates
documented in §8 are all gate tests; together they comprise approximately 30% of the test
count (105 of 347 tests as of v0.8.5).
9.4 The fixture-as-SUI distinction
A subtle but important distinction in the test architecture: the failing/ fixtures are intentionally
malformed Python (or Rust, or Go) source. They are System Under Inspection (SUI) for
furqan-lint, not System Under Test (SUT). Running ruff or mypy against them would defeat the
purpose. pyproject.toml's [tool.ruff.lint.per-file-ignores] section explicitly excludes
tests/fixtures/** from all ruff rule checks. The distinction is part of the four-place pattern's
implementation: the README and the CHANGELOG document the limits, and the
fixture-plus-pinning-test pair makes the limits structurally testable.
9.5 The empirical replicability claim
The full validation suite runs in approximately ninety seconds on a typical developer laptop
(Apple Silicon M-series or comparable x86_64). On the GitHub Actions ubuntu-latest runners
the fourteen-job matrix completes in approximately five to seven minutes wall-clock,
parallelized across runners. The replicability claim is that any reviewer with access to the
public repository can clone at v0.8.5, run pip install -e ".[dev,rust,go]" with a Go 1.21+

24

furqan-lint: A Structural-Honesty Linter

Arfeen, Thesis v1.0

toolchain available, and reproduce all 347 tests passing in under ten minutes. The claim is
falsifiable; reviewers wishing to verify it can do so directly.
9.6 The empirical-gap claim and the comparator-analysis successor study
The empirical-gap claim in §1.2 ("the specific empirical gap, case-illustrated by running both
tools on the same fixtures") is grounded in the worked example in §5 of the white paper and in
the failing/clean fixture pairs in tests/fixtures/. Each fixture is constructed to either trigger
or not trigger a specific check; running ruff and mypy on the failing/ fixtures empirically
demonstrates that those tools do not flag the structural-honesty defect that furqan-lint
catches. This is case-illustrated verification, not corpus-validated verification.
The distinction matters. A case-illustrated claim says: in this specific shape, ruff passes,
mypy in default mode passes, and furqan-lint flags. A corpus-validated claim says: across a
representative corpus of N production codebases, the rates of false negatives in ruff and
mypy on the structural-honesty class are X percent and Y percent respectively, while
furqan-lint's false-negative rate is Z percent. The current paper supports the first claim
directly; the second claim requires a systematic comparator study that has not yet been
conducted.
The systematic comparator study is named here as successor work. Minimum-viable
scope:
select
5
to
10
production
Python
codebases
(open-source,
commercial-with-permission, or both) of comparable size and complexity; run ruff, mypy in
default mode, mypy --strict, pyright, and furqan-lint check against each; classify findings by
structural-honesty category; report per-tool detection and false-positive rates with
confidence intervals. The study would convert the case-illustrated claim into a
corpus-validated claim and is the natural empirical successor to this paper. Effort estimate:
forty to eighty hours after the standard 75 percent buffer; the study is bounded scope and
could ship as a v1.1 update or as a separate empirical paper.
Until the comparator study ships, readers should interpret the empirical-gap claim as
case-illustrated. The cases the paper documents are real and reproducible; the generalization
across a representative corpus is claimed but not yet demonstrated. This is the same
structural-honesty discipline §11.3 applies to the methodological limitations: surface and
substrate must match, and the substrate of the empirical-gap claim is currently the
failing/clean fixtures plus the worked example, not a corpus.

10 RECIPROCAL CONTRACT: TOOL-ON-ITSELF
The Bayyinah Audit Framework's reciprocal contract (Arfeen 2026i, §15) names the
disciplinary symmetry between the tool and the operator. furqan-lint is a particularly clean
instance of the contract because the tool's domain (catching structural-honesty drift in code)
and the tool's own substrate (code that catches structural-honesty drift) are isomorphic. This
section documents how the contract operates in practice and what failure modes the
audit-of-self pattern surfaces that an external auditor would not.
10.1 The recursive domain

25

furqan-lint: A Structural-Honesty Linter

Arfeen, Thesis v1.0

The reciprocal contract is non-trivial in furqan-lint's case because the domain and substrate
are recursive. A linter for structural honesty whose own code is structurally dishonest is a
contradiction; the substrate of the tool's claims is the tool itself. If furqan-lint check src/
produced findings, the tool would be unable to ship without either fixing the findings or
admitting that its own claim of structural honesty is provisional. The recursion is not a
rhetorical flourish; it is a structural property of the project's release pipeline.
In practice the recursion is operationalized through the pre-commit hook. Every commit to
src/ runs furqan-lint check src/. A finding blocks the commit at the local machine, before it
reaches origin. If a finding nevertheless lands on origin (for example, via a manual override or
a hook bypass), the CI matrix re-runs the same check on every supported Python version and
fails the pull request. There is no path by which a finding ships to PyPI.
10.2 The audit-of-self failure modes
Three specific failure modes the audit-of-self pattern surfaces, that an external auditor with
periodic engagement would likely miss. First, drift in inline comments: an audit chain that
attributes findings to a specific named auditor in source-code comments is a four-place
violation if the going-forward convention attributes them differently (the v0.8.5 corrective). An
external auditor reviewing the substrate would not surface inline-comment drift unless
explicitly tasked with it; the recursive audit-of-self does, because the going-forward
convention is itself part of the framework's discipline.
Second, dead-code retirement pinning: a function removed in commit b0a4b18 (the v0.6.1
retirement of _d24_diagnostic_in_r3_set) is at risk of accidental re-introduction in a future
commit. The four-place pattern requires a pinning test asserting non-existence; v0.7.3 added
it. An external auditor verifying the v0.6.1 commit would confirm the function is gone but
would not necessarily add a forward-compatibility pin; the recursive audit-of-self does.
Third, prompt-execution drift: a corrective-action prompt that would have shipped errors if
executed verbatim was discovered to contain five errors during a round-8 review (the v0.4.1
round). The four-revision prompt review pattern (Arfeen 2026i, §12.3) emerged from this
finding. An external auditor reviewing the v0.4.0 substrate would not have caught the
prompt's errors, because the prompt is the recipe and the substrate is the meal; you cannot
taste an unexecuted recipe. The recursive audit-of-self caught it because the audit operates
one level above the substrate, on the prompts that produce the substrate.
10.3 The trust gradient
A reasonable critique of the audit-of-self pattern is that it cannot substitute for an adversarial
external audit. This critique is correct; The Bayyinah Audit Framework v3.0 (Arfeen 2026i,
§21) explicitly names "audit-of-self has an inherent ceiling on adversarial rigor" as one of the
framework's three documented limitations. furqan-lint inherits the limitation. The structural
defenses named in §15.1 of the framework reduce the gap but do not close it. For projects
where regulatory compliance, safety-critical certification, or third-party trust is the binding
constraint, audit-of-self under furqan-lint should be a complement to traditional two-party
audit, not a replacement.
That said, the audit-of-self pattern documented here is empirically what produced the
twenty-seven-version trajectory across two days, with cycle-time compression from

26

furqan-lint: A Structural-Honesty Linter

Arfeen, Thesis v1.0

multi-round closures to single-round closures and a monotonically declining severity slope.
The pattern is offered as the discipline that scales when the team is small, the substrate is
moving fast, and traditional two-party audit is structurally unavailable. It is not offered as a
universal substitute.

11 LIMITATIONS
Three classes of limitation apply to furqan-lint as of v0.8.5. The first is checker-coverage
limitations: shapes the existing checkers do not detect. The second is language-coverage
limitations: features of Python, Rust, or Go that the adapters do not yet handle correctly. The
third is methodological limitations: properties of the audit-of-self pattern that
single-practitioner validation cannot demonstrate. A fourth class is tooling-integration
limitations: surfaces where furqan-lint does not yet meet developers in their existing workflow.
Naming these limitations is itself an application of the framework's discipline; the surface (the
tool's claims) must match the substrate (what has been empirically demonstrated).
11.1 Checker-coverage limitations
Five Furqan structural-honesty primitives are not implemented as checkers in the current
release. Bismillah blocks (scoped initialization with purpose-hierarchy declaration) are a
Furqan language feature without a direct static-analysis analogue on Python, Rust, or Go; no
checker is planned. Mizan calibration constraints are similarly Furqan-specific. Tanzil build
ordering with regression gates is partially covered by the existing additive-only check on the
public surface but does not cover internal module-load ordering. Marad diagnosis-structured
error handling is the Furqan language feature that operationalizes the seven-marker
diagnostic taxonomy; furqan-lint does not currently inspect error-handling structure.
11.2 Language-coverage limitations
Documented limits as of v0.8.5: aliased Optional imports (e.g., from typing import Optional
as Opt) are recognized for the simple case but not when the alias is imported through an
intermediate module; aliased Union imports have a similar limitation; local class definitions
inside function bodies are excluded from D24 path analysis; try-body-only-returns-in-block
fall-through is excluded from R3 (caught by D24's partial-path coverage instead). Each limit
has a fixture in tests/fixtures/documented_limits/ and a pinning test.
For Rust: lifetimes, generics with trait bounds, macro expansion (no checker runs on
macro-expanded code), closure return-type inference, and Cargo workspace traversal (the
adapter operates per-file and does not follow Cargo workspace boundaries). For Go: generics
with type parameters (Go 1.18+) are not yet recognized in the producer-predicate; the (T,
error) recognition is reliable for non-generic code; method receivers are recognized for
public-name extraction (since v0.8.2) but not yet for D11 receiver-method calls.
11.3 Methodological limitations
furqan-lint has been validated by a single practitioner over a two-day window. Generalizability
to other teams, other domains, other repository topologies, and other AI model families is
claimed but not yet demonstrated. The audit-of-self pattern in particular may behave
differently when adopted by practitioners whose epistemic habits differ from the author's; the
27

furqan-lint: A Structural-Honesty Linter

Arfeen, Thesis v1.0

methodology assumes a practitioner already disposed toward structural-honesty discipline
before the framework is read.
The compressed-timeline replicability claim is a property of the validation conditions rather
than of the tool. Software domains with longer feedback loops should not be expected to
exhibit the same cycle-time compression. The tool should reduce structural debt in those
domains as well, but the May 2 through 3 development tempo should not be expected to
transfer linearly. This limitation is inherited from The Bayyinah Audit Framework v3.0 (Arfeen
2026i, §21) and applies equally to furqan-lint.
11.4 Tooling-integration limitations
furqan-lint runs as a command-line program, as a pre-commit hook, and as a
continuous-integration GitHub Action. It does not yet ship a Language Server Protocol
implementation, which means findings do not surface in editors as red squiggles or hover
tooltips. Developers see findings at three points in the development loop: when they invoke
furqan-lint check src/ manually, when pre-commit runs at git commit time, and when CI
runs on pull-request push. The most expensive of those for the developer is the pre-commit
failure, because the work has been written and the feedback arrives late. An LSP
implementation would surface findings at typing-time, which is the cheapest correction point.
The omission is a deliberate scope decision rather than an oversight: shipping an LSP requires
per-editor extension packages and a different release cadence than a Python package, and
the audit chain prioritized correctness of the underlying checkers across three languages over
editor-surface delivery. LSP is expected to land alongside the IDE-integration phase of the
broader project; no specific quarter is committed.
A related integration gap: furqan-lint does not yet provide auto-fix suggestions. ruff's fixer
model (where many findings carry a structurally-safe replacement that pre-commit can apply
automatically) is not implemented for furqan-lint findings. Some findings, particularly D24
missing-return cases, have a single canonical fix shape (add an explicit return None or
restructure); others, particularly D11 status-coverage findings, have multiple legitimate fix
shapes (handle the None case, propagate the Optional, or constrain the upstream type).
Auto-fix is therefore implemented for the canonical-fix subset only when implemented.
Auto-fix is expected to land for D24 first as the simplest case, with D11 and additive-only
deferred indefinitely because their fixes are non-canonical.

12 APPLICATION DOMAINS
furqan-lint is not for every project. Its overhead pays rent only on projects where the cost of a
structurally-dishonest defect is high enough to justify the discipline. Detailed
application-domain analysis appears in the Application Brief (Arfeen 2026j), which names
seven commercial domains by adoption-leverage rank: healthcare software, regulated
infrastructure, multi-agent AI development pipelines, quantitative finance and trading
infrastructure, API-first companies, AI safety and alignment research, and open-source
projects with volunteer maintainers. The Bayyinah Audit Framework v3.0 (Arfeen 2026i,
§23-24) supplies the same content with the public-interest extension covering sentence
calculation, COMPAS-style algorithmic risk assessment, debt collection, and predatory
lending.
28

furqan-lint: A Structural-Honesty Linter

Arfeen, Thesis v1.0

This section names the application-fit profile from the tool's perspective: which projects
are high-fit, which are marginal, and which are not-fit. The recommendations are
conservative; users adopting furqan-lint should match the profile, not aspire to it.
12.1 High-fit
Five project shapes are high-fit. First, libraries with a published public surface: any Python,
Rust, or Go library on PyPI, crates.io, or proxy.golang.org that has external consumers. The
additive-only check provides direct value at the release boundary. Second, services with API
stability requirements: any backend service whose API contract affects downstream
consumers. Third, codebases with safety implications: medical device firmware, financial
infrastructure, alignment research code. Fourth, multi-author codebases where context is not
shared: open-source projects with rotating contributors, AI-assisted codebases where the
author and reviewer are different model instances. Fifth, codebases under active development
with frequent releases: the discipline scales with cycle frequency; high-velocity teams benefit
most because the cumulative cost of small structural drifts compounds quickly.
12.2 Marginal-fit
Two project shapes are marginal-fit. First, internal tools with a small consumer base: the
additive-only check still provides value, but the overhead of running the full suite on every
commit may not pay rent if the team is comfortable with periodic ad-hoc review. Second,
codebases with extensive existing static analysis (ruff, mypy, language-specific tooling):
furqan-lint adds the structural-honesty layer that the existing tools miss, but if the team's
empirical defect-discovery rate is already low, the marginal value of the additional check is
correspondingly lower.
12.3 Not-fit
Three project shapes are not-fit. First, prototypes and hackathon code: the overhead kills
velocity. Second, solo developer projects with no external consumers: the additive-only check
serves consumers; if there are none, it is documentation for nobody. Third, codebases where
the cost of a bug is low: internal dashboards, one-off scripts, exploratory data-analysis
notebooks. furqan-lint's value scales with the cost of failure; below a threshold the discipline
costs more than the bugs it prevents.

13 CODE AND DATA AVAILABILITY
furqan-lint and a constellation of sibling resources are publicly hosted under the
BayyinahEnterprise organization on GitHub. furqan-lint is also published on the Python
Package Index. All resources are listed in Table 4 below.
Verification path: clone furqan-lint at v0.8.5, install development dependencies via pip
install -e ".[dev,rust,go]" (a Go 1.21+ toolchain is required on PATH at install time for the
goast binary to compile), and run pytest. All 347 tests should pass on Python 3.10, 3.11, 3.12,
or 3.13. The full pre-commit suite (ruff, mypy --strict, pytest, furqan-lint check src/) should
likewise complete clean.

29

furqan-lint: A Structural-Honesty Linter

Arfeen, Thesis v1.0

Reviewers wishing to reproduce the empirical claims in §7 (twenty-seven-version
trajectory) and §8 (thirteen quality gates) can inspect the CHANGELOG.md file at the head of
the repository, which preserves all release entries from v0.1.0 through v0.8.5 verbatim per the
framework's immutability discipline. Each entry names the round of the audit chain, the
severity-classified findings closed, and the test-count delta. The audit chain's discipline is
itself observable: every CHANGELOG entry has the same structural shape, with Five
Questions (§11.3 of the framework) answered explicitly.
Resource

URL

Release

furqan-lint repository

github.com/BayyinahEnterprise/fu
rqan-lint

v0.8.5

furqan-lint on PyPI

pypi.org/project/furqan-lint

v0.8.5

Furqan programming language

github.com/BayyinahEnterprise/fu
rqan-programming-language

v0.11.1

Bayyinah Integrity Scanner

github.com/BayyinahEnterprise/Ba v1.2.3
yyinah-Integrity-Scanner

Project home

bayyinah.dev

--

Framework executable demo

tryfurqan.com

--

Table 4. Resource locator. All BayyinahEnterprise repositories are public; furqan-lint and
the Furqan language are licensed Apache 2.0; framework documents are CC BY-NC 4.0;
thesis and white paper are CC BY 4.0.
Licenses: furqan-lint is licensed under Apache 2.0; this thesis paper and the companion
white paper are licensed under Creative Commons Attribution 4.0 International (CC BY 4.0),
permitting commercial use, redistribution, and adaptation with attribution. The Bayyinah Audit
Framework v3.0 and its Application Brief are licensed under Creative Commons
Attribution-NonCommercial 4.0 International (CC BY-NC 4.0); commercial use of the
framework documents requires a separate license: bayyinahenterprises@tuta.com. The
license asymmetry is intentional: furqan-lint and its papers ship under permissive terms
because the tool itself is open source under Apache 2.0, and the papers describing it should
not impose more restrictive terms than the tool. The framework documents impose CC BY-NC
4.0 because the framework's primary value is methodological and licensing protects the
discipline from being repackaged commercially without engagement.

14 REFERENCES
14.1 BayyinahEnterprise companion publications
Arfeen, B. S. (2026a). Detecting Performed Alignment in Artificial Systems -- The Munafiq
Protocol (v2.1). Zenodo. https://doi.org/10.5281/zenodo.19700420
Arfeen, B. S. (2026b). Bayyinah: Detecting Concealed Adversarial Content in Digital
Documents (v.1). Zenodo. https://doi.org/10.5281/zenodo.19745154
Arfeen, B. S. (2026c). Bayyinah as Input-Layer Defense in Artificial-System Safety Pipelines
(v1.1). Zenodo. https://doi.org/10.5281/zenodo.19802455

30

furqan-lint: A Structural-Honesty Linter

Arfeen, Thesis v1.0

Arfeen, B. S. (2026d). Al-Khalifa: A Furqan-Based Super Agent Architecture (v2). Zenodo.
https://doi.org/10.5281/zenodo.19776577
Arfeen, B. S. (2026e). Bilal: An Honest-Autonomous Large Language Model Architecture
(v2). Zenodo. https://doi.org/10.5281/zenodo.19776576
Arfeen, B. S. (2026f). The Fatiha Construct: A Seven-Step Recursive Session Protocol (v.1).
Zenodo. https://doi.org/10.5281/zenodo.19746539
Arfeen, B. S. (2026g). Bayyinah al-Maal: Structural Honesty Verification for Financial Filings
(v1.0). Zenodo. https://doi.org/10.5281/zenodo.19875931
Arfeen, B. S. (2026h). Al-Mutaffifin: Structural Integrity Verification for Financial
Governance Systems (v1.2). Zenodo. https://doi.org/10.5281/zenodo.19894724
Arfeen, B. S. (2026i). The Bayyinah Audit Framework v3.0: Structural Honesty for
AI-Assisted Software Engineering. Zenodo. https://doi.org/10.5281/zenodo.20017335
Arfeen, B. S. (2026j). The Bayyinah Audit Framework: Application Brief (v1.0). Zenodo.
https://doi.org/10.5281/zenodo.20031395
Arfeen, B. S., & Ashraf, F. (2026a). Bayyinah al-Khabir: Information-Layer Integrity
Scanning (v1.0). Zenodo. https://doi.org/10.5281/zenodo.19746298
Arfeen, B. S., & Ashraf, F. (2026b). Cross-Text Computational Linguistics (v1). Zenodo.
https://doi.org/10.5281/zenodo.19961267
Ashraf, F. R., & Arfeen, B. S. (2026). Furqan: A Programming Language with Structural
Honesty (v2). Zenodo. https://doi.org/10.5281/zenodo.19776584
14.2 External references
Astral. (2025). ruff: An extremely fast Python linter and code formatter, written in Rust
[Computer software]. https://github.com/astral-sh/ruff
Python
Software
Foundation.
(2025).
https://docs.python.org/3/library/ast.html

Python

ast

module

documentation.

tree-sitter contributors. (2025). tree-sitter and tree-sitter-rust libraries [Computer
software]. https://github.com/tree-sitter/tree-sitter
Go Project. (2025). Go standard library go/ast package. https://pkg.go.dev/go/ast
mypy contributors. (2025). mypy: Optional static typing for Python [Computer software].
https://mypy.readthedocs.io/
Python Enhancement Proposal 517. (2017). A build-system independent format for source
trees. https://peps.python.org/pep-0517/
Python Enhancement Proposal 604. (2019). Allow writing union types as X | Y.
https://peps.python.org/pep-0604/

15 ACKNOWLEDGEMENTS
I thank Fraz Ashraf for framework methodology contributions to The Bayyinah Audit
Framework v3.0 (Arfeen 2026i), the discipline under which furqan-lint was built. The
substrate-tradition engineering approach that grounds every claim, every finding, and every

31

furqan-lint: A Structural-Honesty Linter

Arfeen, Thesis v1.0

retirement in the audit chain traces in part to his contribution; this tool is the operational
instance of the framework. Per the v0.8.5 attribution discipline, the auditor role across the
twenty-three-round chain has been Bilal applying the framework to his own substrate; tool
authorship and the trajectory documented here are sole-author work.
Audit drafts and code review across the twenty-seven-version trajectory were assisted by
Claude Sonnet 4.6 and Claude Opus 4.6 / 4.7 (Anthropic) and Perplexity Computer (Comet);
literature engagement was assisted by Grok (xAI). The four-revision prompt review pattern
(Arfeen 2026i, §12.3) governs all AI-executed corrective sequences in the project; all findings,
verdicts, and final tool decisions are the responsibility of the author.
This thesis paper and the companion white paper are licensed under Creative Commons
Attribution 4.0 International (CC BY 4.0), permitting commercial use, redistribution, and
adaptation with attribution. The furqan-lint tool itself is licensed under Apache 2.0 (see the
LICENSE file in the repository). Citations should reference the Zenodo DOI assigned upon
upload.
furqan-lint v0.8.5 (substrate documented; v0.11.6 current as of writing) · thesis paper v1.0 ·
May 9, 2026 · CC BY 4.0 · Bilal Syed Arfeen

32



Bismillah ir-Rahman ir-Rahim
