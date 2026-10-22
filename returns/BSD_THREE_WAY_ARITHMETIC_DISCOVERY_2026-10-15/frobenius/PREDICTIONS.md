# Sealed two-norm experiment

Fixed source: mirror389 curve [0,0,1,-21,-27], coefficient prime 3. The retained source coordinates are (0,0,0,0,0,0,1,1,1,1,2). This is a false survivor of scalar and all local conditions, not a Selmer class.

Arithmetic construction: form its exact affine-line norm b in the degree-eight slope field. At a prime completely splitting in the 3-torsion field, choose the first two nonopposite nonzero torsion points in source-root order. Predict that the source passes every additivity row if and only if b at the two affine triples (P,Q,-P-Q) and (P,-Q,-P+Q) is a cube. The prediction must be evaluated using b's exported polynomial, not by reusing the character row calculation.

Fresh sample: first 40 primes greater than 47653 and at most 2000000, congruent to 1 modulo 3, good for the curve, source elements and exported norm, with eight distinct roots of the source polynomial. Record skipped primes and reasons. The 40 norm-only predictions are frozen before generating source-character outcomes. No adaptive change based on success/failure.

The proposed explanation to prove is that all eight conjugate affine norms generate a two-dimensional irreducible Kummer module over Q(E[3]); a calibrated nonzero cubic residue at a completely split prime proves this module nonzero. If proved, its splitting field has degree nine over Q(E[3]) and Chebotarev gives relative failure density 1/9 among completely split primes. The density is a theorem conditional on the explicitly verified module and field inputs, not inferred from forty trials.

Controls: independently check exact affine norm cube identities for known rational points and retained genuine excess classes. If both pass identically, this detector cannot distinguish points from genuine Selmer excess. Do not claim a Sha bound.

Stop conditions: nonintegral/incorrect norm evaluation, failed scalar anti-cube identity, module dimension not two or reducible, norm criterion mismatch, or absent noncube witness must be reported and repaired or hypothesis withdrawn. Existing observed primes are calibration only.
