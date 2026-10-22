# An exact valuation explanation, and the independent seed-bound boundary

Date: 2026-10-13. Baseline: `Bome2017/bsd-seed-lab@f97843a1b4768606787a9760ea4bad727a3dc4a1`.

**Grade: written deduction from published theorems and retained arithmetic; independent review required.** No new general theorem is claimed. The main-conjecture theorems are imported, not proved by this packet. The numerical producers and earlier seed certificates are retained. The new executable checks cover only the arithmetic explicitly described below.

## 1. The proposed explanation and its exact meaning

For a rank-two elliptic curve C/Q, let p be an odd good ordinary prime, gamma a generator with cyclotomic character 1+p, and U=gamma-1. Put

\[
 L_2=[U^2]L_{\rm std,p}(C),\quad
 R_U=\det H_U,\quad
 \varepsilon_p=(1-\alpha_p^{-1})^2,\quad
 c(C)=\prod_v c_v(C),\quad t(C)=|C(\mathbf Q)_{\rm tors}|.
\]

The measure is normalized by the minimal Neron differential and real period. The height is the canonical ordinary cyclotomic height in the same U-coordinate on a p-saturated point pair. Set

\[
 \nu_p(C)=v_p(L_2)-v_p(R_U)-v_p(\varepsilon_p)-v_p(c(C))+2v_p(t(C)). \tag{1}
\]

**DERIVED, under the integral ordinary main conjecture:** if L_2 is nonzero, then the height is nondegenerate, Sha(C/Q)[p^infinity] is finite, and

\[
 \boxed{\nu_p(C)=\operatorname{length}_{\mathbf Z_p}\Sha(C/\mathbf Q)[p^\infty].} \tag{2}
\]

Conversely, finiteness of that primary group and nondegeneracy of the height imply L_2 is nonzero and (2) holds. Neither direction presupposes the complex BSD formula or finiteness at other primes.

Equation (2) is an established-theorem consequence, not a regression fitted to the controls. It explains valuations, not the exact p-adic unit of the corrected quotient. In particular it does not assert that the corrected quotient equals an integer to infinite precision.

## 2. Source interfaces

**THEOREM, BCS.** Burungale--Castella--Skinner, *Base change and Iwasawa Main Conjectures for GL2*, Theorem 1.1.2(a),(b), supplies the integral cyclotomic main conjecture at good ordinary p>3 if C[p] is irreducible and there is sigma in G_(Q(mu_(p^infinity))) with T_pC/(sigma-1)T_pC isomorphic to Z_p. Part (a) alone only gives equality after inverting p; part (b) is necessary here. The theorem has no rank-at-most-one or global squarefree-conductor condition.

**THEOREM, CGS.** Castella--Grossi--Skinner, *Mazur's main conjecture at Eisenstein primes*, Theorem A (also Theorem 7.1.1), supplies the integral equality at good p>2 when the representation has one-dimensional constituents phi and omega*phi^(-1) with phi restricted to G_Qp neither 1 nor omega. Its main-conjecture theorem has no rank restriction. The separate rank-zero/rank-one classical-BSD corollary, Theorem D, is not used.

**THEOREM, algebraic leading term.** Stein--Wuthrich Theorem 6.1, attributed there to Schneider and Perrin-Riou in the good ordinary case, gives ord_U(f_C)>=rank C(Q), with equality precisely when the primary Sha is finite and the p-adic height is nondegenerate. In that case the valuation of its leading coefficient is the valuation of epsilon_p*c(C)*#Sha[p^infinity]*Reg_gamma divided by the square of rational p-primary torsion. Their Section 4.5 specifies Reg_gamma=Reg_p/log(chi_cyc(gamma))^r.

All locators, reading scope and normalization details are in SOURCES.md. These statements concern the dual of the usual ordinary Selmer group, not the earlier full-S Iwasawa H2 module. No equality of those two modules is asserted.

## 3. Proof of (2), with finiteness in the correct order

Let Lambda=Z_p[[U]], and let X be the Pontryagin dual of the usual ordinary Selmer group over the cyclotomic Z_p-extension. Write f_C for a generator of its characteristic ideal. The admitted integral main conjecture gives

\[
 (f_C)=(L_{\rm std,p})\quad\text{in }\Lambda. \tag{3}
\]

Both generators therefore differ by a Lambda-unit, not by an unspecified power of p. The algebraic leading-term theorem first gives U^2 dividing f_C. It follows from (3) that the coefficients of degrees zero and one of the infinite L-series are exactly zero. This conclusion is not inferred from numerical O(p^k) outputs.

If the actual coefficient L_2 is nonzero, ord_U(f_C)=ord_U(L_std,p)=2. The equality case in the algebraic theorem now establishes primary finiteness and height nondegeneracy. Only then do we use its leading coefficient formula. Equality (3) preserves the valuation of the leading coefficient, yielding (1)--(2).

For the reverse direction, primary finiteness and a nonsingular height give ord_U(f_C)=2 and its leading-term valuation by that same theorem. Applying (3) gives the asserted nonzero L_2 and its valuation.

A point pair of p-unit index in the full free point lattice changes the determinant by the square of a p-unit, so it suffices for this valuation statement. The torsion factor may likewise be written using full rational torsion because its prime-to-p part is a unit. A factor two between a primitive real cycle and the full real period is a p-unit for every prime used here. The scalar-to-U conversion divides both quadratic determinants by log(1+p)^2. Arbitrary p-factors in either normalization would invalidate the application.

Finite Lambda-modules are not dropped by a pseudo-isomorphism argument: the specialized algebraic leading-term theorem is the input controlling the actual primary group. This proof does not claim that characteristic ideals alone control all finite errors for arbitrary algebra models.

## 4. The Eisenstein theorem applies to the positive control

Retain the curve

\[
 F:y^2+y=x^3-14959712463303x-22270654620235278500,
\]

which is the fundamental-discriminant d=43737 twist of [0,-1,1,-7820,-263580]. It is rationally 5-isogenous to the d-twist A of [0,-1,1,-10,-20]. The retained proof supplies the actual isogeny, rank two, 5-saturated points, c(F)=4, t(F)=1, and the independent lower bound dim_F5 Sha(F)[5]>=2.

The base conductor-11 isogeny class has residual semisimplification 1 plus omega at 5. For a direct check of the rational constituent, (5,5) on [0,-1,1,-10,-20] has successive multiples (16,-61), (16,60), (5,-6), O; the script verifies these exactly. Rationally isogenous curves have the same residual semisimplification. Quadratic twisting therefore gives

\[
 F[5]^{ss}\simeq\mathbf F_5(\chi_d)\oplus\mathbf F_5(\omega\chi_d). \tag{4}
\]

Here d=3*61*239 is squarefree and congruent to 1 modulo 4, is prime to 5, and d=2 modulo 5. Hence chi_d is unramified at 5 with Frobenius value -1. It is neither the trivial character nor the ramified mod-five cyclotomic character. The other constituent omega*chi_d also differs from both 1 and omega. Thus the actual kernel choice does not change the local hypothesis check.

The curve is good at 5, and direct counting gives #F(F_5)=7, a_5=-1. CGS Theorem A applies integrally. It is not excluded by the reducible representation. No application of the full-image Kato theorem to F is made.

The retained, directly extracted coefficient and independent regulator give

\[
 L_{2,5}(F)=4\cdot5^2+O(5^3),\qquad R_U(F)=4+O(5). \tag{5}
\]

Thus L_2 is genuinely nonzero and has exact valuation two; R_U is a unit. The Euler factor is a unit, with reduction 4. The Tamagawa and torsion valuations are zero. Section 3 now proves

\[
 \boxed{\#\Sha(F/\mathbf Q)[5^\infty]=25.} \tag{6}
\]

The independent isogeny argument had already given dim_F5 Sha(F)[5]>=2. The subgroup killed by 5 therefore has at least 25 elements, while the entire primary group has exactly 25. Consequently

\[
 \boxed{\Sha(F/\mathbf Q)[5^\infty]\simeq(\mathbf Z/5\mathbf Z)^2.} \tag{7}
\]

This is an upgrade from the recorded lower bound at the grade of the retained arithmetic and imported theorems. It does not prove finiteness or order of the full Sha(F), and it is not a fresh modular-symbol computation. The numeral 25 in (6) is exact because it is a power-of-five group order determined by a valuation, not because the p-adic quotient has been recognized as exactly 25.

## 5. The full-image-type controls satisfy the other theorem

For 433a1=[1,0,0,0,1], Delta=-433 and c4=1. For 655a1=[0,0,1,-13,18], Delta=-5^2*131 and c4=624. At the multiplicative primes 433 and 131, respectively, the discriminant valuation is one.

At a multiplicative place q different from p, the Tate-curve inertia representation (also in the nonsplit case, whose unramified twist is trivial on inertia) contains

\[
 \begin{pmatrix}1&1\\0&1\end{pmatrix}
\]

in an integral basis when v_q(Delta)=1. Inertia at q acts trivially on all p-power roots of unity. This directly supplies BCS condition (im), including its primitive rank-one cokernel. No unknown integral lift index occurs.

The following point-count witnesses prove residual irreducibility. An invariant line over F_p would make every unramified Frobenius characteristic polynomial split over F_p, contrary to the listed nonsquare discriminants.

| C,p | Frobenius prime q | a_q | a_q^2-4q mod p |
|---|---:|---:|---:|
| 655a1,7 | 2 | -2 | 3 |
| 433a1,13 | 2 | -1 | 6 |
| 655a1,31 | 2 | -2 | 27 |
| 433a1,7 | 3 | -2 | 6 |
| 655a1,11 | 2 | -2 | 7 |

The script verifies good ordinary non-anomalous reduction, the nonsquare tests, and the multiplicative indices. Thus BCS applies. Subject to the retained rank, p-saturation and coefficient/height data, (2) gives zero primary Sha in each of the old unit-ratio rows. In particular it explains both the coincident-line 655a1/7 row and the distinct-line 433a1/13 and 655a1/31 rows. No line-incidence assumption enters the theorem.

Those observations are applications to existing controls, not newly discovered curves or a fresh scan. The proof does not explain the experimental leading unit Q=1 to arbitrarily high precision; (2) fixes only its valuation.

## 6. The same valuation theorem applies to the seed

For the seed [0,-1,0,-66020924,-65074271436], retain rank two, full odd residual image, the minimal differential, full point lattice and rational torsion of order two. At q=2243, c4 is a unit and v_q(Delta)=1, so the same Tate-inertia argument supplies (im) for every good p>=5.

Consequently BCS applies at every good ordinary p>=5 using the retained residual irreducibility. The seed Tamagawa product is a power of two, and its ordinary primes are non-anomalous by the retained rational-two-torsion argument and separate p=5 count. All finite local, torsion and ordinary Euler terms in (1) are therefore p-units. We obtain

\[
 \boxed{v_p(L_{2,p})-v_p(\det H_{U,p})
       =\operatorname{length}_{\mathbf Z_p}\Sha(E/\mathbf Q)[p^\infty]} \tag{8}
\]

whenever L_2 is nonzero; it also holds in the reverse direction when primary finiteness and height nondegeneracy have already been proved.

This formulation uses usual ordinary Selmer groups. The artificial bad-local comparison exclusions {19,59,487} from the full-S Bockstein route are not hypotheses of this ordinary theorem. This does not settle those primes without additional arithmetic. Supersingular primes are outside this statement.

At p=17 the original Ota certificate at ell=103 already proves Sha[17^infinity]=0 at its retained grade. It is a genuine certified value c2=46298=7 mod17, not the conjectural tame-regulator prediction. The separate retained height data give v_17(det H_U)=1. These two inputs are independent of the unknown cyclotomic coefficient. The reverse implication of Section 3 therefore gives

\[
 \boxed{L_{2,17}\ne0,\qquad v_{17}(L_{2,17})=1.} \tag{9}
\]

As an additional elementary check, a_17=-6 and #E(F_17)=24; Frobenius at 7 has trace -2 and discriminant 10 modulo 17, a nonsquare. These suffice for the BCS hypotheses at this specific prime even without using the all-prime residual theorem.

Equation (9) is a deduction of a previously uncomputed valuation from the old independent tame certificate. It does not evaluate L_2,17/17 modulo 17, create a new base primary result, or provide a new independent proof of Sha17=0. Using (9) to re-prove the input certificate would be circular.

More generally, an admitted Ota vanishing witness at a good ordinary p, plus a nonsingular matched p-adic height, forces equality of the cyclotomic numerator and regulator valuations. This is a bridge from independent tame arithmetic to the cyclotomic valuation, not an assertion that such tame witnesses exist cofinitely.

## 7. Consequence for the earlier source-defect identity

The reviewed defect-inclusive argument and the authenticated source family give, on their smaller ordinary domain and nonzero branch,

\[
 v_p(L_{2,p})-v_p(\det H_{U,p})
 =\operatorname{length}\Sha[p^\infty]+e_p,\qquad e_p\ge0. \tag{10}
\]

Comparing (8) and (10) gives e_p=0 for that matched family on that branch. This is a consequence of adding the integral main-conjecture theorem, not of removing smoothing factors by hand. It does not concern arbitrary rescaled Kato classes, unmatched periods, supersingular conventions, or primes where the nonzero branch has not been established. The antecedent defect-identity proof remains retained, not independently rebuilt here.

## 8. Why this is an explanation but not the missing independent bound

The two observed kinds of controls are governed by the same valuation law, although their integral main-conjecture hypotheses are verified by different theorems. Nonunit regulators account for the point-height contribution; the remaining valuation is actual primary Sha length. A rational p-isogeny is not part of the seed application.

This does not produce a new cheap arithmetic invariant predicting that length before either a coefficient calculation or independent Selmer information is available. The right side of (8) is the original unknown group. Defining an index to equal that side would not create independent control. Likewise the theoretical equality cannot turn a finite set of tests into a cofinite upper bound.

For the standard ordinary source, the precise remaining task is primary finiteness/nondegeneracy and an independent bound on the quantity in (8), or an independent tame/Selmer mechanism forcing it to vanish. The seed17 application uses an already solved prime; it is not evidence that the same inputs settle an unsolved one. FIN, ORDER9, Q36 and new seed-prime coverage remain unchanged.

This packet obtains a concrete exact primary group for the positive control and an exact inferred seed17 coefficient valuation. It supplies no claim of novelty, no new numerator digits, no global Sha support bound, and no full complex BSD identity.
