# H41 successor author-side recheck

Read `AUTHOR_SIDE_ADDENDUM.md` first. This is not an independent referee or canonical seal.

`inputs/` preserves the uploaded proof and check script/output. `checks/` contains the arithmetic replay, receipt, a separate failure-detection patch, and its output. The database directory is absent, so its results are explicitly not replayed. `sources/` records public locators; no PDF bytes are claimed to have been archived.

Run from any directory:

```bash
python3 checks/run_all_checks_fail_closed.py
# Optional supplied database input:
python3 checks/run_all_checks_fail_closed.py /path/to/ecdata/opt_man
```

Requires SymPy. Do not use Python optimization mode; the original script retains assertions. No network calls are made by the check scripts. These checks are finite regressions, not a proof of the infinite family.

`MANIFEST.sha256` hashes every package file except itself. It is a manifest of this author-side package, not the unavailable original nine-entry successor manifest.
