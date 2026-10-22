# Derivative content gives a quantitative Sha bound

2026-10-07. **KATO_DERIVATIVE_CONTENT_BOUND_DERIVED_CONDITIONALLY.** Written deduction under the retained integral Kato, control, lattice and seed inputs. Independent review is required; this is not a formal certificate or a claim of literature novelty.

## The new conclusion

For the actual transported smoothed derivative

\[
\delta_p=A_p\kappa(P_1)+B_p\kappa(P_2)\ne0,
\]

put

\[
m_p=\min(v_p(A_p),v_p(B_p)),\qquad
w_p=\min_i v_p\!\left(\frac{\log_\omega(P_i)}p\right).
\]

On the retained domain

\[
D=\{p\ge5:p\nmid N,\ p\notin\{19,59,487\}\},
\]

the written argument gives

\[
\boxed{\operatorname{length}_{\mathbf Z_p}\Sha(E/\mathbf Q)[p^\infty]+w_p\le m_p.}
\]

The nonzero-derivative result first supplies primary finiteness. Alternating Cassels–Tate duality then makes the primary length even, so

\[
\boxed{m_p\le w_p+1\quad\Longrightarrow\quad\Sha(E/\mathbf Q)[p^\infty]=0.}
\]

In particular **content at most one suffices**. The previous primitive criterion required content zero. One extra common factor of p need not defeat this certificate. When the local point index is positive, the corrected threshold is larger still.

The actual class must satisfy the retained source hypotheses at p. If one fixed smoothing is chosen across primes, its finite support must also be excluded; D does not override those source conditions. The symbol w_p here is the local point index, not the older tame witness scalar.

This is a bound in terms of the existing derivative, not a construction of another receiver. Its proof uses neither a height determinant nor an ordinary filtration, so supersingular primes in D remain covered. No value or upper estimate for m_p has been obtained in this return.

## Why finite errors are included

For the actual free cohomology presentation, write its maximal-minor vector as

\[
\Delta(U)=d(U)\eta(U),\qquad y=g\eta,\qquad z=Ug\eta.
\]

Integral Kato divisibility at every height-one prime gives d dividing Ug. Nonzero augmentation forces d=Ud_1 with d_1 dividing g. Differentiating gives

\[
[U]\Delta=d_1(0)\eta(0).
\]

Smith reduction of the constant matrix over Z_p shows that the torsion order of its actual H² specialization divides every coordinate on the left. The p-content of eta(0) remains on the right. This is precisely where errors invisible to a characteristic ideal can contribute; they have not been dropped.

Global duality and the local Kummer map identify that torsion length as

\[
\operatorname{length}\Sha[p^\infty]+w_p.
\]

The full argument is in [CONTENT_BOUND_PROOF.md](CONTENT_BOUND_PROOF.md). The external duality statements and the separately retained arithmetic inputs are identified in [SOURCES.md](SOURCES.md).

## What the submitted review changes

Its cofactor and smoothing calculations are accepted with their stated conventions. At 17, exact matching gives

\[
(A_{17},B_{17})\equiv(K_{17}/17)(11,2)\pmod{17},\qquad m_{17}=v_{17}(K_{17})-1.
\]

The newly derived bound therefore allows **v17(K17)=1 or 2**. It no longer requires the first possible valuation exactly. This is conditional on the actual source and height matching at 17; an unspecified finite normalization support does not prove that matching. No digit of K17 was evaluated.

At 5 the proposed fixed smoothing has c divisible by 5. The old 5-adic calibration cannot be attached to that fixed source. This limitation is recorded rather than absorbed into a unit.

See [REVIEW_LEDGER.md](REVIEW_LEDGER.md) and [VALUATION_TARGET.md](VALUATION_TARGET.md) for the accepted review and the new correlated threshold.

## Effect on the BSD work

The missing uniform theorem is now sufficient in the weaker form

\[
\delta_p\ne0,\qquad m_p-w_p\le1\quad\text{outside one fixed finite set}.
\]

On a nonsingular ordinary matched-height domain, this becomes an upper bound allowing one extra valuation above the forced lower bound; its exact formula is in VALUATION_TARGET.md. It does not require the regulator or K_p separately to be units.

This return does not prove that estimate, compute a new primary certificate, or settle any exceptional prime. FIN, ORDER9 and Q36 remain unchanged. The concrete gain is a stronger quantitative use of the already matched arithmetic class, with a less restrictive sufficient vanishing test.

## Evidence and review limits

The exact control program checks 288 polynomial-matrix cases, including examples with finite specialization errors. It also checks the counterexample when the height-one condition at (p) is omitted, the review's multiplier (11,2), and the smoothing residues. These are formula controls, not seed Kato computations. The predecessor's three check outputs were replayed and compared byte-for-byte; its height and modular-symbol production engines were not rerun.

The source matching and residual-image inputs retain their previous grades. The new proof has been checked by its author only. The independent review target is the quantitative minor argument and its precise global-duality passage, not another reproof of the primitive criterion.
