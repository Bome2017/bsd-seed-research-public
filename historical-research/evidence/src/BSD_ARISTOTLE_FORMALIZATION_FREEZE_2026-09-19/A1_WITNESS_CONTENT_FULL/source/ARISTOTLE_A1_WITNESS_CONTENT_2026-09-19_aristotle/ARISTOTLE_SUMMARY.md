# Summary of changes for run 694c95cb-6770-4451-b570-02cf4ec310b7
**RESULT: A1_FULL_PROVED** (plus all three optional stretch targets).

**What was done.** I unpacked the attached package into `A1_WITNESS_CONTENT/`, verified its manifest (all files match `MANIFEST.sha256`), reproduced the stated baseline (clean build, 20 `sorry`s, level `BELOW_A1_CORE`), and then replaced every `sorry` in `WitnessContent/Targets.lean` by a complete proof. The frozen files (`WitnessContent/Defs.lean`, `WitnessContent/Spec.lean`, `WitnessContent/Acceptance.lean`, `A1_WITNESS_CONTENT/lakefile.toml`, `lean-toolchain`, `scripts/level.py`) are byte-identical — `shasum -a 256 -c scripts/FROZEN.sha256` reports 6/6 OK — so every accepted theorem has exactly its frozen type `Spec.<Name>`.

**1. Frozen targets proved (all 20).** CORE: `lemmaA_comm`, `gr_killed_by_exponent`, `depth_spec`, `zero_infinitely_divisible`, `hInf_lt_top_iff`, `hInf_le_iff`, `JE_bounds`, `WC_abstract`, `CM_uniform_denominator`, `CM_nonzero_everywhere`, `WC_abstract_nonvacuous`. FULL: `gr_p_primary`, `bridge_517`, `cls2_zero_iff`, `WC_groupRing`, `padicInt_units`, `units_exponent`. STRETCH: `lemmaA_general`, `gr_finite_Z`, `gr_rational_trivial`.

**2. Remaining targets:** none. **3. First remaining formal obstruction:** none.

**4. New helper lemmas** (in new, non-frozen files `WitnessContent/GroupRing.lean`, `Depth.lean`, `Primary.lean`, `WC.lean`, `Countermodels.lean`, `Instances.lean`, `Stretch.lean`; full list also in `STATE.json`): the augmentation representation `f = ∑ f g • (g − 1)`; a truncated binomial expansion `(1+x)^n = 1 + n•x + z` with `z` a multiple of `x²`; `e • I ⊆ I²` and then Lemma A by multiplying by `I^(r−1)`; the graded piece killed by `e` and, after inverting the prime-to-`p` part of `e`, by `p^{v_p(e)}`; downward closure of `p`-divisibility, attainment/maximality/boundedness of depth, attainment of the infimum defining `h_p` in `ℕ∞`; `Sha[p] = 0 ⇒ Sha[p^∞] = 0` by induction; the primary decomposition of a torsion element via the coprime torsion decomposition over `ℤ`; finiteness of a group covered by finitely many finite primary parts; and, for the countermodels, `depth p (p²) = 2` in `ZMod (p³)` together with the existence of a prime not dividing a given nonzero integer.

**5. Assumptions/axioms.** No new `axiom`, no `sorry`/`admit`, no `@[implemented_by]`/`@[extern]`/`unsafe`. `#print axioms` shows only `propext`, `Classical.choice`, `Quot.sound` for every target (`zero_infinitely_divisible` uses `propext` alone). The arithmetic antecedent (`A ≠ 0` and `A ∈ J_E`), Ota Thm 5.17 and Thm 1.5, the Selmer corank facts and torsion of Sha appear only as explicit hypotheses of `WC_abstract`/`WC_groupRing`; none of them is discharged, weakened or strengthened. The false shortcut "a nonzero witness at every `p` ⇒ finite prime support / `J_E ≠ 0`" is used nowhere and is formally refuted by `CM_uniform_denominator` and `CM_nonzero_everywhere`; `WC_abstract_nonvacuous` shows the hypotheses of the abstract theorem are jointly satisfiable, so the implication is not proved from contradictory premises.

**6. Clean-build status:** `rm -rf .lake/build && lake build` ends with `Build completed successfully`. The same sources also build from the repository root (`lake build WitnessContent`) via an added library entry in the root `lakefile.toml` (the package's own frozen lakefile is untouched).

**7. Acceptance-script status:** `bash scripts/acceptance.sh` → frozen check 6/6 OK; clean build OK; no `sorry`/`admit`/`axiom` tokens; `LEVEL: A1_FULL`, `FIRST_NOT_CLEAN_TARGET: None`, `STRETCH_CLEAN: ['lemmaA_general', 'gr_finite_Z', 'gr_rational_trivial']`.

**8. Remaining sorry count:** 0.

**9. Challenged statements:** none — no target turned out to be false, mis-stated or inconsistent, and no package ambiguity needed resolving.

`STATE.json` and `RESUME.md` have been updated with per-target status, the level reached, the helper inventory and the boundary notes.

**Boundary, restated:** this is a machine-checked *conditional* implication. Formalizing WC proves only the implication from the stated witness-content antecedent; it does not prove FIN, finiteness of Sha, `J_E ≠ 0`, or that the antecedent is easier than FIN.