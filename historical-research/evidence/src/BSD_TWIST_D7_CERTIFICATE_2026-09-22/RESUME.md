# RESUME — certify L(E^-7,1) != 0   (D = -7 rank-zero certificate)

## Why (stage 7 of the definite-field gate)
The derived-height inequality forces d^+ = 0 but leaves d^- in {0,1,2}. ONLY this certificate removes those rows:
L(E^-7,1) != 0  =>  GZK at analytic rank 0  =>  rank E^-7(Q) = 0 AND #Sha(E^-7/Q) < inf  =>  d^- = 0.
Then with d^+ = 0 free, Div Sha(E/K)[p^inf] = 0, i.e. A2a. See ~/BSD_DEFINITE_FIELD_GATE_2026-09-22/STAGE7_*.

## Deliverable / scope (FIXED - do not widen)
Record ONLY:  L(E^-7,1) != 0, and the standard consequence rank E^-7(Q) = 0, Sha(E^-7/Q) finite.
NO BSD claim. NO order formula. NO Sha order. If no interval excludes 0 -> CERTIFICATE_NOT_OBTAINED,
and DO NOT infer vanishing.

## Math contract (stage 0 DONE)
L(E^D,1) = 2 * sum_{n>=1} chi_D(n) a_n/n * exp(-c n),   c = 2pi/(|D| sqrt N),  N = 6503188012738584
chi_D = Legendre symbol mod 7 (D = -7 = 1 mod 8, fundamental, gcd(7,N)=1)
c_7 = 1.11306025e-8,  1/c = 8.98e7
Tail: |2 sum_{n>T}| <= 2*tail_ms(c,T),  tail_ms(k,T) = [2 sqrt T + ((log T + 2)/k + 1/(k^2 T))/sqrt T] exp(-k T)
  Justification of the identity: E_1(x) <= e^-x / x, which is exactly why the sealed derivative adapter used
  tail_twist = 2*tail_ms/(cT) and the L'' mode uses tail_l2 = 2*[..]/(cT)^2. The central value is the base case.
  CROSS-CHECKED: 2*tail_ms(c_23, 3456106495)/(c_23*T) = 0.335041797048 vs the sealed run's 0.335041797049. MATCH.

## Tail table (this is the STOPPING CRITERION, not a chosen cutoff)
  T = 1e9  -> 3.75      T = 2e9 -> 5.87e-5     T = 3e9 -> 9.36e-10    T = 4e9 -> 1.48e-14
  T = 5e9  -> 2.33e-19  T = 7e9 -> 5.63e-29    corpus T = 5.5046e10 (3281 segments of 2^24)
RULE: compute successive admissible truncated intervals; stop at the FIRST T whose interval excludes 0.
      Never choose a cutoff in advance.

## Hard constraints
- Master handoff ~/BSD_CODEX6_MASTER_HANDOFF_2026-09-19/ is READ-ONLY. The sealed D=-23 run lives there
  (_work/d23_twist_2026-09-21/) and is the reference adapter. READ IT, NEVER WRITE THERE.
- DO NOT ALTER THE STAGE-W CORPUS. Read-only access to ap segments.
- Table-free traversal ONLY. No dense O(T) allocation (26 GiB at 7e9 on a 16 GiB host).
- Preserve separately S(T), B(T), and the interval [2S-2B, 2S+2B].
- Independently replay the decisive final interval.
- PRIOR INCIDENT: a preflight once symlinked reused segments WITHOUT creating done-markers, and the producer
  wrote THROUGH the symlinks into sealed inputs. If any reuse/symlink scheme is used, create markers FIRST.

## CERTIFICATE OBTAINED - see RESULT.md
    L(E^-7,1) in [9.054319, 9.054421]   ZERO_EXCLUDED  POSITIVE   margin 1.79e5
    => analytic rank 0 => (GZK) rank E^-7(Q) = 0 AND Sha(E^-7/Q) finite.
    NOTHING ELSE CLAIMED.

## Progress
- [x] stage 0  tail bound derived + cross-checked against the sealed run   -> TAIL_BOUND.txt
- [x] stage 1  harness read; corpus = BSD_SEED_P13_RUN_2026-09-21/run/ap (3281 segs); contract confirmed
- [x] stage 2  central7.c written (exp weight; entire E1 node-table apparatus removed); builds warning-free
- [x] stage 3  kernel-test 1280/0 fail; block-test 448 terms/0 fail          -> kernel_test.log block_test.log
- [x] stage 4  T = 2013265919 (120 segments), 600 units, 12 workers, ~4.5 min, peak RSS 0.83 GB
- [x] stage 5  fresh recombination byte-identical; INDEPENDENT end-to-end replay at T=16777215 agrees to 1.8e-15;
               independent mpmath tail matches to 22 digits; corpus integrity 0 segments modified

## Artifacts
  central7.c / central7 / build.sh      the adapter (retained_arbcore.c sha256 56a43aac...67fd7, unmodified)
  TAIL_BOUND.txt                        stopping criterion + cross-check against the sealed D=-23 run
  kernel_test.log block_test.log        validation
  run_T2013265919.log                   the certificate run
  combine_replay.log                    fresh deterministic recombination (byte-identical)
  independent_replay.log                separate-implementation end-to-end check
  run_T16777215.log                     engine at the small cutoff used for that check
  run_T2013265919/ run_T16777215/       unit files (600 and 5)
