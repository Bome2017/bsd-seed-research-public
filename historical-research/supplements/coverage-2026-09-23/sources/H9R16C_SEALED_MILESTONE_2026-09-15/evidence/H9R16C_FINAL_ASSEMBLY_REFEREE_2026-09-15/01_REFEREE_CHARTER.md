# 01 — Charter: H9R16-C FINAL ASSEMBLY REFEREE

§1 is the operator's charter. The math is transcribed from LaTeX to plain Unicode; the wording is unchanged.
§2–§4 are coordinator operating rules. They do not change the question.

## §1. Operator charter

H9R16-C FINAL ASSEMBLY REFEREE

Treat the following as inputs, do not reprove them:

    ϖ_1^* A_r ϖ_{1,*} = A_{r+1} N_{r+1,r},        d_r = 1,

and scalar D4 by Abel–Jacobi functoriality.

Your only task is to decide whether these inputs genuinely imply the correctly typed point-tower theorem.

Use as the target point object

    𝒫_r^♮ = Hom_{Z_p}( B_r^bal , Ĵ_r^{(1)}(F'_r)^ord )^⋆

with the factor-1 dagger twist and the required tame g^c / ε_g^{-1} carrier twist.

Prove or refute:

1. the Lane-5 algebraic contraction induces exactly  Φ̄_r^mod ∈ 𝒫_r^♮;
2. D4 upgrades from the scalar/evaluation statement to the Hom-valued identity
       Kum(Φ̄_r^mod) = Contr_r^{A_r}(Δ_r^ét);
3. after identifying the actual BCPV common-to-native tame pushdown,
       τ_r^MW(Q_{r+1}) ∘ (1 ⊗ N_{r+1,r}) = π_r^* Q_r;
4. no full-triple-G_r or type-A rank factor is reintroduced;
5. the tame ε_g^{-1} twist is preserved.

Do not use BCPV (4.9).
Do not revisit MPC.
Final verdict only:
`H9R16C_CLOSED`
or
`H9R16C_NOT_CLOSED — FIRST EXACT DEFECT = ...`
If closed, state the exact inverse-limit point module created and the exact next gate `G_BIG_KUMMER_TRACE`.

The operator's reasons for items 1–3 are in 00, §"What the operator does NOT yet accept":
- the typed relation lives inside Hom(B_{r+1}^bal, Ĵ_r)^†, because the carrier is contravariant;
- D4 is to be proved evaluationwise on b ∈ B_r^bal and then extended by linearity;
- the Lane 5 packaging Σ_g P_r[g·(a,b,c)] ⊗ g is accepted only as intermediate data, until the
  quotient/balancing map to the final object is written explicitly.

## §2. Operating rules (coordinator)

1. **Inputs are inputs.** The following are theorems for this referee (exact statements in 02 §A):
   MPC_r (L5-T3), the norm element (L5-T2), Lemma W (L5-T1), the group-ring form (L5-T4), and scalar D4 (L5-D4).
   - Do not re-prove them.
   - If you come to believe an input is false as stated, record `INPUT_DEFECT_SUSPECTED` with the exact location
     and reason, stop that item, and do not repair the input.
   - L5-T5 (tame transport) is the tool for item 3. You may check it; that is R3 scope, not MPC.
2. **Prohibited:**
   - BCPV (4.9), label `defn_3rd_vertical_map`, BCPV.tex l.1351–1360.
   - Hida's w-twisted π^r_s tower in place of ϖ_{1,*}.
   - Any downstream input used to patch C: inverse-limit identification, density, H9R15 localization,
     f-branch extraction, weight-one specialization, the big Kummer trace identity.
   - Stating the next gate at the end is required and is not a patch.
3. **Status vocabulary:** PROVED, PROVED_FORMAL, NOT_PRINTED, TYPE_MISMATCH, FALSE, DEFECT, INPUT_DEFECT_SUSPECTED.
   Keep NOT_PRINTED distinct from FALSE. Never give probabilities or confidence percentages.
4. **Write as you go.** Output caps count reasoning, and long case analyses held in one response have been lost.
   - Finish one item, then write its file with a Bash heredoc, and only then start the next item.
   - A truncated turn must lose at most one item.
5. **Files you may create:** only this directory (`03`–`10` below, plus `_verify/` for any new script).
   - Never modify Lanes 1–5, nor 00/01/02 here.
   - Numerical checks are welcome, e.g. copying `~/H9R16C_LANE5_MPC_PROVER_2026-09-15/_verify/msym_check.py`
     into `_verify/` and adding a tame case N_g | N, or a finite-level contraction identity.
     Record the command line and the log.
6. **Sources.** Use local copies (02 §D).
   - If something needed is not on disk, fetch it only from arXiv or the publisher, and record the URL and SHA-256.
   - Otherwise record it as NOT_OBTAINED.
7. **No outside actions.** No Lean, no Aristotle, no email or messages, no publishing, sealing or git.

## §3. Reading order

1. This directory: 00 (operator freeze), then 02 (closed layers, frozen H9R16-A/B definitions, source anchors).
2. `~/H9R16C_LANE5_MPC_PROVER_2026-09-15/`:
   - 05 §2–§4 is the text under review;
   - 01 and 07 for types and referee items R1–R4;
   - 02–04 only for statements.
3. `~/H9R16C_LANE2_KUMMER_TRANSITION_SQUARE_2026-09-15/`: 01 (T3–T5), `_parts/03_1`–`03_4`, 04, 05.
4. `~/H9R16C_LANE4_HOSTILE_OBSTRUCTION_2026-09-15/`: 01 §6–7; 03 §1, §2, §7; 04 §1–§4; 05.
5. `~/H9R16C_LANE1_W_w_DICTIONARY_2026-09-15/`: 00 and 04 (R2, R3). The α-dictionary is not needed on BCPV's point model.
6. `~/H9R16C_LANE3_PRIMARY_LITERATURE_2026-09-15/`: 00 and 04 (E′(a), E′(b), D4).

## §4. Files to write (in this order)

- `03_ITEM1_POINT_OBJECT.md`: the explicit map from the Lane 5 contraction and packaging to Φ̄_r^mod ∈ 𝒫_r^♮;
  the precise ⋆-action; the carrier B_r^bal; the tame push-down used; the orientation of Γ_A versus H9R16-A/B's Φ^mod.
- `04_ITEM2_HOM_VALUED_D4.md`:
  - the typed étale target T_r^♮;
  - the ⋆-equivariance over K_0 of Contr_r^{A_r} restricted from BCPV's triple-dagger module;
  - evaluationwise D4 ⇒ Hom-valued D4;
  - descent and injectivity.
- `05_ITEM3_TAME_PUSHDOWN_AND_TOWER.md`:
  - which tame degeneracy BCPV use (with line numbers);
  - how L5-T5 transports it;
  - the full chain SQ + D4_{r+1} + MPC + Cor 4.11 + D4_r + normalizations ⇒ the typed relation;
  - Kummer injectivity in the correct ambient module.
- `06_ITEM4_RANK_FACTOR.md`: where a |G_r|, p^3, p^{3(r−1)} or type-A factor could enter (packaging identification
  G vs μ_r; the post-contraction dagger group; the level step), and whether it does.
- `07_ITEM5_TAME_TWIST.md`: compatibility of the tame twist with ϖ_{1,*}, π_r, 1 ⊗ N_{r+1,r} and the normalizations.
- `08_INVERSE_LIMIT_AND_NEXT_GATE.md`:
  - if closed: the exact inverse-limit point module and the exact statement of G_BIG_KUMMER_TRACE;
  - if not closed: what is blocked.
- `09_VERDICT.md`: the final block, then one status line per item.
- `10_FILES_CONSULTED.sha256`.

**Final reply to the coordinator:** exactly the §1 verdict block (plus the inverse-limit module and next gate if closed),
then one line naming the files written. Nothing else.
