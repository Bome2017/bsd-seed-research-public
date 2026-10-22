#!/usr/bin/env python3
"""v2 -> v2.1 (merge only; accumulation, checkpoints and digests unchanged).
Defect (found by dft_radius_probe): acb_dft at prime length 2243 (Bluestein/Rader) inflates INPUT radii ~1.7e3x over the l1
bound; the v2 merge fed every class sum with the GLOBAL rounding tally E as its radius, so at m = 2243^2 the symbol radii
would exceed 1/2048 and the run would end with unidentified symbols (fail closed, but a wasted run).
Fix: class sums enter the symbol computation as EXACT dyadic midpoints (radius 0); the accumulated rounding is added once per
symbol as 2E: the true class sums are mid_k + e_k with sum_k |e_k| <= E (each term's bound is charged to exactly one class),
and |cos|, |sin| combinations are <= 2 in absolute value, so |sum_k e_k c_k(b)| <= 2E -- the same l1 argument the certified
core uses for the tail (2 tail_MS). The merge also prints the per-symbol radius budget against 1/(2 LATDEN)."""
p = '/Users/bsm/BSD_2243_PILOT_PREP_2026-09-22/S5_pipeline/acc2243v2.c'; s = open(p).read()
old1 = '''    for (u64 k = 0; k < MM && MM <= 400; k++) printf("S %llu %s\\n", (unsigned long long)k, arb_get_str(S + k, 25, 0));'''
new1 = '''    for (u64 k = 0; k < MM && MM <= 400; k++) printf("S %llu %s\\n", (unsigned long long)k, arb_get_str(S + k, 25, 0));
    /* v2.1: the printed S_k balls carry the global tally E (a valid per-class enclosure). For the SYMBOLS the class sums are used
       as EXACT midpoints and the accumulated rounding is added once per symbol as 2E (l1 bound: sum_k |e_k| <= E, combination
       coefficients <= 2 in absolute value) -- per-class radii would be inflated by acb_dft's Bluestein/Rader steps. */
    for (u64 k = 0; k < MM; k++) mag_zero(arb_radref(S + k));
    { arf_t ue; arf_init(ue); arb_get_ubound_arf(ue, er, NPREC); arf_mul_2exp_si(ue, ue, 1); arf_add(ub, ub, ue, NPREC, ARF_RND_UP); arf_clear(ue); }'''
assert s.count(old1) == 1; s = s.replace(old1, new1)
old2 = '''    periods(om_p, om_m, NPREC); printf("OMEGA_PLUS %s\\nOMEGA_MINUS %s\\n", arb_get_str(om_p, 30, 0), arb_get_str(om_m, 30, 0));'''
new2 = '''    periods(om_p, om_m, NPREC); printf("OMEGA_PLUS %s\\nOMEGA_MINUS %s\\n", arb_get_str(om_p, 30, 0), arb_get_str(om_m, 30, 0));
    { arb_t bt, br, bl; arb_init(bt); arb_init(br); arb_init(bl); arf_t tt; arf_init(tt); tail_ms(bt, KAPPA, T); arb_mul_2exp_si(bt, bt, 1); arb_div(bt, bt, om_p, NPREC);
      arb_mul_2exp_si(br, er, 1); arb_div(br, br, om_p, NPREC); arb_set_ui(bl, 1); arb_div_ui(bl, bl, 2 * (ulong)LATDEN, NPREC);
      printf("SYMBOL_RADIUS_BUDGET plus: tail 2tail/Omega+ %s + rounding 2E/Omega+ %s (+ transform rounding, printed per symbol) vs threshold 1/(2 LATDEN) %s\\n",
             arb_get_str(bt, 6, ARB_STR_NO_RADIUS), arb_get_str(br, 6, ARB_STR_NO_RADIUS), arb_get_str(bl, 6, ARB_STR_NO_RADIUS));
      arb_clear(bt); arb_clear(br); arb_clear(bl); arf_clear(tt); }'''
assert s.count(old2) == 1; s = s.replace(old2, new2)
old3 = '''    printf("XB_PLUS_DETERMINED %ld of %ld (lattice 1/%ld Z)   minus determined %ld\\n", ndet, nb, LATDEN, ndetm);'''
new3 = '''    printf("XB_PLUS_DETERMINED %ld of %ld (lattice 1/%ld Z)   minus determined %ld   max plus radius %.6e (unique iff < %.6e)\\n", ndet, nb, LATDEN, ndetm, maxrad, 0.5 / (double)LATDEN);'''
assert s.count(old3) == 1; s = s.replace(old3, new3)
old4 = '''      arb_div(re, re, om_p, PREC); arb_div(im, im, om_m, PREC); arb_set(XR + b, re);'''
new4 = '''      arb_div(re, re, om_p, PREC); arb_div(im, im, om_m, PREC); arb_set(XR + b, re);
      { double rr = mag_get_d(arb_radref(re)); if (rr > maxrad) maxrad = rr; }'''
assert s.count(old4) == 1; s = s.replace(old4, new4)
old5 = '''    fmpq_t fr; fmpq_init(fr); arf_t ra; arf_init(ra); long ndet = 0, nb = 0, ndetm = 0;'''
new5 = '''    fmpq_t fr; fmpq_init(fr); arf_t ra; arf_init(ra); long ndet = 0, nb = 0, ndetm = 0; double maxrad = 0;'''
assert s.count(old5) == 1; s = s.replace(old5, new5)
old6 = ''' *      m > 400 the identified symbols go to outdir/symbols.bin with its SHA-256; ACC_NOSYMBOLS=1 skips symbol extraction.'''
new6 = ''' *      m > 400 the identified symbols go to outdir/symbols.bin with its SHA-256; ACC_NOSYMBOLS=1 skips symbol extraction.
 *  v2.1 (merge only): class sums enter the symbol computation as EXACT midpoints; the accumulated rounding tally E is added
 *      once per symbol as 2E (l1 bound), next to the tail term -- acb_dft's Bluestein/Rader steps inflate input radii ~1.7e3x
 *      at prime length 2243 (dft_radius_probe), which made per-class radii unusable at m = 2243^2. SYMBOL_RADIUS_BUDGET and
 *      the maximum symbol radius are printed against 1/(2 LATDEN).'''
assert s.count(old6) == 1; s = s.replace(old6, new6)
open(p, 'w').write(s); print('v2.1 merge patch applied')
