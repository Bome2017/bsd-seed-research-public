# Run013 family-minimisation successor — fresh formal audit

Audit date: 2026-09-10 (America/Los_Angeles).
Successor: `/Users/bsm/run013-family-minimisation-successor-2026-09-10/`
Parent (immutable, **not modified by this pass**):
`/Users/bsm/run013-aristotle-formalization-successor-2026-08-23/`

This is a **new audit**, not an inheritance of the 2026-08-23 `PASS`.  Its scope is the family
minimisation pass specified in `IMPLEMENTATION_SPEC_004_FAMILY_MINIMISATION.md`.  It re-derives
every acceptance figure from a build performed in this tree today.

```text
FAMILY_MINIMISATION_PASS        = PASS
BUILD                           = PASS      (lake build, exit 0, 8045 jobs)
LEGACY_INTERFACE_PRESERVED      = PASS      (35/35 types and axiom sets, byte-identical raw output)
F62_BLOCK_BYTE_IDENTICAL        = PASS      (sha256 unchanged; 10/10 declaration slices unchanged)
HARNESS                         = PASS      (42/42 entries)
NEW_MIN_LAYER                   = PASS      (7/7, standard axioms only)
HYGIENE                         = PASS      (0 sorry, 0 admit, 0 axiom, 0 native_decide)
PROPOSITION_A_FORMALIZED        = NO        (conventional; deliberate, see §5)
PROPOSITION_A_B_INDEPENDENT_REVIEW = PASS   (separate model, pre-comparison reconstruction; §8)
PARENT_TREE_MODIFIED            = NO
DEVIATIONS_FROM_SPEC            = NONE
FREEZE                          = COMPLETE
```

## 1. Provenance and pre-edit verification

The work tree was created by `cp -R` from the parent and verified **before any edit** against
`PREPATCH_RECEIPTS_005.md`: all seven touched-file SHA-256 digests matched, and the
`namespace F62 … end F62` block of `Family.lean` (lines 57–111, 1858 bytes) matched
`638b75d1…ddd39f5`.  `COPY_MATCHES_RECEIPTS = PASS`.

Build environment: Lean `4.28.0` (commit `7e01a1bf5c70fc6167d49c345d3bf80596e9a79b`), mathlib
`8f9d9cff6bd728b17a24e163c9402775d9e6a365` — the same revision recorded by the parent audit.
Prebuilt mathlib packages were cloned copy-on-write from an existing local checkout at the identical
revision; `lake-manifest.json` package revisions were compared and are identical.

**Baseline control.** The unedited copy was built first: exit 0, 8045 jobs.  Its live axiom harness
was captured (`_receipts/axioms_baseline_live.txt`) and compared to the frozen listing at
`RUN013_FORMALIZATION_REPORT.md:220–254`: **35/35 names and 35/35 axiom sets identical**.  The
environment therefore reproduces the 2026-08-23 result, so any post-edit difference is attributable
to the edit.

## 2. What changed

Seven files, exactly as specified.  Replaying the inherited `MANIFEST.sha256` against the edited
tree: **25 entries unchanged, 7 changed, 0 missing.**

| file | change |
|---|---|
| `RequestProject/Run013/Family.lean` | `F62min`, `F62.toMin`, and the `F62min.*` helper layer appended **after** `end F62` |
| `RequestProject/Run013/PhiSelmer.lean` | `phi_selmer_eq_min` + wrapper |
| `RequestProject/Run013/DualPhiSelmer.lean` | `dual_phi_selmer_eq_min` + wrapper |
| `RequestProject/Run013/Isogeny.lean` | `phi_selmer_eq_torsion_image_min` + wrapper |
| `RequestProject/Run013/FullTwoSelmer.lean` | `phi_selmer_ncard_min`, `dual_phi_selmer_ncard_min` + wrappers |
| `RequestProject/Run013/Main.lean` | `run013_primary_theorem_min`, `run013_selmer_orders_min` + wrappers |
| `RequestProject/Run013/Audit.lean` | harness 35 → 42 `#print axioms` entries |

`F62min` carries three fields (`prime`, `mod_eight`, `legendre_31`).  Its helper layer duplicates
all ten `F62.*` helpers and adds `ne_three` and `not_dvd_372`.

Declaration counts across the 19 Lean files: **84 theorems, 44 lemmas** (parent: 72 + 36).  The
deltas reconcile exactly: +12 theorems = `F62.toMin` + 4 `F62min` Legendre theorems + 7 `_min`;
+8 lemmas = the 8 `F62min` elementary lemmas.

## 3. Acceptance results

**[1] Build.** `lake build` exit 0, **8045 jobs**, identical job count to the baseline.  No errors,
no warnings.  **The pass required no repairs** — every construction in the spec elaborated as
written, including the `not_dvd_372` proof by iterated `Nat.Prime.dvd_mul`.

**[2] Harness.** 42/42 entries printed; 35 legacy + 7 new `_min`.

**[3] Legacy axiom sets — parsed.** All **35/35** legacy declarations map to identical axiom sets.
The two reduced-footprint controls are unchanged:

```text
Run013.eq_one_of_two_primary        [propext]
Run013.sha_analytic_two_valuation   [propext, Quot.sound]
```

**[3b] Legacy axiom output — raw.** The 35 legacy lines are **byte-identical** to the baseline
capture.  No formatting or ordering difference arose, so the parsed and raw criteria agree and no
adjudication was needed.

**[4] New `_min` layer.** All seven depend on exactly `[propext, Classical.choice, Quot.sound]` —
no custom axioms, nothing outside the standard three.

**[5] Legacy `F62` preservation.** `Family.lean` lines 57–111 hash to
`638b75d17a20592d47a1a4b1f800664363fb674809877f9c450425522ddd39f5`, unchanged, 1858 bytes.  The ten
individual declaration slices were also re-hashed against `PREPATCH_RECEIPTS_005.md` §3: **10/10
identical**.  Every `F62.*` name, type and proof body is byte-for-byte as audited.

**[6] Hygiene.** 0 `sorry`, 0 `admit`, 0 `axiom`, 0 `native_decide`, 0 `ofReduceBool`, 0 `unsafe`
(comment-stripped scan of all 19 files).

## 4. What is preserved, stated exactly

Every existing `F62.*` predicate/helper declaration retains its name, type and proof body
byte-for-byte.  The seven existing Selmer-facing public theorem names and types are preserved, but
their proof bodies are now one-line compatibility wrappers; their former proof bodies were copied
verbatim to the corresponding `_min` declarations.

The audited six-field `F62` structure is untouched, so `F62_FIDELITY` in the parent audit remains
checkable against `TARGET.md` §2 exactly as before.

## 5. Scope boundary — Proposition A is not formalized, deliberately

`F62min q → F62 q` is true (Proposition A, `PROPOSITIONS_A_B.md`) but is **not** formalized here.
Formalizing it needs a `WeierstrassCurve (ZMod q)` point-count bridge — an instantiation, a
nonsingularity proof, and `Nat.card (Affine.Point) = 1 + Nat.card (E62Affine q)` — none of which
exists in this development, whose declared scope is the Selmer identities (Level A) and whose
arithmetic layer is already `LEVEL_C = PARTIAL`.

Consequence, stated plainly: **inside Lean, `F62` and `F62min` are not interchangeable.**  `F62.toMin`
is available; the converse is not.  The `_min` theorems are formally stronger at the predicate level;
Proposition A, a conventional theorem, is what establishes that they have the same arithmetic prime
support.

`E62Affine`, `cardE62` and `aq62` are retained in `Family.lean` unchanged.  They are now unused by
the Selmer layer, but they are the statement of Proposition A and the parent audit's evidence of
actual point counting rather than a placeholder predicate.

## 6. Level grades

Unchanged from the parent audit; this pass alters no proof of a mathematical claim.

```text
LEVEL_A = PASS
LEVEL_B_CANONICAL_STATUS = CONDITIONAL_FORMAL_PASS
LEVEL_C = PARTIAL
LEVEL_D = EXTERNAL_DEPENDENCIES_RECORDED
```

The parent's own `RUN013_FORMALIZATION_REPORT.md:408` records `LEVEL_B = PASS`; the parent
independent audit records `CONDITIONAL_FORMAL_PASS`.  This audit follows the independent audit, as
the September 9 review also did.  That disagreement is inherited, not created here.

## 7. Qualifications

1. The mathlib package tree was reused from another local project at the identical revision rather
   than fetched fresh.  Package revisions were compared against `lake-manifest.json` and match; no
   independent verification of those vendored bytes was performed.
2. Job count is 8045 here against 8052 recorded by the parent audit.  Both builds completed cleanly
   and produced identical axiom output for all 35 legacy declarations; the difference is in lake's
   job accounting for the reused package tree, not in the project.
3. This audit was produced by the same agent that applied the patch.  It is a reproducible
   receipt-based audit, not an independent second party.  Every figure is re-derivable from
   `_receipts/` and the manifest.
4. Proposition A has a conventional proof and a computational hostile check (754 primes below
   60000, with two negative controls); it has not been reviewed by a second party.


---

## 8. Independent referee pass and freeze (added 2026-09-10, second sitting)

Propositions A and B were sent for hostile review to a separate model, in a packet containing no
verdict, roadmap or provenance narrative (`_external/PROP_A_REVIEW_PACKET_2026-09-10.zip`).  That
referee reconstructed Proposition A **before** reading the supplied proof and returned
`PROPOSITION_A = PASS`, `COROLLARY_A1 = PASS`, `PROPOSITION_B = PASS`, `MODEL_TRANSFER = PASS`,
`COUNTEREXAMPLE_FOUND = NO`, with an independent C++ computation over all 9,828 qualifying primes
below 10⁶.  Its bundle is preserved verbatim at
`_external/independent_referee_2026-09-10/` (`SHA256SUMS.txt` self-check 10/10 OK).

Everything the referee asserted was re-checked in this session against a third, independent
implementation; see `INDEPENDENT_REFEREE_VERIFICATION.md`.  9,616 of their rows were recomputed with
zero disagreements, and the new mathematics they contributed — the reciprocity identity
`(−31/q) = (q/31)`, the halving-quartic factorisation, the necessity direction, and the two group
counterexamples — was confirmed symbolically and numerically.

`PROPOSITIONS_A_B.md` is now **v2** (v1 preserved at `_receipts/PROPOSITIONS_A_B.v1.md`).  Changes,
all expository except the added Proposition A′:

1. the reciprocity step now uses `(−31/q) = (q/31)`, valid for every odd `q ≠ 31`;
2. the cyclicity of the Sylow 2-subgroup is derived explicitly from `|S[2]| = 2^r`;
3. the model transfer states the inverse map `u = X/4 − 1`, `v = (Y − X)/8`, gives the projective
   form with determinant 32, and notes that it fixes `[0:1:0]`;
4. step (v) is additive throughout and states that `S` is a cyclic **2-group**, with a remark
   giving `Z/12` and `Z/4 × Z/2` as counterexamples to the lemma without each hypothesis;
5. Proposition B is called **classical and unconditional**, not "elementary", and the phrase
   *relative natural density among the primes* is used without abbreviation;
6. new **Proposition A′** records the sharp finite-field characterisation
   `v₂(#E₁(k)) = 2 ⟺ χ_k(2) = χ_k(−31) = −1`, together with an explicit scope section explaining
   why it does **not** enlarge `F₆₂` — `q = 11` has `a_q = 0`, and `q ≡ 5 (mod 8)` is independently
   load-bearing for the 2-adic descent.

The old Chebotarev argument (`src/curves/F62_INFINITY.md` in the frozen proof project) is
**retained as historical and independent evidence and no longer carries the theorem**.  The referee
re-verified its mechanism; what it establishes is a containment of a positive-density Frobenius
class in `F₆₂`, not the identity of the family or its density.

Two fair criticisms of the packet's computational material were actioned: `_receipts/verify.py` now
exits nonzero on any failed check, and its header records that the halving search uses the very
duplication identity under review.  Re-run: exit 0, `ALL CHECKS PASSED`.

**The formal boundary is unchanged.**  `F62min q → F62 q` remains absent from Lean.  No amount of
conventional review converts it into a kernel-certified theorem, and `Family.lean` says so.
