# Delta task: a fixed 1-motive receiver and its Selmer-complex determinant line (2026-10-06; revised per Pro)

This project contains the canonical packet `BSD_SEED_FRONTIER_2026-10-06` (revision 2). `2_CLOSED_LANES/` also holds:
- the rank-two-anchor result;
- the derived-Gross result;
- the fixed-local-condition carrier note.

Read `CURRENT_FRONTIER.md` first. **This file governs the run.** Every rule in the root `TASK.md` "Do not" list applies.

## Overrides of the canonical `TASK.md` for this run

- **Step 1 is a new statement**, Sel(ℚ, M_E)(p) ≅ Ш[p] for all odd p, for a fixed 1-motive. It is not the record's class-group receiver exactness. Proving it is allowed here despite two canonical items: "do not re-derive receiver exactness" and "no further Selmer bookkeeping equivalence".
- **New input, relative to the K-list entry "1-motive alone"** (G2's 1-motive gives only the regulator side):
  - the Selmer side of the quotient M_E (step 1);
  - the Macias Castillo–Sano determinant-line framework (step 3).

  These satisfy the canonical "reopen only with a new input" rule. The K-list verdict still stands for the regulator side.
- **Scope.** The canonical "The work" section (G1 at the residue level) is replaced by the steps below. G1 enters only at step 6, as a stop condition.

## The object

\[ M_E=[\mathbb Z^2\xrightarrow{\,u\,}E],\qquad u(e_1)=P_1,\quad u(e_2)=P_2. \]

- **E** is the minimal model [0,−1,0,−66020924,−65074271436], with N = 2³·3·2243·4547²·5843.
- **The points.** P₁ = (−3031, 327384) and P₂ = (−2394, 281520). Both were checked to lie on this model (PARI, 10-06). They form a basis of E(ℚ)/tors (record: exact 2-descent plus saturation), and E(ℚ)_tors ≅ ℤ/2.
- **Relation to G2.** M_E is the quotient, by its torus part, of G2's fixed 1-motive 𝓜 = [ℤ² → G₁ ×_E G₂] (`1_PROVED_STATE/G2/G2_PROOF.md` §3).

**Why this object.** The record's 10-06 fine-Selmer lemma (`2_CLOSED_LANES/RECEIVER_FIXED_LOCAL_CARRIER.md`) shows that a carrier built from E[p] with fixed local conditions sees a Mordell–Weil class at every large p. M_E removes the Mordell–Weil plane globally, before any p-adic realization.

## Steps

Do them in order, and stop at the first stop condition.

1. **Prove the fixed receiver theorem** without FIN: Sel(ℚ, M_E)(p) ≅ Ш(E/ℚ)[p] for every odd p.
   - Verify PRE-CHECK (a)–(c), with the exact local conditions.
   - State whether ∞, p = 3 or the bad primes need care.
   - Relate it to the record's receiver B_p ≅ Ш[p] for p ≥ 5 (`1_PROVED_STATE/receiver/INTEGRATED_STATEMENT.md`). The difference: M_E is fixed before p is chosen.
2. **Record that BSS and Sakamoto do not apply to T_pM_E.** This is already settled (PRE-CHECK (d)). State the two failures and do not spend more of the run on Mazur–Rubin, Sakamoto or Burns–Sakamoto–Sano for T_pM_E.
3. **Test the Macias Castillo–Sano construction** (arXiv 2603.23978, "On Selmer complexes, Stark systems and derived p-adic heights") directly on T_pM_E:
   - Selmer complexes ≃ Poitou–Tate complexes;
   - det(Selmer complex) ≅ the module of Stark systems.

   Check **every** standing and local hypothesis explicitly. Do not assume it applies because it says "mild hypotheses". The record already used this paper for a different purpose: U22 link 1 used its Theorem 4.2 (Z_p-extensions) and its Appendix B Theorem B.5. See PRE-CHECK (e).
4. **If it applies, compute the determinant line concretely**, using H⁰(ℚ, M_E)/p = 0. Start from PRE-CHECK (f) and verify or correct it.
5. **The canonical element.** Ask whether that determinant line has a canonical element coming from the fixed 1-motive itself, rather than from an independently chosen p-adic Euler or Heegner system. Identify it, and compare it with the record's tame scalar s_p (PRE-CHECK (g)).
6. **Only then, globalization.** Do these p-adic elements globalize across p, i.e. are they realizations of ONE integral object with index A_M ∈ ℤ, A_M ≠ 0, and Sel(M_E)(p) ≠ 0 ⇒ p | A_M outside an explicit finite set?
   - Stop if this needs ETNC, BSD, q, FIN, #Ш or Q36.
   - Also stop if A_M is the record's Tame Law in another form (G1, or TAC with A = 8q).

## PRE-CHECK (Claude and Pro, 10-06): verify, don't rediscover

**(a) H⁰ of M_E.** H¹(F, ℤ²) = Hom_cont(G_F, ℤ²) = 0 for F = ℚ and for every ℚ_v. The hypercohomology sequence of [ℤ² → E], equivalently the triangle E → M_E → ℤ²[1], then gives:
- H⁰(F, M_E) = E(F)/⟨P₁, P₂⟩;
- H¹(F, E) ↪ H¹(F, M_E), with cokernel inside H²(F, ℤ²).

Globally H⁰(ℚ, M_E) ≅ E(ℚ)_tors ≅ ℤ/2, so H⁰(ℚ, M_E)/p = 0 for odd p.

**(b) The Selmer sequence for Deligne 1-motives:** 0 → H⁰(ℚ, M)/n → Sel(ℚ, M)(n) → Ш¹(ℚ, M)[n] → 0.
- IMPORTED: "On Tate–Shafarevich groups of 1-motives"; see also Harari–Szamuely and Jossen. Check the exact statement and the definition of the local conditions.
- The torsion realization M_E[p] sits in 0 → E[p] → M_E[p] → 𝔽_p² → 0.
- The Tate module sits in 0 → T_pE → T_pM_E → ℤ_p² → 0, with the extension directions given by P₁ and P₂ (Jossen thesis, IMPORTED).

**(c) Ш of M_E.** Ш¹(ℚ, M_E) ≅ Ш(E/ℚ).
- Injective, because H¹(ℚ_v, E) ↪ H¹(ℚ_v, M_E) at every v.
- Surjective, because the obstruction lies in Ш²(ℚ, ℤ²) ≅ Ш¹(ℚ, ℚ/ℤ)² = 0: by Chebotarev, a finite-order character trivial on every decomposition group is trivial.

Hence Sel(ℚ, M_E)(p) ≅ Ш(E/ℚ)[p] for all odd p. At p = 3 this is (ℤ/3)², by the record.

**(d) BSS and Sakamoto are inapplicable (PROVED).** Both theories need ¯T residually irreducible and some τ with T/(1−τ)T free of rank one (Sakamoto, JTNB; Burns–Sakamoto–Sano, arXiv 1805.08448). For T = T_pM_E both fail:
- M_E[p] ⊃ E[p], with trivial quotient 𝔽_p², so it is reducible;
- G_ℚ acts trivially on the lattice quotient ℤ_p², so for every τ, T_pM_E/(1−τ)T_pM_E ↠ ℤ_p², which is never free of rank one.

**(e) HEURISTIC, about step 3.** Stark-system modules are built from sets of Kolyvagin primes.
- If Macias Castillo–Sano's det ≅ Stark-systems isomorphism uses the same τ / rank-one-coinvariant hypothesis, it fails on T_pM_E exactly as in (d). Its Selmer-complex ≃ Poitou–Tate part may still apply.
- Separate the two parts. Also say whether the Cartier dual T_pM_E^∨ = T_pG (G the extension of E by 𝔾_m² attached to P₁, P₂, sub ℤ_p(1)², quotient T_pE) or G2's 𝓜 does better.

**(f) HEURISTIC, about step 4.**
- **The determinant line.** If the local conditions are compatible with the triangle T_pE → T_pM_E → ℤ_p², multiplicativity gives det RΓ_f(T_pM_E) ≅ det RΓ_f(T_pE) ⊗ det RΓ_f(ℤ_p)^{⊗2}. The extension classes P₁, P₂ then enter only the canonical trivialization, not the line itself.
- **Rational cohomology.** H¹_f(ℚ, V_pM_E) ≅ V_pШ(E/ℚ). This is because the connecting map ℚ_p² → H¹_f(ℚ, V_pE) is given by P₁, P₂, and H¹_f(ℚ, ℚ_p) = 0. So RΓ_f(V_pM_E) is acyclic exactly when Ш[p^∞] is finite: M_E behaves as a "rank-zero" object.
- **Its special value.** The expected special value is the BSD quotient, of the shape L*(E,1)/(Ω·Reg) times local factors. Verify or correct.

**(g) HEURISTIC, about steps 5–6.**
- If the canonical element at p is the torsion Euler characteristic of RΓ_f(T_pM_E), its p-adic size is that of #Ш[p^∞] times local factors. That is tautological.
- If it is a zeta element, its value is the leading-term quotient q: `ETNC_CIRCULAR`.
- If it is (up to units) the record's tame scalar s_p (Kato's derived class with the tame regulator of P₁, P₂ removed; ℓ-independent by Theorem W; s_p ≐ x_{ℚ,Σ}·#Ш[p^∞] by BKS), then globalization is the Tame Law G1.
- Any other outcome needs a global object not on this list.

## Return exactly one status

- `FIXED_1MOTIVE_RECEIVER`: only steps 1–2 are established, with any correction stated.
- `GLOBAL_PRIMITIVE_SYSTEM`: a canonical cross-p element of the determinant lines exists, with a fixed nonzero index A_M defined without q, #Ш, FIN, Q36 or BSD/ETNC, and Sel(M_E)(p) ≠ 0 ⇒ p | A_M outside an explicit finite set.
- `P_ADIC_ONLY`: the canonical elements exist for each p but do not globalize.
- `HYPOTHESES_FAIL`: the Macias Castillo–Sano framework does not apply to T_pM_E, its Cartier dual or G2's 𝓜. Name the first failing hypothesis for each.
- `ETNC_CIRCULAR`: the required global element is exactly the conjectural zeta/leading-term normalization.

## Do not (in addition to the canonical list)

- W3, transplants of OpenAI Result 002, the plectic framework, the exceptional primes, any per-prime computation, or any large computation.
- A literature survey without a specific candidate.
- Redoing R1–R5 or the derived-Gross routes A–C.
- Spending the run on Mazur–Rubin, Sakamoto or BSS Kolyvagin systems for T_pM_E (settled in (d)).
- Re-deriving G2, Theorem W, the BKS factorization or the receiver exactness. Cite the packet.

## Return format

As in the canonical `TASK.md`:
- one STATUS line;
- every claim labelled PROVED, IMPORTED or HEURISTIC;
- Lean with no `sorry`, plus `#print axioms` for every new theorem. The algebraic skeleton is enough: for example the coinvariant lemma of (d), and the diagram chase Sel ≅ Ш¹[n] when H⁰/n = 0;
- end with "FIN, ORDER9 and Q36: unchanged", or a precise statement of what changed.
