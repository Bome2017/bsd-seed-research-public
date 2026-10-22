/* dft_mantissa_probe.c -- acb_dft rounding radius on EXACT inputs: short (21-bit) versus long (110-bit) mantissas, same
 * magnitude (~1e-3). Diagnostic for the v2.1 merge, whose exact class sums are 120-bit dyadics. */
#include <flint/acb.h>
#include <flint/acb_dft.h>
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <math.h>
static uint64_t sm(uint64_t x) { x += 0x9E3779B97F4A7C15ULL; x = (x ^ (x >> 30)) * 0xBF58476D1CE4E5B9ULL; x = (x ^ (x >> 27)) * 0x94D049BB133111EBULL; return x ^ (x >> 31); }
int main(int argc, char **argv) {
  long m = atol(argv[1]); int longm = atoi(argv[2]); slong prec = argc > 3 ? atol(argv[3]) : 128;
  acb_ptr v = _acb_vec_init(m), w = _acb_vec_init(m); fmpz_t z; fmpz_init(z);
  for (long k = 0; k < m; k++) {
    if (longm) { fmpz_set_ui(z, sm(3 * k) >> 18); fmpz_mul_2exp(z, z, 64); fmpz_add_ui(z, z, sm(3 * k + 1)); if (sm(3 * k + 2) & 1) fmpz_neg(z, z);   /* ~110-bit */
      arb_set_fmpz(acb_realref(v + k), z); arb_mul_2exp_si(acb_realref(v + k), acb_realref(v + k), -120); }
    else { arb_set_si(acb_realref(v + k), (slong)(sm(k) % 2000001) - 1000000); arb_mul_2exp_si(acb_realref(v + k), acb_realref(v + k), -30); } }
  acb_dft(w, v, m, prec);
  double mx = 0; for (long j = 0; j < m; j++) { double r = mag_get_d(arb_radref(acb_realref(w + j))); if (r > mx) mx = r; }
  double mv = 0; for (long k = 0; k < m; k++) { double a = fabs(arf_get_d(arb_midref(acb_realref(v + k)), ARF_RND_NEAR)); if (a > mv) mv = a; }
  printf("m %ld mantissa %s prec %ld  max|v| %.3e  max rad(Re F_j) %.4e\n", m, longm ? "long(~110b)" : "short(21b)", (long)prec, mv, mx); return 0; }
