# Lane NORM return (Opus 5.5, 2026-09-29)

## Status: DERIVED_AND_CALIBRATED

    w_(p,l) := C2(p,l) / ((a_l - 2) R_(p,l))  ==  K_E  (mod p),
    K_E = 4 * (Omega_E / omega_1) * #Sha * Tam / #tors^2 = 4 * c_inf * #Sha * Tam / #tors^2.

Here omega_1 is the least positive real period (the production normalizer), Omega_E = c_inf omega_1 is BKS's
Omega^+, and c_inf = #pi_0(E(R)). So K_E = 8 #Sha Tam/tors^2 if Delta > 0 and 4 #Sha Tam/tors^2 if Delta < 0.

- **The hypothesis is right only for Delta > 0.** "8 #Sha Tam/tors^2 on every curve" holds for Delta > 0, which
  includes 389a1 and the seed. It FAILS for Delta < 0 in the production convention: at 433a1, p = 11, l = 23 we get
  w = 4 where 8L^alg = 8. It becomes universal only if the symbols are normalized by MT's Omega^+ = Omega_E/2.
- **Calibration.** Eligible rows: 6 curves, 15 (curve, p) pairs. The formula matches 68/68 rows with R != 0. In all
  7 rows with R = 0, C2 = 0 as well. Every negative control fails, on every row.
- **Kill test (389a1, p = 5).** w = 3 = 8 (mod 5) at l = 11, 31, 71, 191. The old fit predicts 1: REJECTED.

## Derivation: where each factor enters

**Setup and sources.** Take p satisfying BKS II Hyp 2.2. Let F = F_l be the degree-p subfield of Q(zeta_l), with
l = 1 (mod p). Then G = C_p, T = sigma_g - 1, and I^2/I^3 = F_p T^2. We use:
- BKS §2.1 (L^alg);
- BKS §2.2: Conj 2.3, (3), (7), (9), (10) and Rem 2.7;
- Birch's formula;
- the retained C-rec (G2 (4.4)–(4.5)).

1. **Production element; period c_per = 1/c_inf; orientation.**
   - The production element is theta_l = sum_a [a/l]^+ sigma_a, with [r]^+ = Re lambda(r)/omega_1 and
     lambda(r) = 2 pi i int_{i oo}^r f dz, so that lambda(0) = L(E,1).
   - Birch's formula: sum_a chi(a) lambda(a/l) = tau(chi) L(E, chibar, 1). BKS (7) normalizes by Omega_E, so
     theta_(F,l) = (omega_1/Omega_E) theta_l. Hence **c_per = omega_1/Omega_E = 1/c_inf**: 1/2 for two real
     components, 1 for one.
   - **Tested.** tau(chi) L(E,chibar,1)/(omega_1 sum chi(a) [a/l0]^+) = 1 to 38 digits, for 6 characters of order 3
     and 5 on each of the 6 curves. The 389a1 pipeline symbols at l = 29 are reproduced exactly.
2. **Manin constant: absent.** [r]^+ is normalized by the Néron period of E itself, and (7) is stated through
   L-values. BKS's factor c(phi)^-1 (Rem 2.7) only converts Darmon's phi-normalized element.
   - Symbols normalized by the lattice of f (Lambda_E = c Lambda_f for optimal E) would multiply K_E by c.
   - c is a p-unit, but it can be a power of 2.
   - **Not testable here.** Every rank-2 curve with N <= 5000 has c = 1 (opt_man join), including the
     non-optimal curve 1615a2. The seed pipeline divides Arb integrals of f by omega_1(E), so c does not enter.
3. **Bad-prime Euler factor c_N: it cancels.**
   - BKS (10) at m = l gives Eul_N theta_(F,l) = u theta_(F,S). Here aug(u) = l = 1 (mod p) and aug(Eul_N) = c_N.
     A multiplier acts on I^2/I^3 through its augmentation.
   - Conj 2.3 gives theta_(F,S) = (-1)^nu(l) L^alg_S R_F, with L^alg_S = L^alg (#E(F_l)/l) c_N (Rem 2.1).
   - Therefore **theta_(F,l) = -L^alg #E(F_l) R_F**. Two cancellations happen: c_N (the S-truncation removes it
     from both theta_(F,S) and L^alg_S), and the l in u against the 1/l. This is Darmon's form, (8) with (9).
   - **Tested.** The candidate K_E c_N is rejected on all 68 rows; c_N != 1 (mod p) at every eligible pair.
4. **Factor 4 (eps·2·H).** Write R_F = det(eps 2 H) T^2 = 4 R_(p,l) T^2. The sign eps² = 1 drops out, because
   the determinant is 2×2.
   - **Tested independently of c_per.** On the Delta < 0 curves, where c_per = 1, w = 4 L^alg exactly (433a1,
     664a1, 655a1, 1615a2).
5. **Signs.** Two signs cancel, so w = +K_E:
   - (-1)^nu(l) = -1, since tau_l(1) = mu(l);
   - #E(F_l) = -(a_l - 2) (mod p), since l = 1 (mod p).
   - The orientation of lambda matters: the opposite orientation flips w. The candidate -K_E is rejected on all
     68 rows.
   - Two further sign changes act by +1 in degree 2: eps, and the involution sigma -> sigma^-1. **Tested:** C2
     computed from sigma_a^-1 equals C2 on every row.
6. **Torsion and Tamagawa numbers.** Both enter only through L^alg = #Sha Tam/#tors^2: Conj 2.3, which in
   Darmon's form is J_S R_S = prod #E(F_l) Tam/tors^2 R_F, BKS (9). Hyp 2.2(iii) makes them p-units.
   - **Tested** on 1615a1 (Tam 8, tors 2): the variant 8 Tam/tors is rejected at p = 11, 13, 23. Also tested on
     664a1 (Tam 4), 655a1 (Tam 2) and 1615a2 (Tam 16, tors 2).
7. **Omega^+ versus omega_1 (one or two real components).** Items 1–6 give c_per C2 = 4 L^alg (a_l - 2) R. So

       w = 4 L^alg / c_per = 4 c_inf L^alg.

   The formula is exact in F_p. It is conditional on Conj 2.3, which is the object being calibrated.

## Calibration table (exact symbols; production C2 and tame_reg.gp; l = 1 mod p, v_p(l-1) = 1, p !| #E(F_l))
#Sha = sha_an = 1 on all test curves (BSD grade; the p-parts agree with Ota Thm 6.4 since C2 != 0). All optimal
curves have Manin constant 1. The prime check covers p !| 6N tors Tam, non-anomalous, p !| #Ens(F_r), no p-isogeny,
plus Serre GL2 Frobenius witnesses. It passed at every p listed except those marked "inelig".

| curve | Delta | Tam, tors | K_E | p: w at each l with R != 0 (zero rows: R = C2 = 0) |
|---|---|---|---|---|
| 389a1 | + | 1, 1 | 8 | 5: 3 at 11,31,71,191 (181, 241 zero) · 11: 8 at 23,89,199,331,353 (67 zero) · 13: 8 at 53,79,157,313,443,521 |
| 433a1 | − | 1, 1 | 4 | 11: 4 at 23,89,199,331 (67 zero) · 13: 4 at 53,79,131,157,313 · [5 inelig, #E(F_5)=10: 4 at 11,41,71,181] |
| 1615a1 | + | 8, 2 | 16 | 11: 5 at 23,67,89,331,397 · 13: 3 at 53,79,131,313,521 · 23: 16 at 47,139,277,461,599 |
| 664a1 | − | 4, 1 | 16 | 11: 5 at 23,67,89,199,331 · 13: 3 at 53,131,157 (79, 313 zero) · [5 inelig, #E(F_5)=10] |
| 655a1 | − | 2, 1 | 8 | 11: 8 at 23,67,89,199,331 · 17: 8 at 103,137,239,307,409 · 19: 8 at 229,419,571 (191, 457 zero) |
| 1615a2 | − | 16, 2 | 16 | 11: 5 at 23,67,89,331,397 · 13: 3 at 53,79,131,313,521 (non-optimal, isogenous to 1615a1) |

- Every entry equals K_E mod p. On every Delta < 0 row (p = 11, 13, 17, 19), 8 L^alg differs from w
  (outputs/curves.out, "hyp8L: 0"; for 1615a2, the swapPer column of controls.out).
- **Other replays.**
  - The 389a1 p = 7 prescreen c2 values are reproduced at all 8 l, with w = 1 = 8 (mod 7).
  - The 389a1 rows agree under two different saturated bases (C-basis).
  - The isogenous pair 1615a1/1615a2 gives identical w at every l, because 4 c_inf L^alg = 16 for both.

## Negative controls (each must fail; outputs/controls.out, tally [68, 68, 7, 7, 68, 68, 68, 68])
1. **Wrong power of 2.** The exponent is pinned modulo lcm(ord_p 2) over the tested primes: modulo 60 for 389a1,
   433a1 and 664a1; 660 for 1615a1; 360 for 655a1; 60 for 1615a2.
   - Delta > 0: 2^j L^alg = w only for j = 3.
   - Delta < 0: only for j = 2.
   - So every other power is rejected on all 68 rows. The old fit (j = 0) is rejected everywhere, including at
     389a1, p = 5.
2. **Mismatched generator.** C2 uses g^s with s^2 != 1 (mod p), while the tame logs use g. This gives
   w' = s^-2 K_E != K_E, rejected on 68/68 rows.
   - At p = 5, s = 3: s^-2 = 4 = -1, so w' = 2 = -8. The mismatch is a square, and here it is a SIGN.
3. **Swapped period convention.** Symbols divided by Omega_E (Delta > 0), or by MT's Omega_E/2 (Delta < 0), scale
   w by 1/c_inf or by 2. Rejected on 68/68 rows.
   - Under the MT normalization every curve gives 8 L^alg. That is the convention in which the hypothesis is
     universal.
4. **Extra controls.**
   - -K_E (sign): rejected on 68/68 rows.
   - K_E·c_N (the Euler factor surviving): rejected on 68/68 rows.
   - Tam/tors in place of Tam/tors^2: rejected on every row of 1615a1 and 1615a2, the only curves with tors != 1.

## Side claims tested at the smallest eligible prime (p = 5 on 389a1)
- **Always c0 = c1 = 0 (mod p) in rank 2.** True on every row, zero rows included.
- **Always R = 0 implies C2 = 0.** 7/7 eligible rows, plus 389a1 at p = 5 with l = 181 and 241.
- **c_N always cancels.** At p = 5, c_N = 388/389 = 2, which is not 1, and the formula without c_N still matches.
- **The involution never changes C2.** True on every row. This follows from binom(-k,2) = binom(k,2) + k together
  with c1 = 0.
- **"Never a sign" is FALSE.** See control 2. The out-of-scope anomalous rows at p = 5 (433a1, 664a1) also matched;
  no claim is made there.

## The seed
- The seed has Delta > 0 (c_inf = 2), Tam = 16 and tors = 2, so Tam/tors^2 = 4. The derived constant is therefore
  K_E = 32 #Sha, and 288 = 32·9 (outputs/replay.out).
- The fitted "2^3" of overview S5 is 4·c_inf. It is now derived, not fitted.
- 389a1's apparent k = 0 at p = 7 was 8 = 1 (mod 7), which is Codex's item 4.

**What K = 288 is evidence for.** It is CONSISTENCY evidence, at conjecture grade (BKS Conj 2.3 with the derived
and calibrated normalization), that the seed's tame leading coefficients are the refined Mazur–Tate values with
#Sha·Tam/tors^2 = 36. Equivalently, #Sha = 9 (mod p) at p = 17, 23, 29, 31, 37, 41, 43, 47. p = 19 is outside Hyp
2.2(iii), since 19 | #Ens(F_2243) = 2242. The evidence is not a proof of FIN, ORDER9, the cross-prime law or #Sha = 9,
and it carries nothing about L'' or q (DNR 17). Sha[p] = 0 at these primes was already known via Ota.

## Grades and limits
- **Derivation.** A written deduction from BKS II §§2.1–2.2 and Birch's formula. It uses the retained C-rec
  (MT pairing = eps·2·H, from G2) as input; the factor 4 is calibrated here, not re-derived. It is conditional on
  Conj 2.3, the conjecture being calibrated.
- **Calibration.** Exact rational computation of the symbols (PARI 2.17.3 msfromell). Their normalization
  kap = 1 is identified by the Birch ratio to 38 digits, and at 389a1, l = 29, by the Arb pipeline. The
  prime-to-p #Sha is sha_an = 1 (BSD grade).
- **Not tested.** The Manin factor at c != 1 (no rank-2 example with N <= 5000). The anomalous p = 5 rows are
  out of scope.
- **Resources.** About 7 min CPU in total, one process at a time. No seed prime runs: the seed replay reused the
  given c2 and ran tame_reg only. No subagents, pushes or messages.
- **Process deviation.** The first RETURN.md write was 67 lines, over the 60-line rule. Later writes complied.

## Files
- scripts/norm_lib.gp: helpers.
- scripts/tame_reg.gp: the production regulator, copied verbatim, sha256 416b38c7….
- scripts/pipeline_389a1_m29.gp: the pipeline symbols.
- scripts/kill_389a1.gp, curves.gp, controls.gp, replay.gp → outputs/*.out.
- outputs/rank2_N5000_scan.txt: the Cremona rank-2 scan (691 curves).

FIN, ORDER9 and Q36 are unchanged.
