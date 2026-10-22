/* fastap.c — rigorous fast trace of Frobenius for y^2 = x^3 + a4 x + a6 over F_p, p < 2^62, for curves with a rational
 * 2-torsion point (the seed). Returns LONG_MIN when it cannot certify (caller then uses PARI's Fl_elltrace).
 *
 * Method (Shanks-Mestre baby-step giant-step), every step exact:
 *  - #E = A mod B from 2-torsion: the cubic has >= 1 root (rational 2-torsion, asserted per prime via the known root X0), so
 *    Legendre(disc) = 1 => 3 roots => 4 | #E; else exactly 1 root => 2 | #E.
 *  - Twist trick (no square roots): pick x0, d = f(x0) != 0; P = (d x0, d^2) lies on E_d: y^2 = x^3 + a4 d^2 x + a6 d^3,
 *    E_d = E if (d/p) = 1, else the quadratic twist; #E_d has the same 2-torsion congruence.
 *  - Candidates h = h0 + B k (k = 0..K-1) cover the Hasse interval |p+1-h| <= floor(2 sqrt p). Find ALL k with (h0 + B k) P = O
 *    by a full BSGS scan (baby steps j*S, S = B*P, j = 1..m; giant steps Q0 + i*m*S); exact x-matches, sign by y.
 *  - Accept only if exactly one k is found and verified by a direct scalar multiplication; otherwise return LONG_MIN.
 *    (Two solutions would differ by a multiple of ord(S); a unique solution in the full interval means #E_d is determined.)
 * Arithmetic: 64-bit Montgomery (R = 2^64), Jacobian coordinates, batched inversion (Montgomery's trick).
 */
#include <pari/pari.h>
#include <stdint.h>
#include <limits.h>
#include <string.h>
#include <math.h>

typedef unsigned __int128 u128;
static uint64_t MP, MPINV, MR2, MONE;           /* modulus, -p^{-1} mod 2^64, R^2 mod p, R mod p (Montgomery 1) */

static inline uint64_t mmul(uint64_t a, uint64_t b) {
  u128 t = (u128)a * b; uint64_t m = (uint64_t)t * MPINV; u128 u = (t + (u128)m * MP) >> 64;
  uint64_t r = (uint64_t)u; return r >= MP ? r - MP : r;
}
static inline uint64_t madd(uint64_t a, uint64_t b) { uint64_t r = a + b; return r >= MP ? r - MP : r; }
static inline uint64_t msub(uint64_t a, uint64_t b) { return a >= b ? a - b : a + MP - b; }
static inline uint64_t tom(uint64_t a) { return mmul(a % MP, MR2); }
static inline uint64_t fromm(uint64_t a) { return mmul(a, 1); }
static uint64_t mpow(uint64_t a, uint64_t e) { uint64_t r = MONE; while (e) { if (e & 1) r = mmul(r, a); a = mmul(a, a); e >>= 1; } return r; }
static inline uint64_t minv(uint64_t a) { return mpow(a, MP - 2); }
static void msetup(uint64_t p) {
  MP = p; uint64_t inv = p; for (int i = 0; i < 6; i++) inv *= 2 - p * inv;   /* p^{-1} mod 2^64 (Newton) */
  MPINV = (uint64_t)(-inv); u128 R = ((u128)1 << 64) % p; MONE = (uint64_t)R; MR2 = (uint64_t)(((u128)MONE * MONE) % p);
}
static int legendre_m(uint64_t am) { uint64_t r = mpow(am, (MP - 1) / 2); if (r == MONE) return 1; if (r == 0) return 0; return -1; }

typedef struct { uint64_t X, Y, Z; } jpt;          /* Jacobian; Z == 0 is infinity */
static uint64_t A4;                                 /* curve coefficient a4 (Montgomery) of the curve in use */

static void jdbl(jpt *r, const jpt *p) {
  if (p->Z == 0 || p->Y == 0) { r->Z = 0; r->X = MONE; r->Y = MONE; return; }
  uint64_t XX = mmul(p->X, p->X), YY = mmul(p->Y, p->Y), YYYY = mmul(YY, YY), ZZ = mmul(p->Z, p->Z);
  uint64_t t = madd(p->X, YY); uint64_t S = msub(msub(mmul(t, t), XX), YYYY); S = madd(S, S);
  uint64_t M = madd(madd(XX, XX), XX); M = madd(M, mmul(A4, mmul(ZZ, ZZ)));
  uint64_t T = msub(mmul(M, M), madd(S, S));
  uint64_t Y8 = madd(YYYY, YYYY); Y8 = madd(Y8, Y8); Y8 = madd(Y8, Y8);
  uint64_t Z3 = madd(p->Y, p->Z); Z3 = msub(msub(mmul(Z3, Z3), YY), ZZ);
  r->X = T; r->Y = msub(mmul(M, msub(S, T)), Y8); r->Z = Z3;
}
/* r = p + (x2, y2) affine (Montgomery); handles doubling and infinity */
static void jaddm(jpt *r, const jpt *p, uint64_t x2, uint64_t y2) {
  if (p->Z == 0) { r->X = x2; r->Y = y2; r->Z = MONE; return; }
  uint64_t Z1Z1 = mmul(p->Z, p->Z), U2 = mmul(x2, Z1Z1), S2 = mmul(y2, mmul(p->Z, Z1Z1));
  uint64_t H = msub(U2, p->X), rr = msub(S2, p->Y);
  if (H == 0) { if (rr == 0) { jdbl(r, p); return; } r->Z = 0; r->X = MONE; r->Y = MONE; return; }
  uint64_t HH = mmul(H, H), I = madd(HH, HH); I = madd(I, I); uint64_t J = mmul(H, I); rr = madd(rr, rr);
  uint64_t V = mmul(p->X, I);
  uint64_t X3 = msub(msub(mmul(rr, rr), J), madd(V, V));
  uint64_t Y1J = mmul(p->Y, J);
  uint64_t Y3 = msub(mmul(rr, msub(V, X3)), madd(Y1J, Y1J));
  uint64_t Z3 = madd(p->Z, H); Z3 = msub(msub(mmul(Z3, Z3), Z1Z1), HH);
  r->X = X3; r->Y = Y3; r->Z = Z3;
}
static void jmul(jpt *r, uint64_t x, uint64_t y, uint64_t n) {   /* r = n (x,y) */
  jpt acc = {MONE, MONE, 0}; if (n == 0) { *r = acc; return; }
  int b = 63; while (!((n >> b) & 1)) b--;
  for (; b >= 0; b--) { jpt t; jdbl(&t, &acc); acc = t; if ((n >> b) & 1) { jaddm(&t, &acc, x, y); acc = t; } }
  *r = acc;
}
static int toaff(const jpt *p, uint64_t *x, uint64_t *y) {       /* returns 0 if infinity */
  if (p->Z == 0) return 0; uint64_t zi = minv(p->Z), zi2 = mmul(zi, zi); *x = mmul(p->X, zi2); *y = mmul(p->Y, mmul(zi2, zi)); return 1;
}

#define MAXM 16384
#define HBITS 15
static uint64_t bx[MAXM + 1], by[MAXM + 1]; static long hkey[1 << HBITS];
static jpt tmpj[MAXM + 1]; static uint64_t pre[MAXM + 1];

static void batch_aff(jpt *v, long n, uint64_t *xs, uint64_t *ys) {    /* all Z != 0 assumed */
  pre[0] = v[0].Z; for (long i = 1; i < n; i++) pre[i] = mmul(pre[i - 1], v[i].Z);
  uint64_t inv = minv(pre[n - 1]);
  for (long i = n - 1; i >= 0; i--) { uint64_t zi = (i ? mmul(inv, pre[i - 1]) : inv); if (i) inv = mmul(inv, v[i].Z);
    uint64_t zi2 = mmul(zi, zi); xs[i] = mmul(v[i].X, zi2); ys[i] = mmul(v[i].Y, mmul(zi2, zi)); }
}
static inline long hslot(uint64_t x) { return (long)((x * 0x9E3779B97F4A7C15ULL) >> (64 - HBITS)); }

/* Number of DISTINCT k in [0,K) with (h0 + B k) P = O (found by an exhaustive BSGS scan); one of them in *kout.
 * Returns -1 on degenerate cases (S = O, a baby step = O, or two baby steps with equal x, i.e. ord(S) <= 2m). */
static long bsgs_count(uint64_t px, uint64_t py, uint64_t h0, uint64_t B, uint64_t K, uint64_t *kout) {
  uint64_t m = (uint64_t)ceil(sqrt((double)K)); if (m < 2) m = 2; if (m > MAXM) return -1;
  jpt S; jmul(&S, px, py, B); uint64_t sx, sy; if (!toaff(&S, &sx, &sy)) return -1;
  jpt cur = {sx, sy, MONE}; tmpj[0] = cur;                       /* tmpj[j-1] = j*S, j = 1..m */
  for (uint64_t j = 1; j < m; j++) { jpt t; jaddm(&t, &cur, sx, sy); if (t.Z == 0) return -1; cur = t; tmpj[j] = cur; }
  batch_aff(tmpj, (long)m, bx, by);
  memset(hkey, -1, sizeof(hkey));
  for (uint64_t j = 0; j < m; j++) { long s = hslot(bx[j]);
    while (hkey[s] >= 0) { if (bx[hkey[s]] == bx[j]) return -1; s = (s + 1) & ((1 << HBITS) - 1); } hkey[s] = (long)j; }
  uint64_t gx = bx[m - 1], gy = by[m - 1];                        /* G = m*S */
  jpt R; jmul(&R, px, py, h0);                                      /* R_i = h0 P + i G */
  uint64_t ks[64]; long nk = 0; uint64_t imax = K / m + 2;
  static uint64_t gxs[64], gys[64]; static jpt blk[64]; static int isinf[64];
  #define ADDK(kv) do { uint64_t _k = (kv); if (_k < K) { long _f = 0; for (long _t = 0; _t < nk; _t++) if (ks[_t] == _k) _f = 1; \
                        if (!_f) { if (nk >= 64) return 99; ks[nk++] = _k; } } } while (0)
  for (uint64_t i = 0; i <= imax; ) {
    long nb = 0; uint64_t i0 = i;
    while (nb < 64 && i <= imax) { isinf[nb] = (R.Z == 0); blk[nb] = isinf[nb] ? (jpt){MONE, MONE, MONE} : R; nb++;
      jpt t; jaddm(&t, &R, gx, gy); R = t; i++; }
    batch_aff(blk, nb, gxs, gys);
    for (long q = 0; q < nb; q++) { uint64_t ii = i0 + (uint64_t)q;
      if (isinf[q]) { ADDK(ii * m); continue; }
      long s = hslot(gxs[q]);
      while (hkey[s] >= 0) { long j = hkey[s];
        if (bx[j] == gxs[q]) { uint64_t jj = (uint64_t)j + 1;
          if (by[j] == gys[q] && ii * m >= jj) ADDK(ii * m - jj);        /* R_i = +jS  =>  (h0 + B(im - j)) P = O */
          if (madd(by[j], gys[q]) == 0) ADDK(ii * m + jj);               /* R_i = -jS  =>  (h0 + B(im + j)) P = O */
        }
        s = (s + 1) & ((1 << HBITS) - 1); }
    }
  }
  if (nk >= 1) *kout = ks[0];
  return nk;
}

long fast_trace(ulong a4, ulong a6, ulong p) {
  if (p < 1000 || p >= (1UL << 62)) return LONG_MIN;
  msetup(p);
  uint64_t a4m = tom(a4), a6m = tom(a6);
  /* discriminant Legendre: disc = -16(4 a4^3 + 27 a6^2) ; sign of -16 irrelevant for squareness only up to (-1/p) */
  uint64_t d3 = mmul(mmul(a4m, a4m), a4m), d2 = mmul(a6m, a6m);
  uint64_t disc = madd(mmul(tom(4), d3), mmul(tom(27), d2)); disc = msub(0, disc);    /* -(4a4^3+27a6^2); times 16 is a square */
  int ld = legendre_m(disc); if (ld == 0) return LONG_MIN;
  uint64_t B = (ld == 1) ? 4 : 2, A = 0;       /* requires >= 1 root (rational 2-torsion): checked by the caller's assert */
  uint64_t W = (uint64_t)floor(2.0 * sqrt((double)p)); while ((W + 1) * (W + 1) <= 4 * p) W++; while (W * W > 4 * p) W--;
  uint64_t lo = p + 1 - W, hi = p + 1 + W; uint64_t h0 = lo + ((A + B - lo % B) % B); uint64_t K = (hi - h0) / B + 1;
  for (uint64_t x0 = 1; x0 < 64; x0++) {
    uint64_t xm = tom(x0); uint64_t f = madd(madd(mmul(mmul(xm, xm), xm), mmul(a4m, xm)), a6m); if (f == 0) continue;
    int chi = legendre_m(f);
    A4 = mmul(a4m, mmul(f, f));                          /* E_d: a4 d^2, a6 d^3 ; point (d x0, d^2) */
    uint64_t px = mmul(f, xm), py = mmul(f, f);
    uint64_t k; long c = bsgs_count(px, py, h0, B, K, &k);
    if (c != 1) continue;                                 /* degenerate or ambiguous: try another point */
    uint64_t h = h0 + B * k; jpt chk; jmul(&chk, px, py, h); if (chk.Z != 0) continue;   /* direct verification */
    uint64_t nE = (chi == 1) ? h : 2 * p + 2 - h;
    return (long)(p + 1) - (long)nE;
  }
  return LONG_MIN;
}
