# 04 — Exact remaining statement (Lane 4)

The frozen square cannot be checked as written: P_r^{tr,†} and T_r^{tr,†} are undefined, and the only explicit receptacle is
mistyped (03 §1–2). Below is a retyped square that avoids every obstruction found in 03, and the smallest statement it still needs.

## §1. Retyped objects (twisted-invariant form, Shapiro-equivalent to an MRS twist)

For σ ∈ G_{K_0}, K_0 = Q(μ_p), write n_σ := χ_cyc(σ) mod N (tame) and m_σ := <χ_cyc(σ)> ∈ 1+pZ_p.

* Output factor: J^{(1)}_r := Jac X_1(N_fp^r) over Q; Ĵ^{(1)}_r(F) := J^{(1)}_r(F) ⊗ Z_p; ordinary part via e'_ord.
* Carrier: B^bal_r (H9R16-A/B, after A_r-transport), with the central diamond action R(<n>) (factor 2 ≡ factor 3 by balance).
* Point module over F'_r := Q(μ_{Np^r}):  M_r := Hom_{Z_p}(B^bal_r, Ĵ^{(1)}_r(F'_r)^{ord}).
* Twisted action:  (σ⋆Φ)(b) := <m_σ>^{-1/2}_{(1)} <n_σ>^{-1}_{(1)} · σ( Φ( R(<n_σ>)^{-1} b ) ).
  (A group action: diamonds are over Q and commute with σ and with R.)
* Receptacle:  P^♮_r := M_r^{Gal(F'_r/K_0), ⋆}.
* Étale target:  T^♮_r := Hom_{Z_p}(B^bal_r, T_p J^{(1)}_r{}^{ord}) with the same ⋆-twist; Kum^♮_r : P^♮_r → H^1(K_0, T^♮_r) is
  descent of the F'_r-Kummer map (restriction injective, 03 §6.2).

Dimension/rank check: rank_{Z_p} T^♮_r = rank(B^bal_r)^∨ · 2g_r (no |G_r| factor); the dagger group is the factor-1 cyclic
quotient; the tame character is present. On the f ⊗ (g-branch) quotient the tame twist is ε_g^{(t)}.

## §2. Lemmas

* **L2 (twisted descent) — PROVED in 03 §2** from Hida p.15 (w^σ = <z>w), BCPV (4.1)–(4.4) and L4.2(ii), and the H9R16-A/B balance:
  Φ̄^mod_r ∈ P^♮_r. Standing input: BCPV's W_{Np^r} and W_{N_gp^r} obey W^σ = <z>∘W. Any other normalization by a Q-rational
  diamond only changes the exponents, not the conclusion. Lane 1 must confirm the literal normalization, and the common-level
  (N) to native-level (N_g) push-down in step 1.
* **L1 (functoriality of twisted invariants) — formal:** a K_0-rational homomorphism commuting with the diamond actions and
  the ⋆-twists maps P^♮_{r+1} to P^♮_r. (In MRS language this is the change-of-rings statement NOT printed in MRS §1–2. In the
  invariant form it is immediate.)
* **L3 (injectivity) — PROVED (03 §6):** Kum^♮_r is injective, including after ⊗Q_p.

## §3. The tower relation, correctly typed

Φ̄_r ∈ Hom(B^bal_r, ·) is contravariant in the carrier, and the Hecke restriction goes B^bal_{r+1} → B^bal_r. So "τ^MW_r: P_{r+1} → P_r"
is not a map of the Hom-modules. The typed relation lives in the common object Hom_{Z_p}(B^bal_{r+1}, Ĵ^{(1)}_r(F'_{r+1})^{ord}):

    (T♮_r)   ϖ^{(1)}_{1,*} ∘ (U'_p)^{-(r+1)} ∘ Φ̄^mod_{r+1}  =  δ♮_r · (U'_p)^{-r} ∘ Φ̄^mod_r ∘ res^bal_{r+1,r},

where δ♮_r is a Q-rational diamond unit (03 §9) to be fixed by Lanes 1–2. The Kummer square becomes: both sides of (T♮_r) have the
same image in Hom(B^bal_{r+1}, H^1(K_0, T_pJ^{(1),ord}_r)^{⋆}). By L3 that equality is equivalent to (T♮_r).

## §4. FIRST EXACT UNPROVED STATEMENT (smallest lemma this lane could isolate)

Two operator-level inputs imply (T♮_r). Given BCPV Cor 4.11, which gives the TRIPLE tower ϖ^{⊗3}_{1,*}Δ^ord_{r+1} = U'^{⊗3}_pΔ^ord_r:

**(K_r) finite operator-level Kummer realization (NOT_PRINTED, formal):**
    Kum_{F'_r} ∘ Φ̄^mod_r = Contr^mod_r ∘ cl_1(Δ^ord_r)   in Hom_{Z_p}(B^bal_r, H^1(F'_r, T_pJ^{(1),ord}_r)),
with Contr^mod_r the étale contraction by the pairing <·, A_r ·> on factors 2,3 and the f-projection on factor 1.
Proof route: étale Abel–Jacobi functoriality under correspondences, plus continuity for e'_ord.

**(★_r) modified-pairing / degeneracy compatibility at operator level (NEW LEMMA REQUIRED — not printed in BCPV, DR22 or Hida):**
on e'_ord H^1_et(X̄_1(N_gp^{r+1}), Z_p(1)), with <,>_r the Poincaré pairing of X_1(N_gp^r),

    ϖ_1^* ∘ W_{N_gp^r}^{-1} ∘ (U'_p)^r ∘ ϖ_{1,*}  =  u_r · W_{N_gp^{r+1}}^{-1} ∘ (U'_p)^{r+1}     (as maps into e_ord H^1),

for an explicit u_r ∈ Z_p[diamonds] (possibly times a power of p). By BCPV L4.10's proof (W interchanges ϖ_1 and ϖ_2), (★_r)
reduces to ϖ_2^*(U'_p)^r ϖ_{1,*} = u_r (U'_p)^{r+1} on the ordinary part, a U-isomorphism identity of the kind in Hida (6.4)
(π^r_s∘π^*_{r,s} = p^{s−r}U(p^{s−r})). There a power of p DOES appear, and it must be matched against the group-ring projection
constant of DR22 L2.8 (none) and against the corrected (4.9) (average over the kernel, 03 §3).
**If a p-power survives unmatched, the integral tower fails and only the Q_p-linear tower survives.**

(★_r) with (K_{r+1}), (K_r), Cor 4.11 and L2 give (T♮_r) with δ♮_r = u_r (times the Lane-1 discrepancy).

## §5. Sufficient conditions on {δ_r} (from 03 §9)

1. δ_r ∈ (Z_p[(Z/Np^r)^×])^× (diamond units), each defined over Q.
2. ϖ_{1,*}∘δ_{r+1} = u'_r·δ_r∘ϖ_{1,*} with u'_r a diamond unit; renormalize P_r by Π_{j<r} u'_j.
3. δ_r contains no single W/w, no level-mixing W_{N/N_g}, and no pseudo-eigenvalue or Gauss-sum scalar.
Under 1–3 the dagger/tame descent of L2 is unchanged and (T♮_r) is insensitive to δ.
