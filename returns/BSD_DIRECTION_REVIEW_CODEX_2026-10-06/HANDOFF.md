# Corrections and next deliverables, not a launch instruction

Read REPORT.md. Do not reopen the accepted B_p ≅ Sha[p] comparison.

## Heegner continuation

- The ordinary criterion is matched to Wei Zhang §8.2 Lemma 8.4 on p≥5, p∤23N, p ordinary, with the retained seed inputs and the genuine primitively normalized Heegner system. Supersingular coverage is not certified by the references checked.
- Use M_ell=gcd(a_ell,ell+1). Exact a_ell=0 is optional; complex-conjugation Chebotarev supplies auxiliaries for any fixed finite batch. It supplies no point indivisibility.
- Correct the index: use eligible prime supports, not division of ell+1 by a squarefree failure product.
- A useful next arithmetic output must concern the genuine P_ell itself: a certified finite-field reduction, an exact algebraic evaluation, or a proved evaluation identity controlling divisibility. Merely listing more auxiliaries does not meet this requirement.
- Match the criterion before claiming a primary certificate. One certificate remains a fixed-prime result unless a separate argument controls the infinite tail. There is no authorized seed-scale computation in this handoff.

## Jet continuation

- Preserve sparse row-combination provenance during elimination, not just reduced rows or a Boolean flag.
- Export J, row and column identifiers, coefficient ring/precision, v, nu, c, lambda, and the integral source/normalization binding. Regenerate rather than trust stored row entries.
- For a homogeneous system verify lambda J=v−c nu on all columns and prove nu(Phi)=1 for the actual normalized source. For an inhomogeneous system record b and check the induced lambda b as well.
- Include all derivative terms and boundary columns. A modulo-p relation is not automatically a p^4 jet certificate.
- If support fails, return its exact residual and the next genuinely different support/cancellation mechanism, not a universal infeasibility claim.
- Do not label another curve's calibration, a formal interpolation lemma, or a fabricated jet as a seed source value. Do not describe one seed value as uniform FIN.

## Smaller-field continuation

The return's strict-Selmer identification gives h_p=2+dim Sha[p]−dim loc_p Sel_p, hence h_p≤2 iff Sha[p]=0 under retained parity, on its p≠4547 domain. A new independently proved class-group estimate would be useful; the identification itself is not the estimate. No repeat of the formal norm sequence is requested.
