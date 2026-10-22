# Item 1 — Route K cross-family source reading

**1a PASS. 1b PASS with the E2/E3 normalization explicitly understood. 1c PASS with E1. 1d PASS at the retained height-certificate grade.**
**K-Astra-1: the factor-3 and factor-9 failure scenarios are excluded at these grades.**

This is an independent Codex reading of the written deduction, not a reproof of all imported theorems, a human referee report, or a replay of the large symbol/descent certificates. The source-first conclusions were saved in ITEM1_PRECOMPARISON.md before reading the three earlier checks. Their results agree with this reading. No blocking error found.

## 1a. D5 Step 1: zero Coleman cokernel

Target line: “Col ... is an ISOMORPHISM (injective, cokernel 0).” This survives.

Let K_n be the Delta-fixed cyclotomic layer and L_n its unramified quadratic extension. The eta-eigenspace of the 3-adic completion of L_n^* has no valuation component; its principal-unit part identifies by twisted Kummer theory with H^1(K_n,Z_3(1) eta), and by the unramified Tate formal-group identification with E-hat(m_n). This supplies the integral justification that equality of ranks alone would not supply.

The unramified quadratic character stays nontrivial throughout the totally ramified tower. Thus its invariant divisible 3-primary groups vanish, as do the dual H^2 obstructions. Norms on the anti-invariant unit modules are onto. For every subgroup of Gamma_n the same argument applies; together with Herbrand quotient one this gives cohomological triviality. The finite-level module is Z_3[Gamma_n]-free of rank one. Under coinvariants, norm(c_n)=c_0; log(c_0)=3/2 generates 3Z_3. Nakayama therefore makes c_n a group-ring generator. Integral local duality makes the Coleman map an isomorphism, not merely a rational one.

Kato 17.12 is consistent with this: its local Coleman proof places the possible cokernel inside the unramified Frobenius coinvariants. For eta, Frobenius minus one is -2, a 3-adic unit. Its printed statement concerns its own T(1) normalization; we do not silently substitute it for the explicit D5 construction.

D1/D2 provide the norm-compatible points; the Dwork proof needs E6's retained unit factor in the coefficient induction. Restoring that factor preserves the integrality conclusion. Local duality, twisted Kummer theory and the cohomologically trivial lattice theorem remain textbook imports.

## 1b. D5 Steps 2–3: the exact series

Target line: “Col(loc_3 z_gamma) = L_3 ... EXACTLY.” Correct with a fixed period, lattice generator and the E3 Tate-twist dictionary; not as a literal equality to unshifted Kato notation or to a differently normalized period.

For a nontrivial even character chi of conductor 3^m, the direct pairing calculation gives

    chi(Col(loc z)) = alpha^(-m) tau(chi) L(E,chi^(-1),1)/Omega_+, alpha=-1.

Kato 12.5(1), applied to chi^(-1), supplies the second bracket. The norm-compatible logarithms supply alpha^(-m) tau(chi). Since tau(chi) tau(chi^(-1))=3^m, this is Stein–Wuthrich §3.2 with the SAME measure convention. No inversion of Gamma is required. At the trivial character, (3/2)(1+1/3)=2, the nonsplit multiplier.

Both series are bounded; equality at all nontrivial finite-order characters forces equality by Weierstrass preparation. This does not need the noncrystalline Perrin–Riou assertion attributed to unpublished KKT. Kato's own function is evaluated at kappa*chi when the Coleman/SW series is evaluated at chi. The plus-cycle period and total real period can differ by 2, so the certificate comparison remains equality up to a specified 3-adic unit, as D7 requires.

## 1c. D6: primitive Selmer and the integral inequality

Target line: “char_Lambda(X) | L_3 in Lambda ... (P=(3) included).” Correct after E1.

Kato 13.4(3) applies to every height-one prime. Residual irreducibility, p=3!=2, and the retained full 3-adic image meet its integral hypotheses: a unipotent matrix in SL_2(Z_3) has free rank-one cokernel for 1-sigma. Kato 13.14 supplies the passage from Euler-system lattices to Z(f,T) up to a finite Lambda-module, invisible at height one. H^1 is free of rank one by 12.4(3), so its evaluation ideal J measures H^1/Z. Since H^2_loc=0 here, H^2_0=H^2.

The final inequality printed in 12.5(4) uses V and is not the justification at (3). Its integral-containment assertion remains usable. These two uses must not be conflated.

At 3 the nonsplit ordinary local condition equals the Bloch–Kato/classical condition integrally: the quotient H^1(K_n,Z_3 eta) has no torsion, making the formal-group image saturated. Away from 3, the j_* condition in Kato 8.2/12.2 and the away-from-p argument of 17.10 give the classical condition in the cyclotomic direct limit. That argument does not require good reduction at those places. Only the good-ordinary p-local part is replaced.

Consequently the four-term sequence gives

    length X_P - ord_P(L_3) = length H^2_P - length(H^1/Z)_P <= 0.

The 5843 factor is retained in Kato's L_{ {3} }; it is not removed on either side. Switching to an imprimitive object would insert 1+1/5843, of valuation 1, but route K does not do so. This excludes the hidden-factor-3 kill scenario.

## 1d. D8: Jones gives 9, not 81

Target line: “v_3(Reg_gamma)=0 ... #Sha[3^inf] <= 9.” Correct with the independently retained normalized regulator.

First, restriction is injective because E(Q_infty)[3^inf]=0. Rank two gives ord_T char(X)>=2. Since char(X)|L_3 and the certified quadratic coefficient has valuation 2, write char(X)=T^2 g and L_3=T^2 h, with g|h and v_3(g(0))<=2. This also bounds the base Selmer corank by two, proving primary finiteness BEFORE applying Jones.

Jones's author copy, printed pp.3–6 and 17–18, requires this finiteness, semistability at p, the stated universal-norm condition (explicitly covered for nonsplit multiplicative elliptic curves), and nondegeneracy of the height. Bad primes split finitely in the cyclotomic extension; none has trivial cyclotomic Frobenius. The nonsplit case has e=0. Its analytic-variable formula must be converted to T by dividing the regulator by log_3(kappa(gamma))^2:

    g(0) = (3-adic unit) * #Sha[3^inf] * Reg_gamma,
    Reg_gamma = Reg_3 / log_3(4)^2.

All seed Tamagawa and rational-torsion factors here are 3-units. The sign and 2! are also 3-units.

Fresh tiny PARI corroboration (checks/normalization.gp, 0.231 seconds wall time, clean exit/stderr) on the supplied minimal model and points gives v_3(Reg_3)=2 at precisions 8,11,14 and v_3(log_3 4)=1, hence v_3(Reg_gamma)=0. It also gives a_3=-1 and v_3(15480)=v_3(7740)=2. This is independent numerical corroboration; the saturated-basis certificate and the identification of the computed canonical height with Jones's height retain their recorded grades. It is not a replacement formal interval proof of those imports.

Thus v_3(#Sha[3^inf])<=2. The retained B2 subgroup (Z/3)^2 supplies the lower bound and exponent, giving Sha[3^inf]=(Z/3)^2. No Cassels–Tate square fallback is needed. Mistaking a gamma-free regulator of valuation zero for the normalized one would permit 81; the actual evidence has gamma-free valuation TWO, excluding that scenario.

## Label and boundary

A precise permitted description is: “Route K has a cross-family source reading of D5/D6/D8 with E1–E7, at the recorded arithmetic-input and imported-theorem grades.” Do not label it fully independently recomputed or human-refereed. This audit does not modify the release or its label.

Retained inputs: the full 3-adic image (including the recorded secondary classification facts), the symbol coefficient certificate and its precision bound, rank and saturation, the canonical-height comparison/certificate, and B2 exact descent. Jones was checked in the author's copy; no fresh journal/preprint reconciliation was performed. The textbook foundational results were used, not reproved.

Primary references: Kato, Astérisque 295 (2004), https://www.numdam.org/item/AST_2004__295__117_0/; Jones, author's “Iwasawa L-functions for multiplicative abelian varieties,” linked from https://hobbes.la.asu.edu/papers.html; the pinned local Kobayashi and Stein–Wuthrich texts. Full local bindings are in SOURCE_BINDINGS.tsv.
