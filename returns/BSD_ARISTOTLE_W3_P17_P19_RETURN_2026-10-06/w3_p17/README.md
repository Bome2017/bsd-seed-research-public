# Seed weight-two symbols at denominator p² (p = 17, 19)

## Build

```
gcc -O3 -march=native -o msl_sq msl_sq.c -lm -lpthread              # plus symbols, kernel exp(-x)
gcc -O3 -march=native -DKERNEL_E1 -o msl_e1 msl_sq.c -lm -lpthread  # twisted L', kernel E_1(x)
```

## Usage

```
msl_sq <Tfactor> <threads> <outprefix> m1 [m2 ...]
```

- Each modulus must satisfy `m ≤ 400` and `gcd(m, N) = 1`.
- The cut-off is `T_m = Tfactor · m · √N`.
- Runs are resumable through `<outprefix>.seg`.
- Setting the environment variable `MSL_XSCALE` rescales `X`. This is used for the functional-equation test.

## Runs whose outputs are kept in `runs/*.out` and `runs/*.log`

| command | purpose |
|---|---|
| `msl_sq 3.0 8 runs/seed_m17_tf3 17` | `[a/17]^+` |
| `msl_sq 2.5 8 runs/seed_m289_m103_tf2p5 289 103` | `[a/289]^+`, plus the 103 calibration against the retained receipt |
| `msl_sq 3.0 8 runs/seed_m1_tf3 1` | `[0]^+` |
| `msl_sq 2.5 8 runs/seed_m361_m19_tf2p5 361 19` | `p = 19` |
| `msl_e1 3.0 8 runs/twist23_E1_tf3 23` | `L'(E^{(-23)},1)` |
| same, with `MSL_XSCALE=1.2` and `MSL_XSCALE=0.8333…` | functional-equation test |

## Analysis

- `analyze_p17.py` writes `P17_RESULTS.json`.
- `analyze_p19.py` writes `P19_RESULTS.json`.
- `analyze_twist.py` writes `TWIST23_RESULTS.json`.
- `surjectivity_check.py` writes `SURJECTIVITY.json`.

## Tests

- `validate_formula.py` compares the symbol formula with exact modular symbols on 11a1, 37a1 and 389a1, at `m = 5, 7, 9, 25, 49`.
- `test_ap.c` compares BSGS `a_p` with naive point counting.
- `ref_brute.c` compares the whole engine with an independent brute-force summation.

The write-up is in `../W3_P17_REPORT.md`.
