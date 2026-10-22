# Summary of changes for run 8d539419-e7bc-4d92-bfce-0a1944c65790
## Result: A2_FULL_PROVED (all three STRETCH targets clean as well)

I unpacked `ARISTOTLE_A2_PRIMARY_SUPPORT_2026-09-19.tar.gz` into `pkg/A2_PRIMARY_SUPPORT/`, verified `MANIFEST.sha256` (all entries OK at unpack time), ran the baseline (`BELOW_A2_CORE`, 28 frozen `sorry` targets, Lean 4.28.0 / mathlib `8f9d9cff6bd728b17a24e163c9402775d9e6a365`), and then proved every target.

**1. Frozen targets proved (28/28, all with their exact packaged types).**
CORE (13): `primary_zero_of_torsionfree`, `torsion_decomposition`, `assembly`, `assembly_WC_shape`, `JOf_ideal`, `JOf_ne_zero_iff`, `positive_depth_divides`, `content_dvd_iff`, `content_padic`, `CM_each_local_finite`, `CM_finite_support`, `CM_nonzero_everywhere`, `CM_profinite_perfectness`.
FULL (12): `finite_iff_local_and_support`, `JOf_generator`, `content_basic`, `content_unimodular`, `exists_primitive`, `content_mod_pk`, `content_bounds_J`, `lemmaB_valuation`, `lemmaB_cokernel`, `card_eq_prod_primary`, `order_nine_t_sq`, `CM_order_441`.
STRETCH (3): `alternating_square`, `CM_noncyclic_target`, `CM_codex_torsion_example`.
All five mandatory countermodels are proved, not weakened.

**2. Targets remaining:** none.
**3. First remaining formal obstruction:** none.

**4. Helper lemmas introduced** (new files under `pkg/A2_PRIMARY_SUPPORT/PrimarySupport/`, frozen files untouched): `Content.lean` (content divisibility, nonnegativity/vanishing, unimodular invariance, primitive factorisation, p-adic and `ZMod p^k` forms incl. the truncation case), `Depth.lean` (`vInf`/`JOf` translation to prime-power divisibility, ideal closure, nonzero criterion, generator, the `JOf = {0}` half of CM2), `Descent.lean` (L7), `LemmaB.lean` (B1, B2 and the CM3 valuation datum), `Primary.lean` (primary-part triviality, torsion decomposition by strong induction on the annihilator, the summation surjection and assembly, P4/P5), `Countermodels.lean` (CM1, CM1′), `Order.lean` (primary-part order is a prime power, H0 by a divisibility-plus-surjection sandwich, H2, CM4), `Pairing.lean` (S2), `CodexExample.lean` (S3), `Symplectic.lean` (S1, by splitting off hyperbolic planes).

**5. External assumptions / axioms:** none added. No `axiom`, `sorry`, `admit`, `native_decide`, `@[implemented_by]`. Every arithmetic input (finiteness, the square-order Cassels–Tate input, the 2-/3-/5-primary data, the comparison lattice vector of L7, the depth function) remains an explicit hypothesis of the abstract statement. `#print axioms` for all 28 targets shows only subsets of `{propext, Classical.choice, Quot.sound}`.

**6. Clean build:** yes — `rm -rf .lake/build && lake build` inside the package completes successfully with zero warnings; the library also builds from the repository root via an added convenience `lean_lib` target (the package's own frozen `lakefile.toml` is unmodified).

**7. Acceptance script:** `bash scripts/acceptance.sh` exits 0: frozen files OK (6/6), clean build, no `sorry`/`admit`/`axiom` tokens in code, axiom probe clean, `LEVEL: A2_FULL`, `FIRST_NOT_CLEAN_TARGET: None`, `STRETCH_CLEAN: [alternating_square, CM_noncyclic_target, CM_codex_torsion_example]`. Re-checking `MANIFEST.sha256` shows exactly three intentional differences: `PrimarySupport/Targets.lean` (the proofs), `STATE.json` and `RESUME.md` (updated as required); every frozen file is byte-identical.

**8. Remaining sorry count:** 0 (the only textual occurrences are in the packaged doc-comment of `Targets.lean`).

**9. Nothing was shown false or inconsistent:** every packaged statement was provable exactly as given; no hypothesis was added, removed or weakened.

Notes on the mathematical content: the separation demanded by the package is machine-checked in both directions — P5 states the exact conjunction, while CM1 (`⨁_p ZMod p`) and CM1′ (`ℕ →₀ ZMod 2`) show neither conjunct suffices, CM2 shows nonzero local witnesses everywhere do not give finite prime support, and CM3 shows finite local cokernels over the profinite product do not. The correction is preserved: H2 concludes `#G = 9t²` with `gcd(t,30)=1` under its explicit hypotheses, and CM4 exhibits order 441 satisfying all of them, so `#G = 9` does not follow. S1 is proved only for a cyclic target `ZMod N`, and S2 proves the packaged non-cyclic counterexample, so the general "alternating nondegenerate ⇒ square order" statement is not available. This formalization proves nothing about any elliptic curve: it does **not** prove FIN, finiteness of Sha, `J_E ≠ 0`, `#Sha = 9`, or BSD.
