# Accepted commands and scope

Working directory:

```text
/Users/bsm/BSD_CLAUDE_RECONCILIATION_AND_CONTINUATION_CODEX_2026-10-15/class_lift/mirror389/ray
```

Full arithmetic replay from the saved certified BNF:

```sh
python3 -I replay.py
```

This reads canonical `construct.gp` and `quotient.gp` without source rewriting, runs them in a fresh `clean_replay/`, preserves the previous clean outputs under `prior_clean_replay_N/`, and checks exit code, stderr and required markers. The cumulative timeout is180 seconds. The original saved BNF and class-source files are inputs and are not edited. The host-specific GP path and input paths are explicit in the scripts.

For standalone GP execution from a fresh output directory, feed the canonical construct script to GP first and the canonical quotient script second. They write relative output paths in that directory. Input paths are absolute and checked against SCRIPT_BINDINGS.json. Existing output files should not be reused because GP's write commands append. `replay.py` handles that isolation.

Portable integer-only check (no original number-field files needed): copy `portable_matrices.gp` and `verify_integer_quotients.gp` together to any directory with PARI/GP, then run there:

```sh
gp -q -f < verify_integer_quotients.gp
```

Expected markers are `PORTABLE_INTEGER_QUOTIENT_CHECK_PASS` and orders1746,9,3. The portable check authenticates the exported integer maps, relation lattices, Smith factors and concrete lift orders. It does not reconstruct the number field, CRT elements, local Kummer images or BNR arithmetic; those are checked by the full replay.

The accepted script hashes, input-certificate bindings and output hashes are in SCRIPT_BINDINGS.json. Earlier failed variants are explicitly retained under failed directories and are not canonical.
