## 03.4 The transition square and the one non-formal identity

### 03.4.1 The point transition is `K_0`-rational (co-ordinary, plain Albanese)

Define, on type-B objects,

    τ_r^MW : P_{r+1}^{tr,†} → Hom_{Z_p}(B_{r+1}^{(ε)}, e'Ĵ_r)^†(K_0),     x ↦ ϖ_{1,*} ∘ x.

* `ϖ_{1,*}` is Q-rational and `O`-semilinear over `pr_r` (T1), so 03.1 extension 4 gives a
  `K_0`-homomorphism of twists; the tame carrier twist is untouched (it acts on factor 3).
* `ϖ_{1,*} ∘ e'_{r+1} = e'_r ∘ ϖ_{1,*}` because `U'_p` commutes with `ϖ_{1,*}` (S2 §1.3) and Lemma T.
* Hida's (u*1) (S4 §3) is the point-level statement that plain Albanese pushforward is a
  `U^*(p)`-isomorphism, i.e. that this is the natural transition on the co-ordinary tower.
  *Using this requires the identification `BCPV U'_p = U^*(p)` on the same model (Lane 1). The square
  itself only uses `ϖ_{1,*}U'_p = U'_pϖ_{1,*}`, which is printed (S2) — it does not need that name.*

Its Tate realization is post-composition with `ϖ_{1,*}` on `Hom(B_{r+1}, e'S)^†`. By Consequence C-F:

    Kum ∘ τ_r^MW = τ_r^et ∘ Kum,      τ_r^et := H^1(K_0, T_p τ_r^MW).                (SQ)

**(SQ) is PROVED — formal naturality.** No `W`, no `w`, no `δ_r` enters it.

### 03.4.2 Typing correction forced by coefficient retention

`Hom(B, −)` is contravariant in the carrier, and `B_{r+1} → B_r` (induced by `π_r`) is surjective.
There is therefore **no** arrow `P_{r+1}^{tr,†} → P_r^{tr,†}` of carrier-valued point modules. The
well-typed receptacle is the injective pull-back

    π_r^* : P_r^{tr,†} ↪ Hom_{Z_p}(B_{r+1}^{(ε)}, e'Ĵ_r)^†(K_0),

and "compatibility" means an equality inside that module. Kummer injectivity holds there (03.1,
extension 2). This is a type correction to the prompt's square, not an obstruction.

### 03.4.3 What must still be shown: compatibility of the contracted classes

Let `c_r := Kum(Q_r)` — by the finite modified point/Kummer realization (H9R10, frozen input `(K_r)`)
this is the BCPV class `Δ_r^et` contracted by `(1 ⊗ t_2 ⊗ A_r t_3)`, normalized by
`(U'_p)^{-r}` on factor 1 and `(U'_p)^{-2r}` on the carrier. For the tower one needs

    (E_ν)   τ_r^et(c_{r+1}) ∘ (1 ⊗ ν_{r+1}) = π_r^* c_r      in H^1(K_0, Hom(B_{r+1}, e'S_r)^†)

for some fixed `ν_{r+1} ∈ e'𝕋'_{r+1} ⊗ Z_p` acting on factor 3 of the carrier. **(E_ν) is not in BCPV.**
It follows from BCPV Corollary 4.11(i) together with the following identity of correspondences on the
auxiliary tower `X_1(N_g p^{r+1})`:

    MPC_r(ν):   <ϖ_{1,*}y, A_r ϖ_{1,*}z>_r = <y, A_{r+1} ν_{r+1} z>_{r+1}
                for all y, z ∈ e'S^g_{r+1}     (equivalently ϖ_1^* A_r ϖ_{1,*} = A_{r+1} ν_{r+1}).

*Derivation of (E_ν) from MPC_r(ν).* Realize `Φ_{r+1}^mod(t_2 ⊗ ν t_3)` on `x_1⊗x_2⊗x_3` as
`x_1 <t_2x_2, A_{r+1}νt_3x_3>_{r+1}`. Push forward on factor 1; MPC_r(ν) with `y = t_2x_2`,
`z = t_3x_3` and `ϖ_{1,*}t = π_r(t)ϖ_{1,*}` turn this into the level-`r` contraction
`[π_r(t_2), π_r(t_3)]` of `ϖ_{1,*}^{⊗3}Δ_{r+1}^et`, which is `U'^{⊗3}_pΔ_r^et` by Corollary 4.11. Moving
the three `U'_p` out (factor 1, and onto the carrier by balance) and inserting the normalizations gives
`ϖ_{1,*} ∘ c_{r+1} ∘ (1⊗ν) = c_r ∘ π_r`. ∎

*From (E_ν) to points.* By (SQ), (K_{r+1}), (E_ν), (K_r):

    Kum( τ_r^MW(Q_{r+1}) ∘ (1⊗ν) − π_r^*Q_r ) = τ_r^et(c_{r+1})∘(1⊗ν) − π_r^*c_r = 0,

so Kummer injectivity gives **`τ_r^MW(Q_{r+1}) ∘ (1⊗ν_{r+1}) = π_r^* Q_r`** — the H9R16-C point
relation in its correctly typed form.

### 03.4.4 Status of MPC_r and the value of `ν`

* By Lemma T, MPC_r(ν) holds on `e'Ĵ` if and only if it holds on `e'S`. It is a statement about
  Hecke correspondences — **no Selmer, Sha, control or L-function input**.
* BCPV assert its Λ-adic form ("(1.7) are interpolated by (1.4)"), citing Ohta and KLZ2; KLZ2
  Theorem [Ohta] `thm:ordinaryfiltration`(v) supplies the canonical `Λ_D`-pairing and remarks that it
  involves `W_{Np^r}^{-1}(U'_p)^r`. The underlying Ohta 2000 statements (Cor. 1.3.8, 2.3.6) were **not
  obtained**.
* If the finite-level group-ring pairings are `Σ_{a} <x, <a> A_r y> [a]` and project compatibly under
  `Z_p[Δ_{p^{r+1}}] → Z_p[Δ_{p^r}]`, reading the identity coefficient gives MPC_r(ν) with
  `ν_{r+1} = N_{r+1,r} := Σ_{k ∈ ker} <k>`, the norm element of `ker((Z/p^{r+1})^× → (Z/p^r)^×)`.
  This is **DERIVED_HERE under that hypothesis, not proved**. Sanity check on old vectors
  `z = ϖ_1^*z_0`: both sides reduce to `p·ϖ_1^*A_r = A_{r+1}ϖ_1^*`, which is the `W`-conjugate of the
  q-expansion relation `U_p ∘ pr_2^* = p·pr_1^*` in weight 2 (KLZ2, proof after
  `thm:ordinaryfiltration`). Heuristic only.
* With `ν = N`, `π_r(N) = p`: the integral relation is `τ^MW(Q_{r+1})∘(1⊗N) = π_r^*Q_r`, and no
  division by `p` occurs. The kernel here is the single-factor kernel, of order `p`. It should not be
  matched with BCPV's printed `1/p` in (4.9): that is a triple-product constant, and commutativity of
  (4.8) forces `p^{-3}` there (03.3.3).
