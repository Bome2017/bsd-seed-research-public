# Continue with actual arithmetic values, not another formal model

The new derivation narrows the finite arithmetic source. It does not supply the uniform nonvanishing theorem. Do not describe this document as that theorem or as a guarantee of a successful route.

## Frozen source and exact quantities

Retain the actual optimized integral Euler system of Ochiai instantiated in ARITHMETIC_SOURCE.md of commit a87b1af, not arbitrary elements of a free local module. Keep the source coordinate shift X=p+(1+p)S and its tame component. On the cofinite ordinary domain, take the two integral weight specializations

    weight 5: T=(1+p)^3-1,
    weight 6: T=(1+p)^4-1.

For the first use s=2,3 and for the second s=3,4. Let q_ws be the image of the specialized GLOBAL arithmetic class in the actual integral local singular quotient. In a primitive integral generator of that quotient, compute its coordinate modulo p^4. These are the four values to target.

The residual representation/local conditions and the index bound for these four points are proved from retained inputs in DERIVATION.md section 4. Their own class indices are used: no equality to the older normalization z_g, no eta_p=1, and no assumed primitive global Kato class.

## What should actually be built

Construct the local quotient images of these two compatible modular Kato systems from their arithmetic source: optimized zeta maps/modular units followed by the exact ordinary localization/Coleman maps, reduced at precision p^4. Use the lower weights to avoid reconstructing the four higher-weight fibres in the previous handoff. A finite-level realization at the previously justified cyclotomic quotient is allowed; no smaller quotient has been proved adequate here.

An alternative proof may compute an integral linear combination of the four images without computing each separately. Such a formula must use actual arithmetic source maps. It must not choose coefficients by dividing an unknown Kato value, replace the source with a norm-compatible formal family, or infer a p-unit from complex nonvanishing.

For NONVANISHING, independent choices of primitive local generators at the four points do not cause a period-comparison gate. Their coordinate changes are units, and whether a residue is zero modulo p^4 is unchanged. For COEFFICIENT RECONSTRUCTION with four_value.py, put all four values in the common source-compatible coordinate or provide the four unit transports. A nonunit or unknown p-power transport invalidates the inference.

## Precision and direct verification

The code takes the four F-values in this order:

    (3,2),(3,3),(4,3),(4,4).

It multiplies by known principal-unit factors r_N,r_N^3,r_N^2,r_N^4, with r_N^4=<N>, and inverts the true p-adic evaluation matrix. It never replaces that matrix by its mod-p reduction when reconstructing higher digits. It returns A,B modulo p^2 and C,D modulo p.

Do not generate a "sample seed input" from synthetic polynomials. The included self-tests are deliberately and explicitly synthetic. Arithmetic residues need separate source identities and certified provenance. The code does not check those identities.

## Endpoint criterion and return obligations

A proven nonzero residue at any one of the four points implies seed Sha[p^infinity]=0 on the established domain. To remove the infinite ordinary tail, prove this for all but finitely many ordinary p by an arithmetic identity or estimate controlling these actual values. A finite list of successful prime computations does not do that.

A valid forward return would supply one of:

1. An independent cofinite nonvanishing proof for the four-value ideal, with its actual finite exceptional set or a fixed independently defined exceptional integer.
2. An explicit arithmetic evaluation/comparison of one or more of these four values with a demonstrably smaller independently specified global object, including all integral factors. A statement merely defining the smaller object to be the value earns no reduction.
3. A seed-specific computed value with a justified finite purpose, clearly NOT a uniform result. Do not launch such a campaign by default; the user has prioritized the uniform argument.

If reviewing this new functional-equation step reveals an error, report and repair that exact error. Do not silently promote a conditional four-value test to an accepted seed theorem. If the step survives but the arithmetic values remain uncomputed, say so; no amount of additional formal examples changes that fact.

## Boundaries that must remain explicit

* Hida/source/global low-jet statements retain their existing grades; independent review is pending.
* The functional equation constrains the seven coefficients but does not force any nonzero.
* No theorem here excludes collisions with existing witnesses. Only an actual matched equality could establish one.
* Ordinary-only coverage does not remove supersingular primes. FIN, ORDER9 and Q36 are not concluded by the present return.
* This document does not authorize paid jobs, production computations, messages, or edits to the frozen research release.
