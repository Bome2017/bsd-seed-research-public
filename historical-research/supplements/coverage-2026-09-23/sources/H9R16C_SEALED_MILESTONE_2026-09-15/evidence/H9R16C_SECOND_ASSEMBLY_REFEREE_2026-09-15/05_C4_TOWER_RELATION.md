# 05 — C4 (tower relation, constant 1) + C4b + C4c  [SECOND referee, independent]

**Verdict: C4 CONFIRMED (conditional on `H_π`, which 01 declares to be part of the statement).
C4b CONFIRMED. C4c CONFIRMED.** Derived below from scratch; no step is "formal".

## §1. The étale level-step lemma

**Lemma (L).** For every `z ∈ H^1(F'_{r+1}, S_{r+1}^{⊗3}(2))` and every `b' = [t'_2⊗t'_3] ∈ B^bal_{r+1}`,

    ϖ^{(1)}_{1,*}( Contr_{r+1}^{A_{r+1}}([t'_2 ⊗ N_{r+1,r}t'_3])(z) )
        =  Contr_r^{A_r}( [π_r(t'_2) ⊗ π_r(t'_3)] )( ϖ^{⊗3}_{1,*} z ).

*Proof.* Evaluate both sides on `y_1⊗y_2⊗y_3` and write `Y_i := pd^t_*y_i ∈ H^1(X_1(N_gp^{r+1}))`.

Factor 1. `pd^{t_f}_*∘ϖ_{1,*} = ϖ_{1,*}∘pd^{t_f}_*`: the tame and `p` degeneracies commute
(`(A,P) ↦ (A,pP) ↦ (A,t_fpP)` either way; for the quotient variant the two subgroups have coprime
order). *Numerically confirmed for both choices of tame map* — `_verify/transport_check.py` (T4g).

Factors 2,3. `pd^t_*ϖ_{1,*}y_i = ϖ_{1,*}Y_i` by the same commutation. Then

    ⟨ϖ_{1,*}Y_2, ρ_r(π_rt'_2) A_r π_r(t'_3) ϖ_{1,*}Y_3⟩_{N_gp^r}
  = ⟨ϖ_{1,*}Y_2, A_r π_r(t'_2t'_3) ϖ_{1,*}Y_3⟩             [transport at level r + commutativity, C1]
  = ⟨ϖ_{1,*}Y_2, A_r ϖ_{1,*}( t'_2t'_3 Y_3 )⟩               [H_π:  ϖ_{1,*}t = π_r(t)ϖ_{1,*}]
  = ⟨Y_2, A_{r+1} N_{r+1,r} t'_2t'_3 Y_3⟩_{N_gp^{r+1}}      [A1 = MPC_r, pairing form, d_r = 1]
  = ⟨Y_2, ρ_{r+1}(t'_2) A_{r+1} N_{r+1,r} t'_3 Y_3⟩          [N central; transport at level r+1]

which is the level-`(r+1)` contraction of `[t'_2⊗Nt'_3]`. ∎

Two things this proof does **not** need, and must not be given: BCPV (4.9) (prohibited), and the
tame-`W` interchange A5 — the common-level `W_{Np^s}` never leaves the definition of `Δ^{ord}_s`,
and the native-level `W_{N_gp^s}` never leaves `A_s`. A5 is needed only for C5.

## §2. The `U'_p` bookkeeping lemma

**Lemma (U).** `Contr_r^{A_r}(b) ∘ (U'_p)^{⊗3} = U'_{p,(1)} ∘ Contr_r^{A_r}( b·(U'_p)^2 )`.

*Proof.* `pd_*U'_p = U'_ppd_*` (T4c/T4d, numerically confirmed), so factor 1 yields `U'_{p,(1)}`
outside. In the pairing, factor 2's `U'_p` crosses by adjunction as `ρ_r(U'_p) = U_p`, and
`U_pA_r = A_rU'_p` (transport; T1b), so it lands on the carrier; factor 3's `U'_p` is already there.
**Exactly one `U'_p` on the output and exactly two on the carrier, per level.** ∎

This is the operator content of the pair `a_p(f)^{-r}`, `a_p(g)^{-2r}` in BCPV Lemma l.1490, and it
is the contraction of BCPV's own `(U'^{⊗3}_p)^{-r}` of Def 4.12 (l.1438): factors 2 and 3 both become
the carrier, so `(U'_p)^{-r}⊗(U'_p)^{-r} ↦ (U'_p)^{-2r}`.

## §3. The unnormalized tower identity

Take `z = res_{F'_{r+1}}Δ^ét_{r+1}[e]`. BCPV Cor 4.11(i) (`cor_DR_lemma_2_5_dual`, l.1422–1430)
gives `ϖ^{⊗3}_{1,*}Δ^ét_{r+1}[a,b,c] = U'^{⊗3}_pΔ^ét_r[a,b,c]` **at fixed index**, with `a,b,c ∈ F_p^×`
"regarded as elements of `(Z/p^r)^×` via their Teichmüller lifts" — precisely C2's `e`, the same at
every level. (Its source `DR_lemma_2_5_dual`, l.1412, requires the level-`(r+1)` index to reduce to
the level-`r` one; Teichmüller lifts do.) No constant, no `p`.

Lemma (L) + Cor 4.11(i) + Lemma (U) + C3 (D4 at both levels) + B1 (Kummer naturality for `ϖ_{1,*}`):

    Kum( ϖ^{(1)}_{1,*} Φ̄^mod_{r+1}( (1⊗N_{r+1,r}) b' ) )
      = Kum( U'_{p,(1)} Φ̄^mod_r( (U'_p)^2 · res^bal_{r+1,r}(b') ) )   in H^1(F'_{r+1}, T_pJ^{(1),ord}_r).

Both arguments are points of `Ĵ^{(1)}_r(F'_{r+1})^{ord}` (the right-hand one lies in the subgroup
`Ĵ^{(1)}_r(F'_r)^{ord}`), so **evaluationwise Kummer injectivity over `F'_{r+1}`** (B1) gives the
point identity

    (★)   ϖ^{(1)}_{1,*} ∘ Φ̄^mod_{r+1} ∘ (1⊗N_{r+1,r})
            =  U'_{p,(1)} ∘ Φ̄^mod_r ∘ (U'_p)^2_{carrier} ∘ res^bal_{r+1,r} .

**C4c is exactly this step and is CONFIRMED**: no class over `K_0`, no `⋆`-descent, is used. (The
`⋆`-structure is needed only to say *where the two sides live*, which is C7.)

## §4. Normalizations: the constant is exactly 1

With `Q_s := (U'_p)^{-s}_{(1)}∘Φ̄^mod_s∘(U'_p)^{-2s}_{carrier}` (integral: `U'_p` is a unit on
`e'_ord`-parts, both on `R_s` and on `Ĵ^{ord}`):

    τ_r^{MW}(Q_{r+1})∘(1⊗N)
      = ϖ_{1,*}∘(U'_p)^{-(r+1)}_{(1)}∘Φ̄^mod_{r+1}∘(U'_p)^{-2(r+1)}_{carrier}∘(1⊗N)
      = (U'_p)^{-(r+1)}_{(1)}∘[ϖ_{1,*}∘Φ̄^mod_{r+1}∘(1⊗N)]∘(U'_p)^{-2(r+1)}_{carrier}
                                            [ϖ_{1,*}U'_p = U'_pϖ_{1,*} (A2); N central]
      = (U'_p)^{-(r+1)}_{(1)}∘U'_{p,(1)}∘Φ̄^mod_r∘(U'_p)^2_{carrier}∘res^bal∘(U'_p)^{-2(r+1)}_{carrier}
      = (U'_p)^{-r}_{(1)}∘Φ̄^mod_r∘(U'_p)^{2-2(r+1)}_{carrier}∘res^bal
                                            [res^bal∘(U'_p)_{r+1} = π_r(U'_p)_r∘res^bal = (U'_p)_r∘res^bal]
      = (U'_p)^{-r}_{(1)}∘Φ̄^mod_r∘(U'_p)^{-2r}_{carrier}∘res^bal
      = Q_r ∘ res^bal_{r+1,r}  =  π_r^*Q_r .                                            ∎

**Constant exactly 1**, integrally, in `Hom_{Z_p}(B^bal_{r+1}, Ĵ^{(1)}_r(F'_{r+1})^{ord})`. It is 1
because (i) `d_r = 1` in A1, (ii) Cor 4.11(i) carries no constant, (iii) the norm element is kept as
an **element** `N_{r+1,r}` on the carrier rather than projected to the scalar `p`.

The exponents are **forced**: writing `Q_s = (U'_p)^{-a(s)}_{(1)}Φ̄^mod_s(U'_p)^{-c(s)}_{carrier}`,
(★) gives `a(r+1) = a(r)+1`, `c(r+1) = c(r)+2`; so `(a,c) = (s, 2s)` up to an `s`-independent shift.

## §5. C4b (factor-1 normalization alone)

Put `Q̃_s := (U'_p)^{-s}_{(1)}∘Φ̄^mod_s` (Lane 4 `04` `(T♮_r)`, Lane 5 `05` §4 as literally written).
By (★), `τ_r^{MW}(Q̃_{r+1})∘(1⊗N) = π_r^*(Q̃_r)∘(U'_p)^2_{carrier}` — the leftover is exactly
`(1⊗(U'_p)^2)` on the carrier, matching `a_p(g)^{-2r}` of BCPV Lemma l.1490. **The constant is not 1.**
C4b CONFIRMED.

Two sharper remarks the ledger should carry:
* Lane 4's `(T♮_r)` as printed has neither the carrier normalization **nor** `(1⊗N_{r+1,r})`. Without
  the norm element, MPC cannot be applied at all, and the deficit `δ♮_r` would have to absorb
  `N_{r+1,r}^{-1}`. That is impossible inside "a `Q`-rational diamond **unit**" (Lane 4 `04` §5.1),
  since `N^2 = pN` makes `N` a non-unit zero-divisor. So `(T♮_r)` as literally printed is not
  repairable by any `δ♮_r` of the declared type; C4's form supersedes it.
* Lane 4 `03` §7's warning that "applying `ϖ_{1,*}` uniformly to all three factors after `A_r`-transport
  is a TYPE error" is answered, not contradicted: in Lemma (L) `ϖ_{1,*}` is applied on factor 1 only;
  the factor-2/3 transport is carried entirely by MPC, whose proof is where `W` converts `ϖ_1^*` into
  `ϖ_2^*`. The `ϖ^{⊗3}_{1,*}` appears only on the **untransported** class, which is Cor 4.11's own
  hypothesis.

## §6. Declared dependencies (not defects, but they are the load)

1. `H_π` — the ring maps `π_r : R_{r+1} → R_r` with `ϖ_{1,*}t = π_r(t)ϖ_{1,*}`, sending generators to
   generators (so `π_r(U'_p) = U'_p`, `π_r(⟨d⟩) = ⟨d mod N_gp^r⟩`, and `π_r` is onto). 01 states that
   this is part of the statement of C4 and is proved nowhere in the packet. It is used **three
   times**: in Lemma (L), in moving `res^bal` past `(U'_p)^{-2(r+1)}`, and (via surjectivity) in C8.
2. A6/D4 at both levels, A1 (MPC, `d_r = 1`), A2 (`N` central, `ϖ_{1,*}U'_p = U'_pϖ_{1,*}`),
   BCPV Cor 4.11(i) at fixed Teichmüller index, B1.
3. The tame push-down is fixed and uniform in `r` (C5).

## §7. Status

| sub-claim | status |
|---|---|
| Lemma (L) (level step of the contracted class) | PROVED (given `H_π`) |
| Lemma (U) (1 on factor 1, 2 on the carrier) | PROVED; numerically corroborated |
| `τ_r^{MW}(Q_{r+1})∘(1⊗N_{r+1,r}) = π_r^*Q_r`, integrally, constant 1 | PROVED (given `H_π`) |
| C4b: factor-1 normalization alone leaves `(1⊗(U'_p)^2)` | PROVED |
| C4c: Kummer injectivity over `F'_{r+1}`, evaluationwise, no `K_0` class | PROVED |

**C4 = CONFIRMED** (with `H_π` carried as a declared, unproved component of the statement).
