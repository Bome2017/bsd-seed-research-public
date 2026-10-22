# 12 — Coordinator audit of the SECOND referee's return (2026-09-15)

## §1. Independence wall: honoured

* `11_FILES_CONSULTED.sha256` cites **no** walled file (checked by pattern for all eleven paths in 00 §2).
* The one `ls -la` of the first referee's directory is disclosed in 10 §"Independence-wall disclosure"; names
  and sizes only, and the names were already printed in its own charter. Acceptable, and disclosed unprompted.
* The first referee's files are untouched (timestamps 16:12–16:24, unchanged; the only later mtime in that
  directory is my own `11_COORDINATOR_AUDIT.md`).
* Lanes 1–5: all 46 files re-verified byte-identical against `_work/LANE_FILES_AT_LAUNCH.sha256`.

## §2. The two defects, checked

**D-C1 (rank clause).** Correct catch. `T^♮_r = Hom_{Z_p}(B^bal_r, T_pJ^{(1),ord}_r)`, so the second factor is
`rank(e'_ord T_pJ^{(1)}_r)`, and the ordinary part is a proper summand for `r ≥ 2`. The clause originated in the
first referee's `06` §3 and **I copied it verbatim into the claims file C1**; so the defect is in the first
referee's bookkeeping *and* in my transcription. Operative content ("no `|G_r|`") is unaffected.

**D-C2 (orientation).** Correct, and it is the more interesting of the two. Re-derived here independently:
in weight 2, `W^2 = id` gives `W^t = W`; `WU'_p = U_pW` gives `W(U'_p)^r = (U_p)^rW`; hence

    A_r^t = ((U'_p)^r)^t W^t = (U_p)^r W = W (U'_p)^r = A_r .

`A_r` is self-adjoint, so **both orientations of `Γ_A` induce the same bilinear form**. This retires, as vacuous
in weight 2: Lane 5 `07` item 5's orientation caveat, the first referee's `03` §2.4 (which reached the right
conclusion by a longer route and honestly recorded that its tests did not separate the two), and pressure point
P5 of `02` §D, which I wrote. Nil scope, in the safe direction.

## §3. What the second referee adds, beyond confirming

1. `A_r` self-adjoint (§2).
2. The diamond action on `Δ^ord` is the `W`-inverted one (`⟨a,a,a⟩Δ^ord[d] = Δ^ord[a^{-2}d]`), which **forces**
   Lane 4's `+1/2` exponent rather than leaving it a convention.
3. Three mandatory narrowings on C1: `R_r` native-level (not Lane 2 `01` T3's common-level algebra); both
   auxiliary coefficient modules must be the regular `R_r`-module (Lane 4 `01` §6 leaves them undefined); the
   `Hom`/`H^1` interchange is for `F ⊇ Q(μ_N)` and **must not** be applied to the ⋆-module over `K_0`.
   Commutativity of `𝕋'` is load-bearing because `ρ_r` is an anti-involution.
4. C5 sharpened: the two tame push-downs differ by `pr^t_{2,*} = W_{N_gp^s}∘pr^t_{1,*}∘W_{Np^s}` (i.e. A5
   rearranged), not by "a tame Hecke scalar" — a single scalar exists only after projecting to lines on which
   each `W` acts by a scalar. **This corrects the phrasing H9R17 used for its (P) hypothesis** (H9R17 `04` §0,
   `05` §3); it does not change H9R17's conclusion, which does not depend on the scalar's shape.
5. Lane 4 `04`'s `(T♮_r)` as printed cannot be rescued by any diamond **unit** `δ♮_r`, because `N_{r+1,r}` is a
   non-unit zero-divisor (`N^2 = pN`). Sharper than the first referee's wording defect.
6. C8's negative clause proved in the sharper form `(1−p)π_r^*Q_r = 0 ⇒ Q_r = 0`: the naive `ϖ_{1,*}`-limit meets
   the C4-system only in `0`.

## §4. `H_π` is now the single unproved load-bearing input

Both referees, independently, identify `H_π` — the ring maps `π_r : e'𝕋'_{r+1}⊗Z_p → e'𝕋'_r⊗Z_p` with
`ϖ_{1,*}t = π_r(t)ϖ_{1,*}` — as a standing input, proved in no lane. The second referee locates it precisely:
consumed three times (its Lemma (L); moving `res^bal` past `(U'_p)^{-2(r+1)}`; C8's injectivity, which needs
`π_r` **surjective**). Everything else in the assembly is now either proved in a lane or an explicit hypothesis.
Pinning `H_π` (existence of the ring map on generators, and surjectivity) is the one remaining conversion of a
SUPPORTED input into a VERIFIED one.

## §5. Numerics

`_verify/transport_check.py`: 124 exact checks, two primes, 0 failures — the `A_r`-transport on every generator,
`ρ_r(t_2)A_rt_3 = A_rt_2t_3` on random products, `U_pA_r = A_rU'_p`, `WT_ℓW = ⟨ℓ⟩^{-1}T_ℓ`, `A_r^t = A_r`, and a
tame block for **both** push-downs. Independent of the first referee's 91-check tame script (walled), so A5 now
has **two independent numerical confirmations** by non-communicating implementations. The referee also records a
failed first attempt at its own `T'_ℓ` coset construction rather than discarding it — correct practice.

## §6. Where this leaves H9R16-C

Two audits, independently derived, agree on every load-bearing claim: the carrier collapse (with three
narrowings), Hom-valued D4, the tower relation with constant exactly 1, no rank factor, tame-twist preservation,
and the inverse-limit module. The two defects found are in clauses that carry no weight, one of which simplifies
the theory. The remaining items are `H_π` (§4), the `(AJ-corr)` citation, and the `NOT_PRINTED` tame push-down.
