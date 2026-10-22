# Weighted stable-ideal generator experiment

Primary source: the pinned degree-48 point field of the rank-two -47 twist of 11a1 at p=7. No old candidate family or completed BNF is used.

Setup exactly checks fourteen integral ideals: O and every prime over 7, 11 and 47. Each is fixed by tau, verified by HNF. The numerical archimedean pairing has twelve exchanged pairs and three fixed complex places. It is used only to choose search weights.

Deterministic schedule: amplitudes 2,4,8,16,32,64; twelve single-pair antisymmetric directions and four full-pair sign patterns; all fourteen ideals in the recorded order. A weight d means multiplying a real embedding row, or both real coordinates of a complex place, by 2^d. Paired places get opposite exponents; fixed places get zero. Thus the geometry breaks tau symmetry. Every weighted real embedding matrix is rounded after multiplication by 2^192, then qflll produces an integer unimodular basis change. Numerical LLL quality has no bearing on exact admission.

At each reduced ideal lattice, test its first twelve columns and the sums/differences of pairs among its first four columns. Keep only mixed-parity candidates, deduplicate up to sign, and calculate each norm exactly. Admit alpha only if it lies in I, |Norm(alpha)|=Norm(I), and idealhnf(alpha)=I. Check epsilon=alpha/tau(alpha) and its inverse are integral and its norm is 1. Export alpha as a compact factor with exponents (1,0,0,-1,0,0) in its six-element scalar orbit.

The main search is bounded to 180 wall seconds and 1GiB. It also stops at eight distinct exact relative units for immediate external rank evaluation. No complete unit basis or class-group bound is inferred. All finite failures and candidate counts are retained. A successful unit must still have nonzero faithful character and actual rejection rank before it reduces the complete-unit upper bound.
