# Check of the v0.2.6 scope and the uniform/Q36 briefs

**Overall: CONFIRMED_WITH_CORRECTIONS.** B.20–B.22 survive at the already accepted retained/imported-theorem grade. The proposed briefs contain repairable wording and task-design errors; the most concrete mathematical defect is the missing irreducibility condition in the Q36 algebraicity criterion.

Date: 2026-09-30. This is a bounded comparison against the accepted review and pinned release, not another full theorem-source or numerical-certificate audit. Exact replacements are in `REPLACEMENTS.md` and machine-readable `REPLACEMENTS.json`; complete corrected copies are in `corrected/`. The originals, release, maps and previously delivered Pro package were not changed.

## Identity and state

- v0.2.6 task manifest: **13/13** passed.
- Local release HEAD: **4344c6a85e6940d6477807ef5d8dda761134bc2e**, clean at inspection.
- Fresh read-only GitHub query: `refs/heads/v0.2.5` is that same commit; `refs/heads/main` is **2a726213a27a12f10fece5bc70137e65e30911ba**. The statement that the v0.2.5 branch is pushed is correct. No merge to main is inferred.
- Pro's independent synthesis review and Codex's return check are completed records. Do not queue another identical review.
- Exact release statements and their qualifications are preserved in `RELEASE_CLAIMS_EXACT.json`; hashes of the read inputs are in `INPUT_BINDINGS.json`.

**Concurrent update reconciled:** during this review the coordinator revised `V026_SCOPE.md` and `TASK.md`, adding the CLW version caveat, the separate ordinary-prime explanation, and correcting the unproved converse. The initial live-input hash check detected the changes and stopped; they were then captured separately in `reconciled_inputs/`. The final corrected copies preserve these additions. The initial equivalence finding below is therefore already fixed in that newer live scope. The remaining suggested changes still apply. Exact tiny counts confirm the added traces a_19=4, a_59=-4, a_487=-28. A live check of the [arXiv submission history](https://arxiv.org/abs/2608.29470) confirms only v1 is listed, so the author-revision caveat is warranted.

## A. v0.2.6 bank scope — CONFIRMED_WITH_CORRECTIONS

**Accepted mathematics:** B.20 is M_infinity=0 and existence of a mod-p unit witness at every good p>=5, including supersingular primes and 19,59,487. B.21 identifies the *minimum unit* length with dim Sel_p, gives even parity and the equivalence with primary vanishing at length two. B.22 is the sufficient strict-depth-<4 test for the full BH-normalized element of a real degree-p cyclic extension at its actual conductor prime to pN. No prior finite Sha is assumed. None proves the uniform bound.

**Required corrections before banking:**

1. Remove “equivalently in effect” between the character test and the other criteria. B.21 makes two-prime unit existence, dim Sel_p<=3, and primary vanishing equivalent. B.22 supplies only a sufficient character test; its converse was not established.
2. Call Z_p²⊕(Z/p)² an abstract **compact dual module**, not Sel_p. Its Fitting pattern is compatible with M_infinity=0. It is not an asserted seed example and does not literally instantiate every arithmetic hypothesis of B.20.
3. Use the existing release grades **PROVED_WRITTEN + IMPORTED_PREPRINT**. `DERIVED` is useful prose but is not a grade accepted by `claims/spec/common.py`. B.22 has kind CONDITIONAL, since its witness is not supplied.
4. Make the negative controls semantic. “Every good p>=5” is correct even if it does not separately spell out 19,59,487. A conditional implication to FIN or a stated open target is not a false assertion that FIN has been proved. Add controls for changing unit to merely nonzero, silently changing the actual conductor, and adding an unproved converse.
5. Resolve the placement conflict: retain the exact model-review label in verification/evidence records; use mathematical grades and source citations in the paper and README as the task's public-text rule requires.

**Review label:** its author/reviewer-family distinction and nonhuman/nonformal caveats agree with the reported history. The source and Part B checks are documented in Claude's supplied addenda. This check did not independently replay the Fable Δ-bridge audit or count independent retrieval sessions from their raw logs. Bind those particular records if repeating those precise additional attributions in the release. Repeated downloads establish source-byte identity, not multiple independent proofs.

The CLW watch item can be resolved only as an applicability/version issue. The upper-bound item stays open. No further mathematical delay is needed to bank the accepted statements once these editorial/schema corrections and the normal release checks are applied.

## B. Uniform-step brief — CONFIRMED_WITH_CORRECTIONS

The intended three alternatives are sufficient, with S explicitly enlarged to contain {2,3,2243,4547,5843}. The corrected text distinguishes the implication directions and defines the two distinct Kato primes and their total-real-period symbol convention. These trace-+2 auxiliaries are not the trace-minus-2 G2 auxiliaries.

The inherited parts need cleanup:

- Restore good p>=5 and **actual conductor** in B.22.
- The nonzero-rational-scalar route must exclude denominator primes as well as numerator primes and every finite exception in the proved identity.
- The level-p^k arithmetic compatibility is explicitly unaudited and must not appear as a proved input to the proposed next step.
- A supplied unit-witness length need not be the minimum r_p. A merely nonzero p-adic witness is not the unit witness used in the bound.
- S.17-47 records one certificate auxiliary for each listed prime. Do not claim several audited auxiliaries for every prime without citing additional records.
- The production tame pairing is half the canonical biextension pairing, up to the shared sign; G2_PROOF.md §4.2 supplies the factor. The corrected brief keeps that distinction.
- Remove the inherited universal claims about all rank-two rationality/nondegeneracy results and per-prime constructions being inherently inadequate. Replace them by the specific failed hypotheses and missing maps in the screened records. In the first-derivative product argument the other factor must be holomorphic; it is not an exclusion of all auxiliary-cycle approaches.

The corrected brief is suitable as background. The **already delivered bounded Pro package remains valid unchanged** and should govern that attempt. Substituting this broader brief for its mechanism gate would undo the effort to avoid another general survey.

## C. Q36 brief — CONFIRMED_WITH_CORRECTIONS

R.2–R.7's quoted numbers agree with the pinned release; they are summaries, not verbatim full claims. Q.4 agrees with the retained Mellin proof, with the logarithm branch made explicit. No numerical replay was performed.

**Q.1 is correct.** The exact epsilon=573/100000 satisfies epsilon<1/174, while 1/175<epsilon.

**Q.2 as transcribed is false without “irreducible”.** The release says *primitive irreducible integer polynomial*. For the exact abstract counterexample q'=36001/1000=36.001, inside the certified interval, take

    P(X) = (X-36)(1000X-36001)
         = 1000X² - 72001X + 1296036.

P is primitive and has q' as a root, but its other root is 36, so the displayed product bound is zero and would falsely certify q'=36. Restoring the minimal/irreducible polynomial excludes this. For an irreducible polynomial, the small product makes the integer P(36) have absolute value below one, hence zero; irreducibility then forces q=36. The exact control is saved in `CHECKS.json`.

**Q.3 is correct, with all its hypotheses.** The primary upper bounds force v_p(B)>=0 for every p, so a positive rational B is an integer. The quotient interval forces B=9. The bounds imply trivial primary groups away from 3 and bound the 3-part by 9; the retained 3-part has order 9. This proves FIN, ORDER9 and Q36 only after those arithmetic hypotheses are independently established, not by defining B=q/4.

**K-D was too strong as an admission rule.** A new proof of q's rationality would be substantive progress even without denominator control. Label it RATIONALITY_ONLY, with Q36 still open. Require the Q.1/Q.2 bound or another exact characterization only when certifying Q36. Likewise a useful intermediate lemma can leave a later comparison open if it states exactly what new input was proved; an unsupported p-adic-to-complex step cannot be used as a proof.

The corrected text also scopes the first-derivative and function-field negatives. Narrowing the real interval alone still does not prove equality, but it is not intrinsically useless if a new independent discreteness bound is supplied.

## Use and next actions

The archive contains corrected copies and exact before/after text for the maintainer to integrate and re-manifest. It does not execute the v0.2.6 bank or authorize a push. Keep the single bounded uniform attempt already selected. A separate Q36 attempt should likewise name a concrete mechanism; three simultaneous copies of the same broad request are not justified by this record check.

FIN, ORDER9 and Q36 are unchanged.
