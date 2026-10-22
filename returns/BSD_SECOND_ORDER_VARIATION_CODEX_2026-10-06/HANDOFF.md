# Independent review: second-order arithmetic tuning

Review the proof before extending the mechanism. This is a research return,
not a launch instruction, Lean certificate, or permission for paid work.

## Claimed theorem

Under the retained full-S Stage-A inputs, every first-order fiber with
radical W contains a genuine nonzero tame character lambda for which
alpha_lambda=0. This supplies both Selmer lifts modulo pi^3 with eta=0.

The new claim goes beyond Pro's proposed variation test: the polarization
on ker b is claimed to have zero radical, by an arithmetic commutator
construction, so the affine quadratic equation can actually be solved.

## Ordered review gates

1. **Mixed diagram and sign.** In VARIATION_AND_TUNING.md Sections 2--3,
   verify exactness of both rows of (10), their local conditions, and
   J(X2,tz)=-e(w2,z). Check that naturality gives P=-C, and that Baer
   linearity plus interchange of the two variables proves bilinearity.
   Do not infer this from scaling alone.
2. **Nonsplit evaluation surjectivity.** Section 4: prove the image is
   an A=k[t]/t^2 submodule using (I,1); check residual independence on
   ker(rho,lambda), then Nakayama. Do not replace this argument by
   semisimplicity of M_lambda or of the group algebra.
3. **Field intersection.** Section 5: check
   Q(E[p],lambda) intersect Q(mu_p,Pi^(1/p))=Q(mu_p), including p=5.
   It must allow Frobenius (-I,0) while every prime in Pi splits in
   the radical field.
4. **Arithmetic separation of orders.** Section 6: verify the cochain
   commutator and the simultaneous Chebotarev prescriptions. The TOP
   value X1(v)=t e1 must be realizable while every residual x_i(v)=0.
   Check that one difference of two normalized conductor-prime
   characters kills ALL b-entries but changes C(X1,X2) by a unit.
   Formula controls alone do not certify this step.
5. **Tuning rather than variation only.** Section 7: show nondegeneracy
   on the infinite-dimensional kernel supplies a nondegenerate binary
   subspace, then complete the affine square. Treat the B=0 case
   separately to retain a nonzero character.
6. **Actual coefficient ring and endpoint.** Section 8: check the
   eta=0 correction and the O/pi^3 identification. Keep all-order
   lifting separate, and read ENDPOINT_SCOPE.md with concurrent
   review c4f53313. No analytic double zero is claimed from Kato.

Return CONFIRMED / CORRECTED / REFUTED / GAP per gate. If a step fails,
try to repair that exact step before treating the entire construction
as a failed lane. Do not reprove the old strict-S theorem in place of
reviewing the full-S dependence.

## Evidence included

Bound copies of Pro's prompt, Stage A, the prior second-order proof,
character realization, and the concurrent Kato-gate review; exact
checker and results; source and commit bindings. No third-party
paper text is newly bundled. The original sealed returns are unchanged.

## Explicit nonclaims

No explicit seed lambda or Selmer basis is computed. No conductor bound,
all-order lift, generic rank-two determinant comparison, global support
invariant, new Sha vanishing, FIN, ORDER9 or Q36 is obtained. The proof
and the old full-S Stage-A input are not independently accepted merely
because this packet is published to the lab.
