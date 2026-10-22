# Engine contract review for the exact p83 / ell167 run

Date: 2026-10-13. Grade: **TARGETED_SOURCE_REVIEW_SUPPORTED_UNDER_RETAINED_INPUTS**. No code was modified and the full sum was not rerun. This is a review of the frozen numerical contract, not an independent production of its Fourier coefficients or a formal software verification. The production run was still in progress when this note was prepared.

## 1. Pinned objects and exact domain

All engine/checker line references below are to the files inside
`FROZEN_RUN_PACKAGE_p83_l167/`.

| File | SHA-256 |
|---|---|
| `runtime/src/arbcore.c` | `56a43aac38161d48848df4ed5c2f931f1dc7d5db745600bd140e4be3cac67fd7` |
| `runtime/src/arbcore` | `47d07f2e856e82d2fece7834085aa99d30fa65d32137f0fde843022050fd89db` |
| `checker/singleton_check.py` | `cdbb8f3201ca26ec6add611a8ec983e971857836cd291a1db744a41623062bf6` |
| `spec/SINGLETON_SPEC.md` | `a734be63d72dadabf356f701ca654c01040e1c2c8da8aed022997497666e9921` |

The retained numerical design read in this review is
`/Users/bsm/BSD_RIGOROUS_STREAM_CORE_2026-09-19/DESIGN.md`, SHA-256
`dfc35acb78179609800dc519e0440fbd8480eb28f2ced484bc6b0f9c401ff829`.
Its relevant sections are lines 13–23, 62–82, and 134–140. The historical singleton corrections are recorded in `spec/SINGLETON_SPEC.md`, lines 3–10 and 109–133; this review did not independently reproduce the original external audit.

The current run uses the seed model `[0,-22735,0,106272484,0]`, Q=N=`6503188012738584`, m=167, sign=+1, T=`57378078719`, SEGQ=`16777216`, and lattice denominator1024. These are the frozen configuration and current parameter lock, not parameters inferred from an expected result. The coefficient prime83 enters the final projected coefficient, not the real-analytic Fourier sum.

`ENGINE_REVIEW_BINDINGS.json` also records the source, executable, design file, and the FLINT/MPFR/GMP library files at the executable's declared RPATH. Library implementations and the historical source-to-binary binding are trusted numerical dependencies, not newly formally verified here.

A separate **post-launch observed inventory**, not a prelaunch freeze, is saved in `ENGINE_RUNTIME_INVENTORY.json`. At 2026-10-13T21:25:25.223278+00:00 the running production process PID60078 had the frozen executable and the following three numerical libraries mapped, as reported by `lsof -a -p 60078 -d txt -Fn`:

| Observed mapped library | Current-file SHA-256 |
|---|---|
| FLINT `libflint.21.0.dylib` | `75096794bb13714f06e028c67eb04fee2baa0bb3f2f538ef74c78711779bc811` |
| MPFR `libmpfr.6.dylib` | `f3c7a1c445b82d9f5ad2bde90e10ab8689dbdd319452544d7caefba1ad686dda` |
| GMP `libgmp.10.dylib` | `9156ae6a79534005ce7875a8014326a5189ad73971b1e84360a96d6b3169fdfa` |

All three paths resolve into the declared `sage-env/lib` RPATH. `otool -L` agrees. No PARI library is linked or observed in this evaluator; setting a PARI search path in the historical launcher does not mean the Arb sum uses PARI. The inventory does not individually hash macOS shared-cache/system components or attest the already-mapped pages by memory dump. It records actual observed dependency paths and current file hashes. No library or process state was modified.

## 2. The analytic formula and the tail

For m=167 coprime to N, the retained modular-symbol formula has Q=N, y=1/(m sqrt(N)), and

`kappa = 2*pi/(m*sqrt(N))`.

It expresses each real or imaginary symbol through two exponential Fourier sums at this height; the source implements the plus-root-number case with cosine addition and sine subtraction. See engine lines9–10, 281–284, and 388–396; retained design lines64–78. The root number, conductor, modularity, and period/symbol convention are inherited seed inputs. This source review does not derive them from a successful numerical output.

The displayed tail is

```
B(T) = exp(-kappa*T) *
       (2*sqrt(T) + ((log(T)+2)/kappa + 1/(T*kappa^2))/sqrt(T)).
```

Engine lines120–127 implement precisely this expression in 256-bit Arb arithmetic. The bound follows from `|a_n| <= d(n)*sqrt(n)`, not an empirical decay fit. To check its derivation explicitly, put `D(x)=sum_(n<=x)d(n)` and `f(x)=exp(-kappa*x)/sqrt(x)`. Partial summation, using

`x*log(x)-x <= D(x) <= x*(log(x)+1)`,

gives

```
sum_(n>T) d(n)*f(n)
 <= 2*sqrt(T)*exp(-kappa*T)
    + integral_T^infinity (log(x)+2)*exp(-kappa*x)/sqrt(x) dx.
```

The remaining integral is bounded using `1/sqrt(x)<=1/sqrt(T)` and
`log(x)<=log(T)+(x-T)/T`; the resulting two elementary exponential integrals give B(T). This verifies the formula and its sign. The Hasse/prime-power recurrence input is retained; neither Sha nor an L-value prediction enters this tail.

There are two Fourier series. Engine lines381 and395 therefore add the **unrounded Arb upper bound for 2*B(T)** to both the real and imaginary numerators before division by their respective periods. It would be wrong to use only B(T), or to divide both parts by the same period. The code does neither.

The `TAIL_MS_UPPER_TIMES2` text at line382 is produced by `arf_get_str` and is only a human-readable diagnostic. The rigorous error added at line395 is the binary upper bound obtained before that text is printed. No conclusion should be based on treating the rounded ten-digit diagnostic as an independently outward-rounded decimal bound. The final XB intervals already include the rigorous error.

## 3. Planner denominator and the quarter margin

The planner code is engine lines315–325. At planner denominator L it requires

`B(T) < omega_plus * 1023/(1024*4*L)`.

For this run L=4096, while the actual identification lattice remains `(1/1024)Z`. Thus the planned **normalized radius contribution** is less than

`2*B(T)/omega_plus < 1023/8388608`,

approximately0.000121952. This is one quarter of the usual half-spacing budget for the1024 lattice, with an additional factor1023/1024 margin. The arithmetic recurrence error is separately carried in the balls; the planner does not assume it is zero.

The saved fresh planner output gives

- kappa approximately `4.665522005838149155743245e-10`;
- omega_plus approximately `0.02804490151943640444830940`;
- TMIN=`57366635244`;
- B(TMIN) below the target, and B(TMIN−1) not below it.

The actual T=`57378078719` is the next segment endpoint. It exceeds TMIN and is well above1/kappa, in the decreasing range of this tail. It therefore preserves the planned margin. The evaluator and checker still use LATDEN1024. There is no4096/1024 mismatch in the frozen command.

The planner uses the plus period; it is not itself a proof that all minus symbols will identify. The engine and acceptance checker additionally demand successful minus identification for every row. A minus failure must invalidate acceptance; it must not be ignored because only plus symbols enter c2.

## 4. Exact coverage and coefficient reconstruction

Let R=floor(sqrt(T))=`239537`. Every1<=n<=T lies in exactly one of two disjoint sets:

1. Every prime divisor of n is at most R: the smooth-block contribution.
2. n=mq with q>R prime. There can be only one such q, since `(R+1)^2>T`; then `m<=R` and gcd(m,q)=1.

This proves both exhaustiveness and disjointness. In the second case multiplicativity gives `a_n=a_m*a_q`, which is exactly the factorization used by the streamed loop. This argument is stronger than merely observing that the final count agrees.

Engine lines140–173 construct primes, read the exact ordered coefficient-segment bytes, and reconstruct prime powers with the good-prime recurrence or the bad-prime power rule. Lines196–216 enumerate smooth blocks, including n with a_n=0 in the coverage count. Lines219–236 enumerate every pair(q,m), again counting zero coefficients. The large-prime loop does not omit a term from the coverage count when a_q=0.

The coefficient arithmetic is integer arithmetic; for this T the elementary bound `d(n)<=2*sqrt(n)` gives `|a_n|<=2n`, far below the signed64-bit range. Prime-power recurrence and intermediate products at this scale likewise remain many orders below that limit. This review is for this frozen T and small model, not every possible argument accepted by the general executable.

There are3,420 coefficient segments and13,680 smooth blocks, hence17,100 units. Engine lines352–366 reads each unit back, verifies its self-hash and layout through lines246–259, and combines the balls in fixed unit order. It requires

`smooth + pairs = sum = T = 57378078719`.

The checker parses the numeric fields rather than trusting the word `identity`; see `singleton_check.py` lines156–171. It also requires exactly one root/count/determination record and compares the ordered receipt root for precisely3420 segments; lines172–191. The expected root is

`53de8838b356300dbb7aed6cfc57cab3498c82bd585954fd244095e338f997da`.

Fresh hashes establish that the consumed data are the retained data. The arithmetic truth of those a_q coefficients still rests on their historical verifier certificates. This pass does not independently repeat all prime point counts.

## 5. Period enclosures and lattice identification

Engine lines261–272 computes the periods from isolated roots and AGM using Arb/ACB. It requires three isolated roots and strictly separated real projections; it does not insert a floating-point period. The resulting plus period is the pipeline's omega1, not automatically the full disconnected-real-locus Néron period2*omega1. The retained specification explicitly records this convention and its odd-prime unit comparison.

Engine lines388–408 visits every invertible numerator b modulo167. The cosine and sine arguments are exact rational multiples of pi (`arb_sin_cos_pi_fmpq`), and the complete tails are added before period division.

A double midpoint is used only to propose a lattice candidate; lines399–404 then test the exact rational candidate's containment and the exact ball-diameter inequality. A poor double proposal cannot manufacture success: containment and uniqueness must still hold. The checker then requires all166 labels exactly once and both plus/minus flags `(contains,unique)=(1,1)`; lines193–216. It also requires plus symmetry, minus antisymmetry, c0=0 exactly, and c1=0 modulo83; lines219–240.

The decisive inherited mathematical premise is that the true normalized symbols belong to `(1/1024)Z`. Narrow intervals alone do not prove that premise. It comes from the retained Manin/cusp/period lattice input, referenced by `spec/SINGLETON_SPEC.md` lines49–52 and78–80 and the current theorem check. The regression on389a1 is an implementation check, not a replacement for the seed lattice theorem. This review retains, rather than recertifies, that theorem.

## 6. Printed XB balls and the independent parser

The XB output uses `arb_get_str(ball,20,0)`, engine lines406–407. Flags0 retain the radius and use the default rigorous decimal conversion. The official [FLINT arb_get_str documentation](https://flintlib.org/doc/arb.html#c.arb_get_str), freshly checked for this review, guarantees that default output can be read back as an enclosing interval; the [ball-arithmetic guide](https://flintlib.org/doc/using.html) explicitly says that decimal-conversion rounding is included in the printed radius. It is therefore the correct output function for an external exact-decimal interval check. No `ARB_STR_NO_RADIUS` flag is used.

The frozen historical checker verifies the engine's flags, not the decimal ball contents themselves. The current additional `independent_verifier.py` closes that downstream checking gap by parsing the printed plus intervals as exact rationals, calculating the lower/upper possible lattice integers, and insisting they coincide; see its lines27–65. It then recomputes the coefficient without trusting the printed candidate or desired residue. This is independent downstream arithmetic, not an independent Arb implementation or an independent Fourier-coefficient construction.

Acceptance should require both the frozen checker and this independent interval/coefficient check to pass. A printed ball that is wider than one lattice step is not rescued by the historical engine flags. Conversely, a byte-identical report hash is only custody, not that interval check.

## 7. Inherited facts, current checks, and conclusion

Inherited arithmetic inputs remain: the seed model/conductor/root number, modularity and Fourier identities, the exact coefficient-corpus certificates, the symbol lattice and period/Manin comparison, rank two, residual/integral image, Tamagawa and Ota theorem hypotheses. The current source worker records the p83/ell167-specific hypothesis check separately in `checks/P83_OTA_THEOREM_CHECK.md`. This numerical review does not promote any of those grades.

Current bounded review confirms: the specified tail formula, doubling of the error, planner/evaluator denominator separation, exhaustive sum decomposition, current T and count ranges, exact rational containment tests, and the appropriate outward decimal output contract. The current engine/source hashes match the frozen package. The W8/W16 bounded determinism test is supporting implementation evidence, not a full re-evaluation.

**No exact-run mismatch requiring a code change was found in this scope.** The production result must still finish and pass every output, custody, interval, coefficient, and theorem-profile check. Only a genuinely nonzero accepted coefficient gives the stated Ota consequence for83. A zero gives no vanishing result; a crash, resource stop, or failed check gives no mathematical verdict. Even a successful83 result leaves FIN, ORDER9, Q36, and the infinite-prime bound open.
