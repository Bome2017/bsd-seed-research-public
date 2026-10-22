# Measurement corrects the first memory hypothesis

The per-iteration profile measured zero reclaimed bytes at every logged
sample. The per-prime decomposition routine already returns a compact
object; the extra `gerepilecopy` adds no memory saving. The earlier
temporary-allocation hypothesis is withdrawn. The separate patch passed
its arithmetic controls but does not repair this resource failure.

At rational prime287117, 6024 usable prime decompositions occupied
486,146,064 retained bytes; total PARI stack use was498,131,896 bytes.
The final check bound is419775. Thus the512MB failure is explained by
required stored prime objects, not a leak demonstrated by this profile.
A rough continuation suggests around700MB for this phase. This is an
estimate, not a measured total and not a memory guarantee for BNF.

The default relation factorbase also extends to419775. The documented
c1=.02 changes that relation bound to4813 while leaving the complete
GRH-generation/honesty bound419775 unchanged. It therefore changes the
later relation matrices even though it cannot fit the complete
prime-decomposition storage into512MB.

One newly authorized gate uses **unmodified** GP with this smaller
relation factorbase and a2GB stack, bounded by120seconds. It uses no
custom library. This is not a repetition of the original default2GB
failure: its relation matrix has a different, smaller generating set,
while the required final completeness checks remain in place.
