# Replay
Work in a copy of this folder; retain the sealed originals. Requires PARI/GP 2.17.3 and Python 3 standard library.

1. Run python3 checks/check_finite_tables.py to independently verify the saved exact tables using fraction/integer arithmetic.
2. Run gp -q -f checks/height_scan.gp and checks/height_geometry.gp from the folder root; compare stdout with the corresponding saved outputs. height_scan also appends height_rows.gp, so use a working copy.
3. For an overconvergent row, copy the saved outputs/*input.gp to checks/row_input.gp and run gp -q -f -D parisizemax=1500000000 checks/one_row.gp. Selected n5 and n6 outputs are retained. Do not accept an exit code or DONE marker alone: reject every genuine PARI error and every non-p-adic output. The known p31/n5 failure is retained as a rejected run; do not needlessly repeat it.
4. Run checks/finite_table.gp (7) or checks/finite_table31.gp (31) through GP to rebuild the exact symbol tables, then repeat the Python check. Coefficients are computed independently of the point heights.

The runner contains the local GP path; change it only in a replay copy. No network, paid resource, modular-symbol database, or full seed computation is needed. All source controls use explicit curve equations. The table paths and raw output are part of the evidence.
