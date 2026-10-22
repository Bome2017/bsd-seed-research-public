# Independent admission review: 1913b1 and 28042a1

Date: 2026-10-15. Grade: source-checked written deduction supported by independent exact verification in PARI/GP. This is not formal proof-assistant verification, and the number-field engine is shared with the producer.

**Verdict.** The complete Selmer dimension claim for 1913b1 is supported, using the retained successful class/unit certification. The three-class Selmer lower bound for 28042a1 is supported without using its unfinished class-group certification. The separate algebraic rank calculations give

- `Sha(1913b1)[3] = F_3^2`;
- `dim_F3 Sha(28042a1)[3] >= 2`.

These statements concern 3-torsion, not the whole 3-primary group. No seed endpoint is established.

## Independent computation

`audit1913/independent.gp` and `independent_28042.gp` import the saved explicit fields, actual elements, and proposed cube roots but **none of the producer libraries**. They recompute the number-field structure from its polynomial, the source cubic residues, scalar norms, local multiplicative quotient maps, and incidence norms. The latter use polynomial resultants, whereas the producer used relative norms and its second checker used multiplication matrices. The final accepted runs have empty stderr. No BNF certification was rerun.

For 1913b1 the independent results are:

- field `w^8+6*w^4+43*w^2-3`, signature `(2,3)`;
- five primes above S={3,1913}; nine residue-independent source directions;
- four actual independent global units and two independent surviving unit elements;
- two directly checked scalar-norm cubes and two directly checked affine-line norm cubes;
- local Kummer dimensions 1 at 3 and 0 at 1913, with minimum certified precision margin 86;
- **scalar-norm residue rows plus the full local conditions already have kernel dimension 2.** Saved finite additivity rows are unnecessary for this upper bound.

For 28042a1 the same verification gives thirteen independent displayed source directions, four independent actual units, and three independent admitted elements. The third is exactly the normalized tangent evaluation at P=(653,675). Three scalar-norm cubes and three affine-line norm cubes verify. Local image dimensions at (2,3,7,2003) are (1,1,0,1), with minimum margin 41. Scalar residue and local rows have kernel dimension 3 on this displayed source. This last number is not an unconditional upper bound on the entire Selmer group because completeness of that source remains uncertified.

An initial independent-checker run was rejected: reading the binary BNF before matching PARI's variable identifiers caused a field-variable mismatch, and some auxiliary rows had denominator/nonunit reductions. The accepted checker rebuilds `nfinit` from the explicit polynomial and excludes inadmissible residue rows before requiring full source rank. The failed first version is retained under `audit1913/rejected_first_audit/`; its completion marker is not accepted evidence. A comment-escaping typo in the adaptation to 28042a1 was also repaired before accepting the empty-stderr run.

## Why the local images are complete

The torsion field represents all eight nonzero 3-torsion points. Its degree-one completions at q count the rational nonzero 3-torsion points. The local decompositions freshly recomputed from the maximal order are:

| Curve | q | (ramification degree, residue degree) | #E(Q_q)[3] | dim E(Q_q)/3E(Q_q) |
|---|---:|---|---:|---:|
|1913b1|3|(2,1),(3,2)|1|1|
|1913b1|1913|(3,1),(3,1),(1,2)|1|0|
|28042a1|2|(1,1),(1,1),(3,2)|3|1|
|28042a1|3|(8,1)|1|1|
|28042a1|7|(3,2),(1,2)|1|0|
|28042a1|2003|(1,1),(1,1),(3,2)|3|1|

The dimension is the 3-torsion dimension plus one at q=3 and plus zero elsewhere (Schaefer–Stoll, printed pp.7,9–10). The exact rational sample approximations satisfy the simple-root Hensel inequality. Their certified root accuracy is sufficient for the tangent values to have the same local cube classes: at a prime above 3 the quotient modulus has depth `floor(3e/2)+1`; away from 3, depth one suffices. The freshly computed sample images attain the independently determined full dimension. At a zero-image place every local evaluation coordinate must vanish; a zero image is not omitted.

This makes the local tests sufficient, rather than an assumption that a random sample found the full image. The curve equation, its y-derivative, the exact Hensel bounds and the local quotient maps were recomputed. Both S sets include 3 and every bad prime. Outside S, unramified source classes meet the Kummer condition by Proposition 4.6; the real place contributes no odd-primary obstruction.

## Global admission and normalization

The source is Schaefer–Stoll, *How to do a p-descent on an elliptic curve*, long June 2001 version, [primary PDF](https://mathe2.uni-bayreuth.de/stoll/papers/p-descent-long.pdf), retained with its hash in `GLOBAL_ADMISSION.md`.

Corollary 7.9 and Proposition 7.10 identify the cohomology image with scalar compatibility and the **affine-line norm** condition. Section 10.1, steps 4–9, supplies the 3-descent algorithm. The eight affine lines are not the four linear subspaces through zero. The code uses the actual degree-eight affine-line algebra, the degree-three incidence algebra, and checks the embeddings of the generic torsion point exactly. The prescribed source and incidence polynomials satisfy the 3-division relation and the Weierstrass equation. Norm cube roots are explicit field elements, and their cubes are checked exactly. The source expressly permits direct cube tests without a unit/class calculation in the affine-line field (printed p.26).

The normalized tangent function is `y-y_T-slope*(x-x_T)`. Its divisor is 3[T]-3[O], and its Laurent leading coefficient at O is -1, which is a cube. Consequently evaluating this normalized function at a point agrees with the degree-zero divisor Kummer evaluation. No unknown scalar normalization is introduced. The rational short-model change is transported exactly and is not treated as an integral change at 3.

These checks prove genuine global and local membership for the displayed elements. Passing a finite set of split-prime additivity rows alone would not do so.

## Completeness and the rank deductions

For 1913b1, the retained `construct.out` reports `bnfcertify=1` for the saved BNF. Its class group is trivial and its roots of unity have order two. Dirichlet's theorem and the five S-primes give `dim A(S,3)=4+5=9`. The independent residue map has rank nine, and every displayed generator has valuation divisible by three outside S; hence it is a complete source. The two lower-bound classes and the independent two-dimensional necessary kernel give `dim Sel_3=2`.

The fresh `candidate_selection/rank0.gp` computes `ellrank=[0,0,0,[]]` and rational torsion C2. This is algebraic 2-descent, not an analytic-rank or Sha-label argument. Thus the rational Kummer quotient is zero, giving `Sha[3]=F_3^2`.

For 28042a1, `bnfcertify` did not finish. No complete class-group statement or complete source upper bound is promoted. The three independent explicit classes and their local/global admission remain valid without such completeness. The fresh `candidate_selection/rank1_28042.gp` computes `ellrank=[1,1,0,[[653,675]]]`, rational torsion C2, and verifies P on the curve. Since P has a nonzero 3-Kummer image, P generates the rational point group modulo 3. The other two independent classes therefore give `dim Sha[3]>=2`. No claim that the entire primary group has order nine follows.

Both rank bounds are reproducible software-assisted algebraic descents, not a second independent descent implementation. The analytic Sha data were used only to select the candidates. Full residual image is separately supplied by the recorded irreducibility and multiplicative-inertia checks; the actual degree-eight torsion-point field and local embedding counts are also verified directly.

## What the experiment establishes

These are positive unit-supported excess controls with good reduction at the coefficient prime and full residual image. In particular, trivial torsion-field class group and admissible unit repair do not force admitted units to be rational-point directions. The rank-one example retains a known nonzero rational point direction while two independent unit classes survive its removal. Neither example by itself proves or disproves a rank-two theorem with additional hypotheses, and neither supplies a bound for the original seed. Their purpose is to test that component of a proposed mechanism rather than assume it vanishes.
