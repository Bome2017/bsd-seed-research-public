# Review of the complete-bound scaling experiment

2026-10-20. Same-team model review with separate exact arithmetic replays,
not human review, proof-assistant verification, or recertification of all
retained descent theorems.

**Verdict: the completed arithmetic and the reports' stated limitations are
supported. No new unconditional complete source bound is established in
these p5 runs.**

## 1. Same curve, coefficient three to coefficient five

The fixed source is genuinely `1664n1`, not a replacement curve. I read its
construction, unit authentication, residue extraction, divisor action,
class-certification receipts and final proof.

A separate GP program checked:

- irreducibility of the actual degree-24 polynomial and its binding to the
  saved maximal-order field;
- the actual point on the curve, its order five, and the literal
  order-four automorphism taking it to twice itself;
- the scalar action on every primitive ideal above `{2,5,13}`;
- all 332 compact-factor principal-ideal identities and the integer
  cancellation forming the 13 actual units.

The accepted replay had empty stderr and the required final marker. It
took about eight seconds. These exact unit identities do not require
accepting the BNF list as fundamental.

The exported rational-polynomial coordinates and all compact exponents
were separately rebound to the GP source. Then an independent Python
extraction at the sufficient split prime 18541 multiplied actual
factor residues before taking fifth-power residue logarithms. It
constructed the affine cosets by choosing a basis of the full rational
five-torsion over the finite field and enumerating nonzero linear forms.
This differs from the producer's factor-by-factor logarithm and coset
construction. It returned source rank three and incidence-norm rank one.

Together with the retained character-unit dimension three, this proves
an upper bound two on the entire ordinary unit kernel. It does not prove
the actual norm rank is exactly one. The primitive scalar ideal
permutations have no faithful component at any allowed valuation place,
so the entire valuation contribution is zero.

The remaining unconditional complete-source bound is therefore

    dim K <= 2 + dim Cl(A)[5]^chi.

Using the potentially smaller class-map kernel in place of the full
class group is also valid, but that kernel was not bounded here.

The provisional BNF class group is `C3`. Its flag-one quotient
certification timed out after the declared 110-second alarm. The process
exit code zero is correctly rejected because stderr contains the alarm
and no certificate marker was produced. Thus upper two for the complete
source remains conditional on GRH or a future complete class certificate.
It is not yet an unconditional five-primary vanishing result.

## 2. Original seed at coefficient five

The separate seed construction uses the fixed model
`[0,-22735,0,106272484,0]`. I independently replayed its field,
torsion point, scalar action and complete prime-ideal decompositions.

The faithful scalar divisor dimensions above
`{2,3,5,2243,4547,5843}` are exactly

    [0,0,0,1,0,0].

The only possible source valuation line occurs at 2243. The matched
multiplicative decomposition/inertia model gives a primitive incidence
coefficient that is a unit modulo five. The ramification quotient
`e_target/e_source` must be included; otherwise a false factor five
appears. The model is matched to the seed's split multiplicative
reduction and discriminant valuation one, not copied without change
from a control's different Frobenius.

Therefore the valuation kernel is zero, while the complete remaining
bound has the form

    dim K <= (3-r_U) + k_C.

Neither the actual seed unit rank `r_U` nor the complete class
contribution `k_C` was computed. The seed BNF failed at a 512 MB stack;
one declared resource adaptation failed at a 2 GB stack. The initial
stack-setting restart is also retained as rejected. No class table was
produced, even at a provisional GRH grade. These are computational
failures, not evidence for a nonzero class contribution.

## 3. Original seed at coefficient three

The old conditional complete bound four is already attained by four
independent exact source classes. Their class images have rank two and
their actual norms are cubes. Repeating their class-map calculation
would not find a new rejection. `seed_three/REPORT.md` records the
retained conditional grade and the earlier failed certification. Its
fresh matrix replay is a replay of old arithmetic, not a new upper
bound.

## 4. Uniform valuation consequence

`UNIFORM_VALUATION_REVIEW.md` separately checks the deduction suggested by
the seed-five result. Under the retained local representation and
reduction inputs, the whole primitive valuation defect vanishes for
good p>=5 outside `{19,59,487}`. The multiplicative p-channel is retained
only when `p | q-epsilon`; the other channel is a unit. Good
nonanomalous coefficient places and the seed's two additive places
have no faithful scalar divisor component.

That deduction is a genuine across-prime removal of this one term.
It does not bound the unit rank or class contribution. On its domain
the complete-source target becomes

    dim K <= (p+1)/2 - r_U + k_C.

No proof that this stays at most two or three across primes is supplied.
No new FIN, ORDER9 or Q36 conclusion follows.

## Replays and boundaries

- `FIELD_UNIT_REPLAY.json`: exact field, ideal-action and unit identities.
- `export_replay.out`: literal binding of exported factors and coordinates.
- `RESIDUE_REPLAY.json`: separate direct multiplicative arithmetic at 18541.
- `UNIFORM_VALUATION_REVIEW.md`: mathematical review of the uniform local
  term, under retained local inputs.

The review did not rerun a failed BNF/class certificate, independently
rebuild maximal orders from a different implementation, or certify a
complete ideal-class presentation. It does not use known seed Sha
vanishing to infer any arithmetic rank.
