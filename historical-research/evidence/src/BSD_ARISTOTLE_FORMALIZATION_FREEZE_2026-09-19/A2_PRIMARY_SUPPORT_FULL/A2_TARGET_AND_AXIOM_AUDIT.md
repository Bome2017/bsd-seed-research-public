# A2_TARGET_AND_AXIOM_AUDIT — 28 targets, frozen types, axioms (fresh replay, 2026-09-19)

## 1. Frozen files vs the ORIGINAL package (byte comparison against the original tarball `36005a0c…`)
| file | sha256 | result |
|---|---|---|
| PrimarySupport/Defs.lean | `d5853edd3c09da27afea8d22b04d0b42c088e5982cded91e9879e04d3fcb0699` | BYTE-IDENTICAL |
| PrimarySupport/Spec.lean | `80d452c2adf830d8d87ce4f4c49a4d686bb4ba5dbc2bf5cbb541c002aa96c2d4` | BYTE-IDENTICAL |
| PrimarySupport/Acceptance.lean | `d586dfd7664c3f75f070dda0e2a16093fc3ad0b7c6e143d3e329fbe5ed4c2624` | BYTE-IDENTICAL |
| lakefile.toml | `7624412eb37e5f6768819f2dc4740efa9cf724c214d91681475827b2c1416bc0` | BYTE-IDENTICAL |
| lean-toolchain | `db7bb24b756d745bbde83fe92718b51bd3625dae3701ba0f598d0eedcd3f3028` | BYTE-IDENTICAL |
| scripts/level.py | `97eae442086888051ca8c017eaeedc533616b80970303e51a50cbb43ca6ca95e` | BYTE-IDENTICAL |

Also unchanged: `scripts/acceptance.sh`, `scripts/FROZEN.sha256`, `lake-manifest.json`, the root `PrimarySupport.lean`, and all
package documents except `STATE.json` / `RESUME.md`.
- Changed: `Targets.lean`, `STATE.json`, `RESUME.md`.
- New: `CodexExample`, `Content`, `Countermodels`, `Depth`, `Descent`, `LemmaB`, `Order`, `Pairing`, `Primary`, `Symplectic`
  (all `.lean`), plus `build.log` and `axioms.log`.
- Full table: `replay/frozen_and_file_comparison.txt`.

## 2. The 28 targets
All 28 have their declared type **syntactically** equal to `PrimarySupport.Spec.<Name>` (TypeIntegrity), and all are CLEAN in
the fresh probe.
- **Axioms.** Every target uses exactly {propext, Classical.choice, Quot.sound}, except `primary_zero_of_torsionfree`, which uses
  only {propext, Quot.sound}.
- **Kernel re-check.** "✓" in the table marks a fully qualified `example` re-check.

| level | theorem | re-check | proof (helper) |
|---|---|---|---|
| CORE | primary_zero_of_torsionfree | | Primary.primaryPart_eq_bot_of_torsionfree |
| CORE | torsion_decomposition | | Primary.torsion_decomposition_aux |
| CORE | assembly | | Primary.finite_of_primary |
| CORE | assembly_WC_shape | ✓ | Primary.finite_of_primary_WC_shape |
| CORE | JOf_ideal | | Depth (zero/add/mul closure) |
| CORE | JOf_ne_zero_iff | ✓ | Depth.exists_ne_zero_mem_JOf_iff |
| CORE | positive_depth_divides | | Depth |
| CORE | content_dvd_iff | | Content |
| CORE | content_padic | | Content |
| CORE | CM_each_local_finite | ✓ | Countermodels (⨁_p ZMod p) |
| CORE | CM_finite_support | ✓ | Countermodels (ℕ →₀ ZMod 2) |
| CORE | CM_nonzero_everywhere | ✓ | Countermodels (p² ∈ ZMod p³; J = {0}) |
| CORE | CM_profinite_perfectness | ✓ | LemmaB (cm3v) |
| FULL | finite_iff_local_and_support | ✓ | Primary.finite_iff_local_and_support_aux |
| FULL | JOf_generator | | Depth.JOf_eq_multiples |
| FULL | content_basic | | Content |
| FULL | content_unimodular | | Content |
| FULL | exists_primitive | | Content |
| FULL | content_mod_pk | | Content |
| FULL | content_bounds_J | ✓ | Descent.exists_ne_zero_mem_JOf_of_content_bound |
| FULL | lemmaB_valuation | | LemmaB |
| FULL | lemmaB_cokernel | | LemmaB |
| FULL | card_eq_prod_primary | | Order.card_eq_prod_primary_aux |
| FULL | order_nine_t_sq | ✓ | Order.order_nine_t_sq_aux |
| FULL | CM_order_441 | ✓ | Order (G441 primary-part lemmas) |
| STRETCH | alternating_square | ✓ | Symplectic.Symp.isSquare_card (ZMod N target) |
| STRETCH | CM_noncyclic_target | ✓ | Pairing (cross product on (ZMod 2)³) |
| STRETCH | CM_codex_torsion_example | | CodexExample |

- **Totals.** 13/13 CORE and 12/12 FULL targets are CLEAN, so the LEVEL is **A2_FULL**; STRETCH is 3/3;
  FIRST_NOT_CLEAN_TARGET = None.
- **Remaining `sorry`/`admit`: 0.** The fresh build has no `sorry` warning, and the only textual "sorry" tokens are comments.

## 3. Result
**No target-integrity defect and no mathematical discrepancy.** The seven boundary points are read against the proofs in
`A2_FORMAL_BOUNDARY.md` §2.
