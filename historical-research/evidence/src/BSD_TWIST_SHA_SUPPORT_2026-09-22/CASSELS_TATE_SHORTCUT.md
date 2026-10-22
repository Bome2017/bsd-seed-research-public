# The Cassels–Tate shortcut — the seed conclusion does not need the twist's Sha support

Date 2026-09-22. Deduction due to an external read-only review; verified here against both returned audits.
**Additive.** Supersedes `GRADING.md` §3 (Run A characterization), and moves `MANIN_GATE*.md`, `MODDEG_GATE.md`,
`TWIST_NORM_INTERIM.md` **off the critical path** for the seed's ordinary conclusion.

---

## 1. Both runs prove the same bound, and it is an EXPONENT bound

Verified in the detailed arguments, not the summary lines:

* **Run B** (`AUDIT_ORDINARY_BRIDGE.md` §7.3): `p^c` = exponent of `Sel_{p^∞}(E^{-7}/Q) = Ш(E^{-7}/Q)[p^∞]`.
  Since `Sel^-` is killed by `p^c` and the finite-level τ-rule kills `Sel^+ × Sel^+`, bilinearity gives
  `p^c Sel ⊆ Sel^{(2)}`, so `A_2 ≤ c`, `v_p(R_der) ≥ −2c`, and **`v_p(#Ш(E/K)[p^∞]) ≤ 2c`**.
* **Run A** (`ORDINARY_BRIDGE_AUDIT.md` ~l.413): `e_0 = exp(E^{-7}(Q)[p^∞]) · exp(Ш(E^{-7}/Q)[p^∞])`,
  `A_2 ≤ v_p(e_0)`, and **`#Ш(E/K)[p^∞] | p^{2 v_p(e_0)}`**.

For `p ≥ 5`, `E^{-7}(Q)_tors = Z/2` so the first factor is 1 and `v_p(e_0) = c`. **The two runs give the identical
bound.**

**Correction to `GRADING.md` §3.** It recorded run A as an *order* bound `A_2 ≤ v_p(#Ш·#tors)` and said "neither
dominates". Wrong: that was run A's *summary line*, which states the support condition; the detailed argument is an
exponent bound, equal to run B's. This is the same failure as citing ARS's summary of Edi89 — a summary line was
graded instead of the argument.

## 2. The deduction

Let `A = Ш(E/Q)[p^∞]`, `B = Ш(E^{-7}/Q)[p^∞]`, `exp(B) = p^c`, `p` admissible good-ordinary.

1. For odd `p`, `Ш(E/K)[p^∞] ≅ A ⊕ B` (the τ-eigenspace bridge, proved for Selmer/`T_pШ` in Task 4 of both runs).
2. `B` is finite (certificate) and carries the Cassels–Tate pairing, which for an elliptic curve is **perfect and
   alternating**. So `B ≅ M ⊕ M`, hence `#B = #M² ≥ exp(M)² = p^{2c}`. Directly: take `x` of order `p^c`; the
   character `⟨x,−⟩` has image of order `p^c`, and alternation puts `⟨x⟩`, of order `p^c`, inside its kernel.
3. Therefore `v_p(#A) + 2c ≤ v_p(#A) + v_p(#B) = v_p(#Ш(E/K)[p^∞]) ≤ 2c`, so **`A = 0`**.

        [c_2] != 0   ==>   Sha(E/Q)[p^inf] = 0     at every admissible good-ordinary p,

**with no condition on the twist's Sha support.** The runs were annihilating the whole group over `K`; the seed only
needs its `+` summand, and the bound is exactly saturated by what `B` alone forces.

Independent check here of the runs' own step `A_2 ≤ c`: for `s ∈ Sel^+`, `⟨p^c s, t⟩ = p^c⟨s, t^+⟩ + ⟨s, p^c t^-⟩
= 0 + 0`, using the τ-rule (`⟨s,t^+⟩ = −⟨s,t^+⟩`, `p` odd) and `p^c Sel^- = 0`; `Sel^-` is killed outright. So
`p^c Sel ⊆ Sel^{(2)}` = the null space of `⟨,⟩_1`. Sound as written. The step `v_p(R_der) ≥ −2A_2` needs only that
`p^{A_2}⟨⟨,⟩⟩_2` is integral on the rank-2 saturated module; it does not depend on whether `⟨⟨,⟩⟩_2` is symmetric or
alternating.

## 3. Two things the review did not draw out

**(a) The deduction also forces the SHAPE of the twist's Sha.** Step 3 gives `v_p(#B) ≤ 2c` as well as `≥ 2c`, so
`#M = p^c = exp(M)`, i.e. `M` is cyclic:

        [c_2] a unit at p   ==>   Sha(E^{-7}/Q)[p^inf]  ≅  0  or  (Z/p^c)^2.

Contrapositive: **at any admissible `p` where `Ш(E^{-7}/Q)[p^∞]` is not homocyclic of rank ≤ 2, `[c_2]` cannot be a
unit.** The twist-Sha question does not vanish — it changes role from *hypothesis* to *consistency test on `[c_2]`*.
(The BSD prediction `#Ш(E^{-7}) = 49 = 7²` puts all of `B` at the non-admissible `p = 7`, so no admissible prime is
predicted to test it.)

**(b) The certificate's role narrows but does not disappear.** The deduction needs `B` **finite** (for perfectness)
and `s^- = 0` (for A2a, i.e. `Ш(E/K)[p^∞]` finite at all). Both come from the `D = -7` certificate via GZK. What is no
longer needed is `B`'s *support*.

## 4. What this makes moot, stated plainly

`MANIN_GATE.md`, `MANIN_GATE_CORRECTION.md`, `MODDEG_GATE.md` and `TWIST_NORM_INTERIM.md` were all in service of
certifying `#Ш_an(E^{-7}) = 49`, i.e. of controlling `B`'s support. **For the seed's ordinary conclusion that is no
longer needed.** Their findings stand as facts (ARS, Edixhoven 4.6.3, CNS 1.2 all correctly source-checked), but
they are off the critical path, and the Wiersema–Wuthrich audit (parts A/B of the last brief) should **not** be
pursued for this purpose.

## 5. Corrections to my own recent artifacts, from the same review

* **`TWIST_NORM_INTERIM.md` "seed model in project use is NON-MINIMAL" — withdrawn.** The given model
  `[0,-22735,0,106272484,0]` maps to Sage's `[0,-1,0,-66020924,-65074271436]` by the translation `x = X + 7578` with
  `u = 1` (verified: `a2' = -1`, `a4' = -66020924`, `a6' = -65074271436`). Same discriminant, same Néron
  differential. The given model **is** minimal; Sage's `is_minimal()` returned `False` because it tests for the
  *reduced* canonical form. No missed differential scaling. (Same for the twist: `r = -53048`, `u = 1`.)
* **`TWIST_NORM_INTERIM.md` "the normalizations line up with no fudge factor" — withdrawn.** The identity
  `Ω_1(E^{-7})·√7 = Im(ω_2(E))` holds exactly between **least-positive** periods. The BSD period of a
  two-component curve is twice the least real period, and the modular-symbol `Ω_-` convention needs its own
  cycle-index argument. That factor-2 bookkeeping was not done. (Moot for the seed conclusion per §4.)
* **`I_3(13)` — my previous answer was wrong.** I said the promotion was not in the record. It is, in two places
  I wrote: `FRONTIER.md` l.111–112 ("`C_1` … is nonzero — **forced by the single good specialization at `p = 13`**")
  and `SYNTHESIS_AB.md` l.15 ("nondegeneracy free from the **certified** `p = 13` unit specialization"). Per
  `SCOPE_AT_13.md`, `I_3(13) = F_13` needs **both** `Ш(E/Q)[13] = 0` and `Ш(E^{-23}/Q)[13] = 0`; only the first is
  supplied. **The matrix lemma survives; its arithmetic premise does not.** `FRONTIER.md` contradicts itself (l.125
  calls the same comparison open). My search missed l.111 because it says "good specialization", not "unit" —
  exactly the grep-misses-transitive-constraints failure. Correction note placed in the frontier folder.

## 6. Ledger

    ORDINARY: [c_2] != 0 ==> Sha(E/Q)[p^inf] = 0 at every admissible good-ordinary p     CONDITIONAL, NEW, STRONGER
      needs: BLV equality, module identification, BD 2.18(5)/2.23/Lemma 3.1 (source-read by both runs, NOT by
             the project), the runs' A_2 <= c (checked here), the D=-7 certificate (finiteness only)
      does NOT need: Sha(E^{-7}/Q) support, Manin constant of E^{-7}, #Sha_an(E^{-7}) = 49
    CONSISTENCY TEST: Sha(E^{-7}/Q)[p^inf] must be 0 or (Z/p^c)^2 wherever [c_2] is a unit
    OPEN: [c_2] != 0 (uniformly); A3 supersingular; q = 36
    DEAD for this seed: interface B (a_p even at every odd good p; p = 5 checked directly)
    NOT SUPPLIED: I_3(13) = F_13 (twist 13-part missing) -- C_1 != 0 is therefore NOT established

---

## Erratum (same day) — the boxed statement in §2 is not prime-local, and must be

§2 and §6 write `[c_2] != 0 ==> Sha(E/Q)[p^inf] = 0 at every admissible good-ordinary p`. That reads as if a single
hypothesis delivered every prime. It does not: `[c_2]` is the mod-`p` `I^2/I^3` coefficient at conductor `p`, a
**different object for each `p`**. The correct statement is

    for each admissible good-ordinary p :   [c_2]_p != 0   ==>   Sha(E/Q)[p^inf] = 0.

Getting finiteness from it requires `[c_2]_p != 0` for all but finitely many `p` — which is exactly the open uniform
problem `DIAGONAL_CROSS_PRIME_GROSS_POINT_NONVANISHING`, not a consequence of anything here. The §2/§6 wording
overstated the reach of the result toward FIN. Likewise §3(a): `B ≅ 0 or (Z/p^c)^2` is conditional on `[c_2]_p`.
