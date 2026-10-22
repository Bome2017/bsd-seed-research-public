# 02 — Primary source ledger (Lane 2)

Date: 2026-09-15. Every row was read in the source text (TeX and/or PDF) stored under `sources/`
unless the Status column says otherwise. Hashes are in `06_FILES_CONSULTED.sha256`.

Status vocabulary: `VERIFIED` = read in the source and used as stated; `DERIVED_HERE` = not printed,
derived in `03` from printed definitions; `NOT_PRINTED` = the source does not contain it;
`CITATION_DRIFT` = the source's internal cross-reference points to the wrong item;
`STANDARD_UNVERIFIED` = standard fact whose numbering was not checked against a text here.

## S1 — BCPV, arXiv:2409.08645 (TeX dated 2024-09-13; PDF 33 pp.)

| Item | Content used | Status |
|---|---|---|
| §1.1.8, (1.6) | modified pairing `x ⊗ y ↦ <x, W_{N_h p^r}^{-1} (U'_p)^r y>` on `T_ord(N_h p^r, k)`, valued in `Z_p[Δ_{N_h p^r}] ⊗ χ^{k+1}` | VERIFIED |
| (1.7) + sentence after it | "The pairings (1.7) are interpolated by (1.4) as k and r vary." | VERIFIED (asserted, cited to Ohta/KLZ2; no operator identity printed) |
| §1.1.9, (1.8)/(1.9) | `e'_ord H^1(TSym(1)) → e_ord H^1(Sym^∨)` via `W^{-1}(U'_p)^r`, inverse `U_p^{-r} W`; "W intertwines U'_p and U_p" cited to Ohta99 (1.5.4) | VERIFIED |
| (1.4), (1.5) | `T_h ⊗ T_{h^c} → χ_h χ_cyc`; `T_h := H^1_ord(Y_1(N_h p^∞))_{m_h} ⊗ R_h` (infinite-level base change) | VERIFIED |
| (1.10), (1.11) | `ad(T_g) ≅ T_g ⊗ (T_{g^c} ⊗ χ_g^{-1}χ_cyc^{-1})`, trace ↔ pairing diagram | VERIFIED |
| (4.1), (4.2), (4.3) | `<a>Δ_r[d] = Δ_r[a_2a_3d_1, a_1a_3d_2, a_1a_2d_3]`; `σ_mΔ_r[d] = Δ_r[md]`; `σ_m = <m,m,m>^{1/2}` on `Δ_r` for `m` a square | VERIFIED |
| (4.4), Lemma 4.2 | `Δ_r^ord := (e'_ord W_{Np^r})^{⊗3} Δ_r` in `CH^2(X_1(Np^r)^3; Q(μ_{p^r}))_{Z_p}`; (i) null-homologous; (ii) = (4.5) `σ_m Δ_r^ord[d] = Δ_r^ord[m^{-1}d]` | VERIFIED (proof of (ii) says only "verified using the moduli description of the Atkin–Lehner operator") |
| (4.6), (4.7), iso `G` | `Δ_r^et = cl_1(Δ_r^ord)`; packaged class `Σ_{d∈G_r} Δ_r^et[d_2d_3a, d_1d_3b, d_1d_2c]<d>`; `G: Hom_{Z_p[G_r]}(S, Z_p[G_r]) ≅ Hom_{Z_p}(S, Z_p)` | VERIFIED |
| Remark 4.5(i),(ii), (4.8), (4.9) | commutative ladder whose OUTER columns are `ϖ_{1,*}^{⊗3}`; third column is the group-ring map with the explicit `1/p` | VERIFIED as printed; **the constant is inconsistent**: commutativity of the middle square of (4.8) forces `1/|ker(G_{r+1}→G_r)| = p^{-3}` (DERIVED_HERE, 03.3.3; Lane 4 independently recorded "off by `p^2`"). No effect on the type-B square. |
| Definition 4.6 | `G_r` = p-Sylow of `(Z/p^r)^{×3}`; `<χ>_r` through `diag`; `Z_p[G_r]^†` has `G_Q` acting by `<χ>_r^{-1/2}`; `M^† := M ⊗_{Z_p[G_r]} Z_p[G_r]^†`; `<χ>_r` faithful on `Gal(Q(μ_{p^r})/Q(μ_p))` | VERIFIED |
| Lemma 4.7 (= DR22 Lemma 2.6) | descent of the packaged class to `H^1(Q(μ_p), ·^†)`; uniqueness by inflation–restriction | VERIFIED |
| Lemma 4.10, Corollary 4.11 | `ϖ_{1,*}^{⊗3} Δ_{r+1}^ord[d'] = U'_p^{⊗3} Δ_r^ord[d]`, same for `Δ^et`, `Δ^et[[a,b,c]]`, `Δ^et` | VERIFIED |
| Definition 4.12 | `Δ_∞^et := {(U'^{⊗3}_p)^{-r} Δ_r^et}_r ∈ lim_{ϖ_{1,*}^{⊗3}} H^1(Q, e'H^1(Y_1(Np^r))^{⊗3}(2)^†)`; inverse of `U'_p` used ONLY on étale ordinary modules | VERIFIED |
| Definitions 4.13, 4.14 | projection to `T_{fgh}^†` via tame `ϖ_{1,*}` to native levels, then `(1.10) ∘ ι_{2,3}^*` | VERIFIED |
| Lemma 4.15, Lemma 4.18 | specialization `a_p(f_κ)^{-r} a_p(g_λ)^{-2r}`; `Δ_r^∘(κ,λ)` and `Δ_r^ord(κ,λ)` have the same projected étale AJ image | VERIFIED |
| (4.13), (4.14) | trace map through `a_p(g_λ)^r λ_{N_g p^r}^{-1} <,>_r`; `res Δ^tr|_(κ,λ) = a_p(f_κ)^{-r}a_p(g_λ)^{-r}λ^{-1}Δ_r^(tr)` | VERIFIED |
| footnote 8 | cites "Remark 4.9(ii)" for the (4.9) morphism | CITATION_DRIFT — the description is Remark 4.5(ii); Remark 4.9 is the Howard comparison |
| Lemma 4.10 attribution | "[DR22], Lemma 2.5" | CITATION_DRIFT vs arXiv:2207.01314v1, where the degeneracy identities are Lemma 2.4 (Lemma 2.5 there is the `θ_q`-annihilation used in BCPV Lemma 4.2). Published Astérisque numbering not checked. |
| anything point-level | Mordell–Weil transition, MRS object, contracted-class transition, operator form of pairing compatibility, Galois law of `W_{Np^r}` | NOT_PRINTED |

## S2 — Darmon–Rotger, "p-adic families of diagonal cycles", arXiv:2207.01314v1 (Astérisque 434)

| Item | Content used | Status |
|---|---|---|
| §1.3 | `ϖ_1:(A,P)↦(A,pP)`, `ϖ_2` = quotient map; `ϖ_i = π_i ∘ μ` with `μ` cyclic Galois of degree p (r ≥ 1) and `π_1, π_2` non-Galois of degree p; `U_p^* := π_{1*} π_2^*`; `H^1(X̄_∞^*) := lim_{ϖ_{1*}}`; Shapiro identification `H^1(X̄_r) = H^1(X̄_1, L_r^*)` intertwining `ϖ_{1*}` with `[p]` | VERIFIED |
| Lemma 2.2, Remark 2.3 | diamond/Galois action on `Δ_r[d]`; `σ_m = <m,m,m>^{1/2}` | VERIFIED |
| Lemma 2.4 | `(ϖ_1^3)_*Δ_{r+1}[d'] = p^3 Δ_r[d]`; `(ϖ_2^3)_*Δ_{r+1}[d'] = U_p^{⊗3}Δ_r[d]`; distribution relation | VERIFIED |
| pairing `<<,>>_r` | `<<λa,b>> = λ^*<<a,b>>`, `<<a,λb>> = λ<<a,b>>`; Galois-invariant for `G_{Q(ζ_1)}`; `U_p`, `U_p^*` adjoint | VERIFIED |
| Lemma 2.6 | packaged class extends to `H^1(Q(ζ_1), H_r)` | VERIFIED |
| Lemma 2.8 | `p_{r+1,r}(κ̂_{r+1}(σ)(γ_{r+1})) = κ̂_r(σ)(γ_r)` whenever `(ϖ_1^3)_*γ_{r+1} = γ_r` | VERIFIED |

## S3 — Mazur–Rubin–Silverberg, "Twisting commutative algebraic groups", J. Algebra 314 (2007); arXiv math/0609066

Hypotheses throughout: `O` commutative ring, `V` commutative algebraic group over `k` with `O → End_k(V)`,
`I ∈ FMod_O(k)` a free `O`-module of finite rank with continuous `G_k`-action (Appendix: projective `I`).

| Item | Content used | Status |
|---|---|---|
| Definition 1.1, Remark 1.2 | `I ⊗_O V` = twist of `V^d` by the cocycle of `I`; independent of basis | VERIFIED |
| Lemma 1.3 | on `I ⊗_O V(A ⊗ L)`, `γ` acts as **`γ^{-1} ⊗ (1⊗γ)`** | VERIFIED — load-bearing inverse convention |
| Theorem 1.4 | `(I⊗_O V)(A) ≅ (I ⊗_O V(A⊗_k L))^{Gal(L/k)}` when `G_L` acts trivially on `I` | VERIFIED |
| Examples 1.5(ii), (iv) | rank-one `I` with character `χ` gives the twist of `V` by **`χ^{-1}`**; `O[Gal(L/k)] ⊗_O V = Res_{L/k} V` | VERIFIED |
| Proposition 1.6(ii), Corollary 1.7, Theorem 1.8 | `Hom_{O[G_k]}(I,J) ⊗_O Hom_k(V,W) ↪ Hom_k(I⊗V, J⊗W)`; functoriality | VERIFIED |
| Theorem 2.1(iii) | `I⊗_O V ≅ V^{rk I}` over `L` if `G_L` acts trivially on `I` | VERIFIED |
| Theorem 2.2 | `(I⊗_O V)(k^s) ≅ I⊗_O V(k^s)`, `[n]`, `T_ℓ(I⊗_O V) ≅ I ⊗_O T_ℓ V`, all with `γ^{-1}⊗γ`, functorial in `I`, `V` | VERIFIED |
| Lemma 2.4, Corollary 2.5, Proposition 2.6 | isogenies of lattices give isogenies; `(I⊗J)⊗V ≅ I⊗(J⊗V)` | VERIFIED |
| Proposition 4.1 | `O[G] ⊗_O V ≅ Res^L_k V` | VERIFIED |

## S4 — Hida, "Limit Mordell–Weil groups and their p-adic closure", Doc. Math. Extra Vol. Merkurjev (2015); UCLA copy `LMWM.pdf` (44 pp.)

| Item | Content used | Status |
|---|---|---|
| §2 (S), Lemma 2.1 | `X̂(κ) = X(κ) ⊗ Z_p = lim X̂(κ)/p^n` over number fields | VERIFIED |
| Lemma 2.2 | canonical injection `lim X̂(κ)/p^n ↪ lim H^1(X[p^n])` (Kummer + left exactness of lim) | VERIFIED |
| §3 (u1), (u*1) | `π^*: J_r → J_s^r` is a `U(p)`-isomorphism; `π_*: J_s^r → J_r` is a `U^*(p)`-isomorphism; `e = lim U(p)^{n!}`, `e^* = lim U^*(p)^{n!}` | VERIFIED |
| §3 model | `Y_1(Np^r)` classifies `(E, φ: μ_{Np^r} ↪ E)` (μ-type model), diamonds `φ ↦ φ∘z` | VERIFIED — differs from the BCPV/DR22/KLZ2 point-of-order model |
| Corollary 3.5, Lemma 3.6 | U-isomorphisms with the `γ^{p^{r-1}}-1` kernel/cokernel | VERIFIED |
| §5, condition (A), Proposition 5.1 | abelian factors `A_s`, `B_s` | VERIFIED (not needed at finite level here) |
| §5 | `w_r` defined over `Q[μ_{Np^r}]` from a fixed `ζ`; **`w_r^σ = <z>∘w_r = w_r∘<z^{-1}>`** for `ζ^σ = ζ^z` (cites MW86 p.237, MW84 2.5.6) | VERIFIED |
| §5 | **`π_s^r := w_r ∘ π_{s,r,*} ∘ w_s` is defined over Q**, commutes with `T(n)` (n prime to Np) and `U(q)` (q ∣ Np); `{J_s, π_s^r}` Hecke-equivariant projective system over Q | VERIFIED |
| §6, display before (6.5), (6.5) | commutative Kummer square for `π_s^r: B_s → B_r` on ordinary parts | VERIFIED |
| Lemma 6.1, (6.6) | `A_r^ord ≅ A_s^ord` via `π^*`, `B_s^ord ≅ B_r^ord` via `π_s^r`; `π_s^r ∘ π^*_{r,s} = p^{s-r}U(p^{s-r})` | VERIFIED |
| (6.7), (6.8) | `π_s^r` and `π^*_{r,s}` adjoint under w-twisted Cartier duality | VERIFIED |
| "Control of Λ-adic Mordell–Weil groups" (PROMS 188, 2016) | the checkpoint's "Hida Lemma 2.1" | NOT OBTAINED — not re-verified; LMWM carries the statements used here |

## S5 — Kings–Loeffler–Zerbes, "Rankin–Eisenstein classes and explicit reciprocity laws", arXiv:1503.02888 (TeX incl. Nov. 2023 correction)

| Item | Content used | Status |
|---|---|---|
| §2 "Atkin–Lehner operators" | `W_Q` matrix definition; `W_Q^2 = [Q]<Q>_{N/Q}<-1>_Q`; `<d>_Q W_Q = W_Q <d^{-1}>_Q`; `W_{QQ'} = <Q'>_Q W_Q W_{Q'}`; convention differs from Atkin–Li (Remark `rmk:conventions`) | VERIFIED (label-level; printed numbers not extracted) |
| §2 moduli definition | `W_Q` on `Y_1(N) × Z[1/N, ζ_Q]`: `(E,P_{N/Q},P_Q) ↦ (E/<P_Q>, P_{N/Q}, P'_Q)` with `<P_Q,P'_Q> = ζ_Q` | VERIFIED |
| Galois law of `W_Q` | `W_Q^{σ_z} = <z>_Q ∘ W_Q` for `σ_z(ζ_Q) = ζ_Q^z` | DERIVED_HERE from the moduli definition (the new `P''` with pairing `ζ_Q^z` is `z·P'_Q`); NOT_PRINTED |
| Theorem [Ohta] `thm:ordinaryfiltration` (v) | canonical perfect `Λ_D`-valued pairing on `H^1_{ord,Par}(Np^∞)`, Hecke self-adjoint; proof of a later theorem notes it "involves the same factor `W_{Np^r}^{-1}∘(U'_p)^r`" | VERIFIED (label-level); finite-level operator identity NOT_PRINTED |

## S6 — Standard facts used without a source text here

| Fact | Status |
|---|---|
| naturality of Kummer connecting maps for homomorphisms of commutative group schemes | STANDARD_UNVERIFIED (no numbering claimed) |
| `H^1_cont(K, T_p A) = lim_n H^1(K, A[p^n])` for finite `H^0` (Tate; Jannsen) | STANDARD_UNVERIFIED |
| `Hom(A,B) ⊗ Z_ℓ → Hom(T_ℓ A, T_ℓ B)` injective (Mumford, *Abelian Varieties* §19; Milne, *Abelian Varieties*) | STANDARD_UNVERIFIED numbering |
| Shapiro isomorphism intertwines induced-lattice projection with corestriction | STANDARD_UNVERIFIED numbering |
| inflation–restriction | STANDARD_UNVERIFIED numbering |

## Project-side sources (context only; not mathematical authorities)

The local checkpoint `.docx` (Downloads and Desktop copies have identical `word/document.xml`,
SHA-256 `623448e3…`) is the tail-truncated local capture of H5–H9R16-C. The operator states the Google
Drive checkpoint is authoritative. It was used only for the frozen H9R16-A/B/C statements quoted in
the lane prompt, which match it.
