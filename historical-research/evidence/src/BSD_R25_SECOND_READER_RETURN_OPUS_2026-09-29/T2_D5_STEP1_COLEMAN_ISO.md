# T2 — D5 Step 1: Col is an isomorphism H^1_Iw(T)/H^1_Iw(T^0) → Lambda (cokernel 0).   VERDICT: PASS

Setting (SEED_DATA_v2, not re-derived): T = T_3E, T^0 = T_3E^ ≅ Z_3(1)⊗eta, T/T^0 ≅ Z_3(eta), eta unramified quadratic;
k_n = n-th layer of the cyclotomic Z_3-extension of Q_3 (totally ramified, [k_n:Q_3] = 3^n, zeta_3 ∉ k_n).
SECONDARY (textbook, used as stated): Tate local duality and Euler characteristic; Serre, Local Fields IX (Thm 7, 8).

## (a) H^0 and H^2 vanish (DERIVED)
- H^0(k_n, Z_3(eta)) = 0 and H^0(k_n, Q_3/Z_3(eta)) = 0: eta|G_{k_n} is non-trivial (k_n/Q_3 totally ramified, eta
  unramified non-trivial), and x = -x in Q_3/Z_3 forces x = 0.
- H^0(k_n, mu_{3^inf}⊗eta) = 0: on mu_3 the character is omega·eta (omega = mod-3 cyclotomic, ramified quadratic,
  non-trivial on G_{k_n} since zeta_3 ∉ k_n; eta unramified); omega·eta ≠ 1 on G_{k_n}, so already the 3-torsion is 0.
- Duality: H^2(k_n,T^0)^v = H^0(k_n, Q_3/Z_3(eta)) = 0; H^2(k_n,Z_3(eta))^v = H^0(k_n, mu_{3^inf}⊗eta) = 0. R25 (a) holds,
  and also for T itself: H^0(Q_3(mu_{3^inf}), E[3^inf]) = 0, because over Q_3(mu_{3^inf}) kappa is trivial and eta is
  non-trivial (totally ramified tower), so both graded pieces become Q_3/Z_3(eta), which has no invariants.
## (b) Freeness, ranks, perfect pairing (DERIVED from Euler characteristic + duality)
rank H^1(k_n,M) = 3^n for M = T^0, Z_3(eta); torsion(H^1(k_n,M)) = H^0(k_n, M⊗Q/Z) = 0 by (a). From
0 → Z_3(eta) → Q_3(eta) → Q_3/Z_3(eta) → 0 and H^2(Z_3(eta)) = 0: H^1(Q_3/Z_3(eta)) = H^1(Z_3(eta))⊗Q_3/Z_3, so Tate duality
H^1(T^0) ≅ H^1(Q_3/Z_3(eta))^v = Hom(H^1(Z_3(eta)), Z_3): perfect Z_3-pairing of free modules. Hom(T^0, Z_3(1)) = T/T^0 (eta^2 = 1),
and the pairing is the one induced by the Weil pairing (T^0 is isotropic, T^0 ⊗ T/T^0 → Z_3(1) perfect).
## (c) Kummer map Ê(m_n) → H^1(k_n,T^0) is an isomorphism (DERIVED)
Lim over 3^m of 0 → Ê(m_n)/3^m → H^1(k_n,Ê[3^m]) → H^1(k_n,Ê(m-bar))[3^m] → 0 (Mittag-Leffler) gives
0 → Ê(m_n) → H^1(k_n,T^0) → T_3 H^1(k_n,Ê(m-bar)) → 0. Ê(m_n) is Z_3-free (torsion = H^0(k_n, mu_{3^inf}⊗eta) = 0) of rank
3^n (log: Ê(m_n)⊗Q ≅ k_n). So the cokernel is finitely generated, of rank 3^n - 3^n = 0 (finite), and torsion-free (a
Tate module): it is 0. Onto: YES. Into H^1(k_n,T): injective since H^0(k_n,T/T^0) = 0.
## (d) Z_3[Gamma_n]-freeness (DERIVED; Serre IX Thm 7–8 SECONDARY)
M := H^1(k_n,T^0). Corestriction to k_{n'} is onto: by Shapiro its cokernel sits in H^2(k_{n'}, T^0⊗I) (I the augmentation
ideal), whose dual is H^0(k_{n'}, Q_3/Z_3(eta)⊗I^*) ⊂ H^0(k_n, ·) = 0. For H = Gal(k_n/k_{n'}): M^H = res H^1(k_{n'},T^0)
(inflation–restriction, H^0 = 0), N_H M = res(cor M) = M^H, so Ĥ^0(H,M) = 0. M⊗Q ≅ k_n ≅ Q_3[Gamma_n] (normal basis), so the
Herbrand quotient is 1 and H^1(H,M) = 0. Gamma_n is a cyclic 3-group: two consecutive vanishing degrees ⇒ cohomologically
trivial (Serre IX Thm 8); Z_3-free + c.t. ⇒ projective ⇒ free (Z_3[Gamma_n] local) of rank 3^n/3^n = 1.
By Nakayama, c_n generates M ⟺ its image generates M_{Gamma_n} ≅ M^{Gamma_n} (norm, M free) ⟺ res(cor c_n) = res(c_0)
generates res H^1(k_0,T^0) ⟺ c_0 generates Ê(3Z_3) (res injective). R25 (d) holds.
## (e) c_0 generates Ê(3Z_3); log c_0 = +3/2 (DERIVED)
- log_Ê(t) = sum c_m t^m/m with c_m ∈ Z_3 (integral minimal model, Néron omega_E). For v_3(t) ≥ 1: v_3(t^m/m) ≥ m - v_3(m) ≥ 2
  for m ≥ 2, so log_Ê ≡ t (mod t·3) is an isometry Ê(3Z_3) → 3Z_3, inverse exp_Ê converging on v_3 > 1/2. So
  Ê(3Z_3) ≅ 3Z_3 via log, and x generates ⟺ v_3(log x) = 1.
- c_0 = theta(y_0) ∈ Ê(3Z_3): theta^phi = theta∘[-1] and phi(y_0) = y_0^{-1} give phi(c_0) = c_0; theta is an isomorphism of
  formal groups over O = Z_9 (Tate uniformisation over Z_9 composed with an O-isomorphism of minimal models), so
  lambda = theta'(0) ∈ O^x and b = lambda^{-1} ∈ O^x, phi(b) = -b.
- log y_0 = (-1)^{0+1} b h(zeta_3 - 1) = -b(3/2 + (zeta_3 + zeta_3^{-1} - 2)) = -b(3/2 - 3) = (3/2) b; log_Ê c_0 = lambda·(3/2)b = +3/2.
  v_3 = 1: c_0 is a generator. The sign is +, consistent with the exact trivial-character value in T1(5).
- Conclusion: {c_n^sigma} is a Z_3-basis of H^1(k_n,T^0); with (b), Col_n: H^1(k_n,Z_3(eta)) → Z_3[Gamma_n] is an
  isomorphism (dual basis); H^1_Iw(T)/H^1_Iw(T^0) = H^1_Iw(Z_3(eta)) (H^2_Iw(T^0) = 0, H^0(T/T^0) = 0); the limit is an
  isomorphism onto Lambda. Cokernel 0: CONFIRMED.
## Hostile notes (none changes the verdict)
- The integrality of c_n (D2, Dwork) is used only through c_n ∈ Ê(m_n); T5 re-checks D2.1 by hand.
- The literal Kob d_n ≠ d_n' by zeta_{p^{n+1}} (R25 REMARK) is irrelevant here: only log values enter.
