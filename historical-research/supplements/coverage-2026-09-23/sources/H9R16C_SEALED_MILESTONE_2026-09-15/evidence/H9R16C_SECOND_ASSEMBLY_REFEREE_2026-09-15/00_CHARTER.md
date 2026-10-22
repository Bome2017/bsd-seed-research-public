# 00 — Charter: SECOND, INDEPENDENT assembly referee for H9R16-C (2026-09-15)

## §1. What this is

A first assembly referee adjudicated H9R16-C and returned CLOSED. The operator's standard is two independent
audits. You are the second. You are given the **statements** it reached (01) and the same frozen inputs it had —
**never its reasoning**. Your job is to derive each statement yourself, or to find the first exact defect.

The operator's own framing: H9R16-C is treated as mathematically closed at the current audit tier, not sealed.
Sealing depends on this run.

## §2. Independence wall (binding)

**Do not read, list, grep, or open** any of:

    ~/H9R16C_FINAL_ASSEMBLY_REFEREE_2026-09-15/03_ITEM1_POINT_OBJECT.md
    ~/H9R16C_FINAL_ASSEMBLY_REFEREE_2026-09-15/04_ITEM2_HOM_VALUED_D4.md
    ~/H9R16C_FINAL_ASSEMBLY_REFEREE_2026-09-15/05_ITEM3_TAME_PUSHDOWN_AND_TOWER.md
    ~/H9R16C_FINAL_ASSEMBLY_REFEREE_2026-09-15/06_ITEM4_RANK_FACTOR.md
    ~/H9R16C_FINAL_ASSEMBLY_REFEREE_2026-09-15/07_ITEM5_TAME_TWIST.md
    ~/H9R16C_FINAL_ASSEMBLY_REFEREE_2026-09-15/08_INVERSE_LIMIT_AND_NEXT_GATE.md
    ~/H9R16C_FINAL_ASSEMBLY_REFEREE_2026-09-15/09_VERDICT.md
    ~/H9R16C_FINAL_ASSEMBLY_REFEREE_2026-09-15/10_FILES_CONSULTED.sha256
    ~/H9R16C_FINAL_ASSEMBLY_REFEREE_2026-09-15/11_COORDINATOR_AUDIT.md
    ~/H9R16C_FINAL_ASSEMBLY_REFEREE_2026-09-15/_verify/msym_tame_check.py
    ~/H9R16C_FINAL_ASSEMBLY_REFEREE_2026-09-15/_verify/tame_check.log

If you open one by accident, say so in your verdict file; do not pretend otherwise.

**You may read:**
* `~/H9R16C_FINAL_ASSEMBLY_REFEREE_2026-09-15/00_OPERATOR_FREEZE_RECORD.md`, `01_REFEREE_CHARTER.md`,
  `02_CLOSED_LAYERS.md`, `02a_COORDINATOR_ERRATUM.md` — all written **before** the first referee ran
  (operator freeze, operator charter, the closed-layer ledger of Lanes 1–5, and a coordinator erratum).
* All five lane directories `~/H9R16C_LANE{1,2,3,4,5}_*_2026-09-15/` and their `sources/`, `_parts/`, `_work/`,
  and Lane 5's `_verify/msym_check.py` (the original checker).
* The frozen H9R16-A/B text: `~/.claude/paste-cache/a81606aed099d4e9.txt` l.161–215, l.229–300.

## §3. Inputs you must NOT re-prove (they are frozen upstream)

02 §A: A1 MPC_r (`ϖ_1^*A_rϖ_{1,*} = A_{r+1}N_{r+1,r}`, `d_r = 1`), A2 the norm element, A3 Lemma W,
A4 the group-ring form, A5 the tame transport, A6 **scalar** D4 (evaluation form, from AJ-functoriality).
If you believe one is false, record `INPUT_DEFECT_SUSPECTED` with the exact location and do not repair it.

Everything in 01 is a **claim to adjudicate**, not an input.

## §4. Where the operator wants pressure

Three structural points, in this order:

1. **C1**: `B_r^bal ≅ R_r` after the `A_r`-transport — including whether the transport hypothesis is really
   available for both auxiliary factors (the `g` / `g^c` asymmetry, `ρ_r` as an anti-involution), whether the
   quotient is free, and whether anything downstream silently uses freeness before it is earned.
2. **C3 + the contravariance in C4**: the Hom-valued D4 upgrade, and `π_r^*` as a pullback along a carrier map
   that goes the other way. Type errors hide here.
3. **C7 + the normalizations in C4**: preservation of the tame `g^c`/`ε_g^{-1}` twist and of the `(U'_p)^{-r}`,
   `(U'_p)^{-2r}` normalizations through the tower.

The other claims still need a verdict; these three get the hardest look.

## §5. Rules

1. Derive, do not assume. For each claim: state the types, then either prove it from the frozen inputs, or give
   the first exact defect. "It follows formally" is not an adjudication — write the maps.
2. Write one file per claim (§7) with a Bash heredoc **before** starting the next claim. Output caps count
   reasoning; a truncated turn must lose at most one claim.
3. Numerical checks are welcome and are yours to design. Copy Lane 5's `_verify/msym_check.py` into this
   directory's `_verify/` and build on it. Do not read the first referee's scripts or logs (§2).
4. Prohibited: BCPV (4.9) (`defn_3rd_vertical_map`, BCPV.tex l.1351); Hida's `w`-twisted tower in place of
   `ϖ_{1,*}`; any downstream input (inverse-limit identification with BCPV's module, density, H9R15
   localization, `f`-branch extraction, weight-one specialization, the big Kummer trace).
5. Never modify the lane directories or the first referee's directory. Write only inside this one.
6. Vocabulary: PROVED / PROVED_FORMAL / NOT_PRINTED / TYPE_MISMATCH / FALSE / DEFECT / INPUT_DEFECT_SUSPECTED.
   NOT_PRINTED is not FALSE. No probabilities, no confidence percentages.
7. No Lean, no Aristotle, no messages, no publishing, no git.

## §6. A standing wording requirement (operator, 2026-09-15)

Whenever `B_r^bal ≅ R_r` is written, it must carry its hypothesis: **after the `A_r`-transport and passage to
the transported commutative primed ordinary Hecke model** (`ι_r(u') = A_r^{-1}ρ_r(u')A_r = u'`). It must never
be applied to the raw pre-transport `g` / `g^c` correspondence modules. If you find the claim true only under a
narrower hypothesis, say exactly which.

## §7. Files to write, in order

`02_C1_CARRIER.md`, `03_C2_POINT_OBJECT.md`, `04_C3_HOM_D4.md`, `05_C4_TOWER_RELATION.md`,
`06_C5_PUSHDOWN_INDEPENDENCE.md`, `07_C6_RANK_FACTOR.md`, `08_C7_TAME_TWIST.md`, `09_C8_INVERSE_LIMIT.md`,
`10_VERDICT.md`, `11_FILES_CONSULTED.sha256`.

**Final reply:** the verdict block below, then one line naming the files written. Nothing else.

    SECOND_REFEREE = CONFIRMS_ALL
      or
    SECOND_REFEREE = DEFECT_FOUND — FIRST EXACT DEFECT = <claim id, exact statement, why>

    then one line per claim:  C1 … C8 = CONFIRMED | CONFIRMED_WITH_NARROWER_HYPOTHESIS | DEFECT | UNDECIDED
