/* acc2243v2.c -- S5 pipeline version of the 2243 pilot accumulator (2026-09-22).
 *
 * Base: S2 prototype acc2243_prof.c (sha256 9fe2cca3..., validated by T1-T3), itself derived from the rigorous stream core
 * arbcore.c (sha256 56a43aac...). UNCHANGED from S2: the kernel, a_n generation, Part S / Part L decomposition, the exact
 * fixed-point accumulation and its error tally, the fingerprints, the checkpoint format, the symbol formula, the lattice
 * identification and the weighted coefficient / nonzero-only test. read_apseg() now takes the directory as an argument.
 * ADDED in v2 (data flow and merge only):
 *  (A) ACC_SELECT restricts run and merge to a declared unit subset. Tokens, comma separated: L<s> or L<s0>-<s1> (every
 *      sub-unit of those segments), L<s>/<j0>-<j1> (sub-units j0..j1 of segment s), S<b> or S<b0>-<b1> (Part S blocks).
 *      Every token must select at least one unit. The selection string is part of PARAMS, so checkpoints of different
 *      selections can never be mixed.
 *  (B) Streaming a_q (run mode, ACC_STREAM_CMD): an L unit whose segment file is absent from apdir, and whose segment has a
 *      single sub-unit, is served by running "<cmd> <segment> <worker-private dir>". The command must produce and verify
 *      the segment and leave ap_<segment>.bin there atomically, with ap_<segment>.sha256 holding the VERIFIER's own hash
 *      (non-zero exit = fatal). After the unit, the SHA-256 of the bytes actually consumed must equal that hash (fatal
 *      otherwise); the same check runs for pre-produced files whenever a .sha256 companion exists. The private directory is
 *      per generation, so a restarted run never shares it with orphaned children of a killed one. A segment with several
 *      sub-units must be pre-produced into apdir (fatal otherwise).
 *  (C) ACC_SHARD=i/n: this process claims only units u with u mod n == i (several machines, one PARAMS). ACC_TAG=<alnum>
 *      adds _t<tag> to checkpoint names so the checkpoints of shards can be pooled into one merge directory. flock() on
 *      outdir/run.lock refuses a second live run process in one directory. ACC_CKPT_SECS adds a time trigger to the
 *      unit-count trigger. Workers that received no unit write no checkpoint.
 *  (D) ACC_TIMING_LOG=1: per-unit wall seconds (stream command and accumulation separately) in outdir/timing_*.txt.
 *  (E) merge: selection-aware coverage (a checkpoint holding an unselected unit is fatal); for a selection the pair count
 *      is checked against an independent recount from a fresh sieve of the selected segments (the full-run identity
 *      #smooth + #pairs = T is unchanged); CHUNK_DIGEST = SHA-256(class sums, error tally, counts) for bit-identity tests;
 *      symbols by ONE length-m acb_dft when m > 400 or ACC_DFT=1 (the direct O(m phi(m)) sum of S2 otherwise); for
 *      m > 400 the identified symbols go to outdir/symbols.bin with its SHA-256; ACC_NOSYMBOLS=1 skips symbol extraction.
 *  v2.1 (merge only): class sums enter the symbol computation as EXACT midpoints; the accumulated rounding tally E is added
 *      once per symbol as 2E (l1 bound), next to the tail term -- acb_dft's Bluestein/Rader steps inflate input radii ~1.7e3x
 *      at prime length 2243 (dft_radius_probe), which made per-class radii unusable at m = 2243^2. SYMBOL_RADIUS_BUDGET and
 *      the maximum symbol radius are printed against 1/(2 LATDEN).
 * usage:
 *   acc2243v2 run   a1 a2 a3 a4 a6 m Q sign T SEGQ apdir W outdir UNIT_TERMS CKPT_UNITS [DIE_AFTER_UNITS]
 *   acc2243v2 merge a1 a2 a3 a4 a6 m Q sign T SEGQ apdir outdir LATDEN [p n r alpha]
 *   acc2243v2 unit  a1 a2 a3 a4 a6 m Q sign T SEGQ apdir UNIT_TERMS KIND IDX [JIDX]   (KIND = S: block IDX; L: segment IDX, sub JIDX)
 *   acc2243v2 plan  a1 a2 a3 a4 a6 m Q sign T SEGQ apdir UNIT_TERMS                    (unit layout; segments to pre-produce)
 *   acc2243v2 dftbench m
 */
#include <flint/arb.h>
#include <flint/acb.h>
#include <flint/acb_poly.h>
#include <flint/acb_dft.h>
#include <flint/fmpq.h>
#include <flint/fmpz.h>
#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <fenv.h>
#include <pthread.h>
#include <unistd.h>
#include <dirent.h>
#include <time.h>
#include <fcntl.h>
#include <limits.h>
#include <sys/stat.h>
#include <sys/file.h>
#include <CommonCrypto/CommonDigest.h>
typedef uint64_t u64; typedef int64_t i64; typedef __int128 i128; typedef unsigned __int128 u128;
#define BLK (1ULL << 22)
#define PREC 128
#define NPREC 256
#define GMAX 4096
#define FBITS 96
#define MAXW 256
#define MAXCK 16384
static i64 a1, a2, a3, a4, a6; static i128 b2, b4, b6, DISC;
static u64 T, SEGQ, MM, QQ, RT, UNIT_TERMS = 1000000000ULL; static int SIGN; static const char *APDIR, *OUT;
static int32_t *A; static u64 ATOP; static u64 *SP; static long NSP; static i64 (*APK)[64];
static int PROFILE = 2; /* unit benchmark only: 0 traversal, 1 + kernel, 2 + fixed-point summation */
static arb_t KAPPA, Q1; static arb_ptr EG, AMT; static u64 *RHO;
static void fatal(const char *m) { fprintf(stderr, "FATAL: %s\n", m); exit(3); }
static int is_bad(u64 p) { return ((DISC % (i128)p) + (i128)p) % (i128)p == 0; }
static void hexs(const unsigned char *d, char *o) { for (int i = 0; i < 32; i++) sprintf(o + 2 * i, "%02x", d[i]); }
static double now(void) { struct timespec ts; clock_gettime(CLOCK_MONOTONIC, &ts); return ts.tv_sec + 1e-9 * ts.tv_nsec; }
static u64 splitmix64(u64 x) { x += 0x9E3779B97F4A7C15ULL; x = (x ^ (x >> 30)) * 0xBF58476D1CE4E5B9ULL; x = (x ^ (x >> 27)) * 0x94D049BB133111EBULL; return x ^ (x >> 31); }
/* ---------------- verbatim from arbcore.c (read_apseg: directory now an argument) ---------------- */
static void tail_ms(arb_t out, const arb_t kap, u64 TT) {
  arb_t e, a, b, t, lg; arb_init(e); arb_init(a); arb_init(b); arb_init(t); arb_init(lg);
  arb_mul_ui(t, kap, TT, NPREC); arb_neg(t, t); arb_exp(e, t, NPREC);
  arb_sqrt_ui(a, TT, NPREC); arb_mul_2exp_si(a, a, 1);
  arb_log_ui(lg, TT, NPREC); arb_add_ui(lg, lg, 2, NPREC); arb_div(b, lg, kap, NPREC);
  arb_sqr(t, kap, NPREC); arb_mul_ui(t, t, TT, NPREC); arb_inv(t, t, NPREC); arb_add(b, b, t, NPREC);
  arb_sqrt_ui(t, TT, NPREC); arb_div(b, b, t, NPREC); arb_add(a, a, b, NPREC); arb_mul(out, a, e, NPREC);
  arb_clear(e); arb_clear(a); arb_clear(b); arb_clear(t); arb_clear(lg);
}
static void small_primes(void) {
  SP = malloc(sizeof(u64) * (RT + 2)); NSP = 0;
  for (u64 p = 2; p <= RT; p++) { int pr = 1; for (u64 d = 2; d * d <= p; d++) if (p % d == 0) { pr = 0; break; } if (pr) SP[NSP++] = p; }
}
static void sieve(u64 lo, u64 hi, unsigned char *comp) {
  memset(comp, 0, hi - lo); for (u64 n = lo; n < hi && n < 2; n++) comp[n - lo] = 1;
  for (long i = 0; i < NSP && SP[i] * SP[i] < hi; i++) { u64 p = SP[i], st = (lo + p - 1) / p * p; if (st < p * p) st = p * p;
    for (u64 m = st; m < hi; m += p) comp[m - lo] = 1; }
}
static void seg_bounds(long s, u64 *lo, u64 *hi) { *lo = (u64)s * SEGQ; *hi = *lo + SEGQ; if (*hi > T + 1) *hi = T + 1; }
static u64 read_apseg(const char *dir, long s, unsigned char *comp, int32_t *buf, unsigned char *dg) {
  u64 lo, hi; seg_bounds(s, &lo, &hi); sieve(lo, hi, comp); u64 np = 0; for (u64 q = lo; q < hi; q++) np += !comp[q - lo];
  char fn[2048]; snprintf(fn, sizeof fn, "%s/ap_%06ld.bin", dir, s); FILE *g = fopen(fn, "rb"); if (!g) fatal("missing ap file");
  if (fread(buf, 4, np, g) != np) fatal("short ap file"); int32_t x; if (fread(&x, 4, 1, g) == 1) fatal("ap file has trailing data");
  fclose(g); CC_SHA256(buf, (CC_LONG)(4 * np), dg); return np;
}
static unsigned char (*APSH)[32]; static long NSEG;
static void load_table(u64 top) {
  ATOP = top; A = calloc(top + 1, 4); if (!A) fatal("alloc A");
  unsigned char *comp = malloc(SEGQ); int32_t *buf = malloc(4 * SEGQ);
  for (long s = 0; (u64)s * SEGQ <= top; s++) { u64 lo, hi; seg_bounds(s, &lo, &hi); read_apseg(APDIR, s, comp, buf, APSH[s]);
    u64 i = 0; for (u64 q = lo; q < hi; q++) if (!comp[q - lo]) { if (q <= top) A[q] = buf[i]; i++; } }
  free(comp); free(buf);
  APK = malloc(sizeof(*APK) * (NSP + 1));
  for (long i = 0; i < NSP; i++) { u64 p = SP[i]; i64 *ak = APK[i]; ak[0] = 1; ak[1] = A[p]; int bad = is_bad(p); int e = 1; u64 pk = p;
    while (pk <= T / p && e < 62) { pk *= p; e++; ak[e] = bad ? ak[e - 1] * A[p] : A[p] * ak[e - 1] - (i64)p * ak[e - 2]; } }
}
static void gen_block(u64 lo, u64 hi, u64 *rem, i64 *an) {
  for (u64 n = lo; n < hi; n++) { rem[n - lo] = n; an[n - lo] = 1; }
  for (long i = 0; i < NSP; i++) { u64 p = SP[i]; u64 st = (lo + p - 1) / p * p;
    for (u64 m = st; m < hi; m += p) { u64 r = rem[m - lo]; int e = 0; while (r % p == 0) { r /= p; e++; } rem[m - lo] = r; an[m - lo] *= APK[i][e]; } }
}
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
static u64 invmod(u64 a, u64 m) { i128 t = 0, nt = 1, r = m, nr = a % m; while (nr) { i128 q = r / nr, x = t - q * nt; t = nt; nt = x; x = r - q * nr; r = nr; nr = x; }
  if (r != 1) fatal("no inverse"); if (t < 0) t += m; return (u64)t; }
static void curve(char **argv) {
  a1 = atoll(argv[2]); a2 = atoll(argv[3]); a3 = atoll(argv[4]); a4 = atoll(argv[5]); a6 = atoll(argv[6]);
  b2 = (i128)a1 * a1 + 4 * (i128)a2; b4 = 2 * (i128)a4 + (i128)a1 * a3; b6 = (i128)a3 * a3 + 4 * (i128)a6;
  i128 b8 = (i128)a1 * a1 * a6 + 4 * (i128)a2 * a6 - (i128)a1 * a3 * a4 + (i128)a2 * a3 * a3 - (i128)a4 * a4;
  DISC = -b2 * b2 * b8 - 8 * b4 * b4 * b4 - 27 * b6 * b6 + 9 * b2 * b4 * b6;
}
static void set_kappa(void) {
  arb_t pi, t; arb_init(pi); arb_init(t); arb_const_pi(pi, NPREC); arb_init(KAPPA); arb_init(Q1);
  arb_sqrt_ui(t, QQ, NPREC); arb_mul_ui(t, t, MM, NPREC); arb_div(KAPPA, pi, t, NPREC); arb_mul_2exp_si(KAPPA, KAPPA, 1);
  arb_neg(t, KAPPA); arb_exp(Q1, t, NPREC); arb_clear(pi); arb_clear(t);
}
/* ---------------- exact fixed-point accumulation (unchanged from S2) ---------------- */
typedef struct { i128 *acc; u128 err; u64 fp, nterm; fmpz_t z; arf_t r; } accum_t;
static void accum_init(accum_t *a) { a->acc = calloc(MM, sizeof(i128)); if (!a->acc) fatal("alloc acc"); a->err = 0; a->fp = 0; a->nterm = 0; fmpz_init(a->z); arf_init(a->r); }
static inline void add_term(accum_t *a, u64 k, const arb_t v) {
  arf_get_fmpz_fixed_si(a->z, arb_midref(v), -FBITS);                     /* |z 2^-F - mid| <= 2^-F */
  if (fmpz_bits(a->z) > 120) fatal("fixed-point overflow risk (term too large)");
  ulong hi, lo; fmpz_get_signed_uiui(&hi, &lo, a->z); i128 z = (i128)(((u128)hi << 64) | lo);
  double rd = mag_get_d(arb_radref(v));                                    /* upper bound for the radius */
  double rs = ldexp(rd, FBITS); if (!(rs < 1e18)) fatal("term radius too large");
  a->err += (u128)(u64)rs + 2;                                             /* ceil(rad 2^F) + 1, as an upper bound */
  a->acc[k] += z; a->fp += (u64)z * RHO[k]; a->nterm++;
}
/* ---------------- units: L sub-units stored (u < NL); S blocks implicit (u = NL + block) ---------------- */
typedef struct { long s; u64 m0, m1; long j, nsub; } lunit_t;              /* segment s, cofactors [m0, m1), sub index j, #sub-units of s */
static lunit_t *LU; static long NL, NUNIT, NBLK;
#define IS_S(u) ((u) >= NL)
#define BLK_OF(u) ((u) - NL)
static u64 ilog2u(u64 x) { u64 r = 0; while (x >>= 1) r++; return r ? r : 1; }
static long sub_count(long s, u64 *mmaxseg) {                            /* deterministic J(s) from integers only */
  u64 lo, hi; seg_bounds(s, &lo, &hi); u64 qlo = lo > RT + 1 ? lo : RT + 1; if (qlo >= hi) { *mmaxseg = 0; return 0; }
  *mmaxseg = T / qlo; u64 est = 0;                              /* sum over primes q of T/q, by dyadic pieces: T/(0.7 i) each */
  for (u64 i = ilog2u(qlo); i < 64; i++) { u64 a = (u64)1 << i, b = i < 63 ? (u64)1 << (i + 1) : ~(u64)0;
    u64 x0 = qlo > a ? qlo : a, x1 = hi < b ? hi : b; if (x0 >= hi) break; if (x0 >= x1) continue;
    est += (T / a) * ((x1 - x0) / (i * 7 / 10 + 1)); }
  u64 J = (est + UNIT_TERMS - 1) / UNIT_TERMS; if (J < 1) J = 1; if (J > *mmaxseg) J = *mmaxseg; return (long)J;
}
static void build_units(void) {                                          /* same unit indices as S2: L sub-units first, then S blocks */
  NSEG = (long)(T / SEGQ) + 1; NBLK = (long)((T + BLK - 1) / BLK); long cap = 1024; LU = malloc(sizeof(lunit_t) * cap); NL = 0;
  for (long s = 0; s < NSEG; s++) { u64 mmax; long J = sub_count(s, &mmax); if (!J) continue; u64 step = (mmax + J - 1) / J; long first = NL;
    for (long j = 0; j < J; j++) { u64 m0 = 1 + (u64)j * step, m1 = m0 + step; if (m1 > mmax + 1) m1 = mmax + 1; if (m0 >= m1) continue;
      if (NL >= cap) { cap *= 2; LU = realloc(LU, sizeof(lunit_t) * cap); }
      LU[NL++] = (lunit_t){s, m0, m1, j, 0}; }
    for (long u = first; u < NL; u++) LU[u].nsub = NL - first; }
  NUNIT = NL + NBLK;
}
/* ---------------- (A) selection ---------------- */
typedef struct { char kind; long a, b, j0, j1, hits; } seltok_t;
static char SELSTR[4096]; static seltok_t *SELT; static long NSELT; static unsigned char *SEL; static long NSEL;
static void parse_select(const char *s) {
  if (strlen(s) >= sizeof SELSTR || !*s) fatal("ACC_SELECT empty or too long"); strcpy(SELSTR, s);
  SELT = malloc(sizeof(seltok_t) * (strlen(s) + 1)); NSELT = 0; const char *p = s; char *e;
  while (*p) { char k = *p++; if (k != 'L' && k != 'S') fatal("ACC_SELECT: token must start with L or S");
    long a = strtol(p, &e, 10); if (e == p || a < 0) fatal("ACC_SELECT: bad index"); p = e; long b = a, j0 = 0, j1 = LONG_MAX;
    if (*p == '-') { p++; b = strtol(p, &e, 10); if (e == p || b < a) fatal("ACC_SELECT: bad range"); p = e; }
    if (*p == '/') { if (k != 'L' || b != a) fatal("ACC_SELECT: sub-unit range only for one L segment"); p++;
      j0 = strtol(p, &e, 10); if (e == p || j0 < 0) fatal("ACC_SELECT: bad sub-unit index"); p = e; j1 = j0;
      if (*p == '-') { p++; j1 = strtol(p, &e, 10); if (e == p || j1 < j0) fatal("ACC_SELECT: bad sub-unit range"); p = e; } }
    if (*p == ',') p++; else if (*p) fatal("ACC_SELECT: expected ','");
    SELT[NSELT++] = (seltok_t){k, a, b, j0, j1, 0}; }
}
static void mark_selection(void) {
  if (!NSELT) { SEL = NULL; NSEL = NUNIT; return; }
  SEL = calloc(NUNIT, 1); NSEL = 0;
  for (long i = 0; i < NSELT; i++) { seltok_t *t = &SELT[i];
    if (t->kind == 'S') { for (long b = t->a; b <= t->b && b < NBLK; b++) { if (!SEL[NL + b]) { SEL[NL + b] = 1; NSEL++; } t->hits++; } }
    else for (long u = 0; u < NL; u++) { if (LU[u].s < t->a || LU[u].s > t->b || LU[u].j < t->j0 || LU[u].j > t->j1) continue;
      if (!SEL[u]) { SEL[u] = 1; NSEL++; } t->hits++; }
    if (!t->hits) fatal("ACC_SELECT: a token selects no unit (segment without primes > sqrt T, sub-unit or block out of range)"); }
}
/* ---------------- units of work (unchanged from S2 except the ap directory) ---------------- */
typedef struct { long u; u64 fp, nterm, cnt; unsigned char h[32]; } rec_t;     /* cnt = pairs (L) or smooth (S) */
/* Part S block: all RT-smooth n in [b BLK + 1, (b+1) BLK] ∩ [1, T] */
static void run_S(long b, accum_t *a, rec_t *rc, u64 *rem, i64 *an) {
  u64 lo = (u64)b * BLK + 1, hi = lo + BLK; if (hi > T + 1) hi = T + 1;
  gen_block(lo, hi, rem, an);
  CC_SHA256_CTX c; CC_SHA256_Init(&c); u64 nsm = 0;
  for (u64 n = lo; n < hi; n++) { int64_t v = rem[n - lo] != 1 ? 0 : an[n - lo]; CC_SHA256_Update(&c, &v, 8); }
  CC_SHA256_Final(rc->h, &c);
  arb_t t, v, w; arb_init(t); arb_init(v); arb_init(w);
  arb_mul_ui(t, KAPPA, lo, PREC); arb_neg(t, t); arb_exp(w, t, PREC);
  u64 fp0 = a->fp, nt0 = a->nterm;
  for (u64 n = lo; n < hi; n++) { i64 x = an[n - lo]; int use = rem[n - lo] == 1; nsm += use;
    if (use && x && PROFILE >= 1) { arb_mul_si(v, w, x, PREC); arb_div_ui(v, v, n, PREC); if (PROFILE >= 2) add_term(a, n % MM, v); }
    if (PROFILE >= 1) arb_mul(w, w, Q1, PREC); }
  rc->fp = a->fp - fp0; rc->nterm = a->nterm - nt0; rc->cnt = nsm;
  arb_clear(t); arb_clear(v); arb_clear(w);
}
/* Part L sub-unit: primes q > RT of segment s, cofactors m in [m0, m1) ∩ [1, T/q]: term (a_q/q) r^m (a_m/m), r = e^{-kappa q} */
static void run_L(const char *dir, long s, u64 m0, u64 m1, accum_t *a, rec_t *rc, unsigned char *comp, int32_t *buf) {
  u64 lo, hi; seg_bounds(s, &lo, &hi); read_apseg(dir, s, comp, buf, rc->h);
  arb_t r, w, t, rp; arb_init(r); arb_init(w); arb_init(t); arb_init(rp);
  u64 i = 0, qprev = 0, pairs = 0; u64 fp0 = a->fp, nt0 = a->nterm;
  for (u64 q = lo; q < hi; q++) { if (comp[q - lo]) continue; int32_t aq = buf[i++]; if (q <= RT) continue;
    u64 mmax = T / q; if (mmax < m0) break;
    if (PROFILE >= 1) { if (qprev && q - qprev <= GMAX) arb_mul(r, r, EG + (q - qprev), PREC); else { arb_mul_ui(t, KAPPA, q, PREC); arb_neg(t, t); arb_exp(r, t, PREC); } }
    qprev = q;
    u64 ms = m0, me = m1 - 1; if (me > mmax) me = mmax; if (ms > me) continue; pairs += me - ms + 1; if (!aq) continue;
    if (PROFILE >= 1) { arb_set_si(w, aq); arb_div_ui(w, w, q, PREC);
    if (ms > 1) { arb_pow_ui(rp, r, ms - 1, PREC); arb_mul(w, w, rp, PREC); } }
    u64 qm = q % MM, k = (u64)(((u128)(ms - 1) * qm) % MM);
    for (u64 m = ms; m <= me; m++) { if (PROFILE >= 1) arb_mul(w, w, r, PREC); k += qm; if (k >= MM) k -= MM;
      if (!arb_is_zero(AMT + m)) { if (PROFILE >= 1) arb_mul(t, w, AMT + m, PREC); if (PROFILE >= 2) add_term(a, k, t); else a->nterm++; } }
  }
  rc->fp = a->fp - fp0; rc->nterm = a->nterm - nt0; rc->cnt = pairs;
  arb_clear(r); arb_clear(w); arb_clear(t); arb_clear(rp);
}
/* independent pair recount for one L sub-unit (merge, selections): fresh sieve, no a_q, no worker record */
static u64 recount_pairs(long s, u64 m0, u64 m1, unsigned char *comp) {
  u64 lo, hi; seg_bounds(s, &lo, &hi); sieve(lo, hi, comp); u64 pairs = 0;
  for (u64 q = (lo > RT + 1 ? lo : RT + 1); q < hi; q++) { if (comp[q - lo]) continue; u64 mmax = T / q; if (mmax < m0) break;
    u64 me = m1 - 1 < mmax ? m1 - 1 : mmax; if (me >= m0) pairs += me - m0 + 1; }
  return pairs;
}
/* ---------------- checkpoints (format unchanged from S2; name may carry a tag) ---------------- */
static char PARAMS[8192]; static int GEN; static unsigned char *DONE; static long DIE_AFTER = 0, CKPT_UNITS = 64; static long NDONE_GLOBAL = 0;
static char TAGSUF[48] = ""; static double CKPT_SECS = 0; static long SHARD_I = 0, SHARD_N = 1; static const char *STREAM_CMD; static int TIMING;
static void write_ckpt(int wid, accum_t *a, rec_t *recs, long nrec) {
  char fn[2048], tmp[2100]; snprintf(fn, sizeof fn, "%s/ckpt_g%03d_w%02d%s.bin", OUT, GEN, wid, TAGSUF); snprintf(tmp, sizeof tmp, "%s.tmp", fn);
  char *mb = NULL; size_t ms = 0; FILE *f = open_memstream(&mb, &ms); if (!f) fatal("memstream");
  fprintf(f, "ACC2243CKPT v1\nPARAMS %s\nFBITS %d\nNREC %ld\n", PARAMS, FBITS, nrec);
  for (long i = 0; i < nrec; i++) { char hx[65]; hexs(recs[i].h, hx);
    fprintf(f, "U %ld fp %016llx nterm %llu cnt %llu hash %s\n", recs[i].u, (unsigned long long)recs[i].fp, (unsigned long long)recs[i].nterm, (unsigned long long)recs[i].cnt, hx); }
  for (u64 k = 0; k < MM; k++) { i128 v = a->acc[k]; if (v > ((i128)1 << 124) || v < -((i128)1 << 124)) fatal("class sum near i128 overflow"); }
  fprintf(f, "ERR %016llx%016llx\nACC %llu\n", (unsigned long long)(a->err >> 64), (unsigned long long)a->err, (unsigned long long)MM);
  fwrite(a->acc, sizeof(i128), MM, f); if (fclose(f)) fatal("memstream close");
  unsigned char dg[32]; char hx[65]; CC_SHA256(mb, (CC_LONG)ms, dg); hexs(dg, hx);
  FILE *g = fopen(tmp, "wb"); if (!g) fatal("cannot write ckpt");
  if (fwrite(mb, 1, ms, g) != ms || fprintf(g, "\nEND %s\n", hx) < 0 || fflush(g) || fsync(fileno(g)) || fclose(g)) fatal("ckpt write");
  free(mb); if (rename(tmp, fn)) fatal("ckpt rename");
}
typedef struct { i128 *acc; u128 err; rec_t *recs; long nrec; } ck_t;
static int read_ckpt(const char *fn, ck_t *ck) {                                /* returns 1 if valid; fatal on corruption */
  FILE *f = fopen(fn, "rb"); if (!f) return 0; fseek(f, 0, SEEK_END); long sz = ftell(f); fseek(f, 0, SEEK_SET);
  unsigned char *buf = malloc(sz + 1); if (fread(buf, 1, sz, f) != (size_t)sz) fatal("ckpt read"); fclose(f); buf[sz] = 0;
  if (sz < 80) fatal("ckpt too short"); long e = sz - 70; if (memcmp(buf + e, "\nEND ", 5) || buf[sz - 1] != '\n') fatal("ckpt not terminated");
  unsigned char dg[32], want[32]; CC_SHA256(buf, (CC_LONG)e, dg);
  for (int i = 0; i < 32; i++) { unsigned v; if (sscanf((char *)buf + e + 5 + 2 * i, "%2x", &v) != 1) fatal("ckpt hash"); want[i] = (unsigned char)v; }
  if (memcmp(dg, want, 32)) fatal("ckpt self-hash mismatch (corrupted checkpoint)");
  char *p = (char *)buf; if (strncmp(p, "ACC2243CKPT v1\nPARAMS ", 22)) fatal("ckpt header"); p += 22;
  char *nl = strchr(p, '\n'); if (!nl) fatal("ckpt params"); *nl = 0; if (strcmp(p, PARAMS)) fatal("ckpt PARAMS differ from this run (refusing to mix)"); p = nl + 1;
  int fb; long nrec; if (sscanf(p, "FBITS %d\nNREC %ld\n", &fb, &nrec) != 2 || fb != FBITS) fatal("ckpt FBITS/NREC");
  p = strchr(p, '\n') + 1; p = strchr(p, '\n') + 1;
  ck->recs = malloc(sizeof(rec_t) * (nrec + 1)); ck->nrec = nrec;
  for (long i = 0; i < nrec; i++) { unsigned long long fpv, nt, cn; char hx[65]; long u;
    if (sscanf(p, "U %ld fp %llx nterm %llu cnt %llu hash %64s", &u, &fpv, &nt, &cn, hx) != 5) fatal("ckpt record");
    ck->recs[i].u = u; ck->recs[i].fp = fpv; ck->recs[i].nterm = nt; ck->recs[i].cnt = cn;
    for (int j = 0; j < 32; j++) { unsigned v; sscanf(hx + 2 * j, "%2x", &v); ck->recs[i].h[j] = (unsigned char)v; }
    p = strchr(p, '\n') + 1; }
  unsigned long long eh, el, mm; if (sscanf(p, "ERR %16llx%16llx\nACC %llu\n", &eh, &el, &mm) != 3 || mm != MM) fatal("ckpt ERR/ACC");
  ck->err = ((u128)eh << 64) | el; p = strchr(p, '\n') + 1; p = strchr(p, '\n') + 1;
  if ((unsigned char *)p + MM * sizeof(i128) != buf + e) fatal("ckpt array length");
  ck->acc = malloc(MM * sizeof(i128)); memcpy(ck->acc, p, MM * sizeof(i128)); free(buf); return 1;
}
static long list_ckpts(char names[][512], long cap) {
  DIR *d = opendir(OUT); if (!d) return 0; struct dirent *de; long n = 0;
  while ((de = readdir(d))) { if (!strncmp(de->d_name, "ckpt_g", 6) && strstr(de->d_name, ".bin") && !strstr(de->d_name, ".tmp")) {
      if (n >= cap) fatal("too many ckpts"); snprintf(names[n++], 512, "%s/%s", OUT, de->d_name); } }
  closedir(d); return n;
}
/* ---------------- run ---------------- */
static long NEXTU; static int W;
static void *worker(void *arg) {
  int wid = (int)(long)arg; accum_t a; accum_init(&a); long cap = 1024, nrec = 0; rec_t *recs = malloc(sizeof(rec_t) * cap);
  u64 *rem = malloc(BLK * 8); i64 *an = malloc(BLK * 8); unsigned char *comp = malloc(SEGQ); int32_t *buf = malloc(4 * SEGQ);
  long since = 0; double tlast = now(); FILE *tl = NULL; char sdir[2048] = "";
  if (TIMING) { char fn[2100]; snprintf(fn, sizeof fn, "%s/timing_g%03d_w%02d%s.txt", OUT, GEN, wid, TAGSUF); tl = fopen(fn, "a"); if (!tl) fatal("timing log"); }
  if (STREAM_CMD) { snprintf(sdir, sizeof sdir, "%s/stream_g%03d_w%02d%s", OUT, GEN, wid, TAGSUF); mkdir(sdir, 0755); }   /* per generation: never shared with orphans of a killed run */
  for (;;) { long u = __atomic_fetch_add(&NEXTU, 1, __ATOMIC_SEQ_CST); if (u >= NUNIT) break;
    if (DONE[u] || (SEL && !SEL[u]) || (SHARD_N > 1 && u % SHARD_N != SHARD_I)) continue;
    if (nrec >= cap) { cap *= 2; recs = realloc(recs, sizeof(rec_t) * cap); }
    rec_t *rc = &recs[nrec]; rc->u = u; double t0 = now(), ts = 0;
    if (!IS_S(u)) { lunit_t *x = &LU[u]; const char *dir = APDIR; int streamed = 0; char fn[2200];
      snprintf(fn, sizeof fn, "%s/ap_%06ld.bin", APDIR, x->s);
      if (STREAM_CMD && access(fn, F_OK) != 0) {
        if (x->nsub != 1) fatal("segment with several sub-units is absent from apdir: pre-produce it (streaming serves single-unit segments only)");
        char cmd[8192]; snprintf(cmd, sizeof cmd, "%s %ld %s", STREAM_CMD, x->s, sdir);
        if (system(cmd) != 0) fatal("stream command failed (produce/verify): fail closed"); dir = sdir; streamed = 1; ts = now() - t0; }
      run_L(dir, x->s, x->m0, x->m1, &a, rc, comp, buf);
      { char hf[2200], want[80] = "", got[65]; snprintf(hf, sizeof hf, "%s/ap_%06ld.sha256", dir, x->s); FILE *h = fopen(hf, "r");
        if (h) { if (fscanf(h, "%64s", want) != 1) fatal("unreadable .sha256 companion"); fclose(h); hexs(rc->h, got);
          if (strcmp(want, got)) fatal("a_q file consumed differs from the file the verifier hashed: fail closed"); }
        else if (streamed) fatal("streamed segment without the verifier's .sha256 companion");
        if (streamed) { if (unlink(hf)) fatal("stream cleanup"); } }
      if (streamed) { snprintf(fn, sizeof fn, "%s/ap_%06ld.bin", sdir, x->s); if (unlink(fn)) fatal("stream cleanup"); } }
    else run_S(BLK_OF(u), &a, rc, rem, an);
    double t1 = now(); nrec++; since++;
    if (tl) { fprintf(tl, "U %ld %c %ld stream_s %.3f acc_s %.3f nterm %llu cnt %llu\n", u, IS_S(u) ? 'S' : 'L', IS_S(u) ? BLK_OF(u) : LU[u].s,
                      ts, t1 - t0 - ts, (unsigned long long)rc->nterm, (unsigned long long)rc->cnt); fflush(tl); }
    long g = __atomic_add_fetch(&NDONE_GLOBAL, 1, __ATOMIC_SEQ_CST);
    if (DIE_AFTER && g >= DIE_AFTER) { fprintf(stderr, "SIMULATED CRASH after %ld units (worker %d)\n", g, wid); _exit(9); }
    if (since >= CKPT_UNITS || (CKPT_SECS > 0 && t1 - tlast >= CKPT_SECS)) { write_ckpt(wid, &a, recs, nrec); since = 0; tlast = now(); } }
  if (nrec && since) write_ckpt(wid, &a, recs, nrec);
  if (tl) fclose(tl);
  free(rem); free(an); free(comp); free(buf); free(recs); free(a.acc); flint_cleanup(); return NULL;
}
static void setup_common(int argc, char **argv, int *ai) {
  if (argc < 13) fatal("too few arguments (see usage)");
  curve(argv); *ai = 7; MM = strtoull(argv[(*ai)++], 0, 10); QQ = strtoull(argv[(*ai)++], 0, 10); SIGN = atoi(argv[(*ai)++]);
  T = strtoull(argv[(*ai)++], 0, 10); SEGQ = strtoull(argv[(*ai)++], 0, 10); APDIR = argv[(*ai)++];
  if (T < 4 || SEGQ < 1024 || MM < 2 || (SIGN != 1 && SIGN != -1)) fatal("bad parameters");
  { u64 g = QQ, h = MM; while (h) { u64 r = g % h; g = h; h = r; } if (g != 1) fatal("gcd(Q, m) != 1"); }
  RT = 1; while ((RT + 1) * (RT + 1) <= T) RT++;
  (void)argc;
}
static void setup_tables(void) {
  small_primes(); NSEG = (long)(T / SEGQ) + 1; APSH = calloc(NSEG, 32); set_kappa(); load_table(RT);
  EG = _arb_vec_init(GMAX + 1); arb_t t; arb_init(t);
  for (long g = 0; g <= GMAX; g++) { arb_mul_ui(t, KAPPA, (ulong)g, NPREC); arb_neg(t, t); arb_exp(EG + g, t, NPREC); }
  u64 *rem = malloc(8 * (RT + 1)); i64 *am = malloc(8 * (RT + 1)); gen_block(1, RT + 1, rem, am); AMT = _arb_vec_init(RT + 1);
  for (u64 m = 1; m <= RT; m++) { if (rem[m - 1] != 1) fatal("m <= RT not RT-smooth"); arb_set_si(AMT + m, am[m - 1]); arb_div_ui(AMT + m, AMT + m, m, NPREC); }
  free(rem); free(am); arb_clear(t);
  RHO = malloc(8 * MM); for (u64 k = 0; k < MM; k++) RHO[k] = splitmix64(k + 1);
}
static void base_params(char *out, size_t n) {
  snprintf(out, n, "%lld %lld %lld %lld %lld m=%llu Q=%llu s=%d T=%llu SEGQ=%llu UT=", (long long)a1, (long long)a2, (long long)a3, (long long)a4, (long long)a6,
           (unsigned long long)MM, (unsigned long long)QQ, SIGN, (unsigned long long)T, (unsigned long long)SEGQ);
}
int main(int argc, char **argv) {
  if (fegetround() != FE_TONEAREST) fatal("FP rounding mode is not round-to-nearest");
  if (argc < 2) fatal("usage: see header");
  if (!strcmp(argv[1], "dftbench")) {
    if (argc < 3) fatal("dftbench m");
    long m = atol(argv[2]); acb_ptr v = _acb_vec_init(m), w = _acb_vec_init(m);
    for (long k = 0; k < m; k++) { arb_set_si(acb_realref(v + k), (slong)(splitmix64(k) % 2000001) - 1000000); arb_mul_2exp_si(acb_realref(v + k), acb_realref(v + k), -10); }
    double t0 = now(); acb_dft(w, v, m, PREC); double t1 = now();
    printf("DFTBENCH m %ld seconds %.2f  sample_radius %.3e\n", m, t1 - t0, mag_get_d(arb_radref(acb_realref(w + 1)))); return 0; }
  int ai; setup_common(argc, argv, &ai);
  if (!strcmp(argv[1], "plan")) {                     /* unit layout only: which segments must be pre-produced (several sub-units) */
    if (argc < ai + 1) fatal("plan: UNIT_TERMS");
    UNIT_TERMS = strtoull(argv[ai++], 0, 10); if (UNIT_TERMS < 1000) fatal("bad UNIT_TERMS"); build_units();
    long multi = 0, last = -1; for (long u = 0; u < NL; u++) if (LU[u].nsub > 1 && LU[u].s != last) { last = LU[u].s; multi++; printf("MULTI %ld %ld\n", LU[u].s, LU[u].nsub); }
    printf("PLAN RT %llu segments %ld L-subunits %ld S-blocks %ld units %ld multi-subunit segments %ld (pre-produce these; the rest may stream)\n",
           (unsigned long long)RT, NSEG, NL, NBLK, NUNIT, multi); return 0; }
  if (!strcmp(argv[1], "unit")) {                     /* benchmark ONE unit, no checkpoint */
    if (argc < ai + 3) fatal("unit: too few arguments");
    UNIT_TERMS = strtoull(argv[ai++], 0, 10); char kind = argv[ai++][0]; long idx = atol(argv[ai++]); long jidx = argc > ai ? atol(argv[ai++]) : 0;
    { const char *pe = getenv("ACC_PROFILE"); if (pe) PROFILE = atoi(pe); }
    double t0 = now(); setup_tables(); double t1 = now();
    accum_t a; accum_init(&a); rec_t rc; u64 *rem = malloc(BLK * 8); i64 *an = malloc(BLK * 8); unsigned char *comp = malloc(SEGQ); int32_t *buf = malloc(4 * SEGQ);
    u64 m0 = 0, m1 = 0; long J = 0;
    if (kind == 'L') { u64 mmax; J = sub_count(idx, &mmax); if (!J) fatal("segment has no primes > RT"); u64 step = (mmax + J - 1) / J;
      m0 = 1 + (u64)jidx * step; m1 = m0 + step; if (m1 > mmax + 1) m1 = mmax + 1;
      double t2 = now(); run_L(APDIR, idx, m0, m1, &a, &rc, comp, buf); double t3 = now();
      printf("UNIT L seg %ld sub %ld/%ld m [%llu,%llu) pairs %llu terms %llu seconds %.3f setup %.1f ns_per_term %.1f\n", idx, jidx, J,
             (unsigned long long)m0, (unsigned long long)m1, (unsigned long long)rc.cnt, (unsigned long long)rc.nterm, t3 - t2, t1 - t0, rc.nterm ? 1e9 * (t3 - t2) / rc.nterm : 0.0); }
    else { double t2 = now(); run_S(idx, &a, &rc, rem, an); double t3 = now(); if (PROFILE < 2) rc.nterm = rc.cnt;
      printf("UNIT S blk %ld smooth %llu terms %llu seconds %.3f setup %.1f ns_per_n %.1f\n", idx, (unsigned long long)rc.cnt, (unsigned long long)rc.nterm, t3 - t2, t1 - t0, 1e9 * (t3 - t2) / BLK); }
    if (getenv("ACC_CKPT_BENCH")) { OUT = getenv("ACC_CKPT_BENCH"); mkdir(OUT, 0755); GEN = 0; snprintf(PARAMS, sizeof PARAMS, "bench");
      double t4 = now(); write_ckpt(0, &a, &rc, 1); double t5 = now(); printf("CKPT_WRITE bytes %llu seconds %.3f\n", (unsigned long long)(MM * 16), t5 - t4); }
    return 0; }
  if (getenv("ACC_PROFILE")) fatal("ACC_PROFILE is for unit benchmarks only");
  if (!strcmp(argv[1], "run")) {
    if (argc < ai + 4) fatal("run: too few arguments");
    W = atoi(argv[ai++]); OUT = argv[ai++]; UNIT_TERMS = strtoull(argv[ai++], 0, 10); CKPT_UNITS = atol(argv[ai++]); if (argc > ai) DIE_AFTER = atol(argv[ai++]);
    if (W < 1 || W > MAXW || UNIT_TERMS < 1000 || CKPT_UNITS < 1) fatal("bad run parameters");
    { const char *e;
      if ((e = getenv("ACC_SELECT"))) parse_select(e);
      if ((e = getenv("ACC_STREAM_CMD")) && *e) STREAM_CMD = e;
      if ((e = getenv("ACC_TIMING_LOG"))) TIMING = atoi(e) != 0;
      if ((e = getenv("ACC_CKPT_SECS"))) CKPT_SECS = atof(e);
      if ((e = getenv("ACC_SHARD"))) { if (sscanf(e, "%ld/%ld", &SHARD_I, &SHARD_N) != 2 || SHARD_N < 1 || SHARD_I < 0 || SHARD_I >= SHARD_N) fatal("ACC_SHARD must be i/n"); }
      if ((e = getenv("ACC_TAG"))) { if (!*e || strlen(e) > 32) fatal("ACC_TAG length"); for (const char *c = e; *c; c++) if (!((*c >= 'a' && *c <= 'z') || (*c >= 'A' && *c <= 'Z') || (*c >= '0' && *c <= '9'))) fatal("ACC_TAG must be alphanumeric");
        snprintf(TAGSUF, sizeof TAGSUF, "_t%s", e); } }
    mkdir(OUT, 0755);
    { char lk[2100]; snprintf(lk, sizeof lk, "%s/run.lock", OUT); int lfd = open(lk, O_CREAT | O_RDWR, 0644); if (lfd < 0) fatal("run.lock open");
      if (flock(lfd, LOCK_EX | LOCK_NB)) fatal("another live run process holds outdir/run.lock"); }        /* released by the kernel at exit */
    char bp[4096]; base_params(bp, sizeof bp);
    if (NSELT) snprintf(PARAMS, sizeof PARAMS, "%s%llu SEL=%s", bp, (unsigned long long)UNIT_TERMS, SELSTR); else snprintf(PARAMS, sizeof PARAMS, "%s%llu", bp, (unsigned long long)UNIT_TERMS);
    setup_tables(); build_units(); mark_selection(); DONE = calloc(NUNIT, 1);
    static char names[MAXCK][512]; long nc = list_ckpts(names, MAXCK); GEN = 1; long ndone = 0;
    for (long i = 0; i < nc; i++) { ck_t ck; read_ckpt(names[i], &ck); int g; sscanf(strstr(names[i], "ckpt_g") + 6, "%d", &g); if (g >= GEN) GEN = g + 1;
      for (long j = 0; j < ck.nrec; j++) { long u = ck.recs[j].u; if (u < 0 || u >= NUNIT) fatal("ckpt unit out of range"); if (SEL && !SEL[u]) fatal("ckpt holds an unselected unit");
        if (DONE[u]) fatal("unit recorded twice"); DONE[u] = 1; ndone++; }
      free(ck.recs); free(ck.acc); }
    printf("RUN units %ld (L-subunits %ld + S-blocks %ld), selected %ld, shard %ld/%ld, already done %ld in %ld checkpoints, generation %d, W %d%s\n",
           NUNIT, NL, NBLK, NSEL, SHARD_I, SHARD_N, ndone, nc, GEN, W, STREAM_CMD ? ", streaming a_q" : ""); fflush(stdout);
    NEXTU = 0; double t0 = now();
    static pthread_t th[MAXW]; for (long i = 0; i < W; i++) pthread_create(&th[i], NULL, worker, (void *)i); for (long i = 0; i < W; i++) pthread_join(th[i], NULL);
    printf("RUN done seconds %.2f\n", now() - t0); return 0; }
  if (!strcmp(argv[1], "merge")) {
    if (argc < ai + 2) fatal("merge: too few arguments");
    OUT = argv[ai++]; long LATDEN = atol(argv[ai++]); long pw = 0, nw = 0, rw = 0, alpha = 1;
    if (LATDEN < 1) fatal("LATDEN must be >= 1");
    if (argc > ai + 3) { pw = atol(argv[ai++]); nw = atol(argv[ai++]); rw = atol(argv[ai++]); alpha = atol(argv[ai++]); }
    /* PARAMS must match the run: UT and the selection are read from the first checkpoint's PARAMS line */
    static char names[MAXCK][512]; long nc = list_ckpts(names, MAXCK); if (!nc) fatal("no checkpoints");
    { FILE *f = fopen(names[0], "rb"); char line[8192]; if (!fgets(line, sizeof line, f) || !fgets(line, sizeof line, f)) fatal("ckpt read"); fclose(f);
      line[strcspn(line, "\n")] = 0; strcpy(PARAMS, line + 7); char *ut = strstr(PARAMS, "UT="); if (!ut) fatal("PARAMS UT"); UNIT_TERMS = strtoull(ut + 3, 0, 10);
      char want[4096]; base_params(want, sizeof want);
      if (strncmp(PARAMS, want, strlen(want))) fatal("merge command line does not match the checkpoints' PARAMS");
      char *sl = strstr(PARAMS, " SEL="); const char *es = getenv("ACC_SELECT");
      if (sl) { parse_select(sl + 5); if (es && strcmp(es, SELSTR)) fatal("ACC_SELECT differs from the checkpoints' selection"); }
      else if (es) fatal("ACC_SELECT given but the checkpoints are a full (unselected) run"); }
    small_primes(); NSEG = (long)(T / SEGQ) + 1; APSH = calloc(NSEG, 32); set_kappa(); build_units(); mark_selection();
    RHO = malloc(8 * MM); for (u64 k = 0; k < MM; k++) RHO[k] = splitmix64(k + 1);
    i128 *tot = calloc(MM, sizeof(i128)); u128 err = 0; unsigned char *seen = calloc(NUNIT, 1); u64 fpsum = 0, smooth = 0, pairs = 0, nterm = 0;
    unsigned char *segseen = calloc(NSEG, 1);
    for (long i = 0; i < nc; i++) { ck_t ck; read_ckpt(names[i], &ck);
      for (u64 k = 0; k < MM; k++) tot[k] += ck.acc[k]; err += ck.err;
      for (long j = 0; j < ck.nrec; j++) { rec_t *r = &ck.recs[j]; if (r->u < 0 || r->u >= NUNIT) fatal("ckpt unit out of range");
        if (SEL && !SEL[r->u]) fatal("checkpoint holds an unselected unit"); if (seen[r->u]) fatal("unit covered twice"); seen[r->u] = 1; fpsum += r->fp; nterm += r->nterm;
        if (IS_S(r->u)) smooth += r->cnt; else { pairs += r->cnt; long s = LU[r->u].s;
          if (segseen[s] && memcmp(APSH[s], r->h, 32)) fatal("two sub-units of one segment report different a_q hashes");
          memcpy(APSH[s], r->h, 32); segseen[s] = 1; } }
      free(ck.recs); free(ck.acc); }
    long miss = 0; for (long u = 0; u < NUNIT; u++) miss += (!SEL || SEL[u]) && !seen[u];
    u64 fparr = 0; for (u64 k = 0; k < MM; k++) fparr += (u64)tot[k] * RHO[k];
    printf("MERGE checkpoints %ld units %ld selected %ld missing %ld terms %llu%s%s\n", nc, NUNIT, NSEL, miss, (unsigned long long)nterm, SEL ? "  SELECTION " : "", SEL ? SELSTR : "");
    printf("FINGERPRINT sum_units %016llx array %016llx match %d\n", (unsigned long long)fpsum, (unsigned long long)fparr, fpsum == fparr);
    if (miss) fatal("units missing: run incomplete"); if (fpsum != fparr) fatal("fingerprint mismatch");
    if (!SEL) { printf("COUNT smooth %llu pairs %llu sum %llu T %llu identity %d\n", (unsigned long long)smooth, (unsigned long long)pairs,
                       (unsigned long long)(smooth + pairs), (unsigned long long)T, smooth + pairs == T);
      if (smooth + pairs != T) fatal("count identity fails"); }
    else { unsigned char *comp = malloc(SEGQ); u64 want = 0; for (long u = 0; u < NL; u++) if (SEL[u]) want += recount_pairs(LU[u].s, LU[u].m0, LU[u].m1, comp); free(comp);
      printf("COUNT_SELECTION pairs %llu recount %llu match %d  smooth %llu (S-block smooth counts are covered only by the full-run identity)\n",
             (unsigned long long)pairs, (unsigned long long)want, pairs == want, (unsigned long long)smooth);
      if (pairs != want) fatal("selection pair recount fails"); }
    /* a_q segment root: full run as in S2 (unseen segments re-read); selection: the selected segments only */
    { unsigned char *comp = malloc(SEGQ); int32_t *buf = malloc(4 * SEGQ); long ns = 0; unsigned char *rootbuf = malloc(32 * (size_t)NSEG);
      for (long s = 0; s < NSEG; s++) { u64 lo, hi; seg_bounds(s, &lo, &hi); if (lo >= hi) continue;
        if (SEL) { if (!segseen[s]) continue; } else if (!segseen[s]) read_apseg(APDIR, s, comp, buf, APSH[s]);
        memcpy(rootbuf + 32 * ns, APSH[s], 32); ns++;
        if (SEL && NSEL <= 2000) { char hx[65]; hexs(APSH[s], hx); printf("SEGHASH %ld %s\n", s, hx); } }
      unsigned char root[32]; char hx[65]; CC_SHA256(rootbuf, (CC_LONG)(32 * ns), root); hexs(root, hx); printf("AP_SEGROOT_SHA256 %s segments %ld\n", hx, ns);
      free(comp); free(buf); free(rootbuf); }
    { CC_SHA256_CTX c; CC_SHA256_Init(&c); for (u64 k0 = 0; k0 < MM; k0 += (1u << 20)) { u64 n = MM - k0 < (1u << 20) ? MM - k0 : (1u << 20); CC_SHA256_Update(&c, tot + k0, (CC_LONG)(n * sizeof(i128))); }
      u64 e2[2] = {(u64)(err >> 64), (u64)err}, cn[3] = {smooth, pairs, nterm}; CC_SHA256_Update(&c, e2, 16); CC_SHA256_Update(&c, cn, 24);
      unsigned char dg[32]; char hx[65]; CC_SHA256_Final(dg, &c); hexs(dg, hx); printf("CHUNK_DIGEST %s\n", hx); }
    /* S_k balls: mid = tot_k 2^-F, radius = err 2^-F (global bound) */
    arb_ptr S = _arb_vec_init(MM); fmpz_t z; fmpz_init(z); arb_t er; arb_init(er);
    { fmpz_t e; fmpz_init(e); fmpz_set_ui(e, (ulong)(err >> 64)); fmpz_mul_2exp(e, e, 64); fmpz_add_ui(e, e, (ulong)err); arb_set_fmpz(er, e); arb_mul_2exp_si(er, er, -FBITS); fmpz_clear(e); }
    mag_t em; mag_init(em); arb_get_mag(em, er);
    for (u64 k = 0; k < MM; k++) { i128 v = tot[k]; ulong hi = (ulong)((u128)v >> 64), lo = (ulong)v; fmpz_set_signed_uiui(z, hi, lo);
      arb_set_fmpz(S + k, z); arb_mul_2exp_si(S + k, S + k, -FBITS); arb_add_error_mag(S + k, em); }
    printf("ROUNDING_ERR_TOTAL %s\n", arb_get_str(er, 10, 0));
    arb_t tl; arb_init(tl); arf_t ub; arf_init(ub); tail_ms(tl, KAPPA, T); arb_get_ubound_arf(ub, tl, NPREC); arf_mul_2exp_si(ub, ub, 1);
    printf("TAIL_MS_UPPER_TIMES2 %s\n", arf_get_str(ub, 10));
    for (u64 k = 0; k < MM && MM <= 400; k++) printf("S %llu %s\n", (unsigned long long)k, arb_get_str(S + k, 25, 0));
    /* v2.1: the printed S_k balls carry the global tally E (a valid per-class enclosure). For the SYMBOLS the class sums are used
       as EXACT midpoints and the accumulated rounding is added once per symbol as 2E (l1 bound: sum_k |e_k| <= E, combination
       coefficients <= 2 in absolute value) -- per-class radii would be inflated by acb_dft's Bluestein/Rader steps. */
    for (u64 k = 0; k < MM; k++) mag_zero(arb_radref(S + k));
    { arf_t ue; arf_init(ue); arb_get_ubound_arf(ue, er, NPREC); arf_mul_2exp_si(ue, ue, 1); arf_add(ub, ub, ue, NPREC, ARF_RND_UP); arf_clear(ue); }
    if (getenv("ACC_NOSYMBOLS") && atoi(getenv("ACC_NOSYMBOLS"))) { printf("SYMBOLS skipped (ACC_NOSYMBOLS)\n"); return 0; }
    if (SEL) printf("PARTIAL_SELECTION: the symbols below come from a unit subset -- plumbing/timing output only, NOT symbol values\n");
    arb_t om_p, om_m, re, im, cs, sn, c2, s2; arb_init(om_p); arb_init(om_m); arb_init(re); arb_init(im); arb_init(cs); arb_init(sn); arb_init(c2); arb_init(s2);
    periods(om_p, om_m, NPREC); printf("OMEGA_PLUS %s\nOMEGA_MINUS %s\n", arb_get_str(om_p, 30, 0), arb_get_str(om_m, 30, 0));
    { arb_t bt, br, bl; arb_init(bt); arb_init(br); arb_init(bl); arf_t tt; arf_init(tt); tail_ms(bt, KAPPA, T); arb_mul_2exp_si(bt, bt, 1); arb_div(bt, bt, om_p, NPREC);
      arb_mul_2exp_si(br, er, 1); arb_div(br, br, om_p, NPREC); arb_set_ui(bl, 1); arb_div_ui(bl, bl, 2 * (ulong)LATDEN, NPREC);
      printf("SYMBOL_RADIUS_BUDGET plus: tail 2tail/Omega+ %s + rounding 2E/Omega+ %s (+ transform rounding, printed per symbol) vs threshold 1/(2 LATDEN) %s\n",
             arb_get_str(bt, 6, ARB_STR_NO_RADIUS), arb_get_str(br, 6, ARB_STR_NO_RADIUS), arb_get_str(bl, 6, ARB_STR_NO_RADIUS));
      arb_clear(bt); arb_clear(br); arb_clear(bl); arf_clear(tt); }
    int use_dft = MM > 400; { const char *e = getenv("ACC_DFT"); if (e) use_dft = atoi(e) != 0; }
    if (!use_dft && MM > 100000) fatal("direct symbol sum is O(m phi(m)): use the DFT path for large m");
    acb_ptr FD = NULL;
    if (use_dft) { acb_ptr V = _acb_vec_init(MM); FD = _acb_vec_init(MM); for (u64 k = 0; k < MM; k++) arb_set(acb_realref(V + k), S + k);
      double t0 = now(); acb_dft(FD, V, MM, PREC); printf("DFT length %llu seconds %.2f\n", (unsigned long long)MM, now() - t0); _acb_vec_clear(V, MM); }
    FILE *symf = NULL; CC_SHA256_CTX symc; char symfn[2100];
    if (MM > 400) { snprintf(symfn, sizeof symfn, "%s/symbols.bin", OUT); symf = fopen(symfn, "wb"); if (!symf) fatal("symbols.bin"); CC_SHA256_Init(&symc); }
    fmpq_t fr; fmpq_init(fr); arf_t ra; arf_init(ra); long ndet = 0, nb = 0, ndetm = 0; double maxrad = 0;
    slong *XP = calloc(MM, sizeof(slong)); int *XOK = calloc(MM, sizeof(int)); arb_ptr XR = _arb_vec_init(MM);
    double ts0 = now();
    for (u64 b = 1; b < MM; b++) { u64 g = b, h = MM; while (h) { u64 r = g % h; g = h; h = r; } if (g != 1) continue; nb++;
      u64 ub_ = invmod((QQ % MM) * b % MM, MM);
      if (use_dft) {        /* acb_dft: FD_j = sum_k S_k e^{-2 pi i jk/m}; so sum_k S_k cos(2 pi jk/m) = Re FD_j, sum_k S_k sin(2 pi jk/m) = -Im FD_j */
        arb_set(re, acb_realref(FD + b)); arb_neg(im, acb_imagref(FD + b));
        if (SIGN > 0) { arb_add(re, re, acb_realref(FD + ub_), PREC); arb_add(im, im, acb_imagref(FD + ub_), PREC); }
        else { arb_sub(re, re, acb_realref(FD + ub_), PREC); arb_sub(im, im, acb_imagref(FD + ub_), PREC); } }
      else { arb_zero(re); arb_zero(im);
        for (u64 k = 0; k < MM; k++) {
          fmpq_set_si(fr, (slong)(2 * ((k * b) % MM)), MM); arb_sin_cos_pi_fmpq(sn, cs, fr, PREC);
          fmpq_set_si(fr, (slong)(2 * ((k * ub_) % MM)), MM); arb_sin_cos_pi_fmpq(s2, c2, fr, PREC);
          if (SIGN > 0) { arb_add(cs, cs, c2, PREC); arb_sub(sn, sn, s2, PREC); } else { arb_sub(cs, cs, c2, PREC); arb_add(sn, sn, s2, PREC); }
          arb_addmul(re, S + k, cs, PREC); arb_addmul(im, S + k, sn, PREC); } }
      arb_add_error_arf(re, ub); arb_add_error_arf(im, ub);
      arb_div(re, re, om_p, PREC); arb_div(im, im, om_m, PREC); arb_set(XR + b, re);
      { double rr = mag_get_d(arb_radref(re)); if (rr > maxrad) maxrad = rr; }
      int cp, up, ci, ui; slong hp, hm;
      { double md = arf_get_d(arb_midref(re), ARF_RND_NEAR); hp = (slong)(md * LATDEN + (md >= 0 ? 0.5 : -0.5));
        fmpq_set_si(fr, hp, (ulong)LATDEN); cp = arb_contains_fmpq(re, fr);
        arf_set_mag(ra, arb_radref(re)); arf_mul_ui(ra, ra, 2 * (ulong)LATDEN, ARF_PREC_EXACT, ARF_RND_UP); up = arf_cmp_si(ra, 1) < 0; }
      { double md = arf_get_d(arb_midref(im), ARF_RND_NEAR); hm = (slong)(md * LATDEN + (md >= 0 ? 0.5 : -0.5));
        fmpq_set_si(fr, hm, (ulong)LATDEN); ci = arb_contains_fmpq(im, fr);
        arf_set_mag(ra, arb_radref(im)); arf_mul_ui(ra, ra, 2 * (ulong)LATDEN, ARF_PREC_EXACT, ARF_RND_UP); ui = arf_cmp_si(ra, 1) < 0; }
      ndet += cp && up; ndetm += ci && ui; XP[b] = hp; XOK[b] = cp && up;
      if (symf) { i64 rec[3] = {(i64)b, (i64)hp, (i64)hm}; unsigned char fl = (unsigned char)(cp | up << 1 | ci << 2 | ui << 3);
        if (fwrite(rec, 8, 3, symf) != 3 || fwrite(&fl, 1, 1, symf) != 1) fatal("symbols write"); CC_SHA256_Update(&symc, rec, 24); CC_SHA256_Update(&symc, &fl, 1); }
      else printf("XB %llu plus %s cand %ld/%ld contains %d unique %d minus %s cand %ld/%ld contains %d unique %d\n", (unsigned long long)b,
                  arb_get_str(re, 20, 0), (long)hp, LATDEN, cp, up, arb_get_str(im, 20, 0), (long)hm, LATDEN, ci, ui); }
    if (symf) { if (fclose(symf)) fatal("symbols close"); unsigned char dg[32]; char hx[65]; CC_SHA256_Final(dg, &symc); hexs(dg, hx);
      printf("SYMBOLS_FILE %s records %ld sha256 %s (record: i64 b, i64 plus cand, i64 minus cand, u8 flags c+|u+<<1|c-<<2|u-<<3)\n", symfn, nb, hx); }
    printf("SYMBOL_PASS seconds %.2f path %s\n", now() - ts0, use_dft ? "dft" : "direct");
    printf("XB_PLUS_DETERMINED %ld of %ld (lattice 1/%ld Z)   minus determined %ld   max plus radius %.6e (unique iff < %.6e)\n", ndet, nb, LATDEN, ndetm, maxrad, 0.5 / (double)LATDEN);
    if (pw && SEL && !(getenv("ACC_PARTIAL_WEIGHTS_TIMING") && atoi(getenv("ACC_PARTIAL_WEIGHTS_TIMING")))) {
      printf("WEIGHTS skipped: partial selection (a_{n,r}, the unit test and the nonzero-only test exist only for a full run)\n"); pw = 0; }
    if (pw && SEL) printf("PARTIAL_TIMING_ONLY: the a_{n,r} / UNIT_TEST / NONZERO_ONLY lines below are computed from a unit subset and mean NOTHING\n");
    if (pw) {                                        /* depth-n coefficient a_{n,r} (SW / Lane 3 convention) and the nonzero-only test */
      u64 pn = 1; for (long i = 0; i < nw; i++) pn *= (u64)pw; if (pn != MM) fatal("weights: m must equal p^n");
      u64 ord = pn / (u64)pw; u64 *dlog = malloc(sizeof(u64) * pn); for (u64 i = 0; i < pn; i++) dlog[i] = (u64)-1;
      u64 g1 = 1; for (u64 j = 0; j < ord; j++) { dlog[g1] = j; g1 = (u64)(((u128)g1 * (1 + pw)) % pn); }
      fmpz_t Aex, c, t2; fmpz_init(Aex); fmpz_init(c); fmpz_init(t2); int allok = 1; arb_t Zb, wb; arb_init(Zb); arb_init(wb); long wsum = 0;
      for (u64 b = 1; b < pn; b++) { if (b % pw == 0) continue;
        u128 om = 1, bb = b; u64 e = ord; while (e) { if (e & 1) om = om * bb % pn; bb = bb * bb % pn; e >>= 1; }   /* omega(b) = b^{p^{n-1}} mod p^n */
        u64 inv = invmod((u64)om, pn); u64 onep = (u64)(((u128)b * inv) % pn); if (dlog[onep] == (u64)-1) fatal("1-unit dlog");
        u64 j = dlog[onep]; fmpz_bin_uiui(c, j, (ulong)rw);                                  /* C(j, r) */
        if (!XOK[b]) allok = 0; fmpz_mul_si(t2, c, XP[b]); fmpz_add(Aex, Aex, t2);          /* exact: sum C(j,r) * (LATDEN x_b) */
        long wr = (long)fmpz_fdiv_ui(c, (ulong)pw); if (wr > pw / 2) wr -= pw; wsum += labs(wr);
        arb_set_si(wb, wr); arb_addmul(Zb, wb, XR + b, PREC); }
      /* a_{n,r} = alpha^{-n} sum mu... ; alpha = +-1 so alpha^{-n} = alpha^n */
      if (nw % 2 && alpha < 0) fmpz_neg(Aex, Aex);
      printf("WEIGHTS p %ld n %ld r %ld alpha %ld  all_symbols_identified %d\n", pw, nw, rw, alpha, allok);
      if (allok) { fmpz_t q, rr; fmpz_init(q); fmpz_init(rr); fmpz_fdiv_q_ui(q, Aex, (ulong)LATDEN); fmpz_set_ui(rr, fmpz_fdiv_ui(Aex, (ulong)LATDEN));
        printf("A_EXACT LATDEN*a_{n,r} = "); fmpz_print(Aex); printf("   (a_{n,r} = LATDEN-multiple / %ld; remainder mod LATDEN ", LATDEN); fmpz_print(rr); printf(")\n");
        printf("A_MOD_P (LATDEN * a_{n,r}) mod p = %lu   UNIT_TEST %s\n", fmpz_fdiv_ui(Aex, (ulong)pw), fmpz_fdiv_ui(Aex, (ulong)pw) ? "PASS (a_{n,r} is a p-adic unit)" : "FAIL (divisible by p: nothing established)");
        fmpz_clear(q); fmpz_clear(rr); }
      /* nonzero-only test on the ball enclosure, balanced weights over all units: K' = LATDEN * Z */
      arb_mul_ui(Zb, Zb, (ulong)LATDEN, PREC); if (nw % 2 && alpha < 0) arb_neg(Zb, Zb);
      arf_t lo_, hi_; fmpz_t fl, fh; arf_init(lo_); arf_init(hi_); fmpz_init(fl); fmpz_init(fh);
      arb_get_lbound_arf(lo_, Zb, PREC); arb_get_ubound_arf(hi_, Zb, PREC);
      arf_div_ui(lo_, lo_, (ulong)pw, PREC, ARF_RND_FLOOR); arf_div_ui(hi_, hi_, (ulong)pw, PREC, ARF_RND_CEIL);
      arf_get_fmpz(fl, lo_, ARF_RND_CEIL); arf_get_fmpz(fh, hi_, ARF_RND_FLOOR);
      printf("NONZERO_ONLY K'=LATDEN*Z ball %s  weight_mass %ld  ceil(L/p) ", arb_get_str(Zb, 20, 0), wsum); fmpz_print(fl); printf(" floor(U/p) "); fmpz_print(fh);
      printf("  EXCLUDES_pZ %d\n", fmpz_cmp(fl, fh) > 0);
      fmpz_clear(Aex); fmpz_clear(c); fmpz_clear(t2); arb_clear(Zb); arb_clear(wb); }
    return 0; }
  fatal("mode must be run, merge, unit or dftbench"); return 1;
}
