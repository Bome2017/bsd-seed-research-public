# 05 — What this object does NOT claim, and what is downstream

## §1. The governing non-claim

> **This milestone makes no claim whatsoever about the applicability of BCPV's unweighted big class to the
> Castella–Hsieh target.**

What is sealed is a finite-level geometric statement: a compatible tower of contracted Chow–Heegner points
in a correctly typed receptacle, plus the Hecke-algebra input it needs. Nothing about the big-trace
comparison, and nothing about any arithmetic application, is sealed.

## §2. The big-trace result, recorded narrowly and deliberately

The separate H9R17 lane proved a big-trace identity. It is recorded **only** in this form:

    BCPV_UNWEIGHTED_BIG_TRACE = PROVED WITH p^3 UNDER (H-ω),  NOT APPLICABLE TO CH TARGET

with:
* the identity `[(id⊗tr)Δ^ét_∞(f⊗ad(g))]_{K_0} = p^3·Ψ(Kum_∞(𝒬_∞))` — a `p^3`, not constant-free, and over
  `K_0`, not `res` from `Q`;
* `(H-ω)` = the `μ_{p−1}`-diamonds act trivially on `R_f` and `R_g`, i.e. BCPV's own `k_∘ = 0`;
* **(H-ω) fails for the Castella–Hsieh target**, on a parity invariant: `k_∘ = 0` forces an even tame
  nebentype, while their `g` is the weight-one theta series of an imaginary quadratic field, whose tame
  character `η_{K/Q}` is odd; `p−1` is even, so an odd `k_∘` is never `≡ 0`. No Dirichlet twist repairs it
  (`ε_g ↦ ε_gφ²` is parity-invariant, and `ad(T_g⊗φ) = ad(T_g)`);
* `Ψ` is defined only on the image of `Contr_∞` — an equality of two elements, **never** a module
  isomorphism.

> **A future summary must not shorten this to `G_BIG_KUMMER_TRACE = PROVED`.** Operator instruction,
> 2026-09-15. The unqualified form is false for the target the program exists to reach.

## §3. Downstream work — listed, and explicitly NOT sealed as proved inputs

| item | status |
|---|---|
| H9R17 big-trace identity | proved under its six hypotheses; **not** an input to anything sealed here |
| ω-rebuild Phase 1 (DR22 `(ω_1,ω_2,ω_3;δ)`) | restatement complete: `Ξ = ω^{-1}`; the sealed tower survives **verbatim**; the trace identity survives with the same `p^3`; first obstruction = BCPV's own specialization sum at l.1474–1475 |
| ω-rebuild Phase 2 | **running**; the live theorem |
| `RECIPROCITY_SUPERSTRUCTURE_TYPECHECKS` | **YES** — the representations, pairings, self-dual twist, balanced local conditions and `f`-extraction typecheck at `t ≠ 0` |
| `WEIGHTED_RECIPROCITY_THEOREM` | **OPEN** — the finite specialization formula that feeds the reciprocity law is exactly where BCPV hard-code the three `e_0`'s. "Reciprocity survives" is a framework check, not a theorem, until Phase 2 replaces those projectors and re-derives the specialization lemma |
| the chain `𝒫^♮_∞ → 𝒫^♮_{∞,𝔭_g} → (E(Q)⊗Q_p)⊗̂R_{g,𝔭_g} --λ_g--> E(Q)⊗F_g` | **NOT PROVED**, and does not follow from anything sealed here |

## §4. Phase 2's success criterion and stop conditions (operator, 2026-09-15)

Live target: define the weighted finite class with DR22's exact factors `δ^{-1}(abc)ω_1(a)ω_2(b)ω_3(c)`;
replace `e_0⊗e_0⊗e_0` by `e_{ω_1}⊗e_{ω_2}⊗e_{ω_3}`; reprove the finite specialization lemma with those
projectors; show the `p^3` computation becomes `(p^3/(p−1)^3)(p−1)^3 e_{ω_1,ω_2,ω_3} = p^3 e_{ω_1,ω_2,ω_3}`,
the same `p^3` but with the projector the identity on the target character component instead of annihilating
it; recover `a_p(f)^{-r}a_p(g)^{-2r}` and the Atkin–Lehner/`λ` term; and re-walk the reciprocity theorem
without invoking any `k_∘ = 0`-only step.

    OMEGA_REBUILD_CLOSED             ⇒ advance to target big-trace identification
    FIRST_K0_ONLY_THEOREM_FOUND      ⇒ freeze the exact new obstruction
    CHARACTER_PROJECTOR_MISMATCH     ⇒ route killed in this form

## §5. Also not claimed

No statement about heights, `L`-values, Selmer groups, Sha, density, `𝔭_g`-localization, `f`-branch
extraction, weight-one specialization, or `E(Q)`. No claim that the point tower is non-torsion. No erratum
against BCPV, DR22 or any other paper is published from this project; recorded defects stay internal.
