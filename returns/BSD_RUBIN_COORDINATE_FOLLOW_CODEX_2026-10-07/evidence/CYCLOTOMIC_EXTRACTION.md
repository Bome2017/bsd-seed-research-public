# Connect the existing seed symbols to the cyclotomic residue

Grade: exact downstream formula and arithmetic replay, conditional on the retained symbol/period certificates. This does not evaluate a Hida weight derivative.

For ordinary p>=5, let alpha be the unit root of X^2-a_p X+p. Retain the supplied measure normalization

    mu(a+p^2 Z_p) = alpha^(-2) [a/p^2]^+ - alpha^(-3) [a/p]^+.

Write u(a)=log_p(<a>)/log_p(1+p) modulo p, represented by 0,...,p-1. Exactly,

    u(a) = ((a^(p-1) mod p^2)-1)/p * (p-1)^(-1) mod p.

For 0<=i<p, binom(u,i) modulo p depends only on u modulo p, so the coefficient ell_i is given modulo p by the finite level-p^2 sum. For fixed b mod p, the lifts a=b+pj have u(a) running bijectively over F_p. For example the first-order binomial expansion gives slope b^(-1), which is nonzero. Therefore

    sum_{a congruent b mod p} binom(u(a),i)
       = sum_{j=0}^{p-1} binom(j,i)
       = binom(p,i+1) = 0 modulo p       (0<=i<=p-2).

The lower-level symbol [a/p]^+ is constant on this fibre. Its entire correction term cancels, yielding

    ell_2 = a_p^(-2) sum_{a in (Z/p^2)^*}
                        [a/p^2]^+ binom(u(a),2) modulo p.

This is valid at all ordinary p>=5 in the stated measure normalization. It is not a nonvanishing assertion. At higher precision or degree p-1 the cancellation must not be assumed.

The reader checks the producer's recorded flags and rational candidates, keeps its original real-period convention, and rejects incomplete tables or p-divisible denominators. It does not inspect Arb balls independently or establish a canonical Hida period comparison.

The seed's retained m=5 and m=25 outputs give ell=(0,0,2,0) modulo 5, both through the full formula in Aristotle's weight2_jet.py and the high-level-only formula. The historical downstream certificate independently records ell_2=2. The old period comparisons involving c_E and 2 are units at 5. This validates the arithmetic connection in that convention, not the full W3 source normalization.

For an already certified future m=p^2 output, use:

    python3 checks/msl_cyclotomic_adapter.py --p P --ap AP --high PATH_TO_MSL_P_SQUARED

An optional --low table runs the full-measure comparison. This command consumes existing outputs only. It does not start Fourier evaluation or generate a coefficient corpus. The old p=5 outputs needed for replay are included under evidence/.
