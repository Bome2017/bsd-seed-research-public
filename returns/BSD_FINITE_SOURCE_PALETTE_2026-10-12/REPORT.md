# An explicit source family for the reviewed ordinary ratio certificate

Date: 2026-10-12.
Baseline lab commit: `581f7a26a1d110bcd6131739f94569e4810a719e`.

**Status: EXPLICIT_SOURCE_NORMALIZATION_DERIVED; FINITE_SMOOTHING_PALETTE_CONSTRUCTED; NO_NEW_RATIO_BOUND.**

The reviewed Bockstein certificate reduces ordinary-prime vanishing to relative divisibility of an actual Kato coefficient and a matched height determinant. I followed its numerator-side normalization further. For a newly specified primitive geometric source and a fixed set of three smoothing pairs, the remaining unspecified image-lattice index can be eliminated. This connects the actual-source coefficient to the standard ordinary modular-symbol leading coefficient on an explicit domain.

The result is a written deduction under retained arithmetic inputs, not a numerical evaluation, external certification, or a novelty claim.

## 1. The additional conclusion

Let L_2,p = [U^2]L_std,p for the standard ordinary measure with the fixed Neron real period and the predecessor's full interpolation convention. Let H_p be the matched BKS height matrix in the same U = gamma - 1 coordinate. On

\[
\mathcal D=\{p\ge5:p\nmid N,\ p\notin\{19,59,487\}\},
\]

restricted to ordinary primes, the constructed source satisfies

\[
\boxed{v_p(K_p)=v_p(L_{2,p}).}
\]

Thus the reviewed sufficient test can be applied as

\[
\boxed{L_{2,p}\ne0,\quad\det H_p\ne0,\quad
v_p(L_{2,p})-v_p(\det H_p)\le1
\Longrightarrow\Sha(E/\mathbf Q)[p^\infty]=0.}
\]

There is no unspecified extra normalization-prime set for this family. The other source, height and cohomological hypotheses remain. An arbitrary earlier Kato packet or numerical height does not acquire authentication from this statement.

[Full construction and proof](PROOF.md) · [Sources and retained inputs](SOURCES.md) · [Review qualifications](REVIEW_NOTES.md).

## 2. How the unknown lattice index is removed

Use the optimal elliptic quotient of J_1(N), followed by a least-degree rational isogeny to the seed. Residual irreducibility of E[p] forces that isogeny to be prime to every p >= 5: apply irreducibility to its dual kernel; a p-divisible degree would allow factoring out [p], contradicting minimality. Therefore the proper-curve cohomology image is exactly T_pE.

The open modular curve could, a priori, enlarge that lattice. The enlargement is a finite quotient of the cusp permutation module, so it has abelian Galois action, since all X_1(N) cusps are cyclotomic. It also embeds in E[p^infinity]. Full residual image rules out any nonzero abelian-action submodule there. Hence the enlargement is zero.

The retained [1/5]^+ = 144 symbol, together with the good-prime Manin comparison, makes its plus image primitive for this map. This proves a period unit without enumerating a huge modular-symbol lattice. The original symbol receipt and global residual theorem were not recomputed here.

## 3. Replace one smoothing pair by a finite fixed palette

Put M = 6N and c_i = 1 + iM for i = 1,2,3. Use the three pairs (c_1,c_2), (c_1,c_3), (c_2,c_3), selecting the first admissible pair at p. At every good p >= 5, at most one c_i is divisible by p and none of c_i - 1 is divisible by p. The selected actual source therefore has unit smoothing augmentation.

This uses three fixed pairs, not a new unbounded source search. It does not divide a class by its intrinsic p-content. For example, the old first pair is inadmissible at p = 5, while (c_2,c_3) is admissible. That is a source repair, not a new Sha[5] result.

The remaining bad-Euler augmentation is

\[
\frac{2^5\cdot19\cdot59\cdot487}{2243\cdot5843},
\]

which accounts for the named exclusions in D. Composing these unit comparisons with the retained interpolation identity proves the displayed equality of valuations.

## 4. What remains missing

For this source family the actual relative-divisibility identity is still

\[
 v_p(L_{2,p})-v_p(\det H_p)
 =\operatorname{length}\Sha[p^\infty]+e_p,\qquad e_p\ge0.
\]

No value of L_2,p, no new height determinant, and no upper bound on this expression was obtained. The palette removes artificial source exceptions; it cannot remove the intrinsic Kato defect. Its integer gcd is not a Sha annihilator and supplies no global finite-prime-support theorem.

This is a normalization advance, not an advance in established seed-prime coverage. FIN, ORDER9, Q36, supersingular coverage and exceptional-primary obligations are unchanged.

## 5. Checks and publication boundary

The [exact checker](checks/verify_palette.py) and [results](checks/RESULTS.json) include 1,132 residual coverage controls, 100 gcd controls, 364 small residual-vector controls, malformed-input and bad-modulus cases, and 17 independently cross-checked small-field seed point counts. None is a Kato or modular-symbol coefficient calculation. The global statements are proved in the written argument, not inferred from the finite tests.

The new construction has author-level written review only: no independent human, formal, or separate-agent verification. Earlier records are references, not silently re-certified inputs. The return is additive, intended for an isolated lab research branch; it does not change the expert-review repository or merge main.

The local complete ZIP is named `BSD_FINITE_SOURCE_PALETTE_2026-10-12.zip`. The package's manifest covers its source and result files; hashes certify custody rather than mathematical correctness.
