# A computed CM index for the 167 rank-one control

Status: **NORMALIZED_CM_INDEX_SQUARE_9_DERIVED_UNDER_EXPLICIT_INPUTS**.

This is a written Gross–Zagier computation with Arb-enclosed analytic ingredients. It is not a direct numerical integration of the Shimura parametrization, a Lean proof, or a BSD assertion. The imported classical modular-degree record and the rational Mordell–Weil generator certificate are explicit inputs below. No analytic Sha order is used.

Let

- C : y²+xy+y=x³+x²+1878418x−485198548 (424347b1);
- N=424347=3·7·11²·167;
- K=Q(√−19), of class number one;
- X=X₀^(501)(847), J=Jac(X), and q:J→C an optimal quotient;
- Y=(480,22723);
- ξ the degree-one rational Hodge class and P the CM point of maximal order;
- H=q([P−ξ]) ∈ C(K)⊗Q.

The actual map q is only fixed up to sign. On the retained rank-one K-domain write H=nY modulo torsion. The conclusion is

**n²=9**, hence n=±3, and in particular H is nonzero modulo5.

For the integral degree-zero correction

D=[2(T₅−6)−(T₁₃−14)]P,

we have q(D)=−2H, so its coefficient has square36. The normalized source (−1/2)D is H; do not confuse the raw square36 with normalized square9.

The signs of q and of the CM orientations are not fixed by this computation. It produces an exact square, not a signed index. In particular its combination with a separately proved component-map normalization must retain that map's factor k. This file proves no new statement for the rank-two BSD seed.

## 1. Exact degree ratio, with every component correction retained

Use δ₀=q₀q₀∨ for the classical optimal quotient J₀(N)→C, and δ_X=qq∨ for the Shimura quotient. These are integers; δ_X should not be silently identified with the degree of a curve map until a rational divisor correction has been specified.

All rational elliptic curves in the isogeny class are isomorphic (the sibling component computation checks the singleton isogeny class). The minimal discriminant is

Δ_C=−3¹⁴·7·11²·167⁵.

Thus the geometric component orders at 3 and167 are 14 and5. The rational Tamagawa factor at3 is2, and must **not** replace geometric14 in this calculation.

Pastén, *Shimura curves and the abc conjecture*, arXiv:1705.09251v4, Proposition6.13, printedp29, gives

δ₀/δ_X = 14·5/(i₃² j₁₆₇²) = 5·14/(i₁₆₇² j₃²),

where i is the image size on classical geometric component groups and j is the cokernel size for the Shimura quotient. The proof explicitly states that this proposition does not require the remaining level847 to be squarefree. The later squarefree simplification is not being imported here.

Classical component groups at the multiplicative primes are Eisenstein. Therefore each i divides r+1−a_r(C) for every r∤N. Exact point counts give a₅=−3 and a₁₃=−2, whence each i divides both9 and16. Thus i₃=i₁₆₇=1. The two displayed formulas imply j₃=j₁₆₇. But j₃ divides14 and j₁₆₇ divides5. Consequently both j are1. We obtain

**δ₀/δ_X=70.**

This proof does not infer component surjectivity merely from optimality.

The external Cremona ecdata row records δ₀=20,576,640. Under this input, δ_X=293,952. The ratio70 proof itself does not require the absolute degree value.

## 2. The classical Manin factor is retained until proved

Let q₀*ω_C=c₀·2πi f(z)dz, c₀>0, f Fourier-normalized. The sibling comparison audit supplies a source proof that c₀=1: optimal Manin constants have no prime factors at primes with conductor exponent≤1; the only remaining candidate here is11. The conductor is cube-free, and the Česnavičius–Neururer–Saha theorem implies c₀|δ₀. Since11∤20,576,640, c₀=1.

This uses an integral theorem and the explicit degree record. It is not a conjectural Manin normalization or a unit chosen to fit the answer. To make the normalization visible, the analytic script computes n²/c₀² before c₀=1 is applied. Mazur's older prime-to-good-prime result alone would establish c₀∈Z₅×, but would not determine its square modulo5.

## 3. Gross–Zagier on the actual quaternionic curve

At3 and167, K is inert; at7 and11 it splits. Therefore the usual classical Heegner construction on X₀(N) is inapplicable. We instead apply Cai–Shu–Tian, arXiv:1408.1733v2, Theorem1.5 and Special case1 (printedpp6–7) on X₀^(501)(847), with χ=1 and conductor1. Since gcd(N,19)=1, Σ=Σ_D=∅; u=1. Their general formula gives

L′(C,1)L(C^(−19),1)
 = (8π²⟨f,f⟩/√19) · ⟨H,H⟩_K/δ_X.

The pairing convention is the K-height used in CST, the same one in its classical specialization Theorem1.1. For a rational point Y it is twice the absolute BSD height h(Y)=lim 4^(−r)h_x(2^rY). This conversion is corroborated independently by Keller–Stoll, *Complete verification of strong BSD for many modular abelian surfaces*, §3.7 Theorem3.7.1: their absolute normalized twice-theta height has denominator16π², and the proof explicitly converts the Gross–Zagier height by1/(2h_K), citing GZ Eq.(I.6.4). Here the class number is1. CST Theorem1.1 has denominator8π² and expressly cites the same Gross–Zagier formula. Its general theorem uses that same height pairing and its classical example recovers Theorem1.1. Thus ⟨H,H⟩_K=2n²h(Y). Independently, the known canonical Heegner point on37a1 for K=Q(√−7) is(0,0), and direct substitution gives K-height/absoluteBSDheight=2; see HEIGHT_CONVENTION_CONTROL.txt. The factor is not chosen to turn the large-curve numerical output into a square.

For A=Im(conj(ω₁)ω₂), the area of the Néron period lattice, pullback of the differential gives

4π² c₀²⟨f,f⟩=δ₀ A.

Consequently, using the exact ratio70,

**n²/c₀² = √19·L′(C,1)·L(C^(−19),1)/(280 A h(Y)).**

This is the numerical target actually evaluated. Its right side contains no assumed Sha order, no BSD quotient, and no fitted modular period. The identity itself is the rank-one Gross–Zagier theorem, whose hypotheses apply to this control curve.

## 4. Replayed ball arithmetic, including explicit infinite tails

Run `certified_GZ_ingredients.py` with the retained Sage Python runtime. It uses RealBallField/ComplexBallField at200 bits, not floating-point recognition.

1. Coefficients a_n are exact elliptic-curve coefficients. The root numbers are −1 for C and +1 for C^(−19). The standard approximate functional equations at1 become

L′(C,1)=2 Σ_(n≥1) a_n E₁(2πn/√N)/n,

L(C^(−19),1)=2 Σ_(n≥1) a_n(C^(−19)) exp(−2πn/√N_tw)/n.

With c=2π/√N and |a_n|≤d(n)√n≤2n, the absolute tails after M are bounded respectively by

4 exp(−c(M+1))/(c(M+1)(1−exp(−c)))

and 4 exp(−c(M+1))/(1−exp(−c)).

The cutoffs are12,000 and120,000. Ball arithmetic handles all finite-sum rounding. Coefficient-vector hashes are recorded.

2. The period area is evaluated by complete elliptic integrals on certified algebraic roots of the completed-square cubic. For e₁ real, e₂ upper-half-plane and e₃ lower-half-plane, put m=(e₂−e₃)/(e₁−e₃). The periods are2K(m)/√(e₁−e₃) and2iK(1−m)/√(e₁−e₃), with the indicated principal continuations. Their area agrees with the separate PARI/Sage period computation.

3. The canonical height is independently enclosed using Tate's archimedean series. All real points have x≥e₁>249. For z(t)=1−b₄t²−2b₆t³−b₈t⁴, exact real-algebraic critical-point isolation proves 1/1000<z(t)<10⁶ on[0,1/249]. This bounds the 42-term tail by log(10⁶)/(3·4⁴²). The only component correction for Y is at3: Y is singular in nonsplit I₁₄ and therefore has component7. At7,11,167 Y is nonsingular. After cancellation of the discriminant terms the BSD height formula is

h(Y)=log480 +(1/4)Σ_(r≥0)4^(−r)log z(1/x(2^rY)) −(7/2)log3.

The output is

- h(Y) ∈ [3.524059016863897789141230 ±2.85·10^(−25)];
- A ∈ [0.004849729069704556462455328873124839176321644731467528619276 ±8.77·10^(−61)];
- L′(C,1) ∈ [3.265902563746264982536719632615535041637651254 ±4.13·10^(−46)];
- L(C^(−19),1) ∈ [3.0253886055598639046371 ±6.68·10^(−23)];
- n²/c₀² ∈ [9.0000000000000000000000 ±8.27·10^(−23)].

## 5. Exact isolation, not arbitrary rational recognition

The retained rank statement is rank C(K)=rank C(Q)=1, with Y a saturated generator of C(Q)/torsion. For any actual point Q∈C(K), its anti-invariant part is torsion, so2Q differs by torsion from a rational point. Hence its coefficient relative to Y lies in(1/2)Z.

The degree-zero Hecke divisor D above is integral and q(D)=−2H. Therefore4n∈Z. Once c₀=1, n² belongs to(1/16)Z; the displayed enclosure contains exactly one such value,9. Thus n²=9 and n=±3.

For an independent check not presupposing c₀=1, the program uses the cusp strip y≥1 to obtain ⟨f,f⟩≥exp(−4π)/(4π). Together with the degree record and period area this gives c₀²<10¹⁰. Since4n is integral, the denominator of n²/c₀² is at most16·10¹⁰. Its distance from9, if nonzero, is at least1/(16·10¹⁰)=6.25·10^(−12), vastly exceeding the ball radius. Hence the program also isolates n²/c₀²=9 without an arbitrary denominator cap. This optional bound is mathematically derived; the simpler c₀=1 argument is preferred.

## 6. Effect and remaining interface

The normalized genuine CM source is now known to be ±3Y modulo torsion on this rank-one control, under the stated external/source inputs. Its Kummer class is therefore nonzero at5. With the predecessor's global affine 5-division-torsor identity it is ±3 times the image of κ_E(2P₁+P₂).

This is a source identification that the primitive-point instrument lacked. The component detector factor k remains a separately normalized comparison; combine its proof with n²=9 rather than absorb k into a chosen unit. No seed primary, uniform bound, ORDER9 or Q36 follows from this one control computation alone.

## Source and evidence boundaries

- Cai–Shu–Tian, https://arxiv.org/pdf/1408.1733 , Thm1.5/Special case1. General quaternionic formula, not intro Thm1.1's classical Heegner case.
- Pastén, https://arxiv.org/pdf/1705.09251 , Prop6.13 and its nonsquarefree qualification; §6.4 geometric component orders; proof Lemma6.14 for classical Eisenstein action.
- Česnavičius–Neururer–Saha, https://arxiv.org/pdf/1911.09446 , cube-free Manin-divides-degree result; detailed source matching in sibling comparison audit.
- Classical degree external record: https://raw.githubusercontent.com/JohnCremona/ecdata/master/alldegphi/alldegphi.420000-429999 . Row424347b1 gives20576640. We did not rerun the original modular-degree computation.
- Rational generator external record: corresponding `allgens.420000-429999`, row424347b1. Fresh saturation is in the sibling audit; the source row alone is not described as a new saturation proof.
- Height-normalization comparison: Keller–Stoll, https://www.mathe2.uni-bayreuth.de/stoll/papers/FiniteSupport.pdf , §3.7, Theorem3.7.1 and its explicit reference to GZ Eq.(I.6.4); the normalized height is with respect to twice the theta divisor. The independent37a1/−7 Heegner-point example is in Chao Li, https://par.nsf.gov/servlets/purl/10546610 , Table3.
- Tate archimedean series/local height formulas are standard imported formulas, executed here with explicit rounding and tail bounds. The enclosure code is same-worker checked until separately replayed; not kernel-certified.
