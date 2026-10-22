/* kolyvagin_scan.c -- read the CERTIFIED verified a_q corpus of the p = 3 run (segments 0..884, q < 885*2^24) and list the
 * primes l with l = 1 (mod 2243) and a_l = 2 = l + 1 (mod 2243): the Kolyvagin primes for p = 2243 (Kurihara numbers of
 * rank 2 need two of them; the cusp denominator is l1*l2). Reads only; produces no coefficient. */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
int main(void) {
  const long SEGQ = 1L << 24, NSEG = 885, P = 2243; const char *dir = "/Users/bsm/BSD_SEED_2243_12_P3_RIGOROUS_RUN_2026-09-19/run/ap";
  long lim = 130000; char *isp = calloc(lim + 1, 1); long *sp = malloc(sizeof(long) * lim), nsp = 0;
  for (long i = 2; i <= lim; i++) if (!isp[i]) { sp[nsp++] = i; for (long j = i * i; j <= lim; j += i) isp[j] = 1; }
  unsigned char *comp = malloc(SEGQ); int32_t *buf = malloc(4 * SEGQ); long found = 0, cand = 0;
  for (long s = 0; s < NSEG; s++) {
    long lo = s * SEGQ, hi = lo + SEGQ; memset(comp, 0, SEGQ); if (lo == 0) comp[0] = comp[1] = 1;
    for (long i = 0; i < nsp && sp[i] * sp[i] < hi; i++) { long p = sp[i], st = (lo + p - 1) / p * p; if (st < p * p) st = p * p; for (long x = st; x < hi; x += p) comp[x - lo] = 1; }
    long np = 0; for (long q = lo; q < hi; q++) np += !comp[q - lo];
    char fn[512]; snprintf(fn, sizeof fn, "%s/ap_%06ld.bin", dir, s); FILE *f = fopen(fn, "rb"); if (!f) { fprintf(stderr, "missing %s\n", fn); return 1; }
    if ((long)fread(buf, 4, np, f) != np) { fprintf(stderr, "short %s\n", fn); return 1; } fclose(f);
    long i = 0;
    for (long q = lo; q < hi; q++) { if (comp[q - lo]) continue; int32_t a = buf[i++];
      if (q % P == 1) { cand++; long r = ((long)a - 2) % P; if (r < 0) r += P; if (r == 0) { found++; if (found <= 12) printf("KOLYVAGIN l = %ld  a_l = %d\n", q, a); } } } }
  printf("scanned q < %ld: primes l = 1 mod %ld: %ld; with a_l = 2 mod %ld: %ld\n", NSEG * SEGQ, P, cand, P, found);
  return 0; }
