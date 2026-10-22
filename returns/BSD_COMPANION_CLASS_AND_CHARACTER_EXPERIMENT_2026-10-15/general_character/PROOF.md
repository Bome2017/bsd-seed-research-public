# Character-resolved bounds and the geometric/arithmetic index distinction

2026-10-15. Written deductions under the retained full-image source and literal incidence-map inputs. The finite checks below are geometric algebra, not arithmetic unit-index computations.

## 1. Integral characters and actual norm maps

Let p be odd, V=E[p], and assume the retained full GL2(F_p) image. Let A and B be the point and nonzero-covector etale fields. On either field use the internal scalar pullback sigma_a, a in F_p^*. Let omega(a) be its Teichmuller lift in Z_p^*. For chi=omega^k set

    e_chi = (p-1)^(-1) sum_a chi(a)^(-1) sigma_a.

This is an integral idempotent in Z_p[F_p^*]. It does not use division by p. A class satisfying the descent relation sigma_a(alpha)=alpha^a modulo p belongs to the chi=omega summand. In general this is one summand of the minus part, not the entire minus part.

Let u:A->B and v:B->A be the actual multiplicative incidence norms. Direct substitution in their defining products gives

    u sigma_a^A = sigma_(a^-1)^B u.

Thus u takes chi to chi^-1. The counting identity gives vu=uv=p on all nontrivial scalar components, hence in particular on odd characters. This is an identity of actual completed unit and divisor lattices. Their paired cokernels are killed by p. Do not identify chi and chi^-1 unless their equality has been checked.

For an odd character the ordinary unit rank is

    d_chi=(p+1)/2.

One derivation uses equivariant Dirichlet: the scalar-homogeneous embedding-function space has rank p+1; complex conjugation has eigenvalues +1 and -1 on V. Its invariant part has rank(p+1)/2. The constant-function subtraction in Dirichlet affects only the trivial character. The fields have real embeddings, so they contain no p-power roots of unity.

## 2. The exact characterwise lattice formula

Tensor all lattices with Z_p. Choose the same rational prime setS on A and B, including the source's required ramification support. Let c_A,chi and c_AS,chi denote lengths of ordinary and S-class components, and r_AS,chi the dimension of Cl(A,S)[p]^chi. Define

    s_U,chi = length coker(u:U_A^chi -> U_B^(chi^-1)),
    t_D,chi = length coker(u:D_AS^chi -> D_BS^(chi^-1)).

The divisor modules are primitive free lattices on all primes aboveS. The exact S-unit and ideal-class sequences, with integral idempotents applied, give

    s_US,chi = s_U,chi + t_D,chi
       + c_A,chi-c_AS,chi - c_B,chi^-1+c_BS,chi^-1.    (1)

Let K_chi be the global scalar-compatible affine-norm kernel in A(S,p)^chi. The unit/class Kummer sequence gives the bound

    dim K_chi <= s_US,chi+r_AS,chi.                   (2)

The unit term is exact: an S-unit with pth-power norm has an S-unit pth root in B. A class projection need not be surjective, which is why(2) is an inequality. Combining the two equations preserves every finite lattice index:

    dim K_chi <= s_U,chi+t_D,chi+c_A,chi-c_B,chi^-1
                    +c_BS,chi^-1-(c_AS,chi-r_AS,chi). (3)

This is valid for largerp. It does not yet remove s_U,chi by replacing it with a geometric determinant.

## 3. A general arithmetic bound that does not need the companion

The valuation vector of a norm-kernel class lies in ker(u_D modp), of dimension t_D,chi. A class whose valuation vector is zero modulo p lies in the ordinary virtual-unit space A(empty,p)^chi. Its dimension is d_chi+r_A,chi by the ordinary unit/class sequence. Consequently

    dim K_chi <= (p+1)/2 + r_A,chi + t_D,chi,          (4)

where r_A,chi=dim Cl(A)[p]^chi is the ORDINARY source class rank. This is a bound on the whole global source kernel, not only its unit-supported part. It requires actual source class and primitive divisor data, neither a known Selmer dimension nor a norm-kernel calculation.

In particular, if t_D,chi=0 and Cl(A)[p]^chi=0, every global admitted class is represented by an ordinary chi-unit, giving upper bound(p+1)/2. Vanishing only of Cl(A,S)[p]^chi would not suffice: ordinary class lifts killed byS can remain after all valuations become divisible byp.

Atp5 this gives upper bound3 when the stated arithmetic inputs are certified. It does not by itself give rank2 equality; any parity use requires its own retained hypotheses. At larger primes the constant grows. This is a valid upper-bound mechanism, not a uniform rank-two bound.

## 4. The aggregate companion bound also extends

Write c_A^- for the sum of all odd-character class lengths. The retained real-regulator/class-number comparison gives

    s_U^- = (p^2-1)/8 + c_B^- - c_A^-.              (5)

The plus-field terms in the original formula are exactly removed by passing to minus class lengths; no claim that A^{+/-1} and B^{+/-1} are isomorphic for allp is needed. Their zeta functions agree because their permutation characters agree. The real logarithmic incidence determinant has absolute value p^((p^2-1)/8), and splitting plus/minus lattices introduces only powers of2.

Applying the same S-unit argument to the entire minus part yields

    dim K^- <= (p^2-1)/8 + t_D^- + c_BS^-
                               -(c_AS^- - r_AS^-)
             <= (p^2-1)/8 + t_D^- + c_BS^-.         (6)

Since K_chi is a summand of K^-, this bounds the descent source as well. The constants are3,6,15 atp5,7,11. Formula(6) is an independent companion bound but is weaker than a characterwise constant1 claim. It does not supply a small class contribution across primes.

## 5. What the finite character experiment actually establishes

For projective representatives P=(1,a) and(0,1), and covectors lambda, the matrix of u on chi-homogeneous functions is

    U_k(lambda,P)=omega(lambda(P))^(-k) if lambda(P) !=0,
                 0 otherwise.

It maps the chi=omega^k coordinate lattice to the inverse-character lattice. We computed these matrices modulo p^4 atp5,7,11 and checked both compositions with the inverse-character matrix are pI. On the complex-conjugation-fixed part the rank is d=(p+1)/2 and the geometric integral index is

    g_k=(k+1)/2,              k=1,3,...,p-2.

These indices are respectively

    p5:  1,2;
    p7:  1,2,3;
    p11: 1,2,3,4,5.

Their sums recover(p^2-1)/8. They were predicted from the formula before the executable run; this was a same-session algebra test, not a blinded arithmetic experiment.

For an exact rank proof, modulo p the matrix entries are(lambda(P))^(p-1-k). Expanding this homogeneous polynomial factors the matrix through the degree(p-1-k) polynomial space. Evaluation on p+1 projective points is injective in that degree, and its binomial coefficients are nonzero modulo p. Thus the full rank is p-k and its kernel has dimension k+1. The c-invariant kernel has dimension(k+1)/2. Since the integral transpose compositions are pI, all Smith exponents are0 or1, giving the asserted geometric index.

The relevant k=1 geometric index is indeed1. But these are embedding-function lattices, not the actual global unit lattices. A unit lattice may be differently situated inside the same rational representation. Equations(1)--(3) deliberately retain that arithmetic index.

## 6. Why the geometric value does not prove a character class-number formula

A concrete lattice countercontrol atp5 keeps the fixed incidence maps and the same rational G-representations. Let M_1,M_3 be the geometric source character lattices and N_3,N_1 the paired targets. Their c-invariant forward indices are1 and2. Replace the two targets by

    N'_3 = u(M_1),
    N'_1 = p^(-1)u(M_3).

Both are integral G-stable lattices in the same rational spaces. Stability follows because u is a G-map. Both transpose maps remain integral and uv=vu=p still holds. On c-invariants the forward indices become0 and3, respectively, while the sum remains3. Thus the rational representation, incidence identity and aggregate determinant do not determine the individual index. In the first character the geometric1 has changed despite preserving that aggregate information.

This is an abstract lattice countercontrol, not an elliptic curve or a number-field unit counterexample. It does not disprove a characterwise arithmetic class-number identity. It proves that such an identity needs additional arithmetic beyond the inputs used for the aggregate comparison.

The ordinary analytic class-number formula controls the aggregate regulator ratio. We did not find in the inspected sources a theorem giving

    s_U,chi = 1+c_B,chi^-1-c_A,chi

for the actual units in this setting. That proposed formula is therefore not imported. The Weil pairing identifies the rational dual representation, but it does not identify the two integral global unit lattices or their characterwise regulators.

## 7. Targeted regulator-constant source screen

Freshly read: Torzewski, arXiv1703.10602v3, Theorems6.6 and6.8 and Remark6.9. His classification uses cohomology of cyclic p-subgroups and, under an additional representation-ring hypothesis, regulator constants and the rational representation. Cyclic Sylow alone is not the stated hypothesis of6.8. We have not verified its additional hypothesis for GL2(F_p), computed the required unit-lattice cohomology, or supplied the regulator constants. No characterwise unit-index formula is obtained by citing that paper here.

This source screen identifies data that could distinguish the integral lattices; it does not declare the desired arithmetic comparison impossible. The finite countercontrol above already suffices to reject the unsupported inference from a rational/geometric equality alone.

Sources and retained inputs:
- Schaefer--Stoll, *How to do a p-descent on an elliptic curve*, long version, Lemmas7.2 and7.6 and Proposition7.8/Corollary7.9 (global source and scalar convention retained from the previous primary-source audit).
- The earlier ordinary incidence index proof, BSD_UNIT_ADMISSION_CONTINUATION_2026-10-13/reviewer/INCIDENCE_NORM_REVIEW.md, section4.
- Sutherland, MIT18.785 Lecture19 (2021), analytic number-field class-number formula, freshly checked in the preceding same-day packet.
- https://arxiv.org/pdf/1703.10602 (targeted primary reading stated above).

No new unit index, class-number certification, Selmer dimension or seed endpoint is inferred from CHARACTER_CHECKS.json.
