/* reviewer's test of the portable SHA-256 shim (compat/CommonCrypto/CommonDigest.h, reviewer's copy of the include path) */
#include "/Users/bsm/BSD_2243_PILOT_PREP_2026-09-22/S5_pipeline/compat/CommonCrypto/CommonDigest.h"
#include <stdio.h>
#include <stdlib.h>
static void hx(const unsigned char *d) { for (int i = 0; i < 32; i++) printf("%02x", d[i]); }
int main(int argc, char **argv) {
  unsigned char d[32];
  const char *v[] = {"", "abc", "abcdbcdecdefdefgefghfghighijhijkijkljklmklmnlmnomnopnopq"};
  for (int i = 0; i < 3; i++) { CC_SHA256(v[i], (CC_LONG)strlen(v[i]), d); printf("vec%d ", i); hx(d); printf("\n"); }
  /* one million 'a' via many odd-sized updates */
  CC_SHA256_CTX c; CC_SHA256_Init(&c); char a[1000]; memset(a, 'a', sizeof a); long left = 1000000; int step = 1;
  while (left > 0) { int n = step % 997 + 1; if (n > left) n = (int)left; CC_SHA256_Update(&c, a, (CC_LONG)n); left -= n; step += 7; }
  CC_SHA256_Final(d, &c); printf("million_a "); hx(d); printf("\n");
  for (int i = 1; i < argc; i++) { FILE *f = fopen(argv[i], "rb"); fseek(f, 0, SEEK_END); long n = ftell(f); fseek(f, 0, SEEK_SET);
    unsigned char *b = malloc(n); if (fread(b, 1, n, f) != (size_t)n) return 1; fclose(f);
    CC_SHA256_CTX c2; CC_SHA256_Init(&c2); long off = 0, s = 1; while (off < n) { long k = (s * 7919) % 65537 + 1; if (k > n - off) k = n - off; CC_SHA256_Update(&c2, b + off, (CC_LONG)k); off += k; s++; }
    CC_SHA256_Final(d, &c2); hx(d); printf("  %s\n", argv[i]); free(b); }
  return 0; }
