# Rank-two determinant switch and the OpenAI release sweep: Gate 4 and lane status (Claude, Opus 5.5, 2026-10-06; corrected the same night)

**Proposal (Pro, 10-06).** Extend OpenAI's generic-rank-one "exact determinant-switch lemma" to generic rank two, so that the determinant line det H¹_η ⊗ (det H²_η)⁻¹ is carried by (P₁∧P₂) ⊗ (P₁^∨∧P₂^∨). The aim is to strip the 2d Ш-surplus dimensions of Sel_p while preserving the Mordell–Weil plane. Pro set four gates:
1. a rank-two switch theorem;
2. preservation of the generic plane;
3. lifting surplus classes from B_p ≅ Ш[p];
4. the terminal anchor.

**Source.** `ring-determinants.tex` (the exact DVR switch and "Selecting a rank-two evaluation") and `ring-limits.tex` (the missing-vertex construction) are both in `openai/math/preprints/A-pointwise-2-converse-for-elliptic-curves-with-rational-two-torsion-September-24-2026/build/sections/`. I read `ring-limits.tex` in full.

## Gate 4 verdict (corrected): `GATE4_FAILS_WITH_THE_CURRENT_KNOWN_ANCHOR`

**Correction.** The first version of this note gave the verdict GATE4_FAILS_STRUCTURALLY. It argued from the principle that a mechanism working over ℤ_p[[…]] at one prime cannot reach the uniform step. **That principle is withdrawn as stated.** OpenAI's missing-vertex theorem is a counterexample to it:
- It works entirely at the fixed prime 2, over Λ[G] with Λ = ℤ₂[[t]] and G a finite elementary abelian 2-group.
- It still reaches a global analytic conclusion at the base, because Gross–Zagier anchors every vertex.

The accurate statement: a fixed-p family reaches the uniform step only through a global anchor at the vertices it uses.

**What the missing-vertex theorem does** (`ring-limits.tex`, Theorem "The fixed-K missing-vertex implication"):
- **Hypotheses.**
  - The base has corank Sel_{2^∞}(E/K) = 1.
  - Binary twist families h_x exist for arbitrarily large b.
  - At every nonzero vertex x, L(E^{(h_x)},s)·L(E^{(h_x k)},s) has a simple zero.
  - There is a uniform bound 2j_{h_x} − 4w(h_x) − s(h_x) − s(h_x k) ≤ B, where j is the 2-adic Heegner index and s are Ш lengths.
- **Conclusion.** ord_{s=1} L(E,s)·L(E^{(k)},s) = 1 at the base. The theorem notes that it does not assume rank one or finite Ш at the base.
- **The anchor.**
  - Suppose the base derivative vanished. Gross–Zagier then makes the base Heegner point torsion, so the determinant coordinate is u₀(0) = 0.
  - The binary-cube congruence produces nonzero vertices whose coordinates are 2-adically close to 0.
  - That contradicts the uniform bound at the known simple-zero vertices, where Gross–Zagier makes the Heegner points nontorsion with controlled index.

**What the seed lacks.** A second-order base test, i.e. a statement of the shape L″(E,1) = 0 ⇒ (the rank-two central determinant attached to P₁∧P₂ vanishes), or an equivalent second-order spectral identity. That is the rank-two global anchor, which the live Aristotle run is testing.

**A further gap specific to FIN.** The missing-vertex theorem runs in the converse direction: from Selmer corank at the base to its analytic rank. The seed's analytic rank 2 is already proved (R.2). FIN needs the opposite direction, analytic to arithmetic (Ш finite), which in rank one comes from Gross–Zagier plus Kolyvagin. A literal second-order version would therefore reprove r_an = 2. It would need to be redesigned to output arithmetic information about the base.

**Lane status (as Pro proposed):**

| Item | Status |
|---|---|
| RANK2_SWITCH (generic-rank-two exact switch) | not disproved; open mathematics |
| RANK2_SWITCH as a seed route | blocked pending a rank-two global anchor |
| Package | deferred |
| Current priority | the live rank-two-anchor Aristotle run |
| Missing-vertex architecture (three low-rank twists around the seed) | kept. Reopen if the run produces even a candidate second-derivative base test. Note the direction gap above. |

## The broader release sweep (Pro, 10-06): assessment against the record

| Pro's item | Assessment |
|---|---|
| 1. Arbitrary-dimensional residual obstruction span (`04-vertical.tex`) | Transport machinery. Its lemma is not rank-one-specific; its application in OpenAI collapses to a line through the global Euler characteristic. Using it to preserve E(ℚ)/p and obstruct the receiver quotient still gives per-p information, and bounding Ш[p] needs an anchor. Blocked pending the anchor. |
| 2. Bockstein alternation, perfect on the non-free quotient (two-primary paper §12) | This is the record's lane-A situation (10-03, `UNIFORM_STEP_FINDINGS` §2, L4/L9). An alternating Bockstein that is nonsingular on every excess Ш pair is consistent with dim Ш[p] = 2: perfectness on the non-free quotient is Cassels–Tate-type structure and does not bound its size. Not a bound. |
| 3. Square switch / rank-two evaluation | The same as RANK2_SWITCH above. Blocked pending the anchor. |
| 4. Missing vertex using Goldfeld-density twists | Architecture kept, with the two gaps above: it needs a second-order base test, and its output direction is converse. |
| 5. Direct bound on the class-group receiver | None found by Pro. This agrees with the record. |

**Verification caveat (Pro).** None of these arithmetic manuscripts appears in the repository's `lean/formalization.yaml`, and OpenAI warns that unformalized results may have issues. Hostile audit is required before anything is imported as a theorem.

FIN, ORDER9 and Q36 are unchanged.
