# BSD successor master status and dependency map — 2026-09-15

**Successor to** `H41_BSD_MASTER_STATUS_AND_DEPENDENCY_MAP_2026-09-13.md`
(SHA-256 `466f1544bb4ca71fe2e90e0f49b64a65a355e14ac848f145f8f9dae9999e9405`), which is **not
overwritten and remains valid for everything it states as of its own date.** This file supersedes it
only where later filesystem evidence exists, and says so explicitly each time.

**Reconstruction and synthesis only.** No theorem proved, no proof audited, no object sealed,
resealed or edited, no Lean run, no Aristotle launched, no agent spawned, no computation rerun.

## What changed since 2026-09-13, in one paragraph

Two things, and they pull in opposite directions. **Mathematically**, the negative H41 branch moved
forward on the route the September 13 map ranked *second*: ADDENDUM_017 proves `κ` odd
(referee-audited) and, through it, the negative H41-W seed bit in positions E and B, while also
promoting two former operator-fixed inputs to proved lemmas. The route the map ranked *first*
(R-X) had already hit a stop condition on September 13. **Custodially**, the entire H5–H9
general-bridge branch — fourteen further audits ending at the live target H9R16-C — exists only as
an unsealed Word document in `~/Downloads`, whose Markdown export silently drops the whole frontier.

## Verification tiers (unchanged from the predecessor)

**L** Lean theorem with preserved rebuild/type/axiom receipts · **A** audited ordinary proof ·
**T** imported conventional theorem with stated source hypotheses · **M** definition/model
resolution · **E** computational evidence / rigorous finite certificate · **D** design-ready ·
**O** open.

New tier used below: **A-ref** = ordinary proof audited by a *fresh independent agent referee under
a no-repair mandate*, **not machine-checked, and not operator-re-audited**. This is the tier of
everything in ADDENDUM_017. It is stronger than an unreviewed draft and weaker than **L**.

Edge convention: **SOLID** = proved at the stated tier · **DASHED** = open · **DOTTED** =
conditional or imported.

---

# TRACK A — H41 explicit algebraic / formal chain

**Status: COMPLETE at its tier. Closed asset library. Do not re-enter.**

Every item below is Lean-certified with preserved external rebuild receipts, on the family
`SDyadic.Params ε m q` + `SDyadic.H41 ε m` + prime instance.

| Result | Statement | Tier |
|---|---|---|
| `F_ff` | sharp finite-field order-4 point-count criterion | L |
| `S_dyadic` | explicit all-places φ-set; dual set | L |
| H41 saturation | `LocalKummerAll ↔ Cov ℚ`; `GlobalSet = SelmerSet`; index 2 | L |
| `Descent.delta_descent` | coordinate δ multiplicative; range = covering-realized subgroup | L |
| `P01.p01_family_two_torsion` | exact rational 2-torsion on both curves | L |
| `P03a`–`P03e` | point maps, additivity, kernels, composites, `ker δ = im φ̂` | L |
| `P04a`–`P04c` | cokernels, corrected ranges, `E_q(Q)/2E_q(Q) ≅ C₂` | L |
| `R0`, `R1` | abstract proper-height torsion; duplication-height | L (×2) |
| `GateR.h41_rank_zero` | `Module.rank ℤ … = 0` | L |
| `GateRFinite.h41_finite` | `Finite ((P01.Ecurve ε m q).toAffine.Point)` | L |

**Boundary that must never be relaxed:** these are theorems about mathlib's *affine point group*.
They contain no `H¹`, no Sel₂, no Sha, no L-function, no BSD object. `SelmerSet` is an explicit
realization, not a cohomological certification.

Conventional companion (tier A/T, two independent ordinary audits): **Composition Theorem A** —
actual `Sel₂(E_q) ≅ C₂`, rank 0, `Ш(E_q)[2^∞] = 0` on H41.

---

# TRACK B — H41 analytic / modular-geometric completion

**Status: ADVANCED on 2026-09-14/15. This is where the program actually moved.**

## B.1 The target

    λ = L(E,1)/Ω_{E,R} ≠ 0,   v₂(λ) = −2
    ⟺  H41-W:  u_ℓ ∈ 2^a U₀ ∖ 2^{a+1} U₀
    ⟺  (negative branch, bit N):  2^{−a} u₃ ≠ 0 in U₀/2U₀  ⟺  4λ odd  ⟺  w₃ ≡ 1 (mod 2)

## B.2 The four-position ledger — **superseded rows marked**

| Position | Missing assertion | Integral form | 2026-09-13 | **2026-09-15** |
|---|---|---|---|---|
| Negative **E** | `[2]P_c ≠ O` (t=4) | `w₃ ≡ 1 (2)` | OPEN | **PROVED** — Thm D, cond. on `E₀=E` + (K2)–(K5) |
| Negative **B** | `P_c ≠ O` (t=2) | `w₃ ≡ 1 (2)` | OPEN | **PROVED** — Thm D′, cond. on `E₀=B` + (K2)–(K5) |
| Negative **F** | retained `z` odd | `w₃ ≡ 2 (4)` | OPEN | OPEN — *provably out of reach of this mechanism* |
| Negative **G** | `P_c ≠ O` (t=2) | `w₃ ≡ 1 (2)` | OPEN | OPEN — *provably out of reach of this mechanism* |
| Positive branch (all) | — | `8λ ≡ 2 (4)` | BLOCKED | BLOCKED — untouched |

At F and G, `n_F = n_G = m−2` is odd so `Φ[2^∞] = 0`: the component group at 2 is blind there,
whatever `κ` is. F additionally needs a mod-4 statement no mod-2 residue argument can produce.
**This is a proved limitation of the κ route, not an unfinished computation.**

## B.3 The ADDENDUM_017 chain (all tier A-ref)

    Theorem G (graph lemma)  #S = (2^m+4)/3;  e_x ∈ {1,3}, exactly two with e_x = 3;
                             Σ 1/e_x = 2^m/3;  Φ_J ≅ Z/3·2^m cyclic;  sp_J(c) of exact order 2^m
                             ⇒ proves Input 1 and (K1), formerly operator-fixed
    Theorem A  B − A = 3(2^{m+1} − 1);  every slope s_x ∈ {3(2^{m+1}−1), 2^{m+1}−1} is ODD
    Theorem B  F_p = 2^A U^{s_x} u_x  ⇒  res_x(ω̄_η) = s_x ≡ 1;  res_x(ω̄_f) = ±s_x ≢ 0 (mod 2)
    Theorem C  (i) toric residue map ρ_J surjective, kernel = residue-free differentials
               (ii) **κ is ODD**;  hence κ ≥ 1 and q*(ξ_E) ≠ 0
    Lemma 4.1  im Φ(q) = gcd(κ, n_E)·Z/n_E ;  κ odd ⇒ Φ(q)(Φ_J[2^∞]) = Φ_E[2^∞]
    Lemma 4.2  n_E = 4(m−2), n_B = 2(m−2), n_F = n_G = m−2; m odd ⇒ Φ_E[2^∞]≅Z/4, Φ_B[2^∞]≅Z/2,
               Φ_F[2^∞] = Φ_G[2^∞] = 0
    Theorem D / D′  ⇒ the negative bit (N) in positions E and B

## B.4 The gate — **PARKED 2026-09-15 pending new 2-primary machinery**

### B.4.1 New proved theorem: `E₀ = E₁` on negative H41

**Uniformly, for every negative H41 base, the `X₀(N)`-optimal and `X₁(N)`-optimal curves coincide.**
Tier **A** (ordinary proof, this program, 2026-09-15; not machine-checked, not externally refereed).

    |Σ(2p)| = (p−1)/2 = 2^{m+1} − 1  is ODD          [Ling–Oesterlé, Astérisque 196–197, Thm 1, p.172]
      -> E₀ ∩ Σ has odd order                        [Vatsal 2003, Remark 1.8: E₁ = E₀/(E₀ ∩ Σ)]
      -> E₀ → E₁ would be an odd-degree isogeny in C
      -> C has NO odd rational isogenies             [retained Stage II theorem]
      -> E₀ ∩ Σ = 0  ->  E₀ = E₁.                                                            ∎

The Shimura-order step is uniform in `m`; the computation in
`H41_VERTEX_IDENTIFICATION_KILL_GATE_2026-09-15/_work/shimura_order.py` reproduces Ling–Oesterlé's
own **Corollary 3** exactly (all 19 values of `N` with `|Σ(N)| = 1`) and is a control, not the proof.

**Effect.** The `X₀`-vs-`X₁` ambiguity — the thing that makes Vatsal's conductor-11 example
(`E* = X₁(11) ≠ X₀(11)`) the standard cautionary tale — **does not arise on negative H41.**

### B.4.2 The exact remaining target

By Česnavičius (`manin_v3` Thm 1.2 = Thm 2.13) the Manin constant is `±1` for squarefree `n` — this
**upgrades** the record's "odd Manin constant" — and optimality gives `H₁(X₀(N),Z) ↠ H₁(E₀,Z)`.
Hence exactly `L(E₀) = Λ_f`, the modular-symbol lattice. With `L(E) ⊂ L(B) ⊂ L(F), L(G)` of indices
`1, 2, 4, 4`:

        TARGET W:   [ Λ_f : L(E) ]  divides  2      ⟺  E₀ ∈ {E, B}      ← sufficient for H41
        TARGET S:   Stevens' conjecture at 2        ⟺  E₀ = E           ← stronger than needed

### B.4.3 Status: PARKED

    VERTEX_ROUTE = PARKED pending new 2-primary machinery

A bounded primary-source audit (2026-09-15) returned `NO_PRIMARY_SOURCE_EXCLUSION_FOUND`. F and G
are not excludable by any located result, and the reason is structural, from the sources' own stated
hypotheses:

| Mechanism | Primary source | Fails because |
|---|---|---|
| Shimura subgroup | Ling–Oesterlé Thm 1; Vatsal Thm 1.1, Rmk 1.8 | gives `E₀ = E₁` and no more; Thm 1.1 needs `n` odd; `μ₂ ≅ Z/2` over **Q** |
| Eisenstein Hecke action on `Φ` | Ribet, via Edixhoven, Astérisque 196–197 pp.159–170 | forces `a_ℓ ≡ ℓ+1 mod 4` at E, mod 2 at B, and **nothing at F or G** — vacuous exactly where needed |
| Multiplicity one mod 2 | Mazur–Ribet, same volume pp.215–256 | requires **odd `p`** and **absolute irreducibility**; footnote 1 explicitly excludes Eisenstein primes. Same barrier that stopped R-X |
| Manin constant | Česnavičius `manin_v3` Thm 1.2 | `c = ±1` for the optimal curve whichever it is — vertex-blind |
| Optimality index bound | Stein–Watkins conj.; Byeon–Kim Acta Arith. 165.4 (2014) Thm 1.1 | bounds `E₀`↔`E₁` (degree **1** here, already proved); **no analogue for `E*`↔`E₁`** |
| Vertex identification by computation | Cremona `ecdata` | exhausted: conductors in range are the four already resolved; next is `N = 1048574` |

**Unparking condition:** either Stevens' conjecture at 2 for a class with no odd isogenies, or a
bound `[Λ_f : L(E)] | 2` by a mechanism that does **not** pass through `Φ[2^∞]` (which vanishes at
F and G, by Lemma 4.2, `m − 2` odd).

**Alignment, retained.** Should the target be proved: the negative positions with `a = 0` — the Zhai
transfer condition — are exactly E, B, G, and ADD_017 Thms D/D′ cover E, B. So `E₀ ∈ {E,B}`
discharges the seed bit **and** the transfer applicability together, giving negative-branch BSD(2)
modulo (K2)/(K5) hardening.

## B.5 Still-standing analytic obligations

- Positive H41-W (`8λ ≡ 2 mod 4`) — BLOCKED, entirely untouched by ADDENDUM_017.
- Surviving `a > 0` transfer cases (negative F; positive B/F/G) — need exclusion or an alternate
  transfer/direct twist theorem.
- Eight exact λ certificates (62, 66, 114, 254, 258, 4098, 16382, 16386) are **falsification
  controls only**; 262142's `117/4` remains numerical/database-derived, not a rigorous certificate.

---

# TRACK C — R_torsion (R-X / R-ID / C)

**Status: OPEN, and its own mechanism audit reached a STOP CONDITION on 2026-09-13.**

`R_X_MECHANISM_AUDIT.md` flags:

    T_P_IN_JM       = PROVED      (T_p ∈ J[𝔪])
    E0_2_IN_JM      = PROVED      (q̂(E₀[2]) ⊆ J[𝔪])
    J_M_DIM_2       = OPEN
    SOCLE_DIM_1     = OPEN
    GORENSTEIN_AT_M = OPEN

Two of master §L PATH 2's three sufficient inclusions are now **proved**; the route is blocked
entirely on the third — `dim_{F₂} J[𝔪] = 2`, equivalently the Hecke socle/Gorenstein question at the
reducible Eisenstein prime with `2 ∥ N`. Česnavičius `manin_v3` Cor. 3.16 bounds
`dim J₀(N)[𝔪] ≤ dim (T/2T)[𝔪] + 1` but **does not set the socle dimension to 1**; §5.16's automatic
Gorenstein cases do not cover this reducible `1 ⊕ 1` even-level instance.

**`H41_W_MECHANISM_AUDIT.md` records that this stop recommendation supersedes the September 13
map's next-action recommendation, without changing any mathematical status.** The September 13
`CURRENT_CRITICAL_PATH` item 1 ("Resolve R-X") is therefore **historical**.

Permanent separations: `dim H⁰(X_{F₂},Ω)[𝔪] = 1` **is not** `dim_{F₂} J₀(N)[𝔪] = 2`. `κ` (a
character-group index) **is not** `T_p` (a Jacobian 2-torsion point). `T_p ∈ ker q_map`, an even
modular degree, and the 16-curve check are **not** proofs of R-X.

Unchanged: G (ADD_014) VERIFIED · M (ADD_015) VERIFIED · (D3)_M (ADD_016) PROVED · realization
lemma = unsealed draft, core audit PASS, **source hardening S1–S6 still outstanding**.

---

# TRACK D — imported / conventional full-BSD compilers

Banwait–Huang **2601.16044v3 Thm 2.13** is the retained compiler. Its local/arithmetic premises —
semistability, discriminant coprimality, `a₃` constraints, no rational 3/5/7-isogenies,
ramification witnesses, ordinarity, the positive-exponent issue and exceptional `n = 9` — are
**already discharged** by the retained H41 audit. **Do not reopen them.** What it still consumes is
exactly: twist nonvanishing + BSD(2).

Qualification that must travel with any claim: v3 Remark 2.11 discloses then-unpublished
dependencies (BSTW, Castella–Ciperiani–Skinner–Sprung, Keller–Yin). Publication/version status was
**not** checked here or in the predecessor. The 66b1 priority/novelty boundary remains unresolved.

---

# TRACK E — generalized-Kato / Mordell–Weil bridge (H5 · H6 · H6A/B · H7 · H8 · H9)

**Status: live at H9R16-C. Custody: UNSEALED, single-document, truncated export.** See `05`.

    H9R15    = LOCAL_WEIGHT_ONE_ROUTE_OPENED       (closed locally; do not reopen)
    H9R16A/B = FINITE_LEVEL_MODIFIED_BALANCE_CLOSED_AFTER_REQUIRED_A_r_TWIST
    H9R16C   = POINT_TRANSITION/KUMMER_SQUARE_OPEN   ← live
               C_W/w_DICTIONARY = OPEN · C_POINT_NORMALIZATION = OPEN
               C_KUMMER_TRANSITION_SQUARE = OPEN
               C_POINT_TOWER_DISTRIBUTION = FORMAL after the square

Logically disjoint from Tracks A–D: no shared theorem, no shared Lean file, no shared input.

---

# TRACK F — historical / withdrawn / failed

Carried forward unchanged from the predecessor §I (all still binding): Vatsal-at-ℓ=2 (withdrawn,
009); Vatsal 1999 Thm 2.7 (ruled out, 011); the old rational `C′` definition (withdrawn, 012);
`range δ_E = K_exp` (false orientation, **do not revive**); the R1-translation-by-T prerequisite
(superseded by `translateMax`); Mordell–Weil necessity for rank (withdrawn); "finiteness probe
only" (superseded); `λ = (m−2)/4` (refuted at N=16386 by 81/4); uniform Tamagawa product 4
(refuted, product 12 example); minimal-height E ⇒ modular-optimal E (wrong identification).

**Newly added to this track by this audit:**

| Item | Why |
|---|---|
| Sept-13 `CURRENT_CRITICAL_PATH` item 1, "Resolve R-X" | Superseded same day by the R-X audit's stop condition; the program moved to the W route |
| W audit `NEGATIVE_ROUTE = BLOCKED` | Unblocked in positions E and B by ADDENDUM_017 Thms D/D′ |
| Input 1 and (K1) as "operator-fixed, not in a sealed object" | Now proved — Theorem G(ii)–(iv) |
| H9R14's "the H9R15 shortcut is NOT currently proved" | Explicitly superseded by the document's own authoritative block |
| H9R10's "only a clerical operator-order writeup remained" | Explicitly superseded by H9R11 |
| Reading `BSD_H5_H6_H6A_H6B_checkpoint_2026-09-14.md` as the checkpoint | It is truncated at H9R2 and omits the entire frontier |

---

# Dependency graph

```mermaid
flowchart TD
  subgraph TA["TRACK A — formal algebraic (COMPLETE, tier L)"]
    R013["Run013 covering / Kummer definitions"] --> SD["S_dyadic"]
    R013 --> DEL["delta descent"]
    SD --> SAT["H41 saturation, index 2"]
    DEL --> P01["P01 two-torsion"]
    P01 --> P03["P03a-e"]
    P03 --> P04["P04a-c: E(Q)/2E(Q) = C2"]
    SAT --> P04
    P04 --> RANK["GateR rank 0"]
    RANK --> FIN["GateRFinite: Finite E(Q)"]
    SAT --> ORD["Conventional: Sel2 = C2, rank 0, Sha[2inf] = 0"]
  end

  subgraph TB["TRACK B — analytic seed (ADVANCED 2026-09-15)"]
    GL["Theorem G: graph lemma<br/>proves Input 1 + K1"] --> TA1["Theorem A: slopes ODD"]
    TA1 --> TB1["Theorem B: node residues = 1 mod 2"]
    TB1 --> TC1["Theorem C: KAPPA IS ODD"]
    TC1 --> L41["Lemma 4.1: im Phi(q)"]
    GL --> L41
    L42["Lemma 4.2: n_E,n_B,n_F,n_G"] --> L41
    L41 --> THD["Thm D / D': negative bit N<br/>positions E and B"]
    VTX["VERTEX ID: E0 in {E,B}"] -. "OPEN — THE GATE" .-> THD
    K25["K2 external cites / K5 unsealed"] -. "hardening" .-> THD
    THD --> NSEED["Negative H41-W seed"]
    FG["Positions F, G"] -. "Phi[2inf]=0 — method blind" .-> NSEED
    POS["Positive branch 8L = 2 mod 4"] -. "BLOCKED" .-> ASEED["All-H41 seed"]
    NSEED --> ASEED
  end

  subgraph TC2["TRACK C — R_torsion (STOPPED)"]
    D3["D3_M proved"] --> RXA["R-X audit"]
    G14["G verified"] --> RXA
    RXA --> TPJ["T_p in J[m]: PROVED"]
    RXA --> E0J["q-hat(E0[2]) in J[m]: PROVED"]
    RXA -. "J[m] dim 2 / socle / Gorenstein: OPEN" .-> RX["R-X"]
    RX -. OPEN .-> RID["R-ID"]
    RID -. OPEN .-> CC["C / C_gen"]
    CC -. .-> NSEED
  end

  subgraph TD2["TRACK D — imported compiler"]
    ASEED --> BSD2["BSD(2)"]
    ORD --> BSD2
    BSD2 -. "BH 2601.16044v3 Thm 2.13<br/>local premises DISCHARGED" .-> FULL["Qualified full BSD"]
  end

  subgraph TE["TRACK E — general MW bridge (DISJOINT)"]
    H15["H9R15 CLOSED locally"] --> H16AB["H9R16-A/B CLOSED<br/>after A_r twist"]
    H16AB --> H16C["H9R16-C: Kummer square OPEN"]
    H16C -. "C1 W/w dictionary" .-> H16C1["normalization"]
    H16C -. "C2 transition square" .-> H16C2["point tower distribution"]
    H16C2 -. "downstream only" .-> BIGK["big Kummer trace"]
  end
```

---

# Namespace guard — the collisions this map exists to prevent

| Do not confuse | With |
|---|---|
| `GateR_rank` (completed formal rank/finiteness) | `R_torsion` (open R-X/R-ID route) |
| theorem **G** (ADD_013/014, generic-fibre identification) | vertex **G** (isogeny position) · Theorem **G** of the *graph lemma* (ADD_017) |
| `F_ff` (finite-field point count) | modular unit `F_p` · vertex **F** · family `F_62` |
| **κ** (character-group index in `X_J`) | `T_p` (Jacobian 2-torsion point) |
| H9 **global** branch Kummer saturation (OPEN) | H9R15 **local** weight-one saturation (PROVED) |
| finite-level modified trace balance (CLOSED) | point-tower distribution (OPEN) |
| big **cohomological** trace | big **point-valued** trace |
| weight-one **coefficient evaluation** | weight-one **MW control** |
| `dim H⁰(X_{F₂},Ω)[𝔪] = 1` | `dim_{F₂} J₀(N)[𝔪] = 2` |
| Theorem **G** (graph lemma, ADD_017) has three sibling meanings | — always qualify it |

Note the newest collision, introduced 2026-09-14: ADDENDUM_017's supersingular-graph lemma is called
**Theorem G**, in a corpus where **G** already meant both the ADD_013/014 generic-fibre theorem and
an isogeny vertex. Always write "the graph lemma (Theorem G of ADD_017)".

---

# UPDATE 2026-09-16 — TRACK B CLOSED at tier SEALED_AREF_T (operator go-ahead; append-only, earlier text preserved)

    H41_MOD4_SUCCESSOR = SEALED_AREF_T   (04_RESEARCH_OBJECTS/H41_MOD4_SUCCESSOR_ADDENDUM_018, archive sha256 648120efb9780435df62e5be510bb66fcb238ad739ac83a5091ccc80b25c8415)
    POSITIVE_OPTIMAL_VERTEX = E                NEGATIVE_OPTIMAL_VERTEX = E
    POSITIVE_CUSP_ORDER = 2                    NEGATIVE_CUSP_ORDER = 4
    POSITIVE_BASE_SEED: 4*L(E,1)/Omega_R odd; v2(L(E,1)/Omega_R) = -2; L(E,1) != 0
    NEGATIVE_BASE_SEED: 4*L(E,1)/Omega_R odd; v2(L(E,1)/Omega_R) = -2; L(E,1) != 0
    H41_RETAINED_TWISTS_BSD2 = CLOSED
    H41_RETAINED_TWISTS_FULL_BSD = CLOSED_AT_EXTERNAL_LITERATURE_QUALIFIED_TIER (BH v3 Remark 2.11)
    OLD_VERTEX_COMPONENT_ONLY_ROUTE = HISTORICAL_FAILED_MECHANISM / SUPERSEDED
    OLD_H41_W_BLOCKED_STATUS = SUPERSEDED_BY_MOD4_INTEGRAL_CHARACTER_ROUTE
    H9_STATUS = UNCHANGED

Proof: R/PROOF.md revision 3 (sha256 71024db1ca0893ac...) of ADDENDUM_018 — two fresh no-repair referees (full reviews rev 0/1, delta reviews
rev 2/3), both ACCEPT WITH REMARKS, 0 BLOCKING. Imports: I1-I13 and R9 of the proof (tiers T/A as stated there); post-review source note
(Agashe–Winters Lemma 2.1: a_p(f) = -w_p for p | N squarefree) hardens the Fricke sign. Not machine-checked.
Superseded rows of this map: B.2 negative E, negative B, negative F, negative G and positive rows (F/G are excluded as vertices: E_0 = E);
B.4 vertex gate PARKED -> CLOSED (E_0 = E, stronger than Target W); B.5 positive H41-W BLOCKED -> CLOSED; the a > 0 transfer cases are moot
(E_0 = E has a = 0 on both branches). ADDENDUM_017 Theorems D/D' are no longer conditional on the vertex. Track C (R-X) is unnecessary for the
seed. Tracks A, D (compiler now applied with its hypotheses verified on the original E) and E/H9 rows are unchanged.

## H41 FROZEN (operator, 2026-09-16) — custody addendum sealed
H41_W_AUDIT_IMPORT_ROWS_CUSTODY_ADDENDUM_019 (archive sha256 8cdf84fd89ff7672726982dee79b6930f4e08594dc8346b0a72ed63ebe9de831): ADDENDUM_018's imports I3-I5 are BOUND — I3 elementary given E_0 = E
(h = 1, a = 0, delta_0 = 2 or 1 by the sign of Delta); I4 (t | 2 positive E, t | 4 negative E) and I5 (z = nu0 delta0 lambda/h, reduced
denominator t) are verbatim statements of the sealed IDENTITY_COMPONENT_REVIEW.md (byte-identical to its member in CODEX_H41_SEED_RESEARCH_FREEZE_001.tar.gz).
The W audit is carried as a negative-result artifact; only its global BLOCKED status is superseded. No residual H41 custody item remains.
H41 = FROZEN: do-not-redo except an identified defect. Research frontier = the general H9 bridge (H9 rows unchanged).
