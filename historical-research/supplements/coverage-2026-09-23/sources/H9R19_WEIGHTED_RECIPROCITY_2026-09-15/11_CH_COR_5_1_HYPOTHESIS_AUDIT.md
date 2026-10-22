# 11 — Castella–Hsieh Corollary 5.1, hypothesis by hypothesis: does it identify kappa_{alpha,alpha^{-1}} in E(Q) (x) L without circularity?

Question (operator): does CH Cor 5.1 already prove that the exact target class kappa_E := kappa_{alpha,alpha^{-1}} lies in E(Q) (x) L using only
inputs independently established, or does it use an unavailable/circular assumption? Return the first unavailable hypothesis.

## 1. What Cor 5.1 says and where it comes from  [V, rendered pp.4, 23-25]
- Theorem A (p.4): assume L(E^K,1) != 0, L(E/K,chi^2,1) != 0, rho-bar_{E,p} irreducible, N^- square-free, rho-bar_{E,p} ramified at every q | N^-.
  Then kappa_{alpha,beta^{-1}} = kappa_{beta,alpha^{-1}} = 0 and:  (i) kappa_{alpha,alpha^{-1}} != 0 in Sel(Q,V_pE)  <=>  (ii) dim Sel_str(Q,V_pE) = 1.
  Standing setup (p.2): p > 2 good ordinary, p = p_frak pbar split in K, disc(K) prime to N, chi ring class of conductor prime to Np, chi(pbar) != +-1.
- Corollary B (p.4): hypotheses of Thm A + rank_Z E(Q) = 2 + #Sha(E/Q)[p^infty] < infinity  =>  kappa_{alpha,alpha^{-1}}, kappa_{beta,beta^{-1}} != 0 and generate Sel_str.
- Corollary C (p.4): hypotheses of Thm A  =>  ( kappa_{alpha,alpha^{-1}} != 0  =>  dim Sel(Q,V_pE) = 2 ).
- Proof of (ii) => (i) (p.24): "Suppose dim Sel_str = 1. By p-parity [Nek01] dim Sel(Q,V_pE) = 2 and log_{omega_E,p_frak}: S -> L is nonzero" ;
  S = Sel(K,V) = Sel(Q,V_pE) (x) L since Sel(Q, V_pE^K) = 0 by Kolyvagin/Kato from L(E^K,1) != 0; S = S^{(rho)} via (5.3) and
  (5.5) r >= rho := ord_J Theta_{f/K}, the latter from the Skinner–Urban divisibility (Theta^2) ⊃ (L_p) "by our hypotheses on rho-bar_{E,p}";
  Cornut–Vatsal for S^{(infty)} = 0; Howard's derived heights [How04]; then (5.6):
      h^{(rho)}(kappa_{alpha,alpha^{-1}}, x) = (1 - p^{-1}alpha_p)/(1 - alpha_p^{-1}) . theta-bar_{f/K} . log_{omega_E,p_frak}(x) . C   for all x in S,
  from Prop 3.7 (derived-height/Coleman-map formula), Theorem 4.7 (Col^eta(loc_p_frak kappa) = Theta_{f/K} . nonzero), Lemma 4.5(2).
- Cor 5.1 (p.25): "immediate consequence of (5.6)": kappa_{alpha,alpha^{-1}} = C . (1-p^{-1}alpha_p)/(1-alpha_p^{-1}) . theta-bar_{f/K}/h^{(rho)}(P,Q) . (P (x) log_p Q - Q (x) log_p P)
  "as elements in E(Q) (x)_Z L, for any basis (P,Q) of E(Q) (x) Q".

## 2. Hypothesis ledger for the identification "kappa_E in E(Q) (x) L via Cor 5.1"

| # | hypothesis | where it enters | status for this program |
|---|---|---|---|
| H1 | p > 2 good ordinary, p split in K, disc(K) prime to N, chi ring class, chi(pbar) != +-1 | setup | available by choice |
| H2 | L(E^K,1) != 0, L(E/K,chi^2,1) != 0 | Thm A; Sel(Q,V_pE^K) = 0; Cor 4.8 | available for suitable (K,chi) (Remark 1.4: [BFH90], [Vat03]); analytic nonvanishing, not circular |
| H3 | rho-bar_{E,p} irreducible, N^- square-free, ramified at q | N^- | Thm A; Skinner–Urban input; Thm 4.2 (iii)-(iv) | available (arithmetic conditions on (E,p,K)) |
| H4 | L(E,1) = 0 | Cor 4.8(1) (via DR17a Thm C: L(f(x)g(x)h,1)=0 => kappa in Sel) | available from analytic rank 2 |
| H5 | (ii) dim Sel_str(Q, V_pE) = 1 | the (ii) => (i) proof, hence (5.6), hence Cor 5.1's formula | NOT available from analytic data; see below |
| H6 | rank_Z E(Q) = 2 | "basis (P,Q) of E(Q) (x) Q" | available only if the program already has two independent points |
| H7 | #Sha(E/Q)[p^infty] < infinity, i.e. V_p Sha(E/Q) = 0 | identifies S = Sel(Q,V_pE) (x) L with E(Q) (x) L, the phrase "as elements in E(Q) (x)_Z L" | NOT available; this is Conjecture 1.2's (2) <=> (3) (Remark 1.3) |
| H8 | theorems used: p-parity [Nek01], Skinner–Urban divisibility [SU14], Cornut–Vatsal [CV05], Howard [How04], Kato/Kolyvagin, Vatsal nonvanishing of Theta_{f/K} | (5.3)-(5.6) | available (printed theorems under H1-H3) |

Relations: given rank-2 points (H6), Sel(Q,V_pE) ⊇ E(Q) (x) Q_p is >= 2-dimensional and log_p is non-zero on it (a non-torsion point has
non-zero formal logarithm), so dim Sel_str = dim Sel - 1 and (H5) <=> dim Sel = 2 <=> (H7). Given only analytic rank 2, (H5) needs both
(H6) and (H7). So the FIRST UNAVAILABLE HYPOTHESIS, on either reading, is
    (H7)  #Sha(E/Q)[p^infty] < infinity   [entering as CH Theorem A (ii) / Corollary B],
with (H6) additionally unavailable on the purely analytic reading.

## 3. Verdict
- Cor 5.1 does NOT supply "kappa_E in E(Q) (x) L" without circularity. Its very statement ("as elements in E(Q) (x)_Z L") presupposes
  Sel(Q,V_pE) = E(Q) (x) Q_p, i.e. Sha-finiteness (H7), and rank 2 (H6); and its proof runs through (ii), which for this program is
  equivalent to (H7) once the points are in hand. Relative to a BSD bridge these are the conclusion, not an input.
- What CH give unconditionally under H1-H4 (no Sha, no rank): kappa_{alpha,alpha^{-1}} in Sel(Q, V_pE) (Cor 4.8(1)) — Selmer, not
  Mordell–Weil — and it is not even known to be non-zero (that is (i), equivalent to (ii)). Cor C is the useful contrapositive-style
  statement: kappa != 0 => dim Sel = 2, so an INDEPENDENT non-vanishing proof of kappa_{alpha,alpha^{-1}} would give Selmer rank 2 and,
  with two independent points, V_p Sha = 0. No such proof is printed; (5.6) itself assumes (ii).
- Identity in Sel without Sha: (5.6) and the Cor 5.1 formula hold IN Sel(Q,V_pE) (x) L for a basis (P,Q) of Sel, under (ii) alone
  (h^{(rho)} alternating for even rho, non-degenerate on S^{(rho)} = S). Reading (P,Q) as rational points is exactly (H7).
- Therefore the next gate is not "nothing" and not a specific CH hypothesis one can supply by choice: it is the single-class
  Selmer -> Mordell–Weil statement for kappa_{alpha,alpha^{-1}} (or V_p Sha(E/Q) = 0), the H5 gap in its sharpest form. The line-IV family
  (10 sec 2(e)) lands in Sel_str (x) O[[T]] and does not change this: a Lambda-adic scalar times one fixed class needs the same upgrade.
- Consistency check with 10: line IV's Q1 is proved without H5-H7; the target point's Selmer membership is proved without H5-H7;
  everything from "Selmer" to "point" is H7. The two audits agree on where the wall is.
