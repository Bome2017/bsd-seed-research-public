#!/usr/bin/env python3
"""Recalculated workload for the routes of 02_DERIVATION.md, using the pinned S4 cost model read-only
(run with python3 -B so nothing is written into the pilot-prep folder). Unit: local core-hours (lch)."""
import math, sys
sys.dont_write_bytecode = True
sys.path.insert(0, '/Users/bsm/BSD_2243_PILOT_PREP_2026-09-22/S4_cost')
from cost_model_s4 import model

p = 2243
N = 2**3 * 3 * 2243 * 4547**2 * 5843
Q = N // p
scale = p * p * math.sqrt(Q)
kappa = 2 * math.pi / scale
T_run = 39119887532031
maxG = 366.262                                   # checks/p2243_relation_rank.txt (s = -1)
T_R6 = T_run + math.ceil(math.log(maxG / 2) / kappa)
T_T5 = 5 * T_run                                  # T_5 route: denominator 5p^2, same kernel ratio
rows = [('R0/R1 current per-symbol (R1 leaves T unchanged)', T_run),
        ('R6 aggregation to column classes (Gauss-period tail)', T_R6),
        ('R3 T_5 relation (denominator 5p^2; sums only)', T_T5)]
print(f"kappa = {kappa:.6e}  scale = {scale:.4e}")
base = None
for label, T in rows:
    c, su, lch, sto = model(T)
    tot = sum(lch.values())
    base = base or tot
    prod = lch['production'] / tot
    note = '  [producer rate extrapolated above 1.687e14]' if T > 1.687e14 else ''
    print(f"{label:55s} T = {T:.4e} ({T / T_run:6.3f}x)  total {tot:12.1f} lch ({tot / base:6.3f}x)  production {100 * prod:4.1f}%{note}")
K_n = 224829349 * 240431657
print(f"R7 Kurihara n = {K_n} : cutoff ~ {K_n * math.sqrt(N) * T_run / scale:.3e} ({K_n * math.sqrt(N) / scale:.3e}x) -- not modelled (outside every measured range)")
