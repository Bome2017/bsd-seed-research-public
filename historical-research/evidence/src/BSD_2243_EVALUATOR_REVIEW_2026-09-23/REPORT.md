# 2243 evaluator review and dependency reconciliation (2026-09-23)

**Scope** (your instruction): review the existing evaluator before any new algorithm or Aristotle package, reconcile D2/D5 against sources already on disk, and list what remains before production.
* Nothing was launched or spent.
* v2.3 was not modified; a fix is proposed, not applied.
* The algebraic compression attempt is queued. 5843 is held.

## 1. Evaluator verdicts

**Codex (independent, different model; `~/BSD_2243_ACC_CODEX_CHECK_2026-09-23/REVIEW.md`): FAIL for the claimed crash/restart isolation of v2.3.** The arithmetic core passes.

**Arithmetic, passing:**
* A fresh m = 27 replay from its own build gives CHUNK_DIGEST `e24f3f4d…` exactly, the 288-segment root matches, and all 18 + 18 symbols are recovered on both merge paths.
* An m = 81 merge of existing checkpoints recovers all 54 + 54 symbols. A_EXACT = 15 851 520 = 1024·15480, and the unit test correctly fails mod 3.
* Five negative controls fail closed.
* The fixed-point tally is an ℓ1 bound, so adding 2E once per symbol is valid. The DFT signs, `div_period` and the integer ranges at the production T and m were all verified.

**The defect** (`acc2243v2.c:431-435`, `:329`).
* The generation number comes from checkpoint files only.
* A run that dies before its first checkpoint lets the restart reuse the same generation and the same stream directories as the dead run's still-running children. Codex reproduced this.
* It stays fail-closed: the consumed-bytes hash equals the verifier's hash, and no false result was shown. But the isolation claim fails and work is lost.
* Proposed fix: `FIX_PROPOSAL_GENERATION_RESERVATION.md`, a durable generation reservation made before spawning, plus per-process scratch names and early-crash tests.

**Codex notes accepted:**
* My "verbatim except read_apseg" claim was too strong. `gen_block`, `invmod` and the `run_L` recurrence differ textually but preserve the mathematics.
* The S1c period label should read ω₁ as the plus period, with 2ω₁ as the total real period. The factor 2 is a unit at 2243.
* The pre-produced a_q corpus is a trust boundary: it must be pinned and immutable.

**Second, fresh-context reviewer** (`independent_review/`): still running (an m = 81 full replay). Same model family, so less independent than Codex. Its verdict is reported when it completes.

## 2. D2 and D5 (`dependencies/D2_D5_RECONCILIATION.md`)

**D2: discharged at source level.**
* Skinner 2016 §3.2 gives Ch_L(f) = (γ − 1)·Ch_L(f)′ in the split case, using only the hypotheses of Proposition 2.3.2; the ℒ ≠ 0 hypothesis is not needed for this step.
* The Selmer-object matching is written out: at p, strict = Kummer via the Tate uniformization; at ℓ ≠ p, unramified = trivial over Q∞. So Skinner's S is the classical Selmer group of SW 6.1.
* Codex's derivation agrees independently.

**D5: necessary at the retained grade, unless the grade is changed explicitly.**
* **SW Theorem 6.1** states "order = r ⟺ height nondegenerate and Sha(p) finite", crediting the multiplicative case to Jones 1989.
* **Jones 1989, read in full:**
  * it assumes Sha finite as standing Hypothesis 1, used in the very definition of the height;
  * its Theorem 3.1 gives only "nondegenerate ⟹ ρ = r + 1 + formula";
  * its Theorem 2.1 iff leaves the α quasi-isomorphism conditional on nondegeneracy (Lemma 2.2).
* **The converse is not in the cited source.** The same SW paragraph also credits multiplicative torsion to Kato 17.4, which Skinner states excludes p | N.
* **The retained 3-primary theorem**, also at a multiplicative prime, used an independent height certificate.
* **Codex frames D5 as a grade choice:** SW "as published" makes it redundant; Jones-forward-only requires it. It did not read Jones. The finding above is what that choice should weigh.
* **Cheapest discharge:** an independent split-height computation (a second code path; hours of work, seconds of CPU).

## 3. What remains before production (`REMAINING_BEFORE_PRODUCTION.md`)

Beyond D5, the Codex defect fix, its re-review, and the verdicts above:
* **Linux/cloud validation:** not exercised.
* **Checkpoint volume control:** not implemented. At fleet scale this is ≈ 103 GB per restart generation uncompacted; the S4 storage line was understated (erratum appended).
* **Checkpoint persistence across spot interruptions:** not designed. The pilot launcher deletes the volume on termination; the spot scenarios silently assumed persistence.
* **Fleet orchestration:** not implemented.
* **Pre-produced segment distribution** and an **independent re-merge**.

The cost figures are modeled scenarios, not quotes. The R5 test validated machinery on 47 units, not the coefficient range.

## Master-record check

`verify_master.py` returns RECONCILIATION_REQUIRED:
* the p = 13 run's bound files changed;
* new BSD_2243 folders;
* the root set changed.

It was not reconciled here; that needs your authorization and belongs to the master's maintenance procedure.

## Addendum (08:30): the second reviewer has returned

**Fresh-context reviewer** (`independent_review/REVIEW.md`; same model family as the author; did not write the engine): **PASS_WITH_CORRECTIONS.**

**Replays:**
* a fresh m = 27 run gives digest `e24f3f4d…`, with 18 + 18 symbols exact on both paths;
* **a fresh full m = 81 run** gives digest `04a7d952…`, identical to the author's, with 54 + 54 symbols exact, A_EXACT = 15 851 520, and UNIT_TEST FAIL as required;
* 1.56 CPU-h in total.

**Major finding F4:** the same stream-directory generation reuse after a crash before the first checkpoint that Codex found. Codex grades it FAIL, this reviewer grades it major; the disagreement is about grade only.

**Minor findings:**
* **F1:** Part L is not verbatim versus arbcore; there are five differences, all valid.
* **F2:** the fingerprint sees only the low 64 bits of each class sum, so a self-consistent corrupted checkpoint with a recomputed SHA passes.
* **F5:** the stream command's curve, T and QB are not bound to PARAMS.
* **F6:** the setup table (a_p for p ≤ √T) is not hash-bound in checkpoints.
* **F7:** the weight arguments are not validated.
* **F8:** `read_ckpt` leaves its struct uninitialized when `fopen` fails.

**Notes:**
* **F3:** lattice identification cannot detect bad input. An arbitrary value is "identified" with probability ≈ 99%. Test A3c shifted every plus symbol by +1 and all checks passed.
* **F9–F13:** overflow guards heuristic but a priori safe; S-leaf hashes unused; no directory fsync; the MAXCK limit; companions optional for pre-produced segments.

**Required before production** (both reviewers): the F4 fix, then F5–F8 and the F1 documentation. Recommended: a full-width fingerprint (F2), a lattice-residue statistic or replicated digests (F3), and SMOOTH_MERKLE again (F10).
