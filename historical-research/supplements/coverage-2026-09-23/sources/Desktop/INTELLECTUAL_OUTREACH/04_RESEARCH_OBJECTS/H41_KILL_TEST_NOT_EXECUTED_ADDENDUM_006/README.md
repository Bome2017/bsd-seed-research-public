# H41_KILL_TEST_NOT_EXECUTED_ADDENDUM_006

The `N = 16382` kill test fixed in `H41_ETA_CONGRUENCE_ADDENDUM_005` §7 **could not be executed**.

    a at N = 16382       UNDETERMINED
    kill condition       neither met nor failed — untested
    (C)                  not supported and not refuted by this attempt

The wall is `msinit` at genus 2047, not `ellmoddegree`: the modular-symbol space at level 16382 does not
construct on this machine. Sage, Magma, or more memory would be needed.

Recorded against me: one attempt requested a 24 GB PARI stack on a 16 GB host, which could never
succeed and made the failure silent instead of diagnosable, and drove free memory to about 15 MB before
I stopped the jobs.

    ADDENDUM.md    the outcome, judged under the pre-fixed kill condition
    computation/   the GP scripts of all four attempts
    receipts/      OUTCOME.txt, and the log of the attempt that died silently

Unchanged: one forced case at `N = 62`, one genuine test at `N = 254`, the uniform congruence (B).
**The H41 seed remains unproved.**
