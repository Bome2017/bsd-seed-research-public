# PROOF — cross-prime derived Heegner points at supersingular inert primes

Continuation run, 2026-10-06. Convention: the minimal model
`E: y² = x³ − x² − 66020924x − 65074271436` (conductor `N = 2³·3·2243·4547²·5843`) and a
fixed optimal modular parametrization `φ: X₀(N) → E`. Finite computations use the record's
original model `y² = x³ − 22735x² + 106272484x`. This is the change `x ↦ x + 7578` with
`u = 1`, so `a_ℓ` agrees at every odd good prime. Imports are cited where they are used and
listed in `ASSUMPTIONS.json`.

Grades: **[L]** is kernel-checked in this run (`RequestProject/Continuation/*.lean`).
**[W]** is a written proof in this file. **[I]** is an imported theorem. **[C]** is an exact
Python computation (`checks/`).

## 0. Choice of mechanism and why

The record's Heegner lane over `K = ℚ(√−23)` is a certified rank-one-twist field
(`rank E^{−23}(ℚ) = 1`, `rank E(K) = 3`). It currently gives only fixed-prime criteria
(Kim, arXiv:2609.15328). The compendium records the blocking reason as **"no cross-prime
index"** (units E12a-158 / 16479, ROUTE_BLOCKED). This run tests one concrete source of such
an index. In the rank-one case, the Gross–Zagier index `[E(K):ℤy_K]` controls every `p` at
once because `y_K` does not depend on `p`. The question is whether a single
`p`-independent derived Heegner point can control several `p` at once in rank two.

The operation: use Kolyvagin primes with `a_ℓ = 0` exactly. Such a prime is a Kolyvagin prime
simultaneously for **every** admissible `p` dividing `ℓ + 1` (Lemma 2). One derived point
`P_ℓ` then yields every class `c_p(ℓ)` at once (Lemma 3). The first unproved equation is a
bound on the `p`-divisibility of `P_ℓ`. §4 shows that archimedean heights cannot supply this
bound, at any prime and however sharp the bound used. §5 records the second missing input,
which is coverage of all large `p`.

## 1. Setting

Let `K = ℚ(√−23)` (class number 3, `O_K^× = {±1}`). Fix an odd prime `ℓ ∤ 23N` inert in `K`.
Let `H_n` be the ring class field of conductor `n`. Then `G_ℓ = Gal(H_ℓ/H_1)` is cyclic of order
`m := ℓ + 1` (since `u_K = |O_K^×|/2 = 1`). Fix a generator `σ`. Let `y_n = φ(x_n) ∈ E(H_n)` be
the Heegner points (Gross, *Kolyvagin's work on modular elliptic curves*, §3). Put

    D_ℓ = Σ_{i=0}^{m−1} i σ^i ∈ ℤ[G_ℓ],
    P_ℓ = Σ_{g ∈ Gal(H_1/K)} g̃ · D_ℓ y_ℓ ∈ E(H_ℓ),

where `g̃` runs over lifts of `Gal(H_1/K)` to `Gal(H_ℓ/K)`.

**Heegner hypothesis [L].** `−23 ≡ 1 (mod 8)`, and `−23` is a nonzero square modulo 3, 2243,
4547 and 5843, via the square roots 1, 142, 2063 and 1428
(`SeedFinite.two_splits`, `SeedFinite.heegner_hypothesis_odd`). The square class of `−23`
modulo `4547` is the condition needed for `4547² ∣ N`. The record already establishes this
hypothesis and `w(E^{−23}) = −1`. The new formal check confirms the arithmetic.

## 2. The derivative identity, all moduli at once

**Lemma 1 [L].** Let `R` be any ring, `s ∈ R` and `s^m = 1`. Then
`(s − 1)·Σ_{i<m} i s^i = m − Σ_{j<m} s^j` (`CrossPrime.derivative_relation`). Let `M` be an
abelian group, `σ` an additive endomorphism with `σ^m = 1`, and `y ∈ M` with
`Σ_j σ^j y = 0`. Then `σ(D y) − D y = m·y`, so `D y` is `σ`-invariant modulo `d·M` for every
`d ∣ m` simultaneously (`cross_prime_invariance`, `cross_prime_invariance_dvd`).

**Application [I+L].** The norm relation (Gross, Prop. 3.7, `ℓ` inert, `u = 1`) is
`Tr_{H_ℓ/H_1} y_ℓ = a_ℓ y_1`. If `a_ℓ = 0`, the trace vanishes. Lemma 1 then gives
`(σ − 1) D_ℓ y_ℓ = (ℓ + 1) y_ℓ` in `E(H_ℓ)`, exactly and not just modulo one `p`.

## 3. Simultaneous Kolyvagin primes and the cross-prime index

**Lemma 2 (simultaneous Kolyvagin primes) [W, with L core].** Suppose `ℓ ∤ 23N` is inert in `K`
and `a_ℓ(E) = 0`. Then `ℓ` is a Kolyvagin prime for `(E, K, p)` for every prime `p ≥ 5` with
`p ∣ ℓ + 1` and `p ≠ 23`. That is, `Frob_ℓ` lies in the conjugacy class of complex
conjugation `τ` in `Gal(K(E[p])/ℚ)`.

*Proof.* Import A.3: `ρ̄_{E,p}` is surjective for every odd `p`. The unique quadratic subfield
of `ℚ(E[p])` is `ℚ(√p*)` with `p* = ±p`. It differs from `K` because `p ≠ 23`. Hence
`Gal(K(E[p])/ℚ) = GL₂(𝔽_p) × Gal(K/ℚ)`. `ℓ` is inert, so `Frob_ℓ` and `τ` have the same
nontrivial image in `Gal(K/ℚ)`. Mod `p`, `Frob_ℓ` has characteristic polynomial
`X² − a_ℓ X + ℓ ≡ (X − 1)(X + 1)` (`CrossPrime.supersingular_charpoly` [L]). Since `p` is odd,
its eigenvalues `±1` are distinct, so it is conjugate in `GL₂(𝔽_p)` to `diag(1, −1) = ρ̄(τ)`. ∎

The ordinary/supersingular nature of `p` itself plays no role. The lemma covers ordinary and
supersingular `p` alike. Only the auxiliary prime `ℓ` is supersingular.

**Lemma 3 (cross-prime criterion) [W + I].** In the situation of Lemma 2, suppose also
`p ∤ 23N` and `p ≥ 5`. Let `c_p(ℓ) ∈ H¹(K, E[p])` be Kolyvagin's class. If `P_ℓ ∉ pE(H_ℓ)`,
then `Sha(E/ℚ)[p] = 0`.

*Proof.*
1. By Lemma 1, `P_ℓ mod p` is `G_ℓ`-invariant in `E(H_ℓ)/p`.
2. `E(H_ℓ)[p] = 0`, because `H_ℓ/ℚ` is generalized dihedral and `ρ̄` is surjective.
   Restriction therefore identifies `H¹(K, E[p])` with `H¹(H_ℓ, E[p])^{Gal(H_ℓ/K)}`. Under this,
   `c_p(ℓ)` is the Kummer image of `P_ℓ` (Gross §4). So `c_p(ℓ) ≠ 0` if and only if
   `P_ℓ ∉ pE(H_ℓ)`.
3. `y_K` is torsion, since `ord_{s=1} L(E/K, s) ≥ 3` and Gross–Zagier applies. Hence
   `c_p(1) = 0`, and the Kolyvagin system first becomes nonzero at `ν = 1`.
4. Import Kolyvagin's structure theorem (Math. Ann. 291 (1991); theorem number not
   re-verified here). Let `ν` be minimal with some `c(n) ≠ 0` and `ω(n) = ν`. Then the
   eigenspace `Sel^{ε_ν}` has dimension `ν + 1` and `Sel^{−ε_ν}` has dimension at most `ν`,
   with `ε_ν = ε_0(−1)^ν`.
5. `y_K` lies in the `ε_0 = −w(E/ℚ) = −1` eigenspace. Hence `ε_1 = +1` and
   `dim Sel_p(E/K)^+ = dim Sel_p(E/ℚ) ≤ 2`.
6. With the rank-two point subspace, `Sha(E/ℚ)[p] = 0`. ∎

The sign bookkeeping in step 5 and the mod-`p` form of step 4 are imported. They are the
points a reviewer should check first. The record's Kim Thm 1.1 (derived-Heegner divisibility
⇔ finiteness, for `r_p^+ ≥ 2`) is the same family of statement at a fixed `p`.

**Definition (cross-prime index).** For `ℓ` as in Lemma 2, let `ι(ℓ)` be the product of the
admissible primes `p ∣ ℓ + 1` with `P_ℓ ∈ pE(H_ℓ)`. Lemma 3 gives `Sha(E/ℚ)[p] = 0` for
every admissible `p ∣ (ℓ + 1)/ι(ℓ)`. A single `p`-independent point thus controls every
admissible prime factor of `ℓ + 1` at once. This is exactly the shape of index the record
said was missing. The prime-power refinement is analogous, using `c_{p^k}(ℓ)` with
`p^k ∣ ℓ + 1`.

**Seed instances [L + C].** `ℓ = 281, 661, 839` are inert in `K`
(`SeedFinite.inert_281`, …). Each has exactly `ℓ` affine points
(`SeedPointCounts.affCount_281`, …), hence `a_ℓ = 0`. The factorizations are
`282 = 2·3·47`, `662 = 2·331` and `840 = 2³·3·5·7`. So `P_281` simultaneously governs
`p = 47`, `P_661` governs `p = 331`, and `P_839` governs `p = 5` and `7`. Among the 30
supersingular inert `ℓ < 10⁵` (`checks/supersingular_inert_100000.out.json`, [C]), `ℓ = 3391`
governs `p = 53` (`3392 = 2⁶·53`). This is the first prime not settled by the record and
relevant to ORDER9. No `P_ℓ` is computed: Heegner points at level `N ≈ 6.5·10¹⁵` are outside
this run's resources and outside the task's scope.

## 4. Attempted control of `ι(ℓ)`: the height route is excluded

The only `p`-independent quantitative control of a point that is available is its Néron–Tate
height. Gross–Zagier–Zhang gives the components `ĥ(e_χ y_ℓ)` through `L′(E/K, χ, 1)`. The
natural attempt is to show that `P_ℓ` is not divisible by `p` because `ĥ(P_ℓ)/p²` would be
smaller than the minimal height on `E(H_ℓ)`. A uniform positive minimum
`μ_ab = inf {ĥ(Q) : Q ∈ E(K^ab) non-torsion} > 0` does exist (Silverman 2004, import; `H_ℓ`
is abelian over `K`).

**Proposition 4 (height obstruction) [W + L].** Let `ℓ` be as in Lemma 2 with `y_ℓ` of infinite
order, and let `p` be any odd prime dividing `ℓ + 1`. Let `μ` be any number with
`0 < μ ≤ ĥ(Q)` for all non-torsion `Q ∈ E(H_ℓ)`. Then `ĥ(D_ℓ y_ℓ)/p² ≥ μ`. Hence no lower bound
for heights of points of `E(H_ℓ)`, of any strength, excludes `D_ℓ y_ℓ ∈ pE(H_ℓ)`. Suppose
`Gal(H_ℓ/K) = G_ℓ × Gal(H_1/K)` (for example when `3 ∤ ℓ + 1`). Then the same argument applies
to `P_ℓ`, with `y_ℓ` replaced by `y′_ℓ = Σ_g g̃ y_ℓ`, provided `y′_ℓ` has infinite order. One
gets `ĥ(P_ℓ) ≥ (m²/4) ĥ(y′_ℓ)` and `μ ≤ ĥ(y′_ℓ)`.

*Proof.*
1. Decompose `E(H_ℓ) ⊗ ℂ` into the eigenspaces of the characters `χ` of `G_ℓ`. These are
   orthogonal for the `G_ℓ`-invariant Hermitian extension of `ĥ`.
2. By Lemma 1 evaluated at `χ(σ) = ζ ≠ 1`, the `χ`-component of `D_ℓ y_ℓ` is
   `m/(ζ − 1) · e_χ y_ℓ` (`CrossPrime.derivative_root_of_unity` [L]). The trivial component of
   `y_ℓ` is `m⁻¹ Tr y_ℓ = 0`, since `a_ℓ = 0`.
3. Using `|ζ − 1| ≤ 2`,
   `ĥ(D_ℓ y_ℓ) = Σ_{χ≠1} |m/(ζ_χ − 1)|² ĥ(e_χ y_ℓ) ≥ (m²/4) ĥ(y_ℓ)`
   (`Height.derivative_height_lower_bound` [L]).
4. `y_ℓ` is itself non-torsion in `E(H_ℓ)`, so `μ ≤ ĥ(y_ℓ)`.
5. `m = ℓ + 1` is even and `p` is odd, so `2p ∣ m` and `m²/4 ≥ p²`. Hence
   `ĥ(D_ℓ y_ℓ)/p² ≥ ĥ(y_ℓ) ≥ μ` (`Height.height_obstruction` [L]). ∎

**Interpretation.** In rank one the height decides the index because `E(K)` has rank one. Here
the Kolyvagin derivative inflates the height by at least `m²/4 ≥ p²`. This happens for every
prime `p` it is meant to test, and it happens by the identity `λ_χ = m/(ζ − 1)` itself, not
because of a weak estimate. The upper bound is
`ĥ(D_ℓ y_ℓ) ≤ m²(m² − 1)/12 · max_χ ĥ(e_χ y_ℓ)`, from the classical sum
`Σ_{k=1}^{m−1} |ζ^k − 1|^{−2} = (m² − 1)/12`. It does not help either, because Prop. 4 is a
lower bound on the quantity that would need to be small. Divisibility of `P_ℓ` by `p` is a
purely `p`-adic/cohomological property, invisible to archimedean heights. This rules out the
whole family "Gross–Zagier heights + Lehmer/Lang/Silverman minimum" as a source of `ι(ℓ)`.
It does not rule out other sources (§6).

## 5. Coverage of the infinite tail

Suppose `ι(ℓ)` were controlled. A cofinite theorem would still need, for every large `p`, an
inert `ℓ` with `a_ℓ = 0` and `p ∣ ℓ + 1 = #E(𝔽_ℓ)`. Supersingular primes of a non-CM curve have
counting function conjecturally `≍ √X/log X` (Lang–Trotter). Elkies proved there are
infinitely many. Their distribution in residue classes `ℓ ≡ −1 (mod p)` is not known, so the
existence of a single such `ℓ` for each large `p` is open. The data to `10⁵` [C]: 30 such `ℓ`.
Together they cover the primes
`5, 7, 11, 13, 17, 19, 23, 29, 31, 43, 47, 53, 59, 61, 71, 73, 83, 89, 113, 137, 139, 331, 353,
401, 487, 883, 1399, 5077`. They miss 37 and 41 (and `p = 23` is excluded anyway). This is
consistent with the heuristic that one needs `ℓ ≍ p² log² p` to cover `p`. It is real
arithmetic input, not a proof of anything uniform.

A variant drops `a_ℓ = 0` and uses `p ∣ gcd(a_ℓ, ℓ + 1)`. This always has Kolyvagin primes for
each `p` by Chebotarev. But `|a_ℓ| < 2√ℓ` limits the simultaneous breadth to
`gcd(a_ℓ, ℓ + 1) < 2√ℓ`, and the trace term `a_ℓ y_1` reappears in Lemma 1. The
`a_ℓ = 0` choice is exactly what makes Lemma 1 exact for all divisors of `ℓ + 1`.

## 6. The two-excess-direction test and what would be needed

Suppose `Sha(E/ℚ)[p] ≅ (ℤ/p)²` at some admissible `p`. Then, by the contrapositive of Lemma 3,
`P_ℓ ∈ pE(H_ℓ)` for every `ℓ` of Lemma 2 with `p ∣ ℓ + 1`. Nothing proved here or in the record
contradicts this. Lemma 1 holds for divisible points too, and Prop. 4 shows heights are
blind to it. The arithmetic property of the real source that would exclude the excess is a
mod-`(ℓ + 1)` formula for the class of `D_ℓ y_ℓ` in `E(H_ℓ)/(ℓ + 1)`, through a quantity with
independent control.

**First remaining equation.** Find an independently controlled `A(ℓ) ∈ ℤ/(ℓ + 1)` with
`(class of P_ℓ in E(H_ℓ)/p) ≠ 0 ⇐ A(ℓ) ≢ 0 (mod p)`, uniformly in `p ∣ ℓ + 1`.

The natural candidate is the first-order coefficient of the Heegner Mazur–Tate element
`θ_ℓ ∈ ℤ[G_ℓ]` modulo `I_G²`, where `I_G` is the augmentation ideal. Its comparison with the
derived class is the Bertolini–Darmon refined (Mazur–Tate type) conjecture for Heegner points.
At level `ℓ` with `a_ℓ = 0` that comparison is again an open rank-two statement. The run did
not prove it. A proof would also need to show that `A(ℓ)` is not merely `#Sha`-weighted, to
avoid recreating the record's uncontrolled scalar `C_p` (W06).
