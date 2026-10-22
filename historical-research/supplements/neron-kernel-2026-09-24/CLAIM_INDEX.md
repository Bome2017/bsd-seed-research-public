# Neron-kernel supplement claim index

The three claims below are separately graded additions to the frozen v0.2.2 record. See [the mathematical addendum](paper/neron_kernel_addendum.pdf), [source ledger](DEPENDENCIES.md) and [machine-readable claims](CLAIMS.json). Original claim IDs refer to the [76-claim manuscript index](../../claims/CLAIM_INDEX.md).

## NK.1 — Good-prime unit scale of the Neron-normalized kernel

**Kind:** THEOREM. **Grades:** PROVED_WRITTEN, IMPORTED_PUBLISHED.

For the chosen seed map, K_E(z,w)=(ed/(c_E^2 M))*psi(z)*psi(w). For each prime p>=5 with p not dividing N, v_p(M)=v_p(d), hence ed/(c_E^2 M) is in Z_p^times.

**Dependencies:** A.1, A.3, A.4.

**Inputs:**
- Retained audited rank-one theta normalization and primitive f-line.
- Kim-Ota section 6.1, Theorem 6.5, Corollary 6.7 and explicit nonordinary adaptation Remark 6.6(1).
- Full Hecke/integral cuspform duality.
- Agashe-Ribet-Stein Theorem 2.1 for the optimal quotient.

**Evidence:**
- [Detailed unit-scale proof](sources/cloud/01_NORMALIZATION_REVIEW.md)
- [Retained theta normalization; only the stated input is imported](sources/lab-context/01_THETA_KERNEL.md)

**Qualifications:**
- No assertion p does not divide M or of a global equality M=d or M=r.
- The nonordinary crystalline adaptation remains a published import with a short justification not reproved here.
- A_E is complex period area, not the BSD real period or the Neron-Tate regulator.
- No seed kernel interval or M2 witness was computed.
- No new primary Sha component, FIN, ORDER9 or Q36 claim.
- A fixed denominator for p-dependent numerators is not a fixed integer controlling Sha prime support.

**Review:** cross-family model review at the linked scope; no human review or new Lean replay.

## NK.2 — Explicit reconstruction denominator for degree-zero theta packets

**Kind:** THEOREM. **Grades:** PROVED_WRITTEN, IMPORTED_PUBLISHED.

For z,w in Z[X] and deg(z)=0, G=Theta(z,w) has D0*omega_G in the Neron cotangent lattice, D0=2*4547. Hence B_theta*K_E(G) is in Z for B_theta=4656128. B_join=595984384 is a valid weaker multiplier.

**Dependencies:** A.1, A.4.

**Inputs:**
- Retained theta expansion via Poisson and local Gauss identities, Lemmas 4 and 4-prime.
- CNS Proposition 5.14 for general cuspforms, Proposition 6.2, Example 6.3, Theorem 6.12.
- Chosen map and retained c_E dividing 512.
- Whole 2-local inclusion 2^8 S subset H for the fallback only.

**Evidence:**
- [Detailed denominator proof; subject to TRANSFER_NOTES.md](sources/cloud/02_DENOMINATOR_LATTICE.md)
- [Chosen map and area identity only; the good-prime comparison is not needed for lattice membership](sources/cloud/01_NORMALIZATION_REVIEW.md)
- [Poisson and Gauss inputs in Lemmas 4 and 4-prime only](sources/lab-context/03_NELSON_CONTINUATION.md)

**Qualifications:**
- Requires an integral degree-zero first packet. Not asserted for a noncuspidal anchor diagonal or all integral cuspforms.
- One factor at 4547 is sufficient; minimality for the actual weighted forms is unproved.
- Manin bound retains its existing geometric dependency grade.
- No new independent computation of the general division-place Gauss identity.
- No seed kernel interval or M2 witness was computed.
- No new primary Sha component, FIN, ORDER9 or Q36 claim.
- A fixed denominator for p-dependent numerators is not a fixed integer controlling Sha prime support.

**Review:** cross-family model review at the linked scope; no human review or new Lean replay.

## NK.3 — Conditional integer witness and exact interval acceptance

**Kind:** CONDITIONAL. **Grades:** PROVED_WRITTEN, EXACT_COMPUTATION.

For the specified integral degree-zero lift z_p^0 of the conductor-p^2 Gross packet and good p>=5 not dividing 7N, n_p=B_theta*K_E(z_p^0,z_p^0) is an integer and p not dividing n_p iff M2(p) is nonzero, implying Sha(E/Q)[p^infinity]=0 by retained B.5.

**Dependencies:** NK.1, NK.2, B.5.

**Inputs:**
- Retained ordinary/supersingular forward bridge B.5.

**Evidence:**
- [Degree-zero relifting and acceptance deduction](reviews/pro6/AUDIT.md)
- [Exact finite checks and conditional interval_decision function](reviews/pro6/independent_checks.py)
- [Recorded independent 41925-case integer oracle](reviews/codex/ACCEPTANCE_CROSSCHECK.json)

**Qualifications:**
- Use Fraction endpoints and the stated multiplier; the arithmetic routine does not certify a seed enclosure or its provenance.
- Exact radius below 1/9312256 guarantees at most one integer after scaling; enclosure and membership supply existence.
- A wider interval may suffice if it contains an integer and no multiple of p. An empty lattice interval is inconsistent.
- An inconclusive or divisible witness gives no contrary Sha conclusion.
- No converse from Sha vanishing to M2 nonvanishing is supplied.
- No seed kernel interval or M2 witness was computed.
- No new primary Sha component, FIN, ORDER9 or Q36 claim.
- A fixed denominator for p-dependent numerators is not a fixed integer controlling Sha prime support.

**Review:** cross-family model review at the linked scope; no human review or new Lean replay.
