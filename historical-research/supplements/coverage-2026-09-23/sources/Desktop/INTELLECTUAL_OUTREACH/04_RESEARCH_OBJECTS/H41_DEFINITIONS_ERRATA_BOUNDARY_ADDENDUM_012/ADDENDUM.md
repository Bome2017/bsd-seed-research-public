# Twelfth addendum — definitions, errata and boundaries, frozen before the `(D3) ⟹ (C)` attack

**Tier: DEFINITION / ERRATA / BOUNDARY OBJECT. Not a proof attempt.** No new mathematics is claimed. No
research object launched, no Codex or Aristotle run, no computation beyond mechanical text extraction.
Prior objects unmodified and byte-identical: `ac82f3ad…`, `d5888b62…`, `82b6730f…`, `81ac107b…`,
`35f21882…`, `0bfb6b5e…`, `3eb98a60…`, `da70ec51…`, `c1a6f8ea…`, `b7ebbf00…`, `8af7a2a5…`, `afae7941…`,
`a2667972…`.

**Purpose.** To prevent a corrected theorem from being proved and then attributed to an imprecise sealed
statement. Every block marked **Verbatim** below was extracted mechanically from the sealed file named on
its marker line; `computation/verify_verbatim_blocks.py` re-reads each source and confirms the block
matches its lines byte for byte (`receipts/VERBATIM_VERIFICATION.txt`). Nothing inside a Verbatim block is
paraphrased. Text outside the blocks is this object's own.

## 1. Errata to ADDENDUM_011 — preserved byte-for-byte, operational reading superseded

`H41_D1_REDUCTION_ADDENDUM_011` (`a2667972…`) is **not modified**. Two of its sentences overstate; their
operational interpretation is superseded here.

### 1.1 The D1 overstatement

**Verbatim** — `H41_D1_REDUCTION_ADDENDUM_011/ADDENDUM.md` lines 110-111
```text
facts and are **not established here**. `(D1)` remains **OPEN**, but its open part no longer contains any
arithmetic risk: no parity can fail, so `(D1)` cannot die on the 2-adic side.
```

**Verbatim** — `H41_D1_REDUCTION_ADDENDUM_011/README.md` lines 28-29
```text
the integral `q`-expansion `q^{−k}(1+O(q))`). **`(D1)` stays OPEN but can no longer die on the 2-adic
side.**
```

**Superseding operational interpretation:**

    (D1) has no remaining valuation/parity obstruction.

**Characteristic-2 special-fibre and geometric pathologies have NOT been excluded.** `ADDENDUM_011` §3
removes dependence on vertical valuations, nodal branch multiplicities and resolution multiplicities. It
does not show that the local expressions glue or extend on the chosen model, that the cusp sections behave
as required, or that `ω_η` lies in the specified integral lattice `ω(H)`. A failure of any of those could
itself be a characteristic-2 phenomenon without being a parity obstruction.

This sentence of the same object is **consistent** with the corrected reading, because it is confined to
arithmetic content, and is **not** superseded:

**Verbatim** — `H41_D1_REDUCTION_ADDENDUM_011/ADDENDUM.md` lines 132-133
```text
It claims: `(D1)`'s arithmetic content is discharged and cannot fail; the remaining part of `(D1)` is
model-theoretic. It records, on the operator's audit rather than this project's reading, that `(D)` is
```

### 1.2 The finite-flat overstatement

**Verbatim** — `H41_D1_REDUCTION_ADDENDUM_011/ADDENDUM.md` lines 126-128
```text
`(E)` as previously formulated is withdrawn as a literature appeal: the theorem named for it does not
apply. The passage `(D3) ⟹ (C)` is now explicitly a statement about the integral / finite-flat 2-torsion
realisation, with no citation standing behind it.
```

The first clause — withdrawal of `(E)` as a literature appeal — stands. The second clause is
**superseded**: `(D3) ⟹ (C)` has **not** been established to be a statement about an integral or
finite-flat 2-torsion realisation. No carrier of any kind has been specified (§5), and a finite-flat
carrier is specifically not endorsed (§6.2).

## 2. Canonical definitions of `(C)` and `(D3)` — verbatim, not paraphrased

Recorded as sealed. They are **not** rewritten into any repaired architecture here.

### 2.1 `(C)`

**Verbatim** — `H41_ETA_CONGRUENCE_ADDENDUM_005/ADDENDUM.md` lines 58-60
```text
## 3. The exact remaining comparison

    (C)    χ_p = α_p mod 2
```

and its sealed status rows (the second row is taken up in §3):

**Verbatim** — `H41_ETA_CONGRUENCE_ADDENDUM_005/ADDENDUM.md` lines 176-177
```text
    (C) χ_p = α_p mod 2                           OPEN; forced at N=62, tested at N=254 only
    (C′) T_p = π̂(S₀)                              OPEN, equivalent to (C)
```

**Recorded classification: `(C)` is a Betti-character statement** — an equality of two `F₂`-valued
characters on `H₁(X₀(2p)(ℂ), ℤ)`. The basis for that classification, verbatim.

On the negative branch the level is `N = 2p`:

**Verbatim** — `H41_ETA_CHARACTER_ATTEMPT_ADDENDUM_002/ADDENDUM.md` lines 23-23
```text
For `p = 2^n − 1` a Mersenne prime with `n ≥ 5` and `N = 2p`:
```

`χ_p` is a character on integral homology of the compact curve:

**Verbatim** — `H41_ETA_CHARACTER_ATTEMPT_ADDENDUM_002/ADDENDUM.md` lines 31-32
```text
Because every divisor order is even, `√f_p` gives an unbranched double cover; its monodromy is an
`F₂`-character `χ_p` on integral homology. With `γ_p = [[(2p+1)/3, 1],[2p, 3]] ∈ Γ₀(N)` sending
```

**Verbatim** — `H41_ETA_CHARACTER_ATTEMPT_ADDENDUM_002/01_attempt/PROOF_ATTEMPT.md` lines 51-55
```text
Thus div(f_p)=k([0]-[infinity]), k=(p^2-1)/8.
For the negative H41 parameters v_2(k)=n-2>=3, so all divisor orders
are even. The square-root extension has no ramification at the cusps;
there are no interior zeros or poles. Its analytic continuation defines
a sign character on the compact curve's integral homology.
```

`α_p` is a pullback to integral homology of `X₀(N)`:

**Verbatim** — `H41_ETA_CHARACTER_ATTEMPT_ADDENDUM_002/01_attempt/PROOF_ATTEMPT.md` lines 94-96
```text
Let alpha_p be the pullback, to integral homology of X_0(N), of the primitive
integer functional on the actual U_0 lattice. Then
alpha_p({0,1/3})=w_3.
```

The objects `E₀`, `π`, `τ`, `H₀`, `U₀`, `h`, `a` that `α_p` depends on:

**Verbatim** — `CODEX_H41_SEED_RESEARCH_FREEZE_001/02_stage_II/STAGE_II_COMPARISON.md` lines 52-58
```text
**THEOREM — verified deduction.** Let E0 be the actual connected optimal quotient of J0(N), π its quotient map composed with the infinity-based Abel–Jacobi map, τ complex conjugation, and

\[
H_0=H_1(E_0(\mathbb C),\mathbb Z),\quad
U_0=H_0/\ker(1+\tau),\quad
h=\Omega_{0,\mathbb R}/\Omega_{E,\mathbb R},\quad a=-v_2(h).
\]
```

including the chosen primitive orientation of `U₀` — the datum that fixes the sign of `α_p`:

**Verbatim** — `CODEX_H41_SEED_RESEARCH_FREEZE_001/01_stage_I/STAGE_I_RECONSTRUCTION.md` lines 149-162
```text
**THEOREM — definition independent of an L-value evaluation.** Let \(H_0=H_1(E_0(\mathbb C),\mathbb Z)\), let \(\tau\) be complex conjugation, and define the torsion-free rank-one lattice

\[
U_0=H_0/\ker(1+\tau).
\]

For an odd good prime \(\ell\), put

\[
\eta_\ell=\sum_{j=1}^{(\ell-1)/2}\{0,j/\ell\}\in H_1(X_0(N),\mathbb Z),\qquad
u_\ell=[\pi_*\eta_\ell]\in U_0.
\]

Each path is a closed cycle on the modular curve because both endpoints represent the same cusp when \((\ell,N)=1\). Choose the primitive real orientation of \(U_0\) and let \(w_\ell\in\mathbb Z\) be the coordinate of \(u_\ell\). This normalization uses an integral lattice, not the desired central value.
```

The correct integral home of `α_p` — plus **cohomology**, not plus homology:

**Verbatim** — `H41_ETA_EXTERNAL_CHECK_ADDENDUM_004/ADDENDUM.md` lines 53-61
```text
The correct comparison is obtained by dualizing. With `π : J₀(N) → E₀` the connected optimal quotient,
connectedness of the kernel gives a surjection on integral homology, so

    π* : H¹(E₀,ℤ) ↪ H¹(X₀(N),ℤ)   is saturated,

and inside the rational newform plane, taking the integral lattice and then its plus eigenline gives
`π* Hom(U₀,ℤ)`. The elementary identity that makes this work:

    Hom(U₀,ℤ) = H¹(E₀,ℤ)^{τ=1}
```

A normalization-free formula for `χ_p`:

**Verbatim** — `H41_ETA_CHARACTER_TEST_ADDENDUM_003/ADDENDUM.md` lines 76-78
```text
`χ_p(γ) = W(γ) mod 2`, where `W` is the logarithmic winding computed from exact Dedekind sums. `W` is a
homomorphism `Γ₀(N) → ℤ` — for `γ, δ`, `log f(γδz) − log f(z)` splits as the sum of the two increments
— so `χ_p` is a character, computed independently of PARI and of any symbol normalization.
```

An equivalent form of `(C)` that **is** argued in both directions in the sealed record, recorded for
contrast with §3:

**Verbatim** — `H41_ETA_CHARACTER_TEST_ADDENDUM_003/ADDENDUM.md` lines 35-42
```text
**C2 — the containment is equivalent to the character equality, not weaker.** With
`ρ : L → U₀/2U₀` surjective (the modular parametrization is surjective on `H₁`, and the remaining maps
are quotients):

    ker ρ ⊆ ker χ_p   ⟺   χ_p = α_p mod 2

Forward: the containment makes `χ̄_p(ρ(x)) = χ_p(x)` well defined on all of `U₀/2U₀`; it is nonzero
because `χ_p` is; and `U₀/2U₀ ≅ F₂` has exactly one nonzero character. Converse is immediate. So it is a
```

### 2.2 `(D3)`

`(D3)` is stated in `ADDENDUM_010` §1, in a block that must be read together with its neighbours:

**Verbatim** — `H41_MOD2_DIFFERENTIAL_ROUTE_ADDENDUM_010/ADDENDUM.md` lines 13-19
```text
    (D)   ARS: for a maximal Hecke ideal of residue characteristic 2 with 2 ‖ N, if U_2 acts by a
          nonzero scalar on the m-part of the regular differentials, then
              dim_{F_2} H^0(X_0(N)_{F_2}, Ω)[m] ≤ 1.
    (D1)  ω̄_η ∈ H^0(X_0(2p)_{F_2}, Ω)   for  ω_η = d log F_p.
    (D2)  W_2^*(ω̄_η) = ω̄_η.
    (D3)  ω̄_η = ω̄_f  as global regular dualizing differentials mod 2.
    (E)   the relevant ordinary Eisenstein étale line is one-dimensional.
```

**Verbatim** — `H41_MOD2_DIFFERENTIAL_ROUTE_ADDENDUM_010/ADDENDUM.md` lines 21-21
```text
with `(D3) + (E)` the candidate route to `(C)`. Tier: **PROPOSED**, except where stated below.
```

**Its hypotheses are stated in three places, and the three lists are not identical.**

**Verbatim** — `H41_MOD2_DIFFERENTIAL_ROUTE_ADDENDUM_010/ADDENDUM.md` lines 116-120
```text
Granted `(D1)`, `(D2)` and `(D)`, the argument sketched is: `(B) Θ_p ≡ f (mod 2)` — already proved
symbolically and frozen in `ADDENDUM_005` — makes `δ := ω̄_η − ω̄_f` have zero `q`-expansion at `∞`; the
`q`-expansion vanishing kills `δ` on the component containing `∞`; `(D2)` and `W₂`'s interchange of the
two main components carry that to the other; the remaining exceptional `P¹`s are killed the same way.
That would give `(D3)`, a uniform theorem-level step rather than another finite example.
```

**Verbatim** — `H41_MOD2_DIFFERENTIAL_ROUTE_ADDENDUM_010/ADDENDUM.md` lines 131-131
```text
    (D3)   PROPOSED, conditional on (D), (D1), (D2) and the special-fibre description.
```

**Verbatim** — `H41_D1_REDUCTION_ADDENDUM_011/ADDENDUM.md` lines 119-119
```text
    (D3)   ω̄_η = ω̄_f                                follows from B + D1 + D2 + ARS
```

Recorded differences:
* `ADDENDUM_010` §5 grants `(D1)`, `(D2)`, `(D)`, and uses `(B)` in its argument without listing it;
* `ADDENDUM_010` §6 adds "the special-fibre description";
* `ADDENDUM_011` lists `B`, `D1`, `D2`, `ARS`, omits the special-fibre description, **and restates `(D3)`
  without the qualifier "as global regular dualizing differentials mod 2"** carried by `ADDENDUM_010` line 18.

**No single canonical hypothesis list for `(D3)` exists in the sealed record.** None is designated
canonical here. Any use of `(D3)` must discharge the union: `(B)`, `(D)`, `(D1)`, `(D2)`, and the
special-fibre description. The objects occurring in `(D3)` — `ω̄_η`, `ω̄_f`, and "global regular
dualizing differentials mod 2" — carry the specification defects frozen in §4.

## 3. `(C) ⟺ (C′)` — UNPROVED IN THE SEALED RECORD

The equivalence is asserted, not argued. The assertion, verbatim — together with the second status row
quoted in §2.1 ("OPEN, equivalent to (C)"):

**Verbatim** — `H41_ETA_CONGRUENCE_ADDENDUM_005/ADDENDUM.md` lines 62-66
```text
equivalently, in the Jacobian, with `J = J₀(2p)`, `T_p = ((p²−1)/16)·([0]−[∞]) ∈ J(ℚ)[2]` the class cut
out by `√F_p`, `π : J → E₀` the connected optimal quotient, `π̂ : E₀ ↪ J` its dual embedding, and
`S₀ ∈ E₀(ℚ)[2]∖{0}` the class of the primitive character `α_p mod 2`:

    (C′)   T_p = π̂(S₀)   in   J₀(2p)[2]
```

**Verbatim** — `H41_ETA_CONGRUENCE_ADDENDUM_005/README.md` lines 10-12
```text
**The exact remaining comparison:** `(C) χ_p = α_p mod 2`, equivalently `(C′) T_p = π̂(S₀)` in
`J₀(2p)[2]`. The sufficient criterion `(L) J₀(2p)(ℚ)[𝔪] = 𝔽₂T_p` is labelled sufficient and **stronger
than the seed**, not equivalent to it.
```

**Status: `(C) ⟺ (C′)` is UNPROVED IN THE SEALED RECORD, and is withdrawn as a proved dependency.** No
section of any sealed object argues it. Contrast the containment form at the end of §2.1, which is argued.

**The rationality clause cannot be part of the definition.** The block above writes
`S₀ ∈ E₀(ℚ)[2]∖{0}` (`ADDENDUM_005` line 64). A 2-torsion point attached to the character `α_p mod 2` is
not a priori rational, so that clause cannot be part of the definition of `(C′)` unless separately
justified. A route by which rationality would follow — **after** `T_p = π̂(S₀)` is proved, from the
rationality of `T_p` — is recorded as a candidate in §6.1.

Downstream objects that adopted `(C′)` as the target, recorded so that nothing is later attributed to them
as though the equivalence were proved. Neither is modified:

**Verbatim** — `H41_LAMBDA_RELABEL_AND_C_PRIME_TARGET_ADDENDUM_008/ADDENDUM.md` lines 137-139
```text
Accordingly `(L)` is **retired as the object of proof** and `(C′)` replaces it:

    (C′)      T_p = π̂(S₀)     in  J₀(2p)[2].
```

**Verbatim** — `H41_VATSAL_ELL2_WITHDRAWN_ADDENDUM_009/ADDENDUM.md` lines 138-142
```text
Even granted `(X)`, in an optimal position carrying several real 2-torsion lines one must still verify
that the corresponding Kummer/Betti character is the **particular primitive character** `α_p`. So the
safest ultimate target remains unchanged:

    (C)      χ_p = α_p (mod 2).
```

`ADDENDUM_009` §5 had already restored `(C)` as the safest target. The implication `(L) ⟹ (C′)` in
`ADDENDUM_005` §4 is **unaffected** — it is an implication into `(C′)`, not the equivalence:

**Verbatim** — `H41_ETA_CONGRUENCE_ADDENDUM_005/ADDENDUM.md` lines 83-84
```text
**(L) ⟹ (C′):** `T_p ≠ 0`; `π̂(S₀) ≠ 0` because the dual of an optimal quotient is an embedding; both
are rational `𝔪`-torsion; and (L) leaves exactly one nonzero such point. So they coincide.
```

## 4. Three specification defects around `(D)`, `(D1)`, `(D3)` — frozen, with a usage prohibition

**(a) `ω̄_f` is undefined.** It occurs in `(D3)` (§2.2, `ADDENDUM_010` line 18), in the §5 argument
(§2.2, `ADDENDUM_010` line 117), in the `ADDENDUM_011` restatement (§2.2, line 119), and here:

**Verbatim** — `H41_MOD2_DIFFERENTIAL_ROUTE_ADDENDUM_010/ADDENDUM.md` lines 66-67
```text
Consistent with, and unchanged by, this: the H41 newform has `a₂ = 1`, so `W₂f = −f`, hence
`W₂ω̄_f = ω̄_f` mod 2. Both differentials carry the same `W₂`-symmetry.
```

Nowhere is it defined. The only differential normalization in the entire sealed record concerns the
**period**, not a section on `X₀(2p)`:

**Verbatim** — `CODEX_H41_SEED_RESEARCH_FREEZE_001/02_stage_II/STAGE_II_COMPARISON.md` lines 26-26
```text
where the period integrates the absolute minimal Néron differential over the **entire** real locus. The withheld record supplies no uniform theorem evaluating the required integral winding class to its exact power of 2. The negative branch's mod-4 formulation remains unproved; the positive branch's additional period and numerator cases remain unproved. No realized H41 counterexample is present.
```

**(b) `Ω` versus `ω` is unresolved.** In the `ADDENDUM_010` §1 block of §2.2, `(D)` (line 15) and `(D1)`
(line 16) are written with `Ω`, while `(D3)` (line 18) speaks of "dualizing differentials". `ADDENDUM_011`
writes `(D)` with `Ω` and `(D1)` with `ω`:

**Verbatim** — `H41_D1_REDUCTION_ADDENDUM_011/ADDENDUM.md` lines 30-32
```text
Applied at `r = 2`, `N = 2p` — where `4 ∤ N` and the H41 newform has `a₂ = 1`, so `U₂f = f` —

    (D)   dim_{F₂} H⁰(X₀(2p)_{F₂}, Ω)[𝔪] ≤ 1.
```

**Verbatim** — `H41_D1_REDUCTION_ADDENDUM_011/ADDENDUM.md` lines 117-118
```text
    (D)    dim H⁰(X₀(2p)_{F₂},Ω)[𝔪] ≤ 1             VERIFIED vs source, applies at 2   [§1]
    (D1)   ω̄_η ∈ H⁰(X₀(2p)_{F₂}, ω)                 OPEN — model bookkeeping only  [§3]
```

The two are never identified, and on a semistable curve they differ at the nodes.

**(c) The integral model is not uniquely fixed.**

**Verbatim** — `H41_MOD2_DIFFERENTIAL_ROUTE_ADDENDUM_010/ADDENDUM.md` lines 78-81
```text
The three local statements — pole loss at a horizontal cusp because `2 | M`, `2^a` killed by relative
differentiation on a vertical component, and `dx/x` being an allowed generator of the dualizing sheaf at a
node `xy = 2` with `d log F_p = (a−b)dx/x + du/u` — are **not verified here**. They are geometry on the
minimal regular semistable model, not arithmetic this object can check. `(D1)` is recorded as a proposed
```

**Verbatim** — `H41_D1_REDUCTION_ADDENDUM_011/ADDENDUM.md` lines 101-102
```text
1. that `F_p`'s divisor on the minimal regular model is (horizontal cusp part) + (vertical part) with no
   other support;
```

**Verbatim** — `H41_D1_REDUCTION_ADDENDUM_011/ADDENDUM.md` lines 109-109
```text
`ω_η = Θ_p·dq/q` with `Θ_p` integral — the same `Θ_p` as in `(B)`. Items 1–2 are Deligne–Rapoport model
```

"Minimal regular semistable model", "minimal regular model" and "Deligne–Rapoport model" are used
interchangeably. The Deligne–Rapoport model and its minimal regular resolution have different special
fibres.

**PROHIBITION.** Until a definition/model-resolution lemma fixes them, none of the following may be used
in any proof of the bridge: the symbol `ω̄_f`; the symbols `Ω` and `ω` as they occur in `(D)`, `(D1)` and
`(D3)`; `X₀(2p)_{F₂}` as an unspecified special fibre. A bridge proof using any of them before that lemma
is sealed is not admissible to the architecture. The lemma must fix, at minimum: the model over `ℤ_(2)`,
and whether statements transfer between it and its resolution; the sheaf, including whether the `Ω` of
`(D)` is the dualizing sheaf; and the normalization and integral structure of `ω_f`, including its link to
`E₀`.

## 5. No integral carrier is part of the theorem architecture — a negative theorem-status fact

    No Néron-model subgroup, finite-flat 2-torsion group scheme, identity-component torsion
    object, component-group extension, or other integral realization has yet been specified
    as the carrier of (D3) ⟹ (C).

Evidence: `computation/audit_integral_carrier.sh` scans every prior H41 addendum and README and the frozen
Stage I and Stage II reports for the vocabulary any such carrier would need; full hit lines are in
`receipts/INTEGRAL_CARRIER_ABSENCE.txt`. It finds four lines in the entire record, and none specifies an
integral object:

* `ADDENDUM_011` line 127 — the sentence superseded in §1.2.
* Stage I line 230 — "identity component" inside the real-period table:

**Verbatim** — `CODEX_H41_SEED_RESEARCH_FREEZE_001/01_stage_I/STAGE_I_RECONSTRUCTION.md` lines 230-230
```text
**THEOREM — full period table.** For an isogeny of differential factor \(c\) with \(k_0\) kernel points in the source identity component,
```

* Stage II lines 28 and 142 — both concern the identity component of the **real locus**, `E₀(ℝ)⁰`:

**Verbatim** — `CODEX_H41_SEED_RESEARCH_FREEZE_001/02_stage_II/STAGE_II_COMPARISON.md` lines 28-28
```text
There is a real, limited theorem-level gain: the withheld Mazur theorem, combined with the frozen local calculations, eliminates all odd-prime isogenies. Consequently the four displayed models form the entire rational isogeny class and the base is the intrinsic minimal-height curve. The real identity component further forces the cusp image to vanish at negative F and positive G, if those are optimal. Together these results prove **4λ∈Z on the negative branch and 8λ∈Z on the positive branch**, where λ=L(E,1)/ΩE,R. In particular, the negative branch's inclusion in 2^aU0 is proved; exclusion from 2^(a+1)U0 is not. This materially simplifies an existing obligation. It does **not** select the modular optimal vertex or determine the required oddness and nonvanishing.
```

**Verbatim** — `CODEX_H41_SEED_RESEARCH_FREEZE_001/02_stage_II/STAGE_II_COMPARISON.md` lines 142-142
```text
**THEOREM — real-component restriction and uniform denominator bound.** The imaginary-axis path from ∞ to 0 is fixed pointwise by the real involution. Its modular image is a continuous real path from O, so the cusp image lies in E0(R)^0. This imposes a restriction missed in the frozen case analysis. At negative F, the three roots are 0<(2√r−1)²<(2√r+1)²; its sole rational involution (0,0) is outside the identity component. Therefore **t=1 if negative F is optimal**. At positive G, the other two roots are positive, so its sole rational involution (0,0) is again outside the identity component; **t=1 if positive G is optimal**. At positive E, the order-four generator (r,r) is on the bounded component, so the identity-component rational torsion has exponent 2 and t≤2.
```

No hit names a Néron model, a finite flat group scheme, a component group, a schematic closure, a
quasi-finite group scheme, or any model over `ℤ_(2)`.

## 6. UNPROVED BRIDGE CANDIDATES — not conclusions, not in the proof graph

### 6.1 The generic-fibre candidate

Schematic shape, as proposed:

    √F_p        ⇝  T_p ∈ J[2],       χ_p(·) = e₂(T_p, ·)
    α_p mod 2   ⇝  π̂(S₀),            S₀ ∈ E₀[2](ℂ)
    (C)  ⟺  T_p = π̂(S₀)              by nondegeneracy of e₂

**UNPROVED.** Neither line enters the proof graph.

**Binding qualification (operator).** The second line requires the identification between the primitive
Betti functional that defines `α_p` and the Weil-pairing character attached to `S₀` to be pinned down.
"Standard duality" is not sufficient for this project: a sign, a plus/minus eigenspace choice, a
polarization, or a normalization mismatch could hide exactly there. §2.1 records the two facts that make
this real: `α_p` is normalized by a *chosen* primitive orientation of `U₀`, and it lives in plus
**cohomology**, not plus homology.

**Added by this object.** The first line likewise rests on a Kummer-class / monodromy compatibility that
is written nowhere in the sealed record. Signs are invisible mod 2, but the identification of
`H₁(X₀(2p)(ℂ),ℤ)/2` with `J[2](ℂ)` that it uses must be stated before it is used.

**Conditional rationality — an elementary implication whose antecedent is unproved.** Suppose
`T_p = π̂(S₀)`, `T_p ∈ J(ℚ)`, and `π̂` is a `ℚ`-defined closed immersion, injective on geometric points.
Then for every `σ ∈ G_ℚ`

    π̂(σS₀) = σ·π̂(S₀) = σT_p = T_p = π̂(S₀),

so injectivity gives `σS₀ = S₀`, and `S₀ ∈ E₀(ℚ)[2]`. The inputs other than the antecedent are in the
sealed record: `T_p ∈ J(ℚ)[2]` as written at `ADDENDUM_005` line 62, of exact order two by `ADDENDUM_009` §3;
and the embedding property quoted at the end of §3. **Rationality of `S₀` is therefore a derived
consequence of `(C′)`, never an input to its definition.**

### 6.2 The finite-flat warning — affects strategy

**Do not choose a finite-flat carrier yet.** `J₀(2p)` has semistable, not good, reduction at 2, so the
2-torsion of its Néron model is quasi-finite and not in general finite. At `2 ‖ N` these are distinct
objects, and the distinctions matter: the Néron identity component; the component group; the schematic
closure of the generic 2-torsion point; the full quasi-finite 2-torsion.

Unverified observation: under the standard Deligne–Rapoport picture the cusps `0` and `∞` reduce onto
different components of the special fibre, so `[0]−[∞]` has nonzero multidegree and `T_p` may specialize
outside the identity component. **Not verified here.**

If `T_p` has nontrivial component specialization, insisting prematurely on a finite-flat subgroup could
manufacture a false obstruction.

## 7. The bifurcation — strategy directive for the next stage

1. **First**, prove the generic-fibre equivalence `(C) ⟺ T_p = π̂(S₀)`, independently of `(D3)`.
2. **Only after that**, determine what exact information `(D3)` supplies and whether it forces that
   equality.

This keeps integral-model problems out of a bridge whose first half may be purely Betti / Kummer /
Weil-pairing.

## 8. Boundaries unchanged

* Uniform optimality `E₀ = E` remains open; the `B` vertex with `C₂ × C₂` is still live
  (`ADDENDUM_009` §4). Nothing here, and no future resolution of `(D1)` or of `(D3) ⟹ (C)`, settles it.
* The negative H41 seed remains unproved.
* The positive branch remains entirely outside this architecture.

**The H41 seed remains unproved.**
