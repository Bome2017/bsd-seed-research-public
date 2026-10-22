# The 167 component factor is a unit under the retained first-raised comparison

Date: 2026-10-11. Grade: written deduction under the retained first-raised C3 theorem and its model admission; fresh exact PARI controls. This is not an independently formalized theorem or an evaluation of a CM point.

## Result

Let J be the Jacobian of the Shimura curve of discriminant 501 and Eichler level 847, and let g be the newform of

    E1 : [a1,a2,a3,a4,a6] = [1,1,1,1878418,-485198548].

Use the Picard Hecke action throughout. Let pi:J -> E1 be the optimal elliptic quotient attached to g, transported by a rational isomorphism to this displayed model. Let I be the exact mod-5 level-raised ideal from the base E=[1,1,1,3,12], with U167=+1. Retain the admitted first-raised assertions

    V_J := T_5(J)/I ~= E[5],
    alpha_J : Phi_J/I -> H1_sing(K_167,V_J) is an isomorphism,

where K=Q(sqrt(-19)); thus K_167/Q_167 is unramified quadratic. These are the C3 inputs, not consequences of optimality alone. For this particular model their base Hecke freeness hypothesis must be certified at 5, as explicitly required by the C3 note.

Choose the canonical source generator phi_J from the primitive base eigenfunctional and its component normalization. Choose a generator phi_1 of the elliptic singular Kummer line from a generator of Phi_E1=Z/5. Define k by the actual map:

    pi_5(phi_J) = k phi_1.

Then

    k is in F_5^times.

No value of k in {1,2,3,4} is asserted. The proof removes possible loss of a factor of 5 at this component transport; it does not choose a normalization or compute the CM source index n.

## 1. The elliptic quotient and displayed model

The retained full modular congruence admits g as a rational newform of conductor 424347=3*7*11^2*167. Its local types at 3 and 167 are discrete series, so the retained Jacquet–Langlands occurrence places its elliptic factor in J. The quotient by the connected g-complement is an optimal quotient pi_0:J -> Eopt in the rational isogeny class of E1.

A fresh exact call to PARI's `ellisomat(E1,0,1)` returns

    [[[90164063/48,-419887775791/864]], Mat(1)].

This is a singleton rational isogeny class. The two displayed short coefficients are the standard rational short model of E1. Thus Eopt is Q-isomorphic to E1, and the actual optimal quotient may be transported to the displayed model without a nontrivial isogeny. The two signs of this isomorphism change both k and the CM coefficient n by the same sign.

This computational input is stronger than is needed at 5. There is a separate proof that does not require computing the whole rational isogeny class. For any rational elliptic curve Eopt isogenous to E1, take a minimal-degree rational isogeny u:E1 -> Eopt. If 5 divides deg(u), the nonzero subgroup ker(u)[5] is a Galois-stable subspace of E1[5]. Residual irreducibility makes it all of E1[5]. The isogeny then factors through [5]:E1 -> E1, producing a rational isogeny of degree deg(u)/25 and contradicting minimality. Hence deg(u) is prime to 5. Its dual Eopt -> E1 induces an isomorphism on 5-torsion and on 5-primary component groups. This proves the required prime-to-5 transport without inferring it merely from membership in an isogeny class.

In the sequel the singleton calculation lets us use an optimal map to the specified E1 itself.

## 2. Optimality gives the exact residual Tate-module map

Let B=ker(pi). Connected-kernel optimality means B is an abelian variety. In characteristic zero multiplication by 5 on B is surjective over the algebraic closure. Applying the snake lemma to

    0 -> B -> J -> E1 -> 0

and multiplication by 5 gives an exact sequence

    0 -> B[5] -> J[5] -> E1[5] -> 0.

Equivalently, T_5(J) -> T_5(E1) is surjective. No claim about component groups is made at this step.

The quotient is taken for the actual Picard g-character. Its character modulo 5 is exactly the character defining I: the complete Sturm comparison includes coefficients at the bad operators, and U167 acts as +1. The comparison is not just equality of traces away from the level. Therefore the composite

    T_5(J) -> T_5(E1) -> E1[5]

annihilates I*T_5(J), and induces a surjection

    bar_pi : V_J -> E1[5].

The retained C3 statement makes V_J two-dimensional over F_5. The target also has dimension two. Thus bar_pi is a G_Q-equivariant isomorphism.

The Picard/Albanese convention is material here. BD §5.4 conjugates the two Hecke actions by the indicated Atkin–Lehner involution. On the multiplicity-one rational g-line this involution acts by a scalar sign, so the two actions have the same g-character; nevertheless pi and I above are both defined using the Picard action. No identification of the actions on the entire Jacobian or graph lattice is being made.

## 3. The elliptic component map is explicitly a singular Kummer isomorphism

The independent local control returns

    elllocalred(E1,167) = [1,9,[1,0,0,0],5],
    a_167(E1)=1,
    v_167(Delta(E1))=5.

The code 9 is Kodaira I5. The sign a_167=1 makes it split multiplicative already over Q_167. Its Tate parameter q_E has valuation 5. Over F=K_167, write E1(F)=F^times/q_E^Z.

The component map is the valuation modulo 5. A component generator is represented by an element u of valuation one. Choose a fifth root of u. Its Kummer cocycle on tame inertia is a generator of the toric mu_5 line. This cocycle is nonzero: the extension adjoining a fifth root of a uniformizer is tamely ramified of degree five. The residue field has order 167^2, and 167^2 is 4 modulo 5, so 5 does not divide 167^2-1. Consequently the fifth-power map on residue-field units, and hence on O_F^times, is bijective. Unit representatives contribute no singular class.

Also E1[5] is unramified at 167. A fifth root of q_E is a uniformizer times a fifth root of a unit; the latter is unramified, and the toric roots of unity are unramified. Its two Frobenius characters are 167^2 and 1 modulo 5, which are distinct. The singular local cohomology line has dimension one. Hence the component Kummer map is an isomorphism

    alpha_1 : Phi_E1/5 = F_5 -> H1_sing(F,E1[5]).

This does not identify a rational Mordell–Weil point with a component generator. Indeed the previously computed rational generator Y=(480,22723) reduces to a smooth point and has zero component class. The local uniformizer source and global CM-point source remain distinct.

## 4. Naturality proves k is nonzero

The quotient pi extends to the Neron models. Specialization to components and Kummer maps are functorial. Thus the following square commutes:

    Phi_J/I          -- alpha_J --> H1_sing(F,V_J)
       | pi_Phi                         | H1_sing(bar_pi)
       v                                v
    Phi_E1/5         -- alpha_1 --> H1_sing(F,E1[5]).

The left vertical map is well defined because pi is Hecke equivariant and I acts trivially on the target modulo 5. The top horizontal map is the retained natural C3 isomorphism, not an arbitrary identification of cyclic groups. The lower map is the Tate-curve isomorphism proved in §3. The right map is an isomorphism by §2. Therefore pi_Phi is an isomorphism. In coordinates, k is nonzero modulo 5.

This proof uses all three interfaces: connected-kernel optimality, residual rank two for the specified Hecke quotient, and the natural component/Kummer isomorphism. Optimality alone does not imply component surjectivity. Known counterexamples for toric Jacobians therefore do not conflict with this deduction. No claim of surjectivity on the full integral component group is needed, only on this residual eigenspace.

## 5. Exact consequence for the still-unknown CM index

Let D_CM be the actual corrected degree-zero CM divisor class prescribed by the construction. Since the retained rank calculation gives rank E1(K)=1, Y is not 5-divisible over K, and E1(K)[5]=0, there is a unique n in F_5 such that

    kappa_E1(pi(D_CM)) = n kappa_E1(Y).

The sealed global torsor comparison proves

    kappa_E1(Y)=f_* kappa_E(2P1+P2)

for its fixed explicit f:E[5] -> E1[5]. That comparison does not compute n.

The normalized common-source tensor is therefore (n/k) times the already evaluated Y-instrument. The latter is 1 for the sealed 167 normalization. Now k is a unit under the inputs above, so

    normalized CM detector is nonzero  <=>  n != 0.

There is no additional unknown vanishing contribution from the component map. This is a simplification of the actual source problem on the control model. It is not a computation of the normalized scalar, and it does not prove that n is nonzero. The source may still be divisible by 5 in E1(K).

In particular neither Y nor its nonzero Kummer class may be substituted for the CM image. The modular/CM index remains visible. FIN, ORDER9 and Q36 for the seed have not changed.

## 6. Source custody and executable boundary

Fresh primary sources read:

- Bertolini–Darmon, *Iwasawa's Main Conjecture for elliptic curves over anticyclotomic Zp-extensions*, Annals 162 (2005), §5.4, Theorems 5.15 and 5.17, the remarks after 5.17, and Corollary 5.18. URL: https://www.math.mcgill.ca/darmon/pub/Articles/Research/27.Main-conjecture/pub27.pdf . These supply the retained Hecke and natural component framework. The bottom-level transport without an ordinary coefficient-prime level remains the explicit retained C3 deduction, not a silent extension of the main theorem.
- Conrad–Stein, *Component Groups of Purely Toric Quotients*, §3, Definition 3.1 and proof of Proposition 3.3. URL: https://www.wstein.org/papers/compgrp/compgrp/node5.html . The torsion exactness in §2 is also proved above.
- Papikian–Rabinoff, *Optimal quotients of Jacobians with toric reduction and component groups*, introduction, §3.10–3.24 and §4.3. URL: https://arxiv.org/pdf/1212.3574 . This was read as a scope control: optimality alone does not justify the conclusion, and squarefree-level applications there do not cover 847.
- PARI official elliptic-curve manual, `ellisomat` and `elllocalred`: https://pari.math.u-bordeaux.fr/dochtml/html-stable/Elliptic_curves.html . The exact commands and raw output are retained here.

Retained project inputs read:

- `BSD_OPENAI_CM_COMPARISON_PUSH_CODEX_2026-10-11/notes/C3_ASSEMBLY.md` and `C3_REVIEW.md`.
- `BSD_COMPARISON_EXPERIMENT_CODEX_2026-10-11/admission/ADMISSION.md`.
- Its `torsors/RESULT.md`, `geometry/GLOBAL_TORSOR_REVIEW.md`, and `geometry/MIXED_PLACE_DIAGRAM.md`.

The exact control script does not construct J or the quotient map. It computes the rational elliptic isogeny class and local reduction of the displayed model. The C3 input at coefficient 5 is kept separate from that computation. The next source computation is n, or the actual CM image modulo 5; refining k's nonzero residue is required only for an exact scalar comparison, not for deciding nonvanishing.
