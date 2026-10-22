# Independent desk review of Codex's Stage-A derivation (Claude, Opus 5.5, 2026-10-07)

**Reviewed.** Lab bb6ed896:
- `work/returns/BSD_CURRENT_STATE_OBSTRUCTION_PUSH_CODEX_2026-10-06/STAGE_A_DERIVATION.md`;
- the companions `NEXT_ARITHMETIC_STEP.md` and `REPORT.md` §4.

**Verdict: `SUPPORTED_AT_DESK_LEVEL`.**
- The structural argument for ker[S_p → Hom(D^W, S_p^*)] = W_p holds as written.
- I re-derived every step in the list below except the two items in "Not verified here". Those are named targets for a full audit.
- This review does not upgrade the derivation to an audited theorem. It is not a bound on Ш.

## Steps re-derived (agree)

1. **Global primitive.** For x, y ∈ S_p, the class x ∪_e y ∈ H²(ℚ, μ_p) = Br(ℚ)[p] is locally zero at every place, because Kummer conditions are maximal isotropic. By Brauer–Hasse–Noether it is globally zero, so du = x ∪_e y with u a GLOBAL cochain. This avoids the 09-28 U22 error, where local primitives were used as global ones.
2. **Local vanishing at a deformation prime.** At q with ρ(Frob_q) = −I:
   - H⁰(ℚ_q, V) = 0;
   - H²(ℚ_q, V) = 0 by Weil self-duality;
   - H¹(ℚ_q, V) = 0 by the local Euler characteristic;
   - the same holds for M_λ through its filtration.

   So the zero local condition at q is forced and exact.
3. **Local splitting at Σ / Π.** For q split in R = ℚ(μ_p, a^{1/p} : a ∈ Π), each a ∈ Π is a p-th power mod q, so λ_q(Frob_a) = 0. At ∞, λ_q(−1) = 0 because −1 has order 2 and p is odd. So M_λ splits locally at Π and the direct-sum Kummer condition is exact there.
4. **The local evaluation.**
   - x|_{G_q} = dA with A = (ρ(γ)−1)^{−1}x(γ).
   - (u − A ∪ y)|_{G_q} is a cocycle, since d(u − A∪y) = x∪y − dA∪y = 0. It is unramified, since u factors through G_{ℚ,Π} and q ∉ Π.
   - The local invariant of λ_q ∪ (that class) is c_q·z_γ(x,y), with c_q ∈ k^× set by the choice of generator of λ_q (tame character evaluated on μ_p ⊂ F_q^×).
   - Only q contributes: λ vanishes at Π, and other places are unramified with zero invariant.
5. **Field intersection.** K = ℚ(E[p]) has Gal(K/ℚ(μ_p)) = SL₂(F_p), which is perfect for p ≥ 5, while R/ℚ(μ_p) is abelian. So K ∩ R = ℚ(μ_p), and γ with ρ(γ) = −I, trivial on R, exists (det(−I) = 1).
6. **Commutator shift.**
   - For v, w ∈ J = ker ρ ⊂ G_{ℚ(μ_p)}, and c = [v, w], c fixes R, V and μ_p, and x_i(c) = 0.
   - On J, u_ij(gh) = u_ij(g) + u_ij(h) − e(x_i(g), x_j(h)), which gives (F): u_ij(c) = −e(x_i(v), x_j(w)) + e(x_i(w), x_j(v)).
   - x_i(γc) = x_i(γ), so A_i is unchanged. u_ij(γc) = u_ij(γ) + u_ij(c), because γ acts trivially on μ_p. (A∪y)(γc) = (A∪y)(γ).
   - Hence z_{γc} − z_γ = u(c).
7. **Matrix units.**
   - The joint evaluation J ↠ V^s holds (H¹(GL₂(F_p), V) = 0, so restrictions are independent; V^s is semisimple and End = k). So x_i(v), x_i(w) can be prescribed independently.
   - Diagonal case: e(e₁,e₂) = 1 gives −2E_ii.
   - Off-diagonal case: −(E_ij + E_ji).
   - These span Sym² since p is odd. Signs and the scalars c_q do not affect the span.
8. **Chebotarev with a marked representative.** z_γ depends on the element γ, not only on its class; the pairing b_λ itself is canonical. Choosing the place above q realizes the prescribed element, so this is fine.
9. **From (C) to (A).** The map λ ↦ b_λ is linear (Baer sum), so its image is a subspace containing Sym²(S^*).
   - For x ∉ W, take φ ∈ W^⊥ with φ(x) ≠ 0. Then φ⊗φ = b_λ for some λ ∈ D, and λ ∈ D^W. This uses the vector-valued kernel b_λ(κ(P_i), ·) = 0.
   - b_λ(x, ·) = φ(x)φ ≠ 0.
   - No complement or basis of S/W defines the map.

## Not verified here: the targets for a full audit

- **Morgan–Smith.** arXiv 2103.08530 (v3, 2023-02-08) is confirmed to exist. Its abstract matches the use made of it: the pairing Sel(M₂) × Sel(M₁^∨) → ℚ/ℤ, with kernels equal to the images of Sel(M) and Sel(M^∨).
  - Still to check: the exact Definition 1.1 exactness conditions for these local conditions;
  - the Definition 3.2 cochain normalization behind (D)/(E);
  - Proposition 4.4 (Baer linearity) with these local conditions.
- **Symmetry of b_λ.** If b_λ is symmetric, then {b_λ : λ ∈ D^W} gives exactly the symmetric forms on S/W ≅ Ш[p]. Worth stating: this is a structure statement, not a bound.

## Corrections from Codex accepted (they affect my earlier notes)

- **The division fields differ.** ℚ(M_E[p]) = ℚ(E[p], p⁻¹P₁, p⁻¹P₂) is NOT the record's class-group receiver field, which is larger.
  - This corrects the field equality in both 1-motive returns, in my checks of them, and in pre-check 3 of the OpenAI package (revision 1).
  - Theorem 1, Sel(ℚ,M_E)(p) ≅ Ш[p], does not use that equality and is unaffected.
  - Corrected pre-check 3: with full Kummer image (G2 §6), inflation–restriction gives ker(H¹(ℚ,V) → H¹(ℚ(M_E[p]),V)) = W, so restriction to ℚ(M_E[p]) separates S/W.
- **Restriction is not deformation obstruction.** Split-prime restriction separates classes, but it is not a first-order lifting obstruction. Codex's construction (Frobenius −I primes; secondary cochain value; generalized Cassels–Tate) is the deformation-theoretic statement that Stage A asks for.
- **One-sided detectors.** A single known-good false alarm (p = 17) does not refute a one-sided detector. The real objection to a wild-regulator index in a FIXED A_E is that the regulator-divisible primes are expected to be infinite (heuristic, Σ1/p). My `WILD_REGULATOR` wording in the OpenAI package (revision 1) is sharpened accordingly in revision 2.

## Next-step note (NEXT_ARITHMETIC_STEP.md): checked

- **The character.** χ(t) = 1 + tλ + (t²/2)λ² (mod t³) is a character for additive λ, verified by expansion. μ(gh) = μ(g) + μ(h) + λ(g)λ(h) holds.
- **(L2)**, d b_i = −λ∪a_i − μ∪c_i, is the correct second-order equation.
- **The formal example.** D(t) = diag(t²I₂, tI₂) correctly shows that a first-order kernel W need not give generic sections.

FIN, ORDER9 and Q36 are unchanged.
