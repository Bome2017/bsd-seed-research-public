# HANDOFF — next unresolved arithmetic step

1. **The uniform step is unchanged.** It still needs an independent bound `dim B_p ≤ 1`, or a
   bound on a correctly defined containing relation kernel `ker E_p`. This is required for all
   `p ≥ 5` outside a fixed finite set. With this return, such a theorem would also apply at
   2243, 4547 and 5843 if its proof does not use good reduction. The first unresolved
   statement is

       ∃ S finite, ∀ p ∉ S:  dim_{𝔽_p} Hom_{Γ_p}(Cl(O_{L_p}[1/p])/p, E[p]) ≤ 1.

   No progress on it is claimed. W16–W21 record which relation-row manipulations do not
   provide it.

2. **Bad-prime obligations (fixed-prime, optional).** At `p ∈ {2243, 4547, 5843}`, a proof of
   `p⁴ ∤ #Cl(O_{L_p}[1/p])` would give `Sha[p^∞] = 0`, but the fields have degree about
   `2p¹⁰`, so this is not a computational proposal. The record's B.18 singleton criterion
   remains the other available route. Neither is executed here. Neither would close uniform
   FIN.

3. **Receiver bookkeeping correction to carry forward.** At 4547 the record's auxiliary point
   `R_p` is locally `p`-divisible (Lemma L(iii)). Any argument there that uses `R_p` as a
   local Kummer generator must be replaced by the `P2` argument. In the global Γ-structure,
   the `ε`-summand of the translation module might degenerate at 4547. This does not affect
   `ker(res) = W` (PROOF.md Step 2), but the record's displayed degree formula (2)
   `[L_p:ℚ] = 2p⁶(p²−1)(p²−p)` is not established at 4547.

4. **Lean infrastructure gap.** To kernel-check Theorem BFR itself, one would need Galois
   cohomology, Selmer groups, formal groups and Néron models, and class field theory in
   Mathlib. None of these is currently available. The concrete arithmetic layer in
   `RequestProject/Seed/` is ready for reuse.
