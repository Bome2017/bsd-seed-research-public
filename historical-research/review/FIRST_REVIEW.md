# First review of the consolidated BSD release

**Date:** 23 September 2026. **Disposition:** corrected research release for further mathematical review. This is not certification of full BSD, independent human review, or a fresh proof audit of every imported theorem.

The original release, original evidence sources and `v0.1-review` archive were preserved. Corrections are in an isolated worktree on `review/codex-first-pass`, based on commit `ce6536bed8f6c20084f610fab92b55c318cf2b32`. The original frozen archive has SHA-256 `ff03e89af78f1342d08cc12406a5ac892c24a35f4c052175dc29399f06a7127d`.

## Conclusion

The release is worth circulating for expert assessment after the remaining privacy/author decisions. It presents a concrete rank-two curve with substantial arithmetic evidence and explicit conditional criteria. It does **not** establish finiteness of Sha, its total order nine, or the real leading-term identity `q = 36`.

This review found a real defect in the common coefficient verifier, recovered important missing proof artifacts, and corrected several claims stronger than their evidence. A supplemental check of the actual retained witness corpus passed. No wrong retained Fourier coefficient was demonstrated, and no retained primary-component result is withdrawn by this review. Their published-theorem and numerical trust dependencies remain explicit.

## Findings and repairs

| Finding | Why it matters | Correction / present grade |
|---|---|---|
| Legacy point-order verifier accepts repeated prime factors | It can certify an incorrect coefficient on this very curve | Exact counterexample, repaired verifier, positive/negative regression, and supplemental check of all retained witness files |
| Full integral basis attributed to a preprint and bounded saturation | Neither item alone proves this particular pair is a full basis | Recovered the global index-bound/saturation record and replayed Sage/eclib; index one verified |
| Independent 3-adic height implementation omitted | The finiteness-first 3-primary proof needs nondegeneracy, not just a PARI comparison | Restored code and precision arguments; replay recovered determinant valuation two |
| Finite Iwasawa lambda confused with nonzero mod-p reduction | Finite lambda alone does not imply mu zero | Statement corrected to finite `ord_T(F mod p)`; Lean core already uses the correct notion |
| Lattice rounding described as detecting wrong powers of two | A wrong assumed lattice can silently identify the wrong value | Removed claim; lattice membership remains a separate theorem obligation |
| Symbol-lattice assertion broader than its rational-cusp argument | Arbitrary cusps need not have rational images | Restricted to the rational unitary cusps used by the retained calculations |
| Split L-invariant and height normalizations abbreviated | Exact logarithm normalization and global denominator contributions matter | Restored exact definitions; retained residues and height determinant unchanged |
| Uniform bound, mass and stopped-route wording overclaimed | Conditional ORDER9 differs from FIN plus ORDER9; enumeration size is not a complexity lower bound | Corrected scopes and retained the distinction between unavailable computation and impossibility |
| Verifier could accept stale generated material / old success output | Hash checking alone did not bind specs to generated text or require a fresh D5 result | Added generator checks, cycle detection, fresh-output check, exact status check and negative controls |
| Private identifiers remained in the redaction script | Masked evidence did not make the Git tree private | Removed identifiers from released code; private configuration now external; old history must not be pushed |
| Bibliography placeholders / wrong metadata | Reviewers need the precise sources actually used | Filled titles from primary records; corrected BD pagination; distinguished BLV v2 from its journal publication |

### Coefficient-verifier counterexample and actual-corpus scope

For the seed at the prime `q = 4099`, exact counting gives `a_q = 86`. The old `check_witness` nevertheless accepts the false claim `a_q = 68` with `x0 = 59`, claimed group order `4032`, six copies of `(2,1)` and two copies of `(3,1)`. The point has order six. Counting repeated factors makes the purported certified divisor `D = 576`, larger than the Hasse-interval width `256`; the old individual tests do not justify that divisor. The counterexample exercises the actual old C program, not just a model of it.

The repair rejects repeated factor primes and checks the multiplication bound **before** multiplying. Both versions also accepted a genuine control witness obtained independently from the exact point count. See `tools/replay/coefficient_verifier_regression.py`, `repairs/wverify_distinct.c` and `replay_logs/coefficient_verifier_regression.txt`.

A read-only supplemental scan covered **3,757 witness files**, **2,693,070,671 records including overlaps**, and **74,359,825,942 bytes**. Every file matched its retained `witsha` binding and every record passed the newly required distinct-factor and safe-product checks. It used at most two scanners, less than 64 MiB per file and approximately 393 seconds.

This is **not** a fresh replay of billions of elliptic-curve operations or primality tests. The retained arithmetic checks supply those premises; the new scan checks the omitted conditions against the same bound bytes. It closes this demonstrated verifier defect for the retained corpus at that combined trust grade, not every conceivable defect in its implementation. The repaired verifier has not been installed into original sealed engines. Future use of that engine must incorporate the repair. The raw witness corpus is not redistributed; the scan logs and rerun program are included.

### Recovered full-basis evidence

Zywina's cited result establishes rank two in the family and the relevant mod-two generation, not by itself the full integral basis used in the regulator. A saturation check through 50 alone would not fill that gap.

The older `BSD_SEED_2243_12_FULL_BSD_LANE3_2026-09-18/B_invariants/` does fill it: eclib computes a **global index bound two**, proves two-saturation, and returns index one. A fresh replay of `scripts/s04a_sage.sage` succeeded. Its returned generators are `P2` and `G = (5843,210348)`; exact arithmetic gives `G = -P1 - P2 + T`, an integral basis change of determinant one. The separate Silverman/ratpoints/Hermite certificate and its repaired enumeration/audits were also restored, but that second large enumeration was not rerun.

The restored lane-3 material contains 104 files; 102 match its retained manifest, while the manifest itself and a later record are not listed in that manifest. There were no listed-file mismatches. Historical superseded calculations remain labeled as such. The new replay is computer-assisted evidence, not a formalized proof of eclib.

### Recovered 3-adic height evidence

Twelve missing files from the architect's `fable_audits/F1_work/` were restored and matched to the retained manifest. The formal-series implementation was rerun and recovered `v_3(det H) = 2`, the needed nondegeneracy/valuation input.

The script's fixed formal-series constant is controlled only to the precision required for the leading terms. This review does **not** certify every high-order p-adic digit printed by that script. Its PARI comparisons and perturbation checks are corroboration, not a substitute for the precision argument. Skinner's theorem remains an imported published theorem; the failed project reconstruction of its Euler-removal interface is still recorded.

## What was actually replayed

| Operation | Result | Limit |
|---|---|---|
| Standard-library release checks | PASS; final record in `VERIFICATION_RUN.md` | Imported exact symbol values are inputs; this does not reproduce their Arb enclosures |
| Coefficients from retained symbols | `C5=2`, `C7=1`, `C11=8`, `C13=2`; 3-adic coefficient `15480` | Recorded period conventions apply; imported theorem implications are separate |
| D5 generator and fresh verifier | Determinant divided by `2243^2` is `2181 mod 2243`, valuation two | Published height identification remains an import |
| Exact compression rank and Atkin-Lehner checks | PASS | Scope stays the stated finite relation space |
| Legacy/repaired C verifier regression | Old accepts fake and genuine; repair rejects fake and accepts genuine | Demonstrated defect only |
| Supplemental witness-structure/hash scan | PASS on all 3,757 files | No new group-arithmetic/primality replay |
| Global full-basis saturation | PASS, index one | Sage/eclib algorithms and runtime in the trust base |
| Independent 3-adic formal-height calculation | PASS for required valuation two | Higher printed digits are not all certified |
| A3 Lean replay | PASS, log byte-identical to retained `build6.log` | Explicit arithmetic hypotheses and partially formalized modeling steps remain |
| Stale-spec, dependency-cycle, stale-D5-result negative controls | All rejected | Finite controls, not a complete security proof |
| PDF rebuild and rendering | 25 pages, no undefined references/citations or overfull boxes; all pages inspected | Some non-fatal TeX spacing/bookmark diagnostics remain |

Lean used version **4.32.2** and Mathlib commit `905b95818eb32af7874a58b427f50c1711a5e96c`. All printed theorem axioms were within `propext`, `Classical.choice`, `Quot.sound`. The written bridge must distinguish usual Iwasawa lambda from the finite order of a nonzero mod-p series; the checked core does so. No arithmetic black box was converted into a Lean theorem by this replay.

The manuscript and all claim statements were checked for consistency and scope. `REVIEW_COVERAGE.md` gives an entry for each of the 76 claims and does not label statement review as proof replay. Source metadata checks are summarized in `SOURCE_CHECKS.md`.

## Missing material and remaining limits

The corrected package contains **3,360 evidence files**, including the **116 restored files** above; its 76 claims reference 204 evidence items, or 159 distinct files. The restored records address two concrete omissions. This is **not** proof that every historical chat, cloud-only document, compressed packet or older research folder has been found. The original coverage statement remains, with this review added to it. No existing master was rewritten.

The coefficient and witness corpora remain external. Exact table replays are portable, but a recipient without those corpora cannot independently regenerate the large analytic certificates. `data/LARGE_DATA.md` makes that boundary explicit. The 2243 evaluator's separate F4 restart-isolation defect remains open in its original implementation; this review did not authorize or run it. No 2243, 5843, 4547 or new good-prime certificate was computed.

The most load-bearing remaining review needs are: (1) expert checking of the published-theorem applications and normalization interfaces, especially the symbol lattice and multiplicative/anticyclotomic comparisons; (2) a further independent implementation-level audit of the retained numerical pipeline, rather than assuming one repaired bug exhausts it; and (3) the arithmetic witnesses and global leading-term result that the paper explicitly leaves open. The third item requires mathematics, not editorial repair.

## GitHub and privacy

Read-only GitHub checks found no remote configured for this release and no matching release repository. The existing private `aristotle-research-program` repository is a separate application, not a synchronized copy of this package. No repository was created, pushed or published.

The old redaction program contained literal private email-thread identifiers. The corrected current tree and 30 embedded tar archives were checked for those known identifiers: zero occurrences. This was not a complete secrets/privacy audit. Researcher names, paraphrases, local paths and the AI-use history still occur and are documented. The original Git history retains the old script, so **do not push that history**. The history-free reviewed archive is the proposed source for any later private repository.

The author name and rights statement were preserved. A factual AI-assistance statement was added. The remaining choices in `NOTES_FOR_AUTHOR.md` concern sharing and authorship; they do not block this completed local review.

## Exact endpoint effect

This review improves the reliability, completeness and reproducibility of the existing results. It proves no new primary vanishing, FIN, ORDER9 or Q36. The corrected release states that boundary directly. Its value for a mathematician is a testable body of work with visible dependencies, not a claim that enough computing power must finish BSD.
