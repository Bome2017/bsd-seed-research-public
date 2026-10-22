# 07 — Coordinator audit of the H_pi return (2026-09-15)

## §1. The proof, checked

The core move — `ϖ_2^*` carries the **primed** ring while `ϖ_1^*` carries the **unprimed** one — was
derived independently in the coordinating session while auditing the second referee, by the same
W-conjugation:

    ϖ_2^*U'_{p,r} = W_{r+1}ϖ_1^*W_rU'_{p,r} = W_{r+1}ϖ_1^*U_{p,r}W_r = W_{r+1}U_{p,r+1}ϖ_1^*W_r = U'_{p,r+1}ϖ_2^* .

Agrees. The three load-bearing steps also check:
* **Well-definedness (Thm 3.1).** If `ev_{r+1}(P) = 0` then `ϖ_2^*ev_r(φ_rP) = ev_{r+1}(P)ϖ_2^* = 0`, and
  `ϖ_2^*` is injective, so `ev_r(φ_rP) = 0`. The kernel inclusion runs *against* `ϖ_{1,*}`, which is why
  (G1)–(G4) alone cannot supply it. Correct, and it is the real content.
* **Uniqueness.** `sϖ_{1,*} = 0 ⟹ sp^2 = 0 ⟹ s = 0` on a torsion-free module. Correct; `p` is cancelled,
  never inverted.
* **Surjectivity.** Generators to generators plus `(Z/N_gp^{r+1})^× ↠ (Z/N_gp^r)^×`. Correct.

## §2. Numerics: the failures are exactly the negative controls

`hpi_gens.log` shows 61 FAILs. Every one is a **predicted-negative control**, by label:
`(E1) ϖ_1^* vs U'_p` (10 runs), `(E2) ϖ_2^* vs unprimed U^t` (10), `(G) ϖ_{1,*} vs unprimed U^t` (10).
No real check fails. The controls firing is what distinguishes this theorem from Hida's printed
(unprimed) tower — if they had passed, the result would have been vacuous.

`hpi_ring_B2/B3` FAILs are **only** the `(RELIABLE)` rank-precision flag ("raise K"). The check the
argument rests on, `(WD-ord) π_r well defined on R_{r+1} → R_r`, **PASSES** in every case, with
`(NONVAC)` confirming the test has content (83, 69 and 46 independent level-`pM` relations). The verdict
does not rest on the absolute rank values, and says so.

Custody: all 46 Lane 1–5 files unchanged; the copied checker is byte-identical to Lane 5's (`f99115c1…`).

## §3. One citation defect — and it is the same slip Lane 3 caught in BCPV

The verdict cites **Ohta99 (1.5.4), p.252** for `W_LT'_nW_L^{-1} = T_n` on cohomology. The source reads:

> `(1.5.4)` … both on `M_k(Γ_r)` and `S_k(Γ_r)`. **Thus** `H_k(Γ_r;R)` and `H^*_k(Γ_r;R)` are canonically
> isomorphic via the correspondence `T(n) ↔ T^*(n)` and `T(q;q) ↔ T^*(q;q)`.

So `(1.5.4)` proper is the identity **on modular forms**; the cohomological statement is the *sentence
following it*. Lane 3 recorded exactly this about BCPV: "(1.8)–(1.9) cite Ohta (1.5.4), which is an
identity about modular forms only". **The same slip has now been made twice, independently.** Correct
citation: *the sentence following Ohta99 (1.5.4), p.252.*

Cost: nil. The fact needed is printed there, and it is over-determined anyway — Lane 5's L5-T1 (proved,
numerically verified by two non-communicating implementations) gives `ϖ_2^* = Wϖ_1^*W`, and the
`W`-intertwining of `U'_p` with `U_p` is BSV22 (68) and Lane 5's check `(vi-c)`. The `ℓ ≠ p` clauses have
a `W`-free proof in `03` §1.2 regardless.

## §4. Where this leaves H9R16-C

`H_π` was the single unproved load-bearing input, named independently by both referees. It is now proved
integrally, with surjectivity, for **all odd `p`** (including `p = 3`), with **no ordinarity hypothesis**,
without Ohta 2000 (still NOT_OBTAINED) and without KLZ17's `p ≥ 5`. The residual list for H9R16-C is now:

1. `(AJ-corr)` — the numbered citation for étale Abel–Jacobi functoriality under correspondences (R1),
   frozen `PROVED_FORMAL` by the operator;
2. `(G2)` `ϖ_{1,*}U'_p = U'_pϖ_{1,*}` — printed twice in DR22 §1.3, proved nowhere there, verified in ten
   exact runs here. This lane correctly calls it the one black box;
3. the tame push-down convention — `NOT_PRINTED` in BCPV, shown immaterial to the tower by both referees.

None is an unproved mathematical step of the assembly itself.
