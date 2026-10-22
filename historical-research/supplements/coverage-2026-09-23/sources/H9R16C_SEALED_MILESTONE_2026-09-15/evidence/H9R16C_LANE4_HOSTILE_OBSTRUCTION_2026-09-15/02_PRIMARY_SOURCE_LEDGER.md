# 02 — Primary source ledger (Lane 4)

All items were read from page images of the PDFs in `sources/` (hashes in 06). "Match" = whether the printed hypotheses
match the H9R16-C use. Classification vocabulary: PRINTED / NOT_PRINTED / FALSE_AS_PRINTED / TYPE_MISMATCH / NEW_THEOREM_REQUIRED.

## BCPV = Büyükboduk–Casazza–Pal–de Vera-Piquero, arXiv:2409.08645v1

| Loc. | Exact content | Match for H9R16-C | Class |
|---|---|---|---|
| §1.1.5 p.4 | f,g primitive Hida families; ε_f = 1 mod N_f; ε_g = ε_g^{(t)} (tame only); N_f square-free; N = lcm(N_f,N_g) | ε_g^{(t)} may be nontrivial; in Castella–Hsieh it contains η_{K/Q} | PRINTED |
| §1.1.4 fn 2 p.3 | k_∘ = 0 for f and g (branches over the weight-0 component) | weight-one point placement is DOWNSTREAM of C; not used here | PRINTED |
| (1.5) p.5 | T_h := H^1_ord(Y_1(N_hp^∞))_{m_h} ⊗ R_h, H^1_ord := e'_ord lim H^1_et(Y_1(N_hp^r),Z_p(1)) | étale side only | PRINTED |
| (1.6) p.5 | <,>_{k,r}: x⊗y ↦ <x, W^{-1}_{N_hp^r}(U'_p)^r y>, target **Z_p[Δ_{N_hp^r}] ⊗ χ^{k+1}**, Δ_m = Gal(Q(μ_m)/Q) | the modified pairing is Galois-equivariant only with a Gal(Q(μ_{N_hp^r})/Q)-group-ring twist (tame part included) | PRINTED |
| (1.7) p.5 | T_h[k,r]⊗T_{h^c}[k,r] = T_h[k,r]⊗(T_h[k,r]⊗ε_h^{-1}) → Z_p[Δ_{p^r}]⊗χ^{k+1} | tame twist absorbed ONLY by the Galois twist h^c = h⊗ε_h^{-1} of the third factor | PRINTED |
| (1.8)–(1.9) p.6 | W intertwines U'_p and U_p, citing [Oht99, Eq. 1.5.4] | used, not re-derived (Lane 1 territory) | PRINTED (cited) |
| §4.2 p.18 | ϖ_1:(A,P)↦(A,pP); Δ_r[d] over Q(μ_{p^r}); (4.1),(4.2),(4.3) | Galois/diamond laws for the raw cycle | PRINTED |
| (4.4) p.19 | Δ^ord_r[d] := (e'_ord W_{Np^r})^{⊗3}Δ_r[d] ∈ CH^2(·;Q(μ_{p^r}))_{Z_p} | W on all three factors, common level N | PRINTED |
| L4.2(ii) p.19 | σ_mΔ^ord_r[d] = Δ^ord_r[m^{-1}d] (m prime to p), by "moduli description of the Atkin–Lehner operator" | confirms W is not Galois-invariant; tame part of σ not treated | PRINTED |
| (4.7) p.20 | packaging Σ_{d∈G_r}Δ^et_r[d2d3a,d1d3b,d1d2c]<d>, valued in Hom_{Z_p[G_r]}(S,Z_p[G_r]) ≅_G Hom_{Z_p}(S,Z_p) | group-ring-equivariant Hom ⇒ rank of S, not \|G_r\|·rank S | PRINTED |
| (4.8)–(4.9) p.21 | third vertical arrow ψ ↦ (1/p)Σ_{g'∈G_r}Σ_{pr(g)=g'} ψ_g∘ϖ_1^{*⊗3}·g' | with \|ker(G_{r+1}→G_r)\| = p^3, the printed 1/p makes (4.8) commute only up to p^2 (03 §3) | FALSE_AS_PRINTED (constant) |
| Def 4.6 p.21 | Z_p[G_r]^† via <χ>_r^{-1/2}; **M^† := M ⊗_{Z_p[G_r]} Z_p[G_r]^†** | fixes the type of T^{†}: tensor over the group ring | PRINTED |
| L4.7 p.21 (=DR22 L2.6) | Δ^et_r[[a,b,c]] is the restriction of a unique class over Q(μ_p) | fixed-base descent is restriction-type (injective), not corestriction | PRINTED |
| Def 4.8 p.22 | Δ^et_r := p^3/(p−1)^3 Σ_{a,b,c}Δ^et_r[[bc,ac,ab]] over Q | base Q ⊃ restriction to K_0 injective (p ∤ p−1) | PRINTED |
| L4.10 p.22 (=DR22 L2.5/2.4) | ϖ^{⊗3}_{1,*}Δ^ord_{r+1}[d'] = U'^{⊗3}_pΔ^ord_r[d]; proof: W "interchange ϖ_{1,*} and ϖ_{2,*}" | exact W/ϖ interchange constants are Lane 1's C1 | PRINTED (constants not shown) |
| Cor 4.11 p.22 | ϖ^{⊗3}_{1,*}Δ^et_{r+1} = U'^{⊗3}_pΔ^et_r | TRIPLE class only; no contracted/trace tower relation | PRINTED |
| Def 4.12 p.23 | Δ^et_∞ := {(U'^{⊗3}_p)^{-r}Δ^et_r} in lim_{ϖ^{⊗3}_{1,*}} H^1(Q, ·^†) | cohomological inverse limit; no points | PRINTED |
| Def 4.13–4.14 p.23 | push to native levels N_f,N_g; (1.10)∘ι*_{2,3} | A_r (native N_g) vs W_{Np^r} (common N) mixed-level | PRINTED |
| L4.15, (4.13), (4.14) p.24–25 | specialized normalizations a_p(f)^{-r}a_p(g)^{-r}λ^{-1}_{Np^r}(g) | specialized scalars; no operator-level identity | PRINTED |
| L4.18 p.24 | global cl_1 image of Δ°_r(κ,λ) = Δ^et_r(κ,λ) (specialized) | global, but for the TRIPLE class | PRINTED |
| §5.2.1 p.26 | P°_r(κ,λ) := pr_{4,*}(Z_r·pr^*_{123}Δ°_r(κ,λ)) ∈ CH^1_0(X_r)⊗F_{κ,λ} over Q(μ_{p^r}); plain diagonal Z | no W, no U'_p, specialized | PRINTED |
| (6.4), L6.1, P6.2, C6.3, R6.4 p.27–29 | Δ^tr = a_p(g)^rλ^{-1}Δ^{(P)}; comparisons only after res_p and Bloch–Kato log | no global Kummer identity for any point | NOT_PRINTED (global) |

## DR22 = Darmon–Rotger, "p-adic families of diagonal cycles", arXiv:2207.01314v1 (Astérisque 434)

| Loc. | Exact content | Match | Class |
|---|---|---|---|
| p.7 (1.13)–(1.14) | X_r=X_1(Mp^r) with (A,P); <a>(A,P)=(A,aP); ϖ_1:(A,P)↦(A,pP) | same model as BCPV | PRINTED |
| p.8 (1.16), U_p^* | H^1_et(X̄^*_∞) := lim_{ϖ_{1*}}; U_p^* := π_{1*}π_2^* compatible with the untwisted tower | untwisted pushforward ↔ starred operator | PRINTED |
| L2.2 p.17 | (2.7) diamonds, (2.8) Galois; R2.3 (2.9) | | PRINTED |
| L2.4 p.18 | (ϖ_1^3)_*Δ_{r+1}=p^3Δ_r; (ϖ_2^3)_*Δ_{r+1}=U_p^{⊗3}Δ_r; Σ_{d'↦d}Δ_{r+1}[d'] = (ϖ_1^3)^*Δ_r[d] | raw cycles, no W | PRINTED |
| p.19 | Λ(G_r)(±1/2) over Q(ζ_1); Ω(1/2) := Ω ⊗_{Λ(G_∞)} Λ(G_∞)(1/2) | group-ring tensor | PRINTED |
| (2.17) p.20 | Λ(G_r)-valued hermitian pairing; H^111(X_r) := Hom_{Λ(G_r)}(H^1(1)^{⊗3}(1/2), Λ(G_r)) | | PRINTED |
| L2.6 p.21 | descent to Q(ζ_1) via an extension class built from a Q(ζ_1)-rational cycle support (2.20)–(2.23) | fixed base Q(ζ_1) | PRINTED |
| L2.8 p.22 | p_{r+1,r}(κ_{r+1}(σ)(γ_{r+1})) = κ_r(σ)(γ_r) whenever (ϖ_1^3)_*γ_{r+1} = γ_r, all σ ∈ G_{Q(ζ_1)} | FIXED base, group-ring projection, **no constant**, no corestriction | PRINTED |
| (2.27), L2.10 p.23–24 | descent to Q lands in a δ-eigenspace: σ_mκ_∞(ω;δ) = δ(m)κ_∞(ω;δ) | character-twisted descent is the norm, not the exception | PRINTED |

## Hida, "Control of Λ-adic Mordell–Weil groups" (preprint dated 2016-02-22; in Elliptic Curves, Modular Forms and Iwasawa Theory, 2016)

| Loc. | Exact content | Match | Class |
|---|---|---|---|
| p.1 | X_r = X_1(Np^r)/Q moduli (E, φ: μ_{Np^r} ↪ E); fixed number field k; w-twisted Albanese system | model ≠ BCPV's (A,P) model | PRINTED |
| L2.1 p.5 | lim X̂(k)/p^n ↪ lim H^1(X[p^n]) (Kummer injection) | holds over any fixed number field | PRINTED |
| p.14 §5, L5.1, L5.2 | untwisted {Ĵ_s, π_{s,r,*}} carries e* (co-ordinary); π_*: Ĵ^r_s(k)^{co-ord} ≅ Ĵ_r(k)^{co-ord}; i: J~_∞^ord ≅ J~_∞^{co-ord} with i∘T(n) = T*(n)∘i | untwisted co-ordinary system exists at the point level | PRINTED |
| T5.3, R5.4 p.15 | (b) holds as fppf sheaves; the pointwise limit map need not be an isomorphism | irrelevant at finite level | PRINTED |
| p.15 §6 | w_r over Q[μ_{Np^r}] with ζ_{Np^r} := ζ_Nζ_{p^r}; **w_r^σ = <z>∘w_r = w_r∘<z>^{-1}**; π^r_s := w_r∘π_{s,r,*}∘w_s over Q; T(n)π^r_s = π^r_sT(n), U(q)π^r_s = π^r_sU(q) | Galois conjugation law used in 03 §2 | PRINTED |
| p.16 L6.1, (6.1)–(6.3), L6.2 | Kummer diagrams with the SAME field κ on both rows | no corestriction between fields | PRINTED |
| p.17–18 (6.4), C6.3, (6.9), P6.4 | π^r_s∘π^*_{r,s} = p^{s−r}U(p^{s−r}); Kummer-compatible H^1 diagrams | fixed field | PRINTED |

## MRS = Mazur–Rubin–Silverberg, "Twisting commutative algebraic groups", arXiv math/0609066 (J. Algebra 314 (2007))

| Loc. | Exact content | Match | Class |
|---|---|---|---|
| p.2 | FMod_O(k): FREE O-modules, continuous right G_k-action; CAG_O(k): morphisms O-equivariant and DEFINED OVER k; O fixed | W, w_r are not morphisms over Q or K_0 | PRINTED |
| Thm 1.4 p.3 | (I⊗_O V)(A) ≅ (I⊗_O V(A⊗L))^{Gal(L/k)} | fixed-base points = twisted invariants | PRINTED |
| Ex 1.5(ii),(iv) p.4 | rank-one I via χ ⇒ twist by χ^{-1}; O[Gal(L/k)]⊗_O V = Res^L_k V | | PRINTED |
| P1.6(ii), T1.8 p.4 | functoriality needs k-morphisms and fixed O | | PRINTED |
| T2.1 p.5 | dim = rank_O(I)·dim V | dimension test of 03 §1 | PRINTED |
| T2.2(iii) p.5 | T_ℓ(I⊗_O V) ≅ I⊗_O T_ℓ(V) | Tate module type test of 03 §1 | PRINTED |
| L2.4 p.6 | lattice k-isogeny ⇒ twist k-isogeny | | PRINTED |
| §1–2 | no change-of-coefficient-ring O_{r+1} → O_r statement | needed for type (G) transitions | NOT_PRINTED |

## Castella–Hsieh, arXiv:1809.09066 (text layer, §4.4–4.5)

| Loc. | Exact content | Match | Class |
|---|---|---|---|
| §4.4 | g = θ_χ(S_2) ∈ S^o(C, ω^{-1}η_{K/Q}, O⟦S_2⟧), h = θ_{χ^{-1}}(S_3) ∈ S^o(C, ω^{-1}η_{K/Q}, O⟦S_3⟧), C = D_Kℓ^{2m} | tame nebentype of the g-family contains η_{K/Q} ≠ 1 | PRINTED |
| (4.5)–(4.7) | κ(f,gh) from twisted diagonal cycles at tame level N = lcm(N_f,C); Shapiro decomposition | | PRINTED |

## Checkpoint text consulted (drift-evidence copy; content of the frozen audits, not a seal source)

`BSD_WHOLE_PROGRAM_SUCCESSOR_AUDIT_2026-09-15/_work/RECOVERED_H5_H9_CHECKPOINT_FULL_TEXT.txt` lines 505–1286:
H9R8 l.750–763 (type (Z) receptacle), H9R9 l.789–801 ("NO TYPE MISMATCH AFTER CONTRACTION"), H9R6 l.679–685 ((4.9) reading),
H9R12 l.939, H9R16-A/B l.1124–1189, H9R16-C l.1191–1244, supersession block l.1246–1284. The mathematical frozen statements
used here coincide with the operator's prompt.
