# ARISTOTLE-B — return: `ARISTOTLE_NEW_LEMMA_ONLY`

> **PARTIALLY SUPERSEDED.**  Three errors in this report's arithmetic interpretation — the
> alternating (rather than symmetric/quadratic) local pairing, the omission of the
> localization kernel in the finite-place model, and the invalid "transposition principle" —
> are corrected in `ARISTOTLE_B_CORRECTIONS.md`, together with a narrowing of the negative
> claims below.  The bad-place cohomology corollary and the abstract intersection lemma
> survive, in the scoped forms stated there.  Read that file first; the text below is kept
> unchanged for the record.

Fixed seed: `E/Q : y^2 = x^3 - 22735 x^2 + 106272484 x`, `N = 2^3 · 3 · 2243 · 4547^2 · 5843`,
`E(Q) = <(0,0)> ⊕ Z P_1 ⊕ Z P_2`, `P_1 = (4547, 327384)`, `P_2 = (5184, 281520)`, `G = Ш(E/Q)`.

**Terminology used here** (per the review's correction, canonical master names preserved):
`FIN` = `G` finite; `ORDER9` = `#G = 9`; `Q36` = `q = 36`. `FIN`, `ORDER9`, `Q36` are all open,
and nothing below closes or reduces any of them.

**What is new and proved.**

* **Theorem 1** (§2): bad-place cohomological vacuity for this seed, with the exceptional
  prime list `19, 59, 487` (for `p ≥ 5`, besides the bad primes themselves) proved exhaustive,
  plus three corollaries — including an exact verdict on the `x(P_1) = 4547`, `4547^2 | N`
  datum.
* **Theorem 2** (§3): the strict Selmer structure of this seed and its relaxed dual yield only
  the identity `0 = 0` and a relative identity between two unknowns. Tested as requested, then
  killed.
* **Theorem 3** (§4): a machine-checked abstract countermodel showing that the failure in
  Theorem 2 is structural for pairing-only mechanisms, not an artifact of bookkeeping.

**What is not achieved.** No bound on `#G[n]`, no bound on `dim Sel_p(E)` for any new prime, no
reduction of FIN or ORDER9. Every mechanism I invented is killed in §5, in each case by an
exact object rather than by a stylistic rule. §7 records the exact unresolved step.

**Evidence grades.** §1 is exact integer computation performed in this run (`scripts/tate.py`
and direct arithmetic): reproducible, no floating point, trust base = the script plus Python's
integer arithmetic. Theorem 1 and Theorem 2 are ordinary written proofs from standard theory
(Tate's algorithm, local Euler characteristic, local Tate duality, Greenberg–Wiles), applied to
the exact local data of §1. Theorem 3 is machine-checked in Lean 4.28.0 / mathlib
`8f9d9cff…`, no `sorry`, axioms `{propext, Classical.choice, Quot.sound}`. The *technique* of
Theorem 1 is standard; its *content* is seed-specific and exact. That is why the return is
`ARISTOTLE_NEW_LEMMA_ONLY` and not `ARISTOTLE_STRICT_REDUCTION`.

---

## 1. Phase 1 — exact constraints derived before naming any framework

### 1.1 Model and invariants

    a_2 = -5 · 4547,   a_4 = 2^2 · 4547 · 5843,   a_2^2 - 4 a_4 = 3^2 · 2243 · 4547
    c_4 = 2^4 · 43 · 1013 · 4547
    c_6 = 2^6 · 5 · 4547^2 · 8501
    Δ  = 2^8 · 3^2 · 2243 · 4547^3 · 5843^2      (minimal: v_ℓ(Δ) < 12 everywhere)

`E` is `y^2 = x(x^2 - 5·4547 x + 4·4547·5843)`, so `x = 4547` divides the quadratic's constant
term; `x(P_1) = 4547` gives `y^2 = 4547^2 · 5184` with `5184 = 72^2`, i.e. `P_1 = (4547,
4547·72)`. `gcd_p #E(F_p) = 2` over the good `p ≤ 43`, consistent with the retained
`E(Q)_tors = Z/2`.

### 1.2 Reduction types, Tamagawa numbers, split types (Tate's algorithm)

| ℓ | Kodaira | `v_ℓ(N)` | `c_ℓ` | `Φ_ℓ` | `#Ẽ_ns(F_ℓ)` | `m_ℓ = c_ℓ·#Ẽ_ns(F_ℓ)` |
|---|---|---|---|---|---|---|
| 2 | `I_1*` | 3 | 2 | `Z/4` geom., `Z/2` rational | 2 (`G_a`) | 4 |
| 3 | `I_2`, **nonsplit** | 1 | 2 | `Z/2` | 4 | 8 |
| 2243 | `I_1`, **split** | 1 | 1 | trivial | 2242 = 2·19·59 | 2242 |
| 4547 | `III` | 2 | 2 | `Z/2` | 4547 (`G_a`) | 9094 |
| 5843 | `I_2`, **nonsplit** | 1 | 2 | `Z/2` | 5844 = 2^2·3·487 | 11688 |

The computed conductor `2^3·3·2243·4547^2·5843` reproduces the retained `N` exactly: an
independent check of the entire local computation. Split types are as corrected: `3` nonsplit,
`2243` split, `5843` nonsplit. All Tamagawa numbers are `2`-powers and `∏_ℓ c_ℓ = 16`.

### 1.3 Interaction of `P_1, P_2, T = (0,0)` with the bad fibres

| | 2 | 3 | 2243 | 4547 | 5843 |
|---|---|---|---|---|---|
| `T = (0,0)` | non-identity | identity | identity | **non-identity** | **non-identity** |
| `P_1` | identity | **non-identity** | identity | **non-identity** | identity |
| `P_2` | non-identity | identity | identity | identity | identity |

So in `∏_ℓ Φ_ℓ(F_ℓ) ≅ (Z/2)^4` (places `2, 3, 4547, 5843`)

    T ↦ (1,0,1,1),   P_1 ↦ (0,1,1,0),   P_2 ↦ (1,0,0,0),

three independent vectors: **the global component map is injective on `E(Q)/2E(Q)`.** This is
an exact statement about the known Mordell–Weil plane; it is `2`-primary, and `G[2^∞] = 0` is
retained, so it says nothing about the quotient.

### 1.4 The `x(P_1) = 4547`, `4547^2 | N` datum — exact consequences, then discard

1. `v_{4547}(c_4) = 1`, `v(c_6) = 2`, `v(Δ) = 3`: Kodaira **III**, `c = 2`, `f = 2`, and
   `e = 12/gcd(12,3) = 4` — potentially good with quartic ramification.
2. Hence `j(E) ≡ 1728 (mod 4547)`, **verified exactly**. Since `4547 ≡ 3 (mod 4)`, the good
   reduction obtained over the ramified quartic extension is **supersingular** with `j = 1728`,
   and `I_{4547}` acts on `T_p E` through the order-`4` group `⟨[i]⟩`.
3. Therefore, for every odd `p ≠ 4547`, the eigenvalues of `I_{4547}` on `E[p]` are primitive
   fourth roots of unity, so `E[p]^{I_{4547}} = 0`.
4. `v_{4547}(x(P_1)) = 1 > 0`, so `P_1` reduces to the singular point: `P_1` and `T` lie on the
   **non-identity** component at 4547, `P_2` on the identity component, and
   `P_1 + T ∈ E_0(Q_{4547})`.

Items 1, 2, 4 agree with the independent local check in the review (`P_1 mod 4547 = (0,0)`
singular, `P_2 mod 4547 = (637,4153)` smooth, `2P_1 mod 4547 = (1296,3361)` smooth) and with
the retained surface C-SURF, of which the seed is the specialization `t = 4547/144` under
`x = 144X, y = 1728Y`; I claim no novelty for the parametrization and spent no further effort
on it. **The one consequence I use that is not a statement about the family is item 3.**

Item 4 is the only consequence that mentions the coincidence at all, and `Φ_{4547} = Z/2` makes
it a statement about `2`-torsion of a component group. By Theorem 1 all of §1.2–§1.4 is
invisible to `G[p]` for `p ≥ 5` outside `{19, 59, 487, 2243, 4547, 5843}`. **Verdict: the
coincidence changes no local Kummer class, formal-group filtration, local height or torsor
evaluation for any odd `p` of interest. Discarded.**

---

## 2. Theorem 1 — bad-place cohomological vacuity for the seed

**Theorem 1.** Let `p ≥ 5` be a prime with `p ∉ {19, 59, 487}`, and let
`ℓ ∈ {2, 3, 2243, 4547, 5843}` with `ℓ ≠ p`. Then

    E(Q_ℓ)[p] = 0    and    H^1(Q_ℓ, E[p]) = 0.

In particular the local Kummer image, the unramified subgroup `H^1_ur(Q_ℓ, E[p])` and the
strict subgroup all coincide — all are zero, and the ambient local cohomology is itself zero.

*Proof.* Fix `ℓ ≠ p`. In `E_1(Q_ℓ) ⊆ E_0(Q_ℓ) ⊆ E(Q_ℓ)`, `E_1(Q_ℓ)` is pro-`ℓ`,
`E_0/E_1 ≅ Ẽ_ns(F_ℓ)`, `E/E_0 ≅ Φ_ℓ(F_ℓ)` of order `c_ℓ`. Since `p ≠ ℓ`, `E(Q_ℓ)[p]` injects
into `E(Q_ℓ)/E_1(Q_ℓ)`, of order `m_ℓ = c_ℓ·#Ẽ_ns(F_ℓ)`. By §1.2,
`m_ℓ ∈ {4, 8, 2242, 9094, 11688}`, whose prime divisors are exactly `2, 3, 19, 59, 487, 4547`
(machine-checked: `SeedBadPlace.prime_dvd_localOrder_iff`). For `p ≥ 5`, `p ∉ {19,59,487}` and
`p ≠ 4547 = ℓ`, we get `p ∤ m_ℓ`, so `E(Q_ℓ)[p] = 0`, i.e. `H^0(Q_ℓ, E[p]) = 0`.

The Weil pairing makes `E[p]` self-dual, so local Tate duality gives
`H^2(Q_ℓ, E[p]) ≅ H^0(Q_ℓ, E[p])^∨ = 0`; and since `ℓ ∤ #E[p]` the local Euler characteristic
is trivial, `#H^1 = #H^0·#H^2 = 1`. Hence `H^1(Q_ℓ, E[p]) = 0`. ∎

At `ℓ = 4547` the vanishing `H^0 = 0` also follows structurally from §1.4(3).

**Corollary 1.1 (the generic object is a strict Selmer structure).** For `p` as above,

    Sel_p(E) = { c ∈ H^1(Q, E[p]) : res_ℓ(c) = 0 for all bad ℓ,
                                    c unramified at every good ℓ ≠ p,
                                    res_p(c) ∈ H^1_f(Q_p, E[p]) }.

At the bad places the strict condition is not a strengthening: the ambient groups vanish, so
strict = unramified = Kummer there. (`E[p]` is ramified at the bad primes, so this may **not**
be rewritten as `H^1(Q_{\{p,∞\}}, E[p])`; the strict Selmer structure is the correct object.)

**Corollary 1.2 (all seed-supplied local data is inert).** For `p` as above, every datum of
§1.2–§1.4 — Kodaira type, component group, Tamagawa number, split type, component image of
`P_1, P_2, T`, the `4547` coincidence, the local Kummer image at each bad place — imposes no
condition on `Sel_p(E)` beyond vanishing, because the group in which such a condition would
live is `0`.

**Corollary 1.3 (no reciprocity relation couples the bad places).** For `c ∈ Sel_p(E)` and any
`x`, the terms of `Σ_v inv_v(res_v c ∪ res_v x) = 0` at all five bad places are identically
zero. A "global reciprocity relation coupling the local data at `2, 3, 2243, 4547, 5843`" is
therefore the relation `0 = 0`; any pairing, matrix of local functionals, or descent invariant
supported on those places annihilates `Sel_p(E)` for trivial reasons and bounds nothing. The
only possibly nonzero terms are at `p`, at `∞` (zero for odd `p`), and at auxiliary good
primes.

**Exceptional primes, exactly.** For `p ≥ 5` a bad place can be non-vacuous only for
`p ∈ {19, 59}` (split `I_1` at 2243: `E(Q_{2243})[p] ≅ μ_p`, `p | 2242`), `p = 487` (nonsplit
`I_2` at 5843, `487 | 5844`), and `p ∈ {2243, 4547, 5843}` (`ℓ = p`). The list is proved
exhaustive, not assumed.

---

## 3. Theorem 2 — the strict structure and its relaxed dual give no bound (tested, then killed)

Let `p ≥ 5` be outside the exceptional list and `d = dim_{F_p} E(Q_p)[p] ∈ {0,1,2}`. Local
dimensions: `dim H^1(Q_p, E[p]) = 2 + 2d`, `dim H^1_f(Q_p, E[p]) = 1 + d` (maximal isotropic),
`dim H^0(R, E[p]) = 1`, `H^1(R, E[p]) = 0`, all bad-place groups `0` (Theorem 1). Write `F_Kum`
for the Kummer structure of Corollary 1.1, `F_str` for strict-at-`p`, `F_rel` for relaxed-at-`p`.

**Theorem 2.**
(i) `F_Kum^* = F_Kum`, and Greenberg–Wiles

    dim Sel_F - dim Sel_{F^*} = dim H^0(Q,E[p]) - dim H^0(Q,E[p]^*) + Σ_v ( dim L_v - dim H^0(Q_v,E[p]) )

reads, term by term, `0 = ((1+d) - d) + (0 - 1) + Σ_{bad}(0-0) = 0`. No inequality, no
information about `dim Sel_p(E)`.

(ii) `F_str^* = F_rel`, and the same formula gives the purely relative identity

    dim Sel_{F_rel} = dim Sel_{F_str} + 1 + d.

Both sides are global unknowns and the difference is a sum of local terms. Since
`Sel_{F_str} ⊆ Sel_{F_Kum} ⊆ Sel_{F_rel}`, bounding `Sel_p(E)` above is equivalent to bounding
the everywhere-strict group `Sel_{F_str}`, a `Ш^2`-type global object, above.

*Transposition principle.* For any Selmer structure `F`, duality determines
`dim Sel_F − dim Sel_{F^*}` and determines it by local dimensions alone. A duality argument
therefore converts "upper-bound `Sel_F`" into "lower-bound `Sel_{F^*}`" of exactly the same
size; for the self-dual Kummer structure the conversion is the identity and is empty. Producing
such a lower bound means exhibiting global classes with prescribed ramification at auxiliary
primes — input this run does not have. **Killed**, by computation rather than by fiat.

---

## 4. Theorem 3 — machine-checked countermodel: the §3 failure is structural

Everything a pairing-only mechanism can use is: a nondegenerate alternating form on
`⊕_v H^1(Q_v, E[p])`, the maximal isotropic `L = ⊕_v L_v` of local conditions, and the maximal
isotropic image `G` of the global classes (this maximal isotropy *is* global reciprocity), with
`Sel_p(E) = G ⊓ L`. Bad places drop out of the sum by Theorem 1.

**Theorem 3** (`RequestProject/SelmerDualityCountermodel.lean`, no `sorry`, axioms
`{propext, Classical.choice, Quot.sound}`):

* `SelmerDuality.exists_maximal_isotropic_pair_inter` — for every `N` and every `k ≤ N` there
  are maximal isotropic `G, L` in the standard symplectic space over `N` places, with `L` the
  fixed **product of local conditions**, such that `dim (G ⊓ L) = k`.
* `SelmerDuality.exists_config_with_known_plane` — the same with a distinguished
  `2`-dimensional subspace (the known Mordell–Weil plane) inside `G ⊓ L` and `k ≥ 2` arbitrary:
  the quotient modelling `G[p]` stays unconstrained after the known plane is fixed.
* `SelmerDuality.inter_unbounded` — hence no bound at all.

**Scope, stated precisely.** This refutes only theorems whose hypotheses are *exactly*
(nondegeneracy) + (maximal isotropy of the local conditions) + (maximal isotropy of the global
image) + (number of places) + (a fixed `2`-dimensional known subspace). It is **not** a no-go
theorem for upper bounds in general. It does not exclude: a surjection onto `Sel_p(E)` from a
source of independently bounded dimension; a map out of `Sel_p(E)` with controlled kernel; an
annihilator theorem; an integral index / valuation comparison that retains torsion information;
or a lower bound on a dual Selmer group from global classes with prescribed ramification. Each
of those carries a hypothesis the countermodel violates.

---

## 5. Mechanisms invented and killed (each by an exact object)

| # | object and intended arrow to `G[n]` | exact killer |
|---|---|---|
| 1 | **Simultaneous local-condition matrix** at `2,3,2243,4547,5843` whose kernel is to be `Sel_p/(E(Q)/p)` | Theorem 1: those matrices are `0 × 0`. Also `G[p]` is a *quotient* of `Sel_p`; presenting it as a kernel of functionals needs a splitting, i.e. the answer. |
| 2 | **Néron-component reciprocity pairing** of `c ∈ Ш[p]` against the component images of `P_1, P_2, T` | Corollary 1.3: every bad-place term is identically `0`. More basically, `Ш` classes are locally trivial everywhere, so no first-order local functional distinguishes them. |
| 3 | **Descent invariant attached to `4547^2 ‖ N`** (quartic inertia, supercuspidal fibre) | §1.4: the true consequences are `j ≡ 1728 (mod 4547)`, `e = 4`, `E[p]^{I_{4547}} = 0`. The last makes the place *more* vacuous; the `P_1` component statement is `2`-primary and `G[2^∞] = 0` is retained. |
| 4 | **Integral-lattice / reduction-theory bound** `#Sel_n(E) ≤ C·n^2` for all `n`, giving `#G[n] ≤ C` and, for `C < 1089`, ORDER9 | Not rejected for being equivalent — under the corrected equivalence rule an independent proof of an equivalent assertion would count. Rejected because **I could prove no instance of it**: `#Sel_n = n^2·#G[n]` exactly for odd `n`, so the hypothesis carries the full unknown, and the minimization/invariant theory that could make the hypothesis independently accessible exists only for `n ≤ 5`, where the primary parts are already retained. Recorded as unresolved, not as a no-go. |
| 5 | **Strict Selmer structure + Poitou–Tate**, bounding via the dual relaxed group | Theorem 2: self-dual structure gives `0 = 0`; strict/relaxed gives a relative identity between two unknowns. |
| 6 | **Any new bilinear/quadratic pairing or global reciprocity identity** built from the local data alone | Theorem 3 (machine-checked), within the scope stated in §4. |

A separate exact remark used above: rank 2 forces `#Sel_p(E) ≥ p^2`, so a `p`-independent bound
on `#Sel_p(E)` is false outright; only `G[p]`-valued targets are admissible.

---

## 6. New obstructions (the reusable negative content)

* **B1 — Bad-place vacuity.** For this seed and `p ≥ 5` outside `{19, 59, 487, 2243, 4547,
  5843}`, `H^1(Q_ℓ, E[p]) = 0` at every bad `ℓ`. A mechanism whose inputs are the seed's
  bad-reduction data has no data. (Theorem 1.)
* **B2 — First-order invisibility of `Ш`.** `Ш` classes are locally trivial at every place, so
  a condition of the form "`c ∈ Ш[p] ⟹ F_v(c) = 0` at several places" is satisfied by *every*
  local functional and carries no information; only a second-order construction (Cassels–Tate,
  or a lift out of `Ш`) can be nonvacuous at all.
* **B3 — Self-duality neutrality / transposition.** The Kummer Selmer structure is its own
  dual, so global duality yields `0 = 0`, and any duality-only bound is equivalent to a lower
  bound of the same size on the dual Selmer group. This constrains duality-only arguments; it
  does not constrain arguments carrying independent input (see §4, Scope).
* **B4 — No `p`-uniform `Sel` target.** `#Sel_p(E) ≥ p^2`, so a fixed object bounding
  `#Sel_p(E)` independently of `p` cannot exist; admissible targets are `G[p]`-valued.

---

## 7. Dependency chain and the exact unresolved step

    Tate's algorithm on the minimal model (§1.2, scripts/tate.py; conductor check)
      -> local orders m_ℓ and their prime divisors (Lean: SeedBadPlace.prime_dvd_localOrder_iff)
      -> E(Q_ℓ)[p] = 0 for p ≥ 5 outside {19,59,487,2243,4547,5843}
      -> [local Euler characteristic + local Tate duality + Weil self-duality]
      -> H^1(Q_ℓ, E[p]) = 0                                            (Theorem 1)
      -> Corollaries 1.1 (strict Selmer structure), 1.2 (inertness), 1.3 (trivial reciprocity)
      -> Greenberg–Wiles for F_Kum, F_str, F_rel                        (Theorem 2)
      -> abstract countermodel for the pairing-only axioms              (Theorem 3, Lean)

**Exact unresolved step.** After Theorem 1 the only non-vacuous local data for `p ≥ 5` outside
the explicit exceptional set sit at `v = p` and at auxiliary good primes; by Theorem 2 the only
way duality yields an inequality is a *lower* bound on a dual Selmer group. The step I could
not complete is:

    for a fixed p and a Chebotarev-admissible auxiliary prime ℓ, construct a global class in
    the ℓ-relaxed Selmer group whose localization at ℓ is nonzero, without an Euler system and
    without assuming FIN.

No theorem was obtained for that step and I record no candidate construction for it: honest
unresolved attempt, not a no-go claim.

---

## 8. Files

| file | content |
|---|---|
| `scripts/tate.py` | Tate's algorithm over `Z_p`; reproduces `N = 2^3·3·2243·4547^2·5843`, the Kodaira types, Tamagawa numbers and split types of §1.2 (sanity-checked against known curves) |
| `RequestProject/SeedBadPlacePrimes.lean` | machine-checked bookkeeping feeding Theorem 1: the primes dividing some `m_ℓ` are exactly `2,3,19,59,487,4547`, plus the exceptional-prime corollary |
| `RequestProject/SelmerDualityCountermodel.lean` | Theorem 3, with its scope stated in the file header |

Both Lean files compile against Lean 4.28.0 / mathlib `8f9d9cff…` with no `sorry` and axioms
`{propext, Classical.choice, Quot.sound}`. The Lean files verify abstract and arithmetic-
bookkeeping statements only; the elliptic-curve content of Theorems 1 and 2 is written proof,
displayed separately above.
