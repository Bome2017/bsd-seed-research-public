# Claude class-lift continuation: independent reconciliation

2026-10-15. Originals read-only. Grade: fresh exact witness, finite-field and rational Hensel replay; retained complete BNF certification and Schaefer–Stoll source theorem. No new BNF certification, prime coverage, or seed bound.

The reliable delta is **five additional rank-two controls, eight total**, all in the same repairable-class configuration. The five are 1141a1, 1246c1, 1480a1, 1525c1, and 1613a1. There is no computed unrepairable class in these controls. This is additional experimental coverage, not a new exclusion theorem.

## Reproduced arithmetic

- All 530 continuation-manifest entries match. All 257 original-at-copy entries still match the original Codex directory. The copied directory changes only RESUME.md and STATE.json among those 257 entries, consistently with continuation.
- Reconstructed the next-24 candidate selection from the original Cremona list: 3 initial certified positives, 19 provisional class-3-zero screens, and 2 timeouts later certified. The provisional screens remain conditional; they cannot support nonexistence or any upper bound.
- Replayed the five exact identity checks: scalar-action cube identities, all rational point cube identities, full ordinary-class ideal identities, and class coordinates reproduce their saved stdout byte-for-byte.
- Replayed all five rational Hensel checks and transvection computations byte-for-byte. Minimum cubeclass precision margins are respectively 41, 41, 44, 89, and 86.
- Independently enumerated all 243 elements of each valuation-zero source and all 81 ordinary-unit combinations. For every curve, the joint accepted set is exactly the 9-element rational-point span; its unit intersection has 3 elements and its ordinary-class image has 3 elements. The full source joint kernel has dimension two as well. This validates the displayed source/class coupling without relying on the printed rank profiles.
- Fresh GP witness checks independently verify that the actual supplied global units have trivial ideal, the rejected antiunit has scalar norm one, the admitted unit is a rational-point combination times a literal cube, and the repaired class lift is a rational-point combination times a literal cube.
- At the reported split primes 73, 1609, 13, 229, and 1171, the fresh checker verifies all eight field roots, their actual nonzero 3-torsion points, the element evaluations, the zero-sum triple, and its noncube residue product. This is genuine arithmetic rejection of the selected antiunit, not synthetic matrix data.

The containing-kernel upper bound plus the independently evaluated two point classes gives the rank-two/Selmer conclusion under the retained complete-source and local-image inputs. Finite split-prime rows remain necessary global tests, not a general replacement for the full additivity condition. Equality of the containing kernel with the point plane suffices in these particular cases.

## Corrections needed in the Claude report

1. **Counts:** the title's “six more,” §4's “all nine,” §5's “9 (3+6),” and STATE.json's “all nine” are incorrect. The actual table has five new and eight total rows. The 48-candidate scan count is correct.
2. **1525 matrix review did not pass:** `review/1525c1_matrix_review.json` is empty, its stderr records AssertionError, and RUN_LOG records `matrix_review rc=1`. The third point is rational 2-torsion with zero mod-3 column. Claude fixed the witness script, but not the separate matrix reviewer. Our new exhaustive checker handles the zero column correctly and closes this check: the first two point columns span the entire joint kernel. The actual class repair identity also passes the fresh GP check. This is a repaired acceptance error, not a contradiction in the arithmetic.
3. **Acceptance runner is not fail-closed:** `run_curve.sh` logs failures and continues; GP can itself continue after an error. A completion marker alone does not establish successful arithmetic. Our checked replays inspect exit status and stderr; actual accepted identity/witness outputs are clean apart from stack warnings. The original failed 1525 trial remains evidence, not a passing check.
4. **Scope of the suggested obstruction:** “an unrepairable class would need both point directions to be unit-supported” is justified only in the one-dimensional relevant class-quotient setting being tested, assuming the two point classes are valuation-zero. For a larger class quotient, some class directions may be rejected while another is occupied by points. It is not a general theorem about all possible controls or the seed.
5. **Saved mirror calculation was missed:** both copies already contain `search/mirror389/` in the original 257-file manifest. Codex had certified Cl=C3, anti-class dimension one, and Cl_S=C3 for the -3 twist of 389a1 before interruption. Its minimal model is [0,0,1,-21,-27], conductor 3501; the saved rank cross-check is zero. No coupling analysis was completed there. Thus a literal claim that no dual/mirror class group had been computed is too broad. This is a saved changed-rank experiment, not an additional rank-two row.
6. **Resource accounting:** initial scan limits stayed at 90 s/1 GB with 100 s outer timeout. The two retries raised the alarm to 600 s. The final 1613 certification used a separate saved-BNF script with 2 GB and no internal alarm; it returned 1 after 1295.558 s. These are retained certification receipts, not freshly rerun certifications. The report partly discloses them, but should not imply every accepted field was certified within the initial bound.

## Exact experimental frontier

All five new rows have trivial S-class group. Their ordinary C3 classes occur as valuation-zero S-unit combinations; all are repairable into the point plane. Therefore they do not test a genuinely nontrivial Cl_S lift, and do not produce a nonzero class-to-local-defect map or order-nine ray lift. Repeating this configuration does not establish that an unrepairable branch is impossible.

The saved mirror389 source is a different, already certified arithmetic input: Cl_S=C3 rather than trivial. It can test the unfinished source branch without rerunning its BNF. Any continuation must keep its changed rank explicit and must compute the actual class defect after allowing every legitimate unit repair. Nothing in the present audit forecasts the result.

FIN, ORDER9 and Q36 are unchanged.

## Audit artifacts

`audit.py` and `audit_results.json`: custody, candidate selection, original checker replays (including the faithfully reproduced 1525 failure).

`exhaustive_matrix_check.py` and `exhaustive_matrix_results.json`: fresh exhaustive source/unit/point/coupling checks, including the repaired 1525 check.

`check_witness_template.gp`, `witness_replay.py`, `witness_results.json`, and per-curve outputs: fresh exact arithmetic witness checks. All original inputs remain unchanged.
