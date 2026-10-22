# Two wording corrections to the accepted derived-height correction

Date 2026-09-21. **Additive.** Corrects phrasing in `DERIVED_HEIGHT_CORRECTION_ACCEPTED.md` §1 and §3.
Those files are preserved unedited; where they conflict with this one, this governs.
Authority: `~/BSD_CODEX6_MASTER_HANDOFF_2026-09-19/_work/bridge_repair_assessment_2026-09-21/MCS_DERIVED_HEIGHT_GATE.md`.
No mathematics changes; both corrections are about attributing cause and grade correctly.

## W1. The division did not destroy a signal

I wrote that dividing by `t^e` "removes precisely the part that the derived Bocksteins could have seen" and "strips out
precisely the part the derived Bocksteins could have seen". That wording implies a detectable Bockstein signal existed
and was destroyed by the operation. **It does not, and it was not.**

Correct statement: `v_∞` lifts through the entire tower, and *that property alone* makes every derived Bockstein vanish
on its specialization. The vanishing is an intrinsic property of `v_∞`, not a consequence of how it was obtained. There
was no signal to remove. `h_j(v̄, w) = 0` would hold for any class that lifts, however produced.

The practical difference: my phrasing invites the repair "divide differently, or by less", which is vacuous. The correct
phrasing closes that door — no choice of divisor produces a lifting class with nonzero derived Bockstein.

## W2. `ord_{s=1} L(E^χ, s) = 1` is one statement, not a statement plus a hypothesis

I wrote that what is needed is "a rigorously certified rank-one twist — certified nonvanishing of `L'(E^K,1)` **plus**
the Kolyvagin hypotheses", and said my earlier formulation "understated the obligation". That framing is wrong in a
specific way: it treats certified derivative nonvanishing as an **additional mathematical hypothesis** alongside
`ord L(E^χ, s) = 1`.

Correct statement: **`ord_{s=1} L(E^χ, s) = 1`, once proved, already supplies analytic rank one**, which is what
Gross-Zagier and Kolyvagin consume. Certified nonvanishing of the derivative is *how that statement gets proved* for a
specific `χ` — an evidence-grade obligation, not a second condition. The distinction to maintain is between

* the **mathematical content**: analytic rank one for the twist; and
* the **evidence grade**: whether that statement holds at `PROVED` / `PROVED_COMPUTER_ASSISTED` for the chosen `χ`.

My original `ord L(E^K,1) = 1` was therefore the right *statement*; what it lacked was a grade, not a hypothesis. I
over-corrected by inflating a computational obligation into a mathematical one.

## Unchanged

The refutation itself stands: `Q_k` is the pairing's target, not its input; `v_∞` lifts, hence all derived Bocksteins
vanish on it; the proposal "divide and evaluate the higher height" is dead. Scope remains local — derived heights on
other Selmer directions are untouched.

Remaining arithmetic work is unchanged: a suitable certified twist, and an independent evaluation or bound of
`I_{i+3}(ε^Hg_{n,0})`. **Naming that ideal has not made its evaluation easier.** No replacement mechanism is proposed.
FIN, ORDER9, Q36 open.
