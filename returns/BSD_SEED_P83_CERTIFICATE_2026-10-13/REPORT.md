# New seed certificate at coefficient prime 83

Date: 2026-10-13. **NEW_SEED_83_PRIMARY_VANISHING — computer-assisted, under retained seed and source inputs.**

For the fixed curve

\[
E:y^2=x^3-22735x^2+106272484x,
\qquad \boxed{\Sha(E/\mathbf Q)[83^\infty]=0.}
\]

This closes a previously unsettled primary component of the actual seed. It does not prove a cofinite bound or complete FIN, ORDER9 or Q36. It uses an existing theorem with a newly evaluated arithmetic witness, rather than claiming a new general mechanism.

## The computed witness

At auxiliary prime 167, all 166 plus modular symbols were identified by rigorous interval evaluation in the retained lattice `(1/1024) Z`. With primitive root 5 and `x(a)=ind_5(a) mod83`, the actual sums are

\[
c_k=\sum_{a=1}^{166}\binom{x(a)}k[a/167]^+,
\qquad(c_0,c_1,c_2)=(0,-23240,-1049574).
\]

Thus

\[
\boxed{(c_0,c_1,c_2)\bmod83=(0,0,44).}
\]

The symbols use the frozen pipeline's omega1 plus-period convention. The matched half-normalization changes the nonzero residue by an 83-adic unit and does not change the conclusion. See [the source application](selection/P83_OTA_THEOREM_CHECK.md) and [the final review](FINAL_MATHEMATICAL_REVIEW.md).

A separately implemented exact-rational checker reads only the printed enclosing balls, not the producer's candidate rationals or uniqueness flags. It recovers the same 166 rational symbols and sums. Replacing the primitive root by 125=5^3 gives the independently recomputed quadratic residue 51, equal to `44*3^(-2) mod83`. The saved prediction 44 was excluded from both production and acceptance; agreement with it is only a diagnostic observation.

## Why this settles the primary component

[Ota, Theorems 1.5 and 6.4](https://arxiv.org/pdf/1509.00682), applied with the retained rank two, full integral Tate-module image, Tamagawa and period hypotheses, converts this nonzero leading augmentation term into `Sha[83]=0`. Fresh exact counts give

\[
\#E(\mathbf F_{83})=92,\qquad \#E(\mathbf F_{167})=168.
\]

The coefficient prime is good and non-anomalous, the retained Tamagawa product 16 is prime to 83, and the auxiliary satisfies `167-1=2*83` with cyclic reduced 83-torsion (in fact zero). The theorem does not require `a_167=2 mod83`. A nonzero 83-primary torsion group would contain a nonzero element of order 83, so the full 83-primary group vanishes without assuming its finiteness first.

The retained rank/image/lattice inputs are not independently reproved here. The primary source application, exact output arithmetic and completed computational custody were reviewed separately within this Codex team. This is not independent human certification or proof-assistant verification.

## What was actually run and checked

The frozen, unchanged Arb engine evaluated the finite sum through `T=57,378,078,719`, using the existing 3,420-segment Fourier-coefficient prefix and a fresh output directory. It completed in approximately 46 minutes 49 seconds, with eight worker threads and no external paid computation. No source repair, retry, or subsequent prime calculation was needed.

The completed checks are:

- Unchanged fail-closed checker: `NONZERO`, no failure reasons; a post-run replay agrees.
- Independent exact interval reconstruction: all 166 symbols; exact lower coefficients and quadratic residue verified.
- Complete work-unit audit: all 3,420 large-prime units and 13,680 smooth blocks, their hashes, ranges, labels and receipt bindings.
- Exact count identity: `38,734,946,655 + 18,643,132,064 = 57,378,078,719`.
- Post-run input custody: all 3,452 frozen manifest entries and all 3,420 consumed coefficient files re-hashed successfully.
- The 20 frozen-checker controls passed before production. The 18 independent-verifier controls passed two seconds after production began, before the output was available. Historical positive calibration and runtime controls are retained.

The coefficient prefix contains 9,673,187,648 bytes. Its bytes were freshly hashed, not independently regenerated. Interval output checking does not itself prove the analytic enclosure theorem or the imported modular-symbol lattice. [Engine review](selection/ENGINE_CONTRACT_REVIEW.md) records that boundary.

The primary output `production/p83_l167/msl.txt` has SHA-256:

`b77ac22a524526d09080ad08c8a47e5a77a8ac2bc5687feb8fefcdbc97329342`.

## Evidence and precise endpoint effect

The complete new-run evidence archive includes the frozen engine/source/checker, input receipts, all 17,100 work units, final interval table, control outputs, monitor history, source audit and same-team review. **The 9.67 GB raw cached coefficient prefix is an external retained dependency and is not included.** Original coefficient-generation certificates and antecedent seed proofs retain their prior project grades. See [REPLAY.md](REPLAY.md) for what can be replayed from this archive alone.

Relative to lab baseline `15db242ee6224c85f60e7a9a999df3e8cfd6469b`, coefficient 83 is newly settled. Coefficient 53 remains unresolved, so the retained conditional alternative `#Sha=9 or #Sha>=25281` is unchanged. There is no claim that all auxiliary primes work, that the 288 identity is proved, or that finite enumeration controls the infinite tail.

**The added result is actual seed-primary vanishing at 83. FIN, ORDER9 and Q36 remain open.**
