# An explicit one-place detector for the two obstruction classes

2026-10-13. Baseline: `Bome2017/bsd-seed-lab@257af6888c80fda3b90d481cf2d94f9950701811`.

**DERIVED UNDER RETAINED GLOBAL INPUTS; EXACT LOCAL ARITHMETIC EXECUTED.**

This is a new written deduction from the supplied representatives. It is not an independent end-to-end review, novelty claim, new seed bound, or replacement of the all-place descent theorem. The lower-bound argument below requires no class-number computation, fundamental-unit claim, height, L-value, or previously calculated Sha order.

## 1. Objects and retained prerequisites

Use the two curves, the degree-five isogeny phi:A -> F, its dual, and the normalized descent function f of the submitted proof. In particular,

    d = 43737, K = Q(sqrt(d)), x_K = (1+sqrt(d))/2,
    A = [0,0,1,-19766893413,-1937478573143510],
    F = [0,0,1,-14959712463303,-22270654620235278500].

The actual descent function is

    f(X,y) = (X-11d/3)(y+1/2)
             + sqrt(d)(-4X^2+(161d/6)X-785d^2/18).

Retain the source identification

    Sel_hatphi(F/Q) = K({5,11},5)^minus,
    A(Q)/hatphi F(Q) -> Sel_hatphi(F/Q) -> Sha(F/Q)[hatphi] -> 0.

Here and below the first arrow in this Kummer sequence is injective. The local membership statement is the precise Miller--Stoll Theorem 11 application in the original return: real kernel, w=1, good reduction at 5, A(Q_5)[phi]=0, Sigma_1={11}, Sigma_2 empty. The theorem and its exceptional cases were checked in the primary text. The curve-specific isogeny, differential and local-reduction inputs remain retained.

Also retain rank A(Q)=2, no rational 5-torsion, and the 5-saturation of

    P1 = (1778638/9, 1169009812/27),
    P2 = (6466626346478/36517849,
          2366996613841078836/220677361507).

These hypotheses make P1,P2 span A(Q)/5A(Q). They are not recomputed by this return. The normalized function represents the isogeny connecting homomorphism and kills 5A(Q).

The two actual Selmer elements are

    epsilon = 23423+112 sqrt(d),
    alpha11 = (68594257+327992 sqrt(d))/14641.

Their membership follows from the retained local theorem, norm one, and valuation support. Membership is not deduced just from the one local calculation below.

## 2. A completely explicit local homomorphism

Let mathfrak p = (11,x_K-1). The polynomial x^2-x-10934 has the simple root 1 modulo 11, so K_mathfrak p = Q_11, with sqrt(d)=1 modulo 11. Fix the uniformizer 11 and the residue-field generator 2 of F_11^*.

For z in K^*, let v=v_mathfrak p(z), and define

    Delta(z) = ( v mod 5,
                 ind_2( reduction(11^(-v)z) ) mod 5 ) in F_5^2.   (1)

The unit in the second entry is reduced at the chosen embedding. This is not the logarithm of a p-adic height. Multiplication adds both entries. Fifth powers are killed.

In fact Delta identifies Q_11^*/Q_11^{*5} with F_5^2. The valuation supplies one factor; reduction of the unit supplies F_11^*/F_11^{*5}, of order five. Fifth powering is an automorphism of 1+11 Z_11, since 5 is a unit in Z_11. This last fact follows directly from Hensel lifting. Thus no uncomputed principal-unit contribution is omitted from (1).

The local uniformizer and residue generator fix the following matrix. Changing them changes coordinates by an invertible matrix and cannot change its rank.

## 3. Compute the signatures from the actual formulas

For epsilon, v=0 and epsilon=6 modulo mathfrak p. Since 2^9=6 modulo 11,

    Delta(epsilon) = (0,4).                                     (2)

For alpha11 use the exact identity

    gamma = -5829-56 x_K,
    Norm(gamma)=11^4,
    alpha11=gamma/conjugate(gamma).

The Hensel root of x^2-x-10934 at this prime is

    x_K = 143430 mod 11^5.

Substitution gives gamma=-8037909=-549*11^4 modulo 11^5, and conjugate(gamma)=1 modulo 11. Thus v(gamma)=4 and v(conjugate(gamma))=0. Moreover alpha11/11^4 has residue 1. Consequently

    Delta(alpha11) = (4,0).                                     (3)

The direct rational-point evaluations give

    v_mathfrak p(f(P1))=v_mathfrak p(f(P2))=0,
    f(P1)=f(P2)=1 modulo mathfrak p,
    Delta(f(P1))=Delta(f(P2))=(0,0).                             (4)

These assertions were evaluated from f and the rational coordinates, not inferred from the supplied class-group output. For additional consistency, the checker also verifies the exact global identities

    f(P1)=-(1249565229839/81)x_K+393863215501942/243,
    f(P2)=f(P1)^2 rho^5,
    rho=(-527625 x_K-54179073)/352403588,
    Norm(f(X,y))=(X-14d/3)^5

on A. The fifth-power relation is not necessary for (4): checking the two spanning points locally is sufficient.

The resulting signature table is

| Element | v_mathfrak p | Unit residue mod 11 | Delta |
|---|---:|---:|---|
| epsilon | 0 | 6 | (0,4) |
| alpha11 | 4 | 1 | (4,0) |
| f(P1) | 0 | 1 | (0,0) |
| f(P2) | 0 | 1 | (0,0) |

The two obstruction columns form [[0,4],[4,0]], of determinant 4 modulo 5.

## 4. Independence in Sha without the global class/unit calculation

Because P1,P2 span A(Q)/5A(Q) and the descent homomorphism kills 5A(Q), (4) implies

    Delta(f(P))=0 for EVERY P in A(Q).                          (5)

Thus Delta on the isogeny Selmer group factors through the actual rational-point quotient, giving a well-defined homomorphism

    D_11 : Sha(F/Q)[hatphi] -> F_5^2.                           (6)

For a putative relation between the two classes in Sha, localize the corresponding relation in the Selmer group. Equations (2)--(5) give

    4b=0, 4a=0 mod 5

for the class epsilon^a alpha11^b. Hence a=b=0. Equivalently,

    D_11([epsilon])=(0,4), D_11([alpha11])=(4,0)

prove both independence and surjectivity of (6). Therefore

    dim_F5 Sha(F/Q)[hatphi] >= 2.                               (7)

The proof of (7) does not use Cl(K)=C20, fundamental-unit status, the fifth-root ideal of f(P1), or any L-value. Those computations remain useful for an UPPER bound. If the submitted exact dimension dim Sha(F)[hatphi]=2 is separately retained from its S-class calculation, (6) is an isomorphism. The local argument alone does not rule out a kernel of (6).

This is an independently computable signature of the supplied excess. It is not a universal upper bound: zero signatures do not generally mean global triviality.

## 5. Why this does not contradict local solubility

D_11 is NOT localization of a Sha torsor into H^1(Q_11,F). That localization is zero. It is the local isogeny-Kummer class before forgetting the covering structure, compared with the image of globally rational points on A.

The local theorem gives

    A(Q_11)/hatphi F(Q_11) = H^1(Q_11,F[hatphi]) ~= F_5^2

in this situation. Yet (5) says that every globally rational point of A has trivial class in that local quotient. The two Selmer elements represent local point classes available over Q_11 but not furnished by any globally rational point under this connecting map. Their images in H^1(Q_11,F) are still zero, as required for local points on the coverings.

Thus the statement is not “a locally insoluble obstruction at 11.” It is a mismatch between the local isogeny quotient and the localization of the global point image. All-place solubility continues to depend on the Miller--Stoll theorem, not on tests at finitely many primes.

## 6. Check of the five-quadric model

Substituting lambda=11, r=1464, s=7 into Fisher Theorem 5.3 reproduces the supplied alternating matrix. Exact arithmetic verifies

    r^2-ds^2=183,
    (r+s sqrt(d))/(r-s sqrt(d))=epsilon.

The checker recomputes all five signed Pfaffians, compares them coefficient by coefficient with the supplied equations, and verifies their five matrix syzygies. Independent Jacobian-minor calculations at the supplied reduction points

    (1:0:1:2:3) modulo 5,
    (1:0:6:0:6) modulo 11

give nonsingular local Hensel charts. The selected triple of equations has a nonzero three-by-three Jacobian minor, and the complementary matrix entry is a unit, so the Pfaffian syzygies force the remaining equations. The minor values can differ from the original receipts because a different triple was selected.

The global smooth genus-one interpretation is supplied by the matched Fisher theorem and the retained geometric check. The all-five-chart Groebner computation was not rerun. Fisher's kernel generator may invert epsilon relative to f; inversion negates its nonzero signature and preserves every nontriviality statement here. No projective-coordinate covering map was constructed in this return.

Combining the source identification with (7) gives the nontriviality, hence rational insolubility, of the supplied smooth model. This alternative argument has fewer retained global number-field inputs than the original proof, but it is not a replacement for its local-membership or rank/saturation inputs.

## 7. An explicit degree-five splitting field

The same unit gives a concrete field over which the unit covering becomes trivial. Let t be a root of

    P(t)=t^5-5t^3+5t-46846,       M=Q(t).                       (8)

The reduction modulo 11 is irreducible. The executable certificate checks

    X^(11^5)=X mod P,  gcd(P,X^11-X)=1 in F_11[X].

These are the finite-field irreducibility conditions for degree five. In particular [M:Q]=5 and M and K are linearly disjoint.

Put D(t)=t^4-3t^2+1. The exact Chebyshev identity is

    (t^5-5t^3+5t)^2-4 = (t^2-4)D(t)^2.

Since 46846^2-4=224^2*d is nonzero, D(t) is nonzero in M. Define

    z=(t+224 sqrt(d)/D(t))/2 in MK.                            (9)

Then z+z^(-1)=t and z-z^(-1)=224 sqrt(d)/D(t). Consequently

    z^5+z^(-5)=46846,
    z^5-z^(-5)=224 sqrt(d),
    z^5=23423+112 sqrt(d)=epsilon.                             (10)

Over MK the Kummer class is therefore zero. Restriction from M to MK is injective on the relevant 5-torsion cohomology because corestriction composed with restriction is multiplication by two. Hence the unit covering is trivial over M. This also covers the inverse-class convention used for the Pfaffian model.

Thus C(M) is nonempty. This is an algebraic splitting-field proof; no coordinates of an M-point on the five quadrics were computed.

The torsor class is nonzero and killed by five, so its period is five. If C has a point over a finite field extension L/Q, restriction/corestriction implies that [L:Q] kills its class. Thus five divides every such degree. The field M realizes degree five, so the minimum splitting degree and the index are both five. These are consequences for this control curve, not statements about the seed's Sha or new field-tower control of the seed.

## 8. What can and cannot be transferred to the seed

The general comparison of a localized Selmer lift with the image of globally rational points makes sense in full p-descent as well. For example, localizing Sel_p(E/Q) and quotienting by the localization of E(Q)/p gives a map

    Sha(E/Q)[p] -> (E(Q_q)/pE(Q_q))/image(E(Q)/pE(Q)).             (11)

A nonzero image detects excess. Vanishing of its target does not prove Sha[p]=0: the kernel of (11) can contain the entire group. There is no kernel bound in this construction without additional global arithmetic.

For the seed at p=17, the particular place q=11 cannot reproduce the control's detector. An exact direct count gives #E(F_11)=14, hence E(Q_11)/17E(Q_11)=0. The formal group is pro-11, where multiplication by 17 is invertible, and reduction has order prime to 17. Thus (11) at q=11 is identically zero. This is not a new proof of the already retained Sha17 vanishing.

More fundamentally, the seed's full residual representation does not provide the control's rational five-isogeny or the same scalar quadratic-field descent. The new local signature is an explanation and detector of this actual positive control, not an exclusion theorem for all possible seed classes. No claim that irreducibility alone rules out such classes is made.

The result meets the narrower discovery goal of extracting an explicit arithmetic relation from the measured positive control. It does NOT meet the stronger seed-finishing goal of independently bounding the unresolved prime tail. FIN, ORDER9, Q36 and seed prime coverage are unchanged.
