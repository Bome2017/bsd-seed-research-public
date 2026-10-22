# VERDICT — prime support of `Ш(E^{-7}/Q)`, hostile referee run

    STAGE_I_A = TWIST_SHA_COFINITE_ONLY
    STAGE_I_B = EIGENSPACE_REFINEMENT_OBSTRUCTED
    STAGE_II  = PRIOR_BOUND_CONFIRMED  (exponent form; order·torsion form correct but slack;
                                        "equivalently A₂ = 0" is an error — counterexample given)
    CHANGED_STAGE_I_AFTER_READING_STAGE_II = no

Full reports: `AUDIT_STAGE_I.md` (frozen before `STAGE_II_ONLY/` was opened),
`AUDIT_STAGE_II.md`. Machine-checked arithmetic: `RequestProject/Main.lean`.

## The required per-prime answer

Question asked: for each prime `p ≥ 5`, is `Ш(E^{-7}/Q)[p^∞] = 0` **unconditionally proved**,
and by which theorem with which hypotheses checked?

| class of `p ≥ 5` | is vanishing proved? | why not / what is missing |
|---|---|---|
| good ordinary (`p ∤ N`, `a_p ≢ 0`) | **no** | Kato's divisibility applies — `ρ̄_p` irreducible ✔, `p ∤ #tors` ✔, `p ∤ ∏c_v` ✔ — but its bound `v_p(#Ш) ≤ v_p(L·#tors²/(Ω∏c_v))` needs the **exact rational** `L/Ω`; only a real interval is certified, which (proved in Lean) excludes nothing at any prime |
| good supersingular (`a_p = 0`; infinitely many, Elkies) | **no** | same, via Kobayashi's `±`-theory instead of Kato; same missing input |
| non-split multiplicative: `p = 2243` | **no** | same missing input |
| split multiplicative: `p = 5843` | **no** | additionally: exceptional (trivial) zero of the `p`-adic `L`-function — split reduction proved here; no unconditional `p`-part bound located in this case |
| additive: `p = 7` (`I₀*`), `p = 4547` (`III`) | **no** | Kato/Kobayashi are stated for good or multiplicative `p`; **no route at all**, even granting an exact `L`-value |
| anomalous `a_p = ±1` | vacuous | provably no such `p` (a rational 2-torsion point forces `a_p` even) |
| Eisenstein / residually reducible | vacuous | provably no such `p ≥ 5` (Mazur + explicit Frobenius certificates) |

So: **`Ш(E^{-7}/Q)[p^∞] = 0` is currently proved at no prime `p ≥ 5`.** What is proved is that
the support is finite (Kolyvagin, from the certified non-vanishing `L(E^{-7},1) ≠ 0`), with no
explicit finite set and no effective bound available at this conductor.

## The numerical BSD quotient

Classified as **prediction only**. It is not used anywhere above. Its `p`-part is not
established for this twist at any prime, in either direction: neither `v_7(#Ш) > 0` nor
`v_p(#Ш) = 0` for `p ≠ 7` follows from any theorem whose hypotheses hold here. Two independent
methodological defects in how it was formed are recorded in `AUDIT_STAGE_I.md` §1 and §5
(period normalisation selected by BSD-circular reasoning; nearest-integer rounding with no
denominator bound).

Anti-anchoring outcome: the audit located obstructions at `4547` and `5843`, primes the
prediction does not flag, and found that the obstructions one would expect — Eisenstein primes,
torsion primes, Tamagawa primes, anomalous primes, CM — do not occur on this curve. The
proved statement is therefore **weaker** than the prediction everywhere, and the best possible
outcome of the audited machinery, even after closing the one missing implication, would be
vanishing outside `{7, 4547, 5843}`, not outside `{7}`.

## First missing implication

    certified real interval for L(E^{-7},1)   ⟹   the exact rational L(E^{-7},1)/Ω

i.e. an explicit `D` with `D·L/Ω ∈ Z` plus numerics of half-width `< 1/(2D)`; or a
Waldspurger/Gross-type closed form for the twisted algebraic `L`-value. Everything downstream
of that (Kato at good ordinary and multiplicative `p`, Kobayashi at good supersingular `p`) has
all of its remaining hypotheses verified on this curve in `AUDIT_STAGE_I.md`.

## Consequence for the ordinary bridge

The saturation-defect estimate is justified in the exponent form `A₂ ≤ v_p(exp Ш(E^{-7}/Q)[p^∞])`,
and the order-times-torsion form follows from it (the torsion factor being vacuous here). But
`A₂ = 0` is only **sufficient** for `v_p(R_der) ≥ 0`, never equivalent — an explicit symmetric
matrix with non-integral entries and unit determinant is given. And because no prime can
currently be certified to satisfy `p ∤ #Ш(E^{-7}/Q)`, the bridge's conclusion, though true for
all but finitely many admissible `p`, cannot at present be invoked at a single named prime.
