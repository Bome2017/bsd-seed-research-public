# Lane 7 return (Fable 5.1, 2026-09-29): the #Sha factor of the tame constant on 194040co6
## Status: SHA_FACTOR_CONFIRMED (the only test available; see the power-of-2 caveat)

194040co6 has rank 2, Delta > 0 (c_inf = 2), Tam 4, tors 2, sha_an 4. On all 17 rows (4 primes, R != 0 on every row),
w = C2/((a_l - 2) R) = K_E = 4 c_inf #Sha Tam/tors^2 = 32 (mod p). The Sha-free constant 8 fails on all 17.

| p | 32 mod p | Sha-free | l: w |
|---|---|---|---|
| 13 | 6 | 8 | 53, 79, 131, 157, 313: 6 (kill test) |
| 17 | 15 | 8 | 103, 137, 239, 307: 15 |
| 19 | 13 | 8 | 191, 229, 419, 457: 13 |
| 23 | 9 | 8 | 47, 139, 277, 461: 9 |

**Kill test (p = 13): PASS.** All 5 admissible l have R != 0; w = 6 = 32 (mod 13) at each; 8 fails at each.

## Method and checks (outputs/*.out)
- **Curve (s1).** ecdata l.25432 = PARI: N, minimal model, Delta > 0, Tam [1,2,1,2,1], tors Z/2, w = +1. The generators lie on the
  curve (weighted [X:Y:Z] -> (X/Z^2, Y/Z^3)) and are saturated at B = 2000. det H = Cremona Reg to 3e-29; sha_an = 4 to 60 digits.
- **Eligibility.** Every p in 13..43 passes: p !| 6N tors Tam; p !| #E(F_p); p !| #Ens(F_r) = 2, 3, 4, 7, 12 (r | N); no p-isogeny;
  lane 4's GL2 witnesses.
- **Symbols.** [a/l]^+ = (1/(l-1)) sum over even chi != 1 of chibar(a) tau(chi) L(E,chibar,1)/omega1 (Birch). The trivial
  character drops out since L(E,1) = 0. L-values: cutoff series, root number w_E chi(N) tau^2/l, 57 digits, tail <= 7e-51.
- **Denominator bound.** co1 is optimal with Manin c = 1 (opt_man). PARI: omega1(co1) = 8 omega1(co6), omega2 equal, both lattices
  rectangular. Since l !| N, a/l ~ 0. lambda(0) = L(E,1) = 0: it lies in (1/4) Lambda_co1, so [0]^+ is in 2Z; numerically 1.5e-59.
  Hence [a/l]^+ is in 8Z. Every value is within 4e-54 of 8Z, so the margin is >= 1e53 against a half-gap of 4.
- **Route checks.**
  - (i) VALIDATION CONTROL PASS: the same code gives lane 4's exact msfromell symbols (equal integer vectors) at 389a1
    l = 11, 29, 53 (also = PIPE29) and 1615a1 l = 23, 53.
  - (ii) The functional-equation (t) residual on co6 is <= 1.4e-54. (iii) lfuntwist agrees on co6 (l = 53, 2 characters) to
    1e-56. All of this is PARI floating point, not ball arithmetic.
- **C2, R.** C2 from lane 4's coef; R from tame_reg.gp verbatim (416b38c7...). Quad/parallelogram checks = 1 and c0 = c1 = 0 on every row.

## Controls (s4; tally [17,17,0,0,17,17,17,17,17,17]; every control fails on every row)
1. **Sha-free** (8): rejected 17/17.
2. **Wrong power of 2.** 2^j L^alg = w only for j = 3 (mod ord_p 2 = 12, 8, 18, 11), i.e. w = 2^5 with the exponent fixed mod 792.
3. **Mismatched generator** g^s (s^2 != 1): rejected 17/17.
4. **Swapped period** (Omega_E = 2 omega1, giving 16): rejected 17/17. Extras -K, K c_N (c_N = 48/55), Tam/tors (64): rejected 17/17.

## Same-class Sha = 1 calibration (s5)
- co1–co5 have sha_an = 1, with Tam/tors/c_inf = 512/4/2, 256/4/2, 32/2/1, 128/4/2 and 16/2/1.
- Their symbols are the co6 symbols times omega1(co6)/omega1 = 1/8, 1/4, 1/4, 1/2 and 1/2 (exact). With their own tame regulators,
  w = 4 c_inf Tam/tors^2 on 40/40 rows (p = 13 at 5 l; p = 17 at 3 l). So at this conductor the Sha = 1 curves need no extra
  factor, and co6 needs exactly 4 = sha_an.

## Scope
- **Shows:** consistency evidence that the tame constant carries #Sha (w tracks 4 c_inf sha_an Tam/tors^2). **Power-of-2 caveat.**
  #Sha = 4 = 2^2, so on co6 every candidate constant is +-2^j; the data pin j = 5. Attributing 2^2 to #Sha rests on lane 4's
  j = 3 pin (68 rows at Sha = 1) and on the 40 partner rows.
  - An odd Sha (like the seed's 9) is untested: all 42 rank-2 curves with sha_an != 1 at N < 500k have sha_an = 4 (scan file).
- **Grade.** Numerical identification of the symbols, then exact mod-p arithmetic. Conditional on BKS Conj 2.3. #Sha = 4 is BSD's
  prediction, not proved. The Manin factor at c != 1 is still untested. It grades K288 only as above; it proves nothing
  about FIN, ORDER9, Q36 or #Sha = 9 for the seed.

## Resources and files
- **Resources.** About 0.17 CPU-h; at most 2 gp processes. No seed prime runs, pushes, messages, paid compute or subagents.
- **Files.** scripts/: lib7.gp, s1–s6, and lane 4's norm_lib.gp, tame_reg.gp, pipeline_389a1_m29.gp (unchanged). outputs/: *.out,
  sym_co6_l*.txt (exact symbols), rank2_sha_ne1_scan.txt. Also NOTES.md, RESUME.md, STATE.json, MANIFEST.sha256.
- **Process deviation.** Earlier RETURN.md writes were 78, 76 and 63 lines; trimmed to 60 by edits.

FIN, ORDER9 and Q36 are unchanged.
