# v0.2.5 candidate row: Theorem W (auxiliary independence of the tame scalar), DRAFT ONLY

This is a proposed addition to `~/BSD_RECORD_RECONCILIATION_CODEX_2026-09-29/V025_CLAIM_UPDATE_DRAFT.md`, under "New theorem
entries". It has not been applied to any release repository. No claim generator was run and nothing was pushed.

**Theorem W (fixed-p auxiliary independence).**
Let p ∉ B* = {2, 3, 19, 59, 487, 2243, 4547, 5843}. Let l ≠ q be primes with:
- gcd(lq, pN) = 1;
- l ≡ q ≡ 1 (mod p);
- p ∤ #E(F_l)·#E(F_q);
- both production tame regulators R_(p,l) and R_(p,q) nonzero mod p.

Use one period, one saturated Mordell–Weil basis, and matching discrete-log and group-ring generators. Then

    C2(p,l) / ((a_l − 2)·R_(p,l)) = C2(p,q) / ((a_q − 2)·R_(p,q))   in F_p.

If Sha(E/Q)[p] ≠ 0, both sides are 0.

**Grade.** A written deduction at retained/imported-input grade. Codex returned CONFIRMED_WITH_CORRECTIONS on 09-29 and
supplied a repaired proof in `A_REPAIR.md`. It is not kernel-formalized and not human-refereed.

**Imports.**
- Ota v1, Thms 6.1 and 6.4.
- BKS II: the §§5.2–5.3 Selmer complexes, Kataoka's Lemma 4.2, and Cor 5.3.
- The p-primary Prop 5.4, proved in A_REPAIR §1. BKS's printed full-Sha hypothesis is NOT used.
- Burns–Macias Castillo Th. 10.3.
- Darmon's regularization (§2.3.1), with the degree-two agreement (A3).
- The retained odd residual surjectivity (G2 §1).
- Lemma A1: no good p ≥ 7 is anomalous.

**Qualifications.**
- This is fixed p only. It gives no relation across primes, no nonvanishing and no value: 288 is not derived.
- At p = 5 it only compares eligible pairs; G2's infinitude theorem excludes 5. It says nothing at 19, 59 or 487.
- A mismatched generator scales the ratio by a square, and that square can be −1. A period change scales every ratio
  by one constant.
- Rows that cite the K288 scalar may write w_p for p ∉ B* and may treat "some auxiliary" and "every auxiliary" as
  equivalent there.

**Evidence custody.**
- The Fable return: `~/BSD_W_ELL_INDEPENDENCE_RETURN_FABLE_2026-09-29/`, MANIFEST 15/15.
- The Codex audit: `~/BSD_UNIFORMITY_ATTEMPTS_CHECK_CODEX_2026-09-29/`, MANIFEST 23/23. INPUT_BINDINGS.json binds 32
  inputs.
- The 389a1 checks at p = 7 are calibration only, not seed certificates.

**Unchanged:** O.1–O.4. FIN, ORDER9 and Q36 are unchanged.
