# T1 — D5 Steps 2-3: Col(loc_3 z_gamma) = L_3 exactly.  VERDICT: PASS_WITH_CORRECTIONS (wording/citation; bound unchanged)

## 1. Interpolation for any norm-compatible c (re-derived from Kobayashi sec. 3)
THEOREM (Kob l.266): "(x, z)_{E,n} = Tr_{k_n/Q_p} log_E^(x) exp*_{omega_E,n}(z)" for x in E^(m_n).
DERIVED (Kob l.277-284 redone): (c_n^s, z) = sum_t t(log c_n^s . exp* z) = sum_t log(c_n^{ts}) exp*(z^t), so
  chi(Col_n z) = sum_s sum_t log(c_n^{ts}) exp*(z^t) chi(s) = [sum_r log(c_n^r) chi(r)] . [sum_t exp*(z^t) chi(t)^{-1}].
Uses only Galois-equivariance of log, exp* and Tr = sum over Gamma_n; valid for every norm-compatible c. Also
DERIVED: Col_n(t z) = t Col_n(z) (invariance of the cup-product pairing), so Col is Lambda-linear for the Galois action.

## 2. The alpha-factor (D1.1(c)) — DERIVED + COMPUTED
chi of conductor p^{n+1}, trivial on Delta: C and S_m (m <= n) are fixed by Gal(k_n/k_{m-1}), where chi is non-trivial,
so their chi-sums vanish; the m = n+1 term has p^0 and gives alpha^{-(n+1)} (tau(chi) - (p-1) sum chi) = alpha^{-(n+1)} tau(chi).
Exact PARI check (checks/ksr12.log): n = 1 (2 characters) and n = 2 (6 of conductor 27, 2 of conductor 9), alpha = -1:
all differences 0; control alpha^{-n} fails on every conductor-3^{n+1} character. Trivial character: Tr L_n = L_0 = 3/2.

## 3. The chi <-> chi^{-1} question — each identification stated
- Col side: Lambda = Z_3[[Gamma]]; a character chi of Gamma acts by sigma -> chi(sigma); gamma -> 1+T sends chi to T = chi(gamma)-1.
- THEOREM (Kato 12.5(1), rendered p.221): "x (x) y -> sum_{sigma in G_n} chi(sigma) sigma(y) per_f(x)^+-, where chi is any
  character G_n -> C^x and +- = (-1)^{k-r-1} chi(-1), sends the image of z_gamma^(p) to (2 pi i)^{k-r-1} L_{p}(f*,chi,r) gamma^+-."
  Applied to chi^{-1} (k = 2, r = 1; chi^{-1} even so the + part): sum_t exp*_{omega}(z^t) chi(t)^{-1} = L_{p}(E,chi^{-1},1)/Omega_+.
- DERIVED: chi(Col(loc z_gamma)) = alpha^{-(n+1)} tau(chi) L(E,chi^{-1},1)/Omega_+   (chi of conductor 3^{n+1}, n >= 1).
- THEOREM (SW sec. 3, (3.1) and 3.2, read at source): L_alpha(E,T) = int (1+T)^{log<x>/log kappa(gamma)} d mu_alpha, and for chi with
  chi(gamma) = zeta of order p^n: "L_alpha(E, zeta - 1) = (1/alpha^{n+1}) . (p^{n+1}/G(chi^{-1})) . L(E,chi^{-1},1)/Omega_E".
  So SW uses the SAME identification (gamma -> 1+T, sigma -> chi(sigma), Galois <-> Z_p^x by kappa). Since
  G(chi) G(chi^{-1}) = chi(-1) p^{n+1} (checked: 27 for n = 2) and chi(-1) = 1: SW value = alpha^{-(n+1)} tau(chi) L(E,chi^{-1},1)/Omega_E.
- Result: the two sides agree character by character up to the constant unit Omega_E/Omega_+ in {1, 2}. There is NO
  mismatch, and in particular no involution T -> (1+T)^{-1} - 1 is needed.
- THEOREM (Kato 16.2(i), p.269): "L_{p-adic,alpha}(f)(kappa^r chi^{-1}) = (r-1)! p^{nr} alpha^{-n} G(chi,zeta_{p^n})^{-1}
  (2 pi i)^{k-r-1} (1/Omega_+-) L_{p}(f,chi,r)". At r = 1 with chi -> chi^{-1}: L_Kato(kappa chi) = SW value at chi (x Omega_E/Omega_+).
  So Kato's element is the SW series with its argument shifted by kappa (the Tate twist: Kato 16.6 uses z_gamma(f*)(k),
  k = 2, i.e. V_3E(1)); again no involution. The kappa-shift is a Lambda-automorphism that R25's T = T_3E never sees.

## 4. Corrections (none changes the bound)
C1. Kobayashi's printed l.301-304 ("sum exp*((z^Kato)^sigma) chi(sigma)^{-1} = e_p(chi) L(E,chi,1)/Omega^+_E") and l.320-322
    ("chi o L_{p,gamma}(E,X) = tau(chi) L(E,chi,1)/Omega^+_E") both carry chi where Kato 12.5(1) and SW literally give chi^{-1}
    (or he uses the geometric Dirichlet convention for L-values but sigma -> zeta^sigma for tau). The two slips cancel, so his
    conclusion and R25's identity stand. R25 RETURN INPUT 4 ("inherited from Kobayashi's printed split identity") should be
    replaced by the literal computation in section 3.
C2. D5 Step 3 writes Col(loc z_gamma) = L_{3-adic,-1,omega_E,gamma}; for Kato's own element this holds as psi -> L_Kato(kappa psi).
    R25's primary proof compares with SW-normalised values, which is the right object; the shift should be stated.
C3. D7 item 1 ("chi <-> chi^{-1} being the standard identification") is muddled; section 3 is the precise statement.

## 5. Uniqueness (Zariski density) — DERIVED
The nontrivial finite-order characters of Gamma give the points zeta - 1 (zeta in mu_{3^inf}, zeta != 1): infinitely many
points of the open unit disc. Col(loc z_gamma) and L_3 lie in Lambda (x) Q_3 (in fact Lambda: loc z_gamma in H^1_Iw(T) by
Kato 12.5(4) first assertion, Z(f,T) in H^1(T)); a nonzero element of Z_3[[T]] (x) Q_3 has finitely many zeros in the open
disc (Weierstrass preparation). So agreement at all nontrivial characters already forces equality; the trivial character
is an extra consistency check (K-SR1: both sides 2 L(E,1)/Omega_+). "Finitely many zeros" is enough here.
Kato Remark 16.3(1) (h = 1, one r) gives the same uniqueness inside H_1.
## 6. What I did NOT re-derive: the existence/integrality of c_n (D1.2, D2) — only log c_n = L_n enters Steps 2-3.
