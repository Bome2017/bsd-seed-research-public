#!/usr/bin/env python3
"""Classify the acceptance level from the output of `lake env lean WitnessContent/Acceptance.lean`.
A target is CLEAN iff its axioms are a subset of {propext, Classical.choice, Quot.sound}."""
import re, sys
PREFIX = "WitnessContent."
CORE = "lemmaA_comm,gr_killed_by_exponent,depth_spec,zero_infinitely_divisible,hInf_lt_top_iff,hInf_le_iff,JE_bounds,WC_abstract,CM_uniform_denominator,CM_nonzero_everywhere,WC_abstract_nonvacuous".split(",")
FULL = "gr_p_primary,bridge_517,cls2_zero_iff,WC_groupRing,padicInt_units,units_exponent".split(",")
STRETCH = "lemmaA_general,gr_finite_Z,gr_rational_trivial".split(",")
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
level = "A1_FULL" if full_ok else ("A1_CORE" if core_ok else "BELOW_A1_CORE")
first = next((n for n in CORE + FULL if st[n] != "CLEAN"), None)
print("LEVEL:", level)
print("FIRST_NOT_CLEAN_TARGET:", first)
print("STRETCH_CLEAN:", [n for n in STRETCH if st[n] == "CLEAN"])
