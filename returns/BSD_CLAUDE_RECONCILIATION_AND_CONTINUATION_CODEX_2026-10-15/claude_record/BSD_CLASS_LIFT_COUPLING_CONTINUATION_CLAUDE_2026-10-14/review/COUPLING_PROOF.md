# Constructive class-defect certificates and their finite arithmetic realization

Date: 2026-10-13. Grade: written derivations of finite linear algebra and ray-class interpretation under explicit source hypotheses. This document supplies no actual new rank bound and assumes no value of Sha. It is intended to make the experiment produce an arithmetic certificate rather than just a final dimension.

## 1. Use a complete source, with the right units

Let p be odd, K the actual nonzero-p-torsion point field, and A=O_K[S^{-1}] for the chosen finite support S. Write

    B = { beta in K^*/K^{*p} : v_q(beta)=0 mod p for q outside S },
    U = A^*/A^{*p},                 C = Cl(A)[p].

There is an exact sequence

    0 -> U -> B -> C -> 0.                                    (1)

The map sends beta, with its outside-S ideal equal to a^p, to [a]. Surjectivity follows by choosing an ideal representing each class and a principalization a^p=(beta) in A. The kernel consists of units times pth powers. These constructions also show (1) is an exact sequence of F_p vector spaces.

For the full-valuation-zero subspace use A=O_K and ordinary units. If allowed S-valuations have not been removed, ordinary units alone cannot be called the kernel: S-units must be used, or valuation columns must remain as a separate block. A list of sampled units or class generators gives no upper bound for (1).

Scalar-character components may be taken by an explicit prime-to-p idempotent. No semisimplicity is assumed for the full Galois group when p divides its order. Alternatively impose the scalar equations as rows of D on the full source, avoiding a projection issue.

Let

    D:B -> Q

be the actual finite collection of necessary defects: scalar/norm, global additivity, and local Kummer-quotient defects. The targets and their bases must be specified. At a local place the target is the local multiplicative/Kummer source **modulo the actual local point image**, not the raw source. If that image is zero, every local evaluation row is an equation; zero does not mean skip the place.

Assume the retained descent comparison injects the true Selmer group into B, sends its rational-point subspace to W, and sends every Selmer class to ker D. Exact equality with ker D is not needed for an upper bound. Each row nevertheless needs a proof that it vanishes on every genuine Selmer class.

## 2. The class-lift defect and the dual rejection certificate

Choose unit basis u_1,...,u_a and class basis c_1,...,c_b with actual lifts beta_j. In bases of Q let

    A = ( D(u_1) ... D(u_a) ),
    Bmat = ( D(beta_1) ... D(beta_b) ).

For c with lift beta define

    kappa_D(c) = D(beta) mod im A.                            (2)

Changing beta by a unit or a pth power changes its value by im A or zero. Thus this map is independent of lifts. Its kernel consists exactly of class directions having an admitted lift after unit repair, and

    0 -> ker(D|U) -> ker D -> ker kappa_D -> 0.               (3)

For a particular lift beta, the following are equivalent:

1. No product beta * product_i u_i^{x_i} has zero D-defect.
2. D(beta) is not in im A.
3. There is a row lambda in Q^dual with

       lambda A=0,             lambda D(beta) != 0.           (4)

The implication3->1 is direct. Conversely, a nonzero vector in Q/im A is separated from zero by a linear functional on that quotient. Pull it back to Q. This is finite-dimensional duality, with no arithmetic duality or Sha finiteness assumption.

Equation(4) is a short rejection certificate: recompute the finitely many entries of lambda A and lambda D(beta), verify all zeros and one nonzero. A repair certificate is equally concrete: exhibit x with A x=-D(beta), and retain the actual product beta * product_i u_i^{x_i}. Merely observing D(beta)!=0 does not reject its class direction; a unit might repair it.

A repaired class is not automatically excess. Test whether the repaired element lies in W by its exact global source coordinates. If it is a point class, retain that identity, including any pth-power factor. If it is not in W, it is only an excess candidate until all-place/global admission is justified.

## 3. Produce an actual minor and an actual arithmetic row

Let r=rank A. After permuting rows and choosing r independent unit columns, write the pivot submatrix as A_11, an invertible r by r matrix. The remaining rows against those columns are A_21. Every unit column is a combination of the selected columns, so

    L = ( -A_21 A_11^{-1} | I )

annihilates all of A. Its rows form the full left kernel of A. Then

    K = L Bmat

is a matrix for kappa_D in an explicit basis of Q/im A. A nonzero k by k minor of K proves rank kappa_D >= k; its determinant is a finite exact residue, not an approximate rank estimate. The certificate includes the pivot inverse, lambda rows, selected ideals/lifts, and the nonzero determinant.

In particular,

    dim ker D = (a-r) + (b-rank K).                           (5)

If W has dimension2 and is contained in ker D, the upper space for Sha has dimension at most a+b-r-rank K-2. A bound on r alone misses repairable ideal classes; a bound on rank K alone misses admitted unit directions. For a source retaining a separate valuation quotient, include its admitted dimension before subtracting W.

A class rejected by scalar/norm rows, one rejected by additivity, and one rejected only after local tests are distinct outcomes. Record the corresponding lambda support. When comparing incremental stages, units available for repair shrink only if they must also preserve every previously imposed equation. The combined matrix formalism enforces that condition automatically.

## 4. What a row means in field arithmetic

Every stored entry must come from a named homomorphism on an actual field element. Examples include:

- v_q(beta) mod p with the ideal q and uniformizer identified;
- a residue discrete logarithm of the leading unit, in a specified finite residue field;
- higher-unit characters modulo q^m, with enough precision proved to capture the local pth-power quotient;
- a multiplicative norm or affine-line map evaluated on beta, followed by an independently specified pth-power character;
- a linear functional on the local source quotient which annihilates **all** local Kummer point images.

A lambda row is therefore a finite sum of explicit characters. If lambda A=0 on a certified full unit basis, its value on a principalization beta is unchanged by every allowable global unit. If the basis is incomplete, that conclusion fails.

For an upper bound it is enough to use a proved subcollection of necessary characters. Such a smaller D enlarges ker D; a sufficiently small containing kernel remains sufficient. This can make a proof shorter than computing every local source exactly. By contrast, treating an unproved or overrestrictive row as necessary can falsely remove actual Selmer classes.

## 5. A concrete interpretation beyond the matrix: order-p lifts in a ray quotient

For the **local-only**, full-valuation-zero version there is an independently defined finite arithmetic object whose connecting map is exactly(2). This is useful because it interprets the defect without defining the object through Sha.

Choose a finite modulus m large enough that the selected local unit characters factor through

    R_m=(O_K/m)^*.

For p odd there is no needed real-sign p-part. Let rho:R_m -> Q be a surjection onto an elementary abelian p-group recording those characters, with any local Kummer allowance already quotiented out. If the original target has unused coordinates, replace Q by the image. Put

    C_0 = Q/rho(O_K^*).

The standard ray-class exact sequence provides

    O_K^* -> R_m -> Cl_m(K) -> Cl(K) -> 0.

This exact sequence is the sole imported arithmetic statement here; see Milne, *Class Field Theory*, Chapter V, Theorem1.7, printedpp150--151. The primary PDF was opened in the web parser this turn: https://www.jmilne.org/math/CourseNotes/CFT.pdf . The definitions and sequence, not any BSD statement, are used.

The induced surjection R_m/im units -> C_0 has a kernel. Quotient Cl_m(K) by the image of that kernel, obtaining a finite abelian group G with

    0 -> C_0 -> G -> Cl(K) -> 0.                             (6)

Because C_0 is killed by p, define

    boundary: Cl(K)[p] -> C_0,    c |-> p*c_tilde,

where c_tilde is any lift to G. The definition is independent of the lift. Choose an ideal a representing c and prime to m, with a^p=(beta). Such ideal representatives can be chosen away from any finite set. Then beta is a unit at the primes in m. By the defining ray relation,

    p*[a] = [(beta)] = rho(beta) mod rho(O_K^*)

in the kernel of(6), up to the harmless inverse convention if the ray map is defined oppositely. Therefore

    boundary = kappa_local.                                 (7)

Consequently a class direction is locally unit-repairable exactly when it has an order-dividing-p lift in G:

    ker kappa_local = image( G[p] -> Cl(K)[p] ).              (8)

A nonzero boundary means every lift has orderp² when c has orderp. Thus a local rejection certificate detects actual p² growth in this finite ray-class extension. A repairable nonzero class has a lift of orderp. Both phenomena can be checked by principal ideal relations and finite residues, without a Sha order or an L-value.

This construction is derived here from the ray exact sequence. The construction is executed on718b1 in§8 below; the abstract derivation itself is not a new uniform theorem. It does not automatically model the global norm/additivity rows, or the allowed-S-valuation source. An S-ray analogue needs its own exact source identifications. For a full combined D, the matrix certificate of§§2--4 remains valid even when no ray-class interpretation is supplied.

At a fixed field and modulus, one may certify selected minors directly from the ideals and residues without computing the whole ray class group. To prove the full class-source upper bound one still needs completeness or an independently proved containing bound for Cl(K)[p]. A convenient quotient whose class source is incomplete is insufficient.

## 6. What the held-out experiment should measure

A genuinely discriminating test should retain the following before reading the final admission rank:

1. A complete or certified containing unit/class source, all allowed valuation columns, actual class ideals, and exact pth-power principalizations.
2. The unit evaluation matrix and the chosen pivot/annihilator rows. These can be constructed without evaluating the held-out class principalizations.
3. A proposed arithmetic rule predicting which selected lambda rows detect which class directions, or predicting a nonzero minor from independently available ideal/residue data. Freeze that rule and the rows before evaluating those held-out class entries.
4. Evaluate the actual principalizations under those rows. Preserve zero minors, unexpected repair solutions, and failures caused by source incompleteness separately.
5. For surviving class directions, solve the unit repair equations and determine whether the repaired lift is a rational point or admitted excess.

The output is not merely a Selmer dimension. It is: which class directions are rejected for a demonstrated reason, which require actual unit repair, and which repairs are exhausted by known points. The ray realization suggests an additional exact discriminator: do the chosen class directions lift with orderp orp² in the local-congruence extension, and which local character detects the latter?

Selecting lambda after seeing D(beta) is a valid *certificate* but is not a held-out predictor. Inferring a rule from one curve and checking it on another is useful only if the complete source and conventions are comparable. A negative result at one local place may be repaired globally by units; raw local nonzero values alone are not the discovery target.

## 7. What would convert these data into a seed bound

A fixed-p upper bound would follow from authenticated source dimensions a,b, an explicit rank lower bound r for unit defects, and k independently certified class-defect directions with

    a+b-r-k <= 3,

together with the retained full source/Kummer comparison, point rank2 and parity on its stated domain. A direct bound<=2 would avoid the parity step. No unknown Sha order occurs in the computation of these quantities.

To cover infinitely many coefficient primes, one needs an arithmetic reason for sufficiently large actual minors of the corresponding maps to remain nonzero, or another bound on their combined deficiencies. The ray interpretation does not make that automatic: K, m, units, class groups and the connecting map change with p. A fixed integer or resultant could suffice if a genuinely fixed integral construction produced it; none is supplied here. An independently proved varying-p rank estimate could also suffice.

The actual additional mechanism identified here is therefore finite and testable: class rejection is an order-p lifting obstruction in a concrete congruence-class extension, with a small dual certificate obtainable from principalizations and local characters. It does not identify that obstruction with Sha, assert it always occurs, or bound the seed's unresolved tail.

## 8. Executable presentation recipe and the actual718b1 realization

The finite extension in§5 can be presented without constructing its class field or performing a new full ray-class-group search. The following data define it arithmetically.

1. Retain a certified complete ordinary class-p basis c_j, ideals a_j and exact principalizations a_j^p=(beta_j).
2. Move each a_j off the selected local primes: choose gamma_j with prescribed valuations -v_q(a_j), including zero prescriptions at the other selected primes. Put J_j=a_j(gamma_j) and beta'_j=beta_j gamma_j^p. Check J_j^p=(beta'_j), coprimality, and every zero local valuation exactly.
3. Fix a finite modulus whose residue-unit quotient modulo pth powers captures the selected local characters. For a deliberately conservative bound, exponents2v_q(p)+1 above p suffice by Hensel; exponent1 suffices away from p. A smaller modulus may be used with a proved local unit-filtration bound. The actual run uses the retained local helper's n=floor(3e/2)+1 at3, with its existing local-source qualification.
4. Form R, the product of the finite residue-unit groups modulo pth powers. Its coordinates come from actual `idealstar`/`ideallog` objects. From each full local Kummer basis take **its intersection with the valuation-zero subspace**, then project to residue-unit coordinates. Quotient R by these allowances and by the image of the full ordinary unit group.
5. Let L be a complete annihilator for that combined image. Evaluate k_j=L*rho(beta'_j). The underlying quotient kernel has dimensiont; the boundary matrix is K=(k_j).
6. The preimage of Cl(K)[p] in the pushout extension has the actual integer presentation

       [ p I_t   -K ]
       [   0    p I_b ],                                    (9)

where integer representatives of the residues in K are chosen. Columns are relation vectors: p e_i=0 and p x_j=k_j. A different residue representative or choice of class lift produces an isomorphic presentation. The positive sign for k_j uses the ray map taking beta to the ideal(beta). Inverting that convention negates K and changes neither ranks nor orders.

If rank K=k, the group in(9) has k factors of orderp² and t+b-2k factors of orderp, with k trivial Smith entries. Thus a specific class direction with nonzero boundary has orderp² in every lift, while a zero-boundary direction has an orderp lift. This is an exact description of the arithmetic pushout, not an arbitrary matrix model: the identifications in steps1--5 bind(9) to actual ideals and finite residue groups.

### Actual718b1 computation

The script `review/ray_pushout_718b1/construct.gp` consumes the full source exported by the primary arithmetic worker. Curve, field and point data are:

    E=[1,0,1,-5,0], points [-1,2],[3,2],
    f=w^8-4w^7+7w^6-7w^5-11w^4+29w^3-324w^2+309w-96,
    Cl(K)=C3, selected rational places2,3,359.

The BNF completeness/field-source certificates are retained from `search/718b1`. This script does not promote an uncertified BNF. It checks the actual shifted ideal J, principalization beta', and class coordinate:

    J³=(beta'),    v_q(J)=v_q(beta')=0 for every selected q,
    [J]=1 in the certified C3.

The chosen modulus has norm

    2^4 * 3^14 * 359^4 = 1271145730342176144.

The finite local residue-unit quotients have dimensions1,9,1 at2,3,359. The actual local Kummer allowances restricted to that unit space have dimensions1,1,0. The full global unit image has rank4. Their combined image has rank5 in an11-dimensional residue-unit space, so C_0 has dimension6. Direct evaluation gives

    kappa_local([J])=0 in F3^6.

Accordingly the actual pushout presentation is3I_7 and its Smith factors are

    (3,3,3,3,3,3,3):       G ≅ (Z/3)^7.

This G is the specified quotient of the ray class group, **not** the whole ray class group, the class group, or a Selmer group. The ordinary class generator has an order3 lift here. It does not become order9. Its zero boundary was calculated from its principalization; it was not inferred from a Sha label.

The primary worker independently supplies a more precise explanation of this repair. With its named global units UE_i and tangent-function point evaluations, the repaired lift is

    beta * UE_2² * UE_4² = ftan(P1) * ftan(P2)² * (explicit cube).

Those are literal field/cube identities in `arithmetic/718b1/witness_data.gp`. Thus this admitted class direction is supplied by rational points, not by excess. Its raw local defects at3 and359 are real, but the unit repair removes them. This is exactly why a nonzero raw class-defect entry would have been an invalid rejection test.

`certificate.gp` retains the actual field, units, class ideal, gamma, shifted ideal, beta', modulus, allowance matrices, residue evaluations, annihilator, boundary, integer presentation and Smith factors. `matrices.json` exports the finite linear algebra for independent reconstruction. The final producer has clean stderr. Rejected development outputs are stored separately, including a singular-system solve attempted before selecting independent columns; their PASS text is not an acceptance record. The run is accepted only with empty final stderr and all displayed exact checks.

This actual realization tests the *repair* branch. A class-rejection example would require a computed nonzero boundary on another source; no order9 example has been manufactured or inferred here.
