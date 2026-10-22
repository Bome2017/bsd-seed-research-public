# The exact seed scalar and the missing analytic comparison

**Grade: CONDITIONAL_NORMALIZATION_DEDUCTION.**
The proposed arithmetic comparison in (T1) is not proved in this return.
This calculation pins its normalization and its endpoint without inserting Sha.

## 1. Retained inputs

Use the seed's saturated basis, total real Néron period Ω_E, regulator Reg,
torsion order 2, and Tamagawa product 16. Set

    q_E=L''(E,1)/(2Ω_E Reg).

Its rationality and exact value 36 remain open. A numerical interval is not
a residue map Q→F_p.

Let S_*={2,3,5,19,59,487,2243,4547,5843}. The joint retained domain of
G2, Theorem W, and the present normalization is p∉S_*.

For each such p, G2 supplies infinitely many auxiliary primes ℓ with
ℓ≡1+p (mod p²), residual Frobenius −I, and R_(p,ℓ)≠0. Therefore
a_ℓ≡−2, #E(F_ℓ)≡4, and a_ℓ−2≡−4 (mod p).
These are not the different auxiliary primes with a_ℓ≡2 used by the
two-prime Kurihara construction.

Write F_ℓ for the degree-p real field in Q(μ_ℓ), S_ℓ={q:q|Nℓ}, and
Σ_ℓ=S_ℓ∪{p}. BKS II's tame modular element uses S_ℓ, not Σ_ℓ.
With the common discrete-log coordinate U_ℓ, the retained W/G2 identifications are

    [θ_(F_ℓ,S_ℓ)]₂ = (1/2)c_N C₂(p,ℓ) U_ℓ²,
    R_(F_ℓ)        = 4 R_(p,ℓ) U_ℓ².

Here 1/2 converts the production least-real period to the total Néron period.
These are equalities in the residual degree-two augmentation quotient, not
equalities of full group-ring elements.

## 2. Exact bad-prime multiplier

The retained nonsingular reduction counts, in order 2,3,2243,4547,5843, are
2,4,2242,4547,5844. Hence

    c_N = ∏_(q|N) #E^ns(F_q)/q
        = 17469664/13105849
        = (2^5·19·59·487)/(2243·5843).

This both checks the constant and explains the additional primes
19,59,487 in the comparison domain. It is a fixed p-unit on that domain.

## 3. Precisely sufficient unproved identity

Suppose a nonzero rational number α is independently constructed, and for
cofinitely many eligible p and a G2-detecting ℓ one proves

    [θ_(F_ℓ,S_ℓ)]₂
      = −bar(α)c_N e_ℓ R_(F_ℓ),                         (T1)

where e_ℓ=#E(F_ℓ)/ℓ and all scalars are reduced in Z_(p). The minus sign
is the single-conductor sign in BKS II's Mazur–Tate convention.

Substituting the two retained identifications and cancelling c_N gives

    (1/2)C₂ = −4 bar(α)e_ℓ R_(p,ℓ).

Since ℓ≡1 (mod p), −e_ℓ≡a_ℓ−2. Thus

    C₂(p,ℓ)=8 bar(α)(a_ℓ−2)R_(p,ℓ).                    (T2)

In particular (T1) with α=q_E would give the recorded 8q_E identity,
provided rationality and a finiteness-free proof of (T1) are supplied.
It is not obtained by relabeling BKS II Conjecture 3.4.

For comparison only, under whole-Sha finiteness the algebraic BSD scalar is
Tam·#Sha/tors²=4#Sha; substituting THAT scalar gives 32#Sha, and hence 288
if #Sha=9. This conditional check cannot be used to construct α.

## 4. Exact endpoint and remaining flexibility

Exclude the finitely many numerator and denominator primes of α. At every
remaining p where (T1) is proved, G2 makes the right side of (T2) nonzero.
The retained Ota implication then gives Sha[p^∞]=0.

Thus (T1), with a fixed nonzero rational α, would close the cofinite
good-prime vanishing step. It would not by itself settle primary finiteness
at the exclusions, ORDER9, or Q36.

For vanishing alone an additional proved p-adic UNIT multiplier in (T1)
would also suffice. Exact matching is required to identify α with q_E or
the residue 288. An unproved valuation cannot be called a unit. A general
uniform estimate could succeed without a rational α at all; this document
specifies one route, not the only possible route.

## 5. Why the existing cyclotomic statement cannot just be substituted

In BKS I's formal convention the conjectural scalar is

    v_ξ (∏_(q∈Σ) e_q) q_E,     v_ξ=Ω^+/Ω_ξ.

At every good seed p≥5, e_p=#E(F_p)/p has valuation −1. The rational
2-torsion/Hasse argument and the separate #E(F_5)=8 check establish this.
That factor is absent from the tame S_ℓ expression (T1). Transporting a
cyclotomic identity to (T1) must account for its cancellation in the actual
integral regulator map; it cannot be absorbed into c_N.

Moreover the analytic comparison, nonzero Bockstein regulator, correct
Mordell–Weil target, and passage to the tame determinant diagram remain
distinct assertions. The weak-order proof in this return supplies none of
those comparisons.

The retained W proof branches on whether Sha[p] is zero, uses the zero
conclusion in the nonzero-Sha branch, and obtains fixed-p auxiliary
independence in the other branch. That proves the stated independence; it
does not prove a nonzero common scalar across p.
