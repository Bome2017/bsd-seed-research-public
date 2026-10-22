# A joint upper bound including unit, ideal-class and valuation directions

Written deduction and new application of unchanged saved arithmetic, October18,2026. This is not a new source computation or a new seed theorem.

## 1. Complete source and exact targets

Let p be odd and use the retained full-image torsion field A and faithful scalar character chi. All vector spaces are over F_p. Define

    V = A(S,p)^chi,
    H0 = A(empty,p)^chi = ker(valuation:V -> D_S/pD_S),
    U = (O_A^*/O_A^{*p})^chi,
    C = Cl(A)[p]^chi.

The Kummer/unit sequence is 0->U->H0->C->0. In the retained setting there are no p-power roots of unity and dim U=d=(p+1)/2. C is the ORDINARY class group contribution, not the S-class group. A field element initially represented through an S-unit can have nonzero ordinary class boundary after all valuations become divisible byp.

Let G:V->Z_G be authenticated necessary global equations (for example the actual incidence norm followed by residue functionals, or the retained scalar/additivity source equations), and L:V->Z_L the local Kummer quotient equations. Put R=(G,L). Every actual Selmer class lies in K=ker R. It is enough that these equations are necessary; G need not be a complete characterization of global cohomology. L must quotient by the full true local Kummer image, or by an independently verified larger allowance, to avoid incorrectly rejecting genuine classes.

The raw saved matrices include scalar equations rather than starting inside chi. Their ordinary unit dimension is4. Restricting to the scalar-minus kernel at p=3 gives the faithful unit dimension2 used in the formulas below. The checker verifies this restriction and the inherited exact unit/class filtration explicitly.

## 2. Quotient by all unit repairs before counting class directions

Set r_U=rank(R|U). Given c in C choose a lift beta in H0 and define

    delta_R(c) = [R(beta)] in (Z_G direct_sum Z_L)/R(U).

Changing beta by a unit changes R(beta) by R(U); hence delta_R is well-defined. A lift can be repaired by a unit to satisfy R precisely when delta_R(c)=0. Consequently

    0 -> ker(R|U) -> ker(R|H0) -> ker delta_R -> 0,

and, writing c=dim C and r_C=rank delta_R,

    dim ker(R|H0) = (d-r_U)+(c-r_C).                 (1)

This counts the complete allowed class image after every permissible unit repair. It does not require C=0 or require the ideal-class norm itself to be injective.

Put q=dim valuation(K). The valuation sequence then gives

    dim K = (d-r_U)+(c-r_C)+q.                       (2)

Every term is exact for the complete screened source and chosen necessary maps. If only upper bounds on c and q and lower bounds on the two ranks are supplied, the corresponding one-sided version remains an upper bound when those bounds apply to the entire source. A matrix on an uncertified subgroup does not make (2) a bound for undiscovered arithmetic classes.

If the actual norm is imposed, q is bounded by the primitive divisor norm-kernel dimension t_D. For a weaker finite global screen, its computed q can exceed t_D. The true Selmer space is still bounded using the smaller of t_D and the screened q, since true classes satisfy both conditions. This distinction avoids assuming a finite residue screen is the full norm map.

For a rank-two curve, upper bound2 implies Sha[p]=0 directly. Upper bound3 needs the separately retained parity theorem on its domain. No primary finiteness is assumed in the direct bound2 implication.

## 3. Why the norm rank alone need not grow

The previous sufficient estimate used the global norm's unit rejection rank and then charged the class and divisor terms separately. Equation(2) uses the rank of the STACKED global/local map on units, and subtracts the induced class obstruction after compatible unit repairs.

Thus the useful inequality is

    r_U+r_C >= d+c+q-2

for an upper bound2, or the analogous threshold with3 when parity is valid. This does not prove that any rank has the required growth. It shows that increasing norm rank is only one possible way to reach the threshold. Local equations and global/local compatibility can also contribute. Neither a fixed unit norm rank nor a nonzero ordinary class group alone rules out a small joint bound.

The ordinary ideal-class-kernel bound remains valid. If one first imposes the actual norm, the class space can be restricted to ker u_C. The subsequent connecting/compatibility obstruction may reduce this space further. Bounding ker u_C alone and dropping that obstruction is a coarser sufficient method, not the only admissible construction.

## 4. Separate repairability does not give simultaneous repairability

Let C_G and C_L be the class images of ker(G|H0) and ker(L|H0), and let K_G=ker(G|U), K_L=ker(L|U). For c in C_G intersect C_L, choose repairs u_G,u_L of a common lift. Their difference defines

    omega(c)=[u_G-u_L] in U/(K_G+K_L).

It is independent of repair and lift choices. Its kernel is exactly the class image of ker R. Hence

    dim admitted class image
      = dim(C_G intersect C_L)-rank omega.           (3)

This is the previously reviewed compatibility mechanism. Its actual nonzero mirror389 example is an old input recovered here; we do not claim to have discovered it in this run.

## 5. Results on complete saved sources

The new checker reads the raw valuation, source, unit, scalar, additivity and local matrices. It ignores the producer's saved coupling matrices and Sha conclusions. It computes the upper bound first, then reads the point columns for comparison. It independently enumerates every unramified source element after reducing the constraint rows, including all ordinary class fibers. No new BNF or local point producer is run.

| Data | faithful unit/class dimensions | global-only unit/class/valuation | joint unit/class/valuation | whole joint upper |
|---|---|---|---|---|
| Six rank-two controls below | 2 / 1 | 1 / 1 / 0 | 1 / 1 / 0 | 2 |
| 1070a1,1480a1 | 2 / 1 | 1 / 1 / 1 | 1 / 1 / 0 | 2 |
| mirror389 | 2 / 1 | 0 / 1 / 2 | 0 / 0 / 0 | 0 |
| seed at3 | 2 / 2 | 2 / 2 / 0 | 2 / 2 / 0 | 4 |

The six in the first row are718b1,997c1,1141a1,1246c1,1525c1,1613a1. There are eight rank-two controls total, not nine. The additional mirror is a different curve of rank0, and the seed is a separate positive-excess case.

For mirror389, the ordinary class group C3 and S-class group C3 are certified in the retained record. The ordinary source norm bound from the earlier incidence calculation is3: ordinary unit contribution0, ordinary class-kernel contribution1, and primitive divisor allowance2. The complete joint matrix gives0. It removes the class direction through incompatible repairs and the two valuation directions through local admission. This is a whole-source bound under the retained completeness/necessary-map/local-image inputs. It does not claim all finite global rows suffice to recognize cohomology: a zero containing space already suffices for exclusion.

On H0, the previously authenticated mirror relation is

    class_boundary = scalar_row + additivity_at127
                       + additivity_at151 + 2*local3_row.

It vanishes on all units but evaluates to1 on the class lift. The raw local defect modulo all units is separately zero; the obstruction appears only when the same unit correction must satisfy both global and local conditions. The saved arithmetic attribution is in the prior ARITHMETIC_ROW_MAP.md; it is retained, not freshly recomputed here.

The eight rank-two controls have one admitted unit direction and one admitted class direction, both occupied by the two point classes. They already give upper2 without killing the class group. The seed3 has two admitted unit directions and two admitted class directions; its point plane occupies one of each, leaving upper excess2. The seed3 full class-source completeness remains GRH-dependent. This is exactly the existing result, not a new seed-primary conclusion.

## 6. What the recovered work changes

The old arithmetic already demonstrates that global/local compatibility can bound the complete class contribution more tightly than the standalone ideal-class kernel, and that nonzero admitted classes can be harmless when occupied by rational points. The current recomputation restores these facts to the scaling target.

It does NOT demonstrate growth of joint rank at p>=5, a small seed bound at a new prime, or a cofinite estimate. The complete-source arithmetic needed to compute these ranks and class maps at larger p is still not supplied by these controls. FIN, ORDER9 and Q36 are unchanged.
