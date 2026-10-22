#!/usr/bin/env python3
"""S4: all-in cost model for the 2243 certificate (per-symbol T_min route, and the scalar nonzero-only screen for
comparison), assembled ONLY from measured component rates (S3 benchmark + feasibility measurements).

Components (as requested): production, verification, traversal, kernel, interval (fixed-point) summation,
checkpointing, storage; plus merge and the final length-m DFT. Wall and money are sensitivity tables, not quotes.
Usage: python3 S4_cost_model.py S3_bench/rates.json
"""
import json, math, sys

def primes_upto(x):
    L = math.log(x); return x / L * (1 + 1 / L + 2 / L**2 + 6 / L**3)

def integral_over_primes(fun, T, steps=4000):
    s, x0 = 0.0, 2.0
    for i in range(steps):
        xa = x0 * (T / x0) ** (i / steps); xb = x0 * (T / x0) ** ((i + 1) / steps); xm = math.sqrt(xa * xb)
        s += fun(xm) / math.log(xm) * (xb - xa)
    return s

def fit_quarter(points):
    """least squares c(q) = a + b q^(1/4) through measured (q, seconds_per_prime) points"""
    xs = [q ** 0.25 for q, _ in points]; ys = [c for _, c in points]; n = len(xs)
    mx, my = sum(xs) / n, sum(ys) / n
    b = sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / sum((x - mx) ** 2 for x in xs); a = my - b * mx
    return a, b

def fit_log2(points):
    xs = [math.log2(q) for q, _ in points]; ys = [c for _, c in points]; n = len(xs)
    mx, my = sum(xs) / n, sum(ys) / n
    b = sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / sum((x - mx) ** 2 for x in xs); a = my - b * mx
    return a, b

def model(r, T):
    ap, bp = fit_quarter(r["producer_points"]); av, bv = fit_log2(r["verifier_points"])
    prod = integral_over_primes(lambda q: max(ap + bp * q ** 0.25, 0.0), T) / 3600
    ver = integral_over_primes(lambda q: max(av + bv * math.log2(q), 0.0), T) / 3600
    nblk = T / 2 ** 22
    trav_S = nblk * r["S_block_traversal_s"] / 3600
    nterm_L, nterm_S = r["L_terms_per_T"] * T, r["S_terms_per_T"] * T
    kern = (nterm_L * r["L_kernel_s_per_term"] + nterm_S * r["S_kernel_s_per_term"]) / 3600
    summ = (nterm_L * r["L_sum_s_per_term"] + nterm_S * r["S_sum_s_per_term"]) / 3600
    trav_L = r["L_traversal_s_per_segment"] * (T / 2 ** 24) / 3600
    ckpt = r["ckpt_write_s"] * r["ckpts_per_worker_hour"] * (prod + ver + trav_S + trav_L + kern + summ) / 3600 / 3600 * 3600
    final = (r["dft_s"] + r["merge_s_per_worker"] * r["workers"]) / 3600
    return dict(production=prod, verification=ver, traversal=trav_S + trav_L, kernel=kern, summation=summ,
                checkpointing=ckpt, merge_and_dft=final)

if __name__ == "__main__":
    r = json.load(open(sys.argv[1]))
    for label, T in r["targets"]:
        m = model(r, T); tot = sum(m.values())
        print(f"== {label}: T = {T:.4e}, primes ~ {primes_upto(T):.3e}")
        for k, v in m.items(): print(f"   {k:15s} {v:12.4e} CPU-h  ({100 * v / tot:5.1f}%)")
        print(f"   {'TOTAL':15s} {tot:12.4e} CPU-h")
