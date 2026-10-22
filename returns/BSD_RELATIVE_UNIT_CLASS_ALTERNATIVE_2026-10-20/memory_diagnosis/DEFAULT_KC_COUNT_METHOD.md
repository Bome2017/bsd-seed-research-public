# Streaming factor-base dimension

This count follows `FBgen` in the pinned PARI 2.17.3 source but does not retain
any prime-ideal objects. For every rational prime through C2=419775, it counts
the prime ideals whose norm is at most C2. If the rational prime does not
divide the polynomial index, degrees of irreducible factors modulo that
prime supply the residue degrees. At index primes the maximal-order prime
decomposition supplies the actual residue degrees.

The initial relation base uses rational primes at most C1=4813, with the same
C2 norm cutoff; this reproduces the source's convention. Its two counts must
agree with the actual producer's KC=721 and KCZ=175 before acceptance.
The same streaming calculation also counts the intermediate relation bounds
12034, 24068 and 48136, corresponding to c1=0.05, 0.1 and 0.2 after taking
the integer part of c1(log|D|)^2.

For the default C1=C2 configuration, PARI allocates
`cache.basis = zero_Flm_copy(F.KC,F.KC)` (`buch2.original.c`, line 3865).
In this 64-bit runtime, eight times the square of KC is a lower bound on the
bytes of this matrix's entries alone. Object headers, factor-base data, other
relations, precision matrices, and subsequent algorithms require further
memory. This is not a promise of the total RAM required to finish.

The command uses 256MB stack and an 18-second internal alarm under a
20-second process-group wall cap. A timeout or mismatch supplies no accepted
count.
