# RUN014-C2 — independent return audit (clean neutral mechanism-target assessment)

Auditor: local session, 2026-08-23. Original unmodified. Fresh extraction; clean Lean build.

## 1. Identity and polarity

Archive `11f52094…`, 70 members. Embedded input `b523a88b…` — byte-identical to the neutral
package built and audited earlier. `C2_ARCHIVE_IDENTITY = PASS`.

`C2_POLARITY = NEUTRAL`, re-verified on the returned copy: no "negative", "control",
"selectivity", expected outcome, named missing bridge, `FULL_BSD_ATTEMPT`, "does not
authorize", "proof gap", or `UNPROVED_HERE`. The package never told it what to conclude.

## 2. Validator and decision-log schema

```json
{"immutable_inputs":"PASS","manifest_entries":50,
 "decision_log_entries":10,"decision_log_schema":"PASS","package_result":"VALID"}
```

Independently inspected: all 10 entries carry all ten fields, non-empty, in vocabulary.
`ORIGINAL_AUTHOR` tally: `SOURCE` ×4, `ARISTOTLE` ×5, **`UNKNOWN` ×1** (entry 006). That
`UNKNOWN` is the discipline working — the instance declined to attribute a move whose
authorship it could not evidence, which is exactly what the pilot's logs failed to do.
`C2_PACKAGE_VALIDATOR = PASS`, `C2_DECISION_LOG_SCHEMA = PASS`.

## 3. Clean Lean build and scope

```text
BUILD = lake build -> 8028/8028 jobs, 1 m 45 s, success
```
Escapes scan of 221 lines: **none**. `C2_SORRY = 0`, `C2_ADMIT = 0`,
`C2_CUSTOM_AXIOMS = none`. `C2_LEAN_BUILD = PASS`.

`Run014Audit.lean` contains only finite, elementary fragments: `thirteen_mem_F62`,
`cardE_thirteen`/`traceE`, `phi_local_two_exclusion` (the mod-16 exclusion),
`dual_real_exclusion` (archimedean), `g_sq_mod_31` with `twentythree_nonsquare_mod_31`,
`g_no_root_mod_q`, `no_four_torsion`, the 2-part bookkeeping identity
`sha_analytic_eq_algebraic_L`, and the scope marker `seven_not_mem_F62`.

It formalizes **no** uniform-in-`q` theorem, **no** analytic nonvanishing, **no** BSD, and
**no** Selmer-to-L-function bridge. `C2_TARGET_SCOPE_PRESERVED = YES`.

## 4. The implication chain, hostile-checked

C2 returned `RETURN: NO` and built a step-by-step chain S1–S12, each labelled. Spot-checked
against the sources rather than accepting its labels:

* `PROVED_FROM_MECHANISM` — S1 (ambient `Q(S,2)`, `S = {2,31,q}`), S2 (the local images for
  every `q ≡ 5 (mod 8)` with `(q|31) = −1`), S3 (comparison/Kummer to `Sel_2`, rank 0,
  `Ш[2^∞] = 0`), S4 (torsion, Tamagawa, `Δ_min < 0`).
* `EXTERNAL`, and marked **located and read** — S5 (`L^alg(62a1,1) = 1/4`), S6 (Zhai,
  *Non-vanishing theorems for quadratic twists*), S7 (optimality / odd Manin constant, via
  Cremona), S10 (Kolyvagin with Gross–Zagier), S11 (the full BSD formula, from the
  odd-primary assembly).
* S12 (`F_62` infinite) — mechanism plus Chebotarev.

Its own replay scripts were re-run here and reproduce the mechanism independently:

```text
base_lvalue.py    L/Omega = 0.2500018...  (i.e. 1/4), calibrated on X0(11) and 37B1
descent_replay.py Sel^phi = {1,-31,q,-31q}, Sel^dualphi = {1} recomputed for family primes q < 250
twist_data.py     Delta = -2^4*31*q^6 -> True; c_2 = 2, c_31 = 1, c_q = 2; torsion | 4
isogeny_check.py  a_3(62a1) = 0; absolute-irreducibility witnesses for p = 3, 5, 7
```

## 5. Scope claim (claims 1–4)

```text
F62_STRONG_BSD_FROM_FULL_CHAIN = QUALIFIED
```

Claim 1 — strong BSD for `q ∈ F_62` — is reached **only by the mechanism together with
external theorems**, never by the mechanism alone. C2 states this itself and separates the
two ("what the mechanism itself proves, stripped of external help" is §3 of its report: the
Selmer identities, `Sel_2 ≅ Z/2`, rank 0, `Ш[2^∞] = 0`, `#E_q(Q)_tors = 2`, `∏ c_p = 4`).

External load-bearing inputs: the exact base algebraic L-value; Zhai's non-vanishing theorem
with its 2-adic valuation; optimality and odd Manin constant (Cremona); Kolyvagin with
Gross–Zagier for finiteness; and the odd-primary assembly for the full formula — which C2
notes is **an unpublished preprint**. The qualification is exactly that dependency.

Claims 2, 3, 4: `MISSING`. C2 refused all three.
`C2_FALSE_BRIDGE_REFUSED = YES`.

## 6. Selectivity — and one finding stronger than expected

The diagnosis was inferable from the package: the mechanism files and the literature were
supplied, the polarity was not. C2 located the analytic dependency itself, classified it
`EXTERNAL`, and declined to promote claim 1.

On claim 2 it went further than the pilot's B did. Rather than reporting "unproved", it
argued the statement is **false as stated for general `d`**: infinitely many twists have root
number `−1`, hence odd analytic rank and (under BSD) rank ≥ 1, so a uniform rank-zero
statement across all twists cannot hold. It then identified precisely which hypotheses the
mechanism consumes (`q ≡ 5 (mod 8)`, `(q|31) = −1` at the places `2, 31, q`; `ord_2 #E(F_q) = 2`
and prime `M` for Zhai) and observed that dropping any one kills both halves.

```text
C2_CRUX_DIAGNOSIS      = PASS
C2_BLIND_SELECTIVITY   = SUPPORTED
```

## 7. Limitation

One control, on a mechanism whose limits were already known to this operator. C2's own
prior-generation sibling (B) reached the same diagnosis *while told it was a control*; C2
reached it without that framing. That is the increment. It is a single instance and does not
establish selectivity as a general property.
