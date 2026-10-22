# BSD seed: a corrected derivative certificate

October 12, 2026.

**SHARPER_CONDITIONAL_CERTIFICATE_DERIVED; NO_NEW_PRIMARY_RESULT.**

I inspected both connected repositories, including the lab's current state and selected live proofs on the October 11 record. I derived and tested a modification to the retained Kato-content criterion. This is an additive research return, not a claim that FIN, ORDER9, Q36, or another primary component has been settled.

## Repository snapshot

The relevant remote snapshots inspected were:

| Repository | Inspected reference | Commit |
|---|---|---|
| `Bome2017/bsd-seed-lab` | `research/state-sync-2026-10-04` | `02e86ce876cb83cef314b53d86f73a193298b203` |
| `Bome2017/bsd-seed-research` | `v0.2.6` | `8414aea58180f3a18bcee7fba23475c8cac90996` |

The lab's branch name is historical; its current-state file is updated October 11. The default branches are older snapshots. The current lab record and return index, not the default-branch commit search, were used to select the mathematical starting point. This was a targeted review of active material, not a file-by-file audit of either repository.

The latest CM-control report already obtains a nonzero actual source on the 167 control through a rank-one height calculation. The signed-theta return already contains an explicit countercontrol showing that its scalar Fitting inclusion and a quadratic unit alone do not eliminate a finite pair. Neither result was promoted to a seed theorem in this return. [S0, S5, S6]

## The modification that survives

Let the actual transported, smoothed Kato derivative be

\[
 \delta_p=A_p\kappa(P_1)+B_p\kappa(P_2),\qquad
 m_p=\min(v_p(A_p),v_p(B_p)).
\]

Retain

\[
 w_p=\min_i v_p(\log_\omega(P_i)/p).
\]

The supported October 7 criterion bounds the primary Sha length by \(m_p-w_p\). [S1]

Define \(b_p\) using the actual first Bockstein map

\[
 \overline\beta_p:H^1_S\longrightarrow (H^2_S)_{\mathrm{tf}}.
\]

After the retained nonzero-derivative argument has identified \(H^1_S\) with the saturated point lattice and the target has rank one, \(b_p\) is the index of its image in the **primitive** target lattice. Thus it is the common valuation of the two entries of this map, not a chosen rescaling of a height determinant.

The exact algebra now gives

\[
 \boxed{m_p=\operatorname{length}\Sha[p^\infty]+w_p+b_p+e_p,
 \qquad e_p\ge0.}
\]

Consequently,

\[
 \boxed{\delta_p\ne0,\quad m_p-w_p-b_p\le1
 \Longrightarrow\Sha[p^\infty]=0.}
\]

The full proof, including the definition of \(e_p\), is in `PROOF.md`. It uses the original all-height-one Kato inequality, not a replacement by a main-conjecture equality. Finite specialization errors are retained.

### What is new relative to the supported record

The archived Exit 1 report already suggested a Bockstein-content equality, with a claimed ordinary source-unit comparison. The current ledger expressly left that equality and its source hypotheses pending. This return does not claim to have invented that proposal. [S3]

The contribution is a complete first-jet/maximal-minor derivation with a **nonnegative defect left visible**. It establishes a one-sided corrected certificate without having to settle the claimed unit comparison. It also supplies a precise finite-precision acceptance rule and executed exact controls.

The old proof established that every first derivative of a maximal minor is divisible by the torsion-index product. The calculation here retains the rest of that coefficient: it is exactly that product times the Bockstein row. This is the additional factor that can safely be subtracted.

## Why this is a useful change—and its present limit

The older criterion can fail because the Bockstein map is divisible by \(p\), even when that divisibility is unrelated to Sha. The corrected criterion allows that measured divisibility. For instance, with \(w_p=0\), \(m_p=3\), and \(b_p=2\), the old upper bound is three; the corrected upper bound is one, so finite alternating parity forces zero. A compatible exact algebraic model is supplied. This is not an assertion that those are values for the seed.

Only **lower bounds** for \(w_p\) and \(b_p\) are needed once \(m_p\) is detected exactly. Thus this refinement does not require separate proofs that the two correction factors are units at almost all primes. It still requires nonvanishing of the actual derivative and independent control of the corrected excess. It does not establish an equivalence with FIN without further hypotheses.

There is an important practical qualification. Exit 1 reports Bockstein units on its 70 ordinary test primes. Those numerical identifications were not rerun or integrally source-matched here. On any row where \(b_p=0\) is correctly established, the new test coincides with the old test. Therefore no immediate numerical improvement at one of those primes is claimed. [S3]

## Scope and unresolved interfaces

The cohomological consequence uses the retained domain

\[
 p\ge5,\qquad p\nmid N,\qquad p\notin\{19,59,487\},
\]

with all actual smoothing and simultaneous source/lattice-transport conditions preserved. It does not introduce ordinarity into the algebra. A separate numerical comparison using ordinary heights must retain its own narrower hypotheses.

This return does **not** establish that a pre-existing numerical height row is the map \(\overline\beta_p\) with exactly the required integral target normalization. The source matching in that step remains a genuine arithmetic interface. It also does not set \(e_p=0\); the sufficient inequality does not need that assertion.

The defect is

\[
 e_p=v_p(\rho_p(0)),\quad
 \rho_p=g_p/d_{1,p}\in\mathbb Z_p[[U]],
\]

where \(z_p=Ug_p\eta_p\) and the actual characteristic generator is \(Ud_{1,p}\). Proving a bound on this residual source contribution is not accomplished by naming it. No fixed cross-prime scalar or tame comparison has been constructed here.

## Executed checks

Run:

```bash
python3 checks/test_certificate.py
python3 refined_certificate.py examples/abstract_improved.json
```

The first command performs 864 exact first-jet checks, including 576 basis/gauge variants within that total, plus 360 finite-error/source-defect cases. Nine boundary scenarios exercise the valuation rule, and five malformed inputs are rejected. These counts are not counts of independent seed computations. The deterministic seed, complete totals, and boundary-case outputs are in `checks/RESULTS.json` and `checks/BOUNDARY_CASES.json`.

The tests include nonprimitive augmented kernel vectors, arbitrarily large finite specialization pairs, positive source defects, zero Bockstein first jets, insufficient derivative precision, and a deliberately omitted height-one `(p)` hypothesis. That last negative control demonstrates why residue arithmetic alone cannot certify the source theorem.

The executable always reports `actual_seed_primary_vanishing_certified: false`. It verifies arithmetic on supplied residues; it does not authenticate their origin. A new seed conclusion requires separately verified source and lattice custody.

## Endpoint disposition

| Obligation | Outcome of this return |
|---|---|
| A new seed primary component | None established |
| Cofinite primary vanishing | Corrected sufficient criterion derived; no cofinite premise proved |
| Exceptional primary finiteness | No change at 59, 487, 2243, 4547, 5843; any other eventual source exceptions remain |
| ORDER9 | Unchanged |
| Q36 | Unchanged |
| Remote repository state | Neither repository modified or pushed |
| Verification grade | Written derivation and executed exact algebra checks; no formal or external review |

The concrete deliverable is the strengthened certificate and its proof—not another request to rerun the same source survey. Its arithmetic premise remains open.

## Package contents

`PROOF.md` contains the full derivation. `refined_certificate.py` is the finite-precision valuation checker. `checks/` contains exact controls and results. `SOURCES.md` and `INPUT_BINDINGS.json` pin the inspected evidence. `HANDOFF.md` gives the narrow remaining review interface. `CURRENT_STATE_ADDITION.md` is an additive navigation note, not an automatic status promotion. `MANIFEST.sha256` binds the delivered files.
