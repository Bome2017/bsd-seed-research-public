# 04 — Exact remaining statement (Lane 2)

## What is no longer open (for this lane)

* The Kummer transition square itself — formal (03.1, 03.4.1).
* Descent of the finite balanced point to the fixed base `K_0 = Q(μ_p)` — proved, with the tame
  nebentype twist on the carrier (03.2).
* The dagger/group-ring and cyclotomic data — a cocycle identity; no corestriction in type B (03.3).
* Where a W/w discrepancy goes — never into the square; sufficient identities (D1)(D2)(D5), plus
  (D3) for the `w`-normalized functional (03.5).

## FIRST_EXACT_UNPROVED_STATEMENT — MPC_r(ν) (modified-pairing level compatibility, operator form)

Setting: `X_s := X_1(N_g p^s)` in the point-of-order model; `S_s := H^1_ét(X̄_s, Z_p(1))`;
`<,>_s` the Poincaré pairing; `U'_p`, `e' = lim (U'_p)^{n!}`, `𝕋'_s` as in BCPV §1.1.8;
`W_s := W_{N_g p^s}` defined by the KLZ2 moduli recipe with `ζ_{N_g p^{s+1}}^p = ζ_{N_g p^s}`;
`A_s := W_s^{-1}(U'_p)^s`; `ϖ_1: X_{r+1} → X_r`, `(A,P) ↦ (A,pP)`.

> **MPC_r(ν).** For every `r ≥ 1` there is `ν_{r+1} ∈ e'𝕋'_{r+1} ⊗ Z_p` such that
>
>     <ϖ_{1,*} y, A_r ϖ_{1,*} z>_r = <y, A_{r+1} ν_{r+1} z>_{r+1}      for all y, z ∈ e'S_{r+1}.
>
> Expected value (derived only under the group-ring-pairing hypothesis of 03.4.4):
> `ν_{r+1} = N_{r+1,r} := Σ_{k ∈ ker((Z/N_g p^{r+1})^× → (Z/N_g p^r)^×)} <k>`.

Equivalent forms: (i) the same identity on `e'Ĵ(Q̄)` for the Weil/Cartier pairing (Lemma T);
(ii) the operator identity `ϖ_1^* ∘ A_r ∘ ϖ_{1,*} = A_{r+1} ∘ ν_{r+1}` on `e'S_{r+1}`.

Why it is the first one: with MPC_r(ν), BCPV Corollary 4.11(i) gives the class compatibility (E_ν);
with the frozen finite realization `(K_r)` and the formal square, Kummer injectivity gives

    τ_r^MW(Q_{r+1}) ∘ (1 ⊗ ν_{r+1}) = π_r^* Q_r      in Hom_{Z_p}(B_{r+1}^{(ε)}, e'Ĵ_r)^†(K_0).

Classification: **NOT_PRINTED** in BCPV, DR22, MRS, Hida LMWM or KLZ2 in this operator form. It is an
identity of Hecke correspondences — no Selmer, Sha, control, reciprocity or L-value input — and it is
Tate-faithful. BCPV assert the Λ-adic form after (1.7), citing Ohta99 and KLZ2 §7. KLZ2 `thm:ordinaryfiltration`(v)
supplies the canonical Λ-adic pairing. **Ohta 2000 (Cor. 1.3.8, 2.3.6) was not obtained** and is the
most likely printed source. It is not `NEW_THEOREM_REQUIRED` unless those sources turn out to print
only the limit pairing without the finite-level comparison.

## Inputs this lane used but did not prove (frozen or standard)

| Input | Where frozen / sourced |
|---|---|
| `(K_r)`: `Kum(Q_r)` = normalized `(1⊗t_2⊗A_r t_3)`-contraction of `Δ_r^et` | H9R10 method (étale Abel–Jacobi functoriality); prompt: "finite modified point/Kummer realization" |
| balance `Φ_r^mod(t_2u', t_3) = Φ_r^mod(t_2, u't_3)` incl. diamonds | H9R16-A/B (frozen) |
| `H_π`: ring maps `π_r: e'𝕋'_{r+1} ⊗ Z_p → e'𝕋'_r ⊗ Z_p` with `ϖ_{1,*}t = π_r(t)ϖ_{1,*}` | standard Hida theory; not re-proved |
| `ϖ_{1,*}U'_p = U'_pϖ_{1,*}` | DR22 §1.3 (printed for `U_p^*`) |
| S6 standard facts | see ledger |

## Conditional statements (only if the corresponding route is chosen)

* Route (α) — prove MPC_r from Hida's `w`-relations: need `MPC_r^w(ν^w)` for `Ã_s = w̃_s^{-1}(U'_p)^s`
  plus (D1), (D5); then `ν = ν^w ũ` (Proposition D.1).
* Route (β) — use the `w`-normalized functional: (D1), (D2), (D5), and (D3) for descent (Proposition D.2–3).
