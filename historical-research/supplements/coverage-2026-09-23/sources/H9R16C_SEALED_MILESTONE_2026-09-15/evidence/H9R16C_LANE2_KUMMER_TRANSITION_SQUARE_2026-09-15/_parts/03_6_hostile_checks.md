## 03.6 Hostile checks on the Lane-2 construction

Labels: `NOT_PRINTED` / `FALSE` / `TYPE_MISMATCH` / `NEW_THEOREM_REQUIRED` / `PASS`.

| # | Attack | Finding | Label |
|---|---|---|---|
| H1 | Does the balanced finite point belong to the fixed-base MRS module over `Q(μ_p)`? | Only with the tame nebentype twist on the carrier's third factor (03.2.3). Without it the point is `K_0(μ_{N_g})`-rational and transforms by `<z_N>^{-1}` on factor 3. With it, (G2) proves membership. | literal "`Q(μ_p)`" is `TYPE_MISMATCH` unless `ε_g`-twist written; PASS with it |
| H2 | Is the Kummer target BCPV's Tate module? | Type B: yes. H9R8's type A has rank `\|G_r\|` times larger and is not BCPV's module; BCPV classes cannot be used there. | type A `TYPE_MISMATCH`; type B PASS |
| H3 | Level change conflated with corestriction? | Type B: no corestriction exists (03.3.3). Type A: the lattice projection is corestriction on its Weil-restriction blocks plus diamond sums. | PASS in type B |
| H4 | Group-ring projection vs MRS lattice | `id⊗pr_r` is `G_{K_0}`-equivariant because `pr_r∘c_{r+1}^{1/2} = c_r^{1/2}`; `μ_r` intertwines A and B with no `1/p`. | PASS |
| H5 | Hida `w`-transition on the twisted object | Not needed. If used on the f-factor it is `K_0`-rational at `p`, and at tame level on `ε_f = 1` parts (03.5.2 γ). | PASS (optional) |
| H6 | Central diamond discrepancy vs dagger descent | Descent uses `W` only, and its law is forced by BCPV (4.5). `δ_r` matters only through (D3) in route (β) and (D5) in the level relation. | PASS given (D1)(D2)(D5); (D3) only for (β) |
| H7 | p-completion / inverting `p` vs Kummer injectivity | Injective on `Â(K_0)`, on `e'`-summands, on `Hom(B, −)`, and after `⊗Q_p`. The integral relation with `ν = N` never divides by `p`. | PASS |
| H8 | Coefficient retention through the transition | No arrow `P_{r+1} → P_r` exists: `Hom(B,−)` is contravariant and `B_{r+1} → B_r` is onto. The correct target is `π_r^*P_r ⊂ Hom(B_{r+1}, e'Ĵ_r)^†`. | `TYPE_MISMATCH` in the prompt's arrow; PASS after correction |
| H9 | Does `g^c` duality change the direction? | No. `A_r` acts on factor 3; carrier transitions are `π_r` on both auxiliary factors; `g^c` changes the Galois module (tame `ε^{-1}`), not the variance. Balance `ι_r = id` keeps both factors covariant on `e'`-parts. | PASS |
| H10 | Finite point inferred from an étale realization? | No. `Φ_r^mod` is a Chow-level construction (H9R16-A/B), and its descent (03.2) is proved at Chow level. The Kummer realization `(K_r)` is a separate frozen input (étale Abel–Jacobi functoriality for algebraic correspondences). | PASS; `(K_r)` is an input |
| H11 | `(U'_p)^{-r}` on points | `e'_r ∈ 𝕋'_r ⊗ Z_p` is idempotent and `U'_p` is a unit of the finite `Z_p`-algebra `e'𝕋'_r ⊗ Z_p`, so the inverse exists on `e'Ĵ_r(F)` (cf. S4 §3). The BCPV Definition 4.12 inversion is not used at point level. | PASS |
| H12 | The class-compatibility identity (E_ν) | Reduces exactly to MPC_r(ν), an identity of Hecke correspondences on `X_1(N_g p^{r+1})`. Not printed in any source obtained. The Λ-adic form is asserted by BCPV after (1.7) and in KLZ2 `thm:ordinaryfiltration`(v); Ohta 2000 was not obtained. | `NOT_PRINTED` (not `NEW_THEOREM_REQUIRED`: no arithmetic input, Tate-faithful) |
| H13 | Citation hygiene | BCPV footnote 8 → Remark 4.9(ii) should be 4.5(ii); BCPV Lemma 4.10 → "[DR22] Lemma 2.5" is Lemma 2.4 in arXiv v1. | `NOT_PRINTED`-type drift, no mathematical effect |

**Obstruction search result.** No `FALSE` item and no `NEW_THEOREM_REQUIRED` item was found. Two
typing corrections are mandatory (H1 tame twist; H8 pull-back target) and one convention is mandatory
(03.3.1 MRS lattice sign). Type A is excluded for BCPV's classes (H2).

## 03.7 Conclusion of the derivation

1. **The square is formal.** With `P_r^{tr,†}` the type-B twist (lattice `c_r^{+1/2}` on the Jacobian
   factor, tame `ε`-twist on the carrier), `τ_r^MW = ϖ_{1,*}∘(−)`, target `π_r^*P_r^{tr,†}`, and
   `τ_r^et = H^1(K_0, T_pτ_r^MW)`, the square commutes by Lemma F. Nothing from Lane 1 is used.
2. **Point normalization over `K_0` is proved** from BCPV (4.1), (4.2), (4.4), (4.5), the KLZ2 diamond
   rule and H9R16-A/B balance (03.2).
3. **The tower relation** `τ_r^MW(Q_{r+1})∘(1⊗ν_{r+1}) = π_r^*Q_r` follows from the square, `(K_r)`,
   `(K_{r+1})`, BCPV Corollary 4.11, and **one** identity of correspondences, MPC_r(ν) (03.4.3).
4. **`δ_r`** is never inserted into the square. It is harmless under (D1)(D2)(D5) for the tower, plus
   (D3) if the `w`-normalized functional is used (Proposition D).

    C2_REDUCES_TO_FORMAL_NATURALITY
    (square PROVED; class compatibility reduced to MPC_r(ν), NOT_PRINTED)
