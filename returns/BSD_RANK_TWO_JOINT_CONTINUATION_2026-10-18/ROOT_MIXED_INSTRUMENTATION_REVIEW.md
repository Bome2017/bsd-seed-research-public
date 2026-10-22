# Independent review of the mixed candidate export

Date: 2026-10-18
Verdict: PASS_MIXED_CANDIDATE_EXPORT_BOUNDARY. Separate from, and additive to, ROOT_INSTRUMENTATION_REVIEW.md. No captured element is certified as a unit by this source audit.

The additional code operates on the exact matrix `ideal=I*u`, where I is the integral ideal supplied by PARI and u is an integer LLL transformation. Its numerical metric affects which basis is chosen, but the stored columns are exact integral-basis coordinates. Every candidate is a literal sum or difference of two such columns. There is no division by two, projection to an eigenspace, change of integral lattice, or implicit extraction of a seventh root.

The original caller can supply a prime ideal or an integral ideal product. Accordingly the precise phrase is “a reduced integral ideal,” rather than “a reduced prime ideal.” This distinction does not invalidate candidate generation or its later ideal authentication.

The supplied scalar matrix was constructed in `unit_export.gp` by applying the retained actual scalar automorphism to every integral-basis vector. The mixed wrapper uses its cube as the central involution. Before each candidate loop, literal equality of the current `NF.zk` with the input basis is required. Therefore the code does not silently apply a matrix in a different integral basis. The central test only rejects additive eigenvectors with eigenvalue +1 or -1. Passing it does NOT prove nontrivial faithful multiplicative projection, nontrivial unit class, or any rejection rank.

The numerical `factorgen` routine is only a search filter. In particular its rounded norm must not be treated as an authenticated complete divisor. Each exported polynomial must still be reconstructed and fully factored in unmodified GP; proposed unit products need exact cancellation in the complete divisor matrix. This retains the same independent acceptance boundary as the first instrumentation review.

The bounds are exact but must be described accurately. Each invocation tests at most128 candidates that pass the mixed-parity filter. At degree48 the raw pair/sign loop has at most696 possibilities before that cap. There is no fixed GLOBAL bound of128 candidates: successive ideals may contribute more. The global limits are64 exported candidates, the117-second GP alarm, and the external time/RSS controller. The inserted early return makes this an intentionally incomplete source-only pass. It must not be reported as a completed class-group computation.

I reconstructed the entire modified C file from the bound original plus the builder's explicit inserted block and wrapper, without executing the builder. The result matches byte-for-byte. Modified source and compiled library match their recorded hashes. The additional wrapper takes two GEN arguments and matches GP's `GG` declaration; the existing PARI2.17.3 ABI, architecture, and library binding checks remain those of the first review. Fixed inputs and the integral scalar-basis producer are bound in ROOT_MIXED_INSTRUMENTATION_REVIEW.json.

No remote job, new harvest, build, or large arithmetic replay was run for this review. Changing the search geometry can expose candidates omitted by the previous search, but no mathematical claim about the full source follows until actual accepted elements and image ranks are calculated. Mutable harvest output is intentionally outside this fixed-source audit.
