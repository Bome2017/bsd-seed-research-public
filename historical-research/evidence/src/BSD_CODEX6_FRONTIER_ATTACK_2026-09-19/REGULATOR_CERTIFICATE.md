# Rigorous regulator and reconstruction certificate

**PROVED_COMPUTER_ASSISTED**, with the explicit arithmetic trust base below. This closes the numerical prerequisite of the D<=174 reduction. It does not prove rationality or FORMULA.

## Result

For the fixed curve and the retained full Mordell–Weil basis P1=(4547,327384), P2=(5184,281520), the BSD-normalized regulator satisfies

    17.79651747249034020748 < Reg < 17.79651747249034039153.

The independently enclosed real period and regulator give

    0.99820315980984172437 < Omega*Reg < 0.99820315980984173470.

Combining this with the retained Arb certificate L''/2 in [35.929604,35.941023] proves

    35.99427 < q_infinity < 36.00573.

Consequently, **q_infinity rational with reduced denominator <=174 implies q_infinity=36**. This conclusion is now supported by rigorous enclosures on both sides of the quotient. No long L-series evaluation was run.

Files: `verify_regulator.py`, `REGULATOR_INTERVAL_100D_30.json`, `REGULATOR_INTERVAL_80D_24.json`. The JSON contains more precise outward endpoints and every exact local check.

## Material older artifact found

Lane 3 already contains `B_invariants/06_period_regulator.md`, `B_invariants/scripts/rig_lib.sage`, `B_invariants/scripts/s06_seed.sage`, `B_invariants/out/s06_seed.out`, and saved balls. Its method really is an interval Tate-series computation; the handoff's statement that Reg was only a PARI value is incorrect. The old output agrees with the new interval.

One implementation detail prevents treating the old code as a fully explicit directed-rounding certificate without further argument: it converts the extremal z bounds to Sage `RR`, computes logarithms, and inflates the result by 1.000001 to choose M. That is a generous numerical margin but is not itself a written outward-rounding proof. We preserve the old bytes and replace this step by the exact bound |log z|<50. This is a small hardening of a located older route, not a newly discovered height algorithm.

## Mathematical derivation

Use the translated real model x_t=x+2. Its coefficients are obtained exactly by substituting x=x_t-2. Put t=1/x_t and

    z(t)=1-b4*t^2-2*b6*t^3-b8*t^4,
    w(t)=4*t+b2*t^2+2*b4*t^3+b6*t^4.

The exact duplication identity is t(2P)=w(t(P))/z(t(P)). Tate's x-normalized local height is

    lambda'_infinity(P) = (log x_t(P))/2
                         + (1/8) sum_(j>=0) 4^(-j) log z(t(2^j P)).

The identity x_t(2P)=x_t(P)^4 z(t(P))/(2y(P))^2 verifies its duplication equation. Near O the correction tends to zero, giving the standard local-height normalization. These are the usual Tate local-height identities used in the older project certificate; no BSD identity enters.

The nonzero real roots e2<e1 of x^2-22735x+106272484 satisfy e2+2<6600 and e1+2>16000: direct substitution at 6598 and 15998 gives negative values, hence both lie strictly between the two roots. Both roots are positive. Therefore the real t-values belong to

    [0,1/16000] union [1/6600,1/2].

The script certifies **1/4 < z(t) < 2^50** on these enclosing intervals, using only exact rational arithmetic:

1. On [0,1/16000], split into eight equal intervals and convert the quartic to the Bernstein basis. Every coefficient exceeds 1/4. Bernstein basis functions are nonnegative and sum to one, so this bounds the polynomial on the whole interval.
2. On [1/6600,1/2], z'/t=-2b4-6b6*t-4b8*t^2 is positive at the left endpoint and increasing, because b6,b8<0. Check z(1/6600)>1/4.
3. The sum of the absolute coefficient bounds at |t|<=1/2 is less than 2^50.

Since log 2<1, this proves |log z|<50. Truncating after n terms therefore has error at most

    (1/8)*50*sum_(j>=n)4^(-j) = 50/(6*4^n).

No floating-point estimate is used for this tail.

For each R in {P1,P2,P1+P2}, compute Q=2R exactly. The script verifies the curve equation and smooth reduction of Q at every bad prime. If a prime divides the x-denominator, primitive weighted coordinates reduce to the smooth point at infinity; otherwise both affine partial derivatives are checked. The model is minimal because the verified discriminant factorization has every valuation below 12.

For a point Q in E0 at every finite prime, the finite x-normalized local-height contribution is (1/2)log den(x(Q)). Hence in BSD/Cremona normalization

    H(R) = [2 lambda'_infinity(2R) + log den(x(2R))]/4,
    <P1,P2> = [H(P1+P2)-H(P1)-H(P2)]/2,
    Reg = H(P1)H(P2)-<P1,P2>^2.

Here H(R)=lim 4^(-j) h(x(2^j R)), agreeing with the normalization in the retained regulator and BSD target. The factor of two has not been inferred from numerical agreement.

The real period is enclosed independently by

    Omega = 2*pi / AGM(sqrt(e1),sqrt(e1-e2)).

Every AGM lies between its geometric and arithmetic iterates; the script encloses both after 18 steps. Pi is enclosed using Machin's identity and exact rational alternating-series bounds for arctan(1/5), arctan(1/239). The imported p=3 period bracket is used only as an overlap check, not to compute the final quotient.

## Arithmetic and verification boundary

The standalone implementation uses Python integers/Fraction for exact algebra and Decimal intervals for transcendental evaluation. Each elementary operation rounds the lower endpoint toward minus infinity and the upper endpoint toward plus infinity. Correctly rounded ln and sqrt are widened by one representable value on each side. [Python's Decimal specification](https://docs.python.org/3/library/decimal.html) documents these arithmetic guarantees.

Run at 100 decimal digits with 30 Tate terms; replay at 80 digits with 24 terms. Both pass exact polynomial, point, local-smoothness and reconstruction checks. The stronger enclosure nests inside the weaker one. A replay under the bundled Python 3.12.14 agrees in every arithmetic field with Python 3.13.2. REPLAY_VERIFICATION.json records the checks and measured CPU times (each below 0.12 CPU-second in the final replay). This is a different arithmetic implementation from Sage/Arb and PARI, although it uses the same standard Tate-series formula.

The current interval contains both 36-1/175 and 36+1/175, verified by exact rational comparisons. Thus 174 is the largest universal reduced-denominator cutoff certified by this interval alone; the choice is not a half-unit rounding convention.

Trust base: Python's exact integers/Fraction and libmpdec implementation; the displayed local-height and AGM theorems; the retained basis/index-one result; the retained Arb L'' certificate; operating system and hardware. This is **not** a Lean kernel proof or an independent revalidation of the retained L'' stream. AMS access to Silverman's 1988 original was refused (403); we have not represented that original as newly read. The Tate identities are derived above and agree with the source code and normalization already in the project.

Replay:

```sh
cd /Users/bsm/BSD_CODEX6_FRONTIER_ATTACK_2026-09-19
python3 verify_regulator.py
python3 verify_regulator.py --precision 80 --terms 24
```

The source folders were not edited. The old reported radii are not retrospectively upgraded by this successor.
