# Independent reading of the submitted four-value packet

Status: CONFIRMED_AS_A_CONDITIONAL_REDUCTION. The retained cofinite Hida, integral source, Selmer-control, determinant-divisibility and parity inputs keep their prior grades. This review does not certify those foundations anew.

## Checked in this pass

1. Howard, section 4, gives the reflection of the cyclotomic character and the constant family sign. Lemma 6 identifies that sign at a nonexceptional weight-two point. The seed has retained root number +1 and non-anomalous ordinary reduction, so the submitted positive sign is consistent with that source. Its exclusions p not dividing 6N phi(N) must remain in the fixed exceptional set.
2. I separately read Ochiai (2.7), Definition 4.1, (4.3), Theorem 4.12 and (4.12). The optimized source is attached to specified signed family symbol bases. Its Coleman image is the corresponding analytic family function. This supports using that function's functional equation, not assigning a symmetry to an arbitrary cohomology coordinate.
3. The dense-point calculation works in the stated frame: w is a multiple of 2(p-1), s a multiple of p-1, j=s+1, j'=w+1-s. The two p-Euler factors interchange; the gamma and i-powers give no extra sign there. The ratio is N^(w/2-s). These points are dense even after the critical-range inequalities, so the analytic identity follows. A change by an arbitrary two-variable unit changes the multiplier; the fixed frame is essential.
4. The changes zeta=(1+S)/(1+T)^(1/2), Y=(zeta-zeta^(-1))/2 and H=zeta^(ell_N/2)F are integral, invertible changes for odd p. Invariance and the retained double zero give precisely AT^2+BY^2+CT^3+DTY^2 modulo the fourth maximal-ideal power. I checked the printed coefficient formulas and the determinant 864 independently of any seed-value claim.
5. The four-point interpolation uses the actual p-adic matrix. The code correctly retains second digits of A,B and the b=3 cases. The determinant calculation modulo p proves invertibility, not an actual nonzero value.
6. The new weights satisfy the old index argument's numerical conditions: r=2,1,2,1 lies strictly below k/2 for k=5,5,6,6; both residual local characters remain the seed characters. Thus the endpoint implication follows if the retained variable-weight index and source theorems apply as written. Those are dependencies, not hypotheses proved by the interpolation matrix.
7. The exact two-fiber uniqueness argument is valid over Z_p[[T,S]]. It requires exact compatible restrictions; it does not give unrestricted interpolation of finite-precision arrays.

## Checks and binding

The supplied ZIP passed integrity checking, its manifest verifies 10/10, and both supplied programs reproduce their JSON outputs byte-for-byte. The 4,200 reconstructions and 140 index-three controls are formal data. The eight Git-blob bindings to the prior return are independently compared in checks/PRIOR_BINDINGS.json.

The new extraction derivation is in ARITHMETIC_EXTRACTION.md. Its moment calculation has a separate calibration using actual Delta symbols, rather than treating the submitted synthetic coefficients as arithmetic data.

## Scope and normalization precision

An isolated value measured in another primitive local frame has the same valuation. It does not necessarily satisfy the displayed functional equation as written. For reconstructing four common coefficients one must use the common source frame. Likewise, an unnormalized modular-symbol eigenvector or complex numerical L-value is not an admissible input to either extractor.

The source's period terminology is not used to infer a p-adic unit from complex nonvanishing or from a density statement. The proposed extraction uses the literal specialized symbol, so its source period ratio is included in the input. No new eta_p unit theorem is claimed.

There is no new proof here that F is outside (p,T,S)^4. The input correctly did not claim one. FIN, ORDER9 and Q36 remain open, and the ordinary theorem does not cover supersingular primes.
