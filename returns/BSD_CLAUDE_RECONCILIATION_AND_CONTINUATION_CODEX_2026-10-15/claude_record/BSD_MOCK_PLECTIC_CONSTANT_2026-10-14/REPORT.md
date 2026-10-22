# Mock plectic constant experiment — REPORT

Claude (Opus 5.5), 2026-10-14/15. The user asked to run both checks: (1) does the conjectural global rank-two class carry
the tame-law constant K_E, and (2) is that constant the same at two primes. Agents read the two mock plectic papers and
tested local software; everything else ran here. No pushes, messages, installs or paid compute.
**Endpoint effect: none. FIN, ORDER9 and Q36 are unchanged.** Control curves only.

## Verdict

1. **Constant = K_E? Not testable as a published prediction.** None of the three plectic papers predicts any constant:
   Darmon–Fornea (Conj. 3.13) and Fornea–Gehrmann (Conj. 2.16) only say the invariant lies in the image of a P∧Q
   regulator, and Fornea–Guitart–Masdeu call their one observed factor of 8 "not explained". What could be tested:
   - **Exact p-adic class:** Lp/Reg_p = analytic Sha, the BSD constant in PARI's normalization (K_E/(4 c_inf)), in 44/44
     runs (8 curves, up to 7 primes each). The cyclotomic p-adic class is exactly the BSD multiple of P1∧P2 everywhere.
   - **Mock plectic proxy** (Fornea–Gehrmann's Gross-point theta elements): the scalar is a p-adic unit wherever p does
     not divide K_E (all 7 informative rows), and its dependence on the auxiliary field is exactly
     sqrt(L(E^K,1) sqrt|d_K|), the Gross–Waldspurger normalization (9/9 field pairs). What remains is a field-independent
     part attached to E alone. Comparing that part with K_E needs Fornea–Gehrmann's normalization (25), which no local
     tool supplies; it is the record's open normalization problem.
2. **Same at two primes? Yes, in the form the proxy allows.** On 1001c1 (K_E = 48) the Gross-point derivative vanishes
   exactly where the determinant of the same two global points vanishes, at p = 7 and at p = 13, with both outcomes
   (zero and nonzero) occurring at each prime, and the scalar is a unit at both, as 7 and 13 do not divide 48.

## A. What the published mock plectic theory says (verified against the papers)
- Darmon–Fornea (arXiv 2310.16758, JIMJ 2025): prime conductor p >= 11, K of class number one with p inert; Thm 3.4: the
  invariant is the first derivative of an anticyclotomic p-adic L-function with Heegner-point values; Conj 3.13: it lies
  in the image of P^Q -> delta(P)(x)log(Q) - delta(Q)(x)log(P). No constant is stated. One prime per curve. No numerics.
- Fornea–Gehrmann (arXiv 2311.03100v2): general N = pN+N-; Conj 2.16 same regulator shape, no scalar; no p-adic L-function
  of E is defined; the computable objects are mod-p^k theta elements of level-raised forms on definite quaternion algebras,
  whose derivative equals ord_p(q)*loc_l(Q_K) up to an unknown unit u_l per auxiliary prime l.
- Fornea–Guitart–Masdeu (2104.12566): genuine plectic invariants; one comparison with global points, factor 8 "not
  explained"; the second point is not printed, so it was not re-tested here.

## B. Exact p-adic constant (cyclotomic p-adic class), sealed (padic_bsd/PREDICTION.md)
44/44 runs: analytic p-adic rank 2 and Lp/Reg_p = 1 = Sha_an (PARI ellpadicbsd/ellpadicregulator), 8 rank-2 curves
(389a1 433a1 664a1 655a1 1615a1 1001c1 1309b1 1653a1) x good ordinary p in 5..23, 3–5 p-adic digits. The constant is the
same rational at every tested prime: the exact form of the 10-14 wild-leg law (a_p - 1)^2 * K_E * det.

## D. Tamagawa vs localization statistics (tamlog/)
7,242 (curve, p) rows: zero localization E(Q)/p -> E(Q_p)/p in 0.4% of p | K_E rows (1/228) vs 0.3% (21/7014): no link.
Side signal, unexplained: at GOOD primes both generators' logs vanish mod p^2 far less often than independence predicts
(p=5: 2/1266 vs about 38), although each generator alone vanishes at the expected rate about 1/p.

## C. Mock plectic proxy (Fornea–Gehrmann level-raised Gross-point theta elements, k = 1), sealed 966c7de8…
All 10 rows (20 field computations) met their sealed predictions. Sum over Gross points S0 = 0 mod p in every field (zero at the trivial character).

| curve | p | aux l | classes | det_l | fields: derivative D_l mod p | prediction | met |
|---|---|---|---|---|---|---|---|
| 655a1 | 5 | 2 | 66 | 2 | -67: 4, -163: 1 | nonzero | yes |
| 655a1 | 5 | 17 | 1,056 | 4 | -163: 2 | nonzero | yes |
| 655a1 | 5 | 23 | 1,452 | 0 | -8: 0, -163: 0 | zero | yes |
| 655a1 | 5 | 47 | 3,036 | 2 | -8: 3 | nonzero | yes |
| 655a1 | 5 | 53 | 3,432 | 4 | -8: 1, -67: 3 | nonzero | yes |
| 1001c1 | 7 | 3 | 224 | 6 | -43: 5, -79: 1 | nonzero | yes |
| 1001c1 | 7 | 47 | 5,152 | 1 | -51: 5, -79: 2, -95: 3 | nonzero | yes |
| 1001c1 | 13 | 17 | 1,792 | 0 | -24: 0, -164: 0, -167: 0 | zero | yes |
| 1001c1 | 13 | 149 | 16,576 | 1 | -83: 12, -164: 5, -167: 11 | nonzero | yes |
| 1001c1 | 7 | 73 | 8,064 | 0 | -43: 0 | zero | yes |

Exploratory cross-field ratios (u_l cancels; pre-registered candidates): (c1/c2)^2 matched candidate (c),
L(E^K,1)*sqrt|d_K| / Omega^-(E), in 9/9 pairs; "same constant in every field" 7/9; BSD-normalized twist value 8/9
(fails at l = 53, Q(sqrt -8) vs Q(sqrt -67)). So the scalar = sqrt(twisted central L-value, Gross normalization) x a
field-independent part attached to E alone.
Engineering: Sage's BrandtModule.hecke_matrix is quadratic in the class number; replaced by brandt_fast.py (neighbors =
2-dim right submodules of I/qI; identification by a lattice-scaled theta bucket + PARI qfisom + is_right_equivalent),
validated equal to Sage's matrices on 3 cases and reproducing finished rows.

## What this says about the missing global object
- Every rank-two object we can compute looks like a shadow of one global class P1∧P2 with a BSD-type constant: the
  finite tame and p-adic legs (10-14: K_E times the full determinant, with leg factors), the exact cyclotomic p-adic class
  (B), and now the Heegner-built mock plectic proxy (C), whose direction is P1∧P2 at both primes tested.
- The proxy's size behaves like a Heegner point's index: it scales with the square root of the twisted central value in
  Gross's normalization, and what is left does not depend on the auxiliary field. So the published candidate for the
  global class is a Heegner-type object over imaginary quadratic fields whose remaining unknown is a single E-constant.
- If that E-constant is sqrt(K_E) up to explicit local factors, mock plectic points are the global object that the tame
  law's step C needs. The test of that is one number per curve: Fornea–Gehrmann's normalization (25), the mod-l Kummer
  normalization of the level-raised eigenfunction, which reads Heegner points of conductor p^2 at a supersingular prime l.

## Limits
- Control curves only; mod p only (k = 1); auxiliary fields with p !| h_K; Cremona generators.
- The proxy sees the scalar up to an unknown unit per auxiliary prime; only valuations, vanishing patterns and ratios
  across fields sharing that prime are tested. The cross-field normalization (c) was one of three pre-registered
  candidates, exploratory, not a sealed pass/fail law.
- The only setup where p divides K_E (3565a1, p = 5) could not test the K_E factor at k = 1, because both generators'
  p-adic logs vanish mod p^2 there.
- Same-session work; the agents' literature notes were spot-checked against the papers (Darmon–Fornea statements re-fetched).

## Next attack
Fix normalization (25) on the cheapest row: 655a1, p = 5, l = 2, K = Q(sqrt -67) (h_K = 1, 30 Gross points). Compute the 30
Heegner points of conductor 25 on X_0(655) to high precision, recognize their minimal polynomial over K, reduce at a prime
above 2, and read them in E(F_2) = Z/5. That gives the canonical derivative, hence u_2, hence the E-part of the scalar to
compare with K_E = 8.
