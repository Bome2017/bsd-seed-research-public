# Audit of the 10-13 work and next paths toward the real seed (2026-10-14)

Claude, Opus 5.5. Inputs: the five Codex returns dated 10-13 afternoon/evening (local + lab `121d0381`), the Fable
invention panel `~/BSD_INVENTION_PANEL_CLAUDE_2026-10-13/`, the record. Independent replays are in `checks/`.
**FIN, ORDER9 and Q36 are unchanged.** FIN at rank two is unsolved with no known method; Banwait 2609.08431 §1 attests
that even "Ш[p] = 0 for infinitely many p" is open for every rank ≥ 2 curve over Q.

## 1. What Codex added after the panel's snapshot

| Return | Result | Endpoint effect |
|---|---|---|
| `BSD_UNRESOLVED_SEED_PUSH_2026-10-13` (lab 10a9fc84) | Ш[83^∞] = 0, Ota witness ℓ = 167, c₂ ≡ 44 | record only; floor 25,281 unchanged (53 open) |
| `BSD_UNIT_ADMISSION_CONTINUATION_2026-10-13` (lab 628d8027) | seed unit component at 3 exhausted; filtration (0,1,1) no longer needs class-group completeness; norm Smith (3,3); **historical local kernel 7 → 4 corrected** | none; the norm bound stops at the uncontrolled count of p-Smith factors |
| `BSD_JOINT_ADMISSION_AND_METHOD_DISTILLATION_2026-10-13` (lab 121d0381) | 12 seed tame rows give 288; 4 ordinary corrected quotients give 9 mod p at 5, 7, 11, 13; three complete 3-descent controls with kernel = point plane | none; residue-level agreement only |
| `BSD_CLASS_LIFT_COUPLING_EXPERIMENT_2026-10-13` | **interrupted at Codex's limit**, STATE "running", local only; 718b1 and 997c1 class directions repaired into points | none; control experiment |
| lab GitHub | tip `121d0381` = all finished returns pushed; research repo `main` still v0.2.2, reference v0.2.6 lacks p = 83 | — |

## 2. The Fable panel, checked

Held up under independent check:
- **Kim 2609.15328 Thm 1.4** (ordinary Kolyvagin conjecture) has no semistability hypothesis; semistability enters only
  at supersingular p (Thm 1.1 second sentence, Thm 1.5). Read at the saved text, lines 135-197. The record's
  "semistable-only" registration is wrong for ordinary p.
- **Valuation-law domain.** `VM/PROOF.md` §6: the Tate transvection at 2243 gives BCS (im) at every good ordinary
  p ≥ 5; {19, 59, 487} are not hypotheses. Note the 10-07 desk (`BSD_EXIT2_ETA_EVEN_ORDER_DESK_2026-10-07`) already
  had the "iff" form; 10-13 adds the exact length equality including nonunit regulators.
- **R± mixing.** With a_p = 0, (1−φ/p)² = ((p−1) − 2φ)/p, so the ± coefficients see R⁺ = (p−1)R_ω + 2pR_F and
  R⁻ = (p−1)R_F − 2R_ω. Re-derived by hand; the panel's correction of its own lemma is right.
- **Tenth tame-law point.** `checks/tame83_audit.gp` (fresh 10-06 audit code, not the prescreen code): R(83,167) = 42,
  a₁₆₇ = 0, w ≡ 39 ≡ 288 (mod 83); second primitive root consistent. Seventh sealed forecast confirmed.
- **p = 53 package.** `checks/tame53.gp`: R(53,107) ≡ 0 for both primitive roots (ℓ = 107 cannot certify);
  R(53,743) = 26, a₇₄₃ = −32, law prediction c₂ ≡ 20 (mod 53) = the package's sealed value.
- **L8 exceptional set** {11,17,19,23,59,127,379,487,2273} = the odd prime factors ≥ 5 of ℓ ± 1 for ℓ ∈ {2243, 5843,
  4547}. Consistent.

Overstated or wrong:
- **The panel's §5 "next attack" is a closed lane.** Its desk kill test ("what plays η at positive even order") was
  run on 10-07: `BSD_EXIT2_ETA_EVEN_ORDER_DESK_2026-10-07`, verdict ETA_AT_POSITIVE_EVEN_ORDER_IS_Q, Exit 2 merged into
  Exit 1. Its arithmetic test (Ψ₃) was not well defined: Ψ_p is a cup product with H¹(G_S, ad⁰), landing in
  Ш²_S(E[p]) ≅ Ш¹_S(E[p])^∨ on Ш-classes, with no mechanism for nondegeneracy. The session card proposed for it on
  10-13 was withdrawn.
- **L7 is one fact, not two.** The F-side value 25 follows from the A-side value 1 and the record's proved isogeny
  identities (L2_F = 5·L2_A, det H_F = det H_A, Tam_A/Tam_F = 5): in `padic7_*.out` the two regulators are identical
  and jj_F/jj_A ≡ 5 mod 7³. The independent content is q_A ≡ 1 (mod 7³, 13²): p-adic BSD consistency on a rank-two
  curve with trivial Ш.
- **L1's norm identity** is BSD-shaped bookkeeping for the rank-0 Weil restriction B_ℓ; v_p(N) = 2 ⟺ c₂ ≢ 0 is
  immediate from θ ∈ I². No cross-p content, as the panel itself concluded.

The panel's headline verdict (no admissible candidate; every new coordinate is length Ш[p^∞] or a bound on it) agrees
with the record.

## 3. Next paths toward the real seed, ranked

1. **Seed exact-law test beyond depth 1 and at the Ш-prime** (`~/BSD_SEED_FULL_LEVEL_LAW_TEST_2026-10-14/`, sealed
   today). Four new seed tables at ℓ = 101, 109, 127, 163 test the per-level identity mod 25, 27, 63, 81 — cells the
   record lists as untested ("odd Ш (seed 9) … the seed beyond depth 1"). ℓ = 163 checks that the MT coefficient
   carries exactly 3² at the prime where Ш[3^∞] ≅ (Z/3)² is proved. About 18 CPU-h local, $0, inside the existing
   coefficient prefix. Endpoint effect: none; it confirms or breaks the exact form of the only live target (G1/MI-1).
2. **p = 53 at ℓ = 743** (`~/BSD_P53_L743_RUN_2026-10-01/`, frozen a766881, PREFLIGHT 27/27). 263 CPU-h central,
   59-77 h wall, idle Mac, $0. Needs a Codex package review, then the user's "go 53b". Gives Ш[53^∞] = 0 if c₂ ≢ 0 and
   raises the conditional floor from 25,281 to 31,329. Record only.
3. **Close the interrupted class-lift run** when Codex is back: finalize STATE as stopped-at-limit with the two
   completed controls, or finish its 24-candidate cap. Collateral either way.
4. **Do not start:** bad-prime certificates (22.5k-71k core-h each; premature while the tail is open), more control-
   curve panels without a stated hypothesis, the Exit-2 congruence lane (closed 10-07), more digits of q (DNR 36).

New mathematics: the live lane is Exit 1 alone. Its missing input MI-1 (one rational α with ᾱ_p ≡ α mod p for almost
all p; equivalently the MT refined conjecture at prime levels, rank two, with the 2×2 MT biextension regulator) has no
known first lemma in the record or the 2026 literature screened on 10-13. Path 1 is the experiment that bears on it.

## 4. Copy-paste prompt (Codex, package review for path 2)

"Review the frozen package `~/BSD_P53_L743_RUN_2026-10-01/FROZEN_RUN_PACKAGE_p53_l743` (local git a766881,
FREEZE_MANIFEST 82a5d962) and its `PREFLIGHT_RETURN.md`. Check: (1) the launcher/adapter against the p83 run's newer
harness in `~/BSD_UNRESOLVED_SEED_PUSH_2026-10-13` (independent exact-rational verifier, monitored run); port that
verifier if missing; (2) T = 262,580,207,615 against tmin for ℓ = 743; (3) prefix custody 0..6444 and the streaming
of 6445..15650; (4) that the sealed prediction 20 is excluded from production and acceptance. Independent check by
Claude 10-14: R(53,743) = 26, a₇₄₃ = −32, 288·(a−2)·R ≡ 20 (mod 53); R(53,107) ≡ 0. Answer READY / NEEDS_FIX with
exact items. Do not launch. New dated folder; RESUME.md + STATE.json first; no remote jobs."

## Addendum 2026-10-14 19:30Z: path 1 ran

Run at the user's request in this session. **All seven sealed rows pass** (`~/BSD_SEED_FULL_LEVEL_LAW_TEST_2026-10-14/REPORT.md`):
c₂ ≡ 1 mod 25 (ℓ = 101), 9 mod 27 (109), 9 mod 63 (127), 18 mod 81 (163), 0 mod 9 (19, 37, 73). The seed's exact per-level law now
holds beyond depth 1 and at the Ш-prime 3 in every tested row. Endpoint effect none. Remaining paths 2–4 unchanged.
