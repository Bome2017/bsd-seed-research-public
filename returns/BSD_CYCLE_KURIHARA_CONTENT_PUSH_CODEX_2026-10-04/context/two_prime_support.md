# Exact reduction to at most two auxiliary primes

Status: proved mathematical deduction from Ota's integral norm relation and I^2 membership. This is a reduction in the support of a witness, not a proof that any witness exists. No Sha finiteness is assumed.

Fix p in P and an Ota-admissible squarefree S. Write

    Gamma_S = product_{ell|S} C_{p^e_ell},  e_ell=v_p(ell-1)>=1,
    X_ell=sigma_ell-1,  I=augmentation ideal of Z_p[Gamma_S].

## Lemma T1: explicit degree-two module

There is an isomorphism

    I^2/I^3 ≅ direct_sum_ell (Z/p^e_ell) X_ell^2
               plus direct_sum_{ell<m} (Z/p^min(e_ell,e_m)) X_ell X_m.

Proof. Present the group ring by variables X_i and relations (1+X_i)^q_i-1 with q_i=p^e_i, and truncate all terms of total degree at least three. The relation is q_i X_i+binom(q_i,2) X_i^2=0. Multiplication by X_j gives q_i X_i X_j=0, including j=i. Since p is odd, binom(q_i,2) is a Z_p-multiple of q_i. Thus the relations are equivalently q_i X_i=0 and q_i X_i X_j=0. These are diagonal monomial relations in the truncated polynomial module; the displayed presentation has no further relations. QED.

The projection from the full cyclotomic G_S to Gamma_S induces an isomorphism on positive augmentation graded pieces. Indeed the complementary subgroup H has order prime to p. Its averaging idempotent e_H splits the group ring into e_H and (1-e_H) components; the latter lies in every positive augmentation power and disappears in each graded quotient. Thus T1 also describes the WC module defined with the full G_S.

In this decomposition, the depth of a nonzero class is the minimum valuation of its nonzero coordinates, each interpreted in its own cyclic quotient. Zero coordinates have depth infinity, not the exponent of their modulus.

## Lemma T2: norm identity on degree two

For T dividing S, Ota Proposition 2.3 gives

    projection_{S/T}(t(p,S))
       = product_{ell|S/T}(a_ell-2) * t(p,T)

in I_T^2/I_T^3.

Proof. Iterate the norm relation for theta. Its factor at ell is -Fr_ell(1-a_ell Fr_ell^(-1)+Fr_ell^(-2)), with augmentation a_ell-2 because ell is good. Theta_T belongs to I_T^2 by Ota 5.17. All positive-degree terms of any factor therefore disappear modulo I_T^3. QED.

## Theorem T3

If t(p,S) is nonzero, some divisor T of S with one or two prime factors has t(p,T) nonzero and

    depth(t(p,T)) <= depth(t(p,S)).

Proof. Choose a coordinate of t(p,S) attaining its depth in T1. Let T contain exactly the one or two primes appearing in that monomial. Projection to Gamma_T keeps that coordinate and its modulus unchanged. By T2 its value is an integer multiple of the corresponding coordinate of t(p,T). A nonzero multiple in a cyclic p-group can only have depth at least the depth of the element multiplied. Hence t(p,T) is nonzero and its full depth is no greater than the chosen coordinate depth. QED.

Consequently the definition of h_p is unchanged if S is restricted to one- or two-prime conductors. More precisely, h_p is the minimum of the depths of the top-support coefficients: the diagonal coefficient at a singleton conductor, and the mixed coefficient at a two-prime conductor. This follows by the same coordinate selection in both directions. The empty conductor has trivial augmentation quotient.

The reduction does not make the prime search finite, impose the Kurihara trace congruence, select a core pair, or establish a bound on the primes. Dividing by a norm factor that is divisible by p is not justified. Nor does it make one fixed finite list of conductors work for infinitely many p: every positive-degree module at a fixed conductor is supported only at prime divisors of its group order.
