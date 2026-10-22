# Order-three tuning: arithmetic normalization and the surviving excess

2026-10-06. **ORDER3_EXCESS_IDENTIFIED_CONDITIONALLY; NO_BSD_BOUND.**

The user's assessment of commit `423fdd10` is consistent with this recheck:
the finite lifting checkpoint is distinct from a bound on the original
Selmer group. The original status remains
**MIXED_CHAR_ORDER3_W_LIFT_DERIVED_CONDITIONALLY**. This is a same-author
recheck, not the independent review still required for full-S Stage A and
the arithmetic tuning proof.

## Result of this pass

1. [The conductor audit](CONDUCTOR_NORMALIZATION.md) spells out one local
   Tate normalization that works simultaneously for every residual and
   lifted pairing entry. It reconstructs the cochain formula and the two
   marked Chebotarev primes. No blocking discrepancy was found under the
   retained inputs. No new numerical conductor or seed character was computed.
2. [The excess calculation](EXCESS_NORMAL_FORM.md) locates exactly what
   survives after tuning. Put `A3=F_p[t]/t^3`, let `C=Sel(M3(lambda))`, and
   suppose `rad(b_lambda)=W` and both rational-point classes lift. Then

   `C ~= A3^2 direct-sum F_p^(dim S - 2)`

   noncanonically, and canonically

   `C[t] / t^2 C ~= S/W ~= Sha(E/Q)[p]`.

   The analogous statement uses pi in the actual mixed-characteristic
   representation modulo pi^3. This deduction only assumes a character
   with the asserted lifting properties; it does not require the existence
   proof to have passed independent review.

The two length-three summands record the lifted points. All the original
excess remains in the length-one part. Removing first- and second-order
obstructions to the points has not removed that excess.

## Consequence for continuing toward BSD

A fourth-order lift is not admitted here as a new FIN task. This calculation
shows why it would need a separate arithmetic payoff: lifting the two point
directions does not control the additional length-one directions. Nor does
torsion-freeness of integral H^1 imply freeness after reduction; a written
cohomology countercontrol in the proof exhibits the missing base-change term.

An independent theorem controlling that term could still use this mechanism.
None is constructed in this return. Merely renaming it a flatness,
saturation, length, or annihilator problem would not be new input.
This is not a nonexistence theorem for further arithmetic work.

The all-order Kato gate remains as recorded. The present calculation gives
no all-order lift, no twisted L-zero, and no comparison with a Mazur--Tate
coefficient. It does not establish that every possible continuation equals
G1. The superseded rank-two submission remains superseded.

**FIN, ORDER9 and Q36 are unchanged.** This return is proof clarification
and exact accounting of the excess, not progress through the uniform bound.
No new cloud job, fixed-prime campaign, or research-repository promotion.

See [HANDOFF.md](HANDOFF.md) for the remaining independent-review questions.
The small [matrix controls](checks/RESULTS.json) are abstract checks, not seed
Selmer computations. Publication and manifest verification are custody only.
