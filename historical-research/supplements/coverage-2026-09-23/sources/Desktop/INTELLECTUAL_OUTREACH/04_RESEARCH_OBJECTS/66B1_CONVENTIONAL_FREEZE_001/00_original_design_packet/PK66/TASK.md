# 66b1 — mathematical design and reconstruction

This is **pre-research**, not a review of a finished result. Nothing in this packet is a theorem
about 66b1. The purpose is to get the analytic normalization right *before* anyone proves or
formalizes anything, so that later work is not built on a factor-of-two error.

Work in the order below. Question 1 gates the rest.

---

## 1. Reconstruct the exact analytic normalization for a positive-discriminant curve

This is the crux and the reason the packet exists.

66b1 has `Δ_min = +528`. The corresponding work for 62a1 relied on that curve's discriminant being
**negative**. That step is unavailable here and must be redone from scratch.

Determine precisely:

- What does Zhai's `L^(alg)(E^(M), 1)` normalize against? His definition is in the excerpts.
- What period appears in the Birch–Swinnerton-Dyer formula as stated by Banwait–Huang
  (Definition 2.1, the quantity written `Ω(E)`) and by BSTW (Theorem 10.12, written `Ω_{E^(M)}`)?
  **Neither definition of that symbol appears in the extracted text of either paper.** Resolving the
  convention is part of this question; go to the primary sources if you need to.
- How do these relate when `E(R)` has two connected components rather than one? Banwait–Huang
  address a normalization discrepancy explicitly — see their item (2) in the excerpts, which
  mentions subtracting the 2-adic valuation of the number of connected components. Work out exactly
  what that does and does not settle for the case at hand.
- Write down, with every factor of 2 accounted for, the relation among `L(E^(q), 1)`,
  `L^(alg)(E^(q), 1)`, the least positive real period, the full real period, and the quantity the
  BSD formula actually uses.

State the result as an identity you would be willing to defend, and say which convention each cited
theorem is in. **A proposed answer to this question has been deliberately withheld from the packet.**

## 2. Fix the analytic input

Zhai's Theorem 1.7 is the positive-discriminant statement. State it exactly, verify its hypotheses
against 66b1's data (§1 of `01_target`), and determine what valuation it yields **in the convention
fixed by Question 1**. Note that its conclusion is `ord₂(L^(alg)) = 1`, not `0`; decide whether that
survives conversion, and what the consequence is for the 2-part of BSD.

Also check whether 66b1 falls under Banwait–Huang's case (3) (`E(Q)[2] ≅ Z/2Z`) and, if so, whether
its conditions (3a)–(3d) can hold for this curve.

## 3. Assess the pre-registered Selmer prediction

`01_target` §4 records a prediction, made in advance:

    Sel^{φ_q} =? {1, 33, q, 33q} ,      Sel^{φ̂_q} =? {1} .

Before looking at any computation: is this the right shape? Check it against the expected image of
the quotient's rational 2-torsion, the ambient `Q({2,3,11,q}, 2)` of 32 squareclasses, and the
proposed family conditions. If you think the prediction is wrong, say so now — that is more valuable
than confirming it later.

## 4. Does the 62a1 finite-field mechanism transport?

`04_62a1_reference_only` describes a mechanism that pinned down `v₂(#Ẽ(F_q))` for 62a1 from an
explicit 4-torsion point and a halving obstruction. Ask whether 66b1 has an analogue: is there an
explicit point of order 4 on the descent model, what is its x-coordinate, and does the relevant
character condition follow from the proposed family?

Raw point-count data is in `03_arithmetic_receipts`, including a control table split by the
characters `((2/q), (33/q))`. It is data. Interpret it yourself.

If the mechanism does **not** transport, that is a real finding and should be reported as one.

## 5. Define failure criteria before starting

Write down, in advance, what would kill or redirect this experiment. At minimum:

- a period-normalization mismatch that makes the 2-part inaccessible;
- a single local Kummer image that disagrees with the prediction in §3;
- an existing theorem in the literature that already covers 66b1 — check `05_prior_art_risk`, which
  records that a 2018 thesis result was found not to apply to this isogeny class, and why;
- the 62a1 mechanism failing to transport in a way that makes the uniform-in-q step unavailable.

Say which of these you would treat as fatal and which as a redirect.

---

## What is deliberately not in this packet

No proposed solution to Question 1. No verdict on whether 66b1 will work. No roadmap. The 62a1
material is a capsule, not the project, and is marked reference-only.

## Ground rules

- Distinguish, always, what you derived from what you read.
- Treat every hypothesis label in `01_target` as a hypothesis, including the family definition.
- The literature excerpts are machine-extracted and lossy; verify anything load-bearing against the
  arXiv source.
