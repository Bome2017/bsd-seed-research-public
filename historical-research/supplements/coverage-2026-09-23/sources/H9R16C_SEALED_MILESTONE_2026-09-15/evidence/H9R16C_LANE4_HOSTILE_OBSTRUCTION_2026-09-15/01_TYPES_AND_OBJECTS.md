# 01 — Types and objects (Lane 4, hostile review of H9R16-C)

Date: 2026-09-15. Every object is typed. "[src]" points to 02_PRIMARY_SOURCE_LEDGER.md.
Frozen inputs taken as given (not re-derived): H9R15 (closed locally), H9R16-A/B (closed). Nothing downstream of
H9R16-A/B is assumed.

## 1. Fields and Galois groups

| Symbol | Type | Note |
|---|---|---|
| p | odd prime | BCPV §1.1.1 |
| N_f, N_g | tame levels; N := lcm(N_f,N_g) | BCPV §1.1.5; diagonal cycle lives at common level N |
| F_r := Q(μ_{p^r}) | number field | field of definition of Δ_r[d] [BCPV p.18; DR22 L2.1] |
| F'_r := Q(μ_{N p^r}) | number field | field of definition of W_{Np^r}, W_{N_g p^r} [Hida p.15; BCPV (1.6)] |
| K_0 := Q(μ_p) | fixed base proposed by H9R16-C | |
| χ_cyc : G_Q → Z_p^×, and z_σ := χ_cyc-type value of σ in (Z/Np^r)^× | | tame part n_σ := z_σ mod N, p-part m_σ := z_σ mod p^r |

## 2. Curves, models, maps

| Symbol | Type | Source |
|---|---|---|
| X_1(Mp^r) (BCPV/DR22) | curve over Q, moduli (A,P), P of order Mp^r | BCPV p.18; DR22 p.7 |
| X_r (Hida) | curve over Q, moduli (E, φ: μ_{Np^r} ↪ E) — a DIFFERENT moduli model | Hida control p.1 |
| <a> | automorphism over Q: (A,P) ↦ (A,aP) | DR22 (1.13) |
| ϖ_1 : X_1(Np^{r+1}) → X_1(Np^r) | (A,P) ↦ (A,pP), over Q | BCPV p.18, DR22 (1.14) |
| ϖ_2 | (A,P) ↦ (A/<p^rP>, P+<p^rP>), over Q | DR22 p.8 |
| W_{Np^r} (BCPV) | automorphism of X_1(Np^r) defined over F'_r, NOT over Q | BCPV (1.6) target Z_p[Δ_{Np^r}], L4.2(ii) |
| w_r (Hida) | automorphism of X_r defined over Q[μ_{Np^r}]; w_r^σ = <z>∘w_r = w_r∘<z>^{-1} | Hida p.15 |
| π^r_s := w_r ∘ π_{s,r,*} ∘ w_s | homomorphism J_s → J_r defined over Q | Hida p.15 |
| π_{s,r,*} | untwisted Albanese pushforward, over Q | Hida p.14 |

## 3. Hecke/idempotents

| Symbol | Type | Source |
|---|---|---|
| U_p, U'_p | correspondences over Q; W intertwines U'_p and U_p | BCPV (1.8)–(1.9) citing [Oht99, 1.5.4] |
| U_p^* := π_{1*}π_2^* | compatible with the untwisted ϖ_{1*} tower | DR22 p.8 |
| U(p), U*(p) | Hida; w_r∘T(n) = T*(n)∘w_r | Hida p.15 |
| e'_ord := lim (U'_p)^{n!} | idempotent on p-adically completed Chow/étale groups | BCPV p.5, p.19 |
| e = lim U(p)^{n!}, e* = lim U*(p)^{n!} | idempotents on Ĵ_r(k) | Hida p.13–14 |
| A_r := W_{N_g p^r}^{-1} (U'_p)^r | FROZEN (H9R16-A/B); acts on the THIRD factor only; defined over F'_r, not over Q | |

## 4. Cycles, classes, dagger modules

| Symbol | Type | Source |
|---|---|---|
| G~_r := ((Z/p^r)^×)^3, G_r := p-Sylow of G~_r ≅ (Z/p^{r−1})^3 | abstract group acting by triple diamonds | BCPV p.18, p.20 |
| Δ_r[d] ⊂ X_1(Np^r)^3 | cycle over F_r; (4.1) diamonds reindex, (4.2) σ_mΔ_r[d] = Δ_r[md] | BCPV p.18 |
| Δ^ord_r[d] := (e'_ord W_{Np^r})^{⊗3} Δ_r[d] | element of CH^2(X_1(Np^r)^3; F_r)_{Z_p}; L4.2(ii): σ_mΔ^ord_r[d] = Δ^ord_r[m^{-1}d] | BCPV (4.4) |
| Z_p[G_r]^† | free rank-one Z_p[G_r]-module, G_Q acting via <χ>_r^{-1/2} | BCPV Def 4.6 |
| M^† := M ⊗_{Z_p[G_r]} Z_p[G_r]^† | **tensor over the group ring**; rank_{Z_p} M^† = rank_{Z_p} M | BCPV Def 4.6; DR22 p.19 Ω(1/2) |
| Δ^et_r[[a,b,c]] ∈ H^1(K_0, H^1_et(X̄_1(Np^r))^{⊗3}(2)^†) | class over the fixed base K_0 | BCPV L4.7 = DR22 L2.6 |
| Δ^et_r ∈ H^1(Q, H^1_et(X̄_1(Np^r))^{⊗3}(2)^†) | class over Q | BCPV Def 4.8 |
| Δ^et_∞ ∈ lim_{ϖ^{⊗3}_{1,*}} H^1(Q, e'_ord H^1(Y_1(Np^r))^{⊗3}(2)^†) | normalized by (U'^{⊗3}_p)^{-r} | BCPV Def 4.12 |

## 5. MRS twists (two inequivalent types)

For O a commutative ring, I a free O-module with a continuous G_k-action, V ∈ CAG_O(k) [MRS p.2]:

| Type | Object | dim | Tate module [MRS Thm 2.2(iii)] | Transition functoriality |
|---|---|---|---|---|
| (Z) — the last EXPLICIT definition in the checkpoint (H9R8 l.750–753, H9R12 l.939) | A_r^{†,Z} := I_r^† ⊗_Z J_r over K_0, I_r^† = Z[G_r] | \|G_r\|·dim J_r [MRS Thm 2.1] | Z_p[G_r]^† ⊗_{Z_p} T_pJ_r | MRS Thm 1.8 with O=Z: any K_0-homomorphism J_{r+1}→J_r |
| (G) — BCPV-type | A_r^{†,G} := I_r^† ⊗_{Z[G'_r]} V_r, with Z[G'_r] acting on V_r by diamonds defined over K_0 | rank_O(I)·dim V_r | I_r^† ⊗_{Z[G'_r]} T_pV_r = (T_pV_r)^† | O changes with r: needs a change-of-rings statement NOT printed in MRS §1–2 |

## 6. The finite modified point (frozen by H9R16-A/B) and its carrier

* B^bal_r := (T^{(2),ord}_r ⊗_{Z_p} T^{(3),ord}_r) / < (t_2u')⊗t_3 − t_2⊗u't_3 >  — a Z_p-module QUOTIENT (after A_r transport).
* Φ^mod_r(t_2,t_3) := Π_{Z,*}((1 ⊗ t_2 ⊗ A_r t_3) Δ^ord_r)  ∈ Ĵ_r^{(1)}(F'_r) := J_{X_1(N_f p^r)}(F'_r) ⊗ Z_p (after the
  degree-zero correction), with the tame push-down N → N_f, N_g applied factorwise as in BCPV Def 4.13.
* Φ̄^mod_r : B^bal_r → Ĵ_r^{(1)}(F'_r), a Z_p-linear map (H9R16-A/B).
* Π_Z := X_14 × Z, Z = X_23 the diagonal: PLAIN diagonal correspondence, over Q [BCPV fn 11, p.26].

## 7. The square as frozen (symbols the checkpoint leaves undefined)

    P_{r+1}^{tr,†} --Kum--> H^1(K_0, T_{r+1}^{tr,†})
         | τ^MW_r                  | τ^et_r
         v                         v
    P_r^{tr,†}     --Kum--> H^1(K_0, T_r^{tr,†})

The checkpoint never defines P_r^{tr,†} or T_r^{tr,†}; its only explicit receptacle is type (Z) of §5.
03 shows: (i) type (Z) does not have BCPV's Tate module; (ii) neither (Z) nor a dagger-only (G) twist contains the
coefficient-retaining finite modified point when the tame nebentype ε_g^{(t)} ≠ 1. Retyped objects are in 04.
