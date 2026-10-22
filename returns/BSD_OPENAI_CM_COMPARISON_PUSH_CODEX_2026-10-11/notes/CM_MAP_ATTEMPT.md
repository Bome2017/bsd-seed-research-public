# An explicit cusp-free CM coefficient function, and the remaining mixed-place comparison

Date: 2026-10-11

Grade: written deductions under the stated retained geometric/Galois inputs. Not an independently accepted new theorem, not a computation of a seed CM class, and not an upper bound for Sha. This note applies the actual OpenAI coefficient construction, rather than its rank-one conclusion.

## 1. Sources actually read and the domain that matters

Read in full or in the indicated sections:

- `/Users/bsm/BSD_EXACT_BD_CONSTANT_2026-10-07/construction/CONSTRUCTION.md`, C0–C9.
- `/Users/bsm/BSD_EXACT_BD_CONSTANT_2026-10-07/notes/stage2_derivation.md`, A1–B7.
- `/Users/bsm/BSD_GITHUB_UPDATE_CODEX_2026-10-04/lab/work/returns/BSD_BD_INTEGRAL_REVIEW_CODEX_2026-10-07/MATHEMATICAL_REVIEW.md`.
- OpenAI/math, pinned commit `fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb`, `preprints/A-pointwise-2-converse-for-elliptic-curves-with-rational-two-torsion-October-7-2026/build/sections/coefficients.tex`, Kummer detector, `co:theta-bridge`, `co:theta-sum`, `co:weighted-comparison`, and `co:odd`.

The BD detector primes in this construction have positive sign, with residual Frobenius eigenvalues 1 and ell, and p does not divide ell^2−1. They are **not** G2 primes with scalar Frobenius −I. Thus the latter mismatch does not reject the construction being attempted here.

Fix R=Z/m, supported on odd primes p>=5, an admitted positive-sign pair ell_1,ell_2, and the indefinite Shimura curve

    X_1 = X_(N^+,N^- ell_1),    J_1 = Pic^0(X_1).

Let I be the specified level-raised Hecke ideal, V_J the retained Galois quotient, and

    Q_2 = H^1_fin(K_(ell_2), V_J).

The geometric comparison from supersingular points at ell_2 to the definite set S'=S(N^- ell_1 ell_2,N^+) is retained. So are the finite-field Kummer map and functoriality under Hecke correspondences. This note does not reprove or recount C4 as new progress.

## 2. What the OpenAI source gives, and why its literal formula cannot just be copied

The source first fixes one global map phi:X_0(N)->E, normalized by phi(infinity)=0. Its coefficient function is

    P_M(s) = lambda_M(L phi_ell(s)).

This is an arithmetic function on the supersingular set, with its scale fixed before forming the weighted theta sum. The subsequent coefficient identity comes from the reduction of its actual CM divisor, plus an explicit orbit count. Its nonzero witness comes separately from a rank-one Heegner point and Gross–Zagier.

Our X_1 has no specified map to E. In fact the retained C8 explanation rules out a nonzero characteristic-zero homomorphism J_1->E, because J_1 is purely toric and E has good reduction at ell_1. Replacing phi by such a map would be invalid. Merely choosing a primitive scalar Brandt eigenvector replaces the arithmetic function by an unknown unit multiple, precisely the normalization problem already recorded in C8.

The repair attempted below keeps the coefficient in Q_2 itself and constructs the degree correction explicitly. It does not invent a parametrization.

## 3. An explicit degree-zero correction using the seed's Hecke data

For a good Hecke prime q away from the relevant geometric level put

    A_q = T_q − (q+1),     c_q = a_q(E) − (q+1) = −#E(F_q).

The correspondence A_q sends any divisor to a degree-zero divisor. Suppose the retained Hecke quotient imposes T_q=a_q(E), and c_q is a unit in R. For a divisor D defined over F_(ell_2^2), define

    q_m(D) = c_q^(-1) Kum_I([A_q D])  in Q_2.            (1)

Here the bracket is an actual element of Pic^0(X_1)(F_(ell_2^2)); Kum_I is finite-field Kummer followed by the specified quotient to V_J. Equation (1) has no basepoint or rational Hodge divisor.

### Independence of the correcting Hecke prime

If r is another permitted correcting prime, A_q and A_r commute as Hecke correspondences. After applying Kummer and the quotient,

    c_q Kum_I([A_r D])
       = Kum_I([A_q A_r D])
       = c_r Kum_I([A_q D]).

Both constants are units. Therefore c_q^(-1)Kum_I([A_q D]) equals c_r^(-1)Kum_I([A_r D]). The displayed function is intrinsic to the quotient, not a choice of correction.

For degree-zero D, A_q acts as c_q on its Kummer image. Thus q_m(D)=Kum_I([D]). In particular this construction is the explicit realization of the retained non-Eisenstein degree correction, not a new reciprocity law.

For our seed the exact counts are

    #E(F_5)=8,   a_5=−2;     #E(F_13)=18,   a_13=−4.

Consequently:

- at coefficient p!=5, use A_5=T_5−6 and c_5=−8;
- at coefficient p=5, use A_13=T_13−14 and c_13=−18, provided its ordinary away-from-p Hecke congruence is part of I;
- the two constructions agree on every overlap.

Positive-sign admissibility excludes ell_i=5 or 13 for every p>=5: it would require p|8 or p|18. Thus the chosen geometric Hecke correspondences are away from both raised primes. The seed conductor is also prime to 5 and 13.

If both T_5+2 and T_13+4 lie in I, the single rational correspondence

    A = 2 A_5 − A_13 = 2 T_5 − T_13 + 2

has degree zero and acts as 2 on the quotient. Hence the particularly simple formula is

    q_m(D) = (1/2) Kum_I([A D]).                        (2)

The denominator in (2) is a unit for every p>=5. It is a canonical degree correction, not a division by the unknown content of a source class. In particular it is not a normalization or modification of the project's actual Kato source.

**Coefficient-prime qualification.** Do not infer T_p=a_p solely from an away-from-p residual representation. Formula (2) applies where both congruences are in the chosen ideal. The two-prime version (1), applied componentwise at coefficient primes, needs only an away-from-p Hecke congruence and covers p=5 using q=13. This qualification prevents an unproved coefficient-prime normalization from being hidden in the formula.

## 4. The actual coefficient-valued function and a finite embedding coefficient

For a supersingular point s in S', put q_m(s)=q_m([s]) via (1). This is an actual Q_2-valued function, with Hecke equivariance. The original CM sum D_K therefore has

    sum_sigma q_m(red_(ell_2) P_sigma)
      = loc_(ell_2) kappa_J(D_K) = beta.                (3)

The equality uses the retained reduction/Kummer square; it is not a second proof of that square. Formula (1) specifies its divisor correction without an auxiliary scalar eigenbasis. The notation kappa_J(D_K) denotes the non-Eisenstein corrected divisor class, not a Kummer map on an unspecified Picard-degree component.

Here is the exact finite coefficient that can be constructed without importing an unverified theta transformation law. Fix the seed field K=Q(sqrt(−7)) and write omega=(1+sqrt(−7))/2, so O_K=Z[omega]. For the definite Eichler order O_s associated to s, define

    Emb_s = {iota:O_K -> O_s : iota is an optimal embedding
             with the retained fixed local CM orientation tuple}.

The tuple includes the orientations at the original level primes and the two raised primes; at ell_2 it is the one selected by the retained localization embedding. These are actual embeddings, not conjugacy classes. Its elements can equivalently be represented by

    x=iota(sqrt(−7)),  trd(x)=0,  x^2=−7,
    (1+x)/2 in O_s,

with the stated local orientation requirements. This is a finite set: the reduced-norm quadratic form on the trace-zero definite quaternion space is positive definite, and Nrd(x)=7. This description specifies the integral generator at 2 exactly. No claim about even fundamental discriminants is made here.

Put e_s=|O_s^times|/2. The unit-conjugation action preserves the orientation conditions. Its stabilizer at an embedding is iota(O_K^times)={+1,−1}, so every orbit has exactly e_s elements. Thus

    n_s=|Emb_s|/e_s

is an integer, equal to the number of oriented embedding orbits at s. All prime divisors of e_s lie in {2,3}: if the finite unit group had a prime divisor r>=5, Cauchy's theorem would give an element of order r, whose minimal polynomial over Q has degree r−1>=4, impossible in a quaternion division algebra. In particular stabilizer weighting introduces no denominator at p>=5.

Define the finite embedding coefficient

    B_K(q_m) = sum_s n_s q_m(s)
             = sum_s e_s^(-1)|Emb_s| q_m(s).            (4)

Under the retained oriented CM/optimal-embedding reduction correspondence, the orbits counted here are exactly the reductions of the CM class-group sum. Consequently

    B_K(q_m) = beta.                                   (5)

Equation (5) is a precise coefficient-valued embedding-count identity, not an assertion that beta is nonzero. It does not require Q_2 to be free or cyclic.

**Theta-series scope.** OpenAI's source constructs a particular family of finite Schwartz functions and checks its transformation law. This note does not supply the full analogous Schwartz functions, lattice/conductor data and transformation calculation for all Fourier indices on our varying raised quaternion algebras. Therefore (4) is retained only as a finite embedding coefficient. No new modular theta series or scalar theta recurrence is claimed. The former provisional assertion that unspecified finite orientation cuts alone supplied the required modular series has been removed.

The explicit part here is construction (1)/(2) feeding the actual finite coefficient (4), without a cusp, a point of degree one or a scalar eigenvector. Identity (5) reformulates the retained reduction map by orbit counting. It is not an independent arithmetic estimate.

## 5. Does this fix the two-place normalization?

Assume additionally the existing C3 hypotheses: H=Hom_G(E[m],V_J) is invertible, evaluation H tensor E[m]->V_J is an isomorphism, and alpha identifies Phi with the singular local line. Then the retained canonical map

    Xi: Q_2 -> Phi tensor F_1 tensor F_2

applies to (4). For a detecting pair, the finite coefficient satisfies

    Xi(B_K(q_m)) = C_K tensor R_P.          (6)

Thus the finite embedding expression retains the absolute geometric coefficient beta, and no scalar h in H has been chosen. This is useful bookkeeping for an exact implementation; it is not a new numerical value.

It does **not** evaluate C_K from scalar definite data. Only if an additional multiplicity-one/base-change theorem proves that the relevant simultaneous Brandt eigenfunction module on S' is free of rank one, and that Q_2-valued eigenfunctions are obtained from it by tensoring, may one choose a primitive scalar generator g_0 and write

    q_m = lambda_(ell_1,ell_2) g_0,

with lambda in Q_2. Primitivity of a chosen g_0 alone does not imply that factorization. First-raised C3 multiplicity one does not by itself prove this higher-depth Brandt assertion. Without this extra theorem the function remains in its full coefficient module. Even when the factorization is justified, the problem is still to measure lambda via Xi relative to the ell_1 singular generator and the E-side point determinant. Formula (1) computes lambda through the finite-field Jacobian, not through the scalar Brandt module alone. Nothing in the finite embedding orbit count compares that finite-field realization to the ell_1 toric realization.

This identifies the precise limit of the attempted import: it does remove an avoidable degree-normalization choice, but it does not remove the mixed-place arithmetic comparison at C8. The existing C6 cancellation already proves independence from a temporary Hom-line basis. Applying it to the explicit finite embedding coefficient does not add a new rational scalar or a p-adic unit estimate.

## 6. Why the coefficient identity and a nonzero function do not give the needed bound

A nonzero coefficient-valued eigenfunction need not have a nonzero selected CM coefficient. In the fixed field Q(sqrt(−7)), whose class number is one, this can already mean that the function vanishes at the single selected CM point; no cancellation among a large class-group sum is required. In more general fields sums can additionally cancel. Surjectivity from all supersingular divisors, even if supplied by a fully matched Ihara argument, does not say that D_K generates their quotient. OpenAI's nonvanishing witness is supplied by a rank-one Gross–Zagier input and is not part of the theta construction alone.

Also, for a fixed pair (ell_1,ell_2), positive-sign level raising only admits coefficient primes dividing the two fixed nonzero integers #E(F_(ell_1)) and #E(F_(ell_2)). Thus a cofinite coefficient-prime argument must vary the raised curves and coefficient modules. Formula (2) is a uniform degree-correction rule across those modules; it does not identify them with one common characteristic-zero source. This is where one must not confuse a fixed correspondence formula with a fixed nonzero arithmetic invariant.

The admissible next theorem would still have to establish a unit/valuation bound for the selected coefficient (5), or independently compare (6) with R_P uniformly. No such bound was obtained here. More embedding-count instances or an arbitrary choice of integral lifts would not establish it.

## 7. Disposition

- Constructed: explicit Hecke-normalized, cusp-free Q_2-valued supersingular function and its finite oriented-embedding coefficient. No modular theta-series claim is retained.
- Uniform denominator control: only 2 and 3 occur in the correction/stabilizer recipe; coefficient-prime Hecke hypotheses remain explicit.
- Already retained, not new: C4 reduction compatibility, C6 basis cancellation, and the fact that beta detects the desired CM divisor.
- Still open: C8's arithmetic two-place comparison, actual selected-coefficient nonvanishing, and cofinite upper control.
- FIN, ORDER9, Q36 unchanged. No seed primary component, class field, large Brandt module or source Kato coefficient was computed.

This is a scoped concrete construction attempt, not evidence that a new upper-bound mechanism has been found. The route should not receive a blind embedding/theta-enumeration campaign on the strength of (4).
