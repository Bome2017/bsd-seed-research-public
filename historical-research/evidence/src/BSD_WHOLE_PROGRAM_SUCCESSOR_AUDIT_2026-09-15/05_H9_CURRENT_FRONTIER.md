# 05 — H5 / H6 / H8 / H9 general-bridge branch: current frontier and its custody

Date: 2026-09-15.

## Custody — corrected 2026-09-15 by the operator

**Superseded claim (mine, 2026-09-15):** "the entire live frontier exists on disk in exactly one
place … it is not sealed." That was **accurate for the iMac filesystem searched and wrong as a
statement about the project.**

**Operator correction, authoritative:** the **Google Drive checkpoint is current through H9R16-C**,
has been verified and repaired by the operator, and includes the authoritative H9R15/H9R16
supersession block. The mathematics is **not** single-copy and is **not** at risk.

**What this actually is: a local-corpus synchronization problem.**

    AUTHORITATIVE COPY   = Google Drive checkpoint (current through H9R16-C, verified + repaired)
    LOCAL CORPUS         = OUT OF SYNC — zero H9 material in 04_RESEARCH_OBJECTS
    LOCAL Downloads .docx= slightly truncated (tail ends mid-word); NOT the repair source
    LOCAL Downloads .md  = badly truncated at end of H9R2; NOT the repair source

**The repair, as directed:** export the **current Drive checkpoint** into the local research-object
corpus and seal that snapshot. **Do not reconstruct the canonical local copy from the truncated
Markdown, nor from the slightly truncated `.docx`.** The recovered text I extracted to
`_work/RECOVERED_H5_H9_CHECKPOINT_FULL_TEXT.txt` is therefore **evidence of the local drift only** —
it is explicitly *not* a repair source and must not be sealed.

### The local drift, measured

| Local artifact | SHA-256 (16) | Extent |
|---|---|---|
| `Downloads/BSD H5-H6-H6A-H6B Checkpoint — 2026-09-14.docx` | `3e5741f33bd1dadaf` | H5 … H9R16-C + supersession block; tail truncated mid-word |
| `…— 2026-09-14-2.docx` | `f05fc78f99873496` | duplicate download; extracted text byte-identical |
| `Downloads/BSD_H5_H6_H6A_H6B_checkpoint_2026-09-14.md` | `e743863b3a8ee656` | **truncated at end of H9R2** — drops H9R3–H9R16-C entirely |
| `04_RESEARCH_OBJECTS/` | — | **no H9 material at all**: zero hits for `H9R…`, `Castella`, `BCPV` |

The live hazard that remains is **local**: a reader working only from the iMac corpus, or from the
`.md`, concludes the frontier is H9R2 `ONE_INTERPOLATION_MAP_MISSING`. It is H9R16-C, fourteen
audits later. Sealing the Drive export into the corpus removes that hazard.

## RECONCILED H9R16-C STATUS — operator merge of four lanes, 2026-09-15

**Provenance.** This section records the **operator's** reconciliation of four parallel H9 lane
reports. The lane material was located 2026-09-15 at
`~/Library/Mobile Documents/com~apple~CloudDocs/Archive.zip`
(SHA-256 `3b446f3f5c0cef547cb6782bcaab3016576fb189fda398ef4115907ab2a79159`, 11,384,245 bytes,
210 entries), extracted read-only to `_work/lanes/`. It contains all four lane directories **and the
primary PDFs** — BCPV 2409.08645, MRS math/0609066, KLZ17 1503.02888, DR22 2207.01314,
Castella–Hsieh 1809.09066, Hida (Control/Limit MW), Howard 1202.6358, Cais 1209.0046, BSV22,
Longo–Vigni, **Ohta 1999 Compositio 115** — plus `bcpv_src.tgz`, `klz2_src.tgz`, `dr22_src.tgz`,
`mrs_src.tgz`. **This is a major custody gain: the H9 primary literature is now local.**

**Screening performed by this session (2026-09-15).** The four `00_VERDICT.md` files were read and
checked against the reconciliation above. **Every substantive claim matches**, including: Lane 1
`STOP_A` / `C_W/w_DICTIONARY = CLOSED` with `W^BCPV = ⟨c_r⟩^{-1}α_r^{-1}w_rα_r` and
`α_r^{-1}π_r^{r+1}α_{r+1} = ⟨u_r⟩^{-1}ϖ_{1,*}`; Lane 1 `C1-d` `U'_p ↔ U(p)`, `U_p ↔ U*(p)`, with
H9R12's dictionary refuted as the ι_ζ-dictionary twisting Galois by `1 + k + ε_N`; Lanes 2 and 4
independently on the type-A receptacle being `|G_r|` too large; Lane 2's four mandatory typing
corrections (MRS sign `c_r^{+1/2}`, type B, tame `ε_g^{-1}` on factor 3, `π_r^*P_r` target); Lane 2
`(v)` type B involves no corestriction; Lane 2 `C2_REDUCES_TO_FORMAL_NATURALITY`; Lane 4 "not
killed". **Three caveats surfaced in the screen are recorded in §"Screening caveats" below.**

    H9R16C_STATUS = RETYPED_AND_REDUCED_TO_FINITE_MODIFIED_PAIRING_COMPATIBILITY
                    (H9R16-C is NOT killed; the target is smaller than what was sent out)

    C_W_w_NATIVE_DICTIONARY        = CLOSED
    C_OLD_H9R8_MRS_RECEPTACLE      = SUPERSEDED / WRONG_TATE_MODULE_FOR_BCPV_DAGGER
    C_CORRECT_RECEPTACLE           = TYPE_B_GROUP_RING_MRS_TWIST
    C_MRS_LATTICE_CHARACTER        = +1/2   (yielding BCPV's -1/2 Tate twist)
    C_TAME_Gc_TWIST                = REQUIRED
    C_FIELD_CORESTRICTION          = NOT_USED in the preferred fixed-base formulation
    C_RETYPED_KUMMER_NATURALITY    = CLOSED / FORMAL
    C_POINT_TOWER_DISTRIBUTION     = OPEN
    FIRST_EXACT_NONFORMAL_STATEMENT= MPC_r(N_{r+1,r}) with explicit central tame/diamond factor d_r
    D4_UNSPECIALIZED_POINT_KUMMER_REALIZATION = FORMAL_BUT_NOT_YET_WRITTEN
    COMMON_LEVEL_TO_NATIVE_LEVEL_W_NORMALIZATION = OPEN_BOOKKEEPING  (Lane-1 "R2")
    G_BIG_KUMMER_TRACE             = DOWNSTREAM

### What survives as proved

Lane 1's model dictionary is retained (its proposed receptacle/transition is **not**):

        W^{BCPV}_{Np^r} = ⟨c_r⟩^{-1} α_r^{-1} w_r α_r
        α_r^{-1} π_r^{r+1} α_{r+1} = ⟨u_r⟩^{-1} ϖ_{1,*}

The discrepancy is a **rational central diamond** — harmless once explicitly normalized.

The apparent clash `U'_p ↔ U(p)` vs `U'_p ↔ U*(p)` is **not a contradiction**: the first is the
Galois-rational `α_r`-bridge needed for a Kummer argument, the second the Hecke-preserving comparison
through the other modular-curve identification, which KLZ says carries an extra Galois/diamond twist.
**The old H9R12 shorthand is superseded, not Lane 1.**

### Type corrections (genuine corrections to the checkpoint)

- The old H9R8 receptacle `I_r^† ⊗_Z J_r` is **wrong**: its Tate module is `|G_r|` times too large.
  BCPV's dagger construction is a tensor **over the group ring**, not over `Z`. Correct object is the
  type-B/MRS form, schematically `I_r ⊗_{Z[G_r]} V_r`.
- **MRS sign:** the twist acts via `σ^{-1} ⊗ σ`, so the lattice must carry `c_r^{+1/2}` for the Tate
  representation to carry BCPV's `⟨χ⟩^{-1/2}`.
- A **tame `g^c` twist** is required: a dagger-only object over `K₀ = Q(μ_p)` is insufficient; the
  `ε_g^{-1}` contribution on the third factor must be built into the carrier.
- **Corestriction disappears.** On the correctly typed fixed-base type-B object, level change is not
  a cyclotomic corestriction; the cyclotomic datum is carried by the compatible lattice cocycle
  `pr_r ∘ c_{r+1}^{1/2} = c_r^{1/2}`. The checkpoint's "descent/corestriction or Shapiro" was too
  loose. Preferred: **fixed-base descent + group-ring change, no field corestriction.**

### The Kummer square is no longer the gate

Once objects and the point homomorphism are typed correctly, the square commutes by **ordinary
Kummer naturality**. So `C_KUMMER_TRANSITION_SQUARE = OPEN` is retired:

        OLD_FROZEN_C_SQUARE                  = SUPERSEDED_BY_TYPE_CORRECTION
        RETYPED_FIXED_BASE_KUMMER_NATURALITY = PROVED / FORMAL
        POINT_CLASS_TOWER_COMPATIBILITY      = OPEN

The residue is compatibility of the specific modified trace points/classes — not naturality itself.

### The one live finite-level identity

Lane 2's `MPC_r(ν)`, Lane 4's `(⋆_r)` and Lane 3's `E′(b)` are three formulations of nearly the same
missing piece. With `A_r = W_{N_g p^r}^{-1}(U'_p)^r` and the auxiliary-factor norm element

        N_{r+1,r} = Σ_{k ∈ ker((Z/p^{r+1})^× → (Z/p^r)^×)} ⟨k⟩

the target on `e'_ord` auxiliary cohomology is

        ϖ_1^* A_r ϖ_{1,*} = d_r · A_{r+1} N_{r+1,r}
   ⟺   ⟨ϖ_{1,*} y, A_r ϖ_{1,*} z⟩_r = d_r ⟨y, A_{r+1} N_{r+1,r} z⟩_{r+1}

with `d_r` an explicit central diamond/unit from the `W/w` and tame-level conventions.

This reconciles Lane 2 vs Lane 3: **Lane 3 is right** that the Λ-adic modified pairing is already in
the literature (KLZ Thm 7.2.3(v), canonical perfect Λ-pairing, attributed to Ohta 2000; KLZ's Galois
module differs from Ohta's by the model-dependent `1 + k + ε_N` twist); **Lane 2 is right** that the
finite-level coefficient-extraction identity with the precise norm element is not written in their
sources. So this reads as a **finite-level unpacking of a published Λ-adic pairing plus the
group-ring projection**, not a new deep arithmetic theorem.

### Formal companion D4

        Kum(P_r^{tr,†}) = Contr^mod_r( AJ_et(Δ_r^ord) )

on the corrected type-B/tame-twisted object. Not found printed unspecialized, but all four lanes
point to it being formal from étale Abel–Jacobi functoriality under algebraic correspondences.
**Treat as a write-the-proof obligation, not an unknown mechanism.**

### BCPV (4.9): record, do not use

    BCPV_4_9_CONSTANT = APPARENT_PRINTED_TYPO; 1/p PRODUCES p^2 ERROR;
                        INVARIANT_DR22_LEMMA_2_8_ROUTE_PREFERRED

**This is the one item this session verified independently.** `G_r` is the `p`-Sylow of
`((Z/p^r Z)^×)^3`; for odd `p` the `p`-Sylow of `(Z/p^r)^×` is cyclic of order `p^{r-1}`, so each
factor contributes kernel `p` and `|ker(G_{r+1} → G_r)| = p^3` for **every** `r ≥ 1`. After `G^{-1}`
the fibre sum contributes `p^3`; the printed `1/p` leaves net `p^2`, while `1/p^3` leaves net `1`.
This reproduces the two lanes' finding and the operator's rerun — a **third** independent
confirmation. Receipt: `_work/bcpv_49_scalar.py`.
**No erratum is to be published from this project.** DR22 Lemma 2.8 is the invariant transition and
does not have the problem; the coordinate formula is not needed.

### Screening caveats found by this session

1. **KLZ 7.2.3(v) verified verbatim, and it is Λ-adic — not finite-level.** Local KLZ17 prints
   *"Theorem 7.2.3 (Ohta, [Oht00])"*, part (v): *"There is a canonical perfect pairing of `Λ_D`-modules
   `H¹_ord,par(Np^∞) × H¹_ord,par(Np^∞) → Λ_D` with respect to which the `T_{Np^∞}`-action is
   selfadjoint, and the modules `F^±` are orthogonal complements."* Its proof paragraph reads
   *"This is equivalent to Corollary 1.3.8 and Corollary 2.3.6 of [Oht00]"* and pins the model twist
   exactly: KLZ's modules *"coincide (as `Λ_D[G_Q]`-modules) with Ohta's modules twisted by the
   character `1 + k + ε_N`"*. So the operator's reading is confirmed word for word — **but the
   printed object is the inverse-limit pairing at a fixed tame level `N`.** The MPC target is a
   **finite-level** identity at `r`, `r+1` and native level `N_g`. The descent from (v) to MPC is the
   group-ring/coefficient-extraction step, i.e. the actual work.
2. **Ohta Part I is local and does NOT contain the cited corollaries.** `Ohta1999_Compositio115`
   (pp. 241–301) has **zero** occurrences of "1.3.8"; its "2.3.6" is an *equation* number, not a
   corollary. The KLZ citation `[Oht00]` is therefore genuinely Part II (Math. Ann. 318). Ohta II
   remains un-located; per KLZ's own "equivalent to" phrasing it is needed only for the internal
   proof or a finer finite normalization, not conceptually.
3. **Lane 2's `ν` is explicitly conditional.** Its verdict reads: *"expected
   `ν_{r+1} = Σ_{k≡1 mod p^r}⟨k⟩`; **derived only under the group-ring-pairing hypothesis**"*. This is
   the same element as the operator's `N_{r+1,r}` (the sum over `ker((Z/p^{r+1})^× → (Z/p^r)^×)`), so
   the "derive it, don't guess it" instruction is load-bearing rather than stylistic.
4. **A second `p^3` appears in Lane 4, distinct from BCPV (4.9).** Lane 4 §1: on the invariant
   subvariety that would repair the type-A receptacle, *"the frozen transition `s_r⊗ϖ_*` is
   `p^3·ϖ_*`, while DR22 L2.8 has no constant."* Type B avoids it, but it should be confirmed that
   this `p^3` is not silently re-entering through `d_r`.
5. **Scope limit on BSV22 (Lane 3).** BSV22 (109) is integer-weight specialization at the fixed level
   `Γ_1(N) ∩ Γ_0(p)` and **does not reach `p`-power levels** — not usable for the tower.

### Next step as directed by the operator

Do **not** advance the four lanes independently. One session proves the finite identity from
KLZ / Ohta / DR22; a second acts as hostile referee afterwards. Requirements: derive `N_{r+1,r}`
(do not guess it); compute `d_r`; include the `N → N_g` tame-level pushdown; **do not use BCPV (4.9)**;
use KLZ 7.2.3(v), perfect control, DR22 Lemma 2.8 and Lane-1's `α_r`/`W`/`w` dictionary; prove D4 in
the same packet after MPC; conclude the typed point relation

        ϖ_{1,*} Q_{r+1} ∘ (1 ⊗ N_{r+1,r}) = d_r · π_r^* Q_r.

If that passes and `d_r` is an invertible diamond, **H9R16-C is effectively closed after
renormalization.**

**Ohta 2000 Part II** (Math. Ann. **318** (2000) 557–583, DOI 10.1007/s002080000119): bibliographic
record clear, no clean open PDF found. KLZ states its Thm 7.2.3 is equivalent to Ohta's Cor. 1.3.8
and 2.3.6, so Ohta II is desirable for the exact finite normalization but **no longer a conceptual
blocker**.

---

## Frozen status, as recorded in the document's own authoritative supersession block


The final block is explicitly "authoritative over earlier historical frontier statements in
H9R14–H9R16 where they conflict".

    H5_STATUS    = MW_RATIONALITY_STILL_INDEPENDENT
    H6_STATUS    = UNRESOLVED        (do NOT revert to ONE_MOTIVE_ROUTE_KILLED)
    H6A_STATUS   = UNRESOLVED        (do NOT revert to ARITHMETIC_SUPPORT_VANISHES)
    H6B_STATUS   = NOT_RUN / OPEN
    H7_STATUS    = V_P_SHA_REMAINS_OBSTRUCTED
    H8_STATUS    = SYSTEM_IDENTIFICATION_PRECEDES_PRIMITIVITY
    H8R2_STATUS  = RANK1_MODIFIED_SELMER_SYSTEM_IS_COMPATIBLE; MW_SHA_SPLIT_STILL_UNRESOLVED

    H9R15_STATUS   = LOCAL_WEIGHT_ONE_ROUTE_OPENED                       ← closed locally, frozen
    H9R16A_B_STATUS= FINITE_LEVEL_MODIFIED_BALANCE_CLOSED_AFTER_REQUIRED_A_r_TWIST
    H9R16C_STATUS  = POINT_TRANSITION/KUMMER_SQUARE_OPEN                 ← THE LIVE TARGET

The whole branch is one obstruction restated fourteen ways: **the Selmer / Mordell–Weil divide.**
Galois-cohomological identities characterize the class; they do not prove it is the Kummer class of
a rational point. H9R16-C is the first version of that divide reduced to a *bounded, checkable*
question.

## H9R15 — closed locally (do not reopen)

At the actual Castella–Hsieh p-regular CM weight-one point of the **primitive/native** g-Hecke
algebra, Dimitrov's local theorem makes `T_{q_g}` a DVR. For the chosen minimal prime `a`:
`a·T_{q_g} = 0`, so `T_{q_g} ≅ (T/a)_{p_g} = A_{p_g}`; a DVR is normal, so `A_{p_g} ≅ R_{p_g}`.
Both H9R14 base-change gates therefore vanish **before** any congruence-generator argument:

    GATE_A_AT_WEIGHT_ONE = CLOSED;  a·T_q = 0
    GATE_B_AT_WEIGHT_ONE = CLOSED;  A_p = R_p
    LOCAL_BRANCH_KUMMER_SATURATION  = PROVED
    GLOBAL_BRANCH_KUMMER_SATURATION = STILL OPEN — but no longer required to reach this point
    NATIVE_LEVEL_RESTRICTION = ESSENTIAL

`NATIVE_LEVEL_RESTRICTION` is load-bearing: working at an artificially enlarged common tame level
reintroduces the components this argument removes. The `g* = θ_{ψ^{-1}}` side runs the same
p-regular CM-split argument.

## H9R16-A/B — closed, but only after a twist that corrects the earlier formulation

The earlier plain-`Π_Z` same-primed formulation was **wrong** and is superseded. With

    A_r = W_{N_g p^r}^{-1} (U'_p)^r

the raw geometric Rosati/transpose adjoint `ρ_r : (T'_r)^op → T_r` satisfies `ρ_r(u')·A_r = A_r·u'`,
so the **modified** adjoint is trivial: `ι_r(u') = A_r^{-1} ρ_r(u') A_r = u'`. The correct functional is

    Φ_r^mod(t₂, t₃) := Π_{Z,*}( (1 ⊗ t₂ ⊗ A_r t₃) Δ_r^ord ),     Φ_r^mod(t₂u', t₃) = Φ_r^mod(t₂, u't₃).

    G_BALANCED_HECKE_DUALITY = PROVED for the A_r-twisted modified functional
    G_COEFFICIENT_RETENTION  = finite-level balanced carrier well-typed; TOWER/BIG POINT OPEN

Retain permanently: `g^c` is the **dual/nebentype-twisted** third factor; never identify the two raw
geometric Hecke actions naively.

## H9R16-C — the live target, in its two gates

    C_W/w_DICTIONARY            = OPEN
    C_POINT_NORMALIZATION       = OPEN
    C_KUMMER_TRANSITION_SQUARE  = OPEN
    C_POINT_TOWER_DISTRIBUTION  = FORMAL after the square + global Kummer injectivity
    RAW_Pi_Z_LEVEL_COMMUTATION  = NOT REQUIRED if the realization square closes

**C1 — the W/w normalization.** Compute the literal relation between BCPV `W_{N_g p^r}` and Hida
`w_r`: central diamonds, Galois action, inverse conventions, `U_p`/`U'_p`, level-dependent units.
Literal equality is *not* required; a central/invertible discrepancy `δ_r` absorbed into the
normalization suffices. This is bookkeeping with a definite answer — the reason it ranks first.

**C2 — the Kummer transition square.** On a fixed base `K₀ = Q(μ_p)` (or an explicitly
Shapiro/Weil-restriction-equivalent model):

    P_{r+1}^{tr,†} ──Kum──► H¹(K₀, T_{r+1}^{tr,†})
         │ τ_r^MW                    │ τ_r^et
         ▼                           ▼
    P_r^{tr,†}     ──Kum──► H¹(K₀, T_r^{tr,†})

Both verticals must **explicitly** carry: the modular/Hida transition, the dagger/group-ring
projection, and the cyclotomic descent/corestriction (Shapiro) data. The document is emphatic that
these must not be merged into one untyped arrow, and that a fixed-base formulation is preferred over
silently identifying Hida's fixed-base transition with raw maps between `H¹(F_{r+1},−)` and `H¹(F_r,−)`.

If the square commutes, then `Kum(τ_r^MW P_{r+1} − P_r) = 0`, and global Kummer injectivity on the
actual completed MW/dagger abelian variety forces `τ_r^MW P_{r+1} = P_r`. This use of injectivity is
legitimate *now* precisely because both sides are constructed geometric objects — it was not
legitimate at H9R3–H9R11, and that distinction is the whole content of the last ten audits.

**Sources retained.** BCPV prove `(ϖ_{1,*})^{⊗3} Δ_{r+1}^{ord} = (U'_p)^{⊗3} Δ_r^{ord}` and normalize
the étale inverse limit by invertibility of `U'_p`. Hida constructs the genuine w-twisted point
transition over **Q**, Hecke-equivariant for `T(n)` away from `Np` and `U(q)` for `q | Np`, in a
commutative Kummer diagram on completed ordinary MW groups. **H9R16-C asks only whether the exact
BCPV normalization matches the exact Hida point transition after the dagger/group-ring packaging.**

## Explicitly downstream — must not be used to patch C

Inverse-limit identification; density; H9R15 localization; global f-branch extraction; the
authorized classical weight-two f-projection; weight-one coefficient evaluation; the big Kummer
trace identity. Also: do **not** invoke a nonexistent general weight-one Hida MW-control theorem if
coefficient specialization suffices.

## Relationship to the H41 program

None, logically. H41/BSD(2) is an explicit2-descent + analytic-seed program on one twist family;
H5–H9 is a general Mordell–Weil-rationality bridge. They share no theorem, no Lean file and no
input. They compete only for operator attention. Do not let a status from one leak into the other.
