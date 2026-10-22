# Desk review of the derivative-content bound recorded

2026-10-07. **NEW_LENGTH_ARGUMENT_SUPPORTED_UNDER_RETAINED_INPUTS — USER_SUPPLIED_DESK_REVIEW_RECORDED.**

The user supplied a detailed review of the maximal-minor and global-duality argument at lab commit c194a996a627e5bdff5c237e43f9f4c2300b7ecf. It supports the conditional bound

\[
\operatorname{length}_{\mathbf Z_p}\Sha(E/\mathbf Q)[p^\infty]+w_p\le m_p
\]

for the specified nonzero derivative, and therefore the sufficient vanishing test

\[
\delta_p\ne0,\qquad m_p-w_p\le1.
\]

The formal review portion is preserved in [SUBMITTED_REVIEW.md](SUBMITTED_REVIEW.md), with display formatting normalized. The preceding narrative supplied the same conclusions, explicitly distinguished primary finiteness from finiteness of the whole Sha group, and made no coefficient computation or new-prime claim. No separately linked review file or archive was available in this message.

## What the review supports

| Interface | Review finding | Boundary preserved |
|---|---|---|
| Actual minors and the specialized H² torsion | The coordinate content of eta(0) retains finite errors invisible at height one | The all-height-one integral Kato inequality remains an antecedent input |
| Fine Selmer and local point correction | length tors H² = length Sha + w_p, with positive sign | The retained local vanishings and nonzero-derivative finiteness implication remain required |
| Parity | The finite p-primary component has even length | Finiteness of the entire Sha group is not assumed |
| Nonprimitive derivative | m_p-w_p=1 can still certify vanishing | No division or replacement of the actual source class |
| p=17 interpretation | Matched coefficient valuation 1 or 2 suffices | No K17 digit supplied; an unspecified finite support does not establish matching at 17 |
| Supersingular scope | The cohomological theorem does not use ordinarity or nonsingular heights | An ordinary numerical formula does not replace the separate supersingular conventions |

This worker separately re-derived the review's matrix example; [FINITE_ERROR_CHECK.md](FINITE_ERROR_CHECK.md) records the exact calculation. It agrees with the earlier proof's treatment of finite errors. It is not a new arithmetic result.

## Current grade and remaining obligation

The new length argument now has a supplied desk review supporting its stated deduction. This is not a Lean certificate, a human-expert certification, a novelty assessment, or a new review of all preceding source transports. Those distinctions are not changed by publication.

The unchanged arithmetic task is to prove, for the actual source,

\[
\delta_p\ne0,\quad m_p-w_p\le1
\quad\text{outside one fixed finite set}.
\]

This ledger supplies no such estimate. No new coefficient, primary result or uniform bound was obtained. **FIN, ORDER9 and Q36 remain unchanged.**

The original sealed proof return remains byte-for-byte unchanged. Its historical “independent review required” header is preserved; this later ledger records the subsequently supplied review and its exact scope. No candidate-search package, remote research job, numerical campaign or expert-repository promotion was initiated.

## Pinned proof

[Original report](https://github.com/Bome2017/bsd-seed-lab/blob/c194a996a627e5bdff5c237e43f9f4c2300b7ecf/work/returns/BSD_KATO_CONTENT_BOUND_CODEX_2026-10-07/REPORT.md)

[Full proof](https://github.com/Bome2017/bsd-seed-lab/blob/c194a996a627e5bdff5c237e43f9f4c2300b7ecf/work/returns/BSD_KATO_CONTENT_BOUND_CODEX_2026-10-07/CONTENT_BOUND_PROOF.md)

[Correlated valuation target](https://github.com/Bome2017/bsd-seed-lab/blob/c194a996a627e5bdff5c237e43f9f4c2300b7ecf/work/returns/BSD_KATO_CONTENT_BOUND_CODEX_2026-10-07/VALUATION_TARGET.md)
