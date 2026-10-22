# Delta task (revision 2): audit the tame Stage-A derivation, then build the point sections toward a rank-two switch (2026-10-07)

This project contains the canonical packet `BSD_SEED_FRONTIER_2026-10-06` (revision 2). `2_CLOSED_LANES/` also holds the later results:
- the rank-two anchor;
- the derived Gross run;
- the fixed-local-condition carrier;
- the fixed 1-motive;
- the W3 calibration at p = 17 and 19;
- the OpenAI Gate-4 check and release audit.

**What changed since revision 1.**
- Codex wrote a Stage-A derivation (lab bb6ed896), included in `4_CODEX_STAGE_A/`:
  - `STAGE_A_DERIVATION.md`;
  - `NEXT_ARITHMETIC_STEP.md`;
  - Claude's desk review, `CLAUDE_DESK_REVIEW.md` (SUPPORTED_AT_DESK_LEVEL).
- Stage A is now an **independent audit** of that derivation, not a fresh construction.
- Stage B starts from the second-order equation (L2).

Read `CURRENT_FRONTIER.md` first. **This file governs the run.** Every rule in the root `TASK.md` "Do not" list applies. The overrides are stated below.

## Notation

- E is the seed on its minimal model [0,−1,0,−66020924,−65074271436]. Its rational points are P₁ = (−3031, 327384) and P₂ = (−2394, 281520): a saturated basis of E(ℚ)/tors, with E(ℚ)_tors ≅ ℤ/2.
- p is an odd prime outside an explicit finite set that you state.
- S_p := Sel_p(E/ℚ) and W_p := E(ℚ)/p = ⟨κ(P₁), κ(P₂)⟩ ⊂ S_p, so that 0 → W_p → S_p → Ш[p] → 0.
- **If the OpenAI machinery works with strict Selmer spaces, say so and adjust.** The strict-at-p Selmer group S_p⁰ has dimension 2 + dim Ш[p] − ε_p (record). It meets W_p only in the line ℓ_p = ker(W_p → E(ℚ_p)/p) (see PRE-CHECK 2). In that case the Stage-A target is ker = W_p ∩ S_p⁰.

## Imported sources: hostile audit required (do not import wholesale)

The sources are in github.com/openai/math (Apache-2.0; read the raw LaTeX). The repository warns that unformalized results may contain errors. Extract **only** the exact statements you need and check every hypothesis against the seed before you use them.

- **`preprints/Exact-Birch-Swinnerton-Dyer-Formula-from-Low-Selmer-Corank-October-3-2026/build/sections/04-vertical.tex`**
  - `vertical:obstruction-span`: finitely many tame directions have lift matrices spanning the required matrix spaces.
  - Also `vertical:lift-test`, `vertical:auxiliary-tuples`, `vertical:tests`, `vertical:enlargement` and `vertical:horizontal-directions`.
  - Note: the proof of `vertical:tests` uses an Euler characteristic of −1 ("one residual degree-one line"). That is a corank-one input.
- **`preprints/A-pointwise-2-converse-for-elliptic-curves-with-rational-two-torsion-September-24-2026/build/sections/ring-determinants.tex`**
  - `rd:det-switch` (the exact determinant switch over a DVR) and `rd:valuation-switch`.
  - `rd:rank-two` (selecting a rank-two evaluation from independent classes).
  - `rd:away-two`, `rd:outer-bound` and `rd:common-tensor`.
  - Note: `rd:det-switch` **assumes generic rank one**: H¹(C_F ⊗ F_O) = F_O·A. A rank-two evaluation is not a rank-two determinant switch.
- **The two-primary BSD paper (Sep 24), §12, conjugate Bockstein alternation.** It was proved in an induced / dyadic setting. Optional: use it only if you derive an odd-p analogue from the relevant self-dual Selmer complex, or cite an exact theorem with matching local conditions. There must be no silent transfer.

## Overrides of the canonical `TASK.md` for this run

- **The scope** is Stages A′, B′ and C below, which replace the canonical "The work" section. G1 enters only as a stop condition.
- **Bookkeeping the stages need is allowed**, despite the canonical "no further Selmer bookkeeping" item. That covers the obstruction maps, the strict / BK comparison and the switch dimension counts.

## Three stops from 10-06 (do not rebuild; respect them)

1. **p = 17 false alarm.** Ш[17] = 0, yet ℓ₂(17) ≡ 0 because the normalized 17-adic regulator is 17-divisible (`2_CLOSED_LANES/W3_P17_P19_REPORT.md`).
   - One false alarm does not refute a one-sided detector.
   - An index containing the wild regulator cannot give a FIXED A_E if regulator-divisible primes are infinite, which is the heuristic expectation. Return `WILD_REGULATOR` in that case.
2. **Fixed receiver (PROVED).** Sel(ℚ, M_E)(p) ≅ Ш[p] for odd p, for M_E = [ℤ² → E] (`2_CLOSED_LANES/ONE_MOTIVE_RESULT.md`). Do not rebuild a receiver. Note too that its Macias Castillo–Sano determinant line carries the wild regulator.
3. **Fixed-local-condition stop (PROVED).** For large p, the line ℓ_p ⊂ W_p is locally trivial at every place in any fixed finite set (`2_CLOSED_LANES/RECEIVER_FIXED_LOCAL_CARRIER.md`). You cannot separate W_p from the excess by moving the Mordell–Weil line around with another fixed Selmer condition. Doing so returns `FIXED_LOCAL_CONDITION_LOOP`.

## Stage A′: hostile audit of the Codex derivation (the first decision point, before any global anchor)

**The claim to audit** (`4_CODEX_STAGE_A/STAGE_A_DERIVATION.md`). D is the span of conductor-q additive characters λ_q, for q ≡ 1 (mod p) with ρ(Frob_q) = −I, chosen locally zero at Σ. For λ ∈ D, take the first-order deformation M_λ = V ⊕ εV, with the local conditions given there. Then:
- b_λ : S_p → S_p^* is the Morgan–Smith Cassels–Tate pairing, whose left radical is image[Sel(M_λ) → S_p];
- D^W = {λ : b_λ(κ(P₁)) = b_λ(κ(P₂)) = 0}, as vector equations;
- ker[S_p → Hom(D^W, S_p^*)] = W_p.

**The universal-map requirement still governs.**
- No complement or basis of S_p/W_p, and no use of dim Ш[p], may define the map.
- A finite list of directions may be extracted only after the kernel theorem.

**Priority checks.**
- (a) Morgan–Smith (arXiv 2103.08530): Definition 1.1 exactness for these local conditions; the Theorem 1.3 kernels; the Definition 3.2 cochain normalization behind (D)/(E); Proposition 4.4 Baer linearity.
- (b) The cochain signs and the reciprocity normalization (§4 of the derivation).
- (c) The field intersection K ∩ R = ℚ(μ_p), and the marked-representative Chebotarev prescription (§5–6).
- (d) Whether b_λ is symmetric. If it is, D^W realizes exactly the symmetric forms on S_p/W_p ≅ Ш[p].

**Outcomes.**
- If the audit finds a fatal gap, return `STAGE_A_FAILS` with the first failure, and stop.
- If it passes, Stage A is `EXCESS_OBSTRUCTION_PROVED` (audited). Separation is not a bound.

## Stage B′ (only if Stage A′ passes): point sections, then a rank-two switch

**B1. Second order** (`4_CODEX_STAGE_A/NEXT_ARITHMETIC_STEP.md`).
- Setup: χ(t) = 1 + tλ + (t²/2)λ² (mod t³), with μ = λ²/2 corrected by admissible η. First-order lifts a_i satisfy d a_i = −λ∪c_i.
- Decide whether (L2) can be solved simultaneously for i = 1, 2, with the **same** η and matching local Selmer conditions: d b_i = −λ∪a_i − μ∪c_i.
- Identify the cokernel of the correction map η ↦ (η∪c₁, η∪c₂).
- Track the dependence on the section choices a_i. They may not be chosen silently to make the obstructions zero.

**B2.** If B1 succeeds, construct the joint point sections to order three.

**B3.** Only then, the rank-two determinant switch.
- Replace the generic-rank-one tensor of `rd:det-switch` by Δ_W = (P₁ ∧ P₂) ⊗ (P₁^∨ ∧ P₂^∨).
- Target: dim H¹(C_η) = dim H²(C_η) = 2 with H¹(C_η) = ⟨P₁, P₂⟩, and dim H¹(C_k) = 2 + 2r.
- A switch sends 2 + 2r ↦ 2 + 2(r−1) while preserving the valuation or class of Δ_W.
- Redo the proof in the top exterior power. A first-order kernel W does not by itself give generic sections; see the formal example diag(t²I₂, tI₂) in the next-step note.

## Stage C (only if Stage B′ succeeds): global support

The global ledger moves only with

  p ∉ S, Ш[p] ≠ 0 ⇒ p ∣ A_E,

for one fixed 0 ≠ A_E ∈ ℤ, or one fixed nonzero rational or fractional ideal after explicitly clearing a finite denominator set.

**These do NOT count:**
- a p-dependent A_{E,p};
- Reg_p, or any wild p-adic regulator;
- an uncontrolled p-unit ambiguity;
- q, #Ш, or the ETNC normalization.

**This is where Gate 4 may reappear** (`2_CLOSED_LANES/OPENAI_GATE4_CHECK.md`): a fixed-p family crosses into the uniform step only through a global anchor at its vertices.

## PRE-CHECK (Claude, 10-07): verify or refute; do not rediscover

1. **Fixed places are blind.** For large p and every fixed finite place v ≠ p, E(ℚ_v)/p = 0, so loc_v vanishes on ALL of S_p. Admissible directions must therefore come from p-dependent tame primes, or from p itself. Directions at p are wild, which means stop 1 applies.
2. **The strict space.** E(ℚ_p)/p is one-dimensional at good non-anomalous p, and the seed is non-anomalous at every good p ≥ 7. So W_p ∩ (strict at p) = ℓ_p, of dimension ≥ 1, and dim S_p⁰ = 2 + dim Ш[p] − ε_p.
3. **Correction to revision 1's pre-check 3** (Codex, accepted).
   - ℚ(M_E[p]) = ℚ(E[p], p⁻¹P₁, p⁻¹P₂) is **not** the record's class-group receiver field, which is larger.
   - With full Kummer image (G2 §6), inflation–restriction gives ker(H¹(ℚ,V) → H¹(ℚ(M_E[p]),V)) = W. So split-prime *restriction* separates S_p/W_p.
   - That is not a first-order *deformation* obstruction. The Codex construction (Frobenius −I primes, a secondary cochain value, the generalized Cassels–Tate pairing) is the deformation-theoretic statement.
4. **The record's tame route is the expected Stage B/C endpoint (HEURISTIC).**
   - G2's auxiliary ℓ (Frob_ℓ = −I, ℓ ≡ 1+p mod p²) make the tame height pairing on W_p nondegenerate (R_{p,ℓ} ≢ 0). That is a tame realization of Δ_W.
   - BKS gives C₂(p,ℓ) ≡ (a_ℓ−2)·s_p·R_{p,ℓ}.
   - So if the terminal switch index is the tame scalar s_p, Stage C is the Tame Law G1, which returns `TAME_LAW_G1`.
5. **Supersingular p.** There are infinitely many, with a_p = 0. Say whether the machinery covers them. If not, return `SUPERSINGULAR_GAP`.

## Return exactly one status

**Progress statuses, in order:**
- `EXCESS_OBSTRUCTION_PROVED`: the Stage A′ audit passes, and B1 is not achieved.
- `POINT_SECTIONS_ORDER3`: Stage A′ plus B1 and B2. The joint point sections are constructed to order three, and the cokernel of the correction map is identified.
- `RANK2_DETERMINANT_SWITCH`: Stage A′ and all of B′, with Δ_W preserved and no rank-one assumption.
- `GLOBAL_SUPPORT_INVARIANT`: Stages A, B and C with one fixed p-independent A_E.

**Stage A fails:**
- `STAGE_A_FAILS`: the audit finds a fatal gap in the Codex derivation. Give the first failure.
- `SECOND_ORDER_OBSTRUCTED`: (L2) has no simultaneous solution with the same η and matching local conditions, for an identified obstruction class. Give it.

**Kill statuses:**
- `NONCANONICAL_SPLITTING`: injectivity needs an unavailable basis or complement, or prior knowledge of dim Ш[p].
- `FIXED_LOCAL_CONDITION_LOOP`.
- `WILD_REGULATOR`: the index contains a cyclotomic / wild p-adic regulator. A fixed A_E must then absorb every regulator-divisible p, and these are expected (heuristically, Σ1/p) to be infinite. p = 17 is one known instance. A single false alarm does not by itself refute a one-sided detector.
- `SUPERSINGULAR_GAP`.
- `GENERIC_RANK1_ONLY`: the switch cannot be done without a generic rank-one class.
- `ETNC_CIRCULAR`: globalization needs q, #Ш or the ETNC normalization.
- `TAME_LAW_G1`: globalization is the record's Tame Law (s_p ≡ A mod p) in another form.
- `SOURCE_HYPOTHESES_FAIL`: an imported OpenAI lemma's hypotheses fail for the seed, or the lemma is wrong. Name it.

## Do not (in addition to the canonical list)

- W3 computations, OpenAI Result 002 transplants beyond the named lemmas, the plectic framework, the exceptional primes, any per-prime computation, or any large computation.
- Rebuilding the receiver, the 1-motive determinant line, R1–R5, or the derived-Gross routes.
- Re-deriving G2, Theorem W or the BKS factorization. Cite the packet.
- Importing an OpenAI statement without the hypothesis audit above.

## Return format

As in the canonical `TASK.md`:
- one STATUS line;
- every claim labelled PROVED, IMPORTED or HEURISTIC. A claim imported from the OpenAI repo also needs its file, its label and the result of the hypothesis audit;
- Lean with no `sorry`, plus `#print axioms` for every new theorem. The algebraic skeleton is enough: for example the universal-kernel linear algebra of Stage A, and the top-exterior-power switch of Stage B;
- end with "FIN, ORDER9 and Q36: unchanged", or a precise statement of what changed.
