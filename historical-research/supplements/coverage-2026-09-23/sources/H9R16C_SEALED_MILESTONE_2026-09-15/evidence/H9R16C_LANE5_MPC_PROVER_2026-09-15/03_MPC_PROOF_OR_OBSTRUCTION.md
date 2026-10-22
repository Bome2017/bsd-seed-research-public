# 03 — MPC: proof (with `d_r = 1`)

Inputs: 01 (objects), 02 §3 (norm element). New input here: the interchange law for `W` (Lemma W below),
proved from KLZ17 Def 2.5.4 and the standard Weil-pairing identities.

## Lemma W (Atkin–Lehner interchanges the two degeneracy maps, exactly, with compatible roots of unity)

Let `ζ_{s+1}^p = ζ_s` (`ζ_s := ζ_{N p^s}`), and let `W_s` be KLZ17's moduli operator (01 §5). Then, as
morphisms `X_{s+1} → X_s` over `Z[1/Np, ζ_{s+1}]`:

    (W-i)   ϖ_1 ∘ W_{s+1} = W_s ∘ ϖ_2,          (W-ii)   ϖ_2 ∘ W_{s+1} = W_s ∘ ϖ_1.

*Weil-pairing facts used* (Silverman III.8.1(e), III.8.2; KLZ17 Lemma 2.4.4): for an isogeny `φ: E → E'`,
`e^{E'}_m(φx, φy) = e^E_m(x,y)^{deg φ}`; and `e_{mm'}(x, y) = e_m(m'x, y)` for `x ∈ E[mm']`, `y ∈ E[m]`.

*Proof of (W-i).* Let `(E,P) ∈ X_{s+1}`, `Q ∈ E[Np^{s+1}]` with `e_{Np^{s+1}}(P,Q) = ζ_{s+1}`, so
`W_{s+1}(E,P) = (E/⟨P⟩, Q mod ⟨P⟩)` and `ϖ_1 W_{s+1}(E,P) = (E/⟨P⟩, pQ mod ⟨P⟩)`. On the other side,
`ϖ_2(E,P) = (E_1, P̄)` with `φ: E → E_1 := E/⟨Np^sP⟩` of degree `p`, `P̄ = φ(P)` of order `Np^s`, and
`W_s(E_1,P̄) = (E_1/⟨P̄⟩, P'')` with `e^{E_1}_{Np^s}(P̄, P'') = ζ_s`. Now `E_1/⟨P̄⟩ = E/⟨P⟩` canonically, and
`e^{E_1}_{Np^{s+1}}(φP, φQ) = ζ_{s+1}^p = ζ_s`, while `e^{E_1}_{Np^{s+1}}(φP, φQ) = e^{E_1}_{Np^s}(φP, pφQ)`
(second fact with `x = φQ`, `m = Np^s`, `m' = p`, plus antisymmetry). Hence `P'' = pφ(Q) mod ⟨P̄⟩`, which
corresponds to `pQ mod ⟨P⟩` under `E_1/⟨P̄⟩ = E/⟨P⟩`. ∎

*Proof of (W-ii).* `ϖ_2 W_{s+1}(E,P) = (E'/⟨Np^s Q̄⟩, Q̄ mod)` with `E' = E/⟨P⟩`, `Q̄ = Q mod ⟨P⟩`. Since
`e_{Np^{s+1}}(P, Np^sQ) = ζ_p ≠ 1`, the subgroup `⟨P⟩ + ⟨Np^sQ⟩ ⊂ E` has order `p·Np^{s+1}` and contains
`⟨pP⟩` with quotient the full `p`-torsion of `E/⟨pP⟩`; so `E/(⟨P⟩+⟨Np^sQ⟩) ≅ E/⟨pP⟩` via `[p]`, under which
`Q mod (⟨P⟩+⟨Np^sQ⟩)` corresponds to `pQ mod ⟨pP⟩`. And `W_s ϖ_1(E,P) = W_s(E, pP) = (E/⟨pP⟩, P''')` with
`e_{Np^s}(pP, P''') = ζ_s`; as `e_{Np^s}(pP, pQ) = e_{Np^{s+1}}(P, pQ) = e_{Np^{s+1}}(P,Q)^p = ζ_s`, `P''' = pQ mod ⟨pP⟩`. ∎

*Matrix check (over C, standard `ζ_m = e^{2πi/m}`, which is a compatible system):* `w_{s+1} = w_s·diag(p,1)
= diag(1,p)·w_s` for `w_s = [[0,−1],[Np^s,0]]`; so `ϖ_2∘W_{s+1} : τ ↦ p·w_{s+1}τ = p·(w_sτ)/p = w_sτ = W_s∘ϖ_1(τ)`
and `ϖ_1∘W_{s+1} : τ ↦ w_{s+1}τ = w_s(pτ) = W_s∘ϖ_2(τ)`. No diamond appears. (KLZ17 §10.1's proof of Prop 10.1.1
prints the same relations with a factor `p^k` on one side in weight `k+2`; `k = 0` here.)

**Cohomological form** (F4, `W^* = W_* = W^{-1} = W` in weight 2): on `H^1`,

    ϖ_1^* W_r = W_{r+1} ϖ_2^*,   ϖ_2^* W_r = W_{r+1} ϖ_1^*,   W_r ϖ_{1,*} = ϖ_{2,*} W_{r+1},   W_r ϖ_{2,*} = ϖ_{1,*} W_{r+1}.

(The last two are what BCPV's proof of Lemma 4.10 invokes: "the Atkin–Lehner operators ... interchange
`ϖ_{1,*}` and `ϖ_{2,*}`".)

## Theorem (MPC_r with `d_r = 1`)

For `r ≥ 1`, on all of `H^1(X_{r+1})` (Betti, étale with any Tate twist, de Rham), with `A_s := W_s^{-1}(U'_p)^s`:

    ϖ_1^* ∘ A_r ∘ ϖ_{1,*}  =  A_{r+1} ∘ N_{r+1,r},        N_{r+1,r} = Σ_{d ∈ K_r} ⟨d⟩,

equivalently  `⟨ϖ_{1,*} y, A_r ϖ_{1,*} z⟩_r = ⟨y, A_{r+1} N_{r+1,r} z⟩_{r+1}`  for all `y, z ∈ H^1(X_{r+1})`.

*Proof.* Four steps, each a cycle identity from 01–02:

    ϖ_1^* W_r (U'_p)^r ϖ_{1,*}
      = ϖ_1^* W_r ϖ_{1,*} (U'_p)^r          [02 §2(c): ϖ_{1,*}U'_p = U'_pϖ_{1,*}, iterated r times]
      = W_{r+1} ϖ_2^* ϖ_{1,*} (U'_p)^r      [Lemma W, cohomological form: ϖ_1^* W_r = W_{r+1} ϖ_2^*]
      = W_{r+1} U'_p N_{r+1,r} (U'_p)^r     [02 §3: ϖ_2^* ϖ_{1,*} = U'_p N_{r+1,r}]
      = W_{r+1} (U'_p)^{r+1} N_{r+1,r}      [N_{r+1,r} central]
      = A_{r+1} N_{r+1,r}.

The pairing form follows from the projection formula for `ϖ_1` (F1) and perfectness of `⟨,⟩_{r+1}`. ∎

Restricting to `e'_ord H^1` (stable under every operator involved, `e'_ord` commuting with diamonds, `U'_p`,
`ϖ_{1,*}`, and `A_s` mapping `e'_ord H^1` isomorphically onto `e_ord H^1` by BCPV (1.8)) gives BCPV's setting.
Nothing about ordinarity was used.

## Corollary (group-ring-valued form; the finite-level content of KLZ17 Thm 7.2.3(v) / DR22 Lemma 2.8)

Let `Δ_s := (Z/Np^s)^×` act by diamonds, `π: Z_p[Δ_{r+1}] → Z_p[Δ_r]` the projection, and define
`⟨⟨x, y⟩⟩_s := Σ_{σ ∈ Δ_s} ⟨x, A_s ⟨σ⟩ y⟩_s [σ^{-1}] ∈ Z_p[Δ_s]` (this is DR22's `⟨⟨,⟩⟩_r` with `A_s` inserted and
BCPV's (1.6) target `Z_p[Δ_{N_h p^r}]`; any of the four placements of `σ`/`σ^{-1}` gives an equivalent statement).
Then for `x, y ∈ H^1(X_{r+1})`:

    π( ⟨⟨x, y⟩⟩_{r+1} ) = ⟨⟨ϖ_{1,*} x, ϖ_{1,*} y⟩⟩_r.

*Proof.* `⟨⟨ϖ_* x, ϖ_* y⟩⟩_r = Σ_{τ ∈ Δ_r} ⟨ϖ_* x, A_r ⟨τ⟩ ϖ_* y⟩_r [τ^{-1}] = Σ_τ ⟨x, ϖ^* A_r ϖ_* ⟨τ̃⟩ y⟩_{r+1}[τ^{-1}]`
(`⟨τ⟩ϖ_* = ϖ_*⟨τ̃⟩` for any lift `τ̃`) `= Σ_τ ⟨x, A_{r+1} N_{r+1,r} ⟨τ̃⟩ y⟩_{r+1} [τ^{-1}]` (Theorem)
`= Σ_τ Σ_{d ∈ K_r} ⟨x, A_{r+1}⟨dτ̃⟩ y⟩_{r+1} [π(dτ̃)^{-1}] = π(⟨⟨x,y⟩⟩_{r+1})`. ∎

So the modified group-ring pairings form a strictly compatible system under `(ϖ_{1,*}, ϖ_{1,*}, π)` with
constant `1`. This is the statement whose Λ-adic limit is KLZ17 Thm 7.2.3(v) ("canonical perfect pairing of
`Λ_D`-modules", proof = Ohta II Cor 1.3.8/2.3.6). Mandatory check 5: KLZ17 7.2.3(v) is used for nothing here;
the finite-level identity is derived, not extracted.

## Obstruction search (what could have gone wrong, and did not)

* A `p`-power in `d_r`: would require a push-then-pull composite (02 §0, first two rows); MPC has the
  pull-after-push composite. `d_r = 1` exactly.
* A diamond unit in `d_r` from the `W` normalization: Lemma W shows none arises when the roots of unity are
  compatible (`ζ_{s+1}^p = ζ_s`). With an incompatible choice `ζ'_{s+1}` (`ζ'^p_{s+1} = ζ_s^c`, `c ∈ (Z/Np^s)^×`)
  one gets `W'_{s+1} = ⟨c⟩^{±1} W_{s+1}` (KLZ17 Def 2.5.2, second relation), hence `d_r = ⟨c⟩^{±1}`, a central
  Q-rational diamond unit — exactly the class of discrepancies Lanes 1/2/4 already showed to be harmless.
  BCPV fix `ζ_{p^r}` "once and for all" (§4.2) and use `ζ_m = e^{2πi/m}` conventions via KLZ17; taking
  the compatible system is forced by their Λ-adic constructions (KLZ17 §7.1).
* Sign from `W^{-1}` vs `W`: none in weight 2 (`W^2 = ⟨−1⟩ = id`).
* Ordinary projector: not needed; the identity is integral and holds on all of `H^1_ét(X̄_{r+1}, Z_p(1))`.
* Cusps / open vs compact: all cycles extend to the compactifications; the identity holds on `H^1(X)` and on
  `H^1(Y)`; BCPV use `Y_1(Np^r)` in (1.6) and `X_1(Np^r)` in §4 — no difference for MPC.
