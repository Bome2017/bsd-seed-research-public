# Bounded feasibility check: the recorded multiplicative-prime routes at 2243 (split) and 5843 (non-split)

Date 2026-09-22. Read-only on every sealed artifact. Nothing was launched. The only computations were:
* the implementation's own exact truncation planner (`arbcore tmin`);
* PARI local data, p-adic regulators and the L-invariant (seconds each);
* throughput measurements on one production-size segment (2²⁴ integers) at each target height;
* one timing and correctness check of a copy of the untrusted producer with enlarged BSGS buffers, built in this folder.

The stream core (`~/BSD_RIGOROUS_STREAM_CORE_2026-09-19/`) was not modified.

## 0. Verdict

**PRECISE UNMET PREREQUISITE. The route is not executable on this host at either prime.** Mathematically the route is
fully specified, and at each prime it reduces to one coefficient mod p (§1). The blocker is computational:
* **Size:** the certificate needs every Fourier coefficient a_n up to T ≈ 3.9·10¹³ (2243) and T ≈ 1.7·10¹⁴ (5843),
  per the implementation's exact planner. That is 2 600× and 11 400× the p = 3 run.
* **Cost:** measured throughput of the present producer/verifier gives ≈ 3.2·10⁵ / 1.9·10⁶ CPU-h as is. With a
  trivial, output-identical fix to the untrusted producer it gives **≈ 1.2·10⁵ / 6.3·10⁵ CPU-h**, about **1.1 / 6.1
  years** of this host (§4).
* **Engineering:** three pieces of the pipeline do not transfer at these sizes (§2).

At the theorem level, 5843 stands exactly where p = 3 stands (Skinner Thm A as published, with the R2-type period
seam). 2243 additionally needs the split-case clause of SW Thm 6.1, which R1 did not cover (§3).

## 1. The exact certified quantity (one coefficient per prime)

Local data (PARI; seed model is minimal):

| p | type | a_p | c_p | v_p(Δ) | in K = Q(√−7) | p-adic regulator (PARI, minimal model) | L-invariant |
|---|---|---|---|---|---|---|---|
| 2243 | I₁ **split** | +1 | 1 | 1 | inert | v_p(Reg_p) = 2 ⇒ Reg_γ = Reg_p/log(κ(γ))² a **unit** | v_p(log_p q_E / v_p(q_E)) = 1 ⇒ ℒ/log κ(γ) a **unit**; ℒ ≠ 0 is known for elliptic curves (stated in Skinner 2016, read here; the underlying Saint-Étienne theorem was not read) |
| 5843 | I₂ **non-split** | −1 | 2 | 2 | inert | v_p(Reg_p) = 2 ⇒ Reg_γ a **unit** | — (ε_p = 2, a unit) |

Every other factor in the SW Thm 6.1 leading-term valuation is a p-adic unit at both primes: ∏c_v = 16,
#E(Q)_tors = 2. So SW Thm 6.1 (with the main-conjecture input of §3) makes the p-primary vanishing equivalent to the
unit status of one coefficient of the p-adic L-function:

    5843 (non-split, r = 2):   Sha(E/Q)[5843^inf] = 0   <==   a_2 is a 5843-adic unit
    2243 (split, order r+1 = 3): Sha(E/Q)[2243^inf] = 0   <==   a_3 is a 2243-adic unit

**Depth two suffices.** By SW Prop 3.5 (read at source, SW 2013 §3): ord_p(a_j − a_{n,j}) ≥ e_{n−1,j} − max(c_n, c_{n+1}),
with e_{n−1,j} = n − 1 for j < p. The symbols are p-integral (c = 0): every cusp b/p^k is Γ₀(N)-equivalent to the
rational cusp 1/p, and the identification lattice is (1/1024)Z. Hence a_j ≡ a_{2,j} (mod p). The quantity is

    a_{2,j}  =  α^{-2} Σ_{b ∈ (Z/p²)^×} [b/p²]⁺ · C(ℓ(b), j)   (mod p),     α = a_p,   j = 2 (5843) or 3 (2243),

where ℓ(b) is the discrete log of the 1-unit part of b to base κ(γ) mod p², and [b/p²]⁺ = Re λ(b/p²)/Ω⁺ with
Ω⁺ = ω₁. This is a single linear functional of the p² − p depth-two plus symbols.

**If the coefficient is divisible by p**, the sufficient test fails and nothing is established. Depth three would
be needed; the planner's T scales like p^{k−1/2}, so that multiplies T by p (≈ 2 243× / 5 843×).

*Correction, same day, after review.* An earlier version said a p-divisible coefficient "would actually prove
Sha[p^∞] ≠ 0" and that the computation was "decisive either way". That converse is **not** part of the retained
sufficient test and is **withdrawn as a claim**. It would additionally need all of the following to be checked:
* Skinner's equality at its exact normalization, including the R2-type period seam;
* exact order and finiteness;
* the normalization of every factor;
* the regulator-unit input.

The certified deliverable is the one-directional statement: coefficient a unit ⇒ Sha[p^∞] = 0.

## 2. What transfers from the completed machinery

| component | transfers? | evidence |
|---|---|---|
| cusp formula for M = p ∥ N: Q = N/p, κ = 2π/(m√Q), u_b = (Qb)⁻¹ mod m, W_Q | **yes**, generic in M | `DESIGN.md` O3; `gcd(Q, m) = 1` holds for m = p² |
| sign s = −w·a_M | **yes** as a derivation (s = ε_Q = w/w_M, w_M = −a_M). **Validated only at M = 3** (5 curves) | `P3_RUN_PLAN.md` §2. Cheap prerequisite: validate at a split and a non-split M ≥ 5 on small curves |
| exact truncation planner `arbcore tmin` | **yes** (it reproduces the recorded m = 81 value 14 832 175 873 exactly) | this folder, planner output |
| independent verifier `wverify` (integer only, u128 mulmod) | **yes**, unchanged | measured at q ≈ 3.9·10¹³: identical-format output, 43.9 µs/prime |
| untrusted producer `apwit` | **yes, but** its fast BSGS path switches off above q ≈ 4·10¹² (`fastap.c` `MAXM 2048`), so every prime falls back to PARI `Fl_elltrace` | measured: `fast 0 pari 536236` at 3.9·10¹³. The producer is outside the trust base and may be sped up freely (§4) |
| a_q storage (int32 per prime, plus 27-byte witnesses) | **no**: 1.3·10¹² primes means ≈ 5 TB of a_q and ≈ 35 TB of witnesses (2243); ≈ 4× that for 5843. About 140 GB is free | the pipeline must become produce → verify → consume with hash chaining and no retention |
| `msl` class-sum design (every work unit stores all m class sums; symbols by a direct cosine sum) | **no**: m = 5.0·10⁶ / 3.4·10⁷ with ≈ 2.3·10⁶ / 1.0·10⁷ Part-L units gives unit output of order 10¹⁴–10¹⁵ balls, and the direct cosine sums cost m·φ(m) ≈ 2.5·10¹³ / 1.2·10¹⁵ ball ops | `arbcore.c` l.203–237, 355–383. Needs a redesign in the trust base, with re-validation (below) |

**Does evaluating the one quantity avoid reconstructing every symbol? Yes for storage and assembly, no for the
dominant cost.**
* **What it saves:** a_{2,j} = Σ_k S_k·W_j(k), with W_j(k) = α⁻²Σ_b C(ℓ(b), j)[cos(2πkb/m) + s·cos(2πk·u_b/m)]/Ω⁺
  precomputed once. Folding W_j into the stream gives one scalar accumulator per thread, with no m-vectors and no
  symbol reconstruction.
* **What it cannot save:** the truncation is set by the kernel e^{−κn}, not by how many symbols are extracted, so
  every a_n up to T is still needed.
* **What it costs:** identifying a weighted sum needs a tighter tail, because the weight mass is about p³/4. The
  planner gives T = 6.99·10¹³ (2243) and 3.15·10¹⁴ (5843), 1.79× and 1.86× the per-symbol T_min.
* **The alternative:** per-symbol identification at T_min, with one m-vector per thread (241 MB at 2243; 1.6 GB at
  5843, so at most about 6 threads in 16 GB) and an FFT for the cosine sums.

Either variant is a trust-base engine change and must be re-validated against exact symbols on small curves.

## 3. Theorem dependencies (read at source this session where marked)

**Main-conjecture input.**
* **Skinner 2016 Thm A covers p | N** (source, l.67–80): p ≥ 3, ordinary (which forces p ∥ N and k = 2), ρ̄
  irreducible, and some q ≠ p with q ∥ N and ρ̄ ramified at q. Here q = 3 works (v₃(Δ) = 2, p ∤ 2), as does the other
  multiplicative prime. Both 2243 and 5843 satisfy it, split and non-split alike.
* **Kato's divisibility is not available at p | N.** Skinner says so explicitly: "this case is excluded from Kato's
  divisibility theorem [2004, Theorem 17.4]", l.74–77. SW 2013's "Kato's Theorem 7.3" states the divisibility for
  semistable p, but for non-split p | N it cites no source beyond Kato 17.4. For the split case it cites Kobayashi
  2006, which has not been read.
* **So the one-sided shortcut** (enough for vanishing, and avoiding Skinner's equality) is **unsupported at 5843** and
  **source-pending at 2243** (Kobayashi 2006).
* **Via Skinner, both primes inherit the R2-type seam recorded at p = 3.** The canonical-versus-Néron/Gross period
  comparison behind SU Prop 12.3.6 is in print (Kim–Ota 2023) only for p ≥ 5 **with p ∤ N**. At 2243 and 5843 the
  available stance is the same as the retained 3-primary theorem: "Skinner Theorem A as published; internal
  provenance open at the Euler-removal interface" (`MASTER_BSD_DAG.md` l.64–90).

**Other inputs:**
* **SW Thm 6.1** (source): ord_T f_E ≥ r; equality iff the height is nondegenerate and Sha(p) is finite; leading-term
  valuation as in §1. The split case replaces ε_p by ℒ_p/log κ(γ).
  * *Non-split (5843):* Jones's formula; R1 passed for it.
  * *Split (2243):* the Jones/split clause was **not** covered by R1, whose review "confirms the nonsplit Jones
    formula". **This is an open source item for 2243 only.**
* **p-adic regulator normalization:** SW §4.2 uses the corrected MTT/Werner height, and in the split case the Tate
  uniformization.
  * *5843:* PARI's multiplicative path agreed with an independent integrality-characterized height at p = 3 (C1).
  * *2243:* the split case has no such independent check yet. **Prerequisite:** an independent split-case height
    check at 2243 (cheap).
* **ρ̄_p surjective** (Sage `non_surjective() = [2]`, computational grade), and hence ρ_p surjective for p ≥ 5 (SW Prop
  7.2). **Rank 2 with saturated generators** (Zywina, merged). The **(1/1024)Z lattice** and **p ∤ c₀** are the same
  theorem inputs as at p = 3; Mazur gives p ∤ c₀ for p ∥ N.

## 4. Cost supported by the present implementation (measured, not modelled)

**How the numbers were obtained.**
* **Rates:** measured single-threaded on this host, one full production segment (2²⁴ integers) at each target
  height: 536 236 primes at q ≈ 3.912·10¹³ and 512 351 primes at q ≈ 1.687·10¹⁴.
* **Integration:** each producer rate is fitted as a + b·q^{1/4} through its two points and integrated over all
  primes q ≤ T (`cost_model.py`, outputs `cost_*.txt`).
* **Verifier:** the recorded verifier model, which matches the measured 43.9 µs at 3.9·10¹³. It measured 54.4 µs at
  1.7·10¹⁴ while running concurrently.
* **msl:** the measured p = 3 rate of 7.3·10⁻⁷ CPU-s per n. This is a lower bound, because the cache behaviour at
  large m was not measured.
* **Wall time:** 16 workers, times the ×1.35 hyperthreading factor observed in the p = 3 run.

| producer | per-prime cost (measured) | 2243, per-symbol T_min | 5843, per-symbol T_min |
|---|---|---|---|
| **present, as is** (fast path off above ≈4·10¹²) | 1.061 ms @ 3.9e13; 1.534 ms @ 1.7e14 | **3.2·10⁵ CPU-h** (≈ 3.1 yr wall) | **1.9·10⁶ CPU-h** (≈ 18 yr) |
| **present + buffer fix** (`MAXM 16384`, `HBITS 15`; untrusted; **identical verified a_q**: ap_sha256 `a3258307…`, `4e91237c…` match) | 0.321 ms; 0.446 ms | **1.17·10⁵ CPU-h** (≈ 1.1 yr) | **6.3·10⁵ CPU-h** (≈ 6.1 yr) |
| single-functional route (T ≈ 1.8×), with the fix | same | 2.3·10⁵ CPU-h (≈ 2.2 yr) | 1.3·10⁶ CPU-h (≈ 12.7 yr) |

The work is dominated by the producer (≈ 80%), then the verifier (≈ 10–13%), then msl (≥ 5–7%).

**How these compare with the recorded figures.** The retained ledger's architect estimates (≈ 2·10⁴ / ≈ 10⁵ CPU-h;
`FIN_FRONTIER.md` §4, "not re-derived") are **≈ 6× too low** even after the producer fix. The crude p²·√N scaling I
noted earlier in the session was **≈ 25× too high**, because the exact planner has T ∝ p^{3/2}·√N at depth two, not
p²·√N. Neither earlier figure should be used.

**Levers not measured here.** A GPU or SIMD BSGS, extra 2-power structure from the rational 2-torsion, or an external
cluster would all help. For scale, 1.17·10⁵ CPU-h is about 1 000 cores for 5 days. Whether to buy that is an economic
decision and is not made here.

## 5. The precise unmet prerequisites

**Compute:**
* **U1.** Verified a_q for every prime ≤ 3.912·10¹³ (2243) / ≤ 1.687·10¹⁴ (5843). That is ≈ 1.2·10⁵ / 6.3·10⁵ CPU-h
  with the fixed producer, and not feasible on this host (≈ 1.1 / 6.1 years).

**Engineering:**
* **U2.** Streaming pipeline (produce → verify → consume, hash-chained, no a_q or witness retention). About 5 TB and
  35 TB would otherwise be needed for 2243; 140 GB is free.
* **U3.** msl redesign for m = 5·10⁶ / 3.4·10⁷: either a functional accumulator, or per-thread m-vectors plus an FFT.
  This is a trust-base change, and must be re-validated against exact eclib symbols on small curves.

**Validation and theorem items:**
* **U4.** Sign rule s = −w·a_M validated at a split and a non-split M ≥ 5 (small curves).
* **U5 (2243 only).** An independent check of the split-case p-adic height normalization (SW §4.2 / Werner). A source
  read of the split clause of SW Thm 6.1 (Jones), which R1 did not cover.
* **U6.** The main-conjecture stance: either accept "Skinner Thm A as published" (the p = 3 stance, with the R2-type
  period seam open at p | N), or supply a one-sided divisibility at p | N.
  * *2243:* read Kobayashi 2006 at source.
  * *5843:* no source is located.

**Cheap and executable now, all read-only or small-curve:** U4, U5 and the Kobayashi 2006 read. None of them settles
a prime. **Nothing about the certificate itself is executable on this host.** The next decision is external compute
(U1) plus the engineering in U2–U3, or holding this lane.

## 6. Addendum (same day): the nonzero-only stopping test, budgeted with the existing planner

**Criterion** (the reviewer's form). K_p = 1024·Z_p ∈ Z, with Z_p = Σ_{b mod ±1} bal_p(2·C(ℓ(b), r))·[b/p²]⁺. A
sufficient certificate is [1024L, 1024U] ∩ pZ = ∅ for an enclosure Z_p ∈ [L, U]. Its best-case radius ceiling is
R < p/2048.

**Weight totals, reproduced here.** W₂₂₄₃ = 1 397 925 114 and W₅₈₄₃ = 24 711 283 191. The fiber formula
((p−1)/2)·Σ_j |bal_p(2C(j,r))| was checked against brute-force enumeration at p = 13.

**2243 local data, reproduced here with PARI's Tate path.** q_E ≡ 4 521 378 839 (mod 2243³), v(q_E) = 1, and
ℓ_γ(E) ≡ 1799 (mod 2243).

**Screen.** Triangle bound |error(Z_p)| ≤ W_p·δ(T), with δ(T) = 2·tail_MS(T)/Ω⁺. The condition W_p·δ(T) < p/2048 maps
to the planner with LATDEN = ⌈1023·W_p/p⌉. The rounding is conservative, and it moves T by < 10⁻⁸ relative.

| | per-symbol exact (LATDEN 1024) | **nonzero-only screen, best case** | same, idealized Parseval-floor weight bound (optimistic) | exact scalar identification |
|---|---|---|---|---|
| 2243: T | 3.912·10¹³ | **5.741·10¹³** (1.47×) | 4.704·10¹³ (1.20×) | 6.798·10¹³ (1.74×) |
| 2243: CPU-h (fixed producer) | 1.17·10⁵ | **1.82·10⁵** | — | 2.21·10⁵ |
| 5843: T | 1.687·10¹⁴ | **2.566·10¹⁴** (1.52×) | 2.075·10¹⁴ (1.23×) | 3.066·10¹⁴ (1.82×) |
| 5843: CPU-h (fixed producer) | 6.35·10⁵ | **1.04·10⁶** | — | 1.27·10⁶ |

**Early stopping saves ln(p)/η over exact scalar identification.** That is 1.06·10¹³ at 2243 and 5.0·10¹³ at 5843,
matching the additive-shift prediction.

**The result.** Even the idealized weight bound (Parseval floor, W_p/F ≈ 1928 / 5049) leaves the scalar screen
**above** the per-symbol T_min. Identifying each symbol exactly at T_min is therefore the cheapest stopping rule, and
it also yields K_p exactly. The scalar's only advantage is O(1) memory per thread. At 2243 memory does not bind: the
class-sum vector is ≈ 121–241 MB. Early stopping cannot rescue the scalar evaluator.

**Tooling note.** `arbcore tmin` does not guard LATDEN ≥ 1, unlike msl mode. A bad argument (0) makes it loop, as
happened once here through a script parsing error. The core was not modified.
