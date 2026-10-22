# Item 3 — Outward text at pinned commit 9828eae

**VERDICT: CONFIRMED_WITH_CORRECTIONS.** The route-K theorem and the grade qualifications are supported by Item 1. One numerical explanatory sentence needs correction before outward use. This is not a new gap in the <=9 deduction.

## Verified state

Read-only local inspection: branch v0.2.5-bank, HEAD 9828eae9bb8f97c78f80b1a970b717679e453e70, clean working tree. The two inspected current files match their pinned Git objects. The prior local commits are 706efb5 and c4e4b83. No remote fetch, push, tag, build or release-verifier rerun was performed here.

## Required wording correction: paper/sections/04_primary.tex, route-K assembly

Current exact sentence:

> For the $\gamma$-free determinant, whose valuation is $2$, the chain would give only $\#\Sha[3^\infty]\le81$.

This conflates the actual determinant with the counterfactual bad normalization. The valid relation is

    v_3(#Sha[3^inf]) <= 2 - v_3(Reg_gamma)
                       = 4 - v_3(Reg_3).

The ACTUAL gamma-free valuation 2 gives <=9 after conversion, not <=81. The <=81 scenario would arise if the only established input were gamma-free valuation ZERO, so normalized valuation -2. Merely inserting raw valuation 2 into the formula for normalized valuation would instead make an unjustified stronger bound; it is not a legitimate alternative proof.

Replacement sentence:

> The gamma-free determinant has valuation 2; division by (log_3 kappa(gamma))^2 gives normalized valuation 0. If only valuation 0 for the gamma-free determinant had been established, the resulting bound would be 81 rather than 9.

The S.3K Imports field's phrase “the gamma-free determinant would give only <=81” needs the same qualification. Its Regulator field already records the right arithmetic. Make the source-spec change and regenerate the claim outputs in the release workflow; do not patch a generated claim file alone.

## Precision corrections, not new theorem gaps

- S.3K says “12.5(4) is printed for V.” More precisely: its FINAL LENGTH INEQUALITY is printed for V; its integral-containment assertion for Z(f,T) is still used and was not withdrawn.
- An updated review label may now add this cross-family reading, with its scope and retained inputs. It must not upgrade to human-reviewed, fully recomputed or formalized.
- The paper's equality Col(z)=L_3 should continue to carry the claim record's fixed-period/Tate-twist dictionary. A raw unshifted Kato function is not the SW power series at the same character.
- The Jones import is read from the author's copy; the existing qualification about unreconciled journal numbering remains appropriate.

No other overstatement in the bounded S.3K/route-K text was identified. This is not a fresh release custody audit or approval to publish. Patch suggestions are supplied in this output folder only; the repository was not edited.
