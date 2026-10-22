/* reviewer's check of the FLINT acb_dft sign convention against a direct sum w_j = sum_k v_k exp(-2 pi i jk/n) */
#include <flint/acb.h>
#include <flint/acb_dft.h>
#include <flint/fmpq.h>
#include <stdio.h>
int main(void) {
  long lens[] = {7, 27, 81, 2243, 6561};
  for (int t = 0; t < 5; t++) { long n = lens[t]; acb_ptr v = _acb_vec_init(n), w = _acb_vec_init(n), d = _acb_vec_init(n);
    flint_rand_t st; flint_rand_init(st);
    for (long k = 0; k < n; k++) { arb_set_si(acb_realref(v + k), (slong)((k * 7919 + 13) % 2001) - 1000); arb_mul_2exp_si(acb_realref(v + k), acb_realref(v + k), -7); }
    acb_dft(w, v, n, 128);
    long bad = 0; long nchk = n > 300 ? 40 : n;
    arb_t s, c; arb_init(s); arb_init(c); fmpq_t q; fmpq_init(q);
    for (long j = 0; j < nchk; j++) { long jj = (j * 104729) % n; acb_zero(d + jj);
      for (long k = 0; k < n; k++) { fmpq_set_si(q, -2 * ((jj * k) % n), n); arb_sin_cos_pi_fmpq(s, c, q, 128);
        arb_addmul(acb_realref(d + jj), acb_realref(v + k), c, 128); arb_addmul(acb_imagref(d + jj), acb_realref(v + k), s, 128); }
      if (!acb_overlaps(d + jj, w + jj)) bad++; }
    /* opposite convention check: conj */
    long bad2 = 0; for (long j = 0; j < nchk; j++) { long jj = (j * 104729) % n; acb_t cj; acb_init(cj); acb_conj(cj, d + jj); if (!acb_overlaps(cj, w + jj)) bad2++; acb_clear(cj); }
    printf("n %ld checked %ld  mismatches vs exp(-2 pi i jk/n): %ld   mismatches vs exp(+2 pi i jk/n): %ld  sample Im w1 = %s\n", n, nchk, bad, bad2, arb_get_str(acb_imagref(w + 1), 10, 0));
    _acb_vec_clear(v, n); _acb_vec_clear(w, n); _acb_vec_clear(d, n); flint_rand_clear(st); }
  return 0; }
