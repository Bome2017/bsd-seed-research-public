# Independent review and continuation

Primary status: KATO_DERIVATIVE_CONTENT_BOUND_DERIVED_CONDITIONALLY.
Endpoint effect: no actual prime settled; FIN, ORDER9 and Q36 unchanged.

Read REPORT.md, CONTENT_BOUND_PROOF.md and SOURCES.md, then the bound predecessor inputs in context/. The new arithmetic conclusion to audit is

    length_Zp Sha[p∞] + w_p <= min(v_p(A_p),v_p(B_p)),

for nonzero actual derivative on D. It is not a claim that the right side has been bounded uniformly.

## Audit in this order

1. In the actual n-by-(n+1) free presentation, prove the signed maximal minors equal d eta for an integral kernel basis eta; identify d with the characteristic factor without losing eta's nonunit coordinate ideal.
2. Use the all-height-one Kato inequality, including (p), to obtain d=Ud1 with d1 dividing g when y=g eta and delta is nonzero.
3. Check that the first derivative of every maximal minor is divisible by the product of the nonzero Z_p Smith factors of D(0). Check invariance of content under the constant changes of basis and saturation of ker D(0).
4. Derive the compact/discrete finite-S Poitou–Tate segment from the finite-coefficient sequence. Check the self-dual twist and all local terms. In particular do not silently identify H² torsion with Sha.
5. Check the exact local correction: localization of the rank-two point group has divisible kernel plus a cyclic group of length w_p. With nonzero delta supplying primary finiteness, prove tors H² has length length Sha+w_p.
6. Use Cassels–Tate only after finiteness to conclude that m_p-w_p<=1 forces vanishing. Check that supersingular primes remain included.

The controls in checks/ are finite algebra tests, not a proof of items 1–6 and not seed cohomology computations. No new agents or Aristotle job are authorized by this handoff itself.

## Continue only on the actual missing arithmetic

If the new bound survives review, the source-matched correlated target is VALUATION_TARGET.md, not strict primitivity. At ordinary nonsingular matched primes it is

    v_p(K_p)+c_p-r_p-w_p <= 2,  K_p != 0.

A continuation must supply new arithmetic control of this expression or of the original derivative content; deriving it again is not a new BSD step. Preserve the fixed source, smoothing and all exception sets. A finite sample does not establish the cofinite claim.

The p17 residue in the user review is accepted only under exact source/height conventions. It supplies no value for K17. The fixed-source cofinite normalization does not certify 17 individually; its proposed smoothing excludes 5.
