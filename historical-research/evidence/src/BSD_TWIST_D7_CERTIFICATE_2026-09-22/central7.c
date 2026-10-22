/* Isolated D=-7 CENTRAL-VALUE adapter.  L(E^-7,1) = 2 sum chi(n) a_n/n exp(-c n),
 * c = 2 pi / (7 sqrt N).  Structure follows the sealed D=-23 first-derivative
 * adapter exactly; the only mathematical changes are:
 *   (a) chi is the Legendre symbol mod 7   (D = -7 = 1 mod 4, so (D/p) = (p/7)),
 *   (b) the weight is exp(-c n) instead of E1(c n)  -- so the entire E1 Taylor
 *       node-table apparatus is removed and arb_exp is called directly,
 *   (c) the tail is 2*tail_ms(c,T) instead of 2*tail_ms(c,T)/(cT).  That factor
 *       (cT) is exactly the E1(x) <= e^-x / x bound the derivative adapter used,
 *       so the central value is the base case of the same family.
 * The included retained source is byte-identical to the sealed C11 engine
 * (sha256 56a43aac38161d48848df4ed5c2f931f1dc7d5db745600bd140e4be3cac67fd7);
 * its main is never called here. */
#define main retained_main
#include "retained_arbcore.c"
#undef main
#include <math.h>
#include <time.h>

static int chi[7];
static arb_t ONE;
static __thread arb_t EX, ET, EV, EW;
static long USTART, UEND;

static void init_twist(void) {
  arb_init(ONE); arb_one(ONE); arb_init(CL2);
  arb_t x, y; arb_init(x); arb_init(y); arb_const_pi(x, NPREC);
  arb_sqrt_ui(y, 6503188012738584ULL, NPREC); arb_mul_ui(y, y, 7, NPREC);
  arb_div(CL2, x, y, NPREC); arb_mul_2exp_si(CL2, CL2, 1);   /* c = 2 pi / (7 sqrt N) */
  for (int r = 1; r < 7; r++) chi[r] = -1;
  for (int r = 1; r < 7; r++) chi[(r * r) % 7] = 1;          /* chi[0] stays 0 */
  arb_clear(x); arb_clear(y);
}
/* exp(-c n): no node model, no Taylor remainder. Arb's own enclosure is the bound. */
static void w_eval(arb_t out, const arb_t x) {
  arb_neg(out, x); arb_exp(out, out, PREC);
}
static void tail_central(arb_t out, u64 cutoff) {
  /* |2 sum_{n>T} chi(n) a_n/n e^{-cn}| <= 2 tail_MS(c,T); inherited elementary tail_MS. */
  tail_ms(out, CL2, cutoff); arb_mul_2exp_si(out, out, 1);
}
static void add_term(arb_t sum, u64 n, i64 a) {
  int ch = chi[n % 7]; if (!ch || !a) return;
  arb_mul_ui(EX, CL2, n, PREC); w_eval(EV, EX);
  arb_mul_si(EV, EV, a * ch, PREC); arb_div_ui(EV, EV, n, PREC);
  arb_add(sum, sum, EV, PREC);
}
static void twist_block(long b, u64 *rem, i64 *an, long u) {
  u64 lo = (u64)b * BLK + 1, hi = lo + BLK; if (hi > T + 1) hi = T + 1;
  gen_block(lo, hi, rem, an, 0); CC_SHA256_CTX hc; CC_SHA256_Init(&hc);
  u64 nsm = 0, nnz = 0;
  arb_ptr sum = _arb_vec_init(1);
  for (u64 n = lo; n < hi; n++) {
    i64 v = rem[n - lo] == 1 ? an[n - lo] : 0; CC_SHA256_Update(&hc, &v, 8);
    if (rem[n - lo] != 1) continue; nsm++;
    if (v && chi[n % 7]) { nnz++; add_term(sum, n, v); }
  }
  unsigned char dg[32]; char hx[65], tmp[2100], fn[2048];
  CC_SHA256_Final(dg, &hc); hexs(dg, hx); FILE *f = unit_open(u, tmp, fn);
  fprintf(f, "BLK %ld lo %llu hi %llu leaf %s nnz %llu smooth %llu\n", b, lo, hi, hx, nnz, nsm);
  put_sums(f, sum, 1); unit_close(f, tmp, fn); _arb_vec_clear(sum, 1);
}
static void twist_lseg(long s, unsigned char *comp, int32_t *buf, long u) {
  u64 lo, hi; seg_bounds(s, &lo, &hi); unsigned char dg[32]; char hx[65];
  read_apseg(s, comp, buf, dg); hexs(dg, hx);
  arb_ptr sum = _arb_vec_init(1); u64 i = 0, nq = 0, pairs = 0, nnz = 0;
  for (u64 q = lo; q < hi; q++) {
    if (comp[q - lo]) continue; i64 aq = buf[i++]; if (q <= RT) continue;
    u64 mmax = T / q; nq++; pairs += mmax; if (!aq || !chi[q % 7]) continue;
    for (u64 m = 1; m <= mmax; m++) {
      if (!chi[m % 7] || arb_is_zero(AMT + m)) continue;
      u64 n = q * m; arb_mul_ui(EX, CL2, n, PREC); w_eval(EV, EX);
      arb_mul_si(EV, EV, aq * chi[n % 7], PREC); arb_div_ui(EV, EV, q, PREC);
      arb_addmul(sum, EV, AMT + m, PREC); nnz++;
    }
  }
  char tmp[2100], fn[2048]; FILE *f = unit_open(u, tmp, fn);
  fprintf(f, "LSEG %ld lo %llu hi %llu apsha %s bigprimes %llu pairs %llu nnz %llu\n", s, lo, hi, hx, nq, pairs, nnz);
  put_sums(f, sum, 1); unit_close(f, tmp, fn); _arb_vec_clear(sum, 1);
}
static void *twist_worker(void *arg) {
  TID = (int)(long)arg; u64 *rem = malloc(BLK * 8); i64 *an = malloc(BLK * 8);
  unsigned char *comp = malloc(SEGQ); int32_t *buf = malloc(SEGQ * 4);
  arb_init(EX); arb_init(ET); arb_init(EV); arb_init(EW);
  for (;;) {
    long u = __atomic_fetch_add(&NEXTU, 1, __ATOMIC_SEQ_CST);
    if (u >= UEND) break; if (unit_done(u)) continue;
    if (u < NSEG) twist_lseg(u, comp, buf, u); else twist_block(u - NSEG, rem, an, u);
  }
  arb_clear(EX); arb_clear(ET); arb_clear(EV); arb_clear(EW);
  free(rem); free(an); free(comp); free(buf); flint_cleanup(); return NULL;
}
/* The weight has no model to validate, so this checks that the working-precision
 * enclosure of exp(-cn) stays tight across the whole range of n actually used,
 * and cross-checks it against a higher-precision evaluation. */
static int kernel_test(void) {
  arb_t x, a, b; arb_init(x); arb_init(a); arb_init(b);
  long checked = 0, bad = 0; double maxrad = 0;
  u64 bases[] = {1, 1000, 1000000, 16777000, 100000000, 295000000, 1000000000,
                 2000000000ULL, 3003121663ULL, 5000000000ULL};
  for (int q = 0; q < 10; q++) for (int k = 0; k < 128; k++) {
    arb_mul_ui(x, CL2, bases[q] + k, PREC); w_eval(a, x);
    arb_neg(b, x); arb_exp(b, b, NPREC);
    checked++; bad += !arb_overlaps(a, b);
    double rr = mag_get_d(arb_radref(a)); if (rr > maxrad) maxrad = rr;
  }
  printf("EXP_TEST checked %ld nonoverlap %ld max_radius %.12e\n", checked, bad, maxrad);
  for (int q = 0; q < 10; q++) {
    arb_mul_ui(x, CL2, bases[q], PREC); w_eval(a, x);
    printf("EXP_SAMPLE n %llu value %s\n", bases[q], arb_get_str(a, 25, 0));
  }
  arb_clear(x); arb_clear(a); arb_clear(b); return bad ? 4 : 0;
}
/* chi by Euler's criterion mod 7, independent of the lookup table. */
static int chi_pow(u64 n) { int r = (int)(n % 7); if (!r) return 0; int z = 1; for (int k = 0; k < 3; k++) z = z * r % 7; return z == 1 ? 1 : -1; }
/* Independent trial-factor coefficient lookup for short validation blocks.
 * The prime table is reused, but partitioning and kernel are not. */
static i64 test_ap(u64 q, unsigned char *comp, int32_t *buf, long *cached) {
  if (q <= ATOP) return A[q]; long s = q / SEGQ;
  if (s != *cached) { unsigned char d[32]; read_apseg(s, comp, buf, d); *cached = s; }
  u64 lo, hi; seg_bounds(s, &lo, &hi); u64 k = 0;
  for (u64 p = lo; p < q; p++) k += !comp[p - lo];
  if (comp[q - lo]) fatal("test factor not prime"); return buf[k];
}
static i64 test_coeff(u64 n, unsigned char *comp, int32_t *buf, long *cached) {
  i64 out = 1; u64 rem = n;
  for (long i = 0; i < NSP && SP[i] * SP[i] <= rem; i++) {
    u64 p = SP[i]; if (rem % p) continue; i64 ap = A[p], prev = 1, cur = ap; int e = 0;
    while (rem % p == 0) { rem /= p; e++; if (e > 1) { i64 next = is_bad(p) ? cur * ap : ap * cur - (i64)p * prev; prev = cur; cur = next; } }
    out *= cur;
  }
  if (rem > 1) out *= test_ap(rem, comp, buf, cached); return out;
}
static int block_test(void) {
  u64 starts[] = {1, 1000000, 100000000, 295000000, 1000000000, 2000000000ULL, 2999999000ULL};
  const u64 width = 64; long bad = 0, checked = 0;
  u64 *rem = malloc(width * 8); i64 *an = malloc(width * 8);
  unsigned char *comp = malloc(SEGQ); int32_t *buf = malloc(SEGQ * 4); long cached = -1;
  arb_t direct, model, v, x; arb_init(direct); arb_init(model); arb_init(v); arb_init(x);
  arb_init(EX); arb_init(ET); arb_init(EV); arb_init(EW);
  for (int q = 0; q < 7; q++) {
    u64 lo = starts[q], hi = lo + width; if (hi > T + 1) continue;
    gen_block(lo, hi, rem, an, 0); arb_zero(direct); arb_zero(model);
    for (u64 n = lo; n < hi; n++) {
      i64 a = an[n - lo]; if (rem[n - lo] > 1) a *= test_ap(rem[n - lo], comp, buf, &cached);
      i64 ref = test_coeff(n, comp, buf, &cached); if (a != ref) bad++;
      int c = chi_pow(n); if (c != chi[n % 7]) bad++;
      add_term(model, n, a);
      if (c && ref) { arb_mul_ui(x, CL2, n, NPREC); arb_neg(v, x); arb_exp(v, v, NPREC);
        arb_mul_si(v, v, ref * c, NPREC); arb_div_ui(v, v, n, NPREC); arb_add(direct, direct, v, NPREC); }
      checked++;
    }
    int ok = arb_overlaps(model, direct); bad += !ok;
    printf("BLOCK_TEST lo %llu hi %llu overlaps %d model %s direct %s\n", lo, hi, ok, arb_get_str(model, 24, 0), arb_get_str(direct, 24, 0));
  }
  printf("BLOCK_TEST_TOTAL terms %ld failures %ld\n", checked, bad); return bad ? 4 : 0;
}
static void setup_stream(u64 cutoff, const char *apdir) {
  T = cutoff; SEGQ = 16777216; MODE = 2; MM = 1; APDIR = apdir;
  if ((T + 1) % SEGQ || T > 55046045695ULL) fatal("cutoff must be complete retained segments");
  a1 = 0; a2 = -22735; a3 = 0; a4 = 106272484; a6 = 0;
  b2 = 4 * (i128)a2; b4 = 2 * (i128)a4; b6 = 0;
  DISC = -(b2 * b2 * (-(i128)a4 * a4)) - 8 * b4 * b4 * b4;
  RT = 1; while ((RT + 1) * (RT + 1) <= T) RT++;
  small_primes(); NSEG = T / SEGQ + 1; APSH = calloc(NSEG, 32); load_table(RT);
  u64 *rem = malloc(8 * (RT + 1)); i64 *am = malloc(8 * (RT + 1)); gen_block(1, RT + 1, rem, am, 0);
  AMT = _arb_vec_init(RT + 1);
  for (u64 m = 1; m <= RT; m++) {
    if (rem[m - 1] != 1) fatal("small coefficient not smooth");
    arb_set_si(AMT + m, am[m - 1]); arb_div_ui(AMT + m, AMT + m, m, NPREC);
  }
  free(rem); free(am); NBLK = (T + BLK - 1) / BLK; NUNIT = NSEG + NBLK;
}
static void combine(void) {
  arb_t total, v, tail, result; arb_init(total); arb_init(v); arb_init(tail); arb_init(result);
  char hdr[65536]; unsigned char (*leaves)[32] = malloc(32 * NBLK);
  u64 smooth = 0, pairs = 0;
  for (long u = 0; u < NUNIT; u++) {
    read_unit(u, hdr, v, 1); arb_add(total, total, v, PREC);
    if (u < NSEG) { if (hdr_u64(hdr, "LSEG ") != (u64)u) fatal("bad unit order");
      hdr_hex(hdr, "apsha ", APSH[u]); pairs += hdr_u64(hdr, "pairs "); }
    else { long b = u - NSEG; if (hdr_u64(hdr, "BLK ") != (u64)b) fatal("bad block order");
      hdr_hex(hdr, "leaf ", leaves[b]); smooth += hdr_u64(hdr, "smooth "); }
  }
  if (smooth + pairs != T) fatal("count identity failed");
  printf("COUNT smooth %llu pairs %llu sum %llu T %llu identity 1\n", smooth, pairs, smooth + pairs, T);
  unsigned char dg[32]; char hx[65]; CC_SHA256(APSH, 32 * NSEG, dg); hexs(dg, hx); printf("AP_SEGROOT_SHA256 %s segments %ld\n", hx, NSEG);
  CC_SHA256(leaves, 32 * NBLK, dg); hexs(dg, hx); printf("SMOOTH_MERKLE_SHA256 %s blocks %ld\n", hx, NBLK);
  arb_mul_2exp_si(total, total, 1); tail_central(tail, T); arb_set(result, total);
  arf_t up; arf_init(up); arb_get_ubound_arf(up, tail, NPREC); arb_add_error_arf(result, up);
  printf("C %s\nPARTIAL_2S %s\nPARTIAL_DUMP %s\nTAIL_BOUND %s\nTAIL_DUMP %s\nLVALUE_BALL %s\nLVALUE_DUMP %s\n",
    arb_get_str(CL2, 30, 0), arb_get_str(total, 30, 0), arb_dump_str(total), arb_get_str(tail, 25, 0), arb_dump_str(tail), arb_get_str(result, 30, 0), arb_dump_str(result));
  print_dec_bounds("LVALUE_INTERVAL", result, 1000000);
  printf("ZERO_EXCLUDED %d\nPOSITIVE %d\n", !arb_contains_zero(result), arb_is_positive(result));
}
int main(int argc, char **argv) {
  if (fegetround() != FE_TONEAREST) fatal("rounding mode");
  if (argc < 2) fatal("kernel-test | block-test APDIR | run T APDIR W OUT [START END] | combine T APDIR W OUT");
  init_twist();
  if (!strcmp(argv[1], "kernel-test")) return kernel_test();
  if (!strcmp(argv[1], "block-test")) {
    if (argc != 3) fatal("block-test APDIR");
    setup_stream(179ULL * 16777216 - 1, argv[2]); return block_test();
  }
  if (argc < 6) fatal("run/combine T APDIR W OUT");
  setup_stream(strtoull(argv[2], 0, 10), argv[3]); W = atoi(argv[4]); OUT = argv[5];
  if (W < 1 || W > 12) fatal("workers must be 1..12");
  mkdir(OUT, 0755);
  /* Range arguments are operational, not certificate parameters. */
  char *locked[] = {argv[0], "twist-D7-central-v1", argv[2], argv[3], argv[4], argv[5]};
  params_lock(6, locked, 4);
  if (!strcmp(argv[1], "combine")) { combine(); return 0; }
  if (strcmp(argv[1], "run")) fatal("unknown command");
  USTART = argc > 6 ? atol(argv[6]) : 0; UEND = argc > 7 ? atol(argv[7]) : NUNIT;
  if (USTART < 0 || UEND > NUNIT || USTART > UEND) fatal("bad unit range");
  NEXTU = USTART; pthread_t th[12];
  for (long i = 0; i < W; i++) pthread_create(th + i, 0, twist_worker, (void *)i);
  for (long i = 0; i < W; i++) pthread_join(th[i], 0);
  printf("WORK_UNITS_DONE %ld %ld TOTAL %ld\n", USTART, UEND, NUNIT);
  if (USTART == 0 && UEND == NUNIT) combine(); return 0;
}
