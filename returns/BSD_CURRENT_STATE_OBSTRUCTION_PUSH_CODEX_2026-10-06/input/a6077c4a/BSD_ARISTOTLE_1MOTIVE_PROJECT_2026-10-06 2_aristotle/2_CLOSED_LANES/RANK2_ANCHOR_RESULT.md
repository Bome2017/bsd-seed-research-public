# Return: the rank-two global anchor (delta 2026-10-06)

## STATUS: PRECISE_OBSTRUCTION

No independent rank-two global identity replacing piece (iii) was found. Five candidate constructions were run through the admission test. Each one fails at a named step, for a reason that does not depend on how the curve was chosen. The failures share one root cause (§3). A strictly weaker reduction (`RANK2_REDUCTION`) was not found either; see §4.

Labels: **PROVED** means proved here, either by the Lean file `Rank2Anchor/Obstruction.lean` or by the elementary argument given. **IMPORTED** means taken from the canonical packet (file named) or from a published source with a theorem number. **HEURISTIC** means anything else, including literature statements whose exact theorem number was not checked in this run.

Scope: no W3 work, no per-prime computation, nothing redone from G2, Theorem W or the K288 residues, and no closed lane reopened. The record's closed candidates (Beilinson–Kato, diagonal cycles / elliptic Stark, plectic points, Yun–Zhang, Tan 1995, K1–K11) are not retested. §5 lists their first failures as recorded.

---

## 0. The target, as fixed by the record

- **IMPORTED** (`CURRENT_FRONTIER.md` §1.4–1.6; `DELTA TASK.md`). Pieces (i) and (ii) are in hand. Theorem W together with the BKS factorization gives C₂(p,ℓ) ≡ (a_ℓ − 2)·s_p·R_{p,ℓ} (mod p), with s_p independent of ℓ. G2 gives the nondegenerate auxiliaries.
- **The replacement for (iii).** We need m ∈ ℚ^× with s_p ≡ m (mod p) for all p outside a finite set. It must come from a characteristic-zero object, and m must be defined without FIN, Ш, Q36 or BSD.
- **IMPORTED** (record Lean `TameCarrier.carrier_unique`, `TameScalar.eq_288_of_mem_lattice`). Such an m is unique if it exists. Under the audited convention, the eleven residues force m = 288 whenever den(m) ≤ 21.

## 1. Why the rank-one anchor degenerates, stated exactly

Rank-one mechanism (Result 002 §5, Gross–Zagier). A characteristic-zero quantity, the height of a Heegner point y_K, is the **first** nonvanishing Taylor coefficient of L(E/K,s) = L(E,s)·L(E^K,s). It is normalized by a **nonzero constant factor**, L(f⊗ε_K,1).

For the seed, take any imaginary quadratic K with ε(E/K) = −1. Write G = L(E,s), with ord G = 2 (IMPORTED: analytic rank 2, `CURRENT_FRONTIER.md` §0), and H = L(E^K,s), with ord H ≥ 1 because its root number is −1.

1. **PROVED** (`ProductOrder.low_derivs_vanish`). Put F = G·H. Then F(1) = F′(1) = F″(1) = 0. So every identity linear in L^{(k)}(E/K,1) with k ≤ 2 reads 0 = 0.
2. **PROVED** (`ProductOrder.third_deriv`). F‴(1) = 3·G″(1)·H′(1), i.e. L‴(E/K,1) = 3·L″(E,1)·L′(E^K,1). This is the boundary fact in the delta task, now checked as the Leibniz rule.
3. **PROVED** (`ProductOrder.first_order_anchor_height_zero`). Any identity of the form c·ĥ = F′(1) with c ≠ 0 forces ĥ = 0. With the Gross–Zagier formula this means ĥ(y_K) = 0, i.e. y_K is torsion. (The Gross–Zagier formula itself is IMPORTED, Gross–Zagier, Invent. Math. 84 (1986), Thm I.6.3; HEURISTIC as to that exact numbering.)
4. **PROVED** (`degenerate_identity_blind`). Consider a family of identities c·Z(t) = B(t), with the tame variable t and a fixed factor c = L(f⊗ε,1) = 0. Any two candidate values Z, Z′ satisfy it equally. So it determines nothing about Z, at any tame order. This is the "0 = 0 at every tame order" statement, in exact form.

**Consequence (PROVED from 1–4).** Every replacement for (iii) built from E over a quadratic field must evaluate a quantity of order ≥ 3 in L(E/K,s). Equivalently, it must evaluate L″(E,1) times a known nonzero factor. Its geometric side must therefore be a second-order invariant: a 2×2 height determinant, not a single height.

## 2. Candidates tested (admission test, stopping at the first failure)

The admission steps are those in canonical `TASK.md`: (1) defined over ℚ or ℤ[1/D] with no p; (2) no Ш, no BSD, no q ∈ ℚ; (3) the tame realization gives C₂(p,ℓ) and not 0 = 0; (4) the regulator realization gives (a_ℓ − 2)·R_{p,ℓ}; (5) exact normalization; (6) a nonzero rational m; (7) consistency with the residues.

### R1. Higher-order Heegner identity over K (ε(E/K) = −1)
- **Object.** Heegner points over K, together with the order-3 coefficient L‴(E/K,1) = 3·L″(E,1)·L′(E^K,1).
- **Steps 1–2: pass.** Heegner points are defined from X₀(N) with no p, no Ш and no BSD.
- **First failure: step 3.**
  - The only known identity attached to the object is first order (Gross–Zagier). On the seed it reads 0 = 0 (§1.1, §1.3, §1.4; PROVED).
  - No identity attached to Heegner points over a number field evaluates L‴(E/K,1). IMPORTED from the record: higher Gross–Zagier is known over function fields only (Yun–Zhang).
- **Input that would change it.** A number-field higher Gross–Zagier formula, L‴(E/K,1) = c·⟨Z, Z⟩, for a cycle or derived class Z defined without p, with c explicit.

### R2. Twist-split anchor: Gross–Zagier for E^K, then divide
- **Object.** Take K with E^K of analytic rank 1. IMPORTED from `twist/`: E^{−23} has rank 1, with L′ ∈ [39.512236, 40.182321]. Gross–Zagier applies to E^K over an auxiliary field and gives a genuine rank-one anchor for E^K.
- **Steps 1–2: pass.**
- **First failure: step 3.** It has two parts.
  - **(a) PROVED** (algebra on §1.2). Write L″(E,1) = L‴(E/K,1)/(3·L′(E^K,1)). Dividing by the twist anchor only moves the problem to L‴(E/K,1), which is R1.
  - **(b) PROVED** (`equivariant_minus_to_plus_eq_zero`, `equivariant_minus_to_trivial_eq_zero`; p odd, so 2 is invertible).
    - The tame realization of E^K's anchor lies in the (−1)-eigenspace of Gal(K/ℚ), since E^K(ℚ) ⊗ ℚ = E(K)^− ⊗ ℚ.
    - C₂(p,ℓ) and (a_ℓ − 2)·R_{p,ℓ} are built from E over ℚ and from E(ℚ) = E(K)^+ (modulo torsion), and Gal(K/ℚ) acts trivially on them.
    - So every Gal(K/ℚ)-equivariant transfer from the first to the second is zero.
    - (That the realizations are equivariant is HEURISTIC, i.e. standard functoriality, not re-verified here.)
- **Input that would change it.** A non-equivariant comparison pairing the two eigenspaces. Such a comparison is a statement about L(E/K) at order 3, so this is R1 again.

### R3. Ring-class-character Heegner family (χ ≠ 1)
- **Object.**
  - Heegner points y_c over ring class fields K[c], and their χ-components for nontrivial ring class characters χ.
  - Gross–Zagier–Zhang / Yuan–Zhang–Zhang give L′(E/K,χ,1) = (explicit)·ĥ(y_χ). HEURISTIC as to exact theorem numbers.
  - For χ ≠ 1, L(E/K,χ,s) = L(E ⊗ Ind χ, s) does not factor through L(E,s). So these are genuinely nondegenerate rank-one anchors.
- **Steps 1–2: pass.** c can be a tame ℓ, and no p is needed for the points.
- **First failure: step 3.**
  - The tame variable of this object is the anticyclotomic group Gal(K[ℓ]/K). C₂(p,ℓ) lives on Gal(ℚ(μ_ℓ)/ℚ).
  - For ℓ split in K, Gal(K[ℓ]/K[1]) is cyclic of order dividing ℓ − 1, like Gal(ℚ(μ_ℓ)/ℚ). But K[ℓ] is dihedral over ℚ and K(μ_ℓ) is abelian over ℚ, so their degree-p layers are different fields (HEURISTIC, standard class field theory).
  - The only part of the family that sees E itself is the trivial-character part. There the anchor is y_K, which is torsion (§1.3).
  - The I-adic leading term of the Heegner theta element over K[ℓ] is a derived Heegner class (Darmon's refined conjecture type). The record has no identity relating it to C₂(p,ℓ).
- **Additional failure if the conjecture were imported: step 2.** The conjectural leading coefficient is normalized by #Ш(E/K) (HEURISTIC; Darmon, Invent. Math. 110 (1992)).
- **Input that would change it.** A cyclotomic–anticyclotomic tame reciprocity law, with an exact constant, equating the derived Heegner leading coefficient over K[ℓ] with C₂(p,ℓ) over ℚ(μ_ℓ).

### R4. Definite Gross-point theta element (ε(E/K) = +1, e.g. K = ℚ(√−7))
- **Object.**
  - Gross points on the definite quaternion algebra, and θ_{K,ℓ} = Σ_σ f(x_σ)·σ.
  - Gross's formula (Gross 1987; Waldspurger) gives L(E/K,χ,1) ≐ |χ(θ)|² (HEURISTIC as to theorem number).
- **Steps 1–2: pass.**
- **First failure: step 3.**
  - At the trivial character the formula reads L(E,1)·L(E^{−7},1) = 0 = |θ_1|². This is the degenerate case of `degenerate_identity_iff` (PROVED form of the degeneracy).
  - The degree-two term M₂ lies in a finite group at every level, so it has no characteristic-zero realization (IMPORTED, `ADMISSION.md` §1).
  - Even granting the degree-two term, the formula has no Mordell–Weil side, so step 4 would fail as well. Gross's identity relates θ·θ* to L-values only.
  - Record status (IMPORTED, delta `TASK.md`): M₂(p) ≠ 0 ⇒ Ш[p^∞] = 0 is a per-prime criterion only.
- **Input that would change it.** A derived Gross formula, with an exact constant free of Ш, identifying the I²-coefficient of θ_{K,ℓ} with a Mazur–Tate-type 2×2 regulator on E(K)^+ = E(ℚ). (Bertolini–Darmon-type derived heights; HEURISTIC. In the known formulations the constant includes #Ш.)

### R5. "Limit of rank-one anchors" as χ → 1
- **Object.** The family of identities {L′(E/K,χ,1) = c_χ·ĥ(y_χ)} over characters χ of order p and conductor ℓ, expanded in powers of (χ − 1).
- **First failure: step 1.**
  - Characters of order p, and the augmentation filtration they define, exist only once p is chosen. So the expansion is p-dependent.
  - In characteristic zero, finite-order characters form a discrete set, so there is no archimedean derivative at χ = 1.
- **Input that would change it.**
  - An archimedean family through the trivial character, such as Hecke characters of infinite order.
  - Together with a Gross–Zagier formula for the derivative in the family direction at χ = 1, which is itself a higher Gross–Zagier statement.

## 3. The common obstruction (the precise statement)

- **PROVED (§1).** For the seed, every identity of Gross–Zagier type over an imaginary quadratic field is first order in s and linear in one height. Each falls into one of three cases:
  - (a) it evaluates a vanishing coefficient (0 = 0; R1, R4 at the trivial character);
  - (b) it lands in a Galois-isotypic part that cannot map equivariantly to E(ℚ)'s part (R2; R3 for χ ≠ 1);
  - (c) it becomes p-dependent (R5).
- **PROVED (§1.2 + §1.4).** The first nondegenerate characteristic-zero invariant available is L″(E,1). It appears through L‴(E/K,1) = 3·L″(E,1)·L′(E^K,1).
- **What a replacement for (iii) must be.** A formula that evaluates L″(E,1), or a fixed nonzero multiple of it, against a 2×2 height determinant on E(ℚ). The formula must have an exact constant and be defined without p. That is a number-field rank-two (higher) Gross–Zagier formula, or a statement of equal strength. No such formula is known (IMPORTED: record, Yun–Zhang over function fields only).
- **Why any success needs new input. IMPORTED** (record Lean `Frontier.support_finite_of_tameCarrier`; `CURRENT_FRONTIER.md` §3). Any RANK2_IDENTITY gives finite support of Ш for the seed through G2 + Theorem W + Ota.
  - HEURISTIC: finiteness of Ш is not known for any elliptic curve over ℚ of analytic rank ≥ 2.
  - So the identity sought would prove something currently out of reach. This explains why no construction from known theorems can pass.
- **Calibration constraint on any general mechanism (step 7).**
  - PROVED arithmetic (`seed_calibration`): 4·c∞·Tam·#Ш/tors² = 4·c∞·(#Ш·Tam/tors²), and on the seed's numbers 4·2·16·9/2² = 288 = 8·36.
  - HEURISTIC: under BSD the right-hand side is 4·c∞·q. So a general Ш-free m must conjecturally equal the analytic invariant 4·c∞·q. The only Ш-free definition of m consistent with the calibration is therefore analytic (TAC with q ∈ ℚ), or an identity that proves it equal to such a quantity. This is again the higher Gross–Zagier gap.

## 4. Why not RANK2_REDUCTION

The reductions found are:
- G1 ⇐ (higher Gross–Zagier for L‴(E/K,1) or L″(E,1), with an exact constant, plus a tame comparison);
- G1 ⇐ RAT + TAC, which is already in the record (`Frontier.support_subset_of_tame8q`).

Neither hypothesis is strictly weaker than G1. Each implies FIN-tail through the IMPORTED arrow of §3 (HEURISTIC that each is in fact stronger). No residue-level identity strictly weaker than G1 and not equivalent to FIN-tail was found. So this return is PRECISE_OBSTRUCTION.

## 5. Closed candidates (not retested; first failure as recorded)

| Candidate | Recorded first failure | Source |
|---|---|---|
| Beilinson–Kato / Kato determinantal element | multiplier x_ℚ·#A_p; the archimedean realization is at s = 2, and the central point is reached only p-adically | `2_CLOSED_LANES/K288_UNIFORMITY_ANALYSIS.md`, `CLOSED_LANES.md` |
| Diagonal cycles / elliptic Stark | per p | `CLOSED_LANES.md` (K-list) |
| Plectic points | missing construction | `CLOSED_LANES.md` |
| Yun–Zhang higher Gross–Zagier | function fields only | `CURRENT_FRONTIER.md` §3 |
| Tan 1995, Thms 3.12/3.14/3.16 | assumes BSD over intermediate fields; constant only up to F_p^× | `ADMISSION.md` |
| Θ_E ↔ Z ↔ M_G2 comparison | degree-two class is in a finite group, so it has no ℚ-valued realization | `ADMISSION.md` |

## 6. Lean

The file is `Rank2Anchor/Obstruction.lean`, in Lake library `Rank2Anchor`. It builds with `lake build Rank2Anchor.Obstruction` and contains no `sorry`. Every arithmetic input is an explicit hypothesis, and nothing in the file is a statement about Ш of the seed.

```
'Rank2Anchor.leibniz' depends on axioms: [propext, Classical.choice, Quot.sound]
'Rank2Anchor.ProductOrder.low_derivs_vanish' depends on axioms: [propext, Classical.choice, Quot.sound]
'Rank2Anchor.ProductOrder.third_deriv' depends on axioms: [propext, Classical.choice, Quot.sound]
'Rank2Anchor.ProductOrder.first_order_anchor_height_zero' depends on axioms: [propext, Classical.choice, Quot.sound]
'Rank2Anchor.degenerate_identity_iff' depends on axioms: [Quot.sound]
'Rank2Anchor.degenerate_identity_blind' depends on axioms: [propext, Quot.sound]
'Rank2Anchor.equivariant_minus_to_plus_eq_zero' depends on axioms: [propext]
'Rank2Anchor.equivariant_minus_to_trivial_eq_zero' depends on axioms: [propext]
'Rank2Anchor.seed_calibration' depends on axioms: [propext, Classical.choice, Quot.sound]
```

Project note: the packet's original `lakefile.toml` library entry was rejected by Lake ("expected glob", because of the hyphen in `2026-10-06`). It is commented out, with an explanation, and the packet's Lean files are unchanged. A new library `Rank2Anchor` is the default target.

FIN, ORDER9 and Q36: unchanged.
