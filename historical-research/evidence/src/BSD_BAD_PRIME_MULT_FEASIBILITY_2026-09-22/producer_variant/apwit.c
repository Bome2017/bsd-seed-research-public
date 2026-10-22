/* apwit.c -- PRODUCER of a_q witnesses for the rigorous stream core (DESIGN.md O6).
 * usage: apwit a1 a2 a3 a4 a6 T QB SEGQ witdir s0 s1 [fast]
 *   For every segment s in [s0,s1) (q in [s*SEGQ, min((s+1)*SEGQ, T+1))) writes witdir/wit_<s>.bin:
 *     header u64 lo, u64 hi, u64 count; then for every prime q in [lo,hi) with q >= QB and q not dividing Delta:
 *     u64 q, i32 a_q, u8 x0, u8 k, k x (u64 l, u8 e)
 *   Trace: fastap.c (BSGS, seed-type curves with a rational 2-torsion point; flag 'fast') else PARI Fl_elltrace.
 *   Certificate: P = (d x0, d^2) on E_d (short model A4=-27c4, A6=-54c6; d = x0^3+A4x0+A6), h = q+1-(d/q)a;
 *   checks [h]P = O itself (a wrong trace aborts here), ord(P) via PARI Fle_order, then lists the largest prime powers of
 *   ord(P) until their product exceeds 2*isqrt(4q). The verifier (verifier/wverify.c) re-checks everything independently.
 */
#include <pari/pari.h>
#include <stdio.h>
#include <stdint.h>
#include <limits.h>
#include <string.h>
#include <time.h>
long fast_trace(ulong a4, ulong a6, ulong p);                    /* fastap.c (unchanged copy) */

static GEN A4g, A6g, DISCg; static long B2;
static ulong isqrt_u(ulong v) { ulong r = 0; for (int b = 31; b >= 0; b--) { ulong t = r | (1UL << b); if ((unsigned __int128)t * t <= v) r = t; } return r; }

int main(int argc, char **argv) {
  if (argc < 12) { fprintf(stderr, "usage: apwit a1 a2 a3 a4 a6 T QB SEGQ witdir s0 s1 [fast]\n"); return 1; }
  pari_init(64000000, 1000000);
  GEN E = ellinit(mkvecn(5, stoi(atol(argv[1])), stoi(atol(argv[2])), stoi(atol(argv[3])), stoi(atol(argv[4])), stoi(atol(argv[5]))), NULL, DEFAULTPREC);
  A4g = gclone(mulsi(-27, ell_get_c4(E))); A6g = gclone(mulsi(-54, ell_get_c6(E))); DISCg = gclone(ell_get_disc(E));
  B2 = itos(ell_get_b2(E));
  ulong T = strtoul(argv[6], 0, 10), QB = strtoul(argv[7], 0, 10), SEGQ = strtoul(argv[8], 0, 10);
  const char *wd = argv[9]; long s0 = atol(argv[10]), s1 = atol(argv[11]); int fast = (argc > 12 && !strcmp(argv[12], "fast"));
  unsigned char *comp = malloc(SEGQ);
  for (long sg = s0; sg < s1; sg++) {
    ulong lo = (ulong)sg * SEGQ, hi = lo + SEGQ; if (hi > T + 1) hi = T + 1; if (lo >= hi) break;
    clock_t c0 = clock();
    char fn[1024]; snprintf(fn, sizeof fn, "%s/wit_%06ld.bin", wd, sg); FILE *f = fopen(fn, "wb");
    uint64_t hdr[3] = {lo, hi, 0}; fwrite(hdr, 8, 3, f);
    memset(comp, 0, hi - lo); for (ulong n = lo; n < hi && n < 2; n++) comp[n - lo] = 1;       /* producer's own sieve */
    for (ulong p = 2; p * p < hi; p++) { int pr = 1; for (ulong d = 2; d * d <= p; d++) if (p % d == 0) { pr = 0; break; } if (!pr) continue;
      ulong st = (lo + p - 1) / p * p; if (st < p * p) st = p * p; for (ulong m = st; m < hi; m += p) comp[m - lo] = 1; }
    ulong cnt = 0, nfast = 0, nfb = 0, nx0 = 0;
    for (ulong q = (lo < QB ? QB : lo); q < hi; q++) {
      if (comp[q - lo] || umodiu(DISCg, q) == 0) continue;
      pari_sp av = avma;
      ulong a4 = umodiu(A4g, q), a6 = umodiu(A6g, q); long t = LONG_MIN;
      if (fast) { ulong X0 = (ulong)(((3 * B2) % (long)q + (long)q) % (long)q);           /* rational 2-torsion root 3*b2 */
        ulong fx0 = Fl_add(Fl_mul(Fl_sqr(X0, q), X0, q), Fl_add(Fl_mul(a4, X0, q), a6, q), q);
        if (fx0 != 0) { fprintf(stderr, "FATAL: 2-torsion assertion fails at q=%lu\n", q); return 3; }
        t = fast_trace(a4, a6, q); if (t != LONG_MIN) nfast++; }
      if (t == LONG_MIN) { t = Fl_elltrace(a4, a6, q); nfb++; }
      ulong s = isqrt_u(4 * q); int done = 0;
      for (ulong x0 = 1; x0 < 256 && !done; x0++) {
        ulong d = Fl_add(Fl_mul(Fl_sqr(x0 % q, q), x0 % q, q), Fl_add(Fl_mul(a4, x0 % q, q), a6, q), q); if (!d) continue;
        long chi = krouu(d, q); ulong h = (ulong)((long)q + 1 - chi * t);
        ulong a4d = Fl_mul(a4, Fl_sqr(d, q), q);
        GEN P = mkvecsmall2(Fl_mul(d, x0 % q, q), Fl_sqr(d, q));
        GEN Z = Fle_mulu(P, h, a4d, q); if (!ell_is_inf(Z)) { fprintf(stderr, "FATAL: [h]P != O at q=%lu (trace %ld wrong?)\n", q, t); return 3; }
        ulong ord = itou(Fle_order(P, utoi(h), a4d, q)); if (ord <= 2 * s) { nx0++; continue; }
        GEN F = factoru(ord), pr = gel(F, 1), ex = gel(F, 2); long np = lg(pr) - 1;
        ulong pw[64]; long idx[64]; for (long i = 0; i < np; i++) { pw[i] = upowuu(pr[i + 1], ex[i + 1]); idx[i] = i; }
        for (long i = 0; i < np; i++) for (long j = i + 1; j < np; j++) if (pw[idx[j]] > pw[idx[i]]) { long tt = idx[i]; idx[i] = idx[j]; idx[j] = tt; }
        unsigned char k = 0; ulong D = 1; uint64_t ls[64]; unsigned char es[64];
        for (long i = 0; i < np && D <= 2 * s; i++) { D *= pw[idx[i]]; ls[k] = pr[idx[i] + 1]; es[k] = (unsigned char)ex[idx[i] + 1]; k++; }
        uint64_t qq = q; int32_t a32 = (int32_t)t; unsigned char xx = (unsigned char)x0;
        fwrite(&qq, 8, 1, f); fwrite(&a32, 4, 1, f); fwrite(&xx, 1, 1, f); fwrite(&k, 1, 1, f);
        for (int i = 0; i < k; i++) { fwrite(&ls[i], 8, 1, f); fwrite(&es[i], 1, 1, f); }
        cnt++; done = 1;
      }
      if (!done) { fprintf(stderr, "FATAL: no certificate point with x0 < 256 at q=%lu\n", q); return 3; }
      set_avma(av);
    }
    hdr[2] = cnt; fseek(f, 16, SEEK_SET); fwrite(&hdr[2], 8, 1, f); fclose(f);
    printf("SEG %ld lo %lu hi %lu witnesses %lu fast %lu pari %lu retried_x0 %lu cpu %.2f\n", sg, lo, hi, cnt, nfast, nfb, nx0,
           (double)(clock() - c0) / CLOCKS_PER_SEC); fflush(stdout);
  }
  pari_close(); return 0;
}
