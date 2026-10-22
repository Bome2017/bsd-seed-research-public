# Fifth addendum — the uniform coefficient congruence, and the exact remaining comparison

**Tier: one SYMBOLIC uniform result, plus finite checks and independent determinations.** No proof of
the H41 seed, no proof of the identification, no certification. Prior objects unmodified:
`ac82f3ad…`, `82b6730f…`, `81ac107b…`, `35f21882…`, `0bfb6b5e…`.

This object freezes only what is established. The `N = 16382` modular-degree job was still running when
this was sealed and is **deliberately not folded in**; if it returns it goes to a sixth addendum and is
judged under the kill condition fixed in §6 below, not retrofitted here.

## 1. The uniform congruence — SYMBOLIC, valid for every negative-branch member

For `p = 2^n − 1` prime, `n ≥ 5`, `N = 2p`, and the verified modular unit

    F_p(z) = η(z)^(2p−1) η(2z)^(2−p) η(pz)^(p−2) η(2pz)^(1−2p)

put `Θ_p(q) = q·d/dq·log F_p(q)`. From `q·d/dq·log η(δz) = δ/24 − δ·Σ_M σ₁(M) q^(δM)`:

    [q^m] Θ_p  =  − Σ_{δ | 2p, δ | m}  r_δ · δ · σ₁(m/δ),        constant term = −(p²−1)/8 = −M

Mod 2: every `r_δ` is odd, and the `δ = 2` and `δ = 2p` terms carry an even factor `δ` and vanish, so

    [q^m] Θ_p  ≡  σ₁(m) + [p|m]·σ₁(m/p)   (mod 2)

and for `m = p^k u` with `p ∤ u`, since `σ₁(p^k) ≡ k+1` and `σ₁(p^{k−1}) ≡ k`,

    (A)   [q^m] Θ_p  ≡  σ₁(p-free part of m)   (mod 2)

**Newform side.** Rational 2-torsion makes the residual representation reducible with trivial
semisimplification, so `a_ℓ ≡ 1 + ℓ ≡ 0 (mod 2)` for good odd `ℓ`; the Hecke recurrence then gives
`a_{ℓ^k} ≡ σ₁(ℓ^k)`; and at the two multiplicative primes `2` and `p`, `a_2, a_p ∈ {±1}`, so
`a_{2^j} ≡ a_{p^j} ≡ 1`. Multiplicativity gives `a_m ≡ σ₁(p-free part of m)`, matching (A). Hence

    (B)   Θ_p  ≡  f_H41   (mod 2)   as formal q-expansions,   for every negative-branch member.

**`v₂(M) = n − 2 ≥ 3`**, so the constant term vanishes mod 2 — which is what lets the reduction sit in
the cuspidal space at all.

**What (B) is, stated so it is not overweighted.** It is the composition of two standard facts: the
logarithmic derivative of an eta quotient is an Eisenstein series, and a curve with rational 2-torsion
has `f` congruent to an Eisenstein series mod 2. The content is that the two land on the *same*
Eisenstein series, uniformly. This is not a new deep theorem, and it is the serious evidence for the
architecture — more so than any finite level.

## 2. Finite checks — confirmatory only

`computation/verify_congruence.py`, output `receipts/VERIFICATION_OUTPUT.txt`. Over `m = 1..4000`:

    N = 62     p = 31     (B) mismatches 0    (A) mismatches 0    M = 120,     v₂ = 3
    N = 254    p = 127    (B) mismatches 0    (A) mismatches 0    M = 2016,    v₂ = 5
    N = 16382  p = 8191   (B) mismatches 0    (A) mismatches 0    M = 8386560, v₂ = 11

Newform-side steps confirmed at all three: `a₂ = 1`, `a_p = −1`, no good odd `ℓ < 200` with `a_ℓ` odd,
and no failure of `a_{ℓ^k} ≡ σ₁(ℓ^k)`. Total discrepancies across every finite check: **0**.

These confirm (B); they do not prove it. The proof is §1.

## 3. The exact remaining comparison

    (C)    χ_p = α_p mod 2

equivalently, in the Jacobian, with `J = J₀(2p)`, `T_p = ((p²−1)/16)·([0]−[∞]) ∈ J(ℚ)[2]` the class cut
out by `√F_p`, `π : J → E₀` the connected optimal quotient, `π̂ : E₀ ↪ J` its dual embedding, and
`S₀ ∈ E₀(ℚ)[2]∖{0}` the class of the primitive character `α_p mod 2`:

    (C′)   T_p = π̂(S₀)   in   J₀(2p)[2]

(C) is what the seed needs. (B) explains why the two sides have the same q-expansion mod 2; it does
**not** give (C), because a congruence of q-expansions does not control the integral Betti/cohomology
comparison. That gap is where residue characteristic 2, the bad prime `2 | N`, and the integral lattice
distinctions live.

## 4. The sufficient rational-line criterion — SUFFICIENT AND STRONGER, NOT EQUIVALENT

With the characteristic-2 Eisenstein maximal ideal

    𝔪 = ( 2,  T_ℓ − (1+ℓ) for ℓ ∤ 2p,  U₂ − 1,  U_p − 1 )

the criterion is

    (L)    J₀(2p)(ℚ)[𝔪] = 𝔽₂·T_p

**(L) ⟹ (C′):** `T_p ≠ 0`; `π̂(S₀) ≠ 0` because the dual of an optimal quotient is an embedding; both
are rational `𝔪`-torsion; and (L) leaves exactly one nonzero such point. So they coincide.

**(L) is labelled sufficient and strictly stronger than the seed.** It is not an equivalent
characterisation. By §6 it entails `a = 0` at every negative-branch level, which the seed alone does not.

Verified here at all three levels: `f` is genuinely killed by `𝔪` mod 2 — `a₂ = 1` and `a_p = −1`, both
odd, so `U₂ − 1` and `U_p − 1` annihilate mod 2; and `a_ℓ ≡ 0 ≡ 1 + ℓ` for every good odd `ℓ` tested.
`a_8191` was computed specifically for the third level.

## 5. N = 62 is FORCED, and is removed from the evidentiary count

`J₀(62)(ℚ) ≅ ℤ/5 × ℤ/120`, and `120 = 2³·3·5`, so the rational 2-torsion is `ℤ/2` — exactly one
nonzero point. Two nonzero rational 2-torsion classes must therefore coincide, so **(C) at `N = 62` is
forced: a theorem, not a test.** The full-homology agreement reported there in
`H41_ETA_CHARACTER_TEST_ADDENDUM_003` could not have failed, and presenting it as a passed test
overstated it.

**Corrected evidentiary count: one forced case, plus one genuine full-homology test at `N = 254`** —
and that one required the spanning repair recorded in `H41_ETA_EXTERNAL_CHECK_ADDENDUM_004`. Less
empirical support than previously reported, and a more accurate record.

(L) at `N = 62` is likewise satisfied for the trivial reason. Whether the reason generalises is the
question.

## 6. Independent `a = 0` determinations at N = 62 and N = 254 — not from their L-values

`computation/optimal.gp`, output `receipts/OPTIMALITY_OUTPUT.txt`.

    level     isogeny degree matrix                    real-period ratios    modular degrees
    N = 62    [1,2,4,4; 2,1,2,2; 4,2,1,4; 4,2,4,1]     1 : 1/2 : 1/2 : 1/4   2, 4, 8, 8
    N = 254   [1,2,4,4; 2,1,2,2; 4,2,1,4; 4,2,4,1]     1 : 1/2 : 1/2 : 1/4   24, 48, 96, 96

**The inference.** The optimal curve minimises the modular degree within its isogeny class, because
every other parametrisation factors through it and so has degree multiplied by the connecting isogeny.
Curve 1 — the H41 base itself, in both cases — attains the minimum. Hence the base **is** the
Γ₀-optimal member at both levels, so `h = Ω_{E₀,R}/Ω_{E,R} = 1` and

    a = −v₂(h) = 0   at N = 62 and N = 254,

established from optimality and period data, with no L-value used. This is an independent route to a
fact previously derived inside the frozen report from the certified `λ` values.

## 7. The falsification rule, fixed here in advance

    a = 1   ⟹   (C) fails

because `a = 1` puts `u₃ ∈ 2U₀`, so `ρ(η₃) = 0`, while `χ_p(η₃) = 1`.

Therefore `N = 16382` is a **legitimate kill test for this architecture**. Its two outcomes are not
symmetric:

* `a = 1` there — (C) is refuted immediately. The H41 seed would be untouched; only this eta-character
  mechanism dies.
* `a = 0` there — merely another survivor. It would add one more `a = 0` level and would **not** be
  evidence sufficient for uniformity.

Structural note bearing on the expected outcome: the isogeny degree matrix and the real-period ratios
are identical at `N = 62`, `254` and `16382`, and the Eisenstein data match at all three. That makes
`a = 0` the likelier outcome — that is, the less informative one.

## 8. The Frobenius/Eisenstein target — a PROPOSED ROUTE, not a result

The route under consideration is to prove

    dim_{𝔽₂} J[𝔪]^{G_ℚ} = 1

or a suitably justified local or Frobenius criterion implying it, which would give (L) and hence (C).

Observed, and **not** to be promoted: `a₃ = 0` at all three levels, so

    X² − a₃X + 3  ≡  X² + 1  =  (X+1)²   (mod 2)

This says Frobenius at 3 is **unipotent** mod 2. It leaves open a nontrivial unipotent action; it does
**not** establish a one-dimensional fixed space, and nothing here should be read as doing so.

Separately, the relevant multiplicity-one results in the literature exclude this case: the standard
squarefree statements restrict to residue characteristic `ℓ ∤ 6N` and then `ℓ > 3`, whereas here `ℓ = 2`
with `2 | N`. So "same residual eigensystem, therefore the same integral class" is not a step being
overlooked — it is a step that is not available.

## 9. Discipline point — the positive branch is entirely outside this architecture

The construction requires `N = 2p` exactly. The positive branch has `N = 2·3·ℓ`, so `F_p`, `Θ_p`, `T_p`,
`𝔪` as written, and (B), (C), (C′) and (L) **all fail to be defined there**. Nothing in this object
bears on the positive branch, and no result here may be quoted in connection with it. If this
architecture closes, it closes the negative branch only.

## 10. Status

    negative branch   u₃ ∈ 2^a U₀                PROVED
                      u₃ ∉ 2^(a+1) U₀            OPEN
    (B) Θ_p ≡ f mod 2                             PROVED symbolically, uniform in p
    (C) χ_p = α_p mod 2                           OPEN; forced at N=62, tested at N=254 only
    (C′) T_p = π̂(S₀)                              OPEN, equivalent to (C)
    (L) rational 𝔪-line                           OPEN; SUFFICIENT for (C), stronger than the seed
    a = 0                                         established at N = 62, 254; unknown at N = 16382
    positive branch                               outside this architecture entirely

**The H41 seed remains unproved.** The architecture's serious evidence is the uniform congruence (B);
the unresolved question is whether that congruence controls the required integral Eisenstein line in
the Jacobian. No Aristotle or model run was used for anything in this object, and none is authorised.
