# Review of the first isolated PARI stack-compaction patch

Status: FIRST_PATCH_ARITHMETIC_PRESERVATION_SUPPORTED; TEMPORARY_GARBAGE_HYPOTHESIS_DISPROVED_BY_PROFILE; SEED_MEMORY_REPAIR_NOT_ESTABLISHED.

I inspected the official PARI2.17.3 buch2.c, the exact diff, compile command, exported symbols, smoke program and its output, and the first changed seed receipt. This is source review plus a separate arithmetic replay, not formal C memory verification.

## Exact patch and stack lifetimes

The only algorithm-body change replaces the assignment of `idealprimedec_limit_f`'s result by the same call followed by `gerepilecopy` at a stack pointer captured immediately before that call. The persistent `nf`, `prim`, all factor-base arrays, and every previous `LP` object predate this pointer. The returned object is copied before the previous clone-bit marker and F.LV insertion. This is consistent with ordinary PARI stack compaction: it preserves the needed returned decomposition and discards temporary objects made during that call. No prime, decomposition or relation filter is changed.

The wrapper additionally requests c1=.02, c2=0, nrpid=4 and nf_FORCE. Inspection confirms that the full LIMC2 bound is still obtained through GRHchk, every relevant prime up to it still enters FBgen, and the unchanged be_honest check remains required before return. A successful BNF would remain provisional until independently certified; decreasing c1 is not permission to omit the honesty check.

The dynamic library contains additional public symbols from its copied translation unit. The separate original-runtime replay below avoids relying on symbol-binding claims: it does not load the library at all. Limiting exports to the wrapper alone would be a defensible packaging hardening, but no such change is asserted in this review.

## Independent arithmetic replay with the installed runtime alone

`unmodified_smoke_replay.gp` runs in a fresh GP2.17.3 process WITHOUT installing the patch library. It reads the patched run's saved degree8 BNF, recomputes the original BNF, and runs unmodified bnfcertify on both. Both pass. The class group is C6. Every supplied fundamental unit is reconstructed literally from the original unit basis and torsion generator, its principal ideal is the identity, and the change-of-basis determinant is ±1. The class-generator relation is also reconstructed as an exact principal ideal. The receipt has empty stderr and its pass marker. This validates the saved small test independently of the loaded patch library; it does not certify any seed result.

## The seed run did not pass

The changed seed run still overflowed the512MB stack after13.46seconds, before relation collection. It has no completion marker and was correctly rejected despite process exit0. No seed BNF, class bound or complete unit source follows.

A further diagnosis matters before proposing a second patch. In the full FBgen loop there are no other allocating operations before the captured pointer: it reads cached degree patterns, runs scalar arithmetic, and updates the existing integer `prim`. `cache_prime_dec` already copies each cached result to the heap and restores its stack pointer per iteration. Therefore merely moving this GC boundary to the top of that same loop is not an evidenced repair.

The remaining possibilities include the memory required by retained prime-decomposition objects up to LIMC2, or the peak work of one decomposition. The first changed run retained LIMC2=419775 despite C1=4813. Instrumenting returned-object sizes and the stack position is needed to distinguish those explanations. A lazy or compact representation of C2-only decompositions would be a materially different patch, requiring its own lifetime and completeness review. No such patch is approved by this document.

## Measurement result: the first memory hypothesis was wrong

The separately instrumented build retained exactly the first patch's arithmetic and compaction. I inspected its diff and independently parsed all 25 samples in `profile_seed.err`. Every sample reports zero discarded bytes. Every sample also has precisely 11,985,832 bytes of stack use beyond the retained prime-decomposition objects. At the last sample, prime 287117, retained objects occupy 486,146,064 of 498,131,896 bytes (97.59%). The run then overflows the 512,000,000-byte stack. This disproves the proposed explanation that accumulated removable temporary garbage in this loop causes this failure. The compaction patch did not repair it.

An independent integer sieve gives 35,373 rational primes through the unchanged full bound 419775. Extrapolating the observed 1,000-prime increments from the last sample gives approximately 677–725 MB, central estimate 698 MB, for the completed factor-base stack alone. This is an engineering estimate, not a proved memory bound: it does not cover exceptional decomposition peaks or later relation collection, matrices, unit recovery, honesty checks or certification. The exact measurements and method are saved in `RETAINED_OBJECT_PROFILE_REVIEW.json`.

The instrumentation's logical `gsizebyte` measure exceeds physical retained size because a recursive size can count shared components more than once. The physical `avp-avma` and full stack differences are the relevant measures. No test saw unsigned underflow in the discarded-byte counter; its observed value was exactly zero throughout.

## Admission of the unmodified public-API parameter experiment

The proposed next call is original GP `bnfinit(NF,1,[0.02,0,4])`, with no installed patch library. Official PARI 2.17.3 `bnfinit0` at source lines 3468–3493 maps these parameters to `Buchall_param(NF,0.02,0,4,nf_FORCE,prec)`. This is the same parameter choice as the initial wrapper, through the public API.

In the unchanged `Buchall_param` code, c2=0 starts the GRH bound search at 1 and continues the full `GRHchk` search. c1=.02 changes the initial smaller relation factor base; it does not replace the full tested ideal bound. All relevant primes through LIMC2 still enter `FBgen`. If the relation base is insufficient, `START` increases it. The `be_honest` call remains mandatory for the ideals outside the relation base before return. Therefore these parameters alter the search strategy without deleting the class-generation check. They do not by themselves remove the usual conditional completeness status of an uncertified BNF.

I support this as a bounded, unmodified-runtime experiment using the parent-approved 2 GB / 120 second cap. I do not assert it will finish. A returned BNF still requires original-runtime exact unit/ideal validation and independent `bnfcertify` or a separately justified primary-completeness certificate before it can supply the complete seed bound.
