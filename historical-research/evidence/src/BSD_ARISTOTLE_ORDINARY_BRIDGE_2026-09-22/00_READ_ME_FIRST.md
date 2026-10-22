# READ ME FIRST

## What this is
A **hostile source audit** of one implication, on one curve, at good-ordinary primes only. It is not a research
brief and not an invitation to extend the project.

## Read in this order
1. `INPUTS.md`  — the retained/certified facts. Do not re-derive them. §7 lists what is NOT source-read.
2. `GATE.md`    — scope limits, forbidden assumptions, verdict definitions. Binding.
3. `TASK.md`    — the seven tasks and the deliverable.
4. `evidence/`  — supporting records, listed below.

## The one-line question
Conditional on `[c_2] != 0`, and given the certified `L(E^{-7},1) != 0`, do existing theorems already prove
`Sha(E/K)[p^inf] = 0` at good-ordinary `p` — or what is the first missing theorem?

## Evidence files
| file | what it is |
|---|---|
| `D7_CERTIFICATE_RESULT.md` | the 2026-09-22 certificate, its validation record and its explicit scope limits |
| `BRANCH_THETA.md` | where `c_2` lives, at line level: the `I^2/I^3` coefficient of the stabilized Gross-point theta |
| `STAGE5_A0_RESOLVED.md` | A0 = theta order 2 / full order 4, and the `2 max(r^+,r^-)` derivation |
| `STAGE6_A2_SPLIT.md` | the A2a/A2b split, and the Lambda-module example showing A2a does NOT follow from order+unit alone |
| `STAGE7_A2A_ROUTE_LIVE.md` | the tau-equivariant route, and the configuration enumeration Task 5 replays |
| `STAGE8_D7_CERTIFIED.md` | what the certificate discharges |

**The evidence files are this project's own reasoning, not authority.** Several of their claims about
Bertolini–Darmon Theorems 2.7 / 2.18 / 2.23 / Remark 2.21 were accepted without source-reading — `INPUTS.md` §7 says
so explicitly. Where they conflict with the sources, **the sources win and you should say so.**

## Two things this project has got wrong before, for calibration
* A limitation of *one theorem* was promoted into a structural claim about the whole branch, and had to be withdrawn
  when newer literature covered the missing case. Check what exists before declaring a gap.
* A `Lambda`-module argument that dropped complex conjugation produced a counterexample that dissolved once the
  `tau`-structure was restored. Keep the eigenspace decomposition in view throughout.

## What a good return looks like
A theorem-by-theorem audit, one principal verdict, the closing ledger, and — if the chain breaks — the **first**
missing implication stated precisely enough to be looked up or attacked. Early negatives are welcome.
