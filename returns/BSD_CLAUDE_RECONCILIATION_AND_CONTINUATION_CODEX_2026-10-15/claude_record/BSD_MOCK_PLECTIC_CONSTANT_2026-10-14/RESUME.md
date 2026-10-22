# Mock plectic constant experiment — RESUME (Claude Opus 5.5, 2026-10-14, user: "go ahead and run both")

## Two checks (shape experiment, controls only)
1. Constant vs K: does the conjectural mock plectic point (Darmon–Fornea, arXiv 2310.16758) of a small rank-2 curve
   over Q carry the same rational constant as the tame law K_E = 4*c_inf*Sha*Tam/tors^2?
2. Two primes: on a curve where the construction applies at two primes, is the constant the same at both?

## Why (from the two-leg and wild-leg experiments, 2026-10-14)
Every finite direction sees K_E * det(full height pairing) * (leg factors). Finite levels split prime by prime, so the
cross-prime link must be a global object. Mock plectic points are conjectured to be such an object in Alt^2 of the
Mordell–Weil group. Endpoint effect: none (controls; shape only).

## Plan
A. Literature agents (lit/): DF 2310.16758 notes; FG 2311.03100 notes; software feasibility (Sage in run040 env; no Magma).
B. Curve selection (outputs/candidates.*): rank 2, small N, multiplicative at small p; prefer two such primes.
C. Implement the computable route (likely anticyclotomic p-adic L-function from Gross points / Brandt modules).
D. Seal predictions (constant under each plausible normalization) BEFORE computing any invariant. E. Compute, evaluate.

## Rules
No pushes, messages, installs, downloads to disk, paid or cloud compute. <= 4 CPU processes. Do not frame anything as a
single-prime certificate. Verify literature claims against paper text. Record prior attempt:
~/BSD_PLECTIC_ACTUAL_EVALUATOR_ATTEMPT_CODEX_2026-09-30 (seed-scale definite class set ~2.5e19: infeasible there).

## Agent A (Darmon–Fornea 2310.16758) — verified by my own fetch of the paper text, 2026-10-14
- Setting: E of PRIME conductor p (>= 11), K imaginary quadratic of class number one with p inert. No auxiliary level.
- Theorem 3.4: the mock plectic invariant Q(tau) = L_p'(E,K,1), first derivative of an anticyclotomic p-adic L-function
  (eq. 21) whose measure is Heegner-point valued; Q(tau) lives in H^1_f(K,T_pE) (x) K_p, not in a number field.
- Conj 3.12: if L(E/K,1)=0, Q(tau) != 0 iff (a_p=+1, ranks (E,E')=(0,2)) or (a_p=-1, ranks (1,1)); E' = twist by K.
- Conj 3.13: Q(tau) is in the image of P^Q -> delta(P)(x)log^{a_p}(Q) - delta(Q)(x)log^{a_p}(P). NO constant is
  stated (only "in the image"), so the paper predicts no Sha/Tamagawa constant. No numerical examples in the paper.
- Consequence: our controls are outside the setting (the rank-2 curve must be the twist E'); one prime per curve (p = N),
  so "two primes" is impossible in this framework; Q(tau) needs Heegner points of conductor p^n (agent: infeasible).
- Usable (agent's scan of local Cremona data): E=109a1, D=-8, E'=6976f1; 139a1/2224f1; 179a1/1611d1 (125 cases).

## Progress 2026-10-14 evening (rolling state)
- Agents: DF + FG predict NO constant; FG computable proxy (level-raised Gross-point theta elements) sees the scalar c_K only
  up to an unknown unit u_l per auxiliary prime l, so: vanishing patterns, v_p(c), and cross-field ratios (u_l cancels).
- p-adic constant check (padic_bsd/): 44/44 runs Lp/Reg_p = 1 = Sha_an, rank 2, 8 curves x up to 7 primes. DONE.
- Proxy (proxy/): predictions sealed (PREDICTIONS_SEALED.md sha 966c7de8...). Pipeline: global_side.py, gross_side.py.
  * 655a1 p=5 l=2: 66 classes, S0=0, D=4 (K=-67), D=1 (K=-163): nonzero as predicted. Cross-field (c1/c2)^2 = 4 mod 5
    = r(-67)/r(-163) = 144/576 (candidate b/c); candidate (a) "same constant" fails.
  * 1001c1 p=7 l=3: 224 classes, S0=0, D=5 (-43), D=1 (-79): nonzero as predicted. (c1/c2)^2 = 2 mod 7 = 216/24 (b/c).
  * Running (background): 655a1 l=17,23,53; 1001c1 p=13 l=17. Then 655a1 l=47; 1001c1 p=7 l=47; heavy: p=7 l=73, p=13 l=149.
- Side observation: the only p | K_E setup (3565a1, p=5, c_31 = 5) is also the only one with E(Q) -> E(Q_p)/p zero.
  Statistical test running: tamlog/ (rank-2 curves N < 20000, p in 5..13).
- tamlog DONE (7,242 rank-2 (curve,p) rows, N < 20000, p in 5..13): zero localization E(Q)/p -> E(Q_p)/p in 1/228 rows with
  p | K_E vs 21/7014 with p !| K_E: NO association (3565a1 was a coincidence). Side signal: per-generator vanishing ~1/p as
  expected, but BOTH vanish far less than independence predicts at GOOD primes (p=5: 2/1266 vs ~38 expected; p=7: 4/1607;
  p=11: 1/1715; p=13: 3/1706); multiplicative primes look random. Unexplained; basis-independent event (fine Selmer mod p).
- Proxy rows done (v1, sealed predictions all met): 655a1 l=2 (D 4,1), l=17 (D 2), l=23 (D 0,0 where det=0);
  1001c1 p=7 l=3 (D 5,1); p=13 l=17 (D 0,0,0 where det=0, three fields). Cross-field (c1/c2)^2: 2/2 match twist BSD ratio.
- Sage's BrandtModule.hecke_matrix is quadratic (1,106 s at 1,792 classes, 9.4 GB at ~3,400): replaced by brandt_fast.py
  (neighbors = 2-dim right submodules of I/qI; identification = qfrep bucket + qfisom + is_right_equivalent on ties),
  validated equal to Sage's matrices (3 cases) and reproducing the finished rows. gross_side_v2.py uses it, with
  row-sampled constraints for q >= 5. Running: run_v2.sh (655a1 l=53,47; 1001c1 p=7 l=47; then p=13 l=149; p=7 l=73).
