## 03.5 Where a W/w discrepancy `δ_r` can enter, and which identities make it harmless

Provisional Lane-1 output (value not guessed): after the model identifications,
`W_r = δ_r ∘ w̃_r` on `e'S^g_r` and `e'Ĵ^g_r`, where `w̃_r` is Hida's `w_r` transported to the BCPV model.
Put `Ã_r := w̃_r^{-1}(U'_p)^r`, so `A_r = Ã_r δ_r^{-1}` whenever `δ_r` commutes with `U'_p`.

### 03.5.1 Places where `δ_r` does **not** enter

| Step | Uses | `δ_r` needed? |
|---|---|---|
| descent of `Φ_r^mod` to `P_r^{tr,†}` (03.2) | BCPV (4.1)(4.2)(4.4)(4.5), KLZ2 diamond rule, balance | **No** — the Galois law of `W` is forced by (4.5) |
| the square (SQ) (03.4.1) | plain Albanese `ϖ_{1,*}` on co-ordinary parts, MRS functoriality, Lemma F | **No** |
| W on the f-factor inside `Δ^ord` | BCPV Lemma 4.10 (Chow level, printed) | **No** |

### 03.5.2 Places where it may enter

(α) **Proving MPC_r from Hida's `w`-relations** (S4 (6.6)–(6.8): `π_s^r∘π^*_{r,s} = p^{s-r}U(p)^{s-r}` and
`w`-twisted Cartier adjointness) instead of from Ohta's pairing.

(β) **Building the tower with the `w`-normalized functional** `Φ_r^w(t_2⊗t_3) := Π_{Z,*}((1⊗t_2⊗Ã_r t_3)Δ_r^ord)`,
i.e. with Hida's involution on the auxiliary factor. Then `Φ_r^w = Φ_r^mod ∘ (1 ⊗ δ_r)`.

(γ) **Using Hida's ordinary `w`-twisted tower on the f-factor** (`x ↦ w̃_r ∘ x`, transition `π_{r+1}^r`).
This involves the f-side `w` only. On the type-B twist it is `K_0`-rational at `p`
(`<z>c^{-1/2} = c^{+1/2}`) and at tame level wherever `ε_f = 1` (BCPV assume `ε_f` trivial). It is
isomorphic to the co-ordinary formulation and not needed.

### 03.5.3 Sufficient identities

    (D1) centrality      δ_r ∈ e'𝕋'_r ⊗ Z_p   (commutes with all T'_ℓ, U'_ℓ, <d>, e'_r)
    (D2) invertibility   δ_r ∈ (e'𝕋'_r ⊗ Z_p)^×        [integral tower]
                         δ_r ∈ (e'𝕋'_r ⊗ Q_p)^×        [Q_p-linear tower only]
    (D3) rationality     δ_r^σ = δ_r for all σ ∈ G_{K_0}
                         ⇔ W_r and w̃_r have the same Galois cocycle on G_{K_0}
                         ⇔ (by 03.2.1) w̃_r^σ = <z(σ)> ∘ w̃_r in the BCPV model
    (D4) diamond rule    <d> ∘ w̃_r = w̃_r ∘ <d^{-1}>            [implied by D1 and the rule for W]
    (D5) level           π_r(δ_{r+1}) = u_r · δ_r with u_r ∈ (e'𝕋'_r ⊗ Z_p)^× Q-rational
                         (simplest case u_r = 1)

**Proposition D.** Assume (D1), (D2), (D5).

1. *(α)* If `MPC_r^w(ν^w)`: `<ϖ_{1,*}y, Ã_r ϖ_{1,*}z>_r = <y, Ã_{r+1} ν^w z>_{r+1}` holds, then MPC_r(ν)
   holds with `ν_{r+1} = ν^w_{r+1} · ũ_{r+1}` for any lift `ũ_{r+1}` of `u_r` along `π_r`.
2. *(β)* Balance holds for `Φ_r^w` (ι_r = id), and the `w`- and `W`-normalized towers determine each
   other: `τ^MW(Q^w_{r+1})∘(1⊗ν^w) = π_r^*Q^w_r` ⇔ `τ^MW(Q_{r+1})∘(1⊗ν^wũ) = π_r^*Q_r`.
3. *(β, descent)* If moreover (D3), `Φ_r^w ∈ P_r^{tr,†}` with the same twist as `Φ_r^mod`.
   Without (D3), writing `δ_r^σ = κ_r(σ)δ_r`, `Φ_r^w` descends to the twist of the carrier by `κ_r`.

*Proof.* (1) By (D1), `A_r = Ã_rδ_r^{-1}`. By the defining property of `π_r` and (D5),
`δ_r^{-1}ϖ_{1,*} = u_r ϖ_{1,*}δ_{r+1}^{-1} = ϖ_{1,*}ũ_{r+1}δ_{r+1}^{-1}`. Hence
`<ϖ_*y, A_rϖ_*z> = <ϖ_*y, Ã_rϖ_*(ũδ_{r+1}^{-1}z)> = <y, Ã_{r+1}ν^wũδ_{r+1}^{-1}z> = <y, A_{r+1}(ν^wũ)z>`,
using `MPC_r^w` and commutativity of `e'𝕋'_{r+1}`.
(2) `ρ_r(u')Ã_r = ρ_r(u')A_rδ_r = A_ru'δ_r = Ã_ru'` by H9R16-A/B and (D1), so `ι_r = id` for `Φ^w`.
`Φ_r^w = Φ_r^mod∘(1⊗δ_r)`; the normalizations commute with `δ_r` (D1); `δ_r` is invertible (D2); and
(D5) converts `π_r^*(Q_r∘(1⊗δ_r))` into `(π_r^*Q_r)∘(1⊗δ_{r+1}ũ^{-1})`.
(3) Repeat 03.2.2 with `Ã_r^σ = A_r^σ δ_r^σ`. ∎

**Reading.** (D1)+(D2)+(D5) are what the tower consumes. (D3) is consumed only by (β)'s descent.
A central diamond `δ_r = <a_r>` (Q-rational) satisfies (D1)–(D3). It satisfies (D5) iff
`a_{r+1} ≡ a_r·(unit diamond)` compatibly, e.g. `δ_r = <p>_N^{±r}` has `u_r = <p>_N^{±1}`, a unit that is
absorbed. A scalar `δ_r = p^{e_r}` is central and Q-rational but fails (D2) integrally when `e_r > 0`;
over `Q_p` it is harmless if `u_r = p^{e_{r+1}-e_r}`. A discrepancy involving a Galois element or a
non-Hecke correspondence would violate (D1) or (D3); nothing in the sources read here suggests one.

**How to insert `δ_r`.** Never inside the square. Insert it (i) on factor 3 of the carrier, as
precomposition with `1⊗δ_r`, when converting between `W`- and `w`-normalized functionals; and (ii) in
the correction element `ν_{r+1} = ν^w_{r+1}ũ_{r+1}` of the compatibility relation.
