# Reproduction and evidence boundary

Use a working copy, because scripts update their result files. The mathematical source papers are linked in the proofs. Raw third-party PDFs and full unrelated Cremona conductor-range files are excluded from this return; selected exact database rows, source URLs and whole-file hashes are retained in cm/SOURCE_ROWS.json.

Runtime used: Sage Python at
`/Users/bsm/run040-order7-cayley-coordinate-slice-genus-census-2026-09-03/tools/sage-env/bin/python`.
Use its Python directly or `sage -python` in an ordinary installed Sage environment. This host's wrapper does not support `sage -python` reliably. Python3 alone suffices for the three saved-data checks.

Exact reconstruction:

```
sage -python checks/base_brandt.py
python3 checks/verify_base_brandt.py
python3 comparison/check_comparison.py
python3 component/torsion_and_indices.py
sage -python component/basis_check.py
sage -python cm/certified_GZ_ingredients.py
sage -python cm/height_convention_control.py
```

The Brandt construction took about16seconds on this host. The certificate evaluates12000 derivative terms,120000 twist terms and42 height-series terms at200-bit ball precision, with proved infinite tails. `cm/analytic_probe.py` is explicitly exploratory and is not the certificate. The height-convention control is likewise a separate numerical control; the proof cites the convention at source.

`component/component_check.gp` can also be run through PARI/GP on standard input to reproduce the singleton-isogeny and local controls. `comparison/check_comparison.py` optionally binds the predecessor at its original host paths when present; absence of those paths does not create a replacement mathematical input.

The parent replay of the governing analytic certificate is saved in checks/parent_GZ_replay.out, with empty stderr. Replaying the same implementation is reproducibility evidence, not an independent numerical algorithm or formal verification. The stored-matrix verifier and small-field enumerations are independent implementations of those exact subchecks.

Classical modular degree20576640 is an imported primary data record, not freshly recomputed from modular symbols. Antecedent rank bounds, geometric C3 transport and global torsor comparison retain their predecessor grades and are bound in INPUT_BINDINGS.json. Publication and hashes do not certify those theorems.

The exact finite-sum coefficient vectors are also preserved, compressed, in cm/C_coefficients.json.gz and cm/C_twist_minus19_coefficients.json.gz. `checks/export_coefficients.py` regenerates them and checks their vector hashes against the certificate. They are included so the finite sums can be reviewed without depending on missing historical work units. Runtime versions: Sage10.9; Python3.13.15.
