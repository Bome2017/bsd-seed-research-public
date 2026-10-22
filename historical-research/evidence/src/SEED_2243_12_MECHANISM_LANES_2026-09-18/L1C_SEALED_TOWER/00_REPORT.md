# L1C_SEALED_TOWER — where the sealed H9R16-C tower lands at the seed (2243,12), p = 5

Lane 1 (H9 calibration). Written 2026-09-18. Read-only on every record outside this directory. No ledger, memory or sealed file was modified.
Compute used: two PARI/GP 2.17.3 scripts (`runs/l1c_seed_checks.gp`, session 1; `runs/l1c_s3_fingerprint.gp`, session 2), each well under 1 CPU-s. No heavy process was launched. Session 2 resumed session 1 and redid nothing; its additions are §2 A2.2 update, §3, §4, §5 and `01_TWIST_COMPONENT_DERIVATION.md`.

Status words: PROVED, PROVED_DERIVED, CERTIFIED_COMPUTATION, VERIFIED_FROM_SOURCE, CONDITIONAL(on X), OPEN, NOT_APPLICABLE(at H), BLOCKED(at step).
Three statements are kept apart throughout: "a printed result does not apply", "a component of a construction vanishes", "a route is impossible". This report never makes the third kind of statement.

## Sources (local; line numbers are those of the files named)

| key | file | used for |
|---|---|---|
| CERT | `~/SEED_2243_12_MASTER_CERTIFICATE_2026-09-18/00_CERTIFICATE.md` | N0 (l.44), N1 (l.45), N2 (l.46), N3 (l.47), N11 (l.55), non-claims (l.72-78) |
| SEAL-00 | `~/H9R16C_SEALED_MILESTONE_2026-09-15/00_MILESTONE.md` | hypotheses and objects (l.18-27), theorem (l.30-41) |
| SEAL-01 | `.../01_THEOREMS.md` | MPC (l.10-17), H_π (l.83-87), carrier (l.63-79), ⋆-action (l.98-111) |
| SEAL-04 | `.../04_RESIDUAL_CITATIONS.md` | R1-R3; list of inputs not used (l.35-38) |
| SEAL-05 | `.../05_NON_CLAIMS.md` | the chain (l.41), the (H-ω) failure for CH (l.21-25), what is not claimed (l.56-60) |
| REF2-C7 | `.../evidence/H9R16C_SECOND_ASSEMBLY_REFEREE_2026-09-15/08_C7_TAME_TWIST.md` | the tame carrier twist (§1) |
| H17 | `~/H9R17_BIG_KUMMER_TRACE_2026-09-15/08_ASSEMBLY.md` (§1 l.7-22, §2 l.23-58), `09_VERDICT.md` (l.1-15, l.60-82), `07_LEVELS_AND_BRANCH.md` (§3 l.44-62) | big-trace identity, its hypotheses, the three obstacles named for the chain |
| H17B | `~/H9R17B_ADMISSIBILITY_SCOPING_2026-09-15/01_BCPV_HYPOTHESIS_LEDGER.md`, `04_VERDICT.md` (l.5-37) | BCPV hypothesis list with TeX lines; A-DICH |
| BCPV | `~/H9R16C_LANE5_MPC_PROVER_2026-09-15/sources/tex/BCPV.tex` (sha256 b25d6e47…) | l.459 (N_f square-free), l.479-485 (root numbers), l.706 (Selmer), l.344-351 (Conj. with ε(f) = −1) |
| LEDGER | `~/H9R19_WEIGHTED_RECIPROCITY_2026-09-15/08_PROGRAM_STATUS_FREEZE.md` | top block (l.3-33), lines I-IV (l.45-50), derived-point gate (l.122-128), terminal block (l.130-156), coefficient gate (l.219-237) |
| F09 | `.../09_BRANCH_INVOLUTION_AUDIT.md` | line table (l.58-63), verdict (l.73-92) |
| F20 | `.../20_DERIVED_POINT_GATE.md` | gate 1 (l.7-23) |
| F22 | `.../22_SRC_castella_nonvanishing_GKC_IMC.txt` | Castella Thm A (l.88-114), Choice 5.2.1 (l.839-849), Thm 5.2.3 (l.861-869) |
| F25/F26/F31 | `.../25_SRC_pro_…md` (Prop 3.1, Cor 3.2, l.53-79), `26_ARITHMETIC_OUTPUT_AND_CERTIFICATE_AUDIT.md` (§2 l.78-94, §3 l.96-106), `31_COEFFICIENT_GATE_SOURCE_CHECK.md` (l.48-65, l.82-87) | G-SUPPORT, gate definitions, G-COEFF |
| CH | `~/H9R16C_LANE4_HOSTILE_OBSTRUCTION_2026-09-15/sources/CastellaHsieh_1809.09066.txt` (sha256 8302d020…) | Thm A (l.155-161), Cor B (l.182-184), CM families (l.1074-1078), Thm 4.2 (l.1038-1046) |
| F12 | `.../12_H9R21_CROSS_SHEET_GEOMETRIC_REALIZATION_SOURCE_AUDIT.md` | the rank-2 Chow–Heegner remark (l.50-55), which that file cites from memory |
| L3-01 | `~/H9R16C_SEALED_MILESTONE_2026-09-15/evidence/H9R16C_LANE3_PRIMARY_LITERATURE_2026-09-15/01_TYPES_AND_OBJECTS.md` | type findings T5, T6, T9 (l.178-179, l.222): Hida's MW control fixes the base field, old-form subvariety towers vanish, and the two Hida systems |

## §0. Cheap exclusion gate (rule 5), run first

Question: is "identify the sealed tower's specialization at the seed with E(Q)⊗Q_5" the same as a statement the ledger already records?

1. **The terminal H9 statement is already settled at this instance.** The seed satisfies rank E(Q) = 2 (CERT N1) and Sha(E/Q)[5^∞] = 0 (CERT N11). So Sel(Q, V_5E) = E(Q)⊗Q_5 has dimension 2, and W = S (W = the rational Kummer image, S = the Selmer group, as in LEDGER l.135-139). The recorded wall, "Selmer-corank-2 Sha finiteness" (LEDGER l.195-198), is therefore not an obstacle at this curve. That is why the operator calls this a calibration. PROVED_DERIVED (from CERT N1 and N11).
2. **What the lane asks is a sealed non-claim.** "Specialize the tower into E(Q)⊗F_g" is exactly the chain of SEAL-05 l.41, recorded as NOT PROVED. At the CH weight-one point, the line-I specialization is recorded as the same-root class κ_{α,β^{-1}} = 0 (LEDGER l.17-20).
3. Neither point is a reduction to Proposition K, the C1 Gate-B class-group component, the MR residual Stark equivalence or Gate G. Those are statements about bounding Sha, and at the seed Sha[5^∞] = 0 is already proved.

Exclusion verdict: the lane's question reduces to (a) the recorded non-claim SEAL-05 l.41 and (b) the recorded line-I zero. Only consequences of W = S that are specific to this seed can be new. The rest of this report looks for exactly those consequences.

## §1. Deliverable (1): the data needed to instantiate the seal at an E, and the seed at p = 5

### 1a. The sealed theorem's own hypotheses (SEAL-00 l.18-27, SEAL-01 §1, §7)

| datum or hypothesis (as written) | where | seed at p = 5 | status |
|---|---|---|---|
| p odd | SEAL-00 l.18; H_π "all odd p" SEAL-01 l.87 | p = 5 | MET, CERTIFIED_COMPUTATION |
| tame level N_f prime to p (the f-side receptacle is J^(1)_r = Jac X_1(N_f p^r); **no newform is chosen**) | SEAL-00 l.18-20 | N_f = N_E = 6503188012738584 = 2³·3·2243·4547²·5843, and 5 ∤ N_E (C1) | MET, CERTIFIED_COMPUTATION |
| tame level N_g prime to p (the carrier is R_r = e'_ord 𝕋'_{N_g p^r} ⊗ Z_p, the whole ordinary Hecke algebra; **no g is chosen**) | SEAL-00 l.18, l.22 | free choice; for the H9 target N_g = C = |D_K|·ℓ^{2m} (CH l.1076-1077) with 5 ∤ C | MET for any admissible choice |
| N = lcm(N_f, N_g), K_0 = Q(μ_p), F'_r = Q(μ_{Np^r}) | SEAL-00 l.18-19 | K_0 = Q(μ_5). For CH data N = N_E·C, since (D_K ℓ, N_E) = 1 | definitions only |
| fixed cycle index e | SEAL-01 l.100 (left free; H17 fixes e = (1,1,1), H17 08 l.15) | — | convention |
| tame push-down pr^t_1 or pr^t_2, used uniformly in r | SEAL-04 R3 (l.23-31) | — | convention |
| (G2) ϖ_{1,*}U'_p = U'_pϖ_{1,*}: printed in DR22 without proof | SEAL-04 R2 (l.13-21) | seed-independent | citation item |
| **not used by the seal:** ordinarity, KLZ17's p ≥ 5, Hida MW control, any Selmer, Sha, L-value, density or weight-one input | SEAL-04 l.35-38; SEAL-01 l.17, l.87 | — | — |

**Finding 1.1 (PROVED_DERIVED from SEAL-00 l.18-41).** The sealed tower exists at the seed for every admissible N_g, and it depends on E **only through N_f = N_E**. Its outputs Q_r lie in Hom_{Z_p}(B^bal_r, Ĵ(X_1(N_E·5^r))(Q(μ_{N·5^r}))^ord)^{Gal/K_0,⋆}. These are Hom-valued points on the whole Jacobian, over cyclotomic fields. Nothing E-specific is sealed: E enters only at the second arrow of the chain (f-projection), and g and K enter only at the first (localization at 𝔭_g). So instantiating the seal at the seed is automatic and carries no arithmetic information about E.

### 1b. Data the chain of SEAL-05 l.41 needs (the seal's intended use), and the seed

Hypotheses of the H9R17 big-trace identity (H17 08 l.7-22) and the BCPV standing hypotheses it inherits (H17B ledger; BCPV TeX lines):

| hypothesis | source | seed / p = 5 | status |
|---|---|---|---|
| f = Hida family through the ordinary 5-stabilization f_α of f_E; a_p(f) ∈ R_f^× | BCPV l.429 (H-1.8) | a_5 = −2, so the unit root α ≡ 3 (mod 5), valuations of the roots (0, 1) (C3) | MET |
| ε_f = 1 | BCPV l.459 (H-2.1) | E/Q, so the nebentype is trivial | MET |
| **N_f square-free** | **BCPV l.459 (H-2.3)** | **v_2(N) = 3, v_4547(N) = 2 (C1)** | **FAILS as written** |
| (Irr) ρ̄_f absolutely irreducible | BCPV l.437-439 | image GL₂(F_5) (CERT N3) | MET |
| (Dist) p-distinguished | BCPV l.449-456 | good ordinary at 5: sub-character ramified mod 5, quotient unramified, so distinct | MET, PROVED_DERIVED |
| (NA) α_f ≢ 1 mod m_{R_f} | BCPV l.619-626 (H-5.1) | α ≡ 3 (mod 5) (C3) | MET |
| k_∘ = 0 for f | BCPV fn l.425 (H-1.5) | weight 2, trivial character | MET |
| **global root number ε(f_κ) = −1** | **BCPV l.485 (H-3.3); BCPV's Conjecture assumes ε(f) = −1 (l.344-351)** | **w(E) = +1 (C2)** | **FAILS** |
| local root numbers ε(WD_ℓ(T^†_{κ,λ})) = +1 for ℓ \| N_f N_g | BCPV l.479-483 (H-3.1) | depends on g; the local root numbers of E alone are (2:+1, 3:+1, 2243:−1, 4547:+1, 5843:+1) (C2) | NOT CHECKED (needs g) |
| g: tame nebentype ε_g = ε_g^{(t)} **and** k_∘ = 0, i.e. (H-ω) | BCPV l.459, fn l.425; H17 08 (H-ω) l.14-15 | **CH's g = θ_χ(S_2) ∈ S^o(C, ω^{-1}η_K) (CH l.1077-1078) violates both. This is recorded in SEAL-05 l.21-25 and H17B 04 l.25-37 (A-DICH).** A BCPV-admissible CM g exists (H17B 04 l.5-20), but its weight-one members are p-ramified, so it is not the CH target | FAILS for the H9 target g; seed-independent |
| non-Eisenstein m_f; KLZ17 control (p ≥ 5) | H17 07 l.50-52 | irreducible mod 5; p = 5 | MET |

Data for the live target (the class that spans the strict line). This is owned by lanes L1A and L1B and is recorded here only as far as the tower needs it:

| datum | source | seed | status |
|---|---|---|---|
| K imaginary quadratic, 5 split (CM Hida family), q = 2243 inert, and 2, 3, 4547, 5843 split (Castella Choice 5.2.1 (1)-(2)) | F22 l.839-843 | the smallest discriminants with this pattern are −119, −311, −551, −1151, −1751 (C7). At D = −119, w(E^K) = +1 (C7). **L(E^K, 1) ≠ 0 was not checked** (conductor ≈ 10^20) | splitting pattern: CERTIFIED_COMPUTATION; the L-value conditions: existence only (F22 Remark 5.2.2, l.848-850) |
| χ a ring class character of conductor ℓ^m O_K (m even), ℓ ∤ 5N_E split in K; g = θ_χ(S_2), h = θ_{χ^{-1}}(S_3), N_g = C = |D_K|ℓ^{2m} | CH l.1074-1078 | choosable | existence |
| CH Thm A: N^- square-free; ρ̄ ramified at every q \| N^- | CH l.155-158 | N^- = 2243. It is square-free, and E[5] is ramified at 2243 because v_2243(Δ) = 1 (CERT N3) | MET |
| CH Thm 4.1 (sq): gcd(N_f, N_g, N_h) square-free | CH l.980 | gcd = 1, since D_K ℓ is prime to N_E. **CH does not need N_f square-free** | MET |

**Finding 1.2.** At the seed, the seal itself is instantiable, while the BCPV frame that the seal was built to serve is not. H-2.3 fails (N_f is not square-free) and H-3.3 fails (w(E) = +1, while BCPV assume ε(f) = −1). Both are **statements that a printed hypothesis does not hold at this seed**. They do not show that the H9R17 identity fails: H17 07 §3 cites only the non-Eisenstein hypothesis and KLZ17's control theorem for the f-branch, and whether the proof uses H-2.3 or H-3.3 anywhere is NOT DETERMINED here. H-3.3 fails for **every** curve the H9 program targets, since those all have w = +1. The seed simply makes this concrete. The H17B lane left it NOT_VERIFIED (H17B 02 l.122).

## §1c. The known target at the seed (CERTIFIED_COMPUTATION, `runs/l1c_seed_checks_output.txt` C4-C6)

The model y² = x³ − 22735x² + 106272484x has good reduction at 5 and is minimal there (v_5(Δ) = 0). #E(F_5) = 8. Put log_5(P) := ellpadiclog(E, 5, 40, [8]P)/8. This is the formal-group logarithm of the model's invariant differential; the ratio of two logarithms does not depend on that normalization.

    log_5(P1) = 2·5² + 3·5⁴ + 2·5⁵ + 3·5⁶ + 5⁷ + 3·5¹¹ + … + O(5²²)            v_5 = 2
    log_5(P2) = 2·5 + 5² + 4·5³ + 3·5⁴ + 3·5⁵ + 4·5⁶ + 2·5⁷ + … + O(5²²)       v_5 = 1
    t := log_5(P1)/log_5(P2) = 5 + 2·5² + 3·5³ + 3·5⁴ + 2·5⁸ + 3·5⁹ + 5¹¹ + … + O(5²⁰)      v_5(t) = 1
    STRICT LINE  ker(loc_5) ⊂ E(Q)⊗Q_5  =  Q_5·(log_5(P2)P1 − log_5(P1)P2)  =  Q_5·(P1 − t·P2),     −t ≡ 13320 (mod 5⁶)

This agrees with the recorded Kummer images: loc_5 = (0, 2) and P1 ∈ 5E(Q_5) (small-seed report `~/BSD_SMALL_SEED_FIXED_PRIME_2026-09-17/00_REPORT.md`, correction C1, l.42-46). In both computations v_5(t([8]P1)) = 2 and v_5(t([8]P2)) = 1.
Consequence: an integral generator of the strict line reduces mod 5 to a unit multiple of P1 in E(Q)/5E(Q) = ⟨P1, P2⟩ (CERT N2).

**The live class spans this line at the seed (PROVED_DERIVED).** Castella's Thm A has hypotheses (i)-(iii) (F22 l.88-99). At the seed, E[5] is irreducible with image GL₂(F_5) (N3). The prime q = 2243 divides N exactly once (N0) and 2243 ≡ 3 (mod 5). The reduction at 5 is good ordinary, w = +1 (C2), and L(E,1) = 0 because the rank is 2 (N1, N7). Sel(Q, V_5E) = E(Q)⊗Q_5 has dimension 2 (N1, N11), and loc_5 ≠ 0 on it because log_5(P2) ≠ 0. Thm A(2) therefore gives, for every admissible (K, χ) as in Choice 5.2.1 (existence: F22 Remark 5.2.2, l.848-850), κ_5(E) = λ·(P1 − t·P2) with λ ∈ Q_5^×. By CH Thm A (l.155-161) and Cor B (l.182-184), the same holds for κ_{α,α^{-1}}. The hypothesis audit for (K, χ), including the additive primes 2 and 4547, belongs to lanes L1A and L1B. This lane uses only the conclusion: **the strict-line point that H9 was built to construct exists at the seed and is known explicitly.**

## §2. Deliverable (2): the chain of SEAL-05 l.41 at the seed, arrow by arrow

    𝒫^♮_∞  --A1-->  𝒫^♮_{∞,𝔭_g}  --A2-->  (E(Q)⊗Q_5)⊗̂R_{g,𝔭_g}  --A3 = λ_g-->  E(Q)⊗F_g

H9R17 names three obstacles on this chain (H17 09 l.79-82): the 𝔭_g-localization of the carrier, the Mordell–Weil descent, and the λ_g-specialization (where DEFECT D1 becomes live). This section splits each arrow into its operations and gives, for the seed at p = 5, the first operation that fails, together with the missing object.

### A1: localization at 𝔭_g

| op | content | seed at p = 5 | status |
|---|---|---|---|
| A1.1 | choose the branch g and its arithmetic height-one prime 𝔭_g ⊂ 𝕋'_∞(N_g) = lim_r R_r | for the H9 target, g = θ_χ(S_2) (CH l.1077) at its weight-one point S = v − 1. That branch is a component of the ordinary Hecke algebra of tame level C, and the seal does not depend on k_∘ (SEAL-05 l.37: "the sealed tower survives verbatim" under the ω-rebuild) | defined |
| A1.2 | localize the 𝕋'_∞(N_g)-module 𝒫^♮_∞ at 𝔭_g | exact functor; no hypothesis | defined |
| A1.3 | 𝒬_∞ ≠ 0 in 𝒫^♮_{∞,𝔭_g} | not claimed: "No claim that the point tower is non-torsion" (SEAL-05 l.58-60) | **OPEN** |
| A1.4 | select the live branch pair (g_α, g_β) = (g, h) | the carrier is collapsed, B^bal_r ≅ R_r (SEAL-01 l.63-71), so after localization the pair is (g, g^c). For CH's g, g^c = g as branches, and at 𝔭_CH the pair is (g_α, g_α), the same-root pair (LEDGER l.14-20; F20 l.11-13; F09 l.79-80) | **BLOCKED at A1.4** (recorded; seed-independent; not reopened) |

**No operation of A1 fails at the seed.** The first statement A1 leaves unestablished is A1.3. Relative to the target, A1 already fixes the wrong pair (A1.4). The missing object there is an h-direction, meaning a second CM sheet, in the carrier. The ledger records this; the seed changes nothing.

### A2: Mordell–Weil descent to (E(Q)⊗Q_5)⊗̂R_{g,𝔭_g}

| op | content | seed at p = 5 | status |
|---|---|---|---|
| A2.1 | f-projection: e'_ord Ĵ_1(N_E·5^r) → the f_α-quotient, which is ≅ Ê⊗Z_5 only after ⊗Z_5 because α ∉ Q. Quotient towers are levelwise isomorphic; old-form subvariety towers have zero integral pro-limit (lane-3 T6: HidaC Lemma 6.2, Prop 6.4), so the quotient must be used | (Irr), (Dist), non-Eisenstein, KLZ17 p ≥ 5 all hold (§1b) | defined at each finite level |
| A2.2 | fix the ⋆-component of the E-projected value (TWIST-COMPONENT, see below) | for CH's g, ε_g^{(t)} = η_K ≠ 1 | **OPEN** (typing item) |
| A2.3 | pass from Hom(R_r, Ê(F'_r)) over the growing fields F'_r = Q(μ_{N·5^r}) to a fixed-field Mordell–Weil group Ê(K_0) and then Ê(Q), with R_g coefficients | this needs a Λ-adic Mordell–Weil control/descent for this tower. None is available: a weight-one Hida MW control theorem is excluded by the H9R17 charter (H17 09 l.80-81); Hida's MW control fixes the base field and varies the level, while this tower varies the field (lane-3 T5, T9); subvariety towers vanish (T6) | **BLOCKED at A2.3** — missing object: a descent/control map E-proj(𝒫^♮_{∞,𝔭_g}) → (E(Q)⊗Q_5)⊗̂R_{g,𝔭_g} |
| A2.4 | K_0 → Q | the seal is "over K_0, not res from Q" (SEAL-05 l.20). BCPV's printed class is K_0-rational only (H17 09, D2). Weighted replacement: DR22 (2.27) | not in the seal |

**First failing operation of A2 as a Mordell–Weil arrow: A2.3.**

**Seed-specific reduction (PROVED_DERIVED from CERT N11 and BCPV l.706).** At the seed W = S, so the Mordell–Weil content of A2 can be bypassed on the étale side:

    Kum_∞ (sealed, SEAL-01 §8)  →  Ψ (H17 08 §2)  →  H¹(K_0, T_f^†⊗̂R_g)  →  descent to Q  →  H¹_f(Q, T_f^†)⊗̂R_g (BCPV l.706)  →  specialize at λ  →  Sel(Q, V_5E)⊗F_λ = (E(Q)⊗Q_5)⊗F_λ   [N11]

Every Q-level Selmer value is automatically Mordell–Weil-valued at this curve. **So at the seed, A2 is equivalent to the étale identification of the tower's Kummer image with a Q-rational Selmer family.** A2.3 was the obstruction; the proved Sha[5^∞] = 0 makes it unnecessary here. It does not make it unnecessary for the program: W = S is an input from outside H9, so this is a calibration and not a mechanism.
The first failing operation of the bypass is **Ψ-identification**. The H9R17 identity [(id⊗tr)Δ^ét_∞]_{K_0} = p³·Ψ(Kum_∞(𝒬_∞)) is proved under (H-ω) and (B) (H17 08 l.7-22).
- (H-ω) is false for CH's g (SEAL-05 l.21-25).
- (B) does not hold as written at the seed (H-2.3 and H-3.3; §1b), for any g.
- The weighted replacement is PROVED_CONDITIONAL for the BCPV diagonal class (LEDGER l.7-12). At 𝔭_CH it is the same-root class (A3.3).

Status: NOT_APPLICABLE(at (H-ω)) for CH's g. For a BCPV-admissible g, the result does not apply as printed (at (B)), and whether the proof uses H-2.3 or H-3.3 is NOT DETERMINED here. Such a g also has no CH weight-one point (A-DICH, H17B 04 l.25-37).

**TWIST-COMPONENT (A2.2). OPEN typing item; not claimed as a defect of the seal or of H9R17.**
- After f-projection the factor-1 diamonds ⟨m_σ⟩_{(1)} and ⟨n_σ⟩_{(1)} act trivially: ε_f = 1, and f_α has trivial nebentype. So ⋆-invariance (SEAL-01 l.108-109) reads σ(Φ(R(⟨n_σ⟩)^{-1}b)) = Φ(b).
- On the g-branch, R(⟨n⟩) acts by ε_g^{(t)}(n) (REF2-C7 §1). Using the R_g-linearity of the branch-projected functional (H17 08 §2.3), this gives σ·Φ(1) = ε_g^{(t)}(n_σ)^{±1}·Φ(1) for σ ∈ Gal(F'_r/K_0). This is a two-line derivation from the sealed formula.
- H17 08 §2.2 instead reads the tame half-twist as BCPV's g^c labelling and takes the branch-projected target to be the untwisted H¹(K_0, T^†_f⊗R_g).
- The record contains no computation that reconciles these two readings at the level of the E-projected **point**. When ε_g^{(t)} = 1 there is nothing to reconcile. For CH's g, ε_g^{(t)} = η_K.
- If the twisted reading were the right one, the Q-descended E-output for CH's g would lie in the η_K-component, that is, in E^K(Q)⊗(coefficients). That group is torsion whenever L(E^K,1) ≠ 0 (Kato), and both Castella's Choice 5.2.1(5) and CH Thm A impose that condition. CONDITIONAL(on the twisted reading).
- A hostile check of REF2-C7 §1 against H17 08 §2.2 should settle this before anyone builds A2.

**Session-2 update to A2.2 (supersedes the CONDITIONAL above for CH's g; details in `01_TWIST_COMPONENT_DERIVATION.md`).** For CH's g the tame nebentype η_K is quadratic, so the point-level statement needs only Z_5-linearity of Φ, not the R_g-linearity that the two readings disagree about. From the sealed ⋆-formula (SEAL-01 l.108-112), REF2-C7 §1 and the Galois-equivariance of the f_α-projection π_E:
- σ(π_EΦ(b)) = η_K(n_σ)·π_EΦ(b) for every b in CH's local factor of B^bal_r ⊗ Q̄_5 and every σ ∈ Gal(F'_r/K_0);
- η_K is nontrivial on Gal(F'_r/K_0), because K ⊄ Q(μ_5) (5 splits in K);
- hence π_EΦ(e_g B^bal_r) ∩ (E(K_0)⊗Q̄_5) = 0, and so its intersection with E(Q)⊗Q̄_5 is 0 too, **at every finite level r and for every element of 𝒫^♮_r**.

Status: PROVED_DERIVED, not refereed. This is a statement that a component vanishes: the E(Q)-component of the E-projected CH-branch values is zero. Any Galois-compatible A2 therefore sends CH's branch to 0 before A3 is reached. It is not a statement that the chain is impossible. The Galois-side typing question for BCPV-admissible g with ε_g^{(t)} ≠ 1 (H17 08 §2.2) stays OPEN and is not claimed as a defect.

### A3: λ_g-specialization at the target point

| op | content | seed at p = 5 | status |
|---|---|---|---|
| A3.1 | R_{g,𝔭_g} is a DVR, and λ_g is its residue map to F_g, a finite extension of Q_5 (F31 l.61-63) | the CM family is étale over weight space at a p-regular weight-one point (BSV Assumption 1.1 / BD16, as in H17B 04 l.50-53). This needs α² ≠ 1 for the ring class character (α = χ(p̄), β = α^{-1}), which is choosable | defined, given the choice |
| A3.2 | a specialization lemma that carries the tower normalization (a_p(f)^{-r}a_p(g)^{-2r}, λ_{N_gp^r}(g)) to a class at λ_g | BCPV's lemma (l.1468-1500) is stated for BCPV arithmetic points only. Their W^cl has no weight-one point (H17B D-1). Its printed sum annihilates branches with nontrivial wild nebentype (H17 09 D3). The AL level index is DEFECT D1 (H17 09 l.60-82). The ω-rebuild names "BCPV's own specialization sum at l.1474-1475" as the first obstruction (SEAL-05 l.37) | **BLOCKED at A3.2** — missing object: a weight-one specialization lemma for the (weighted) diagonal class in the tower's normalization |
| A3.3 | the value, if A1-A3.2 were supplied through the weighted class | the same-root class κ_{α,β^{-1}}, which is 0 (CH Thm A l.159: "κ_{α,β^{-1}} = κ_{β,α^{-1}} = 0"; LEDGER l.17-20). The hypotheses of CH Thm A hold at the seed for an admissible (K, χ) (§1b) | the construction's component **vanishes** at 𝔭_CH: CONDITIONAL(on A1-A3.2 and the weighted identification) for the tower; VERIFIED_FROM_SOURCE for κ_{α,β^{-1}} = 0 |

### §2 answer to the operator's question

- **Where the tower lands (proved):** in 𝒫^♮_∞(N_E, N_g, 5). These are Hom-valued, ⋆-invariant points of Jac X_1(N_E·5^r) over Q(μ_{N·5^r}). No sealed map brings them closer to E (Finding 1.1).
- **Where the chain would land (if A1-A3.2 were supplied):** at the CH weight-one prime, on κ_{α,β^{-1}} = 0 ∈ E(Q)⊗F_g. That is the zero vector: it is neither the strict line Q_5(P1 − tP2) nor a two-dimensional span.
- **First failing operation, in chain order:**
  - A1 has none. A1.3 (non-vanishing) is OPEN, and A1.4 (the live pair) is BLOCKED.
  - A2 fails at A2.3, the Mordell–Weil control. At this seed A2.3 can be bypassed because W = S, and the bypass then fails at Ψ-identification: it is NOT_APPLICABLE(at (H-ω)) for CH's g.
  - A3 fails at A3.2, the weight-one specialization lemma.
- **Can the specialization be identified with the two-dimensional rational MW space?** Not by anything proved. At the only point where a value is known (conditionally), the image is {0}. Anywhere else there is no input (§3).

**Session-2 addendum to the §2 answer.** On CH's branch the E(Q)-component of the E-projected tower values is 0 at every finite level (A2.2 update above; `01_TWIST_COMPONENT_DERIVATION.md`). So a Galois-compatible A2 gives 0 on that branch before A3 is reached, and this is independent of A1.4. There are now two separate reasons why the chain's value at 𝔭_CH is 0. The first is the recorded one: on line I the chain lands on the same-root class. The second is new: the η_K component. Neither of them says the route is impossible.

## §3. Deliverable (3): necessary conditions that the known answer creates (session 2)

Setup at the seed. Every item below is CERTIFIED_COMPUTATION or PROVED_DERIVED from the certificate.
- S := Sel(Q, V_5E) = W = E(Q)⊗Q_5 = Q_5P1 ⊕ Q_5P2 (CERT N1, N11).
- E(Q)⊗Z_5 = Z_5P1 ⊕ Z_5P2, index 1 at 5 (N2).
- S_0 := ker(loc_5|S) = Q_5·w, with w := P1 − tP2 and t = log_5P1/log_5P2 ∈ 5Z_5 (v_5(t) = 1; C5 and F0). The vector w is primitive in E(Q)⊗Z_5.
Outputs: `runs/l1c_s3_fingerprint_output.txt` (F0-F4).

| id | necessary condition on any specialization v claimed to be the live class, or any element of S_0⊗F (F/Q_5 finite) | new? | finitely checkable? | status |
|---|---|---|---|---|
| **NC1** (lands in ker loc_5) | Write v = aP1 + bP2 with a, b ∈ O_F. Then b = −t·a exactly, so v(b) = v(a) + 1, and **b ≡ c_k·a (mod 5^k·a·O_F)** with c_k ≡ −t (mod 5^k). The values are c_1..c_12 = 0, 20, 70, 195, 820, 13320, 75820, 388320, 1169570, 3122695, 42185195, 188669570 (F2). Mod 5: loc_5 = (0, 2) (F1), so the strict Selmer group mod 5 is ⟨P1⟩ and a primitive v is ≡ unit·P1 | The mod-5 form was already recorded in the small-seed report. The 5^k table, and its reading as a statement about E(Q)⊗ (which needs W = S, i.e. N11), are new | yes, on any object that produces elements of E(Q)⊗Z/5^k | CERTIFIED_COMPUTATION (target side) |
| **NC2** (support rank = G-SUPPORT at the seed) | At the seed, "two rational directions" means all of W = S. Since t ∉ Q, w lies on no rational line Q_5·P with P ∈ E(Q) (F25 Prop 3.1, l.55-59). So if the outputs {v_i} are rational points, w can lie in their closed Z_5-span only when that span has **rank 2**. Two finite certificates exist. Positive: a nonzero 2×2 minor of the (P1, P2)-coordinates. Negative: exact proportionality of all coordinates, which is decidable for a finite set; an infinite family needs a proof | Seed-specific form of G-SUPPORT: the span must equal S, and the explicit basis is saturated at 5 | yes for rational-point outputs; no for p-adic-coefficient outputs (F31 C3: not closed under limits) | PROVED_DERIVED |
| **NC3** (G-COEFF at the seed) | A nonzero v ∈ S_0 has coordinate ratio b/a = −t, and t is transcendental over Q (FP16 Thm 2.2; F31 C2). So no finite vector with coordinates algebraic over Q, even up to a common 5-adic scalar, lies in S_0. Sanity check: no (a, b) ∈ [−50, 50]² \ 0 has v_5(a log P1 + b log P2) ≥ 8 (F3) | Instance of a recorded gate | yes, for each candidate | VERIFIED_FROM_SOURCE (F31); F3 is CERTIFIED_COMPUTATION |
| **NC4** (the live class is nonzero at the seed) | Rank 2 (N1) and Sha(E/Q)[5^∞] = 0 (N11) are exactly the hypotheses H6 and H7 that file 11 names as unavailable for CH Cor 5.1 (file 11 l.30-38). Both hold at the seed. So CH Cor B (CH l.182-184) gives κ_{α,α^{-1}} ≠ 0, spanning S_0 = Q_5·w, and Cor 5.1 gives κ_{α,α^{-1}} = (nonzero constant)·(P1⊗log_5P2 − P2⊗log_5P1). Consequence: **at this instance, the ledger's l.60 "CH_COR_5_1_SHORTCUT = UNAVAILABLE (needs V_p Sha(E/Q) = 0)" has its missing hypothesis met.** A construction identified with the live class must have a nonzero value at the seed | new at this instance; a calibration, not a mechanism (the input N11 comes from outside H9) | yes (a value is nonzero or it is not) | CONDITIONAL(on an admissible (K, χ) with L(E^K,1) ≠ 0 and L(E/K,χ²,1) ≠ 0: existence only, per file 11 H2 and F22 Remark 5.2.2; not checked for any explicit (K, χ)) |
| **NC5** (twist component) | For CH's g, the E-projected values of every element of 𝒫^♮_r on CH's branch are η_K-eigen under Gal(F'_r/K_0). Their E(K_0)⊗Q̄_5 component, and so their E(Q)⊗Q̄_5 component, is **0** (`01_TWIST_COMPONENT_DERIVATION.md`) | new (upgrades A2.2 from OPEN) | it is a derivation, not a computation | PROVED_DERIVED (not refereed) |

**Could the checks be run on the sealed tower?**
- **NC1-NC3: NOT RUN. BLOCKED at A2.3 and A3.2.** The tower has no descended output: "DESCENDED_OUTPUT_IN_E(Q)⊗Q_p = NOT DEFINED" (F26 §2, l.89; SEAL-05 l.41). The only weight-one value the construction has, the line-I same-root class 0, which in any case is CONDITIONAL on A1-A3.2, **passes NC1 and NC3 vacuously and fails NC2 (support rank 0) and NC4 (it is 0 where the live class is nonzero).** In other words, the known answer does not discriminate on line I, because the zero vector lies on every line. Its only discriminating content concerns the live branch, and the tower does not retarget there (LEDGER l.47-48).
- **NC5: RUN, as a derivation.** It is the only one of these checks that can be applied to the sealed object itself, because it needs nothing beyond the sealed ⋆-formula, the carrier diamond on the branch, and Galois-equivariance of π_E. Its outcome is that, under any Galois-compatible descent, the tower's CH-branch output fails NC4 at the seed at every finite level. The argument does **not** use the seed: it holds for every E and every p split in K. So the seed's specific data (NC1-NC4) were not needed to reach the one informative outcome. This matches F26 §4 (l.111-113), where BENCHMARK is excluded and "Its failure test cannot fail informatively."
- **Direct computation on raw finite-level points: not runnable.** The receptacle is Jac X_1(5·N_E). Its genus is on the order of μ(Γ_1(5N_E))/12 ≈ 2.8·10³¹ (F4); X_0(N_E) alone is ≈ 1.1·10¹⁵ (C8).
- **Target side: RUN** (C4-C6, F0-F3), CERTIFIED_COMPUTATION.

## §4. Deliverable (4): the eight admission gates on the proposal "calibrate H9 at the seed"

Gate definitions: F26 §3 l.96-106 and F31 SC6 l.82-87. The gate list is the one at LEDGER l.231.

| gate | definition (source) | at the seed | verdict |
|---|---|---|---|
| **G-DATUM** | name the new arithmetic datum: two rational directions, an independent Selmer or Sha bound, or a construction with a stated non-collapse test (F26 l.97) | Two rational directions P1, P2 (N1, N2) and an independent Sha bound, Sha[5^∞] = 0 (N11). Both come **from outside H9**, from the master certificate | **PASS as an input.** The datum exists, but H9 does not supply it |
| **G-MECH** | name the mechanism that supplies it, independent of the targeted conclusion (F26 l.98) | The mechanism that supplies the datum is Zywina's 2-descent together with the SW/Kato/Manin chain (N1-N11). This chain is κ-free and makes no use of H9. H9 supplies **no** mechanism: A1.3 is OPEN, A1.4 and A2.3 are BLOCKED, A2.2 has zero E(Q)-component on CH's branch (NC5), and A3.2 is BLOCKED (§2) | **FAIL.** This is the first failing gate in the listed order |
| **G-REUSE** | when reusing a stopped route, name the exact hypothesis or equation that changes (F26 l.99-100) | The proposal reuses line I, the sealed same-sheet tower. At the seed exactly one hypothesis changes: V_5Sha(E/Q) = 0, together with rank 2, which are H7 and H6 of file 11. That hypothesis belongs to the **printed CH route** (LEDGER l.60, l.72) and sits downstream of the point where the tower stops. No hypothesis of any stopped H9 route changes: A1.4 (wrong pair; LEDGER l.47-48), (H-ω) (SEAL-05 l.21-25), A-DICH (H17B 04), D1 (H17 09) and the terminal step "object → rational point" (LEDGER l.143-144) all stand as recorded | **FAIL** for H9. The changed hypothesis revives only CH's own printed Cor B / Cor 5.1 at this instance (NC4), and that route is not H9 |
| **G-SUPPORT** | descended outputs must be able to span two rational directions (F26 l.101; F25 Cor 3.2) | The tower has no descended output (F26 l.89). On CH's branch, every Galois-compatible descent has E(Q)-component 0 (NC5). The conditional line-I value is 0. The support rank is 0 wherever it is defined | **FAIL** |
| **G-AUX** | varying the auxiliary (K, χ) never supplies independence (F26 l.102; F25 §4) | The proposal does not rely on auxiliary variation. At the seed, every admissible (K, χ) gives a class on the same line S_0 = Q_5·(P1 − tP2), which is explicit (C5, F2) | **PASS** (not violated) |
| **G-WSHA** | give information about W (a rational lower bound), about V_pSha, or an argument that puts κ in W (F31 l.82-84) | At the seed, W = S and V_5Sha = 0 are **inputs** (N1, N11). The calibration uses them up and produces no new information about W or V_5Sha. κ ∈ W follows from N11 alone (LEDGER terminal (d), l.147-148; Castella Thm A(2)) | **FAIL** (nothing new) |
| **G-COEFF** | do not end in a finite algebraic-coordinate vector, and name the genuinely p-adic coefficient or limit mechanism, handling descent, control and the live branch separately (F31 l.85-87) | Clause 1: the intended coefficient field F_g is a finite extension of Q_5, outside the test (F31 l.61-63), so clause 1 is not violated. Clause 2: a limit mechanism is named (the Hida tower), but descent and control (A2.3), the live branch (A1.4) and the η_K component (NC5) are not handled | **FAIL** at clause 2 |
| **G-TEST** | a bounded failure test runs before any construction (F26 l.104) | A bounded test exists and was run: NC5, a derivation from sealed statements. Its outcome is that the tower's CH-branch output has E(Q)-component 0, so the tower **fails**. The seed-specific tests NC1-NC4 are written down, but they cannot be run on the tower (§3). The informative test does not use the seed, as F26 l.111-113 anticipates for a BENCHMARK | **PASS** (a test was run; the tower failed it) |

**Admission verdict: NOT ADMITTED.** The first failing gate is **G-MECH**. G-REUSE, G-SUPPORT, G-WSHA and G-COEFF (clause 2) also fail. G-DATUM passes only as an external input; G-AUX and G-TEST pass.
Scope note (VERIFIED_FROM_SOURCE, F26 §4 l.111-113): a per-curve calibration is the BENCHMARK option. The record excludes it by name under the operator's $1M-only rule and describes it as adding no arithmetic. This lane was assigned by the operator, so it is recorded as a calibration, not as a candidate.

## §5. Verdict (session 2)

    L1C_SEALED_TOWER                      = CALIBRATION_COMPLETE / NO_IDENTIFICATION
    SEAL_INSTANTIATION_AT_SEED            = AUTOMATIC (depends on E only via N_f = N_E; no arithmetic content)   [PROVED_DERIVED]
    BCPV_FRAME_AT_SEED                    = H-2.3 FAILS (N_f not square-free); H-3.3 FAILS (w = +1); (H-ω) FAILS for CH's g   [CERTIFIED_COMPUTATION / VERIFIED_FROM_SOURCE]
    TARGET                                = S_0 = Q_5·(P1 − tP2), v_5(t) = 1, −t ≡ 13320 (mod 5^6); mod 5: <P1>   [CERTIFIED_COMPUTATION]
    CHAIN A1                              = no failing operation; A1.3 (non-torsion) OPEN; A1.4 (live pair) BLOCKED (recorded)
    CHAIN A2                              = A2.2 CH-branch E(Q)-component = 0 under any Galois-compatible descent   [PROVED_DERIVED, unrefereed; NEW]
                                            A2.3 BLOCKED: missing Λ-adic MW control/descent map (bypassed at the seed by W = S; the bypass then fails at Ψ: NOT_APPLICABLE(at (H-ω)))
    CHAIN A3                              = A3.2 BLOCKED: missing weight-one specialization lemma in the tower's normalization
    VALUE AT 𝔭_CH (if A1-A3.2 existed)    = 0 (same-root κ_{α,β^{-1}}; and, independently, the η_K component)
    IDENTIFICATION WITH E(Q)⊗Q_5          = NOT PROVED. Wherever a value is defined it is 0: support rank 0, not 2
    NEW NECESSARY CONDITIONS              = NC1 (5^k fingerprint), NC2 (support rank 2 = S), NC3 (transcendental ratio), NC4 (κ_{α,α^{-1}} ≠ 0 at the seed; CH Cor 5.1 shortcut's missing H7 met), NC5 (η_K component)
    CHECKS RUN ON THE TOWER               = NC5 only (as a derivation); NC1-NC3 BLOCKED at A2.3/A3.2; raw points not computable (genus ~ 2.8e31)
    ADMISSION ("calibrate H9 at the seed") = NOT ADMITTED; first failing gate G-MECH

**First open statement (chain order).** A1.3: whether 𝒬_∞ is non-torsion after localization at 𝔭_CH. This is the sealed non-claim at SEAL-05 l.58-60, and it is OPEN.
- The first BLOCKED operation is A1.4. The missing object is an h-direction in the collapsed carrier (LEDGER l.47-48).
- The first missing object for an E(Q)-valued output is a map from the η_K-eigen E-projected CH-branch values to (E(Q)⊗Q_5)⊗̂R_g that is compatible with the Kummer maps. No Galois-compatible map of this kind is nonzero on them (NC5). A non-equivariant or untwisting identification is not excluded by this lane.

**Provisional versus independently verified.**
- Independently verified upstream: CERT N0-N11, all merged records; the seal (two assembly audits); the ledger entries cited.
- Verified in session 2 against source: SEAL-00 l.18-41; SEAL-01 l.60-119; SEAL-05 l.1-60; LEDGER l.1-237; F20; F25 l.30-110; F26 l.70-115; F31 l.40-101; file 11; CERT l.1-84; BCPV l.457-486; CH l.155-161, l.182-184.
- CERTIFIED_COMPUTATION, author-run only with no second implementation: C0-C8 and F0-F4. These are small PARI checks.
- PROVISIONAL, **not refereed**: NC5 / `01_TWIST_COMPONENT_DERIVATION.md`, in particular step 3 (the tame diamond acts by a scalar on CH's local factor of the primed carrier) and step 1 (the factor-1 diamonds are trivial after π_E). The same applies to the session-1 citation line numbers not listed above (H17, H17B, L3-01, F09, F12, F22).
