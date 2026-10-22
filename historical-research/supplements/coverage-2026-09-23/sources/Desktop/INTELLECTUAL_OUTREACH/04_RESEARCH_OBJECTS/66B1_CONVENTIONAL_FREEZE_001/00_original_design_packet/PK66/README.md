# 66b1 design packet

Pre-research packet. Start with `TASK.md`.

    01_target/              the curve, the proposed descent model, the proposed prime family,
                            and the pre-registered Selmer prediction — hypotheses, labelled as such
    02_literature/          exact excerpts: Zhai's normalization definition and Theorems 1.3/1.4/1.7;
                            Banwait-Huang Definitions 2.1-2.3, Theorem 2.5, the 2-part conditions,
                            the normalization remark, Remark 2.15, Theorem 2.13;
                            BSTW Theorem 10.12, Remark 10.13, Example 1
    03_arithmetic_receipts/ dependency-free point-count script and its output — corroboration only
    04_62a1_reference_only/ a mechanism capsule from a finished, unrelated-in-status piece of work,
                            marked reference-only: do not assume portability
    05_prior_art_risk/      Nam 2018 coverage by isogeny class, risk flags, other theorem families
                            checked, and the positive-discriminant warning

## Why this packet exists

66b1 has **positive** discriminant. The finished work on 62a1 depended on that curve's discriminant
being negative, so its period bookkeeping does not carry over. Getting the analytic normalization
wrong here would silently corrupt everything built on top of it. Question 1 of `TASK.md` is
therefore gating, and a proposed answer to it has been withheld on purpose.

## Status of every claim in here

| section | status |
|---|---|
| `01_target` §1, curve data | established (Cremona/LMFDB rows) |
| `01_target` §2, descent model | proposed; the change of variables is **not** supplied |
| `01_target` §3, prime family | hypothesis |
| `01_target` §4, Selmer prediction | hypothesis, recorded in advance |
| `02_literature` | verbatim excerpts, machine-extracted and lossy |
| `03_arithmetic_receipts` | computation over primes below 4000; corroboration, not proof |
| `04_62a1_reference_only` | a finished result about a **different curve** |
| `05_prior_art_risk` | verbatim from a 2026-08-22 prior-art audit |

Nothing in this packet is a theorem about 66b1. No descent has been carried out for 66b1.
