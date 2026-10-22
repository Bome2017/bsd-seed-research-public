# Integration verification — 24 September 2026

This transfer was prepared in an isolated research worktree from `2a726213a27a12f10fece5bc70137e65e30911ba`, using the lab result pinned to `b358f7507759dad4a1e016c519d6f486ffca37e1`. All copied source bytes are recorded in `PROVENANCE.json`. No large computation, new Lean build or seed numerator evaluation was run.

| Check | Result |
|---|---|
| Original `tools/verify_release.py` | **18/18 passed**, including retained coefficient-table, lattice and D5 exact replays |
| Updated `tools/verify_patch_release.py` | **PATCH_RECHECK_PASS**; old README/checker bindings follow two explicit history redirects, all other checks preserved |
| Original v0.2.2 manifest | **4,226 entries preserved**, with README and checker kept in history; unchanged manuscript/PDF, 76-claim index, evidence and Lean source |
| Copied source custody | **31 files** match source hashes; lab-derived files also match their pinned Git blob identities |
| Supplied Pro review | **10/10 original manifest entries** match |
| Exact finite replay | **262 Eichler Gauss cases**, including 96 dyadic; wrong phase and amplitude controls both rejected |
| Cusp and integer arithmetic | **13 cusp inequalities**, both denominator integers, exact radius fractions and **9 degree-zero relift cases** pass |
| Independent interval oracle | **41,925 cases** agree with direct integer enumeration; **8 inadmissible primes** rejected; fallback-scale and exact-boundary controls pass |
| Claim dependency check | **NK.1–NK.3** reference known retained claims or earlier supplement claims; no new Lean or human-review grade |
| PDF | **5 pages**, built with installed TeX Live 2025 / latexmk 4.86a; no unresolved references or overfull boxes; all pages visually inspected |

The PDF has one harmless underfull bibliography line. Its mathematical constants, theorem labels, qualifications and exact acceptance inequalities are visible in the rendered copy. The original paper PDF was not rebuilt or replaced.

The new `verify.py` repeats the portable integrity, dependency and exact-arithmetic checks from a fresh checkout using only the standard library. Run it without `-O`, because the retained exact checker uses assertions. The current manifests bind the final artifacts; historical build and audit reports are evidence at their own stated scope.

These checks establish packaging integrity and finite algebra. They do not independently reprove Kim–Ota, ARS, CNS, the retained Manin bound, or the general division-place Gauss formula. The original numerical period comparisons remain numerical evidence only. No new claim about FIN, ORDER9, Q36 or a settled primary component is made.
