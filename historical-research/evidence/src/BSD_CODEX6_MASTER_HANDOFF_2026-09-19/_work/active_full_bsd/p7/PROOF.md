# Exact p=7 implication; numerical premise discharged on2026-09-20

The conditional argument below was saved before the numerical result. The completed coefficient is1 modulo7 in the omega1 convention, so the premise now holds. See ../../../audits/P7_PRIMARY_THEOREM.md for the integrated theorem and exact scope.

Let E be the fixed seed and let L_7(T) be the ordinary p-adic L-function in the retained Neron-period normalization, with gamma=1+7. Write c_2=[T^2]L_7(T).

**Proposition.** If c_2 is a 7-adic unit, then Sha(E/Q)[7^infinity]=0. No exact computation of the p-adic regulator and no assumed finiteness of Sha are required.

**Retained inputs.** Algebraic rank two and its complete basis; good ordinary reduction at 7; full residual (and therefore full 7-adic) image; Tamagawa product 16; torsion order two; Manin constant a power of two. The retained rank/basis preprint and Manin-source qualifications remain. A direct count gives #E(F7)=10 and a7=-2. The coefficient stream independently contains the same a7.

**Proof.** Kato's good-ordinary divisibility, as stated in Stein-Wuthrich Theorem 7.3 in the applicable good-ordinary case, gives L_7(T)=f_E(T)d(T) with f_E,d in Z7[[T]]. Their Theorem 6.1 gives ord_T(f_E)>=2. Thus c_2 a unit implies ord_T(L_7)=ord_T(f_E)=2, and f_E's leading coefficient is a unit. The equality clause of Theorem 6.1 now proves finiteness of the 7-primary Sha and nondegeneracy of the canonical 7-adic height. This ordering does not assume the finiteness being proved.

Its leading-term valuation formula, with epsilon7=(1-alpha^-1)^2 and alpha congruent to -2 modulo7, gives

    0 = v7(#Sha[7^infinity]) + v7(Reg_gamma).

Indeed epsilon7, all Tamagawa numbers, and the torsion denominator are 7-units. It remains to justify nonnegativity of the regulator valuation, rather than assume it from a numerical p-adic height.

Every rational point multiplied by 20 has good reduction at every finite prime and lies in the formal group at7: 2 kills each finite component group, and 10 kills E(F7). The multiplier is a 7-unit. For a non-torsion point R, the canonical sigma formula in Stein-Wuthrich section4.1 gives

    h7(R) = (2/20^2) log_7(e(20R)/sigma7(20R)).

For any nonzero u in Q7, log_7(u) belongs to 7Z7, using log_7(7)=0 and the decomposition u=7^k*zeta*(1+7a). Therefore h7(R) belongs to 7Z7. Polarization divides by 2, a unit, so every entry of its pairing matrix on the retained integral basis belongs to 7Z7. Its determinant belongs to 7^2 Z7. Since v7(log_7(8))=1, Reg_gamma=Reg7/log_7(8)^2 is integral. Both summands in the displayed valuation equation are nonnegative. Hence the Sha valuation is zero. QED.

The proof uses the canonical height formula as printed, including its factor of two. It does not rely on the previously observed raw-model PARI height digits or on any exact p-adic BSD conjecture.

## The finite coefficient to compute

Let S_b=[b/49]^+ and s_a=[a/7]^+ in the engine's omega1 convention. Neron-period symbols are half these values; this factor is a 7-unit. Let alpha be the unit root of X^2+2X+7, omega the Teichmuller character, and b=omega(a)*8^j modulo49. The depth-two approximation is

    P2(T)=sum_(a=1..6,j=0..6) (alpha^-2*S_b-alpha^-3*s_(b mod7))*(1+T)^j.

All symbols are 7-integral because their retained denominator divides1024. Stein-Wuthrich Proposition3.5 therefore gives [T^2]L_7 congruent to [T^2]P2 modulo7 (after the same period convention is used).

The lower-level contribution disappears modulo7 since sum_(j=0..6) binom(j,2)=35. Also alpha^-2 congruent to2 modulo7. Using S_b=S_(49-b), a direct enumeration gives

    [T^2]P2 = 5(S2+S4+S11+S13+S22+S23)
             +4(S6+S9+S10+S15+S16+S24)
             +3(S12+S17+S20)                    (mod7).

This fifteen-symbol expression is derived before seeing the computed values. The independent downstream implementation also constructs the complete depth-two measure using Hensel lifting and Teichmuller representatives and retains the lower-level contribution. Its high-precision output describes P2 only; Proposition3.5 identifies only the stated first digit with the infinite p-adic L-function.

## Certification plan already in execution

The unchanged Arb engine encloses every symbol at denominators49 and7 in the retained lattice (1/1024)Z, including explicit Fourier tails. Target cutoffs are15569256447 and2147483647. Prime-coefficient segments0..884 are reused after their actual bytes and verifier records were checked against the sealed p3 manifest. Segments885..927 are generated and independently verified by the unchanged integer verifier. Every arithmetic work unit is checkpointed and hashed.

Numerical result: coefficient1 modulo7; all retained-input, symbol, coefficient, and theorem checks described in the final report pass. Sha[7^infinity]=0, with the stated imported qualifications.

Load-bearing local source: /Users/bsm/BSD_STEIN_WUTHRICH_P5_GATE_2026-09-18/src/SteinWuthrich2013_shark.txt, section4.1, Proposition3.5, Theorem6.1, Theorem7.3. The good-ordinary application avoids the separate multiplicative-prime provenance issue. This is the same source chain retained for p5, instantiated at7 with an explicit regulator-integrality argument.
