# 23 — GLOBAL RATIONAL-FUNCTION SPLITTING OF THE TARGET EXTENSION (operator proposal, 2026-09-16): kill audit
Sources: operator's proposal (this turn; its note, programs and manifest are NOT in ~/Downloads and were not run here); DR22
eqn:extension-construction l.2366-2400 (excision extension at finite level r on X_r^3, coefficients H^3(X_r^3-bar, Z_p)(2), packaged over
Lambda(G_r) by j, Kunneth projection p); CH (1.8); lane 12, 13 sec 5, 08 terminal block; Castella Thm A (lane file 22).

## A. Components verified independently of the cited Ciperiani–Krashen numbering
V1 Detection (2). Pic(E_Qbar) = Z[O] (+) E(Qbar) as Galois modules and H^1(Q, Z) = 0, so H^1(Q, Pic E_Qbar) = H^1(Q, E); Hochschild–Serre with the
   rational point O gives Br_1(E) = Br(Q) (+) H^1(Q, E) (H^3(Q, G_m) = 0), so each q_n in H^1(Q,E)[N] has a unique O-normalized class in
   Br(E); Br(E) injects into Br(Q(E)) (E regular, integral). Hence B_n = 0 iff q_n = 0 iff x_n in Kum_N(E(Q)/N). CORRECT.
V2 Extraction (sec 3). Div(E_Qbar) is a permutation module, H^1(G_Q, Div) = (+)_P H^1(G_{Q(P)}, Z) = 0 (Shapiro; Hom_cont(G, Z) = 0), and
   Div = Div^0 (+) Z[O] equivariantly, so H^1(G_Q, Div^0(E_Qbar)) = 0. Given (8), C_sigma = p^a D_sigma - div(u_sigma) is a cocycle, hence a
   coboundary sigma D - D, and (10)-(11) follow. CORRECT — and equivalent to: (8) holds iff p^a q_n = 0.
V3 Precision lemma (sec 4). The map of Kummer sequences (p^{n-m} on E[p^n] -> E[p^m], p^{n-m} on the middle E, id on the right E) gives
   q_m = p^{n-m} q_n. With p^{a_n} q_n = 0 and n - a_n >= m, q_m = 0. All q_m = 0 => x Kummer (finite Kummer injectivity + compatibility +
   Mordell–Weil finite generation; no Sha input). CORRECT, and strictly weaker than a fixed denominator.
V4 Cocycle (3)-(7). (4) from equal divisors and normalized leading coefficient at O; (6) from c_n(sigma tau) = c_n(sigma) + sigma c_n(tau);
   (7) by construction. CORRECT (closure only; the executed controls could not be re-run here).
V5 Remarks. For a Selmer class B_n is split over every Q_v(E) and unramified on E; the compatible q_n lie in the divisible part of Sha,
   which the Cassels–Tate pairing does not see. Both CORRECT. Only a global identity in Q-bar(E)^x can decide q_n = 0.

## B. Kill — three independent defects; the first is decisive and is the same wall as (TC)
K1 NO SOURCE FOR u_sigma. The excision extension DR22 l.2366-2400 is geometric at finite level r: H^3(X_r^3-bar, Z_p)(2), support cycles
   Delta_r^o[[a,b,c]], Lambda(G_r)-structure through j. The target extension (13) is reached from it by two operations that are not
   correspondences: (i) the Hida-module specialization at the weight-one Hecke point (a tensor operation (x)_T over the Hecke algebra,
   which on divisor groups produces Div^0 (x)_T T/p_{wt 1}, not a permutation module of any variety); (ii) the Artin contraction on the
   (g,h)-coefficients, which is not cycle-induced at any classical weight and has no characteristic-zero equivariant model there
   (13 sec 5(iii)-(iv); no cross-sheet correspondence on the tower, 12). Neither operation acts on Div^0(E_Qbar). So the "support and
   rational-equivalence data behind the excision extension" has no map to Q-bar(E)^x at all; the functions u_sigma have no source.
   This is the H9R21 obstruction relocated into Br(Q(E)), not a new operation.
K2 THE MOD-p^n SHORTCUT IS CLOSED. The descent (9) is a characteristic-zero fact. Mod p^n, H^1(G_Q, Div^0(E_Qbar)/p^n) contains
   (+)_P Hom(G_{Q(P)}, Z/p^n) != 0, so a mod-p^n cocycle of divisors does not descend. (8) must be an identity of actual rational functions;
   the only equivariant form the live contraction has at classical weight is the mod-p^n functional c-bar_n (13 sec 5(iv)), which cannot
   produce actual rational functions. The weaker precision (12) does not help: it weakens a condition on a construction that does not exist.
K3 TERMINAL EQUIVALENCE. (16) for all n <=> q_m = 0 for all m <=> kappa Kummer <=> (Castella Thm A, kappa != 0) rank E(Q) = 2 <=> Sha[p^inf]
   finite (08 terminal block). The u_sigma exist iff the point R with p^a c_n = sigma R - R exists, i.e. iff a second independent rational
   point exists. "Furnishing u_sigma from the source" is constructing that point. The proposal restates the endpoint as an identity.

## C. What is retained
(16) is an exact global CHECKER against which any future candidate point construction can be tested, with the weaker precision criterion
(12) replacing the fixed denominator of H9R22-23. It is retained as a criterion. It is not a construction and cannot be started: no
candidate u_sigma has a source, and by K3 producing one is producing the second point.

## Return
```
SPLITTING_CRITERION (2)          = VERIFIED (V1)
POINT_EXTRACTION (8)->(11)       = VERIFIED (V2)
WEAKER_PRECISION (12)            = VERIFIED, strictly weaker than a fixed denominator (V3)
COCYCLE_b_n                      = VERIFIED (closure); executed controls not re-run (files not local)
SOURCE_OF_u_sigma                = NONE: excision data reaches the target only through a Hecke-module specialization and a
                                   non-cycle contraction; neither acts on Div^0(E_Qbar)  (K1)
MOD_pN_DIVISOR_DESCENT           = FAILS: H^1(G, Div^0/p^n) != 0  (K2)
EQUIVALENT_TO                    = rank E(Q) = 2 <=> Sha[p^inf] finite  (K3)
FIRST_DEFECT                     = K1
DISPOSITION                      = CRITERION RETAINED AS CHECKER; CONSTRUCTION NOT STARTABLE. No new H9R number. No launch.
```

## D. Narrowing of K2 (operator/Pro 6, 2026-09-16) — accepted
H^1(k, Div^0(E_kbar)/N) is generally nonzero, but its everywhere-locally-trivial subgroup vanishes: D_N = (+)_P Ind_{G_{k(P)}}^{G_k} Z/N, a
continuous cocycle has finite support, each component is a character G_{k(P)} -> Z/N, local triviality at all places of k kills it on
every decomposition group of k(P), and Chebotarev finishes. So Sha^1(k, D_N) = 0 while H^1(k, D_N) != 0. K2 is restated: a mod-p^n divisor
cocycle descends only if it is locally trivial in D_N, and nothing supplies either the cocycle or its local triviality without the source
map of K1. K1 remains the decisive defect; K3 unchanged. Pro 6's further negative checks (Flapan–Lang: coefficient motives only; Qiu: height-
quotient vanishing, not rational equivalence; Fornea–Gehrmann polyquadratic plectic invariant forced to 0 by ord_{s=1} L(E/H,s) >= r+2;
Darmon–Fornea Conj 3.13 and the mock-plectic corank theorems stop at Selmer corank) are consistent with the terminal block and add no source.
