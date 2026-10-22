# Review and repairs of the proposed integral BD construction

October 7, 2026. **CONDITIONAL_TENSOR_RECIPE_SUPPORTED; HOWARD_VALUATION_CORRECTED; ARITHMETIC_REALIZATION_OPEN.**

This review reads the supplied REPORT.md and detailed D1–D5, not only the pasted summary. The source returns are copied unchanged in input/. The conditional deductions below are written arguments by this reviewer, not formal verification, a literature-novelty assertion, or a seed BSD bound.

## 1. What the proposed cancellation actually proves

Fix R=Z/m and suppose the required level-raised quotient V_J and E[m] are defined, with

    H=Hom_G(E[m],V_J)

invertible over R and with evaluation H tensor E[m] -> V_J an isomorphism. Let F_i=H^1_fin(K_ell_i,E[m]), both invertible, and suppose there is the geometric isomorphism

    alpha: Phi -> H^1_sing(K_ell_1,V_J),
    Phi=Phi_ell_1/I.

Tate duality for E and the natural tensor identifications then give

    Phi -> H tensor F_1^vee,
    H -> Phi tensor F_1,
    Xi: H^1_fin(K_ell_2,V_J) -> Phi tensor F_1 tensor F_2.

These are well-typed canonical maps under the hypotheses. Given the actual CM-divisor image beta and a generator

    R_P=loc_1(P1) tensor loc_2(P2)-loc_1(P2) tensor loc_2(P1)

of F_1 tensor F_2, there is a unique C in Phi with Xi(beta)=C tensor R_P. An isomorphism V_J -> E[m] need not be selected.

Explicitly, choose temporary bases h, phi, e1, e2 and write alpha(phi)=a h tensor e1^vee, beta=b h tensor e2 and R_P=r e1 tensor e2, with a,r units. Then C=(b/(ar))phi. Under h'=u h, both a and b are divided by u; the quotient is unchanged. Under e1'=v e1 and e2'=w e2, a becomes av and b,r acquire the respective factors w^(-1) and (vw)^(-1), again cancelling. This proves the claimed independence from these auxiliary bases.

**This supports the tensor recipe.** It does not construct alpha, beta, the rank-one component quotient, or the bottom-layer reciprocity system in the seed's proposed setting. Nor does it prove that all orientation choices at different raised levels amount to one common sign. These were not fixed in the submitted return. Calling the whole arithmetic construction already canonical up to one global sign is therefore premature.

BD Corollary 5.18 supplies the singular comparison in its own hypotheses; the published version is printed p.52, while the supplied September 2007 preprint numbers it p.64. The proposed removal of the p-level and substitution of conductor-one classes is an additional interface. The existing report itself leaves it unverified. Theorem 9.2's surjectivity proof also explicitly uses the p-level. No new global p-free realization follows just from combining coefficient primes by CRT.

## 2. Repair the integral freeness justification, rather than infer p-isolation

D1 defines eta_f using the torsion of M/I_f M and infers that excluding its support makes the localized Hecke algebra Z_p. That implication is not valid for general integral Hecke modules.

A concrete algebra control is T={(a,b) in Z^2: a=b mod q}, M=T with its regular action, and f(a,b)=a. Here I_f=ker f and M/I_f M=Z is torsion-free, yet the localization at the shared residual character modulo q has rational rank two, not one. This is not a Brandt-module counterexample; it shows the missing implication cannot follow from the stated torsion definition alone.

There is a finite-support repair for the fixed base module. Retain the rational multiplicity-one eigenspace for f and its rational Hecke idempotent e_f. Invert a fixed nonzero integer J clearing the denominators of e_f, the image-lattice comparison, and the nonzero coordinate of f on e_f M. Then

    M[1/J]=e_f M[1/J] plus (1-e_f)M[1/J],
    e_f M[1/J] has rank one,
    M[1/J]/I_f M[1/J] -> Z[1/J]

is an isomorphism through f, after clearing the stated coordinate index. The last assertion follows because 1-e_f lies in the localized kernel ideal and f identifies the remaining rank-one summand. This directly provides the needed rank-one coefficient quotient. It does not require the unjustified inference from the torsion group in D1.

J concerns the fixed base module, not an arbitrary family of raised levels. It is not computed, does not certify eligibility at 5 or 7, and is not a Sha annihilator. Bad-local, residual-image and level-raising hypotheses remain separate. The report's 2-by-2 cokernel calculation itself is correct: the entry -1 makes the cokernel cyclic, its determinant is ell+1-epsilon*a_ell, and (1,-epsilon) reads its quotient modulo that integer.

## 3. The proposed ell=283 example cannot detect the rational points

For an inert admissible ell with sign epsilon=-1,

    a_ell = -(ell+1) mod p,
    #E(F_ell) = 2(ell+1) mod p != 0,

because p is odd and p does not divide ell^2-1. Hence multiplication by p is bijective on E(F_ell). The good-reduction local Kummer image of every rational point in E(Q_ell)/p is zero. Restriction to K_ell does not change that zero class. A determinant made from P1,P2 therefore vanishes if either chosen prime has this sign. Use epsilon=+1 for both rational-point detectors.

Fresh exact point counts and group arithmetic give:

| coefficient prime | auxiliary primes | point-coordinate rows | determinant |
|---|---|---|---|
| 5 | 73, 223 | (1,4), (1,3) | 4 mod 5 |
| 7 | 173, 367 | (1,2), (0,1) | 1 mod 7 |
| 11 | 47, 271 | (1,7), (1,2) | 6 mod 11 |

Each auxiliary prime is inert in Q(sqrt(-7)), good, satisfies p not dividing ell^2-1, and has epsilon=+1. Coordinates are measured after multiplying the reduced points by #E(F_ell)/p and choosing the first nonzero image as generator. The p-primary part is cyclic here because Frobenius eigenvalues 1 and ell are distinct modulo p. Thus the calculation detects the quotient E(F_ell)/p even at ell=173 where #E(F_173)=196.

At ell=283 the count is 288, prime to both 5 and 7; it is admissible with epsilon=-1 but its rational-point row is zero at both primes.

There is an additional eligibility correction: BD's introduction assumes the discriminant of K is coprime to its level including the coefficient prime. Thus p=7 is outside that source setup for K=Q(sqrt(-7)). Its row remains a valid local group-arithmetic control, not a BD-admitted example. The original claim that BD supplies one law covering 5 and 7 at ell=283 is therefore unsupported for this second reason as well.

These are denominator controls only. They do not compute beta or C, check the unknown J, establish the full level-raising hypotheses, or settle a primary component. An initial bounded search for one common positive-sign pair at both coefficient primes found only ell=367 as a candidate through 3000; no conclusion beyond that range was drawn. The reproducible checker uses the six explicit auxiliary primes in the table, not a continued prime search.

## 4. Repair of the modified-Selmer comparison without assuming Sha=0

The following is a conditional general deduction. It requires the actual classical self-dual Kummer local conditions, complementary self-dual replacement lines at the two auxiliary places, and the saturated point plane W=E(K)/p^k generated by P1,P2 on the relevant odd-primary domain. The last condition imports the seed's rank-zero twist and the retained point basis; it is not inferred just from root numbers.

Put R=Z/p^k and S=Sel_{p^k}(E/K). Suppose

    W -> F_1 plus F_2

is an isomorphism. Let S^(1) replace the finite line F_1 by the complementary ordinary line, and let S^(12) make both replacements. Then

    S^(12)=ker(S -> F_1 plus F_2),
    S^(12) -> S/W = Sha(E/K)[p^k]

is a canonical isomorphism. No finiteness of Sha[p^infinity] or vanishing of Sha[p^k] is assumed.

Proof. First relax the local condition at ell_1. For x in this relaxed group and y in S, global reciprocity makes their local pairings sum to zero. At every place other than ell_1 they lie in the same self-dual condition, so their pairing there is zero. Since loc_1(W)=F_1, loc_1(x) annihilates all of F_1. Self-duality forces loc_1(x) back into F_1. Thus relaxing creates no new classes. Replacing F_1 by its complementary line then imposes loc_1=0, giving S^(1)=ker(loc_1:S->F_1).

The subgroup W_1=ker(W->F_1) maps isomorphically onto F_2 because the two-place map on W is an isomorphism. Repeat the same reciprocity argument for S^(1), whose replacement condition at ell_1 remains self-dual, to get S^(12)=ker(loc_2:S^(1)->F_2).

Finally, each coset in S/W has a unique representative with both localizations zero, obtained by subtracting its unique matching element of W. This proves the quotient identification.

This repairs the logical route to the target. It is not an independent bound on that quotient, and it does not supply the missing geometric Euler system.

## 5. Howard's rigidity formula has a Selmer term

Howard Definition 2.2.8 and Theorem 2.5.1 give, at an even vertex b and coefficient length k,

    (lambda_b)=m^(delta_sys) Stub_b,
    Stub_b=m^(length M_b) R.

Therefore the correctly truncated index is

    ind_R(lambda_b)=min(k, delta_sys+length M_b).

It is not generally delta_sys alone. The theorem assumes a nontrivial free Euler system with its specified local conditions. A scalar attached to a single pair does not by itself establish that family.

Applying Section 4 when its hypotheses and the geometric realization hold gives

    Sel_F(b) = Sha(E/K)[p^k] = M_b plus M_b

at the even vertex b=ell_1 ell_2. If C differs from lambda_b by the unit denominator and valid line identifications, then

    ind_R(C)=min(k, delta_sys + length(Sha(E/K)[p^k])/2).

For detecting pairs in one fixed fully realized system, the corrected truncated index is therefore pair-independent even without assuming Sha=0: the same Sha[p^k] occurs at each such vertex. This conclusion concerns the index, not the residue or a common rational scalar.

This is a conditional application, not a new value of C. The detailed D4 proof assumed Sha(E/K)[m]=0 before deriving pair-independence; that assumption must not disappear in the summary. Under that assumption the Selmer term is zero. Without it, the term cannot be omitted. No unconditional constancy of the residue across pairs follows.

The useful implication survives with its family hypotheses: at k=1, a nonzero C forces the modified Selmer group, hence Sha(E/K)[p], to vanish. A nonzero fixed rational scalar realizing these values outside finite support would consequently give cofinite primary vanishing. But neither the scalar nor that law is constructed here.

Primary source: Howard, *Bipartite Euler systems*, https://arxiv.org/pdf/1202.6353, printed pp.6,9,13–14. Source hypotheses and the additional Section 4 argument must both be retained.

## 6. Disposition for the seed

Keep the basis-free tensor construction as a conditional normalization mechanism. Do not retain the unqualified assertion that all geometric interfaces are closed, that pair valuations equal delta_sys independently of Sha, or that the proposed test is ready to run.

The immediate useful continuation, if this route is chosen, is to instantiate alpha and beta for the specified bottom-layer curves with one orientation convention and prove the exact CM-divisor/localization compatibility. Then an evaluation must use detecting pairs and an actual integral line normalization. A literature survey stopping because no exact law was found does not establish that construction impossible.

The desired cofinite law remains a substantive arithmetic target. It could bypass the derivative route by proving primary vanishing directly. No comparison with the actual Kato derivative's m_p-w_p has been constructed, and Sha vanishing alone would not imply the sufficient content estimate for an arbitrarily smoothed class.

FIN, ORDER9 and Q36 are unchanged. No research job, proposed task card, expensive Shimura-set computation or new primary-certificate campaign was launched.
