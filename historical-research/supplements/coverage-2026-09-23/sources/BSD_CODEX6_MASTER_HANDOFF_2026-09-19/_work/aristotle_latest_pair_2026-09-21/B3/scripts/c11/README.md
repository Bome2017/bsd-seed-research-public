# Pipeline for the modular symbols `[b/121]⁺` of the seed curve and for `C₁₁`

Curve `E : y² = x³ − 22735x² + 106272484x`, conductor `N = 6503188012738584`, root number `+1`,
`ω₁ = 0.028044901519436404448309401807930384171`.

Build (needs `libpari-dev`, PARI ≥ 2.17, and OpenMP):

    gcc -O2 -o apgen apgen.c -I/usr/include/x86_64-linux-gnu -lpari
    gcc -O2 -o buildidx buildidx.c -lm
    gcc -O3 -fopenmp -o stage2 stage2.c -lm

Stages:

1. `run_ap.sh` — `a_p` for all primes `p < X` (`X = 4·10^{10}`) in 400 chunks of `10⁸`, 8 workers,
   via PARI's `Fl_elltrace` on the short model; the five bad primes `2, 3, 2243, 4547, 5843` are
   special-cased with the certified local values `0, −1, +1, 0, −1`. Output `/tmp/ap/cNNNN.bin`
   (int32, primes in increasing order); concatenate in order into `/tmp/ap/ap.bin`.
2. `buildidx X` — odd-prime bitmap plus rank index, so that `a_q` can be looked up for the large
   prime cofactor of any `n < X`.
3. `stage2 X out.txt` — one segmented pass over `n < X` that reconstructs `a_n` multiplicatively
   (`a_{p^{k+1}} = a_p a_{p^k} − p a_{p^{k−1}}` at good `p`, `a_{p^k} = a_p^k` at bad `p`) and
   accumulates, with Kahan summation, the bucket sums
   `S_m[j] = Σ_{n ≡ j (m), n ≤ X_m} (a_n/n) e^{−2πn/(m√N)}` for `m ∈ {1, 11, 25, 49, 121}`,
   `X_m = min(X, 25·m√N/2π)`.
4. `stage3.py out.txt` — cosine transform, the Fricke identity
   `Re λ(a/m) = −c_a − w·c_B`, `B ≡ −(aN)^{−1} (mod m)`, normalisation by `ω₁`, identification in
   `(1/1024)Z`, and the depth-one Mazur–Tate assembly mod `p`.

Sign convention: `stage3.py` returns `[r]⁺ = Re λ(r)/ω₁` with `λ(r) = 2πi∫_r^{i∞} f`, which agrees
with PARI's `mseval(msfromell(E,1), …)`. The retained project runs use the opposite global sign
(their `[0]⁺ = +L(E,1)/ω₁`); negate to compare.

Validation scripts (small conductors, exact modular symbols from PARI):

* `proto.py LABEL m X` — checks `Re λ(a/m) = −c_a − w·c_B` against `mseval` for every `a`.
  Verified with 0 mismatches for `37a1` and `389a1` at `m = 121`, `389a1` at `m = 25`,
  `11a1` at `m = 7` (all 110/20/6 values, primitive and imprimitive components, both root numbers).
* `padicL.py LABEL p` — depth-one and depth-two Mazur–Tate approximations from exact symbols.
* `reduced.py LABEL p` — checks the folded mod-`p` formula against the full approximation.
