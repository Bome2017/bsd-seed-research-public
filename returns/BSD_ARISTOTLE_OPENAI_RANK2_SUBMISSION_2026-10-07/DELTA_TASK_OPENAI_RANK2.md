# Delta task: can the OpenAI rank-two obstruction / determinant machinery see exactly the excess over the Mordell–Weil plane? (2026-10-07)

This project contains the canonical packet `BSD_SEED_FRONTIER_2026-10-06` (revision 2). `2_CLOSED_LANES/` also holds the later results:
- the rank-two anchor;
- the derived Gross run;
- the fixed-local-condition carrier;
- the fixed 1-motive;
- the W3 calibration at p = 17 and 19;
- the OpenAI Gate-4 check and release audit.

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

- **The scope** is the three stages below, which replace the canonical "The work" section. G1 enters only as a stop condition.
- **Bookkeeping the stages need is allowed**, despite the canonical "no further Selmer bookkeeping" item. That covers the obstruction maps, the strict / BK comparison and the switch dimension counts.

## Three stops from 10-06 (do not rebuild; respect them)

1. **p = 17 false alarm.** Ш[17] = 0, yet ℓ₂(17) ≡ 0 because the normalized 17-adic regulator is 17-divisible (`2_CLOSED_LANES/W3_P17_P19_REPORT.md`). Any detector whose index contains a cyclotomic / wild p-adic regulator must explain p = 17. If it cannot, return `WILD_REGULATOR`.
2. **Fixed receiver (PROVED).** Sel(ℚ, M_E)(p) ≅ Ш[p] for odd p, for M_E = [ℤ² → E] (`2_CLOSED_LANES/ONE_MOTIVE_RESULT.md`). Do not rebuild a receiver. Note too that its Macias Castillo–Sano determinant line carries the wild regulator.
3. **Fixed-local-condition stop (PROVED).** For large p, the line ℓ_p ⊂ W_p is locally trivial at every place in any fixed finite set (`2_CLOSED_LANES/RECEIVER_FIXED_LOCAL_CARRIER.md`). You cannot separate W_p from the excess by moving the Mordell–Weil line around with another fixed Selmer condition. Doing so returns `FIXED_LOCAL_CONDITION_LOOP`.

## Stage A (the first decision point, BEFORE any global anchor)

**Question.** Can the first-order deformation machinery canonically distinguish the Ш[p] quotient from the fixed Mordell–Weil plane?

**Universal-map requirement (Pro, 10-07).** First define 𝒟_p, the full module of admissible tame deformation directions supplied by the audited OpenAI construction, and the universal obstruction map

  𝒪_p^univ : S_p → Hom_{𝔽_p}(𝒟_p, 𝔽_p),  𝒪_p^univ(x)(d) = Obs_d(x).

If necessary, define intrinsically

  𝒟_p^W := {d ∈ 𝒟_p : Obs_d(P₁) = Obs_d(P₂) = 0}.

Stage A succeeds only if

  ker( S_p → Hom(𝒟_p^W, 𝔽_p) ) = W_p.

- **What the proof may use.** P₁ and P₂, which are fixed known data.
- **What it may not do.** It may not choose a complement or a basis of S_p/W_p, and may not use the unknown dim Ш[p] to define the obstruction map.
- **When finite lists are allowed.** Extract a finite list of directions d₁,…,d_r, giving S_p/W_p ↪ 𝔽_p^r, only **after** the universal kernel theorem is proved.

**Prove the two halves separately:**
- (A1) Obs_d(P₁) = Obs_d(P₂) = 0 for every admissible d (or every d ∈ 𝒟_p^W), for an arithmetic reason intrinsic to the construction.
- (A2) x ∉ W_p ⇒ ∃ d ∈ 𝒟_p^W with Obs_d(x) ≠ 0. This is where `vertical:obstruction-span` must enter.

**The fork to test explicitly.**
- The obstruction-span theorem may separate *all* residual Selmer classes, including κ(P₁) and κ(P₂). Then W_p ⊄ ker 𝒪_p^univ.
- Restricting to 𝒟_p^W is legitimate only if the obstruction-span property survives the restriction. If restriction destroys it, Stage A fails. Say exactly why.
- **If Stage A fails, stop immediately.**

## Stage B (only if Stage A succeeds): a rank-two determinant switch

**The tensor.** Replace the generic-rank-one tensor of `rd:det-switch` by

  Δ_W = (P₁ ∧ P₂) ⊗ (P₁^∨ ∧ P₂^∨).

**The target.** A DVR family of self-dual complexes with
- dim H¹(C_η) = dim H²(C_η) = 2 and H¹(C_η) = ⟨P₁, P₂⟩;
- dim H¹(C_k) = 2 + 2r.

A rank-two switch must send 2 + 2r ↦ 2 + 2(r−1) while preserving the valuation, or the class, of Δ_W.

**Requirements.**
- The proof must be redone in the top exterior power. Do not cite the generic-rank-one lemma as though the generalization were formal.
- The Bockstein is an available mechanism, not a required one.

## Stage C (only if Stage B succeeds): global support

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
3. **The receiver already supplies Stage A (HEURISTIC, to verify against the exact definition of Obs_d / z_γ).**
   - Take tame primes γ split completely in L_p = ℚ(E[p], p⁻¹E(ℚ)) = ℚ(M_E[p]). Then κ_γ(P_i) = 0 for an intrinsic reason, so (A1) holds.
   - For x ∉ W_p, x|_{G_{L_p}} ≠ 0 (receiver / Theorem 1). Chebotarev gives γ split in L_p with κ_γ(x) ≠ 0, and local duality at γ gives a direction d with Obs_d(x) ≠ 0, so (A2) holds.
   - If this is right, `EXCESS_OBSTRUCTION_PROVED` is a reformulation of the receiver. **State explicitly what `vertical:obstruction-span` adds beyond Chebotarev on L_p.**
4. **The record's tame route is the expected Stage B/C endpoint (HEURISTIC).**
   - G2's auxiliary ℓ (Frob_ℓ = −I, ℓ ≡ 1+p mod p²) make the tame height pairing on W_p nondegenerate (R_{p,ℓ} ≢ 0). That is a tame realization of Δ_W.
   - BKS gives C₂(p,ℓ) ≡ (a_ℓ−2)·s_p·R_{p,ℓ}.
   - So if the terminal switch index is the tame scalar s_p, Stage C is the Tame Law G1, which returns `TAME_LAW_G1`.
5. **Supersingular p.** There are infinitely many, with a_p = 0. Say whether the machinery covers them. If not, return `SUPERSINGULAR_GAP`.

## Return exactly one status

**Progress statuses, in order:**
- `EXCESS_OBSTRUCTION_PROVED`: Stage A only.
- `RANK2_DETERMINANT_SWITCH`: Stages A and B, with Δ_W preserved and no rank-one assumption.
- `GLOBAL_SUPPORT_INVARIANT`: Stages A, B and C with one fixed p-independent A_E.

**Stage A fails:**
- `STAGE_A_FAILS`: give the exact first failure. Typical cases: obstruction-span does not survive restriction to 𝒟_p^W, or (A1) needs non-intrinsic input.

**Kill statuses:**
- `NONCANONICAL_SPLITTING`: injectivity needs an unavailable basis or complement, or prior knowledge of dim Ш[p].
- `FIXED_LOCAL_CONDITION_LOOP`.
- `WILD_REGULATOR`: the index contains a cyclotomic / wild p-adic regulator, and p = 17 is unexplained.
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
