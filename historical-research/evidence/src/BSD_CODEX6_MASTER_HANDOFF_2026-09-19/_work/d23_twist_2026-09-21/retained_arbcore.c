/* arbcore.c -- RIGOROUS streaming core (Arb/FLINT ball arithmetic) for the BSD seed project.  See DESIGN.md.
 *
 * usage:
 *   arbcore l2  a1 a2 a3 a4 a6 N T SEGQ apdir W outdir
 *        L''(E,1)/2 = 2 sum_{n<=T} a_n/n G2(2 pi n/sqrt N)  +/- tail_L2(T)      (valid when w = +1 and L(E,1) = 0)
 *   arbcore ms  a1 a2 a3 a4 a6 m Q sign T SEGQ apdir W outdir [LATDEN]   natural order; needs a 4(T+1)-byte a_q table
 *   arbcore msl a1 a2 a3 a4 a6 m Q sign T SEGQ apdir W outdir [LATDEN]   table-free: Part S = R-smooth n (natural order,
 *        R = isqrt T) + Part L = n = m q with q > R prime (q streamed per a_q segment, m <= R); RAM independent of T
 *        S_k = sum_{n<=T, n=k (m)} a_n/n exp(-2 pi n y), y = 1/(m sqrt Q);  Re/Im lambda(b/m) = sum_k S_k (z^{kb} + sign z^{-k u_b}),
 *        u_b = (Q b)^{-1} mod m;  x_b = Re lambda/Omega+, x_b^- = Im lambda/Omega- (Omega+- by AGM, Delta > 0);  tails +/- 2 tail_MS(T)
 *   arbcore tmin a1 a2 a3 a4 a6 m Q LATDEN   least T >= 1/kappa with 2 tail_MS(T)/Omega+ <= (1 - 2^-10)/(2 LATDEN)
 *   arbcore g2t                              unit test of the G2 evaluator (node Taylor models vs direct series)
 * Inputs: apdir/ap_<s>.bin = the VERIFIER's output (int32 a_p for every prime in [s*SEGQ, (s+1)*SEGQ) ∩ [0,T], increasing).
 * a_n: segmented cofactor division by primes <= isqrt(T) (a_{p^e} by recurrence; bad p: a_p^e), leftover prime from the table.
 * l2/ms: Merkle SHA-256 of int64-LE a_n over 2^22-blocks (must equal `wverify an`).  All modes: SHA-256 of every a_q segment
 * consumed (must equal the verifier's SEG ... ap_sha256 lines) and their root.  Work units write once to outdir (tmp + rename;
 * restart skips complete units; each unit ends with a SHA-256 self-hash checked on read; outdir/PARAMS locks the parameters).  Combination in fixed unit order (deterministic).
 * No M_PI, no double in any enclosure: pi, gamma, sqrt, exp, log, E1, cos/sin(pi*rational), AGM all from Arb.  Doubles only
 * choose loop lengths and node indices; every such choice is re-checked in ball arithmetic (g2_eval range guard). */
#include <flint/arb.h>
#include <flint/acb.h>
#include <flint/acb_poly.h>
#include <flint/arb_hypgeom.h>
#include <flint/fmpq.h>
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <fenv.h>
#include <pthread.h>
#include <unistd.h>
#include <sys/stat.h>
#include <CommonCrypto/CommonDigest.h>
typedef uint64_t u64; typedef int64_t i64; typedef __int128 i128;
#define BLK (1ULL << 22)
#define PREC 128
#define NPREC 256
#define JDEG 12
#define HEXP 8                                      /* node spacing H = 2^-8 */
#define GMAX 4096                                   /* msl: exp(-kappa g) table for prime gaps g <= GMAX */
static int MODE;                                    /* 0 = l2, 1 = ms, 2 = msl */
static i64 a1, a2, a3, a4, a6; static i128 b2, b4, b6, DISC;
static u64 T, SEGQ, NCOND, MM, QQ, RT; static int SIGN, W; static long LATDEN = 2; static const char *APDIR, *OUT;
static int32_t *A; static u64 ATOP;                 /* A[q] = verified a_q for primes q <= ATOP (T for l2/ms, RT for msl) */
static u64 *SP; static long NSP; static i64 (*APK)[64];   /* primes <= RT = isqrt(T) and a_{p^e} */
static arb_t CL2, KAPPA, Q1; static arb_ptr EG, AMT;       /* c = 2pi/sqrt N; kappa = 2 pi y; q1 = e^-kappa; EG[g] = e^-kappa g; AMT[m] = a_m/m */
static long NBLK, NSEG, NUNIT; static long NEXTU;          /* work units (atomic counter NEXTU) */
/* ---- G2 node table (l2) ---- */
static double X0D = 1.0; static long NNODE; static arb_ptr GC; static mag_ptr GR;   /* GC[(j+1)*(JDEG+2)+i], GR[j+1] */
static arf_t TLO, THI;                              /* -H, 2H (exact) */

static void fatal(const char *m) { fprintf(stderr, "FATAL: %s\n", m); exit(3); }
static int is_bad(u64 p) { return ((DISC % (i128)p) + (i128)p) % (i128)p == 0; }
static void hexs(const unsigned char *d, char *o) { for (int i = 0; i < 32; i++) sprintf(o + 2 * i, "%02x", d[i]); }

/* G2(x) = 1/2 (log x + gamma)^2 + pi^2/12 + sum_{k>=1} (-1)^k x^k / (k^2 k!), rigorous tail (ratio <= 1/2 once k >= 2x). */
static void g2_direct(arb_t res, const arb_t x, slong prec) {
  arb_t L, g, pk, t, s; arb_init(L); arb_init(g); arb_init(pk); arb_init(t); arb_init(s);
  arb_log(L, x, prec); arb_const_euler(g, prec); arb_add(L, L, g, prec); arb_sqr(L, L, prec); arb_mul_2exp_si(L, L, -1);
  arb_const_pi(g, prec); arb_sqr(g, g, prec); arb_div_ui(g, g, 12, prec); arb_add(res, L, g, prec);
  arf_t xu; arf_init(xu); arb_get_ubound_arf(xu, x, prec); double xd = arf_get_d(xu, ARF_RND_UP); slong K0 = (slong)(2.0 * xd) + 4;
  arb_one(pk); arb_zero(s); mag_t tm, eps; mag_init(tm); mag_init(eps); mag_one(eps); mag_mul_2exp_si(eps, eps, -prec - 10);
  slong k;
  for (k = 1; ; k++) {
    arb_mul(pk, pk, x, prec); arb_div_ui(pk, pk, (ulong)k, prec);            /* pk = x^k/k! */
    arb_div_ui(t, pk, (ulong)k, prec); arb_div_ui(t, t, (ulong)k, prec);       /* x^k/(k^2 k!) */
    if (k & 1) arb_sub(s, s, t, prec); else arb_add(s, s, t, prec);
    arb_get_mag(tm, t); if (k >= K0 && mag_cmp(tm, eps) < 0) break;
  }
  /* tail <= 2 |t_{k+1}| = 2 pk x/(k+1)^3, since k+1 > K0 > 2x makes every later ratio <= x/(j+1) < 1/2 */
  mag_t xm; mag_init(xm); arb_get_mag(xm, x); arb_get_mag(tm, pk); mag_mul(tm, tm, xm);
  mag_div_ui(tm, tm, (ulong)(k + 1)); mag_div_ui(tm, tm, (ulong)(k + 1)); mag_div_ui(tm, tm, (ulong)(k + 1)); mag_mul_2exp_si(tm, tm, 1);
  arb_add_error_mag(s, tm); arb_add(res, res, s, prec);
  mag_clear(tm); mag_clear(eps); mag_clear(xm); arf_clear(xu);
  arb_clear(L); arb_clear(g); arb_clear(pk); arb_clear(t); arb_clear(s);
}
/* Taylor coefficients G2^{(i)}(x)/i!, i = 0..JDEG+1, at exact node x, by exact series algebra (DESIGN.md O2 (G2)). */
static void g2_node(arb_ptr out, const arb_t x, slong prec) {
  slong L = JDEG + 2; arb_ptr ex = _arb_vec_init(L), iv = _arb_vec_init(L), w = _arb_vec_init(L), e1 = _arb_vec_init(L), f = _arb_vec_init(L);
  arb_t t, one; arb_init(t); arb_init(one); arb_one(one);
  arb_neg(t, x); arb_exp(ex + 0, t, prec);                                   /* e^{-x} (-1)^k/k! */
  for (slong k = 1; k < L; k++) { arb_div_si(ex + k, ex + k - 1, -k, prec); }
  arb_inv(iv + 0, x, prec); for (slong k = 1; k < L; k++) { arb_div(iv + k, iv + k - 1, x, prec); arb_neg(iv + k, iv + k); }
  for (slong k = 0; k < L; k++) { arb_zero(w + k); for (slong i = 0; i <= k; i++) arb_addmul(w + k, ex + i, iv + k - i, prec); }
  arb_hypgeom_expint(e1 + 0, one, x, prec);                                  /* E1(x) */
  for (slong k = 0; k + 1 < L; k++) { arb_div_si(e1 + k + 1, w + k, -(k + 1), prec); }   /* E1' = -e^{-t}/t */
  for (slong k = 0; k < L; k++) { arb_zero(f + k); for (slong i = 0; i <= k; i++) arb_addmul(f + k, e1 + i, iv + k - i, prec); }
  g2_direct(out + 0, x, prec);                                               /* G2' = -E1/x */
  for (slong k = 0; k + 1 < L; k++) arb_div_si(out + k + 1, f + k, -(k + 1), prec);
  _arb_vec_clear(ex, L); _arb_vec_clear(iv, L); _arb_vec_clear(w, L); _arb_vec_clear(e1, L); _arb_vec_clear(f, L); arb_clear(t); arb_clear(one);
}
static void build_nodes(double xmax) {
  NNODE = (long)((xmax - X0D) * (1 << HEXP)) + 3; if (NNODE < 2) NNODE = 2;
  GC = _arb_vec_init((NNODE + 1) * (JDEG + 2)); GR = _mag_vec_init(NNODE + 1);
  arb_t x; arb_init(x);
  for (long j = -1; j < NNODE; j++) {                                        /* node x_j = 1 + j/256 (exact dyadic) */
    arb_set_si(x, (1 << HEXP) + j); arb_mul_2exp_si(x, x, -HEXP);
    g2_node(GC + (j + 1) * (JDEG + 2), x, NPREC);
  }
  for (long j = 0; j < NNODE; j++) {                                         /* R_j = |g_{j-1,J+1}| (2H)^{J+1} */
    arb_get_mag(GR + j + 1, GC + j * (JDEG + 2) + JDEG + 1); mag_mul_2exp_si(GR + j + 1, GR + j + 1, (slong)(-(HEXP - 1) * (JDEG + 1)));
  }
  arb_clear(x);
  arf_init(TLO); arf_init(THI); arf_set_si_2exp_si(TLO, -1, -HEXP); arf_set_si_2exp_si(THI, 1, 1 - HEXP);
}
static void g2_eval(arb_t res, const arb_t x, arb_t t, slong prec) {        /* node table for x >= 1, direct series below */
  double xd = arf_get_d(arb_midref(x), ARF_RND_NEAR);
  if (xd < X0D) { g2_direct(res, x, prec); return; }
  long j = (long)((xd - X0D) * (1 << HEXP)); if (j >= NNODE) fatal("node table too short");
  arb_set_si(t, (1 << HEXP) + j); arb_mul_2exp_si(t, t, -HEXP); arb_sub(t, x, t, prec);   /* t = x - x_j */
  arf_t lb, ub; arf_init(lb); arf_init(ub); arb_get_lbound_arf(lb, t, prec); arb_get_ubound_arf(ub, t, prec);
  if (arf_cmp(lb, TLO) < 0 || arf_cmp(ub, THI) > 0) fatal("Taylor step outside [-H, 2H]");   /* remainder bound needs this */
  arf_clear(lb); arf_clear(ub);
  arb_srcptr c = GC + (j + 1) * (JDEG + 2);
  arb_set_round(res, c + JDEG, prec);
  for (long i = JDEG - 1; i >= 0; i--) { arb_mul(res, res, t, prec); arb_add(res, res, c + i, prec); }
  arb_add_error_mag(res, GR + j + 1);
}
/* ---- tails (DESIGN.md O2/O3): elementary, Hasse + D(x) in [x log x - x, x(1+log x)] ---- */
static void tail_ms(arb_t out, const arb_t kap, u64 TT) {
  arb_t e, a, b, t, lg; arb_init(e); arb_init(a); arb_init(b); arb_init(t); arb_init(lg);
  arb_mul_ui(t, kap, TT, NPREC); arb_neg(t, t); arb_exp(e, t, NPREC);
  arb_sqrt_ui(a, TT, NPREC); arb_mul_2exp_si(a, a, 1);                       /* 2 sqrt T */
  arb_log_ui(lg, TT, NPREC); arb_add_ui(lg, lg, 2, NPREC); arb_div(b, lg, kap, NPREC);
  arb_sqr(t, kap, NPREC); arb_mul_ui(t, t, TT, NPREC); arb_inv(t, t, NPREC); arb_add(b, b, t, NPREC);
  arb_sqrt_ui(t, TT, NPREC); arb_div(b, b, t, NPREC); arb_add(a, a, b, NPREC); arb_mul(out, a, e, NPREC);
  arb_clear(e); arb_clear(a); arb_clear(b); arb_clear(t); arb_clear(lg);
}
static void tail_l2(arb_t out, const arb_t c, u64 TT) {
  arb_t e, a, b, t, lg, cT2; arb_init(e); arb_init(a); arb_init(b); arb_init(t); arb_init(lg); arb_init(cT2);
  arb_mul_ui(t, c, TT, NPREC); arb_sqr(cT2, t, NPREC); arb_neg(t, t); arb_exp(e, t, NPREC);
  arb_sqrt_ui(a, TT, NPREC); arb_mul_2exp_si(a, a, 1); arb_div(a, a, cT2, NPREC);        /* 2 sqrt T / (cT)^2 */
  arb_log_ui(lg, TT, NPREC); arb_add_ui(lg, lg, 2, NPREC); arb_div(b, lg, c, NPREC);
  arb_sqr(t, c, NPREC); arb_mul_ui(t, t, TT, NPREC); arb_inv(t, t, NPREC); arb_add(b, b, t, NPREC);
  arb_sqrt_ui(t, TT, NPREC); arb_div(b, b, t, NPREC); arb_div(b, b, cT2, NPREC); arb_add(a, a, b, NPREC);
  arb_mul(out, a, e, NPREC); arb_mul_2exp_si(out, out, 1);
  arb_clear(e); arb_clear(a); arb_clear(b); arb_clear(t); arb_clear(lg); arb_clear(cT2);
}
/* ---- primes, a_q segments, a_n ---- */
static void small_primes(void) {                    /* SP = all primes <= RT, by trial division (own code) */
  SP = malloc(sizeof(u64) * (RT + 2)); NSP = 0;
  for (u64 p = 2; p <= RT; p++) { int pr = 1; for (u64 d = 2; d * d <= p; d++) if (p % d == 0) { pr = 0; break; } if (pr) SP[NSP++] = p; }
}
static void sieve(u64 lo, u64 hi, unsigned char *comp) {   /* comp[i] = 1 iff lo+i not prime; hi <= T+1 so SP suffices */
  memset(comp, 0, hi - lo); for (u64 n = lo; n < hi && n < 2; n++) comp[n - lo] = 1;
  for (long i = 0; i < NSP && SP[i] * SP[i] < hi; i++) { u64 p = SP[i], st = (lo + p - 1) / p * p; if (st < p * p) st = p * p;
    for (u64 m = st; m < hi; m += p) comp[m - lo] = 1; }
}
static void seg_bounds(long s, u64 *lo, u64 *hi) { *lo = (u64)s * SEGQ; *hi = *lo + SEGQ; if (*hi > T + 1) *hi = T + 1; }
/* read ap segment s: exactly one int32 per prime of [lo,hi) (own sieve), no trailing data; buf[i] = a of the i-th prime */
static u64 read_apseg(long s, unsigned char *comp, int32_t *buf, unsigned char *dg) {
  u64 lo, hi; seg_bounds(s, &lo, &hi); sieve(lo, hi, comp); u64 np = 0; for (u64 q = lo; q < hi; q++) np += !comp[q - lo];
  char fn[2048]; snprintf(fn, sizeof fn, "%s/ap_%06ld.bin", APDIR, s); FILE *g = fopen(fn, "rb"); if (!g) fatal("missing ap file");
  if (fread(buf, 4, np, g) != np) fatal("short ap file"); int32_t x; if (fread(&x, 4, 1, g) == 1) fatal("ap file has trailing data");
  fclose(g); CC_SHA256(buf, (CC_LONG)(4 * np), dg); return np;
}
static unsigned char (*APSH)[32];                   /* per-segment SHA-256 of the a_q stream */
static void load_table(u64 top) {                   /* A[q] for primes q <= top; hashes of the segments read */
  ATOP = top; A = calloc(top + 1, 4); if (!A) fatal("alloc A");
  unsigned char *comp = malloc(SEGQ); int32_t *buf = malloc(4 * SEGQ);
  for (long s = 0; (u64)s * SEGQ <= top; s++) { u64 lo, hi; seg_bounds(s, &lo, &hi); read_apseg(s, comp, buf, APSH[s]);
    u64 i = 0; for (u64 q = lo; q < hi; q++) if (!comp[q - lo]) { if (q <= top) A[q] = buf[i]; i++; } }
  free(comp); free(buf);
  APK = malloc(sizeof(*APK) * (NSP + 1));
  for (long i = 0; i < NSP; i++) { u64 p = SP[i]; i64 *ak = APK[i]; ak[0] = 1; ak[1] = A[p]; int bad = is_bad(p); int e = 1; u64 pk = p;
    while (pk <= T / p && e < 62) { pk *= p; e++; ak[e] = bad ? ak[e - 1] * A[p] : A[p] * ak[e - 1] - (i64)p * ak[e - 2]; } }
}
/* a_n for n in [lo,hi): cofactor division by SP; rem[] = leftover (1 or one prime > RT); use_table: multiply by A[rem] */
static void gen_block(u64 lo, u64 hi, u64 *rem, i64 *an, int use_table) {
  for (u64 n = lo; n < hi; n++) { rem[n - lo] = n; an[n - lo] = 1; }
  for (long i = 0; i < NSP; i++) { u64 p = SP[i]; u64 st = (lo + p - 1) / p * p;
    for (u64 m = st; m < hi; m += p) { u64 r = rem[m - lo]; int e = 0; while (r % p == 0) { r /= p; e++; } rem[m - lo] = r; an[m - lo] *= APK[i][e]; } }
  if (use_table) for (u64 n = lo; n < hi; n++) { u64 r = rem[n - lo]; if (r > 1) { if (r > ATOP) fatal("cofactor beyond table"); an[n - lo] *= A[r]; } }
}
static u64 hdr_u64(const char *h, const char *key) { const char *p = strstr(h, key); if (!p) fatal("header field missing"); return strtoull(p + strlen(key), 0, 10); }
static void hdr_hex(const char *h, const char *key, unsigned char *d) { const char *p = strstr(h, key); if (!p) fatal("header hash missing"); p += strlen(key);
  for (int i = 0; i < 32; i++) { unsigned v; if (sscanf(p + 2 * i, "%2x", &v) != 1) fatal("bad hex"); d[i] = (unsigned char)v; } }
/* ---- work units: l2/ms = blocks of n; msl = L segments (heaviest first) then S blocks ---- */
static void unit_name(long u, char *fn, size_t sz) {
  if (MODE == 2 && u < NSEG) snprintf(fn, sz, "%s/lseg_%06ld.txt", OUT, u);
  else snprintf(fn, sz, "%s/blk_%06ld.txt", OUT, MODE == 2 ? u - NSEG : u);
}
static int unit_done(long u) { char fn[2048]; unit_name(u, fn, sizeof fn); struct stat st; return stat(fn, &st) == 0 && st.st_size > 0; }
/* unit files: content is built in memory, then written as content + "END <sha256 of content>" to tmp and renamed (write-once) */
static char *UBUF_P[64]; static size_t UBUF_N[64]; static __thread int TID;
static FILE *unit_open(long u, char *tmp, char *fn) { unit_name(u, fn, 2048); snprintf(tmp, 2100, "%s.tmp", fn);
  FILE *f = open_memstream(&UBUF_P[TID], &UBUF_N[TID]); if (!f) fatal("open_memstream"); return f; }
static void unit_close(FILE *f, const char *tmp, const char *fn) {
  if (fclose(f)) fatal("memstream"); unsigned char dg[32]; char hx[65]; CC_SHA256(UBUF_P[TID], (CC_LONG)UBUF_N[TID], dg); hexs(dg, hx);
  FILE *g = fopen(tmp, "w"); if (!g) fatal("cannot write unit");
  if (fwrite(UBUF_P[TID], 1, UBUF_N[TID], g) != UBUF_N[TID] || fprintf(g, "END %s\n", hx) < 0 || fclose(g)) fatal("write error");
  free(UBUF_P[TID]); UBUF_P[TID] = NULL; if (rename(tmp, fn)) fatal("rename"); }
static void put_sums(FILE *f, arb_srcptr S, long nv) {
  for (long k = 0; k < nv; k++) { char *s = arb_dump_str(S + k); if (MODE == 0) fprintf(f, "SUM %s\n", s); else fprintf(f, "S %ld %s\n", k, s); flint_free(s); }
}
static void do_block(long b, u64 *rem, i64 *an, long u) {  /* l2, ms: all n; msl: R-smooth n only */
  u64 lo = (u64)b * BLK + 1, hi = lo + BLK; if (hi > T + 1) hi = T + 1;
  gen_block(lo, hi, rem, an, MODE != 2);
  CC_SHA256_CTX c; CC_SHA256_Init(&c); u64 nnz = 0, nsm = 0;
  for (u64 n = lo; n < hi; n++) { int64_t v = (MODE == 2 && rem[n - lo] != 1) ? 0 : an[n - lo]; CC_SHA256_Update(&c, &v, 8); }
  unsigned char dg[32]; char hx[65]; CC_SHA256_Final(dg, &c); hexs(dg, hx);
  arb_t x, t, v, w; arb_init(x); arb_init(t); arb_init(v); arb_init(w);
  long nv = MODE == 0 ? 1 : (long)MM; arb_ptr S = _arb_vec_init(nv);
  if (MODE == 0) {
    for (u64 n = lo; n < hi; n++) { i64 a = an[n - lo]; if (!a) continue; nnz++;
      arb_mul_ui(x, CL2, n, PREC); g2_eval(v, x, t, PREC); arb_mul_si(v, v, a, PREC); arb_div_ui(v, v, n, PREC); arb_add(S, S, v, PREC); }
  } else {
    arb_mul_ui(t, KAPPA, lo, PREC); arb_neg(t, t); arb_exp(w, t, PREC);                          /* w = exp(-kappa lo) */
    for (u64 n = lo; n < hi; n++) { i64 a = an[n - lo]; int use = (MODE == 1 || rem[n - lo] == 1); nsm += (MODE == 2 && use);
      if (use && a) { nnz++; arb_mul_si(v, w, a, PREC); arb_div_ui(v, v, n, PREC); arb_add(S + (n % MM), S + (n % MM), v, PREC); }
      arb_mul(w, w, Q1, PREC); }
  }
  char tmp[2100], fn[2048]; FILE *f = unit_open(u, tmp, fn);
  fprintf(f, "BLK %ld lo %llu hi %llu leaf %s nnz %llu smooth %llu\n", b, (unsigned long long)lo, (unsigned long long)hi, hx,
          (unsigned long long)nnz, (unsigned long long)nsm);
  put_sums(f, S, nv); unit_close(f, tmp, fn);
  _arb_vec_clear(S, nv); arb_clear(x); arb_clear(t); arb_clear(v); arb_clear(w);
}
/* msl Part L on ap segment s: every prime q in the segment with q > RT, every m <= T/q:  a_n/n e^{-kappa n} = (a_q/q) r^m (a_m/m),
 * r = e^{-kappa q} (from the previous prime by EG[gap], exact arb_exp at segment start or gap > GMAX). */
static void do_lseg(long s, unsigned char *comp, int32_t *buf, long u) {
  u64 lo, hi; seg_bounds(s, &lo, &hi); unsigned char dg[32]; char hx[65]; read_apseg(s, comp, buf, dg); hexs(dg, hx);
  arb_ptr S = _arb_vec_init(MM); arb_t r, w, t; arb_init(r); arb_init(w); arb_init(t);
  u64 i = 0, qprev = 0, nq = 0, pairs = 0, nterm = 0;
  for (u64 q = lo; q < hi; q++) { if (comp[q - lo]) continue; int32_t aq = buf[i++]; if (q <= RT) continue;
    u64 mmax = T / q; pairs += mmax; nq++; if (!aq) continue;
    if (qprev && q - qprev <= GMAX) arb_mul(r, r, EG + (q - qprev), PREC); else { arb_mul_ui(t, KAPPA, q, PREC); arb_neg(t, t); arb_exp(r, t, PREC); }
    qprev = q;
    arb_set_si(w, aq); arb_div_ui(w, w, q, PREC); u64 qm = q % MM, k = 0;
    for (u64 m = 1; m <= mmax; m++) { arb_mul(w, w, r, PREC); k += qm; if (k >= MM) k -= MM;
      if (!arb_is_zero(AMT + m)) { arb_addmul(S + k, w, AMT + m, PREC); nterm++; } }
  }
  char tmp[2100], fn[2048]; FILE *f = unit_open(u, tmp, fn);
  fprintf(f, "LSEG %ld lo %llu hi %llu apsha %s bigprimes %llu pairs %llu nnz %llu\n", s, (unsigned long long)lo, (unsigned long long)hi, hx,
          (unsigned long long)nq, (unsigned long long)pairs, (unsigned long long)nterm);
  put_sums(f, S, MM); unit_close(f, tmp, fn);
  _arb_vec_clear(S, MM); arb_clear(r); arb_clear(w); arb_clear(t);
}
static void *worker(void *arg) {
  TID = (int)(long)arg; u64 *rem = malloc(BLK * 8); i64 *an = malloc(BLK * 8); unsigned char *comp = malloc(SEGQ); int32_t *buf = malloc(4 * SEGQ);
  for (;;) { long u = __atomic_fetch_add(&NEXTU, 1, __ATOMIC_SEQ_CST); if (u >= NUNIT) break; if (unit_done(u)) continue;
    if (MODE == 2 && u < NSEG) do_lseg(u, comp, buf, u); else do_block(MODE == 2 ? u - NSEG : u, rem, an, u); }
  free(rem); free(an); free(comp); free(buf); flint_cleanup(); return NULL;
}
/* read back a unit file: header line + balls */
static void read_unit(long u, char *hdr, arb_ptr vals, long nv) {   /* verifies the END self-hash, then parses */
  char fn[2048]; unit_name(u, fn, sizeof fn); FILE *f = fopen(fn, "rb"); if (!f) fatal("unit file missing");
  fseek(f, 0, SEEK_END); long sz = ftell(f); fseek(f, 0, SEEK_SET); char *buf = malloc(sz + 1);
  if (fread(buf, 1, sz, f) != (size_t)sz) fatal("unit read"); buf[sz] = 0; fclose(f);
  if (sz < 70 || buf[sz - 1] != '\n') fatal("unit not terminated"); long e = sz - 2; while (e > 0 && buf[e - 1] != '\n') e--;
  if (strncmp(buf + e, "END ", 4) || sz - e != 69) fatal("unit not terminated");
  unsigned char dg[32], want[32]; CC_SHA256(buf, (CC_LONG)e, dg); hdr_hex(buf + e, "END ", want);
  if (memcmp(dg, want, 32)) fatal("unit file self-hash mismatch (corrupted checkpoint)");
  buf[e] = 0; char *save = NULL, *line = strtok_r(buf, "\n", &save); if (!line) fatal("empty unit"); strcpy(hdr, line);
  for (long i = 0; i < nv; i++) { line = strtok_r(NULL, "\n", &save); if (!line) fatal("short unit"); int off = -1;   /* "SUM <dump>" or "S k <dump>" */
    long kk = -1; if (MODE == 0) sscanf(line, "SUM %n", &off); else if (sscanf(line, "S %ld %n", &kk, &off) < 1 || kk != i) off = -1;
    if (off <= 0) fatal("bad unit line"); if (arb_load_str(vals + i, line + off)) fatal("arb_load_str"); }
  if (strtok_r(NULL, "\n", &save)) fatal("unit has extra lines");
  free(buf);
}
/* Omega+ and Omega- (Delta > 0): roots of 4x^3 + b2 x^2 + 2 b4 x + b6 by acb_poly_find_roots (isolated => guaranteed) */
static void periods(arb_t om_p, arb_t om_m, slong prec) {
  acb_poly_t P; acb_poly_init(P); acb_poly_set_coeff_si(P, 3, 4); acb_poly_set_coeff_si(P, 2, (slong)b2);
  acb_poly_set_coeff_si(P, 1, (slong)(2 * b4)); acb_poly_set_coeff_si(P, 0, (slong)b6);
  acb_ptr r = _acb_vec_init(3); slong iso = acb_poly_find_roots(r, P, NULL, 0, prec); if (iso != 3) fatal("roots not isolated");
  arb_ptr e = _arb_vec_init(3); for (int i = 0; i < 3; i++) { if (!arb_contains_zero(acb_imagref(r + i))) fatal("non-real root: Delta < 0 not supported"); arb_set(e + i, acb_realref(r + i)); }
  for (int i = 0; i < 3; i++) for (int j = i + 1; j < 3; j++) if (arb_lt(e + i, e + j)) arb_swap(e + i, e + j);
  if (!arb_gt(e + 0, e + 1) || !arb_gt(e + 1, e + 2)) fatal("roots not separated");
  arb_t u, v, pi; arb_init(u); arb_init(v); arb_init(pi); arb_const_pi(pi, prec);
  arb_sub(u, e + 0, e + 2, prec); arb_sqrt(u, u, prec); arb_sub(v, e + 0, e + 1, prec); arb_sqrt(v, v, prec); arb_agm(om_p, u, v, prec); arb_div(om_p, pi, om_p, prec);
  arb_sub(v, e + 1, e + 2, prec); arb_sqrt(v, v, prec); arb_agm(om_m, u, v, prec); arb_div(om_m, pi, om_m, prec);
  arb_clear(u); arb_clear(v); arb_clear(pi); _arb_vec_clear(e, 3); _acb_vec_clear(r, 3); acb_poly_clear(P);
}
static u64 invmod(u64 a, u64 m) { for (u64 x = 1; x < m; x++) if ((a % m) * x % m == 1) return x; fatal("no inverse"); return 0; }
static void curve(char **argv) {
  a1 = atoll(argv[2]); a2 = atoll(argv[3]); a3 = atoll(argv[4]); a4 = atoll(argv[5]); a6 = atoll(argv[6]);
  b2 = (i128)a1 * a1 + 4 * (i128)a2; b4 = 2 * (i128)a4 + (i128)a1 * a3; b6 = (i128)a3 * a3 + 4 * (i128)a6;
  i128 b8 = (i128)a1 * a1 * a6 + 4 * (i128)a2 * a6 - (i128)a1 * a3 * a4 + (i128)a2 * a3 * a3 - (i128)a4 * a4;
  DISC = -b2 * b2 * b8 - 8 * b4 * b4 * b4 - 27 * b6 * b6 + 9 * b2 * b4 * b6;
}
static void set_kappa(void) {                       /* kappa = 2 pi/(m sqrt Q), q1 = e^{-kappa} */
  arb_t pi, t; arb_init(pi); arb_init(t); arb_const_pi(pi, NPREC); arb_init(KAPPA); arb_init(Q1);
  arb_sqrt_ui(t, QQ, NPREC); arb_mul_ui(t, t, MM, NPREC); arb_div(KAPPA, pi, t, NPREC); arb_mul_2exp_si(KAPPA, KAPPA, 1);
  arb_neg(t, KAPPA); arb_exp(Q1, t, NPREC); arb_clear(pi); arb_clear(t);
}
static void print_dec_bounds(const char *tag, const arb_t x, ulong scale) {   /* floor(lo*scale)/scale, ceil(hi*scale)/scale: exact */
  arf_t l, h; fmpz_t zl, zh; arf_init(l); arf_init(h); fmpz_init(zl); fmpz_init(zh);
  arb_get_lbound_arf(l, x, NPREC); arb_get_ubound_arf(h, x, NPREC);
  arf_mul_ui(l, l, scale, ARF_PREC_EXACT, ARF_RND_DOWN); arf_mul_ui(h, h, scale, ARF_PREC_EXACT, ARF_RND_UP);
  arf_get_fmpz(zl, l, ARF_RND_FLOOR); arf_get_fmpz(zh, h, ARF_RND_CEIL);
  printf("%s [", tag); fmpz_print(zl); printf(", "); fmpz_print(zh); printf("] / %lu\n", scale);
  arf_clear(l); arf_clear(h); fmpz_clear(zl); fmpz_clear(zh);
}
static void params_lock(int argc, char **argv, int widx) {
  char buf[8192] = "", fn[2048]; for (int i = 1; i < argc; i++) if (i != widx) { strncat(buf, argv[i], 1000); strcat(buf, " "); }
  snprintf(fn, sizeof fn, "%s/PARAMS", OUT); FILE *f = fopen(fn, "r");
  if (f) { char old[8192] = ""; if (!fgets(old, sizeof old, f)) old[0] = 0; fclose(f); old[strcspn(old, "\n")] = 0;
    if (strcmp(old, buf)) fatal("outdir/PARAMS differ from this command line (refusing to mix runs)"); }
  else { f = fopen(fn, "w"); if (!f) fatal("cannot write PARAMS"); fprintf(f, "%s\n", buf); fclose(f); }
}

int main(int argc, char **argv) {
  if (fegetround() != FE_TONEAREST) fatal("FP rounding mode is not round-to-nearest");
  if (argc < 2) fatal("usage: see header");
  if (!strcmp(argv[1], "g2t")) {                     /* unit test: node Taylor models vs direct series, x in (0, 20] */
    build_nodes(20.5); arb_t x, a, b, t; arb_init(x); arb_init(a); arb_init(b); arb_init(t); long bad = 0, n = 0; double maxrad = 0;
    for (long k = 1; k <= 200000; k++) { arb_set_ui(x, (ulong)k); arb_div_ui(x, x, 10000, PREC);   /* x = k/10^4, 1e-4 .. 20 */
      g2_eval(a, x, t, PREC); g2_direct(b, x, NPREC); n++; if (!arb_overlaps(a, b)) bad++;
      double r = mag_get_d(arb_radref(a)); if (r > maxrad) maxrad = r; }
    printf("G2T points %ld non_overlapping %ld max_radius %.3e\n", n, bad, maxrad);
    const char *pts[] = {"1/1000", "1/10", "1", "7/2", "10", "35/3"};
    for (int i = 0; i < 6; i++) { fmpq_t q; fmpq_init(q); fmpq_set_str(q, pts[i], 10); arb_set_fmpq(x, q, NPREC); g2_eval(a, x, t, PREC);
      printf("G2(%s) = %s\n", pts[i], arb_get_str(a, 30, 0)); fmpq_clear(q); }
    return bad ? 4 : 0; }
  if (!strcmp(argv[1], "tmin")) {                    /* least T >= ceil(1/kappa) with 2 tail_MS(T)/Omega+ <= (1-2^-10)/(2 LATDEN) */
    if (argc < 10) fatal("usage: tmin a1 a2 a3 a4 a6 m Q LATDEN");
    curve(argv); MM = strtoull(argv[7], 0, 10); QQ = strtoull(argv[8], 0, 10); LATDEN = atol(argv[9]); set_kappa();
    arb_t om_p, om_m, tg, tl; arb_init(om_p); arb_init(om_m); arb_init(tg); arb_init(tl); periods(om_p, om_m, NPREC);
    arb_mul_ui(tg, om_p, 1023, NPREC); arb_div_ui(tg, tg, 1024, NPREC); arb_div_ui(tg, tg, 4 * (ulong)LATDEN, NPREC);   /* tail target */
    arf_t ku; arf_init(ku); arb_get_lbound_arf(ku, KAPPA, NPREC); u64 lo = (u64)(1.0 / arf_get_d(ku, ARF_RND_DOWN)) + 1, hi = lo;
    for (;;) { tail_ms(tl, KAPPA, hi); if (arb_lt(tl, tg)) break; lo = hi; hi *= 2; }
    while (hi - lo > 1) { u64 mid = lo + (hi - lo) / 2; tail_ms(tl, KAPPA, mid); if (arb_lt(tl, tg)) hi = mid; else lo = mid; }
    tail_ms(tl, KAPPA, hi); printf("KAPPA %s\nOMEGA_PLUS %s\nTAIL_TARGET %s\nTMIN %llu\nTAIL_AT_TMIN %s\n", arb_get_str(KAPPA, 25, 0),
      arb_get_str(om_p, 25, 0), arb_get_str(tg, 20, 0), (unsigned long long)hi, arb_get_str(tl, 20, 0));
    tail_ms(tl, KAPPA, hi - 1); printf("TAIL_AT_TMIN_MINUS_1 %s  (not below target: %d)\n", arb_get_str(tl, 20, 0), !arb_lt(tl, tg));
    return 0; }
  MODE = !strcmp(argv[1], "ms") ? 1 : !strcmp(argv[1], "msl") ? 2 : 0; if (!MODE && strcmp(argv[1], "l2")) fatal("mode must be l2, ms, msl, tmin or g2t");
  if (argc < (MODE ? 15 : 13)) fatal("too few arguments");
  curve(argv);
  int ai = 7, widx;
  if (MODE == 0) { NCOND = strtoull(argv[ai++], 0, 10); }
  else { MM = strtoull(argv[ai++], 0, 10); QQ = strtoull(argv[ai++], 0, 10); SIGN = atoi(argv[ai++]); }
  T = strtoull(argv[ai++], 0, 10); SEGQ = strtoull(argv[ai++], 0, 10); APDIR = argv[ai++]; widx = ai; W = atoi(argv[ai++]); OUT = argv[ai++];
  if (MODE && argc > ai) LATDEN = atol(argv[ai]);
  if (W < 1 || W > 64 || T < 4 || SEGQ < 1024 || LATDEN < 1 || (MODE && (MM < 2 || (SIGN != 1 && SIGN != -1)))) fatal("bad parameters");
  if (MODE) { u64 g = QQ, h = MM; while (h) { u64 r = g % h; g = h; h = r; } if (g != 1) fatal("gcd(Q, m) != 1"); }
  mkdir(OUT, 0755); params_lock(argc, argv, widx);
  RT = 1; while ((RT + 1) * (RT + 1) <= T) RT++;
  small_primes(); NSEG = (long)(T / SEGQ) + 1; APSH = calloc(NSEG, 32);
  arb_init(CL2);
  if (MODE == 0) { arb_t pi, t; arb_init(pi); arb_init(t); arb_const_pi(pi, NPREC);
    arb_sqrt_ui(t, NCOND, NPREC); arb_div(CL2, pi, t, NPREC); arb_mul_2exp_si(CL2, CL2, 1);   /* 2 pi / sqrt N */
    arf_t xu; arf_init(xu); arb_mul_ui(t, CL2, T, NPREC); arb_get_ubound_arf(xu, t, NPREC); build_nodes(arf_get_d(xu, ARF_RND_UP) + 0.01); arf_clear(xu); }
  else set_kappa();
  load_table(MODE == 2 ? RT : T);
  if (MODE == 2) {                                   /* EG[g] = e^{-kappa g}; AMT[m] = a_m/m for m <= RT */
    EG = _arb_vec_init(GMAX + 1); arb_t t; arb_init(t);
    for (long g = 0; g <= GMAX; g++) { arb_mul_ui(t, KAPPA, (ulong)g, NPREC); arb_neg(t, t); arb_exp(EG + g, t, NPREC); }
    u64 *rem = malloc(8 * (RT + 1)); i64 *am = malloc(8 * (RT + 1)); gen_block(1, RT + 1, rem, am, 0); AMT = _arb_vec_init(RT + 1);
    for (u64 m = 1; m <= RT; m++) { if (rem[m - 1] != 1) fatal("m <= RT not RT-smooth"); arb_set_si(AMT + m, am[m - 1]); arb_div_ui(AMT + m, AMT + m, m, NPREC); }
    free(rem); free(am); arb_clear(t); }
  NBLK = (long)((T + BLK - 1) / BLK); NUNIT = MODE == 2 ? NSEG + NBLK : NBLK; NEXTU = 0;
  pthread_t th[64]; for (long i = 0; i < W; i++) pthread_create(&th[i], NULL, worker, (void *)i); for (long i = 0; i < W; i++) pthread_join(th[i], NULL);
  /* combine in fixed unit order */
  long nv = MODE == 0 ? 1 : (long)MM; arb_ptr tot = _arb_vec_init(nv), bv = _arb_vec_init(nv); char hdr[65536];
  unsigned char (*LEAF)[32] = malloc(32 * NBLK); u64 smooth = 0, pairs = 0;
  for (long u = 0; u < NUNIT; u++) { read_unit(u, hdr, bv, nv); for (long i = 0; i < nv; i++) arb_add(tot + i, tot + i, bv + i, PREC);
    if (MODE == 2 && u < NSEG) { if (hdr_u64(hdr, "LSEG ") != (u64)u) fatal("unit order"); hdr_hex(hdr, "apsha ", APSH[u]); pairs += hdr_u64(hdr, "pairs "); }
    else { long b = MODE == 2 ? u - NSEG : u; if (hdr_u64(hdr, "BLK ") != (u64)b) fatal("unit order"); hdr_hex(hdr, "leaf ", LEAF[b]); smooth += hdr_u64(hdr, "smooth "); } }
  unsigned char root[32]; char hx[65];
  if (MODE == 2) { long ns = 0; for (long s = 0; s < NSEG; s++) { u64 lo, hi; seg_bounds(s, &lo, &hi); if (lo < hi) ns++; }
    CC_SHA256(APSH, (CC_LONG)(32 * ns), root); hexs(root, hx); printf("AP_SEGROOT_SHA256 %s segments %ld\n", hx, ns);
    CC_SHA256(LEAF, (CC_LONG)(32 * NBLK), root); hexs(root, hx); printf("SMOOTH_MERKLE_SHA256 %s blocks %ld\n", hx, NBLK);
    printf("COUNT smooth %llu pairs %llu sum %llu T %llu identity %d\n", (unsigned long long)smooth, (unsigned long long)pairs,
           (unsigned long long)(smooth + pairs), (unsigned long long)T, smooth + pairs == T);
    if (smooth + pairs != T) fatal("count identity #smooth + #pairs = T fails"); }
  else { long ns = 0; for (long s = 0; s < NSEG; s++) { u64 lo, hi; seg_bounds(s, &lo, &hi); if (lo < hi) ns++; }
    CC_SHA256(APSH, (CC_LONG)(32 * ns), root); hexs(root, hx); printf("AP_SEGROOT_SHA256 %s segments %ld\n", hx, ns);
    CC_SHA256(LEAF, (CC_LONG)(32 * NBLK), root); hexs(root, hx); printf("AN_MERKLE_SHA256 %s blocks %ld T %llu\n", hx, NBLK, (unsigned long long)T); }
  arb_t tl; arb_init(tl); arf_t ub; arf_init(ub);
  if (MODE == 0) {
    tail_l2(tl, CL2, T); arb_get_ubound_arf(ub, tl, NPREC);
    arb_t res; arb_init(res); arb_mul_2exp_si(res, tot + 0, 1);
    printf("PARTIAL_2S %s\n", arb_get_str(res, 30, 0)); printf("TAIL_L2_UPPER %s\n", arf_get_str(ub, 10));
    arb_add_error_arf(res, ub);
    printf("L2HALF_BALL %s\nL2HALF_DUMP %s\n", arb_get_str(res, 30, 0), arb_dump_str(res)); print_dec_bounds("L2HALF_INTERVAL", res, 1000000);
    { char *ms = arf_get_str(arb_midref(res), 25); printf("L2HALF_MID %s\nL2HALF_RAD_UPPER %.12e\n", ms, mag_get_d(arb_radref(res))); flint_free(ms); }
    printf("ZERO_EXCLUDED %d\nPOSITIVE %d\n", !arb_contains_zero(res), arb_is_positive(res));
    arb_clear(res);
  } else {
    tail_ms(tl, KAPPA, T); arb_get_ubound_arf(ub, tl, NPREC); arf_mul_2exp_si(ub, ub, 1);      /* 2 tail for each of Re, Im */
    printf("TAIL_MS_UPPER_TIMES2 %s\n", arf_get_str(ub, 10));
    for (u64 k = 0; k < MM; k++) printf("S %llu %s\n", (unsigned long long)k, arb_get_str(tot + k, 25, 0));
    for (u64 k = 0; k < MM; k++) { char *s = arb_dump_str(tot + k); printf("SDUMP %llu %s\n", (unsigned long long)k, s); flint_free(s); }
    arb_t om_p, om_m, re, im, cs, sn, c2, s2; arb_init(om_p); arb_init(om_m); arb_init(re); arb_init(im); arb_init(cs); arb_init(sn); arb_init(c2); arb_init(s2);
    periods(om_p, om_m, NPREC); printf("OMEGA_PLUS %s\nOMEGA_MINUS %s\n", arb_get_str(om_p, 30, 0), arb_get_str(om_m, 30, 0));
    fmpq_t fr; fmpq_init(fr); arf_t ra; arf_init(ra); long ndet = 0, nb = 0;
    for (u64 b = 1; b < MM; b++) { u64 g = b, h = MM; while (h) { u64 r = g % h; g = h; h = r; } if (g != 1) continue; nb++;
      u64 ub_ = invmod((QQ % MM) * b % MM, MM); arb_zero(re); arb_zero(im);
      for (u64 k = 0; k < MM; k++) {
        fmpq_set_si(fr, (slong)(2 * ((k * b) % MM)), MM); arb_sin_cos_pi_fmpq(sn, cs, fr, PREC);
        fmpq_set_si(fr, (slong)(2 * ((k * ub_) % MM)), MM); arb_sin_cos_pi_fmpq(s2, c2, fr, PREC);
        if (SIGN > 0) { arb_add(cs, cs, c2, PREC); arb_sub(sn, sn, s2, PREC); } else { arb_sub(cs, cs, c2, PREC); arb_add(sn, sn, s2, PREC); }
        arb_addmul(re, tot + k, cs, PREC); arb_addmul(im, tot + k, sn, PREC); }
      arb_add_error_arf(re, ub); arb_add_error_arf(im, ub);
      arb_div(re, re, om_p, PREC); arb_div(im, im, om_m, PREC);
      /* nearest point of (1/LATDEN)Z; contains = ball contains it; unique = ball diameter < 1/LATDEN (exact test) */
      int cp, up, ci, ui; slong hp, hm;
      { double md = arf_get_d(arb_midref(re), ARF_RND_NEAR); hp = (slong)(md * LATDEN + (md >= 0 ? 0.5 : -0.5));
        fmpq_set_si(fr, hp, (ulong)LATDEN); cp = arb_contains_fmpq(re, fr);
        arf_set_mag(ra, arb_radref(re)); arf_mul_ui(ra, ra, 2 * (ulong)LATDEN, ARF_PREC_EXACT, ARF_RND_UP); up = arf_cmp_si(ra, 1) < 0; }
      { double md = arf_get_d(arb_midref(im), ARF_RND_NEAR); hm = (slong)(md * LATDEN + (md >= 0 ? 0.5 : -0.5));
        fmpq_set_si(fr, hm, (ulong)LATDEN); ci = arb_contains_fmpq(im, fr);
        arf_set_mag(ra, arb_radref(im)); arf_mul_ui(ra, ra, 2 * (ulong)LATDEN, ARF_PREC_EXACT, ARF_RND_UP); ui = arf_cmp_si(ra, 1) < 0; }
      ndet += cp && up;
      printf("XB %llu plus %s cand %ld/%ld contains %d unique %d minus %s cand %ld/%ld contains %d unique %d\n", (unsigned long long)b,
             arb_get_str(re, 20, 0), (long)hp, LATDEN, cp, up, arb_get_str(im, 20, 0), (long)hm, LATDEN, ci, ui); }
    printf("XB_PLUS_DETERMINED %ld of %ld (lattice 1/%ld Z)\n", ndet, nb, LATDEN);
    fmpq_clear(fr); arf_clear(ra);
  }
  return 0;
}
