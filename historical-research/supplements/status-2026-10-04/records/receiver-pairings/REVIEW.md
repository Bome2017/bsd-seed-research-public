# Independent review of the uploaded pairing argument

**Verdict: CONFIRMED_AT_RETAINED_INPUT_GRADE.** No blocking defect was found in the claims reviewed below. Literature novelty and formal verification are not claimed.

The input is bound in `INPUT_ZIP.json`. References below point to its `PROOF.md`. The exact receiver and its exceptional set are retained inputs, not proved again in this review.

## R1. Primary cup product — confirmed

For c,d in Sel_p and p odd, their localizations belong to the local Kummer conditions. These conditions annihilate themselves under local Tate duality. The local invariants therefore send each localized Weil cup to zero. Local Brauer invariants are injective, and the odd-primary Brauer group at a real place is zero. The field Kummer sequence identifies H²(Q,μ_p) with Br(Q)[p]; global Brauer localization is injective. Thus the global cup is zero.

This proves vanishing for every pair of Selmer lifts and makes the receiver expression independent of the rational-point ambiguity. No rank estimate follows. The proof correctly avoids the sign error of treating this degree-one cup product as alternating simply because its coefficient pairing is alternating.

The needed local statement is in Morgan–Smith, Proposition 6.1; global injectivity is in Milne, IV, Example 2.14(e). The source locations were checked this turn; see `SOURCES.md`.

## R2. First secondary radical — confirmed

Morgan–Smith, Theorem 1.3 and Example 1.4, apply to the multiplication sequence with its actual Kummer conditions. They identify the pairing kernel with the image of Sel_{p²} under multiplication by p. Rational Kummer classes lift, so quotienting by W_p is legitimate.

For the last identification, use the commutative Kummer sequences. The coefficient map E[p²] -> E[p] induces multiplication by p on Sha, not the identity. Its image is p A[p²], where A=Sha[p∞]. An element x in A[p] that equals p y automatically has p²y=0. Thus

    rad(b_0) = (image Sel_{p²} -> Sel_p)/W_p
             ≅ p A[p²] = A[p] ∩ pA.

This is valid without assuming FIN. A nonzero pairing value proves that its arguments are nonzero receiver directions; it is not a relation killing those directions.

## R3. Higher filtration — confirmed

Set F_n=A[p] ∩ p^n A. For x,y in F_n choose X with p^n X=x and put b_n(x,y)=CT(X,y). A second choice differs by z in A[p^n]. Writing y=p^nY gives CT(z,y)=CT(p^nz,Y)=0. This proves choice independence. Bilinearity follows from the same argument; CT(X,p^nX)=0 proves alternation.

Since A[p] is finite, A has the form D ⊕ F, with D a finite-corank divisible p-group and F a finite p-group. The pairing kills D and is perfect alternating on F. For the perfect finite pairing,

    (F[p] ∩ p^n F)^perp = pF + F[p^n].

Consequently a lift X annihilates the pairing precisely when x=p^nX belongs to p^(n+1)F. This gives rad(b_n)=F_{n+1}, with D[p] retained at every stage. The finite symplectic decomposition gives the same result one block at a time.

The argument distinguishes finite layers from the persistent divisible part. It does not extend the p-level class-group receiver theorem to p^n-division fields.

## R4. Dimension identity and controls — confirmed

Writing d=dim D[p] and r_n=rank b_n, each finite symplectic pair of exponent p^e contributes two to r_(e-1), and zero to the other r_n. Therefore

    dim B_p = d + sum_n r_n.

The input's examples with exponent p and exponent p² demonstrate the claimed two different failures of inference. All 24 supplied exact cases reproduce byte-for-byte. They are model checks, not realizations of this seed's Sha.

## R5. Additional accounting used in the attempted bound

The same block calculation gives

    log_p #F = sum_n (n+1) r_n.

This is an elementary consequence of the paired-group decomposition, not a new arithmetic upper bound. It is checked against the existing 24 cases in `checks/BOUND_ACCOUNTING.json`. `BOUND_ATTEMPT.md` explains exactly what further arithmetic valuation input would bound this sum and why that input has not been supplied.

## R6. Retained scope

The receiver identification holds on the supplied cofinite domain, under its retained global hypotheses. The present review confirms the deductions made from it, not the whole historical seed program. The packet's negative conclusions are correctly scoped to the tested primary cup product and invalid uses of secondary pairings. They do not refute arbitrary cochain constructions, non-Selmer inputs, or independently proved arithmetic bounds.
