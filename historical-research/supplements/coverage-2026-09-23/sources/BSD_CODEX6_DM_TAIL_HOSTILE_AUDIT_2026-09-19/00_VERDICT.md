# Destrempes–Malinin tail theorem: hostile audit verdict

**DM_TAIL_THEOREM_FAILS_AT_THEOREM_6_STEP_2_TRACE**

The proof does not establish a uniform Sha-vanishing tail for the seed. Its essential intermediate lifting statements are false, and the error is not a missing small-prime hypothesis.

## Exact failure

In Theorem 6, Step 2, printed pages 29–30, the inference from equation (135) to (137) uses

    α₀ ∈ 𝔓,  𝔓 | p  ⇒  Tr(Lₙ/Q)(α₀) ∈ pZ.

That implication is false. In Q(i), the element 4+i lies in the prime ideal (4+i) above 17, but its trace is 8. The global trace sums over all primes above p; the hypothesis controls just one.

There is also a direct contradiction in the paper's actual full-image torsion-field setting: at a completely split division-field prime, (137) would force all nonzero ell-torsion points to have the same squared y-coordinate. There are ell²−1 such points but at most six points with any specified nonzero squared y-coordinate. Thus special properties of the paper's α₀ cannot rescue its universal congruence.

Source: [arXiv:1703.02215v2, §3.4](https://arxiv.org/html/1703.02215v2#S3.SS4). The official HTML and retained PDF text agree at the defective step.

## Why this is not a routine repair

Two independent written proofs strengthen the diagnosis:

1. No finite set of algebraic points can lift all reduced ell-primary points as the auxiliary prime varies. This disproves Theorem 6's uniform bound as used to construct K′.
2. For any fixed finite number field F, there are infinitely many primes where every point of E(F) is locally divisible by ell but E(Q_p)/ell is nonzero. This disproves Proposition 10 itself. A strengthened version covers the residual Frobenius shape diag(λ,1) used later.

See [the proofs](/Users/bsm/BSD_CODEX6_DM_TAIL_HOSTILE_AUDIT_2026-09-19/TRACE_AND_FIXED_FIELD_OBSTRUCTION.md).

The failed dependency reaches Proposition 12 precisely at Step 6, its inclusion I⊆I′, via Proposition 11 and Corollary 10. Lemma 8's prime-selection argument, Sah's cohomology vanishing, prime-to-ell descent, and Sha[ell]=0 ⇒ Sha[ell^∞]=0 do not provide the missing arithmetic arrow. See the [step-by-step audit](/Users/bsm/BSD_CODEX6_DM_TAIL_HOSTILE_AUDIT_2026-09-19/PROOF_AUDIT.md).

## Seed and FIN status

The supplied short model and factor support are correct:

    4A³+27B² = −2⁴·3¹⁴·2243·4547³·5843².

The upstream full residual image does imply full ell-adic image for every ell≥5, including 11. Its determinant is cyclotomic and surjective. Thus the proposed set {7,13,2243,4547,5843} is correct **conditional bookkeeping for DM**, but it is not an established exhaustive set of remaining Sha primes. Details: [SEED_HYPOTHESES.md](/Users/bsm/BSD_CODEX6_DM_TAIL_HOSTILE_AUDIT_2026-09-19/SEED_HYPOTHESES.md).

**FIN remains open. Exact Sha order 9 remains unproved. No exceptional-prime Sha computation was run.** Existing small-primary results and their provenance qualifications are unchanged. No FORMULA work was undertaken.

## Prior record and search

The master had already rejected DM using 20806a1 at ell=11. The present work newly supplies an exact internal proof failure and broader lifting obstructions. Fresh primary-data checks corroborate the earlier example, but this session did not replay its exact modular-symbol L-ratio; the verdict does not rely on that imported step. See [COUNTEREXAMPLE_EVIDENCE.md](/Users/bsm/BSD_CODEX6_DM_TAIL_HOSTILE_AUDIT_2026-09-19/COUNTEREXAMPLE_EVIDENCE.md).

The bounded search located no independently documented repair or expert correction. Citation-index results were inconsistent and are not evidence for the verdict. See [SEARCH_LOG.md](/Users/bsm/BSD_CODEX6_DM_TAIL_HOSTILE_AUDIT_2026-09-19/SEARCH_LOG.md).

## Research gate

- **Endpoint:** FIN, and the exact-Sha input needed for FORMULA.
- **First failed arrow:** the trace inference leading to universal lifting.
- **New information:** impossibility proofs for finite universal lift sets and fixed-field universal local Kummer coverage.
- **Progress type:** no-go compression only; no new Sha regime closed.
- **Kill condition:** met. Do not repair this branch by assuming the false universal lifting statement, varying the field while retaining a fixed-field conclusion, or substituting a Selmer-specific assertion without an independent proof.
- **Stop:** this audit is complete; no automatic return to the interrupted invention experiment or another route.
