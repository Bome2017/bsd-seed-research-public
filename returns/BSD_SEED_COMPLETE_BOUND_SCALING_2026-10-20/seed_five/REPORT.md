# Actual seed, coefficient 5: source constructed; complete bound not obtained

Status: `ACTUAL_SEED_SOURCE_CONSTRUCTED_CLASS_GATE_RESOURCE_LIMITED`.

This run applied the same source arithmetic to the original curve
`[0,-22735,0,106272484,0]`. It did not substitute another control, and did
not use the seed's known 5-primary vanishing as an input.

## Actual arithmetic completed

The nonzero 5-torsion point field has degree 24 and signature `(4,10)`.
The saved point lies on the curve and has order five; its coordinates
generate the field. A literal field automorphism takes that point to
twice itself and has order four. The complete field construction,
reduction, point checks and maximal-order calculation took 0.48 seconds.

Its exact field discriminant is

```
2^32 * 3^16 * 5^23 * 2243^16 * 4547^18 * 5843^16.
```

The complete faithful-character valuation allowance on
`S={2,3,5,2243,4547,5843}` is zero. Actual prime decomposition and scalar
action leave one possible line at 2243; the correctly ramification-
normalized incidence map on that line is a unit modulo five. The finite
local model was changed from the earlier control's Frobenius 4 modulo 5
to the seed's Frobenius 3 modulo 5, and matched to the actual ideal
orbits. See `DIVISOR_PROOF.md`.

Thus valuation directions do not account for a possible excess in this
source. The complete remaining expression is

```
dim K <= (3-r_U) + k_C,
```

where three is the full faithful ordinary-unit dimension, `r_U` is
the actual unit map rank, and `k_C` is the remaining ordinary-class
contribution after its class map and connecting obstruction. Neither
unknown was replaced by a known Selmer or Sha value.

## The complete class gate did not finish

This was the first seed-p5 BNF attempt found in the scoped source
recovery. Prior p5 BNF records concerned 389a1 and 37a1; the seed's
earlier class calculation concerned p3.

The first setup placed `default(parisizemax,...)` inside a GP brace
block. GP restarted evaluation and emitted only a warning, without
executing the requested arithmetic. That run was rejected and preserved
in `rejected_stack_restart/`.

Setting the stack through GP's command-line option repaired that setup.
The actual computation then failed with explicit stack overflow:

| Stack limit | Elapsed time | Result |
|---|---:|---|
|512 MB|13.76 seconds|No class or unit table|
|2 GB|18.41 seconds|No class or unit table|

The second run was a documented resource adaptation. It was not accepted
because GP returned exit code zero: both runs had a nonempty error output
and lacked the completion marker. No BNF or class certificate was
created. No repeated attempt with the same failed configuration was run.

Consequently this run has **no complete class bound**, no unit-norm rank,
and no numerical complete-source upper bound. It does not even supply a
GRH-conditional class table. The resource failure is not a theorem that
the class contribution is large or that the construction cannot work.

## Effect on the requested experiment

The method can construct the actual seed's source and eliminate its
entire valuation contribution at p5. The successful p3 control's
complete arithmetic has **not** yet scaled to a complete seed-p5
calculation: the required ordinary-class and faithful-unit arithmetic
was not produced.

This is an attempted complete-bound computation with a recorded
computational stop, not another successful detector experiment.
It yields no seed-primary result, no across-prime bound, and no change
to FIN, ORDER9 or Q36.

`replay.py` regenerates the accepted field, prime ideals, local binding,
and finite incidence model in a fresh directory. It deliberately does
not rerun the failed BNF gates. Those failures remain auditable through
the preserved scripts, output, and receipts.
