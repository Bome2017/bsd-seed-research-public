# What the memory failure does and does not establish

The measured facts distinguish mathematical possibility, software limits,
and hardware.

The host has 16 GiB physical RAM. The earlier failure message named PARI's
allocated 2,000,000,000-byte arithmetic stack, not exhaustion of all host RAM.
A new 512,000,000-byte diagnostic actually used about 534 MB resident memory.
It failed while preparing the required prime-ideal table, before relation
collection. A source-level allocation profile shows essentially all growth
is retained decomposition data: 486,146,064 bytes by rational prime 287117,
with the required final bound 419775. The tested extra stack compaction
recovered zero bytes. Our initial temporary-allocation hypothesis is rejected.

A smaller relation factor base is a genuinely changed computation. It leaves
the larger prime-generation and honesty checks intact. The changed gates use
the unmodified runtime with documented parameters and source-checked branch
behavior, rather than claiming the experimental C patch solved the problem.

No memory overflow proves that the mathematical bound cannot be established.
Conversely, producing a provisional class table does not prove completeness;
class certification and actual incidence/connecting maps remain necessary.
A single-prime success also cannot establish a bound across all primes.

The changed unmodified run subsequently completed the factor base and entered
relation collection at a peak resident set of 732,577,792 bytes. Its random
relation-search variant used 734,720,000 bytes. Both stopped at their time
alarms without a class/unit output. The observed initial memory obstacle is
therefore avoidable on the existing machine; completing the arithmetic is
still unresolved.

The final intermediate-base random search used 933,396,480 bytes at peak
and ended after 177.13 seconds at its alarm, still in its first random
search call. No additional columns beyond its 24 initialized principal
relations were printed. It returned no BNF or unit/class data.

An exact streaming count, without storing the ideals or launching BNF,
reproduced the changed producer's 721 ideals and 175 rational-prime entries.
It counted 35,749 ideals in the default relation base. The pinned source
allocates a square machine-word cache of that dimension. In this 64-bit
runtime, its entries alone require

    8 * 35749^2 = 10,223,928,008 bytes = approximately 9.52 GiB.

That one array cannot fit in the old 2 GB arithmetic stack. It is a lower
bound on a particular implementation, not on the mathematical problem.
With the changed c1=.02 setting the corresponding entries need 4,158,728
bytes; c1=.1 requires 63,664,328 bytes and c1=.2 requires 206,207,432 bytes.
The full larger prime-ideal check is retained in each configuration.

A machine with more memory could give the default algorithm more room, but
these data do not determine the total memory or running time needed for a
finished, certified result. They do not justify buying a particular machine.
The current machine already passes the initial stage with changed settings.

At larger coefficient primes the point-field degree is p^2-1: 24 at five,
48 at seven, and 288 at seventeen. The entire anti-unit rank is
(p^2-1)/4, while one needed scalar character has rank (p+1)/2. Those are
exact structural counts, not a RAM extrapolation. Computing an unbounded
sequence of larger fields would not by itself prove the cofinite FIN bound.
