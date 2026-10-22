# Scope and additive supersession

This supplement transfers the source-reviewed Néron normalization and denominator result from lab commit `b358f7507759dad4a1e016c519d6f486ffca37e1`. The three claims in `CLAIMS.json`, and only those claims, enter the research supplement index. The frozen v0.2.2 paper and its 76 claims are unchanged. Old statements about unavailable reconstruction reflect their dated state and are superseded here only for this normalized degree-zero kernel.

The source reports are copied byte-for-byte. The following clarifications govern their use:

1. **Sufficient multiplier, not optimality.** Phase 2's table headed “smallest t with p^t omega_G regular” establishes the smallest integer justified by its displayed lower bound. It does not prove that the actual forms need that multiplier. In particular, sharpness of exponent one at 4547 is untested.
2. **Integrality at infinity versus other cusps.** Phase 2 Lemma N1 proves cuspidality at every cusp and integral coefficients at infinity. Its heading must not be read as integral coefficients at every cusp; N2 explicitly allows negative valuations there.
3. **Degree-zero input.** Balanced lifts of the mod-p weights need not have integer degree zero. The lift and anchor correction in the addendum are part of an actual future certificate. The sharper lattice applies to the final cuspidal packet, not an arbitrary anchor diagonal.
4. **Exact acceptance.** Decimal radius displays are approximate. Use strictly less than `1/9312256` (or the stated fallback `1/1191968768`) after propagating every error. A scaled interval containing no integer is inconsistent with lattice membership and is rejected.
5. **Review scope.** The local Claude audit does not cover Phase 1. Kim–Ota's nonordinary extension, the chosen-map Manin bound and the division-place Gauss identity retain their stated import/written grades. Reusing an exact checker is a replay, not a second independent derivation of its parent theorems.
6. **Analytic gap is route-specific.** An affordable certified evaluation is still missing for this route. Full BSD additionally needs an all-prime arithmetic conclusion and the exact real leading term. No uniformity, new primary component or theorem novelty is claimed.

## Custody

`PROVENANCE.json` binds 31 copied files to Git blobs, the supplied review archive, or named local audit records. Context files are included so the normalization and Poisson inputs are inspectable; their remaining exploratory claims and historical task instructions do not become current instructions or research results.

The original Codex `acceptance_crosscheck.py` retains its original relative input path as historical evidence. The portable integration verifier supplies the correct packaged path and runs an independent direct-integer oracle against the retained Pro acceptance routine. Neither original script is silently changed.

The navigation update preserves the old README, old patch verifier and old root manifest under `review/history/v0.2.2/`. An explicit transition record redirects only the old README and patch-verifier bindings to those exact historical bytes; all other legacy checks are unchanged. The new root manifest binds the current supplement and navigation. This is a new additive review snapshot, not a retagging of v0.2.2.
