Bismillah ir-Rahman ir-Rahim

1

Bayyinah al-Amāna: Provenance Integrity for Public Open Data
Verifying Declared Provenance, Freshness, and Schema Against the Substrate, with a
Reproducible Worked Example on New York MTA Datasets
Bilal Syed Arfeen (BayyinahEnterprise), with collaborative analytical assistance from
Claude (Anthropic).
DOI: 10.5281/zenodo.21446613. Audit and provenance ledger and dataset: DOI
10.5281/zenodo.21446618. Version 1.0, the canonical converged release (three consecutive
qualifying cross-instance audit passes; the two-consecutive-pass gate under Standing Rule 7 was
met and confirmed clean, with the rotation gap closed). Section 8 and the companion Current
State record the full round history and the honestly-recorded convergence caveats; the
reproduction package is deposited alongside the ledger at the second DOI.
Governed by: Bayyinah, Portable Structural Honesty Verification for Public-Service
Institutions (Arfeen 2026, the framework paper). Sibling notes: the Public-Ledger Allocation and
Asymmetric-Measure Audits (Arfeen 2026, DOI 10.5281/zenodo.21445552), which surfaced
and deferred the provenance divergence this note takes up; and Bayyinah at-Taʿlīm (Arfeen
2026, DOI 10.5281/zenodo.21436484).
Audit trail, full version history, and finding-by-finding provenance are published
separately in the Audit and Provenance Companion. The frozen captures and reproduction script
are published as a Companion Dataset (see Data Availability, Section 9).
"Render the trusts to those they belong to." (an-Nisa 4:58)

2
Abstract
Every civic-accountability analysis built on public open data silently assumes the data is
what the portal claims: official rather than derived, current rather than stale, and stable rather
than silently rewritten. This note applies Structural Honesty Verification to that assumption
itself. Structural Honesty Verification verifies the correspondence between a system's surface
(what it claims, reports, or certifies) and its substrate (what it actually is, produces, or contains).
Here the system is an open dataset, the surface is its declared provenance, freshness, and schema,
and the substrate is its actual provenance classification, row-level creation and update
timestamps, and served field inventory. The note defines three tiers of what can and cannot be
verified, and demonstrates the method end-to-end on two New York State datasets that report the
same underlying MTA procurement records: a community-created view (gpsc-qqsz) and the
first-party official dataset (twsw-2mqa). The worked example, reproducible from a single live
pull, establishes that the two diverge (identically in FY2023, by 70 records and about $58.1M in
FY2024, and by $0.75 in summed face value in FY2022 despite identical row counts); that both
datasets serve history whose currently-served rows were created hundreds to over a thousand
days after each fiscal year closed, in a single post-close batch (consistent with a wholesale
republish and equally with a first-time bulk load, which a single-pull timestamp cannot
distinguish); and that the community view exposes a different schema (23 fields versus 32). The
method detects and quantifies these divergences and refuses to judge whether any was legitimate,
authorized, or improper. It is a meta-layer: it makes the data-integrity assumption underlying
other accountability work checkable rather than inherited on faith.

3
1. Purpose and Scope
Structural Honesty Verification (SHV) is the verification of correspondence between a
system's surface and its substrate. Two sibling notes apply it to what public institutions distribute
(educational funding) and to what they report about procurement. Both, like nearly all open-data
analysis, rest on an unstated premise: that the portal serving the data is faithful, that a dataset
labeled official is first-party, that a "last updated" timestamp reflects the actual last change, and
that querying a closed historical period returns the same answer tomorrow as today. This note
verifies that premise directly.
The scope is deliberately narrow. The note measures provenance, freshness, and schema
fidelity as byte-level and structural facts. It does not assess data quality, accuracy, or fitness for
any purpose, and it does not adjudicate whether an observed divergence or post-close batch load
was a correction, a migration, an error, or a manipulation. That legitimacy question is reserved
for the publisher and for oversight; the method supplies the reproducible, tamper-evident
measurement those judgments would rest on, and stops there.
2. The Governing Divergence: Declared Provenance versus Actual Provenance
The surface of an open dataset is its self-presentation. A Socrata dataset declares a
provenance (official or community), a name, a schema, a row count, and a last-updated time, and
it implicitly presents any query against a closed reporting period as stable. The substrate is what
the bytes and system metadata actually show: whether the portal classifies the dataset as firstparty or as a derived view (the Socrata-declared provenance field, not an independent inquiry
into agency authorship), whether its currently-served historical rows were created at or long after
the period they describe, whether its served field inventory matches its declared schema, and
whether two datasets that claim to report the same records in fact agree.

4
Divergence between surface and substrate here is not rare or exotic. A communitycreated view can closely shadow an official dataset, close enough that a careful analyst
reproduces off the wrong one. A portal can republish an entire historical dataset years after the
fact while the "last updated" surface says little about how much of the past was regenerated. The
method names each such divergence precisely and quantifies it.
3. Tier Discipline: What Can and Cannot Be Verified
Consistent with the framework, the note sorts every claim into three tiers.
Tier 1 is verified and byte-deterministic: the SHA-256 of a frozen capture; a dataset's row
count and served field inventory; whether two datasets are byte-identical over a shared window;
and the row-level Socrata system timestamps :created_at and :updated_at for a fixed
historical window, including whether any historical row's timestamp postdates the close of its
own reporting period.
Tier 2 is structural and rests on disclosed parameters: the provenance classification read
from portal metadata (the Socrata-declared provenance field, official versus community view,
not an independent chain-of-custody inquiry); the declared last-updated time reconciled against
the actual row-timestamp distribution; and whether the served history is preserved-since-origin
or was instantiated in a single post-close batch, inferred from a uniform recent creation
timestamp across old rows (a batch that a single pull cannot resolve into a republish versus a
first-time bulk load).
Tier 3 is interpretive and is refused: whether a change was legitimate, authorized,
malicious, or intended to deceive; whether a divergence reflects error, correction, or
manipulation. The method detects and quantifies the divergence and hands the legitimacy

5
question to the publisher and to oversight. This refusal matters more here than in the sibling
notes, because the language of "silent edit" and "republished history" invites over-reading as an
accusation, and the substrate facts do not support one.
4. The Data-Interface Contract and the Socrata Adapter
The method depends on a small, portable interface. A Socrata portal exposes, for any
dataset, a metadata endpoint carrying provenance, schema, and last-updated fields, and a SODA
query endpoint that supports aggregate queries over the data and over the per-row system
columns :created_at and :updated_at. The dedicated revision endpoint
(/revisions.json) is not publicly served for these datasets, so a portal-native change log is
unavailable; the row-level system timestamps supply an available freshness signal (rowinstantiation timing) in its place, though not a full change log with prior values or edit
authorship. Because both New York City Open Data and data.ny.gov run Socrata, a single
adapter covers thousands of civic datasets. The MTA pair below is one worked instance of a
portable check, not an MTA-specific tool.
5. Worked Example: Two New York MTA Procurement Datasets
The datasets are gpsc-qqsz ("MTA Procurement Report (All)", declared provenance
community) and twsw-2mqa ("MTA Procurements: Beginning 2018", declared provenance
official), both on data.ny.gov, examined across the fiscal years ending December 31 of 2022,
2023, and 2024. Every figure below is reproducible from the accompanying package, offline
from a frozen capture and live against the endpoints.

6
5.1 Provenance classification and divergence
The metadata declares gpsc-qqsz a community-created view and twsw-2mqa official.
Comparing the two on the same reporting periods: FY2023 is identical (both 12,114 records,
$63,569,204,049.36); FY2024 diverges by 70 records and $58,072,427.23, a count divergence of
0.5103% and a face-value divergence of 0.0891%; and FY2022, despite identical row counts
(both 12,156), diverges by $0.75 in summed face value ($54,698,007,774.69 versus
$54,698,007,775.44). The last is the sharpest illustration of the method's resolution: a value-level
difference that a billion-rounded reading calls identical, surfaced only because the comparison is
exact.
5.2 Declared-versus-actual freshness
The primary freshness method reads the row-level :created_at system column for
each fixed historical window and asks whether the currently-served rows could have existed
when the period closed. They could not. In the community view, every FY2022, FY2023, and
FY2024 row carries a uniform :created_at of 2025-12-01, that is 1066, 701, and 335 days
respectively after each fiscal year closed. In the official dataset, every such row carries a uniform
:created_at of 2026-04-01, that is 1187, 822, and 456 days after close. A uniform creation

timestamp across an entire closed year indicates the window was instantiated in one batch after
the period closed, rather than through selective edits. That single-batch instantiation is consistent
with a wholesale republish of previously-served history and equally consistent with a first-time
bulk load of a dataset or view that had no prior served instance; a single live pull cannot
distinguish the two, and the note claims only the batch-after-close fact, not which of the two
produced it. Either way, none of the currently-served rows for that closed year predates a recent
bulk creation. The finding requires only a single live pull; no two-dated-pull time gap is needed.

7
5.3 Schema divergence
The community view serves 23 fields; the official dataset serves 32. Sixteen fields appear
in the official dataset but not the community view, and seven appear in the community view but
not the official dataset. Two datasets presenting as reports of the same records expose materially
different schemas, which a consumer selecting a source on name alone would not anticipate.
5.4 What the method emits, and what it refuses
At Tier 1 it emits the hashes, counts, exact divergences, and row timestamps. At Tier 2 it
emits the provenance classifications, the freshness reconciliation, and the post-close-batch
inference (a batch load after the period close, which a single pull does not resolve into a
republish versus a first-time bulk load). At Tier 3 it refuses: it does not conclude that the
community view is unauthorized, that any batch load was improper, that the FY2024 divergence
is an error in either dataset, or that any party intended to mislead. Batch loads, migrations, and
corrections routinely regenerate rows and their timestamps; detecting that a dataset's served
history was created recently is a substrate fact, not a charge.
6. Portability
The check generalizes to any Socrata-hosted dataset with a reporting-period field, and
degrades gracefully without one: the provenance, schema, snapshot-hash, and post-close-batch
checks need no period field, and only the "timestamp postdates period close" refinement does.
Across New York City Open Data and data.ny.gov alone this is thousands of datasets. The
value of the method is not the MTA finding but the portable capacity to verify, for any civic
dataset another analysis depends on, that its declared provenance, freshness, and schema match
its substrate.

8
7. Limitations
The method reads provenance, freshness, and schema; it says nothing about whether the
data values are correct, complete, or fit for a purpose. The freshness signal rests on Socrata's
:created_at/:updated_at semantics, which record when a row entered or last changed in

the served instance, not the full edit history; a portal that reloads a window wholesale erases finer
history, which the method reports as a post-close batch load (a republish or a first-time bulk load,
which a single pull cannot distinguish) rather than reconstructing what changed. The revision
endpoint being unavailable means the note cannot present a portal-native change log. The twodataset worked example is a demonstration of a portable method, not a survey; a systemwide
claim about the portal would require sampling many datasets. And, as everywhere in this
program, the note is producer-side and awaits the independent cross-instance audit described
next; no result here is convergence-verified.
8. Provenance and Verification
This is version 1.0, the canonical converged release. Under the framework's Standing
Rule 7, an artifact meets the convergence gate after two consecutive qualifying passes by
independent, non-producer-lineage auditors that execute the reproduction and return zero critical
and zero high findings. Three such passes have occurred (F-AM-R1, F-AM-R2, F-AM-R3), each
with at least two qualifying non-producer members returning zero critical and zero high; the
Claude producing lineage was quarantined throughout. The gate was met at F-AM-R2 and
confirmed clean at F-AM-R3 on the corrected artifact, and the F-AM-R3 pass-bearing set (GPT
5.5 and the rotated-in, successfully-isolated GPT 5.4) includes a qualifying member new relative
to the earlier clean pair, closing the rotation gap the earlier rounds could not. The remaining
caveat is honest and narrow: v1.0 is the thrice-passed substance with one LOW Section 1

9
wording fix absorbed (materially identical), and the convergence is met inside this producerdefined governance framework, while the externally-verifiable result -- every figure reproduces
exactly from live data.ny.gov under the exact fiscal-window filter, and the comparator is tamperevident under hash-gate defeat -- holds independently of the framework. The full round history
and finding-by-finding dispositions are in the Audit and Provenance Companion. The design
vocabulary (amāna as faithful safekeeping of a trust) is drawn from structural readings of the
Qur'an and is inspiration, not evidence: every figure in Section 5 is justified entirely by public
data, portal metadata, and arithmetic.
9. Data Availability and Reproduction
Every figure is reproducible from the New York State open-data portal without
authentication. The datasets are gpsc-qqsz and twsw-2mqa on data.ny.gov; provenance
and schema come from each dataset's metadata endpoint; freshness comes from the SODA
:created_at/:updated_at system columns filtered by fiscal_year_end_date; and the

divergence figures come from count(*) and sum(contract_amount) per fiscal year. A
frozen capture, its SHA-256 manifest, and a standard-library reproduction script that verifies the
hash, reproduces all four checks offline, re-pulls the live endpoints to detect drift, and self-tests
its own comparator accompany this note as a single reproduction package, deposited under an
immutable DOI alongside the audit and provenance ledger at DOI 10.5281/zenodo.21446618;
anyone can retrieve it there and re-run the full reproduction.
References
Arfeen, B. S. (2026). Bayyinah: Public-Ledger Allocation and Asymmetric-Measure Audits.
Zenodo. DOI 10.5281/zenodo.21445552. https://zenodo.org/records/21445552

10
Arfeen, B. S. (2026). Bayyinah at-Taʿlīm: Structural Honesty Verification for Educational
Fairness Systems. Zenodo. DOI 10.5281/zenodo.21436484.
https://zenodo.org/records/21436484
Arfeen, B. S. (2026). Al-Mutaffifīn: Structural Integrity Verification for Financial Governance
Systems. Zenodo. DOI 10.5281/zenodo.19894724. https://zenodo.org/records/19894724



Bismillah ir-Rahman ir-Rahim
