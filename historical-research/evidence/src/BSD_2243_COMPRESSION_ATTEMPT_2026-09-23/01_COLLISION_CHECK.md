# Collision check: what earlier work already did with the depth-2 sum (2026-09-23)

**Purpose** (from your instruction): identify the additional relation that changes what the earlier trace-only calculations could determine, and do not repeat those calculations under new notation.

The check covers the local research tree only. **It makes no novelty claim** about the literature.

## Found on disk

| where | what it does | relation used | collides with this attempt? |
|---|---|---|---|
| `BSD_SEED_2243_12_FULL_BSD_LANE3_2026-09-18/D_primes/01_GATES.md` §3 | derives the depth-2 test Σ_b C(j_b, 2)[b/p²]⁺ for ordinary p ∤ N, with j_b ≡ −q_p(b) (Fermat quotient) | **U_p fibre traces only**: the [b/p]⁺ part drops because Σ_j C(j,2) = C(p,3) ≡ 0 (mod p) | yes, this is "the trace-only calculation". At 2243 the same argument, with weight C(j,3) and Σ_j C(j,3) = C(p,4) ≡ 0, gives the retained formula. **Not repeated**: 02 §2 only states its content (Lemma T: traces fix row sums, hence only c₀) |
| same file §3, p = 5 check | the merged six-symbol formula | same trace argument | same as above |
| `BSD_BAD_PRIME_MULT_FEASIBILITY_2026-09-22/REPORT.md` §2 | the **scalar mode** a_{2,j} = Σ_k S_k·W_j(k): full aggregation to one weighted sum. It notes "the truncation is set by the kernel e^{−κn}, not by how many symbols are extracted" | none (linear aggregation) | **partial.** Aggregation route R6 in 02 is only the intermediate point, to p + 2 column-class sums. Its cutoff, 4.62·10¹³, lies between per-symbol (3.91·10¹³) and scalar (6.8–7.0·10¹³). Recorded as a by-product, not as a new route |
| same report, table row "cusp formula … W_Q"; `S5_pipeline/CODEX_CHECK_REQUEST.md` item on re/im signs | the unitary-cusp evaluation formula, which uses W_Q to balance the two halves of the integral (sign s = −w·a_p) | **W_Q, used as an evaluation device** | the symmetry itself is already inside the engine's formula. Its **consequence on the certificate polynomial** (column map j ↦ −L − j, parity in W = T(1+T)^{−1/2}, which coefficients it fixes) was not derived anywhere. That consequence is new relative to disk, and it is the relation this attempt tests |
| definite-theta / Gross-point work (`~/BSD_DEFINITE_FIELD_GATE_2026-09-22/`, `~/BSD_TWIST_SHA_SUPPORT_2026-09-22/`) | distribution relations for quaternionic theta elements | Gross-point norm relations | no; a different object (supersingular/definite branch), not modular symbols at denominator p² |
| `BSD_ARISTOTLE_TAIL_COMPRESSION_2026-09-22/` | asks whether I₃ is the mod-p reduction of a fixed p-independent object (tail finite support) | none applied | no; a different question, and no computation was authorized there |
| pilot-prep S1–S5, evaluator review | the certificate formula, normalization and engine; no rewrite of the sum | — | no |

## Conclusion

* **The earlier calculations used exactly one relation, the U_p trace.** It fixes the row sums of the depth-2 symbol matrix (fibres of reduction mod p), so by itself it determines only c₀.
* **The additional relation that acts on the wild (Fermat-quotient) coordinate is the W_Q Atkin–Lehner pairing** x_{u_b} = s·x_b, u_b = (Qb)^{−1}. It is already implicit in the engine's evaluation formula, but it was never applied to the certificate polynomial.
* 02 §3 derives exactly what it fixes: the even W-coefficients. c₃ stays free.
* Nothing in the table is recomputed in this attempt.
