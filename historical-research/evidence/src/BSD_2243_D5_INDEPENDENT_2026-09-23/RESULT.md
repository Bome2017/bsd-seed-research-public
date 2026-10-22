# D5_CERTIFIED_NONZERO

The corrected split-multiplicative height on the retained basis satisfies

    H_2243 / 2243 = [[2127,1294],[1294,764]] mod 2243,
    Reg_2243 = 2181 * 2243^2 + O(2243^3),
    v_2243(Reg_2243)=2,
    Reg_gamma = 2181 mod 2243, for kappa(gamma)=1+2243.

This independently supplies D5 at computer-assisted, published-formula-import grade. The global denominator contribution, canonical sigma truncation, Tate correction, polarization, and gamma normalization are all accounted for in PROOF.md.

The implementation uses standard-library exact integers and fractions, a logarithmic-size division-polynomial recurrence, and no PARI/Sage height functions. It never consumes the Fourier corpus. The retained PARI residue was compared only after deriving and executing the independent calculation; it agrees.

## Replay

From any working directory, with Python 3:

    python3 /Users/bsm/BSD_2243_D5_INDEPENDENT_2026-09-23/certify_d5.py --digits 7 --output /tmp/d5_replay.json
    python3 /Users/bsm/BSD_2243_D5_INDEPENDENT_2026-09-23/verify_d5.py

The second command recomputes VERIFICATION.json inside this additive folder. The sealed source folders are read-only to both programs. For a byte-preserving external replay, copy this small folder and run verify_d5.py from the copy.

## Verification

The separate verifier checks division-free recurrences, projective multiplication, exact small-multiple global denominators, every bad-prime cancellation case for the actual large multiple, higher-precision stability, the parallelogram identity, scaling, and a unimodular basis change. All checks pass. These checks are not a formal Lean proof or an independent reproof of the imported analytic height formula.

## Endpoint effect

D5 no longer needs an unverified numerical nondegeneracy input. A future certified unit cubic coefficient C_(2243,3), together with the retained D1--D7 theorem/period/rank/image/lattice assumptions, would now permit the stricter Jones-forward proof of Sha(E/Q)[2243^infinity]=0. The finite-primary input required by Jones is then supplied first by D2/D4, not assumed by this height calculation.

This operation does not compute C_(2243,3) or prove any new primary Sha vanishing, FIN, total order nine, or the real leading-term identity. It does not resolve, require, or adjudicate the converse attribution question in Stein--Wuthrich/Jones. No successor is launched.

## Resource and custody record

One local standard-library process per check, no subagents, no paid compute, no coefficient extension, no cloud activity. The finite calculation and additional verification together took under one second, with measured peak RSS below 12 MiB. The initial address-space and data-limit requests were rejected by macOS; the 120 CPU-second limit succeeded, the algorithm's input sizes were explicitly bounded, and peak RSS was checked. Existing bound inputs all remain byte-identical.

Exact times, software information and source checks are in RESOURCE_REPORT.json and INPUT_IMMUTABILITY_CHECK.json. PROOF.md is the final mathematical statement; DERIVATION.md is the preserved preliminary working derivation and is superseded where it described pending checks.
