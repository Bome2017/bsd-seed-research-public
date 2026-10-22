# Oxford release and previously unchecked source delta

Date: October 11, 2026. Status: **NEW_RELEVANT_SOURCES_CHECKED; SUPERSINGULAR_HYPOTHESIS_SCREEN_PASSES; NO_NEW_SEED_BOUND.**

There is one confirmed new Oxford recording and several relevant sources that the searched project record either had not located or had listed only as unchecked titles. The strongest additions are an applicable supersingular Fitting theorem and a later local interpolation formula addressing an explicit gap in a previously overlooked theta-class thesis. Neither supplies the seed's missing nonvanishing or excess-content estimate.

This is a targeted primary-source read and application screen. It is not a proof audit of every cited paper, an exhaustive search of the computer, or independent certification of the retained seed inputs. FIN, ORDER9 and Q36 remain unchanged.

## 1. Actual new Oxford release

Clay posted **Wei Zhang, Arithmetic Diagonal Cycles and L-Functions**, on October 9, 2026. The talk was given September 23 during the Oxford Clay Research Conference, alongside the September 21–25 BSD workshop. The project's September 29 check had found no recording. [Official lecture and recording](https://www.claymath.org/lectures/arithmetic-diagonal-cycles-and-l-functions/).

The release date and recording are verified. A transcript was not recovered, so no new theorem inside the talk is claimed. The workshop schedule and thirteen abstracts were already read; they are not counted again. No new slide collection was found on the official pages inspected. [Release audit](notes/OXFORD_DELTA.md).

## 2. Strongest immediately applicable theorem: Shii's supersingular Fitting inclusion

Ryota Shii's *On the Mazur–Tate refined conjecture for the anticyclotomic tower at inert primes*, Theorem 1.2, places the product of a definite theta element and its involution in the Fitting ideal of the dual Selmer group over finite anticyclotomic layers. The old record listed this paper only as **titles only, UNCHECKED**. We have now read the theorem and its setup. [Primary source](https://arxiv.org/html/2503.09034v1).

For this seed and K=Q(sqrt(-7)), the hypothesis screen passes under the retained conductor and full residual-image inputs:

- N-minus = 3·2243·5843 has three distinct inert factors; N-plus = 2³·4547² has split factors.
- The class number is one and 7 does not divide N.
- The three inert multiplicative primes have minimal-discriminant valuations 2, 1, 2. Thus their residual inertia is nontrivial for every coefficient prime p>=5, stronger than the paper's required subset.

The resulting domain is **good supersingular p>=5, p!=7, inert in K**. This is an actual source-hypothesis application, not just a title match. It does not cover split supersingular primes or the entire cofinite domain. Its theta source and integral normalization must be matched before applying the inclusion to the project's detector. It supplies neither a unit coefficient nor the 288 identity.

[Detailed theorem and hypothesis table](notes/EXTERNAL_PREPRINTS.md) · [exact arithmetic receipt](checks/SHII_SEED_ARITHMETIC.json) · [independent arithmetic replay](checks/check_shii_seed.py).

## 3. A specific missing formula is now available

The public 2024 thesis **Crafting Euler Systems: Beyond the Motivic Mold**, by Marco Sangiovanni Vincentelli, constructs integral CM theta classes. The old watchlist awaited an in-preparation paper; this underlying thesis was not found in the searched reading record. It is older work newly located, not an Oxford release. [Thesis record](https://theses-dissertations.princeton.edu/items/5d68c4c6-d0f8-48a7-b34b-e98a7289652c).

Its page 29 explicitly leaves finite-character interpolation and period matching unfinished. Two later sources change that situation:

- **Sano–Venjakob, December 2024**, Corollary 2.6.5, gives finite-character interpolation for the Lubin–Tate regulator. [Paper](https://arxiv.org/abs/2412.12429).
- **Venjakob, 2026**, Theorem 1.3, extends the interpolation through an unramified variable. [Author's preprint](https://www.mathi.uni-heidelberg.de/~venjakob/papervenjakob/LT-maxabelian.pdf).

This makes the local comparison a specific calculation: match the thesis's signed local-resolvent period to the displayed period, Gauss-sum, Frobenius and uniformizer factors. No such identification has been proved in this return. The later papers' L-analytic hypotheses concern the appropriate CM component; they cannot automatically be applied to the full non-CM seed representation.

Even successful local matching would still require the global product/pushforward construction, seed projection, and arithmetic control of its value. The new contribution is an available formula at a named missing interface, not a completed seed comparison. [Exact source dictionary and remaining comparison](notes/LUBIN_TATE_DELTA.md).

## 4. Further relevant papers now checked beyond their titles

| Source | What is usable | What it does not supply |
| --- | --- | --- |
| [Abhishek–Ray–Karmakar, 2605.29783v2](https://arxiv.org/html/2605.29783v2) | Explicit signed theta-content and transition formulas, including inert supersingular primes | Control of the quadratic coefficient or lambda invariant across coefficient primes |
| [Loeffler–Zerbes, 2511.08793v2](https://arxiv.org/html/2511.08793v2), Theorem 6.15 | Nonordinary local-condition machinery and a Selmer-length bound in terms of the initial Euler-system class's divisibility | An upper bound on that divisibility; an identification of the initial class with our divided Kato derivative |
| [Pratap–Ray, 2511.21979v2](https://arxiv.org/html/2511.21979v2) | A finite-level Kida formula tracking local costs in abelian p-extensions, including additive reduction | The base nonvanishing/content estimate that the transition carries forward |

The first two were previously unchecked titles; no matching ID/title was found for the third in the searched record. The first two can support careful supersingular source comparisons. They should not be used to rename the same uncontrolled seed coefficient.

Disegni–Zhang's arithmetic Gan–Gross–Prasad preprint was also read at theorem level. It gives a normalization template for a first-derivative height formula with substantial field and ordinarity restrictions, not this seed's second-derivative identity. A K2 indivisibility paper was retained only as a technique reference. [Detailed source ledger](notes/EXTERNAL_PREPRINTS.md) · [Disegni–Zhang scope](notes/DISEGNI_ZHANG.md) · [separate model-agent interface review](notes/SHORTLIST_REVIEW.md).

## 5. Recommended continuation

Two source comparisons are now justified without repeating the old search:

1. **Apply Shii's exact theta/Fitting setup to the seed's source conventions.** Its explicit seed hypothesis screen is already finished. Compare theta elements and integral lattices, retaining signed local errors; do not start another prime-by-prime enumeration.
2. **Compare the thesis period to the later finite-character formulas.** A missing source formula is now on the page. Compute the whole normalization, including nonunit factors, before attempting a seed projection.

These are candidate inputs to the arithmetic route, not promises of an upper bound. The missing seed conclusion remains nonzero actual derivative with m_p-w_p<=1 cofinitely, or another independent uniform mechanism such as a matched tame identity. There is no reason to restrict every possible proof to a fixed integer, but no new uniform estimate has been obtained here.

## Reading and publication boundaries

- Baseline lab: 006c407c848e25eadfc7acc2c3a830196e7eed27. The prior construction repair and source screen remain intact.
- OpenAI math remains at fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb: no commit delta. One overlooked section-conjecture family was read but did not provide an admissible seed application. [Screen](notes/OPENAI_OVERLOOKED.md).
- Search evidence distinguishes no record match from title-only and theorem-level prior reading. None means every file on the host was inspected.
- Full downloaded papers, web snapshots and raw large search output are retained in a separate local source cache. The lab publishes authored notes, source URLs/hashes and small checks, not copies of the entire external literature.
- Hashes and the arithmetic replay establish custody and the stated numerical checks. They do not certify the imported theorems or establish FIN, ORDER9 or Q36.
