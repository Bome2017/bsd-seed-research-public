# A changed unit/class computation on the actual seed

2026-10-20. This return tests the actual seed, rather than adding another
control curve. The complete seed unit/class bound has **not** been
established. The finite-prime experiments here do not establish a bound
across coefficient primes.

The current complete-source requirement, on the retained valuation-zero
domain, is

\[
\dim K_\chi\le \frac{p+1}{2}-r_U(p)+k_C(p).
\]

Here \(r_U\) is arithmetic rank on the full faithful ordinary-unit
space. The term \(k_C\) retains the surviving ordinary class contribution
and its connecting obstruction. A sufficient upper bound of two from
this formula requires

\[
r_U(p)-k_C(p)\ge(p-3)/2.
\]

No known Sha value, provisional class table, or lower-field class number
has been substituted for either missing arithmetic term.

## 1. The memory failure was diagnosed rather than extrapolated

The host has 16 GiB of physical memory. The old error named PARI's
2,000,000,000-byte arithmetic stack. It was not a measurement showing
that all 16 GiB of host RAM had been exhausted.

A new 512 MB diagnostic identified the initial failing phase: construction
of the prime-ideal factor base through norm bound 419775. This precedes
the class-group relation search. A source-level profile found that, at
rational prime 287117, required retained decompositions occupied
486,146,064 bytes of 498,131,896 stack bytes.

Our first hypothesis was that temporary allocations accumulated in this
loop. It was tested and rejected: an isolated extra-compaction patch
discarded **zero bytes** in every recorded sample. Although the patch
passed a separate small-field arithmetic replay, it did not fix the
seed memory problem. That unsuccessful hypothesis is preserved in the
receipts rather than described as a software improvement.

The measured retained data suggested approximately 0.7 GB for the full
factor base, excluding later work. This engineering estimate motivated
a different, documented PARI strategy: reduce the relation factor base
while retaining the complete larger prime-ideal check.

An exact streaming count subsequently identified a separate large
allocation in the default strategy. Its relation base has 35,749
prime ideals. PARI's square cache for those ideals requires
**10,223,928,008 bytes in its entries alone**, before headers, the
prime-ideal table, relations or other working memory. This already
exceeds the old 2 GB stack. The smaller-base strategy reduces this
particular cache to about 4.2 MB without discarding the larger check.
The count independently reproduced the actual changed run's dimensions.

## 2. The changed actual-seed run passed the memory stage

The unmodified PARI 2.17.3 call

```
bnfinit(NF, 1, [0.02, 0, 4])
```

was run with a 2 GB arithmetic stack and a bounded wall time. No custom
library was loaded for this run. The full bound remained 419775; the
relation-base bound became 4813, with 721 prime ideals used for relations.
The remaining ideals were not dropped from PARI's completeness checks.

This run completed factor-base construction and entered relation
collection. Peak resident memory was **732,577,792 bytes**. Thus this
stage was executable on the existing machine without purchasing memory.

The run did not finish a BNF. It stopped at its alarm after approximately
117 seconds. Following eleven initial relation columns, repeated
small-norm searches took about 23–24 seconds each without resolving the
missing relation rank. There was no accepted class table or unit system.

A further changed gate disabled that unproductive small-norm phase and
used PARI's random-relation search. It stopped at its 177-second alarm
at 734,720,000 bytes peak resident memory, still with only the initial
eleven relation columns. It produced no BNF.

The streaming count also measured intermediate base sizes before a
final balanced-base test: c1=.2 has 5,077 relation ideals and requires
206,207,432 bytes for the square cache entries. This offers a larger
smoothness base without restoring the default ten-gigabyte cache.
Its final result is recorded in the resource report and receipts.
These are changed bounded algorithms, not a claim that extending the
same unsuccessful run must eventually finish.

The final balanced gate ended at its 177.13-second alarm with peak
resident memory **933,396,480 bytes** and no stack overflow. It remained
in its first random-relation search. The log contained only its 24
initialized principal-ideal relation columns; no additional column or
class/unit output appeared. This is a bounded unsuccessful search,
not proof that a longer or different relation algorithm cannot work.

| Actual seed strategy | Peak resident bytes | Completed arithmetic output |
|---|---:|---|
| Small relation base; small-norm search | 732,577,792 | Full factor base; no BNF |
| Small relation base; random search | 734,720,000 | Full factor base; no BNF |
| Intermediate relation base; random search | 933,396,480 | Full factor base; no BNF |

Thus the tested configurations operate below one GB through their
observed search stages. Their full completion and certification
requirements remain unknown.

Even a successfully returned BNF would initially be provisional. A
complete bound would still need the relevant class-generation
certification, authenticated unit projections, and incidence and
connecting maps. PARI explicitly distinguishes its provisional class
computations from unconditional certification in its
[number-field documentation](https://pari.math.u-bordeaux.fr/dochtml/html-stable/General_number_fields.html#bnfcertify).

## 3. The relative-field alternative was tested on the seed

The actual degree-24 five-torsion point field \(A\) was expressed in its
scalar tower:

\[
F=A^{C_4},\quad [F:\mathbf Q]=6,\qquad
A^+=A^{\{\pm1\}},\quad [A^+:\mathbf Q]=12.
\]

The exact equations, embeddings, scalar action and relative quadratic
equations are saved and replayed. Their signatures are respectively
\((2,2),(4,4),(4,10)\). Their free unit ranks are \(3,7,13\).
The genuine relative norm-one unit group for \(A/A^+\) has rank six;
the desired character occupies three of those directions.

A bounded degree-six class/unit attempt also overflowed its 256 MB
stack and supplied no arithmetic output. More importantly, examining
PARI's actual relative norm implementation showed that it internally
requires the absolute extension's BNF. Calling that routine would have
hidden, rather than avoided, the outstanding full-field computation.

The smaller fields also cannot supply the missing faithful class bound
by direct transfer. On five-primary ideal classes, extension and norm give

\[
\mathrm{Cl}(A)\{5\}
 =j\mathrm{Cl}(A^+)\{5\}\oplus R_5,\qquad
R_5=\ker N_{A/A^+}.
\]

Both faithful scalar characters lie entirely in \(R_5\). Their norms
to both proper scalar subfields vanish. Therefore even certified
class-zero results for those smaller fields would leave exactly the
faithful relative class contribution uncontrolled.

This excludes the proposed direct transfer. It does not exclude a
genuine relative algorithm that computes and certifies \(R_5\).
The [class proof](class_control/PROOF.md) distinguishes those assertions.

## 4. What changes when the coefficient prime grows

The [scaling calculation](class_control/SCALING.md) follows from the
actual torsion-field representation under the retained full-image input:

\[
[A:\mathbf Q]=p^2-1,\qquad
\operatorname{rank}U_A^-=(p^2-1)/4,\qquad
\operatorname{rank}U_A^\chi=(p+1)/2.
\]

Computing the entire relative norm-one unit group still has quadratic
rank growth. A method targeting one faithful character has a smaller,
linearly growing unit target. Merely writing \(A\) over a smaller
coefficient field does not remove rational coordinates or transfer its
faithful classes to that field.

These formulas quantify what a dedicated character computation could
save. They neither prove small arithmetic kernels nor give a RAM formula.
The new experiments do not determine \(r_U\) or \(k_C\) for the actual
seed at five, and do not establish their required scaling at larger
primes.

## 5. Status and evidence

| Question | Result |
|---|---|
| Does the old overflow prove mathematical impossibility? | No. It was a resource failure of a particular computation. |
| Can the initial seed factor-base stage run on this machine? | Yes: the changed run completed it at about 733 MB peak resident memory. |
| Did extra stack compaction repair it? | No: the proposed temporary-allocation explanation was disproved. |
| Do proper scalar-subfield classes bound the faithful seed classes? | No, by the exact transfer decomposition above. |
| Is the complete seed bound now proved small? | No. The actual unit rank and surviving class contribution remain uncomputed. |
| Does this show a fixed amount of RAM will finish certification? | No. Total resources for completion have not been measured. |

The packet preserves raw failures, source bindings, the rejected patch,
separate small-field replay, actual seed resource receipts, exact
relative-field replay, and written reviews. Eighty abstract
prime-power module controls test the class-transfer distinction; they
are not seed class groups.

**FIN, ORDER9, Q36 and seed-prime coverage remain unchanged.**
