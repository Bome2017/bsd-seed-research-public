# Theorem status — the H¹-free bridge, complete

`OBJECT_TYPE = CONSOLIDATED_THEOREM_STATUS`
`DATE = 2026-09-11`
`MATHEMATICS_ADDED_BY_THIS_OBJECT = NONE`
`PROGRAMME_STATUS = COMPLETE — closed by decision at the agreed endpoint, not by failure`

This document states **exactly** what the completed programme proves and **exactly** what lies
outside it. It supersedes no frozen object; it summarises them. Where this document and a freeze
disagree, the freeze governs.

---

## 1. The family

For `ε ∈ {1, −1}`, `m ≥ 3`, `r = ε·2^m`, and

    A = 1 − 2r        B = r²        D = 1 − 4r

and a prime `q` satisfying `SDyadic.Params ε m q`:

    q ∤ 2D        q ≡ 5 (mod 8)        (D/q) = −1        every v_ℓ(D) odd for odd ℓ ∣ |D|

on the certified stratum `SDyadic.H41 ε m`:

    (D < 0 and s = 1)   or   (D > 0, s = 2, and every odd prime divisor of |D| is ≡ 3 mod 4)

where `s` counts the odd prime divisors of `|D|`. The two curves are actual
`WeierstrassCurve ℚ` objects:

    E_q  : y² = x³ + (Aq)x²  + (r²q²)x
    E'_q : Y² = X³ + (−2Aq)X² + (Dq²)X

and all statements below are about `WeierstrassCurve.Affine.Point` — **mathlib's own group of
nonsingular rational points**, with mathlib's own addition.

Non-vacuity is witnessed at both `H₄₁` branches: `(ε,m,q) = (1,3,13)` with `D = −31`, and
`(−1,3,5)` with `D = 33 = 3·11`.

---

## 2. What is proved

### 2.1 The endpoint

`P04c.two_descent_quotient`, double-run certified:

    E_q(ℚ) / 2E_q(ℚ)  ≃+  Additive (G_{φ,exp} ⧸ K_exp)

    Nat.card (E_q(ℚ) / 2E_q(ℚ)) = 2

    E_q(ℚ) / 2E_q(ℚ)  ≃+  ZMod 2

together with the point-cokernel exact sequence that yields them: `φ̂` induces a **surjection**

    E'_q(ℚ) ⧸ φ(E_q(ℚ))  →+  E_q(ℚ) ⧸ 2E_q(ℚ)

pinned to be `⟦P'⟧ ↦ ⟦φ̂(P')⟧`, whose kernel is exactly the image of `ker φ̂`.

Here `2E_q(ℚ)` is `AddMonoidHom.range` of doubling, `G_{φ,exp} = ⟨[D],[q]⟩` and
`K_exp = ⟨[D]⟩` are `Subgroup (ℚˣ ⧸ squares)`.

### 2.2 The twelve certified stages beneath it

| stage | what it certifies | replication grade |
|---|---|---|
| Theorem F, `S_dyadic` | the explicit descent-realization objects | two runs |
| `H₄₁` saturation | `LocalKummerAll ⟺ Cov` both sides; `GlobalSet = SelmerSet` both sides; `[G_{φ,exp} : K_exp] = 2` | two runs, substantially different architectures |
| δ (`Descent.delta_descent`) | δ is a homomorphism on the actual point group; its image is the covering-soluble classes | two runs |
| P01 | the 2-torsion of both curves, named points, the Legendre obstruction | two runs, 1 shared name |
| P03a | actual coordinate point maps `φ`, `φ̂`, nonsingularity | two runs, 4 shared names |
| P03b | both maps respect the group law | two runs, **0 shared names, different constructions** |
| P03c | bundled `AddMonoidHom`s and exact kernels `{O,T}`, `{O,T'}` | two runs, confirmation-grade |
| P03d | `φ̂(φ(P)) = P + P` and `φ(φ̂(P')) = P' + P'` | two runs, **architectural cross-check** |
| P03e | `ker δ_E = im φ̂`, `ker δ_{E'} = im φ` | two runs, **constructive cross-check** |
| P04a | the actual cokernels, identified with `range δ` by δ itself; cokernel of `φ` nontrivial | two runs, confirmation-grade |
| P04b | `range δ_{E'} = G_{φ,exp}`, `range δ_E = ⊥`, `δ_{E'}(ker φ̂) = K_exp` | two runs, **architectural cross-check** |
| **P04c** | **the endpoint above** | two runs, confirmation-grade |

Every stage: `lake build` clean at the pin with zero `sorry`, axiom footprint
`[propext, Classical.choice, Quot.sound]`, `sorryAx` absent, verified by external rebuild.

### 2.3 Consequences certified by the cross-run probes

Proved through the frozen targets, in both developments, for the whole family:

* every rational point of `E_q` has trivial descent class, hence `im φ̂ = E_q(ℚ)` and the dual
  cokernel `E_q(ℚ) ⧸ φ̂(E'_q(ℚ))` is the **trivial group**;
* `T' = (0,0)` on `E'_q` is a **nonzero** class in `E'_q(ℚ) ⧸ φ(E_q(ℚ))`, while `T = (0,0)` on
  `E_q` is **zero** in `E_q(ℚ) ⧸ φ̂(E'_q(ℚ))` — the certified Legendre obstruction visible as
  nontriviality of an actual point cokernel;
* `K_exp ≤ G_{φ,exp}`, derived rather than assumed;
* in `E_q(ℚ)/2E_q(ℚ)` there is exactly one nonzero class, every class is killed by doubling, and
  every class is the class of a `φ̂`-image.

### 2.4 The dependency footprint of the endpoint

A Lean elaborator walking the whole proof term (`receipts/dependency_footprint.lean`,
`receipts/DEPENDENCY_FOOTPRINT.txt`) finds 385 (Run A) / 393 (Run B) project constants beneath
`P04c.two_descent_quotient`, with **identical answers in both runs** on every headline constant.
Genuine dependencies include the saturation theorem, both exhaustion lemmas, the audited 62a1
core `Run013.cov_iff_inKummer`, the δ layer, `P01.Ecurve_two_torsion`, and P03a–P03e and P04b.

Three constants are **not** dependencies, in either run:

* `P04a.isogeny_cokernels` — thirteen P04a constants are (`deltaHomE`, `deltaHomE'` and their
  simp lemmas), but not the theorem. P04a is load-bearing for the programme, not for this proof
  term;
* `P01.p01_family_two_torsion` — its component `P01.Ecurve_two_torsion` is;
* `P04c.KExp_le_GphiExp`, which Claude supplied proved in the handoff.

---

## 3. What is NOT proved — the boundary, stated positively

`FORMALIZATION_LEVEL = EXPLICIT_2_ISOGENY_DESCENT_REALIZATION`
`ACTUAL_H1_SELMER_OBJECT = NO`
`touches_L_function = NO`

**3.1 `rank E_q(ℚ) = 0` is NOT proved, and does not follow.** An abelian group can satisfy
`G/2G ≅ C₂` without being finitely generated — a divisible or otherwise non-finitely-generated
part is not excluded by any statement in this development. Reaching the rank requires
Mordell–Weil finite generation, which is **not** formalized here and is not in the pinned
mathlib for these curves.

**3.2 `E_q(ℚ)` is NOT proved finite.** `Nat.card (E_q(ℚ) ⧸ 2E_q(ℚ)) = 2` is a statement about the
quotient. No `Finite` or `Fintype` hypothesis appears in code anywhere in the development, in
either return of any stage; the construct scans record this.

**3.3 No cohomological Selmer group exists here.** `S_dyadic`, `Run013.SelmerSet`, `G_{φ,exp}`
and `K_exp` are defined by solubility of quartic coverings over ℝ and every ℚ_p. None is
`H¹(ℚ, E[φ])`. The phrase "formalized cohomological Selmer group" is **false** of every object in
this programme. Genuine `Sel₂` is a separate construction.

**3.4 Ш, `Ш[2^∞]`, and BSD are untouched.** Nothing here bounds or computes a Tate–Shafarevich
group, and nothing here touches `L(E,s)` or any analytic invariant.

**3.5 No mathlib `Isogeny` object was created.** The pinned mathlib has no isogeny API; `φ` and
`φ̂` are a manually constructed degree-2 point-map pair with certified kernels, composites, image
characterisation and cokernels. Describe it that way, never as "the isogeny is formalized in
mathlib".

**3.6 The family is not broadened.** `m ≥ 3` is retained exactly; `m ≥ 1` was never in scope. The
frozen 66b1 family is not enlarged.

**3.7 No novelty is claimed.** `PRIOR_ART_BLOCKER` for 66b1 remains `UNRESOLVED`. Nothing in this
programme — including `E_q(ℚ)/2E_q(ℚ) ≅ C₂` — is asserted to be new.

---

## 4. What "certified" means here

`LEAN_CERTIFIED` in this programme means: proved in Lean 4 at toolchain
`leanprover/lean4:v4.28.0` against mathlib `8f9d9cff6bd728b17a24e163c9402775d9e6a365`, and
**replayed by two independent Aristotle proof-search runs**, each audited by external rebuild.

It does **not** mean independent proof-assistant verification. Both runs use the same Lean kernel
and the same mathlib revision; a soundness defect in either would affect both identically. It
also does not establish that the two runs were causally isolated — that rests on the operator's
run discipline, not on anything in these objects. **This qualification is mandatory wherever any
of these results is described.**

Three other certification tiers are used in the surrounding corpus and must never be merged with
the above: `DOUBLE_INDEPENDENT_CONVENTIONAL_PROOF` (Theorem A) and
`CONVENTIONAL, BASE-CONDITIONED, LITERATURE-DEPENDENT` (Theorem B).

---

## 5. Custody findings worth carrying forward

**21 of the programme's 22 Aristotle returns shipped defective or absent metadata.** Counted
from the notices on disk rather than from a running tally: 18 stale-manifest notices covering 17
distinct returns, 3 partial-wrapper notices, and saturation Run A, which shipped no root manifest
at all and returned the handoff's unchanged.

**Exactly one return was clean: saturation Run B**, the very first stage, whose successor manifest
replayed 30/30 against its own tree (`S_DYADIC_SATURATION_FORMALIZATION_FREEZE_002/ERRATA.md`
E2). No return since has matched it. The running "Nth occurrence" ordinals inside the individual
notices are **not** a consistent series — see `P04C_…FREEZE_001/ERRATA.md` E10, which also records
that this document's own first draft got the tally wrong.

This is the empirical basis of the standing rule:

> **Never certify an Aristotle return from its own receipts.** The returned source is the object
> to audit; build, axiom, source-scan, manifest and archive evidence is regenerated externally,
> and declarations are counted from source with block comments stripped.

No metadata defect was ever a proof defect.

**Replication strength cannot be read off a shared-name count.** P04a scored 0 shared names and
was confirmation-grade; P04b scored 5 and was a cross-check; P04c scored 2 and was
confirmation-grade. From P04a onward every grade is reported with a normalised route comparison,
a citation profile, and — from P04c — a transitive dependency footprint. Recorded as `ERRATA` E7
in the P04a, P04b and P04c freezes.

**Withholding the route works.** For P04c the sender verified reachability privately by
transporting along `P04a.isogeny_cokernels`; **neither run took that route.** Both independently
built two surjections out of `E'_q(ℚ)` with a common kernel, never forming
`E'_q(ℚ) ⧸ φ(E_q(ℚ))` as an intermediate object.

**One orientation error was caught by reading the frozen sources rather than the notation.**
`range δ_E` was described in prose as `K_exp = ⟨[D]⟩`; it is trivial, and `K_exp` is the image of
`ker φ̂` under `δ_{E'}`. Corrected before any Lean statement was written; it never entered a
frozen object. Recorded as `ERRATA` E8 in the P04b and P04c freezes.

---

## 6. The frozen objects

28 programme objects are listed in `receipts/ALL_OBJECT_VERIFICATION.txt` with their digests.
**27 carry root manifests; all 27 replayed clean — 1869 manifest entries, 0 mismatches** — and
every archive digest was recomputed from disk.

`P03_GENEALOGY_001` is the twenty-eighth: a four-file provenance note with no root manifest. It
is listed as such rather than silently omitted. This object, which contains the table, is not in
it.

---

## 7. What would come next, and why nothing is authorised

The remaining gates, in dependency order:

1. **Mordell–Weil finite generation for `E_q(ℚ)`** — without it, §3.1 stands and the rank is out
   of reach whatever else is proved.
2. **Genuine cohomological `Sel₂`** — an actual `H¹(ℚ, E[φ])`, which requires Galois cohomology
   machinery the pinned mathlib does not have for these objects.
3. **`Ш[2^∞]`**, then
4. **BSD**, which additionally requires `L(E,s)` — and `touches_L_function = NO` has been the
   standing finding about this whole line of work since the Run013 terminal-state assessment.

Each is a separate phase with its own go/no-go decision. **None is authorised by the completion
of this programme.** The correct reading of P04c is that it is the end of the bridge the two
hostile audits prescribed, not a licence to continue automatically.
