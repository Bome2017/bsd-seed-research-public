# The ramified weight-three dual-exponential lattice

Grade: WRITTEN_DERIVATION_UNDER_RETAINED_INPUTS_AND_IMPORTED_THEOREMS.
This is a new calculation in this return, not an independently accepted
theorem or a claim of literature novelty.

## 1. Datum and conventions

Fix a good ordinary seed prime p >= 5 outside {19,59,487}. Use the
retained weight-three specialization g, its actual coefficient DVR O,
fraction field L, uniformizer pi, and saturated ordinary lattice T in
U=D(g)(1). Write e=v_pi(p); this need not be one. Retain

    0 -> A=O(alpha^{-1} chi) -> T
      -> M=O(alpha chi^{-1} omega) -> 0,       alpha-bar != 1.

Here chi is the p-adic cyclotomic character and omega its Teichmuller
part, extended trivially on the unramified quotient. Cohomology is
continuous local Galois cohomology over Q_p. H_f^1(T) is the inverse
image of H_f^1(U). Use the Bloch--Kato dual exponential on H^1(U),
called exp*_{U^*(1)} in the convention of Venjakob (A.67).

The retained rational calculation says H_f^1(U)=image H^1(A tensor L).
Its proof is copied in context/LOCAL_PREDECESSOR.md, sections 3-4.
This return does not substitute ordinary Greenberg conditions for an
unchecked Bloch--Kato comparison.

## 2. Integral reduction to the quotient character

The character alpha-bar is nontrivial and unramified. Thus H^0(M)=0
and H^0(M/pi)=0. The latter implies H^1(M)[pi]=0, so H^1(M) is
torsion-free. Integral local Tate duality gives H^2(A)=0: its discrete
dual is (L/O)(alpha), which has no invariants, since alpha-bar != 1.
Consequently the long exact cohomology sequence gives

    0 -> H^1(A) -> H^1(T) -> H^1(M) -> 0.               (1)

Its left image is saturated. After tensoring with L it is the retained
finite subspace. Saturation therefore identifies it with H_f^1(T).
We obtain an integral isomorphism, not just a rational one:

    Q := H^1(T)/H_f^1(T)  ~=  H^1(M).                 (2)

The representation A has Fil^0 D_dR(A tensor L)=0, whereas
Fil^0 D_dR(M tensor L)=D_dR(M tensor L). Strictness of the de Rham
filtration gives an isomorphism

    Fil^0 D_dR(U) -> D_dR(M tensor L).                 (3)

Naturality of the dual exponential identifies exp*(Q) through (2)-(3)
with exp* H^1(M). Thus the extension class in T contributes no further
unknown local lattice index. Much of the saturation argument was
already implicit in the retained local calculation; it is not claimed
as a newly discovered general cohomological fact.

## 3. A specified de Rham frame; the Gauss sum is retained

First put T0=O(alpha) chi^{-1}, with generator v0. This is Venjakob's
T=O(eta)(r), with eta=alpha and r=-1. Choose the unit unramified
eigenperiod a_alpha used in his (A.61). Set

    e0 = a_alpha t tensor v0,       M0=O e0,
    phi(e0)=p a^{-1} e0,            a=alpha(tau_p) in O^times.

The source specifies tau_p and its Frobenius convention. Reversing that
convention only changes the indicated unramified unit consistently;
it does not change the lattice exponent below. The eigenperiod is
unique only up to an O-unit after choosing an integral generator of its
unramified period lattice.

Fix zeta=zeta_p and write Delta=Gal(Q_p(mu_p)/Q_p). Define

    tau(omega)=sum_{b=1}^{p-1} omega(b) zeta^b.

This has Delta-character omega^{-1}. For an integral generator v_minus
of M=T0 tensor omega, define

    e_minus = tau(omega) a_alpha t tensor v_minus.      (4)

It is a nonzero invariant de Rham vector. It is a frame, not an
assertion that the Gauss sum is a unit or that this is a canonical
modular-form differential. Changing the chosen root of unity or
integral generators multiplies the frame by an O-unit.

In particular the tame Gauss sum has the nonzero valuation

    v_p(tau(omega))=(p-2)/(p-1).                       (5)

For a direct check, expand at zeta=1+X. The coefficient of X^j modulo p
is sum_{b in F_p^times} b binom(b,j). It vanishes for j<p-2 and is
nonzero for j=p-2. The earlier coefficients have valuation at least
one; at X=zeta-1 the j=p-2 term has strictly smaller valuation than
them and every later term. This proves (5). We do not absorb this
factor into an unspecified unit or enlarge O by zeta_p.

## 4. Integral Coleman comparison

Use Venjakob, Appendix A, Proposition A.2(ii), with the coefficient-ring
extension explicitly permitted on printed page 26. Its cokernel is

    M0/(1-p^r phi)M0 = M0/(1-a^{-1})M0 = 0,

because alpha-bar != 1. Its kernel is the Iwasawa torsion submodule,
which is zero here: T0 has no invariant vector over the cyclotomic
extension, its nontrivial residual unramified character remaining
nontrivial there. Hence the Coleman map followed by inverse Mellin is
an INTEGRAL isomorphism

    H^1_Iw(Q_p,T0) ~= O[[Gamma]] e0.                   (6)

This uses the source's integral exact sequence, not an isomorphism
obtained by inverting p.

There is also no hidden integral specialization cokernel at level
K1=Q_p(mu_p). Local Iwasawa duality identifies H^2_Iw(T0) with the
dual of the invariants of (L/O)(alpha^{-1} chi^2) over the cyclotomic
extension. Those invariants vanish: chi restricts to one and
alpha-bar^{-1} remains nontrivial. The standard local Iwasawa
specialization sequence therefore identifies

    H^1_Iw(T0)_{Gamma_1} ~= H^1(K1,T0).               (7)

One may equally obtain (7) from derived Galois descent: its possible
Tor term is H^2_Iw(T0)[gamma_1-1], which is zero. No global main
conjecture or seed Sha hypothesis enters (6)-(7).

Since |Delta|=p-1 is invertible in O, restriction and tame descent
identify H^1(Q_p,M) with the omega^{-1}-eigenspace of H^1(K1,T0),
after the specified twist is removed. Taking that eigenspace is
integrally exact. Under (6)-(7) a generator is represented by

    epsilon = (p-1)^{-1} sum_{b in Delta} omega(b)[b].  (8)

Its augmentation is zero and epsilon^2=epsilon. All tame descent
normalizations have degree p-1, a unit, not p.

## 5. Evaluate the dual exponential of this integral generator

Venjakob (A.67) compares the Coleman map with the dual exponential;
its factorial is (-r)!=1 for r=-1. Formula (A.73), with n=1, K=Q_p,
r=-1, and measure mu, reads

    Psi_{M0,1}(mu e0)
      = [p^{-2} a sum_b mu_b zeta^b
         + p^{-1}(1-p a^{-1})^{-1} aug(mu)] e0.       (9)

Here the map marked pr_n in diagram (A.72) is projection to level n,
not an additional power of p. Frobenius on K-coefficients is trivial;
the coefficient extension O is held fixed, as in the source's
O-valued version.

For (8), the second term of (9) is zero and the first is

    p^{-2} a/(p-1) tau(omega) e0.

There is also a direct check of the two powers of p. For f=(1-phi)F,
the rank-one Frobenius is (p/a) times substitution X -> (1+X)^p-1.
Thus F(0)=f(0)/(1-p/a) and
F(zeta-1)=f(zeta-1)+(p/a)F(0). The map Xi at level one multiplies
this last evaluation by a/p^2. It gives exactly (9). This prevents
confusing the factor p^{-1} from level descent with the additional
p^{-1} from the weight r=-1 Frobenius.

After descent and restoring the twist, this is p^{-2} times an O-unit
times the frame e_minus in (4). The harmless unit depends on the
restriction/induction and eigenbasis convention; its valuation is zero.
More importantly, (6)-(8) show that we evaluated a GENERATOR of the
actual integral cohomology lattice. This proves equality of lattices:

    exp* H^1(Q_p,M) = p^{-2} O e_minus.               (10)

This is stronger than an inclusion for a chosen class. No use is made
of Kato 14.21, whose good-level hypothesis fails here.

## 6. The weight-three index

Let e_g be the unique preimage of e_minus under (3). Then (2) and (10)
prove

    exp*(Q) = p^{-2} O e_g.                          (11)

Write exp*(loc_p^s z_g)=xi_g e_g for the fixed normalized Kato class.
The index in the retained theorem is therefore

    b_g = v_pi(p^2 xi_g).                            (12)

Equivalently, in this specified frame lambda_g=-2 v_pi(p)=-2e.
The p-normalized exponent is exactly -2. Ramified coefficient extension
rescales pi-valuations; it does not create an unknown local loss.
The equality (11) proves the local subproblem for every admitted
specialization and does not estimate xi_g.

The retained inequality now has the fully specified local denominator:

    dim_Fp Sha(E/Q)[p] <= v_pi(p^2 xi_g)-2.           (13)

Thus an independent bound v_pi(p^2 xi_g)<=3 would close the admitted
ordinary primary cases. Neither that bound nor a single new seed
primary vanishing is asserted in this derivation.
