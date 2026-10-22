# Pro follow-up, local Lean core, and Batch C: independent audit

2026-09-27. Read-only on the project, original bundles, completed runs and existing Mathlib. All new files are confined to this additive audit folder. No production computation, corpus extension, successor, cloud session, repository change or communication was launched.

## Verdict

**Retain Pro's review, the 37/41 arithmetic results at their retained dependency grade, and the Lean block-determinant core. Correct Batch C's cutoff and budget before authorizing its production run.**

The mathematical work is useful. There is no new FIN, ORDER9 or Q36 conclusion. The Lean result proves a determinant congruence; it does not supply nonvanishing or a prime-uniform bound.

Two concrete planning corrections are needed:

1. The retained quarter-tail rule at auxiliary prime 311 requires an aligned endpoint of **108,129,157,119**, not approximately 104 billion. This is **6,445 total segments, 1,643 new segments** beyond the retained 4,802-segment corpus.
2. The quoted **160 CPU-hours for the extension** is not supported by the recent extension logs it claims to scale from. A transparent model from those logs suggests approximately **42–56 CPU-hours for generation/verification**, plus roughly **29–31 CPU-hours for the three symbol runs**. Treat **about 70–90 CPU-hours overall as a provisional model**, not a measured guarantee or a production cap. A short new-range preflight must measure the complete pipeline before committing the extension.

## 1. Identity, review integrity and replays

Inputs:

| Artifact | SHA-256 | Check |
|---|---|---|
| Pro follow-up ZIP | `d36d8029bc9340a7ca1518df5969bd9021fc6e16defd5e8c022d2980d4972b0a` | 21/21 payload hashes, exact manifest coverage |
| Completed 37/41 ZIP | `9fae7f08465585588dbdf21328a4fd3036495d2fe530fbe93cb77648c5765845` | 28/28, exact coverage |
| Earlier Codex dual-return ZIP | `bd8e0558ba76379c9e139a68c5c6890f5daf062e87b7682907b5b75825777f6b` | 69/69, exact coverage |
| Local `BlockDet.lean` | `d54683318320e09d2834793214b625e6983ff8d63ff1684e7a4a39eb14a60f7b` | Fresh compile and statement audit |

ZIP extraction rejected unsafe paths, duplicate entries and symlinks. The first local manifest-coverage comparison needed a checker repair to normalize leading `./`; the bytes and hashes themselves were correct. That was an audit-script issue, not an input defect.

Pro's exact table checker was replayed on copied inputs. The local Python environments lacked SymPy. Only its three-line symbolic cancellation was replaced with exact sparse integer-polynomial subtraction; the table checks were unchanged. The adaptation is recorded in `checks/pro_replay_adaptation.diff`. All reported outputs agree exactly. Pro's rational tame-pairing program ran unchanged and agrees exactly apart from CPU time.

This corroborates the review's reported checks. It does not convert Pro's arithmetic imports into new proofs or constitute an original Fourier/prime-corpus recomputation.

## 2. Completed numerical results

| Witness | Supplied symbol intervals independently checked | Coefficients `(c0,c1,c2)` | Residue |
|---|---:|---|---:|
| p=41, ell=83 | 164 | `(0,-5904,-83420)` | 15 mod 41 |
| p=37, ell=149 | 296 | `(0,28860,762756)` | 1 mod 37 |

The printed intervals were checked with exact rational arithmetic for the unique point of `(1/1024)Z`. All labels, symmetries, generator changes, parameter strings and available package bindings pass. The point counts are 36 and 92 at 41 and 83, and 28 and 160 at 37 and 149.

For **37**, this audit additionally accessed the complete local freeze: **32/32 frozen files match**, the live engine matches its pinned hash, and the frozen acceptance checker replayed read-only against the original parameters and receipt logs. It returned precisely the recorded `NONZERO` JSON. The root over 3,045 receipts is `7a174afdbc9e6bf961365963b1e6b1624188337958e5ce046f94f9ed5c7df595`. This closes the 24-file availability limit of Pro's small bundle for this run; it does **not** re-verify all underlying prime witnesses or rerun the analytic sum.

Thus the retained Ota/lattice/corpus theorem chain gives `Sha[37^infinity]=0` and `Sha[41^infinity]=0` at its existing grade. The p=41 full local acceptance replay was already performed in the preceding Codex audit; its table was checked again here through Pro's independent implementation.

The tame computations also reproduce:

* `(41,83)`: `H(92E)=[[32,4],[4,34]]`, determinant 6, unscaled regulator residue 19.
* `(37,149)`: `H(80E)=[[33,30],[30,26]]`, determinant 32, unscaled regulator residue 32.

The two candidate-K=288 predictions are consequently 15 and 1. These are separate tame calculations, not independent reconstructions of the analytic symbol tables.

The common-modulus arithmetic is correct: `17*19*23*29*37*41 = 326823997`. The precise statement is that the six normalized residues are consistent with **a putative common integer** congruent to 288 modulo this product. They do not prove that a common integer exists. Claude's adoption note preserves this qualification even though its short message abbreviates it.

## 3. Lean: what is actually proved

The supplied source compiles with Lean **4.28.0**, `--trust=0`, against the existing Mathlib checkout **8f9d9cff6bd728b17a24e163c9402775d9e6a365**. No packages were installed or rebuilt. Fresh compile: exit 0, no warnings, about 26.5 seconds, peak child RSS about 3.17 GiB. The four public theorem axiom lists contain only `propext`, `Classical.choice`, `Quot.sound`.

For a commutative ring R, ideal I, finite block matrix M=`[[A,B],[C,D]]`, and `s=card(n)`:

* If every entry of B and D lies in I, `det(M) in I^s`.
* If C also has entries in I, `det(M)-det(A)det(D) in I^(s+1)`.
* If additionally A is congruent to `diag(d)` modulo I, `det(M)-(product d_i)det(D) in I^(s+1)`.

These are the correct division-free identities, and their proofs do not smuggle in unit pivots. The hypothesis on C is explicit and necessary for the second assertion: `[[0,T],[1,0]]` over `Z[T]`, I=(T), has determinant -T, not an element of I^2.

The fourth theorem proves, for natural p>1 and u coprime to p,

`p^v*u = 0 in Z/(p^k)  iff  k <= v`.

This is correct, even with the theorem's slightly greater generality allowing composite p. The project's interpretation of zero as depth infinity is a separate definition; the file does not define and formalize the entire depth function.

**Important scope:** “degree-s leading term” here means its class modulo I^(s+1), which may be zero. Lean does not prove that the order is exactly s. It also does not formalize the Smith reduction, identify the minor with an arithmetic Bockstein, identify the pivot product with the finite Sha quotient, or prove BKS, Selmer duality or a main conjecture. The README names these boundaries correctly. No blocking flaw was found in the local formalization.

Another Aristotle run to reprove these same core identities would add little. A later formalization of the Smith/base-change/Bockstein translation could close a different verification boundary, but would still not supply the missing arithmetic bound.

## 4. Corrected determinant realization

Pro retains the casewise theorem and the five corrections from the preceding independent audit. This turn rechecked the adoption and elementary core, not the full arithmetic sources again.

Retain the scope excluding `{2,3,5,19,59,487,2243,4547,5843}`, the auxiliary hypotheses, and the Sigma label on the integral Kato coordinate. Write

`s_p=2+corank Sha[p^infinity]`, `A_p=H^2_f(Q,T_pE)_tors`.

The realization says that the quadratic witness is zero if s_p>2; if s_p=2 it is a unit times `x_(Q,Sigma) * |A_p| * det(B)`. The imports remain named arithmetic inputs.

A nonzero singleton witness in this scope forces both primary Sha vanishing and primitivity of that specified determinant element. In particular this applies to the accepted 23,29,37,41 witnesses (and the previously accepted 17 witness). It does not put 19 into the BKS scope and does not give a supersingular main conjecture or a cross-prime rational element.

The blanket assertion “no property of Kato's element could ever control the witnesses” remains withdrawn. The proved boundary concerns the supplied integrality/perfect-complex inputs, not all possible arithmetic relations.

## 5. Batch C: exact cutoffs and resource evidence

I invoked only the pinned engine's inexpensive **tail planner**, not its coefficient producer or symbol evaluator. It computes periods and tail inequalities in milliseconds. This uses the same LATDEN=4096 quarter-tail planning convention as the accepted runs, while final symbol identification remains on the 1/1024 lattice.

| p | ell | Sealed prediction | Exact planner TMIN | Aligned endpoint T | Total segments | New segments |
|---|---:|---:|---:|---:|---:|---:|
| 31 | 311 | 3 | 108112514659 | **108129157119** | **6445** | **1643** |
| 43 | 173 | 15 | 59468143596 | 59475230719 | 3545 | 0 |
| 47 | 283 | 42 | 98202218916 | 98213822463 | 5854 | 1052 |

Current endpoint: `4802*2^24-1 = 80564191231`.

The quoted 1.03–1.04e11/1,315-new-segment approximation is too short for the retained planning rule. This does not prove a shorter run could never certify; it means it would not follow the predeclared quarter-tail rule used to cost the accepted pipeline.

**Measured anchor, not an old prose estimate.** The 249 recent new segments have producer CPU totals of **21,203.19 seconds = 5.8898 hours**, mean **85.153 seconds/segment**, range 62.65–88.07. These are real `clock()` CPU measurements in `apwit.c`. The complete parallel producer→verifier→witness-hash→scanner batch took **2,810 wall seconds with 10 workers**, with one segment already supplied by the smoke test. It ran while another symbol task was active.

For 1,643 new segments:

* Straight observed producer scaling gives **38.86 CPU-hours**.
* Applying a q^(1/4) BSGS stress factor of 1.08343 at the new endpoint gives **42.11 producer CPU-hours**. This is a model; witness generation and factorization need not obey precisely that scaling.
* Scaling the observed complete-pipeline occupied-worker-slot ceiling and applying the same stress factor gives **56.03 CPU-hours**. This is an extrapolation, not a proven upper bound for the new range. The verifier's CPU time was not separately recorded.
* The three recent accepted symbol runs give approximately **11.7–12.5 CPU-hours at 31**, **6.4–6.9 at 43**, and **10.6–11.4 at 47** under a linear-in-T throughput model: **28.7–30.8 hours total**. This is consistent with the proposed “about 30” part of Claude's budget.

Hence about **70–90 CPU-hours** is a more defensible provisional whole-job model than 190. A small high-range preflight is needed before turning that into an execution budget. Nothing here promises the scaling or authorizes production.

**Storage and RAM.** The old 249 segments retain 4.883 GiB of witnesses plus verified coefficients, about 21.06 MB per segment. The corresponding new evidence estimate is **32.22 GiB**. Scaling observed symbol checkpoint sizes by T times ell gives another approximately **1.13–1.14 GiB** for all three runs. Allow at least 40 GiB of new disk for planning, retain the witnesses, and preserve the existing 60-GiB free-space floor. The host reports **16 GB RAM, 10 physical processors/20 logical CPUs**, and had about **208.8 GiB free** during this audit. Recent eight-worker symbol jobs peaked below 0.75 GB aggregate RSS; a new-range producer/verification peak has not been measured here. The producer is segmented, the symbol mode is table-free, and extending T does not require a dense T-entry array.

**Required implementation preparation:** the old extension worker and scanner explicitly stop at segment 4801/endpoint 80564191232. An additive extension needs updated range guards, a new scanner hash, correct old-source routing, complete coverage checks, and all earlier receipt roots reproduced. Its new range is **4802..6444**. Do not reuse a `.done` marker as proof of intact outputs on restart: the retained worker skips markers before validating their files, while the final check detects corruption later. A capped preflight should include restart/tamper behavior as well as new-range production and verification. No original sealed file needs editing.

The p=47 forecast hash is `2be68ea10c09204dbeb49a76688b0274d37108848f0017eba6b5ae3dda0b490b`. Its conversion from the recorded tame row gives 42 exactly. I did not independently regenerate its large rational-point tame calculation; that remains a prediction, not a certificate.

## 6. Mathematical return and recommendation

The conditional thresholds are correct:

| Newly accepted nonzero certificates, beyond the current record | First remaining small prime | Conditional alternatives for #Sha |
|---|---:|---|
| None | 31 | 9 or at least 8649 |
| 31 | 43 | 9 or at least 16641 |
| 31 and 43 | 47 | 9 or at least 19881 |
| 31,43,47 | 53 | 9 or at least 25281 |

These rely on the retained lower-prime results, the exact 3-primary order 9, finiteness, and the square-order consequence of the Cassels–Tate pairing. Settling 43 alone uses the present corpus and is cheaper, but cannot move the current threshold while 31 is open.

**Recommendation:** keep the completed results and close this Lean-core task. Batch C is a reasonable optional local attempt if the user wants three more primary conclusions and a stronger conditional order bound. Prepare its corrected, capped execution plan and a small new-range preflight before any full launch. It does not require a paid cloud job. Do not treat an arithmetic result differing from its prediction as invalid: record validity, nonvanishing and forecast agreement separately, and keep the previously stated stop/no-recalibration rule.

For the global objective, the missing relation still has to control the actual rank/torsion/Kato data across primes. A finite batch and this formalization do not establish FIN, exact ORDER9 or Q36. That limits the payoff of Batch C; it does not invalidate the finite results or prove that further research cannot help.

## Reproduction and limits

`checks/prepare_replay.py` verifies the three input manifests and sets up disposable copies. `checks/check_p37.py` performs the independent interval/moment/custody checks and replays the frozen checker on live read-only inputs. `checks/lean_replay.json` records the exact compiler, Mathlib pin, source hash and library path; `checks/lean_replay.log` contains the axiom output. Pro's replays and the minimal dependency adaptation are recorded under `replay/` and `checks/`.

The cost inputs, exact planner outputs, source bindings and calculated models are saved in this folder. There was no coefficient generation, no corpus extension and no production symbol computation. Earlier source audits remain imports at their previously recorded grades.
