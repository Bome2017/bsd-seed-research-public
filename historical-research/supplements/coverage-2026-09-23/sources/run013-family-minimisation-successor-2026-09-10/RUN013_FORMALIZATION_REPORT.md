# RUN013 — ARISTOTLE FORMALIZATION REPORT

Independent formal reconstruction of the frozen `62a1` BSD-at-2 target.

---

## 1. Project identity

| item | value |
|---|---|
| project root | `.` (this repository) |
| Lean library | `RequestProject` (glob `RequestProject.+`) |
| namespace | `Run013` |
| module tree | `RequestProject/Run013/*.lean` |
| exported main module | `RequestProject.Run013.Main` |
| axiom audit module | `RequestProject.Run013.Audit` |

Module list (build order):

```
RequestProject/Run013/Basic.lean              generic descent infrastructure
RequestProject/Run013/PadicTools.lean         p-adic valuation tools
RequestProject/Run013/Support.lean            support lemma + support reduction
RequestProject/Run013/Squareclasses.lean      squarefree representatives, classification
RequestProject/Run013/Selmer.lean             Q*/Q*^2 and the genuine Selmer sets
RequestProject/Run013/Family.lean             the exact family F_62
RequestProject/Run013/LocalInfinity.lean      archimedean local condition
RequestProject/Run013/LocalTwo.lean           local condition at 2
RequestProject/Run013/LocalThirtyOne.lean     local condition at 31
RequestProject/Run013/LocalQ.lean             local conditions at the moving prime q
RequestProject/Run013/PhiSelmer.lean          LEVEL A, phi side
RequestProject/Run013/DualPhiSelmer.lean      LEVEL A, dual side
RequestProject/Run013/Curves.lean             exact Weierstrass models
RequestProject/Run013/Isogeny.lean            exact isogeny, dual, orientation
RequestProject/Run013/FullTwoSelmer.lean      LEVEL B
RequestProject/Run013/BSDTwoBookkeeping.lean  LEVEL C
RequestProject/Run013/Main.lean               exported headline theorem
RequestProject/Run013/Audit.lean              #print axioms
```

## 2. Toolchain identity

| item | value |
|---|---|
| Lean | `leanprover/lean4:v4.28.0` (`lean-toolchain`) |
| Mathlib commit | `8f9d9cff6bd728b17a24e163c9402775d9e6a365` |
| Mathlib toolchain | `leanprover/lean4:v4.28.0` |
| build system | `lake` |

`lakefile.toml` pins `mathlib` at tag `v4.28.0`; the resolved working tree in
`.lake/packages/mathlib` is at commit `8f9d9cff6bd728b17a24e163c9402775d9e6a365`.
`lake build` emits one benign bookkeeping warning
(`manifest out of date: source kind (git/path) of dependency 'mathlib' changed`) because
the dependency is materialized as a local path package in this environment.  It is not a
build error and does not affect the compiled mathematics.

## 3. Supplied handoff identities (verified, read-only)

| item | expected | observed | verdict |
|---|---|---|---|
| archive SHA-256 | `652944cf19010247368525f3a68c310c9abc7d3eb20df2a2509c291c5c5d410e` | identical | PASS |
| handoff file count | 29 | 29 | PASS |
| `MANIFEST.sha256` SHA-256 | `39816c9244f00bdb124aeaf693e5e4772eab21018b5f4fe0af844eb47130c3e7` | identical | PASS |
| strict manifest replay | all entries OK | 28/28 OK | PASS |
| `provenance/SOURCE_PROJECT_MANIFEST.sha256` SHA-256 | `921fce81c78a3164431da6cf6eb618d37bb3d376108f733c534111726ee55d40` | identical | PASS |

`HANDOFF_IDENTITY = PASS`.

The archive was extracted **outside** the Lean project tree, made read-only, and never
modified.  `SOURCE_EVIDENCE_MODIFIED = NO`.

Material read before designing the formalization: `ARISTOTLE_HANDOFF.md`, `README.md`,
`STATUS.md`, `PROOF.md`, `TARGET.md`, `BSD_CHAIN.md`, `PRIOR_ART.md`,
`evidence/INDEPENDENT_REVIEW.md`, `evidence/DESCENT_DERIVATION.md`,
`src/curves/MODELS.md`, `src/isogeny/ISOGENY.md`, `src/selmer/EXACT_SEQUENCES.md`,
`src/selmer/SUPPORT_AND_GLOBAL.md`, `src/infinity/INFINITY.md`, `src/local_2/LOCAL_2.md`,
`src/local_31/LOCAL_31.md`, `src/local_q/LOCAL_Q.md`.

## 4. Theorem-layer map

### Layer 0 — generic descent infrastructure (`Basic.lean`)

* `SqEq K d c` — equality of square classes in a field `K`.
* `KummerImage K a b` — the image of the descent (`x`-coordinate) map on the curve
  `A_{a,b} : y^2 = x^3 + a x^2 + b x`, i.e. `{1} ∪ {b} ∪ {x ≠ 0 : ∃ y, y^2 = x^3+ax^2+bx}`.
* `InKummer K a b d` — `d` lies in that image modulo squares.
* `Cov K a b d` — the homogeneous space `n^2 = d u^4 + a u^2 v^2 + (b/d) v^4`
  with `(u,v) ≠ (0,0)`.
* `cov_iff_inKummer` — **proved bridge**: `Cov K a b d ↔ InKummer K a b d`
  (for `b ≠ 0`, `d ≠ 0`).  The Selmer group is *not* defined by the coverings; the
  coverings are proved equivalent to the genuine local Kummer images.

### Layer 1 — square classes of `Q` (`Selmer.lean`, `Squareclasses.lean`)

* `Qsq := ℚˣ ⧸ sqSubgroup` — the honest group `Q*/Q*^2`; `cls : ℚ → Qsq`.
* `SelmerSet a b : Set Qsq` — classes `d` with `InKummer` at `ℝ` **and** at every `ℚ_p`.
* `exists_squarefree_rep`, `squarefree_int_classify` — every class has a squarefree
  integral representative, and a squarefree integer supported on two primes lies in
  `± {1, r, s, rs}`.

### Layer 2 — local conditions

| place | statement | file |
|---|---|---|
| any `p ∤ b` | `support_lemma`: `v_p(D) = 1` kills the covering over `ℚ_p` | `Support.lean` |
| any `p ∤ b` | `support_reduction`: a squarefree everywhere-locally-soluble `D` has all prime factors dividing `b` | `Support.lean` |
| `∞` | `localinf_dual`: no real point on the dual covering for `d < 0` | `LocalInfinity.lean` |
| `2` | `local2_phi`: a `2`-adically soluble odd class on the `phi` covering satisfies `D ≡ 1 (mod 4)` | `LocalTwo.lean` |
| `31` | `local31_dual`: `v_31(D) = 1` kills the dual covering over `ℚ_31` | `LocalThirtyOne.lean` |
| `q` | `localq_dual_two`, `localq_dual_q`, `localq_dual_twoq`: the classes `2`, `q`, `2q` are excluded over `ℚ_q` | `LocalQ.lean` |

### Layer 3 — the family (`Family.lean`)

`F62 q` carries all five literal fields of `TARGET.md` §2.  Derived and proved:
`q ≠ 2`, `q ≠ 31`, `q % 4 = 1`, `¬ IsSquare (2 : ZMod q)` and
`¬ IsSquare ((-31 : ℤ) : ZMod q)` (the last by quadratic reciprocity from `(q/31) = -1`).

### Layer 4 — LEVEL A

* `phi_selmer_eq` (`PhiSelmer.lean`)
* `dual_phi_selmer_eq` (`DualPhiSelmer.lean`)
* `run013_primary_theorem` (`Main.lean`)

### Layer 5 — models and orientation (`Curves.lean`, `Isogeny.lean`)

`E62Curve`, `EqCurve`, `EqPrimeCurve` as mathlib `WeierstrassCurve ℚ`; discriminants
`Δ(62a1) = -2^4·31`, `Δ(E_q) = -2^16·31·q^6`, `Δ(E'_q) = 2^14·31^2·q^6`;
the frozen change of variables (`model_62a1`); the twist relation; the rational
two-torsion of both curves; `phi_maps_to`, `dual_phi_maps_to`,
`dual_comp_phi_eq_double` (checked against mathlib's own `addX`/`slope` duplication);
and `phi_coeffs` / `dual_coeffs`, which pin the orientation.

### Layer 6 — LEVEL B (`FullTwoSelmer.lean`)

Unconditional: the four classes are pairwise distinct, so
`(SelmerSet (phiA q) (phiB q)).ncard = 4` and `(SelmerSet (dualA q) (dualB q)).ncard = 1`.
Conditional (labelled `CONDITIONAL_ON_EXTERNAL_INPUT`), fully proved group theory:
`card_middle_of_exact`, `subsingleton_of_exact`, `eq_one_of_two_primary`.

### Layer 7 — LEVEL C (`BSDTwoBookkeeping.lean`)

Unconditional: `cq_component_root_iff` (the arithmetic reason for `c_q = 2`),
`no_rational_four_torsion` and `Eq_two_torsion_unique` (the `2`-primary torsion),
`descent_differential_is_half_neron` (the factor-of-two period normalization),
`tamagawa_product_valuation`.
Conditional: `sha_analytic_two_valuation`.

## 5. Exact Lean statements of the headline theorems

```lean
/-- LEVEL A, phi side. -/
theorem phi_selmer_eq (hq : F62 q) :
    SelmerSet (phiA q) (phiB q) = {cls 1, cls (-31), cls (q : ℚ), cls (-(31 * (q : ℚ)))}

/-- LEVEL A, dual side. -/
theorem dual_phi_selmer_eq (hq : F62 q) :
    SelmerSet (dualA q) (dualB q) = {cls 1}

/-- RUN013 PRIMARY THEOREM. -/
theorem run013_primary_theorem {q : ℕ} (hq : F62 q) :
    SelmerSet (phiA q) (phiB q) = {cls 1, cls (-31), cls ((q : ℚ)), cls (-(31 * (q : ℚ)))} ∧
    SelmerSet (dualA q) (dualB q) = {cls 1}

/-- The Selmer orders that feed the isogeny comparison. -/
theorem run013_selmer_orders {q : ℕ} (hq : F62 q) :
    (SelmerSet (phiA q) (phiB q)).ncard = 4 ∧ (SelmerSet (dualA q) (dualB q)).ncard = 1
```

with

```lean
def phiA (q : ℕ) : ℚ := 30 * q          -- a-coefficient of E'_q
def phiB (q : ℕ) : ℚ := -31 * (q : ℚ) ^ 2   -- b-coefficient of E'_q
def dualA (q : ℕ) : ℚ := -15 * q        -- a-coefficient of E_q
def dualB (q : ℕ) : ℚ := 64 * (q : ℚ) ^ 2   -- b-coefficient of E_q

structure F62 (q : ℕ) : Prop where
  prime : Nat.Prime q
  not_dvd_372 : ¬ (q ∣ 372)
  mod_eight : q % 8 = 5
  legendre_31 : legendreSym 31 (q : ℤ) = -1
  val_two : padicValNat 2 (cardE62 q) = 2
  trace_ne_zero : aq62 q ≠ 0

def LocalKummerAll (a b d : ℚ) : Prop :=
  InKummer ℝ (a : ℝ) (b : ℝ) (d : ℝ) ∧
    ∀ (p : ℕ) [Fact p.Prime], InKummer ℚ_[p] (a : ℚ_[p]) (b : ℚ_[p]) (d : ℚ_[p])

def SelmerSet (a b : ℚ) : Set Qsq :=
  {c | ∃ d : ℚˣ, qcl d = c ∧ LocalKummerAll a b (d : ℚ)}
```

## 6. Build result

`lake build` — **PASS**, all 18 modules of `RequestProject.Run013`, no errors, no
warnings other than the single dependency-bookkeeping note described in §2.

## 7. `sorry` / `admit` / custom-axiom audit

| quantity | value |
|---|---|
| `SORRY_COUNT` | 0 |
| `ADMIT_COUNT` | 0 |
| `axiom` declarations | 0 |
| `@[implemented_by]` | 0 |
| `native_decide` | 0 |
| `Lean.ofReduceBool` | 0 |
| `unsafe` | 0 |

Verified by a recursive text scan of `RequestProject/` (the only hits for the strings
`sorry`/`admit` are inside prose in doc-comments) and by `#print axioms`.

## 8. `#print axioms` results

Every headline theorem depends only on the standard Lean foundations
`[propext, Classical.choice, Quot.sound]` (two of the elementary group-theoretic lemmas
use strictly fewer).  Full list, as produced by `RequestProject/Run013/Audit.lean`:

```
Run013.phi_selmer_eq                      [propext, Classical.choice, Quot.sound]
Run013.dual_phi_selmer_eq                 [propext, Classical.choice, Quot.sound]
Run013.run013_primary_theorem             [propext, Classical.choice, Quot.sound]
Run013.run013_selmer_orders               [propext, Classical.choice, Quot.sound]
Run013.support_lemma                      [propext, Classical.choice, Quot.sound]
Run013.support_reduction                  [propext, Classical.choice, Quot.sound]
Run013.squarefree_int_classify            [propext, Classical.choice, Quot.sound]
Run013.exists_squarefree_rep              [propext, Classical.choice, Quot.sound]
Run013.localinf_dual                      [propext, Classical.choice, Quot.sound]
Run013.local2_phi                         [propext, Classical.choice, Quot.sound]
Run013.local31_dual                       [propext, Classical.choice, Quot.sound]
Run013.localq_dual_two                    [propext, Classical.choice, Quot.sound]
Run013.localq_dual_q                      [propext, Classical.choice, Quot.sound]
Run013.localq_dual_twoq                   [propext, Classical.choice, Quot.sound]
Run013.cov_iff_inKummer                   [propext, Classical.choice, Quot.sound]
Run013.mem_selmerSet_iff                  [propext, Classical.choice, Quot.sound]
Run013.model_62a1                         [propext, Classical.choice, Quot.sound]
Run013.EqCurve_Δ                          [propext, Classical.choice, Quot.sound]
Run013.EqPrimeCurve_Δ                     [propext, Classical.choice, Quot.sound]
Run013.phi_maps_to                        [propext, Classical.choice, Quot.sound]
Run013.dual_phi_maps_to                   [propext, Classical.choice, Quot.sound]
Run013.dual_comp_phi_eq_double            [propext, Classical.choice, Quot.sound]
Run013.phi_coeffs                         [propext, Classical.choice, Quot.sound]
Run013.dual_coeffs                        [propext, Classical.choice, Quot.sound]
Run013.phi_selmer_eq_torsion_image        [propext, Classical.choice, Quot.sound]
Run013.phi_selmer_ncard                   [propext, Classical.choice, Quot.sound]
Run013.dual_phi_selmer_ncard              [propext, Classical.choice, Quot.sound]
Run013.card_middle_of_exact               [propext, Classical.choice, Quot.sound]
Run013.subsingleton_of_exact              [propext, Classical.choice, Quot.sound]
Run013.eq_one_of_two_primary              [propext]
Run013.cq_component_root_iff              [propext, Classical.choice, Quot.sound]
Run013.no_rational_four_torsion           [propext, Classical.choice, Quot.sound]
Run013.descent_differential_is_half_neron [propext, Classical.choice, Quot.sound]
Run013.tamagawa_product_valuation         [propext, Classical.choice, Quot.sound]
Run013.sha_analytic_two_valuation         [propext, Quot.sound]
```

`CUSTOM_AXIOMS = none`.

## 9. Semantic drift audit

1. **Does the formal theorem quantify over EVERY `q` satisfying the exact frozen `F_62`
   predicate?**  **YES.**  `phi_selmer_eq (hq : F62 q)` with `q : ℕ` universally
   quantified; `F62` carries all five literal fields.  No numerical bound, no sampling.
2. **Are `E_q` and `E'_q` exactly the frozen models?**  **YES.**
   `EqCurve q = ⟨0, -15q, 0, 64q^2, 0⟩`, `EqPrimeCurve q = ⟨0, 30q, 0, -31q^2, 0⟩`, and
   `phiA/phiB`, `dualA/dualB` are proved equal to their `a₂`/`a₄` coefficients
   (`phi_coeffs`, `dual_coeffs`).
3. **Is the isogeny orientation exactly correct?**  **YES.**  `phi_maps_to` shows
   `phi_q(x,y) = (y^2/x^2, y(64q^2-x^2)/x^2)` lands on `E'_q`; `dual_phi_maps_to` shows
   `hat phi_q(x,y) = (y^2/(4x^2), y(-31q^2-x^2)/(8x^2))` lands on `E_q`;
   `dual_comp_phi_eq_double` shows the composite has the `x`-coordinate of `[2]` on `E_q`,
   checked against mathlib's own `addX`/`slope`.  The `phi`-Selmer group is computed from
   the coefficients of `E'_q` and the dual from those of `E_q`, so the two cannot be
   interchanged.
4. **Are the formal Selmer objects the genuine `phi` and dual-`phi` Selmer groups?**
   **YES.**  `SelmerSet` is defined by membership of the *local Kummer images*
   `InKummer` at `ℝ` and at every `ℚ_p`, inside the honest quotient group `ℚˣ/(ℚˣ)^2`.
   The coverings are only used after the proved equivalence `cov_iff_inKummer`.  No finite
   test appears in the definition.
5. **Is the `phi` group proved exactly equal to `{1,-31,q,-31q}`?**  **YES**, as an
   equality of subsets of `Qsq = ℚ*/ℚ*^2`, both inclusions proved.
6. **Is the dual group proved exactly trivial?**  **YES**, `= {cls 1}`.
7. **Is the reduction to finitely many square classes proved rather than assumed?**
   **YES.**  `exists_squarefree_rep` + `support_reduction` (itself proved from
   `support_lemma`, a genuine `p`-adic valuation-parity argument) + `squarefree_int_classify`.
   The finite list is *produced* by these theorems, not substituted for them.
8. **Are local conditions proved at infinity, 2, 31, and `q`?**  **YES.**
   `∞`: `localinf_dual`.  `2`: `local2_phi` (a primitive mod-16 argument, and the support
   lemma also applies at `2` on the `phi` side because `b = -31q^2` is odd).
   `31`: `local31_dual` on the dual side (on the `phi` side `31 | b`, so `31` is admitted
   into the support and the classes involving `31` are separated by the `2`-adic condition
   — exactly the asymmetry of the frozen proof).  `q`: `localq_dual_two`, `localq_dual_q`,
   `localq_dual_twoq`.  All other primes: `support_lemma`.
9. **Is there any hidden numerical bound on `q`?**  **NO.**
10. **Is any external checker verdict imported into the theorem?**  **NO.**  The supplied
    JSON certificate, the PARI script and the Python checker are not referenced by any
    Lean declaration.
11. **Is any BSD statement assumed in proving the Selmer theorem?**  **NO.**  `PhiSelmer`
    and `DualPhiSelmer` import only `Basic`, `PadicTools`, `Support`, `Squareclasses`,
    `Selmer`, `LocalTwo`/`LocalInfinity`/`LocalQ` and `Family`.  `BSDTwoBookkeeping`
    depends on them, never the converse.
12. **Is the distinction between rank zero and trivial `Sha[2]` preserved?**  **YES.**
    `subsingleton_of_exact` derives triviality of `Sha(E)[2]` from triviality of
    `Sha(E)[phi]` **and** `Sha(E')[hat phi]` through the exact sequence; no rank hypothesis
    appears anywhere in it.
13. **Is the Néron-period normalization kept distinct from the nonminimal descent-model
    differential?**  **YES.**  `descent_differential_is_half_neron` proves
    `dX/(2Y) = (1/2)·du/(2v+u+1)` explicitly; the factor of two is preserved and
    documented.
14. **Is the final strong-BSD conclusion kept separate from external deep theorem
    dependencies?**  **YES.**  Nothing beyond `sha_analytic_two_valuation` is claimed, and
    that theorem's analytic input is an ordinary hypothesis labelled
    `CONDITIONAL_ON_EXTERNAL_INPUT`.  Zhai and Banwait–Huang are recorded in prose only.

## 10. Finite-computation mechanism

There is exactly one kernel computation of any size: `local2_phi_mod16` in
`LocalTwo.lean`, discharged by `decide` over explicitly enumerated `List (ZMod 16)`
values (8 odd residues `D` × 2 residues of `q` × 4 possible squares each for
`u^2, v^2, m^2`).  It is a genuinely finite proposition about `ZMod 16`, encoded in Lean,
and evaluated by the Lean kernel.  `native_decide` is **not** used anywhere, and no
external computation is imported.

That finite statement is reached only after:

* `covM_integral` (integral normalization of a `ℚ_2`-point, with `(U,V)` primitive), and
* the reduction homomorphism `PadicInt.toZModPow 4 : ℤ_[2] →+* ZMod 16`,

so the finite case analysis is *derived*, not postulated.

The remaining case analyses (`squarefree_int_classify`, the eight-way split in
`phi_selmer_eq`, the eight-way split in `dual_phi_selmer_eq`) are ordinary `rcases`
over proved disjunctions, closed by `omega`/`decide` on integer congruences.

## 11. Formal-library obstruction

`FORMAL_LIBRARY_OBSTRUCTION` (Levels B and D only; Level A is unaffected).

* **Missing object:** Galois cohomology of elliptic curves — `H^1(G_Q, E[n])`, the
  Selmer group `Sel_n(E/Q)` as a cohomological object, and the Tate–Shafarevich group
  `Sha(E/Q)`.  Mathlib has `WeierstrassCurve`, its affine group law and `Δ`, but no
  `H^1`, no Selmer group, and no `Sha`.
* **Where the conventional proof needs it:** `BSD_CHAIN.md` §2, to run the isogeny-Selmer
  comparison sequence
  `0 → E'(Q)[hat phi]/phi(E(Q)[2]) → Sel^phi(E) → Sel_2(E) → Sel^{hat phi}(E')`,
  and the Kummer sequence `0 → E(Q)/2E(Q) → Sel_2(E) → Sha(E)[2] → 0`.
* **Strongest faithful layer formalized:** the *isogeny*-Selmer groups themselves are
  fully formalized and computed (Level A), because for a two-isogeny with rational kernel
  they are classical objects inside `ℚ*/ℚ*^2` describable by local Kummer images — which is
  exactly what `SelmerSet` is.  Their orders are computed unconditionally
  (`4` and `1`).  The exact-sequence step is then formalized as fully proved finite group
  theory whose inputs are ordinary hypotheses.
* **What remains outside Lean:** the construction of `Sel_2` and `Sha` and the exactness of
  the two displayed sequences; Tate's algorithm (hence `c_2 = 2`, `c_31 = 1`, and the
  reduction-type statement behind `c_q = 2`); the absence of odd torsion; Zhai's
  non-vanishing theorem; Banwait–Huang Theorem 2.13.

Also worth recording as a `FORMALIZATION_ENGINEERING_GAP` rather than an obstruction:
the handoff excludes the dual class `d = 2` at the prime `2` and the dual classes at
`31` by explicit `2`-adic and `31`-adic case analyses.  The reconstruction here excludes
`2` at the prime `q` instead (`localq_dual_two`) and `31` by the support lemma
(`local31_dual`); both routes are uniform and use only `q ≡ 5 (mod 8)` and `(q/31) = -1`.
The alternative `2`-adic exclusion of `d = 2` (which provably needs a mod-256 analysis,
not mod 16) was therefore not needed and is not formalized.

A formal-library limitation is not evidence that the mathematical theorem is wrong.

## 12. Boundary between kernel-verified mathematics and external dependencies

**Kernel-verified in this project (no `sorry`, no custom axiom):**

* the exact models, discriminants, change of variables and twist relation;
* the exact isogeny, its dual, and `hat phi ∘ phi = [2]` on `x`-coordinates;
* the equivalence between the quartic coverings and the local Kummer images;
* the structural reduction to a finite set of square classes;
* the local conditions at `∞`, `2`, `31`, `q` and at every other prime;
* `Sel^{phi_q}(E_q/Q) = {1, -31, q, -31 q}` and `Sel^{hat phi_q}(E'_q/Q) = {1}`
  for every `q ∈ F_62`;
* the orders `4` and `1` of those two groups;
* the finite group theory that converts the exact sequences into
  `#Sel_2 = 2`, `Sha(E)[2] = 0`, `Sha(E)[2^∞] = 0`;
* the arithmetic reason for `c_q = 2`;
* the `2`-primary torsion computation for `E_q(Q)`;
* the factor-of-two period normalization;
* the final `2`-adic valuation identity `0 + 2 - 2 = 0`, given its three inputs.

**External, recorded but not formalized:**

* Galois cohomology, `Sel_2`, `Sha` and the exactness of the two comparison sequences;
* Tate's algorithm and the reduction types at `2`, `31`, `q`;
* the absence of odd torsion in `E_q(Q)`;
* Zhai, *Non-vanishing theorems for quadratic twists of elliptic curves*,
  Asian J. Math. 20 (2016), Theorem 1.5 — giving `L(E_q,1) ≠ 0` and
  `v_2(L(E_q,1)/Ω(E_q)) = 0`;
* Banwait–Huang Theorem 2.13 and the odd-primary BSD assembly, together with the
  preprint qualifications recorded in `BSD_CHAIN.md` §6;
* the exact base modular-symbol value `|L(E,1)/Ω(E)| = 1/4`.

None of these is asserted as a Lean axiom.  Where they are needed they appear as ordinary
hypotheses of clearly labelled conditional theorems.

---

## Success classification

```text
RUN013_ARISTOTLE_LEVEL_A = PASS
RUN013_ARISTOTLE_LEVEL_B = PASS   (unconditional Selmer orders; the exact-sequence
                                   step is proved group theory with the sequence
                                   supplied as an explicit hypothesis)
RUN013_ARISTOTLE_LEVEL_C = PARTIAL (the elementary arithmetic reasons and the exact
                                   valuation identity are kernel-verified; the
                                   Tamagawa numbers themselves require Tate's
                                   algorithm, absent from mathlib)
RUN013_ARISTOTLE_LEVEL_D = EXTERNAL_DEPENDENCIES_RECORDED
```
