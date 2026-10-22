# Aristotle project (revision 2): audit the tame Stage-A derivation, then build point sections toward a rank-two switch (BSD seed, 2026-10-07)

**Read order**
1. `CURRENT_FRONTIER.md`
2. `DELTA_TASK_OPENAI_RANK2_REV2.md`, which governs this run
3. `TASK.md`

**What is new in revision 2**
- `4_CODEX_STAGE_A/` holds Codex's Stage-A derivation (lab bb6ed896), its next-step note with (L2), and Claude's desk review (SUPPORTED_AT_DESK_LEVEL).
- **Stage A′** is a hostile audit of that derivation, with priority checks on Morgan–Smith, the cochain normalization and the Chebotarev prescription.
- **Stage B′** proceeds in order:
  - the second-order joint lifting (L2) of both point sections with the same η;
  - the cokernel of the correction map;
  - the sections to order three;
  - only then the rank-two determinant switch.
- **Stage C** is unchanged.
- **Corrections carried:**
  - ℚ(M_E[p]) is not the class-group receiver field;
  - restriction is not deformation obstruction;
  - the one-sided-detector wording for p = 17.
- **New statuses:** `POINT_SECTIONS_ORDER3` and `SECOND_ORDER_OBSTRUCTED`.

The packet and closed lanes are as in revision 1. The OpenAI sources are not bundled; read them from github.com/openai/math if used. The Lean templates are on v4.28.0.

**Submission:** see `SUBMIT_COMMAND.txt`.
