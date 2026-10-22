# Second-order tuning: a proposed solution of the finite lifting gate

2026-10-06. **SECOND_ORDER_VARIATION_DERIVED;
MIXED_CHAR_ORDER3_W_LIFT_DERIVED_CONDITIONALLY.**

**Written proof requiring independent review.** Full-S Stage A remains a
retained provisional input; the separate strict-S Aristotle result does
not certify it. FIN, ORDER9 and Q36 remain unchanged.

## What was done

I derived Pro's requested addition law and continued through its arithmetic
tuning test. The proposed conclusion is stronger than a formula:

> For each good seed prime p>=5, under the retained inputs, one can choose
> an actual nonzero finite-support tame character lambda with
> ker b_lambda=W and alpha_lambda=0. Both rational-point classes then
> have Selmer lifts through pi^3 in the genuine root-of-unity twist.

This is an existence proof, not a computed seed character or a bound on
its conductor. Its main new arithmetic argument is in
[VARIATION_AND_TUNING.md, Sections 4--6](VARIATION_AND_TUNING.md).

## The addition law

Write K_0=ker b. For lambda,mu in D^W,

    alpha_(lambda+mu)
       = alpha_lambda + alpha_mu + P(lambda,mu),

where P is symmetric bilinear. With the Weil-pairing convention fixed
in the earlier return, its mixed term is

    P(lambda,mu)=-C_mu^lambda(X1,X2).

Here X1,X2 are first Selmer lifts and C is the actual first-order
Cassels--Tate pairing for a mu-twist of the lifted module M_2(lambda).
The proof uses an explicit two-variable finite-module diagram, including
the local conditions. It is not an inference from the scaling law.

## What supplies tuning rather than only variation

For EVERY nonzero lambda in K_0, the proof constructs mu in K_0 with
P(lambda,mu)!=0. It does this by selecting two new tame primes using
cochains of the lifted Selmer classes. A commutator has zero effect on
every original b-row but nonzero effect on the mixed lifted pairing.

The key new evaluation lemma uses the nonsplit action 1+t and Nakayama;
it does not treat the full Galois module as semisimple. The compatible
Frobenius prescription has a separate field-intersection proof.

Thus P on K_0 has zero radical. Since K_0 is infinite-dimensional, it
contains a nondegenerate binary plane. On that plane completing the
square solves alpha_(lambda+mu)=0 in ANY fixed first-order fiber with
radical W. This proves the asserted tuning. For a nonzero first-order
form, every prescribed alpha value occurs in the same fiber.

The earlier correction criterion now supplies the two order-three
lifts with eta=0. Therefore they match the actual character
chi_lambda=zeta_p^[lambda], not a freely adjusted formal character.

## How this changes Pro's proposed chain

At the stated written-proof grade the two middle finite steps are now
supplied together:

    full-S Stage A (retained, independently unconfirmed)
       -> second-order variation and arithmetic tuning
       -> both point classes lift modulo pi^3.

The all-order lift, rank-two determinant comparison and global support
invariant are NOT supplied. No relation between alpha and the original
Sha dimension has been inferred. The construction is compatible with
arbitrary finite dimension of the starting Selmer group.

While working, I fetched lab commit c4f53313 and read its new Kato gate.
It rules out treating finite-order success as an automatic route to a
generic rank-two family. A genuine compatible all-order lift would force
a central twisted L-value to vanish. See [ENDPOINT_SCOPE.md](ENDPOINT_SCOPE.md).
This does not refute the finite-order construction. It does mean that
this return is not permission to restart the superseded OpenAI job or
to launch an all-order campaign on the strength of the pi^3 result.

## Evidence and review limits

- The actual mathematical proof is written in full, with separate
  cochain, field, local-condition, and finite-field arguments.
- 16,265 exact algebra controls pass, including the dual-map sign,
  truncated character law, nonsplit evaluation model, the commutator
  which changes the lifted row and leaves all old rows zero, and
  quadratic tuning. A countercontrol rejects the false inference
  that nonconstant variation alone guarantees a zero.
- These are finite algebra checks, not evaluations of seed Selmer
  classes and not a machine proof of the arithmetic construction.
- No remote job, seed-prime campaign, paid computation or message was
  launched. This return is published only to the authorized lab branch.

[Proof](VARIATION_AND_TUNING.md) · [Review handoff](HANDOFF.md) ·
[Check results](checks/RESULTS.json) · [Sources](SOURCES.md)
