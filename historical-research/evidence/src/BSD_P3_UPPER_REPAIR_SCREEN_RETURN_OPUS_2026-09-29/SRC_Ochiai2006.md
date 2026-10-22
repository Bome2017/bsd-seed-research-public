# SRC — T. Ochiai, "On the two-variable Iwasawa main conjecture", Compositio Math. 142 (2006) 1157-1200.
# Fetched from cambridge.org (published PDF): sources/Ochiai2006_Compositio.pdf; ".txt" = "Oc l.N".
Read: §2 (Oc l.225-620), Def 2.1 + basic properties (l.296-340), §6 periods/Kitagawa/Prop 6.9
(l.2180-2330), §7 Conj 7.4, Cor 7.5 and its proof (l.2600-2730). THEOREM statements quoted below.
## Setting
- p >= 3 fixed throughout (Oc l.248). Tame level N prime to p (l.262). H^ord_F = component of Hida's
  ordinary Hecke algebra for a Lambda-adic eigenform F; H^n.o_F = H^ord_F[[Gamma]] (l.263-270).
- Condition (Ir): residual representation irreducible (l.298); implies T^ord_F free of rank 2 (l.300-302).
- Def 2.1 (l.306-316): arithmetic points of weight w; X_arith(H^ord_F)_{>=0} includes w = 0, i.e.
  weight-2 specializations f_I (l.326-330). For the seed's family (tame level M = N/3), the weight-2
  trivial-character point is f itself (3-new, a_3 = -1).
## Theorem 3 (l.553-567) + Theorem 2 (l.510-540)
Assume (Ir) and H^n.o_F ≅ O[[X1,X2]]. Suppose tau in G_{Q(mu_p^inf)} with rho(tau) = [[1, P_tau],[0,1]]
(P_tau != 0) and tau' in G_Q acting on T/MT by -1. Then for every height-one l of H^n.o_F:
  length (Sel_T^dual)_l <= ord_l(L^Ki_p(T)) + ord_l(P_tau^m)   (integral: l may contain p).
- L^Ki_p = Kitagawa's two-variable p-adic L (Thm 6.7 = [Kit94, Thm 1.1], l.2257-2270).
## Specialization (Cor 7.5 and its proof, l.2660-2730)
- Conj 7.4 uses L^MTT_p(T_I) with complex period Omega_{inf,I} = <Per(f_I), delta^B_I> (Def 6.6,
  l.2244-2255): q-expansion f_I on the de Rham side, an O-basis of H^1_{B,c}(Y_1(M'), Sym^w O) ∩ V_B^+-
  on the Betti side (canonical-type periods, Rem 6.8 l.2277-2296).
- Proof, (14) (l.2704-2709): "the p-adic period C_{p,I,b} is known to be a p-adic unit by Kitagawa's
  construction", so L^Ki mod I = unit * L^MTT(T_I). (12)-(13): Sel_I = Sel_T[I] (Prop 5.2 + Cor 7.5's
  local assumption) and char specializes (Lemma 7.2). Theorem 3 with P_tau a unit then gives, at every
  I in X_arith_{>=0}, the one-sided integral inclusion (L^MTT_p(T_I)) ⊆ char(Sel_I^dual).
  [This one-sided reading of the proof of Cor 7.5 (stated there as an equivalence of equalities) is
  mine; each step is the printed step. UNCHECKED as a written deduction.]
- Cor 7.5 extra assumptions (l.2660-2664): P_tau a unit; ((T^ord_F)^*)_{I_v}[Ker I] = 0 for all v in
  Sigma \ {p, inf}. Rem 7.6 (l.2672-2682): holds e.g. when ord_v(N) <= 1 or local monodromy at v finite.
## Seed check (p = 3)
- K-R3: p = 3 allowed: YES (l.248). Nonsplit multiplicative p allowed: YES at the weight-2 point
  (in X_arith_{>=0}; no exclusion found; split/exceptional issues do not arise for a_3 = -1).
- (Ir): YES. tau: inertia at 2243 (Steinberg at 2243 in the family; rho-bar(tau) != 1, so P_tau is a unit).
- tau': -I is in the image GL2(F_3) of rho-bar: YES (Lemma 2.6 needs p > 2: YES).
- Local assumption at v = 2243, 5843: ord_v(N) = 1: YES (Rem 7.6). At v = 2 (2^3), 4547 (4547^2):
  needs finite local monodromy (potentially good reduction) — UNCHECKED here (tiny check below).
- **H^n.o_F ≅ O[[X1,X2]], i.e. H^ord_F ≅ O[[X]]: UNCHECKED for the seed.** First unverified hypothesis.
- Black boxes at p = 3 (UNCHECKED, not read): [Kit94] Thm 1.1 incl. freeness of B^+-; [Och03] Coleman map;
  [Och05] Euler system theory. Ochiai states p >= 3 for his paper; inputs not re-read.
## Tiny check (PARI 2.17 in run040 sage-env; one process, <1 s), minimal model [0,-1,0,-66020924,-65074271436]
- N = 2^3*3*2243*4547^2*5843. v_2(j) = 4, v_4547(j) = 0 (potentially good: finite local monodromy);
  v_3(j) = -2, v_2243(j) = -1, v_5843(j) = -2; a_3 = -1, a_2243 = 1, a_5843 = -1.
- So Rem 7.6's sufficient condition holds at every v in Sigma \ {3, inf} (grade: Ochiai's REMARK, "not
  difficult to see"; Thm 3.3 not re-derived).
## Route-3 status from this source: REDUCED (see RETURN.md, MS-R3 = H^ord_F ≅ O[[X]] for the seed's branch)
- Not read (pointer only): arXiv:1706.01571 (Euler system theory over NORMAL deformation rings), which
  may weaken the regularity hypothesis. Not screened; no claim.
