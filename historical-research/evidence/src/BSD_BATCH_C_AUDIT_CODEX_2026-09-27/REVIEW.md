# Independent certificate audit of Batch C

Date: 2026-09-27.

**Verdict: BATCH_C_CERTIFICATES_PASS_AT_RETAINED_GRADE.**

All three numerical certificates pass the frozen acceptance replay and an independent exact-rational check of every printed symbol interval. The retained Ota/lattice/rank/image/corpus imports therefore give

\[
\Sha(E/\mathbf Q)[31^\infty]=\Sha(E/\mathbf Q)[43^\infty]
=\Sha(E/\mathbf Q)[47^\infty]=0.
\]

No blocking defect was found. Keep the conclusions at the existing written-theorem/applied-numerical-certificate grade. This is not a fresh independent evaluation of the modular symbols or a reproof of the imported theorems.

## 1. Input identity and frozen bindings

Input: `BSD_BATCH_C_REVIEW_2026-09-27.zip`, SHA-256

    c2619d82e498a38376951ebb4d8d699695379a5d59ab3dff904e48fd176dfc33

All **71 supplied manifest entries** pass. The archive has no duplicate names, escaping paths or symbolic links. The source ZIP and extracted input remain unchanged.

The bundle does not contain every frozen checker/engine/specification dependency. I retrieved those named local files read-only, checked **117 frozen file bindings**, and copied them into this audit's sources directory. The freeze manifests match these Git objects:

| Run | Full frozen commit |
|---|---|
| 43/173 | `1a4564d46bc4b694419b4c1469cf5174ba9d3b32` |
| 47/283 | `0d4711eb9d31de4ab63d5f9120b94e2041f73043` |
| 31/311 | `f9700404f525c12e9639fc7b6d2a935cc687fc7f` |

All three package working trees were clean. Their recorded freeze times precede their recorded run starts. These are local provenance records, not externally notarized timestamps.

The source run outputs, PARAMS, run manifests and acceptance reports match the bundled copies. The currently installed engine matches `47d07f2e856e82d2fece7834085aa99d30fa65d32137f0fde843022050fd89db`. The three checkers/launchers are identical to the previously audited p=17 versions. The new worker, repaired verifier, scanner and producer hashes also match their declared pins.

## 2. Independent arithmetic and interval checks

The fresh checker uses Python standard-library exact fractions. It derives the integer candidates from the interval endpoints, using

    ceil(1024 * lower) = floor(1024 * upper),

then compares that unique integer with the declared candidate. It does not accept the engine's printed `contains`/`unique` flags as a substitute for this calculation.

Every plus and minus interval contains exactly its declared point of the retained 1/1024 lattice. The labels are exactly all nonzero residues, each once; plus symmetry and minus antisymmetry hold. The parsed COUNT records satisfy smooth + pairs = T with the exact frozen cutoff. Output, engine and parameter bindings pass.

| p | ell | Generator | Symbol intervals | c0 | c1 | c2 | c2 mod p |
|---|---:|---:|---:|---:|---:|---:|---:|
| 43 | 173 | 2 | 344 | 0 | -13072 | -227412 | **15** |
| 47 | 283 | 3 | 564 | 0 | 27260 | 596378 | **42** |
| 31 | 311 | 17 | 620 | 0 | 22072 | 330990 | **3** |

All **1,528 intervals** pass. Each c1 is divisible by p. The coefficients are recomputed by summing the exact identified plus symbols with the binomial discrete-log weights. All primitive roots were tested independently: 84 at 173, 92 at 283 and 120 at 311. They obey the expected inverse-square change, preserving nonvanishing.

Fifteen altered tables were rejected by the independent checker: for each run, duplicate and missing labels, a changed candidate, an interval with several lattice candidates, and an interval with no lattice candidate. An empty intersection is not counted as success.

The frozen acceptance program was then replayed on each genuine run, using a snapshot of the same receipt lines. All three returned NONZERO with exactly the supplied report values. The shipped twenty-control record remains retained evidence; I did not rerun its fixture-generating workflow.

The first invocation of this audit's own arithmetic script stopped at Python's handling of UTC `Z` timestamps. Explicit conversion to `+00:00` fixed that compatibility issue. It was not a certificate or mathematical failure.

## 3. The arithmetic implication and its retained dependencies

The curve is the seed `[0,-22735,0,106272484,0]`. Direct quadratic-residue point counts, separate from the supplied PARI output and the frozen checker's double loop, give:

| p | #E(F_p) | ell | #E(F_ell) |
|---|---:|---:|---:|
| 43 | 52 | 173 | 196 |
| 47 | 44 | 283 | 288 |
| 31 | 40 | 311 | 296 |

All p and ell are prime; p does not divide 6N or the retained Tamagawa product 16. Each ell is prime to pN, v_p(ell-1)=1, and p does not divide #E(F_ell). These auxiliaries therefore satisfy the frozen checker's stronger torsion-free condition, hence the required cyclicity condition. The three target primes are good ordinary and non-anomalous.

The route remains the retained Ota Theorems 1.5/6.4 implication. With the project rank, residual-image and period/lattice inputs, the plus-symbol coefficient represents the required leading term up to the already audited p-unit normalization. The full label sum and the 1024 denominator have been preserved. No additional division by p is introduced.

Nonzero c2 gives Sha[p]=0 under that retained theorem application. A nonzero p-primary torsion group has an element of order p, so this kills the entire primary group without assuming its finiteness first.

This audit checks the prime-specific arithmetic and certificate bindings. It does not newly prove Ota, the rank/basis theorem, the image theorem, c_E dividing 512, the 1/1024 lattice, or the interval engine. The old good-prime and new BH bad-prime theorem profiles have not been interchanged.

## 4. Corpus extension and cutoff evidence

The additive extension covers exactly segments 4802 through 6444, yielding 6,445 total segments. The worker's restart validation checks the stored witness and coefficient hashes before skipping a done marker. The final corpus checker additionally checks exact receipt tiling, file sizes, producer/verifier counts and scanner bindings. The checked source scripts match extension commit `6c144a90431fa508bdd31911d7c7fac73ce3cad5`.

I read the **6,445 small receipt logs**, required exactly one correctly tiled receipt per segment, and independently rebuilt their ordered hash roots. All ten previously pinned roots reproduce. The relevant run roots also reproduce:

| Prefix | Receipt root |
|---|---|
| 3545 | `80b814ed11cb387bbca86919c4ce01fcb6afe68bc9a0f037006777307ddbbf6a` |
| 5854 | `9fc6b8e850307d586046f31e038a58ac1af2f6f468e60ab52761f8375bbff643` |
| 6445 | `92cd0222d32e722087897738839a560b24af45a9a44221c6271502e0ed7de60f` |

For all 1,643 new segments, producer/verifier witness-count metadata agree, verifier stderr is empty, and scan metadata match the recorded witness hashes. **I did not rehash the large coefficient/witness files or rerun their arithmetic verifier.** That part remains the bound original corpus-check evidence. The engine's consumed-coefficient root matches these receipts through the retained implementation.

All six supplied planner outputs (three denominators, two error budgets) replay byte-for-byte with the pinned engine. The aligned quarter-tail endpoints are:

| p | T | Segments |
|---|---:|---:|
| 43 | 59,475,230,719 | 3545 |
| 47 | 98,213,822,463 | 5854 |
| 31 | 108,129,157,119 | 6445 |

Here LATDEN=4096 is the planner's quarter-tail reserve; the arithmetic symbol lattice remains 1/1024. Final interval acceptance was also checked, so no planner-only conclusion is being substituted for completed numerical certification.

## 5. Forecasts and the common-multiplier claim

All three Batch C forecast files match their frozen hashes, and all three computed residues match. The forecasts are not read by the acceptance program. An independently certified nonzero disagreement would still have given primary vanishing; agreement is a separate observation.

One chronology correction should accompany future summaries. The p=29 forecast was written **while its run was in progress, before its result**, as its own header says. It should not be counted as a forecast made before launch. The later 37,41,43,47,31 forecasts were recorded before their respective launches. Thus “six pre-result forecasts matched” is the appropriate summary; “six pre-launch predictions” would overstate the record.

The product calculation is correct:

    17*19*23*29*31*37*41*43*47 = 20,475,850,236,047.

The previously retained normalized residues and these new ones are consistent with a **putative common integer** congruent to 288 modulo that product. This is not a construction of a prime-independent multiplier, proof of its exact value, or a quantitative probability of the conjecture. I did not regenerate the large rational-point tame-regulator calculations in this audit; their forecast inputs retain their previous grade.

## 6. Consequence, resources and disposition

Combining these three accepted primary conclusions with the retained results at the earlier primes gives the recorded complete primary list through 47: zero except at 3, where the group is (Z/3)^2. Those older results are imports, not new replays here.

If the full Sha group is finite, its p-primary orders have the square-order property. The first unexcluded prime is 53, so

\[
\#\Sha(E/\mathbf Q)=9\quad\text{or}\quad
\#\Sha(E/\mathbf Q)\ge 9\cdot53^2=25{,}281.
\]

This remains conditional on FIN. It neither proves FIN nor determines ORDER9. Q36 is also unchanged.

The supplied complete timing logs total about 69.534 CPU-hours for the three symbol runs, Stage W and successful preflight. Adding the ledger's small aborted-preflight and corpus-check allowances gives about 69.604 hours, consistent with the reported 69.6 and below the 100-hour cap. Symbol-run peak RSS is below 0.75 decimal GB. The disk/free-space history is retained from the launch records; it was not newly measured as an audit benchmark. These measured local runs do not by themselves reprice the much larger bad-prime jobs.

**Disposition:** retain the three new primary results and updated conditional order bound. Add the p=29 chronology qualification to future summaries. No numerical repair, rerun or additional prime is needed to accept Batch C at its recorded grade.

Only this additive audit folder and its export were written. No production, full corpus rehash, witness generation, repository edit, push, outreach, paid computation or successor was performed.

## Reproduction

`independent_check.py` is standard-library-only and checks the bundled interval tables without original-host data. It writes INDEPENDENT_CHECKS.json beside itself; run a scratch copy to preserve the sealed audit.

`replay_custody.py` requires the named original-host frozen engine, receipt logs and package paths. It opens receipt/metadata files, not the large coefficient or witness payloads, and executes only the acceptance checker and short cutoff planner. Its outputs are retained under replay/ and in REPLAY_RESULTS.json. SOURCE_BINDINGS.json, ADDITIONAL_BINDINGS.json and the receipt bindings identify the copied evidence.
