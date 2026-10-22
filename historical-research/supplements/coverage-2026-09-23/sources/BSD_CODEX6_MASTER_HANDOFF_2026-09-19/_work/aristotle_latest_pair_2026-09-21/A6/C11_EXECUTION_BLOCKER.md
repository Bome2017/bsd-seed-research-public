# `C₁₁` — execution blocker report

**Return of this run: no value of `C₁₁`.** It was not computed, and no feasibility or
infeasibility claim is made about computing it. This file reports the execution blocker, as
instructed, rather than substituting other work for the requested certificate.

The task was: *produce the actual arithmetic certificate — determine*

```
C₁₁ := [T²] L₁₁(E, T)  (mod 11),      E : y² = x³ − 22735x² + 106272484x,
                                       N = 2³ · 3 · 2243 · 4547² · 5843
```

*rigorously, using the existing certified machinery or an exact derivation.*

---

## 1. The blocker

The material supplied with this project is the archive `ARISTOTLE_BSD_INVENTION_2026-09-20.tar.gz`.
It contains **24 files**, all prose records plus `MANIFEST.sha256` and `STATE.json`, and its own
manifest lists exactly those 24. Every load-bearing computational artifact cited by
`record/P7_PRIMARY_THEOREM.md` §4 is referenced by a relative link that points *outside* the
archive, and none of them is present:

| cited artifact | what it supplies | present? |
|---|---|---|
| `_work/active_full_bsd/p7/DOWNSTREAM.json` | certified plus-symbol tables at denominators 49 and 7, and the exact downstream calculation | no |
| `_work/active_full_bsd/p7/CERTIFICATE_BINDINGS.json` | coefficient, witness, source/binary and work-unit bindings | no |
| `_work/active_full_bsd/p7/run/msl_m49.txt`, `msl_m7.txt`, `P3_CHECK.txt` | engine output and exact cross-check | no |
| `_work/active_full_bsd/p7/downstream.py`, `seal.py`, `continue.sh` | downstream code, custody checker, restartable command | no |
| the 885 sealed coefficient segments and their verifier records | the verified `a_p` stream | no |
| the Arb-based modular-symbol engine itself (`p3plan/run_p3.sh` and the rigorous stream core) | the truncation-bounded evaluation, its normalisation, and its trust base | no |

Consequence, stated plainly: **“determine `C₁₁` using the existing certified machinery” is not
executable here**, because the machinery, its inputs and its custody chain are not in the handoff.
Anything I produced instead would be a *new* engine with a different trust base, a
separately-derived normalisation, and no binding to the sealed coefficients that the retained
7-primary theorem rests on. That is the project the redirection rules out, and I have not built it.

## 2. Minimal handoff that would unblock the computation

1. The engine and its build (with the recorded Arb/FLINT/GMP/MPFR and compiler versions), plus the
   restartable command.
2. The sealed coefficient segments and their verifier and manifests — **extended to the bound the
   denominator-121 evaluation needs**; the bound used for the denominator-49 run does not cover it,
   so new segments have to be produced and sealed under the same policy.
3. `DOWNSTREAM.json`. It is not optional context: reproducing the three retained sums
   `−165, −512, 314` at denominator 49 is the only available end-to-end check that a run has the
   same normalisation, sign and folding conventions as the retained 7-primary computation.
4. The written normalisation and error analysis the engine implements: which period, how the Manin
   constant is handled, the `ω₁` versus Néron/full-real-period convention, and the truncation bound
   with its constants. Test curves can validate an implementation; they cannot supply this.
5. The custody/seal policy, so that the output of the run is a certificate in the same sense as the
   `p = 7` one rather than an unbound number.

With (1)–(5) in hand the run is the existing pipeline pointed at denominator 121 and level 11, and
the derived 45-symbol expression you already hold is what consumes its output.

## 3. Correction I owe you

Earlier in this run I asserted that there is **“no shortcut”** to `C₁₁` short of reconstructing all
45 plus-symbols. That assertion was unsupported and I withdraw it.

`C₁₁` is a *single* `𝔽₁₁`-linear functional of the symbols. Reconstructing the 45 symbols
separately is sufficient, not necessary. Two consequences worth recording, both structural and
neither a proposed method:

* Lifting the mod-11 coefficients to fixed integers turns the target into one integer-weighted
  combination of the symbols. Since the individual symbols lie in a fixed lattice (a power-of-two
  denominator in the retained set-up), so does that combination; an evaluation may therefore
  identify **one** lattice point instead of 45. Whether that reduces total cost depends on how the
  engine is organised — the Fourier-coefficient stream is shared either way — but the identification
  burden is not 45-fold.
* Exact routes that never evaluate individual symbols at all are not excluded by anything I have
  shown.

## 4. What I deliberately did not do

* I did not re-derive the 45-symbol reduction formula, the local inputs at 11 (`a₁₁ = −2`, good
  ordinary reduction, unit Euler factor, the multiplier 28), or the vanishing of the level-one term.
  You have already derived and cross-checked that layer; re-deriving it would duplicate the
  preparation rather than supply the missing quantity.
* I did not build a coefficient or modular-symbol engine, install numerical dependencies, or
  calibrate conventions empirically on test curves.
* I offer no runtime extrapolation. A partial timing measurement of one stage is not a benchmark of
  the pipeline and would establish neither feasibility nor infeasibility; none is reported here.

## 5. State of the project after this run

The Lean development is unchanged: the nine modules under `RequestProject/` are exactly as they
were, and the Properties table is unchanged. No new claim is asserted and no status is upgraded.

`C₁₁` remains uncomputed. The 11-primary test remains what it was before this run: a sufficient
test whose one arithmetic input does not yet exist, and which in either outcome supplies neither the
infinite-tail theorem nor the real regulator comparison.
