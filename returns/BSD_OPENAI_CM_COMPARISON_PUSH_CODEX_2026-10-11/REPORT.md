# OpenAI CM comparison: actual construction attempt for the BSD seed

October 11, 2026.

**FINITE_MODULUS_CONSTRUCTION_REPAIRED; EXPLICIT_CM_MAP_DERIVED; NO_NEW_UPPER_BOUND.**

I applied the source method to the existing BD construction. This produced a concrete arithmetic map and a repair to the first raised-level comparison. It did not prove that the resulting CM value is nonzero, or establish the cross-level identity needed for the seed. The new statements are written deductions under retained inputs; an adversarial model-agent review supports the C3 argument. They are not formal or independent human certification.

## 1. The construction made in this attempt

On the first raised Shimura curve `X_1`, let `I` be the matched Hecke ideal and let `Kum_I` be the actual finite-field Kummer map into its Galois quotient. For a divisor `D`, define

\[
q_m(D)=c_q^{-1}\operatorname{Kum}_I((T_q-q-1)D),
\qquad c_q=a_q(E)-(q+1).
\]

The correspondence makes the divisor degree zero. Its scalar is invertible at the permitted coefficient primes. Commutativity of Hecke operators proves that the definition is independent of the correcting prime; on degree-zero divisors it is the original Kummer map.

For this seed, fresh exact point counts give `c_5=-8` and `c_13=-18`. Thus the correction works with one of these two fixed primes, without a cusp, an unknown rational Hodge denominator, or a freely chosen scalar eigenvector. Where both Hecke congruences are imposed, the single correspondence

\[
\boxed{2T_5-T_{13}+2}
\]

has degree zero and acts as **2**. Its normalization therefore introduces only the denominator 2. At coefficient 5, the componentwise construction uses the away-from-5 operator at 13; an unproved `T_p` congruence is never inserted.

The function on supersingular points feeds an explicit finite oriented-embedding coefficient for `K=Q(sqrt(-7))`. Under the retained CM/reduction correspondence, that coefficient is exactly the localization `beta` of the actual corrected CM divisor. This construction keeps its value in cohomology rather than replacing it by an arbitrarily scaled scalar eigenform.

This is an explicit realization of a previously implicit step. The C4 reduction square and C6 Hom-line cancellation were already in the record. No new modular theta-series transformation law is asserted: the full local Schwartz-function construction was not completed. [Map and finite coefficient](notes/CM_MAP_ATTEMPT.md).

## 2. A recorded C3 obstruction was removable

The claim that multiplicity one is “only proved prime by prime” does not prevent a uniform finite-modulus construction. I constructed a fixed base Hecke idempotent with one finite denominator, then followed BD's finite geometric proof for every admissible prime power outside that denominator. The natural component/Kummer maps assemble over `Z/m` by CRT. The Hom-line construction cancels a temporary Galois-module isomorphism without requiring a characteristic-zero raised eigenform.

This closes the **first raised, finite-modulus C3 checkpoint**, conditional on the stated base module, residual-image and geometric inputs. The reviewer checked the nonsquarefree base level, the integral rank-two quotient, and the difference between freeness and Galois identification. No particular small prime has been proved outside the uncomputed fixed denominator.

For a fixed positive-sign auxiliary pair,

\[
m\mid\gcd(\#E(\mathbf F_{\ell_1}),\#E(\mathbf F_{\ell_2})).
\]

Consequently that pair supports only finitely many coefficient powers. CRT on one pair does not compare the different Jacobians needed as the coefficient primes vary. That stronger comparison remains open. [Construction](notes/C3_ASSEMBLY.md) · [agent desk review](notes/C3_REVIEW.md).

The follow-through also supplies a fixed-cover descent argument. A `Gamma_1(5)` cover has degree 12, and pullback followed by norm is multiplication by 12. A published large-image Ihara theorem supplies the required upstairs cohomological injectivity. This repairs the cover-index and Ihara-kernel issues for coefficient primes at least 7. Applying it to the packet's exact finite-field model still requires the explicit model binding recorded in the note; this return does not infer that every usual fine-level supersingular fiber is rational. Even full supersingular generation would not make the selected CM point nonzero. [Fixed-cover attempt](notes/FIXED_COVER_ATTEMPT.md).

I pushed that last binding to an exact adelic calculation: the local scalar action is trivial on the coarse Eichler curve, and the degree-12 forgetful map kills it upstairs. What remains is checking that the cited canonical-model definition uses precisely that descent action; its defining Part I §6 was not retrieved. The accessible Part II explicitly omits that section. This is a narrow unverified source interface, not an assertion that the construction fails. [Calculation and source boundary](notes/MODEL_BINDING.md).

## 3. Correction to the earlier OpenAI applicability screen

The earlier `-I` Frobenius mismatch concerns G2 primes. Our BD detector uses **different, positive-sign primes** with eigenvalues `1,ell`. The mismatch did not rule out the construction attempted here. I corrected that scope and carried out the CM-map construction on its actual domain. [Correction record](CORRECTIONS.md).

## 4. Why this still does not supply the seed bound

The outstanding arithmetic is the value of the selected CM class after transport between the two local realizations. A well-defined function on all supersingular points can vanish at the selected CM point. The source manuscript supplies its nonvanishing separately, from a rank-one Heegner witness; the map construction alone does not supply a rank-two replacement.

The parallel determinant attempt reached the same distinction in another form. I constructed the actual central quotient by the known point plane, retaining `H^2`, and tested a noncentral acyclic-fiber replacement. Even a successful analytic/determinant **unit comparison** permits arbitrarily large central finite content unless a separate central arithmetic evaluation controls it. The explicit alternating matrix control keeps that content visible; it is not a seed example. [Attempt and exact boundary](notes/INDEPENDENT_CONTROL_ATTEMPT.md).

Cornut's CM-point nondivisibility theorem is a genuinely relevant cross-coefficient-prime input. It concerns a span in a tower, under different geometric hypotheses; it does not identify the selected depth-two class. Freezing a prime-to-coefficient tower gives an idempotent augmentation ideal, so merely taking its quadratic augmentation quotient cannot supply the missing projection. No global impossibility claim is made.

Thus the attempt supplies a usable construction and removes an overstated source obstruction. It supplies **no independent upper control** on the selected CM value or the actual derivative's excess content. It is not a reason to launch a large value-enumeration campaign. A further main-line continuation needs an arithmetic comparison or value bound, not another proof that the function exists.

## 5. Evidence and endpoint status

- Actual point counts at 5 and 13 and the Hecke degree/eigenvalue calculation reproduce exactly.
- Nine alternating finite-content models check the stated limitation of a unit comparison. These are algebra controls, not seed realizations.
- Source copies and original paths are bound in `INPUT_BINDINGS.json`. The OpenAI pin is `fd4aeeb2ee4fc729c18d98444fed42fd0529eeeb`.
- The new deductions retain the previous seed modularity, saturated basis, residual-image and CM geometry grades. None was freshly recertified here.
- No seed CM scalar, Kato coefficient, new primary certificate, uniform valuation bound or rational leading-term comparison was computed or proved.

**FIN, ORDER9 and Q36 remain unchanged.** The mathematical change is a more complete finite arithmetic construction, not progress through its missing nonvanishing theorem.

[Sources](SOURCES.md) · [exact controls](checks/exact_controls.json) · [review handoff](HANDOFF.md).
