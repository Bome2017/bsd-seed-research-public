#include <flint/arb.h>
#include <stdio.h>
int main(void) {
  arb_t x, y, q; arb_init(x); arb_init(y); arb_init(q); arf_t ub; arf_init(ub);
  arb_set_str(y, "[0.0280449015194364044483094018079 +/- 3.04e-32]", 128);
  arf_set_d(ub, 1.368039570e-5);
  const char *mids[] = {"0", "0.001", "0.19", "1.5", "-0.37"};
  for (int i = 0; i < 5; i++) { arb_set_str(x, mids[i], 128); arb_add_error_arf(x, ub);
    arb_div(q, x, y, 128); printf("mid %-6s rad(x) %.10e  rad(x/y) %.10e  rad(x)/|y| %.10e\n", mids[i], mag_get_d(arb_radref(x)), mag_get_d(arb_radref(q)), mag_get_d(arb_radref(x)) / 0.0280449015194364); }
  return 0; }
