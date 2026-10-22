/* reviewer's checks of the FLINT primitives add_term and div_period rely on (FLINT 3.3.1):
   (1) mag_get_d(r) >= r (upper bound; exact for representable exponents), then ldexp(.,96) exact
   (2) arf_get_fmpz_fixed_si(z, x, -96): |z 2^-96 - x| < 2^-96 for random x of both signs and many exponents
   (3) div_period(x, om) encloses every X/Om for X in x and Om in om, and compare its radius with plain arb_div */
#include <flint/arb.h>
#include <flint/fmpz.h>
#include <stdio.h>
#include <math.h>
static void div_period(arb_t x, const arb_t om) {   /* verbatim copy of acc2243v2.c v2.3 lines 307-311 */
  mag_t r, lo; mag_init(r); mag_init(lo); mag_set(r, arb_radref(x)); mag_zero(arb_radref(x));
  arb_div(x, x, om, 128); arb_get_mag_lower(lo, om); if (mag_is_zero(lo)) { printf("period ball contains 0\n"); return; }
  mag_div(r, r, lo); arb_add_error_mag(x, r); mag_clear(r); mag_clear(lo);
}
int main(void) {
  flint_rand_t st; flint_rand_init(st);
  long bad1 = 0, bad2 = 0, n1 = 0, n2 = 0;
  arf_t a, b, e; arf_init(a); arf_init(b); arf_init(e); mag_t m; mag_init(m); fmpz_t z; fmpz_init(z);
  for (long i = 0; i < 200000; i++) {
    /* (1) */
    mag_randtest(m, st, 200); double d = mag_get_d(m); arf_set_mag(a, m);
    if (d != INFINITY) { arf_set_d(b, d); if (arf_cmp(b, a) < 0) bad1++; double s = ldexp(d, 96); arf_set_d(e, s); arf_mul_2exp_si(b, b, 96); if (s != INFINITY && arf_cmp(e, b) != 0) bad1++; }
    n1++;
    /* (2) random x with exponent in [-140, 40], both signs, 128-bit mantissas */
    arf_randtest(a, st, 128, 8); arf_mul_2exp_si(a, a, (slong)(n_randint(st, 180)) - 140);
    arf_get_fmpz_fixed_si(z, a, -96); arf_set_fmpz(b, z); arf_mul_2exp_si(b, b, -96);
    arf_sub(e, b, a, ARF_PREC_EXACT, ARF_RND_DOWN); arf_abs(e, e); arf_one(b); arf_mul_2exp_si(b, b, -96);
    if (arf_cmp(e, b) >= 0) bad2++; n2++;
  }
  printf("(1) mag_get_d upper bound + exact ldexp: %ld violations in %ld\n", bad1, n1);
  printf("(2) arf_get_fmpz_fixed_si(.,-96) error >= 2^-96: %ld violations in %ld\n", bad2, n2);
  /* (3) */
  arb_t om, x, y, X, q, lo, hi; arb_init(om); arb_init(x); arb_init(y); arb_init(X); arb_init(q); arb_init(lo); arb_init(hi);
  arb_set_str(om, "[0.0280449015194364044483094018079 +/- 3.04e-32]", 128);
  long bad3 = 0, n3 = 0; double sumratio = 0;
  for (long i = 0; i < 20000; i++) {
    arb_randtest(x, st, 128, 4); arb_get_mid_arb(y, x); arf_set_d(a, 1.4e-5 * (1 + n_randint(st, 100) / 50.0)); arb_add_error_arf(y, a);   /* [mid +- ~1.4e-5] */
    arb_set(X, y); div_period(X, om); arb_div(q, y, om, 128);
    /* endpoints and midpoint of y divided by the endpoints of om, at 512 bits: must be inside X */
    for (int s = -1; s <= 1; s++) for (int t = -1; t <= 1; t += 2) {
      arb_t xe, oe, r; arb_init(xe); arb_init(oe); arb_init(r);
      arf_set_mag(a, arb_radref(y)); arf_mul_si(a, a, s, ARF_PREC_EXACT, ARF_RND_DOWN); arf_add(a, a, arb_midref(y), ARF_PREC_EXACT, ARF_RND_DOWN); arb_set_arf(xe, a);
      arf_set_mag(b, arb_radref(om)); arf_mul_si(b, b, t, ARF_PREC_EXACT, ARF_RND_DOWN); arf_add(b, b, arb_midref(om), ARF_PREC_EXACT, ARF_RND_DOWN); arb_set_arf(oe, b);
      arb_div(r, xe, oe, 512); if (!arb_contains(X, r)) bad3++; n3++; arb_clear(xe); arb_clear(oe); arb_clear(r); }
    sumratio += mag_get_d(arb_radref(q)) / mag_get_d(arb_radref(X));
  }
  printf("(3) div_period enclosure violations: %ld in %ld point checks; mean radius ratio arb_div/div_period = %.6f\n", bad3, n3, sumratio / 20000);
  /* author's motivating case: |x| = 1.5, radius 1.4e-5 */
  arb_set_str(y, "[1.5 +/- 1.4e-5]", 128); arb_set(X, y); div_period(X, om); arb_div(q, y, om, 128);
  printf("    x = [1.5 +/- 1.4e-5]: arb_div radius %.10e, div_period radius %.10e, rad/|om| %.10e\n", mag_get_d(arb_radref(q)), mag_get_d(arb_radref(X)), 1.4e-5 / 0.0280449015194364);
  return 0; }
