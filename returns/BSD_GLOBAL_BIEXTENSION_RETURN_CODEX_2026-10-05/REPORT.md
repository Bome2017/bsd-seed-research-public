# Global biextension scalar attack — construction return

**NO_GLOBAL_SCALAR_CONSTRUCTED** · 2026-10-05

I carried out the proposed construction through the actual seed fibers and its saved modular symbols. The Neron side can be repaired and written explicitly. I did not construct the modular section or a rational scalar controlling the primes. This return therefore establishes no new BSD obligation for the seed.

## What was constructed and checked

The [proof](PROOF.md#2-explicit-rational-poincare-fibers-before-p-is-chosen) writes four rational Poincare fiber sections at \(Q_i=16P_i\), with their finite-place normalization

\[
r^0_{ij}=\frac{d(Q_i)d(Q_j)}{d(Q_i+Q_j)}r_{ij}.
\]

Their exact rational coordinate data are included. A separate PARI calculation agrees with the rational group-law implementation. The use of the Neron cubical extension at bad places remains a named retained G2 input.

The naive tensor expression \(\mathcal P_{11}\mathcal P_{22}/(\mathcal P_{12}\mathcal P_{21})\) realizes a sum and difference of heights, not their determinant. The repair is an explicitly constructed primitive quadratic map

\[
(\wedge^2L)^{\otimes2}\hookrightarrow\operatorname{Sym}^2(\operatorname{Sym}^2L),
\quad (P_1\wedge P_2)^{\otimes2}\mapsto (P_1^2)(P_2^2)-(P_1P_2)^2.
\]

It gives the required regulator with the retained production factor \(4\cdot16^4\). **This carrier already appears in the September 18/19 LINE record.** Its explicit reconstruction here is not a newly discovered cross-prime input.

## The ratio argument needs more than a common rational line

For the actual Poincare splitting, multiplication of a section by \(c\in\mathbf Q^\times\) adds its tame character. It does not multiply the tame height by \(c\bmod p\). Globally, a rational change of lift disappears in the idele-class quotient. These are the local and global definitions in [Tan, Definitions 2.2 and 2.6](https://aif.centre-mersenne.org/item/10.5802/aif.1457.pdf).

Thus the packet's scalar inference is valid only after constructing a **reduction-linear map on a fixed integral determinant lattice**. The repaired line provides such a regulator map. It does not put the Mazur–Tate class in its image.

## Actual seed calculation and the attempted modular lift

At the already settled p=17, ell=103, the replayed pairing matrix on the fixed Q_i is

\[
\begin{pmatrix}15&10\\10&6\end{pmatrix}.
\]

The naive tensor expression gives 1; the determinant gives 7. The production regulator is 6. Recombining all 102 stored plus symbols gives \(C_2=7\), hence \(w_{17}=16=288\bmod17\). This is a normalization check using existing certified input, not a new primary certificate or a new run of the large analytic pipeline.

I attempted the modular lift in two ways. Rationalizing its finite augmentation quotient kills the positive-degree class: over Q the augmentation ideal is idempotent. Keeping the integral classes at all primes and applying W gives separate residual sections \(w_p\omega\); no theorem in these operations puts that family in the reductions of one nonzero rational section.

I also checked the retained U22/BKS inputs at this exact comparison. The corrected U22 review does not provide a map from the boundary coefficient to these fibers. BKS's algebraic leading-term comparison imports conjectural input, and the newer [Bullach–Honnor manuscript, Remark 1.8(b)](https://dominikbullach.github.io/MazurTate.pdf) expressly leaves the finer positive-rank regulator comparison separate. None supplies the missing section unconditionally here. This is not a proof that every possible future geometric construction requires BSD or TNC.

## Endpoint and disposition

A nonzero rational section with the stated integral realizations would indeed give cofinite primary vanishing through G2 and Ota, with ordinary and supersingular coverage on their retained domain. That payoff survives. The section itself is not constructed in this return.

Do not promote this return to `GLOBAL_BIEXTENSION_PARTIAL` on the strength of the old squared determinant line. Do not use raw torsor scalar multiplication as the missing modular comparison. No further fixed-prime or automatic continuation campaign is justified by this output.

**FIN, ORDER9 and Q36 remain open.** New derivations are same-worker checked and require independent review. The attached checks verify rational arithmetic, normalization and algebra, not global scalar existence or novelty.

[Full proof](PROOF.md) · [Attempt ledger](ATTEMPT_LEDGER.md) · [Handoff](HANDOFF.md) · [Sources and retained grades](SOURCES.md) · [Check instructions](checks/README.md)
