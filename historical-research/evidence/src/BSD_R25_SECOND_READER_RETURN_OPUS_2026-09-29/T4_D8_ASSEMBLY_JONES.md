# T4 — D8 steps 4–6 and Jones 1989.   VERDICT: PASS (the O5 input is corroborated by an independent PARI value, SECONDARY)

Jones PDF: printed page = 28 - pdf page (checked: printed 17 = pdf 11, printed 18 = pdf 10).
## THEOREM (Jones 1989, author copy, read on rendered pages)
- p.1: "Let p ≠ 2 be a prime number and let K be a number field." p.2: "we write a ≈ b if a/b is a unit";
  "If L is the cyclotomic extension, then log_p is Iwasawa's logarithm."
- p.3 standing hypotheses: "1. Sha_{p^inf}(K) is finite; 2. every prime of K for which A has bad reduction splits finitely in L;
  3. the reduction of A is semi-stable at every place of K dividing p, and is an extension of an ordinary abelian variety by
  a torus for every t ∈ T; 4. for every place t ∈ T, the universal norms of A(L_t) are of finite index in A(K_t)", and (4)
  "is known to hold ... A is an elliptic curve with non-split multiplicative reduction at v (see [11])".
- p.5: F_M^{(m)}(0) := (1/m!) d^m/dT^m F_M(T)|_{T=0} "up to a p-adic unit" (normalised leading coefficient).
- p.6: S_∞ := Image H^1(O_L, A^0_{p^inf}) → H^1(O_L - T, A^0_{p^inf}); "They are quasi-isomorphic to the classical p-Selmer
  group of A over K and L respectively (see [6])." Also: "Since we assume that the p-primary component of Sha_K is finite".
- p.16 (end of §2): ker g / cok g = ℒ(A)/(log_p κ(γ))^{r+e} · det<,>_p Sha_K / (A_{p^inf}(K) Ã_{p^inf}(K)) · prod_{l∤∞} m_l;
  p.13: "m_l denotes the number of connected components in the fiber of A over l".
- p.17: 0 → S_∞ → H → (Q_p/Z_p)^e → 0, f_H(t) = (t-1)^e f_S(t), L_H(s) := f_H(κ(γ)^{1-s}); Theorem 3.1: ρ ≥ r + e;
  "If <,>_p is non-degenerate, then ρ = r + e and L_H^{(ρ)}(1) ≈ ℒ(A) det<,>_p Sha_K/(A^fin(K) Ã^fin(K)) prod m_l."
- p.18 proof: "L_H^{(ρ)}(1) = (-log_p κ(γ))^ρ f_S^{(r)}(1)"; nonsplit form: "If A is the Néron model of an elliptic curve with
  non-split multiplicative reduction at p, then ρ ≥ r. Furthermore, if <,>_p is non-degenerate, then ρ = r and
  L_H^{(ρ)}(1) ≈ det<,>_p Sha_K/(A_{p^inf}(K) Ã_{p^inf}(K)) prod_{l∤∞} m_l."
## DERIVED: what this gives in L_3's variable
e = 0 (nonsplit), so H = S_∞ (classical Selmer up to quasi-isomorphism: same characteristic ideal). With T = t - 1:
g(0) = leading T^r-coefficient of f_S ≈ det<,>_p/(log_p κ(γ))^r · #Sha[3^inf] · prod m_l / #E(Q)[3^inf]^2.
So Reg_γ := det<,>_p/(log_p κ(γ))^2 is the γ-normalised regulator, and the (log_p κ(γ))^{-r} factor is CONFIRMED (p.16, p.18).
v_3(log_3 κ(γ)) = 1 for every topological generator (κ(γ) ∈ 1+3Z_3 \ 1+9Z_3), so v_3(Reg_γ) = v_3(det<,>_3) - 2.
Seed values: m_l = 2 (l=3, I_2), 1 (2243, I_1), 2 (4547, III), 2 (5843, I_2), 4 or 2 (l=2, I_1*): all prime to 3 whether
m_l is read geometrically or rationally; E(Q)_tors = Z/2, Ã = E: no 3. Standing hypotheses: 1 from Ka Thm 18.4 (p.281: corank Sel ≤
ord_{s=1} L_{p-adic,α} when α ≠ 1) with ord = 2 = rank, or directly from T-INT (below); 2 (cyclotomic); 3 (multiplicative =
torus); 4 (quoted nonsplit case). ORDER OF INFERENCE: finiteness must precede Jones; it does (R25 D8 step 4 remark).
## Step 4 (control, ord_T f_E ≥ 2): CONFIRMED
ker(Sel(E/Q) → Sel(E/Q_∞)^Γ) ⊂ H^1(Γ, E(Q_∞)[3^inf]) = 0 as E(Q(mu_{3^inf}))[3] = 0 (SL_2(Z_3) ⊂ image fixes no vector).
So corank Sel(E/Q_∞)^Γ ≥ 2, i.e. rank_{Z_3} X/TX ≥ 2. For torsion X ~ ⊕ Λ/(f_i): rank X/TX = #{i : T | f_i} ≤ ord_T char(X)
(pseudo-isomorphism changes X/TX by finite groups). Only the injective half of control is used.
## Step 5 (a_1 = 0 forced, v_3(g(0)) ≤ 2): CONFIRMED
T^2 | f_E | L_3 ⇒ T^2 | L_3, so a_0 = a_1 = 0 without any analytic input on a_1 (a_0 = 2L(E,1)/Ω_+ = 0 is consistent).
L_3 = T^2 h, f_E = T^2 g, and L_3 = f_E u' ⇒ h = g u' (Λ a domain) ⇒ g(0) | h(0) = a_2 in Z_3; a_2 ≠ 0 ⇒ ord_T f_E = 2 and
v_3(g(0)) ≤ v_3(a_2) = 2. Needs a_2 in the SAME variable as f_E: O4/D7's changes (unit multiples, T ↦ (1+T)^v - 1, the
involution) multiply a_2 by units only (T1, D7 items 5–6). Also finiteness again: corank Sel(E/Q) ≤ 2 = rank.
Jones's non-degeneracy hypothesis: supplied by Reg ≠ 0 (input); ρ = r = 2 is then also Jones's conclusion.
## Step 6–8 against O5 (v_3(Reg_γ) = 0): INPUT, corroborated (SECONDARY, COMPUTED here, checks/reg.gp, reg2.gp, reg.log)
PARI 2.17.3 ellpadicregulator(E,3,n,[P1,P2]) on the minimal model — manual: "the determinant of the Gram matrix ... with
respect to the 'canonical' cyclotomic p-adic height", log_p-valued (f = log_p(den x) - 2 log_p σ(P)), canonical case
stated for "non split multiplicative reduction": Reg_3 = 3^2 + 3^4 + 2·3^5 + ... (n = 8, 11, 14 agree), v_3 = 2.
[P1,P2] is 3-saturated (ellsaturation: index^2 = 1.000). Hence v_3(Reg_γ) = 2 - 2 = 0, matching D8 step 7. Route C
(K-SR3: certificate value belonging to det<,>_p instead of Reg_γ, bound ≤ 81) is EXCLUDED at this grade: det<,>_3 has
v_3 = 2, not 0. [Caveat: PARI's height and Jones's <,>_p agree up to a unit (factor 2 normalisation, sign) — SECONDARY.]
Then v_3(#Sha[3^inf]) = v_3(g(0)) - v_3(Reg_γ) ≤ 2: #Sha[3^inf] ≤ 9; with B2 (order-9 subgroup Sha[3] ⊇ (Z/3)^2):
Sha[3^inf] = (Z/3)^2. No Cassels–Tate needed; no Skinner, no SU, no GRH used in steps 1–9.
## Note on the Δ-branch (checked, no correction)
Ka 12.5(1): z_{ι(γ)} = -σ_{-1}(z_γ) puts z_{γ^+} in the σ_{-1} = -1 part of H^1(V(f)); the ζ-twist to H^1(V(f)(1)) = H^1(V_3E)
flips the sign (κ(σ_{-1}) = -1), so z_{γ^+} spans the Δ-trivial branch used by Col — consistent with ± = χ(-1) in 12.5(1).
