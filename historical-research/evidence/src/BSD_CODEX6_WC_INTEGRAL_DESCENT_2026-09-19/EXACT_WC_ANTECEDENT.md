# Exact WC input, with preserved quantifiers

The following two sections are copied without mathematical edits from the sealed predecessor WITNESS_CONTENT_THEOREM.md. Its SHA-256 is 556ecfa56f87f4497cdc7f2e25db3ec6a5431b2a70393ccbb80ea96fc085738e. The source's status remains a conditional mathematical proof using Ota; this is not a kernel proof.

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

## Quantifier and selection audit

The arithmetic antecedent is: there exists A in Z minus {0} such that for every p outside S0 there exists an admissible S with t(p,S) nonzero and depth(t(p,S))<=v_p(A). S and its number/size of factors may depend on p. There is no requirement of a compatible unit, a common scalar equality, or a previously fixed auxiliary pair. This session proves that S may be restricted to one or two factors without changing h_p.

An admissible auxiliary prime may have E(F_ell)[p]=0 or Z/p. The additional trace congruence a_ell=ell+1 mod p used for Kurihara/core primes is NOT part of WC's definition. Full leading-term depth is not automatically equal to the valuation of one chosen projection. A nonzero projection gives only an upper bound for full depth.

Zero is assigned infinite depth even in Z/p^k. A coefficient divisible by p^k does not give a witness of depth k. This distinction is required in every content or ideal calculation below.

The exclusions remain exactly S0. The existing results close the 2-,3-,5-primary groups (with the inherited p=3 source qualifications). Finiteness at 2243,4547,5843 remains an additional open input to the WC-to-global-FIN assembly. No computation or theorem in this session closes those cases.

ORDINARY_CONVERSE_GATE.md proves h_p=0 iff Sha[p^infinity]=0 for ordinary p in P. It distinguishes this from finite-depth existence and from a global equivalence. This new conclusion changes the interpretation of the antecedent, not its quantifiers.
