# One connection between completed threads: exact localization at 11

2026-09-21. This is a finite-level deduction from retained arithmetic, with a small exact coordinate calculation. It does not prove a new primary vanishing result, FIN, ORDER9 or Q36. No novelty claim, Lean build, subagent, numerical L-function run, or literature survey is made.

## Inputs that really match

1. The completed [11-primary theorem](../../audits/P11_PRIMARY_THEOREM.md), with its retained qualifications, gives `Sha(E/Q)[11^infinity]=0`.
2. The retained saturated Mordell–Weil basis is `P1=(4547,327384)`, `P2=(5184,281520)`, and rational torsion has order two.
3. Aristotle-B's [corrected localization record](/Users/bsm/BSD_ARISTOTLE_INVENTION_PACKET_2026-09-20/review_2026-09-20/returned_archives/B_revision2/output-final_aristotle/ARISTOTLE_B_CORRECTIONS.md), §§0,2, gives `H^1(Q_l,E[11])=0` at every bad place and correctly retains the global localization kernel. Its written cohomological deduction is separate from the Lean-checked finite divisibility and linear algebra.

The newer [Aristotle-B status](/Users/bsm/BSD_ARISTOTLE_INVENTION_PACKET_2026-09-20/review_2026-09-20/returned_archives/B_revision2/output-final_aristotle/ARISTOTLE_B_STATUS.md) is local to that returned run and predates its import of C11. Its wording that 11 is unsettled does not override input 1. The corrections also withdraw the original auxiliary-class “first missing arrow,” because its dimension-inequality justification was invalid. That target is not revived here.

## Statement

Let `S={infinity,2,3,11,2243,4547,5843}`, and let `delta_11` be the usual global Kummer map. Use local Kummer conditions in `Sel_11(E/Q)`. Define the coordinate

\[
\lambda_{11}:E(\mathbf Q_{11})/11E(\mathbf Q_{11})\longrightarrow\mathbf F_{11},
\qquad
\lambda_{11}(Q)=14^{-1}\frac{t([14]Q)}{11}\pmod{11},
\quad t=-x/y.
\]

At the origin set `t(O)=0`. This is an isomorphism, and the exact calculation gives

\[
\lambda_{11}(P_1)=1,\qquad \lambda_{11}(P_2)=2.
\]

Consequently the retained arithmetic identifies

\[
\operatorname{Sel}_{11}(E/\mathbf Q)
=\mathbf F_{11}\delta_{11}(P_1)\oplus\mathbf F_{11}\delta_{11}(P_2),
\]

and localization to the product over `S` has the exact kernel

\[
\boxed{\ker\!\left(\operatorname{loc}_S\bigm|\operatorname{Sel}_{11}(E/\mathbf Q)\right)
=\mathbf F_{11}\delta_{11}(2P_1-P_2).}
\]

The kernel and localization image each have dimension one. This is a statement about mod-11 Selmer, not the kernel after tensoring with `Q_11`. Local divisibility by 11 does not mean the full 11-adic logarithm vanishes.

## Proof

The Kummer sequence and input 1 give

\[
E(\mathbf Q)/11E(\mathbf Q)\xrightarrow{\sim}\operatorname{Sel}_{11}(E/\mathbf Q).
\]

The saturated basis and prime-to-11 torsion therefore give the displayed two-dimensional basis.

The discriminant is nonzero modulo 11. An exact finite count gives `#E(F_11)=14`. Thus the reduction quotient has order prime to 11, `E(Q_11)[11]=0`, and multiplication by 14 sends every point into the formal subgroup `E_1(Q_11)`. The reduction exact sequence shows that inclusion of the formal subgroup induces an isomorphism, written in the inverse direction as

\[
E(\mathbf Q_{11})/11E(\mathbf Q_{11})
\simeq E_1(\mathbf Q_{11})/11E_1(\mathbf Q_{11}).
\]

The integral formal-group logarithm identifies `E_1(Q_11)` with `11 Z_11`, with `log(t)=t mod 11^2`. Hence multiplication by 11 has image corresponding to `11^2 Z_11`, and the displayed coordinate is well defined and bijective. Its factor `14^{-1}` makes it agree with `log_11(Q)/11 mod11` for the invariant differential of the displayed minimal model. Equivalently, additivity modulo `11^2` follows directly from the integral formal group law.

Exact rational elliptic-curve addition gives

\[
t([14]P_1)\equiv33\pmod{121},\qquad
t([14]P_2)\equiv66\pmod{121}.
\]

Because `14=3 mod11` and `3^{-1}=4 mod11`, these yield local coordinates 1 and 2. Therefore a Selmer vector `a delta_11(P1)+b delta_11(P2)` localizes at 11 to zero exactly when `a+2b=0`. This line is spanned by `(2,-1)`.

At every other finite place in `S`, the local cohomology group is zero by input 3. At the real place odd-primary degree-one cohomology vanishes. Thus the kernel at 11 equals the kernel over all of `S`, proving the assertion. Nontriviality follows from the global basis: `(2,-1)` is nonzero modulo 11. In particular, this rational-point class is nonzero globally although `2P1-P2` is divisible by 11 over `Q_11`.

## Reproduction and exact limits

`c11_localization_exact.py` uses only integer and rational arithmetic. It checks good reduction, the finite point count, every group-operation output, the two local coordinates, and the claimed kernel combination directly. Two addition schedules agree, but they use the same implementation and are not represented as independent implementations. The arithmetic output and code hash are saved in `C11_LOCALIZATION_EXACT.json`.

The result connects the completed C11 arithmetic to Aristotle-B's corrected finite-localization framework and the explicit Mordell–Weil basis. The previously unidentified kernel direction at this prime is entirely accounted for by known rational points. This does not upgrade the abstract local-intersection model into a model of the whole Selmer group without its kernel.

This is a standard consequence with an explicit seed calculation, not a new upper-bound method. It consumes the 11-primary theorem, so it cannot be used to prove that theorem again or to infer the same conclusion at an unsettled prime. It gives no uniform prime-support bound and no real-height comparison. Its value for later constructions is an exact compatibility test on any independently produced mod-11 class claimed to be strict; passing that test alone gives no nonvanishing, arithmetic realization, or BSD progress.

## Other proposed connections checked in the same operation

- The older family/actual-point/Gate-R/H41 assembly is a genuine completed chain, already retained in master §5.10; its rank-zero conclusions do not supply the current curve's rank-two derivative comparison.
- The fixed-prime Kummer equality does not repair H9's wrong character component. The [seed tower report](/Users/bsm/SEED_2243_12_MECHANISM_LANES_2026-09-18/L1C_SEALED_TOWER/00_REPORT.md), §3, already distinguishes a compatible target strict line from the absence/vanishing of the proposed descended output. No new H9 branch was launched.
- The [RS2 archive correction](/Users/bsm/BSD_FABLE_RS2_L3_2026-09-20/ARCHIVE_NOTE.md) retains an analytic pairing proportional to `L(f,2)L''(f,1)`, with its source-normalization qualification. Combining it with the Mellin identity connects two analytic expressions. No inspected arithmetic result supplies the missing real regulator factor. The archive's overbroad impossibility wording remains withdrawn; no arithmetic successor was independently identified here.

The global problem remains open. This operation demonstrates an actual matched conclusion/premise, while preserving the distinction between such a composition and a new route to the full BSD endpoints.
