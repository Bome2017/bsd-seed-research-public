# 06 — ITEM 4: does any full-triple-G_r or type-A rank factor re-enter?

Continues 03–05. Per 02a §2, the claim "a multiplication-type identification produces p^3 per level" is
**not** taken as a recorded fact; every candidate factor is computed here for the objects actually used.

## §1. The five places a factor could enter, and what each actually gives

| # | place | candidate factor | computed result |
|---|---|---|---|
| 1 | packaging → point object (03 §4) | `\|G_r\| = p^{3(r−1)}` | none for `G`; `μ_r` gives a different functional, not a factor (§2) |
| 2 | the carrier `B_r^bal` | `\|G_r\|` in the rank | none: `B_r^bal ≅ R_r` (04 Lemma C), rank independent of `G_r` (§3) |
| 3 | the post-contraction dagger group | `G_r` vs factor-1 quotient | factor-1 cyclic quotient only, order `p^{r−1}` (§3) |
| 4 | the level step `r+1 → r` | `p^3 = \|ker(G_{r+1}→G_r)\|` (L4-T2), or `p^{±1}`, `p^{±2}` | none; the single `p` appears only as `π_r(N_{r+1,r}) = p` (§4) |
| 5 | BCPV's normalizing constants | `p^3/(p−1)^3` (Def 4.9, l.1397–1399) | level-independent; cancels in the relation (§5) |

## §2. `G` versus `μ_r` — computed for the Lane-5 packaging

Reindexing: BCPV (4.1) (l.1218) `⟨a_1,a_2,a_3⟩Δ_r[d] = Δ_r[a_2a_3d_1, a_1a_3d_2, a_1a_2d_3]`, and
`⟨a⟩W = W⟨a⟩^{-1}` give, for `Δ_r^{ord} = (e'W_{Np^r})^{⊗3}Δ_r` and `g = ⟨d_1,d_2,d_3⟩ ∈ G_r`:

    Δ_r^{ord}[g·(a,b,c)] := Δ_r^{ord}[d_2d_3a, d_1d_3b, d_1d_2c] = ⟨g⟩^{-1} Δ_r^{ord}[a,b,c] .

Hence, with `P_r[d] = Π_{A,*}Δ_r^{ord}[d]` and 03 §2.5 (factor-1 operators pass to the output; factors 2,3
pass to the carrier, and by balance `⟨d_2⟩,⟨d_3⟩` merge on slot 3):

* **`G` (identity coefficient, BCPV l.1331–1332).**  `G(P_r[[a,b,c]]) = P_r[(a,b,c)]` — the index-`e` point
  of 03 §4. **No factor**, and no information lost: `G` is BCPV's own inverse to the packaging.
* **`μ_r` (multiplication, `g⊗v ↦ ⟨g⟩v`).**
  `μ_r(P_r[[a,b,c]]) = Σ_{g∈G_r} ⟨d_1⟩·⟨d_1⟩^{-1}Φ_r^{mod}(t_2 ⊗ ⟨d_2d_3⟩^{-1}t_3)
   = Σ_{g∈G_r} Φ_r^{mod}(t_2 ⊗ ⟨d_2d_3⟩^{-1}t_3)`, i.e. `Φ_r^{mod} ∘ (1 ⊗ Σ_{g}⟨d_2d_3⟩^{-1})`.
  This is **not** `\|G_r\|·Φ_r^{mod}`: it is `Φ_r^{mod}` precomposed with a diamond sum in `R_r`. The
  factor-1 twists cancel exactly (that is the `p`-part cancellation of B3/B2 again), and what is left is a
  carrier element, `Σ_{(d_2,d_3)}⟨d_2d_3⟩^{-1}` times `p^{r−1}` (the `d_1`-sum, which no longer acts).
  On a branch where the carrier diamonds act through a character `ψ`, this is
  `p^{r−1}·(Σ_{d_2}ψ(d_2)^{-1})(Σ_{d_3}ψ(d_3)^{-1})` — **zero unless `ψ` is trivial there**, and `p^{3(r−1)}`
  when it is.
  **Conclusion:** `μ_r` does not merely rescale; it destroys the object generically and inflates it by
  `\|G_r\|` on the trivial-character part. It is refused in 03 §4 and is used nowhere in 03–05.
  This *computes* what 02 §D P1 asserted, for the Lane-5 packaging, as 02a §2 requires: the danger is real
  but is avoided by construction, and its shape is `\|G_r\|`-or-`0`, not a uniform `p^3` per level.

## §3. Ranks: the receptacle has no `|G_r|`

* `B_r^bal ≅ R_r = e'_ord𝕋'_{N_gp^r}⊗Z_p`, free over `Z_p` (04 Lemma C) — the balancing quotient already
  removes the second tensor factor. `rank_{Z_p}T_r^♮ = rank_{Z_p}(B_r^bal)·2g^{(1)}_r`, with **no** `|G_r|`.
* This is the type-B situation of B3: `T_p(A_r^†) = T_pV_r ⊗_{Z_p[G_r]} Z_p[G_r]^†` has the same `Z_p`-rank
  as `T_pV_r`, whereas the type-A object `Z_p[G_r]^†⊗_{Z_p}T_pV_r` has rank `|G_r| = p^{3(r−1)}` times
  larger (L4-T1). Nothing in 03–05 constructs a type-A object: the point module is `Hom_{Z_p}(B^bal, Ĵ)`
  with the ⋆-twist, never `Z[G_r]⊗_Z J`.
* **Post-contraction dagger group.** After `Contr^{A_r}` only factor 1 survives, and by B2/B3 the `p`-part
  twist is `⟨m_σ⟩^{1/2}` on factor 1 alone (the two auxiliary half-twists cancel against
  `σ(A_r) = A_r⟨m⟩^{-1}`). So the dagger group is the factor-1 cyclic quotient of order `p^{r−1}`, and the
  triple group `G_r` never acts on the receptacle. Consistent with `BCPV`'s own diagonal `⟨𝛘⟩_r`
  (`defn_Gal_twisted_general`, l.1363–1365): the diagonal character is what survives contraction.

## §4. The level step: where the `p`-powers could have come from, and where the one `p` is

* **Type-A transition (L4-T2).** `s_r ⊗ ϖ_*` on `G_r`-invariants equals `p^3·ϖ_*` in `M`-coordinates,
  because `ker(G_{r+1}→G_r) ≅ (Z/p)^3` acts trivially after `ϖ_*`. **Not used**: our transition is
  `τ_r^MW(x) = ϖ^{(1)}_{1,*}∘x` on `Hom(B^bal,Ĵ)`; there is no `s_r`, no group-ring tensor factor, and no
  invariant-subvariety identification. The `p^3` therefore cannot enter.
* **BCPV (4.9)** (prohibited, and B4 records `1/p` printed vs `p^{-3}` forced): never used; the chain of 05
  §3 uses only `cor_DR_lemma_2_5_dual` (l.1421) and A1.
* **Hida-type `p`-powers** (`ϖ_{i,*}ϖ_j^*`): absent, because the only degeneracy composite in the chain is
  the pull-after-push inside A1, whose value is the *element* `N_{r+1,r}` (A2, 02 §A l.24).
* **The single `p`.** It appears exactly once, as `π_r(N_{r+1,r}) = p·1` under
  `Z_p[(Z/N_gp^{r+1})^×] → Z_p[(Z/N_gp^r)^×]` (A2). It is `p^1`, not `p^3`, because the norm element sits on
  **one** slot of the carrier: factor 1's level change is carried by `ϖ^{(1)}_{1,*}` itself, and factor 2's
  is absorbed by the transposition into the modified pairing (05 §3.1, §3.3). Integrally, the relation of 05
  §3.5 carries the group-ring element, never a division by `p`; only after `π_r` does it read
  `ϖ_{1,*}Q_{r+1} = p·Q_r`.
* **`p^{±1}`, `p^{±2}` from `ϖ_{1,*}ϖ_1^* = p^2` etc.**: no such composite occurs in 05 §3.

## §5. BCPV's own constants

`Δ_r^ét := (p^3/(p−1)^3)Σ_{a,b,c∈F_p^×}Δ_r^ét[[bc,ac,ab]]` (l.1396–1399) carries `p^3/(p−1)^3` at **every**
level with the same value, and `cor_DR_lemma_2_5_dual`(ii) (l.1424) is stated for `Δ_r^ét` with those
constants included. In 03–05 the index-`e` class is used, so the constant does not arise at all; if one
prefers BCPV's symmetrized class, both sides of 05 §3.5 acquire the same factor and the relation and its
constant 1 are unchanged. **No per-level factor.**

## §6. Verdict for item 4

**ITEM 4 = PROVED (no factor re-enters).** The receptacle is type B with the factor-1 dagger; the carrier is
`R_r` (no `|G_r|`); the transition is `ϖ_{1,*}∘(−)` (no `s_r⊗ϖ_*`, hence no `p^3`); BCPV (4.9) is unused;
the only `p` is the image of the norm element under the group-ring projection. The one identification that
would reintroduce `|G_r|` (or annihilate the point) is `μ_r`, and it is refused in 03 §4 — this is the
single place where the assembly has to make a choice, and the choice is forced by BCPV's own `G`.

ITEM4_STATUS = PROVED (no |G_r|, no p^3, no p^{±1}/p^{±2}; the unique p is π_r(N_{r+1,r}) = p)
