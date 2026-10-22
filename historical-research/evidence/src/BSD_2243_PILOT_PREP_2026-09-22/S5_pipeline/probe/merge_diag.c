/* merge_diag.c -- rebuild the R5-A class sums exactly (sum of the checkpoint i128 arrays, x 2^-96) and measure the acb_dft
 * output radii on them at prec 128; also the plus combination Re F_b - Re F_{u_b} (sign -1) as the merge forms it. */
#include <flint/acb.h>
#include <flint/acb_dft.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
typedef __int128 i128; typedef unsigned __int128 u128;
int main(int argc, char **argv) {
  const long M = 5031049; i128 *tot = calloc(M, sizeof(i128));
  for (int f = 1; f < argc; f++) { FILE *g = fopen(argv[f], "rb"); fseek(g, 0, SEEK_END); long sz = ftell(g); fseek(g, 0, SEEK_SET);
    unsigned char *b = malloc(sz); if (fread(b, 1, sz, g) != (size_t)sz) return 1; fclose(g);
    char key[64]; snprintf(key, sizeof key, "\nACC %ld\n", M); unsigned char *p = memmem(b, sz, key, strlen(key)); if (!p) return 2; p += strlen(key);
    i128 *a = (i128 *)p; for (long k = 0; k < M; k++) tot[k] += a[k]; free(b); }
  acb_ptr V = _acb_vec_init(M), F = _acb_vec_init(M); fmpz_t z; fmpz_init(z);
  for (long k = 0; k < M; k++) { i128 v = tot[k]; fmpz_set_signed_uiui(z, (ulong)((u128)v >> 64), (ulong)v); arb_set_fmpz(acb_realref(V + k), z); arb_mul_2exp_si(acb_realref(V + k), acb_realref(V + k), -96); }
  double maxin = 0; for (long k = 0; k < M; k++) { double r = mag_get_d(arb_radref(acb_realref(V + k))); if (r > maxin) maxin = r; }
  acb_dft(F, V, M, 128);
  double mx = 0, mxi = 0; long jm = 0; for (long j = 0; j < M; j++) { double r = mag_get_d(arb_radref(acb_realref(F + j))); if (r > mx) { mx = r; jm = j; } double s = mag_get_d(arb_radref(acb_imagref(F + j))); if (s > mxi) mxi = s; }
  printf("input max radius %.3e; DFT output max rad(Re) %.4e at j=%ld, max rad(Im) %.4e; Re F_jm = %s\n", maxin, mx, jm, mxi, arb_get_str(acb_realref(F + jm), 10, 0));
  return 0; }
