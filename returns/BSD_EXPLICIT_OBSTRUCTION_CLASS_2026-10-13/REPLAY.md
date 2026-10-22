# Reproduction

From this directory:

```
python3 checks/independent_exact.py
gp -fq -s 128M checks/certified_field.gp
sage -python implementation/fisher_model.py
sage -python implementation/geometry_check.py
```

Requirements: Python with SymPy; PARI/GP2.17.3 for the recorded BNF output; SageMath for the Pfaffian and Groebner checks. The local session used the existing Sage environment recorded in outputs/REPLAY.json. The first checker also independently verifies every saved successful finite-field Hensel witness. The optional `implementation/local_witnesses.py` regenerates the bounded search, including places where this naive model did not yield a simple witness; those failures are not insolubility results.

The GP verification must print `ALL_CERTIFIED_FIELD_ASSERTIONS_PASS` with empty stderr. GP's exit code alone is not sufficient. The replay wrapper `checks/replay.py` uses explicit executable arguments and checks these conditions.

The exploration scripts in theory/ reproduce the longer field-element and ideal outputs; run them from the package root. They are not the fail-closed acceptance checker.

The written proofs remain necessary: a successful replay does not independently prove that Miller--Stoll's source hypotheses match the retained isogeny or that the rank upper bound is valid. Those dependencies are listed separately.
