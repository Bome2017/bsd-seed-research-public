# Uniform step: what was discovered, 2026-10-02 → 10-03

Written by Claude on 10-03 while the attack lanes were still running; sections marked (in progress) will be updated from the lane folders under `~/BSD_UNIFORM_ATTACK_2026-10-03/`. Governing records: the master map `~/BSD_BUILD_MAP/SEED_MASTER_MAP_2026-10-01.md` (§13–14), Codex's `~/BSD_UNIFORM_ASSEMBLY_CODEX_2026-10-03/ASSEMBLY.md`, and `RUN_NOW_2026-09-29.md`.

## 0. The target, stated once

For the seed curve E (rank 2, P₁, P₂, Tam 16, torsion ℤ/2, N = 2³·3·2243·4547²·5843):

> **Find one finite set S such that dim_{F_p} Sel_p(E/ℚ) ≤ 3 for every prime p ∉ S.**

Under the retained parity theorem this forces dim Sel_p = 2 and Ш[p^∞] = 0 outside S. That is the uniform step. FIN = this plus finiteness at the finitely many primes of S; ORDER9 and Q36 come after. Per-prime results (p = 53, the bad primes, the K167 plectic evaluator) do not touch it.

## 1. What the record already had (verified facts used by every lane)

- **Fact 1** (p ∉ B* = {2,3,19,59,487,2243,4547,5843}): E(ℚ_v)/p = 0 and E(ℚ_v)[p] = 0 at every bad place v, and E(ℚ_p)[p] = 0 at every good p ≥ 5 (lane B, Lemma 0: a_p is even because of the rational 2-torsion point (−7578,0), so a_p ≢ 1 mod p). So H²(ℚ_v, E[p]) = 0 for every v ∈ S.
- **Fact 2:** the p-strict Selmer group S₀ = ker(loc_p) equals Ш¹_S(E[p]), and H²(G_S, E[p]) = Ш²_S(E[p]) ≅ S₀^∨. Euler characteristic: h¹(G_S, E[p]) = 1 + h²(G_S, E[p]). Hence **Ш[p] = 0 ⟺ h²(G_S, E[p]) ≤ 2 ⟺ dim S₀ ≤ 2 − ε_p**, where ε_p = rank(loc_p on Sel_p) ∈ {0,1}. On the seed ε_p = 1 at every good p in [5, 47] (P₁ ∈ pE(ℚ_p) only at p = 5; P₂ never).
- **K-LOC (locality lemma, unaudited by Codex, re-verified numerically by lanes A and B):** for a finite G_S-module M with Ш²_S(M) = 0 and any fixed z ∈ H¹(G_S, Hom(E[p], M)), the map x ↦ z ∪ x vanishes on S₀. Any construction that factors through localization at a fixed finite set of places is blind to the excess. Admissible shapes: (a) targets with Ш² ≠ 0, above all E[p] itself, reached by twist-0 coefficient classes; (b) secondary operations; (c) uniform control of a p-dependent family by a p-independent identity; (d) fixed global geometric objects.
- **Codex's assembly (10-03):** with auxiliaries a, b from the determinant construction, Sel_p = ⟨P₁,P₂⟩ ⊕ X_{p,a,b} with X_{p,a,b} ≅ Ш[p]; δ_ab ≠ 0 ⟺ X_{p,a,b} = 0 ⟺ Ш[p^∞] = 0; δ_ab = C_p·e_a·e_b·D_ab² with D_ab, e_a, e_b nonzero by choice; **C_p ≠ 0 for almost all p is the unproved statement.** The existing parts permit "first nonzero witness length ≥ 4, C_p = 0." Named sufficient shape: an integer A from independent data with X_{p,a,b} ≠ 0 ⇒ p | A; or a p-dependent uniform estimate killing the kernels.

## 2. Lane A — twist-0 adjoint class, pairing on S₀ (DONE: FIRST_FAILURE)

Folder `A_twist0_adjoint/` (LEMMAS.md L0–L9, FIRST_FAILURE.md, gp/).

**Construction that works.** For ordinary p outside B* and a finite set, the Hida family through E has tangent class z_Hida ∈ H¹(G_S, ad E[p]); its trace-zero part z = z_p⁰ ∈ H¹(G_S, ad⁰E[p]) is non-crystalline at p. The cup product δ_z : x ↦ z ∪ x maps H¹(G_S, E[p]) → H²(G_S, E[p]) = S₀^∨ with **no Tate twist** (the action map ad⁰ ⊗ E[p] → E[p] is twist 0; the Weil twist is absorbed in E[p]^∨ ≅ E[p]). Target checked nonzero at every p in [5,47] (dim = 1 + dim Ш[p]). K-LOC passes: the target has Ш² ≠ 0 and the map has no local formula.

**Lemmas (DERIVED unless noted).**
- L3: the pairing β_z(x,y) = ⟨z ∪ x, y⟩_PT on Sel_p × S₀ is well defined and equals the Selmer-complex Bockstein of the deformation T_Λ/(p, X²) (Nekovář formalism, IMPORTED).
- L4: **β_z is alternating.** On W = ⟨P₁,P₂⟩ it is one scalar a_p. On S₀ × S₀ it is degenerate whenever ε_p = 1.
- L5: the Flach pairing of the weight-3 lane decomposes as β^Fl = β_z + c·h_θ (alternating + symmetric), where h_θ is the mod-p cyclotomic height.
- L6: auxiliary-prime coefficient classes with a fixed auxiliary set T are **empty** for p ∤ D_T (so shape (a)(ii) with fixed T is dead; p-dependent T is the per-prime route).
- L7: z is determined by its restriction z|_{G_p} (which carries Greenberg's L-invariant), but β_z is not a function of z|_{G_p} through any local formula.
- L8: p-independent lifts of κ(P_i) through J₁(Np²) are killed: the composite is multiplication by p².
- L9 (kill test on the countermodel Sel = F_p⁴ ⊇ W): **every alternating form on Sel_p is consistent with everything proved or on record.** In particular "β_z nondegenerate on W (a_p ≠ 0)" plus "rank β_z ≤ 2" is consistent with Sel_p = W ⊕ rad(β_z) and dim Ш[p] = 2.

**First failure (precise).** To conclude Ш[p] = 0 one needs (H2): h²(G_S, T_Λ/(p, X²)) ≤ 2 for all ordinary p outside a finite set (plus a Coleman-family analogue at supersingular p). That is equivalent to the target: COLLATERAL. No p-independent identity constrains β_z on the excess. The two statements a first-order construction from P₁, P₂ could prove — nondegeneracy on the points, and a rank bound — never distinguish Ш[p] = 0 from Ш[p] ≅ (ℤ/p)².

**Refuters (3 per lemma, in progress at time of writing):** folders refute_1..3 for L0, L1, L2/L3 exist; verdicts to be read from the workflow result.

## 3. Lane B — secondary operations (DONE: FIRST_FAILURE)

Folder `B_secondary_ops/` (LEMMAS.md Lemma 0–6, FIRST_FAILURE.md, gp/: seedcheck, s0check, heights, h17).

**Twist bookkeeping settled (Lemma 2–3).** With V = E[p], det V = ω (mod-p cyclotomic), V ≅ V^∨(1): every Massey product whose entries all come from H¹(G_S, V) has twist (k−1)/2 for k entries, **never zero** for 2 ≤ k ≤ p−1. In particular ⟨κ(P₁), κ(P₂), x⟩ is defined for every x ∈ Sel_p but lands in H²(G_S, E[p](1)), whose Ш² is dual to the ω⁻¹-eigenspace of the strict Selmer group over ℚ(μ_p), not to S₀. The G1 failure (10-01) was an instance of this. Twist-zero operations on x ∈ S₀ require a fixed entry from H¹(G_S, F_p) (the cyclotomic character θ), from H¹(G_S, ad⁰E[p]), or an opposite-twist pair H¹(V(j)) × H¹(V(−1−j)).

**Indeterminacy (Lemma 6).** Every twist-zero Massey product containing x ∈ S₀ is a coset of a subgroup containing H¹(G_S, M) ∪ x with M ⊆ End E[p] = F_p ⊕ ad⁰. So a secondary operation defines a functional on S₀ only on S₀ ∩ ker(θ ∪ −) ∩ ker(z′ ∪ −): only after the first-order shape-(a) functionals (the cyclotomic height θ ∪ x and the adjoint/weight heights z′ ∪ x) vanish on x.

**Fails on the seed.** h^(1)(x₀,x₀) = ⟨θ ∪ x₀, x₀⟩ ≠ 0 for the generator x₀ of S₀ at **every good ordinary p ≤ 200** (value 2 at p = 5 and 7). So at every tested prime the domain of ⟨θ,θ,x⟩ on S₀ is zero, and every Massey product containing x₀ with F_p in M is the full one-dimensional target: no information.

**New fact of independent interest:** the mod-p cyclotomic height pairing on S₀ is nonzero at all good ordinary p ≤ 200 on the seed. This is a p-adic-height-type nondegeneracy statement at the mod-p level; whether it has a uniform proof is open (it would be shape (c)).

## 4. Lane C — Codex's "S" relation from data (DONE: FIRST_FAILURE, kill test FIRED)

Folder `C_selmer_relation_S/` (LEMMAS.md Lemma 1–9, FIRST_FAILURE.md, checks/kato_loc.log; 3 refuters per lemma running).

**Setting.** X_B = Sel_p(E/L)^∨ over A_B = F_p[T₁,T₂]/(T₁^p, T₂^p), L the C_p² field of two transvection Kato primes q₁, q₂, with Codex's contracted datum β ≡ δ·T₁T₂ mod J³, δ ≠ 0, and the saving statement S: r_p > 2 ⇒ β ∈ Fitt_{r−3}(X_B).

**Lemmas (DERIVED unless noted).**
- Lemma 1: **S is a generator bound, not a relation among relations.** The requested identity would express a class of exact degree 2 by minors of size d_L − (r − 3); the degree count forbids it unless the generator count is already ≤ 2.
- Lemma 2: the bad places carry nothing for p ∉ B* (Fact 1 re-derived with independent numbers; H¹(ℚ_v, E[p]) = 0).
- Lemma 3: the generator count of X_B equals dim Sel_p(E/ℚ).
- Lemma 4: the local cup product at a Kato prime is perfect; the twist is absorbed locally.
- Lemma 5: at first order the T_i-action on X_B is the Bockstein x ↦ x ∪ χ_{q_i} with the Kurihara characters; its global part lives in Ш²_{S∪{q₁,q₂}}(E[p]) ≅ (S₀ ∩ ker loc_{q₁} ∩ ker loc_{q₂})^∨.
- **Lemma 6: the relation that holds at r = 2 and fails at r = 4 is "r = 2" restated.**
- Lemma 7 (COMPUTED, gp): localization determinants at Kato primes for p = 3, 5, 7, 11, 13 on the seed.
- Lemma 8: the certified p = 3 relation ([T²]L₃ ≡ 0 mod 3) is the depth statement itself; and the p = 3 contrast is contaminated (3 ∈ B*: 3 | 5844 gives a nontrivial local condition at 5843).
- Lemma 9: the structural sources named in the brief (Cassels–Tate alternation, Steinberg constraints at 3/2243/5843, the 2-torsion) give relations among relations or local vanishings, never a generator bound.

**First failure (precise).** The generator count. Nothing in the presentation bounds the number of A_B-generators of X_B by 2 without assuming it.

**What would fix it:** (1) an independent bound dim Sel_p^{rel(q₁,q₂)}(E/ℚ) ≤ 2 for one Kato pair per p, i.e. Ш¹_{S∪{q₁,q₂}}(E[p]) = 0, which is the target (COLLATERAL); or (2) a secondary operation on S₀ computable from a p-independent object (lane B's territory; Lemma 5 identifies the operation the two-prime presentation actually uses: the Bockstein with the Kurihara characters, which are p-dependent). Not a fix: more presentations, more symmetry, more matrix identities, more primes (Lemma 1 holds for every presentation and every p). No conjecture proposed.

## 5. Lane D — receptacle / integer-A shape (DONE: FIRST_FAILURE per candidate)

Folder `D_receptacle/` (LEMMAS.md D1–D4, FIRST_FAILURE.md, a1check.gp; refuters running).

Four candidate receptacles F with maps X_{p,a,b} → F[p], each checked for (a) factoring through fixed-place localization, (b) Tate twist, (c) independence from Ш(E):

| F | Map | First failure |
|---|---|---|
| Br(A)/Br₁(A), A = E × 37a1 (finite by Skorobogatov–Zarhin) | linear via Kummer → H¹(ℚ, Pic Ā); bilinear x ∪ y ∈ H²(ℚ, E[p] ⊗ E′[p]) | linear image lies in Br₁ (not the transcendental part); bilinear image has μ_p^{⊗2}, no map to μ_p for p ≥ 3 |
| H²_et(ℤ[1/S], E[p] ⊗ W), W a fixed auxiliary motive (E′[p], μ_p^{⊗j}, ℤ/p[Gal(K/ℚ)]) | x ↦ x ∪ y, y ∈ H¹(G_S, W) fixed | receptacle is Ш²_S(E[p] ⊗ W) ≅ Ш¹_S(E[p] ⊗ W*)^∨; injectivity on X ⟺ a lower bound on that motive's Ш¹ by dim X: self-defeating (Lemma D2(d)) |
| E(K)_tors, (E(K)/E(ℚ))_tors, H¹(Gal(K/ℚ), E(K)[p]), K fixed | restriction / inflation–restriction / corestriction | restriction is injective and factors through G_S; the map is defined on the zero subgroup; F reached is not independent |
| Sel_p / Ш of a fixed isogenous E′ or fixed twist E^D | φ_*; or res to ℚ(√D) then project | F = Ш(E′) ≅ Ш(E)[p], not independent; the twist by χ_D kills every G_ℚ-map E[p] → E^D[p] |

**The common failure (Lemma D2, extending K-LOC from Ш² = 0 to all first-order receptacles):** every first-order cup-product map from X_{p,a,b} is (α) zero, (β) defined on the zero subgroup, (γ) injective but into Ш of an object containing E, or (δ) into a p-dependent Ш² of a motive not containing E, where injectivity is equivalent to a lower bound on that motive's Ш¹. In case (δ) a fixed finite F bounds the receptacle only by making the map vanish, so "X injects into F[p]" restates X = 0. **Scoped conclusion: the named sufficient shape cannot be realized by first-order cup-product maps with any auxiliary motive, fixed or p-dependent.** Not excluded: higher-order operations into S₀^∨ (lane B: also dead on the seed at first order), and geometric surjections from a fixed F onto X (visibility; by SZ the receiver contains E and the statement is equivalent to the target).

**What would fix it:** a proved Ш-transfer E → M* valid at every p outside a fixed finite set, i.e. dim Ш¹_S(M*) ≥ dim Ш(E)[p] for one auxiliary M* whose Ш¹ is independently bounded. None is on record; Agashe–Stein visibility supplies it only at level N·ℓ with ℓ depending on p.

## 6. What this changes in the map

- §13.3 shapes: (a), (b) and (d) are now **exhausted at first order** (lanes A, B, D); the Codex 'S' relation is a generator bound, not a relation (lane C, Lemma 1). (a) is exhausted at first order for the seed: the only non-crystalline twist-0 class available (Hida tangent) gives an alternating pairing that cannot see the excess (lane A, L4/L9); fixed auxiliary sets give no classes (L6). Shape (b) with E[p]-entries only is dead by twist (lane B Lemma 2–3); with a θ or ad⁰ entry it reduces to the shape-(a) functionals and is undefined on the seed's S₀ because the cyclotomic height is nonzero there (lane B).
- New derived facts to bank: lane A L4 (alternating), L5 (Flach = β_z + c·h_θ), L6, L8; lane B Lemma 0 (no anomalous primes, uniform), Lemma 2–3 (Massey twist formula), Lemma 6 (indeterminacy), and the numerical fact h^(1)(x₀,x₀) ≠ 0 for all good ordinary p ≤ 200.
- Frontier statement unchanged: **C_p ≠ 0 for almost all p** (Codex), equivalently h²(G_S, E[p]) ≤ 2 cofinitely. Current known frontier; not "all that remains."
- **Sharpest statement of what the four lanes together establish (scoped):** every first-order cohomological operation with E[p]-coefficients available on the seed — cup products with fixed or Hida/adjoint classes, Massey products, Bockstein/Cassels–Tate pairings, receptacle maps into any auxiliary motive — is either twist-wrong, zero on S₀, defined on the zero subgroup, or equivalent to the target. The two excess countermodels (Ш[p^∞] = (ℚ_p/ℤ_p)² and Ш[p^∞] = (ℤ/p)² with the Cassels–Tate pattern) pass every test these constructions can perform (lane B Lemma 7, lane A L9). The only invariant on record that separates them from the target is Kato's per-prime unit condition λ(L_p mod p) = 2 (the T²-coefficient of the p-adic L-function a unit), which under p-adic BSD equals a unit times #Ш·Reg_p·Tam/tors², and Reg_p ≡ 0 mod p does occur on the seed (p = 17). **So the uniform step, as far as these architectures go, is the statement "λ_p = 2 for cofinitely many p" — a leading-term uniformity, not a cohomological one.** What is missing is a new global object (lane B F2: a space of known dimension ≤ 1 paired perfectly with S₀ for a p-independent reason), not a new operation on the old objects.

## 7. Process record (so this is not repeated)

- 10-02→03: six toy stages of the K167 plectic evaluator were run and passed (A-1, Revised0, R0-patch, A, B with c = 1, C-small SEED_SCALING_NOT_ESTABLISHED); endpoint effect of the whole route was finiteness at one bad prime. **Frozen** by the user and Pro 6; Claude's error was running it instead of refusing on endpoint grounds. Rule now in memory: state the best-case endpoint effect before launching anything.
- 10-03: the uniform-step attack (lanes A–D) is the only live work. Best-case endpoint effect: FIN progress. Realized so far: two precise first failures that close shapes (a) and (b) at first order, and the new nondegeneracy fact of the mod-p cyclotomic height on S₀.

FIN, ORDER9 and Q36 are unchanged.
