# Receiver / excess-class-group congruence object: admission screen (Claude, Opus 5.5, 2026-10-06; scope corrected the same night)

**Question (Pro, 10-06).** Is there a fixed characteristic-zero module M_E, independent of p, with B_p ≠ 0 ⇒ M_E[p] ≠ 0 for all large p? Here B_p ≅ Ш(E/ℚ)[p] for p ≥ 5 (record). The statuses offered were FIXED_RECEIVER_MODULE, REDUCTION_TO_NEW_CONGRUENCE_THEOREM, SELMER_LOOP and NO_FIXED_OBJECT.

## Verdict (scope corrected per Pro, 10-06)

**`FIXED_LOCAL_CONDITION_CARRIER = SELMER_LOOP`.** This is proved below (Lemma 1).
- It is **not** `RECEIVER_UPPER_BOUND = CLOSED`. The exact receiver B_p quotients the global Kummer kernel W = E(ℚ)/p by passing to L_p. So a direct, independent arithmetic bound on B_p remains logically open. Identifying B_p with Ш[p] does not exclude an independent estimate on B_p (cf. the receiver review).
- The OpenAI arbitrary-dimensional obstruction-span mechanism is **not** covered by Lemma 1. It chooses deformation directions after identifying global classes. Whether it can keep the two Mordell–Weil directions while killing the excess is still open.
- A fixed object that carries E(ℚ) itself is not excluded. The natural one is the 1-motive M_E = [ℤ² → E] (Pro, 10-06), and a bounded admission package was built for it. My heuristic expectation that its invariant is q is a prediction to test, not a verdict.
- No Aristotle package was built for the fixed-local-condition carrier.

## Lemma 1 (the fine-Selmer Kummer line; PROVED, elementary)

**Statement.** Let E/ℚ have rank r ≥ 2, and let Σ be a finite set of places containing ∞ and the bad primes. Take any prime p ∉ Σ such that:
- p ∤ #Ẽ(F_p);
- p ∤ ∏_{v∈Σ finite} #E(ℚ_v)_tors.

Then ℓ_p := ker(E(ℚ)/p → E(ℚ_p)/p) has dimension ≥ r − 1. Its Kummer image lies in the fine Selmer group: classes unramified outside Σ ∪ {p} and locally zero at every place of Σ ∪ {p}.

**Proof.**
1. The Kummer map E(ℚ)/p → H¹(ℚ, E[p]) is injective.
2. For finite v ∈ Σ, E(ℚ_v) has a pro-v subgroup of finite index, so dim E(ℚ_v)/p = dim E(ℚ_v)[p] = 0.
3. E(ℝ)/p = 0 for p odd.
4. At v = p, good and non-anomalous, E(ℚ_p) ≅ ℤ_p × (a finite group of order prime to p), so E(ℚ_p)/p is one-dimensional.
5. Kummer classes of global points are unramified at good v ≠ p.

So the kernel has dimension ≥ r − 1, and its image is locally zero at every place of Σ ∪ {p}. ∎

**For the seed.** r = 2. Since a_p is even and |a_p| ≤ 2√p, the seed is non-anomalous at every good p ≥ 7. The exceptional set is finite and explicit.

## Corollary 1

**Statement.** Let F be any Selmer structure with arbitrary local conditions at a fixed finite set T and the unramified condition elsewhere. Then H¹_F(ℚ, E[p]) ⊇ κ(ℓ_p) ≠ 0 for all p outside a finite set; enlarging T only enlarges that set.

**Consequences.**
- A fixed automorphic or deformation problem (fixed level, fixed local conditions) sees a nonzero extension of 1 by E[p] at every large p.
- If every such class forced p | #M_E, then M_E would be divisible by every large prime. So "B_p ≠ 0 ⇒ M_E[p] ≠ 0" with M_E finite cannot come from a mechanism that applies to all classes of a local-condition Selmer group.
- **Dainobu agrees.** arXiv 2405.19142v3 (2026-04-22), Theorem A remark: the E[p]-component of Cl(ℚ(E[p])) is always nonzero when rank E(ℚ) ≥ 2. Fine-Selmer classes give everywhere-unramified E[p]-extensions of ℚ(E[p]).
- **Pro's step "quotient out the Kummer part"** is exactly the step that local conditions cannot perform. ℓ_p is a p-dependent line, invisible to every fixed local condition for large p.

## What survives

A working M_E must carry E(ℚ). The receiver does this by passing to L_p = ℚ(E[p], p⁻¹E(ℚ)), the p-torsion field of the fixed 1-motive [ℤ² → E].
- The natural fixed invariant of such an object pairs L-data with the Mordell–Weil lattice. The only known one is q = L″(E,1)/(2Ω·Reg) (HEURISTIC).
- That is Pro's stop condition 4 when used as an input, and the rank-two anchor when proved as an identity.
- No known congruence or automorphic theory for the (mixed) Galois representations of 1-motives would supply a different invariant.

## Record cross-checks (do not redo)

- **10-01, REPORT addenda 35–40 (Claude + Codex): the GL₃ realizations of this idea.**
  - Weight-2 datum: the constant term is L(E,1) = 0, and the strict Bloch–Kato condition returns S₀ ≠ 0 at every p. That is the Mordell–Weil baseline, the same phenomenon as Lemma 1.
  - R^red = T (Berger–Klosin Assumption 5.1(1), dim H¹_Σ = 1) amounts to m_p = 1, which is circular.
  - Weight-3 repair: b_p ≤ 3 ⇒ Ш[p^∞] = 0, three-way checked. It is per-prime only, because g_p varies with p.
- **Lane C receptacles (10-01).** Fixed abelian-variety receptacles force B ~ E × C. Prime-to-p twist parts are blind. The adjoint receptacle is zero.
- **Invisible-Ш test bank (10-01, scope-corrected).** It refutes moddeg and the congruence number specifically, not all fixed integers.
- **U22 (paused 09-29).** Eisenstein congruences bound Selmer from below. Revival needs the I3 identity C₂ = u·det h.

## Sources checked 10-06 (abstract level; leads, not audited)

| Source | What it gives |
|---|---|
| Dainobu, arXiv 2405.19142 v3 | Ribet direction only, analytic rank 1. Its quantity mixes L′(E,1)_alg with a p-adic factor. In rank ≥ 2 the component is always nonzero. |
| Dainobu, arXiv 2304.05035 | A lower bound on the multiplicity, via everywhere-unramified points |
| Ray–Weston, arXiv 2204.09757 | Height-ordered statistics, conditional on finite Ш |
| Prasad–Shekhar, arXiv 1912.12928 (read 10-01) | m_p ≤ rank Sel_p + #T: a bound by Selmer |
| Kim, arXiv 2609.15328 (2026-09-14, new) | Heegner detection of Ш[p^∞] finiteness, any rank, for **semistable** curves, prime by prime. The seed is not semistable (additive at 2 and 4547, and potentially good at 4547, so no quadratic twist is semistable). |
| Destrempes–Malinin, arXiv 1703.02215 | Claims Ш[ℓ] = 0 for almost all ℓ, every non-CM curve. **Already KILLED** (09-19 hostile audit: Theorem 6 Step 2 trace error; DO_NOT_RESURRECT row 18). |
| **Plectic (Pro's next item, checked at the gate):** Fornea–Gehrmann, arXiv 2203.15998 | Algebraicity only for polyquadratic plectic points, where the rank comes from a product of rank-one Heegner pieces. The seed's rank two sits in E(ℚ) with the twist of rank 0, which this does not cover. Archimedean plectic objects for that case are conjectural (Nekovář–Scholl). **Status: MISSING_CONSTRUCTION**, as Pro predicted. |
| MIT "Gross–Zagier, 40 years later" (Aug 3–7, 2026) | Higher Gross–Zagier is still presented as function-field only (Z. Wang). Grossi presents Heegner results in analytic rank > 1 inside Iwasawa theory, i.e. prime by prime. |

## Corrections accepted (Pro, 10-06)

- **Plectic.** `MISSING_CONSTRUCTION` for the seed, meaning no usable seed object exists at present. It is not a structural impossibility.
- **Literature wording.** No number-field analogue of the Yun–Zhang higher-derivative (r > 1) formula is known; Chao Li notes this. Number-field higher-dimensional Gross–Zagier-type results do exist for **first** derivatives: arithmetic inner product formulas, and Disegni–Zhang's p-adic Gan–Gross–Prasad formula.
- **Targeted literature delta**, to screen before anything further is closed:
  - Grossi: Heegner points and Iwasawa theory in analytic rank > 1;
  - Sangiovanni Vincentelli: theta classes and a base-change Euler system;
  - number-field arithmetic GGP / Siegel–Weil machinery.
- **Canonical state.** Do not write "every route now ends at one missing theorem". Two materially different exits remain open: an independent bound on the exact receiver, and the OpenAI rank-two obstruction/determinant mechanism.

## Re-admission

Reopen only with either:
- a datum that carries E(ℚ) (for example a congruence object for the 1-motive [ℤ² → E]) whose fixed invariant is defined without q, Ш, Q36 or BSD; or
- a proved rank-two identity.

FIN, ORDER9 and Q36 are unchanged.
