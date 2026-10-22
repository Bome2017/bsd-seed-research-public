# Derived-height proposal: correction accepted

Date 2026-09-21. **Additive.** Supersedes §5 of `JOIN_AUDIT_AND_NEXT_QUESTION.md`; that file is not edited.
Authority: `~/BSD_CODEX6_MASTER_HANDOFF_2026-09-19/_work/bridge_repair_assessment_2026-09-21/MCS_DERIVED_HEIGHT_GATE.md`.

## 1. My §5 is refuted as stated. Two distinct errors.

**Error 1 — input/output conflation.** I wrote "evaluate the derived height pairing `<·,·>_k` on the resulting class
in `Q_k = I^k/I^{k+1}`". That is wrong. MCS §1.4 gives
`<·,·>_k^BD : S_p^(k) x S_p^(k) -> Q_k`. The **input** filtration is `S_p^(k)`; `Q_k` is the **target**. A class does
not live in `Q_k`; its pairing value does. I had the arrow backwards.

**Error 2 — the substantive one.** Writing `y_∞ = t^e v_∞` with `v_∞ ∉ tS`, my proposal was to divide out and evaluate
the higher height of `v̄`. That returns zero, necessarily. Verified from the source: MCS Appendix A.1 defines the
spectral sequence by

    Z_k^{i,j} := ker( I^i C^{i+j} --d^{i+j}--> C^{i+j+1} / I^{i+k} C^{i+j+1} ),

with `d_k^{i,j}` induced by `d^{i+j}`. So `Z_k` consists of elements whose differential vanishes only *to depth k*, and
the derived Bockstein sends a class to the class of its differential. **An element that is an actual cocycle — `da = 0`
exactly, not merely to some depth — therefore lies in `Z_k` for every `k` and is sent to zero by every `d_k`.**

`v_∞` still lifts through the entire tower: it is a genuine element of the Λ-adic Selmer group, hence a genuine
cocycle. So `h_j(v̄, w) = 0` for every `j`. Dividing by `t^e` removes precisely the part that the derived Bocksteins
could have seen. The proposal is self-defeating, and the finiteness of `e` (from the retained tower results) does not
rescue it.

## 2. Scope of the correction — stated exactly, not generalized

This kills **"divide the Heegner class by `t^e` and evaluate its higher height"** as a way to produce the missing
coefficient. It does **not** kill derived heights on other Selmer directions, and I make no claim that it does. I have
been corrected once already in this thread for turning a local failure into a class-wide impossibility; this one stays
local.

## 3. What survives from my note

* **The depth observation itself.** `y_K` torsion (root number `-1` over `K`, `ord L(E/Q,s) = 2`, Gross-Zagier) forces
  positive augmentation depth for `y_∞`. That is your `t^e`, and it stands. What fails is my proposed use of it.
* **The twist refinement, now correctly conditioned.** I proposed adding `ord_{s=1} L(E^K, s) = 1` to the conditions on
  `K`. The sharpened version is right: what is needed is a **rigorously certified rank-one twist** — certified
  nonvanishing of `L'(E^K,1)` plus the Kolyvagin hypotheses checked for that specific `K`, yielding
  `rank E^K(Q) = 1` and `Sha(E^K)` finite as *theorems for that K*, not as an analytic expectation. That is a real
  computational obligation per candidate `K`, and my formulation understated it.
* The join audit in §§1-4 of that file (squarefree tracing, KaSa24 citation, residual-image argument) is untouched.

## 4. The sharpened statement I now record as the target

With a certified suitable `K`, dualizing the Kummer sequence and splitting off the free rank-three quotient gives

    Fitt^i_{Z/p^n}( Sha(E/K)[p^n]^* ) = I_{i+3}( ε^Hg_{n,0} ),

**without assuming FIN** — the rank-three shift is exactly the removal of the Mordell-Weil directions, which is what my
§6 friction asked for and did not supply. In particular

    I_3( ε^Hg_{1,0} ) = F_p   =>   Sha(E/Q)[p^inf] = 0.

That names the single ideal whose evaluation would suffice. It does not evaluate it.

## 5. Status

Remaining here: (a) a certified suitable twist, and (b) an independent arithmetic evaluation or bound of
`I_{i+3}(ε^Hg_{n,0})`. Neither is supplied by me, and I am **not** proposing a replacement mechanism in this note —
proposing one immediately after having a proposal refuted is how the previous three errors in this thread were
generated.

FIN, ORDER9, Q36 unchanged. Full BSD open. Nothing modified: master, packet and sealed folders untouched.
