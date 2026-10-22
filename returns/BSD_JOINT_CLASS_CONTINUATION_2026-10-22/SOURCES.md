# Inputs, source checks, and scope

The immediately preceding lab snapshot is e79f03a8ee8a0eb4d2d9a95cfd8c905694c03ee6
on research/state-sync-2026-10-04. All earlier return paths below are inside
work/returns at that snapshot; no frozen record was altered.

- BSD_PRIMARY_TORSION_BOUND_2026-10-22: actual seed primary-packing test,
  its retained analytic constants and its scoped scaling failure.
- BSD_CLOSED_CLASS_CONSTRUCTION_2026-10-20: COMPLETE_CLASS_BOUND.md supplies
  the exact relative regulator conventions, norm-surjectivity argument,
  whole relative class bound97, field objects and analytic outward bounds.
- BSD_CLASS_MAP_AND_PARTIAL_RELATIONS_2026-10-20: complete1664 control and
  partial ideal-relation history; no fresh control computation is claimed.
- BSD_GENUINE_RELATIVE_CLASS_METHOD_2026-10-20: generation-mod-p suffices
  for upper presentations; the failed genuine relative-ideal source.
- BSD_COMPANION_CLASS_AND_CHARACTER_EXPERIMENT_2026-10-15: actual class-map
  accounting and the already-attempted source quotient certification.
- BSD_JOINT_REPAIR_TARGET_EXPERIMENT_2026-10-15: the common unit/local repair
  construction was already present and is not a new proposal here.
- BSD_RANK_TWO_JOINT_CONTINUATION_2026-10-18: smaller-subfield obstruction
  and the previously checked p-rationality/source limitations.

The new arithmetic input copies and SHA-256 bindings are in
arithmetic/INPUT_BINDINGS.json. Their exact field and maximal-order grades
are retained. The arithmetic program does not use BNF class groups, known
Sha dimensions or analytic values. The analytic checker binds its retained
input separately and does not evaluate an L-function.

Primary literature checks and their source-specific scope are in
sources/PRIMARY_SOURCE_ADMISSION.md. The root also checked the official
[PARI number-field documentation](https://pari.math.u-bordeaux.fr/dochtml/html-stable/General_number_fields.html)
and [library documentation](https://pari.math.u-bordeaux.fr/dochtml/html-stable/usersch6.html):
bnfcertify(flag1) certifies a class-group quotient; bnftestprimes verifies
generation through a supplied bound. Neither justifies assuming a selected
factor base is complete. No undocumented p-only certification mode is used.

The elementary correspondence, parity, presentation and rational-isolation
deductions are written here. They are not attributed as new published
theorems, and the finite controls are not seed class computations.
