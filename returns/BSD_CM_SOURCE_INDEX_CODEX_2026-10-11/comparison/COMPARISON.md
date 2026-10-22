# Source-normalized Gross-Zagier and monodromy comparison at 167

Date: 2026-10-11. Scope: the admitted rank-two control model E=2541c1, its rank-one level-raised partner E1=424347b1, K=Q(sqrt(-19)), and coefficient prime 5. This is not an application of a rank-one theorem to the rank-two BSD seed.

## Outcome

There is a concrete way to eliminate the unknown scale of the Shimura parametrization from the square of the desired source ratio. Generalized Gross-Zagier supplies the height divided by the polarized quotient degree. Functorial monodromy supplies that degree divided by the square of the component-source index. Their product is (n/k)^2, after retaining the explicit Hecke correction used to define the CM source.

The companion GRAPH_NORM_COMPARISON.md derives the residual monodromy factor 2 at 5 under the retained C3 framework and the executed small Brandt calculation. The new Manin-constant deduction below removes a separate classical period uncertainty: for the optimal classical parametrization of this partner, c0=1 follows from published theorems and the retained degree record. Combining these deductions with the sibling CM calculation and coefficient-lattice audit now gives

    k^2=1,   (n/k)^2=4 in F5.

Here n is the coefficient of the correctly normalized residual CM source, not the raw Hecke divisor. Thus its oriented normalized value is either 2 or -2; its sign remains unevaluated. This is an actual source nonvanishing result for the admitted control model, conditional on the explicit geometric/theorem inputs. It is not a seed uniform bound.

## 1. The appropriate Gross-Zagier theorem

Use Cai-Shu-Tian, arXiv:1408.1733v2, Theorem 1.5 and its Special case 1 on printed page 7, not the introductory classical Heegner statement. Set N=424347=3*7*11^2*167, conductor c=1, trivial ring-class character, and K discriminant -19. The relevant indefinite algebra has discriminant 3*167; the Eichler level is 7*11^2=847. The primes 3 and 167 are inert, while 7 and 11 split. The ordinary X0(N) Heegner hypothesis therefore fails, but the quaternionic local epsilon condition is the intended one. The local-order intersection must be O_K at each place. In particular the split level at 11^2 is permitted; the general theorem does not require squarefree N. Also gcd(N,19)=1, and h_K=u_K=1.

For an oriented CM point P and the degree-one Hodge class xi on X, write P_H=[P-xi] in J(K) tensor Q. For a quotient pi:J -> E1 define Q_H=pi(P_H) and delta by pi*pi^vee=[delta]. With the paper's K-height pairing and Petersson measure, the theorem has the form

    H_GZ := sqrt(19)*L'(E1/K,1)/(8*pi^2*(g,g)_Gamma0(N))
          = height_K(Q_H)/delta.

The chosen local admissible order, CM orientation, height convention, and finite-versus-completed L-function convention must be matched before substituting numeric values. There is no Sha-order factor in this theorem. Its left side must be evaluated by actual L-series/period arithmetic, not an analytic BSD prediction of a Sha order.

## 2. Match the actual Hecke-corrected source to P_H

For any q away from N, T_q xi=(q+1)xi in Pic(X) tensor Q. Thus the degree-zero divisor (T_q-(q+1))P maps under pi to (a_q(E1)-(q+1))*Q_H. This is an equality of rational points modulo torsion, not an unknown period unit.

For example a2(E1)=-1, so

    D_2 = -(T2-3)P/4

has coefficients in Z_(5) and satisfies pi(D_2)=Q_H modulo torsion. This is an alternative normalization, not a replacement for the already prescribed source.

The current integral Hecke correction uses

    D_raw = [2(T5-6) - (T13-14)]P.

The exact traces a5(E1)=-3 and a13(E1)=-2 give

    pi(D_raw) = [2*(-9)-(-16)] Q_H = -2 Q_H.

It is essential to retain the multiplier -2. In the base eigensystem, a5(E)=-3 and a13(E)=-7, so the same operator has scalar 2*(-9)-(-21)=3. The predecessor's canonical degree-correction map applies the inverse of this base scalar modulo 5. Thus the actual residual source is (1/3)Kum(D_raw), whose elliptic image is (-2/3)Kum(Q_H). Since -2/3=1 in F5, the normalized residual source equals the Hodge-normalized residual source. Equivalently the auxiliary normalization (-1/2)D_raw gives the same residual class, because -1/2=1/3 modulo 5. These are specified integral units; no unit is fitted to the output.

If Q_H=rY in E1(K) tensor Q for Y=(480,22723), then the raw coefficient is -2r and the normalized residual coefficient is n=(-2/3)r=r modulo 5. The absence of 5-torsion makes this valid for Kummer classes. The sibling coefficient-lattice audit now proves the needed denominator bound 4r in Z, and the certified CM calculation proves r^2=9. Therefore n^2=4 modulo 5. Neither raw square36 nor Hodge square9 may be substituted for a differently normalized scalar without this calculation.

## 3. Quotient scale cancels exactly

Let X_167(J) be the character lattice, with its integral monodromy pairing. For a generator of X_167(E1)=Z, put v=pi^*(1). The geometric component group of E1 has order 5. Functoriality gives

    <v,z>_J = 5 lambda(z),   lambda(v)=delta,
    <v,v>_J = 5 delta.

If x in X_167(J)^vee lifts the specified normalized component source, then its image on E1 components is k=x(v) modulo 5. For any nonzero integer r, replacing pi by [r]pi multiplies v and x(v) by r and delta by r^2. Hence delta/x(v)^2 is invariant under such a replacement. This is why the parametrization's unknown scale can be removed; it does not assert that an arbitrary scale is a 5-unit.

Writing v=s*v0 for a primitive rational eigenvector, h=<v0,v0>, and a=x(v0), one obtains

    delta/x(v)^2 = h/(5*a^2).

With the same K-height convention throughout, the exact source-square identity is

    (n_raw/x(v))^2 = 4 * H_GZ/height_K(Y) * h/(5*a^2).

For the canonical source represented over Z_(5) by D_raw/3, the rational square has an additional factor 1/9. Reducing after the proved coefficient bounds gives the normalized residual ratio.

For a residual comparison x(v) must be a 5-unit; that is precisely the separately proved component-unit statement. Changing the representative x changes its integer evaluation but not the residue k, so use a fixed representative for any rational equality. The residual graph lemma computes the residue of the last factor without constructing v0. The square loses the sign of the oriented scalar n/k. It can establish unitness or a squared comparison; it cannot distinguish opposite signs.

## 4. The classical Manin constant is actually 1 here

Let pi0:X0(N) -> E1 be the optimal classical modular parametrization, and c0 its positive Manin constant for the Neron differential. The singleton rational isogeny class in the current component control identifies this optimal curve with the displayed E1. Retain the exact classical degree record

    delta0=20576640=2^7*3*5*7*1531.

Cesnavicius-Neururer-Saha, arXiv:1911.09446v3, Theorem 1.2 proves c0 divides delta0 when N is cube-free. This N is cube-free. For an optimal parametrization c0 is supported only on additive-reduction primes; the same primary paper's introduction records the semistable-prime result, including 2, from Cesnavicius (2018). Here the exact local reduction table has multiplicative types I14,I1,I5 at 3,7,167, good reduction away from 3,7,11,167, and type II at 11. The only possible prime divisor of c0 is therefore 11. But 11 does not divide delta0. Thus

    c0=1.

This does not invoke the general Manin conjecture, empirical verification below a conductor cutoff, or BSD. It does rely on the degree record and the optimality/model identification already stated. It concerns the classical parametrization; it does not identify a separate Shimura differential constant with c0.

Consequently the ordinary area identity for pi0 may be used with no undetermined Manin factor:

    delta0 * area(E1(C),omega) = 4*pi^2*(g,g)_Gamma0(N).

Use the area and the K-height normalizations consistently. In particular the convention in which height_K(Y)=2*height_Q(Y) must not be silently replaced by Sage's absolute height. The separate CM computation is responsible for the numeric convention check and rigorous enclosures.

## 5. Direct computation choices and exact limits

The two concrete continuations are now:

1. Obtain a certified real enclosure for the source-square identity, together with an independently proved rational denominator/lattice bound. This has now been executed in ../cm/RESULT.md and ../cm/CERTIFIED_GZ_INGREDIENTS.json, with the lattice in ../component/BASIS_AND_DEGREE_REVIEW.md: the enclosure for r^2 has radius below 10^-21 around 9 and r^2 belongs to (1/16)Z. Exactly one allowed value remains, so r^2=9. The parent reports an independent replay of the enclosure code. This note did not independently replay that analytic computation a third time.
2. Compute the actual CM Abel-Jacobi image by quaternionic uniformization and compare its local elliptic logarithm with Y. Bertolini-Darmon (1999), Section 4, provides multiplicative-divisor/monodromy machinery. It still requires the actual lattice and path data; it does not let an arbitrary rational point substitute for the CM source.

The first route is substantially smaller once the separate quotient-degree calculation and c0=1 are supplied. The graph comparison independently constrains its mod-5 normalization. Neither route needs a conjectural Sha value. The result remains a calibration on a level-raised rank-one partner; extending this comparison to the original seed would require the separate global source theorem.

Hamidi arXiv:2607.23244v1 cannot be applied directly to replace the degree calculation: its standing level hypothesis is squarefree, whereas 11^2 divides this N. Its computational diagrams are relevant, but its squarefree theorem has not been transported here.

## Sources freshly read

- Cai-Shu-Tian, *Explicit Gross-Zagier and Waldspurger Formulae*, Theorem 1.5, Special case 1, and definitions of normalized Hodge class, U-pairing, admissible order, and Petersson norm: https://arxiv.org/pdf/1408.1733 . Source text was read; no fresh visual PDF audit is asserted.
- Cesnavicius-Neururer-Saha, *The Manin constant and the modular degree*, Theorem 1.2 and introduction/footnote 4: https://arxiv.org/pdf/1911.09446 .
- Bertolini-Darmon, *Iwasawa's Main Conjecture for elliptic curves over anticyclotomic Zp-extensions*, Section 5: https://www.math.mcgill.ca/darmon/pub/Articles/Research/27.Main-conjecture/pub27.pdf .
- Bertolini-Darmon, *p-adic periods, p-adic L-functions and the p-adic uniformization of Shimura curves*, Section 4: https://www.math.mcgill.ca/darmon/pub/Articles/Research/20.Periods-Cerednik/pub20.pdf . Its strong-Weil quotient convention must remain attached.
- Hamidi, arXiv:2607.23244v1, Section 2 squarefree setup and Section 10 algorithms: https://arxiv.org/html/2607.23244v1 . Read only as a scoped comparison, not as an applicable theorem here.

## Endpoint effect

The three source ingredients now combine on this control model: the actual CM source is nonzero modulo 5, the component factor is a unit with k^2=1, and the normalized ratio satisfies (n/k)^2=4. Its signed residue is still one of 2,-2; no exact affine CM coordinate is claimed. The ratio and Manin arguments are written deductions, not formal certificates or claims of novelty. FIN, ORDER9 and Q36 for the fixed BSD seed remain unchanged.
