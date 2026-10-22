# RETURN — Lane R25 (MS-R24 at nonsplit p = 3; route K bookkeeping). Claude Opus 5.5, 2026-09-29.

## STATUS: T_INT_PROVED_MODULO — UNAUDITED until the checker passes it
MS-R24, O2 and O4 are written with every cited input and its grade, and the chain to #Sha(E/Q)[3^inf] <= 9 (then
(Z/3)^2 with B2) is assembled. No named gap was found in MS-R24, O2 or O4. "Modulo" = the INPUTS listed below.
No refutation: no power of 3 that fails to cancel was found. At l = 5843 no factor (1 + 5843^{-1}) arises.

## Collision check: PASS (NOTES.md §1). Kato (upper-bound) direction; no R1/R2, SU, MS-B1, MS-R3 item reopened; no FIN claim.

## Kill tests (run first, in order): all three PASS
- K-R25a (split sanity): PASS (D3). The twisted family L_n^(alpha) (D1) at alpha = +1 is Kobayashi's log_p(d_n)
  (Kob l.115) term by term; Gauss sums tau(chi) (l.290-294); L_0 = 0, so Col(z)(0) = 0 (l.325-329). Exact checks
  n <= 3 in checks/coleman_family.log. By-product (REMARK): Kob's literal d_n (with log(1+X) inside ell) equals
  zeta_{p^{n+1}} d_n' and is not Delta-fixed (d_0 != 1); harmless, only log_p(d_n) is used (NOTES §3).
- K-R25b (trivial character): Claude's pre-computation CONFIRMED EXACTLY. Col(z)(0) = L_0 * exp*(z_0) with
  L_0 = (1-alpha^{-1})(1-alpha/p)^{-1} = 3/2 (D1.1(b); = Ka Thm 16.4(ii) at source) and exp*(z_0) = (1+1/3) L/Omega_+
  (Ka 12.5(1) + 6.2): product 2 L(E,1)/Omega_+ = (1-alpha^{-1}) L/Omega_+ = Ka 16.2(ii). Sage's 3-adic L-series gives
  constant term = 2 L(E,1)/Omega_E on all 289 nonsplit test curves (A = B), and 0 at split 21a1, 51a1.
- K-R25c (bookkeeping): PASS (D4). 289 rank-0 curves, 3 || N, a_3 = -1 (126 with a nonsplit l = 2 mod 3; 26 with
  9 | sha_an): route K's v_3(char(Sel^v)(0)) <= v_3(L_3(0)) holds, with equality, on all 289; no off-by-one on the
  126. Negative controls (extra Euler factor (1 - a_l/l) on the Selmer side; wrong local term #E(Q_l)[3^inf]) are
  CAUGHT on 126/126. Stated limits: C = A is forced for rank 0 by the definition of sha_an; a stray factor on the
  L-side is numerically invisible (excluded by D6(c) instead). Rank 1: NOT RUN (Sage has no 3-adic regulator at
  nonsplit multiplicative p; not cheap).

## Target 1 — MS-R24 (D1, D2, D5): DERIVED
- Explicit integral norm-compatible c in lim E^(m_n): log_E^(c_n) = L_n^(-1) = (-1)^{n+1}(3/2) + sum_m (-1)^m 3^{-(n+1-m)} S_m.
  Integrality over Z_9 via Dwork's lemma (proved inline) for G = exp(b h), b = lambda^{-1}, phi(b) = -b (D2).
- Col(z) = lim sum (c_n^sigma, z)sigma is an ISOMORPHISM H^1_Iw(T)/H^1_Iw(T^0) -> Lambda (cokernel 0); Ka Lemma 17.12
  independently gives finite cokernel. Col(loc z_gamma) = L_{3,-1,omega_E,gamma} EXACTLY, by Kobayashi's interpolation +
  uniqueness argument (Ka 12.5(1), 16.2-16.3). Cross-check: Ka Thm 16.6 (16.1 allows p | N), but its p | N case runs
  through Ka Rem 16.5(2) = unpublished [KKT]; the primary proof does not use it.
## Target 2 — O2 (D6): DERIVED on Kato's printed 17.13 template
0 -> H^1(T)/Z(f,T) -> Lambda/(L_3) -> X -> H^2(T) -> 0; with Ka 12.5(4) (O1): char(X) | L_3 (T-INT).
Nonsplit replacements for Ka 17.9: H^2_loc = 0; H^1_f = image of H^1(T^0) at every level (Greenberg = classical).
l = 5843: Ka 17.10's l != p step (no reduction hypothesis) gives lim(j_*-condition) = lim(BK) = 0; both Kato's zeta
elements (L_{p}: only p removed, Ka 6.2) and Kato's H^q (j_*, Ka 8.2) are PRIMITIVE at 5843. A factor 1 + 5843^{-1}
(v_3 = 1) only arises from a Sigma-imprimitive Selmer group, which route K never uses. Delta-branch: gamma^+ only.
## Target 3 — O4 (D7): DERIVED. The certificate's L_3 (SW conventions) = unit * L_{3,-1,omega_E,gamma}; units: 2 (two
real components, checks/seed_sign_check.log), Manin constant (3 does not divide c: Cesnavicius arXiv:1703.02951
Thm 1.2/2.11, 3 || N; THEOREM), change of generator of Gamma, signs.
## Target 4 — Assembly (D8): T-INT + v_3(a_2) = 2 + ord_T f_E >= 2 => f_E = T^2 g, v_3(g(0)) <= 2 => (Jones 3.1 forward,
height certificate) #Sha[3^inf] <= 9 => with B2: Sha[3^inf] = (Z/3)^2. No Skinner, no SU, no GRH.

## INPUTS (the "modulo"), and the checker's first targets
1. O5: Jones 1989 Thm 3.1 (forward) and the height certificate giving v_3(Reg_gamma) = 0 in the normalisation matching
   L_3's T (>= -1 suffices, via squareness). WARNING: 156a1 shows normalized regulators can have negative v_3 (D8).
2. S.3's certified a_{4,2} (v_3(a_2) = 2); B2 (Sha[3] contains (Z/3)^2); O1 (addendum 5).
3. SECONDARY (textbook, not re-read): Tate local duality/Euler characteristic; Nakayama-Rim; Tate curve over Q_9.
4. Convention matching chi <-> chi^{-1} between Kob, Ka 16.2/16.4 and SW: inherited from Kobayashi's printed split
   identity; the alpha-dependent factors were matched separately (D1.1(c), Ka 16.4). Worth an independent check.

## Grades: THEOREM at source — Ka 6.2, 8.2, 12.4, 12.5, 14.1, 14.9.3, 16.1-16.3, 17.10, 17.12, 17.13; Kob l.79-329 (Ka 16.4/16.6: cross-check, KKT caveat);
SW l.290-521; Cesnavicius Thm 1.2/2.11. DERIVED — D1, D2, D5-D8. REMARK — Kob d_n slip. COMPUTED — checks/*.
Resources: 1 process at a time, ~0.03 CPU-h, < 20 MB. Fetched: 2 arXiv PDFs (sources/SOURCES.sha256). No pushes,
messages, seed prime runs, paid compute or subagents. Files: see MANIFEST.sha256.

FIN, ORDER9 and Q36 are unchanged.
