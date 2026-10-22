# E11 RESULT — one bounded construction attempt from Kato's determinant element

## VERDICT: SCOPED_FAILURE

The one candidate worked (the BKS II determinantal zeta element 𝔷_Q, specialized through the Bloch–Kato Selmer
complex to the Ota witness module, with target lattice L = ∧²E(Q)_tf ⊗ ∧²E(Q)_tf) does **not** give a fixed,
prime-independent bound on witness depth. It fails at one explicit map. The leading-term specialization

    sp_p : D_p = det^{-1}_{Z_p} RΓ(Z_Σ, T_p E) → Z_p ⊗ L

is integral with cokernel of order exactly #H^2_f(Q,T_p)_tors = #Sha(E/Q)[p^∞]. Every arrow of the
construction bounds the witness depth from **below** only. At p ∈ P_K with Sha[p^∞] finite, and at any regime-A
auxiliary F whose Mazur–Tate regulator is primitive,

    depth t(p,F) = κ_p + len Sha(E/Q)[p^∞],     κ_p := v_p[D_p : Z_p 𝔷_Q] ≥ 0.

No input of the construction bounds either summand from above uniformly in p. An abstract model with all the
construction's properties (including an IMC at every p) has depth 2 at every p. The failure is scoped to this
candidate. It excludes neither other Kato, motivic, Galois or finite-support constructions, nor an external upper
bound on the observable.

## Session facts

- Private lab `Bome2017/bsd-seed-lab`, branch `claude/e11-kato-integral-comparison-yh5iqb` (content from `e11` at
  b13f81b). Packet manifest 18/18 OK and experiment manifest 20/20 OK before work. `BRANCH_TASK.md`, named in the
  launch prompt, does not exist in the checkout and nothing was substituted for it.
- Start 04:41 UTC. Written only under `work/e11/`. Total computation under 1 CPU-second, pure python3. No
  PARI/Sage/Lean (none installed), network sources, subagents or paid resources. Local run outputs were not used.
- One primary source was read: the packet copy of BKS II (arXiv 2103.11535v1): Hyp. 2.2, §§2–5, Lemma 4.2,
  Def. 4.3, Props 4.4 and 5.1–5.4, Cor. 5.3, Lemma 5.5. No other source was opened.

## The candidate and its maps (01)

Arrows: 𝔷_{F∞} → 𝔷_F → φ_F → π_{F,f} → Z_p[G] ⊃ I^2 → I^2/I^3 (Cor. 5.3: 𝔷_F ↦ θ_{F,S}), over
𝔷_Q ∈ D_p → φ_Q → det^{-1}RΓ_f(Q,T). BKS's π_{Q,f}, η^alg and (11) need Sha[p^∞] finite (audit ITEM 1). They
were **not used**. They are replaced by Lemma 2.1, which is valid for every Selmer corank s_p.

## Results proved in this pass (grades relative to the imports listed below)

| # | statement | file | grade |
|---|---|---|---|
| 1.1 | H^1(Z_Σ,T) = H^1_f(Q,T) is free of rank s_p; H^2_f = Z_p^{s_p} ⊕ A_p; s_p = 2 ⟺ Sha[p^∞] is finite, and then #A_p = #Sha[p^∞] | 01 | PROVED (standard) |
| 2.1 | Torsion-minor lemma: for Ψ ∈ M_d(Z_p[G]) with Ψ mod I of rank d−s, det Ψ ∈ I^s and det Ψ ≡ unit·#(coker)_tors·det(Bockstein block) mod I^{s+1} | 02 | PROVED; toy-checked 6/6 |
| 2.2 | θ_{F,S} ∈ I^{s_p} and θ_{F,S} ≡ u·ε(g_F)·#A_p·Reg^{Boc}_F mod I^{s_p+1}, for every admissible F, without any Sha hypothesis | 02 | DERIVED from Cor. 5.3 |
| 2.3 | If Sha[p^∞] is infinite, t(p,F) = 0. If it is finite, t(p,F) = u·p^{κ_p}·#Sha[p^∞]·R_F | 02 | DERIVED; uses [3, Th 10.3] |
| 3.1 | Single-prime regime-A witness: c_2(θ_ℓ) ≢ 0 ⟹ Sha[p^∞] = 0 **and κ_p(Σ_ℓ) = 0**. The converse holds when R_{F_ℓ} ≢ 0, e.g. at G2 auxiliaries | 03 | DERIVED |
| 3.1′ | κ_17 = κ_23 = κ_29 = 0 (for the recorded auxiliaries 103, 47, 233; all four recorded pairs are regime A by point count; 23 and 29 are supersingular) | 03 | DERIVED, three primes only |
| D′ | E10's multiplier is identified: M_p ≐ p^{κ_p}·#Sha[p^∞]. The converse of Prop. D now holds wherever κ_p = 0, not only at ordinary p | 03 | DERIVED |
| 3.2 | W_B ⟺ for all p ∉ B: Sha[p^∞] = 0 and κ_p(Σ_ℓ) = 0 for some G2 auxiliary ℓ | 03 | DERIVED |
| 4.1 | The local lattices sp_p(D_p) globalize to a Z-lattice ⟺ Sha has finite support on P_K | 04 | PROVED (elementary) |
| M_∞ | The construction's properties are compatible with depth 2 at every p ∈ P_K | 04 | PROVED; instance 7/7 |

**New relative to the supplied records.** Items 2.1–2.3 remove the Mordell–Weil realization from the
BKS specialization by a case split on s_p. The separation of the multiplier into an Iwasawa-theoretic factor
κ_p and the torsion minor #Sha[p^∞] is new. So are the consequence "nonzero regime-A witness ⟹ 𝔷_Q is a
Z_p-basis" (no ordinarity), its scoped application at 17, 23 and 29, Prop. 3.2, Lemma 4.1, and the countermodel
instance inside the determinant formalism. 02 §4(2) gives a valuation-level Σ-independence of κ_p, modulo two
imports. **Not new:** θ ∈ I^{s} recovers Ota Thm 5.17 for admissible F. "Nonzero witness ⟹ Sha[p^∞] = 0"
re-derives Ota 6.4 in regime A. Neither is a new Sha result. No novelty against the literature is claimed.

## Relation to the exact h_p of WITNESS_CONTENT_THEOREM

Take a single-prime regime-A witness S = ℓ, where Ota's and BKS's elements agree up to units (01 §4). Its depth
is at least δ_p := κ_p + len Sha[p^∞], with equality when R_F generates I^2/I^3. At a level-1 (G2) auxiliary it is
nonzero iff δ_p = 0. The construction therefore controls h_p only through δ_p, and only from below. Multi-prime S
(where the two elements differ by diagonal terms) and regime-K witnesses (E(F_ℓ)[p] ≅ Z/p, where Hyp. 2.2 fails)
are outside this construction.

## Imports (not re-proved) and unmet hypotheses

- Seed data at recorded grades: rank 2, saturated basis, torsion Z/2, Tam = 16, all-odd residual surjectivity,
  no anomalous p ≥ 7, and ∏#E^ns(F_ℓ) over ℓ | N.
- BKS II: Hyp. 2.2 framework; Lemma 4.2 (Kataoka [16], via [10], [8]); Ann(z_{F∞}) = 0 ([16, §6.1]); integrality
  of z_F ([9]); (20)–(24); Prop. 5.1 (Ota [20], Kato's (14)); Prop. 5.2 and Cor. 5.3; base change of RΓ_f; H^2_f ≅
  Sel^∨; [3, Th. 10.3] (Bockstein = Mazur–Tate pairing).
- Retained identifications: c_2(θ_ℓ) ↔ BKS θ_{F,S} for single ℓ (LINE_HOSTILE_AUDIT 3.1), and R_{p,ℓ} ↔ R_F
  (G2 §4, DINF_03 §4). G2 existence and R_{p,ℓ} ≢ 0 (audited). Ota 5.17 and 6.4 are used only for comparison.
- IMC (Kato + Skinner–Urban) at its recorded grade: supplies κ_p = 0 at good ordinary p only.
- **Unmet:** (U1) κ_p = 0 at almost all supersingular p. (U2) #A_p = 1 at almost all p. (U3) a global rational
  structure on (𝔷_Q^{(p)})_p; the packet supplies none and this pass asserts none. (U4) Deeper regime-A
  auxiliaries with a primitive R_F, needed for finite depth where p | M_p. (U5) O1–O3 of DINF_03 for candidate
  G-c. Kato's Σ-enlargement relation and the compatibility of π, used only in 02 §4(2), were not re-read.

## Prime scope

P_K = primes outside S0 ∪ {19, 59, 487}, where S0 = {2, 3, 5, 2243, 4547, 5843}. Ordinary and supersingular
primes are both included, since Hyp. 2.2 has no ordinarity condition. Exceptional primes:
- 2, 3, 5, 19 are settled by recorded results.
- 2243, 4547 and 5843 are open.
- 59 and 487 lie outside this construction but inside WC's P.
- Every p ∈ P_K with p | M_p needs (U4) for a finite depth.

Nothing about finiteness at any exceptional prime is changed. **No FIN, ORDER9, Q36 or new settled primary
component is claimed.**

## First remaining step

An upper bound δ_p ≤ v_p(C), for one fixed C ≠ 0 and all p ∈ P_K outside a finite set. It must come from outside
the Euler system, because every Euler-system arrow is a divisibility in the other direction. Inside this
construction it splits into (U1), which is available at ordinary primes and open at supersingular ones, and (U2),
which the torsion minor cannot address.

## Files

`DERIVATION_01.md` … `DERIVATION_04.md`, `checks/torsion_minor_check.py(.out)`,
`checks/regime_check.py(.out)`, `checks/countermodel_instance.py(.out)`, `RESUME.md`, `MANIFEST.sha256`.
