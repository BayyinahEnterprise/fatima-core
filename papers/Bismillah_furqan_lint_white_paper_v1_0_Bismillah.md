Bismillah ir-Rahman ir-Rahim

furqan-lint
The structural-honesty checks ruff and mypy do not catch, across
Python, Rust, and Go
Bilal Syed Arfeen
BayyinahEnterprise
bayyinahenterprises@tuta.com
White Paper · Version 1.0

EXECUTIVE SUMMARY
This paper documents furqan-lint v0.8.5 (May 3, 2026), the substrate that grounds the
empirical record in the companion thesis paper. The latest release at the time of writing is
v0.11.6 (May 9, 2026); the test count has grown from three hundred and forty-seven at v0.8.5
to five hundred and ninety-nine at v0.11.6, the project has added a fourth language adapter
(ONNX, v0.9.0) and a Sigstore-CASM Gate 11 verifier for Python and Rust (v0.10.0 plus
v0.11.0), and the structural-honesty claims in this paper apply equally to the current head:
subsequent versions extend rather than retract the surface described here. Readers seeking
the current substrate state should consult CHANGELOG.md at the repository head.
There is a class of bug ruff and mypy do not catch. It is the bug where a function correctly
handles an Optional locally (checks for None, branches cleanly) but propagates the result
through a return type that strips the original incompleteness, and the next caller down the
chain consumes it as if the Optional had never existed. It is the bug where a refactoring
renames a public function and downstream consumers' imports can break in production, with
no mypy error because mypy operates on one version at a time. It is the bug where the
codebase has no type annotations at all (the majority of real Python), mypy passes silently in
default mode, and the structural drift goes uncaught for months. It is the bug that ships with
green continuous-integration results, a clean code review, and confident documentation, then
breaks in production when an end user constructs the input the test suite never tried.
furqan-lint is the linter that catches that class of bug. Five checks ship in the current
release: D24 (all-paths-return), D11 (status-coverage on Optional and Result and (T, error)
producers), R3 (zero-return / ring-close), return-None mismatch, and additive-only
public-surface diff. mypy in --strict mode catches the obvious return-type mismatches when
annotations are present and complete; furqan-lint catches the cases mypy structurally cannot:
status propagation through narrowing return types (D11's caller-signature case),
public-surface deletion across versions (additive-only diff), and the no-annotation cases that
comprise the majority of real Python codebases. Together with ruff and mypy, the three tools
form a three-layer pre-commit stack each layer of which catches what the previous layers
cannot.
ruff catches style. mypy catches the type errors you wrote down. furqan-lint catches the
structural drift between what your function says it returns and what its substrate, propagated
through callers and across versions, actually delivers.

1

furqan-lint: Structural-Honesty Linter

Arfeen, White Paper v1.0

The tool ships across three languages with Python as the default install and Rust and Go as
optional pip extras: pip install furqan-lint covers all four Python checks; pip install
furqan-lint[rust] adds D24, D11, and R3 on Rust source via tree-sitter; pip install
furqan-lint[go] adds D24, D11, and additive-only on Go source via a Go binary compiled at
install time. It runs as a command-line program, as a pre-commit hook, and as a
continuous-integration GitHub Action that adds three lines to a workflow file. It is published on
PyPI as furqan-lint and licensed under Apache 2.0.
This white paper introduces the tool to technical decision-makers: the gap furqan-lint
addresses, the four static checks plus the diff check, the three-language coverage with brief
theorization of additional adaptable languages, the CI integration story, a worked example,
and the application-fit profile. The companion thesis paper supplies the full technical
specification including the twenty-seven-version empirical record across two days of
development; the companion audit framework supplies the engineering discipline under which
the tool was built.

1 THE STRUCTURAL-HONESTY GAP
Three categories of static analysis are routine in modern engineering: style and formatting
(ruff in Python, rustfmt for Rust, gofmt for Go), type soundness (mypy in Python; the language
compilers themselves for Rust and Go), and security and dependency analysis (Snyk,
Veracode, language-ecosystem audit tooling). A specific class of defects falls outside all three
categories. We call it structural-honesty defects. The class has four shapes.
1.1 Optional collapse through propagation
A Python function declares it returns Optional[X]. Its caller correctly handles both branches
locally (checking for None, returning a default on the None arm). The caller's return type
annotation, however, is X (not Optional[X]). The original incompleteness has been silently
narrowed away in the type signature. Two function calls down the chain, a consumer reads
the value as if it were always X. mypy passes because every individual function's body is
internally consistent; the structural drift is across the chain, not within any single function. The
defect ships when the upstream input causes the original Optional source to return None, the
local handler returns its default, and the downstream consumer treats the default as a real
value. furqan-lint's D11 check catches this because it compares the producer's declared
incompleteness against the consumer's declared completeness, even when both producer
and consumer pass mypy individually.
1.2 Silently-removed public name
A library author renames a public function inside a minor-version bump. Semantic versioning's
version string says "no breaking changes." Downstream consumers that import the old name
find their builds can break in production. No conventional tool catches this; the version string
is a contract the substrate does not enforce.
1.3 Zero-return ring-close on unannotated code
A function declares it returns an integer (or has no annotation at all). Its body has zero return
statements anywhere. In Python, falling off the end yields None, which is not an integer. When
2

furqan-lint: Structural-Honesty Linter

Arfeen, White Paper v1.0

the function is fully annotated, mypy in default mode catches this as "Missing return
statement." The defect ships in two empirically common cases mypy does not catch: when
the function has no return-type annotation (mypy passes silently in default mode on
unannotated code, and most production Python codebases are not under --strict), and when
the function is dynamically constructed in ways mypy's static analysis does not reach.
furqan-lint's R3 check fires unconditionally on the structural shape: a function declaring (or, in
unannotated cases, expected to return) a non-None type with zero return statements is
flagged regardless of whether mypy's annotations are complete enough to surface it. In Rust
the compiler rejects the shape; in Go the compiler rejects the shape; in Python the interpreter
does not.
1.4 Return-None mismatch on unannotated or dynamic code
A Python function expected to return a string has an explicit return None on at least one path.
When the function is fully annotated as returning str, mypy in default mode catches this as an
Incompatible return value type error. The defect ships, again, in the cases mypy does not see:
unannotated code (the majority of production Python in default-mode environments),
dynamically constructed functions, and functions whose return-type annotation has been
weakened to a Union or Any during a refactoring that mypy then accepts as conformant.
furqan-lint's return-None-mismatch check enforces the structural shape directly rather than
depending on annotation completeness. This is the strong form of (1.1) on a single function
rather than a propagation chain; it is detected separately because the diagnostic prose differs.
1.5 The empirical-gap claim is case-illustrated
The four shapes documented in this section are case-illustrated, not corpus-validated. The
companion thesis paper's §9.6 names the systematic comparator-analysis study as successor
work: a representative corpus of 5 to 10 production Python codebases run through ruff, mypy
default and strict modes, pyright, and furqan-lint, with per-tool detection and false-positive
rates reported with confidence intervals. Until that study ships, readers should interpret the
empirical gap claim as demonstrated on specific cases (the failing/clean fixtures plus the
worked example in §5) rather than across a representative corpus.

2 THE FIVE CHECKS
furqan-lint runs four static checks via the check subcommand and one diff check via the diff
subcommand. All five are derived from the structural-honesty primitives of the Furqan
programming language; they are translations of compile-time language semantics into
static-analysis findings on languages that lack those semantics.
2.1 D24: all-paths-return
Fires when a function with a non-None return type has at least one control-flow path that does
not reach a return statement. Closes the partial-path coverage gap. False positives
suppressed: provably-non-returning bodies (raise-only, while True without break),
@abstractmethod and @overload decorated functions.
2.2 D11: status-coverage
3

furqan-lint: Structural-Honesty Linter

Arfeen, White Paper v1.0

Fires when a function with a non-may-fail return type invokes a may-fail producer without
handling the failure case. May-fail producers: Optional[X] in Python, Option<T> and
Result<T, E> in Rust, (T, error) in Go. The cleanest case, deepest empirical history, and
most consequential check in the suite.
2.3 R3: zero-return / ring-close
Fires when a function with a non-None return type contains zero return statements anywhere.
Disjoint complement of D24: D24 catches partial-path, R3 catches zero-statement.
Documented not-applicable for Go (compiler rejects all firing shapes).
2.4 return-None mismatch
Fires when a Python function with a non-Optional return type has an explicit return None on at
least one path. Python-only by design: rustc and the Go compiler reject the corresponding
shapes at compile time, so the firing condition is unreachable on Rust or Go source.
2.5 additive-only diff
Invoked separately as furqan-lint diff old.py new.py. Fires on any public name present in
old that is absent in new. Adding a public name is silent. Renaming a public name is a finding
(structurally a deletion plus an addition). Diagnostic prose is language-aware: Python users
see Python alias suggestions, Go users see Go re-export hints, Rust users see Rust
analogues.

3 THREE-LANGUAGE COVERAGE
furqan-lint ships three language adapters that share a common runner pipeline. The adapters
translate source code into a unified intermediate representation; the same checker functions
then operate on the IR regardless of the source language. Table 1 summarizes coverage.
Check

Python

Rust

Go

D24 (all-paths-return)

applies

applies

applies

D11 (status-coverage)

applies

applies

applies

R3 (zero-return)

applies

applies

N/A (compiler rejects)

return-None mismatch

applies

N/A (compiler rejects)

N/A (compiler rejects)

additive-only diff

applies

applies

applies

Table 1. Coverage matrix across the three currently-shipping adapters. Cells marked N/A
denote firing conditions unreachable on source the language compiler accepts; the check is
documented not-applicable rather than absent.
3.1 Python (built-in)
Python adapter ships in the standard wheel. Installation via pip install furqan-lint covers
all four Python checks plus the Python diff. Translation uses the standard library's ast module
and the upstream Furqan adapter; no source build, no toolchain dependency.

4

furqan-lint: Structural-Honesty Linter

Arfeen, White Paper v1.0

3.2 Rust (opt-in via [rust])
Rust adapter ships behind pip install furqan-lint[rust]. Runs D24, D11, and R3 on .rs
files. Translation uses tree-sitter and tree-sitter-rust; both ship pre-built wheels for ARM64
and x86_64. Limitations: lifetimes, generic trait bounds, macro expansion, closure return-type
inference, and Cargo workspace traversal are not yet supported and are documented in the
README and pinned by tests/fixtures/rust/documented_limits/.
3.3 Go (opt-in via [go])
Go adapter ships behind pip install furqan-lint[go]. Runs D24, D11, and additive-only on
.go files. Translation uses a Go binary called goast that is compiled at install time via a PEP 517
build hook. The Go toolchain (1.21 or later) is required at install time but not at runtime; the
compiled binary ships in the wheel. R3 and return-None are documented not-applicable for Go
(compiler rejects firing shapes).
3.4 ONNX (opt-in via [onnx], shipped after v0.8.5)
A fourth adapter shipped in v0.9.0 (May 4, 2026) and is summarised here for completeness
although the documented v0.8.5 substrate predates it. ONNX support is behind pip install
furqan-lint[onnx] and runs three checks on .onnx computational graph files: D24-onnx
(all-paths-emit on graph outputs), opset-compliance (against a pinned opset registry), and
D11-onnx (shape and type coverage). Two further checks ship behind sub-extras:
numpy-vs-ONNX divergence under [onnx-runtime] and a score-validity ADVISORY under
[onnx-profile]. ONNX is documented as a parallel diagnostic family rather than an instance of
the existing checkers on a unified intermediate representation; the structural-honesty
primitives that govern Python, Rust, and Go map onto computational graphs by analogy rather
than by direct translation. v0.10.0 and v0.11.0 additionally ship a Sigstore-CASM Gate 11
verifier (Python plus Rust), a cryptographically-witnessed additive-only contract on the public
surface signed via Sigstore Rekor at release time.
3.5 Theorized future adapters
The three currently-shipping adapters are not the boundary of what the structural-honesty
primitives can address. The companion thesis paper (§5.4) develops a full theorization; the
executive summary appears here. Strong-fit candidates are languages with first-class
Option-or-Result-shaped sum types and an existing AST or compiler API: TypeScript and
JavaScript (TypeScript Compiler API or tree-sitter-typescript), Kotlin (tree-sitter-kotlin or
kotlinc PSI), Swift (SwiftSyntax), Scala (scalameta), C# (Roslyn with Nullable patterns or a
Result library), C++23 (libclang on std::optional and std::expected), OCaml and F#
(compiler-libs on option and Result), and Zig (its native ?T and !T forms). Partial-fit candidates
require additional translation work in the producer predicate: Java with its Optional and
checked-exception shapes, and Elixir with its {:ok, ...} | {:error, ...} convention.
Compiler-enforced families collapse the suite to additive-only as the primary value: Haskell,
where Maybe and Either firing conditions are mostly compiler-rejected. The weak-fit case
(Ruby) is named explicitly to delimit the framework's applicability rather than to suggest
adoption. None of these adapters are committed to a release schedule; the v0.8.5 release
ships with Python, Rust, and Go.

5

furqan-lint: Structural-Honesty Linter

Arfeen, White Paper v1.0

4 CI INTEGRATION IN THREE LINES
furqan-lint integrates into a project's continuous-integration pipeline through three
deployment paths: a GitHub Action, a pre-commit hook, or direct invocation as a
command-line tool. The first path adds three lines to a workflow file.
4.1 As a GitHub Action
# .github/workflows/furqan-lint.yml
name: Furqan Lint
on: [push, pull_request]
jobs:
lint:
runs-on: ubuntu-latest
steps:
- uses: actions/checkout@v4
- uses: BayyinahEnterprise/furqan-lint@v0.8.5
with:
path: src/

That is the integration. Every push and every pull request runs the four static checks
against the directory specified in path. Findings appear as GitHub Actions status checks; the
standard required-status-checks branch protection setting will then block merges of pull
requests with findings until they are resolved.
4.2 As a pre-commit hook
Run

the

same

checks

locally

on

every

git

commit

by

adding

furqan-lint

to

.pre-commit-config.yaml:
repos:
- repo: https://github.com/BayyinahEnterprise/furqan-lint
rev: v0.8.5
hooks:
- id: furqan-lint

Then pre-commit install. Findings block the commit at the local machine before the
change reaches origin. The recommended ordering pairs furqan-lint with ruff and mypy: ruff
first (lint and format), then mypy (types), then furqan-lint (structural honesty); each layer
catches what the previous layers cannot.
4.3 As a command-line tool
Direct

invocation:

path/to/file.py or furqan-lint
check
path/to/directory/. The diff subcommand: furqan-lint
diff
old_version.py
new_version.py. The version subcommand: furqan-lint version. Exit code 0 on clean, 1 on
furqan-lint

check

findings, 2 on argument errors. Composable with any continuous-integration system that runs
shell commands.

5 A WORKED EXAMPLE
Consider this Python module, representative of code Copilot or Claude Code might generate:

6

furqan-lint: Structural-Honesty Linter

Arfeen, White Paper v1.0

# example.py
from typing import Optional
def find_record(user_id: int) -> Optional[dict]:
if user_id < 0:
return None
return {"id": user_id, "name": f"user_{user_id}"}
def get_record_or_default(user_id: int) -> dict:
record = find_record(user_id)
if record is None:
return {}
return record
def display_name(user_id: int) -> str:
record = get_record_or_default(user_id)
return record["name"]

ruff passes. mypy in default mode passes. The propagation chain is the bug: find_record
honestly declares Optional[dict]; get_record_or_default handles the None arm locally
(returning an empty dict as a default) but its return-type annotation strips the original
incompleteness; display_name reads record["name"] from what looks like a dict, but on the
negative-id input the dict is empty and the substrate raises KeyError. mypy is not wrong to
pass: every individual function body is internally type-consistent. The structural drift is across
the chain, not within any single function. This is the bug that ships green. furqan-lint catches it
before the merge.
Run furqan-lint check example.py and the output is:
example.py:8: D11 (status-coverage)
get_record_or_default returns 'dict' but consumes Optional[dict]
from find_record. The caller's signature has silently narrowed
away the incompleteness that find_record declared.
Fix: declare get_record_or_default as returning Optional[dict],
so the union is honestly propagated to display_name. If the
narrowing is intentional, raise on the None arm rather than
returning a degenerate default:
record = find_record(user_id)
if record is None:
raise ValueError(f"no record for user_id={user_id}")
return record

The check fires at the line of the offending call. The diagnostic prose names the producer
(find_record) and the consumer (get_record_or_default). The fix is two structurally-distinct
shapes: propagate the Optional honestly (preferred when the caller may not always have a
record) or narrow with an explicit raise (preferred when the caller's contract is that a record
always exists). mypy passed both before and after the fix; the structural-honesty gap was
invisible to it.

6 WHERE FURQAN-LINT FITS
furqan-lint is not for every project. Its overhead pays rent only on projects where the cost of a
structurally-dishonest defect is high enough to justify the discipline. Five project shapes are

7

furqan-lint: Structural-Honesty Linter

Arfeen, White Paper v1.0

high-fit:
• Libraries with a published public surface. Any Python, Rust, or Go library on PyPI,

crates.io, or proxy.golang.org with external consumers. The additive-only check provides
direct value at the release boundary.
• Services with API stability requirements. Backend services whose API contract affects

downstream consumers. Stripe-grade reliability requires substrate-level enforcement of
the contract.
• Codebases with safety implications. Medical device firmware, financial infrastructure,

alignment research code. The structural-honesty class of defects is the class that
compounds catastrophically.
• Multi-author codebases without shared context. Open-source projects with rotating

contributors; AI-assisted codebases where the author and reviewer are different model
instances. Structural enforcement substitutes for shared context.
• Codebases under active development with frequent releases. The discipline scales with

cycle frequency; high-velocity teams benefit most because the cumulative cost of small
structural drifts compounds quickly.
The tool's value scales with the cost of failure. Below a threshold, the discipline costs more
than the bugs it prevents.
6.1 Where it does not fit
• Prototypes and hackathon code. The overhead kills velocity. Ship first; add discipline if

the prototype graduates to a product.
• Solo developer projects with no external consumers. The additive-only check serves

consumers; if there are none, it is documentation for nobody.
• Projects where the cost of a bug is low. Internal dashboards, one-off scripts, exploratory

data-analysis notebooks. The marginal value does not justify the overhead.
• Codebases where Optional/Result is not idiomatic. D11 (status coverage) is the central

check, and it requires Optional[T] / Result<T,E> / (T, error) producers to surface
findings. A codebase that consistently uses sentinel values, exceptions, or untyped
dynamic returns instead will see most D11 findings absent rather than green-passing.
furqan-lint will still run D24, R3, and additive-only, but the highest-value check is
structurally inactive.

INSTALL
pip install furqan-lint

pip install "furqan-lint[rust]" for Rust support. pip install "furqan-lint[go]" for

Go support (Go 1.21+ required at install time, not at runtime).

RESOURCES
• github.com/BayyinahEnterprise/furqan-lint · source repository (Apache 2.0).

8

furqan-lint: Structural-Honesty Linter

Arfeen, White Paper v1.0

• pypi.org/project/furqan-lint · latest release (v0.11.6 as of May 9, 2026; v0.8.5 is the

substrate documented in this paper).
• CHANGELOG.md · release history including all post-v0.8.5 advances (ONNX adapter in

v0.9.0, Sigstore-CASM Gate 11 in v0.10.0 + v0.11.0).
• tryfurqan.com · the tool, made executable, in a browser.
• bayyinah.dev · project home.

READ
This white paper is the introduction. Two companion documents supply the rest:
• Thesis paper · full technical specification: the five checkers, the three-language

implementation, the empirical trajectory across twenty-seven versions, the audit-of-self
pattern, the thirteen quality gates, validation methodology, and limitations.
• The

Bayyinah Audit Framework v3.0 (doi.org/10.5281/zenodo.20017335) · the
engineering discipline under which furqan-lint was built. Application Brief is the executive
companion to that document (doi.org/10.5281/zenodo.20031395).

DISCUSS
bayyinahenterprises@tuta.com · for technical decision-makers,
deployment, partnerships, and research collaboration.

regulated-industry

ruff catches style. mypy catches types. furqan-lint catches structural honesty.
furqan-lint v0.8.5 (substrate documented; v0.11.6 current as of writing) · white paper v1.0 ·
May 9, 2026 · CC BY 4.0 · Bilal Syed Arfeen

9



Bismillah ir-Rahman ir-Rahim
