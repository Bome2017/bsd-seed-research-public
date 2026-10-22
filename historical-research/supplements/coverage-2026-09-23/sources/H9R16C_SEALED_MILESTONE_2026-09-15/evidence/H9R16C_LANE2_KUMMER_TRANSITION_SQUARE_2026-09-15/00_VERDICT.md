# 00 — Verdict, Lane 2 (general well-typed point/Kummer transition square; sufficient identities on δ_r)

Date: 2026-09-15. Finite levels only; nothing downstream of H9R16-C used. Sources: `02`.

## Result in four sentences

On the correctly typed fixed-base object — the **type-B** MRS twist of the carrier-valued Jacobian,
with lattice character `c_r^{+1/2}` (MRS's inverse convention) on the Jacobian factor and the tame
`ε_g^{-1}` twist on the carrier's third factor — the point/Kummer transition square with
`τ_r^MW = ϖ_{1,*}∘(−)` commutes by fixed-base Kummer naturality alone. The finite balanced point
descends to that object over `Q(μ_p)`; the proof uses only BCPV (4.1), (4.2), (4.4), (4.5), the KLZ2
Atkin–Lehner diamond rule and H9R16-A/B balance, and (4.5) itself forces `W^σ = <z>∘W`.
A W/w discrepancy `δ_r` never enters the square; it is harmless for the tower under
(D1) centrality, (D2) invertibility, (D5) level compatibility, plus (D3) rationality if Hida's `w` is
used to normalize the functional. What remains is one identity of Hecke correspondences, MPC_r(ν),
whose Λ-adic form BCPV assert with citations but which no source obtained here prints in operator form.

## Typing corrections that are mandatory

1. MRS lattice sign: `c_r^{+1/2}`, so that `T_p` of the twist is BCPV's `M^†`.
2. Type B (`⊗_{Z[G_r]}`, diamonds), not H9R8's type A (`⊗_Z`), whose Tate module is `|G_r|` times too large.
3. Tame nebentype twist on factor 3 of the carrier (the `g^c` twist of BCPV (1.7)).
4. The transition lands in `π_r^*P_r ⊂ Hom(B_{r+1}, e'Ĵ_r)^†(K_0)`, with a Hecke correction `ν_{r+1}`.

LANE = 2 — construct the most general well-typed point/Kummer transition square for H9R16-C and determine sufficient identities on {δ_r}
STATUS = C2_REDUCES_TO_FORMAL_NATURALITY — the square is PROVED formal on the type-B object; the class compatibility feeding the tower reduces to the correspondence identity MPC_r(ν), which is NOT_PRINTED (not an arithmetic theorem)
PROVED = (i) fixed-base Kummer naturality/injectivity for K_0-rational elements of Hom ⊗ Z_p between carrier-valued, e'-cut MRS twists (Lemma F, extensions 1–4); (ii) the square (SQ) with τ_r^MW = ϖ_{1,*}∘(−), τ_r^et = H^1(K_0, T_pτ_r^MW); (iii) C_POINT_NORMALIZATION: σΦ_r^mod(t_2⊗t_3) = <c_r(σ)^{1/2}>_{(1)}Φ_r^mod(t_2⊗<z_N(σ)>^{-1}t_3) for σ ∈ G_{K_0}, so Φ_r^mod ∈ P_r^{tr,†}; (iv) BCPV (4.5) ⇔ W_{Np^r}^{σ} = <z(σ)>∘W_{Np^r} given (4.1), (4.2) and the diamond rule; (v) type B involves no corestriction, and type A realizes corestriction inside its lattice projection, with μ_r∘(pr_r⊗ϖ_{1,*}) = ϖ_{1,*}∘μ_{r+1}; (vi) Proposition D — under (D1)(D2)(D5) the W- and w-normalized towers determine each other and MPC_r^w(ν^w) ⇒ MPC_r(ν^w ũ); (D3) additionally gives descent of the w-normalized point; (vii) MPC_r(ν) + (K_r) + (K_{r+1}) + BCPV Cor. 4.11 ⇒ τ_r^MW(Q_{r+1})∘(1⊗ν_{r+1}) = π_r^*Q_r
REFUTED = (a) H9R8/H9R9's type-A receptacle I_r^†⊗_Z J_r as the Kummer target for BCPV's dagger classes (TYPE_MISMATCH: wrong rank); (b) the literal "fixed base Q(μ_p)" without the tame ε_g^{-1} carrier twist (TYPE_MISMATCH: the point is only Q(μ_{N_g p^r})-rational); (c) the literal arrow τ_r^MW: P_{r+1}^{tr,†} → P_r^{tr,†} under coefficient retention (TYPE_MISMATCH: Hom is contravariant in the carrier); (d) any need to insert δ_r into the square or to use Hida's w for the square; (e) the printed constant 1/p in BCPV (4.9): commutativity of the middle square of (4.8) forces 1/|ker(G_{r+1}→G_r)| = p^{-3} (DERIVED_HERE, agrees with Lane 4; the type-B square does not use it)
FIRST_EXACT_UNPROVED_STATEMENT = MPC_r(ν): for every r ≥ 1 there is ν_{r+1} ∈ e'𝕋'_{r+1}⊗Z_p with <ϖ_{1,*}y, W_{N_g p^r}^{-1}(U'_p)^r ϖ_{1,*}z>_r = <y, W_{N_g p^{r+1}}^{-1}(U'_p)^{r+1} ν_{r+1} z>_{r+1} for all y, z ∈ e'H^1_ét(X̄_1(N_g p^{r+1}), Z_p(1)) (expected ν_{r+1} = Σ_{k≡1 mod p^r}<k>; derived only under the group-ring-pairing hypothesis)
TYPE_CHECK = PASS after the four mandatory corrections above; FAIL for type A, for the untwisted carrier over Q(μ_p), and for the literal P_{r+1} → P_r arrow
NEW_ASSUMPTIONS = none beyond frozen inputs and standard facts: (K_r) finite modified point/Kummer realization (frozen); H9R16-A/B balance including diamonds (frozen); H_π Hida transition of ordinary Hecke algebras (standard); DR22's ϖ_{1,*}U'_p = U'_pϖ_{1,*}; W_{N_g p^s} built from compatible ζ_{N_g p^s}; standard Galois-cohomology and Tate-faithfulness facts (numbering unverified, ledger S6)
COUNTEREXAMPLE_OR_OBSTRUCTION = none found; no FALSE and no NEW_THEOREM_REQUIRED item. A genuine obstruction would be a failure of MPC_r(ν) for every Hecke element ν (it would block the tower, not the square)
NEXT_SMALLEST_TEST = decide MPC_1(ν) and the value of ν_2 — from Ohta 2000 Cor. 1.3.8/2.3.6 if printed, else in weight-2 modular symbols for one small (N_g, p), e.g. p = 3, N_g = 13 — and run the free Lane-1 consistency test "BCPV (4.5) ⇔ W^σ = <z>∘W"
ARISTOTLE_READY = NO
STOP_ROUTE = NO
