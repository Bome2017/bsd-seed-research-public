# Third addendum — the four corrections, and the containment test actually run

**Tier: COMPUTATION at two levels, plus recorded corrections.** Not a proof of the H41 seed, not a
proof of the identification, not a certification. No prior object is reopened:
`CODEX_H41_SEED_RESEARCH_FREEZE_001` (`ac82f3ad…`), `H41_SEED_FREEZE_ADDENDUM_001` (`82b6730f…`) and
`H41_ETA_CHARACTER_ATTEMPT_ADDENDUM_002` (`81ac107b…`) are unmodified.

## 1. Why this was not an Aristotle job

Aristotle is a Lean proof-search service. There is no Lean statement here to prove: the deliverable is
a pass/fail computation with a certificate, and even a pass at finitely many levels is a diagnostic
rather than a theorem. The programme's own sequencing rule is that Aristotle comes **after** an
ordinary mathematical proof exists. Further, the identification, if ever proved, is conventional
mathematics about modular curves — `J₀(N)`, cuspidal divisor classes, Eisenstein theory — none of
which exists in the frozen certified base, which has deliberately kept modular curves out of scope.
Commissioning a proof search here would have been a category error.

The computation was done locally with the source-built PARI/GP 2.17.4 already recorded in
`CODEX_ANALYTIC_H41_RESEARCH_FREEZE_001` (binary digest `ccdb2f08…`) plus exact Python arithmetic.

## 2. Four corrections, recorded

**C1 — my divisor-order inference was invalid.** I wrote that a modular unit with divisor `M·c` must
have `M` equal to the order of `c`. That is false: existence of such a unit gives only

    ord(c) ∣ M

and squaring any unit doubles the multiplicity without changing `ord(c)`. Exactness here comes from the
separately established cusp-order theorem, which was verified independently in
`CODEX_H41_SEED_RESEARCH_FREEZE_001` — and which does give `ord(c) = (p²−1)/8`. So the conclusion
survives; my route to it did not. Without exactness, `T_p = (M/2)c` could be zero; with it, `T_p` is
nonzero of exact order two. The nonvanishing `χ_p({0,1/3}) = 1` gives a second, independent reason the
double cover is nontrivial.

**C2 — the containment is equivalent to the character equality, not weaker.** With
`ρ : L → U₀/2U₀` surjective (the modular parametrization is surjective on `H₁`, and the remaining maps
are quotients):

    ker ρ ⊆ ker χ_p   ⟺   χ_p = α_p mod 2

Forward: the containment makes `χ̄_p(ρ(x)) = χ_p(x)` well defined on all of `U₀/2U₀`; it is nonzero
because `χ_p` is; and `U₀/2U₀ ≅ F₂` has exactly one nonzero character. Converse is immediate. So it is a
reformulation, and the whole unproved comparison is still present. My "reduction in shape, not in
difficulty" was the right hedge but the wrong word — "equivalent reformulation" is correct.

**C3 — the Jacobian statement is a pullback, and contravariance matters.** With
`φ : X₀(2p) → E₀` the ∞-based modular parametrization and `S₀ ∈ Pic⁰(E₀)[2]` the class of the nonzero
character of `U₀/2U₀`, the character equality is equivalent to

    T_p = φ* S₀   in   Pic⁰(X₀(2p))[2]

This is **not** established by showing the forward quotient sends `T_p` to zero, and showing `T_p`
comes from *some* elliptic 2-torsion class would not identify the required one. My earlier phrasing
"test whether pairing against `T_p` kills it" was vaguer than this and should be read as superseded.

**C4 — factorization cannot hold when `a = 1`, so it is strictly stronger than the seed.** If `a = 1`
then `u₃ ∈ 2U₀`, so `ρ(η₃) = 0`, while `χ_p(η₃) = 1`. Hence `η₃` itself witnesses

    ker ρ ⊄ ker χ_p     whenever a = 1

Consequences, which must not be blurred:

* factorization holding ⟹ `a = 0` at that level, and then the required oddness follows;
* factorization failing does **not** refute the seed — the seed can hold with `a = 1`, or with `a = 0`
  and a different elliptic character;
* uniform factorization would therefore be a **sufficient theorem strictly stronger than the seed**,
  since it additionally excludes the `a = 1` optimal-period position. It is not an equivalent
  characterization of the negative-branch seed.

## 3. The test, run at both available levels

Specification followed: compute `χ_p` and `α_p mod 2` on cycles, with `α_p` from the primitive integral
lattice and **not** normalized using the known central value; return either agreement with evidence, or
an explicit witness `x` with `ρ(x) = 0`, `χ_p(x) = 1`.

`χ_p(γ) = W(γ) mod 2`, where `W` is the logarithmic winding computed from exact Dedekind sums. `W` is a
homomorphism `Γ₀(N) → ℤ` — for `γ, δ`, `log f(γδz) − log f(z)` splits as the sum of the two increments
— so `χ_p` is a character, computed independently of PARI and of any symbol normalization.

`α_p` comes from `msfromell`, evaluated on the cycle `{0, γ(0)}`, divided by its gcd over the sample.

### Result

    N = 62,  p = 31      1338 cycles   c ∈ {62,124,186,248}     α even/odd  873/465   agree 1338/1338   DISAGREEMENTS 0
    N = 254, p = 127     1367 cycles   c ∈ {254,508,762,1016}   α even/odd  922/445   agree 1367/1367   DISAGREEMENTS 0

**The test returns `c = v` at both levels, non-vacuously.** Non-vacuity matters: both parities occur in
quantity, so `ker ρ` genuinely meets the sample and agreement is not automatic. No witness against the
containment exists in either sample.

Two robustness facts:

* At `N = 62` the comparison was run against **all four curves** of the rational isogeny class. The gcd
  differs between them — `1/2, 1, 1, 2` — but the normalized parity pattern is identical, and all four
  give 0 disagreements. The parity is a property of the cycle lattice, not of which curve is chosen.
* Widening the `N = 62` sample from 226 to 1425 cycles left the gcd unchanged at `1/2` and the
  disagreement count at 0.

### The normalization question, and how it was settled

The frozen report warned that the primitive generator of `U₀ = H₁/ker(1+τ)` must not be replaced by a
generator of the plus eigensublattice. The `msfromell` symbol `xs` is not integrally normalized — it
takes the value `−1/4` on `[0,∞]` and `−1/2` on `{0,1/3}` — so the warning was live.

`computation/norm62.gp` settles it. Solving `L·co = xs` for PARI's integral lattice `L = mslattice(M)`
of rank 14 gives coordinates with denominators dividing 2, and

    2·co = [5, 0, 0, −19, 0, −1, 0, 14, −15, −19, 0, 0, 0, 20]

is integral with gcd 1. So `2·xs` lies in the integral lattice and is a **primitive** vector of it,
while `xs` does not lie in the lattice. Since the gcd over cycles is `1/2`, dividing by it multiplies by
exactly 2 — so the normalization used **is** the primitive integral one, and `α_p = mseval(M, 2·xs, ·)`.

**Residual, stated precisely.** What remains unverified is a PARI-semantics question, not a vague worry:
whether `mslattice` on this space is the `U₀` lattice rather than the plus eigensublattice. The two can
differ by index 2, and if they do, the parities invert wholesale and the test would fail rather than
pass. I did not independently establish which lattice PARI returns, and I will not bluff it. Anyone who
can settle that one documented question converts this result from conditional to unconditional.

### What the result does not establish

* **Not the identification.** Two levels are a diagnostic. The comparison for symbolic `p = 2^n − 1`
  is unproved, and by C2 it is equivalent to the full character equality — so nothing here is weaker
  than the original obstruction.
* **Nothing about `a = 1`.** Both test levels have `a = 0`, since `h = 1` was established at the first
  five conductors. By C4 the factorization must fail wherever `a = 1`, and whether that case occurs is
  unknown.
* **Nothing about `p = 8191` or beyond.** `N = 16382` was not attempted.
* **No proof of the seed.** Agreement at two `a = 0` levels reproduces facts already known there from
  `λ = 1/4` and `λ = 3/4`. Its value is as a test of the *mechanism*, which is what the test was for.

## 4. Status — unchanged

    negative branch   u₃ ∈ 2^a U₀             PROVED
                      u₃ ∉ 2^(a+1) U₀         OPEN
    identification    χ_p = α_p mod 2         passes at N = 62, 254; UNPROVED in general
    a = 1 case        factorization fails there by C4; occurrence unknown
    positive branch   OPEN, additional period and numerator ambiguity

**The H41 seed remains unproved.** The candidate mechanism now has a concrete pass at both available
levels and a precisely stated residual. No gate, no new bottleneck, no run authorised.
