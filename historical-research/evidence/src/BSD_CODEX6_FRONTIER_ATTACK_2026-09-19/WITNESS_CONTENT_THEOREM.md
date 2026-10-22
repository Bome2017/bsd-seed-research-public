# A witness-content criterion for uniform finiteness

Status: **PROVED conditional reduction from the stated published Ota inputs**. The sufficient antecedent for the seed is **UNKNOWN**. This is new work in this session, not a claim of mathematical novelty. It neither assumes finite Sha to define its objects nor proves finite Sha for the seed.

## 1. Unconditional objects

Fix an elliptic curve E/Q of rank two. Let S0 be a finite set containing every prime excluded by Ota's Theorems 5.17 and 6.4, and put P = {primes outside S0}. For the fixed seed we may use

    S0 = {2, 3, 5, 2243, 4547, 5843}.

This uses the retained all-odd residual-image theorem, its p-adic lifting for p >= 5, Tamagawa product 16, and the absence of anomalous good primes. The latter follows from rational 2-torsion and Hasse: for p >= 7, a positive even multiple of p exceeds p+1+2 sqrt(p). We also put 5 in S0 so that its already sealed vanishing theorem is used directly; no new tame witness at 5 is required. The Ota hypotheses would also hold at 5, where the group order is 8.

For p in P, let S range over squarefree products of good primes ell not dividing pN, with ell = 1 mod p and E(F_ell)[p] cyclic. Write

    M(p,S) = I_S^2 / I_S^3 over Z_p,
    t(p,S) = the degree-two image of theta_S in M(p,S).

Ota supplies membership theta_S in I_S^2 without Sha-finiteness. M(p,S) is a finite p-primary module. We use the full leading term; choosing core pairs or a cyclic multilinear projection is optional.

For a nonzero element t of a finite p-primary Z_p-module M define

    depth_M(t) = max {j >= 0 : t belongs to p^j M}.

This is finite, since p^j M eventually vanishes. Do not assign a finite truncated depth to the zero element. Define

    h_p = min {depth_M(p,S)(t(p,S)) : t(p,S) != 0},

with h_p = infinity if the displayed set is empty. Each finite h_p is attained, by well-ordering of the nonnegative integers. Set

    J_E = {a in Z : v_p(a) >= h_p for every p in P},

where v_p(0)=infinity. This is an ideal of Z, possibly the zero ideal: the valuation inequality is preserved under addition and multiplication by integers. Its definition uses modular symbols and finite augmentation quotients, not #Sha or the BKS Mordell-Weil realization. It is nonzero exactly when every h_p is finite and only finitely many are positive. In that case its positive generator is the finite product of p^h_p. These assertions follow directly from prime factorization of a nonzero integer; they impose no coherence on unit parts.

## 2. The theorem

**Theorem WC.** If J_E contains a nonzero integer A, then:

1. Sha(E/Q)[p^infinity] is finite for every p in P;
2. Sha(E/Q)[p^infinity] = 0 for p in P with p not dividing A;
3. if the primary groups at the finitely many primes in S0 are finite, Sha(E/Q) is finite.

**Proof.** For p in P, h_p <= v_p(A) < infinity supplies an S with t(p,S) nonzero. If the p-primary Sha group were infinite, its Z_p-corank would be positive: the p-primary Selmer group is cofinitely generated, and a cofinitely generated p-primary group of corank zero is finite. Hence the Selmer corank would exceed rank E(Q)=2. Ota 5.17 would place theta_S in I_S^{min(corank,p)}, a submodule of I_S^3, contradicting t(p,S) != 0. This proves (1).

If p does not divide A, h_p=0. The attaining t is not in pM, so its reduction in M/pM is nonzero. Ota 6.4 gives Sha[p]=0. Any nonzero p-primary torsion element has a nonzero multiple of order p, so the entire p-primary group vanishes. This proves (2).

Sha is a torsion group, thus the direct sum of its primary groups. All but finitely many vanish by (2); those left are finite by (1) and the S0 hypothesis. Their direct sum is finite. QED.

The imported Ota assertions are read in the retained primary text, lines 2069–2078 and 2146–2156, and checked against [Ota's paper](https://arxiv.org/abs/1509.00682). The proof above is our deduction. No converse is asserted.

## 3. Exactly what this weakens

The original tame LINE, with common coprime nonzero a,b, implies a belongs to J_E. At each core pair the regulator projection is primitive. Reduction mod p first forces p not to divide b. Choose a core pair at level k>v_p(a). Its projected theta coefficient has depth v_p(a), because b is a unit and the regulator component generates a group of order at least p^k. A projection cannot decrease divisibility; therefore the full leading term has depth at most v_p(a). Thus h_p <= v_p(a).

WC needs neither equality of any scalar across primes nor equality among all witnesses at one prime. It asks for one bounded-depth witness at each prime. Even its unit parts are unconstrained.

Strictness at the level of the proposed algebraic data is explicit: take primitive regulators in cyclic groups Z/p^k and coefficients u_p times those regulators, compatibly for every k, with u_7=1, u_11=2, and u_p=1 otherwise. All h_p=0, so J=Z. A common rational scalar would equal 1 in Q_7 and hence equal the rational number 1, but would have to equal 2 in Q_11. Impossible. This is an abstract logical countermodel to the stronger scalar assertion, not a computation of these primes or a claim about the seed's modular symbols.

An intermediate weakening is a single finite idele of nonzero local scalars, units at almost every prime. A diagonal rational scalar is unnecessary even there. WC is weaker still: it requires no coherent choice of a local scalar.

## 4. Attempts to prove the antecedent

### Uniform symbol denominators

The project bounds denominators by a power of 2. That gives integrality at every odd p. It does not bound h_p. Counterexample: the fixed lattice Z with element 1, evaluated by the integral maps n -> p^2 n in Z_p. The source has no denominator at all, yet the image is divisible by p at every prime. The actual logarithmic and localization maps must supply additional arithmetic information.

### Finite generation over the profinite integers

Let R = product_p Z_p and d=(d_p), where d_2=d_5=1, d_3=9, and d_p=p^2 at all p>=7. The complex [R --d--> R] is a two-term complex of finite free R-modules. At every p it becomes an isomorphism over Q_p. Every local cokernel is finite. Nevertheless its cokernel is

    product_{p>=7} Z/p^2 Z  times Z/9 Z,

which is infinite, and the intersection of the local determinant ideals with Z is zero. Each nonzero integer has finite prime support. A direct sum of groups (Z/p Z)^2 gives the corresponding torsion-group example with alternating nondegenerate local pairings, zero 2- and 5-parts, and 3-part (Z/3)^2. Thus the known primary data and square-order constraints do not remove this obstruction.

This kills the abstract implication “perfect profinite determinant complex + finite local defects => finite global defect.” It does not kill a complex with genuinely stronger global descent or Euler-system properties.

### Descent to Z with a primitive comparison

Here is a valid sufficient theorem, also proved now. Let M be a finite free Z-module, z a nonzero element, and c the positive gcd of its coordinates in a Z-basis. Suppose that outside an explicit finite set B, the arithmetic construction produces an Ota witness whose depth is at most the content of z in M tensor Z_p. Then h_p <= v_p(c) outside B. If each remaining prime has a finite-depth witness or an independently finite primary group, WC proves FIN. The proof is that Smith normal form gives z=c z_0 with z_0 primitive, so its local content is exactly v_p(c).

The missing input is the comparison with that **primitive integral lattice**, not the existence of some rational source or some p-adic maps. Maps n -> p^2 n satisfy the latter weaker requirements and refute the inference.

## 5. Exact stop

    WC_IMPLICATION = PROVED
    LINE_IMPLIES_WC = PROVED using the retained core-pair normalization/existence
    WC_ANTECEDENT_FOR_SEED = UNKNOWN
    NONZERO_ELEMENT_OF_J_E = NOT CONSTRUCTED
    EXCEPTIONAL_PRIMARY_FIN = OPEN at 2243, 4547, 5843
    SEED_FIN = OPEN

The seed's sealed p=5 cyclotomic symbol certificate is not silently relabelled as a tame Ota witness: 5 is excluded and its known vanishing is used directly. The p=3 group also lies in S0. No value of h_p has been newly computed. Neither the 20 p=5 symbols nor any finite set of primes can establish J_E != 0.

The next theorem attempt should address integral descent and bounded witness content directly. The reduction makes the target smaller than LINE, but does not supply an executable proof of its antecedent.
