# Summary of changes for run 428469bc-67e1-4e1b-8a30-24797d797890
RUN013 — ARISTOTLE FORMALIZATION OF THE FROZEN 62a1 BSD-AT-2 TARGET

Full details are in `RUN013_FORMALIZATION_REPORT.md` (12 numbered sections, including the theorem-layer map, exact Lean statements, the `#print axioms` table, the 14-question semantic-drift audit, the finite-computation mechanism, and the kernel-verified/external boundary).

============================================================
FINAL RESPONSE BLOCK
============================================================

HANDOFF_ARCHIVE_SHA256 =
652944cf19010247368525f3a68c310c9abc7d3eb20df2a2509c291c5c5d410e

HANDOFF_MANIFEST_SHA256 =
39816c9244f00bdb124aeaf693e5e4772eab21018b5f4fe0af844eb47130c3e7

HANDOFF_IDENTITY =
PASS
(archive hash matches; 29 files; strict `sha256sum -c MANIFEST.sha256` replay 28/28 OK; frozen source-project manifest hash 921fce81c78a3164431da6cf6eb618d37bb3d376108f733c534111726ee55d40 matches; extracted read-only outside the Lean tree and never modified)

LEAN_PROJECT =
. (repository root; library `RequestProject`, modules `RequestProject/Run013/*.lean`)

LEAN_VERSION =
leanprover/lean4:v4.28.0

MATHLIB_IDENTITY =
mathlib4, tag v4.28.0, commit 8f9d9cff6bd728b17a24e163c9402775d9e6a365

LAKE_BUILD =
PASS (clean rebuild of all 18 project modules, no errors, no Lean warnings)

SORRY_COUNT = 0
ADMIT_COUNT = 0
CUSTOM_AXIOMS = none
(no `axiom`, no `@[implemented_by]`, no `native_decide`, no `Lean.ofReduceBool`, no `unsafe`; all headline theorems depend only on `propext`, `Classical.choice`, `Quot.sound`)

PRIMARY_PHI_SELMER_THEOREM =
PROVED — `Run013.phi_selmer_eq`:
`SelmerSet (phiA q) (phiB q) = {cls 1, cls (-31), cls (q:ℚ), cls (-(31*(q:ℚ)))}` for every `q` with `F62 q`.

PRIMARY_DUAL_PHI_SELMER_THEOREM =
PROVED — `Run013.dual_phi_selmer_eq`: `SelmerSet (dualA q) (dualB q) = {cls 1}`.

RUN013_ARISTOTLE_LEVEL_A =
PASS

FULL_2_SELMER_CONSEQUENCE =
PROVED as conditional finite group theory (`Run013.card_middle_of_exact`), on top of the unconditional orders `#Sel^φ = 4`, `#Sel^φ̂ = 1` (`Run013.run013_selmer_orders`).

SHA_2_PRIMARY_CONSEQUENCE =
PROVED as conditional group theory (`Run013.subsingleton_of_exact` for `Ш[2]=0`, `Run013.eq_one_of_two_primary` for `Ш[2^∞]=0`).

RUN013_ARISTOTLE_LEVEL_B =
PASS (unconditional Selmer orders; the comparison exact sequences are ordinary theorem hypotheses, not axioms, since Galois cohomology is absent from mathlib)

BSD_AT_2_BOOKKEEPING =
PARTIAL — kernel-verified: the arithmetic reason for `c_q = 2` (`cq_component_root_iff`), the 2-primary torsion `E_q(ℚ)[2]={O,(0,0)}` and absence of order-4 points (`no_rational_four_torsion`), the period normalization `dX/(2Y) = ½·du/(2v+u+1)` (`descent_differential_is_half_neron`), `v_2(∏c_p)=2`, and the valuation identity `0+2-2=0` (`sha_analytic_two_valuation`). Not formalized: Tate's algorithm, absence of odd torsion, Zhai's analytic input.

RUN013_ARISTOTLE_LEVEL_C =
PARTIAL

STRONG_BSD_EXTERNAL_CHAIN =
RECORDED (prose only; no Lean declaration asserts Zhai, Banwait–Huang or BSD)

RUN013_ARISTOTLE_LEVEL_D =
EXTERNAL_DEPENDENCIES_RECORDED

NO_HIDDEN_Q_BOUND = YES
TRUE_SELMER_OBJECTS_USED = YES (Selmer group defined by local Kummer images at ℝ and every ℚ_p inside the honest quotient `ℚˣ ⧸ squares`; the quartic coverings enter only through the proved bridge `cov_iff_inKummer`)
FINITE_REDUCTION_PROVED = YES (`support_lemma` → `support_reduction` → `squarefree_int_classify`, all before any enumeration)
EXTERNAL_CHECKER_IMPORTED_AS_PROOF = NO
BSD_ASSUMED_IN_PRIMARY_THEOREM = NO
FORMALIZATION_FATAL_ERROR = NO

FORMAL_LIBRARY_OBSTRUCTION =
Galois cohomology of elliptic curves is absent from mathlib: no `H¹(G_ℚ, E[n])`, no `Sel_2(E/ℚ)` as a cohomological object, no `Ш(E/ℚ)`, and no Tate algorithm. Needed for `BSD_CHAIN.md` §2 (isogeny-Selmer comparison and Kummer sequences) and for the Tamagawa numbers `c_2=2`, `c_31=1`. The isogeny-Selmer groups themselves are unaffected — for a two-isogeny with rational kernel they live in `ℚ*/ℚ*²` and are fully formalized — so Level A is complete.

FORMALIZATION_ENGINEERING_GAP =
The handoff excludes the dual class `d = 2` at the prime 2 and the dual classes at 31 by 2-adic/31-adic case analyses. This reconstruction excludes `2` at the moving prime `q` instead (`localq_dual_two`) and `31` via the support lemma (`local31_dual`); both routes are uniform in `q` and use only `q ≡ 5 (mod 8)` and `(q/31) = -1`. The alternative 2-adic exclusion of `d = 2` (which provably needs mod 256, not mod 16) was therefore not required and is not formalized.

SOURCE_EVIDENCE_MODIFIED = NO

PROJECT_MANIFEST_SHA256 =
60c6e5ddef0902b715ed2a361818e18b53879a733c2a35af90b27de3bbb08f51
(recursive manifest of all 26 tracked project files at `PROJECT_MANIFEST.sha256`)

RUN013_FORMALIZATION_REPORT =
RUN013_FORMALIZATION_REPORT.md

NEXT =
INDEPENDENT CLEAN BUILD AND SEMANTIC AUDIT (Level A passes).