/* dft_radius_probe.c -- how acb_dft (FLINT 3.3.1, prec 128) propagates INPUT radii at the production length m = 2243^2.
 * Input: v_k = [mid_k +/- eps] with realistic midpoints (|mid| ~ 1e-3) and a common radius eps (the merge gives every class
 * the global rounding tally). Output: max over j of rad(Re F_j) / (m eps). An ideal l1 propagation gives <= 1 (+ rounding).
 * Also run with eps = 0 to get the DFT's own rounding floor. Diagnostic only; not part of the certified path. */
#include <flint/acb.h>
#include <flint/acb_dft.h>
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <time.h>
static uint64_t sm(uint64_t x) { x += 0x9E3779B97F4A7C15ULL; x = (x ^ (x >> 30)) * 0xBF58476D1CE4E5B9ULL; x = (x ^ (x >> 27)) * 0x94D049BB133111EBULL; return x ^ (x >> 31); }
int main(int argc, char **argv) {
  long m = argc > 1 ? atol(argv[1]) : 5031049; double epsd = argc > 2 ? atof(argv[2]) : 4.4e-16;
  acb_ptr v = _acb_vec_init(m), w = _acb_vec_init(m); mag_t e; mag_init(e); mag_set_d(e, epsd);
  for (long k = 0; k < m; k++) { arb_set_si(acb_realref(v + k), (slong)(sm(k) % 2000001) - 1000000); arb_mul_2exp_si(acb_realref(v + k), acb_realref(v + k), -30);
    if (epsd > 0) arb_add_error_mag(acb_realref(v + k), e); }
  clock_t t0 = clock(); acb_dft(w, v, m, 128); double sec = (double)(clock() - t0) / CLOCKS_PER_SEC;
  double mx = 0, mn = 1e300, sum = 0; for (long j = 0; j < m; j++) { double r = mag_get_d(arb_radref(acb_realref(w + j))); if (r > mx) mx = r; if (r < mn) mn = r; sum += r; }
  double ideal = (double)m * epsd;
  printf("m %ld eps %.3e seconds %.1f  rad(Re F_j): max %.4e min %.4e mean %.4e   max/(m eps) = %.4f\n", m, epsd, sec, mx, mn, sum / m, ideal > 0 ? mx / ideal : 0.0);
  return 0; }
