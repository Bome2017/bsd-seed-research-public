# 10 — VERDICT (SECOND, INDEPENDENT assembly referee, H9R16-C, 2026-09-15)

    SECOND_REFEREE = DEFECT_FOUND

    FIRST EXACT DEFECT = C1, the clause
        "Consequently rank_{Z_p}T_r^♮ = rank_{Z_p}(R_r)·2g^{(1)}_r with no |G_r| factor."
    WHY: T_r^♮ = Hom_{Z_p}(B_r^bal, T_pJ^{(1),ord}_r) (C3's own definition), so the second factor is
    rank_{Z_p}(e'_ord T_pJ^{(1)}_r), which by Hida's control theorem is a PROPER direct summand of
    T_pJ^{(1)}_r for r ≥ 2 (ordinary rank ≍ p^r, 2g^{(1)}_r ≍ p^{2r}). The printed equality is true
    only if g^{(1)}_r is read as the dimension of the ordinary part, a reading 01 nowhere licenses
    (g is the auxiliary Hida family, (1) the factor index, so g^{(1)}_r reads as the genus of
    X_1(N_f p^r)). Correct form: rank T^♮_r = rank_{Z_p}(R_r)·rank_{Z_p}(e'_ord T_pJ^{(1)}_r).
    SCOPE: nil. The clause's operative content ("no |G_r| factor") is PROVED, and no downstream claim
    uses the numeric value.

    SECOND EXACT DEFECT = C2, the clause
        "the opposite orientation (A_r^t = (U_p)^rW) is not the frozen functional."
    WHY: in weight 2, W^2 = id (so W^t = W_* = W) and W U'_p W = U_p, whence
        A_r^t = ((U'_p)^r)^t W^t = (U_p)^r W = (W U'_p W)^r W = W (U'_p)^r = A_r .
    A_r is SELF-ADJOINT; the two orientations of Γ_A induce the same bilinear form, so the opposite
    orientation IS the frozen functional. Verified numerically (_verify/transport_check.py (T5),(T5'),
    (N_g,p,r) ∈ {(5,3,1),(5,3,2),(7,2,1),(3,5,1)}, ℓ ∈ {1000003,999983}, all PASS).
    SCOPE: nil, and in the safe direction — A6's orientation caveat (Lane 5 07 item 5) and pressure
    point P5 are VACUOUS in weight 2. The clause should be struck, not repaired.

    NEITHER DEFECT BLOCKS THE ASSEMBLY. The three points the charter §4 sent me at hardest —
    C1's carrier collapse and freeness; C3's Hom-valued D4 with C4's contravariant π_r^*; C7 with
    C4's (U'_p)^{-r}/(U'_p)^{-2r} normalizations — are each PROVED below, and C4's constant is
    exactly 1.

## Per claim

    C1 = DEFECT  — rank clause FALSE as printed (above). Everything else PROVED: the balance relation
                   IS R_r-bilinearity after the A_r-transport and passage to the transported
                   commutative primed ordinary Hecke model; B_r^bal = R_r⊗_{R_r}R_r ≅ R_r; finite
                   FREE over Z_p; freeness is earned before it is used (C3 §2). Three mandatory
                   narrowings: (a) R_r is the NATIVE-level e'_ord𝕋'_{N_gp^r}⊗Z_p, not Lane 2 01 T3's
                   common-level algebra; (b) both auxiliary coefficient modules must be the regular
                   R_r-module (Lane 4 01 §6 leaves T^{(2),ord}, T^{(3),ord} undefined); (c) the
                   Hom/H^1 interchange holds for F ⊇ Q(μ_N) (carrier Galois-trivial) and must NOT be
                   applied to the ⋆-twisted module over K_0. COMMUTATIVITY of 𝕋' is load-bearing:
                   ρ_r is an anti-involution and the collapse fails without it.
    C2 = DEFECT  — orientation clause FALSE (above). Well-definedness PROVED; Φ̄^mod_r ∈ 𝒫^♮_r PROVED,
                   re-derived here from W^σ=⟨z⟩W, BCPV (4.1)/l.1257 and the post-transport balance,
                   including the step that the diamond action on Δ^ord is the W-INVERTED one
                   (⟨a,a,a⟩Δ^ord[d] = Δ^ord[a^{-2}d]); with the naive (4.1) the p-part does not cancel.
                   "Coincides with the frozen functional" holds only under Lane 4 01 §6's reading of
                   the unstated tame push-down (the bare frozen formula is not type-correct: A_r is a
                   native-level operator on a common-level cycle, and the frozen Φ^mod has no
                   pd^{t_f}_* on factor 1). NOT_PRINTED, not FALSE.
    C3 = CONFIRMED — Contr_r^{A_r} well typed and G_{F'_r}-equivariant (not G_{K_0}: P3);
                   evaluationwise D4 = A6 + B1 (A6 does not itself contain the factor-1 tame
                   push-down); Hom-valued upgrade consumes C1's freeness; (T^♮_r)^{G_{F'_r}} = 0 makes
                   H^1(K_0,T^♮_r) ≅ H^1(F'_r,T^♮_r)^{⋆} an ISOMORPHISM, so the descent is unique.
                   No type error at the contravariance seam. E′(a) does follow — but it is derived
                   FROM the point side, so it is not independent evidence for it.
    C4 = CONFIRMED — derived from scratch: Lemma (L) (level step of the contracted class, from MPC +
                   H_π + the transport) + Cor 4.11(i) at fixed Teichmüller index (BCPV l.1422–1430,
                   no constant) + Lemma (U) (exactly one U'_p on factor 1, exactly two on the
                   carrier) + evaluationwise Kummer injectivity over F'_{r+1}. Constant exactly 1,
                   integrally. The exponents (s, 2s) are FORCED. CARRIED DEPENDENCY: H_π, which 01
                   declares to be part of the statement and which is proved nowhere in the packet; it
                   is consumed three times (Lemma (L); moving res^bal past (U'_p)^{-2(r+1)}; C8's
                   injectivity). C4b CONFIRMED, with the sharper remark that Lane 4 04's (T♮_r) as
                   printed is unrepairable by any diamond UNIT δ♮_r, since N_{r+1,r} is a non-unit
                   zero-divisor (N^2 = pN). C4c CONFIRMED.
    C5 = CONFIRMED_WITH_NARROWER_HYPOTHESIS — C4 consumes only four properties of pd (commutation
                   with ϖ_{1,*}, with U'_p, with diamonds; the projection formula), all four verified
                   numerically for BOTH tame maps, so the constant cannot move; uniformity in r is a
                   REAL hypothesis (the commutation is a two-level statement). The NOT_PRINTED
                   citation is exact (l.1198–1199 vs l.1457 and l.1486–1487, all checked verbatim).
                   NARROWING: "a tame Hecke scalar on h-isotypic quotients" is imprecise — the exact
                   comparison is pr^t_{2,*} = W_{N_gp^s}∘pr^t_{1,*}∘W_{Np^s} (A5, verified numerically
                   here for the first time); W_{Np^s} is an involution on a >1-dimensional h-OLD space
                   for t>1, so a single scalar exists only after projecting both sides to lines on
                   which each W acts by a scalar.
    C6 = CONFIRMED — exhaustive audit: deg ϖ_1 = p^2, the ϖ_{i,*}ϖ_j^* composites, the triple p^3,
                   BCPV (4.9), Cor∘res = p, and BCPV's p^3/(p−1)^3 all fail to enter; the only p is
                   π_r(N_{r+1,r}) = p·1, and only on carrier projection. μ_r is not used. Its
                   counterfactual value is convention-sensitive; under Lane 4 03 §1's reading of μ_r
                   it is exactly C6's printed Φ^mod∘(1⊗Σ_g⟨d_2d_3⟩^{-1}) (|G_r|-or-0), under Lane 2
                   01 T4's reading it is |G_r|·Φ^mod. Both exhibit a full |G_r|. BCPV's G at
                   l.1331–1332 confirmed verbatim.
    C7 = CONFIRMED — all five preservation statements checked separately; the (1⊗N) clause is right
                   for the stated reason (d ≡ 1 mod N_gp^r ⟹ d ≡ 1 mod N_g); both tame push-downs
                   verified numerically; and both sides of C4 shown ⋆-invariant in the mixed module
                   Hom(B^bal_{r+1}, Ĵ^{(1)}_r(F'_{r+1})^{ord}), INCLUDING the Gal(F'_{r+1}/F'_r) steps
                   created by the level gap. C4 itself does not depend on this (C4c), which is the
                   correct order of dependence.
    C8 = CONFIRMED — 𝒫^♮_∞ is the equalizer inside the mixed ⋆-modules (not a naive inverse limit,
                   which contravariance forbids); π_r^* injective given H_π's surjectivity;
                   𝕋'_∞(N_g)-module structure verified; 𝒬_∞ integral because U'_p is a unit on
                   e'_ord-parts. The negative clause is true and admits a SHARPER proof: a system
                   satisfying both C4 and the naive ϖ_{1,*}-relation has (1−p)π_r^*Q_r = 0, hence
                   Q_r = 0 — the naive limit meets the C4-system only in 0, which subsumes
                   "would need Q_r ∈ p^rĴ".

## What this run adds that is not in the claims

1. `A_r` is self-adjoint in weight 2 (retires A6's orientation caveat and P5 entirely).
2. The diamond action on `Δ^ord` is the W-inverted one; the `+1/2` exponent in Lane 4 `03` §2 is
   forced by this and is not a convention choice.
3. A5 (`L5-T5`, the tame transport) is numerically verified for the first time — Lane 5 `04` §3
   explicitly records that `msym_check.py` has no tame case.
4. `H_π` is the single unproved load-bearing input of the whole assembly, used three times.
5. Lane 4 `04`'s `(T♮_r)` as literally printed cannot be rescued by any `δ♮_r` of its declared type.

## Independence-wall disclosure

No file listed in charter §2 was read, opened, grepped or imported. I did run one `ls -la` on
`~/H9R16C_FINAL_ASSEMBLY_REFEREE_2026-09-15/`, which displayed the file NAMES (already printed in
charter §2), sizes and timestamps of the walled files; no content. Nothing else in that directory was
touched beyond the four pre-referee files §2 permits. Lanes 1–5 and the first referee's directory were
not modified; the only writes are inside this directory. Custody: the Lane 5 checker copied into
`_verify/` is byte-identical to the original (`f99115c1…`, matching 02 §F), and the BCPV.tex and
paste-cache hashes match 02 §F exactly.

## Numerical work (mine, designed for this run)

`_verify/transport_check.py` (imports Lane 5's unmodified `msym_check.py`), log
`_verify/transport_check.log`: **124 exact checks mod ℓ ∈ {1000003, 999983}, 0 failures** —
the `A_r`-transport on every generator (`⟨d⟩`, `U'_p`, `T'_ℓ`) at `(N_g,p,r) ∈ {(5,3,1),(7,2,1),(3,5,1)}`;
`ρ_r(t_2)A_rt_3 = A_rt_2t_3` on random products (the carrier collapse); `U_pA_r = A_rU'_p` (the
C4/C4b leftover); `W T_ℓ W = ⟨ℓ⟩^{-1}T_ℓ`; `A_r^t = A_r`; and the tame block A5 with
`pd_*ϖ_{1,*} = ϖ_{1,*}pd_*`, `pd_*U'_p = U'_ppd_*`, `pd_*⟨n⟩ = ⟨n⟩pd_*` for **both** tame
degeneracies at `(N_g,t,p,s) = (5,2,3,1)`, `(3,2,5,1)` and the square 30→10→5 vs 30→15→5.

Method note: my first `T'_ℓ` coset construction failed Hecke commutativity `[T'_ℓ,U'_p] = 0`; that
failure was a bug in my own operator, not in any claim, and was fixed by using
`η_ℓ·diag(ℓ,1)` with `η_ℓ ≡ diag(ℓ^{-1},ℓ) mod L`. The failing variant is recorded here rather than
discarded.
