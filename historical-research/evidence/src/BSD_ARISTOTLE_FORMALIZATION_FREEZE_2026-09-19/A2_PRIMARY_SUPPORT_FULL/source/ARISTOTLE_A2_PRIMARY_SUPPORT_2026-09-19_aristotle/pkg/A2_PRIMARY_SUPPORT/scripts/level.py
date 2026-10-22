#!/usr/bin/env python3
"""Classify the acceptance level from the output of `lake env lean PrimarySupport/Acceptance.lean`.
A target is CLEAN iff its axioms are a subset of {propext, Classical.choice, Quot.sound}."""
import re, sys
PREFIX = "PrimarySupport."
CORE = "primary_zero_of_torsionfree,torsion_decomposition,assembly,assembly_WC_shape,JOf_ideal,JOf_ne_zero_iff,positive_depth_divides,content_dvd_iff,content_padic,CM_each_local_finite,CM_finite_support,CM_nonzero_everywhere,CM_profinite_perfectness".split(",")
FULL = "finite_iff_local_and_support,JOf_generator,content_basic,content_unimodular,exists_primitive,content_mod_pk,content_bounds_J,lemmaB_valuation,lemmaB_cokernel,card_eq_prod_primary,order_nine_t_sq,CM_order_441".split(",")
STRETCH = "alternating_square,CM_noncyclic_target,CM_codex_torsion_example".split(",")
OK = {"propext", "Classical.choice", "Quot.sound"}
log = open(sys.argv[1] if len(sys.argv) > 1 else "axioms.log").read()
def status(name):
    full = re.escape(PREFIX + name)
    if re.search(r"'%s' does not depend on any axioms" % full, log):
        return "CLEAN"
    m = re.search(r"'%s' depends on axioms: \[(.*?)\]" % full, log, re.S)
    if not m:
        return "MISSING"
    bad = [a.strip() for a in m.group(1).replace("\n", " ").split(",") if a.strip() not in OK]
    return "CLEAN" if not bad else "USES:" + ",".join(bad)
st = {n: status(n) for n in CORE + FULL + STRETCH}
for group, names in (("CORE", CORE), ("FULL", FULL), ("STRETCH", STRETCH)):
    for n in names:
        print(f"{group:8s} {n:32s} {st[n]}")
core_ok = all(st[n] == "CLEAN" for n in CORE)
full_ok = core_ok and all(st[n] == "CLEAN" for n in FULL)
level = "A2_FULL" if full_ok else ("A2_CORE" if core_ok else "BELOW_A2_CORE")
first = next((n for n in CORE + FULL if st[n] != "CLEAN"), None)
print("LEVEL:", level)
print("FIRST_NOT_CLEAN_TARGET:", first)
print("STRETCH_CLEAN:", [n for n in STRETCH if st[n] == "CLEAN"])
