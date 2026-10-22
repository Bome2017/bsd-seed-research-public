# Eleventh addendum — ARS validated, Vatsal 2.7 ruled out, and `(D1)` reduced to one proved parity

**Tier: SOURCE-AUDIT OUTCOMES (operator-retrieved) + ONE REDUCTION PROVED HERE.** No research object
launched, no Codex or Aristotle run, no finite-level computation, no retrieval performed by this object.
Prior objects unmodified and byte-identical: `ac82f3ad…`, `d5888b62…`, `82b6730f…`, `81ac107b…`,
`35f21882…`, `0bfb6b5e…`, `3eb98a60…`, `da70ec51…`, `c1a6f8ea…`, `b7ebbf00…`, `8af7a2a5…`, `afae7941…`.

`ADDENDUM_010` recorded that the route's two ends each rested on a paper absent from this corpus. The
operator has now retrieved and audited both. The outcome is asymmetric.

## 1. Agashe–Ribet–Stein — VALIDATED, and applicable at `r = 2`

Recorded from the operator's retrieval and direct audit of *Agashe–Ribet–Stein, "The Modular Degree,
Congruence Primes, and Multiplicity One"*. **The source is not in this corpus and was not re-read here**;
what is recorded is the audit as reported, with its specific locations:

* the paper's setup takes a prime `r` with `r² ∤ N`;
* **Proposition 5.14**: for a maximal Hecke ideal `𝔪` of residue characteristic `r` with `r | N`, if `U_r`
  acts by a nonzero scalar on the `𝔪`-part of the regular differentials, the `q`-expansion map is
  injective there;
* **Lemma 5.17**: under the same hypothesis, `dim_{T/𝔪} H⁰(X₀(N)_{F_r}, Ω)[𝔪] ≤ 1`, **with no odd-`r`
  restriction in the statement**;
* the proof of **Proposition 5.10** notes that for a newform with `r | N` one has `U_r = ±1`, hence a
  nonzero scalar on the relevant mod-`r` differential space — and in characteristic 2, `±1 = 1`, still
  nonzero;
* the proof uses the `r ‖ N` special fibre directly: two copies of `X₀(N/r)`, swapped by `W_r`, with the
  `U_r`-relation propagating vanishing from the component containing `∞` to the other, then to the
  exceptional `P¹`s.

Applied at `r = 2`, `N = 2p` — where `4 ∤ N` and the H41 newform has `a₂ = 1`, so `U₂f = f` —

    (D)   dim_{F₂} H⁰(X₀(2p)_{F₂}, Ω)[𝔪] ≤ 1.

**Tier: VERIFIED BY THE OPERATOR AGAINST THE SOURCE, APPLICABLE AT 2.** This supersedes
`ADDENDUM_010` §4's classification of `(D)` as unverified. `ADDENDUM_010` is not modified; it correctly
recorded the state of knowledge at its sealing.

## 2. Vatsal 1999, Theorem 2.7 — RULED OUT for H41, and the reason unifies both Vatsal failures

Recorded from the operator's retrieval of *V. Vatsal, "Canonical Periods and Congruence Formulae"* (Duke
Math. J. 98 (1999) no. 2), the paper identified in `ADDENDUM_010` §4 as the home of the étale
multiplicity-one Theorem 2.7. Again the source is not in this corpus. The audit as reported:

* the relevant second case concerns a `p`-stabilized newform of level `Np`, but **requires the two
  characters `ξ₁, ξ₂` of the residual semisimplification to be distinct on the decomposition group `D_p`**;
* case 1 is `Γ₀(q)` at **prime** level, whereas our level is `2p`;
* case 3 is `Γ₁(N)` with residue characteristic **prime to `N`**, whereas `2 | N`;
* the paper's weight-two Eisenstein congruence theorem assumes `p ≥ 3`.

    [Vat99] Theorem 2.7 does NOT supply (E) for H41.

**This project can corroborate the decisive reason from material already frozen here.** The proof of
Vatsal 2003 Proposition 5.3, quoted verbatim in `ADDENDUM_009` §1, states that the composition factors of
`E₀[ℓ]` carry the characters `χ` and `χ⁻¹ω` for the Teichmüller character `ω`, and notes parenthetically
that `χ = 1` when `E₀` is semistable. At `ℓ = 2` the Teichmüller character is trivial and our curves are
semistable, so **both characters are trivial**: the residual semisimplification is `1 ⊕ 1` and
`ξ₁|_{D₂} = ξ₂|_{D₂} = 1`. The load-bearing hypothesis of Theorem 2.7's second case therefore fails, for a
reason visible in the corpus.

**The two Vatsal failures are one phenomenon.** `ADDENDUM_009`'s blocker was the collapse of the `±`
complex-conjugation eigenspaces (`+1 = −1` over `F₂`); this one is the coalescence of `ξ₁` and `ξ₂`
(trivial mod-2 cyclotomic character). Both are the same characteristic-2 degeneracy of the residual
representation, met at two different points of the argument. Recorded because it explains why patching one
would not have helped the other.

## 3. `(D1)` — REDUCED here to a single parity, which is already proved

`computation/verify_D1_inputs.py`, receipt `receipts/D1_INPUTS.txt`. Symbolic in `p`.

`d log F_p` has at worst simple poles at the zeros and poles of `F_p`, with residue the multiplicity
there. So the whole obstruction to regularity is residues, and the local analysis splits three ways. **The
finding is that only one of the three carries any arithmetic condition.**

**(a) Smooth point of a vertical component.** The special fibre is the divisor `(2)`; at a smooth point of
a multiplicity-one component `2` is a uniformizer, so `F_p = 2^a·u` with `u` a unit. Since `2` is a base
constant, `d(2) = 0` in **relative** differentials, so `d log F_p = du/u`, regular. **No condition on `a`.**

**(b) Node, local equation `xy = 2`.** Differentiating the base constant gives `x dy + y dx = 0`, so
`dx/x = −dy/y`, and that element generates the relative dualizing sheaf `ω` at the node. With
`F_p = x^a y^b u`, `d log F_p = (a−b) dx/x + du/u`, a section of `ω` for **any** integers `a, b`. **No
condition on `a, b`.**

**(c) Horizontal cusp section, `F_p = t^M u`.** `d log F_p = M dt/t + du/u`, residue `M`. **This is the
only case carrying a condition, and it is exactly `2 | M`.**

`F_p` is a modular unit with `div(F_p) = k([0] − [∞])`, `k = (p²−1)/8`, so only two of the four cusps are
involved and the residues are `±k`. Cross-checked independently from the `q`-expansion: `Σ d·r_F =
−3(p²−1)`, leading exponent `−k`, confirming `ord_∞(F_p) = −k` and `ord_0(F_p) = +k`. And

    v₂(k) = v₂(p²−1) − 3 = (1+n) − 3 = n−2 = m ≥ 3,

so both residues vanish mod 2 **with room to spare — `8 | k`, not merely `2 | k`**, uniformly in `p`.

    CONSEQUENCE.  (D1) does not depend on the vertical multiplicities of div(F_p), nor on the
    nodal branch multiplicities, nor on the exceptional P¹'s from regular resolution.  None of
    those impose a parity condition.  (D1) reduces to the single statement that every HORIZONTAL
    residue of d log F_p is even — which is proved, uniformly, with a margin of 2^(m-1).

**What remains in `(D1)` is therefore model-theoretic bookkeeping, not arithmetic:**

1. that `F_p`'s divisor on the minimal regular model is (horizontal cusp part) + (vertical part) with no
   other support;
2. that the horizontal cusp sections are disjoint and meet the special fibre at smooth points of
   multiplicity-one components, so that (c) is the correct local picture;
3. that `ω_η` is integral as a section of `ω(H)` over `Z₂`, so "reduce mod 2" is defined and residue
   formation commutes with reduction.

Item 3 is supported at `∞` by the integral `q`-expansion `F_p = q^{−k}(1 + O(q))`, giving
`ω_η = Θ_p·dq/q` with `Θ_p` integral — the same `Θ_p` as in `(B)`. Items 1–2 are Deligne–Rapoport model
facts and are **not established here**. `(D1)` remains **OPEN**, but its open part no longer contains any
arithmetic risk: no parity can fail, so `(D1)` cannot die on the 2-adic side.

## 4. The architecture as it now stands

    (B)    Θ_p ≡ f_H41 (mod 2)                      PROVED, symbolic, uniform    [ADDENDUM_005]
    (D2)   W₂*(ω̄_η) = ω̄_η                           PROVED, symbolic, uniform    [ADDENDUM_010]
    (D)    dim H⁰(X₀(2p)_{F₂},Ω)[𝔪] ≤ 1             VERIFIED vs source, applies at 2   [§1]
    (D1)   ω̄_η ∈ H⁰(X₀(2p)_{F₂}, ω)                 OPEN — model bookkeeping only  [§3]
    (D3)   ω̄_η = ω̄_f                                follows from B + D1 + D2 + ARS
    (D3) ⟹ (C)                                      THE GAP.  Not supplied by [Vat99] 2.7  [§2]
    (C)    χ_p = α_p (mod 2)                         the target
    (X)    T_p ∈ π̂(E₀)[2]                            unproved                     [ADDENDUM_009]
    uniform optimality E₀ = E                        open; B position still live
    positive branch                                  entirely outside this architecture

`(E)` as previously formulated is withdrawn as a literature appeal: the theorem named for it does not
apply. The passage `(D3) ⟹ (C)` is now explicitly a statement about the integral / finite-flat 2-torsion
realisation, with no citation standing behind it.

## 5. What this object does and does not claim

It claims: `(D1)`'s arithmetic content is discharged and cannot fail; the remaining part of `(D1)` is
model-theoretic. It records, on the operator's audit rather than this project's reading, that `(D)` is
legitimate at 2 and that `[Vat99]` 2.7 is not. It corroborates the second from frozen material.

It does **not** claim `(D1)`, `(D3)`, `(C)`, or the seed. It does not re-derive ARS. If `(D1)`'s
model-theoretic part fails, the differential route dies cleanly, as intended.

**The H41 seed remains unproved.**
