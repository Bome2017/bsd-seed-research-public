# 11 — Coordinator audit of the referee return (2026-09-15, after 09)

Not a second adversarial pass. This records what the coordinating session verified independently, and one
addition to the gate statement. Nothing in 00–10 is modified.

## §1. Verified independently

1. **Custody.** All 46 Lane 1–5 deliverables re-hashed against `_work/LANE_FILES_AT_LAUNCH.sha256`: every
   file unchanged. The referee wrote only 03–10 and `_verify/`.
2. **New numerics re-read.** `_verify/tame_check.log`: 3 cases (N_g,t,p,r) = (3,3,2,1), (5,3,2,1), (5,2,3,1),
   two primes, 91 checks, 0 FAIL — including A5 (L5-T5), which no earlier lane exercised, and the composite
   (★) `A_r pr^t_{1,*} W_{Np^r} = (U_p)^r pr^t_{2,*}`.
3. **(★) re-derived by hand:** `A_r pr^t_{1,*}W_{Np^r} = W_g U'^r_g pr^t_{1,*}W_c = W_g pr^t_{1,*}U'^r_cW_c
   = W_g pr^t_{1,*}W_cU^r_c = W_gW_g pr^t_{2,*}U^r_c = U^r_g pr^t_{2,*}`, using (C-U), `U'_pW = WU_p` and
   A5. Agrees.
4. **Level-step U'_p bookkeeping (05 §3.3) recomputed:** moving `U'_p` off slot 2 by adjunction gives `U_p` on
   slot 3, converted by `U_pA_r = A_rU'_p`; so `(U'_p)^{⊗3}` leaves one `U'_p` on the output and `(U'_p)^2` on
   the carrier. Agrees.
5. **μ_r computation (06 §2) recomputed:** the d_1-sum contributes `p^{r−1}`, the (d_2,d_3)-sums give
   `(Σψ^{-1})^2` on a branch with carrier character ψ — `|G_r|`-or-`0`, as stated, not a uniform rescaling.
6. **Citations behind the R3 decision spot-checked in the local TeX:**
   - KLZ17 l.541–551: `pr_1(E,e_1,e_2) = (E,e_1,Ae_2)`, `pr_2` the quotient, **for arbitrary `A`**, with
     "`pr_1` and `hpr_1` correspond to the identity map on `(Z/MZ)^* × H`". Accurate.
   - KLZ17 l.800: "if `N` is any common multiple of `N_f` and `N_g`, there is a natural degeneracy morphism
     `Y_1(N)^2 → Y_1(N_f)×Y_1(N_g)`. Pushforward … defines a projection map `pr_{f,g}`". Accurate — and it
     does **not** name an index, which is why 05 §1 classifies the forgetful reading as inherited convention,
     `NOT_PRINTED`. That classification is the honest one.
   - DR22 l.1145–1154 (`ϖ_1`: `(A,P) ↦ (A,pP)`, `τ ↦ τ`; `ϖ_2`: quotient, `τ ↦ pτ`). Accurate.
   - BCPV footnote 11, l.1647: `Z := X_{23}` the diagonal, `Π_Z := X_{14} × Z`, and `𝒵_r` is represented by
     `Π_Z`. Accurate, and it is what fixes the orientation in 03 §2.4.

## §2. Addition to the gate statement (08 §3–§4), not to the closure

The closure is proved for a **fixed cycle index** `e = (a,b,c)` (03 §4). Over `K_0 = Q(μ_p)` that is
legitimate: `σ ∈ Gal(F'_r/K_0)` has `m ≡ 1 mod p`, so the index-shift law `σ_mΔ^ét[e] = Δ^ét[m^{-1}e]`
(BCPV l.1257) fixes `e`. BCPV's class, by contrast, is the symmetrized
`Δ_r^ét = (p^3/(p−1)^3)Σ_{a,b,c∈F_p^×}Δ_r^ét[[bc,ac,ab]]` (l.1396–1399), which is what descends to `Q`
(`lemma_Gal_action_on_bold_Delta`(ii), l.1390–1392).

06 §5 correctly notes that both sides of the tower relation acquire the same factor, so **the closure is
unaffected**. But `G_BIG_KUMMER_TRACE` compares against the symmetrized class over `Q`, so the
**index/symmetrization dictionary** — which `Z_p`-combination of indices the point system must carry, and
where the `p^3/(p−1)^3` sits on the point side — belongs in 08 §4's table beside the `(U'_p)^{-r}/(U'_p)^{-2r}`
and `a_p(g)^rλ_{N_gp^r}(g)^{-1}` rows. Recorded here so the gate does not start without it.

## §3. Residuals carried by the referee (none used in its proof), repeated for the record

1. `(AJ-corr)` numbered citation still unpinned (R1); frozen `PROVED_FORMAL` by the operator.
2. `H_π` (ring maps `π_r` with `ϖ_{1,*}t = π_r(t)ϖ_{1,*}`): standard Hida theory, part of the statement.
3. Tame push-down scalar at `ℓ | t` (05 §5): immaterial to H9R16-C, must be fixed before naming
   `λ_{N_gp^r}(g)` or `a_p(g)^{±r}`.
4. Drive checkpoint `NOT_OBTAINED`; the two local copies of §C agree on every load-bearing formula.

## §4. Status of this audit

Custody, numerics, the four load-bearing citations and four computations check out. The structural arguments
of items 1, 2 and 5 were read and are coherent, but reading is not an independent second derivation: if the
same standard applied to MPC (a separate prover and a separate adversarial lane) is wanted here, a second
referee over 03–08 is the way to get it. That is the operator's call.

## §5. Wording requirement carried into every later freeze (operator instruction, 2026-09-15)

The identification `B_r^bal ≅ R_r` must always be written with its hypothesis:

> **after the `A_r`-transport and passage to the transported commutative primed ordinary Hecke model**
> (`ι_r(u') = A_r^{-1}ρ_r(u')A_r = u'`, §C),

i.e. `B_r^bal = R_r ⊗_{R_r} R_r ≅ R_r` holds for the *transported* carrier, where both auxiliary factors are
modules over the same commutative `R_r = e'_ord𝕋'_{N_gp^r}⊗Z_p`. It must **not** be applied to the raw,
pre-transport `g` / `g^c` correspondence modules, whose two geometric Hecke actions are related by the
anti-involution `ρ_r` and must not be identified naively (§C, "G_c / DUAL-MODEL CAUTION").
