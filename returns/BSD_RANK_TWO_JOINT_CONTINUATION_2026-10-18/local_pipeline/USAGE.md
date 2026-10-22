# Actual local pipeline

`python3 run_pipeline.py CONFIG.json` consumes a new authenticated unit source. It does not search for units or run BNF. The config has these fields:

```json
{
  "label": "655a1_new_source",
  "p": 7,
  "curve": [0, 0, 1, -13, 18],
  "nf": "/absolute/path/to/nf.gp",
  "source": "/absolute/path/to/eval_data.json",
  "source_format": "factored_units",
  "unit_authentication": "/absolute/path/to/actual_admission_receipt.json"
}
```

`factored_units` is the existing five-entry field/point/scalar export, with each unit given as factor-pack/integer-exponent pairs. `orbit_relations` accepts the six-entry form: the same four field entries, base factors, and an integer matrix on their six scalar orbits. Every exponent is preserved before local valuation cancellation. The script freezes the exact compact source and hashes its inputs and admission receipt. Hashing the receipt does not independently prove its mathematical assertions.

The model is explicit and all five Weierstrass coefficients are used. The engine rejects anomalous or supersingular reduction because the implemented formal-branch condition is the ordinary nonanomalous one. It verifies the actual point field, formal branch, finite-field point coordinates and scalar action. Split-prime values are tested modulo the entire two-dimensional linear-function allowance; this is the full affine-norm screen at that split place, not a second independent constraint.

The coefficient-local computation uses the actual degree-six formal branch. Unit seventh-power classes are computed at P^8 and P^9. The branch has e=6, so these precisions capture the full quotient; the code retains common-uniformizer cancellation, a nonpower control and a seventh-power control. Required completion markers and stderr are checked, not just process exit codes. Every arithmetic child is capped at60seconds and this driver's cumulative arithmetic cap is180seconds.

Output records the actual stacked rank and ordinary-unit kernel upper bound4-r under the retained full-image framework. It explicitly leaves ordinary class and primitive divisor terms unresolved. It does not promote the source or a previous BNF output to complete class data, use a known Sha answer, or assert a whole-source bound from units alone.

The655 field preflight has already been completed without a unit search: #E(F7)=11, formal branch(e,f,vx,vy)=(6,1,-2,-3), two other branches(7,3,0,0), and fully split primes41413,44843,63533. No new unit rank has been obtained merely by preparing these inputs.
