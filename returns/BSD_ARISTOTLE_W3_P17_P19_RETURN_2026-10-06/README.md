# Aristotle W3 runs on the seed at p = 17, 19 and 31, plus the Heegner ν note: canonical return (2026-10-06)

**What this is.** One archive, 9a3a411e, containing two Aristotle runs on the reviewed W3 source-construction supplement:
- **Run be7a0018.** W3 evaluated on the actual seed at p = 17 and p = 19, with weight-two plus symbols at denominators p², and the Heegner ν note over ℚ(√−23).
  - It is the return behind the p = 17, m = 289 coefficients Pro relayed earlier (ℓ₀..ℓ₄ ≡ 0, 0, 0, 0, 13 mod 17). Those were previously marked unverified because no return had been received.
- **Run 4e7dc730.** A W3 source construction at p = 31, returning `SPECIFIC_OBSTRUCTION`. Λ₂ mod 31 was not produced.

**Results** (every COMPUTED value is floating point, not interval-certified):
- **p = 17.** ℓ₂ ≡ 0, so λ = 4: negative calibration. The normalized 17-adic regulator is 17-divisible, and Ш[17] = 0 was already settled.
- **p = 19.** ℓ₂ ≡ 18, so λ = 2. Through imported theorems this gives Ш[19^∞] = 0, a conditional second certificate at a prime Ota had already settled.
- **Heegner.** Cofinitely, ν_p ≤ 2 ⟺ ν_p = 1 ⟺ Ш[p] = 0, which agrees with the record's closed lane.

**Lean:** `RequestProject/`. It checks finite arithmetic on the computed integer tables, the ν identities and the quadratic-jet forcing lemma. It does not check the analytic computation.

**Files.** Reports (`W3_P17_REPORT.md`, `HEEGNER_NU_NOTE.md`, `W3_SOURCE_REPORT.md`), `ARISTOTLE_SUMMARY.md`, the task files (`TASK.md`, `ADDENDUM.md`, `REVIEW.md`, `SUBMISSION_PROMPT.txt`), and the code and data in `w3_p17/` and `w3_source/`.

**Excluded from this folder:**
- the compiled executables (x86-64 Linux ELF) and `__pycache__`;
- the input supplement's `original/` and `retained/` (the latter is pinned lab commit 2032198);
- Aristotle's README banner.

The unchanged archive is `../archives/9a3a411e-9b4c-4cc2-a3b0-2021519e607c-aristotle.tar.gz`.

**`CLAUDE_CHECK.md`:** integrity, an independent recompile and a claim audit against the record.

**Endpoint effect: none.** The W3 lane is frozen, and p = 17, 19 and 31 are settled. FIN, ORDER9 and Q36 are unchanged.
