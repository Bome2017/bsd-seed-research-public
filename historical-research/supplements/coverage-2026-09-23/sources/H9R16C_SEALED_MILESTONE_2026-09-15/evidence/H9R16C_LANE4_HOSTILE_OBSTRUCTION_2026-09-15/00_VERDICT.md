# 00 — Verdict, Lane 4 (hostile review of H9R16-C)

Date: 2026-09-15. Sources were read from page images (06). H9R15 not reopened; H9R16-A/B taken as closed; nothing downstream assumed.

## Result in one paragraph

H9R16-C is **not killed**, but the square **as frozen is not well-typed**, for two independent reasons proved here.
(1) The only explicit "dagger/MRS object" in the checkpoint is A_r^† := I_r^† ⊗_Z J_r (H9R8/H9R12). Its Tate module has Z_p-rank
|G_r|·2g, whereas BCPV's dagger module M^† := M ⊗_{Z_p[G_r]} Z_p[G_r]^† has rank 2g (MRS Thm 2.1/2.2(iii); BCPV Def 4.6). On the
invariant subvariety that would repair it, the frozen transition s_r⊗ϖ_* is p^3·ϖ_*, while DR22 L2.8 has no constant.
(2) The A_r-modified coefficient-retaining finite point is **not** in any dagger-only receptacle over Q(μ_p). A_r = W_{N_gp^r}^{-1}(U'_p)^r
is defined only over Q(μ_{Np^r}), and Hida's conjugation law W^σ = <z>W applies to it. The p-part auxiliary twists cancel exactly,
but a tame diamond twist survives: σ∘Φ̄^mod_r = <m_σ>^{1/2}_{(1)}<n_σ>_{(1)}∘Φ̄^mod_r∘R(<n_σ>). On the g-branch it acts by ε_g^{(t)}, which
contains η_{K/Q} ≠ 1 in the Castella–Hsieh case. BCPV absorb the same twist on the étale side only through g^c = g⊗ε_g^{-1} ((1.6)–(1.7)).
Side findings: BCPV (4.9)'s constant 1/p makes (4.8) commute only up to p^2 (correct: 1/p^3). A literal cyclotomic
corestriction on one vertical against descent on the other is off by p per level. Building τ^MW from Hida's w-twisted π^r_s does not
match BCPV's untwisted ϖ_{1,*} tower without two extra W-conjugations. Kummer injectivity, p-completion, ⊗Q_p, g^c direction and a
Q-rational central diamond δ_r are all harmless under stated conditions.

## Classification of every stress point (details 03 §11)

TYPE_MISMATCH: receptacle Tate module (§1); dagger-only receptacle vs A_r-point (§2).
FALSE_AS_PRINTED: BCPV (4.9) constant (§3). FALSE if literal: Cor vs descent (§4).
NOT_PRINTED: model/U'↔U* dictionary (§5); operator-level coefficient transition (§7); finite global Kummer identity (§10).
NEW_THEOREM_REQUIRED: (★_r), the operator-level modified-pairing/degeneracy compatibility with explicit constant (04 §4).
PASS: Kummer injectivity (§6); g^c direction (§8); Q-rational central δ_r (§9).

LANE = 4 — hostile review: try to break H9R16-C (point-transition/Kummer square)
STATUS = H9R16C_NOT_KILLED; FROZEN_SQUARE_TYPE_OBSTRUCTED (two TYPE_MISMATCHes); RETYPED_SQUARE_WELL_TYPED_AND_OPEN
PROVED = (i) rank_{Z_p} T_p(I_r^†⊗_Z J_r) = |G_r|·2g ≠ 2g = rank (T_pJ_r)^† [MRS T2.1, T2.2(iii); BCPV Def 4.6]; (ii) on G_r-invariants s_r⊗ϖ_* = p^3·ϖ_* vs DR22 L2.8 (no constant); (iii) twisted descent over Q(μ_p): σ∘Φ̄^mod_r = <m_σ>^{1/2}_{(1)}<n_σ>_{(1)}∘Φ̄^mod_r∘R(<n_σ>), p-part auxiliary twists cancel, tame twist ε_g^{(t)} survives [Hida p.15; BCPV (4.1)–(4.4), L4.2(ii); H9R16-A/B balance]; (iv) BCPV (4.9) with 1/p commutes with (4.8) only up to p^2; (v) Cor_{F_{r+1}/F_r} vs descent+p_{r+1,r} differ by p; (vi) Kummer injectivity survives p-completion, ⊗Q_p and fixed-base descent when coefficients enter via Hom
REFUTED = H9R9 "DAGGER_TRANSITION_VS_MRS = NO TYPE MISMATCH AFTER CONTRACTION" for A_r^† := I_r^†⊗_Z J_r; the implicit claim that a dagger-only fixed-base receptacle over Q(μ_p) contains the A_r-modified coefficient-retaining point when ε_g^{(t)} ≠ 1; BCPV (4.9)'s constant as printed. NOT refuted: the route, the balance identity, Kummer injectivity
FIRST_EXACT_UNPROVED_STATEMENT = (★_r): on e'_ord H^1_et(X̄_1(N_gp^{r+1}),Z_p(1)), ϖ_1^*∘W_{N_gp^r}^{-1}∘(U'_p)^r∘ϖ_{1,*} = u_r·W_{N_gp^{r+1}}^{-1}∘(U'_p)^{r+1} for an explicit u_r ∈ Z_p[diamonds] (possibly times a power of p, to be matched against DR22 L2.8), which with (K_r) [finite operator-level Kummer realization, formal] and BCPV Cor 4.11 yields the typed tower relation (T♮_r): ϖ_{1,*}(U'_p)^{-(r+1)}Φ̄^mod_{r+1} = δ♮_r(U'_p)^{-r}Φ̄^mod_r∘res^bal_{r+1,r} in Hom(B^bal_{r+1}, Ĵ^{(1)}_r(F'_{r+1})^{ord}) on the tame-and-dagger-twisted receptacle P^♮ of 04 §1
TYPE_CHECK = FROZEN SQUARE FAILS (P_r^{tr,†}, T_r^{tr,†} undefined; only explicit receptacle has wrong Tate module; dagger-only descent omits ε_g^{(t)}; "τ^MW: P_{r+1}→P_r" is not a map of Hom-modules since the carrier restriction goes B_{r+1}→B_r); RETYPED (T♮_r) on P^♮_r → H^1(Q(μ_p),T^♮_r) PASSES
NEW_ASSUMPTIONS = none beyond: BCPV's W_{Np^r}, W_{N_gp^r} obey the standard Atkin–Lehner conjugation law W^σ = <z>W up to Q-rational diamonds (source-evidenced by BCPV L4.2(ii) and the Z_p[Δ_{N_hp^r}] target of (1.6); literal normalization is Lane 1's C1)
COUNTEREXAMPLE_OR_OBSTRUCTION = TYPE obstruction, repairable: σ ∈ Gal(Q(μ_{Np^r})/Q(μ_{p^r})) with n_σ ≠ 1 acts on the g-branch projection of Φ̄^mod_r by ε_g^{(t)}(n_σ) (η_{K/Q}(n_σ) = −1 possible in Castella–Hsieh), so Φ̄^mod_r ∉ (dagger-only receptacle)(Q(μ_p)); and rank T_p(I_r^†⊗_Z J_r) = p^{3(r−1)}·2g ≠ 2g
NEXT_SMALLEST_TEST = compute u_r in (★_1) (r = 1→2) on e'_ord H^1 of X_1(N_gp^2): decide whether ϖ_2^*(U'_p)ϖ_{1,*} = u·(U'_p)^2 holds with u a diamond unit or with an extra power of p (compare Hida (6.4) π^r_s∘π^*_{r,s} = p^{s−r}U(p^{s−r})), and independently re-verify the p^2 constant defect of BCPV (4.9)
ARISTOTLE_READY = NO
STOP_ROUTE = NO
