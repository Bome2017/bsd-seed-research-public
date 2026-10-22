# 03 — Derivation or obstruction (Lane 3)

## 0. Answer

    EXISTING_THEOREM_CLOSES_C = NO

No consulted primary source states H9R16-C. No source proves a theorem whose hypotheses cover a
fixed-base dagger/MRS point/Kummer transition square for contracted Chow–Heegner points.

The square does assemble from printed pieces plus three formal lemmas (F1–F3 below). Those
lemmas are standard, but none of the consulted sources prints them.

**Revision v2, after operator input (verified in the local copies).** The étale compatibility of the
modified pairing along the tower (statement E) is **PRINTED BY REFERENCE** in KLZ17's convention:
- KLZ17 Thm 7.2.3(v): a canonical perfect Λ_D-pairing on H^1_ord,par(Np^∞), existing before any
  arithmetic specialization (proof = Oht00 Cor 1.3.8, 2.3.6);
- the proof of KLZ17 Prop 10.1.1: this pairing involves the factor W_{Np^r}^{-1}∘(U'_p)^r on
  cohomology, and U_p^r∘W_{Np^r}^{-1} on forms;
- KLZ17 Rem 7.4.1 and Lemma 7.4.2: Ohta's τ_r equals W_{Np^r}^{-1} up to signs.

BSV22 (103), (104), (109) and (114) are verified, **with a scope correction**: (109) is weight
specialization at the fixed level Γ_1(N)∩Γ_0(p), for integer weights k ∈ U_f^cl. It does not reach
p-power levels or wild characters.

After this revision, the delta between the literature and C is two unprinted statements that are
expected to be formal — **E′** (dagger / group-ring packaging of the A_r-contraction) and **D4**
(finite-level Abel–Jacobi identity for the packaged contracted points), both in 04 — plus a
normalization transport check (N1–N4 in 04). The v1 text of §3 and §5 below is kept for custody;
where it conflicts with this block, this block governs.

No FALSE statement and no genuinely incompatible normalization was found in the consulted
sources. One TYPE_MISMATCH hazard (T9) and several citation defects in BCPV are recorded in §4.

---

## 1. Nearest theorems, ranked by how much of C they carry

1. **Howard 2007, §2.2** — eqs (6)–(9), the twisted Kummer map, Def 2.2.3, Lemma 2.2.4. This is the
   same architecture as C:
   - a *fixed-base twisted point module* H^0(H_c, J_s(L_{c,s})^ord ⊗ ζ_s), obtained by corestriction
     from the varying fields L_{c,s} = H_{cp^s}(μ_{p^s}) (eq. (7));
   - a twisted Kummer map equivariant for Hecke and Galois;
   - the plain Albanese transition α_*, with lim U_p^{-s} normalization;
   - Kummer naturality used as formal: Kum_s(α_* x) = α_* Kum_{s+1}(x).

   *Delta.* Howard's points are Heegner points on one Jacobian tower. His point-level distribution
   identity (11)–(12) comes from CM theory and is proved **before** applying Kummer. His twist Θ is
   Hecke-valued on a single tower, not BCPV's triple-diamond G_r dagger. He performs no contraction,
   and uses twisted H^0 rather than an MRS twist (the two agree at finite level by MRS Thm 1.4 —
   lane-3 remark). BCPV Rem 4.9 and Rem 4.16 point to exactly this analogy.

2. **Hida, HidaC §5–6 and HidaL §5–6.** Q-rational, Hecke-equivariant projective systems of modular
   Jacobians, in two isomorphic forms: the untwisted starred Albanese system and the w-twisted
   system π^{sr}. They give p-completed Mordell–Weil groups over a **fixed** base k, the Kummer
   injection (HidaC Lemma 2.1), Kummer diagrams that force isomorphisms of quotient towers
   (HidaC (6.2)–(6.3), Lemma 6.2; HidaL (6.4)–(6.5), Lemma 6.1), vanishing of subvariety towers
   (HidaC Prop 6.4), and control theorems (HidaC Thm 9.2, 10.1).

   *Delta.* No Weil restriction, no cyclotomic or dagger lattice, no contraction. Hida uses the
   μ-model. His control hypotheses (principal P, good reduction over Z_p[μ_{p^∞}], finite
   Sel(A_{P_0})^ord) are stated for fixed k, so they give no Mordell–Weil control for the twisted
   tower.

3. **MRS** Def 1.1, Thm 1.4, Prop 1.6, Cor 1.7(ii), Thm 1.8, Thm 2.1, Thm 2.2(iii), Prop 4.1,
   Rem 5.11. These supply the receptacle and its functoriality.

   *Delta.* No Kummer map or Galois cohomology; finite Galois image only; coefficients Z.

4. **BCPV** Lemma 4.10, Cor 4.11, Def 4.12–4.14, (4.13)–(4.14), with **DR22** Lemma 2.4, 2.6, 2.8.
   These give the Chow-level ordinary transition, the uncontracted étale transition with dagger
   descent to Q(μ_p) and to Q, and the Λ-adic big class with its adjoint trace.

   *Delta.* U'_p is inverted only on étale cohomology. The *contracted* transition appears only after
   specialization. No points.

5. **Conventions and the twisted pairing:** KLZ17 Def 2.4.1–2.5.4, Prop 2.4.5, Prop 7.2.1,
   Thm 7.2.3, §7.4, Prop 10.1.1–10.1.2; Cais Prop 2.3.6, Prop 5.2.4; BSV22 §2.3.1, (65)–(68),
   (114), proof of Lemma 6.1, §7.2, (157); Ohta (1.1.5), (1.5.4), (2.2.3), (3.3.4)–(3.3.6), (4.2.4).

---

## 2. What is formal

The lemmas in this section are lane-3 derivations of standard facts. They are **not printed** in the
consulted sources; Milne 1972 and Brown's *Cohomology of Groups* were not consulted.

Notation: K_0 = Q(μ_p), L = Q(μ_{p^r}), J = J_r (a Jacobian over Q). I is a finitely generated free
Z-module with continuous right G_{K_0}-action, trivial on G_L. For a commutative group scheme A,
Â(K_0) := A(K_0) ⊗ Z_p.

**Lemma F1 (Kummer naturality over a fixed base).** Let φ : A → B be a homomorphism of abelian
varieties over a number field k. Then

    δ_B ∘ φ = (T_pφ)_* ∘ δ_A :  Â(k) → H^1(k, T_pB),

where δ is the p-adic Kummer map of HidaC Lemma 2.1.

*Proof.* φ commutes with multiplication by p^n, so it maps the Kummer sequence
0 → A[p^n] → A → A → 0 over k̄ to the one for B. Connecting homomorphisms are natural. Pass to the
limit, using lim_n H^1(k, A[p^n]) = H^1(k, T_pA) (HidaC Lemma 8.2 / [CNF 2.7.6]). □

**Lemma F2 (MRS twists: points, Tate modules, Kummer).** Put A^I := I ⊗_Z J over K_0.

1. (Points.) Â^I(K_0) ≅ (I ⊗ Ĵ(L))^{Gal(L/K_0)}. This is MRS Thm 1.4 tensored with Z_p; invariants of
   a finite group are a kernel, and Z_p is flat over Z.
2. (Tate module.) T_p(A^I) ≅ I ⊗ T_p(J), with γ acting as γ^{-1} ⊗ γ (MRS Thm 2.2(iii)).
3. (Kummer injection.) A^I is an abelian variety (MRS Thm 2.1(i)–(ii)), so HidaC Lemma 2.1 gives an
   injection δ : Â^I(K_0) ↪ H^1(K_0, I ⊗ T_pJ).
4. (Functoriality.) For f ∈ Hom_{Z[G_{K_0}]}(I, I') and φ ∈ Hom_Q(J, J') — e.g. Hecke
   correspondences or Alb(ϖ_1) — the map f ⊗ φ is a K_0-homomorphism (MRS Prop 1.6(ii),
   Cor 1.7(ii), Thm 1.8), and δ ∘ (f⊗φ) = (f ⊗ T_pφ)_* ∘ δ by F1.
5. (Ordinary operators.) A Hecke operator h ∈ h_r(Z_p) acts on I ⊗ Ĵ(L) through the second factor
   and commutes with the Gal(L/K_0)-action. So e, e* and the unit U'_p ∈ (e'h_r)^× act on Â^I(K_0),
   compatibly with δ. (U'_p is a unit on the e'-part because e' is defined as the idempotent cutting
   out the part where U'_p is invertible, h_r being finite over Z_p.) □

**Lemma F3 (Weil restriction, Shapiro, norms).** Take I = Z[Gal(L/K_0)] with its regular action.

1. I ⊗ J ≅ Res^L_{K_0}(J_L) (MRS Prop 4.1), and T_p(I⊗J) ≅ Ind_{G_L}^{G_{K_0}} T_pJ (MRS Thm 2.2(iii)).
2. Let Sh : H^1(K_0, Ind T_pJ) ≅ H^1(L, T_pJ) be the Shapiro isomorphism. Then
   Sh ∘ δ_{Res} = δ_{J/L} under (Res J)(K_0) = J(L).
3. For K_0 ⊆ F ⊆ L, the morphism R_{L/F,J} : Res^L_{K_0}J ↠ Res^F_{K_0}J induced by
   Z[Gal(L/K_0)] ↠ Z[Gal(F/K_0)] (MRS Rem 5.11) is the norm N_{L/F} on points and corestriction
   Cor_{L/F} on H^1.

*Proof sketch.* Sh is restriction to G_L followed by the G_L-equivariant evaluation Ind T → T. The
MRS isomorphism of Prop 4.1 comes with the L-morphism η = p_1 ∘ φ^{-1} : (I⊗J)_L → J_L; η induces
evaluation on Tate modules and the identification (4.1) on points. F1 applied to η over L, together
with the compatibility of restriction with Kummer maps, gives (2). Part (3) is the standard
compatibility of Shapiro isomorphisms with the coefficient projection Ind_L → Ind_F. □

**Consequence F4 (when the square is formal).** Let τ_r^MW be any K_0-homomorphism between the
finite-level twists — for example s_r ⊗ Alb(ϖ_1) in the point model, or s_r ⊗ π^{sr} after
transport to that model. Define τ_r^et as its Tate-module map, read through Shapiro where needed.
Then Kum ∘ τ_r^MW = τ_r^et ∘ Kum, by F1–F3. **So the square in C is formal for this τ_r^et.**
Everything non-formal in C is concentrated in one question: does this τ_r^et agree, on the
relevant classes, with BCPV's normalized étale transition after contraction? Equivalently, is
τ_r^et(Kum P_{r+1}^{tr,†}) = Kum P_r^{tr,†}? That is item D3 in §3.

**On s_r (hazard T2).** Z[G_{r+1}] → Z[G_r] splits into two different operations. Along the diagonal
Galois direction (the image of Gal(Q(μ_{p^{r+1}})/K_0)) it is a norm/corestriction, covered by F3.
Along the complementary diamond directions, whose kernel has order p^2 per level step, it is a
Galois-equivariant summation of lattice coordinates, covered by F2(4). Both are formal, but they are
different maps. Neither is a Shapiro corestriction for the modular level change, and the three
operations must not be merged into one untyped arrow.

---

## 3. The exact delta (what no consulted source prints)

**D1 — Formal lemmas F1–F3.** NOT_PRINTED in the consulted sources, but formal (§2).

**D2 — A K_0-rational point transition exists.**
- In the point model (BCPV and KLZ17 conventions), Alb(ϖ_1) is Q-rational.
- Its Tate-module map is the étale trace. Ohta (3.3.4) prints this for generalized Jacobians (in
  dual form); the limit convention is KLZ17 Thm 4.5.1(1), and BCPV Def 4.12 uses the same trace.
- For p dividing the level, compatibility of ϖ_{1,*} with U'_p is printed on cohomology
  (KLZ17 Prop 7.2.1(2); BSV22 §4.3: "the maps pr_{1*} are Hecke-equivariant"). On Jacobians it is
  the same correspondence identity (lane-3 remark).
- Point-level inversion of U'_p is available on p-completed ordinary parts (HidaC §5; F2(5)).

Class: PRINTED pieces + formal transport.

**D3 — Unspecialized finite-level compatibility of the contracted dagger classes.** This is the étale
identity E of 04: the modified pairing is compatible with ϖ_{1,*} on the two auxiliary factors, up to
one extra U'_p, a diamond sum over the new p-part, and an explicit central unit c_r. Its consequence
is τ_r^et(Contr^mod_{r+1} Δ^ét_{r+1}) = (normalization) · Contr^mod_r Δ^ét_r in H^1(K_0, T_r^{tr,†}).

Printed only as:
- the de Rham, local analogue in Cais's w_r convention (proof of Cais Prop 5.2.4, displayed chain);
- Λ-adic existence (KLZ17 Thm 7.2.3(v), proved via Oht00 Cor 1.3.8, 2.3.6 — not consulted — plus the
  KLZ17 Prop 10.1.1 proof remark on W_{Np^r}^{-1}(U'_p)^r);
- after specialization at (κ,λ) ∈ A_r^{(2)} (BCPV (4.14), which asserts "compatibility of the
  Poincaré duality pairing with degeneracy maps" without stating it).

Class, v1: NOT_PRINTED at the needed level. **Class, v2 (governs): PRINTED BY REFERENCE** —
KLZ17 Thm 7.2.3(v), the proof of Prop 10.1.1, and Rem 7.4.1 / Lemma 7.4.2, with the finite-level
formula and sign in Oht00 (not consulted). In KLZ17's normalization c_r = 1 up to sign. What
remains is the packaging statement E′ and D4 (04).

**D4 — Finite-level Abel–Jacobi identity** Kum(P_r^{tr,†}) = Contr^mod_r(cl_1 Δ_r^ord), dagger-packaged
and unspecialized. BCPV use Hecke-equivariance of cl_1 in the proof of Cor 4.11 and prove the
specialized Lemma 4.18. Étale Abel–Jacobi functoriality for algebraic correspondences is standard,
but it is not a numbered statement in the consulted sources (compare H9R10).
Class: NOT_PRINTED (formal).

**D5 — The W normalization.** BCPV never define W.

| Source | Model | Printed W data |
|---|---|---|
| KLZ17 Def 2.5.2–2.5.4, Rem 2.5.3 | point | W_Q over Z[1/N,ζ_Q]; W_Q^2 = [[Q,0],[0,Q]]⟨Q⟩_{N/Q}⟨−1⟩_Q; ⟨d⟩_Q W_Q = W_Q⟨d^{-1}⟩_Q; W_{QQ'} = ⟨Q'⟩_Q W_Q W_{Q'}; W^{AL} = W⟨−1⟩_Q⟨Q^{-1}⟩_{N/Q}. Galois twist: NOT printed. Level identities (N → Np) in the proof of Prop 10.1.1. |
| BSV22 §2.3.1, (65)–(68) | point | U_p w_p = w_p U'_p ⟨p⟩_N; U_p w_{Np} = w_{Np} U'_p; w_p is G_Q-equivariant, w_{Np} is G_{Q(μ_N)}-equivariant (on their coefficient modules) |
| Cais Prop 2.3.6 | Katz–Mazur balanced, over Q_p | (γ^*w_r)^γ = γ w_r⟨χ(γ)⟩^{-1}⟨a(γ)⟩_N^{-1}; w_r^2 = ⟨−p^r⟩_N⟨−N⟩; ρw_{r+1} = w_rσ; σw_{r+1} = ⟨p⟩_N w_r ρ |
| HidaC §6, HidaL §5 | μ-type | w_r^σ = ⟨z⟩w_r = w_r⟨z^{-1}⟩; w_r^2 = 1; π^{sr} = w_r π_{s,r,*} w_s over Q |
| Ohta (4.2.4), (1.5.3)–(1.5.4) | canonical model, i∞ rational | w_r^σ = w_r T(a,a) = T*(a,a) w_r; τ_r intertwines T and T* on forms |

The most plausible reading of BCPV's W_{N_h p^r} is KLZ17 Def 2.5.4 with Q = N_h p^r. This is
PLAUSIBLE, NOT_PRINTED. Every candidate central discrepancy printed above is a diamond or scalar
matrix, possibly with a sign: central in the Hecke algebra, and Q-rational when tame. Tame diamonds
act on a Hida branch through nebentype values. p-part diamonds are exactly the G_r directions, so
they interact with the dagger twist. Lane 3 asserts no value of δ_r; that is lane 1's computation.

---

## 4. Source-level findings and hazards

**H1 (T9) — the w-twisted transition versus the untwisted one.**
- HidaC §5: the untwisted Albanese system {Ĵ_s, π_{s,r,*}} is starred and co-ordinary ((5.2)). It is
  isomorphic to the w-twisted ordinary system through i, with i∘T(n) = T*(n)∘i.
- That isomorphism is realized levelwise by w_s, and w_s^σ = ⟨z⟩w_s, so it is not K_0-rational.
- BCPV's étale tower uses ϖ_{1,*} with primed operators (BCPV §1.1.8, Def 4.12; KLZ17 Prop 7.2.1).
- Matching that tower with one of Hida's two systems requires a change of moduli model (point model
  vs μ-model). That change is printed only for Λ-adic Galois modules (KLZ17 Thm 7.2.3 proof: twist
  by 1+k+ε_N).

Consequence: taking τ_r^MW := s_r ⊗ π^{sr} against BCPV's τ_r^et, **without** explicitly inserting the
levelwise w_s Galois twist, is a TYPE_MISMATCH hazard. The simpler route supported by the literature
(not a proof) stays in the point model with τ_r^MW := s_r ⊗ Alb(ϖ_1), with U'_p normalization on the
p-completed ordinary part. This needs no Hida w on the transition; W then enters only through A_r.

**H2 (T6) — subvariety towers vanish integrally** (HidaC (6.4), Prop 6.4). An integral point tower
must therefore live in the full ordinary Jacobian or a quotient tower (HidaC Lemma 6.2), with the
classical f-factor extracted only at the end. This agrees with the H9R16 ordering (steps 8–9). A
Q_p-linear tower is not killed this way, since multiplication by p is invertible on Q_p-vector
spaces.

**H3 (T1) — model mismatch.** BCPV, DR22, KLZ17 and BSV22 use the point model; Hida and Ohta use the
μ-type / i∞-rational model. The printed dictionary covers Λ-adic Galois modules only (KLZ17 Thm 7.2.3
proof; KLZ17 Rem 2.6.1). Transport of degeneracy maps, W, or Mordell–Weil points between the models is
NOT_PRINTED.

**H4 (T7) — two tame levels.** BCPV (4.4) uses W_{Np^r} at the common tame level, while (1.6) and A_r
use W_{N_h p^r} at the native level. How they relate under the tame pushforward of Def 4.13 is
NOT_PRINTED. KLZ17's relation W_{QQ'} = ⟨Q'⟩_Q W_Q W_{Q'} and BSV22's tame identities
w_N pr_p^* = ⟨(p,1)⟩ pr_p^* w_N and w_N pr_1^* = pr_1^* w_N are the nearest printed tools.

**H5 — citation defects in BCPV** (documentary; none is a mathematical error).
- Lemma 4.10 cites "[DR22] Lemma 2.5"; in arXiv v1 the distribution relation is **Lemma 2.4**.
- §1.1.9 and fn. 7 point to "[BSV22] between Prop 3.2 and Rem 3.3". In the consulted BSV22 version
  that passage contains no Atkin–Lehner operator; W appears in §2.3.1, §4.1.2, §7.2 and §8.2.
- (1.8)–(1.9) cite "[Oht99] Eq. 1.5.4". That equation is a slash-operator identity on modular forms;
  Ohta's Galois-twist statement for w_r is (4.2.4), and the transfer to étale cohomology is not in
  (1.5.4).

**H6 (T2) — G_r is not a Galois group.** See the note on s_r in §2.

**H7 — U'_p^{-1} and integrality.** BCPV invert U'_p only on étale cohomology (Def 4.12). Hida's e and
e* act on Ĵ_r(k), and U'_p is a unit on the e'-part (F2(5)). So the point-level ordinary inversion that
H9R12 relies on is available on p-completed ordinary parts, including MRS twists. This supports
H9R12 and contradicts nothing.

**H8 — BSV22 is a fixed-level construction.** It interpolates in weight at level Np (overconvergent
sheaves) and prints a Galois descent from Q(μ_p) to Q for the w'_p-twisted diagonal class ((157) and
following text). That is a fixed-level analogue of dagger descent, not a p-power tower.

---

## 5. Classification (the lane prompt's vocabulary)

| Item | Class |
|---|---|
| Kummer naturality for K_0-morphisms of MRS twists (F1, F2) | NOT_PRINTED (formal) |
| Shapiro and norm compatibility under Weil restriction (F3) | NOT_PRINTED (formal; Milne/Brown not consulted) |
| A K_0-rational τ_r^MW exists (point model) | PRINTED pieces + formal |
| "Hida's MW control applies to the MRS/cyclotomic point tower" | FALSE as a citation (hypotheses fix k); not needed for C |
| τ_r^MW := s_r⊗π^{sr} paired with BCPV τ_r^et without the w_s twist | TYPE_MISMATCH (hazard T9) |
| D3 / statement E (finite-level étale modified-pairing tower compatibility) | v1: NOT_PRINTED → **v2: PRINTED BY REFERENCE** (KLZ17 Thm 7.2.3(v) + Prop 10.1.1 proof; Oht00 not consulted) |
| E′ (dagger/group-ring packaging of the contraction) and D4 (finite-level Abel–Jacobi identity) | NOT_PRINTED (expected formal; see 04) |
| D4 (finite-level Abel–Jacobi identity for packaged contracted points) | NOT_PRINTED (formal) |
| D5 (BCPV's W: definition, Galois twist, degeneracy interchange) | NOT_PRINTED in BCPV; PRINTED elsewhere in five differing conventions |
| Any point-valued Chow–Heegner tower in the literature | NOT_PRINTED (title/abstract search negative; not proof of absence) |
| A FALSE mathematical statement, or a genuinely incompatible normalization | NONE FOUND |

---

## 6. Update after operator input (2026-09-15) — what was verified, and the scope correction

| Operator claim | Lane-3 check against the local source | Result |
|---|---|---|
| KLZ17 §7.2.3: a Λ-adic perfect ordinary pairing exists before specialization | KLZ17 v6 Thm 7.2.3(v): canonical perfect Λ_D-pairing on H^1_ord,par(Np^∞), Hecke self-adjoint, F^± orthogonal; proof = Oht00 Cor 1.3.8, 2.3.6 | **VERIFIED** |
| KLZ Rem 7.2.2 covers only the tame W_Q | Rem 7.2.2 discusses W_Q for Q ∥ N only | **VERIFIED** (distinction kept) |
| KLZ Rem 7.4.1: Ohta's τ_r = W_{Np^r}^{-1} up to signs; Lemma 7.4.2 uses ⟨α⟩_p∘U_p^r∘W_{Np^r}^{-1} | as stated | **VERIFIED** |
| The duality pairing contains W_{Np^r}^{-1}∘(U'_p)^r; the forms side uses U_p^r∘W_{Np^r}^{-1} | the proof of KLZ17 Prop 10.1.1 says exactly this (in a proof, not as a numbered statement) | **VERIFIED** |
| BSV22 (103)–(104): big perfect pairing | (103) ⟨,⟩_f : V(f)⊗V^*(f) → O_f is perfect, induced by det^*_{U_f} "(cf. [Oht00] and §4.3)"; (104) gives the ± restrictions. No W occurs in (103). | **VERIFIED** |
| BSV22 (109): exact specialization compatibility | ⟨x,y⟩_f(k) = ⟨ρ_k x, ρ_k y⟩_{f_k} for k ∈ U_f^cl = {k ∈ U_f∩Z : k ≥ 2, k ≡ k_o mod 2(p−1)}, with ρ_k landing in H^1_ét(Y_1(N,p), L_{k−2}(1)) | **VERIFIED, but scope is fixed level Np and integer weights.** Not a p-power-level statement. |
| BSV22 (114): w_{Np} intertwines U'_p, T'_ℓ, ⟨d⟩ with U_p, T_ℓ, ⟨d⟩^{-1} | the text before (114), and (114) itself | **VERIFIED** |
| "A recent exposition has (T_p^*)^r W_{Np^r} with a factor (Np^r)^{2−k}" | source not named or located | **NOT VERIFIED — not used** |

**Consequence for this lane.** The étale pairing tower compatibility is settled by reference in
KLZ17's convention. C itself is **not** upgraded. As the operator also notes, the point-level
pieces — the packaged contraction E′, the Abel–Jacobi identity D4, and Kummer injectivity applied to
constructed points — are logically separate. So is the transport of BCPV's W normalization (N1).

### 6.1 Post-verification check: KLZ17 §13 "Correction (November 2023)"

The arXiv v6 correction does three things:
- corrects the characterization of cuspidal branches (Def 7.5.1) and the congruence module I_a
  (Notation 7.7.1);
- in the proof of Prop 10.1.1 ("page 92"), replaces "space of Λ_D-adic cusp forms" with "modular forms
  (not necessarily cuspidal)";
- fixes a typo on p.93.

It does **not** alter the sentence that the duality pairing involves W_{Np^r}^{-1}∘(U'_p)^r, nor
Thm 7.2.3(v), Rem 7.4.1 or Lemma 7.4.2. The v2 status of E stands.

**Scope note.** Thm 7.2.3(v) is stated on *parabolic* cohomology H^1_ord,par. For non-Eisenstein
families M(f)^*_par = M(f)^* (KLZ17 Def 7.2.6), which BCPV's hypothesis (Irr) guarantees. The
correction's remark about CM families with an Eisenstein weight-one specialization (BDV22) does not
apply to a cuspidal p-regular CM weight-one point with irreducible residual representation. If (Irr)
failed for the actual Castella–Hsieh CM g-family at p, the parabolic-vs-full question would have to be
reopened — see lane 4 in 05.
