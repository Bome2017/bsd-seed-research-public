# Independent-control attempt using the OpenAI determinant argument

Date: 2026-10-11. Status: **NO_NEW_UPPER_CONTROL_FROM_TESTED_SUBSTITUTIONS**.

This is a bounded attempt to apply the actual horizontal-divisor argument, not another screen of the low-rank theorem's headline. No seed coefficient was computed. The result is not an impossibility claim about a rank-two extension of the paper. The source is pinned to `openai/math@fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb`.

## 1. The arithmetic interface I tried to use

In `exact_08-extraction.tex`, Proposition `extraction:theta-implication`, a horizontal zero of the undepleted analytic theta series gives a nonzero one-sided strict/full Selmer group for the curve or a companion. In `exact_09-unit.tex`, the proof proceeds through three actual interfaces:

1. `unit:quotient-regularity`: an irreducible divisor of the integral analytic/determinant quotient forces an analytic zero, and hence a Selmer jump.
2. `unit:simultaneous-jumps`: extra tame directions make simultaneous jumps have codimension at least two. The tangent algebra itself permits arbitrary dimensions; it is not a dimension-one lemma.
3. `unit:unit-comparison`: the two conjugate quotient ideals agree. A divisor would therefore force forbidden simultaneous jumps, so the quotient is a unit.

This is stronger than integrality alone. It is a concrete potential tool for an analytic/determinant comparison. It does not say the determinant itself is a unit, nor that its central value has bounded valuation.

## 2. First substitution: remove the known point plane

Let `C_0` be the actual integral specialization of the seed's full S-cohomology complex. Retain a finite-free model in degrees 1 and 2 and the saturated Kummer plane `W = Z_p P_1 + Z_p P_2` in `H^1(C_0)`.

**DERIVED, elementary construction.** Choose cocycles representing the two points and form

`C_red = Cone(W[-1] -> C_0)`.

Then

`H^1(C_red) = H^1(C_0)/W`, and `H^2(C_red) = H^2(C_0)`.

The point map is injective on cohomology. Because `W` is saturated in the kernel of the degree-one differential, and that kernel is saturated in the free degree-one term, the chosen `W` is a direct summand over `Z_p`. Its two contractible cone blocks can be cancelled integrally. Thus this is an actual perfect central quotient, with the degree-two terms retained, not a quotient of dimensions alone.

This construction does **not** make `H^1(C_red)` zero. It removes the two known points and nothing in degree two. In the already-established branch `delta_p != 0`, retained weak-order control gives `H^1(C_0)=W`, so the reduced complex is injective in degree one, but its degree-two cokernel still has the free line and torsion from the content theorem. No use of this branch proves the missing nonvanishing of `delta_p`.

There is also no automatic family version of the displayed point map. A map from a free rank-two family module would require compatible deformations of the point cocycles through all orders. A central direct summand is not such a map. The historical order-three result only lengthens the two known strings to that order and leaves all excess directions visible. I did not use it to assert all-order liftability.

**First failed arithmetic step:** Proposition `extraction:theta-implication` concerns the paper's actual scalar-twisted strict/full complex and its theta series. It supplies no theta-to-jump statement for `C_red`, and no analytic determinant section of this reduced object. Replacing the source complex by `C_red` without constructing a new analytic comparison would change the theorem's object.

## 3. Second substitution: use a noncentral acyclic character instead

I then tried to avoid the unavailable family lift of `W`. In `exact_04-vertical.tex`, lemma `vertical:parity`, generic acyclicity is established from a rank-one central point and nonzero localization. This particular proof can be replaced by a different acyclic fiber, if one can actually supply it:

**DERIVED, limited algebraic replacement.** For the same finite free square model, if one arithmetic specialization has invertible differential over its coefficient field, the universal determinant is nonzero. Generic acyclicity follows. A perfect alternating model then has even residual nullity on the specified tests exactly as in the source proof. The acyclic fiber need not be the seed's central character.

This avoids falsely asserting that the seed's central strict/full complex is acyclic. It does not construct the required arithmetic specialization, prove its local conditions, or transfer central integral information from it. Generic Heegner nonvanishing is relevant to finding such fibers; I inspected Cornut's primary theorem, which concerns a non-torsion trace in the anticyclotomic tower, not a uniform unit statement for the seed's central divided Kato class. The ordinary qualifications on quoted Selmer consequences also cannot be silently extended to the supersingular domain.

Even granting this replacement and all the remaining hypotheses needed to run Section 9, its output is an analytic/determinant **unit comparison**, not an upper bound on either central factor. Section 10 of the source then uses a separate, rank-one geometric evaluation: the Heegner trace is non-torsion, generates a finite-index subgroup of a rank-one Mordell–Weil group, and its logarithmic central value is evaluated before the exact determinant volume is compared. That central evaluation has no rank-two substitute in the supplied source.

Thus the noncentral-fiber repair does not by itself improve the seed's `m_p-w_p` estimate. It removes one possible proof prerequisite only; it does not remove the missing rank-two central arithmetic comparison.

## 4. Exact alternating control for the second substitution

This is a formal algebra control, not a curve or a counterexample to any source theorem.

Let `A = Z_p[[t,u]]`, choose any integer `a >= 1`, and set

`F=t+u+p^a`,

`D = [[0,F],[-F,0]]`, `L=det(D)=F^2`, `B=F^2`.

Then:

- the model is alternating and generically acyclic;
- `L mod(p,t) = u^2 != 0`, so the high-character regularity hypothesis is satisfied;
- neither `L` nor `B` has the vertical divisor `(p)`;
- `B/L=1` is already an integral unit; equality of conjugate quotient ideals and exclusion of all quotient divisors are automatic;
- after `t=u=0`, the cokernel is `(Z_p/p^a)^2`, of length `2a`.

Consequently, even **successful** removal of every divisor of the analytic/determinant quotient does not bound central finite torsion. The analytic factor has precisely the same unrestricted central content as the determinant. The even length is compatible with an alternating pairing. This is why a central arithmetic evaluation is necessary after the horizontal-divisor argument, rather than a technical normalization that can be omitted.

This control is different from dropping finite errors: the finite cokernel is kept in the actual matrix. It does not invalidate Section 9. It identifies exactly what Section 9 proves and why Section 10 adds a separate arithmetic input.

## 5. Consequence for the seed attempt

The specific extension worth retaining is the conditional noncentral-acyclic-fiber replacement in Section 3. It is a possible repair to one prerequisite if a future rank-two analytic comparison needs it. It should not be advertised as a BSD bound or commissioned as another independent long run.

For the present source, the shortest substantive task remains construction of the **rank-two central arithmetic evaluation**, with actual geometric source and integral realization. A further quotient argument or another proof of generic acyclicity would not supply the estimate

`delta_p != 0` and `m_p-w_p <= 1`

cofinitely. Nor has this attempt proved that only a fixed scalar could supply that estimate.

The existing October 6 `GATE4_CHECK.md` and rank-two-anchor task already located the missing global comparison. This attempt does not rebrand that target as a new discovery. It checks two precise substitutions against the October 7 source revision and stops them at their actual missing arithmetic maps.

### Additional arithmetic source found during this test

Cornut's Theorem B (printed p.22, with the elliptic optimal-quotient case on p.4) is stronger than rational nonvanishing: for a fixed ring-class tower at a prime `l`, the relevant CM-point span modulo a coefficient prime `q` is infinite-dimensional outside the fixed divisors of `phi(N d_K) eta`. Here `eta` counts the geometric components of the parametrization kernel. This is a real source of cofinite coefficient-prime nondivisibility, with its Heegner hypotheses retained. It does not bound the augmentation depth needed to see it or identify the seed's divided Kato class.

**Derived scope check.** Freezing `l` and taking `q != l` cannot itself give a quadratic augmentation witness from the finite `l`-power deck groups. In `F_q[G]`, for `G` of `l`-power order, the averaging idempotent `e=|G|^{-1} sum_g g` exists. The augmentation ideal is `(1-e)F_q[G]`, hence `I^2=I` and `I^2/I^3=0`. Nonzero CM classes can still exist in nontrivial character summands. Taking `l=q` avoids this particular check but restores the varying coefficient-prime tower and still supplies no depth-two bound. This rejects only that proposed fixed-tower augmentation extraction, not other geometric maps from Cornut's source.

## Sources and scope

- `sources/direct/exact_03-models.tex`: determinant convention, line/square switches, strict-finite volume, and rank-one Kummer-volume statement.
- `sources/direct/exact_04-vertical.tex`: `vertical:parity` and its central acyclicity proof.
- `sources/direct/exact_06-pair.tex`: actual analytic measure and strict determinant, including integral primitive construction.
- `sources/direct/exact_08-extraction.tex`: `extraction:theta-implication` and its primitive strict/full local conditions.
- `sources/direct/exact_09-unit.tex`: quotient regularity, association, augmented alternating matrices, simultaneous jumps, integral unit comparison.
- `sources/direct/exact_10-center.tex`: the independent rank-one central logarithmic/point-index evaluation.
- Cornut, *Mazur's conjecture on higher Heegner points*, primary published PDF: https://webusers.imj-prg.fr/~christophe.cornut/papers/mcinv_published.pdf . Used to delimit the possible noncentral input, not imported as a theorem proving seed primitivity or whole-domain strict acyclicity.
- Historical collision checks: `lab/work/returns/BSD_OPENAI_RELEASE_SCREEN_CLAUDE_2026-10-06/GATE4_CHECK.md` and `lab/work/returns/BSD_ARISTOTLE_RANK2_ANCHOR_SUBMISSION_2026-10-06/DELTA_TASK_RANK2_ANCHOR.md`. Their old source claims were not recertified.

All local source paths above are relative to `/Users/bsm/BSD_OPENAI_MATH_SCREEN_CODEX_2026-10-11/`. This note is a written comparison, not a formalization or an independent review of the source papers. No remote job, paid computation, or publication was made by this subtask.

**FIN, ORDER9 and Q36 remain unchanged.**
