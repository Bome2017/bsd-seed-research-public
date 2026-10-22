# The common second-order correction: an exact criterion

2026-10-06. **WRITTEN_DERIVATION; INDEPENDENT_REVIEW_REQUIRED.**
The spanning assertion from Stage A is retained provisionally, not re-certified
here. Everything below is conditional on that assertion and its stated seed
inputs. No claim of novelty, formal verification, or BSD completion is made.

## 1. Statement

Use the actual classical Selmer group S, the rational-point plane
W=<w1,w2>, and the tame-character space D defined in the bound Stage-A input.
Let k=F_p, p>=5, and fix lambda in D^W. Write M_n for

    V tensor k[t]/t^n,   g acting by rho(g) exp(t lambda(g)),

for n=1,2,3,4. These truncated exponentials are genuine characters:
all denominators through 3! are units. Give them the local conditions of
Section 2 below. Set R_lambda=ker b_lambda, so W is contained in R_lambda.

We derive:

1. Every b_eta (eta in D) is symmetric. Combined with Stage A, the image of
   D in bilinear forms on S is exactly Sym^2(S^*).
2. There is a well-defined alternating second obstruction

       h_lambda^(2): R_lambda x R_lambda -> k.

   It is defined using actual Selmer lifts and the generalized Cassels--Tate
   pairing, not an arbitrary formal complex.
3. For ANY prescribed first-order Selmer lifts of w1,w2, ONE eta in D
   makes BOTH lifts extend through t^2, with character

       1+t lambda+t^2(lambda^2/2+eta),

   if and only if

       alpha_lambda := h_lambda^(2)(w1,w2) = 0.                 (1)

4. If ker b_lambda=W, condition (1) is also equivalent to obtaining both
   second-order lifts with eta=0, after changing the first-order lifts.

Thus the off-plane obstruction terms can be solved using the existing
Stage-A theorem. A single alternating compatibility value cannot be
changed by eta or by changing the first lifts. Its value for any useful
seed direction has NOT been computed or proved zero in this return.

## 2. Exact local conditions at each truncated order

At Sigma every character in D is locally zero. Use the direct sum of n
copies of the genuine Kummer local condition in the polynomial coordinates.
At any new ramified prime q, rho(Frob_q)-1 is invertible; the residual
H^0,H^1,H^2 at q all vanish, by local duality and the local Euler
characteristic. Filtration by V proves the corresponding vanishing for
every M_n used here. The local condition is zero. Elsewhere use the
unramified condition.

These conditions make all the polynomial inclusion and quotient sequences
below exact in Morgan--Smith's category SMod. At Sigma this is split exactness;
at the new primes all the cohomology is zero; elsewhere the unramified
condition has the required exactness by procyclic residue cohomology.
In particular, the arguments are unchanged at a supersingular coefficient
prime: no ordinary local condition is introduced.

For eta with additional tame support use the union of the two supports.
At its new primes the same acyclicity applies to every module in the
comparison. Consequently the Baer-sum comparison below also respects the
local conditions, rather than merely the underlying representations.

## 3. First-order symmetry, including the sign

Let e:V x V -> mu_p be the alternating Weil form, written additively.
Put j(x)=e(x,-). Define the Galois-equivariant perfect pairing on M_n by

    J_n(f,g) = [t^(n-1)] e(f(t),g(-t)).                       (2)

The scalar twists cancel between t and -t. Direct coefficient comparison
gives

    J_n(g,f)=(-1)^n J_n(f,g),
    J_n(tf,g)=-J_n(f,tg).                                   (3)

The local conditions are mutual annihilators under these pairings:
at Sigma use Kummer isotropy coefficient by coefficient, at new primes
use zero cohomology, and at the other primes use unramified duality.

For E1=[0 -> V --t--> M2 -> V -> 0], J2 is symmetric. Its induced
maps from E1 to the dual exact sequence are j on the left and -j on the
right: explicitly J2(tx,z)=e(x,z0), whereas J2(z,tx)=-e(z0,x).
Apply Morgan--Smith Theorem 1.3, duality and naturality. Since
j^vee beta=-j, the two minus signs cancel, giving

    b_lambda(x,y)=b_lambda(y,x).                             (4)

This is a symmetry statement about this scalar-twist extension. It is not
the assertion that every Cassels--Tate pairing is symmetric.
Baer linearity and the retained Stage-A spanning theorem now give

    {b_eta: eta in D}=Sym^2(S^*).                            (5)

## 4. The actual second obstruction and its lift ambiguity

Apply the same theorem to

    E2=[0 -> V --t^2--> M3 -> M2 -> 0].

For x_tilde in Sel(M2) define

    O_lambda(x_tilde,y)=CTP_E2(x_tilde,j(y)),   y in S.       (6)

Its vanishing for every y is NECESSARY AND SUFFICIENT for x_tilde to
lift to Sel(M3). This retains the local obstructions as well as the
global cocycle equation.

The image of Sel(M2) in S is R_lambda, by the first-order kernel theorem.
Two lifts of the same x differ by t z for some z in S. To see that the
ambiguity is exactly this, apply global cohomology to E1 and then the
inverse-image local conditions; H^0(Q,V)=0 follows from full residual image.

Pulling E2 back along V --t--> M2 gives E1. Naturality therefore gives

    O_lambda(x_tilde+t z,y)
      = O_lambda(x_tilde,y)+b_lambda(z,y).                   (7)

For y in R_lambda the last term vanishes, by symmetry. Hence

    h_lambda^(2)(x,y)=O_lambda(x_tilde,y),   x,y in R_lambda (8)

is well-defined and bilinear, independent of the chosen first lift.

## 5. Alternation without importing an unmatched height theorem

Use the actual order-four module to form

    E22=[0 -> M2 --t^2--> M4 -> M2 -> 0].

J4 and J2 from (2) are symmetric. They identify this exact sequence with
its dual with J2 on BOTH endpoints: the factor t^2 has positive sign.
Therefore the pairing

    C(u,v)=CTP_E22(u,J2(v,-)),  u,v in Sel(M2),

is symmetric by Theorem 1.3. Multiplication by t is an endomorphism of
the sequence, and its adjoint for J2 is -t by (3). Naturality gives

    C(tu,v)=-C(u,tv).                                       (9)

There is also a morphism E22 -> E2: reduction M4 -> M3 in the middle,
constant-term projection M2 -> V on the left, and the identity on the
right. The pullback of j(y) to M2^vee is J2(t y_tilde,-), for ANY first
lift y_tilde of y. Thus

    O_lambda(x_tilde,y)=C(x_tilde,t y_tilde).                (10)

Using symmetry of C and (9), the right side equals
-C(y_tilde,t x_tilde). Equations (8)--(10) prove

    h_lambda^(2)(x,y)=-h_lambda^(2)(y,x).

Since p is odd this pairing is alternating. This finite-module proof uses
no ordinary filtration, no conjectural height comparison, and no formal
character over k[[t]]. In particular M4 exists even when such a formal
character does not; see CHARACTER_REALIZATION.md.

## 6. What the SAME eta can change

Write M3,eta for the actual module with character

    exp(t lambda+t^2 eta) mod t^3.

As an extension of M2 by V, its difference from E2 is the pullback of
E_eta=[0 -> V -> M_eta -> V -> 0] along M2 -> V. This can be checked
directly: the difference in the action's top coefficient on
(x0,x1,x2) is eta(g) rho(g)x0. Its lower two coefficients agree.
The local checks in Section 2 make this also a Baer-sum identity in SMod.
Consequently

    O_lambda,eta(x_tilde,y)
      =O_lambda(x_tilde,y)+b_eta(x,y),   x=x_tilde mod t.    (11)

Choose a linear section over W using the two specified first lifts, and
put O(x,y)=O_lambda(x_tilde,y) for x in W, y in S.

An elementary extension lemma says that a bilinear map W x S -> k extends
to a symmetric form on S if and only if its restriction to W x W is
symmetric. Proof: extend a basis of W to S; the W rows determine the W
columns, and the remaining square block may be chosen arbitrarily
symmetric. The basis proves existence; it does not define the obstruction.

By (5), every such symmetric extension is b_eta for an ACTUAL eta in D.
Thus (11) can vanish for all x in W and y in S exactly when O|W x W
is symmetric. But that restriction is h_lambda^(2)|W x W, which is
alternating. It is both symmetric and alternating iff it is zero.
Because dim W=2, this is exactly alpha_lambda=0.

This proves (1) in both directions, for the same eta and for arbitrary
prescribed first lifts. In particular

    O_lambda,eta(w1_tilde,w2)
      -O_lambda,eta(w2_tilde,w1)=2 alpha_lambda.             (12)

No common eta can change this difference. Equation (7) shows that
changing the first lifts cannot change it either.

Equivalently, the cokernel of the available correction map is explicitly

    coker[D -> Hom(W,S^*)] = wedge^2 W^*,

where the map to the cokernel sends O to O(x,y)-O(y,x) on W. It is a
one-dimensional cokernel, not two independently adjustable scalar tests.

## 7. A repair compatible with a genuine root-of-unity character

Stage A permits choosing lambda with ker b_lambda=W: take a nondegenerate
symmetric form on S/W and pull it back, then use (5). This is an existence
argument, not an efficient procedure for finding the seed's Selmer group.
If S=W, a nonzero lambda with b_lambda=0 exists because D has infinitely
many independent conductor lines whereas the space of forms is finite
dimensional. The Stage-A Chebotarev construction supplies those lines.

Suppose now ker b_lambda=W. Then im b_lambda=Ann(W). If alpha_lambda=0,
each O_lambda(wi_tilde,-) vanishes on W, so choose z_i in S satisfying

    b_lambda(z_i,-)=-O_lambda(wi_tilde,-).

Equation (7) shows that wi_tilde+t z_i extends to Sel(M3) with eta=0.
Conversely any such two lifts force alpha_lambda=0.

Therefore, for these directions, the common-eta freedom can be eliminated
entirely by correcting the first lifts. That matters: the root-of-unity
realization in CHARACTER_REALIZATION.md supplies eta=0, but does not
supply all the independent eta choices available over k[t]/t^3.

More generally, with eta=0 and no assumption R_lambda=W, liftability after
changing the first lifts is equivalent to h_lambda^(2)(W,R_lambda)=0,
since im b_lambda=Ann(R_lambda). Merely testing W x W is then insufficient.

## 8. What has and has not been established

This is a complete written solution of the correction-map calculation,
conditional on the retained Stage-A span. It does NOT prove alpha_lambda=0
for a useful seed direction. In particular it is not an unconditional
SECOND_ORDER_W_LIFT, nor a computed SECOND_ORDER_OBSTRUCTION for the seed.

The honest status is SECOND_ORDER_COMMON_CORRECTION_CRITERION.
Neither the pairing symmetry nor the existence of many directions supplies
a theorem selecting lambda with BOTH ker b_lambda=W and alpha_lambda=0.
Rescaling lambda cannot do it: substituting t -> a t gives
alpha_(a lambda)=a^2 alpha_lambda for a nonzero in k.

Formal models with first coefficient diag(0,0,1,1) and second coefficient
a nonzero alternating 2x2 block on W obey the relevant adjoint symmetry
and fail (1). They are controls on a logical inference, not seed examples.

FIN, exceptional primary finiteness, ORDER9 and Q36 remain unchanged.
Do not turn this calculation into repeated coefficient-generation runs.
The actual arithmetic task, if this mechanism is pursued, is to control
this second pairing while keeping a useful first-order form, in an
arithmetically realizable coefficient ring.
