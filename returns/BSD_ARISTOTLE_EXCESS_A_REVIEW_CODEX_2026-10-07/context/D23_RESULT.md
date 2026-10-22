# TWIST_D23_NONZERO_CERTIFIED

The local computation completed on 2026-09-21 and proves, with the declared retained coefficient/software trust base,

\[
\boxed{39.512236\le L'(E^{-23},1)\le40.182321.}
\]

The twist has root number -1, so its central value is zero and its analytic rank is exactly one. The retained Gross–Zagier–Kolyvagin theorem gives rank E^{-23}(Q)=1. Combining with the retained rank-two seed theorem gives

\[
\boxed{\operatorname{rank}E(\mathbf Q(\sqrt{-23}))=3.}
\]

This supplies the previously missing suitable rank-one twist premise of the existing Selmer-to-Sha comparison. It does not evaluate the Stark ideal. No new primary component of the seed, FIN, ORDER9 or Q36 is proved.

## Numerical certificate

At T=3,456,106,495, the finite sum has the conservative printed enclosure

\[
2S_T=39.847278312318874\ \pm\ 4.28\cdot10^{-16}.
\]

That enclosure includes all finite Arb rounding and Taylor remainder contributions. The infinite tail is bounded by

\[
B_{-23}(T)\le0.335041797049.
\]

The engine adds the Arb upper bound before producing the outward-rounded rational final interval above. The original cutoff is therefore adequate; the seven-billion extension was unnecessary and was not executed.

All 1,030 atomic units passed self-hash and range checks. The exact coverage identity is

\[
1,132,735,953+2,323,370,542=3,456,106,495.
\]

The 206 consumed coefficient segments and verifier records were rehashed against the retained C11 bindings. The coefficient root is

    2cd379caf9b8ac9f96377281202180b4398a11eee8ce006f5287f9b1c73a44cb

Fresh deterministic recombination reproduced the output exactly. An independent Python sieve/prime-power calculation also reproduced the first segment's 1,433,093,153 large-prime pairs and 642,830,217 nonzero weighted terms. Kernel validation checked 5,609 values against direct higher-precision Arb. Seven short blocks, 448 terms total, agreed after the documented reference-harness integer-width repair; the failed pre-repair log is preserved.

The main run took 708.40 seconds with twelve workers and about 1.00 GB peak resident memory, reusing twelve completed benchmark units. The first large-prime segment dominated the elapsed time. These are measurements of this adapter and run, not a cost guarantee for another cutoff or host.

## Exact evidence and qualifications

* [Mathematical implication and scope](PROOF.md).
* [Derivative/kernel/traversal contract](DESIGN.md).
* [Full result with individual unit hashes](RESULT.json).
* [Completion review](COMPLETION_REVIEW.json).
* [Retained input bindings](INPUT_BINDINGS.json) and [current build identities](BUILD_BINDINGS.json).
* [Validation and actual benchmarks](VALIDATION_AND_BENCHMARK.json).
* [Original run output](run_T3456106495.log) and [fresh combination](combine_T3456106495.log).

The sealed engine and original corpus are unchanged. The new adapter is an isolated implementation using the retained table-free traversal and E1 Taylor machinery. This is a computer-assisted certificate with written error bounds and finite validation, not a Lean proof, fresh witness verification of the entire coefficient corpus, independent human review, or a second full numerical implementation.

K=Q(sqrt(-23)) also satisfies the recorded splitting requirements at p=13, which has good ordinary non-anomalous reduction. Thus the retained comparison specializes there with a known rank-three point contribution. The value of I3 remains uncomputed. No successor operation is launched.
