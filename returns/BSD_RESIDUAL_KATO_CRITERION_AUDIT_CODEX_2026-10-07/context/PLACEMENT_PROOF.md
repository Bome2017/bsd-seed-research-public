# Integral Mordell–Weil placement of the first derivative

**Status: MW_PLACEMENT_DERIVED_FROM_RETAINED_WEAK_ORDER_INPUTS.**
Written deduction by the same worker; independent review pending. No literature
novelty or machine verification is claimed.

## 1. Domain, object and retained inputs

Use the fixed seed in its retained minimal model

    E: y²=x³−x²−66020924x−65074271436.

Let p≥5 be a good prime in the retained irreducible-residual domain. Put
T=T_pE, S={∞}∪{primes dividing pN}, H=H¹(G_(Q,S),T), and

    W=κ(E(Q)⊗Z_p) ⊂ H.

The retained rank is exactly two. The retained saturated basis is
P₁=(−3031,327384), P₂=(−2394,281520); the torsion group has order two.
These seed inputs are not recertified here.

Use the actual integral smoothed Kato class, with its lattice transported
simultaneously as specified in context/FOUNDATION_CHECK.md §3. In that convention,
the preceding weak-order proof gives

    z_∞=U y_∞,  U=γ−1,
    δ_p:=∂_γ z=aug(y_∞) ∈ H.                         (1)

Do not replace it by an independently normalized primitive Kato class.

The retained proof and its source audit give these precise facts:

1. H is finitely generated and torsion-free over Z_p; W has rank two.
2. M=H¹_Iw is free of rank one over Λ=Z_p[[U]], and M/UM→H is injective.
3. Writing z_∞=f m for a basis m of M, the Kato length inequality and
   derived control imply

       rank_Zp H − 1
          ≤ length_(Λ_(U)) H²_Iw,(U)
          ≤ ord_U(f)                                  (2)

   when z_∞≠0. The lower bound uses the full H² term.
4. In particular,

       δ_p⊗1≠0  ⇒  ord_U(f)=1  ⇒  dim_Qp(H⊗Q_p)=2.    (3)

These are imported at their existing source-audited written-proof grade,
from lab commits d4d86454 and 54637ae1. We do not re-audit them or assume
Sha finite. Good supersingular primes are included; no ordinary filtration
is used.

## 2. Rational placement by a case split

**Proposition 1.** Under the retained inputs,

    δ_p⊗1 ∈ W⊗Q_p.                                    (4)

If δ_p⊗1=0, this is immediate. If it is nonzero, (3) says H⊗Q_p has
dimension two. Its subspace W⊗Q_p already has dimension two, so they are
equal. This proves (4) in both cases.

The reasoning does not assume the nonzero case occurs. It also does not
claim H⊗Q_p=W⊗Q_p when the derivative is zero. That distinction prevents
an illicit conclusion about the size of the ambient cohomology.

## 3. The integral issue: the Kummer image is saturated

Rational placement by itself does not imply integral placement for an
arbitrary chosen point sublattice. We use the full Mordell–Weil lattice.

**Lemma 2.** W is p-saturated in H:

    p h∈W, h∈H  ⇒  h∈W.                               (5)

Proof. Write ph=κ(w), w∈E(Q)⊗Z_p. The coefficient sequence

    0→T --p--> T →E[p]→0

makes the kernel of reduction H→H¹(G_(Q,S),E[p]) equal to pH.
After inflation to H¹(Q,E[p]), compatibility of Kummer maps identifies
the reduction of κ(w) with

    κ_p(w mod p),  κ_p:E(Q)/pE(Q)→H¹(Q,E[p]).

The finite Kummer map κ_p is injective: it is the connecting map in
the cohomology sequence of multiplication by p on E(Qbar). The natural
identification

    (E(Q)⊗Z_p)/p ≅ E(Q)/pE(Q)

uses finite generation; here the torsion of order two disappears on both
sides. Since ph reduces to zero, κ_p(w mod p)=0. Thus w=pw₁ for some
w₁∈E(Q)⊗Z_p. Consequently p(h−κ(w₁))=0. Torsion-freeness of H gives
h=κ(w₁), proving (5).

For completeness, the retained torsion-freeness also follows directly
from this coefficient sequence: H[p] is an image of H⁰(Q,E[p]), which
vanishes by residual irreducibility. Iteration eliminates all p-power
torsion.

The finite Kummer sequence and its compatibility in n are standard and
are printed in Milne, *Elliptic Curves*, Chapter IV, equation (28), p.112,
and the diagrams on p.129. This proof needs neither a Sha-finiteness
assumption nor an inverse-limit assertion about the Weil–Châtelet group.

**Corollary 3.**

    H ∩ (W⊗Q_p)=W                                     (6)

inside H⊗Q_p. Indeed if h belongs to that intersection, some p^n h
belongs to W. Apply (5) n times.

## 4. Integral point-valued derivative

Combining (1), (4) and (6) proves the new placement statement:

    ∂_γ z ∈ κ(E(Q)⊗Z_p).                              (7)

In the retained saturated basis there are unique a_p,b_p∈Z_p with

    ∂_γ z=a_p κ(P₁)+b_p κ(P₂).                         (8)

This is an existence-and-uniqueness statement for coordinates of the
already constructed cohomology class, not a calculation of those
coordinates. It holds also if a_p=b_p=0.

At every finite coefficient level p^n, the reduction of (8) is the
Kummer class of

    (a_p mod p^n)P₁+(b_p mod p^n)P₂ ∈ E(Q)/p^nE(Q).

Thus this derivative has no excess Selmer component. This does not say
that other Selmer classes have no excess component.

## 5. Lattice and normalization safeguards

Equation (7) is made after the simultaneous lattice-and-class transport
in the retained foundation audit. If L_φ is the original image lattice
and s:L_φ→T_pE is that integral Galois-equivariant isomorphism, the statement
is about s_*(∂_γ z_(L_φ)). No independent source generator is substituted.

Two such homothetic lattice identifications differ by a Z_p-unit; either
therefore preserves membership in W. This does not compute the absolute
power of p comparing an independently fixed modular source normalization
with a separately fixed Tate-module normalization.

Integrality of a_p,b_p does NOT say that either is a unit, nonzero, rational,
or independent of p. Nor does a p-adic linear combination of P₁,P₂ have to
be one rational point of E(Q). No smoothing or Euler factor is divided
away in proving (7).

## 6. Endpoint and exact scope

The earlier conditional implication remains:

    (a_p,b_p)≠(0,0) ⇒ Sha(E/Q)[p^∞] is finite.

It follows from (3) and the compact Kummer sequence, exactly as in the
retained weak-order proof. It is not a new bound supplied by (7), and it
does not imply primary vanishing. No nonzero coordinate has been obtained.

The statement supersedes only the earlier reservation that this particular
derivative has not been placed in the rational-point plane. It does not
prove the analytic Mordell–Weil/Bockstein formula, a relation to q_E, or the
cyclotomic-to-tame comparison. In particular the coefficient-prime factor
#E(F_p)/p of valuation −1 remains part of that distinct comparison problem.

FIN, ORDER9 and Q36 remain unchanged. The result closes a placement
prerequisite of the derivative route; it supplies no independent
nonvanishing input.
