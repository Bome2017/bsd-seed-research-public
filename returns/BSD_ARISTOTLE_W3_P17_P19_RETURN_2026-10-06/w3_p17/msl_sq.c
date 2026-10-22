/* msl_sq: bucket sums for plus modular symbols of the seed at arbitrary moduli m with
 * gcd(m, N) = 1 (in particular m = p^2), one pass over the coefficient range.
 *
 *   S_b(m) = sum_{n <= T_m, n == b mod m} a_n / n * exp(-2 pi n / (m sqrt N)),
 *   [a/m]^+ = (1/Omega^+) sum_b S_b ( cos(2 pi a b/m) + cos(2 pi a' b/m) ),  a' = (N a)^{-1} mod m
 * (root number +1).  The formula is validated against exact Manin-relation symbols in
 * validate_formula.py.
 *
 * Decomposition of n <= T (P0 = isqrt(Tmax)):
 *   (C) n P0-smooth: depth-first enumeration with multiplicative a_n,
 *   (D) n = k q, q > P0 prime (unique, exponent 1), k <= T/q < P0: a_n = a_k a_q.
 * a_q for q > P0 by certified BSGS (ap.h).  Bad primes: 2, 4547 additive (a = 0),
 * 3, 2243, 5843 multiplicative (a_{p^k} = a_p^k, a_p by counting).
 *
 * usage: msl_sq <Tfactor> <nthreads> <outprefix> m1 [m2 ...]
 * Resumable: completed large-prime segments are appended to <outprefix>.seg
 */
#include "ap.h"
#include <pthread.h>
#include <stdatomic.h>
#include <time.h>
#include <unistd.h>

#define MAXMOD 4
static const u64 NCOND = 6503188012738584ULL;
static int nmod; static u64 mods[MAXMOD]; static u64 Tm[MAXMOD]; static double invX2pi[MAXMOD];
static u64 Tmax, P0;
static u64 *primes; static long nprimes;     /* primes <= P0 */
static i64 *apsmall;                        /* a_p for primes[i] */
static i64 *ak; static double *akk;         /* a_k, a_k/k for k <= P0 */
static int nthreads;

/* kernel: exp(-x) (plus symbols, default) or E_1(x) (derivative of a twisted L-function, -DKERNEL_E1) */
static inline double e1(double x) {
    if (x <= 1.0) {
        double sum = 0, term = 1;
        for (int k = 1; k < 40; k++) { term *= -x / k; double t = -term / k; sum += t; if (fabs(t) < 1e-18 * fabs(sum)) break; }
        return -0.57721566490153286060651209 - log(x) + sum;
    }
    /* modified Lentz continued fraction */
    double b = x + 1.0, c = 1e300, d = 1.0 / b, h = d;
    for (int i = 1; i < 200; i++) {
        double an = -(double)i * i; b += 2.0;
        d = 1.0 / (an * d + b); c = b + an / c; double del = c * d; h *= del;
        if (fabs(del - 1.0) < 1e-16) break;
    }
    return h * exp(-x);
}
#ifdef KERNEL_E1
#define KERNEL(x) e1(x)
#else
#define KERNEL(x) exp(-(x))
#endif
static int is_bad(u64 p) { return p == 2 || p == 3 || p == 2243 || p == 4547 || p == 5843; }

/* ---------------- phase C: smooth numbers ---------------- */
typedef struct { long double S[MAXMOD][400]; } acc_t;

static void add_node(acc_t *A, u64 n, i64 an) {
    if (!an) return;
    for (int t = 0; t < nmod; t++) {
        if (n > Tm[t]) continue;
        double w = (double)an / (double)n * KERNEL((double)n * invX2pi[t]);
        A->S[t][n % mods[t]] += w;
    }
}
/* subtree: all n = base * (products of prime powers with prime index > i) */
static void dfs(acc_t *A, u64 n, i64 an, long i) {
    for (long j = i + 1; j < nprimes; j++) {
        u64 p = primes[j];
        if (n > Tmax / p) break;
        if (p == 2 || p == 4547) continue;
        u64 q = n * p;
        i64 apk_prev = 1, apk = apsmall[j];
        int bad = is_bad(p);
        while (1) {
            i64 v = an * apk;
            add_node(A, q, v);
            dfs(A, q, v, j);
            if (q > Tmax / p) break;
            q *= p;
            i64 nx = bad ? apk * apsmall[j] : apsmall[j] * apk - (i64)p * apk_prev;
            apk_prev = apk; apk = nx;
        }
    }
}
typedef struct { long i; int e; long j; } task_t;
static task_t *tasks; static long ntasks; static atomic_long next_task;

static void *smooth_worker(void *arg) {
    acc_t *A = (acc_t *)arg;
    while (1) {
        long t = atomic_fetch_add(&next_task, 1);
        if (t >= ntasks) break;
        task_t tk = tasks[t];
        u64 p = primes[tk.i];
        /* a_{p^e} */
        i64 a0 = 1, a1 = apsmall[tk.i]; u64 n = p;
        for (int e = 1; e < tk.e; e++) {
            i64 nx = is_bad(p) ? a1 * apsmall[tk.i] : apsmall[tk.i] * a1 - (i64)p * a0;
            a0 = a1; a1 = nx; n *= p;
        }
        if (tk.j == -1) { add_node(A, n, a1); continue; }
        if (tk.j == -2) {            /* whole subtree with smallest prime p, all exponents */
            u64 q = p; i64 c0 = 1, c1 = apsmall[tk.i];
            while (1) {
                add_node(A, q, c1);
                dfs(A, q, c1, tk.i);
                if (q > Tmax / p) break;
                q *= p;
                i64 nx = is_bad(p) ? c1 * apsmall[tk.i] : apsmall[tk.i] * c1 - (i64)p * c0;
                c0 = c1; c1 = nx;
            }
            continue;
        }
        /* subtree n * pj^f * (primes > j) */
        u64 pj = primes[tk.j];
        u64 q = n * pj; i64 b0 = 1, b1 = apsmall[tk.j];
        while (1) {
            i64 v = a1 * b1;
            add_node(A, q, v);
            dfs(A, q, v, tk.j);
            if (q > Tmax / pj) break;
            q *= pj;
            i64 nx = is_bad(pj) ? b1 * apsmall[tk.j] : apsmall[tk.j] * b1 - (i64)pj * b0;
            b0 = b1; b1 = nx;
        }
    }
    return NULL;
}

/* ---------------- phase D: large primes ---------------- */
#define SEGLEN (1ULL << 23)
static u64 seg_lo0; static long nseg; static atomic_long next_seg;
static char *segdone;
static pthread_mutex_t io_mtx = PTHREAD_MUTEX_INITIALIZER;
static FILE *segf;
static atomic_long segs_finished; static atomic_long fails;

typedef struct { long seg; u64 nprimes; u64 apsum; i64 apsum_signed; long double S[MAXMOD][400]; } segrec_t;

static void *large_worker(void *arg) {
    (void)arg;
    bsgs_ws W; ws_init(&W);
    unsigned char *sieve = malloc(SEGLEN);
    double (*Sd)[400] = malloc(sizeof(double) * MAXMOD * 300);
    segrec_t *rec = malloc(sizeof(segrec_t));
    while (1) {
        long sidx = atomic_fetch_add(&next_seg, 1);
        if (sidx >= nseg) break;
        if (segdone[sidx]) continue;
        u64 lo = seg_lo0 + (u64)sidx * SEGLEN, hi = lo + SEGLEN;   /* [lo, hi) */
        if (hi > Tmax + 1) hi = Tmax + 1;
        memset(sieve, 0, SEGLEN);
        for (long i = 0; i < nprimes; i++) {
            u64 p = primes[i];
            if (p * p >= hi) break;
            u64 st = (lo + p - 1) / p * p; if (st < p * p) st = p * p;
            for (u64 x = st; x < hi; x += p) sieve[x - lo] = 1;
        }
        memset(rec, 0, sizeof(segrec_t));
        rec->seg = sidx;
        for (int t = 0; t < nmod; t++) for (int b = 0; b < 400; b++) Sd[t][b] = 0;
        int flushc = 0;
        for (u64 x = lo; x < hi; x++) {
            if (sieve[x - lo] || x <= P0 || (x & 1) == 0) continue;
            u64 q = x;
            int ok = 1; i64 aq = is_bad(q) ? ap_naive(q) : ap_bsgs(q, &W, &ok);
            if (!ok) { atomic_fetch_add(&fails, 1); fprintf(stderr, "AP_FAIL %lu\n", q); continue; }
            rec->nprimes++; rec->apsum += (u64)aq * (q % 1000003); rec->apsum_signed += aq;
            if (!aq) continue;
            double v = (double)aq / (double)q;
            for (int t = 0; t < nmod; t++) {
                if (q > Tm[t]) continue;
                u64 m = mods[t], qm = q % m, idx = qm;
                u64 K = Tm[t] / q;
                double *S = Sd[t];
#ifdef KERNEL_E1
                double xq = (double)q * invX2pi[t];
                for (u64 k = 1; k <= K; k++) {
                    double c = akk[k];
                    if (c != 0.0) S[idx] += v * c * e1(xq * (double)k);
                    idx += qm; if (idx >= m) idx -= m;
                }
#else
                double r = exp(-(double)q * invX2pi[t]), w = r;
                for (u64 k = 1; k <= K; k++) {
                    double c = akk[k];
                    if (c != 0.0) S[idx] += v * c * w;
                    w *= r;
                    idx += qm; if (idx >= m) idx -= m;
                }
#endif
            }
            if (++flushc == 256) {
                flushc = 0;
                for (int t = 0; t < nmod; t++) for (u64 b = 0; b < mods[t]; b++) { rec->S[t][b] += Sd[t][b]; Sd[t][b] = 0; }
            }
        }
        for (int t = 0; t < nmod; t++) for (u64 b = 0; b < mods[t]; b++) { rec->S[t][b] += Sd[t][b]; Sd[t][b] = 0; }
        pthread_mutex_lock(&io_mtx);
        fwrite(rec, sizeof(segrec_t), 1, segf); fflush(segf);
        pthread_mutex_unlock(&io_mtx);
        atomic_fetch_add(&segs_finished, 1);
    }
    return NULL;
}

static double now(void) { struct timespec t; clock_gettime(CLOCK_MONOTONIC, &t); return t.tv_sec + t.tv_nsec * 1e-9; }

int main(int argc, char **argv) {
    if (argc < 5) { fprintf(stderr, "usage: %s Tfactor nthreads outprefix m1 [m2..]\n", argv[0]); return 1; }
    double Tf = atof(argv[1]); nthreads = atoi(argv[2]); const char *pre = argv[3];
    nmod = argc - 4; if (nmod > MAXMOD) return 1;
    long double sqrtN = sqrtl((long double)NCOND);
    Tmax = 0;
    for (int t = 0; t < nmod; t++) {
        mods[t] = strtoull(argv[4 + t], 0, 10);
        if (mods[t] > 400) { fprintf(stderr, "m too large\n"); return 1; }
        long double X = (long double)mods[t] * sqrtN;
        if (getenv("MSL_XSCALE")) X *= (long double)atof(getenv("MSL_XSCALE"));   /* functional-equation test */
        Tm[t] = (u64)(Tf * X);
        invX2pi[t] = (double)(2.0L * 3.14159265358979323846264338327950288L / X);
        if (Tm[t] > Tmax) Tmax = Tm[t];
    }
    P0 = isqrt64(Tmax);
    double t0 = now();
    /* primes <= P0 */
    char *c = calloc(P0 + 1, 1);
    primes = malloc(sizeof(u64) * (P0 / 2 + 10)); nprimes = 0;
    for (u64 i = 2; i <= P0; i++) { if (c[i]) continue; primes[nprimes++] = i; for (u64 j = i * i; j <= P0; j += i) c[j] = 1; }
    apsmall = malloc(sizeof(i64) * nprimes);
    { bsgs_ws W; ws_init(&W);
      for (long i = 0; i < nprimes; i++) {
        u64 p = primes[i];
        if (p == 2 || p == 4547) { apsmall[i] = 0; continue; }
        if (p < 2000 || is_bad(p)) { apsmall[i] = ap_naive(p); continue; }
        int ok; apsmall[i] = ap_bsgs(p, &W, &ok);
        if (!ok) { fprintf(stderr, "small ap fail %lu\n", p); return 2; }
      } }
    /* a_k for k <= P0 */
    ak = calloc(P0 + 1, sizeof(i64)); akk = calloc(P0 + 2, sizeof(double));
    { u64 *spf = calloc(P0 + 1, sizeof(u64)); long *pidx = calloc(P0 + 1, sizeof(long));
      for (long i = 0; i < nprimes; i++) { pidx[primes[i]] = i; for (u64 j = primes[i]; j <= P0; j += primes[i]) if (!spf[j]) spf[j] = primes[i]; }
      ak[1] = 1;
      for (u64 k = 2; k <= P0; k++) {
        u64 p = spf[k], r = k; int e = 0; while (r % p == 0) { r /= p; e++; }
        i64 a0 = 1, a1 = apsmall[pidx[p]];
        for (int j = 1; j < e; j++) { i64 nx = is_bad(p) ? a1 * apsmall[pidx[p]] : apsmall[pidx[p]] * a1 - (i64)p * a0; a0 = a1; a1 = nx; }
        ak[k] = ak[r] * a1;
      }
      for (u64 k = 1; k <= P0; k++) akk[k] = (double)ak[k] / (double)k;
      free(spf); free(pidx); }
    fprintf(stderr, "Tmax=%lu P0=%lu nprimes(P0)=%ld setup %.1fs\n", Tmax, P0, nprimes, now() - t0);

    /* ---- phase C ---- */
    char fn[1024]; snprintf(fn, sizeof fn, "%s.smooth", pre);
    acc_t *Ctot = calloc(1, sizeof(acc_t));
    FILE *fs = fopen(fn, "rb");
    if (fs && fread(Ctot, sizeof(acc_t), 1, fs) == 1) { fprintf(stderr, "smooth part loaded from %s\n", fn); fclose(fs); }
    else {
        if (fs) fclose(fs);
        tasks = malloc(sizeof(task_t) * 8000000); ntasks = 0;
        for (long i = 0; i < nprimes; i++) {
            u64 p = primes[i]; if (p == 2 || p == 4547) continue;
            u64 n = p; int e = 1;
            while (1) {
                if (p < 400) {
                    tasks[ntasks++] = (task_t){i, e, -1};
                    for (long j = i + 1; j < nprimes && n <= Tmax / primes[j]; j++) {
                        if (primes[j] == 2 || primes[j] == 4547) continue;
                        tasks[ntasks++] = (task_t){i, e, j};
                    }
                } else { tasks[ntasks++] = (task_t){i, e, -2}; break; }
                if (n > Tmax / p) break;
                n *= p; e++;
            }
        }
        /* -2 tasks enumerate all exponents themselves */
        fprintf(stderr, "smooth tasks %ld\n", ntasks);
        pthread_t th[64]; acc_t *As[64];
        for (int t = 0; t < nthreads; t++) { As[t] = calloc(1, sizeof(acc_t)); pthread_create(&th[t], 0, smooth_worker, As[t]); }
        for (int t = 0; t < nthreads; t++) { pthread_join(th[t], 0); for (int u = 0; u < nmod; u++) for (int b = 0; b < 400; b++) Ctot->S[u][b] += As[t]->S[u][b]; }
        /* n = 1 */
        for (int u = 0; u < nmod; u++) Ctot->S[u][1 % mods[u]] += (long double)KERNEL(invX2pi[u]);
        fs = fopen(fn, "wb"); fwrite(Ctot, sizeof(acc_t), 1, fs); fclose(fs);
        fprintf(stderr, "smooth phase done %.1fs\n", now() - t0);
    }
    /* ---- phase D ---- */
    seg_lo0 = 0; nseg = (long)(Tmax / SEGLEN) + 1;
    segdone = calloc(nseg, 1);
    snprintf(fn, sizeof fn, "%s.seg", pre);
    long double (*Dtot)[400] = calloc(MAXMOD * 300, sizeof(long double));
    u64 totprimes = 0, apsum = 0; i64 apsum_s = 0; long nloaded = 0;
    { FILE *f = fopen(fn, "rb"); segrec_t r;
      if (f) { while (fread(&r, sizeof r, 1, f) == 1) { if (r.seg < nseg && !segdone[r.seg]) { segdone[r.seg] = 1; nloaded++; } } fclose(f); } }
    fprintf(stderr, "segments %ld, already done %ld\n", nseg, nloaded);
    segf = fopen(fn, "ab");
    pthread_t th[64];
    for (int t = 0; t < nthreads; t++) pthread_create(&th[t], 0, large_worker, NULL);
    double tl = now(); long tick = 0;
    while (atomic_load(&segs_finished) + nloaded < nseg) {
        sleep(1);
        if (++tick % 120) continue;
        long d = atomic_load(&segs_finished);
        double el = now() - tl;
        fprintf(stderr, "progress %ld/%ld segments, %.0fs, eta %.0fs, fails %ld\n", d + nloaded, nseg, el,
                d ? el / d * (nseg - nloaded - d) : -1.0, atomic_load(&fails));
    }
    for (int t = 0; t < nthreads; t++) pthread_join(th[t], 0);
    fclose(segf);
    /* re-read every segment record (dedupe) and total */
    memset(segdone, 0, nseg);
    { FILE *f = fopen(fn, "rb"); segrec_t r; long ns = 0;
      while (fread(&r, sizeof r, 1, f) == 1) {
        if (r.seg >= nseg || segdone[r.seg]) continue;
        segdone[r.seg] = 1; ns++;
        totprimes += r.nprimes; apsum += r.apsum; apsum_s += r.apsum_signed;
        for (int u = 0; u < nmod; u++) for (u64 b = 0; b < mods[u]; b++) Dtot[u][b] += r.S[u][b];
      }
      fclose(f);
      if (ns != nseg) { fprintf(stderr, "missing segments %ld/%ld\n", ns, nseg); return 3; } }
    snprintf(fn, sizeof fn, "%s.out", pre);
    FILE *fo = fopen(fn, "w");
    fprintf(fo, "N %lu\nTfactor %.6f\nP0 %lu\nlarge_primes %lu\nap_checksum %lu\nap_sum %ld\nfails %ld\n", NCOND, Tf, P0, totprimes, apsum, apsum_s, atomic_load(&fails));
    for (int u = 0; u < nmod; u++) {
        fprintf(fo, "MOD %lu T %lu\n", mods[u], Tm[u]);
        for (u64 b = 0; b < mods[u]; b++) fprintf(fo, "S %lu %lu %.24Le\n", mods[u], b, Ctot->S[u][b] + Dtot[u][b]);
    }
    fclose(fo);
    fprintf(stderr, "done %.1fs, large primes %lu, fails %ld\n", now() - t0, totprimes, atomic_load(&fails));
    return atomic_load(&fails) ? 4 : 0;
}
