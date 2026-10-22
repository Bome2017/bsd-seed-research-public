# DESIGN: rigorous streaming L-series / modular-symbol core (Phase 0, written before any code; 2026-09-19)

## Objects enclosed

Throughout:
- E is given by integral a-invariants (a₁, a₂, a₃, a₄, a₆), in a model that is minimal at every bad prime. This is checked: v_q(Δ) < 12 at each bad q.
- a_n are the L-series coefficients.
- Every real number below is carried as an Arb ball [m ± r]. All constants are Arb-generated: π = `arb_const_pi`, γ = `arb_const_euler`, √N = `arb_sqrt_ui`.
- There is no `M_PI`, and no double constant enters any ball.

### O1. Fourier coefficient stream (exact integers)

**Primes.**
- a_p for primes p ≤ T comes only from the verifier's output table `apq_verified.bin`: one int32 per prime, in increasing order, with its SHA-256 printed.
- The verifier derives:
  - small primes (p < Q_B = 4096) and bad primes (p | Δ) by exhaustive point counting;
  - every other prime from a producer witness that it checks (O6).

**Prime powers.** a_{p^{e+1}} = a_p·a_{p^e} − p·a_{p^{e−1}} for good p; a_{p^e} = a_p^e for bad p.

**Composites.** a_n = ∏ a_{p^e} over p^e ‖ n.

**Hasse and Deligne-type bound.** |a_n| ≤ d(n)√n. This follows from Hasse (|a_p| ≤ 2√p good, |a_p| ≤ 1 bad) and a_{p^e} = Σ α^i β^{e−i} with |α| = |β| = √p. It needs neither Deligne nor any divisor-bound constant.

**Stream hash.** The engine and the verifier each compute an a_n Merkle SHA-256 independently:
- leaf b = SHA-256 of int64-LE a_n for n ∈ [b·2²² + 1, (b+1)·2²²] ∩ [1, T];
- root = SHA-256 of the concatenated leaves.

### O2. Second-derivative kernel (analytic rank)

For w = +1 and L(E,1) = 0 (hence L′(E,1) = 0):

    L″(E,1)/2 = 2 Σ_{n≥1} (a_n/n) G₂(c n),   c = 2π/√N,   G₂(x) = ∫₁^∞ e^{−xy} log y dy/y.

Sources: Cremona, *Algorithms*, §2.13 (Buhler–Gross–Zagier, r = 2); Lane 3 A2_FORMULA.md, re-derived by the referee.

Facts used (each proved in the report):
- **(G1)** G₂(x) = ½(log x + γ)² + π²/12 + Σ_{k≥1} (−1)^k x^k/(k²·k!). Derivation: F(s) = x^{−s}Γ(s,x) = ∫₁^∞ e^{−xy}y^{s−1}dy, and G₂ = F′(0).
- **(G2)** G₂′(x) = −E₁(x)/x and E₁′(x) = −e^{−x}/x. E₁ comes from `arb_hypgeom_expint(1, x)`.
- **(G3)** 0 < G₂(x) ≤ e^{−x}/x², since log y/y ≤ y − 1 on [1, ∞).
- **(G4)** Complete monotonicity: (−1)^k G₂^{(k)}(x) = ∫₁^∞ y^{k−1} log y e^{−xy} dy is positive and decreasing in x.

**Evaluation of G₂(x_n), x_n = c·n** (a ball; n exact):
- **x < X₀ = 1.** Direct series (G1). Stop at K ≥ max(2x, 4) once |term| < 2^{−prec−8}. The tail is bounded rigorously by 2·|t_{K+1}|, because the term ratio is x·k²/(k+1)³ ≤ x/(k+1) ≤ ½ for k ≥ K ≥ 2x.
- **x ≥ X₀.** Taylor models on nodes x_j = X₀ + j·H, with H = 2⁻⁸ and degree J = 12.
  - The coefficients g_{j,i} = G₂^{(i)}(x_j)/i! are computed EXACTLY as power-series algebra in balls: G₂(x_j) by (G1); the series of e^{−t}, 1/(x_j + t), E₁(x_j + t) and E₁/x by (G2).
  - Remainder, by (G4) with ξ ∈ [x_j − H, x_j + 2H]: |R| ≤ |g_{j−1,J+1}|·(2H)^{J+1}. Here g_{j−1,J+1} is the (J+1)-st coefficient at node x_{j−1} = x_j − H.
  - The per-n evaluation is Horner in balls at t = x_n − x_j, plus the ball [±R]. It is valid for t ∈ [−H, 2H]; the chosen j keeps t within [0, H] up to rounding.

**Truncation (proved in the report; no BBR constant):**

    tail_L2(T) ≤ 2 e^{−cT} [ 2√T/(cT)² + T^{−1/2}(cT)^{−2} ((log T + 2)/c + 1/(T c²)) ]

It rests on:
- |a_n| ≤ d(n)√n;
- partial summation;
- D(x) = Σ_{n≤x} d(n) ∈ [x log x − x, x(1 + log x)] (elementary, from H_n bounds);
- g(x) = x^{−1/2}G₂(cx), which is decreasing and bounded by x^{−1/2}e^{−cx}/(cx)² (G3).

**Output.** The ball 2·S_T ± tail_L2(T). Success means 0 ∉ ball.

### O3. Exponential kernel and residue-class modular-symbol sums (denominator m)

**Setting.** Unitary cusps b/m, with M = gcd(m, N), Q = N/M and gcd(Q, M) = 1.
- y = 1/(m√Q) and κ = 2πy.
- W_r gives Im(τ) = Im(W_r τ) = y (Wuthrich 2018, (8)).

**Class sums.** S_k = Σ_{n≤T, n≡k (m)} (a_n/n)·e^{−κn}, for k = 0..m−1, as balls.
- Kernel: w_n = e^{−κn} = w_{n₀}·q₁^{n−n₀}, with q₁ = e^{−κ} and w_{n₀} = `arb_exp`(−κn₀) recomputed at each block start. The recurrence error is carried by the balls.
- Symbols: Re λ(b/m) = Σ_k S_k [cos(2πkb/m) + s·cos(2πk·u_b/m)], with u_b = (Q·b)⁻¹ mod m. The cosines are exact rational multiples of π (`arb_cos_pi_fmpq`), so no π constant is needed.
- Im λ has the same form with sin and −s.
- The sign s is +w for M = 1 (validated: 37a1 with w = −1), and −w·a_M for M = 3 (Lane 3 D §1; for the seed, +1).

**Truncation (elementary, as in O2):**

    tail_MS(T) = Σ_{n>T} |a_n| n^{−1} e^{−κn} ≤ e^{−κT} [ 2√T + T^{−1/2} ((log T + 2)/κ + 1/(T κ²)) ]

Both series (λ(τ) and λ(W_r τ)) are truncated at T, so |error in Re λ| ≤ 2·tail_MS and |error in Im λ| ≤ 2·tail_MS.

**Normalized symbols.** x_b = Re λ(b/m)/Ω⁺.
- For Δ > 0 (all validation curves and the seed): Ω⁺ = ω₁ = π/AGM(√(e₁−e₃), √(e₁−e₂)), where e₁ > e₂ > e₃ are the roots of 4x³ + b₂x² + 2b₄x + b₆. The roots come from `acb_poly_find_roots`; 3 isolated roots means guaranteed enclosures.
- The minus period is Ω⁻ = π/AGM(√(e₁−e₃), √(e₂−e₃)). It is cross-checked against PARI `E.omega`; the formula is standard for rectangular lattices.

### O4. Constants

| constant | source |
|---|---|
| π | `arb_const_pi` |
| γ | `arb_const_euler` |
| √N, √Q | `arb_sqrt_ui` |
| log | `arb_log` |
| exp | `arb_exp` |
| cos, sin | `arb_sin_cos_pi_fmpq` |
| E₁ | `arb_hypgeom_expint` |
| AGM | `arb_agm` |

Working precision is 128 bits for streaming and 256 bits for node tables and ω₁. Every step is ball arithmetic; there is no heuristic error term.

### O5. Summation enclosure and determinism

- Each block (2²² consecutive n) is summed sequentially into its own ball. Block balls are combined in increasing block order after all threads join, so the result does not depend on thread count or scheduling.
- The block log is append-only. Each line holds: block, n-range, Merkle leaf, the number of nonzero a_n, and the partial ball, serialized exactly with `arb_dump_str`.

### O6. Coefficient witness (producer → verifier) for a good prime q ≥ Q_B

**Record:** q (u64), a (i32), x₀ (u8), k (u8), then k × (ℓ u64, e u8).

**Verifier checks**, using its own code (affine arithmetic, Euler's criterion, deterministic Miller–Rabin), on the short model over F_q with A₄ = −27c₄ and A₆ = −54c₆:
1. q equals the next prime of its own sieve. Segment [q_lo, q_hi) boundaries tile [Q_B, T], and the counts match.
2. a² ≤ 4q.
3. d = x₀³ + A₄x₀ + A₆ ≢ 0 and χ = (d/q). Set h = q + 1 − χ·a.
4. P = (d·x₀, d²) lies on E_d: Y² = X³ + A₄d²X + A₆d³.
5. [h]P = O.
6. For each (ℓ, e): ℓ is prime, ℓ^e | h, v = v_ℓ(h), and [h/ℓ^{v−e+1}]P ≠ O. Hence ℓ^e | ord(P).
7. D = ∏ℓ^e is greater than 2s, where s = ⌊2√q⌋ = isqrt(4q).
8. Exactly one multiple of D lies in [q+1−s, q+1+s].

**Conclusion.** #E_d(F_q) is a multiple of D (Lagrange) in the Hasse interval, so it equals h. Hence a_q = a, because E_d ≅ E when χ = 1 and E_d is the quadratic twist when χ = −1.

**Other primes.**
- Small and bad primes: a_q = −Σ_{x∈F_q} χ(4x³ + b₂x² + 2b₄x + b₆) for odd q; direct enumeration for q = 2.
- Minimality: v_q(Δ) < 12 is asserted at every bad q.

### O7. Rounding-mode assumptions

- Arb's ball arithmetic is exact-integer based (mpn mantissas, mag_t upper bounds). The engine never changes the floating-point environment, and it asserts `fegetround() == FE_TONEAREST` at start-up.
- No native double enters any enclosure. Doubles appear only in progress messages and in cost estimates.
- The verifier uses only integer arithmetic (`unsigned __int128` mulmod).

## Addendum (post-implementation, 2026-09-19): deviations and additions (the Phase 0 text above is unchanged)

- **O1 layout.** The verified a_q table is stored per segment, as `ap_<s>.bin` (one int32 per prime of [s·SEGQ, min((s+1)·SEGQ, T+1))), rather than as one `apq_verified.bin`. The verifier logs the SHA-256 of each segment. The engine recomputes these hashes and prints their root (`AP_SEGROOT_SHA256`).
- **O2 range guard.** For every term, the engine checks t = x − x_j ∈ [−H, 2H] with Arb lower and upper bounds before using the node's remainder bound. A violation is FATAL.
- **O3 table-free mode `msl`.**
  - Part S takes the √T-smooth n in natural order, by cofactor division.
  - Part L takes n = m·q with q > √T prime, streamed per a_q segment, and m ≤ √T. There a_n = a_m·a_q, since gcd(m, q) = 1.
  - The kernel is r_q = e^{−κq}, carried from the previous prime by an exact e^{−κg} table (g ≤ 4096, else `arb_exp`).
  - The count identity #smooth + #pairs = T is checked. RAM is independent of T.
- **O3 truncation planner `tmin`.** It gives the least T ≥ 1/κ with 2·tail_MS(T)/Ω⁺ ≤ (1 − 2⁻¹⁰)/(2·LATDEN), evaluated in Arb (tail_MS is decreasing for T > 1/(2κ)).
- **O3 identification output.** For each b, the engine prints the nearest point of (1/LATDEN)Z. It also prints `contains` (the ball contains that point) and `unique` (2·radius < 1/LATDEN, an exact test).
- **O5 custody.**
  - Work units are write-once and carry a SHA-256 self-hash ("END <hex>"), verified when read back.
  - `PARAMS` locks the command line (all arguments except W, including the outdir path).
  - Units are combined in a fixed order, so the output is independent of the thread count.
