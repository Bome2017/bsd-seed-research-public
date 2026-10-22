# RESULT — continuation run, 2026-10-06

> **Revision 2 (after the 2026-10-06 direction review):** several claims below are narrowed or
> withdrawn — Lemma 3 is restricted to good ordinary `p` (so `p = 29` leaves the coverage list),
> exact `a_ℓ = 0` is not needed (modulus `M_ℓ = gcd(a_ℓ, ℓ+1)`), the coverage obstacle (B) is
> removed for fixed finite batches, Prop. 4 refutes only the specific height test, and cofinite
> vanishing gives FIN, not ORDER9. See `REVISION_2.md`; it takes precedence over this file.

Status label (a claim for review): **PARTIAL_CONSTRUCTION / TESTED_CANDIDATE (height route
refuted). FIN, ORDER9 and Q36 are UNCHANGED.**

Input: this project directory. `prepare_reference.py` extracted and verified
`payload/COMPLETE_READING_SET.zip` (5,180 members). `prepare_latest_review.py` extracted and
verified `payload/BFR_REVIEW.zip` (64 members). See `STATE.json` for what was extracted versus
what was actually read.

## 1. Mechanism selected

The record's Heegner lane over `K = ℚ(√−23)` is blocked with the recorded reason "no
cross-prime index". This run builds and tests a candidate cross-prime index: **derived
Heegner points at supersingular inert auxiliary primes**.

## 2. Strongest statements proved (exact scope in `PROOF.md`)

* **Lemma 1 (kernel-checked).** Kolyvagin's derivative identity `(σ − 1)D = m − Tr` holds in
  any ring with `σ^m = 1`. If the trace of `y` vanishes, then `σ(Dy) − Dy = m·y`, so `Dy` is
  `σ`-invariant modulo every divisor of `m` at once. With the Heegner norm relation and
  `a_ℓ = 0` this gives `(σ − 1)D_ℓ y_ℓ = (ℓ + 1)y_ℓ` exactly.
* **Lemma 2 (written; characteristic-polynomial core kernel-checked).** If `ℓ ∤ 23N` is inert
  in `K` and `a_ℓ(E) = 0`, then `ℓ` is a Kolyvagin prime for `(E, K, p)` simultaneously for
  every prime `p ≥ 5`, `p ≠ 23`, with `p ∣ ℓ + 1`. This holds for ordinary and supersingular
  `p` alike. It uses retained A.3.
* **Lemma 3 (written, with imports).** For such `ℓ` and admissible `p ∣ ℓ + 1`, `p ∤ 23N`:
  `P_ℓ ∉ pE(H_ℓ)` implies `Sha(E/ℚ)[p] = 0`. Here `P_ℓ` is a single, `p`-independent derived
  Heegner point. This defines a cross-prime index `ι(ℓ)`: the point governs every admissible
  prime factor of `ℓ + 1` at once. Imports are Kolyvagin's structure theorem in its mod-`p`
  form, with `ν = 1` because `y_K` is torsion, and the Gross–Zagier and norm relations.
* **Proposition 4 (written; all inequalities kernel-checked).** Archimedean heights cannot
  certify `ι(ℓ)`. For every odd `p ∣ ℓ + 1`, `ĥ(D_ℓ y_ℓ)/p² ≥ ĥ(y_ℓ) ≥ μ`, where `μ` is any lower
  bound for heights of non-torsion points of `E(H_ℓ)`. So no Lehmer/Lang/Silverman-type
  minimum, however sharp, excludes `p`-divisibility of the derived point.
* **Seed finite facts (kernel-checked).**
  * Heegner hypothesis for `ℚ(√−23)` (explicit square roots of `−23` modulo 3, 2243, 4547,
    5843, and `−23 ≡ 1 (mod 8)`).
  * `ℓ = 281, 661, 839` are inert and have `a_ℓ = 0` (by a complete enumeration of all `ℓ²`
    pairs).
  * `282 = 2·3·47`, `662 = 2·331`, `840 = 2³·3·5·7`.
* **Exact computation (Python, not kernel-checked).** There are 30 supersingular inert
  `ℓ < 10⁵`. Their `ℓ + 1` cover 28 primes `p ≥ 5`, including `p = 53` via `ℓ = 3391`. They miss
  37 and 41.

## 3. Endpoint effect, stated without enlargement

* **FIN: unchanged.** No `P_ℓ` was computed, so no `ι(ℓ)` is known and no new primary
  component is settled. A cofinite theorem via this mechanism needs two inputs that remain
  open:
  * (A) a mod-`(ℓ + 1)` arithmetic formula controlling the class of `P_ℓ`; and
  * (B) for every large `p`, a supersingular inert `ℓ ≡ −1 (mod p)`.
    This is a Lang–Trotter-type statement in progressions, which is open.
* **ORDER9: unchanged.**
* **Q36: unchanged.**
* **What changed.**
  * The record's "no cross-prime index" verdict for the Heegner lane is narrowed. A
    `p`-independent object whose indivisibility controls several primes at once does exist,
    with the identity of Lemma 1 holding uniformly.
  * One natural method of controlling it, Gross–Zagier heights combined with height lower
    bounds, is now excluded by a proof, not merely left untried.
  * Lemma 3 is an equivalent-type criterion. Per the task rules it is not counted as new
    upper control.

## 4. Formal verification

New Lean sources are in `RequestProject/Continuation/`:

* `CrossPrimeKolyvagin.lean`
* `HeightObstruction.lean`
* `SeedFinite.lean`
* `SeedPointCounts.lean`

They build with Lean 4.28.0 and the pinned Mathlib. They contain no `sorry` and no
`native_decide`, and add no axioms. `#print axioms` reports only `propext`,
`Classical.choice` and `Quot.sound` (see `lean/`). Heegner points, Selmer groups,
Kolyvagin's theorem and Néron–Tate heights are **not** formalized. Prop. 4 is formalized at
the level of its inequalities; the identification of `ĥ(D_ℓ y_ℓ)` with the weighted character
sum is a written step.

## 5. First remaining arithmetic equation

An independently controlled `A(ℓ) ∈ ℤ/(ℓ + 1)` with `P_ℓ ∉ pE(H_ℓ) ⇐ A(ℓ) ≢ 0 (mod p)` for all
admissible `p ∣ ℓ + 1`. The candidate is the first-order coefficient of the Heegner
Mazur–Tate element `θ_ℓ` at a supersingular inert `ℓ`, via a Bertolini–Darmon-type
comparison. That comparison is unproved, and it must avoid reintroducing the record's
uncontrolled `C_p`. See `HANDOFF.md`.
