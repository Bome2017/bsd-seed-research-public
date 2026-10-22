# Next arithmetic task: the genuine Kato zeta map modulo the fourth power

## Target, not a promise

Use the cofinite ordinary Hida datum from commit 1f402a60b6fb8f1002fe6a4211f33e5a713e0884. Verify the new local-family lemma in PROOF.md only as needed to use its maps. Then work on the global arithmetic image. Do not end the run after another general local-lattice review.

The new operation is:

    original integral Kato modular-unit/zeta construction
      -> actual family class on the specified weight/cyclotomic component
      -> reduction modulo (p,T,S)^4
      -> local rank-one quotient
      -> T=S=p modulo p^4.

The desired residue is epsilon_p. A proved epsilon_p!=0 on a cofinite ordinary domain, with the source condition below, gives primary vanishing on that domain.

## 1. Fix the arithmetic source before any interpolation

Construct the finite-order image of Kato's *actual* integral zeta map, using the original etale regulator/Chern-class and moment maps. Use a primitive signed family Betti vector from the newly free integral module and match the fixed Kato period vector at the weight-three point. Do not choose a new complex embedding to make a local line agree and then silently replace the old vector.

Retain the smoothing factors from the modular-unit construction. It is sufficient to prove that the specialized class is an integral multiple r_p z_g. A proof that r_p is a unit is convenient but not mandatory for a positive certificate. A rational comparison with an unknown p-denominator does not suffice.

If an existing family theorem supplies only one winding-normalized class, compute its relation to the primitive Betti vector; do not call it primitive. If it necessarily inserts an extra p^2 factor, the b<=3 test for that particular class cannot succeed. Repair the arithmetic source through the linear zeta map, not by dividing the resulting cohomology class without justification.

## 2. Use the correct family and finite coefficient ring

Intrinsic coefficient ring: R=Z_p[[T,S]], with nu_T and nu_S defined in PROOF.md.

    U=V(T) tensor nu_S^(-1),
    M=R(bold-alpha(T) nu_S^(-1)).

The W3 point is T=S=p. In Ochiai's original cyclotomic coordinate the shift is S_src=p+(1+p)S, and the tame component is shifted by omega. At W3, the source arithmetic character is chi_cyc^2 omega^(-1). Check the contragredient eigenform and its nebentypus when using the source L-value formula.

Work modulo m^4=(p,T,S)^4, retaining the coefficient precisions p^(4-i-j). The local cohomology base-change lemma permits this reduction without a hidden local Tor term. It says nothing about selecting arbitrary global lifts.

## 3. Compute the arithmetic image, not a formal compatible family

Obtain the ten coefficients f_ij, i+j<4, of the actual Coleman/cohomology coordinate of the class from step 1. Give the formula or finite algebraic source for them. Source bindings must distinguish actual modular-unit classes from formal packet variables satisfying norm relations.

The exact scalar to study is

    epsilon_p = sum_(i+j<4) p^(i+j) f_ij mod p^4.

A nonzero jet before diagonal specialization is not enough. Keeping T and S distinct until this evaluation is mandatory. Do not assume a T^2 zero or discard f_00, f_10 or f_01 without an arithmetic proof.

The supplied checker evaluates the finite-ring formula once coefficients are provided. It does not certify their arithmetic origin and must not be reported as a seed computation on its built-in formal controls.

## 4. Continue to the actual bound

Try to derive a closed expression or relation for epsilon_p from the constructed finite-order regulator, exploiting the fixed target curve and its primitive point data. A cross-prime ancestor is allowed but not required. Any proposed relation must apply to the actual Kato classes rather than all formal norm-compatible packets.

The acceptable success is a proof of nonzero epsilon_p for all p in a cofinite ordinary domain. A formula for the ten genuine coefficients or a proved source specialization law is a concrete intermediate result, with the uniform nonvanishing still stated open. An arbitrary cohomology generator is not such a result.

If the residue is proved equal to an old uncontrolled witness up to a unit, record the equality. Do not present the renaming as progress. The identity is not itself a theorem that all further arithmetic work on W3 is impossible; follow the user's stop direction for that tested construction unless there is an explicit new independent estimate.

## 5. Preserve the alternative already available

Do not delete the M_p route. If the eta_p comparison is computed incidentally, use its actual valuation h_p and the valuation-aware test of PROOF.md section 7. Do not reject it solely because h_p is not zero. Do not commission a normalization-only successor as the default output of this task.

## Return labels

- W3_COFINITE_BOUND: cofinite ordinary nonvanishing proved with source law and all lattice conditions.
- W3_GENUINE_JET_CONSTRUCTED: actual finite Kato jet constructed with source law, nonvanishing still open.
- W3_SOURCE_LAW_PROVED: a proved integral primitive-source/interpolation map, but no genuine jet evaluation yet.
- W3_COLLISION_IDENTIFIED: exact matched relation to a previously uncontrolled witness, no new estimate.
- NO_NEW_ARITHMETIC_RESULT: only a rephrasing, formal control, or an uninstantiated source theorem.

A limited mathematical obstruction may be documented if proved; it must name the tested source or operation. It must not replace this construction task with another broad audit.

No expensive fixed-prime production campaign, outside message, paid job or automatic successor is authorized by this file. The user's live instructions govern execution. Supersingular primes and finite exceptions are outside the cofinite ordinary claim. FIN, ORDER9 and Q36 are not consequences of this brief.
