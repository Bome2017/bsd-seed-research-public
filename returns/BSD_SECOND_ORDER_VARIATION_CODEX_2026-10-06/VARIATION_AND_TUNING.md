# Second-order variation and arithmetic tuning in a fixed first-order fiber

2026-10-06. **WRITTEN_DERIVATION; INDEPENDENT_REVIEW_REQUIRED.**

This proof uses the full classical Selmer group, not the strict group in the
separate Aristotle return. The retained Stage-A span and the previous
second-order comparison have their existing provisional grades. No seed
Selmer computation, novelty assertion, formal verification, or BSD theorem
is claimed here.

## 1. Statement and notation

Let k=F_p, p>=5, V=E[p], and S=Sel_p(E/Q), with the retained full residual
image GL_2(k). Let w1,w2 be the independent rational-point classes, and
W=<w1,w2>. Use the tame-character space D, local conditions, and canonical
symmetric forms b_lambda from the bound Stage-A and second-order inputs.
Write

    D^W = {lambda : b_lambda(W,S)=0},
    K_0 = ker[b : D -> Sym^2(S^*)].

The notation K_0 denotes a character space, NOT a number field.
For lambda in D^W put

    q(lambda) = alpha_lambda = h_lambda^(2)(w1,w2).

We derive three assertions.

**Variation.** There is a symmetric bilinear form P on D^W such that

    q(lambda+mu)=q(lambda)+q(mu)+P(lambda,mu).                 (1)

It has the following arithmetic description. Put A=k[t]/t^2 and
M_lambda=V tensor A, with twist 1+t lambda. Choose Selmer lifts X1,X2
of w1,w2 to M_lambda, and set

    J(f,g)=[t]e(f(t),g(-t)),
    C_mu^lambda(X,Y)=CTP_[0->M_lambda->M_lambda(mu)->M_lambda->0]
                          (X,J(Y,-)),                      (2)

where M_lambda(mu) has coefficient ring k[t,s]/(t^2,s^2) and
twist (1+t lambda)(1+s mu); the injection in (2) is multiplication
by s. With j(y)=e(y,-), the sign in our convention is

    P(lambda,mu) = -C_mu^lambda(X1,X2).                     (3)

**Arithmetic nondegeneracy.** For every nonzero lambda in K_0 there
is an actual mu in K_0, using two new tame conductor primes, for which

    P(lambda,mu) != 0.                                    (4)

Thus P|K_0 has zero radical. This is a statement about the actual
arithmetic character space; it is not inferred from an abstract matrix
model or from the size of D.

**Fiber tuning.** For every B in the image of b whose radical is W,
there is a nonzero lambda with

    b_lambda=B,              q(lambda)=0.                  (5)

The retained Stage-A span supplies such B. The preceding return then
gives Selmer lifts of both w1,w2 to

    V tensor k[u]/u^3,    twist exp(u lambda),              (6)

with no additional second-order character eta. Under the retained
mixed-characteristic identification, (6) is reduction modulo pi^3 of

    T_lambda = T_pE tensor Z_p[zeta_p](chi_lambda),
    chi_lambda = zeta_p^[lambda],    pi=zeta_p-1.

This solves the proposed order-three existence gate at written-proof
grade, conditional on the retained inputs. It does not solve the
all-order lifting or determinant/global-support gates.

## 2. Local conditions and the two-variable construction

For any finite collection of characters use the union of their tame
supports. At Sigma all characters vanish; use the polynomial-coordinate
copies of the original Kummer condition. At a new ramified prime the
residual representation has H^0=H^1=H^2=0; filtration by copies of V
gives the same acyclicity for every finite module below. Elsewhere use
the unramified conditions. Polynomial injections, quotients and the
diagrams below are exact in Morgan--Smith's SMod category.

In particular the local conditions on M_lambda are self-annihilating
for J: at Sigma this is coefficientwise Kummer duality, at the new
primes acyclicity, and elsewhere unramified duality. No ordinary
filtration is used.

Let lambda,mu belong to D^W, and form

    R_3=k[t,s]/(t,s)^3,  R_2=k[t,s]/(t,s)^2,
    U_3=V tensor R_3,    U_2=V tensor R_2,

with scalar action exp(t lambda+s mu). These are genuine finite
Galois modules: exponential multiplication is valid in total degree
at most two since 2 is invertible in k.

For a class x in W choose first lifts with cocycle representatives

    x+t a_lambda,       x+s a_mu.

They combine into x+t a_lambda+s a_mu in Sel(U_2). To justify this
at the level of cocycles rather than just classes, representatives can
be adjusted by coboundaries so that both constant terms are the same
chosen cocycle x. The degree-one equations and the local conditions
are linear, so their sum is a Selmer cocycle in U_2.

The sequence

    0 -> V tensor <t^2,ts,s^2> -> U_3 -> U_2 -> 0          (7)

has a generalized Cassels--Tate obstruction. Pair its three top
coordinates with j(y), y in W. Naturality under s=0, t=0 and
(t,s)=(u,u), respectively, identifies these values as

    h_lambda^(2)(x,y),
    h_mu^(2)(x,y),
    h_(lambda+mu)^(2)(x,y).

The last value is the sum of the three coordinate values, because
t^2,ts,s^2 all map to u^2. This follows from linearity in the dual
argument in (7); it does not assume a base-change theorem for global
Selmer groups. In particular the mixed coordinate is

    h_(lambda+mu)^(2)(x,y)
      -h_lambda^(2)(x,y)-h_mu^(2)(x,y).                    (8)

All lift ambiguities vanish on W: they contribute rows of b_lambda
or b_mu, and both forms kill W. This proves that (8) is canonical.

For reference, its global connecting cocycle is

    lambda cup a_mu + mu cup a_lambda
                    + (lambda mu) cup x,                 (9)

where (lambda mu)(g)=lambda(g)mu(g) is a pointwise product of
one-cochains, not the two-cocycle lambda cup mu. The expression (9)
alone would not capture the local Selmer obstruction; (7) does.

## 3. Identify the mixed coordinate and prove bilinearity

Quotient (7) by its t^2 and s^2 kernel coordinates. Put

    U=V tensor k[t,s]/(t^2,s^2),
    P_1=V tensor k[t,s]/(t^2,ts,s^2).

There is a morphism of exact SMod sequences

    0 -> V       --ts--> U -> P_1      -> 0
         | t             | id  | s=0
    0 -> M_lambda --s--> U -> M_lambda -> 0.               (10)

The first lift in P_1 maps to X1 in the lower quotient. On the left,
the dual pullback of J(X2,-) is

    z |-> J(X2,t z) = -e(w2,z) = -j(w2)(z).

Morgan--Smith naturality applied to (10) gives exactly (3). This also
fixes the minus sign; no guess based on polarization conventions is used.

For fixed lambda and fixed X1,X2, the lower extension in (10) is
linear in mu under Baer sum, with the same local conditions. Therefore
(3) is linear in mu. Interchanging t and s in (7) shows symmetry in
lambda and mu. It is consequently bilinear in both variables.

Scaling u gives q(a lambda)=a^2 q(lambda), including a=0. Setting
mu=lambda in (1) gives P(lambda,lambda)=2q(lambda).

For a fixed first-order fiber b_lambda=B and mu in K_0, the requested
addition law is therefore

    alpha_(lambda+mu)-alpha_lambda
             = alpha_mu - C_mu^lambda(X1,X2).             (11)

Neither term in (11) is an unspecified normalization unit. Both are
pairings of actual finite Galois modules with fixed identifications.

## 4. A joint evaluation lemma for the nonsplit lifted module

Fix NONZERO lambda in K_0 for the rest of Sections 4--6. Every class
of S has a first Selmer lift to M_lambda, since b_lambda is zero.
Take a basis x1=w1,x2=w2,x3,...,xd of S and choose lifts X_i.

The field cut out by (rho,lambda) has group

    G_lambda = GL_2(k) x C_p.                              (12)

Indeed the degree-p field cut out by lambda ramifies at some tame
good prime where Q(E[p]) is unramified. A degree-p field intersecting
Q(E[p]) nontrivially would be contained in it, which is impossible
by that ramification. This proves (12), not just a subgroup inclusion.

Let J_lambda=ker(rho,lambda). On J_lambda each X_i is a homomorphism.
The joint evaluation image

    N = image[J_lambda -> M_lambda^d]

is a k-vector space stable under G_lambda. An element (I,1) acts as
1+t, so tN is contained in N; it is an A-submodule.

Reduction modulo t is onto V^d. Here are the necessary details.
A central nonidentity scalar (aI,0) in G_lambda acts on V as a.
Central-scalar cohomology vanishing gives H^1(G_lambda,V)=0.
Inflation--restriction implies that the independent residual classes
x_i remain independent on J_lambda. Their evaluation image is a
G_lambda-submodule of V^d. If it were proper, a simple quotient would
give a nonzero linear relation among the x_i, since V^d is a direct
sum of simple copies of V and End_Glambda(V)=k. Thus

    N+t M_lambda^d=M_lambda^d.

Nakayama's lemma over A=k[t]/t^2 now gives

    N=M_lambda^d.                                        (13)

This does NOT apply Maschke's theorem to a group of order divisible
by p. The only semisimple module used is V^d; the nonsplit part is
handled by the actual (I,1) action and Nakayama. The basis and lifts
are proof witnesses, not an assumption that the seed's Selmer group
has been computed.

## 5. Simultaneously read the old and lifted obstruction forms

The self-dual module M_lambda has symmetric coefficient pairing J.
For each i,j choose a continuous primitive

    d U_ij = X_i cup_J X_j.

Such primitives exist: the cup class vanishes locally by the specified
self-annihilating Selmer conditions, hence globally by Brauer--Hasse--
Noether and the field Kummer sequence. For the old residual classes
choose primitives u_ij of the corresponding evaluation cup products.
All these cochains have finite image and factor through finite
quotients. Enlarge a finite set Pi to include Sigma, the support of
lambda, and their ramification.

We will use new conductor-prime characters mu_q that vanish locally
at every prime of Pi and have

    (rho(Frob_q),lambda(Frob_q))=(-I,0).                   (14)

They lie in D. The relevant local cohomology vanishes for M_lambda
as well as V. The cochain formula in Morgan--Smith Definition 3.2,
substituted just as in Stage A, says that the tame contribution for
any coefficient pairing beta and lifted classes X,Y is the common
tame normalization times

    z_gamma(X,Y)=U(gamma)-beta(A_X,Y(gamma)),
    A_X=(gamma-1)^(-1)X(gamma).                           (15)

For M_lambda take beta=J. For V, the evaluation convention with
j(y)=e(y,-) gives beta(x,y)=e(y,x). The possible overall sign relative
to a convention writing e(x,y) does not affect the zero calculation
below. We normalize each mu_q so that its local invariant evaluates
mu_q cup z as z(Frob_q). This one scalar normalization is used for
all old and lifted entries simultaneously.

The exact compatibility of (14) and local vanishing at Pi needs a
field intersection check. Put

    R=Q(mu_p, a^(1/p): a is a rational prime in Pi).

Then

    Q(E[p],lambda) intersect R = Q(mu_p).                  (16)

For clarity, R/Q is solvable. The commutator subgroup SL_2(k) of
GL_2(k) is perfect for p>=5, so any common solvable quotient of
GL_2(k) x C_p is abelian. On the other hand the abelianization of
Gal(R/Q) has no extra p-part: conjugation by a nonidentity element
of Gal(Q(mu_p)/Q) acts on its Kummer p-group by the cyclotomic
scalar, so that whole p-group is in the commutator subgroup.
Its maximal abelian subfield is Q(mu_p). This proves (16).

Consequently one may choose gamma with (rho,lambda)(gamma)=(-I,0)
and trivial action on R. A Chebotarev prime for it has q=1 mod p
and makes every prime in Pi a p-th power modulo q. The degree-p
conductor-q character is therefore locally zero at Pi. Infinity is
automatic because p is odd.

## 6. A commutator changes the mixed pairing but leaves EVERY old row zero

Choose e1,e2 in V with e(e1,e2)=1. By (13), choose v,w in J_lambda
with the following exact joint values:

    X1(v)=t e1,      X_i(v)=0 for i!=1;
    X2(w)=e2,        X_i(w)=0 for i!=2.                   (17)

In particular every residual x_i(v) is zero. Put c=[v,w]. Because
J_lambda acts trivially on all coefficient modules, its cocycle
restrictions are homomorphisms, so X_i(c)=x_i(c)=0.
Also c fixes R: J_lambda fixes mu_p and acts on R through an
abelian Kummer p-group.

For a primitive dU=X cup_beta Y on J_lambda the inhomogeneous
cochain equation gives

    U([v,w])=-beta(X(v),Y(w))+beta(X(w),Y(v)).              (18)

Thus for EVERY old pair i,j,

    u_ij(c)=0,                                           (19)

whereas for the lifted pair 1,2,

    U_12(c)=-J(t e1,e2)=-1.                              (20)

Choose two distinct rational primes q0,q1 with marked Frobenius
gamma and gamma c in a finite Galois quotient recording the modules,
cochains and R. Chebotarev permits this outside all the finite sets
already used. The markings specify the representatives, not only
their conjugacy classes. Both characters mu_0,mu_1 satisfy (14) and
the Pi-local vanishing, and both are normalized as in (15).

Because all X_i(c) and x_i(c) are zero, the A_X and cocycle terms
in (15) agree for gamma and gamma c. The determinant of rho(gamma)
is one, so its action on mu_p is trivial. Their differences in
(15) are exactly (19)--(20). Put

    mu=mu_1-mu_0.

Baer linearity gives

    b_mu(x_i,x_j)=0 for every i,j,
    C_mu^lambda(X1,X2)=-1.                               (21)

Hence mu belongs to K_0 and (3) gives P(lambda,mu)=1 in the stated
normalization. In particular it is nonzero, independent of a global
choice of sign convention. The two conductor primes are new, so mu
is a genuine nonzero character, not a formal difference in a model.

This proves (4). It is essential to prescribe the TOP coefficient
t e1 in (17). Prescribing only residual values reproduces the old
first-order forms and does not prove (21).

## 7. Solve the affine quadratic equation

D is infinite-dimensional: arbitrarily many distinct admissible
conductor lines exist by the same Chebotarev/radical-field argument,
and they are independent by ramification. The image of b is finite-
dimensional, so K_0 is infinite-dimensional.

By (4), P|K_0 has zero radical. Since p is odd, q(v)=P(v,v)/2.
One can therefore find a two-dimensional subspace U of K_0 on
which P is nondegenerate. Here is an explicit finite-dimensional
argument, without confusing infinite dimension with automatic tuning.
First choose e with q(e)!=0, using polarization if necessary. Its
orthogonal complement is infinite-dimensional. Choose a nonzero z
in that complement. If q(z)!=0, span(e,z) works. Otherwise use
(4) to choose h with P(z,h)!=0; then span(z,h) has Gram determinant
-P(z,h)^2!=0. Only finitely many characters are involved.

Fix lambda_0 with b_lambda0=B. On U find v with

    P(v,u)=P(lambda_0,u) for every u in U.

This is possible because P|U is nondegenerate. Equation (1) becomes

    q(lambda_0+u)=q(u+v)+q(lambda_0)-q(v).                 (22)

A nondegenerate binary quadratic form over k represents every element
of k. To prove the exact assertion needed here, diagonalize it as
a x^2+b y^2 with a,b nonzero. For a specified r, the two subsets
{a x^2} and {r-b y^2} both have (p+1)/2 elements, so they intersect.
Thus choose u satisfying q(u+v)=q(v)-q(lambda_0). Then (22) is zero
and b_lambda0+u remains B.

If B!=0 the resulting character is automatically nonzero. If B=0
(here rad B=W forces S=W), a nonzero isotropic vector in K_0 is
available using a nondegenerate three-dimensional subspace: represent
minus its third diagonal coefficient by its first two variables and
take the third coordinate to be 1. Such a three-dimensional subspace
exists by the same nondegeneracy and orthogonal-complement argument.
This also handles the nontrivial-character requirement in (5).

More strongly, for B!=0 the same proof represents ANY prescribed
value of alpha in the fiber. In particular alpha does not descend
to a function of b alone. The arithmetic proof (21), rather than
scaling or dimension counting, is what makes this conclusion possible.

## 8. Convert the zero into actual order-three lifts

Take the character in (5). Since rad b_lambda=W,

    image b_lambda=Ann(W).

The obstruction functional for each chosen first lift of wi restricts
to zero on W because q(lambda)=0 and the second pairing is alternating.
It is therefore a row of b_lambda. Change the first lift by t z_i
to cancel that row, as in the retained second-order proof. The
Cassels--Tate kernel theorem now gives Selmer lifts to M_3(lambda)
with the unchanged character exp(u lambda), not an independently
chosen exp(u lambda+u^2 eta).

For O=Z_p[zeta_p] and pi=zeta_p-1, p is a unit times pi^(p-1).
For p>=5 the quotient O/pi^3 has characteristic p; with
u=pi-pi^2/2 it identifies with k[u]/u^3 and

    chi_lambda=1+u lambda+u^2 lambda^2/2.

The retained matching local conditions give the announced pi^3 Selmer
lifts. No p-adic logarithm of zeta_p is used. The congruence coordinate
u is only a truncated polynomial parameter.

## 9. Quantifiers, scope and the remaining endpoint

The conclusion is: for each good seed p>=5 satisfying the retained
inputs, and each attainable first-order B with rad B=W, there EXISTS
a finite-support tame character giving the prescribed B and alpha=0.
There is no numerical conductor bound, no algorithm supplied for
computing S, and no explicit seed character evaluated in this return.
The proof does not assume S=W or Sha[p]=0. It works with arbitrary
finite dimension of S, so it cannot itself be a bound on that dimension.

The full-S Stage-A span is needed to know that a B with radical W is
attainable. The variation and arithmetic nondegeneracy proofs use
the actual first-order modules, local conditions and retained residual
image, without treating Aristotle's strict-space result as a full-S
certificate. All new arithmetic steps in Sections 4--6 need independent
review; exact finite algebra controls are insufficient to certify them.

The concurrent lab review c4f53313 places a separate gate at ALL orders:
compatible nonzero Selmer lifts for T_lambda imply a nonzero rational
twisted Selmer space, and Kato's theorem forces the corresponding
central twisted L-value to vanish. Finite pi^3 lifts do not imply this.
This return neither constructs that zero nor identifies alpha with a
Mazur--Tate coefficient. It does not revive the superseded rank-two
OpenAI submission or an impossible fixed-tame F_p[[t]] family.

FIN, ORDER9 and Q36 are unchanged. The precise mathematical increment
claimed here is a proposed proof that the requested finite-order
tuning problem is solvable, rather than another name for its scalar.
