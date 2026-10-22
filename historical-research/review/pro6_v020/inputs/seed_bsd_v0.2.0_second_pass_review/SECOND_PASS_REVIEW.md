# Second-pass review — BSD seed release v0.2.0-private-review

Date: 23 September 2026.

## Verdict

The principal first-pass **omission and evidence-access objections have been materially addressed**. The revised package is suitable for targeted private expert review after the specific bibliography correction below. This is not a complete independent certification of the large numerical calculations or all arithmetic/geometric imports, and not an endorsement of a proof of full BSD.

The first review's major-revision recommendation should not simply be repeated as if the new appendices and evidence were absent. The numerical Manin-bound composition, the added A3 algebra, the repaired verifier predicate and preservation argument, and the C13 custody explanation can now actually be examined.

No counterexample to the retained rank-two statement or the conditional A3 implication was found in this pass. No new prime, finiteness-of-Sha result, total order, or real leading-term equality is established by this release audit.

## 1. Exact object reviewed

Repository: Bome2017/bsd-seed-research, accessed with the authorized GitHub connector.

- Tag: `v0.2.0-private-review`
- Annotated tag object: `4ae2bc15f7fcbc8f28b2ee95f1668845d5d3f67d`
- Tagged commit: `e8af0b76db3cec7c2610355babc4da25c8396be1`
- Git tree: `f008308751e76c052b248ff9672aa7bb976e4a94`
- Uploaded ZIP SHA-256: `c52c77c569bfdc63ad774e58056dd0fa57c831af99e75241d72072c2b9124052`
- Revised PDF SHA-256: `5f3455927c0099fac1edafb35d67a215ee43d1c77266754a5e045642081efcf8`
- Revised PDF: **32 pages**, not the 25-page PDF from the first review.

I reconstructed the Git tree from every ZIP file and its executable mode. It equals the GitHub commit tree exactly. This is stronger than checking a few filenames. The final commit, rather than the pre-stamp source parent in `SOURCE_SNAPSHOT.json`, identifies the reviewed artifact.

The snapshot has 3,473 files. All 3,472 root-manifest entries pass; the root manifest does not hash itself. All 3,365 evidence-file hashes, 207 evidence bindings, and 76 claim entries pass the supplied portable checks. The review runs caused zero changes, additions or deletions in the extracted input tree.

## 2. Checks performed and limits

### Executed

- `python -B tools/verify_release.py`: **18/18 PASS**, without `--record` or `--lean`.
- Three supplied negative controls: edited specification rejected; dependency self-cycle rejected; a no-op D5 verifier rejected even when an old PASS file exists.
- D5 certificate and separate verifier run in fresh temporary copies by the release checker; determinant residue 2181 and valuation two reproduced.
- Fresh Linux compilation of both the original and repaired coefficient verifier, preserving their C source. A compatibility header maps only CommonCrypto SHA-256 functions to OpenSSL.
- Each verifier was exercised on the malicious q=4099 record and an independently found genuine record, both with and without undefined-behavior sanitization. Eight compiled cases behaved as expected: old code accepts the false trace 68; repaired code rejects it with exit 3 and the duplicate-factor message; genuine trace 86 is accepted by both. No sanitizer error occurred in these small executions.
- Read the revised main paper and mathematical appendices, original retained Manin derivation, A3 signature/source boundaries, repaired predicate, receipt-join code, response to the first review, and custody reconciliation. Rendered the revised PDF and inspected key proof pages for notation and layout.
- Selected external primary-source checks: CNS 1911.09446v3; BLV 2306.17784v2; the two distinct Agashe–Ribet–Stein papers.

### Not executed or established

- No new billion-record elliptic-curve/primality verification or full coefficient-corpus scan.
- No fresh large L-series, modular-symbol, or original real-height production.
- No fresh eclib global saturation run.
- No Lean rebuild: `lean` and `lake` are absent from this runtime. I inspected the supplied signature/source and recorded scope; the pinned previous build is not a build performed by this reviewer.
- No formal verification that the C implementation matches the mathematical predicate on all well-formed inputs.
- No independent reconstruction of all Katz–Mazur geometry or every arithmetic input inside BLV and its dependencies.

These limits should accompany the review, rather than being hidden behind “all checks passed.”

## 3. Manin-bound and symbol-lattice repair

Printed Appendix D (source file `paper/sections/F_lattice_proof.tex`) now specifies the optimal quotient and the actual parametrization of the seed. In particular it excludes arbitrary further multiplication maps, and accounts for the possible degree-two isogeny through `c_psi | 2`.

The proof separates the integral-lattice inequality from its geometric estimate. With e' the exponent needed to put the infinity-integral cuspform lattice S inside the dualizing lattice H, and kappa describing the projected differential lattice, it obtains

    v_2(deg phi_0) >= v_2(c_0) + kappa,
    v_2(deg phi_0) <= e' + kappa.

Hence `v_2(c_0) <= e'`. This is a meaningful displayed argument, not merely “apply Pasten.”

For the rigidified level-eight model, the stated component, genus and incidence facts yield

    K*mu/12 <= 2*mu - 4*c' - 3*(mu/6 - c' + mu/4)
              = 3*mu/4 - c',
    K <= 9 - 12*c'/mu < 9.

Thus the integral pole order is at most eight. The sign of the vertical divisor and the possibility of a positive vertical zero at the infinity component are accounted for. I rederived these inequalities and found no algebraic error **conditional on the stated geometric inputs**.

The final implication is now explicit:

    c_0 | 2^8 -> c_E | 2^9 -> symbols lie in (1/1024) Z.

The last step uses the specified rational unitary cusps, torsion exponent two, and the rectangular period lattice. It does not claim every cusp is rational or assert the lattice from numerical rounding.

The remaining expert-review target is the application of the integral model facts to this precise rigidified model: regularity, four multiplicity-one geometric components, their genus and mutual-incidence bounds, and the differential descent. CNS's generic-etaleness and component formulas are relevant primary inputs; an arithmetic test of the curve is not a proof of these geometric statements. This is a now-visible mathematical review task, not a missing appendix.

### Required correction: two ARS papers have been conflated

Appendix D.1, printed p.25, cites **[1, Corollary 3.7]** for the odd-prime support of the Manin constant. Reference [1], bib key `ars`, is **The modular degree, congruence primes, and multiplicity one** (2012).

The required support corollary is Corollary 3.7 of **The Manin Constant** (Agashe–Ribet–Stein, 2006). In the 2012 paper, 3.7 is a remark about modular degree and congruence number. The 2012 Theorem 3.6(a), used later in Appendix D.2, is the appropriate modular-exponent input.

Use separate bibliography keys and retain both papers. Do not globally replace the existing ARS reference and thereby break the correct later citation. The true support theorem was checked in the authors' primary source, so this is a repairable citation binding error, not a counterexample to the bound.

## 4. A3 repair

Printed Appendix E (source `G_bridge_proof.tex`) now supplies the actual chain:

1. exact specialization lengths remove a possible finite Z_p-torsion submodule;
2. an equivariant arithmetic presentation and a sign-twisted canonical resolution give equal conjugation eigenspace ranks;
3. at residual order two, the surjection from the plus eigenspace onto Z_p^2 has zero kernel, so the seed Sha-dual vanishes.

I found no algebraic error in this deduction from I1–I4 and the stated structural facts. The corrected use of `d = ord_T(F mod p)` is preserved. Conventional finite Iwasawa lambda alone is not substituted for `mu=0`.

The important arithmetic input is still I3: after base change, the kernel and cokernel must have equal **individual** plus/minus dimensions. Equal total dimensions alone would not suffice. The new proof explicitly identifies this arithmetic comparison instead of asking Lean to supply it invisibly. The complete capstone signature and the `harith` hypothesis make the boundary inspectable.

Source checks confirm the relevant BLV v2 numbering: discrete control is Proposition 5.9, compact injectivity Proposition 5.10, and global freeness Proposition 5.13. Corollary 5.14 is printed for n>=1; the n=0 extension in the package is a separate argument using 5.10 and 5.13, not a verbatim quotation from 5.14. Exact lengths use Theorem 7.1's non-exceptional equality, not merely characteristic divisibility.

This addresses the outline-only objection. It does not mean this review formally proves the Selmer-theoretic instantiation or independently validates every theorem imported by BLV. Asking an expert to inspect those now-explicit comparisons is appropriate; insisting that every published dependency be reproved would be a different and unreasonable review standard.

## 5. Verifier rehabilitation

Printed Appendix F now provides the missing mathematical predicate. If n is the order of the witnessed point and n divides h, the test

    [ h / ell^(v_ell(h)-e+1) ] P != O

forces `v_ell(n) >= e`. Distinct prime factors then make `D = product ell^e` divide n and hence the actual group order. The Hasse interval and the unique-multiple test identify that order and the trace.

This directly explains why repeated factors invalidated the old checker. The revised proof also states the right preservation claim: on well-formed retained-range records whose old tests passed, distinctness and safe product bounds imply acceptance by the repaired predicate. It does not assert equivalence for arbitrary malformed or overflowing inputs.

The receipt join ties all 3,757 scanned witness files to their retained acceptance and witness-hash records. My portable replay confirms the join's arithmetic and byte identities. The compiled regression confirms the old bug and the patch's effect on the decisive example. These resolve the previously missing explanation at the declared computational trust grade.

They are not a fresh validation of the truth of every old acceptance receipt or a billion-record group-calculation replay. The package now says this accurately. The original receipts and their association with historical input bytes remain execution evidence. The original C group arithmetic, compiler, and hardware remain trusted unless separately verified.

## 6. C13 custody

The old blanket assurance has been replaced by a specific argument.

- Changed metadata: RESULT.json, STATE.json, RESUME.md.
- Nine separately bound calculation inputs remain intact, including the denominator-13 and denominator-169 symbol tables and their Arb outputs.
- The current downstream replay reads the intact symbol tables, not those three changed metadata files, and returns the expected residues.
- The original STATE.json status content is not recovered, so an unchanged entire execution history is explicitly not claimed.

The portable check reproduces these nine matches and three mismatches. This addresses the earlier objection to the unexplained claim that the custody problem did not matter. It supports retention of the numerical theorem at its stated input/receipt trust grade; it does not independently re-evaluate the original series.

## 7. Other revision dispositions

Confirmed in the revised manuscript/source:

- explicit (m,n)=(2243,12) rank-family specialization and a separate saturation claim;
- more explicit residual-image argument, including the alternate transvection prime at residual prime 2243;
- Arb described as controlling floating-point rounding, rather than avoiding floating point;
- 54 residues at denominator 81 plus 18 at denominator 27, rather than 72 residues at 81;
- p=5 handled separately in the anomalous-prime argument;
- full real period and least positive real period distinguished;
- evaluator reliability moved out of the mathematical antecedents;
- cofinite primary vanishing plus separate finite exceptions recognized as sufficient for FIN;
- historical statements without self-contained definitions demoted to research records, not used as main-result proofs;
- no claim that the elementary trace counterexample alone disproves a named paper under unstated assumptions;
- no promotion of the missing D=-23 twist 13-primary input;
- M2 remains a sufficient, prime-dependent witness, not a necessary BSD condition;
- no uniform nonvanishing or full BSD endpoint claimed.

The exact prime-isogeny classification and integral-lifting results in the residual-image proof would benefit from complete primary bibliographic references rather than only named imports. This is secondary to the concrete ARS collision above.

## 8. Recommendation

Make the two-ARS bibliography correction in a new tagged patch release; preserve v0.2.0 unchanged. Then send the dossier for targeted private expert review, especially its integral-model application and equivariant Selmer comparison. A private GitHub URL alone does not give an outside referee access.

The first review's principal presentation/evidence-access complaints should be marked repaired or specifically narrowed, not repeatedly rediscovered from the old PDF. At the same time the 18 portable checks must not be presented as an end-to-end proof of all numerical and arithmetic claims.

Readiness to seek expert review is not an expert endorsement of correctness, novelty, suitability for large compute allocation, or proximity to full BSD.

## Primary source locations checked

- CNS: https://arxiv.org/html/1911.09446v3 (notably 5.8–5.10, 5.15, 6.2 and 6.12(c)).
- BLV: https://arxiv.org/html/2306.17784v2 (5.3, 5.9–5.16, 7.1 and 7.3).
- ARS Manin support: https://wstein.org/papers/ars-manin/html/node6.html (Corollary 3.7).
- ARS modular degree: https://www.math.fsu.edu/~agashe/math/moddeg3.pdf (Theorem 3.6(a), Remark 3.7).

## Files accompanying this review

- `results/snapshot_check.json`: full ZIP/manifest/Git-tree identity.
- `results/portable_checks.log`: actual 18-check run.
- `results/negative_controls.json`: three rejection controls.
- `results/c_verifier_linux.json`: compiled C regression results and source hashes.
- `results/no_input_changes.json`: post-review input immutability.
- `checks/verify_snapshot.py`: standalone ZIP/tree identity checker.
- `checks/check_c_verifier_linux.py`: repeat the bounded Linux C regression against an extracted release; requires clang and OpenSSL headers/libraries.
