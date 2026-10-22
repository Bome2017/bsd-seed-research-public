# Corrections to carry with the Aristotle return

Original return files are preserved unchanged. This review has precedence for
the following scope and evidence attributions.

1. **Exact 1274 residue.** The original `chainCert_true` proves the modular
   valuation/unit checks, not the numeric residue 1274. Its Python JSON also
   omits the residue. The independent review calculation reproduces 1274 and
   adds a separate exact Lean assertion. No change to BFR's mathematical proof
   is required, because valuation one suffices.
2. **Genus-two argument.** Different j-invariants do not imply different
   p-torsion representations. The two Frobenius counts at 11 and 19 in this
   review establish the required nonisomorphism for every odd p. This excludes
   direct equivariant linear transfer from E2[p]; it is not a proof that every
   use of the genus-two curve fails. The E factor of its Jacobian remains E.
3. **Prior theorem identity.** B.20 concerns unit Kurihara witnesses, not the
   class-group receiver. The receiver's actual predecessor is the separately
   bound good-prime forward comparison. BFR extends that comparison; it does
   not extend B.20 or settle its bad-prime exclusions.
4. **Formal grade.** BFR is not a Lean theorem in this package. The submitted
   finite arithmetic check is also not linked formally to the p-adic group law.
   The model, point, Hensel and finite-arithmetic theorems compile at their
   literal scopes. Their names/comments must not substitute for these scopes.
5. **Degree at 4547.** Preserve the original return's caution: the third
   translation constituent is not proved full. Do not report the old full
   degree as established at this prime.
6. **Endpoint grade.** No new primary component is proved finite or zero.
   No part of the missing uniform upper estimate, ORDER9 or Q36 is supplied.
   No claim of literature novelty is justified by the internal collision search.
