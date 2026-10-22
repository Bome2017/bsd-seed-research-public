# 06 — C5 (push-down independence)  [SECOND referee, independent]

**Verdict: CONFIRMED_WITH_NARROWER_HYPOTHESIS.** The load-bearing half (C4 and its constant are
insensitive to the choice, uniformity in `r` required) is PROVED and numerically corroborated. The
`NOT_PRINTED` citation is exact. The description of *how* the constructed point changes is imprecise
as stated and is replaced below by the exact form.

## §1. Exactly which properties of `pd` C4 consumes

Auditing §§1–4 of `05_C4_TOWER_RELATION.md`, the tame push-downs enter only through:

| # | property | forgetful `pr^t_1` | quotient `pr^t_2` |
|---|---|---|---|
| P1 | `pd_*∘ϖ_{1,*} = ϖ_{1,*}∘pd_*` | PASS (T4g) | PASS (T4g) |
| P2 | `pd_*∘U'_p = U'_p∘pd_*` | PASS (T4c) | PASS (T4d) |
| P3 | projection formula `⟨pd_*u, x⟩ = ⟨u, pd^*x⟩` (any finite morphism) | holds | holds |
| P4 | `pd_*∘⟨n⟩ = ⟨n mod⟩∘pd_*` (used in C2/C7) | PASS (T4e) | PASS (T4f) |

(T-labels: my `_verify/transport_check.py`, exact mod ℓ ∈ {1000003, 999983}, `(N_g,t,p,s)` =
`(5,2,3,1)` and `(3,2,5,1)`, levels 30→15, plus the commutation square 30→10→5 vs 30→15→5.)

`pr^t_1(A,P) = (A,tP)` and `pr^t_2(A,P) = (A/⟨N_gp^sP⟩, P mod)` are both finite and both defined over
`Q`, and no step of C4 uses any property distinguishing them. Hence **C4 holds verbatim, with the
same constant 1, for either choice.** Neither is used in A1 (MPC is entirely at one tame level) or
in Cor 4.11 (entirely at common level), so the constant cannot move.

## §2. Uniformity in `r` is necessary, not decorative

P1 is a statement about *two* levels: `pd^{(r)}_*∘ϖ_{1,*} = ϖ_{1,*}∘pd^{(r+1)}_*`. If the choice were
`pr^t_2` at level `r+1` and `pr^t_1` at level `r`, the left- and right-hand sides of Lemma (L) would
involve genuinely different morphisms and the identity fails (A5 shows they differ by an
Atkin–Lehner interchange, not by a scalar). C5's proviso "provided the choice is uniform in `r`" is
therefore a real hypothesis. The same applies independently to `pd^{t_f}` on factor 1.

## §3. The `NOT_PRINTED` citation: verified verbatim

* `ϖ_1` is defined **only** in the `p`-direction: BCPV.tex **l.1198–1199**,
  "`denote by ϖ_1 the degeneracy map X_1(Np^r) → X_1(Np^{r-1}), (A,P) ↦ (A,pP)`". ✔
* The symbol `ϖ_{1,*}` is then reused for the **tame** direction with no separate definition:
  `definition_big_diagonal_Hida_families`, **l.1457**,
  `H^1_ord(Y_1(Np^∞))^{⊗3} --ϖ_{1,*}⊗ϖ_{1,*}⊗ϖ_{1,*}--> H^1_ord(Y_1(N_f p^∞))⊗̂ …`. ✔
* `pr_h` in (4.16), **l.1486–1487**: "`the map pr_h is induced from the pushforward map
  H^1_ét(X̄_1(Np^r),Z_p)(1) --ϖ_{1,*}--> H^1_ét(X̄_1(N_hp^r),Z_p)(1) composed with projection to the
  h-isotypical Hecke eigenspace`". ✔

So "which map BCPV intend is `NOT_PRINTED`" is **correct**, and it is `NOT_PRINTED`, not FALSE: the
forgetful reading is natural but is an interpretation (coordinator erratum item 1, which C5 honours).

## §4. What actually changes: the exact form

A5 (`L5-T5`, frozen; **numerically confirmed here for the first time** — T4a/T4b PASS at
`(N_g,t,p,s) = (5,2,3,1)` and `(3,2,5,1)`, both primes):

    pr^t_{1,*} W_{Np^s} = W_{N_gp^s} pr^t_{2,*},     pr^t_{2,*} W_{Np^s} = W_{N_gp^s} pr^t_{1,*}
    ⟹  pr^t_{2,*} = W_{N_gp^s} ∘ pr^t_{1,*} ∘ W_{Np^s}    (W^{-1} = W in weight 2).

Since `Δ^{ord}_s` carries `W_{Np^s}^{⊗3}` inside its own definition, the two constructed points are
related by **conjugating the tame push-down with the two Atkin–Lehner involutions**,
`W_{N_gp^s}(−)W_{Np^s}` — "a change of degeneracy map, no scalar and no diamond" (Lane 5 `04` §3).

C5 describes this as "a tame Hecke scalar at the primes dividing `t` on `h`-isotypic quotients".
**That is not exact as printed.** `W_{N_gp^s}` does act by the pseudo-eigenvalue `λ_{N_gp^s}(h)`, a
scalar, on an `h`-**new** line at native level; but `W_{Np^s}` acts on the `h`-isotypic subspace of
`H^1(X_1(Np^s))`, which for `t > 1` is an **oldform space of dimension > 1** on which `W_{Np^s}` is an
involution, not a scalar. The supported statement is:

> The two choices give points that differ by the Atkin–Lehner interchange `pr^t_1 ↔ pr^t_2`. A single
> scalar comparison is available only after projecting *both* sides to lines on which each `W` acts
> by a scalar — e.g. after fixing an `h`-new line at native level and a `W_{Np^s}`-eigenvector in the
> `h`-old space at common level — and the scalar is then the corresponding ratio of pseudo-eigenvalues
> at the primes dividing `t`.

This narrowing costs nothing here (the tower relation and its constant are untouched), but it must
be carried, because the *identity* of the Chow–Heegner point is what any later comparison with BCPV's
`Δ^ét(f⊗ad g)` will need. Lane 5 `04` §3's own closing sentence flags the same thing.

## §5. Status

| sub-claim | status |
|---|---|
| C4 and its constant unchanged under either tame push-down | PROVED (§1), numerically corroborated |
| uniformity in `r` required | PROVED necessary (§2) |
| "which map BCPV intend is `NOT_PRINTED`", with the three line citations | CONFIRMED verbatim (§3) |
| "only the identity of the constructed point changes" | PROVED |
| "a tame Hecke scalar at the primes dividing `t` on `h`-isotypic quotients" | imprecise; exact form in §4 |

**C5 = CONFIRMED_WITH_NARROWER_HYPOTHESIS** (§4).
