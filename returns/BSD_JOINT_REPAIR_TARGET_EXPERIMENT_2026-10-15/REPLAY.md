# Replaying the checks

From this folder, with standard-library Python:

```sh
python3 heldout/check_arithmetic.py
python3 arithmetic/1913b1/local_witness_check.py
python3 arithmetic/28042a1/local_witness_check.py
```

The first command checks every fresh field/root/point/cubic-symbol/triple/row identity, including the separately sealed mirror extension. It also confirms the serialization repair left the arithmetic blocks unchanged. No PARI, class group, L-value or Sha-order input enters that replay.

`heldout_analysis/analyze.py` reconstructs the 2340 initial exact F3 profiles and source-bindings. Its output contains literal dual-row certificates. `theory/dual_overlap.py` documents its source adapter and rejects blocks bound to a different matrix. Extension analysis is retained alongside those files.

The GP norm and source scripts in each new control retain their runtime and failure receipts. They need PARI/GP with the relevant number-field routines. The actual norm cube roots and Hensel witnesses are retained, so admission is not inferred from a successful termination string. The independent source audit is under `source_screen/`.

Fresh block production used the pinned local historical sources listed in each `INPUTS.json`; those absolute original paths are not portable. The exported `source.json` files contain the exact field, torsion coordinates and factored source polynomials needed for the independent finite-field replay. The underlying complete-source certificates keep their separate historical grades.

The root manifest excludes only itself and generated Python bytecode. Original rejected attempts are deliberately retained and labelled; they are not accepted outputs. Primary-paper cache files are referenced by URL/hash and retained locally outside the public return.
