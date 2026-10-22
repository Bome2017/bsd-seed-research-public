# COLLISION_CHECK

| Atlas card / record item | Applies? | Relation to this run |
| --- | --- | --- |
| E12a-158 / unit 16479 "Heegner/Gross–Zagier: base point torsion; derived Kolyvagin classes give fixed-prime criteria; no cross-prime index" (ROUTE_BLOCKED) | Directly | This run attacks exactly the stated blocker. New: supersingular inert `ℓ` make one derived point serve every `p ∣ ℓ + 1` (Lemmas 1–3). The blocker is narrowed, not removed: `ι(ℓ)` is uncontrolled. |
| Kim arXiv:2609.15328 (record unit 52721): derived-Heegner divisibility ⇔ finiteness at fixed `p` | Yes | Lemma 3 is the `ν = 1` direction of the same family. It is not claimed as new. The new element is the simultaneous use over all `p ∣ ℓ + 1`. |
| W02 (witness existence vs. first nonzero length) | Yes | The analogous gap here is whether `ν = 1` occurs. Lemma 3 needs `ν = 1`. No length bound is proved. |
| W03 (singleton classes and localization) | Partly | The Heegner `ν = 1` class over `K` needs no localization hypothesis, because `c(1) = y_K = 0` and the sign flips to the `E(ℚ)` eigenspace. This is consistent with W03; it does not remove its gap. |
| W05/W06 (uncontrolled scalars `w_p`, `C_p`) | Risk | The proposed `A(ℓ)` must not be `#Sha`-weighted. This is recorded as an explicit requirement in `HANDOFF.md`. |
| W04 (elliptic Wieferich, finite samples) | Analogy | The supersingular coverage data (§5) are finite samples only. No density or progression theorem is claimed. |
| A3 "first-derivative formulas 0 = 0 at order ≥ 2" | Yes | Prop. 4 is a sharper, proved version for the derived points. The height route is not merely degenerate but provably blind to `p`-divisibility, for every `p ∣ ℓ + 1`. |
| H5–H9 generalized Kato classes / diagonal cycles | No | Not used. |
| BFR (accepted) | No direct use | BFR concerns the receiver `B_p`. This run changes method, as the task permits. A future bound from `ι(ℓ)` would apply at good `p ∤ 23N`, not at 2243, 4547 or 5843. |

**Genuinely new arithmetic input:** the exact identity `(σ − 1)D_ℓ y_ℓ = (ℓ + 1)y_ℓ` at
`a_ℓ = 0`, valid for all moduli at once, combined with simultaneous Kolyvagin primes. A
search of the compendium for supersingular auxiliary primes in Kolyvagin/Heegner context
found no prior use (`grep` of `FULL_COMPENDIUM.md`). This internal search is not a
literature-novelty claim; the identity itself is classical.
