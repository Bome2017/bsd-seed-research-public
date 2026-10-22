#!/usr/bin/env python3
"""Read-only trace of the D=-23 twist records in the supplied archives.

Run from project/ after `python3 prepare_reference.py`. Uses only the Python
standard library. It does NOT recompute L'(E^{-23},1). It checks:
  1. custody: which files of the 2026-09-21 certificate directory are present
     and whether they match that directory's MANIFEST.sha256 and the hash
     fields inside RESULT.json / BUILD_BINDINGS.json;
  2. exact arithmetic: the tail bound (2) of MCS_TWIST_IDEAL_REVIEW.md at the
     run cutoff, and the endpoint arithmetic 2S_T -/+ (err + tail);
  3. exact arithmetic: twist root-number sign from the Kronecker symbols;
  4. that the two Weierstrass models used in the record have equal c4, c6;
  5. the 2026-10-06 floating-point value, re-derived from the shipped bucket
     sums (post-processing only; the coefficient engine is not rerun).
"""
import hashlib, json, os, sys
from decimal import Decimal as Dm, getcontext
from fractions import Fraction as F

getcontext().prec = 80
H = lambda p: hashlib.sha256(open(p, 'rb').read()).hexdigest()
CERT = ("reading_set/BSD_SEED_ARISTOTLE_2026-10-05/working_set/repo/evidence/src/"
        "BSD_CODEX6_MASTER_HANDOFF_2026-09-19/_work/d23_twist_2026-09-21")
W3 = ("current_overlay/BSD_CURRENT_OVERLAY_2026-10-06/current_lab/work/returns/"
      "BSD_ARISTOTLE_W3_P17_P19_RETURN_2026-10-06")
out = {}

# 1. custody
present, missing, mismatch = [], [], []
for line in open(os.path.join(CERT, "MANIFEST.sha256")):
    parts = line.split(None, 1)
    if len(parts) < 2 or not parts[1].strip():
        continue
    h, f = parts[0], parts[1].strip()
    p = os.path.join(CERT, f)
    if os.path.exists(p):
        (present if H(p) == h else mismatch).append(f)
    else:
        missing.append(f)
res = json.load(open(os.path.join(CERT, "RESULT.json")))
bb = json.load(open(os.path.join(CERT, "BUILD_BINDINGS.json")))
ib = json.load(open(os.path.join(CERT, "INPUT_BINDINGS.json")))
out["custody"] = {
    "manifest_entries_present_and_matching": len(present),
    "manifest_entries_mismatching": mismatch,
    "manifest_entries_absent": len(missing),
    "absent_atomic_units": sum(1 for m in missing if m.startswith("run_T3456106495/")),
    "absent_other": [m for m in missing if not m.startswith("run_T3456106495/")],
    "RESULT.input_bindings_sha256_matches": H(os.path.join(CERT, "INPUT_BINDINGS.json")) == res["input_bindings_sha256"],
    "RESULT.build_bindings_sha256_matches": H(os.path.join(CERT, "BUILD_BINDINGS.json")) == res["build_bindings_sha256"],
    "RESULT.engine_log_sha256_matches": H(os.path.join(CERT, "run_T3456106495.log")) == res["engine_log_sha256"],
    "RESULT.combine_log_sha256_matches": H(os.path.join(CERT, "combine_T3456106495.log")) == res["combine_log_sha256"],
    "build_bound_files_present": {n: os.path.exists(os.path.join(CERT, n)) for n in bb["sha256"]},
    "coefficient_corpus_paths_are_external_host_paths": all(
        s["coefficients"]["path"].startswith("/Users/") for s in ib["segments"]),
    "input_bindings_witness_replay": ib.get("witness_replay"),
}

# 2. tail bound and endpoint arithmetic (exact decimals, 80 digits)
pi = Dm("3.1415926535897932384626433832795028841971693993751058209749445923078164062862")
N, T, D = 6503188012738584, 3456106495, 23
c = 2 * pi / (D * Dm(N).sqrt())
cT = c * T
B = 2 * (-cT).exp() * (2 * Dm(T).sqrt() / cT
        + Dm(T) ** Dm("-0.5") / cT * ((Dm(T).ln() + 2) / c + 1 / (T * c * c)))
S, err = Dm("39.847278312318874"), Dm("4.28e-16")
lo, hi = S - err - B, S + err + B
out["tail_and_endpoints"] = {
    "c": str(c)[:40], "tail_bound_B": str(B)[:40],
    "log_TAIL_BOUND": "0.3350417970483208239547061 +/- 1.74e-26",
    "lower": str(lo)[:30], "upper": str(hi)[:30],
    "inside_[39.512236,40.182321]": lo >= Dm("39.512236") and hi <= Dm("40.182321"),
}

# 3. root number sign of the twist
def factor(n):
    f, p = {}, 2
    while p * p <= n:
        while n % p == 0:
            f[p] = f.get(p, 0) + 1; n //= p
        p += 1
    if n > 1: f[n] = f.get(n, 0) + 1
    return f
fac = factor(N)
def chi(q):  # Kronecker (-23/q); -23 = 1 mod 8 gives chi(2)=+1
    if q == 2: return 1 if (-23) % 8 == 1 else -1
    r = pow((-23) % q, (q - 1) // 2, q)
    return -1 if r == q - 1 else r
sign = -1  # chi(-1) = -1 for the odd character
for q, k in fac.items(): sign *= chi(q) ** k
out["root_number"] = {"N_factorization": {str(k): v for k, v in fac.items()},
                      "chi(q)": {str(q): chi(q) for q in fac},
                      "chi(-N)": sign, "w(E^-23)=chi(-N)*w(E) with imported w(E)=+1": sign}

# 4. models
def c4c6(a1, a2, a3, a4, a6):
    b2 = a1*a1 + 4*a2; b4 = 2*a4 + a1*a3; b6 = a3*a3 + 4*a6
    return b2*b2 - 24*b4, -b2**3 + 36*b2*b4 - 216*b6
out["models_equal_c4_c6"] = c4c6(0, -1, 0, -66020924, -65074271436) == c4c6(0, -22735, 0, 106272484, 0)

# 5. floating-point value of 2026-10-06 from shipped bucket sums
def load(name):
    Sb = {}
    for line in open(os.path.join(W3, "w3_p17", "runs", name)):
        w = line.split()
        if w and w[0] == "S": Sb[int(w[2])] = float(w[3])
    return Sb
leg = lambda b: 0 if b % 23 == 0 else (1 if pow(b, 11, 23) == 1 else -1)
Sb = load("twist23_E1_tf3.out")
Lp = 2 * sum(leg(b) * Sb[b] for b in range(23))
Sa, Sc = load("twist23_E1_tf3_xs0.833.out"), load("twist23_E1_tf3_xs1.2.out")
Lt = sum(leg(b) * (Sa[b] + Sc[b]) for b in range(23))
out["float_2026_10_06"] = {"L_prime": Lp, "split_t_1.2": Lt, "fe_discrepancy": abs(Lt - Lp),
                           "minus_certified_partial_2S_T": Lp - 39.847278312318874,
                           "inside_certified_interval": 39.512236 <= Lp <= 40.182321}
json.dump(out, sys.stdout, indent=1); print()
