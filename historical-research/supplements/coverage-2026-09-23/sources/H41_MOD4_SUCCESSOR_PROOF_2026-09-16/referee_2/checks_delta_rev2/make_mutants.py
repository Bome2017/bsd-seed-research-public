src = open('/Users/bsm/H41_MOD4_SUCCESSOR_PROOF_2026-09-16/checks/run_all_checks.py').read()
muts = {
 "M1_mod4_to_mod8": ("ok = all((a[n]-Ecoef(n)) % 4 == 0 for n in range(1, M+1))", "ok = all((a[n]-Ecoef(n)) % 8 == 0 for n in range(1, M+1))"),
 "M2_component_group": ("if two != 4 or", "if two != 8 or"),
 "M3_manin_flag": ('mine[5] != "1"', 'mine[5] != "2"'),
 "M4_slope_residue": ("{(3*(l-1)//x) % 4 for x in e} != {2}", "{(3*(l-1)//x) % 4 for x in e} != {0}"),
}
for name, (old, new) in muts.items():
    assert src.count(old) == 1, (name, src.count(old))
    open(f"mutant_{name}.py", "w").write(src.replace(old, new))
print("mutants written:", list(muts))
