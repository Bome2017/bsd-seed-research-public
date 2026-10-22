# Uniform finite support: synthesis and source update

Date: 2026-09-30.

**Verdicts:** `SOURCE_UPDATE_APPLIES_AT_RETAINED_INPUT_GRADE`; `ALL_GOOD_PRIME_KURIHARA_EXISTENCE`; `UNIFORM_LOW_DEPTH_BOUND_STILL_OPEN`.

There is one concrete reason to reopen a previously blocked part of the program. A newer author-hosted Castella–Liu–Wan theorem removes the squarefree-level restriction that excluded this seed at supersingular primes. Its replacement hypothesis holds at the seed's multiplicative prime 2243. Combined with Castella–Sano, it gives some mod-p unit Kurihara witness at every good p>=5, ordinary or supersingular, at the imported-theorem and retained-seed-input grades.

It does not put those witnesses at length two. No argument finishing finite support was found in this pass.

## What was checked

I read the catch-up brief, the uniform-step reduction sheet with its latest admission repairs, the prior A1 nonvanishing screen and its closest sources, the ordinary-converse gate, the A3/A4 and U22 stop records, the BH audit, and relevant retained seed inputs. I compared primary statements in Kriz–Nordentoft, Castella–Sano, Kim, Bullach–Honnor, and both versions of Castella–Liu–Wan. I also screened adjacent horizontal-moment and Selmer-distribution results for the exact required implication.

This is a targeted synthesis, not an end-to-end re-audit of all certificates, all correspondence, or the entire mathematics literature. Route K and the prime certificates retain their existing grades. The selected local records read are hash-bound in `LOCAL_BINDINGS.json`; the external sources and exact anchors are in `SOURCE_REGISTER.md`.

## 1. A real source change

The old arXiv CLW Theorem A required squarefree N. The author-hosted version dated September 21 instead permits weight two with a prime q||N where the residual representation is ramified. For this curve, q=2243 works for every good p>=5: v_2243(Delta)=1. Supersingularity gives a_p=0, hence p-regularity; the other hypotheses are the retained modularity and large-image inputs.

I checked the cyclotomic-character shift and determinant normalization before invoking Castella–Sano. In particular, CLW's omega component at weight two becomes the trivial component for T_pE; their integral Kato element uses the quotient-lattice generators, not the generators multiplied by the congruence ideal.

See `NEW_INPUT_APPLICATION.md` for the deduction. It updates the precise watch item in `V025_CANDIDATE_EDITS_2026-09-29.md` section 6. It supplies all-good-prime existence, not nonvanishing at the required small depth. No deep imported theorem has been reproved here.

## 2. The remaining problem is a sharp upper bound

Define r_p to be the minimum number of Kato auxiliary primes needed for a Kurihara quantity that is nonzero modulo p. Combining the new application with Kim's higher-Fitting theorem gives

    r_p = dim_Fp Sel_p(E/Q),
    r_p is finite and even,
    r_p >= 2,
    r_p = 2 iff Sha(E/Q)[p^infinity]=0.

Thus the desired theorem can be written

    r_p < 4 for every p outside one finite set.

This is a useful exact specification, not a proof of the inequality. A rank-two free module with an extra (Z/p)^2 already has r_p=4 while satisfying eventual unit-witness existence. That countermodel pinpoints why the new main-conjecture input alone does not finish FIN.

Kriz–Nordentoft propagates a length-r unit witness into character values with depth bounded in terms of r. It does not independently bound r. Constants allowed to depend on p in the asymptotic character count are not the main issue; the conductor cutoff is allowed to depend on p. The missing input is the low-depth estimate.

## 3. The analytic target can be broader than a singleton

The retained BH Fitting argument, combined with the even Selmer dimension above, gives a sufficient test:

    For a real cyclic degree-p field K/Q of conductor prime to pN,
    a faithful value of the full normalized theta_K of lambda-depth <4
    implies Sha(E/Q)[p^infinity]=0.

Here lambda=zeta_p-1. A squarefree composite conductor is allowed. One need not find a G2 singleton, recover 288, use a common auxiliary field, or solve Q36 first. The proof and normalization boundary are in `DEPTH_TARGET.md`.

This broadens what would count as success. It is not evidence that low-depth values must exist, and it does not justify substituting complex nonvanishing or an untracked L-value normalization.

## 4. Which work should reopen

| Part | Decision | Reason |
|---|---|---|
| Supersingular main-conjecture/Kurihara coverage | Reopen narrowly for review and adoption of this application | A new source version changes its actual first failing hypothesis |
| Uniform low-depth nonvanishing | Remains the main target | No independent upper bound was found |
| U22 gluing, primitivity, Hecke engine | Keep paused | The missing upper/exact relation remains; CLW does not supply it |
| Exact 288 / LINE / rationality | Keep as alternative targets, not mandatory admission gates | A direct depth bound would bypass them |
| Prime ladder and expensive bad-prime computations | Keep frozen for this objective | They do not supply the uniform implication |
| Adjacent Selmer statistics | No applicable transfer found | Varying twists or extension Selmer structures need not bound the base curve's Selmer group |

No route is rejected merely because it is formulated one prime at a time: one theorem applicable to every good p, as above, is a legitimate uniform argument. Conversely, an average over varying curves or extensions does not automatically say anything sufficient about this fixed curve at all p.

## 5. The next plan, with no invented proof step

1. Give Pro the new application and depth deduction for an independent check, concentrating on the source version, the canonical lattice/character dictionary, and Kim's Fitting indices. This is a small, concrete task, not another general BSD search.
2. If it passes, update the governing state to “some unit Kurihara witness exists at every good p; minimum length remains uncontrolled.” Do not upgrade FIN or automatically identify historical E11 scalars without their normalization comparison.
3. Admit a further construction only if it supplies an explicit mechanism for the independent bound below four, or another upper bound that excludes excess Selmer classes. A computation of unknown horizontal mu/lambda invariants in terms of r_p does not qualify. Neither does assuming a two-prime unit witness to obtain one.

`NEXT_TASK.md` packages the exact review and the gate for a later construction. I do not currently have a concrete new inequality that passes that gate. This is a source-backed improvement to coverage and a more flexible endpoint test, not a promise that another model session can finish the theorem.

## 6. Corrections to the supplied overview

- The statement “no method exists for any rank-two curve” exceeds what our source search or Keller's reported knowledge establishes. No applicable finite-support theorem was located here.
- Rationality of q and a narrow real interval do not determine q=36: a denominator/height bound or another exact characterization is also needed.
- FIN plus zero results at five named primes does not establish ORDER9 unless the eventual uniform theorem covers every other prime. Its finite exceptional set must be derived, not fixed in advance from Theorem W.
- “Everything possible prime by prime has been proved” is too strong. The record contains criteria without computed witnesses, and other finite-prime statements could still be proved. They simply do not settle this target.
- Independent model readings are checks at their recorded grades, not a substitute for a human referee or formal verification of the entire arithmetic argument.

All writes were confined to this output folder and its companion archive. No source record, frozen artifact, repository, running job or memory file was changed. No push, message, paid computation or production prime run was made.

FIN, ORDER9 and Q36 are unchanged.
