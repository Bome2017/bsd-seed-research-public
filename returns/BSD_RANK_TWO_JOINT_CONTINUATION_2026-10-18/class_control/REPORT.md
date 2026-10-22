# Complete class contribution screen

Date: 2026-10-18
Status: NO_NEW_COMPLETE_CLASS_BOUND; SMALLER_FIELD_SHORTCUT_EXCLUDED_FOR_FAITHFUL_CHARACTER.

The cached 11a1, p=7 calculation still proves only the unit and valuation conclusions previously recorded. Its surviving source injects into the **ordinary** class group component Cl(A)[7]^chi. This pass did not prove that component zero or bound its dimension. No seed endpoint changes.

Three changed certification routes were checked before attempting another field calculation.

1. PARI's weaker `bnfcertify(B,1)` was already the failed operation. The official documentation says a successful return proves the true class group is a quotient of the computed group. It has no documented coefficient-prime-only flag. The retained log contains only the start marker, the Zimmert bound 1593360910660456325376, and an alarm interrupt. There is no partial class-index certificate and no certified upper index prime to seven in that record. The process's exit code zero is not success. [PARI documentation](https://pari.math.u-bordeaux.fr/dochtml/html-stable/General_number_fields.html#bnfcertify)

2. Hofmann–Johnston's September 2026 algorithms were checked in the primary paper and current implementation. The class-free method uses the special cyclotomic-unit index formula for real cyclotomic fields. The arbitrary-field quasi-p-rationality test controls units and local conditions; the p-rationality step still needs class-number information. Hecke's general `_is_class_number_divisible` explicitly calls `class_group(OK; GRH=GRH)`. Our field has signature (6,21), so it is outside the real-cyclotomic shortcut. Running that predicate would not bypass the missing class certificate. [Paper, §§12,15](https://arxiv.org/html/2609.15190v1) · [Pinned implementation](https://github.com/thofma/Hecke.jl/blob/a94794874196e6181b62ceca7df82f4f52fa8200/src/NumField/NfAbs/prational.jl)

3. A genuinely changed finite experiment tested generalized norm relations through smaller subfields. It enumerated all 84 subgroup conjugacy classes of GL2(F7). Every subgroup of index below 48 meets the scalar center nontrivially. The minimum index of a center-disjoint subgroup is 48. Consequently, the faithful scalar character cannot be reconstructed through strictly smaller-degree fields inside this normal closure, even with rational coefficients. The proof and exact scope are in PROOF.md; the whole enumeration and replay are included. This rules out this particular subfield shortcut. It does not exclude relations involving fields of degree at least 48, unrelated arithmetic maps, or analytic class certification. [Generalized norm-relation framework](https://www.math.u-bordeaux.fr/~fetienne002/computing_class_groups.pdf)

The saved regulator is approximately 8.6541921559e19, but no unconditional interval for the Dedekind-zeta residue was supplied alongside it. A floating regulator and a provisional class number do not furnish a class-index upper bound. An analytic alternative would have to supply an independently rigorous residue estimate together with adequate unit-index control; changing software alone does not supply either. The source distinction between generator completeness, relations and analytic saturation is explicit in the current Magma account. [Elsenhans–Voight](https://jvoight.github.io/articles/clgpunitgp-magma-02Oct25.pdf)

The useful decision from this pass is narrow: do not rerun the same certification, do not call unit p-saturation a class certificate, and do not spend on strictly lower-degree subfields for the faithful component. A successful next class calculation still needs a certified generating source or a rigorous upper bound on the missing class index. No such bound has been obtained here.

Arithmetic cost was under 12 seconds in GAP, including two corrected startup failures. No new BNF, ray class group, paid job, or publication was run.
