/* First-review repair: distinct factors and checked multiplication.
 * Legacy source is preserved in evidence/src. See FIRST_REVIEW.md. */
/* wverify.c -- INDEPENDENT verifier for the rigorous stream core (integer arithmetic only; no PARI, no Arb, no floats in results).
 *  wit a1 a2 a3 a4 a6 T QB SEGQ witdir outdir s0 s1 : check witness segments s0..s1-1; write outdir/ap_<s>.bin (int32 per prime)
 *  an  a1 a2 a3 a4 a6 T SEGQ outdir                  : rebuild a_n (n <= T) from ap_*.bin by a multiplicative sieve; print the
 *                                                      Merkle SHA-256 (leaf = SHA-256 of int64-LE a_n over 2^22-blocks)
 * Certificate for a good prime q >= QB (DESIGN.md O6): record (q,a,x0,k,{l,e}); P = (d x0, d^2) on E_d : Y^2 = X^3 + A4 d^2 X + A6 d^3,
 * d = x0^3 + A4 x0 + A6, h = q+1-(d/q)a; [h]P = O; each l prime, l^e | h, [h/l^(v-e+1)]P != O; D = prod l^e > 2s, exactly one multiple
 * of D in [q+1-s, q+1+s] (s = isqrt(4q)). Then #E_d(F_q) = h (Lagrange + Hasse), so a_q = a. Small/bad q: exhaustive count. */
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <CommonCrypto/CommonDigest.h>
typedef uint64_t u64; typedef int64_t i64; typedef __int128 i128; typedef unsigned __int128 u128;
#define BLK (1ULL << 22)
static u64 Q;                                                     /* current modulus */
static u64 mulm(u64 a, u64 b) { return (u64)((u128)a * b % Q); }
static u64 addm(u64 a, u64 b) { u64 r = a + b; return r >= Q ? r - Q : r; }
static u64 subm(u64 a, u64 b) { return a >= b ? a - b : a + Q - b; }
static u64 powm(u64 a, u64 e) { u64 r = 1 % Q; while (e) { if (e & 1) r = mulm(r, a); a = mulm(a, a); e >>= 1; } return r; }
static u64 invm(u64 a) {                                          /* extended Euclid, independent of any Fermat/Montgomery code */
  i64 t = 0, nt = 1; u64 r = Q, nr = a % Q;
  while (nr) { u64 qq = r / nr, tr = r - qq * nr; r = nr; nr = tr; i64 tt = t - (i64)qq * nt; t = nt; nt = tt; }
  if (r != 1) { fprintf(stderr, "FATAL: non-invertible\n"); exit(2); }
  return t < 0 ? (u64)(t + (i64)Q) : (u64)t;
}
static u64 modz(i128 v) { i128 r = v % (i128)Q; if (r < 0) r += Q; return (u64)r; }
static int euler(u64 a) { a %= Q; if (!a) return 0; return powm(a, (Q - 1) / 2) == 1 ? 1 : -1; }
static int isprime64(u64 n) {                                     /* deterministic Miller-Rabin for n < 2^64 */
  if (n < 2) return 0; static const u64 sp[] = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37};
  for (int i = 0; i < 12; i++) { if (n == sp[i]) return 1; if (n % sp[i] == 0) return 0; }
  u64 d = n - 1; int s = 0; while (!(d & 1)) { d >>= 1; s++; }
  static const u64 B[] = {2, 325, 9375, 28178, 450775, 9780504, 1795265022}; u64 sv = Q; Q = n;
  for (int i = 0; i < 7; i++) { u64 a = B[i] % n; if (!a) continue; u64 x = powm(a, d); if (x == 1 || x == n - 1) continue;
    int ok = 0; for (int r = 1; r < s && !ok; r++) { x = mulm(x, x); if (x == n - 1) ok = 1; } if (!ok) { Q = sv; return 0; } }
  Q = sv; return 1;
}
typedef struct { u64 x, y; int inf; } pt;                         /* affine point on Y^2 = X^3 + CA X + CB over F_Q */
static u64 CA;
static pt padd(pt P, pt R) {
  if (P.inf) return R; if (R.inf) return P; u64 l;
  if (P.x == R.x) { if (addm(P.y, R.y) == 0) { pt o = {0, 0, 1}; return o; }
    l = mulm(addm(mulm(3, mulm(P.x, P.x)), CA), invm(addm(P.y, P.y))); }
  else l = mulm(subm(R.y, P.y), invm(subm(R.x, P.x)));
  pt S; S.inf = 0; S.x = subm(subm(mulm(l, l), P.x), R.x); S.y = subm(mulm(l, subm(P.x, S.x)), P.y); return S;
}
static pt pmul(pt P, u64 n) { pt A = {0, 0, 1}; for (int b = 63; b >= 0; b--) { A = padd(A, A); if ((n >> b) & 1) A = padd(A, P); } return A; }
static u64 isqrt64(u64 v) { u64 r = 0; for (int b = 31; b >= 0; b--) { u64 t = r | (1ULL << b); if ((u128)t * t <= v) r = t; } return r; }
/* curve data */
static i64 a1, a2, a3, a4, a6; static i128 b2, b4, b6, c4, c6, DISC;
static void invariants(void) {
  b2 = (i128)a1 * a1 + 4 * (i128)a2; b4 = 2 * (i128)a4 + (i128)a1 * a3; b6 = (i128)a3 * a3 + 4 * (i128)a6;
  i128 b8 = (i128)a1 * a1 * a6 + 4 * (i128)a2 * a6 - (i128)a1 * a3 * a4 + (i128)a2 * a3 * a3 - (i128)a4 * a4;
  c4 = b2 * b2 - 24 * b4; c6 = -b2 * b2 * b2 + 36 * b2 * b4 - 216 * b6;
  DISC = -b2 * b2 * b8 - 8 * b4 * b4 * b4 - 27 * b6 * b6 + 9 * b2 * b4 * b6;
}
static i64 brute_ap(u64 q) {                                      /* a_q = q + 1 - #E~(F_q) on the (minimal) model, singular pt included */
  if (q == 2) { i64 c = 1; for (int x = 0; x < 2; x++) for (int y = 0; y < 2; y++) {
      i128 v = (i128)y * y + (i128)a1 * x * y + (i128)a3 * y - ((i128)x * x * x + (i128)a2 * x * x + (i128)a4 * x + a6);
      if (v % 2 == 0) c++; }
    return 3 - c; }
  Q = q; u64 B2 = modz(b2), B4 = modz(2 * b4), B6 = modz(b6); i64 s = 0;
  for (u64 x = 0; x < q; x++) s += euler(addm(addm(mulm(mulm(4 % q, x), mulm(x, x)), mulm(B2, mulm(x, x))), addm(mulm(B4, x), B6)));
  return -s;
}
static int vq(i128 v, u64 q) { int e = 0; if (v == 0) return 99; while (v % (i128)q == 0) { v /= (i128)q; e++; } return e; }
static void sieve_seg(u64 lo, u64 hi, unsigned char *comp) {    /* comp[i] = 1 iff lo+i is not prime */
  memset(comp, 0, hi - lo); for (u64 n = lo; n < hi && n < 2; n++) comp[n - lo] = 1;
  for (u64 p = 2; p * p < hi; p++) { int pr = 1; for (u64 d = 2; d * d <= p; d++) if (p % d == 0) { pr = 0; break; } if (!pr) continue;
    u64 st = (lo + p - 1) / p * p; if (st < p * p) st = p * p; for (u64 m = st; m < hi; m += p) comp[m - lo] = 1; }
}
static int rd(FILE *f, void *p, size_t n) { return fread(p, 1, n, f) == n; }
static void hexdig(const unsigned char *d, char *out) { for (int i = 0; i < 32; i++) sprintf(out + 2 * i, "%02x", d[i]); }
__attribute__((noreturn)) static void fail(u64 q, const char *why) { fprintf(stderr, "FATAL: q=%llu: %s\n", (unsigned long long)q, why); exit(3); }

static int check_witness(u64 q, FILE *f, i64 *aout) {
  u64 qr; int32_t a; unsigned char x0, k;
  if (!rd(f, &qr, 8) || !rd(f, &a, 4) || !rd(f, &x0, 1) || !rd(f, &k, 1)) fail(q, "truncated witness");
  if (qr != q) fail(q, "record q differs from the verifier's own next prime (segment misalignment)");
  if ((i128)a * a > (i128)4 * q) fail(q, "Hasse bound violated");
  Q = q; u64 A4 = modz(-27 * c4), A6 = modz(-54 * c6), X0 = x0 % q;
  u64 d = addm(addm(mulm(mulm(X0, X0), X0), mulm(A4, X0)), A6); if (!d) fail(q, "d = f(x0) = 0");
  int chi = euler(d); i64 h = (i64)q + 1 - (i64)chi * a;
  CA = mulm(A4, mulm(d, d)); u64 CB = mulm(A6, mulm(d, mulm(d, d)));
  pt P = {mulm(d, X0), mulm(d, d), 0};
  if (mulm(P.y, P.y) != addm(addm(mulm(P.x, mulm(P.x, P.x)), mulm(CA, P.x)), CB)) fail(q, "P not on E_d");
  if (!pmul(P, (u64)h).inf) fail(q, "[h]P != O");
  u64 D = 1, seen[256];
  for (int i = 0; i < k; i++) { u64 l; unsigned char e; if (!rd(f, &l, 8) || !rd(f, &e, 1)) fail(q, "truncated factor list");
    if (!isprime64(l) || e == 0) fail(q, "factor not prime"); Q = q;
    for (int j = 0; j < i; j++) if (seen[j] == l) fail(q, "duplicate prime factor");
    seen[i] = l;
    u64 hh = (u64)h; int v = 0; while (hh % l == 0) { hh /= l; v++; } if (v < e) fail(q, "l^e does not divide h");
    u64 m = (u64)h; for (int j = 0; j < v - e + 1; j++) m /= l;
    if (pmul(P, m).inf) fail(q, "order certificate: [h/l^(v-e+1)]P = O");
    for (int j = 0; j < e; j++) { if (D > (u64)h / l) fail(q, "D exceeds h or overflows"); D *= l; } }
  u64 s = isqrt64(4 * q), lo = q + 1 - s, hi = q + 1 + s;
  if (D <= 2 * s) fail(q, "D <= 2s: uniqueness not implied");
  if (hi / D - (lo - 1) / D != 1 || (u64)h % D) fail(q, "not exactly one multiple of D in the Hasse interval");
  *aout = a; return 1;
}

int main(int argc, char **argv) {
  if (argc < 9) { fprintf(stderr, "usage: see header\n"); return 1; }
  a1 = atoll(argv[2]); a2 = atoll(argv[3]); a3 = atoll(argv[4]); a4 = atoll(argv[5]); a6 = atoll(argv[6]); invariants();
  u64 T = strtoull(argv[7], 0, 10);
  if (!strcmp(argv[1], "wit")) {
    u64 QB = strtoull(argv[8], 0, 10), SEGQ = strtoull(argv[9], 0, 10); const char *wd = argv[10], *od = argv[11];
    long s0 = atol(argv[12]), s1 = atol(argv[13]); unsigned char *comp = malloc(SEGQ);
    for (long sg = s0; sg < s1; sg++) {
      u64 lo = (u64)sg * SEGQ, hi = lo + SEGQ; if (hi > T + 1) hi = T + 1; if (lo >= hi) break;
      char fn[1024]; snprintf(fn, sizeof fn, "%s/wit_%06ld.bin", wd, sg); FILE *f = fopen(fn, "rb"); if (!f) fail(lo, "missing witness file");
      u64 hlo, hhi, hcnt; if (!rd(f, &hlo, 8) || !rd(f, &hhi, 8) || !rd(f, &hcnt, 8)) fail(lo, "bad header");
      if (hlo != lo || hhi != hi) fail(lo, "segment boundaries differ from the verifier's tiling");
      snprintf(fn, sizeof fn, "%s/ap_%06ld.bin", od, sg); FILE *g = fopen(fn, "wb"); CC_SHA256_CTX c; CC_SHA256_Init(&c);
      sieve_seg(lo, hi, comp); u64 np = 0, nw = 0;
      for (u64 q = lo; q < hi; q++) { if (comp[q - lo]) continue; i64 a; Q = q; int bad = (modz(DISC) == 0);
        if (bad && vq(DISC, q) >= 12) fail(q, "v_q(Delta) >= 12: model not certified minimal");
        if (q < QB || bad) a = brute_ap(q); else { check_witness(q, f, &a); nw++; }
        int32_t a32 = (int32_t)a; fwrite(&a32, 4, 1, g); CC_SHA256_Update(&c, &a32, 4); np++; }
      unsigned char extra; if (fread(&extra, 1, 1, f) == 1 || nw != hcnt) fail(lo, "witness count mismatch / trailing data");
      fclose(f); fclose(g); unsigned char dg[32]; char hx[65]; CC_SHA256_Final(dg, &c); hexdig(dg, hx);
      printf("SEG %ld lo %llu hi %llu primes %llu witnesses %llu ap_sha256 %s\n", sg, (unsigned long long)lo, (unsigned long long)hi,
             (unsigned long long)np, (unsigned long long)nw, hx); fflush(stdout);
    }
    return 0;
  }
  if (!strcmp(argv[1], "an")) {                                   /* multiplicative sieve over n <= T; independent of the engine */
    u64 SEGQ = strtoull(argv[8], 0, 10); const char *od = argv[9]; if (T > 268000000ULL) { fprintf(stderr, "T too large for an\n"); return 1; }
    int32_t *ap = calloc(T + 1, 4), *an = malloc((T + 1) * 4); unsigned char *comp = malloc(SEGQ), *isp = calloc(T + 1, 1);
    for (long sg = 0; (u64)sg * SEGQ <= T; sg++) { u64 lo = (u64)sg * SEGQ, hi = lo + SEGQ; if (hi > T + 1) hi = T + 1;
      char fn[1024]; snprintf(fn, sizeof fn, "%s/ap_%06ld.bin", od, sg); FILE *g = fopen(fn, "rb"); if (!g) fail(lo, "missing ap file");
      sieve_seg(lo, hi, comp); for (u64 q = lo; q < hi; q++) if (!comp[q - lo]) { int32_t v; if (!rd(g, &v, 4)) fail(q, "short ap"); ap[q] = v; isp[q] = 1; }
      int32_t extra; if (fread(&extra, 4, 1, g) == 1) fail(lo, "ap file has trailing data"); fclose(g); }
    for (u64 n = 0; n <= T; n++) an[n] = 1;
    for (u64 p = 2; p <= T; p++) { if (!isp[p]) continue;             /* primes from the verifier's own sieve */
      Q = p; int bad = (modz(DISC) == 0); i64 pe_prev = 1, pe = ap[p]; u64 pk = p;
      for (;;) { for (u64 n = pk; n <= T; n += pk) if ((n / pk) % p) an[n] = (int32_t)((i64)an[n] * pe);
        if (pk > T / p) break; pk *= p; i64 nx = bad ? pe * ap[p] : (i64)ap[p] * pe - (i64)p * pe_prev; pe_prev = pe; pe = nx; } }
    unsigned char leaves[32 * 128]; long nl = 0; CC_SHA256_CTX c;
    for (u64 b0 = 1; b0 <= T; b0 += BLK) { CC_SHA256_Init(&c); u64 e = b0 + BLK; if (e > T + 1) e = T + 1;
      for (u64 n = b0; n < e; n++) { int64_t v = an[n]; CC_SHA256_Update(&c, &v, 8); }
      if (nl >= 128) { fprintf(stderr, "too many blocks\n"); return 1; } CC_SHA256_Final(leaves + 32 * nl, &c); nl++; }
    unsigned char root[32]; char hx[65]; CC_SHA256(leaves, (CC_LONG)(32 * nl), root); hexdig(root, hx);
    printf("AN_MERKLE_SHA256 %s blocks %ld T %llu\n", hx, nl, (unsigned long long)T); return 0;
  }
  fprintf(stderr, "unknown mode\n"); return 1;
}
