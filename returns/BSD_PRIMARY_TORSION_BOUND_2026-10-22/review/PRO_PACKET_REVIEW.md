# October 21 source experiments: October 22 review

Status: **SCOPED DEDUCTIONS SUPPORTED UNDER RETAINED FIELD/INERTIA INPUTS**.
This is a model desk review and exact computational recheck, not a human review,
novelty assessment, formal certificate, or fresh certification of the seed field.

The uploaded ZIP has SHA-256
`6f0aa3eab6268e034e2874d8cb75041b17d93a91e02562207d54137c43543595`.
All 45 manifest entries match. Archive members were checked for traversal and
symlinks before extraction. The supplied originals remain unchanged under inputs/.

## Exact computations actually repeated

1. The supplied independent companion-matrix checker passed all 17 degree-24
   samples and its positive/negative quadratic controls.
2. A separately written norm checker reconstructed all **20,180 linear and 260
   quadratic norms**, using homogenized integer Horner evaluation and symbolic
   resultants. It reconstructed removal of all primes at most 65536 and all
   polynomial-discriminant primes, and checked every proposed private cofactor
   divides the resulting remainder and avoids those excluded primes.
3. The supplied C/GMP **direct-product** verifier was freshly compiled and passed
   all **20,440** cross-row private-support certificates. This is a replay of
   the separately implemented verifier, not a new implementation of that step.
4. The exact fifth-power checker passed all **20,180** linear private remainders.
   This does not certify the two separate character ranks for the 260 quadratic
   entries, and the source correctly does not claim that conclusion.
5. The analytic-expression constant checker replayed exactly. I also re-derived
   its factorial, logarithmic and square-root substitutions directly.

Neither the original maximal-order construction nor all 20,452 traces were
recomputed. Trace samples, all norm inputs, and cross-row private support have
the distinct scopes above. No class group or seed Selmer group was computed.

## Why the source exclusion is correctly scoped

A private rational prime outside the polynomial discriminant contributes a
nonzero anti-invariant divisor for its one generator. The generator and its
order-four scalar translate are independent over Q, since the scalar square acts
as -1. Different private primes separate the different generator orbits.
Consequently an ordinary-unit product in this tested scalar-closed family has
zero exponents in every independent pair. The exact inverse identities and the
twelve factored redundancies then make the product 1. Saturation introduces no
non-torsion unit.

The stronger linear mod-five argument additionally uses the degree-one prime
and its free scalar orbit, and a private valuation not divisible by five. The
rational norm test alone would not supply that conclusion for the quadratic
generators. This restriction is preserved.

## Why the analytic exclusion is correctly scoped

Put d=(p^2-1)/4 and q=4547. With the previous positivity and inertia inputs,
the October 20 expression B_p has lambda>0, Q>=q^(2d) and
lambda<=log(Q)/sqrt(p(p-1)). Substitution of
Gamma(d/2+1)>=(d/(2e))^(d/2) yields

    B_p >= 2^(1+(p-1)/4)
           [q e^(3/2) log(q) sqrt(2p/(p+1))/(8 pi^(3/2))]^d.

The elementary inequalities used in the packet give B_p>1000^d>p^4.
This lower-bounds an **upper-bound expression**, not an actual class number.
It therefore excludes obtaining a small class allowance by merely evaluating
that expression more accurately. It does not exclude a smaller actual faithful
class kernel, new relations with complete generation, or a different bound.

## Effect on this continuation

Keep the tested Cayley families and the old whole-order expression out of the
active search. The new small-split-prime torsion experiment is a different
primary-specific construction and is assessed separately. None of the checks
above reduces the surviving class contribution or changes FIN, ORDER9 or Q36.
