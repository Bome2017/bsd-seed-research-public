# Mock-plectic and rank-two Kolyvagin audit

2026-10-15. Read-only audit of the two named Claude returns. Written assessment, not a formal proof or independent reconstruction of the original Brandt, modular-symbol, or p-adic computations. No original files changed, no heavy job or publication.

## Decision

The mock-plectic experiment supplies reproducible **saved-output evidence for a mixed determinant's vanishing pattern**, with a field-dependent scalar. It does not supply a common rational scalar, an actual global rank-two class with a computed index, or an independent seed bound. The Kolyvagin folder contains only a report; it adds no arithmetic computation or proof of its missing premise.

The best bounded next experiment is a missing discriminating cell: a source-admissible control with `p | K_E`, nonzero mixed determinant modulo p, and unit twist factor. A nonzero proxy there would refute the naive `K_E`-divisibility explanation, independently of the unknown eigenfunction unit. This is preferable to another collection of unit-scalar examples. A separately useful, more expensive task is to compute one genuinely normalized local modular-parametrization value.

## What was independently checked

`audit_saved.py` uses standard-library exact integer/Fraction arithmetic. Its `audit_results.json` records inputs with hashes.

* All 79 submitted manifest entries match. Both recorded prediction hashes match. A hash matches contents; it does not establish when the prediction was sealed relative to computation.
* The two p-adic logs contain 44 distinct completed `(curve,p)` rows on eight curves. Their printed ratios are `1+O(p^k)`, with k between 3 and 5. The first run overflowed, and the second resumes the remaining cases; the completed rows are not duplicate experiments. I did not rerun the engines or recheck their numerical error bounds.
* There are **10**, not 11, completed proxy rows and 20 field computations. `STATE.json`'s 11/11 is a counting error. Every saved trivial-character sum is zero. The 10 zero/nonzero patterns match the recorded determinant calculations.
* Independent modular arithmetic reproduces the cross-field tallies: constant ratio 7/9, real-period twist ratio 8/9, Gross-period ratio 9/9. The nine pairs are overlapping comparisons of 20 fields, not nine independent experiments.
* The twist inputs `r,s` were produced by `bestappr` on floating `lfun`/period values. Replaying their residue arithmetic does not certify those recognized rationals as exact L-values.

The report's phrases “exact p-adic class” and “exactly the BSD multiple ... everywhere” are too strong. The outputs establish finite-precision numerical agreement on the chosen controls. They neither identify an exact infinite-precision equality nor construct a class in an exterior square. PARI documents `ellpadicbsd` as a numerical p-adic BSD quantity to compare with `ellpadicregulator`, not a proof of the conjectural formula. [PARI manual](https://pari.math.u-bordeaux.fr/dochtml/html-stable/Elliptic_curves.html#ellpadicbsd)

## What the unknown unit permits and prevents

The implemented comparison has the shape

`D(E,p,ell,K) = u(E,p,ell) * c(E,p,K) * det(E,p,ell) mod p`,

after the stated field-coordinate conventions. Scaling the level-raised eigenfunction changes `u`. For an individual nonzero row, **every** nonzero proposed scalar is compatible after changing this unit; the checker explicitly verifies that fact. Cross-field ratios at fixed `(E,p,ell)` cancel `u` and genuinely distinguish some field-factor hypotheses. Ratios at different auxiliary primes do not cancel it. Ratios at different coefficient primes do not even lie in the same residue field.

Consequently the two-prime result on 1001c1 says that the tested scalar is a unit at both 7 and 13. It does not identify one rational scalar. The auxiliary-field lists at these two primes also differ. The report's field-independent “E-part” is a proposed interpretation of the nine ratios; it is not a computed object independent of p and ell.

Fornea–Gehrmann's equation (25) fixes the eigenfunction by an actual local Kummer map. Their Theorem 3.16 compares the normalized theta element and localization of the Heegner class; arbitrary eigenvectors only retain a unit ambiguity. Their conjectural exterior-square placement supplies no BSD constant. The theorem uses multiplicative reduction at the coefficient prime, so for one fixed curve it is not an all-good-prime construction. [FG, §§2.3 and 3.4.5](https://arxiv.org/html/2311.03100v2)

The fast implementation imposes some Hecke conditions on sampled rows and uses additional fresh-row tests. A one-dimensional intersection can identify the desired line **if** the full desired eigensystem is independently known to exist in that exact module: every selected constraint then contains it. The saved outputs alone do not re-establish all that theorem matching. They should remain implementation evidence under the retained source hypotheses.

## Kolyvagin report: corrections that matter

1. “The bound is not a separate missing theorem” is a conditional architectural observation, not a theorem produced here. A fixed nonzero source, bounded integral index, correct local conditions, and the actual comparison to the per-prime source would indeed imply finite support. Merely positing a global class gives none of those comparisons.
2. “The index of the bottom class equals the dual Selmer length” omits a primitivity qualification. Burns–Sakamoto–Sano Theorem 5.2 gives ideal inclusion for an arbitrary system; the stated equality requires a **basis** of the system module, with additional coefficient-ring hypotheses for higher ideals. No rank-two system with those properties is supplied for the seed. Core rank in that theorem is not automatically the seed's Mordell–Weil rank. [BSS, Theorem 5.2](https://arxiv.org/pdf/1805.08448)
3. Kim's Question 4.6 is a **fixed-p** placement problem for derived Heegner points as k and the conductor vary. It does not assert that solving it is equivalent to constructing a p-independent object. Theorem 4.7's finite local test depends on the global subgroup and a Mordell–Weil basis over ring-class fields; Question 4.8 asks how to avoid that computation. Replacing its subgroup by the entire finite-field point group loses the needed restriction. Its supersingular theorem assumes semistability; the seed's additive reduction at 2 prevents a direct seed import. [Kim, Theorem 1.1 and §§4.2.4–4.3](https://arxiv.org/html/2609.15328v1)
4. Banwait's height discussion concerns a specified product-formula approach for CM curves, not an impossibility theorem for all p-dependent estimates. A fixed algebraic number is one sufficient mechanism. It is not the only logically permissible route. The paper itself discusses complementary criteria and leaves the fixed-number question open. [Banwait, §13](https://arxiv.org/html/2609.08431v1)
5. The 2015 Dasgupta–Spieß note supports an augmentation-order theorem, not the desired elliptic leading-term identity. Calling the entire higher-rank multiplicative analogue “still open” requires a current theorem-by-theorem survey; this report did not provide one. Its suggested GL1-to-GL2 transfer remains an unexecuted source-comparison task. [Dasgupta–Spieß, 2015 note](https://sites.math.duke.edu/~dasgupta/papers/Glennfest.pdf)

These corrections do not kill higher-rank Euler systems, the mock-plectic construction, or a correlated valuation bound. They prevent results with different hypotheses and outputs from being treated as the missing seed arithmetic.

## Next bounded discriminator

The current proxy panel mostly tests the easy cell `p does not divide K_E`. The sole reported `p | K_E` setup, 3565a1 at 5, also has zero point-log row, so its determinant is zero: it cannot distinguish a unit scalar from a divisible scalar modulo 5.

For a new control, freeze these alternatives before producing its Gross sum:

* H_div: after explicitly recorded local and field factors, the scalar has positive p-valuation because the proposed `K_E` factor does.
* H_unit: the scalar is a unit despite `p | K_E`.

Require nonzero determinant and a unit Gross twist factor. Then H_div predicts zero and H_unit predicts nonzero. An unknown **unit** multiplying the eigenfunction cannot change that decision. An odd valuation in `K_E` also means a proposed literal `c^2=unit*K_E` cannot hold with `c in Q_p` unless another factor contributes; this must be accounted for before prediction.

Prefer `N^- = 1`, so every prime dividing `N/p` splits in K. Check nonsplit multiplicative p, full residual image, `p>=5`, `p` inert in K, discriminant coprime to N, `p` not dividing h_K or `ord_p(q)`, and auxiliary-prime admissibility. Tamagawa divisibility at a split prime of `N^+` is not excluded by the cited FG assumptions. When `N^-` is nontrivial its residual ramification conditions must be checked separately.

A result here would select or refute a scalar explanation. It would not yet prove a seed inequality. To move from a surviving explanation to the seed, one still needs a genuine source comparison and control of its content, without inserting a known Sha value as the predictor.

FIN, ORDER9 and Q36 are unchanged.
