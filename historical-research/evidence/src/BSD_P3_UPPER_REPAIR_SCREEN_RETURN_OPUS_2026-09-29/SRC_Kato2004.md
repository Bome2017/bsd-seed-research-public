# SRC — Kato 2004, Astérisque 295, 117-290 ("Ka" = inputs/Kato2004_AST295.txt, OCR; same bytes as B1's copy)
Read: §12.4-12.8, §13.1-13.5, §13.14, §14.1, §16.1-16.2, §16.6, §17.1-17.5, §17.11-17.13, §18.1-18.11.

## A. Thm 18.4 — THEOREM (printed), covers nonsplit multiplicative p; RATIONAL (orders only)
- Setup 18.1 (Ka l.8672-8677): any alpha in F_lambda with 1 - alpha*u | 1 - a_p u + eps(p) p^{k-1} u^2
  and ord_p(alpha) < k-1; omega != 0, gamma^+- != 0 (choices "not important").
- Thm 18.4 (Ka l.8707-8723): T any Gal-stable O-lattice of V(f)(k/2). corank_O Sel(T) <= ord_{s=k/2}
  (L_{p-adic,alpha}(f)) if alpha != p^{(k-2)/2}; <= ord - 1 if alpha = p^{(k-2)/2}. Elliptic case: E not a
  Tate curve => bound by ord_{s=1}. No restriction on p; no p ∤ N; no image condition.
- Proof (Ka l.8725-8845): 18.6 (exact sequence mod finite groups, 14.9.4, 14.12), 18.7 (via 12.5(3):
  rational, height-one primes not containing p), 18.9 (via 16.4/16.6 explicit reciprocity).
- Sel(T) = Bloch-Kato Selmer group; for an abelian variety it is the usual p^inf-Selmer group
  (Ka 14.1, l.6362-6391).
- p-adic L (16.1-16.2, Ka l.8014-8075): Amice-Velu/Vishik with alpha; for p ∥ N, eps(p) = 0 so alpha = a_p.
  Remark 18.3 (Ka l.8700-8705): the value at s = k/2 carries (1 - p^{k/2-1}/alpha); for k = 2 it vanishes
  iff alpha = 1 (Tate curve). So s = k/2 is the central point.
## A'. Seed check (p = 3): alpha = a_3 = -1, ord_3 = 0 < 1, alpha != 1 (nonsplit): PASS.
  E non-CM (multiplicative at 3), so the Euler-system input 13.4(i)-(v) (rational part (2)) applies.
  T = T_3E (V(f)(1) = V_3E: Ka 17.5 uses T_pE(-1) for V(f), l.8298-8300).
## A''. Consequence (one-way; uses retained seed inputs, no main conjecture, no Skinner/SU/Jones)
  corank_{Z_3} Sel_{3^inf}(E/Q) <= ord_{s=1} L_{3-adic,-1}(f_E) <= 2,
  the last because the coefficient a_2 != 0 (S.3 certificate: a_{4,2} = 15480, SW Prop 3.5 congruence;
  orders are normalization-free). rank E(Q) = 2 (retained, A-series) => corank Sha[3^inf] = 0 =>
  Sha(E/Q)[3^inf] FINITE. [Identification of Kato's ord_{s=1} with SW's ord_T L_3(E,T): both are the
  unique bounded interpolants with alpha = -1, equal up to a nonzero constant; twist bookkeeping read,
  standard — UNCHECKED beyond that reading.]
  This gives the finiteness half only. It does NOT give #Sha[3^inf] <= 9 (no integral statement).
## B. Integral statements in Kato vs multiplicative p (route-3 screen of §§12-17)
- 17.4(3) integral divisibility with p-adic L: good ordinary only (17.1: p ∤ N, Ka l.8218-8219). Seed: NO.
- 12.5(4) (Ka l.5727-5739) integral, general f (p | N allowed; exceptions (12.5.1) at k = 2 not
  potentially good, primes ker(kappa^{-2} chi)), but "main conjecture WITHOUT p-adic zeta functions"
  (H^2 vs H^1/Z(f,T)); image hypothesis (12.5.2) replaceable per Skinner (B1). No p-adic L attached.
- No integral Kato-direction divisibility WITH p-adic L at multiplicative p is stated in §§12-18.
