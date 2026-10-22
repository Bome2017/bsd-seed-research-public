# Exact Sha coverage — session verdict

**NO_INDEPENDENT_SHA_COMPRESSION_FOUND**

Stage 1 did not produce an independent compression theorem for
\[
E:y^2=x^3-22735x^2+106272484x.
\]
The session stops under the user's hard-stop rule. No new primary
component has been proved zero, and neither finiteness nor order nine
has been established.

The decisive gap is in the ordinary regime. The strongest applicable
nonvanishing result checked gives a unit Kurihara number at some
auxiliary conductor for each ordinary prime. It does not constrain that
conductor to the two-prime level needed by the retained rank-two
vanishing mechanism. The existing ordinary converse already identifies
depth zero with the desired primary Sha vanishing. Requiring depth zero
uniformly therefore supplies no independent compression. See the
[source and implication audit](/Users/bsm/BSD_CODEX6_EXACT_SHA_COVERAGE_2026-09-19/COMPRESSION_THEOREM.md).

The supersingular criterion remains conditional on a separate successful
coefficient test at each prime. No theorem covering the entire
supersingular regime was obtained. The bad primes were classified from
the discriminant, but this does not prove that Sha is supported there.

| Required output of Stage 1 | Result |
|---|---|
| An actual cutoff with a vanishing theorem beyond it | Not obtained |
| Exhaustive regimes with uniform arithmetic conclusions | Not obtained |
| A proved nonzero arithmetic support bound | Not obtained |
| Another independent finite/uniform reduction | Not obtained |

Stages 2–4 were not entered. No exceptional-prime computations, new
formalization runs, period constructions, or FORMULA work were performed.
A1 and the newly available A2 successor freezes were imported only for
their conditional algebra; their manifests were checked, not their Lean
builds rerun.

This is a bounded negative research result. It is not a theorem that no
such compression exists, nor a claim that the literature has been
exhaustively searched. No new no-go theorem is claimed. Even granting all
three stipulated primary imports without qualification, Stage 1 still
fails. Their existing provenance qualifications remain recorded in
[EXACT_ENDPOINT.md](/Users/bsm/BSD_CODEX6_EXACT_SHA_COVERAGE_2026-09-19/EXACT_ENDPOINT.md).

The bundle is sealed by [MANIFEST.sha256](/Users/bsm/BSD_CODEX6_EXACT_SHA_COVERAGE_2026-09-19/MANIFEST.sha256).
