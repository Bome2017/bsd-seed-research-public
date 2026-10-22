# Summary of changes for run c7c587b4-4454-4df8-bad1-00694dbeeed6
**STATUS: EXCESS_OBSTRUCTION_PROVED.** Stage A succeeds, but it is a reformulation of the receiver kernel and gives no bound on Ш[p]. Stage B fails first at `GENERIC_RANK1_ONLY`, so Stage C was not entered. Full report, with every claim labelled PROVED, IMPORTED or HEURISTIC: `research_return/EXCESS_OBSTRUCTION_RETURN.md`. Lean: `RequestProject/Continuation/ExcessObstruction.lean`; it builds with no `sorry`, and `#print axioms` shows only propext, Classical.choice and Quot.sound.

**Hostile audit of the OpenAI lemmas** (read from the raw LaTeX):
- **The tests never see Sel_p(E/ℚ).** The residual tests in `04-vertical.tex` live over Frac(𝔽_p[[u]]), twisted by the artificial tame characters. Sel_p(E/ℚ) is the untwisted special point (χ = 1), so the machinery can only be transported there.
- **What survives the transport:** `vertical:scalar-localization`, `vertical:lift-test` (once acyclicity at the bad places is supplied by the record's fact that E(ℚ_v)[p] = 0 there for p outside B*), and the commutator identity inside `vertical:obstruction-span`. `rd:rank-two` passes as stated.
- **`vertical:obstruction-span` fails as stated** (PROVED). It needs the paired representations to be non-isomorphic, but at χ = 1 they are isomorphic through the Weil pairing. Its commutator changes are then symmetric forms, so they cannot span all rectangular matrices (Lean `commChange_symm`, `not_mem_span_of_not_symm`).
- **Not applicable or failing:** `vertical:tests` is corank-one and generic, so it does not apply. `rd:det-switch`, `rd:away-two` and `rd:outer-bound` all assume generic rank one or a simple zero.

**Stage A** (p outside B* = {2,3,19,59,487,2243,4547,5843}, supersingular p included; strict version, as the delta prescribes):
- **Setup.** Admissible directions are tame primes γ ≡ 1 (mod p) at which every bad prime and p is a p-th power, and where Frobenius minus 1 is invertible on E[p]. Obs is the lift-test invariant, independent of cochain choices (PROVED).
- **Theorem A:** ker(S_p⁰ → Hom(𝒟_p^ℓ, 𝔽_p)) = ℓ_p = W_p ∩ S_p⁰. PROVED from the packet's GL₂ image, Kummer fullness and receiver kernel, plus Chebotarev.
- **The fork.** For any obstruction map, ker(S → Hom(𝒟^W)) = W + ker 𝒪 (Lean `ker_restrictObs`), so restricting to 𝒟^W never loses separation. On the full 𝒟_p the obstruction is injective, so the points are obstructed there.
- **(A1), intrinsic reason:** for directions that differ by commutators fixing L_p, the obstruction vanishes on the points because P_i are p-divisible over L_p.
- **(A2):** for x outside W_p the change is −2e(x(v),x(w′)) ≠ 0 (Lean `stageA_kernel`).
- **What obstruction-span adds beyond Chebotarev on L_p:** only the commutator identity that turns x|G_{L_p} ≠ 0 into a nonzero second-order Frobenius invariant. It says nothing about the size of Ш[p].
- **Caveat (HEURISTIC):** if neither point localises nontrivially at p, the strict version misses at most one non-strict excess direction.

**Stage B:**
- **Single-prime no-go.** Keeping the generic H¹ = ⟨P₁,P₂⟩ forces both points to be locally trivial at the switch prime. That removes the unit-volume mechanism of `rd:det-switch` (Lean `preserve_forces_loc_zero`). For a single switch prime, a drop of the special fibre by two forces the Δ_W valuation to move by at least 2 (Lean `single_plane_drop_two`).
- **Two primes at once escape this linear algebra** (exponents (1,1,1,−3), Lean `two_plane_escape`), but no audited lemma supplies the classes such a switch needs.
- **No DVR family carries the target** (HEURISTIC). Over ℤ_p it needs Ш[p^∞] finite, and the local planes are torsion. The cyclotomic family has generic H¹ = 0 and is wild. The tame families carry generic rank ≤ 1.

**PRE-CHECK:**
1. Fixed places are blind: verified.
2. Non-anomalous at every good p ≥ 7: verified, via rational 2-torsion making #E(𝔽_p) even (Lean `not_dvd_of_even_card`).
3. Receiver supplies Stage A: verified with a correction. Primes split in L_p are *not* admissible; the correct directions are the commutator differences above.
4. Tame route leads to `TAME_LAW_G1`: not tested.
5. Supersingular p: Stage A covers them; the Stage-B sources do not, but Stage B fails earlier anyway.

**Stops and do-not list:** no p-adic regulator or direction at p enters Stage A, the receiver is not rebuilt, no fixed local condition is used, and there is no per-prime computation, W3 or plectic input.

Five Lean results are registered in the Properties table and marked proved. FIN, ORDER9 and Q36: unchanged.