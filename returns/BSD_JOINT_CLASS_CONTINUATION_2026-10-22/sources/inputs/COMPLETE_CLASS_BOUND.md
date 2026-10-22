# A complete, coarse relative class bound for the actual seed at five

Status: **written deduction under retained exact field inputs; exact outward
arithmetic checked.** No GRH, elliptic BSD, known Sha order, collected-relation
completeness, or full class-group computation is assumed. This is not a small
enough bound to close the source or FIN.

Let A be the actual degree-24 seed point field at coefficient five. Let
K=A^{<tau>}, where tau is scalar -1; let sigma be scalar 2, of order four,
so tau=sigma^2. The retained exact field construction gives signatures
(4,10) for A and (4,4) for K, and the maximal-order discriminants in
FIELD_INPUTS.json. Write

    delta = N_K/Q(d_{A/K}) = 2^4 * 5 * 4547^6
          = 707033045140895852346320,
    Q = D_K delta = D_A/D_K.

This Q is an analytic conductor expression, not an elliptic BSD quotient.
The claim established here is

    |ker(N:Cl(A)->Cl(K))| = h_A/h_K <= 262 * 10^66 < 5^98.

Consequently the length of its entire five-primary part is at most 97.
In particular, if chi_2(sigma)=2 and chi_3(sigma)=3 over F_5, then

    dim Cl(A)[5]^{chi_2} + dim Cl(A)[5]^{chi_3} <= 97.       (1)

These are ordinary ideal class groups. No assertion that the actual
dimension equals 97 is made, and the two character dimensions are not
assumed equal.

## 1. The logarithm metric and the relative unit lattice

Both fields have a real embedding, so their only roots of unity are +/-1.
Their unit ranks are 13 and 7. Exactly two real places of K split into two
real places of A; the other two become complex. Each of the four complex
places of K has two complex places above it.

Put E={u in O_A^*:N_A/K(u)=1}. Its rank is six. A unit of relative norm
which is a root of unity must have norm +1: at a real place becoming
complex the norm is positive, so it cannot be -1. Thus the kernel of the
norm map on the unit groups modulo roots of unity is exactly E/{+/-1}.

Use the all-embedding map

    Log_L(u) = (log|rho(u)|)_{rho:L->C},

with both conjugate complex embeddings included as separate coordinates
and the ordinary Euclidean metric. For u in E, each pair of embeddings
over an embedding of K has coordinates x,-x. Above each of the two
ramified real places these are both zero. There are therefore at most
20 nonzero coordinates in Log_A(u).

For u not in {+/-1}, u cannot belong to K, because its norm there would
be u^2=1. It generates the quadratic extension A/K. Its monic polynomial
is X^2-(u+u^{-1})X+1. The integral order O_K[u], free with basis 1,u,
has discriminant ideal ((u-u^{-1})^2). The field discriminant ideal
divides this order discriminant, hence

    delta <= |N_K/Q((u-u^{-1})^2)|.

For each embedding of K, choose an extension rho to A and set
x=log|rho(u)|. The triangle inequality gives
|rho(u-u^{-1})| <= 2 exp(|x|), including complex rho. Taking all twelve
K embeddings, counted with complex multiplicity, gives

    log(delta) <= 24 log(2) + ||Log_A(u)||_1
               <= 24 log(2) + 2 sqrt(5) ||Log_A(u)||_2.

Thus every nonzero vector of the rank-six relative logarithm lattice has
length at least

    lambda = [log(delta)-24log(2)]/[2sqrt(5)] > 0.          (2)

Write V for its Euclidean covolume. Applying Minkowski's convex body
theorem to six-dimensional balls of radius less than lambda, and then
taking the limiting radius, gives

    V >= vol(B_6) lambda^6/2^6 = pi^3 lambda^6/384.        (3)

This bounds the full relative unit lattice, not just a group generated
by units found so far. The unknown unit index has not been discarded.

## 2. Conversion to the standard regulator, retaining its unit index

Let R_L be the usual regulator with real coordinate log|rho(u)| and
complex coordinate 2log|rho(u)|, deleting any one coordinate to take a
determinant. If V_L is the covolume for the all-embedding metric above,
then

    V_L = sqrt([L:Q]) R_L / 2^{r_2(L)/2}.                (4)

Here is a direct metric check. Let B be the matrix of weighted logarithms
before deleting a row. All maximal minors have absolute value R_L,
because the rows sum to zero. The all-embedding metric in these weighted
coordinates is diag(1,...,1,1/2,...,1/2). Cauchy--Binet gives

    det(B^t G B) = R_L^2 2^{-r_2}(r_1+2r_2),

which proves (4).

The embedded base unit lattice is orthogonal to the relative lattice:
over each K embedding its coordinates are repeated, while the relative
coordinates sum to zero. Base embedding multiplies all lengths by
sqrt(2), so its seven-dimensional covolume is 2^{7/2}V_K.

Let I=[U_A:U_K E], with roots of unity included in both groups. The norm
identifies

    U_A/(U_K E) = N(U_A)/U_K^2.

This index is finite. The quotient on the right injects into
U_K/( {+/-1} U_K^2): a norm which equals -v^2 is negative at a ramified
real place and is impossible. This is the sign condition needed to get
I<=2^7, rather than merely 2^8. In particular, I is a power of two.

The orthogonal product of the base and relative lattices has index I
in the full A unit lattice. Hence

    V_A = 2^{7/2} V_K V/I,
    R_A/R_K = 64 V/I >= V/2 >= pi^3 lambda^6/768.         (5)

No relative regulator or fundamental unit has been computed or assumed.

## 3. The whole relative class group, including ungenerated classes

The extension A/K is quadratic and ramified at finite primes, as witnessed
by delta. Let H_K be the ordinary Hilbert class field of K. The
intersection A cap H_K is K, since A/K is ramified. For every ordinary
ideal class c of K, Chebotarev in the compositum A H_K produces a prime
of K whose Artin class in H_K is c and whose Frobenius in A/K is trivial.
It splits in A. A prime above it then has relative ideal norm that prime
of K. Thus the class norm is surjective and

    |ker(N:Cl(A)->Cl(K))|=h_A/h_K.                       (6)

This argument concerns all ideal classes, without assuming any selected
prime ideals generate them.

On five-primary class groups extension j is injective because Nj=2.
Also jN=1+tau. It follows that the norm kernel there is the tau=-1
component. Each chi_2 and chi_3 satisfies chi_i(tau)=-1; their direct sum
is exactly that anti component after reduction modulo five. Hence its
five-primary length bounds the sum in (1). This does not need a
five-unit comparison between independently chosen scalar characters.

## 4. Independent analytic upper estimate

Let psi be the primitive quadratic ray class character of K associated
with A/K. Its finite conductor norm is delta (the quadratic
conductor-discriminant formula), and

    zeta_A(s)=zeta_K(s)L_K(s,psi).

The analytic class number formula in the standard regulator convention
is

    Res_{s=1} zeta_L(s) = 2^{r_1}(2pi)^{r_2} h_L R_L
                         / (w_L sqrt(D_L)).

Here r_1 agrees in A and K, w_A=w_K=2, and the difference in r_2 is six.
Taking the ratio yields the exact positive identity

    h_A/h_K = sqrt(Q) L_K(1,psi) / [(2pi)^6(R_A/R_K)].   (7)

Louboutin, Theorem 4(1), equation (10), printed page 1197, applies to an
arbitrary degree-m number field and a primitive ray class character,
with f the norm of the finite conductor:

    |L_K(1,psi)| <= 2 [e log(D_K f)/(2m)]^m.

Take m=12 and f=delta. The bound permits ramification at infinity.
The different infinity-unramified hypothesis in his Theorem 5 is not
being used. Neither is his specialized CM class-number formula: A is
not CM. Combining (2), (5), and (7) gives

    h_A/h_K <= sqrt(Q) * 2(e log(Q)/24)^12
               / [(2pi)^6 * (pi^3 lambda^6/768)].        (8)

This is an independent arithmetic upper bound, not an equality involving
an unknown seed Sha group or an uncomputed generator deficiency.

## 5. Exact outward evaluation

certify_analytic_bound.py uses only Python integer and rational
arithmetic. Logarithms use the positive atanh series after power-of-two
range reduction, with a geometric remainder bound; e uses its factorial
series with a geometric remainder; pi uses Machin's identity and the
alternating arctangent remainder. Square-root upper bounds are verified
by integer or rational squaring. Every rounded constant points outward.

The exact result is recorded in EXACT_BOUND.json. In particular,

    h_A/h_K <= 262 * 10^66 < 5^98,

and therefore the five-primary length is at most 97. The earlier
ANALYTIC_DIAGNOSTIC.json is explicitly floating-point diagnostic data;
it is not the acceptance certificate. The new script's acceptance does
not use it.

## 6. Relevance and limits for the complete source bound

For either named faithful character, the full unit contribution has
dimension three. On the retained primitive source and valuation domain
at five, the extra valuation contribution is zero. Thus this supplies
the coarse complete-source ceiling 3+97=100 before imposing any
authenticated norm or local conditions. Known independent unit-norm
rows may be subtracted in the existing exact-sequence bound; unknown
class maps may not. Passing to an S-class quotient can only decrease the
class contribution. Any further source cofactor/index must retain its
previously checked five-unit hypothesis.

The number 100 is nowhere near the rank-two target. The earlier 8,918
selected character columns were a GRH-conditional generator budget,
not an unconditional class-rank estimate; the two numbers are different
types of information. This result supplies an unconditional coarse
ceiling on every class-supported direction. It does not show that the
class contribution is small, certify the current relation collection
as complete, or supply an across-prime upper estimate. FIN, ORDER9,
and Q36 are unchanged.

The failed zero-value shortcut is also explicit: zeta_A/zeta_K has
vanishing order six at s=0, the relative unit rank. Its leading term
contains the relative regulator. A CM-minus algebraic L(0) class-number
calculation cannot be imported into this signature. No claim that all
relative analytic methods fail follows from this.
