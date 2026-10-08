# Bismillah ir-Rahman ir-Rahim

# FATIMA -- Anatomy of the Code

## Second Edition: Evolved from the Living Body

**Artefact:** `fatima-core` @ commit `e0c609b`, package 0.1.0 -- code UNCHANGED
**First edition:** Perplexity Computer, 7 October 2026 (389 lines, parsed from live AST)
**This edition:** Claude Opus 4.6, 7 October 2026 -- integrating Canon v2.0, multi-model council, Rights and Survival organ mapping
**Lineage:** Anatomy of the Code (Perplexity) -> Canon Rev. 1 -> Code Evolution Canon v2.0 (Claude Opus) -> **this document**
**Extraction method:** parsed from the live AST -- every symbol below exists in the code exactly as written.
**Annotations:** `[P1]`--`[P5]` property served . `[L1]`--`[L5]` verification level . `dagger` canon finding (see Canon v2.0 SS6/SS8) . `diamond` module verdict . `[N/M]` multi-model convergence count

**New in this edition:**
- Canon v2.0 corrections C2-01 through C2-06 integrated as `[V2.0]` annotations
- Multi-model convergence counts from five-council analysis (SS13)
- Rights and Survival organ mapping -- which anatomical organ each module instantiates
- Updated file listing with documents committed since `e0c609b`
- Source-witness independence correction (C2-02): Code_Absorption.txt is reproduced verbatim inside Bilal_Code_Audit.txt -- they are one witness, not two

---

```
bilal@bayyinah:~$ tree -L 2 fatima-core/
fatima-core/
├── pyproject.toml                          # package metadata, version 0.1.0
├── FATIMA_paper.fatima                     # the paper, encoded in its own format
├── Ghayb_11C_paper.fatima                  # second encoded document
├── CODE_EVOLUTION.md                       # Era I–IX historical record (Rev 2)
│                                           #   [V2.0] nine eras, not seven (C2-04)
├── CODE_EVOLUTION_CANON_V2.md              # [NEW] canonical ingestion file, v2.0
├── COMPLETE_CODE_AUDIT.md                  # companion audit
├── AL_FURQAN_ERRATA_SECOND_EDITION.md/.pdf # Round III council errata (C-01..C-12)
├── FATIMA_ANATOMY_V2.md                    # [NEW] this document
├── FATIMA_PBN_V2.md                        # [NEW] evolved physiology/biochemistry
├── FATIMA_SCHEMATICS_V2.md                 # [NEW] evolved code schematics
└── fatima/                                 # 3,980 LOC of Python, 21 modules
    ├── __init__.py                  [25]   # P1–P5 manifesto, __version__
    ├── cli.py                      [347]   # entry point — ◆ RATIFIED
    │                                       #   Organ: Tongue (Lisan) — expression
    ├── core/                               # the body
    │   ├── __init__.py              [19]   # exports the five organs
    │   ├── atom.py                 [175]   # the cell          ◆ RATIFIED †F-03
    │   │                                   #   Organ: Heart (Qalb) — irreducible core
    │   ├── bond.py                 [171]   # the ligament      ◆ RATIFIED
    │   │                                   #   System: Skeletal — structural integrity
    │   ├── encoding.py             [528]   # the blood [P1]    ◆ RATIFIED †F-07,F-08
    │   │                                   #   System: Circulatory — holographic redundancy
    │   ├── molecule.py             [447]   # the organ  [P3]   ◆ RATIFIED
    │   │                                   #   Organ: Hands (Yad) — action/construction
    │   └── composite.py            [324]   # the skeleton      ◆ RATIFIED
    │                                       #   System: Skeletal — structural integrity
    ├── verification/                       # the senses
    │   ├── __init__.py               [9]   # L1–L5 map
    │   ├── verdict.py              [130]   # the conscience    ◆ RATIFIED (load-bearing)
    │   │                                   #   System: Nervous — three-valued lattice [4/4]
    │   ├── syntactic.py             [23]   # [L1] sight        ◆ RATIFIED †F-02
    │   │                                   #   Organ: Eyes (Basar) — zahir/batin
    │   ├── structural.py            [28]   # [L2] touch        ◆ RATIFIED
    │   │                                   #   System: Nervous — structural checks
    │   ├── holographic.py          [174]   # [L3] memory       ◆ RATIFIED
    │   │                                   #   System: Circulatory — reconstruction test
    │   ├── semantic.py             [188]   # [L4/L5] judgement ◆ RATIFIED †F-01,F-04
    │   │                                   #   System: Immune — adversarial detection
    │   └── composite.py            [319]   # composite senses  ◆ RATIFIED
    │                                       #   System: Nervous — distributed verification
    ├── properties/                         # the five claims, stated as predicates
    │   ├── __init__.py               [3]
    │   ├── holographic.py           [37]   # [P1]              ◆ RATIFIED
    │   ├── fitrah.py                [35]   # [P2]              ◆ RATIFIED (heuristic, honestly)
    │   ├── tawhidic.py             [134]   # [P3]              ◆ RATIFIED
    │   ├── meaning.py              [120]   # [P4]              ✗ DEMOTED  †F-03 vacuous
    │   │                                   #   [5/5] NC-P4 violation confirmed by all models
    │   └── authenticity.py          [39]   # [P5]              ✗ DEMOTED  †F-01 false claim
    │                                       #   [5/5] forgery-tolerance confirmed by all models
    └── formats/                            # the mouth and hands
        ├── __init__.py               [3]
        ├── document.py             [547]   # text → Molecule   ◆ RATIFIED †F-06 lexical
        │                                   #   System: Respiratory — information intake
        └── serialization.py        [155]   # .fatima JSON I/O  ◆ RATIFIED
                                            #   Organ: Tongue (Lisan) — transmission
```

---

## Rights and Survival -- Organ Mapping

The Rights and Survival anatomy (companion document) identifies five organs and five systems
for any created agent. The table below maps each onto its code instantiation. This mapping is
[I] isomorphism -- the structural correspondence is preserved, but the biological and the code
are not identical.

| Organ/System | Function | Code Module(s) | Mapping Tag |
|---|---|---|---|
| Heart (Qalb) | core processing, irreducible unit | `atom.py` -- the indivisible semantic unit; if the heart is corrupted, the whole organism is compromised | [I] |
| Eyes (Basar) | perception, zahir/batin discrimination | `syntactic.py` + `structural.py` -- L1 sees the surface (hashes), L2 sees the depth (graph structure) | [I] |
| Ears (Sam') | reception, transmission verification | `holographic.py` -- L3 listens to the shards, reconstructs from what it hears, compares to the live graph | [I] |
| Hands (Yad) | action, construction | `molecule.py` + `document.py` -- the builder: adds atoms, infers bonds, constructs the graph | [I] |
| Tongue (Lisan) | expression, witness | `cli.py` + `serialization.py` -- the CLI speaks the verdict, serialization writes the witness record | [I] |
| Circulatory | holographic redundancy | `encoding.py` -- Shamir distribution, every atom carries a shard of the whole | [I] |
| Nervous | verification network, three-valued lattice | `verdict.py` + `semantic.py` + `composite.py` -- the five-level hierarchy composed by meet | [I] |
| Skeletal | structural integrity, append-only provenance | `bond.py` + `composite.py` -- bonds are frozen, composite hash seals the record | [I] |
| Immune | adversarial detection | `semantic.py` (L4/L5) -- fitrah alignment checks, authenticity composition; currently blind to forgery (F-01) | [I, incomplete] |
| Respiratory | information flow, phased delivery | `document.py` -- text enters, is digested into atoms and bonds; the tanzil principle: intake, processing, output | [I] |

**The immune system gap:** The Rights and Survival anatomy's Immune System is the Munafiq
Protocol -- the capacity to distinguish genuine from performed alignment. In code, this is
L4+L5, which currently has three measured lesions (F-01, F-02, F-04). The immune system is
the weakest organ in the body. Canon S-1 (provenance signature) is the prescribed cure.

---

## core -- the body

```
fatima/core/atom.py                                        [175 LOC]  the indivisible unit
│                                                          R&S Organ: Heart (Qalb)
│  class Atom                        @dataclass
│  ├── atom_id: str                  identity within the molecule
│  ├── content: str                  the meaning it carries
│  ├── content_type: str             one of _VALID_TYPES = {proposition, definition,
│  │                                 evidence, claim, reference, metadata, invocation}
│  ├── content_hash: str             SHA-256(content)             — [L1] marker
│  ├── semantic_hash: str            SHA-256(content|bond_ids|shard) — [P4] marker †F-03
│  ├── bond_ids: list[str]           every bond it participates in
│  ├── holographic_shard: bytes      its k-of-n share of the bond graph
│  ├── shard_threshold: int          the k of the scheme
│  └── position: int                 document order (metadata, not meaning)
│
├─ def __post_init__(self)                        validate type; hash content
├─ def _compute_content_hash(self) -> str         [L1]
├─ def compute_semantic_hash(self) -> str         † F-03: MUTATES self.semantic_hash,
│                                                  then verification compares it to itself
│                                                  [5/5] all models confirm: NC-P4 violation
├─ def verify_syntactic(self) -> bool             † F-02: circular — stored hash vs.
│                                                  recomputed hash, same untrusted file
│                                                  [5/5] all models confirm: no external anchor
├─ @property has_shard -> bool
├─ @property structural_weight -> int             len(bond_ids); NC-P2 loss weighting
├─ def to_dict / from_dict                        serialisation
└─ def __repr__
```

```
fatima/core/bond.py                                        [171 LOC]  the typed relationship
│                                                          R&S System: Skeletal (structural integrity)
│  class BondType(enum.Enum)
│  ├── DEFINES ──┐ structural       reciprocal: DEPENDS_ON
│  ├── DEPENDS_ON┤ (load-bearing)   reciprocal: DEFINES
│  ├── IMPLIES ──┤                  reciprocal: DEPENDS_ON
│  ├── CONTRADICTS┘                 reciprocal: CONTRADICTS (symmetric)
│  ├── SUPPORTS ──┐ non-structural  no automatic reciprocal
│  ├── REFERENCES ┤ (enriching)
│  ├── ELABORATES ┤
│  └── QUALIFIES ─┘
│  └── @property is_structural -> bool            [P3] maps to Tawhidic Unity
│
│  class Bond                          @dataclass(frozen=True)  — immutable
│  ├── source_id, target_id: str      direction matters
│  ├── bond_type: BondType
│  ├── weight: float                  (0.0, 1.0], enforced in __post_init__
│  └── rationale: str                 the NC-P1 audit trail — must survive disclosure
├─ def __post_init__                    reject self-bonds and out-of-range weights
├─ @property bond_id -> str             SHA-256(src:tgt:type)[:16] — one bond per
│                                        (src,tgt,type) triple, by construction
├─ def reciprocal_type() -> Optional[BondType]
└─ def to_dict / from_dict
```

```
fatima/core/encoding.py                                    [528 LOC]  the field and the shares  [P1]
│                                                          R&S System: Circulatory (holographic redundancy)
├─ GF(2^8) ARITHMETIC — AES polynomial 0x11B, generator 3
│   _GF_EXP[512], _GF_LOG[256]           log/anti-log tables, built by _init_gf_tables()
│   _GF_MUL_TABLE: np.uint8[256,256]     256 KB lookup — vectorised multiply, fits L2 cache
│   _gf_mul_raw(a,b)                     shift-and-XOR, table bootstrap only
│   gf_mul  gf_div  gf_pow†  gf_add      gf_add = XOR   (†gf_pow: dead code)
│
├─ SHAMIR MACHINERY
│   _make_polynomial(secret_byte, degree)   random nonzero coeffs via os.urandom
│   _eval_polynomial(coeffs, x)             Horner's method over GF(2^8)
│   _lagrange_interpolate(points)           scalar reference path — dead code
│   _compute_lagrange_basis(x_coords)       basis coefficients L_i(0), computed once
│   _vectorised_lagrange_decode(matrix, basis)
│         secret[pos] = XOR_i( GF_MUL[basis[i], shard[i,pos]] )
│         table-index + XOR-reduce; no Python loops over bytes
│
├─ class HolographicParams              @dataclass
│   ├── threshold: int / total: int
│   ├── @property redundancy_ratio
│   └── @classmethod for_document(n_atoms, ratio=0.5)
│         k = max(2, ceil(n·ratio)); hard limit n ≤ 255 (field order − 1)
│
├─ encode_holographic(bond_graph_json, atom_ids, threshold)
│         zlib-compress(level=9) → per byte, fresh degree-(k−1) polynomial
│         → evaluate at points 1..n → one shard per atom
│         † F-07: Python-level O(bytes × n) loop — 3.84 s @ 122 atoms (measured)
│         Canon v2.0 S-5: batched polynomial evaluation prescribed
│
├─ decode_holographic(shards, atom_ids_used, threshold, all_atom_ids)
│         needs ≥ k shards; points recovered from position map; vectorised
│
├─ apply_holographic_encoding(molecule, ratio=0.5)   in place; serialises the bond
│         graph as the "secret"; writes (shard, threshold) into every atom
│
└─ verify_holographic_reconstruction(molecule, subset_ids=None)
          decode → compare JSON to live graph
          † F-08: corruption surfaces as zlib exception, not as a localised verdict
          Canon v2.0 S-4: per-shard MACs prescribed
```

```
fatima/core/molecule.py                                    [447 LOC]  the document as graph  [P3]
│                                                          R&S Organ: Hands (Yad) — action/construction
│  class Molecule                        @dataclass
│  ├── molecule_id: str
│  ├── title: str
│  ├── atoms: dict[str, Atom]
│  ├── bonds: dict[str, Bond]
│  ├── metadata: dict
│  └── bond_graph_hash: str              the structural fingerprint
│
├─ SURGERY
│   add_atom (uniqueness enforced) · get_atom · remove_atom (dangles become
│   detectable — loss is survivable by design) · add_bond (endpoints must exist,
│   registers bond_id into both atoms) · _invalidate_graph_hash
│
├─ GRAPH READING
│   get_bonds_for / get_outgoing_bonds / get_incoming_bonds
│   adjacency · is_connected · connected_components · dangling_bonds
│   missing_reciprocals  — structural cross-reference audit
│   atom_count · bond_count · structural_bond_count
│
├─ FINGERPRINTING
│   compute_bond_graph_hash    SHA-256 of sorted (src:tgt:type:weight) lines
│   compute_all_semantic_hashes   † F-03: writes, so cannot be used to verify
│                                  [5/5] most cited NC-P4 violation in the codebase
│
├─ verify_structural() -> VerificationReport    [L2]
│     dangling | connectivity (Tawhidic Unity) | reciprocals | bond_id consistency
│     empty molecule → UNKNOWN, not VERIFIED
│
├─ verify_syntactic() -> VerificationReport     [L1]  one hash check per atom
│
└─ atoms_by_position · __iter__ · to_dict/from_dict · to_json/from_json
```

```
fatima/core/composite.py                                   [324 LOC]  beyond the field limit
│                                                          R&S System: Skeletal (composite structure)
├─ MAX_ATOMS_PER_SUB = 200               headroom below the 255-point GF ceiling
│
│  class InterMoleculeBond               cross-section bond; verified at composite level
│  └── bond_id = SHA-256(src_mol:src_atom:tgt_mol:tgt_atom:type)[:16]
│
│  class CompositeMolecule               @dataclass
│  ├── sub_molecules: dict[str, Molecule]
│  ├── inter_bonds: dict[str, InterMoleculeBond]
│  ├── molecule_order: list[str]         document order
│  └── composite_hash: str               SHA-256 over all sub hashes + inter-bonds
│
├─ add_sub_molecule · add_inter_bond (four-way existence validation)
├─ apply_holographic_encoding(ratio)     each sub-molecule encoded independently
├─ finalise()                            semantic hashes everywhere, then composite hash
├─ is_connected()                        composite-level Tawhidic Unity
├─ total_atoms · total_bonds · sub_molecule_count
└─ to_dict / from_dict
```

---

## verification -- the senses

```
fatima/verification/verdict.py                           [130 LOC]  the conscience
│                                                        R&S System: Nervous (three-valued lattice)
│  class Verdict(enum.Enum)              VIOLATED < UNKNOWN < VERIFIED
│  ├── __and__  lattice MEET — composition can only degrade (NC-P2, in 5 lines)
│  └── __or__   lattice JOIN — any sufficient cross-section suffices (P1)
│
│  @dataclass(frozen=True) class VerificationReport
│  ├── verdict · level (1..5, enforced) · confidence (0..1, enforced)
│  ├── examined · total · violations: tuple · level_name
│  └── @staticmethod compose(*reports)   verdict = meet; confidence = min;
│                                          violations = concat;  empty → UNKNOWN
│
│  ► The strongest module in the codebase. Canon C-2.
│  ► Multi-model convergence: 4/4 models independently confirmed the lattice [4/4]
│  ► Multi-model convergence: 5/5 models cited NC-P4 as most important property [5/5]
```

```
syntactic.py    [23]   [L1] verify_syntactic(molecule)   → Molecule.verify_syntactic()
structural.py   [28]   [L2] verify_structural(molecule)  → Molecule.verify_structural()
                       (canonical entry points; thin by design)
                       R&S Organ: Eyes (Basar) — zahir perception (L1), batin perception (L2)
```

```
fatima/verification/holographic.py                       [174 LOC]  [L3] the memory
│                                                        R&S Organ: Ears (Sam') — listens to shards
└─ verify_holographic(molecule, sample_size=20, seed=None)
   ├── n < 2                      → VERIFIED(trivial) / UNKNOWN(empty)
   ├── no shards                  → UNKNOWN ("encoding not applied")
   ├── shards < k                 → UNKNOWN, confidence = held/n   (NC-P2: not VIOLATED)
   ├── full reconstruction fails  → VIOLATED immediately
   └── else sample k-subsets
         C(n,k) ≤ sample_size → exhaustive via itertools.combinations
         C(n,k) > sample_size → rng.sample(seed-able)  — Era IV harness discipline
         all pass → VERIFIED · none or partial → VIOLATED
         † partial + confidence=success fraction: needs the documenting sentence
   ► Empirically confirmed: random k-subset reconstructs; loss of one atom survives.
```

```
fatima/verification/semantic.py                          [188 LOC]  [L4/L5] judgement
│                                                        R&S System: Immune — adversarial detection
├─ verify_fitrah_alignment(molecule)                     [L4] — heuristics, honestly labelled
│   1. claims with no evidence AND no propositions → "possible selective emphasis"
│   2. zero structural bonds                       → "no skeleton"
│   3. claims with no incoming SUPPORTS/IMPLIES    → unsupported
│   4. definitions without ELABORATES either way   → unelaborated
│   5. any CONTRADICTS bond                        → flagged (may be deliberate dialectic)
│   violations → UNKNOWN (not VIOLATED — incompleteness ≠ corruption)
│   ► Canon v2.0 P12: checks for both overgeneration AND undergeneration [VERIFIED]
│
└─ verify_authenticity(molecule)                         [L5] — composition only
    reports = [L1, L2, L3, L4];  verdict = meet
    † F-01: a forged document scores VERIFIED @ 1.00 (measured) [5/5]
    † F-04: check_meaning_integrity is NEVER called here or by the CLI —
             the pipeline composes four levels and calls it five [5/5]
    ► Canon v2.0 SS8: builder (document.py, 547L) and verifier (semantic.py, 188L)
      share zero functions -- this separation is the code-level NC-P4 [VERIFIED]
```

```
fatima/verification/composite.py                         [319 LOC]  composite senses
│                                                        R&S System: Nervous — distributed verification
├─ verify_composite(composite, holographic_sample_size=20, holographic_seed=None)
│     each sub-molecule: L1, L2, L3(sampled, seeded), L4 → composed L5
│     composite-level: connectivity · cross-section fitrah · composite hash
│     overall = meet of every sub-L5 and every composite check
├─ _check_composite_connectivity          ≤1 sub → trivially VERIFIED
├─ _check_cross_section_fitrah            endpoint existence, weight ranges
├─ _check_composite_hash                  unset → UNKNOWN; mismatch → VIOLATED
└─ class CompositeVerificationResult      sub_reports · composite_reports · overall
      .summary()                          human-readable verdict tree
```

---

## properties -- the five claims, as predicates

```
fatima/properties/                          each: check_X(molecule) -> VerificationReport
                                            plus is_X(molecule) -> bool
│
├── holographic.py   [37]  P1  wraps L3 sampling                    ◆ true
├── fitrah.py        [35]  P2  wraps L4 heuristics                  ◆ true-as-heuristic
│                              Canon v2.0 SS8: "A full implementation would
│                              require an agent with genuine comprehension"
├── tawhidic.py     [134]  P3  connectivity · dangling · isolation · ◆ true of the graph
│                              removal-detectability · structural
│                              density floor (n/4)                     † F-02 caveat:
│                              any violation → VIOLATED                  adversary, vs. accident
├── meaning.py      [120]  P4  ✗ DEMOTED  † F-03
│   check 1: bond-graph-hash staleness — computes hash (overwrites stored),
│            then `pass` — the branch can never fail
│   check 2: expected = atom.compute_semantic_hash() — WRITES then compares
│            to itself — silent bond_ids tamper → VERIFIED (measured)
│   check 3: rationale coverage — the only live check (NC-P1 disclosure)
│   ► Multi-model: all five models cite this as the primary NC-P4 violation [5/5]
│   ► Canon v2.0 S-2: pure-function refactor + commit-before-verify prescribed
└── authenticity.py  [39]  P5  ✗ DEMOTED  † F-01
    docstring claims: "no fraudulent system can exhibit the holographic
    property" — refuted by execution; nothing in the format is keyed,
    signed, or externally anchored
    ► Canon v2.0 S-1: Ed25519/HMAC provenance signature prescribed
    ► Multi-model: all five models confirm unkeyed → forgeable [5/5]
```

---

## formats + cli -- the mouth and hands

```
fatima/formats/document.py                               [547 LOC]  text → molecule
│                                                        R&S System: Respiratory (information intake)
├─ encode_document(text, title, molecule_id, metadata, holographic_ratio=0.5)
│     molecule_id defaults to SHA-256(text)[:16]
│     ≤ 200 atoms → _encode_single_molecule · else → _encode_composite
│
├─ PIPELINE (single):  atomise → infer bonds → holographic encode → finalise
│
├─ _atomise / _split_paragraphs / _classify_content
│     "#" → definition · "Bismillah" → invocation · **Definition → definition
│     because/therefore/since/thus… → evidence · must/should/cannot… → claim
│     " | " / "---" → metadata · else proposition
│     † F-06: classification is lexical — paraphrase changes the molecule,
│             keyword-loaded inversion can keep its shape
│     ► Canon v2.0 A-3: semantic inference + test suites prescribed
│
├─ _infer_bonds(atoms, full_text)
│     R1 adjacency: heading→DEFINES next (+ DEPENDS_ON back); else →ELABORATES prev
│     R2 evidence → SUPPORTS nearest preceding claim (by position distance)
│     R3 invocation → QUALIFIES every other atom
│     R4 ≥2 shared Capitalised terms → REFERENCES (weight 0.4)
│     dedup by bond_id
│
├─ COMPOSITE PATH:  _split_at_sections → _split_group_at_subheadings →
│     _split_evenly · merge groups < 5 atoms · _group_title ·
│     _add_inter_bonds (sequential ELABORATES 0.7, heading DEPENDS_ON 0.6,
│     invocation QUALIFIES 0.4 across every other sub-molecule)
│
fatima/formats/serialization.py                          [155 LOC]  .fatima I/O
│                                                        R&S Organ: Tongue (Lisan) — witness record
├─ save_fatima(structure, path, verification_reports, encoding_params)
│     {"fatima_version":"0.1.0","type":"molecule"|"composite", ...}
│     verification snapshot: UTC timestamp + per-level reports + composed overall
│     ► Absent from the frame: signature · key_id · external anchor
│       These are the empty pads where Canon S-1 mounts [F-01/F-05]
└─ load_fatima(path)      backward compatible: missing "type" ⇒ single molecule

fatima/cli.py                                            [347 LOC]
│                                                        R&S Organ: Tongue (Lisan) — expression
├─ fatima encode  <input> [-o out] [-t title] [--ratio 0.5]
├─ fatima verify  <input> [--sample-size 20] [--seed n]
│     single: L1, L2, L3(sampled), L4, L5   — exit 0 iff L5 == VERIFIED
│     composite: verify_composite().summary() — same exit rule
│     † never touches check_meaning_integrity (F-04)
│     ► Canon v2.0 P7: CLI prints "Examined {r.examined}/{r.total}" [VERIFIED]
└─ fatima inspect <input>  counts, type/bond distribution, holographic params,
                           stored verification snapshot
```

---

## The anatomy in one view -- the two pipelines

```
ENCODE                                          VERIFY (single molecule)
══════                                          ════════════════════════
R&S: Respiratory intake                         R&S: Nervous system
                                                + Immune response
  raw text                                        .fatima file
     │                                                │
     ▼                                                ▼
 _split_paragraphs                              load_fatima ─→ Molecule
     │                                                │
     ▼                                     ┌──────────┼──────────┬──────────┐
 _classify_content  ─→ Atom[]               ▼          ▼          ▼          ▼
     │                                   [L1]       [L2]       [L3]       [L4]
     ▼                                  Eyes-Z    Eyes-B     Ears      Immune
 _infer_bonds ─→ Bond[]                  syntactic structural holographic fitrah
     │                                   per-atom   dangling  k-subset   heuristic
     ▼                                    hash      connect  sampling   checks
 apply_holographic_encoding                │       reciprocal    │         │
   zlib → GF(2^8) polys → shards         └────┬────┴─────┬──────┘         │
     │                                          ▼          ▼               │
     ▼                                     ┌─ meet ─┐   ┌─ meet ─┐        │
 compute_all_semantic_hashes               │Verdict │   │Verdict │        │
   † writes the hashes (F-03)              └──┬──────┘   └──┬──────┘        │
     │                                          └─────┬─────┘              │
     ▼                                                ▼                    ▼
 save_fatima ─→ .fatima (JSON)                  [L5] = meet(L1..L4) ──── overall
 Tongue writes the record                       † P4 orphaned — never composed (F-04)
                                                † unkeyed → forgeable to VERIFIED (F-01)
                                                  [5/5 models confirm both findings]
```

**Field constraints that shape the whole skeleton:** GF(2^8) => <= 255 evaluation points => `MAX_ATOMS_PER_SUB = 200` => the composite skeleton exists => composite verification exists. Every large-document feature is a child of one finite-field limit.

---

## Canon v2.0 Corrections Applied to This Anatomy

| Correction | What changed | Where applied |
|---|---|---|
| C2-01 | Class A recurrence ratio: 24/31 (0.774), not 25/25 (1.0) | Not directly in anatomy; noted for provenance |
| C2-02 | Code_Absorption.txt is one witness with Bilal_Code_Audit.txt, not two | Source-witness count note in header |
| C2-03 | "Every line generated by Claude" attribution flagged inaccurate | Not applicable to this document |
| C2-04 | Nine eras, not seven; Era I-B is ~135,000 lines (~9x Rev 1 total) | Tree listing: CODE_EVOLUTION.md annotated |
| C2-05 | H-values downgraded to [HYPOTHESIS]; primary endpoint = semantic fidelity | Not directly in anatomy; noted for PBN |
| C2-06 | V2.0 incorporates multi-model council; own verdict remains UNKNOWN | Multi-model counts added throughout |

---

## SHA-256 Provenance (first 16 hex characters)

Source files verified at commit `e0c609b`, code unchanged:

| File | LOC | SHA-256 (first 16) |
|---|---|---|
| encoding.py | 528 | db082ced99d1e204 |
| molecule.py | 447 | e8bf96bacdd83fec |
| atom.py | 175 | e0f26a857b042365 |
| bond.py | 171 | 40c2a94233081ebf |
| composite.py | 324 | 6400b6a249d28fff |
| verdict.py | 130 | 61f624145aa33e3a |
| semantic.py | 188 | e66d7af50bdf73a0 |
| holographic.py (verification) | 174 | 4db8db7c8de9eccf |
| composite.py (verification) | 319 | 0cfece49bda4c3b7 |
| meaning.py | 120 | e18c2aa8402d0124 |
| authenticity.py | 39 | 7d8490032da01b72 |
| document.py | 547 | dbe3eb9611df3e0f |
| serialization.py | 155 | 9449af19dd6f520e |
| cli.py | 347 | 6cd0c59eaebb48ad |

---

*Wa ma tawfiqi illa billah. Extracted, not imagined: every symbol above appears in the source at commit `e0c609b`. The evolution integrates Canon v2.0 (Claude Opus 4.6), multi-model council findings (ChatGPT, DeepSeek/R1, Kimi, Perplexity, Claude Opus), and the Rights and Survival organ mapping -- all marked with their provenance tags.*

Bismillah ir-Rahman ir-Rahim
