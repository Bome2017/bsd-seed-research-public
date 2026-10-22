# SOURCE_AND_HASH_INDEX (2026-09-19)

All paths are under `~/`. sha256 computed at 2026-09-19 ~14:05Z by this hand-off session. "READ" = read by this architect in this
conversation; "carried" = taken from the project's session records or from another listed source without re-reading.

## 1. Primary on-disk sources

| sha256 | path | role | how used here |
|---|---|---|---|
| `1645f4849571c2ac3f49b6d859347dff779ba8726008e150bc741e561a89a690` | `SEED_2243_12_MASTER_CERTIFICATE_2026-09-18/00_CERTIFICATE.md` | Sha[5^inf]=0 DAG N0-N11 (frozen 2026-09-18) | READ (head, nodes, weakest links) |
| `ef0d90f1e17d68c89459aad2dcbe3822f8fb52c58f6fecd118fa5b3cbebdc614` | `BSD_RIGOROUS_STREAM_CORE_2026-09-19/ANALYTIC_RANK_CERTIFICATE.md` | ord_{s=1}L = 2, Arb | READ (statement, data, proof steps 1-3) |
| `cb6f57810f3a9b298c2400525b1b7ed1c2660503f8aabfc4e5f61eee7c04875c` | `BSD_RIGOROUS_STREAM_CORE_2026-09-19/00_REPORT.md` | rigorous stream core report | hash only |
| `276e3ccabbec3548a48d13b3fe1e6a6fb40724a45b010e42ad1fe227af30a549` | `BSD_SEED_2243_12_P3_RIGOROUS_RUN_2026-09-19/SHA3_THEOREM.md` | Sha[3^inf]=(Z/3)^2 theorem + R1/R2 | READ in full |
| `1913ea078daf46c9adf058ad02b82cfa35c8ede35b09b623407484038c9698e8` | `BSD_SEED_2243_12_P3_RIGOROUS_RUN_2026-09-19/P3_CERTIFICATE.md` | rigorous depth-4 p=3 run certificate | READ in full |
| `4433478aa1b9e1286a9921917a6f9b7c5e349c3d3d6a46db0db40f88b8fbe6a2` | `BSD_SEED_2243_12_P3_RIGOROUS_RUN_2026-09-19/P3_FINAL_REPORT.md` | p=3 final report | hash only |
| `2b984abaa1a20fa91a8ad6795b1f3da3fd647832924aaba6049627ff3274892d` | `BSD_SEED_2243_12_P3_RIGOROUS_RUN_2026-09-19/addenda/P3_R2_PERIOD_PROVENANCE_AUDIT.md` | R2 sharpened: gap is exactly p=3 || N | READ in full |
| `3e1c96b05eda41a0eb9652c4d92e09a67c1b604e4fb4c7a03d7fce0770985d20` | `BSD_SEED_2243_12_GLOBAL_ARCHITECT_2026-09-18/FULL_BSD_SEED_DAG.md` | older global DAG (G0-G28) - SUPERSEDED as top-level architecture | carried via F2 |
| `099c84a350f33afa9d2ad668c7de650e45958ee19db2d3410f86bb03c2bbd3a8` | `BSD_SEED_2243_12_GLOBAL_ARCHITECT_2026-09-18/fable_audits/F1_P3_HOSTILE_AUDIT.md` | p=3 chain audit PASS_WITH_CORRECTIONS; R1-R8 | carried via SHA3_THEOREM section 4 |
| `96e16935e1b19883aa068f9451017e6316f7ac164ec26547fccf801e81e4cd49` | `BSD_SEED_2243_12_GLOBAL_ARCHITECT_2026-09-18/fable_audits/F2_MINIMAL_FULL_BSD_AUDIT.md` | MINIMAL_SET_NEEDS_REPAIR; Criterion SS; 4547; FIN/FORMULA | READ (verdict, sec B.1, sec F) |
| `f04a1b3f0cb229ea967ab52d60bd95df98d019a0958dee7baf642237d2d479df` | `BSD_SEED_2243_12_GLOBAL_ARCHITECT_2026-09-18/fable_audits/F3_LARGE_P_SHA_HUNT.md` | large-p hunt NOT_FOUND; Ota near miss | READ in full (earlier in this conversation) |
| `1894fc91ff1605972ff434649c38c32a9abdf2fbf5d270885c085dec012204c7` | `BSD_SEED_2243_12_GLOBAL_ARCHITECT_2026-09-18/fable_audits/F4_SECOND_DERIVATIVE_RATIONALITY_HUNT.md` | archimedean hunt NOT_FOUND | READ in full (earlier in this conversation) |
| `6b347683743eee1ba21649c379b076b4e3c7bcd85d212fdafd69e13ebf138bcf` | `BSD_SEED_2243_12_RANK2_GLOBAL_OBJECT_2026-09-18/RANK2_GLOBAL_OBJECT_COMPOSITION.md` | LINE design lane (use the AUDIT where they differ) | authored in this conversation |
| `4e7208397257f75fc955dcb0da04d73b184bccf08cb50d1f94cac3332733c178` | `BSD_SEED_2243_12_LINE_HOSTILE_AUDIT_2026-09-19/LINE_HOSTILE_AUDIT.md` | LINE_THEOREM_C_PASS_WITH_CORRECTIONS; (N); C1-C7 | authored in this conversation |
| `fab04792bd667a0805fc6554cf1e420dea6947a05f15e1cada89dd1da99bbfb5` | `SEED_2243_12_MECHANISM_LANES_2026-09-18/00_LANE1_SYNTHESIS.md` | H9 calibration; NC5; Castella gate | READ (operator review + top line) |
| `277eba753f7b541a6390420b1cd31837647bcee9bce3f657962140e3944369e4` | `BSD_LANE2_SEED_TO_FAMILY_2026-09-18/LANE2_REPORT.md` | regulator transport; ONE-BIT | carried from session record |
| `5d7e98b091198b1f305742ef0cea3208ede48003f858c6035f621e9a30ee7d6e` | `BSD_SEED_2243_12_FULL_BSD_LANE3_2026-09-18/00_REPORT.md` | certified numerics L''/2, Sha_an = 9; prime table (partly superseded) | READ (sections 1-2 head) |
| `6a29866d31fe08f7dd5c686066c9eb97397657be0a40d52c03c9798d322415ee` | `BSD_SEED_2243_12_LANE4_AUDIT_FORMAL_2026-09-18/00_REPORT.md` | v2(c0)<=8 audit; 4 Lean files | READ (Lean section lines) |
| `7062cfd0c5fe2f212e29f7d3aa244b088f262e38bb5a189f996cd66cc4850685` | `H9R19_WEIGHTED_RECIPROCITY_2026-09-15/08_PROGRAM_STATUS_FREEZE.md` | program ledger (merged blocks live here) | hash only |
| `6e0ff500095737c687c304fe934bda32c36ff1e511e8810293a93a61b74f9d04` | `BSD_SEED_2243_12_R2_LEADING_TERM_BRIDGE_2026-09-19/R2_LEADING_TERM_BRIDGE_DESIGN.md` | R2 bridge design (corrections in its §11; the audit governs) — authored in this conversation | authored |
| `cc95623276f3f4e90640c6eebab5c714c323855addd3154073e9326cf46f9e13` | `BSD_SEED_2243_12_R2_LEADING_TERM_BRIDGE_2026-09-19/LEMMA_U_AND_P5_UNIT_AUDIT.md` | self-audit: Lemma U = BKS I Thm 7.3; u₅ ≡ 1 mod 5 — authored in this conversation | authored |

## 2. The p = 5 rigorous upgrade — SEALED (`P5_RIGOROUS_SHA5_ZERO_CONFIRMED`); hashes taken 2026-09-19 07:30 PDT

| sha256 | path | role / how used |
|---|---|---|
| `eb583f83f9b4c78331f34d7240ee90df3fee634edacfd07183f3a182ac5b9c77` | `BSD_SEED_2243_12_P5_RIGOROUS_UPGRADE_2026-09-19/P5_RIGOROUS_REPORT.md` | RETURN P5_RIGOROUS_SHA5_ZERO_CONFIRMED (READ: head, result table, method) |
| `2dfa96d000efa7a4862674f5cdc7953341fcc5fb3ef0e4308281456eba441d77` | `BSD_SEED_2243_12_P5_RIGOROUS_UPGRADE_2026-09-19/P5_CERTIFICATE.md` | rigorous replacement of node N7 (READ: head) |
| `adfa6a96cd23041938d91c92629c4572b3c967a3d02b639d8aef0d73106a27d0` | `BSD_SEED_2243_12_P5_RIGOROUS_UPGRADE_2026-09-19/SHA5_RIGOROUS_THEOREM.md` | Sha[5^inf] = 0 with N7 at proof grade (READ in full) |
| `4a00292c74b8b0d795e3c59cf3ec6c1d76d598b162aa027ecec6457392c3318b` | `BSD_SEED_2243_12_P5_RIGOROUS_UPGRADE_2026-09-19/P5_REPLAY.md` | replay status PASS (READ: table) |
| `630fa14ddec1d47807f31b736d7c5cba8ecafbdcf57de1d1045dd35bb70a1c58` | `BSD_SEED_2243_12_P5_RIGOROUS_UPGRADE_2026-09-19/P5_RESOURCE_LOG.md` | resources (hash only) |
| `d010edc983503ecbdd9b3e87738839797ff1771f26a60c96ceddfdcd974fcd44` | `BSD_SEED_2243_12_P5_RIGOROUS_UPGRADE_2026-09-19/P5_MANIFEST.sha256` | 9 424 entries; the five report files checked against it by this architect; full verification reported by the owning session |
| `c2bb05a2c83bbb8d5f51ad2da92303eed44aec959e0450f3b814758037f1708b` | `BSD_SEED_2243_12_P5_RIGOROUS_UPGRADE_2026-09-19/STATE.json` | phase DONE__P5_RIGOROUS_SHA5_ZERO_CONFIRMED, merged false (READ) |
| `cbef3def433279e904244245617ec7067109c477e03a17276325d2bfd10ab458` | `BSD_SEED_2243_12_P5_RIGOROUS_UPGRADE_2026-09-19/run/P3_CHECK.txt` | stage C check (generic checker name) (READ) |
| `3b100824795bdd9445bbf91fa03ad24d25f8271e6f7e358d1cf9cfc49506fdba` | `BSD_SEED_2243_12_P5_RIGOROUS_UPGRADE_2026-09-19/downstream/P5_DOWNSTREAM.txt` | routes A/B/C, normalisations (READ) |
| `8f14edece2db3f46763880361102b4f2fe8acc019bdeb695e10f69b675a13a9c` | `BSD_SEED_2243_12_P5_RIGOROUS_UPGRADE_2026-09-19/downstream/INTEGRITY.txt` | independent re-hash (READ tail) |
| `de48225ff58e80a0260204a14b87586c6e6e02d6a65eb446f5c426dca6e360f8` | `BSD_SEED_2243_12_P5_RIGOROUS_UPGRADE_2026-09-19/downstream/CROSS_RUN_P3.txt` | a_q byte-identical to the p = 3 run (READ) |
| `863110b74eef7c792045117e0524f1ffff7d93cf0ed74a54e2930a2d865d9e3f` | `BSD_SEED_2243_12_P5_RIGOROUS_UPGRADE_2026-09-19/logs/stageW_summary.txt` | Stage W totals (READ) |

Coefficient roots: p = 3 run `5f9994d95c31a49e7cbd91435fd33a9cbdadc81fcc4f47439fbbf2fa5bb4713f` (885 segments), `ca234d65fa40332695f5f08675ade782c9a8439bee068b69ac9b64a470002084` (segments 0..287);
p = 5 upgrade `fcd024375b54642344d03502caf0c53882190973ab2683239011f813ca2848d4` (467 segments; CROSS_RUN_PASS: identical to the p = 3 run on the shared range).

## 2b. CRITERION_SS hostile gate — `CRITERION_SS_VALID_WITH_CORRECTIONS` (2026-09-19)
| sha256 | path (under ~) | content |
|---|---|---|
| `7c58bb165fe75ac92390ded335e1d616f4cc455ea9b9c06a47150ed33765fe59` | `BSD_SEED_2243_12_CRITERION_SS_HOSTILE_GATE_2026-09-19/CRITERION_SS_HOSTILE_GATE.md` | verdict, surviving theorem, 9 attacks, corrections C1–C6, validation (446d1 p = 19, 61; 389a1 p = 107), provenance P1–P6 |
| `805e255ac54126c179e82675b566b3fe79c2021a841a000b716de21ec4284a80` | `BSD_SEED_2243_12_CRITERION_SS_HOSTILE_GATE_2026-09-19/AUDIT_MANIFEST.sha256` | custody of the gate folder (9 files) |

## 2c. Cross-family frontier attack (Codex, 2026-09-19; `BSD_FRONTIER_UNKNOWN`) and the Opus cross-check
| sha256 | path (under ~) | content |
|---|---|---|
| `41611609b1cb8537aae9a1dd16e6618d30274b582cd88802ab379b55eb1dfeaa` | `BSD_CODEX6_FRONTIER_ATTACK_2026-09-19/00_VERDICT.md` | verdict BSD_FRONTIER_UNKNOWN and the thirteen answers |
| `182bf46ded79383ef3912c19def8fd89de28b73608d8faf12deb088ffdc52145` | `BSD_CODEX6_FRONTIER_ATTACK_2026-09-19/REGULATOR_CERTIFICATE.md` | rigorous Reg, Ω, Ω·Reg and q_∞ interval; trust base |
| `6e53a287a4804e3bc09b3dae8749c64f7f2ce0e5a3cf8c94cce2c1c7711aefcd` | `BSD_CODEX6_FRONTIER_ATTACK_2026-09-19/verify_regulator.py` | standalone certificate script (Python Fraction + Decimal, directed rounding) |
| `eaaf833f7e92ca78aa75003e8e2eaedab4cfddfa875983f808e6db19746e93a4` | `BSD_CODEX6_FRONTIER_ATTACK_2026-09-19/REGULATOR_INTERVAL_100D_30.json` | certificate output at 100 digits / 30 terms |
| `664305c162af37c25fb2a8b1a3a6869354fc6bb8f1eca2e826e08207796ae18c` | `BSD_CODEX6_FRONTIER_ATTACK_2026-09-19/REGULATOR_INTERVAL_80D_24.json` | replay output at 80 digits / 24 terms |
| `556ecfa56f87f4497cdc7f2e25db3ec6a5431b2a70393ccbb80ea96fc085738e` | `BSD_CODEX6_FRONTIER_ATTACK_2026-09-19/WITNESS_CONTENT_THEOREM.md` | WC theorem (conditional on Ota 5.17/6.4), countermodels |
| `8dcd44af28fef1648a0a0e37085eda632f80bca2aa214585df6935c797d3f8b6` | `BSD_CODEX6_FRONTIER_ATTACK_2026-09-19/ALGEBRAIC_REDUCTION_LEMMAS.md` | Lemmas A–H (augmentation, descent, contraction, spacing, Lemma E, p-adic digits, FIN ⇏ order 9) |
| `8b7c91a24d0450699953447c58ab58e7dd0c522d9739698011e5c70a0d842387` | `BSD_CODEX6_FRONTIER_ATTACK_2026-09-19/COMMON_OBJECT_ANALYSIS.md` | one-sided common certificate B (proposition + proof) |
| `810b5f5f7ec3da00de596f9a944b69b47655c52c713d0ce160db49a413f8a74f` | `BSD_CODEX6_FRONTIER_ATTACK_2026-09-19/NEW_THEOREM_DAG.md` | corrected DAG |
| `d5098589066dda8d371d23640d21e5b095ceac6af57d1021c15f5adfce0d47d3` | `BSD_CODEX6_FRONTIER_ATTACK_2026-09-19/FORMULA_ATTACK.md` | FORMULA minimum-strength attack |
| `0fb5b18c5c773978dff0770c1e04178860d0f12ac619e132b71b7bdb3e681dfc` | `BSD_CODEX6_FRONTIER_ATTACK_2026-09-19/FIN_ATTACK.md` | FIN frontier and WC attack |
| `2f19d86fe01191d76f34c12038ce4d56b25c5e50b964d61a82fdc52b6d7bd699` | `BSD_CODEX6_FRONTIER_ATTACK_2026-09-19/FORMALIZABLE_GAPS.md` | Codex formalization proposal (Packages A, B) |
| `29997d2337802a45c8b3a1237894177c980445ff2289bf900a03d10422ca19bb` | `BSD_CODEX6_FRONTIER_ATTACK_2026-09-19/MANIFEST.sha256` | custody of the Codex folder (27 files, re-verified 27/27 by Opus) |
| `b714fce95ccb886bf1bb83926800466fc6a793e35a941f1995aec01233ab3104` | `BSD_SEED_2243_12_FIN_ASSUMED_FORMULA_AUDIT_2026-09-19/ADDENDUM_CROSS_FAMILY_2026-09-19.md` | Opus cross-check: certificate replay identical at both settings; corrections accepted; WC caveat |
| `1d8d689a2d591994938aa372560ad30299c0a2bec318690d4f2e7b82ab8e316c` | `BSD_SEED_2243_12_FIN_ASSUMED_FORMULA_AUDIT_2026-09-19/FIN_ASSUMED_FORMULA_REDUCTION_AUDIT.md` | Opus: FIN (with #Sha = 9) assumed ⇒ FORMULA ⟺ bounded rationality (FORMULA_REDUCES_TO_RATIONALITY_DENOMINATOR) |
| `7b3e32bcd2f536b0e1b581b3d81babf62488b081df566b24fb6083e69f0eb93f` | `BSD_SEED_2243_12_FULL_BSD_LANE3_2026-09-18/B_invariants/06_period_regulator.md` | HISTORICAL: Lane 3 Arb interval Ω/Reg (labelled CERT-NUM there); superseded by the certificate above, kept unedited |

## 2d. Aristotle formalization freezes (2026-09-19)
| sha256 | path (under ~) | content |
|---|---|---|
| `dfe5f660d750cbe835f04369db052b6f8d3a5984322ea92a94863d0d9567e1ef` | `BSD_ARISTOTLE_FORMALIZATION_FREEZE_2026-09-19/A1_WITNESS_CONTENT_FULL_FREEZE_2026-09-19.tar.gz` (103463 bytes) | A1 successor freeze: A1 WC FINITE-ALGEBRA FORMALIZATION = MACHINE-CHECKED · STATUS = CONDITIONAL · LEVEL = A1_FULL · ARITHMETIC ANTECEDENT A != 0 AND A ∈ J_E = NOT PROVED · FIN STATUS = UNCHANGED. Custodian replay from a fresh unpack (Lean v4.28.0, mathlib 8f9d9cff6bd728b17a24e163c9402775d9e6a365) |
| `278588e0c570e39379e7dd2a495153d984be12e4269fee212e3830cc15e59948` | `Downloads/0ee48359-59b9-4108-a7fd-0ee16939d0e4-aristotle.tar.gz` (copy in the freeze `provenance/`) | Aristotle's returned A1 archive (its internal pre-run MANIFEST.sha256 is stale by design; superseded by the freeze manifest) |
| `eba016585d080c5bf8578b3c4454d63a256712a6770ba50f3a0f671667a04763` | `BSD_ARISTOTLE_PACKAGES_2026-09-19/ARISTOTLE_A1_WITNESS_CONTENT_2026-09-19.tar.gz` | the original A1 package as sent (frozen Defs/Spec/Acceptance unchanged in the return) |
| — | `BSD_ARISTOTLE_FORMALIZATION_FREEZE_2026-09-19/A2_PRIMARY_SUPPORT_FULL/` | A2: no successor freeze yet (result not recorded; do not infer) |

## 3. Unreconciled items / seams (no mathematical contradiction found)

1. **R2 (p = 3).** R2 remains OPEN as a provenance seam, narrowed to the canonical-vs-Gross period comparison for p = 3 with 3 ∣ N (source-reading addendum `P3_R2_PERIOD_PROVENANCE_AUDIT.md`: in print only for p ≥ 5, p ∤ N — Kim–Ota 2023, Pollack–Weston 2011; no located source covers the seed's case; nothing found shows it fails). It is load-bearing for BOTH finiteness and the order of Sha[3^∞]. The label "PROVED_COMPUTER_ASSISTED relative to Skinner Thm A as printed" is F1's recommended label, confirmed unchanged by the addendum; a cross-family reader may judge it differently.
2. **R1 (p = 3).** Jones 1989 unread.
3. **RANK.** rank E(Q) = 2 rests on a 2025 arXiv preprint (Zywina) plus an exact PARI 2-descent replay; Sha[2] = 0 is taken from the preprint (PARI s = 0 consistent).
4. **Numerics.** SUPERSEDED on 2026-09-19.
   - Reg, Ω and Ω·Reg are now rigorously enclosed (Codex `REGULATOR_CERTIFICATE.md`, §2c; the Opus replay is identical), so q_∞ ∈ (35.99427, 36.00573) is PROVED_COMPUTER_ASSISTED.
   - The earlier wording "Reg and C are PARI values (CERTIFIED_NUMERIC), not Arb enclosures" was incorrect. Lane 3 `B_invariants/06_period_regulator.md`
     (historical, §2c) already used Arb interval Tate series. Its tail step used a non-directed RR logarithm with a safety factor; Codex replaced that step with an exact bound.
   - Still CERTIFIED_NUMERIC: the 15-digit L″ value (q = 36 ± 3·10⁻¹⁵), which is not a rigorous ball.
   - These items affect FORMULA's evidence only, not any Sha[p^∞] theorem.
5. **p = 5.** RESOLVED: the rigorous upgrade is finished and sealed (`P5_RIGOROUS_SHA5_ZERO_CONFIRMED`); N7 is PROVED_COMPUTER_ASSISTED and #Sha[30^∞] = 9 carries no CERT-NUM qualifier. Residual custody note only: the frozen master certificate file is unedited and still prints N7 = CERT-NUM; the successor `SHA5_RIGOROUS_THEOREM.md` governs the grade; neither is merged into the ledger.
6. **Architecture wording.** F2 calls S_4547 "a third genuine root W3"; this hand-off files it under FIN as instructed. Both are correct in their own frame (prime-by-prime versus global).
7. **Normalisation.** Master certificate N9 quotes 152 ≡ 2 (mod 5) (ω₁ normalisation) while Lane 2 quotes a₂^{SW} ≡ 1 (mod 5) (Néron normalisation). Reconciled: factor 2 = Ω⁺/ω₁, a 5-adic unit (stated explicitly in the p = 5 upgrade downstream log).
8. **Same-family audits.** See `00_READ_FIRST.md` §6.
9. **Sources not read by anyone in the project** (from the records): Mazur–Tate Duke 1987 (Tan 1995 restatement used), Edixhoven 1991 (restatements used), Jones 1989, Pollack–Weston 2011 beyond the cited parts, Bertolini–Darmon 1994/95/2005, YZZ book, Kato Astérisque 295 (secondary statements), Fouquet–Wan proof details.
10. **Costs never re-derived:** ≈ 2·10⁴ / 10⁵ CPU-h at 2243 / 5843; Ota per-prime certificate cost. (CRITERION_SS cost was RE-DERIVED by its gate with exact T_min: ≈ 270 / 460 CPU-h at p = 23 / 29, replacing F2's ≈ 120.)
