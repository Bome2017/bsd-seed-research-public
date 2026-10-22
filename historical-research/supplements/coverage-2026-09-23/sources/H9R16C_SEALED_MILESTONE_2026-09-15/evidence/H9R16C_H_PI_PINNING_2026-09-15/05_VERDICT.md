# 05 — Verdict

## §1. Verdict

**H_PI_PROVED.**

> Let `p` be odd, `p ∤ N_g`, `r ≥ 1`, `X^g_s = X_1(N_gp^s)`, `S_s = H^1_ét(X̄^g_s, Z_p(1))` (or the
> open model `H^1_ét(Ȳ^g_s, Z_p(1))`), `ϖ_1(A,P) = (A,pP)`.  There is a **unique** homomorphism of
> `Z_p`-algebras `π_r : 𝕋'_{N_gp^{r+1}} → 𝕋'_{N_gp^r}` with
>
>     ϖ_{1,*} ∘ t = π_r(t) ∘ ϖ_{1,*}      in Hom_{Z_p}(S_{r+1}, S_r),  for every t.
>
> On generators `π_r(T'_ℓ) = T'_ℓ`, `π_r(U'_p) = U'_p`, `π_r(U'_ℓ) = U'_ℓ`,
> `π_r(⟨d̃⟩) = ⟨d̃ mod N_gp^r⟩`.  It is **surjective** (and never injective for `r ≥ 1`).  It
> satisfies `π_r(e'_ord) = e'_ord`, hence restricts to a surjective ring homomorphism
> `π_r : R_{r+1} ↠ R_r` on `R_s = e'_ord𝕋'_{N_gp^s}` with the same intertwining on `e'_ord`-parts.

**Surjectivity of `π_r` IS included in the verdict** — it is Theorem 4.1 of `03` and is the cheap
half: once `π_r` is well defined, the generators of `R_r` are hit by the like-named generators of
`R_{r+1}` (the diamonds because `(Z/N_gp^{r+1})^× ↠ (Z/N_gp^r)^×`).

One-line summary of the proof: **`ϖ_2^*` — not `ϖ_1^*` — is an injection `S_r ↪ S_{r+1}`
equivariant for the primed operators, so every relation holding at level `r+1` holds at level `r`;
that gives the ring map, multiplicativity then propagates the four printed/proved generator
intertwinings of `ϖ_{1,*}` to all of `R_{r+1}`, and uniqueness follows from `ϖ_{1,*}ϖ_1^* = p^2` on a
torsion-free module.**

What it needs: (G2) `ϖ_{1,*}U'_p = U'_pϖ_{1,*}` — **printed**, DR22 §1.3 (`DR22.tex` l.1220–1222,
l.1569); Ohta99 (1.5.4) p.252 for `W_LT'_nW_L^{-1} = T_n`, `W_L⟨d⟩W_L^{-1} = ⟨d⟩^{-1}`; Poincaré
duality with the projection formula; and (for the sharper uniqueness only) Ohta99 Lemma (1.2.12)
p.249.  Everything else is proved in `03`.

## §2. Integral, or only after inverting `p`?

**Fully integral over `Z_p`.  `p` is never inverted, anywhere in the statement or the proof.**

* `𝕋'_s` and `R_s` are `Z_p`-algebras; `π_r` is a `Z_p`-algebra map; the intertwining is an identity
  in `Hom_{Z_p}(S_{r+1}, S_r)`.
* `deg(ϖ_1) = p^2` enters only through `ϖ_{1,*}ϖ_1^* = p^2`, and only to conclude
  `s·p^2 = 0 ⟹ s = 0` **from torsion-freeness of `S_r`** — a cancellation, not a division.
* The only inverse that appears in the surrounding machinery, `(U'_p)^{-1}`, exists **integrally** on
  `e'_ord`-parts by the definition of `e'_ord`; the consumers' normalisation `(U'_p)^{-2(r+1)}` is
  therefore integral and `π_r` moves past it integrally (`π_r(U'_p) = U'_p`).
* Where integrality could have failed and does not: the identification of the primed and unprimed
  Hecke algebras is via `W_L`, whose square is a **diamond** — a unit of `𝕋'` — not `p^k`; and
  Ohta's Eichler–Shimura comparison, which is printed only over `Q` (`02` §3), is **not used**: the
  proof runs entirely inside `End_{Z_p}(S_s)`.
* Caveat, stated: on the Mordell–Weil carrier `Ĵ_s = J_s(k)⊗Z_p` the *existence* and *surjectivity*
  clauses transport by functoriality, but **uniqueness** does not — `Ĵ_s` can have `p`-torsion, so an
  operator killing `Ĵ_r[p^∞]` is invisible there.  Uniqueness must be quoted from the `S_s` form, as
  `01` §3.3 and `03` Cor. 3.3 do.  Consumers that need a uniquely-determined `π_r(t)` acting on
  `e'Ĵ` must obtain it as the image of the `S`-level `π_r(t)`.

## §3. Is ordinarity needed?

**No.  H_pi is not an ordinary statement.**

* (G1)–(G4) are proved on the whole of `S_{r+1} → S_r`.
* Well-definedness (`03` Thm 3.1) uses only that `ϖ_2^*` is injective and equivariant on the whole
  of `S_r`; `e'_ord` plays no role.
* So `π_r : 𝕋'_{N_gp^{r+1}} ↠ 𝕋'_{N_gp^r}` exists, is unique and is surjective **before** any
  ordinary projection.
* Ordinarity enters only afterwards, and only as bookkeeping: because `π_r(U'_p) = U'_p` and `π_r` is
  continuous (finite `Z_p`-algebras), `π_r(e'_{r+1}) = e'_r`, so `π_r` descends to the quotient rings
  `R_s = e'𝕋'_s` (`03` §5).  That descent is where the consumers actually live.
* Two places where ordinarity is genuinely *useful* but not *necessary*: (i) it makes `U'_p`
  invertible, which the consumers need for `(U'_p)^{-2(r+1)}` — not for H_pi; (ii) it upgrades
  uniqueness from "`im(ϖ_{1,*})` has finite index" to "`ϖ_{1,*}` is onto" (Ohta99 (1.2.12)).  Both
  are strengthenings, not hypotheses.

Consequence worth flagging to the assembly: the second referee's `10_VERDICT.md` records `H_π` as
"the single unproved load-bearing input of the whole assembly, used three times".  All three uses —
Lemma (L), moving `res^bal` past `(U'_p)^{-2(r+1)}`, and `π_r^*` injectivity in C8 — are discharged
by `03` §6, integrally, with surjectivity, for all odd `p`.

## §4. Dependency audit of the verdict

| depends on | status |
|---|---|
| DR22 §1.3, `ϖ_{1,*}U'_p = U'_pϖ_{1,*}` | printed; re-verified numerically (`04` §2) |
| Ohta 1999 (1.5.4), p.252 | printed, in hand |
| Ohta 1999 Lemma (1.2.12), p.249 | printed, in hand (used only for the sharper uniqueness) |
| **Ohta 2000 (Math. Ann. 318)** | **NOT_OBTAINED — and NOT USED.**  The verdict does not depend on it |
| KLZ17 `prop:controlthm` / `thm:ordinaryfiltration` | not used; in particular KLZ17's standing hypothesis `p ≥ 5` is not inherited, and `p = 3` is covered (and exercised numerically) |
| Hida, *Control of Λ-adic MW groups* / *Limit MW groups* | not used in the proof; cited in `02` §4 as the printed analogue for the **unprimed** algebra on Jacobians |
| BCPV (4.9) | not used (prohibited) |
| any weight-one specialization | none |
| any Selmer / Sha / `L`-value / control-theorem input | none |

## §5. Residual risk, stated plainly

1. `(G2)` is **cited, not re-proved** here.  It is the one black box.  It is printed twice in DR22
   §1.3 and verified in 10 independent exact runs in `04`; DR22 give no proof of it either.  If a
   referee insists on a proof, the route is the explicit `π_{1*}π_2^*` computation on `X_{r,r+1}`
   (DR22 l.1157–1165) — not attempted here, since the prompt lists it as printed.
2. The proof uses `W_L` as a `Z_p`-module automorphism of the **geometric** cohomology.  `W_L` is
   defined over `Q(μ_{N_gp^r})`, so it is **not** `G_Q`-equivariant.  This is harmless because H_pi is
   a statement about `Z_p`-linear endomorphisms only — but any consumer that wants a `G_Q`-equivariant
   refinement of the *proof* (as opposed to the statement) must not import `W` into it.
   The `ℓ ≠ p` clauses have a `W`-free proof (`03` §1.2 and the remark after Prop. 2.4); only the
   `U'_p` clause of Prop. 2.4 uses `W`.
3. `04` is five levels in weight 2 on a Betti carrier.  It cannot prove the theorem and is not
   claimed to; it is a falsification attempt with three deliberately-chosen negative controls, all of
   which fired correctly.
4. Absolute `Z_p`-rank values for the ordinary algebras in the two largest PART B cases carry `±1`
   truncation uncertainty (`04` §4.3).  The verdict does not rest on them.

## §6. Files written by this lane

`00_TASK.md`, `01_STATEMENT_AND_TYPES.md`, `02_LITERATURE.md`, `03_PROOF_OR_OBSTRUCTION.md`,
`04_NUMERICS.md`, `05_VERDICT.md`, `06_FILES_CONSULTED.sha256`, and
`_verify/{msym_check.py (copied, unmodified), hpi_gens.py, hpi_ring.py, *.log}`.
Nothing outside `/Users/bsm/H9R16C_H_PI_PINNING_2026-09-15/` was created or modified.
