# Checks and executable extraction

`python3 check_signed_extraction.py` reproduces `signed_extraction_controls.json`.
It checks exact cyclotomic factorizations, finite-ring representatives, retained
p-content, the two-layer extraction and Lucas weights, and rational valuation
identities. Its inputs are deliberately synthetic. The 140 reconstructions are
not new seed witnesses.

`python3 independent_fitting_control.py` reproduces the maximal-minor
countercontrols in `independent_fitting_control.json`. These are abstract modules,
not class groups or Selmer groups computed for the seed.

`python3 signed_theta_extractor.py INPUT.json` is the finite extractor if actual
source coefficients become available. Input must contain:

- `p`: the coefficient prime, at least five;
- `theta1`: exactly p integer coefficients in the gamma basis, from the degree-p
  anticyclotomic layer (ring conductor p^2);
- `theta2`: exactly p^2 integer coefficients, from the degree-p^2 layer (ring
  conductor p^3);
- `source_metadata`: a nonempty record identifying the primitive quaternionic
  eigenfunction, its basis/sign, Gross-point choices, generator/reciprocity,
  producer, and coefficient receipts.

Metadata is passed through and explicitly marked unverified. The extractor
does not construct or certify those arithmetic inputs. Arrays of arbitrary
modular-symbol values are not interchangeable with this source.

The output contains the signed constant, linear and quadratic coefficients
modulo p. For correctly matched seed inputs, the first two must vanish by the
written seed augmentation and inversion arguments. Passing these consistency
checks does not validate the input. A nonzero quadratic coefficient does not
certify Sha vanishing: see `../notes/INDEPENDENT_SEED_CONTROL.md`.

No seed input JSON is supplied because no such source arrays were computed in
this return. No large field, Brandt-module enumeration, or auxiliary-prime
campaign was run.
