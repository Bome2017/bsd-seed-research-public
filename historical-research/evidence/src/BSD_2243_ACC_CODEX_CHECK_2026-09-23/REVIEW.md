# Local 2243 evaluator review — stopped before paid compute

**Review verdict: FAIL for the claimed crash/restart isolation of v2.3.** The arithmetic core passed the bounded replay and the checks described below. This is an execution defect, not a refutation of the 2243 mathematical route or any retained certificate.

**Financial boundary:** no paid pilot, cloud instance, production run, storage purchase, or new coefficient corpus was launched. The user has explicitly ruled out paid compute. This review ends here; there is no successor job or authorization to spend.

## 1. Concrete finding: generation reuse before the first checkpoint

**Priority 1.** `acc2243v2.c:431-435` chooses GEN from checkpoint filenames alone. `acc2243v2.c:329` uses GEN to name the streaming directory. If a process dies before writing a checkpoint in that generation, its restart chooses the same GEN and the same worker directory. This also applies to a later generation that dies before writing its own first checkpoint.

The independent reproduction used the unmodified rebuilt binary, a retained coefficient segment, selection L1, and a delayed stub at the documented streaming-command interface. After the first command started, only the parent accumulator was killed, exactly the orphan scenario the implementation claims to handle. A second accumulator was then started with the same arguments. Both live stream children were passed

    restart_probe/out/stream_g001_w00

and there were zero saved checkpoints when the second accumulator started. Evidence: `restart_probe/RESULT.json`, both run logs, and `restart_probe.py`. The probe terminated all its children afterward and generated no coefficient data.

This contradicts the claimed non-sharing of stream directories with orphaned producers. In the real wrapper both children can clear/write the same `wit` and `ap.tmp` directories (`stream_seg.sh:12`), causing interference and lost work. **No falsely certified arithmetic result was demonstrated.** The hash checks still provide separate integrity protection; this finding is an execution/restart failure.

Required correction before production: reserve a durable fresh run-generation identifier before spawning children, or use non-reusable unique scratch directories. Then test a crash BEFORE the first checkpoint, including a repeated early crash. No repair was made to the reviewed files.

## 2. Independent replay actually performed

The pinned source, binaries, wrapper and SHA adapter matched all five recorded build hashes. An independent local build of the unchanged source completed with no compiler warnings. Its distinct Mach-O hash is recorded in BUILD_BINDINGS.json; binary-byte equality was not used as a correctness criterion.

Fresh m=27 replay:

- T=4,831,838,207; 1,445 work units; existing retained coefficients only; 8 workers.
- Wall time 301.35 seconds; user CPU 2,316.48 seconds; system CPU 21.20 seconds; reported peak RSS 717,389,824 bytes.
- CHUNK_DIGEST exactly `e24f3f4d4e705b42e6002bf8059430aa73ae3315bc437d2665bd99d151330681`.
- The 288-segment root exactly matches the retained `ca234d65fa40332695f5f08675ade782c9a8439bee068b69ac9b64a470002084`.
- Both direct and DFT merges recover all 18 plus and 18 minus symbols.

For m=81, copied/hash-bound existing checkpoints were merged through both paths. This was NOT a fresh m=81 summation. All 54 plus and 54 minus symbols match the retained exact table. The weighted anchor is exactly

    1024 a_{4,2} = 15,851,520 = 1024 * 15,480,

and the unit test correctly fails modulo 3.

The independent comparator uses exact rational arithmetic on the displayed interval endpoints and reference values. Across both denominators, both signs and both merge paths it checks 288 containments, equality of candidates, lattice uniqueness and pairwise interval overlap. It does not reuse the author's comparator. Results: REPLAY_COMPARISON.json.

Five independent negative controls all fail closed: a flipped checkpoint bit, a missing checkpoint, a duplicated checkpoint, a removed unit record with a recomputed SHA trailer, and a mismatched truncation parameter. Results: NEGATIVE_TESTS.json.

The source's earlier 24-test suite and full-denominator/47-unit test were inspected, not independently rerun. In particular this review does not claim to have performed the full 2243 transform or certificate summation.

## 3. Mathematical and numerical checks of the accumulator

### Inherited arithmetic and changes

Function extraction and token comparison (FUNCTION_DIFF.json/txt) confirm unchanged tail_ms, small_primes, sieve, seg_bounds, periods, curve and set_kappa. read_apseg gains an explicit directory argument; load_table passes it. gen_block removes the unused dense-table branch, leaving exactly the table-free recurrence used by the retained msl mode. invmod is changed to extended Euclid. Thus “everything is verbatim except read_apseg” is too strong as a textual claim, although the additional differences inspected preserve the intended msl mathematics.

The Part S / Part L decomposition is valid: every n<=T either has all prime factors <=floor(sqrt(T)), or has a unique prime factor q>floor(sqrt(T)) and n=q m with m<=floor(sqrt(T)). The cofactor is coprime to q. The L subunit ranges partition the cofactor interval; the S blocks partition the integer interval. The recurrence builds the same multiplicative a_n. In run_L the exponential recurrence now advances through zero a_q as well; this is an enclosure-preserving change, not an identical sequence of floating operations.

### Fixed-point errors and integer range

Each term interval has midpoint m_i and radius r_i. The fixed-point conversion contract gives |2^-96 z_i-m_i|<=2^-96. The error increment bounds r_i 2^96+1, so the total E bounds the SUM of absolute term errors. Grouping terms into residue classes therefore gives sum_k |error_k|<=E, not merely a per-class bound.

The installed MAG_BITS=30 and the FLINT 3.3.1 mag_get_d implementation were checked. In its normal exponent range the conversion is exactly representable in binary64; its extreme cases round upward or return infinity. Scaling by 2^96 is exact over the accepted range. The guard rejects an infinite/NaN or oversized scaled radius. The +2 increment conservatively covers integer conversion and midpoint truncation. FLINT/Arb remain imported numerical-library dependencies, not formally verified here.

For valid certified Fourier coefficients |a_n|<=d(n)sqrt(n)<=2n. Thus an exponential-weight term has absolute value <=2; with the accepted radius and rounding it contributes less than 3*2^96 in fixed-point units. At the production T and m=2243^2, a residue class contains at most 7,775,693 terms. The resulting conservative sum fits in 121 bits, below both the 124-bit checkpoint guard and the signed 128-bit limit. The worst accepted total error tally fits in 105 bits. For the m=27 replay the analogous sum fits in 126 bits, still below signed overflow; the actual checkpoint guards passed. These are bounds for the stated valid inputs, not protection against arbitrarily forged checkpoint arrays or unsupported T,m choices. The C additions themselves are not universal overflow checks.

### DFT, periods and scalar test

The DFT convention has negative exponential sign. Thus the direct plus combination is Re F_b + s Re F_u, and the direct minus combination is -Im F_b + s Im F_u. Both signs match the implementation.

Each cosine/sine combination has absolute value <=2. Since E is an l1 error bound, adding 2E ONCE per output is valid. Sending exact dyadic class midpoints into the DFT and adding that uncertainty afterward avoids multiplying E by the number of classes. Arb still encloses the transform's own rounding. The separately added tail is the inherited twice-tail_MS bound.

For a period interval Omega bounded away from zero,

    (m+e)/Omega = m/Omega + e/Omega,
    |e/Omega| <= radius / inf|Omega|.

This proves the div_period enclosure used by v2.3. Source normalization still matters: the plus period is omega_1, not the total two-component real BSD period 2 omega_1.

The discrete logarithm calculation uses omega(b)=b^(p^(n-1)) mod p^n and generator 1+p; this is the Teichmueller/principal-unit decomposition for the stated odd prime powers. The exact weights are binomial(j,r), with alpha^(-n)=alpha^n for alpha=+/-1. The nonzero-only test correctly uses ceil(L/p)>floor(U/p), with outward division, on the LATDEN-scaled interval. Its interpretation requires the retained REAL lattice and p not dividing LATDEN; mere p-integrality is insufficient.

### Integrity boundaries

SHA trailers detect accidental checkpoint corruption; coverage detects omitted/duplicate work units; the linear 64-bit fingerprint is a consistency check, not a cryptographic proof of the computation. In particular it is insensitive to certain deliberately constructed changes in high fixed-point bits if the SHA is also forged. None of these checks proves the original coefficients or the tail theorem.

The streaming path requires a verifier hash and compares it to the consumed bytes before checkpointing the completed unit. The pre-produced path only checks a hash companion when present, and load_table does not itself authenticate its small-prime input. Therefore the pre-produced corpus must stay independently verified, pinned and immutable across setup, workers and restart. This retained trust boundary is not removed by the new stream wrapper. The fresh replay binds the consumed segment root to the retained result; it did not re-run every coefficient witness verifier.

## 4. D2/D5 and exact normalization

See MATHEMATICAL_CHECK.md for the complete local derivation and source bindings.

- D2 is supplied by Skinner's integral exact sequence together with the explicit Tate/Kummer identification of S with the classical Selmer group.
- If SW Theorem 6.1 is imported as published, the successful cubic-unit test implies minimal classical order, hence height nondegeneracy and primary finiteness. A separate nonzero-regulator computation is then redundant as a mathematical premise.
- If the project insists on reconstructing the conclusion from Jones's forward statement alone, D5 remains a separate input at THAT stricter grade. No such independent reconstruction or numerical height certificate is claimed here.
- Exact modular arithmetic rechecks q_E mod 2243^3 and ell_gamma=1799 mod 2243 (LOCAL_L_INVARIANT.json).
- The period label in S1c needs the harmless-at-2243 factor-2 clarification. All main-conjecture/period-comparison/lattice inputs retain their existing qualifications.

## 5. Stopping point

The arithmetic replay passed; the restart-isolation claim failed at an explicit case. Checkpoint compaction remains unimplemented, and Linux/cloud execution was not tested. No full-production readiness verdict is earned.

The approximately $2,000 cloud model purchases a single sufficient test, not full BSD and not a guaranteed new Sha result. A successful nonzero coefficient would settle only the 2243-primary component under the retained dependencies. A zero coefficient would leave the sufficient test inconclusive.

**The local review is complete and stopped. No paid work or successor is scheduled.** No new Sha prime, FIN, total order nine, or q=36 has been proved.

Source implementation for mag_get_d: https://raw.githubusercontent.com/flintlib/flint/v3.3.1/src/mag/get_d.c (retrieved narrowly to check the error-tally conversion; pinned in FLINT_SOURCE_BINDING.json).
