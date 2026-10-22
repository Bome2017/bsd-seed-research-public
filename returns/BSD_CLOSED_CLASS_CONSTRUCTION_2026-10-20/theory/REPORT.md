# Actual complete class contribution: a coarse independent bound

**Result:** for the actual seed's degree-24 coefficient-five point field A
and degree-12 scalar quotient K,

    |ker(Cl(A)->Cl(K))| <= 262*10^66 < 5^98.

The sum of the two faithful five-class dimensions is therefore at most
97; each separately is at most 97. This includes classes absent from
every collected relation list. It is independent of GRH and elliptic
Sha/BSD inputs, under the retained exact identification of the fields,
signatures, and discriminants.

The construction combines an elementary discriminant lower bound for
every nontrivial relative norm-one unit, Minkowski's theorem for the
full rank-six unit lattice, the explicit power-of-two norm-unit index,
the analytic class-number formula, and Louboutin's unconditional
ray-class L-value upper bound. It computes neither class group nor
regulator. The exact integer/rational certificate replays identically.

This changes the logical status of the class budget: it supplies a
finite ceiling for the whole contribution without assuming selected
generators are complete. It does not make that ceiling sufficiently
small. Adding the three-dimensional unit sector gives a coarse complete
source ceiling 100 before retained norm/local conditions (and using the
retained zero valuation contribution). That is far above the desired
rank-two ceiling. It yields no new primary vanishing, FIN, ORDER9, or Q36.

SCALING.md derives the symbolic odd-prime form, retaining the actual
discriminants, relative unit rank (p^2-1)/4, and a positive-logarithm
gate. It establishes no useful uniform bound. The naive CM-minus
special-value shortcut was also checked: it does not apply to these
signatures, whose relative zeta quotient has zero order six at s=0.

Files:

- COMPLETE_CLASS_BOUND.md: full proof and normalization bookkeeping.
- SCALING.md: precise symbolic extension and remaining growth terms.
- certify_analytic_bound.py / EXACT_BOUND.json: exact outward arithmetic.
- FIELD_INPUTS.json / INPUT_BINDINGS.json: retained arithmetic bindings.
- SOURCES.md: fresh primary source scope and inherited hypotheses.
- ANALYTIC_DIAGNOSTIC.json: earlier approximate diagnostic, not acceptance.

No old pseudo-relations were relabelled as complete; no hidden generator
deficiency was set to zero; no paid job, remote computation, publication,
or full number-field BNF computation was performed in this lane.
