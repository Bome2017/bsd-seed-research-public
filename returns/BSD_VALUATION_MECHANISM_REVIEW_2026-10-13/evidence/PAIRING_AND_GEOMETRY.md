# Paired comparison and geometry selection

Written deduction under named canonical ordinary-height conventions. No BSD, finiteness, exact Sha order or seed bound is assumed.

For the d43737 pairs, the exact degree5 isogeny satisfies phi*omega_F=omega_A, all kernel points are real, and detM=5. Therefore Omega_F=Omega_A/5. The same rational newform normalized by these periods gives L_std,F=5 L_std,A. With a common cyclotomic character and functorial ordinary unit-root splitting, M^t H_F M=5 H_A. Determinants give detH_F=detH_A. C_A/C_F=5 and trivial torsion give the exact identity Q_F=25 Q_A wherever the quotient is defined. Numerical comparison only checks this to available precision; it cannot show Q_A=1 or Q_F=25 exactly.

The new A-side calculation did not use F values. It supplies direct L2_A=4*5+O(5^2), determinantH_U,A=4+3*5+5^2+5^3+2*5^4+O(5^8), Q_A=1+O(5). The actual height matrices satisfy the functorial identity to O(5^11), and normalized logarithms to O(5^10). The computation uses the same PARI library; it is an independent extraction from A, not an independent modular-symbol implementation.

## Structural selection lemma
Let Abar_F=(H_scalar,F/5) mod5, Abar_A similarly, and ellbar_F=log(Q)/5 mod5, ellbar_A similarly. Assume these matrices/rows are integral, the differential scaling is1, and detM has valuation1. Then

    Mbar^t Abar_F Mbar=0,  ellbar_F Mbar=ellbar_A.

The image of Mbar is a line. If Abar_F has rank1, its isotropic vectors are exactly its radical: write the symmetric rank1 form as c l l^t. Hence imMbar=rad(Abar_F). If ellbar_A is nonzero, this line is not ker(ellbar_F). Thus height rank1 plus primitive A logarithm is a sufficient selection test for the seed17 distinct-line geometry. This is a linear-algebra consequence of the actual isogeny identities; it is not a nonvanishing theorem for L2.

At d329233 the actual data are Abar_F=[[4,2],[2,1]], ellbar_F=(1,3), ellbar_A=(0,0), M=[[-2,1],[-1,-2]]. The height radical, imMbar and logarithm kernel coincide, all spanned by (1,3). The criterion does not apply: its primitive A-log premise fails. This is a positive-excess/nonunit-regulator control but not the seed17 distinct-line configuration. Its residual representation remains reducible.

## Sources
The attached Pro check and a separate agent desk check retain canonical height functoriality, not arbitrary numerical pairings. Iovita--Werner, https://arxiv.org/pdf/math/0209362, Lemma2.1 discussion gives the unit-root functoriality; Besser--Mueller--Srinivasan, https://arxiv.org/pdf/2112.03873, Lemma4.31 gives pullback/tensor compatibility of canonical logarithms. Cassels isogeny-Selmer formula is in Miller--Stoll section6, https://www.mathe2.uni-bayreuth.de/stoll/papers/isogeny-descent.pdf. These are imported framework inputs, not an independent certification of this entire packet.

## Local index change in the new control
Since ell_A=ell_F M, detM=5, and adj(M) is integral, the contents satisfy w_F<=w_A<=w_F+1. The actual rows give w_F=0 and ell_A=0 mod5, hence w_A=1 exactly. Thus the isogeny moves one factor into the global point lattice's local logarithm index. This follows from the actual map and row computations; it is not a theorem linking the seed's Kato coefficient to that index. The regulator determinants remain equal on the named pairs even though these local point indices differ.
