# `C₁₁` for the seed curve: computed

**Result of this session.** For

    E : y² = x³ − 22735x² + 106272484x,   N = 2³·3·2243·4547²·5843 = 6503188012738584,

the prime 11 is good ordinary (`#Ẽ(F₁₁) = 14`, `a₁₁ = −2`), and

> **`C₁₁ := [T²] L₁₁(E,T) ≡ 8 (mod 11)`** in the `ω₁` normalisation
> (`≡ 4 (mod 11)` in the Néron / full-real-period normalisation). **In particular `C₁₁ ≠ 0`.**

The 45 modular symbols at denominator 121 that the value rests on are listed in
`RequestProject/SeedC11Value.lean` and `scripts/c11/symbols_seed.json`; the exact arithmetic taking
them to `8` is machine-checked (`SeedC11.C_eleven_value`, `SeedC11.C_eleven_ne_zero`; no `sorry`,
axioms `propext`, `Quot.sound`).

Under the review's retained specialisation of the 7-primary argument — `C₁₁ ≠ 0 ⟹ Ш(E/Q)[11^∞] = 0`
— this supplies the missing arithmetic component for `p = 11`. That implication is **not** proved
here and is not claimed here; this note delivers the certificate it consumes. Nothing here bounds
`#Ш`, settles order 9, or touches `q = 36`.

---

## 1. The assembly, and why it is 45 symbols

Let `α` be the unit root of `X² + 2X + 11` (so `α ≡ −2`, `α^{−2} ≡ 3 mod 11`), `ω` the Teichmüller
lift mod 121, and for `u` prime to 11 let `j(u) ∈ Z/11` satisfy `u ≡ ω(u)·12^{j(u)} (mod 121)`.
With `S b = [b/121]⁺`, `s a = [a/11]⁺` the plus symbols in the `ω₁` normalisation, the depth-one
Mazur–Tate approximation is

    P(T) = Σ_{u ∈ (Z/121)ˣ} ( α^{−2} S u − α^{−3} s (u mod 11) ) (1+T)^{j(u)},

and Stein–Wuthrich Prop. 3.5 gives `[T²]L₁₁ ≡ [T²]P (mod 11)`. Three finite facts, each `decide`-checked
in `RequestProject/SeedC11Assembly.lean`, collapse this:

* **the denominator-11 symbols drop out**: for each residue `a`, `Σ_{u ≡ a (11)} C(j(u),2) = C(11,3)
  = 165 ≡ 0 (mod 11)` (`level_drop_eleven`);
* **folding**: `j(121−b) = j(b)` and `S(121−b) = S b`, so each coefficient doubles to
  `α^{−2}·j(j−1)` (`jlog_neg_eleven`, `fold_coeff_eleven`);
* **support**: `3·j(j−1) ≡ 0` exactly for `j ∈ {0,1}`, removing 10 of the 55 folded classes and
  leaving **45** (`supp_eleven_length`).

Hence `C₁₁ ≡ 3·Σ_b j(b)(j(b)−1)·[b/121]⁺ (mod 11)`, i.e. with the weight classes of `table_eleven`:

| weight | `j(b)` | `b` | Σ of the computed symbols |
|---:|---|---|---:|
| 2 | 6 | 2, 6, 18, 41, 54 | −110 |
| 3 | 4, 8 | 5, 14, 15, 17, 25, 32, 42, 45, 46, 51 | −70 |
| 5 | 5, 7 | 8, 20, 24, 26, 43, 47, 49, 56, 59, 60 | −10 |
| 6 | 2, 10 | 10, 16, 23, 28, 30, 31, 35, 37, 48, 52 | 102 |
| 7 | 3, 9 | 7, 19, 21, 29, 34, 38, 50, 53, 57, 58 | −46 |

`2(−110) + 3(−70) + 5(−10) + 6(102) + 7(−46) = −190 ≡ 8 (mod 11)`.

The same assembly at `p = 7` (`α^{−2} ≡ 2 mod 7`) yields 15 symbols with weights `5` on
`{2,4,11,13,22,23}`, `4` on `{6,9,10,15,16,24}`, `3` on `{12,17,20}` — **identical to the
predeclared formula of the retained `P7_PRIMARY_THEOREM`**, which was derived independently of this
work.

## 2. The numerical run

Symbols are obtained pointwise (no character decomposition, so imprimitive components need no
separate treatment): for `gcd(m,N) = 1`, `y₀ = 1/(m√N)`, root number `w = +1`,

    c_a = Σ_{n ≤ X} (a_n/n) cos(2πna/m) e^{−2πn y₀},
    [a/m]⁺ = (c_a + w·c_B)/ω₁,     B ≡ −(aN)^{−1} (mod m).

(Split `{a/m, i∞}` at `a/m + iy₀`, push the lower half by `W_N` and then by
`γ = [[A,B],[aN,m]] ∈ Γ₀(N)`, `Am − BaN = 1`; the image is `{i∞, B/m + i/(Nm²y₀)}`, and
`Nm²y₀² = 1` balances the two halves. The sign here is the retained project's, `[0]⁺ = +L(E,1)/ω₁`;
PARI's `mseval` uses the opposite one.)

**Truncation.** With `|a_n| ≤ d(n)√n` and `Σ_{n≤t} d(n) = t log t + (2γ−1)t + O(t^{1/3})`,

    Σ_{n>X}(|a_n|/n)e^{−λn} ≤ (log X + 2γ + 2/(λX))·X^{−1/2}e^{−λX}/λ + O(X^{−1/6}e^{−λX}),
    λ = 2π/(121√N) = 6.4392·10^{−10}.

Each symbol uses two `c`'s, so identification in `(1/1024)Z` needs `2·tail < ω₁/2048`, i.e.
`tail < 6.85·10^{−6}`. The run used `λX = 25`, `X = 3.882·10^{10}` (coefficients generated to
`4·10^{10}`), giving `tail ≤ 2.9·10^{−6}` — margin 2.4. Floating point: Kahan summation per bucket
bounds the accumulated rounding error by `≈ 5·10^{−16}·Σ_n |a_n|n^{−1}e^{−λn} ≈ 7·10^{−10}`, i.e.
`2.5·10^{−8}` after division by `ω₁`.

**Observed:** every one of the 110 values at denominator 121 (and at 49, 25, 11, 7, 5) came out
within **`8.2·10^{−11}`** of an *integer* — identification window `1/2048 = 4.9·10^{−4}`.

**Cost, measured on this machine (8 cores, 64 GB).** `a_p` by PARI 2.17.2 `Fl_elltrace` on the
short model: 18 µs at `10⁶`, 34 µs at `10⁸`, 50 µs at `10⁹`, 90 µs at `10¹⁰`, 118 µs at `3.8·10¹⁰`,
with linear 8-way scaling. All `1 711 955 433` primes below `4·10^{10}`: ≈ 45 core-hours, done in
one pass of 400 chunks. Downstream: 2 min to build the prime bitmap/rank index; **310 s** for the
single segmented pass over `n < 4·10^{10}` that reconstructs `a_n` multiplicatively and accumulates
the bucket sums for `m ∈ {1,5,7,11,25,49,121}`; seconds for the cosine transform and assembly.
Storage 6.9 GB (`a_p`) + 2.5 GB (bitmap). So the dominant cost is the coefficient stream, and the
number of symbols extracted is irrelevant to it.

Code and data: `scripts/c11/` (`apgen.c`, `buildidx.c`, `stage2.c`, `stage3.py`, `run_ap.sh`,
`buckets_final.txt`, `symbols_seed.json`).

## 3. Checks passed

| check | outcome |
|---|---|
| `Fl_elltrace` vs PARI `ellak` | all 168 primes `< 1000`, and samples at `10⁶, 10⁹, 10^{10}, 4·10^{10}` |
| prime count: `ap.bin` length vs an independent sieve | `1 711 955 433` both ways |
| bucket sums vs an independent `ellan`-based computation | agree to `3·10^{−16}` at `X = 10⁷` |
| symbol formula vs PARI exact `mseval` | `37a1` and `389a1` at `m = 121` (110 values each), `389a1` at `m = 25`, `11a1` at `m = 7`: no mismatch, both root numbers, primitive and imprimitive components |
| `m = 1` bucket sum `= L(E,1)/2 = 0` | `3.4·10^{−13}` |
| retained `p = 5` certificate: the 20 symbols `[b/25]⁺` | reproduced exactly: `(−54, 16, 90, −52, −76, 16, 76, −52, −54, 90, 90, −54, −52, 76, 16, −76, −52, 90, 16, −54)` |
| retained `p = 5` certificate: `a_{2,2} ≡ 2 (mod 5)`, `ord₅ = 0` | reproduced |
| retained `p = 7` certificate: group sums `−165, −512, 314` | reproduced exactly |
| retained `p = 7` certificate: `[T²]L₇ ≡ 1 (mod 7)` | reproduced (`SeedC11.C_seven_value`, Lean) |
| rank-2 consistency at `p = 11`: `[T⁰]P = 0`, `[T¹]P ≡ 0 (mod 11)` | both hold |
| folded formula vs full depth-one assembly (level-11 terms kept, Hensel-lifted `α` mod `11⁶`) | both give `8` |
| truncation stability | identical integers at `X = 2.28·10^{10}` and `X = 3.88·10^{10}` |
| depth independence of `[T²] mod p` | checked on `389a1` at `p = 11` (depths 1 and 2 agree) |

## 4. Custody and caveats

* The symbols are produced by a **new** pipeline written in this session, not by the retained Arb
  engine, which was not available here. Its arithmetic trust base is PARI 2.17.2 (`Fl_elltrace`),
  glibc `exp`/`cos`, and the error budget above — **double precision with explicit bounds, not
  interval arithmetic**. The observed `10^{−11}` distances give seven orders of margin over the
  identification threshold, but this is weaker custody than an Arb ball.
* That the symbols lie in `(1/1024)Z` is a **retained project input** (`v₂(c₀) ≤ 8`, DERIVED). All
  computed values are in fact integers, which is consistent with, and stronger than, that lattice.
* `ω₁ = 0.028044901519436404448309401807930384171` was recomputed with PARI and agrees with the
  retained certified value to all printed digits.
* `w = +1`, the bad-prime `a_ℓ` values `(0, −1, +1, 0, −1)` at `(2, 3, 2243, 4547, 5843)` and the
  conductor are retained inputs, independently reproduced by PARI here.
* `[T²]L₁₁ ≡ [T²]P (mod 11)` for the depth-one approximation is Stein–Wuthrich Prop. 3.5, used as
  in the retained 7-primary run; it is not re-proved here. The empirical depth-1/depth-2 agreement
  on `389a1` is a check, not a proof.
* The pipeline has not been independently re-implemented. Its strongest external evidence is that
  it reproduces, value by value, two retained certificates (`p = 5` and `p = 7`) that were produced
  by different software.

## 5. What this does and does not settle

It supplies the arithmetic certificate the review asked for, and it is nonzero, which is the
favourable outcome: the 11-primary sufficient test **passes**. Completing `Ш[11^∞] = 0` from it
needs the retained chain — Kato's good-ordinary divisibility, Stein–Wuthrich Thm 6.1 and 7.3, the
`ε₁₁ = (1−α^{−1})²` unit check, and the regulator-integrality argument with the multiplier 28 —
exactly as recorded for `p = 7`; none of that is formalised here.

It does not prove finiteness of `Ш`, does not bound `#Ш` (in particular not below 1089), does not
control any prime other than 11, and says nothing about `q = 36`.
