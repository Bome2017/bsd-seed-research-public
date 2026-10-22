# Actual seed field: measured memory repair and relation search

The default PARI calculation's memory problem has been diagnosed and a
documented parameter change gets past it. Three bounded changed producers
did not supply new relation columns, a complete class group, or a unit
system. This producer is stopped. FIN, ORDER9 and Q36 are unchanged.

## Arithmetic input and fixed completeness condition

The input is the previously verified degree-24 field of a nonzero
five-torsion point on the actual seed. Its maximal-order `nf` object,
polynomial, and rational mappings remain in the sealed seed-five lane.
No known Sha certificate is an input to these calculations.

PARI 2.17.3 requires the checked GRH generation bound C2=419775 for this
field. Every changed run retains that bound and the later `be_honest`
phase. A reduced relation base changes which prime ideals are used for
finding relations; it does not silently declare the smaller base complete.
An eventual BNF table remains GRH-conditional until `bnfcertify` succeeds.

## What the measurements establish

The original 512MB gate overflowed while storing prime decompositions,
before relation collection. Instrumenting the local stack showed that the
proposed extra garbage-collection call reclaimed exactly zero bytes at
every sample: the prime-decomposition routine already returns compact
objects. The temporary-allocation hypothesis is withdrawn. The isolated
patch passed arithmetic smoke controls but provides no memory repair.

The accepted streaming count used 19,525,632 peak resident bytes and
2.78 seconds. It counted every rational prime through C2, using the actual
maximal order at index primes, and exactly reproduced the running
producer's smaller-base dimensions KC=721 and KCZ=175.

For default parameters it gives KC=35749. The source's explicit allocation
`zero_Flm_copy(KC,KC)` therefore needs **10,223,928,008 bytes (about 9.52 GiB)
for matrix entries alone**. Required prime decompositions, matrix headers,
relations, precision data and later algorithms add further memory. This
explains why merely retrying the default configuration with a 2GB stack
could not work. It is not a calculation of the total RAM needed to finish.

For c1=0.02 the dense entries need only 4,158,728 bytes. The unmodified
producer completed its full factor-base phase in 13.47 seconds and used
732,577,792 peak resident bytes over its bounded run. Thus the observed
phase does not require a larger computer. Completion time and later peak
memory remain unmeasured.

## Changed producers

The first unmodified small-base gate retained default small-norm searching.
It reached HNF dimensions 721 by 11, then repeated small-norm searches
without adding columns before its 117-second alarm.

The documented `nrpid=-1` change then used random relations instead.
This second gate ended at its 177-second alarm, with peak resident memory
734,720,000 bytes. The log remained at the initial eleven relation columns,
and requested the same 728 relations after each completed search pass.
No BNF completion marker, class table, or seed unit system was produced.

Those initial columns are initialized principal-ideal relations. Their
presence alone is not a computed unit system or completeness certificate.
No independent-rank increase is inferred from mere search activity.

The final authorized balanced-base gate used c1=0.2, hence KC=5077,
KCZ=1199 and 206,207,432 dense-cache entry bytes. It accepted more possible
smooth ideal factorizations while preserving C2=419775. It completed
factor-base construction in 13.44 seconds, initialized 24 principal-ideal
relation columns, and entered its first random search. No further column
was printed before the 177-second alarm. Peak resident memory was
933,396,480 bytes. There was no stack overflow and no BNF output.

| Producer | Relation bound C1 | Initial columns | Further columns observed | Peak RSS bytes | Stop |
|---|---:|---:|---:|---:|---|
| small norm, c1=0.02 | 4813 | 11 | 0 | 732,577,792 | 117-second alarm |
| random, c1=0.02 | 4813 | 11 | 0 | 734,720,000 | 177-second alarm |
| random, c1=0.2 | 48136 | 24 | 0 | 933,396,480 | 177-second alarm |

There is no evidence of an independent relation-rank increase in these
windows. The balanced run did not finish its first random-search pass;
the bounded observation does not prove that a longer or genuinely
different producer could never succeed. No unchanged extension is made.

## Evidence and limits

`SOURCE_BINDING.json` binds the source to the official PARI 2.17.3 archive.
The installed library is unchanged. The final producer loads no custom
library. Direct stdout/stderr files survive interruption, and the external
wall gate kills the entire new process group if necessary. The marker and
error checks reject PARI's exit-code-zero alarm returns.

The first diagnostic receipt was reconstructed from its unchanged saved
logs after a malformed postprocessing regular expression stalled the
Python wrapper. It explicitly retains an unknown process exit code; it is
not counted as a completed arithmetic result. The corrected direct-log
runner is used for the later gates.

The useful computational change is removal of a measured avoidable
memory bottleneck. It does not supply the missing unit norm rank, complete
class contribution, or a seed upper bound. No finite resource failure here
is a theorem that the arithmetic cannot be computed.
