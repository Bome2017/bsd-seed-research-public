# The fixed-prime implication used by the C11 computation

This is the already established fixed-prime method specialized to 11. Its numerical premise is pending until DOWNSTREAM.json and CERTIFICATE_BINDINGS.json pass. No Sha[11] conclusion is asserted in advance.

Let E be the fixed seed and let S_b=[b/121]^+ and s_a=[a/11]^+ use the retained omega1 convention. Exact counting gives #E(F11)=14 and a11=-2, so reduction is good ordinary. The unit root alpha of X^2+2X+11 satisfies alpha=9 mod11, alpha^-2=3 mod11, and (1-alpha^-1)^2=5 mod11.

The retained lattice bound gives 11-integral symbols at every denominator 11^n: these cusps are equivalent to 0, the unweighted period is zero, and the retained Manin constant is a power of two. Thus the coefficients of the depth-n measures are integral. Stein--Wuthrich Proposition 3.5 implies

\[
C_{11}:=[T^2]L_{11}(E,T)\equiv[T^2]P_2(T)\pmod {11},
\]

where, for gamma=12 and the Teichmuller lifts omega(a),

\[
P_2(T)=\sum_{a=1}^{10}\sum_{j=0}^{10}
\bigl(\alpha^{-2}S_{\omega(a)12^j\bmod121}
-\alpha^{-3}s_{\omega(a)12^j\bmod11}\bigr)(1+T)^j.
\]

The lower-level quadratic term vanishes modulo11 because sum_j binom(j,2)=165. For a unit b modulo121 its cyclotomic exponent is j(b)=-((b^10-1)/11) modulo11. Its coefficient weight is 3 binom(j(b),2). Folding S_b=S_(121-b) gives exactly the five lists in downstream.py, with weights 2,3,5,6,7 and 45 nonzero symbols. These lists were declared before any new symbol computation. The second implementation retains the lower-level term and evaluates P2 independently with Hensel and Teichmuller lifts.

If C11 is nonzero, it is a unit. The retained rank is two and the retained full residual image at11 lifts to full 11-adic image. Kato's integral good-ordinary divisibility (Stein--Wuthrich Theorem 7.3) gives L11=f_E d in Z11[[T]]. Theorem 6.1 gives ord_T f_E>=2. The unit quadratic coefficient therefore forces ord_T f_E=ord_T L11=2 and a unit leading coefficient of f_E. The equality clause of Theorem 6.1 then proves finiteness of Sha[11^infinity] and nondegeneracy of the canonical 11-adic height, before its leading-term order formula is used.

All torsion, Tamagawa and interpolation factors are 11-units. Every component group has order one or two. Multiplication by 28=2#E(F11), an 11-unit, sends a rational point into all identity components and the formal group at11. On a global minimal model the canonical sigma-height formula gives, for a nontorsion rational point P,

\[
\widehat h_{11}(P)=\frac{2}{28^2}
\log_{11}\!\left(\frac{e(28P)}{\sigma_{11}(28P)}\right)
\in11\mathbf Z_{11}.
\]

Here sigma11 belongs to Z11[[t]], is nonzero at a nonzero sufficiently small formal point, and log11(Q11^x) is contained in 11Z11. Torsion has height zero. Polarization and v11(log11(12))=1 give Reg_gamma=Reg11/log11(12)^2 in Z11. The leading-term valuation formula now reads

\[
0=v_{11}(\#\Sha[11^\infty])+v_{11}(\operatorname{Reg}_\gamma).
\]

Both terms are nonnegative; hence Sha[11^infinity]=0 and Reg_gamma is a unit. No integral main-conjecture equality or prior finiteness assumption is used. If C11=0, this sufficient test makes no such inference.

Dependencies are the retained [p7 fixed-prime argument](../../../audits/P7_PRIMARY_THEOREM.md), [canonical rank/image/Manin/local inputs](../../../MASTER_BSD_DAG.md), and the local [Stein--Wuthrich source](../../../../BSD_STEIN_WUTHRICH_P5_GATE_2026-09-18/src/SteinWuthrich2013_shark.txt), Proposition 3.5, Section 4.1, Theorems 6.1 and 7.3. The existing preprint and Manin-source qualifications remain. The numerical trust base is the unchanged coefficient producer, independent integer witness verifier, and Arb modular-symbol engine, with their actual bytes bound at launch and completion.

This closes only the 11-primary component if the computation supplies a unit. FIN, order nine and the real scalar identity remain separate open obligations.
