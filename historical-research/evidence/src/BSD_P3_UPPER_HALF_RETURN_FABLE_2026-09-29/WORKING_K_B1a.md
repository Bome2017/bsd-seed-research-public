# WORKING K-B1a — Kato's hypotheses for f_m at p = 3
Source fetched: numdam.org/article/AST_2004__295__117_0.pdf -> sources/Kato2004_AST295.pdf (hash in
sources/KATO_SOURCE.sha256); text by pdftotext -layout -> sources/Kato2004_AST295.txt ("Ka", OCR noisy).

## Kato Thm 17.4 (Ka l.8265-8280, OCR repaired; Greek restored by hand)
Assume f has good ordinary reduction at lambda (Prop 17.1 (i): p ∤ N and a_p in O_lambda^x; Ka l.8218-8219).
Let T be a Gal-stable O_lambda-lattice of V(f). X(T) = dual of lim Sel(Q(zeta_p^n), T(r))(-r) (Ka l.8256-8263).
 (1) X(T) is a torsion Lambda-module.
 (2) alpha as in 17.1, omega != 0 in S(f*), gamma in V(f*) with gamma^+ != 0, gamma^- != 0:
     L_{p-adic,alpha,omega,gamma}(f) in Lambda ⊗ Q and length_{Lambda_P} X(T)_P <= ord_P(L) for every
     height-one P NOT containing p.
 (3) alpha, omega, gamma as in (2); assume omega AND gamma are GOOD for some Gal-stable lattice (17.5);
     assume p != 2 and condition (12.5.2) of 12.5(4). Then L_{p-adic,alpha,omega,gamma}(f) in Lambda and
     length_{Lambda_P} X(T)_P <= ord_P(L) for EVERY height-one P (so also P = (p): the mu-part).
## Definitions in (3)
- 12.5.2 (Ka l.5730-5732): there is an O_lambda-basis of T for which the image of Gal(Qbar/Q(zeta_p^inf))
  -> GL(T) = GL2(O_lambda) contains SL2(Z_p).
- omega good for T (Ka l.8296-8300): image of omega under S(f) ⊗ F_lambda -> D_dR(V) -> D_dR(V'') (17.5.1)
  is an O_lambda-basis of H^0(Q_p, Zhat_p^ur ⊗ T''(k-1)), T'' = image of T in the unramified quotient.
  Weight 2, T = T_pE(-1): omega good <=> omega is a Z_p-basis of coLie(Neron model) ⊗ Z_p.
- gamma good for T (Ka l.8301-8302, ref. 14.18): gamma^+ an O_lambda-basis of T^+, gamma^- of T^-.
## Consequence for the normalization (important for K-B1b)
Kato's integral L is L_{alpha,omega,gamma} with omega normalized p-ADICALLY (integral D_dR of the
unramified quotient), not by q-expansion (a_1 = 1) and not by SU §3.3.3 canonical periods.

## Where (12.5.2) enters, checked at source (~12:20)
- Ka l.8583-8586, 8625-8640 (17.13): for height-one P containing p, 17.4(3) assumes p != 2 and (12.5.2)
  only to invoke 12.5(4) (Z(f,T) ⊆ H^1(T), length H^2 <= length H^1/Z(f,T)); then 17.11 + 16.6 + good
  omega, gamma turn Z(f,T) into Lambda_P * L_{alpha,omega,gamma}.
- Ka l.6345-6350 (13.14, proof of 12.5(4)): (12.5.2) is used for T = a*V_{O_lambda}(f) (via 12.8/14.7),
  freeness of H^1(T) (12.4: needs p != 2, T/mT irreducible; Ka l.5682-5683), then Thm 13.4(3).
- Ka l.5940-5947 Thm 13.4(3): needs sigma in Gal(Qbar/Q(zeta_p^inf)) with Coker(1-sigma: T->T) free of
  rank 1 over O, T/mT irreducible, p != 2. Also 13.4(i)-(v) (Ka l.5920-5935), (ii)-(iv) automatic in
  Example 13.3 (Ka l.5949-5951), (v) implied by the sigma of (3), (i) by Prop 13.7.
- So Skinner's replacement (Sk l.936-963) of (12.5.2) by (a) rho-bar irred + (b) such sigma is
  CONFIRMED against Kato's text: homothety of lattices by Sk Lemma 2.1.1 replaces 14.7.
## Check for f_m (level M = N/3, weight k_m > 2, k_m = 2 mod 2*3^{r_m}), p = 3
- good ordinary at 3: 3 ∤ M, a_3(f_m) in O^x (Sk (a) l.1101-1102). PASS.
- p != 2: PASS.  T/mT irreducible: rho-bar_{f_m} = rho-bar_f = GL2(F_3) (Sk (d) l.1112-1113). PASS.
- sigma: q = 2243 || M; rho-bar ramified at 2243 (seed M5: v_2243(Delta) = 1); f_m new of level M with
  trivial character, so rho_{f_m}|I_q unipotent (Carayol, Sk l.957-960); tau in I_q generating tame
  quotient has rho-bar(tau) != 1, so Coker(1-tau) = O (rank-1 nilpotent, not 0 mod m); I_q fixes
  Q(zeta_{3^inf}) (unramified at q). PASS.  f_m non-CM (Steinberg at q), so 13.4(iv)/(v) apply.
- Serre's lemma / Z_3-image: NOT NEEDED (the SL2(Z_p) condition is bypassed, not verified).
=> Image/integrality hypotheses of 17.4(3): PASS for every f_m. Conclusion obtained:
   L_{alpha,omega,gamma}(f_m) in Ch(f_m) in Lambda (all height-one P, incl. P = (p)) FOR omega, gamma
   GOOD in Kato's sense (17.5).

## The remaining hypothesis of 17.4(3): "omega and gamma good" — FAILS TO BE CHECKED (~12:24)
- Kato's integral L is L_{alpha,omega,gamma} with (omega, gamma) good for one lattice (Ka l.8273-8277).
  Scaling T -> aT scales good omega and good gamma by a, so L^good(f_m) is well defined up to O^x.
- Skinner's transfer uses L^Sigma_{f_m} of Sk (2-4-1)/(2-4-2) with SU §3.3.3 canonical periods: omega =
  q-expansion-normalized f_m (a_1 = 1), gamma^+- = basis of M(f)_(p) = H^1(Gamma_1, Sym^{k-2})[lambda_f]
  (SU author copy l.1522-1548). That is the object in the congruence (2-6-3) (Sk l.1062-1075).
- Kato 12.5(1) (Ka l.5684-5705; paraphrase): exp*(z_gamma) = (L-value / Omega(omega)) * omega, so for omega = c*f:
  L_{alpha,c f,gamma} = c^{-1} L_{alpha,f,gamma}. With gamma matched: L^can(f_m) = c_m * L^good(f_m)
  where omega_good = c_m * f_m. Hence L^can(f_m) in Ch(f_m) follows from Kato under the one-way
  sufficient condition c_m in O (a good omega has O-integral q-expansion); necessity not claimed.
- Weight 2, elliptic curve (Ka l.8298-8300): good omega = Neron differential; c = Manin constant in Z,
  so the needed direction is the integrality-of-Manin-constant direction. For f_m: weight k_m >= 8 > p = 3,
  outside the Fontaine-Laffaille range (k <= p-1); no statement comparing Kato-good omega with the
  q-expansion of f_m is in Kato (grep: no q-expansion/good comparison beyond Ka l.8298-8300), in SU
  (grep "good for", "Neron", "normaliz": none near Thm 3.5.6), or in Skinner (only weight 2, Sk l.1470).
- SU Thm 3.5.6 (SU l.2277-2279; cites "Theorem 17.14 of [Ka04]", evidently 17.4) states Kato's
  integral divisibility for the canonical L^Sigma_f with no normalization argument; SU Thm 3.6.4's proof
  (SU l.2400-2405) and hence Sk Thm 2.5.2 for f_m use it in that form.
## VERDICT K-B1a: FAIL (GAP; not refuted).
- PASS: good ordinary, p != 2, rho-bar irreducible, image condition via Skinner (a)+(b) at q = 2243
  (checked against Kato 13.14 / 13.4(3) at source). Serre's lemma is not needed.
- UNCHECKED: the 17.4(3) hypothesis "omega good" for the normalization in which Skinner's congruence
  (2-6-3) holds. Missing statement MS-B1 (exact form in RETURN.md). Stop rule: K-B1b, K-B1c NOT RUN.
