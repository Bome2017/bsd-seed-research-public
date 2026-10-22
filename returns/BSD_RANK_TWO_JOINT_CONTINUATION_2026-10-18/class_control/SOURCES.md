# Source checks

Accessed 2026-10-18. Sources were read for the limited interfaces below, not exhaustively audited.

- PARI official `bnfcertify`: https://pari.math.u-bordeaux.fr/dochtml/html-stable/General_number_fields.html#bnfcertify . Flag1 is a quotient-only whole-class certification. No prime-only flag is documented.
- Hofmann–Johnston, *Algorithms for p-rationality and for p-saturation of units*, arXiv:2609.15190v1, §§12–15: https://arxiv.org/html/2609.15190v1 . The arbitrary-field algorithm retains class information; the class-free shortcut uses real cyclotomic units and their index formula.
- Hecke documentation: https://docs.hecke.thofma.com/dev/manual/number_fields/p_rationality . Implementation pinned at a94794874196e6181b62ceca7df82f4f52fa8200, `src/NumField/NfAbs/prational.jl`: https://github.com/thofma/Hecke.jl/blob/a94794874196e6181b62ceca7df82f4f52fa8200/src/NumField/NfAbs/prational.jl . The general `_is_class_number_divisible` invokes the class-group routine with the selected GRH policy.
- Fabrice Etienne, *Computing class groups by induction with generalised norm relations*: https://www.math.u-bordeaux.fr/~fetienne002/computing_class_groups.pdf . Introduction, Theorems A–C and the displayed definition of generalized norm relation. The finite-group obstruction in this return is a new direct calculation, not a theorem attributed to the paper.
- Elsenhans–Voight, *Computing class groups and unit groups in Magma*, 2025 version: https://jvoight.github.io/articles/clgpunitgp-magma-02Oct25.pdf . §§1,4 describe proof regimes and factor-base generation versus relation/saturation checks. No Magma computation was run.

The BNF log and field bindings are recorded in INPUT_BINDINGS.json. There is no rigorous zeta-residue enclosure in the inspected small_conductor7 return. The provisional real regulator alone is not such an enclosure.
