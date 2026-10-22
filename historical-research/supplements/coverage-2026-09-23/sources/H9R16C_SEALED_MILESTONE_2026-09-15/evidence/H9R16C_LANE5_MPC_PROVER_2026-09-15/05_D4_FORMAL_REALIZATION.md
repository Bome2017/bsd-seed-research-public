# 05 — D4: formal statement and proof on the corrected (type-B, tame-twisted) carrier

MPC is proved (03), so this file is live. D4 is stated for objects defined from BCPV's printed
constructions only. The identification of the point defined here with the H9R16-A/B packaged point
`P_r^{tr,†}` is a definitional comparison the referee must make (their text is not in this packet; 07 item R2).

## §1. The one external input (standard, not in the packet)

**(AJ-corr) Functoriality of the étale Abel–Jacobi map under algebraic correspondences.** Let `V, V'` be smooth
projective varieties over a number field `F'`, `𝒵 ∈ CH^{dim V' + c}(V × V')` a correspondence defined over `F'`,
`𝒵_* : CH^i_0(V)_{Z_p} → CH^{i+c}_0(V')_{Z_p}`, `z ↦ pr_{V',*}(pr_V^* z · 𝒵)`. Then for `z ∈ CH^i_0(V; F')`,

    cl_1(𝒵_* z) = [𝒵]_* cl_1(z)   in H^1(F', H^{2(i+c)−1}_ét(V̄', Z_p(i+c))),

where `[𝒵]_*` is induced by the cycle class of `𝒵` acting on cohomology (Künneth + cup product + pushforward).
Source: Jannsen, *Mixed motives and algebraic K-theory* (LNM 1400), §9 (the cycle-class / Abel–Jacobi maps are
morphisms of the correspondence categories); Nekovář, *p-adic Abel–Jacobi maps and p-adic heights* (2000), §1.
(Not in the packet; the referee should pin the exact numbered statement. BCPV themselves use the same principle
for `Π_{Z,*}` in Prop 6.2 via Daub's thesis Prop 2.3.5, de Rham side, and for the Hecke-equivariance of `cl_1` in the
proof of Cor 4.11.)

Special cases used: `𝒵` = graph of a finite morphism (pushforward/pullback compatibility), and `𝒵 = X_{14} × Γ`
with `Γ ⊂ X_2 × X_3` a correspondence on the curve.

## §2. Objects (all from BCPV §4, DR22 §2, KLZ17 §2.5; see 01)

* `X := X_r = X_1(Np^r)` over `Q`; `F' := Q(μ_{Np^r})`; `K_0 := Q(μ_p)`; `S := H^1_ét(X̄, Z_p)`, so
  `T_pJ = S(1)` and the Kummer map `Kum : J(F') ⊗ Z_p → H^1(F', S(1))`.
* `Δ_r^ord[d] ∈ CH^2_0(X^3; Q(μ_{p^r}))_{Z_p}` (BCPV (4.4)); `Δ^ét_r[d] := cl_1(Δ_r^ord[d])`; the packaged
  `Δ^ét_r[[a,b,c]] = Σ_{g ∈ G_r} Δ^ét_r[g·(a,b,c)] g` (BCPV (4.7)), a cocycle valued in
  `Hom_{Z_p[G_r]}(S^{⊗3}(1), Z_p[G_r]) ≅ S^{⊗3}(2)` (BCPV Rem 4.5(i)), descending to `H^1(K_0, S^{⊗3}(2)^†)` (BCPV Lemma 4.7).
* The auxiliary correspondence: `A := A_r = W_{Np^r}^{-1}(U'_p)^r`, an algebraic correspondence on `X` defined over `F'`
  (`U'_p` over `Q` — DR22 §1.3 / KLZ17 Def 2.4.4 — and `W_{Np^r}` over `F'`, KLZ17 Def 2.5.4). Let `Γ_A ⊂ X_2 × X_3`
  be its cycle, oriented so that `[Γ_A]_*` on `H^1` is `A` and the induced bilinear form is `(y_2, y_3) ↦ ⟨y_2, A y_3⟩`
  (Poincaré pairing composed with `A` on the second slot; this is BCPV (1.6) with `k = 0`). (Native level `N_g`:
  replace `X_2 × X_3` by `X_1(N_gp^r)^2` after the tame push-down of 04 §3; the statement is identical.)
* Chow-level contraction (BCPV §7.2 footnote / §6.3 with the diagonal `Z` replaced by `Γ_A`):
  `Π_A := X_{14} × Γ_A ⊂ X_1 × X_2 × X_3 × X_4`,   `Π_{A,*} : CH^2_0(X^3; F') → CH^1_0(X; F') = J(F')`,
  `Δ ↦ pr_{4,*}(Π_A · pr_{123}^* Δ)`.
* Étale contraction: `Contr^A : S^{⊗3}(2) → S(1)`, `y_1 ⊗ y_2 ⊗ y_3 ↦ ⟨y_2, A y_3⟩ · y_1` (after the Tate-twist bookkeeping
  `S(1) ⊗ S(1) → Z_p(1)`... i.e. `⟨,⟩ : S(1) ⊗ S(1) → H^2(X̄, Z_p(2)) ≅ Z_p(1)`; BCPV Def 4.5 / DR22 (2.17) use exactly
  this normalization, values `Z_p` after the twist). It induces `Contr^A_* : H^1(F', S^{⊗3}(2)) → H^1(F', S(1))`.
* Definitions of the finite point and packaged point (from BCPV's cycles):

      P_r[d] := Π_{A,*} Δ_r^ord[d] ∈ J(F') ⊗ Z_p,
      P_r[[a,b,c]] := Σ_{g ∈ G_r} P_r[g·(a,b,c)] ⊗ g ∈ (J(F') ⊗ Z_p[G_r]),
      P_r := (p^3/(p−1)^3) Σ_{a,b,c} P_r[[bc, ac, ab]]        (mirror of BCPV Def 4.9).

  (Coefficient retention / carrier `B^bal_r` in the sense of Lanes 2/4: keep the Hecke-orbit indexing of `t_2 ⊗ t_3` as
  in `Φ^mod_r(t_2 ⊗ t_3) := Π_{(t_2 ⊗ A t_3),*} Δ` — every such `Π` is again `X_{14} × Γ` for an algebraic correspondence
  `Γ = Γ_{t_2}^t ∘ Γ_A ∘ Γ_{t_3}`, so all statements below hold verbatim with `A` replaced by `t_2^t A t_3`.)

## §3. Statement D4 and proof

**D4 (scalar, level `r`, over `F'`).** For every `d ∈ G̃_r` (and every Hecke pair `(t_2, t_3)`):

    Kum(P_r[d]) = Contr^A_*( K ∘ cl_1(Δ_r^ord[d]) )   in H^1(F', S(1)) = H^1(F', T_pJ),

where `K` is BCPV's Künneth projection to `H^1(F', S^{⊗3}(2))`.

*Proof.* Apply (AJ-corr) with `V = X^3`, `V' = X`, `𝒵 = Π_A`, `z = Δ_r^ord[d]`, `i = 2`, `c = −1`: `cl_1(Π_{A,*} z) =
[Π_A]_* cl_1(z)`. For `X^3 → X` the target is `H^1(F', H^1(X̄)(1))`, and `cl_1` on `CH^1_0(X) = J` is the Kummer map
(standard; BCPV (6.?) `eqn_2023_11_21_1605` uses this identification). It remains to compute `[Π_A]_*` on
`H^3(X̄^3)(2)`: by Künneth and the definition of `Π_A = X_{14} × Γ_A`, `[Π_A]_*` kills all Künneth components except
`H^1 ⊗ H^1 ⊗ H^1`, and on `y_1 ⊗ y_2 ⊗ y_3` it is `y_1 · ⟨y_2 ⊗ y_3, [Γ_A]⟩` where `⟨y_2 ⊗ y_3, [Γ_A]⟩ =
pr_*((y_2 ⊗ y_3) ∪ [Γ_A]) ∈ H^4(X̄^2)(3) ≅ Z_p(1)` equals `⟨y_2, [Γ_A]_* y_3⟩ = ⟨y_2, A y_3⟩` by the standard
cycle-class/operator dictionary for correspondences on curves (the same computation BCPV make for `Γ = Z` the
diagonal: "`cl_dR(ε_0[Z])` identified with `η_g ⊗ ω_{g^c}`, which pair to 1", Prop 6.2). Hence `[Π_A]_* = Contr^A_* ∘ K`. ∎

**D4 (packaged, type B, descended to `K_0`).** With `Contr^A` extended `Z_p[G_r]`-linearly:

    Kum(P_r[[a,b,c]]) = Contr^A_*( Δ^ét_r[[a,b,c]] )    in H^1(F', S(1) ⊗ Z_p[G_r]),

and both sides are the restriction to `G_{F'}` of unique classes in `H^1(K_0, (S(1) ⊗_{Z_p[G_r]} Z_p[G_r])^{†,tame})`
(dagger twist `⟨χ⟩_r^{-1/2}` on the factor-1 group ring, tame `ε_g^{-1}`-twist on factor 3 as in Lanes 2/4), where
they agree. Hence `Kum(P_r) = Contr^A_*(Δ^ét_r)` in `H^1(K_0, ·)`.

*Proof.* Termwise from the scalar D4 (both packagings are `Z_p[G_r]`-linear combinations with the same group-ring
coefficients `g`; `Contr^A` acts on the coefficient module `S^{⊗3}(2)`, not on the group ring). Descent: the étale side
descends by BCPV Lemma 4.7 (inflation–restriction with `(S^{⊗3}(2)^†)^{G_{F'}} = 0`... as used there); the point side
descends by Lanes 2/4's twisted-descent lemma (Lane 2 (G2), Lane 4 L2 — frozen inputs; they prove the packaged
point is `Gal(F'/K_0)`-invariant for the type-B/tame-twisted action, using `W^σ = ⟨a⟩W`, Ohta (4.2.4)). Restriction
`H^1(K_0, S(1)^{†}) → H^1(F', S(1))` is injective because `(S(1)^†)^{G_{F'}} = (T_pJ)^{G_{F'}} = T_p(J(F')[p^∞]) = 0`
(`J(F')` finitely generated). Two classes over `K_0` with equal restrictions are equal. ∎

**Is the type-B receptacle genuinely the right one?** Yes for the objects defined here: the packaged point lives in
`J(F') ⊗ Z_p[G_r]` (rank `2g·|G_r|` over `Z_p` before invariants) and its Kummer image in `H^1(F', S(1) ⊗ Z_p[G_r])`;
the descent statement identifies the invariant part with `H^1(K_0, S(1) ⊗_{Z_p[G_r]} Z_p[G_r]^†)`-type classes — the
`⊗_{Z_p[G_r]}` (type-B) module of rank `2g` — because the `G_r`-action on the packaging is through the *diamond*
action on the point (`P_r[g·d]` is `⟨g⟩` applied inside the cycle, BCPV (4.1)), not through a free `Z[G_r]`. This is
exactly Lane 4's L4-T1 refutation of the type-A receptacle and Lane 2's mandatory correction 2, now realized on the
Chow side. The `p^3` of the type-A comparison (Lane 4 L4-T2: `s_r ⊗ ϖ_* = p^3 ϖ_*` on invariants) does not appear:
`P3_REAPPEARS = NO` on the type-B object (the transition below has no constant).

## §4. The tower on points (what D4 + MPC + Cor 4.11 give; Lane 2's (E_ν), Lane 4's (T♮_r), typed)

Let `ν_{r+1} := N_{r+1,r}` act on the third slot (as a Hecke operator on the carrier, i.e. inside `Π`). Then in
`H^1(F'_{r+1}, S_r(1) ⊗ Z_p[G_r])` (equivalently, by Kummer injectivity on `p`-completed points — Lane 4 L3, Lane 2 Lemma F —
in `J_r(F'_{r+1}) ⊗ Z_p[G_r]`):

    ϖ_{1,*} P_{r+1}[[a,b,c]] ∘ (1 ⊗ N_{r+1,r})   =   (U'_p)^{⊗ 3-shape} ⋯ P_r[[a,b,c]]   — precisely:

    Kum( ϖ_{1,*} Π_{A_{r+1} N_{r+1,r},*} Δ^ord_{r+1}[d'] ) = Contr^{A_{r+1}N}_*(ϖ_{1,*}^{(1)} Δ^ét_{r+1}[d'])
      = Contr^{A_r}_*( (ϖ_{1,*}^{⊗3}) Δ^ét_{r+1}[d'] )                     [MPC_r, 03: ⟨ϖ_*y, A_rϖ_*z⟩_r = ⟨y, A_{r+1}N z⟩_{r+1}]
      = Contr^{A_r}_*( (U'_p)^{⊗3} Δ^ét_r[d] )                                [BCPV Cor 4.11(i)]
      = U'_p · Kum( Π_{U'^t_p A_r U'_p,*} Δ^ord_r[d] ) .                     [D4 at level r; `U'_p` on factor 1 = `U'_p` on `J_r`]

Reading: the `A`-modified contraction of the level-`(r+1)` cycle, pushed down by `ϖ_{1,*}` on the output factor and
contracted with the norm element on the carrier, equals the level-`r` contraction of `(U'_p)^{⊗3}Δ_r`. This is Lane 4's
§7 statement made exact: "one `U'_p` per level is left over" on each of the three factors, and the factor-3 transport
is `ϖ_2`-type only in the sense that `W` converts `ϖ_1^*` into `ϖ_2^*` inside the pairing — MPC has already absorbed it;
no explicit `ϖ_2` and no constant appears. With BCPV's normalization `(U'_p^{⊗3})^{-r}` (Def 4.12) on the cycle and
`(U'_p)^{-r}` on the point, the normalized points form a strictly compatible system:

    ϖ_{1,*}( (U'_p)^{-(r+1)} P_{r+1}^{norm} ) ∘ (1 ⊗ N_{r+1,r}) = (U'_p)^{-r} P_r^{norm} ∘ res^{bal}_{r+1,r}

with `δ♮_r = 1` in Lane 4's notation and `ν_{r+1} = N_{r+1,r}`, `d_r = 1` in Lane 2's. The group-ring projection
`p_{r+1,r}` sends `N_{r+1,r}` to `p`, so on `G_r`-coinvariants the relation reads `ϖ_{1,*}P_{r+1}^{norm} = p · P_r^{norm}`
only after that projection — the *integral* group-ring statement carries the norm element, not the scalar `p`.

## §5. Relation to the printed specialized statement

BCPV Rem 6.4 (`remark_2023_11_22_0818`) proves, after specialization at `(κ,λ)` and after `res_p` and `log_BK`,
that `(Π_{𝒞_g})_*` on cycles matches `id ⊗ tr` on the `f ⊗ ad(g)`-quotient, i.e. the specialized, local, logarithmic
shadow of D4 with the *diagonal* contraction (their `𝒞_g`), the `A_r`-modification then entering as the scalar
`a_p(g)^r λ_{N_gp^r}(g)^{-1}` (BCPV (6.?) `eqn_2024_02_09_0654`). §3 above is the unspecialized, global, integral
statement with the operator `A_r` kept as a correspondence; it specializes to BCPV's because on the `g`-isotypic
quotient `A_r` acts through the scalar `a_p(g)^r λ_{N_gp^r}(g)^{-1}` (pseudo-eigenvalue), which is how the two
normalizations of BCPV §6 (`Δ^tr` vs `Δ^{(P)}`) are related.

## §6. What D4 does NOT claim

* It does not identify `P_r[[a,b,c]]` with H9R16-A/B's `P_r^{tr,†}` (definition not in packet; R2 in 07).
* It does not assert the Chow–Heegner point is non-torsion, nor anything about heights, L-values, or weight one.
* It does not use BCPV (4.9). It does not use Ohta II. It does not use density or localization.
