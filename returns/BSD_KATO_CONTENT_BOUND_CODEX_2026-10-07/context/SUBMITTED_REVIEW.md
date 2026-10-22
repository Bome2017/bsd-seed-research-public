# Review of the Rubin-coordinate follow-through
Date: 2026-10-07
Pinned project source: eddb24fe53e7450d7b9ff553ff3fd6ed038857ef

## Grade and scope

Desk review under the preceding retained Kato/control and placement hypotheses.
The local-log calculations below were independently recomputed using exact
rational elliptic-curve arithmetic. The height matrices and higher height digits
were read from the retained Sage output; the height engines were not rerun.
No Kato/Coleman coefficient or global source-lattice index was computed.
No FIN, ORDER9, or Q36 claim is made.

Files inspected at the pinned commit:
- REPORT.md
- COMPARISON_REVIEW.md
- COFINITE_NORMALIZATION.md
- SEED_CALIBRATION.md
- SOURCES.md
- INPUT_BINDINGS.json
- checks/SEED_COFACTORS.json (relevant short entries)
- evidence/reg17_sage.txt

All these paths are relative to
work/returns/BSD_RUBIN_COORDINATE_FOLLOW_CODEX_2026-10-07/.

## 1. Comparison and normalization

BKS, On derivatives of Kato's Euler system for elliptic curves,
arXiv:1910.07404v2, Theorem 6.2(i), has prefactor

    epsilon_rho=(1-rho^(-1))^(-1)(1-sigma^(-1)), sigma=p/rho.

Its Hypothesis 2.2 includes primary finiteness. The source-derived formula and
the project's finiteness-free case split must be distinguished:
nonzero delta supplies the needed finiteness under the retained control theorem;
zero delta is treated by Col(M) contained in U H_infinity, not by deleting the
source hypothesis.

The reported fixed-source argument is valid as a finite-support normalization
argument, provided the modular parametrization, rational projection, Betti input
and smoothing are fixed as specified. Full rational Betti lattices are
commensurable. Compatible comparison for the same map then gives one fixed
finite exceptional support.

This controls normalization errors. It does not control the intrinsic content
of a derivative and does not give a Sha annihilator. The source-lattice integer
has not been computed, so a cofinite assertion does not establish that p=17 is
outside its support.

The ordinary interpolation comparison is consistent with BKS Section 6.1:
the coefficient-prime Euler factor at the trivial character cancels against
the displayed interpolation prefactor. Since the functions already vanish
to order at least two, multiplication by an Euler/smoothing series changes
their quadratic coefficients only by its constant coefficient.

This is distinct from the Rubin prefactor epsilon_rho, whose valuation is -1
at a nonanomalous ordinary prime. Supersingular distributions and heights must
retain their root-specific conventions; the ordinary bounded-measure calculation
does not replace those checks.

## 2. Independent finite arithmetic at 5 and 17

Using E: y^2=x^3-x^2-66020924x-65074271436,
P1=(-3031,327384), P2=(-2394,281520):

    #E(F5)=8;  (log(P1)/5, log(P2)/5)=(0,2) mod 5.
    #E(F17)=24; (log(P1)/17,log(P2)/17)=(2,13) mod 17.

The computation uses -x(nP)/y(nP)/(np) modulo p, for n=#E(Fp), and repeats
with 2n. All point additions are rational and checked on the curve.
It uses log(t)=t mod p^2, valid here for p>=5 and the formal parameter in pZ_p.

Combining with the retained matrices:

    H5 mod5  = [[2,2],[2,0]];
    H17 mod17 = [[13,5],[5,15]],

gives divided cofactor vectors (1,4) mod5 and (16,6) mod17.

The first two retained native-height coefficients at 17 are:
h11=13*17+16*17^2+O(17^3);
h12=5*17+7*17^2+O(17^3);
h22=15*17+12*17^2+O(17^3).
Their determinant has valuation 3 and leading unit 13.
After dividing each height by log_17(18), the determinant has valuation 1
and det(H_gamma)/17=13 mod17. This verifies the downstream determinant
calculation, not the original height-engine computation.

## 3. A more explicit CONDITIONAL residue formula at 17

Assume exact agreement with the displayed BKS height coordinate, source,
differential, gamma and Coleman convention. Let

    K=K17=[U^2]Col_rho(z),
    ell=(log(P1),log(P2))^t.

The reviewed comparison reads H_gamma*(A17,B17)^t=epsilon_rho*K*ell.

The ordinary unit root satisfies rho=-6=11 mod17. Hence

    17*epsilon_rho = rho(17-rho)/(rho-1) = 10 mod17.
    det(H_gamma)/17 = 13 mod17.
    adj(H_gamma)*ell/17 = (16,6) mod17.

Integrality of the actual A17,B17 forces K in 17 Z_17. Put k=K/17.
Then

    (A17,B17) = k*(11,2) mod17.

Calculation: 10/13=6 mod17 and 6*(16,6)=(11,2) mod17.

This adds no K-value and no primitivity result. It specifies what the missing
second digit would do under exact convention matching. If the height convention
is known only up to a common unit, retain only the projective direction
[16:6]=[11:2] and the valuation criterion, not this absolute residue multiplier.

In particular:

    min(v17(A17),v17(B17)) = v17(K17)-1

with the zero case treated as both coordinates zero. K17=0 mod17 is forced
and is not a failed primitivity test. The test is K17/17 != 0 mod17.

## 4. Concrete smoothing check

For the proposed fixed parameters c=1+6N,d=1+12N:

    c,d mod17=(11,4);
    cd(c-1)(d-1) mod17=11, a unit.

At 5, c=0 mod5. Thus the proposed fixed source excludes 5 through its
smoothing support. The old p=5 numerical calibration need not use that source,
as the report already cautions. This is not a contradiction.

This does not resolve the separate Betti-image index or the height convention
at 17.

## 5. Exact remaining scope

No extra valuation upper bound has been proved. On the nonsingular ordinary,
matched-source domain, integrality gives a lower bound

    v_p(K_p) >= r_p-c_p+1,

where r_p=v_p(det H_p) and c_p=min v_p(adj(H_p)*ell_p).
Primitivity requires equality. The present calculations show why the correct
question is that equality rather than unitness of K_p or of the regulator
separately. They do not show the equality holds cofinitely.

A finite-source normalization theorem and a correlated-valuation theorem are
different statements. The first now has a written argument; the second remains
unproved.

## Sources

Project report:
https://github.com/Bome2017/bsd-seed-lab/blob/eddb24fe53e7450d7b9ff553ff3fd6ed038857ef/work/returns/BSD_RUBIN_COORDINATE_FOLLOW_CODEX_2026-10-07/REPORT.md

Source normalizations and height data: companion files named above at the same
pinned commit.

BKS:
https://arxiv.org/html/1910.07404v2
Sections 2.1–2.2, 5.1, 6.1, Theorems 6.2 and 6.10.
The paper supplies the published theorem, not independent certification of the
project's finiteness-free extension.
