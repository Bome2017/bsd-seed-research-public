# 05 — Next handoff (Lane 2 → coordinator)

## Do not redo

1. The Kummer transition square on the type-B dagger object is formal (Lemma F + MRS functoriality).
2. `Φ_r^mod` descends to `K_0` (03.2, identity (G2)); BCPV (4.5) forces `W^σ = <z>∘W`.
3. MRS lattice for BCPV's `†` has character `c_r^{+1/2}` (MRS Lemma 1.3 inverse convention).
4. Type A (`Z[G_r] ⊗_Z J_r`) is not a receptacle for BCPV's classes; type B is.
5. In type B there is no corestriction; the level map descends by itself.
6. `δ_r` is not inserted into the square.

## Mandatory corrections to carry into the checkpoint's H9R16-C text

* "fixed-base dagger/MRS object over `K_0 = Q(μ_p)`" → add: **with the tame `ε_g^{-1}` (g^c) twist
  on the carrier's third factor**; otherwise the balanced point is only `K_0(μ_{N_g})`-rational.
* "`τ_r^MW: P_{r+1}^{tr,†} → P_r^{tr,†}`" → **`τ_r^MW: P_{r+1}^{tr,†} → Hom(B_{r+1}^{(ε)}, e'Ĵ_r)^†(K_0) ⊇ π_r^*P_r^{tr,†}`**,
  and the compatibility is `τ_r^MW(Q_{r+1})∘(1⊗ν_{r+1}) = π_r^*Q_r`.
* "`A_r^† := I_r^† ⊗ J_r`" (H9R8) → type B `O_r(c_r^{+1/2}) ⊗_{O_r} V_r` with `O_r = Z[G_r]`
  acting by diamonds.

## Work orders

**Lane 1 (W/w dictionary).**
1. Consistency test (free): any dictionary must reproduce `W_{Np^r}^σ = <z>∘W_{Np^r}`, since BCPV
   (4.5) is equivalent to it given (4.1), (4.2) and the diamond rule (03.2.1).
2. Compute `δ_r`; check (D1), (D2), (D5); check (D3) only if the `w`-normalized functional is wanted.
3. Try to prove MPC_r(ν) — either directly (degeneracy/Atkin–Lehner calculus on `X_1(N_g p^{r+1})`) or
   via Proposition D.1 from Hida's (6.6) and `w`-twisted Cartier adjointness.

**Lane 3 (literature).**
1. Obtain Ohta, *Ordinary p-adic étale cohomology groups attached to towers of elliptic modular curves*
   I (Compositio Math. 115, 1999: eq. (1.5.4), §2.2) and II (Math. Ann. 318, 2000: Cor. 1.3.8, 2.3.6).
   Decide whether the **finite-level** group-ring-valued pairings with `W^{-1}(U'_p)^r` and their
   projection compatibility are printed. If yes, MPC_r(N) is sourced and C2 closes completely.
2. Record KLZ2 printed theorem numbers for `thm:ordinaryfiltration` and the Atkin–Lehner subsection.
3. Obtain Hida, *Control of Λ-adic Mordell–Weil groups* (PROMS 188, 2016) to reconcile the checkpoint's
   "Hida Lemma 2.1" with LMWM Lemma 2.2.

**Lane 4 (kill).**
1. Attack MPC_r(ν) numerically: weight-2 modular symbols for one small case (e.g. `p = 3`,
   `N_g = 13`, `r = 1`), including the value of `ν`. A failure for every Hecke element `ν` would be a
   genuine obstruction to the tower, not to the square.
2. Attack (G2) at the tame primes when `ε_g` is nontrivial (the CM weight-one case of H9R15).
3. Attack the scope of `(K_r)` for the unspecialized carrier-valued functional.

## Cross-lane consistency (read after this lane's conclusions were written)

Lane 4 (`~/H9R16C_LANE4_HOSTILE_OBSTRUCTION_2026-09-15`, as summarized in its memory note) reports
four findings: the type-A receptacle has the wrong rank; a tame `ε_g` twist survives while the p-part
auxiliary twists cancel; BCPV (4.9) is off by `p^2`; and the first gap is an operator-level
modified-pairing identity `(★_r)`. All four agree with 03.3.2, (G2), 03.3.3 and MPC_r(ν) here.

Lane 4 writes its tame law as `σ∘Φ = <m>^{1/2}_{(1)}<n>_{(1)}∘Φ∘R(<n>)`. That is the same statement as
(G2): the tame diagonal diamond fixes `Δ_r^ord`, because `<n,n,n>_N` preserves the diagonal and
commutes past `W^{⊗3}`, so balance gives `Φ = <n>_{(1)}∘Φ∘(1⊗<n>^2)`, and the two formulas agree.
Lanes 1 and 3 were not read.

## Next smallest test

MPC_1(N_{2,1}) on `e'H^1` of `X_1(N_g p^2)` vs `X_1(N_g p)` for one `(N_g, p)`, together with the exact
form of `ν_2`. Not run here: PARI/GP offers `msinit`, `mshecke`, `msatkinlehner`, but degeneracy maps
between levels would have to be implemented by hand.

## Custody

Lane directory `~/H9R16C_LANE2_KUMMER_TRANSITION_SQUARE_2026-09-15/`. Primary sources are copied into
`sources/` with SHA-256 in `06`. `_parts/` holds the section drafts concatenated into `03`. Nothing
sealed, nothing sent, no Lean, no Aristotle.
