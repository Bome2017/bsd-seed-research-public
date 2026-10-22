#!/usr/bin/env python3
"""Audit of saved tables and elementary transfer precision; not a seed engine."""
from fractions import Fraction
from hashlib import sha256
from math import comb
from pathlib import Path
import json
import subprocess

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "submitted/BSD_CYCLOTOMIC5_AND_MOMENT_2026-10-12"
REPO = Path("/Users/bsm/BSD_GITHUB_UPDATE_CODEX_2026-10-04/lab")
BASE = "0e8bb6859d1391e6d449b1ef02aff2cfd85310f1"
PREFIX = "work/state-sync-2026-09-30/release/v0.2.6/evidence/src/BSD_SEED_2243_12_P5_RIGOROUS_UPGRADE_2026-09-19/run/"

def table(name):
    data = (SRC / "inputs" / name).read_bytes()
    historical = subprocess.check_output(["git", "show", BASE + ":" + PREFIX + name], cwd=REPO)
    assert historical == data
    rows = [line.split() for line in data.decode().splitlines() if line and not line.startswith("#")]
    return {int(x): Fraction(y) for x,y,_ in rows}, sha256(data).hexdigest()

top, top_hash = table("SYMBOLS_m25.txt")
low, low_hash = table("SYMBOLS_m5.txt")
assert set(top) == {x for x in range(25) if x % 5}
assert set(low) == {1,2,3,4}

# Solve omega^(p-1)=1 directly, then enumerate exponent coordinates independently.
teich = [x for x in range(25) if pow(x,4,25) == 1]
assert teich == [1,7,18,24]
coordinate = {}
for j in range(5):
    for omega in teich:
        b = omega * 6**j % 25
        assert b not in coordinate
        coordinate[b] = j
weights = [sum((top[b] for b in top if coordinate[b] == j), Fraction()) for j in range(5)]
jet = [sum((comb(coordinate[b],k)*value for b,value in top.items()), Fraction()) for k in range(5)]
assert weights == [-76,0,-76,76,76]
assert jet == [0,380,608,380,76]
assert sum(low.values()) == 0
hecke = {str(a): [int(sum(top[a+5*j] for j in range(5))), int(-2*low[a])] for a in low}
assert all(v[0] == v[1] for v in hecke.values())
normalized = jet[2]/2
assert normalized == 304
L2 = int(normalized) * pow(3,-2,5) % 5
assert L2 == 1

# Exact integer transfer coefficients, including the n=2 boundary.
transfer = []
for p in [5,7,11,13,17]:
    for n in range(2,6):
        h, modulus = p**(n-2), p**(n-1)
        nu = [sum(comb(k*h,r) for k in range(p)) for r in range(3)]
        assert nu[0] == p and all(x % modulus == 0 for x in nu[1:])
        assert modulus % p == 0 and comb(modulus,2) % modulus == 0
        for alpha in range(1,p):
            assert (alpha*alpha-p) % p != 0
        transfer.append({"p":p,"n":n,"transfer_coefficients":nu,"precision_modulus":modulus})

# The same finite-level image can hide a different quadratic valuation.
sharp = []
for p,n in [(5,2),(5,3),(7,2),(11,2),(17,2)]:
    q = p**(n-1)
    f0 = q
    f1 = q + (p-1)*q
    assert f1 == p*q
    sharp.append({"p":p,"n":n,"quadratic_coefficients":[f0,f1],
                  "difference_multiple":"(p-1)*U*((1+U)^q-1)"})

print(json.dumps({
    "status":"PASS_SEPARATE_SAVED_TABLE_AND_TRANSFER_CHECK",
    "historical_commit":BASE,
    "historical_table_bytes_match":True,
    "sha256":{"SYMBOLS_m25.txt":top_hash,"SYMBOLS_m5.txt":low_hash},
    "teichmuller_mod25":teich,
    "gamma_weights":[int(x) for x in weights],
    "raw_jet_degrees_0_through_4":[int(x) for x in jet],
    "exact_hecke_rows":hecke,
    "lower_transfer_is_exactly_zero":True,
    "neron_moment":int(normalized),
    "standard_L2_mod5":L2,
    "transfer_controls":transfer,
    "precision_controls":sharp,
    "new_modular_symbol_evaluations":0,
    "original_arb_core_replayed":False,
    "tower_theorem_verified_by_this_script":False
},indent=2,sort_keys=True))
