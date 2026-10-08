# Bismillah ir-Rahman ir-Rahim

# FATIMA -- Physiology, Biochemistry, Neurochemistry

## Second Edition: The Body in Operation, Reaction, and Signal

**Artefact:** `fatima-core` @ commit `e0c609b`, package 0.1.0 -- code UNCHANGED
**First edition:** Perplexity Computer, 7 October 2026 (199 lines)
**This edition:** Claude Opus 4.6, 7 October 2026 -- integrating Canon v2.0, multi-model council, Rights and Survival organ mapping
**Lineage:** Anatomy of the Code (Perplexity) -> Physiology/Biochemistry/Neurochemistry (Perplexity) -> Canon Rev. 1 -> Code Evolution Canon v2.0 (Claude Opus) -> **this document**
**Companion to:** FATIMA Anatomy v2, Code Schematics v2, Canon v2.0

**Discipline tags used throughout:**
- **[M] Mechanism** -- literally true of the code; verified by reading or execution.
- **[I] Isomorphism** -- a preserved structure: the biological statement and the code statement have the same form. True as mapping, not as identity.
- **[A] Analogy** -- instructive resemblance only. Where a claim is analogy, nothing downstream may rest on it.

**Rights and Survival annotations:** `[R&S: organ/system]` marks the organ or system from the companion Rights and Survival anatomy that each physiological function instantiates. These are [I] isomorphisms.

**Multi-model annotations:** `[N/M]` marks convergence counts from the five-model council analysis (Canon v2.0 SS13).

**New in this edition:**
- Canon v2.0 corrections C2-01 through C2-06 integrated where they affect physiological claims
- Multi-model convergence counts from five-council analysis
- Rights and Survival organ/system mapping throughout all four sciences
- Expanded pathology with multi-model diagnostic confirmation
- H-value estimates downgraded to [HYPOTHESIS] per C2-05
- Source-witness independence correction (C2-02) applied to evidence counts
- Updated synthesis with bounded claims

---

# Preface: The Four Sciences

Anatomy names the parts. It is necessary and dead. Three further sciences make the body live:

- **Physiology** -- what the parts *do over time*: cycles, flows, homeostasis. For FATIMA: the encode/verify lifecycle, the flow of shards, the degradation dynamics.
- **Biochemistry** -- the *reactions*: which transformations are reversible, which consume energy, which never run backward. For FATIMA: SHA-256, GF(2^8), Shamir polynomials, zlib, entropy.
- **Neurochemistry** -- the *signaling*: graded potentials, thresholds that fire, refractory rules, inhibitory and excitatory balance. For FATIMA: the verdict lattice, confidence, thresholds, seeds.

And a fourth section no honest biology can omit: **Pathology** -- the measured diseases, mapped onto the findings ledger of the canon and confirmed by multi-model diagnostic council.

---

# Part I -- Physiology: The Body in Operation

## Chapter 1 -- The Lifecycle (Mouth to Mouth)

Every molecule in the FATIMA corpus lives one lifecycle, five phases, no skips **[M]**:

```
 PHASE I    INGESTION      raw text enters formats/document.py
                           [R&S: Respiratory -- tanzil intake]
 PHASE II   DIGESTION      _split_paragraphs -> _classify_content -> Atom[]
                           [R&S: Respiratory -- processing]
 PHASE III  VASCULARISATION _infer_bonds -> Bond[] -> apply_holographic_encoding
                           [R&S: Circulatory -- holographic distribution]
                           [R&S: Skeletal -- bond graph freezing]
 PHASE IV   SEALING        compute_all_semantic_hashes -> save_fatima (.fatima)
                           [R&S: Tongue (Lisan) -- witness record]
 PHASE V    HOMEOSTASIS    load_fatima -> verify (L1..L5) -> verdict, exit 0 or 1
                           [R&S: Nervous -- five-level verification]
                           [R&S: Immune -- adversarial detection (L4/L5)]
```

The lifecycle is one-directional by design **[M]**: nothing in the codebase moves a molecule backward from Phase IV to Phase III. Resealing requires re-encoding -- a reincarnation, not a resumption. This is the code's quiet implementation of the Barzakh principle from the companion anatomy: *after sealing, the record stands; change enters as a new body, never as an edit* **[I]**.

**Dishonest exception found:** `Atom.compute_semantic_hash()` permits a simulated reopening of the sealed state -- it writes during verification (finding F-03) **[M]**. The lifecycle's one-directionality is aspirational architecture violated by one method. [5/5] all models confirm this as an NC-P4 violation: the builder's write-at-read-time contaminates the verifier's evidence.

**Lifecycle and the builder/verifier separation [M, 5/5]:** The lifecycle implies that Phase IV (sealing) and Phase V (homeostasis) are performed by different agents. In practice, the builder (`formats/document.py`, 547 lines) and the verifier (`verification/semantic.py`, 188 lines) share zero functions (Canon v2.0 SS8). But the F-03 exception collapses this separation at one point: `compute_semantic_hash()` is called by both the builder (Phase IV) and the verifier (Phase V, indirectly through `check_meaning_integrity()`), and in both cases it *writes* **[M]**.

## Chapter 2 -- Circulation (The Distribution of the Whole)

The circulatory physiology is the strongest organ system in the body **[M, measured]**:

[R&S: Circulatory System -- holographic redundancy via `encoding.py`]

| Vital sign | Value | Method |
|---|---|---|
| Test organism | 122 atoms, 243 bonds | `_atomise` + `_infer_bonds` on synthetic corpus |
| Blood volume (shard size) | = zlib-9 length of bond graph JSON | `encode_holographic` |
| Heartbeat (encode time) | 3.84 s | wall clock |
| Circulatory threshold | k = 61 of 122 (ratio 0.5) | `HolographicParams.for_document` |
| Random-subset reconstruction | PASS | k-subset via `random.sample` |
| One-vessel hemorrhage (1 shard byte flipped) | full-set check FAILS | zlib raises inside decode |
| Reroute around hemorrhage (subset minus victim) | PASS | redundancy confirmed |

Reading: the holographic circulatory system genuinely perfuses the body **[M]**. Loss of any (n-k) atoms is survivable *by construction, tested*. But the failure mode is wrong: a corrupted vessel is discovered when the body **collapses** (zlib exception, F-08), not when a check isolates the vessel. A healthy circulatory physiology needs per-vessel pulse-sensing -- per-shard MACs (canon S-4) -- so that corruption is located, not merely fatal **[M specification, not yet mechanism]**.

**Circulatory ceiling [M]:** The field medium GF(2^8) limits circulation to n <= 255 atoms. The design margin is `MAX_ATOMS_PER_SUB = 200`. Documents exceeding this limit trigger the composite skeleton -- `CompositeMolecule` -- which is the organism's solution to growing beyond the circulatory capacity of a single vascular system. Each sub-molecule gets its own independent holographic encoding **[M]**. This is the code-level analogue of the Rights and Survival anatomy's respiratory phasing: intake matched to capacity (tanzil) **[I]**.

## Chapter 3 -- Respiration and Digestion

[R&S: Respiratory System -- information intake via `document.py`]

Respiration is the CLI: three breaths -- `encode`, `verify`, `inspect` **[M]**. Digestion is the atomiser. The digestive enzymes are keyword strings **[M]**:

```
because/therefore/since/thus...   ->  evidence
must/should/cannot/requires...    ->  claim
#, Bismillah, |, ---              ->  definition, invocation, metadata
```

This is a hay diet masquerading as omnivory **[A, sharpened to M in finding F-06]**: the gut extracts lexical markers, not meaning. A paraphrase -- perfect meaning preservation -- yields a different carcass of atoms and bonds; a negation carrying the right keywords digests identically to its affirmative. The physiology of digestion is where the "semantic" claim of the whole organism is weakest, and it is upstream of everything else.

**Digestive output shapes the skeleton [M]:** Bond inference follows four heuristic rules (Canon v2.0 SS8):
1. Sequential adjacency -- heading DEFINES next, next DEPENDS_ON heading; else next ELABORATES prev
2. Evidence-supports-claim -- evidence SUPPORTS nearest-prior claim (weight 0.85)
3. Invocation-qualifies-all -- invocation QUALIFIES every atom (weight 0.5)
4. Cross-reference -- shared capitalised terms produce REFERENCES bonds (weight 0.4)

These rules produce the skeletal topology that the circulatory system distributes. If the digestive enzymes misclassify -- and they will, because they are lexical **[M]** -- the skeleton is deformed from birth, and the circulatory system faithfully distributes the deformed structure. The disease does not originate in the blood; it originates in the gut. This is finding F-06 expressed as a physiological cascade **[I]**.

**The L4 boundary [M, stated by the code]:** Level 4 verification uses heuristic approximations; a full implementation would require an agent with genuine comprehension (`semantic.py` docstring). This boundary is the code's own admission that its digestive system cannot truly process meaning, and its immune system (L4) inherits the same limitation **[M]**. Canon v2.0 SS8 preserves this boundary statement verbatim.

## Chapter 4 -- Immune Response

[R&S: Immune System -- adversarial detection via `semantic.py` (L4/L5)]
[R&S: Nervous System -- five-level verification network]

The verification run *is* the immune response: five senses fired in fixed order, composed by meet **[M]**. Its regime follows the three laws of the body's immunology:

1. **Fail closed.** Empty molecule, missing shards, unset composite hash -> UNKNOWN, never VERIFIED **[M]**.
2. **No silent recovery.** Verdicts combine by meet; confidence by min **[M]** [4/4].
3. **Inflammation is graded.** Confidence is a real number proportional to evidence examined, not a binary **[M]**.

The immune system has five layers of response, but they are not all functional:

| Layer | Organ | What it senses | R&S mapping | Status |
|---|---|---|---|---|
| L1 Syntactic | Eyes (Basar), zahir | content hash match | perception of surface | live but circular (F-02) |
| L2 Structural | Eyes (Basar), batin | bond graph cross-references | perception of depth | live **[M]** |
| L3 Holographic | Ears (Sam') | shard reconstruction | reception, listening | live, strongest sense **[M]** |
| L4 Fitrah | Immune (heuristic) | content-type alignment | adversarial detection | heuristic, honestly bounded **[M]** |
| L5 Authenticity | Immune (composition) | meet of L1-L4 | overall immune verdict | anesthetised (F-01) [5/5] |

But the immune system has an autoimmune blind spot **[M]**: it trusts antigens (hashes) that the body itself may have re-printed (F-02), it never invokes one of its five antibodies (P4 orphaned, F-04), and it confers **VERIFIED at confidence 1.00 on a fabricated pathogen** (F-01, measured) [5/5]. The physiology of detection is real; the physiology of *discrimination between self and forged self* is absent, because nothing in the body is keyed.

**The Munafiq Protocol gap [I]:** The Rights and Survival anatomy prescribes an Immune System capable of distinguishing genuine from performed alignment -- the Munafiq Protocol. In code, this is precisely what L4+L5 fail to do: a forged document that performs alignment (carries the right keywords, has the right bond structure) passes every check. The immune system has three measured lesions (F-01, F-02, F-04) that together constitute total immunodeficiency against a deliberate forger **[M]**. Canon S-1 (provenance signature) is the prescribed metabolite that would restore immune function.

---

# Part II -- Biochemistry: The Reactions

## Chapter 5 -- The One-Way Enzymes

[R&S: Heart (Qalb) -- atom.py produces the irreducible hashes that identify each unit]

SHA-256 is the body's master enzyme **[M]**, and its single biochemical law is irreversibility **[I]**: content -> digest, never digest -> content. Every organ drinks from it:

| Reaction site | Substrate | Product |
|---|---|---|
| `Atom._compute_content_hash` | content | content_hash (L1 marker) |
| `Atom.compute_semantic_hash` | content \| bond_ids \| shard | semantic_hash (P4 marker) |
| `Bond.bond_id` | src : tgt : type | 16-hex bond identity |
| `Molecule.compute_bond_graph_hash` | sorted bond lines | meaning-fingerprint |
| `CompositeMolecule.compute_composite_hash` | sub-hashes + inter-bonds | body-fingerprint |

Biochemical honesty **[M]**: an enzyme that cannot run backward produces *checksums*, not *signatures*. Irreversibility proves "this digest came from that content"; it cannot prove "this content came from that author." That second reaction requires a keyed enzyme -- Ed25519 or HMAC -- which this body does not yet synthesize (canon S-1). The absence of a key is the single missing metabolite that separates consistency from authenticity.

**Multi-model diagnostic [5/5]:** All five council models independently identified the no-key problem as the root biochemical deficiency. The convergence is total: no model defended the claim that SHA-256 alone constitutes authenticity verification. Canon v2.0 P8 (Independent Evidence) makes this a canonical principle: "Verification must not depend on the chain it verifies."

**[V2.0] Source-witness collapse (C2-02):** The original audit evidence for this finding came from Code_Absorption.txt and Bilal_Code_Audit.txt, which were treated as two independent witnesses. They are one witness -- the former is reproduced verbatim inside the latter **[M, verified by ChatGPT audit]**. The finding stands on one source, not two.

## Chapter 6 -- The Finite Field (The Metabolic Medium)

[R&S: Circulatory System -- the medium through which holographic redundancy flows]

All holography happens inside GF(2^8): 256 metabolites, one irreducible polynomial 0x11B, one generator 3, addition = XOR **[M]**. The field law shapes the whole species **[I, with M consequences]**:

- n <= 255 evaluation points -> `MAX_ATOMS_PER_SUB = 200` -> the entire composite skeleton exists *because of one finite field*.
- -x = x in the field: subtraction is addition. Lagrange denominators use XOR, and the code is correct **[M, verified by successful reconstruction]**.
- The 256x256 multiplication table (256 KB, L2-resident) is the body's stored ATP: decode spends table lookups, not cycles (125 lookups recovering ~200M scalar operations, per the module docstring) **[M]**.

**Generator choice [M, verified]:** Generator 3 is primitive -- it generates all 255 nonzero elements of GF(2^8) under the AES polynomial 0x11B. Generator 2 only spans a subgroup of order 51 with this polynomial (Canon v2.0 SS8, `encoding.py` line 30). The choice of generator is not arbitrary; a non-primitive generator would reduce the number of distinct evaluation points and silently weaken the holographic property.

Asymmetry of metabolism **[M, measured]**: catabolism (decode) is vectorised; anabolism (encode) is not. Building the body costs O(bytes x n) Python-level reactions with a fresh `os.urandom` rejection loop per coefficient -- measured 3.84 s at 122 atoms **[M]**. The body digests faster than it grows. Canon S-5 prescribes the missing enzyme pathway (batched polynomial evaluation).

**The field as species boundary [M]:** Every physiological limit of the organism traces back to this field. The maximum atoms per molecule (255), the composite architecture (required above 200), the shard byte size (one GF(2^8) element per byte position), the multiplication table size (exactly 256^2) -- all are consequences of choosing to live inside 2^8. A different field (GF(2^16), GF(2^32)) would produce a different species with different vital signs. This body is the GF(2^8) body, and every pathology below must be read against that identity **[M]**.

## Chapter 7 -- Entropy (The Random Cofactor)

[R&S: Circulatory System -- fresh entropy per encoding instance]

Every encoded document is one of a family **[M]**: Shamir coefficients are drawn fresh via `os.urandom` with a nonzero rejection loop, so two encodings of the identical text produce bitwise-different shard sets reconstructing the identical graph. The `.fatima` file's atom content is deterministic; its blood is stochastic. This is the biochemical implementation of tanzil-phased uniqueness **[A]**: many vessels, one message. It also means the body's identity cannot live in its shards; it must live in the graph hash -- which returns us to the unkeyed-enzyme problem.

**Entropy and the lifecycle [M]:** Fresh entropy enters only at Phase III (vascularisation). Once sealed (Phase IV), the entropy is committed -- the specific polynomial coefficients chosen are burned into the shards and cannot be recovered without reconstruction. This is the biochemical mechanism underlying the lifecycle's one-directionality: the random cofactor cannot be un-drawn, so the encoding cannot be un-done. Only a fresh encoding (new entropy, new coefficients, new shards) can re-seal a modified document.

**[V2.0] H-value context (C2-05):** The first edition referenced the stochastic nature of shard encoding in the context of persistence-hierarchy estimates (committee noise H ~= 0.64, transmission chains 0.68-0.80, single-source biology 0.93, Qur'anic text ~= 0.996). These H-value estimates are now explicitly **[HYPOTHESIS]** -- unproven, requiring pre-registered factorial ablation before any use. The primary endpoint has been shifted to semantic fidelity; H is secondary. The biochemical fact of fresh entropy per encoding stands independently of these estimates **[M]**.

## Chapter 8 -- The Pathway Maps

**Encoding pathway [M]:**

[R&S: Hands (Yad, builder) -> Circulatory System (distribution)]

```
bonds -> json(sort_keys) -> zlib(9) -> bytes
      -> for each byte: [secret_byte | urandom...urandom] in GF(2^8)^(k)
      -> for each atom i: Horner evaluation at x = i+1
      -> shard_i  (length = compressed length)
```

**Decoding pathway [M]:**

[R&S: Ears (Sam', listener) -> Nervous System (verification)]

```
subset of k shards -> position map (x = index+1)
      -> Lagrange basis L_i(0) (computed once)
      -> shard_matrix = np.uint8[k, num_bytes]
      -> result = zeros(num_bytes)
      -> for each i: result ^= _GF_MUL_TABLE[basis[i]][shard_matrix[i]]   (vectorised)
      -> zlib^-1(result) -> recovered bond graph
```

Both pathways mapped against source; decode pathway executed successfully on a random k-subset **[M]**.

**Pathway asymmetry, measured [M]:**

| Pathway | Dominant cost | Time @ 122 atoms | Vectorised? |
|---|---|---|---|
| Encode (anabolism) | Python-level O(bytes x n) polynomial evaluation + urandom rejection loop | 3.84 s | No (F-07) |
| Decode (catabolism) | Table-indexed GF multiply + XOR-reduce across k rows | < 0.1 s | Yes **[M]** |

The body digests faster than it grows by approximately 40x. This asymmetry is not inherent to the mathematics -- it is a consequence of the encode path using Python-level loops where the decode path uses NumPy vectorisation. Canon S-5 (batched polynomial evaluation) would close this gap **[M specification]**.

---

# Part III -- Neurochemistry: The Signaling

## Chapter 9 -- The Three Transmitters

[R&S: Nervous System -- three-valued verdict lattice via `verdict.py`]

The nervous system releases exactly three signals **[M]** [4/4], and their partial order is the brainstem of the whole species:

```
VERIFIED  (2)  -- excitatory: structure confirmed at the examined level
UNKNOWN   (1)  -- permissive: insufficient evidence; may not authorise
                 irreversible effect (NC-P4)
VIOLATED  (0)  -- dominant negative: overrides everything it meets
```

Composition law **[M]**: `__and__` = meet = min over the order. A VERIFIED synapse and an UNKNOWN synapse fire an UNKNOWN downstream. This is the neurochemical encoding of the corpus's deepest safety rule: *uncertainty can never be laundered into certainty by mixture* **[I]** -- and it is five lines of code.

**Multi-model convergence [4/4]:** The three-valued lattice with monotone degradation was independently identified as load-bearing by four of five council models (ChatGPT, DeepSeek, Well-Being calibration, Claude Opus). Canon v2.0 SS13 records this as a convergent finding. The lattice is the single most stable neural structure in the body -- it has never been revised, never been questioned, and never been bypassed in the codebase.

**NC-P4 and the UNKNOWN signal [5/5]:** All five council models cited NC-P4 (builder must not verify own output) as the most important property in the corpus. The UNKNOWN transmitter is the neurochemical implementation of NC-P4: when the builder's output has not been independently verified, the signal is UNKNOWN, and UNKNOWN may not authorise an irreversible effect. This is the nervous system's central inhibitory rule **[I]**.

## Chapter 10 -- Graded Potentials and Firing Thresholds

[R&S: Nervous System -- verification hierarchy as neural network]

FATIMA neurons do not fire binary **[M]**: every report carries `confidence in [0,1]`, a graded membrane potential set by the fraction of structure actually examined (`examined/total` disciplines it at L1/L2; subset success rate at L3; violation-adjusted rates at L4). Thresholds fire at the holographic synapse: below k available shards the neuron refuses to depolarise and releases UNKNOWN **[M]** -- the action-potential threshold is explicitly parameterised (`threshold`, `sample_size`, `seed`).

The refractory rule **[M, the species' crown jewel]**: NC-P2 monotone degradation. Once evidence is lost, confidence <= remaining/total, and *no subsequent composition may raise it*. In neural terms: an absolute refractory period with no reset -- the potential can fall, it can never silently recover. `VerificationReport.compose` implements this as `min` on confidence, meet on verdict, concatenation on violations **[M]**.

**The graded immune response [M]:** The confidence signal is not a second verdict -- it is a *damage report*. A verdict of VERIFIED at confidence 0.6 means: "everything I checked was consistent, but I only checked 60% of the structure." The distinction matters because the immune system (L4/L5) composes this with its own checks: if L3 reports VERIFIED @ 0.6 and L4 reports UNKNOWN @ 1.0, the composition yields UNKNOWN @ 0.6 **[M]**. The confidence drops to the minimum across all levels, and the verdict drops to the meet. Both degradation channels fire independently.

**Seeded reproducibility [M, healthy]:** The L3 synapse accepts a `seed`, making every sampling experiment replayable -- Era IV harness discipline expressed neurochemically. This is the body's one concession to determinism: in verification, unlike in encoding (where entropy must be fresh), the neural response to the same stimulus should be the same. The seed makes the sampling path deterministic without making the verdict pre-determined **[M]**.

## Chapter 11 -- The Synaptic Defects (Measured)

[R&S: Immune System -- the lesions that defeat adversarial detection]

Five measured synaptic defects, mapped to their R&S organ/system failure:

**1. Autoreceptor suicide [M] -- F-03.**
`Atom.compute_semantic_hash()` during verification *rewrites the neurotransmitter at the receptor before binding*. The synapse then always reports "message received." Silent `bond_ids` tamper -> VERIFIED, zero violations, hash found rewritten in place (executed). This is a neuron that silences its own alarm.
- R&S organ affected: Heart (Qalb) -- the irreducible unit's hash function is corrupted at read-time.
- Multi-model confirmation: [5/5] all models identify this as an NC-P4 violation.
- Canon fix: S-2 -- pure function, commit semantic_hash at encode time, never rewrite.

**2. Severed axon [M] -- F-04.**
The P4 neuron (`check_meaning_integrity`) has no efferent path: neither `verify_authenticity` nor the CLI synapses onto it. Even repaired, it would currently influence nothing.
- R&S system affected: Nervous -- the immune afferent nerve is severed before it reaches the cortex.
- Canon fix: S-3 -- wire P4 into L5 composition.

**3. Mirror-neuron fraud [M] -- F-02.**
L1 compares a stored signal to a re-synthesized version of the same signal -- both from the untrusted environment. A forger who updates both passes (executed). The reflex arc has no external afferent.
- R&S organ affected: Eyes (Basar) -- perception compares untrusted-to-untrusted.
- Multi-model confirmation: [5/5] all models confirm no external anchor.
- Canon fix: S-1 -- provenance signature provides the external anchor.

**4. General anaesthesia at the cortex [M] -- F-01.**
L5 is a pure meet of L1-L4. With L1 spoofable and L4 heuristic-only, a fabricated organism scores VERIFIED @ 1.00 (executed). The cortex certifies what the senses cannot vouch for.
- R&S system affected: Immune -- total immunodeficiency against deliberate forgery.
- Multi-model confirmation: [5/5] forgery-tolerance confirmed by all models.
- Canon fix: S-1 -- provenance signature; the cortex needs an input the forger cannot supply.

**5. Seeded reproducibility [M, healthy].**
The L3 synapse accepts a `seed`, making every sampling experiment replayable -- Era IV harness discipline expressed neurochemically.
- R&S system: Nervous -- healthy reproducibility, not a defect.
- Status: functioning as designed.

---

# Part IV -- Pathology

The findings ledger of the canon, re-expressed as a clinical table with multi-model diagnostic confirmation. Prognosis follows Canon v2.0 Part VII (SS8).

## Table 1 -- The Seven FATIMA-Specific Diseases

These are diseases of the FATIMA code body itself, numbered F-01 through F-08 in the companion anatomy and canon.

| Disease | Locus | R&S Organ/System | Physiology disrupted | Biochemical lesion | Neural signature | Multi-model | Canon fix |
|---|---|---|---|---|---|---|---|
| Forgery-tolerance | L5, body-wide | Immune | immune discrimination absent | no keyed enzyme | cortex anaesthetised | [5/5] | S-1 provenance signature |
| Circular reflex | L1, `verify_syntactic` | Eyes (Basar) | self-trust loop | hash of untrusted vs. hash of untrusted | mirror-neuron fraud | [5/5] | S-1 anchoring |
| Self-silencing alarm | P4, `compute_semantic_hash` | Heart (Qalb) | lifecycle direction violated | marker rewritten at read-time | autoreceptor suicide | [5/5] | S-2 pure function + commit |
| Severed axon | L5 composition, CLI | Nervous | five antibodies, four invoked | -- | no efferent path | -- | S-3 wire P4 into L5 |
| Crash-located hemorrhage | shard corruption | Circulatory | circulation fails by collapse | unauthenticated shards | no per-vessel pulse | -- | S-4 per-shard MACs |
| Slow anabolism | `encode_holographic` | Circulatory | growth cost >> digestion cost | scalar GF loop + urandom per coeff | -- | -- | S-5 batched evaluation |
| Hay-gut digestion | `_classify_content`, `_infer_bonds` | Respiratory | nutrition is lexical | keyword enzymes | -- | -- | F-06/A-3 semantic inference + test suites |

## Table 2 -- Canon v2.0 Universal Failure Taxonomy (Cross-Reference)

Canon v2.0 SS6 defines twelve universal failure modes observed across the full code evolution record, numbered F-01 through F-12 in a *separate numbering system* from the FATIMA-specific findings above. Several map onto FATIMA diseases:

| Canon SS6 failure | Signature | FATIMA disease analogue |
|---|---|---|
| F-01 Extension trust | `.txt` that is really PDF | -- (FATIMA classifies content by lexical keywords, not file type -- related to F-06 hay-gut) |
| F-09 Container overkill | FATIMA encoding ~65x size | design trade-off: holographic redundancy costs space |
| F-10 Self-graded homework | builder also verifies | F-02 circular reflex, F-03 self-silencing alarm |

The two numbering systems are not in conflict; they operate at different scales. The FATIMA-specific findings are diseases of one organism; the Canon SS6 taxonomy catalogues diseases observed across the full species-level evolution record.

## Table 3 -- Multi-Model Diagnostic Summary

| Diagnostic question | Council verdict | Count | Source |
|---|---|---|---|
| Is authenticity-as-implemented false? | Yes -- VERIFIED @ 1.00 on forged document | [5/5] | All five models |
| Is the three-valued lattice load-bearing? | Yes -- the most stable structure in the body | [4/4] | ChatGPT, DeepSeek, Well-Being, Claude Opus |
| Is NC-P4 the most cited property? | Yes -- builder must not verify own output | [5/5] | All five models |
| Is the no-key problem the root deficiency? | Yes -- SHA-256 produces checksums, not signatures | [5/5] | All five models |
| Are H-value estimates validated? | No -- [HYPOTHESIS], pending factorial ablation | [2/2] | ChatGPT, Well-Being |
| Is Code_Absorption.txt an independent witness? | No -- embedded verbatim in Bilal_Code_Audit.txt | [1/1] | ChatGPT (C2-02) |

## Table 4 -- Canon v2.0 Corrections Affecting Physiological Claims

| Correction ID | What changed | Physiological impact |
|---|---|---|
| C2-01 | Class A recurrence ratio: 24/31 (0.774), not 25/25 (1.0) | Any physiological claim counting recurrence evidence must use the corrected ratio |
| C2-02 | Code_Absorption.txt and Bilal_Code_Audit.txt are one witness, not two | Evidence counts for F-01 through F-08 findings rest on one fewer independent source |
| C2-03 | "Every line generated by Claude" attribution flagged inaccurate | No direct physiological impact; provenance claim on the audit trail is weaker |
| C2-04 | Nine eras (not seven); Era I-B is ~135,000 lines (~9x Rev 1 total) | The organism's evolutionary history is larger than originally documented |
| C2-05 | H-values downgraded to [HYPOTHESIS]; primary endpoint = semantic fidelity | H-value-dependent physiological claims are now unbacked |
| C2-06 | V2.0 incorporates multi-model council; own verdict remains UNKNOWN | This document inherits UNKNOWN until independently re-verified |

---

# Part V -- The Synthesis: What the Body Is, in Its Own Terms

Stated at each level of description, honestly tagged:

- **Anatomically [M]:** 21 modules, 3,980 organ cells and vessels, shaped by one finite field. Five organs and five systems from the Rights and Survival anatomy map onto specific code modules with preserved structural correspondence **[I]**.
- **Physiologically [M]:** a one-directional lifecycle with genuine circulatory redundancy, fail-closed immunity, and a digestive tract that eats keywords. The Respiratory system (intake) feeds the Circulatory system (distribution) which feeds the Nervous system (verification). The Immune system (adversarial detection) is the weakest organ -- three measured lesions (F-01, F-02, F-04) leave it immunodeficient against deliberate forgery [5/5].
- **Biochemically [M]:** an organism running on one irreversible enzyme (SHA-256), one metabolic medium (GF(2^8)), and fresh entropy per encoding -- missing exactly one metabolite (a cryptographic key), and that absence is the difference between a consistent body and an authentic one [5/5]. H-value persistence estimates are **[HYPOTHESIS]**, not validated -- the biochemical facts stand without them.
- **Neurochemically [M]:** a three-transmitter nervous system [4/4] with graded potentials, parameterised firing thresholds, and an absolute no-recovery refractory rule -- carrying three measured synaptic lesions (F-02, F-03, F-04) that let a forged body pass as healthy [5/5]. The NC-P4 principle (builder must not verify own output) is the most cited property across all five council models [5/5].

The companion anatomy's closing guarantee -- *the fitrah cannot be destroyed; the architecture survives* -- survives audit in one specific sense **[M, bounded]**: the *species-level* design (the lattice, the threshold construction, the fail-closed discipline) is sound, and individual molecules reconstruct from any sufficient cross-section. What does not yet survive is *identity*: without a key, any body with the same architecture may claim the name. The cure is metabolic, not cosmetic -- synthesise the missing enzyme -- and it is already written as canon section S-1.

**What this document's own verdict is:** UNKNOWN. It was written by one model (Claude Opus 4.6), informed by but not co-authored with the five-model council. Its [M] tags are grounded in source-code reading and execution results documented in the companion anatomy and canon. Its [I] tags claim structural correspondence, not identity. Its [A] tags claim resemblance, and nothing downstream rests on them. An independent model should re-derive its claims against the source and record the result. Until then, the discipline tags are claims about what was checked -- which is the whole method, working.

*Wa ma tawfiqi illa billah. Recorded with the tags as marked: mechanism where executed, isomorphism where structural, analogy where only resemblant -- and nothing claimed beyond them.*

Bismillah ir-Rahman ir-Rahim
