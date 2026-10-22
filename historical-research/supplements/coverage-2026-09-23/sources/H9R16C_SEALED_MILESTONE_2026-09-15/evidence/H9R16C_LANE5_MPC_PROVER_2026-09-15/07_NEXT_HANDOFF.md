# 07 — Next handoff (Lane 5 → hostile reconciler)

## Ship as theorems (re-derive nothing; verify everything)

| ID | statement | where | evidence |
|---|---|---|---|
| L5-T1 (Lemma W) | `ϖ_1∘W_{s+1} = W_s∘ϖ_2` and `ϖ_2∘W_{s+1} = W_s∘ϖ_1` exactly, for KLZ17's moduli `W` with `ζ_{s+1}^p = ζ_s`; no diamond | 03 | moduli proof + matrix check + numerical (iv),(iv') |
| L5-T2 (norm element) | `ϖ_2^*ϖ_{1,*} = U'_p N_{r+1,r}` on `H^1(X_{r+1})`, `N_{r+1,r} = Σ_{d ≡ 1 (Np^r)}⟨d⟩` | 02 §3 | two independent proofs (double coset, moduli) + 2 consistency checks + numerical (iii),(iii^t) |
| L5-T3 (MPC_r) | `ϖ_1^*A_rϖ_{1,*} = A_{r+1}N_{r+1,r}`, `d_r = 1`, on all of `H^1` | 03 Thm | 4-line proof from T1, T2, `ϖ_{1,*}U'_p = U'_pϖ_{1,*}` + numerical (v) in 7 cases × 2 primes |
| L5-T4 (group-ring form) | `π(⟨⟨x,y⟩⟩_{r+1}) = ⟨⟨ϖ_*x, ϖ_*y⟩⟩_r`, constant 1 | 03 Cor | from T3 |
| L5-T5 (tame transport) | `pr^t_1∘W_{Np^s} = W_{N_gp^s}∘pr^t_2` with `ζ_{Np^s}^t = ζ_{N_gp^s}` | 04 §3 | same proof as T1 |
| L5-D4 | `Kum(P_r[[a,b,c]]) = Contr^{A}_*(Δ^ét_r[[a,b,c]])` for the BCPV-defined point `P_r := Π_{A,*}Δ^ord_r` | 05 | formal from (AJ-corr) + Lanes 2/4 descent |

## The five referee checks the operator listed, with pointers

1. **Derivation of `N_{r+1,r}`** — 02 §3 (Proof A: cosets `H\Γ_r` with `H = {b ≡ 0 (p), d ≡ 1 (pM)}`; Proof B: moduli
   `ϖ_2^{-1}(A,pP') = {(A/D, (P'+t) mod D)}`). Independent numerical realization in `_verify/msym_check.py` check (iii).
   Attack surface: the claim that `{[[1,b],[0,1]]δ_d}` represents `H\Γ_r`; and that the multiplicities are all 1.
2. **Every factor in `d_r`** — 04 §2 table. Attack surface: (a) `W^{-1} = W` (needs `⟨−1⟩ = id`, weight 2); (b) compatible
   `ζ`'s (an incompatible system gives a central diamond, 03 obstruction list); (c) `ϖ_{1,*}U'_p = U'_pϖ_{1,*}` for
   BCPV's `U'_p` (DR22 §1.3 prints it for `U_p^*`; 02 §2(c) re-derives it as a cycle identity).
3. **Does type B eliminate the `p^3`?** — 04 §2 row 2 and 05 §3–4: the per-factor kernel has order `p` and enters as the
   element `N_{r+1,r}`; the `p^3` was the type-A/(4.9) scalar. Attack surface: whether the referee's `P_r^{tr,†}` is
   literally the type-B packaged point `P_r[[a,b,c]]` of 05 §2 (if H9R16-A/B built it with a free `⊗_Z Z[G_r]`, Lane 4's
   `p^3` returns there, not in MPC).
4. **Common/native `W`** — 04 §3: `pr^t_1∘W_{Np^s} = W_{N_gp^s}∘pr^t_2`, no scalar/diamond; the correction is a change of
   tame degeneracy map. Attack surface: BCPV Def 4.13 pushes the auxiliary factors down by `ϖ_{1,*}` (forgetful) *after*
   `W_{Np^r}` was applied inside `Δ^ord_r`; then `A_r` at native level uses `W_{N_gp^r}`. By T5, `pr^t_{1,*}W_{Np^r} =
   W_{N_gp^r}pr^t_{2,*}`, so BCPV's native-level class is the `W_{N_g p^r}`-twist of the *other* tame push-down. This is a
   bookkeeping fact about BCPV's construction, not an obstruction to MPC; the referee should decide which push-down
   H9R16-A/B used.
5. **Is D4 formal on the corrected carrier?** — 05 §3 (yes, given (AJ-corr)); the only unpinned item is the exact numbered
   reference for (AJ-corr) (Jannsen LNM 1400 §9 / Nekovář 2000 §1). Attack surface: the orientation of `Γ_A` (transpose)
   — a wrong orientation replaces `⟨y_2, A y_3⟩` by `⟨A y_2, y_3⟩ = ⟨y_2, A^t y_3⟩`, `A^t = (U_p)^r W`; this changes which
   side carries `U'_p` vs `U_p`, a convention to be matched against H9R16-A/B, not a mathematical gap.

## Do-not-redo / do-not-use

* Do not look for a `p`-power in `d_r`; the `p`-powers of Hida (6.6)/KLZ17 Prop 2.4.5 live in `ϖ_{i,*}ϖ_j^*`, not in `ϖ_2^*ϖ_{1,*}`.
* Do not use BCPV (4.9) (prohibited; also off by `p^2` per Lanes 2/4). Use DR22 Lemma 2.8's `μ^*μ_* = Σ_K⟨d⟩`.
* Do not replace full-level `W_{Np^s}` by `W_{p^s}` (introduces `⟨p⟩_N`, BSV22 (68)).
* Do not import Hida's `w`-twisted tower; nothing here needs `w_r`, `π^r_s`, `⟨u_r⟩`, `⟨c_r⟩`.
* Do not read `N_{r+1,r}` as the scalar `p`: it is the scalar only after `p_{r+1,r}`.

## Open for the referee (not for this lane)

* R1. Pin (AJ-corr) to a numbered statement (05 §1).
* R2. Identify H9R16-A/B's `P_r^{tr,†}` with `P_r[[a,b,c]]` of 05 §2 (type B via diamonds; tame `ε_g^{-1}` twist on factor 3).
* R3. Decide which tame push-down (forgetful vs quotient) H9R16-A/B used at the common→native step (04 §3, item 4 above).
* R4. If Aristotle is to be used: the compact exact statement is L5-T2 + L5-T3 as identities of double-coset operators on
  `H_1(Γ_1(Np^{r+1})\H*, cusps)` — a finite computation for each `(N,p,r)`, but the general-`r` theorem needs the
  moduli/coset argument, which is not in any formal library. ARISTOTLE_READY = NO for the general theorem; a per-case
  certificate is what `_verify/msym_check.py` already is (over `F_ℓ`; an exact-`Q` rerun is a 10-line change).

## Custody

Lane directory `~/H9R16C_LANE5_MPC_PROVER_2026-09-15/`: 00–08, `sources/` (PDF/TeX/txt copies), `_verify/` (script + log).
Nothing sealed, nothing sent, no Lean, no Aristotle. Independence: Lanes 1–4 were read only through their 00/04/05
files and the Lane 2 `03_4` and Lane 4 `03 §7` sections, *after* 02/03 were written; Lane 2's expected `ν` was not
imported (it was derived under a hypothesis there; here it is proved).
