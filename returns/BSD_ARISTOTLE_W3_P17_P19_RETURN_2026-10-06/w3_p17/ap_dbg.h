/* a_p for the seed curve  E : y^2 = x^3 + A2 x^2 + A4 x,  A2 = -22735, A4 = 106272484
 * (a-invariants [0,-22735,0,106272484,0], conductor 6503188012738584),
 * by Shanks-Mestre baby-step/giant-step with Montgomery arithmetic, for good primes
 * 5 <= p < 2^62.  Every returned value is certified by: (i) a unique group order in the
 * Hasse interval compatible with every tested point (points on E and on quadratic
 * twists, intersected), (ii) an explicit check N*P = O for each accepted point.
 * Small primes use naive counting (ap_naive).
 */
#ifndef SEED_AP_H
#define SEED_AP_H
#include <stdint.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <stdio.h>

typedef unsigned __int128 u128;
typedef uint64_t u64;
typedef int64_t i64;

static const i64 SEED_A2 = -22735;
static const i64 SEED_A4 = 106272484;

typedef struct { u64 p, pinv, r2, r3, one; } mont_t;

static inline u64 m_redc(const mont_t *M, u128 T) {
    u64 m = (u64)T * M->pinv;
    u128 t = (T + (u128)m * M->p) >> 64;
    u64 r = (u64)t;
    return r >= M->p ? r - M->p : r;
}
static inline u64 m_mul(const mont_t *M, u64 a, u64 b) { return m_redc(M, (u128)a * b); }
static inline u64 m_add(const mont_t *M, u64 a, u64 b) { u64 c = a + b; return c >= M->p ? c - M->p : c; }
static inline u64 m_sub(const mont_t *M, u64 a, u64 b) { return a >= b ? a - b : a + M->p - b; }
static inline u64 m_neg(const mont_t *M, u64 a) { return a ? M->p - a : 0; }

static void mont_init(mont_t *M, u64 p) {
    M->p = p;
    u64 inv = p;               /* Newton: inv = p^{-1} mod 2^64 */
    for (int i = 0; i < 6; i++) inv *= 2 - p * inv;
    M->pinv = (u64)0 - inv;
    u128 R = ((u128)1 << 64) % p;   /* R mod p */
    M->one = (u64)R;
    M->r2 = (u64)(((u128)M->one * M->one) % p);
    M->r3 = (u64)(((u128)M->r2 * M->one) % p);
}
static inline u64 m_to(const mont_t *M, u64 a) { return m_mul(M, a % M->p, M->r2); }
static inline u64 m_from(const mont_t *M, u64 a) { return m_redc(M, (u128)a); }

/* plain modular inverse of a (0 < a < p) by extended Euclid */
static inline u64 inv_plain(u64 a, u64 p) {
    i64 t = 0, nt = 1; u64 r = p, nr = a;
    while (nr) { u64 q = r / nr; i64 tt = t - (i64)q * nt; t = nt; nt = tt; u64 rr = r - q * nr; r = nr; nr = rr; }
    if (t < 0) t += (i64)p;
    return (u64)t;
}
/* inverse in Montgomery domain: (aR)^{-1} R */
static inline u64 m_inv(const mont_t *M, u64 a) { return m_mul(M, inv_plain(a, M->p), M->r3); }

/* Jacobi symbol (a/n), n odd */
static int jacobi(u64 a, u64 n) {
    int s = 1; a %= n;
    while (a) {
        int z = __builtin_ctzll(a); a >>= z;
        if ((z & 1) && ((n & 7) == 3 || (n & 7) == 5)) s = -s;
        if ((a & 3) == 3 && (n & 3) == 3) s = -s;
        u64 t = a; a = n % t; n = t;
    }
    return n == 1 ? s : 0;
}

typedef struct { u64 x, y; int inf; } pt_t;

/* curve y^2 = x^3 + a x + b in Montgomery form */
typedef struct { mont_t M; u64 a, b; } curve_t;

static inline pt_t pt_add(const curve_t *C, pt_t P, pt_t Q) {
    const mont_t *M = &C->M;
    if (P.inf) return Q;
    if (Q.inf) return P;
    u64 lam;
    if (P.x == Q.x) {
        if (P.y != Q.y || P.y == 0) { pt_t O = {0, 0, 1}; return O; }
        u64 x2 = m_mul(M, P.x, P.x);
        u64 num = m_add(M, m_add(M, m_add(M, x2, x2), x2), C->a);
        lam = m_mul(M, num, m_inv(M, m_add(M, P.y, P.y)));
    } else {
        lam = m_mul(M, m_sub(M, Q.y, P.y), m_inv(M, m_sub(M, Q.x, P.x)));
    }
    pt_t R;
    R.x = m_sub(M, m_sub(M, m_mul(M, lam, lam), P.x), Q.x);
    R.y = m_sub(M, m_mul(M, lam, m_sub(M, P.x, R.x)), P.y);
    R.inf = 0;
    return R;
}

/* Jacobian scalar multiplication k*P, P affine, returns affine */
typedef struct { u64 X, Y, Z; } jac_t;
static inline jac_t jac_dbl(const curve_t *C, jac_t P) {
    const mont_t *M = &C->M;
    if (P.Z == 0 || P.Y == 0) { jac_t O = {M->one, M->one, 0}; return O; }
    u64 XX = m_mul(M, P.X, P.X), YY = m_mul(M, P.Y, P.Y), YYYY = m_mul(M, YY, YY);
    u64 ZZ = m_mul(M, P.Z, P.Z);
    u64 S = m_mul(M, P.X, YY); S = m_add(M, S, S); S = m_add(M, S, S);           /* 4 X Y^2 */
    u64 Mm = m_add(M, m_add(M, XX, XX), XX);
    Mm = m_add(M, Mm, m_mul(M, C->a, m_mul(M, ZZ, ZZ)));
    jac_t R;
    R.X = m_sub(M, m_mul(M, Mm, Mm), m_add(M, S, S));
    u64 y8 = m_add(M, YYYY, YYYY); y8 = m_add(M, y8, y8); y8 = m_add(M, y8, y8);
    R.Y = m_sub(M, m_mul(M, Mm, m_sub(M, S, R.X)), y8);
    R.Z = m_mul(M, P.Y, P.Z); R.Z = m_add(M, R.Z, R.Z);
    return R;
}
static inline jac_t jac_madd(const curve_t *C, jac_t P, pt_t Q) {
    const mont_t *M = &C->M;
    if (Q.inf) return P;
    if (P.Z == 0) { jac_t R = {Q.x, Q.y, M->one}; return R; }
    u64 ZZ = m_mul(M, P.Z, P.Z);
    u64 U2 = m_mul(M, Q.x, ZZ), S2 = m_mul(M, Q.y, m_mul(M, ZZ, P.Z));
    u64 H = m_sub(M, U2, P.X), r = m_sub(M, S2, P.Y);
    if (H == 0) {
        if (r == 0) return jac_dbl(C, P);
        jac_t O = {M->one, M->one, 0}; return O;
    }
    u64 HH = m_mul(M, H, H), HHH = m_mul(M, HH, H), V = m_mul(M, P.X, HH);
    jac_t R;
    R.X = m_sub(M, m_sub(M, m_mul(M, r, r), HHH), m_add(M, V, V));
    R.Y = m_sub(M, m_mul(M, r, m_sub(M, V, R.X)), m_mul(M, P.Y, HHH));
    R.Z = m_mul(M, P.Z, H);
    return R;
}
static pt_t pt_mul(const curve_t *C, pt_t P, u64 k) {
    const mont_t *M = &C->M;
    jac_t R = {M->one, M->one, 0};
    if (P.inf || k == 0) { pt_t O = {0, 0, 1}; return O; }
    int top = 63 - __builtin_clzll(k);
    for (int i = top; i >= 0; i--) {
        R = jac_dbl(C, R);
        if ((k >> i) & 1) R = jac_madd(C, R, P);
    }
    pt_t out;
    if (R.Z == 0) { out.x = out.y = 0; out.inf = 1; return out; }
    u64 zi = m_inv(M, R.Z), zi2 = m_mul(M, zi, zi);
    out.x = m_mul(M, R.X, zi2); out.y = m_mul(M, R.Y, m_mul(M, zi2, zi)); out.inf = 0;
    return out;
}

/* batch: out[i] = P[i] + Q[i], with all special cases handled */
static void batch_add(const curve_t *C, const pt_t *P, const pt_t *Q, pt_t *out, int n, u64 *scratch) {
    const mont_t *M = &C->M;
    u64 *d = scratch, *pre = scratch + n;
    u64 acc = M->one;
    for (int i = 0; i < n; i++) {
        u64 di = M->one;
        if (!P[i].inf && !Q[i].inf && P[i].x != Q[i].x) di = m_sub(M, Q[i].x, P[i].x);
        d[i] = di; pre[i] = acc; acc = m_mul(M, acc, di);
    }
    u64 inv = m_inv(M, acc);
    for (int i = n - 1; i >= 0; i--) {
        u64 di_inv = m_mul(M, inv, pre[i]);
        inv = m_mul(M, inv, d[i]);
        if (P[i].inf || Q[i].inf || P[i].x == Q[i].x) { out[i] = pt_add(C, P[i], Q[i]); continue; }
        u64 lam = m_mul(M, m_sub(M, Q[i].y, P[i].y), di_inv);
        u64 x3 = m_sub(M, m_sub(M, m_mul(M, lam, lam), P[i].x), Q[i].x);
        out[i].y = m_sub(M, m_mul(M, lam, m_sub(M, P[i].x, x3)), P[i].y);
        out[i].x = x3; out[i].inf = 0;
    }
}

static inline u64 isqrt64(u64 n) {
    u64 r = (u64)sqrt((double)n);
    while (r * r > n) r--;
    while ((r + 1) * (r + 1) <= n) r++;
    return r;
}

#define BS_MAX 8192
typedef struct {
    pt_t *baby, *tmpP, *tmpQ, *tmpO, *gian;
    u64 *scratch;
    u64 *hkey; int32_t *hval; int hmask;
} bsgs_ws;

static void ws_init(bsgs_ws *W) {
    W->baby = malloc(sizeof(pt_t) * (BS_MAX + 2));
    W->tmpP = malloc(sizeof(pt_t) * (BS_MAX + 2));
    W->tmpQ = malloc(sizeof(pt_t) * (BS_MAX + 2));
    W->tmpO = malloc(sizeof(pt_t) * (BS_MAX + 2));
    W->gian = malloc(sizeof(pt_t) * (BS_MAX + 2));
    W->scratch = malloc(sizeof(u64) * 2 * (BS_MAX + 2));
    W->hmask = 4096 - 1;
    W->hkey = malloc(sizeof(u64) * 4096);
    W->hval = malloc(sizeof(int32_t) * 4096);
}

/* All N in [Nb, Nb + L*Mstep] with N == Nb mod Mstep and N*P = O.  Returns count
 * (written into outN, at most maxout), or -1 if the point has tiny order (retry). */
static long g_calls=0; static int bsgs_orders(const curve_t *C, pt_t P, u64 Nb, u64 L, u64 Mstep, u64 *outN, int maxout, bsgs_ws *W) {
    g_calls++; pt_t R = pt_mul(C, P, Mstep);
    if (R.inf) return -1;
    u64 s = (u64)sqrt((double)L / 2.0) + 1;
    if (s > 1800) s = 1800;
    /* baby B[1..s] by doubling tree: B[k+1..2k] = B[k] + B[1..k] */
    pt_t *B = W->baby;
    B[1] = R;
    u64 have = 1;
    while (have < s) {
        u64 n = have; if (have + n > s) n = s - have;
        for (u64 i = 0; i < n; i++) { W->tmpP[i] = B[have]; W->tmpQ[i] = B[i + 1]; }
        batch_add(C, W->tmpP, W->tmpQ, B + have + 1, (int)n, W->scratch);
        have += n;
    }
    /* hash */
    for (int i = 0; i <= W->hmask; i++) W->hval[i] = -1;
    for (u64 i = 1; i <= s; i++) {
        if (B[i].inf) return -1;            /* ord(R) <= s: tiny order */
        u64 h = (B[i].x * 0x9E3779B97F4A7C15ULL) >> 52; h &= (u64)W->hmask;
        while (W->hval[h] >= 0) {
            if (W->hkey[h] == B[i].x) return -1;  /* B_i = +-B_j: tiny order */
            h = (h + 1) & (u64)W->hmask;
        }
        W->hkey[h] = B[i].x; W->hval[h] = (int32_t)i;
    }
    u64 step = 2 * s + 1;
    /* H = (2s+1) R = B[s] + B[s] + R */
    pt_t H = pt_add(C, pt_add(C, B[s], B[s]), R);
    if (H.inf) return -1;
    /* j = s + u, N = Nb + j*Mstep, Qc = (Nb + s*Mstep) P ; Qc + u R = O */
    pt_t Qc = pt_mul(C, P, Nb + s * Mstep);
    i64 G = (i64)(L / step) + 1;
    int cnt = 0;
    int c = 64; if (c > G + 1) c = (int)G + 1;
    pt_t *Hm = W->gian;     /* Hm[1..c] = H, 2H, ..., cH */
    Hm[1] = H; int hv = 1;
    while (hv < c) {
        int n = hv; if (hv + n > c) n = c - hv;
        for (int i = 0; i < n; i++) { W->tmpP[i] = Hm[hv]; W->tmpQ[i] = Hm[i + 1]; }
        batch_add(C, W->tmpP, W->tmpQ, Hm + hv + 1, n, W->scratch);
        hv += n;
    }
    pt_t Y = Qc;
    i64 g0 = 0;
    while (g0 <= G) {
        W->tmpO[0] = Y;
        for (int j = 1; j <= c; j++) { W->tmpP[j - 1] = Y; W->tmpQ[j - 1] = Hm[j]; }
        batch_add(C, W->tmpP, W->tmpQ, W->tmpO + 1, c, W->scratch);
        for (int j = 0; j < c; j++) {
            i64 g = g0 + j; if (g > G) break;
            pt_t Z = W->tmpO[j];
            i64 u;
            if (Z.inf) {
                u = g * (i64)step;
                i64 jj = (i64)s + u;
                if (jj >= 0 && jj <= (i64)L && cnt < maxout) outN[cnt++] = Nb + (u64)jj * Mstep;
                continue;
            }
            u64 h = (Z.x * 0x9E3779B97F4A7C15ULL) >> 52; h &= (u64)W->hmask;
            while (W->hval[h] >= 0) {
                if (W->hkey[h] == Z.x) {
                    i64 i = W->hval[h];
                    u = (Z.y == B[i].y) ? g * (i64)step - i : g * (i64)step + i;
                    i64 jj = (i64)s + u;
                    if (jj >= 0 && jj <= (i64)L && cnt < maxout) outN[cnt++] = Nb + (u64)jj * Mstep;
                    break;
                }
                h = (h + 1) & (u64)W->hmask;
            }
        }
        Y = W->tmpO[c];
        g0 += c;
    }
    return cnt;
}

/* a_p by BSGS; returns a_p, sets *ok = 0 on failure */
static i64 ap_bsgs(u64 p, bsgs_ws *W, int *ok) {
    curve_t C0;
    mont_t *M = &C0.M;
    mont_init(M, p);
    *ok = 1;
    /* short Weierstrass: x = X - A2/3 : a = A4 - A2^2/3, b = 2 A2^3/27 - A2 A4/3 */
    i64 A2 = SEED_A2 % (i64)p; if (A2 < 0) A2 += p;
    u64 a2 = m_to(M, (u64)A2), a4 = m_to(M, (u64)SEED_A4 % p);
    u64 inv3 = m_inv(M, m_to(M, 3)), inv27 = m_inv(M, m_to(M, 27));
    u64 a2sq = m_mul(M, a2, a2);
    u64 ca = m_sub(M, a4, m_mul(M, a2sq, inv3));
    u64 two = m_to(M, 2);
    u64 cb = m_sub(M, m_mul(M, m_mul(M, two, m_mul(M, a2sq, a2)), inv27), m_mul(M, m_mul(M, a2, a4), inv3));
    /* 2-torsion: full iff A2^2 - 4 A4 is a square */
    i64 disc = (i64)((SEED_A2 * SEED_A2 - 4 * SEED_A4) % (i64)p); if (disc < 0) disc += p;
    u64 Mstep = (jacobi((u64)disc, p) == 1) ? 4 : 2;
    u64 sq = isqrt64(4 * p);           /* floor(2 sqrt p) */
    u64 Nlo = p + 1 - sq, Nhi = p + 1 + sq;
    u64 Nb = (Nlo + Mstep - 1) / Mstep * Mstep;
    u64 L = (Nhi - Nb) / Mstep;
    /* candidate traces for E, as a bitmap over offsets of t in [-sq, sq] */
    int ncand = -1; i64 cand[64]; int nc = 0;
    u64 x0 = 1;
    for (int attempt = 0; attempt < 60; attempt++, x0++) {
        u64 X0 = m_to(M, x0);
        u64 d = m_add(M, m_mul(M, m_add(M, m_mul(M, X0, X0), ca), X0), cb);   /* X0^3 + a X0 + b */
        if (d == 0) continue;
        int chi = jacobi(m_from(M, d), p);
        curve_t Cd; Cd.M = *M;
        u64 d2 = m_mul(M, d, d);
        Cd.a = m_mul(M, ca, d2); Cd.b = m_mul(M, cb, m_mul(M, d2, d));
        pt_t P = {m_mul(M, X0, d), d2, 0};
        u64 outN[64];
        int k = bsgs_orders(&Cd, P, Nb, L, Mstep, outN, 64, W);
        if (k < 0) continue;
        if (k == 0) { *ok = 0; return 0; }  /* impossible if code correct */
        /* verify each candidate explicitly */
        i64 tl[64]; int tn = 0;
        for (int i = 0; i < k; i++) {
            pt_t Z = pt_mul(&Cd, P, outN[i]);
            if (!Z.inf) { *ok = 0; return 0; }
            i64 t = (i64)(p + 1) - (i64)outN[i];
            t *= chi;
            int dup = 0; for (int j = 0; j < tn; j++) if (tl[j] == t) dup = 1;
            if (!dup) tl[tn++] = t;
        }
        if (ncand < 0) { nc = 0; for (int i = 0; i < tn; i++) cand[nc++] = tl[i]; ncand = 1; }
        else {
            int nn = 0;
            for (int i = 0; i < nc; i++) { int f = 0; for (int j = 0; j < tn; j++) if (cand[i] == tl[j]) f = 1; if (f) cand[nn++] = cand[i]; }
            nc = nn;
        }
        if (nc == 1) return cand[0];
        if (nc == 0) { *ok = 0; return 0; }
    }
    *ok = 0; return 0;
}

/* naive a_p (p odd prime, small), affine count with Legendre via table */
static i64 ap_naive(u64 p) {
    if (p == 2) return 0;
    signed char *chi = malloc(p);
    memset(chi, -1, p); chi[0] = 0;
    for (u64 y = 1; y < p; y++) chi[(y * y) % p] = 1;
    i64 A2 = SEED_A2 % (i64)p; if (A2 < 0) A2 += p;
    u64 A4 = (u64)SEED_A4 % p;
    i64 s = 0;
    for (u64 x = 0; x < p; x++) {
        u64 r = ((x * x % p) * x + (u64)A2 * (x * x % p) + A4 * x) % p;
        s += chi[r];
    }
    free(chi);
    return -s;
}
#endif
