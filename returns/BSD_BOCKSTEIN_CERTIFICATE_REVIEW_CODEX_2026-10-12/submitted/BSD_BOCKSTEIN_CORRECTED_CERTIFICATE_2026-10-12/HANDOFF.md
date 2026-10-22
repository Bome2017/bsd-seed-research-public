# Narrow review and integration handoff

**Status to preserve:** SHARPER_CONDITIONAL_CERTIFICATE_DERIVED; NO_NEW_PRIMARY_RESULT.

This package contains an executed derivation and checks, not a request to repeat the investigation. Integrate only additively, without editing frozen inputs or promoting an endpoint.

## Review target

Check `PROOF.md` §§2–4 independently against the retained October 7 content proof. The decisive statement is

\[
 m=\tau+b+v_p((g/d_1)(0)),
\]

where `d=U*d1` is the characteristic generator extracted from the actual maximal-minor vector, and `b` is the image index of the actual first Bockstein into primitive `H^2_tf`.

The proof's critical points are: the all-height-one inequality includes `(p)`; the nonprimitive augmentation of the kernel generator is retained; constant Smith operations are p-unimodular; the coefficient of `U` in the minor vector is the torsion-index product times the Bockstein row; and the arithmetic equality `tau=length Sha+w` is used only at its retained grade.

Do not demand a new main-conjecture equality merely to obtain the one-sided certificate. The defect is nonnegative under the old inequality, which is enough.

## The single useful unresolved interface

To use existing numerical height data, establish an integral identification between its height row and this precise Bockstein row, including the target lattice, cyclotomic variable, and local conventions. An equality up to a rational scalar whose p-valuation is unknown is insufficient. A p-unit ambiguity is harmless. The archived Exit 1 claim is evidence to inspect, not an already accepted identification.

Until that interface and an actual derivative value are supplied, the residue checker produces only a conditional valuation result. Do not feed an arbitrarily normalized height row to the checker and promote its output to a seed theorem.

## Permitted conclusions after a correct review

The additive status may record the improved conditional bound

\[
 \operatorname{length}\Sha[p^\infty]\le m_p-w_p-b_p
\]

and its parity criterion on the same retained cohomological domain. No actual prime is newly settled by the review itself. FIN, ORDER9, Q36 and the named exceptional-primary remainder remain unchanged.

A source-unit equality would additionally remove the defect, but that is a separate claim requiring a full source check. No source-unit premise is needed for the weaker conclusion already derived here.

## Reproduce the delivered computation

```bash
python3 checks/test_certificate.py
python3 refined_certificate.py examples/abstract_improved.json
```

The tests are standard-library exact rational/integer arithmetic. The reported totals overlap where explicitly indicated: the basis/gauge variants form part of the first-jet total. None is a computation of seed arithmetic.

## Suggested additive destination

`work/returns/BSD_BOCKSTEIN_CORRECTED_CERTIFICATE_2026-10-12/`

`CURRENT_STATE_ADDITION.md` is proposed navigation text only. No automatic script edits the current state, and no remote write was made in this pass. The accompanying additive patch creates the return directory; it does not promote the text into `CURRENT_STATE.md` or modify the research release.
