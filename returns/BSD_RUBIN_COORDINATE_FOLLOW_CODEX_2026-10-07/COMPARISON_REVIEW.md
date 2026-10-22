# Finiteness-free Rubin comparison: review of the submitted argument

2026-10-07. **RUBIN_COMPARISON_CONFIRMED_UNDER_RETAINED_INPUTS.**
This is a written mathematical review, not a machine-checked or human-certified theorem. The preceding Kato construction, image theorem, saturated basis and integral criterion retain their original grades. The published source was read, including its finiteness hypothesis; that hypothesis is not silently deleted.

## 1. Fixed objects

Use the submitted model, differential, full Mordell–Weil lattice and domain

    D = {p >= 5 : p does not divide N, p not in {19,59,487}}.

Write U=gamma-1, M=H^1_Iw, z=Uy, and delta=aug(y)=A kappa(P1)+B kappa(P2). These are the actual transported smoothed class and its derivative. In particular no power of p has been divided out of z. The retained conclusions are: M is free of rank one, M/UM injects into integral global H^1, delta is in the integral point lattice, delta nonzero implies primary finiteness, and a primitive coordinate pair implies primary vanishing on D.

For an allowable root rho of X^2-a_p X+p, put sigma=p/rho and

    epsilon_rho = (1-rho^(-1))^(-1)(1-sigma^(-1)),
    K_rho = [U^2] Col_rho(loc_p z).

The height below is its coefficient in the U-basis of I/I^2. It is not the numerical height obtained after applying log_p to the cyclotomic character without dividing by log_p(chi_cyc(gamma)).

## 2. Rational local-finiteness lemma

For q different from p, E(Q_q) has finite p-primary torsion: an open subgroup is pro-q and the quotient is finite. Thus V_pE has no local invariants. Weil self-duality and local Tate duality give H^2(Q_q,V_pE)=0. The rational local Euler characteristic gives H^1(Q_q,V_pE)=0. This assertion concerns rational cohomology; it does **not** say that the corresponding finite-coefficient groups vanish.

At a good p, E(Q_p) has a one-dimensional rational Kummer image. Its formal logarithm has torsion kernel on E(Q_p): multiplication into the formal group reduces the claim to the injective formal logarithm on a sufficiently small open subgroup. A nontorsion rational point consequently gives a nonzero local Kummer class and spans this line.

Apply global reciprocity to an arbitrary global rational class x and that rational point. All local pairings away from p vanish by the preceding paragraph (the odd-p real term also vanishes). The local pairing at p is therefore zero. Since the Kummer line is its own annihilator under local Tate duality, loc_p(x) belongs to it.

No global identification with the Mordell–Weil group was used. Rational Tate-module Sha directions have not been discarded.

By the constant interpolation formula for the Coleman map, its augmentation on any global Iwasawa class is zero: the dual exponential kills this local Kummer line. Hence

    Col_rho(M) is contained in U H_infinity.

At a supersingular prime this is a statement about the constant Taylor coefficient of a distribution. It is not an assertion that its coefficients are p-integral.

## 3. The case split is valid

If delta is nonzero, retained control proves primary finiteness. BKS Hypothesis 2.2 is then available in this branch. Theorem 6.2(i), applied before cancelling the smoothing factor, gives

    h_rho(P,delta) = epsilon_rho log_omega(P) K_rho.       (R)

This is exactly the formula printed on page 896; the smoothed formula and cancellation are on page 903. Simultaneously transporting the class and its coefficient lattice scales both sides by the same scalar. This does not make that scalar a p-unit relative to a separate numerical source.

If delta is zero, injectivity of M/UM into H^1 gives y in UM, so z is in U^2M. The lemma above gives Col_rho(z) in U^3 H_infinity, and K_rho=0. Both sides of (R) vanish, without invoking primary finiteness in this branch.

Thus (R) holds for this class in both cases under the retained inputs. The derivation introduces neither an ordinary filtration nor a nondegeneracy assumption. BKS's supersingular height uses its specified (phi,Gamma)-module local condition; arbitrary numerical supersingular heights cannot be substituted for it.

## 4. Coordinates and the exact content

Let H=(h(P_i,P_j)) and l=(log P1,log P2)^t. Equation (R) is

    H (A,B)^t = epsilon_rho K_rho l.

If det H is nonzero, put c = min valuation of the entries of adj(H) l and r=v_p(det H). For K_rho nonzero,

    min(v_p(A),v_p(B)) = v_p(K_rho)+v_p(epsilon_rho)+c-r. (C)

At a non-anomalous ordinary prime, rho is a unit, rho-1 is a unit and sigma has valuation 1. Consequently v_p(epsilon_rho)=-1. At a good supersingular prime both roots have valuation 1/2, and the numerator and denominator in epsilon both have valuation -1/2. Consequently its valuation is 0. These are the Rubin prefactors; they are not the ordinary MTT interpolation factor (1-rho^(-1))^2, which is a unit on the non-anomalous domain.

Integrality of the actual A,B supplies the lower bound

    v_p(K_rho) >= r-c-v_p(epsilon_rho).

Primitivity is equality, not an independent assertion that r=0. If K_rho=0 and H is nonsingular, the pair is zero. If H is singular, do not divide: a nonzero row gives

    min(v_p(A),v_p(B)) <= v_p(epsilon_rho K_rho l_i)
                         - min_j v_p(h_ij).

A right side strictly less than 1 forces primitivity, because the left side is a nonnegative integer. The same logic works with fractional root-field valuations.

## 5. Scope

This confirms the submitted comparison at its stated conditional grade. It does not prove a new nonzero Kato coefficient or a cofinite equality in (C). An equality that calculates the coordinate content is not itself an upper estimate for that content. FIN, ORDER9 and Q36 are unchanged.

Source: Burns–Kurihara–Sano, JMSJ 76 (2024), 855–919, Hypothesis 2.2, Sections 5.1 and 6.1–6.4, Theorems 6.2, 6.10, 6.11 and Lemma 6.14. The published numbering matches the submitted v2 numbering at these interfaces. Local copy binding and pages inspected are in SOURCES.md.
