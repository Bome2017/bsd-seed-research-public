# October 3 review and constructive follow-through

**FOUR_LANE_CLOSURE_NOT_ESTABLISHED.**
**RECEIVER_FORWARD_INJECTION_CONFIRMED_AT_RETAINED_INPUT_GRADE.**
**RECEIVER_REVERSE_COMPARISON_DERIVED; NO_NEW_UNIFORM_BOUND.**

The new receiver is a real arithmetic map. I found no blocking error in
its proof that restriction kills exactly the two known point directions
and carries the full Sha[p] into its p-split class-group receiver. Its
quadratic auxiliary point supplies the local Kummer line at every good
p>=5, including supersingular primes and the case where both known points
are locally p-divisible. This removes that obstruction to the comparison.
It does not bound the receiver.

I then pushed the construction beyond its submitted forward injection.
The finite group Gamma_p has H^2(Gamma_p,E[p])=0 for p>=5. The proof uses
its affine module structure, a Sylow calculation, and the impossibility
of lifting a 2x2 unipotent of order p to order p modulo p^2. Thus every
equivariant class-group homomorphism in the receiver descends globally.

Outside the fixed set {2,3,19,59,487,2243,4547,5843}, this gives

    0 -> Sha[p] -> B_p -> C_p^loc -> 0,    dim C_p^loc <= 1.

If the known points localize nontrivially at p, the local error is zero.
The at-most-one result does not need that extra hypothesis. The submitted
bound dim B_p<=1 is therefore equivalent to Sha[p]=0 on this cofinite
domain, using retained parity. This is a reverse comparison, not an
independent proof of that bound. The new derivation awaits a second reader.

I also tested the next implications. Vanishing finite-group H^2 does not
bound absolute Galois cohomology or the class group. A two-dimensional
receiver corresponds to an explicit unramified, p-split extension with
kernel E[p]^2 and the prescribed Galois action. Its abstract group exists;
the elementary Minkowski discriminant bound does not exclude it. No
uniform annihilator or multiplicity bound resulted.

## Corrections to the four-lane findings

1. **A:** its actual connecting-map count survives. Its unramified mod-p^2
   tangent identification and blanket full-Selmer height comparison do not.
   Its claimed supersingular coverage is unproved, and surjectivity is not
   necessary for the stated H^2 dimension criterion.
2. **B:** all 40 height rows replay at higher precision. They concern the
   known-point line W intersect S0, not the whole strict Selmer group at
   unsettled primes. They do not kill all secondary constructions on
   S0/(W intersect S0). RELATIVE_PAIRING.md explicitly repairs that domain
   and proves its Schur-complement formula, without deriving a bound.
3. **C:** it changed the actual coinvariant module in the one-index
   construction to a two-prime-field Selmer module without a comparison.
   Its numerical localization table also has errors: at p=5 the claimed
   nonzero pair (941,991) has proportional rows and determinant zero.
4. **D:** the cup-product containment survives; the universal impossibility
   conclusion does not. Vanishing of a separately bounded target plus a
   PROVED injection would be a successful argument, not a contradiction.
   Its X subset S0 assumption and general Cartier-dual formula need repair.

Accordingly the assertion that every route reduces to a cyclotomic T^2
unit, or that all first-order receivers have been exhausted, should be
withdrawn. The retained minimum tame-depth theorem must not be replaced
by a single cyclotomic-direction statement.

## What these parts actually make

The established chain remains:

    independent cofinite control of the receiver's V-quotients
        -> dim B_p<=1 cofinitely
        -> Sha[p]=0 cofinitely
        -> FIN after the finitely many primary-finiteness obligations.

The first arrow is still missing. The map after it is constructed and
checked; it is not guessed. Exact order nine and Q36 remain separate.
The receiver gives a concrete location for a uniform arithmetic bound,
not evidence that obtaining that bound is easy or inevitable.

## Verification and files

* Receiver ZIP integrity and 12/12 manifest entries pass.
* Its 166-prime exact control output is reproduced exactly.
* All 40 ordinary-height rows through 200 agree in a precision-12 replay.
* Fresh exact group operations check the diagnostic localization rows.
* 3,026 matrix lifts and 12,500 Schur complements pass exact controls,
  with separate normalizer checks at seven primes.

Read AUDIT.md for the lane corrections, RECEIVER_AUDIT.md for the submitted
map, RECEIVER_DESCENT.md for the new proof, and UPPER_CONTROL_ATTEMPT.md for
the attempted bound. Sources and dependency grades are in SOURCES.md.

Original reports, maps, memories and release repositories were not edited.
No worker, prime-certification job, class-group computation, push, or
external message was launched.

FIN, ORDER9 and Q36 are unchanged.
