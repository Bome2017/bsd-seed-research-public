# 00 — SEALED MILESTONE: H9R16-C (finite point tower) + H_π

**Sealed 2026-09-15**, by operator instruction, in the session that ran the lanes and audits recorded here.
This object is deliberately narrow. It seals a finite-level geometric result and one Hecke-algebra input.
It seals **nothing** about the big-trace comparison or about any target application. See `05_NON_CLAIMS.md`.

## Status block (operator's own wording, 2026-09-15)

    H9R16C                    = CLOSED
    MPC                       = PROVED
    d_r                       = 1
    H_π                       = PROVED
    POINT TOWER               = CONSTRUCTED / COMPATIBLE
    BIG TRACE FOR CH TARGET   = STILL UNDER ω-REBUILD      ← NOT part of this seal

## The sealed theorem

Let `p` be odd, `N_f`, `N_g` tame levels prime to `p`, `N = lcm(N_f,N_g)`, `K_0 = Q(μ_p)`,
`F'_r = Q(μ_{Np^r})`, `X^g_s = X_1(N_gp^s)`, `J^{(1)}_r = Jac X_1(N_fp^r)`,
`A_r = W_{N_gp^r}^{-1}(U'_p)^r`. Define

    R_r      := e'_ord𝕋'_{N_gp^r} ⊗ Z_p                      (NATIVE level)
    B^bal_r  ≅ R_r    — after the A_r-transport and passage to the transported commutative primed
                        ordinary Hecke model (ι_r(u') = A_r^{-1}ρ_r(u')A_r = u'); finite free over Z_p
    𝒫^♮_r    := Hom_{Z_p}(B^bal_r, Ĵ^{(1)}_r(F'_r)^{ord})^{Gal(F'_r/K_0), ⋆}
    Q_r      := (U'_p)^{-r}_{(1)} ∘ Φ̄^mod_r ∘ (U'_p)^{-2r}_{carrier}  ∈ 𝒫^♮_r
    τ_r^MW(x):= ϖ^{(1)}_{1,*} ∘ x ,   π_r^*(y) := y ∘ res^bal_{r+1,r} ,
    N_{r+1,r}:= Σ_{d ≡ 1 mod N_gp^r} ⟨d⟩        (the order-p diamond norm element)

> **Theorem (H9R16-C).** For every `r ≥ 1`,
>
>     τ_r^MW(Q_{r+1}) ∘ (1 ⊗ N_{r+1,r})  =  π_r^*(Q_r)
>
> in `Hom_{Z_p}(B^bal_{r+1}, Ĵ^{(1)}_r(F'_{r+1})^{ord})`, **integrally, with constant exactly 1**, for
> either tame degeneracy map used uniformly in `r`. Consequently the system `𝒬_∞ = (Q_r)_{r≥1}` built from
> BCPV's own cycles lies in
>
>     𝒫^♮_∞ := { (Q_r)_r ∈ ∏_r 𝒫^♮_r : the relation above holds for all r } ,
>
> a module over Hida's big ordinary Hecke algebra `𝕋'_∞(N_g) = lim_r R_r`, carrying the tame `ε_g^{-1}`
> twist inside `⋆`. The naive inverse limit along `ϖ_{1,*}` alone is **not** this object.

Full statements of every ingredient: `01_THEOREMS.md`.

## Evidentiary tier

* **Two independent assembly audits**, the second run behind a hard file-level independence wall, agreeing
  on every load-bearing claim (`02_AUDIT_RECORD.md`).
* **Every load-bearing input either proved in a lane or printed**, with `H_π` — the last unproved one,
  identified independently by both audits — now proved (`01` §7).
* **Numerical corroboration by non-communicating implementations**: the tame transport `L5-T5` was checked
  by three separate scripts written without sight of each other; MPC itself in 7 cases × 2 primes.
* **Residuals are citation items only** (`04_RESIDUAL_CITATIONS.md`), not unproved steps of the assembly.

## Directory

    00_MILESTONE.md            this file
    01_THEOREMS.md             exact statements of everything sealed
    02_AUDIT_RECORD.md         the two independent audits, what each verified and found
    03_CORRECTIONS_LEDGER.md   every correction made to the record along the way
    04_RESIDUAL_CITATIONS.md   the three open citation items
    05_NON_CLAIMS.md           what this object does NOT claim, and the downstream work
    06_CUSTODY.sha256          hashes of everything in this seal and of the sources relied on
    evidence/                  copies of the lane deliverables, audits, scripts and logs (101 files)
