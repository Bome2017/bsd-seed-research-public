import os, sys
D = "/Users/bsm/run013-bsd-scout-2026-08-22/_data/ecdata/curvedata"
cols = ['label', 'isoclass', 'number', 'lmfdb_label', 'lmfdb_isoclass',
                  'lmfdb_number', 'iso_nlabel', 'faltings_index', 'faltings_ratio',
                  'conductor', 'ainvs', 'jinv', 'cm',
                  'isogeny_degrees', 'semistable', 'squarefree_disc', 'signD', 'absD',
                  'min_quad_twist_ainvs', 'min_quad_twist_disc',
                  'bad_primes', 'tamagawa_numbers', 'kodaira_symbols',
                  'reduction_types', 'root_numbers', 'conductor_valuations',
                  'discriminant_valuations', 'j_denominator_valuations',
                  'rank', 'rank_bounds', 'analytic_rank', 'ngens', 'gens',
                  'heights', 'regulator', 'torsion', 'torsion_structure',
                  'torsion_generators', 'tamagawa_product', 'real_period',
                  'area', 'faltings_height', 'stable_faltings_height',
                  'special_value', 'sha_an', 'sha',
                  'trace_hash', 'degree',
                  'xcoord_integral_points', 'num_int_pts',
                  'twoadic_index', 'twoadic_label', 'twoadic_log_level', 'twoadic_gens',
                  'modp_images', 'nonmax_primes', 'nonmax_rad']
targets = {"62a1","66b1","114c1","254d1","258d1","4098f1","16382b1","16386a1","262142c1","262146b1"}
want = ['label','ainvs','isogeny_degrees','bad_primes','tamagawa_numbers','reduction_types','discriminant_valuations','torsion_structure','real_period','special_value','sha_an','degree']
found = {}
for fn in sorted(os.listdir(D)):
    lo = int(fn.split('.')[1].split('-')[0])
    if not any(lo <= int(''.join(ch for ch in t if ch.isdigit() and True) [:len(str(lo))] if False else 0) or True for t in targets): pass
    Ns = {int(''.join(c for c in t if c.isdigit())[:-1]) for t in targets}
for t in sorted(targets, key=lambda s: int(s.rstrip('0123456789abcdefghijklmnopqrstuvwxyz') or 0)):
    pass
import re
def N_of(t): return int(re.match(r'(\d+)', t).group(1))
for t in sorted(targets, key=N_of):
    N = N_of(t); lo = (N//10000)*10000
    fn = os.path.join(D, f"curvedata.{lo:05d}-{lo+9999:05d}")
    with open(fn) as fh:
        for line in fh:
            if not line.startswith(t+" "): continue
            tok = line.split()
            if len(tok) != len(cols):
                print("COLCOUNT MISMATCH", t, len(tok), len(cols))
            rec = dict(zip(cols, tok))
            print(" | ".join(f"{k}={rec[k]}" for k in want))
            found[t] = rec
            break
print("found", len(found), "of", len(targets))
