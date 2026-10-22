# OpenAI math release: consolidated audit for the BSD seed (Claude, Opus 5.5, 2026-10-06)

**Repository.** github.com/openai/math, under the Apache-2.0 license. It holds 722 manuscripts in 372 families, at mixed verification levels; its README warns that some unformalized results may contain issues.

**Formalization status.** `lean/formalization.yaml` was read on 10-06. It lists about 250 entries, and none of them is a manuscript on BSD, Selmer groups, Ш, converse theorems, Goldfeld density or elliptic curves. Pro reported the same.

**Consequence.** No arithmetic result from this release is imported into the seed record as a theorem. Using any specific lemma would first require a hostile audit of that lemma.

## Papers and items considered

| Paper (folder date) | Item | Who read what | What it gives | Status for the seed |
|---|---|---|---|---|
| Exact BSD formula from low Selmer corank (Oct 3) | Main theorem: if some s_q(E) ∈ {0,1}, full BSD holds | Claude: §1, §5, §10 in full; §9 in part | Its rational anchor is rank ≤ 1 in three places: X_p needs Q_E ∈ ℚ; the tame Gross–Zagier spectral identity for Heegner points; and a(E)+a(E^D) = 1 at the center | **G1 transplant: PRECISE_CORANK2_BREAK** (`BSD_SEED_FRONTIER_2026-10-06/2_CLOSED_LANES/EXTERNAL_OPENAI_RESULT002_TRANSPLANT.md`) |
| same | §5 "A nonzero height direction" | Claude | Poincaré biextension, Kummer cocycle, Weil-pairing commutators, then Chebotarev | Independent instance of **G2's mechanism**. Corroborates the method, not G2's seed statement |
| same | §4 `vertical:obstruction-span` (arbitrary-dimensional) | Pro (not read by Claude) | Tame directions span the first-order obstruction space; a full-rank combination kills a tested strict space generically. In OpenAI's application the residual complex collapses to one line | Transport machinery. Bounding Ш[p] with it needs an anchor: **blocked** |
| same | §7–8 position-cut / increasing-level theta estimates | Pro | Uniform bounds on moments as the p-level grows; the lemma statement is not rank-one-specific | A W3-only use would improve only the per-prime engine. **No endpoint effect**; not built |
| The two-primary BSD formula in Selmer corank ≤ 1 (Sep 24) | §12 conjugate Bockstein alternation, ⟨x,∂x⟩ = 0, perfect on the non-free quotient | Pro | Excess comes in hyperbolic pairs | Structure, not a bound: a perfect alternating space can have dimension 2, 4, …. This is the record's lane A (10-03). **No bound** |
| A pointwise 2-converse, rational two-torsion (Sep 24) | `ring-limits.tex`: fixed-K missing-vertex implication | Claude, in full | A 2-adic family over Λ[G]. With simple zeros and a uniform index-minus-Ш bound at all nonzero vertices, ord L(E)L(E^{(k)}) = 1 at the base. Gross–Zagier anchors every vertex | Architecture kept. It needs a **second-order base test**, and its output runs Selmer → analytic rank, while the seed's r_an = 2 is already proved. **Blocked pending a rank-two anchor** |
| same | `ring-determinants.tex`: exact DVR determinant switch (generic rank one); "Selecting a rank-two evaluation"; square switches h ↦ h − 2 | Pro (Claude: location only) | Strips surplus specialized classes while preserving a determinant-line valuation | RANK2_SWITCH is not disproved. As a seed route: **GATE4_FAILS_WITH_THE_CURRENT_KNOWN_ANCHOR**. Package deferred |
| The Selmer converse at every prime (Sep 24), cited as [C] | low-corank converse | not read (file list only) | — | not assessed |
| Goldfeld's analytic density conjecture and the 2-converse (Sep 23) | rank-0 and rank-1 twists each of density 1/2, with prescribed local conditions | Pro | Supplies low-rank vertices around the seed | An input to the missing-vertex architecture; blocked with it |
| Adjacent results (Pro): Milne rationality, modularity over imaginary quadratic fields, Fontaine–Mazur at 2 | — | Pro | — | No route to any open gate found |

## Against the three live endpoints (Pro, 10-06)

1. **A new rank-two global identity** (higher Gross–Zagier / derived leading term over a number field).
   - The release supplies none: every exact constant in it comes from rank ≤ 1 Gross–Zagier or from modular symbols.
   - The Aristotle rank-two-anchor run (`PRECISE_OBSTRUCTION`) tested the natural candidates and found none.
2. **An independent upper bound on the receiver Hom_{Γ_p}(Cl(O_{L_p}[1/p])/p, E[p]) that does not pass back through Selmer.**
   - None found. The class-group and S-unit arguments in the release concern fixed supports and twist families, not the varying division fields L_p.
3. **Q36 (rationality and the exact leading term of q).**
   - None found. Milne rationality is a different rationality problem.

**Bottom line.** The release supplies much of a transport apparatus: obstruction spanning, Bockstein alternation, rank-two evaluation and switches, and missing-vertex group-ring transfer. It does not supply the rank-two global anchor that would give that apparatus something to transport at the seed's rank-two vertex. In Pro's words, OpenAI supplies much of the gearbox, and the missing engine is still the rank-two global anchor. No theorem-building workers should be assigned to these items until one of the three endpoints has a genuinely new input.

FIN, ORDER9 and Q36 are unchanged.
