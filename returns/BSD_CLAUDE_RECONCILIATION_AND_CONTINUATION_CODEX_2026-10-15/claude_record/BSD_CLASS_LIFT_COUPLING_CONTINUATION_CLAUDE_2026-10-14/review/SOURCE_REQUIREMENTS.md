# Class-lift coupling: source and acceptance audit

Date: 2026-10-13. Scope: independent desk audit of `CONTRACT.md` and the source construction in `lib/selmer.gp`, with a fresh primary-source check. No candidate arithmetic is certified by this document, and no expensive computation was run.

## 1. The source exact sequence must be named before taking a quotient

Let L be the degree-eight field of a nonzero 3-torsion point, let S_L contain every prime above the chosen rational set S (in particular every prime above 3), and set

\[
V_S=\{a\in L^\times/L^{\times3}:v_{\mathfrak q}(a)=0\pmod3
\text{ for }\mathfrak q\notin S_L\}.
\]

The source sequence is

\[
0\longrightarrow U_S/U_S^3\longrightarrow V_S
\xrightarrow{\pi_S}\operatorname{Cl}(\mathcal O_{L,S})[3]
\longrightarrow0.
\tag{1}
\]

Schaefer–Stoll, §5, printed p.8, supplies this sequence; their (5.1) and Corollary 7.9 then distinguish the source space from its global cohomology and Selmer subspaces. Their §10 gives the specialized 3-descent algorithm. Fresh source: [How to do a p-descent on an elliptic curve](https://mathe2.uni-bayreuth.de/stoll/papers/p-descent-long.pdf).

Taking zero valuation modulo 3 **also at the primes of S_L** gives a different sequence:

\[
0\longrightarrow U/U^3\longrightarrow V_0
\xrightarrow{\pi_0}\operatorname{Cl}(\mathcal O_L)[3]
\longrightarrow0.
\tag{2}
\]

This second statement follows directly by writing `(a)=c^3`; its kernel consists precisely of a unit times a cube. In (1), the ideal equality only holds away from S_L. Consequently:

* the full-source repair group in (1) is the **S-unit** space;
* the valuation-zero repair group in (2) is the **ordinary-unit** space;
* ordinary class 3-torsion is not interchangeable with S-class 3-torsion;
* an ordinary class killed on passing to the S-class group can still occur in V_0, represented by an S-unit combination with valuations divisible by 3;
* a nonzero ordinary class group need not yield a nonzero S-class source, and a class in the quotient Cl_S[3] need not lift to an order-three element of the ordinary class group.

The map to the ordinary class group on V_0 must be recovered from the cube root of the **full ideal divisor**. It cannot be read merely from the appended class-generator coordinates of `lsgens2`.

## 2. Audit of `lsgens2`

Write the certified ordinary class group as `Z^r / diag(cyc) Z^r`. Let `lp` have columns the class coordinates of the S_L primes. Then

\[
\operatorname{Cl}(\mathcal O_{L,S})
=\mathbf Z^r/(\operatorname{diag}(\mathrm{cyc})\mathbf Z^r+
\mathrm{lp}\mathbf Z^{|S_L|}).
\]

Let H be the column HNF of the displayed relation matrix and `U H V = D` its Smith decomposition. For every diagonal entry d_i divisible by 3, the vector

\[
e_i=U^{-1}(d_i/3)\mathbf e_i
\]

represents a basis vector of Cl_S[3]. This is the convention used by `lsgens2` and is correct. PARI's complete `matsnf(...,1)` output has precisely this transformation convention. [PARI matrix documentation](https://pari.math.u-bordeaux.fr/dochtml/html-stable/Vectors__matrices__linear_algebra_and_sets.html#matsnf)

Choose the corresponding fractional ideal c_i. Solve

\[
\mathrm{lp}\,n_i=[c_i^3]\pmod{\mathrm{cyc}},
\]

and construct a literal principal witness

\[
(\beta_i)=c_i^3\prod_{\mathfrak q\in S_L}\mathfrak q^{-n_{i,\mathfrak q}}.
\tag{3}
\]

Its image under pi_S is [c_i]. Together with a full S-unit basis these give a full independent basis of V_S. The proof is elementary: projection of any relation to Cl_S[3] kills the class coefficients; independence of the remaining S-unit classes kills the rest. Conversely, subtracting class lifts from any element leaves an S-unit class.

The original inspected version of `lsgens2` requested `bnfisprincipal(bnf,a,5)` and appended its second entry without checking the first entry. This was weaker than the older `lsgens` guard. Require a zero class-coordinate vector and verify (3) as equality of ideal HNFs. The returned second entry is a **famat of field elements**, not a prime-ideal factorization. Multiply the principal ideals of its factors, with their literal signed integer exponents. No enormous element expansion is necessary.

`bnfunits` orders its generators as nonunit S-units, ordinary fundamental units, then a torsion generator. Omitting the last generator is justified here only after checking that roots of unity have order prime to 3. A real embedding suffices; record the actual signature and `bnf.tu[1]`. Record the expected dimension

\[
\dim V_S=r_1+r_2-1+|S_L|+dim\mu(L)[3]+dim\operatorname{Cl}_S[3].
\]

Use `bnfcertify(bnf)` with the default full flag and require output 1. The weaker flag-one certification is not a certificate of the complete unit and class groups. These distinctions and the principal-ideal relation returned by `bnfisprincipal` are explicit in the [PARI number-field documentation](https://pari.math.u-bordeaux.fr/dochtml/html-stable/General_number_fields.html).

## 3. What the coupling map proves

For either exact sequence above, denote its source by V, unit kernel by U, class quotient by C, and let D:V→Y be a specified linear map of arithmetic constraints. Choose any linear section c↦beta_c and define

\[
\partial_D:C\longrightarrow Y/D(U),\qquad
c\longmapsto D(\beta_c)\bmod D(U).
\tag{4}
\]

The map is independent of the chosen lift. Two lifts differ by U, so their images differ by D(U). It has the exact kernel sequence

\[
0\longrightarrow\ker(D|_U)\longrightarrow\ker D
\xrightarrow{\pi}\ker\partial_D\longrightarrow0.
\tag{5}
\]

Indeed a class has zero defect exactly when some unit correction cancels the defect of its chosen lift. Thus

\[
\dim\ker D=\dim\ker(D|_U)+\dim\ker\partial_D.
\]

This is a useful computable decomposition, but does not by itself make the right side small. All admissible repairs must be allowed before calling a class excluded.

For staged scalar, global-additivity and local constraints, there are two safe implementations:

1. Stack all rows and apply (4) to the full source and full unit group; report which successive row block first makes the class's repair problem inconsistent.
2. After each stage, replace V by that stage's actual kernel, U by its intersection with the previous unit space, and C by its actual image in the original class quotient. Retain lifts and the projection. Then apply (4) again.

It is not safe to compute an abstract scalar eigenspace on the class group, choose unrelated lifts, and assume those lifts already satisfy scalar constraints. Unit corrections may be needed to lift an eigenvector. For the order-two scalar involution at p=3, averaging supplies a theoretical exact projector, but its actual correction and induced coordinates must still be recorded.

An executable quotient matrix is easy to authenticate: with D_U and D_C the unit and lift column blocks, choose a full row basis Q for the left annihilator of D_U. Then the coupling matrix is Q D_C. Check `rank(D_U)` independently and check `ker Q = im D_U`; checking only `Q D_U=0` is insufficient. For each claimed repaired class, save its solution x to `D_U x = -D_C c`. For each excluded class save an annihilator row witnessing nonzero defect.

## 4. Arithmetic acceptance conditions

Required retained data and independently cheap checks:

1. Exact field polynomial, curve model, actual nonzero 3-torsion point, and field/model maps; irreducibility and degree alone do not prove every desired residual-image property.
2. Full `bnfcertify=1` receipt for the actual saved BNF, prime-ideal list S_L, class invariants/generators, S-prime class-coordinate matrix, HNF and Smith transformations.
3. Every S-unit famat and every class lift with the literal witness (3). Verify unit support and every principal-ideal equality. Save any cube multiplier used by `redcube`, or independently verify the reduced/original ratio is an exact cube.
4. Source dimension from the certified groups; an auxiliary cubic-residue evaluation matrix of full column rank can additionally certify independence of the displayed mod-cube elements. Rank deficiency of that auxiliary matrix is not proof of dependence.
5. Exact scalar-action coordinates, with cube witnesses or another proved complete source-coordinate computation. Agreement at finitely many auxiliary primes is not by itself an equality in L*/L*³.
6. Global additivity: finite split-prime residue rows are necessary tests. Unless the actual Schaefer–Stoll global norm/additivity equation is verified, their kernel is a **containing space**, not a fully computed H¹ or Selmer group. This limitation does not prevent an upper bound of two once two independent rational-point classes fill the kernel.
7. Every local-image basis must consist of actual Kummer values with justified finite precision; sampling until the known image dimension is reached is sound only when each recorded sample belongs to that image. Save enough point/root and precision data to check this. Repeating a computation at higher precision is useful corroboration, not a replacement for a precision bound. Preserve the zero-image branch: if the local Kummer image is zero, every evaluation row is an equation.
8. Rational-point evaluation columns and literal global coordinate checks, plus independence modulo 3. Point columns in a containing kernel certify the matching lower bound; a surviving source class is not called Sha until quotient by the full rational-point image is justified.
9. Separate matrices for the full source V_S, its valuation-zero subspace V_0, ordinary units, S-units, and the two class projections. Label which sequence is being used by every coupling matrix.

If the complete source is obtained but only finite global-additivity rows are used, report both the containing-kernel dimension and the exact point-subspace dimension. If they agree, the 3-Selmer upper bound closes without needing to prove those finite rows characterize the entire global image. If they do not agree, no extra direction may be declared genuine Selmer merely from that survival.

## 5. Useful primary-source comparison example

Schaefer–Stoll §11.1 uses `y²=x³−22x²+21x+1`, with points `(0,1)` and `(1,1)`, and an octic class group of order 24. Their reported class lift mixes with a unit in the kernel of localization at 3; their historical computation assumes GRH. A new certified replay would be an explicit test of unit repair on a nonzero class source, not a discovery of a previously unknown mechanism. This example was suggested to the parent as a fallback, not launched by this audit.

## 6. Status

The class-lift construction is mathematically appropriate when the stated witnesses and completeness checks pass. The map (4) is canonical for its **named source sequence**, and it measures whether units can repair an arithmetic defect. No result here bounds its kernel uniformly across coefficient primes. Candidate-specific outputs still require independent matrix and witness inspection.
