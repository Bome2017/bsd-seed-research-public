# Changed memory algorithm

Pinned source: PARI2.17.3 `src/basemath/buch2.c`, retained official archive.
The observed failure is inside `FBgen`, before relation collection.
`FBgen` stores required prime decompositions through C2 but does not
discard temporary stack allocations made while obtaining each one.

The proposed arithmetic-preserving change is local:

```
pari_sp avp = avma;
LP = idealprimedec_limit_f(nf,prim,l);
LP = gerepilecopy(avp,LP);
```

The old `LP` call is replaced by the same call followed by PARI's normal
stack compaction, retaining exactly its returned object. This runs before
the source's existing `setisclone(LP)` marker and before storing LP in
F.LV. Earlier F.LV entries and the factorbase arrays predate avp, so remain
untouched. No ideals, incidence maps, class relations or completeness
checks are removed.

Compile only this renamed translation unit into a separate dynamic
library, linked to the installed2.17.3 runtime. Do not replace installed
PARI. A wrapper uses its documented c1=.02 with c2=0(default), and exact
compact-data flag1. The smaller relation factorbase reduces the later
quadratic relation matrices. The unchanged C2 computation still selects
the full GRH-generation bound and performs the later honesty check.

Before seed execution, compare the wrapper's outputs and source/target
unit norms against unmodified GP on a known small field; require an
unmodified bnfcertify and exact unit checks. A completed seed BNF would
still need its own class certification. The first seed gate remains
512MB/90seconds; no increase is authorized by this patch.
