# C3 repair: uniform hypotheses and finite-modulus assembly

2026-10-11. Grade: written deduction under the retained modularity, rational multiplicity-one and full residual-image inputs. Not independently reviewed or formally verified. No seed coefficient or class group is computed.

## Outcome

The stated reason for `CONSTRUCTION_BLOCKED_AT_C3` is too strong. A theorem proved for each arbitrary coefficient prime can be applied at every prime satisfying one uniformly stated set of hypotheses. Its being proved locally at each prime is not an obstruction to assembling the natural maps over a finite ring `Z/m`.

Here the first level-raising multiplicity-one argument in BD Theorem 5.17 needs no new denominator or exceptional set depending on the raised prime. After isolating the fixed base eigensystem outside a single fixed integer, the argument applies to every admissible raised prime and every admitted prime-power modulus. Chinese remaindering then gives the exact finite-modulus Hom-line construction already proposed in C6. No characteristic-zero level-raised eigenform or rational level-raised idempotent is required.

This repairs C3 as a finite-modulus construction checkpoint. It does **not** show that the resulting contents at varying auxiliary levels are reductions of one rational number. It does not repair C4's additional surjectivity/second-law interface, C8's evaluation, or any higher-depth multiplicity-one assertion. It gives no nonvanishing or Sha bound.

## 1. Source inspected and exact boundary

Primary source: Bertolini–Darmon, *Iwasawa's Main Conjecture for elliptic curves over anticyclotomic Zp-extensions*, Annals 162 (2005), [published PDF](https://www.math.mcgill.ca/darmon/pub/Articles/Research/27.Main-conjecture/pub27.pdf).

I freshly opened the published PDF text and read the preserved September 2007 preprint text around Propositions 5.8–5.14, Theorems 5.15 and 5.17, Lemma 5.16, and Corollary 5.18, including both steps of the multiplicity-one proof. Preprint printed pages 58–64 have different numbers from the published paper. I did not reprove Boston–Lenstra–Ribet's theorem.

The published introduction imposes ordinary reduction and a p-level for the anticyclotomic Iwasawa construction. This note does **not** import that main theorem for supersingular p. It reads the finite geometric proof in Section 5: the graph and monodromy statements concern arbitrary Eichler levels; 5.15 uses residual irreducibility, base character-group freeness and admissibility; 5.17 additionally uses the stated full residual image. No ordinary filtration, unit root, anticyclotomic limit, or p-level degeneracy map occurs in those finite proofs.

Removing the p-level therefore requires this finite-proof transport, not a claim that the original main theorem has broader hypotheses. That transport was already asserted in C1/C3 of the retained construction. The explicit argument below records what is needed and why its exceptions can be fixed before choosing coefficient or auxiliary primes. Section 9's surjectivity argument is different and is not transported here.

## 2. A fixed base Hecke denominator that actually supplies the hypothesis

Fix the definite Brandt module (or the corresponding base character group) `M`, its faithful integral Hecke algebra `T`, and the rational eigensystem of E. Retain rational multiplicity one. Work in the cuspidal summand, or remove the Eisenstein degree component at the non-Eisenstein localization.

The argument needs an idempotent **in the rational Hecke algebra**, not only an integral projector in `End(M)`. One explicit way to get a fixed denominator is as follows.

Choose finitely many Hecke operators separating the rational E-eigensystem from the other characteristic-zero eigensystems. A suitable integral linear combination `h` of these operators has eigenvalue `a=f(h)` on the E-line and has no eigenvalue a on any other eigensystem. Such a combination exists: there are finitely many eigensystems and each unwanted equality defines a proper rational linear condition on the integral coefficients. It can be found by finite search with exact characteristic polynomials; no efficiency is asserted.

Write the characteristic polynomial of h on `M_Q` as

    det(X-h)=(X-a)Q(X),     Q in Z[X],     J=Q(a) != 0.

The multiplicity-one hypothesis makes the displayed `(X-a)` factor simple. The complementary characteristic polynomial annihilates the complementary summand. Consequently

    e=Q(h)/J in T[1/J]

is the E-idempotent. It gives

    T[1/J]=Z[1/J]e x (1-e)T[1/J],
    eM[1/J] is free of rank one over Z[1/J].

The first identity uses that the Hecke action on the rational E-line is scalar with integral eigenvalues and that `e` belongs to the localized Hecke algebra. Thus, for every p not dividing J, the completion of the base Hecke algebra at the residual E-character is `Z_p`, and the base character group there is free of rank one. This proves the actual freeness hypothesis of BD 5.15(2), rather than inferring it from torsion-freeness of a quotient.

The argument is also compatible with the earlier base-idempotent repair in the October 7 review. Its finite-support conclusion requires no numerical value for J. Conversely it certifies no particular small prime as outside J unless J or a more precise local isolation certificate is computed. J is a construction denominator; it is **not** a Sha annihilator or a bound on a leading term.

If one uses the whole Brandt module instead of the exact base character group in this construction, the fixed identification and primitive eigenfunctional indices must also be inverted. They depend only on the fixed base module, not on the later auxiliary primes. Alternatively construct h directly on the character group occurring in BD 5.15 and include those indices in J by definition.

## 3. Uniform domain before level raising

Fix K and the factorization `N=N+ N-` with N- squarefree and of odd prime parity as in C0. Let S contain the primes dividing

    6 N disc(K) J,

the finite residual-image exceptions, and any fixed denominators in the retained model/Hecke-module identifications. One may conservatively add the fixed modular degree and the primes dividing `q+1` for squared bad-level primes q if carrying all introduction-level assumptions of BD rather than only the hypotheses actually used in Section 5. These additions are fixed and finite. For the seed the full residual-image assertion is a retained input, not newly recertified here.

For every p outside S, every n>=1, and every prime ell satisfying

    ell inert in K, ell not dividing Np,
    p not dividing ell^2-1,
    a_ell = epsilon(ell+1) mod p^n,

the base hypotheses of 5.15 hold. Theorem 5.15 constructs the character of the raised Hecke algebra and proves

    Phi_ell/I_(p,n) ~= Z/p^n.

Theorem 5.17 then gives

    T_p(J_ell)/I_(p,n) ~= E[p^n]

as Galois modules. The statement is existential as to the last isomorphism. That is sufficient for the Hom-line method.

Here is why the raised level introduces no further unrecorded multiplicity-one exception in this argument. Step 1 of 5.17 uses the toric uniformization exact sequence, the Boston–Lenstra–Ribet isotypy statement, and the already proved one-dimensional component quotient. If the residual Tate quotient were k copies of E[p], its singular local cohomology would have dimension k. The component quotient surjects onto that singular part and has dimension one, forcing k=1. Step 2 uses Lemma 5.16's exponent p^n, residual irreducibility/full image, and Nakayama to obtain a rank-two free quotient at p^n. Corollary 5.18 identifies the natural component-to-singular Kummer map as an isomorphism.

No factor whose prime support varies with ell is inverted in this proof. Admissibility imposes the visible condition that `ell^2-1` is a p-unit; the level-raising congruence is supposed to be divisible by p^n. Those conditions are the input, not a hidden new output denominator.

The conclusion concerns the **first raised quotient from the fixed base**. Iterating the argument at additional raised levels would require a new verification of the base freeness hypothesis at those stages. It is not obtained by pretending the original fixed idempotent survives all level raising.

## 4. Exact finite-m assembly

Fix a positive finite modulus

    m=product p^n_p,       R=Z/m,

with all p outside S, and a single auxiliary ell satisfying the stated conditions at each p^n_p. Use the same bottom-level curve J_ell for every factor. Let `f_(p,n_p):T_ell -> Z/p^n_p` be the characters from Section 3 and define

    f_m=(f_(p,n_p))_p : T_ell -> product Z/p^n_p ~= R,
    I_m=intersection I_(p,n_p).

The map is onto: integer scalar operators already map onto R. The ideals are pairwise comaximal because they contain the distinct prime powers. Hence CRT gives

    Phi_ell/I_m ~= product_p Phi_ell/I_(p,n_p) ~= R,
    V_m := product_p (T_p J_ell/I_(p,n_p)).

The second module is an R[G_Q]-module and is noncanonically isomorphic to E[m]. Define, without making an isomorphism choice,

    H_m=Hom_(R[G_Q])(E[m],V_m).

Full residual image implies `End_G(E[p^n])=Z/p^n`. For completeness: reduce an endomorphism modulo p, where it is scalar; subtract that scalar and divide the matrix entries by p; repeat the centralizer argument modulo successively smaller powers. Consequently H_m is an invertible R-module and evaluation is a canonical isomorphism

    H_m tensor_R E[m] -> V_m.

Although every invertible module over this finite product of local rings is free, no basis of H_m is selected.

The natural geometric map assembles to the isomorphism

    alpha_m: Phi_ell/I_m -> H^1_sing(K_ell,V_m).

This is not obtained by choosing unrelated scalar normalizations at the different p's: start with geometric Kummer and specialization maps on the one curve and apply the quotient functor. The prime-power theorems prove that this already-defined map is an isomorphism at each factor. CRT proves it is an isomorphism over R. Cohomology, the finite/singular decomposition and cup products commute with finite products.

This is the required C3 finite-modulus object. A rational idempotent on the raised Jacobian is neither supplied nor needed.

## 5. Tensor normalization and compatibility

For a second auxiliary prime ell2, let F_i denote the rank-one finite local cohomology of E[m] at ell_i. Under the retained local duality convention,

    alpha_m: Phi -> H_m tensor F_1^dual

gives a canonical identification `H_m ~= Phi tensor F_1`. Thus the geometrically defined finite localization beta_m of the CM class maps canonically into

    Xi_m(beta_m) in Phi tensor F_1 tensor F_2.

If the actual two-point determinant R_P generates `F_1 tensor F_2`, there is a unique

    C_m in Phi,       Xi_m(beta_m)=C_m tensor R_P.

No Sha-vanishing premise enters this construction. A primitive fixed base eigenfunctional supplies the component coordinate `Phi ~= R` through the retained C2/component formula, subject to its orientation convention. Changing a temporary identification of V_m with E[m] multiplies both local comparison coordinates by the same unit and cancels from C_m.

If m' divides m and the same two auxiliary primes and same geometric CM input are retained, all quotient characters are reductions of f_m. The toric Kummer map, finite Kummer map, local duality, and point localizations commute with these reductions. The finite/singular local modules are free rank one in this admissible setting, so there is no base-change defect here. Uniqueness then gives

    C_m mod m' = C_m'.

This is actual finite-level compatibility. It concerns one fixed geometric pair wherever both coefficient levels are admissible.

## 6. Why this does not yet produce the global scalar

There are two distinct assertions:

1. For every admissible finite modulus and geometric pair, natural maps define a basis-independent C_m, compatibly under coefficient reduction for that pair.
2. One rational number c has reduction C_m for every varying admissible pair and modulus, with one fixed normalization.

Section 4 proves the first. It does not prove the second. CRT is a statement about a finite product of coefficient rings, not a cross-level arithmetic identity.

In fact, for a fixed positive-sign pair, admissibility requires

    m divides gcd(ell1+1-a_ell1, ell2+1-a_ell2).

Both integers are positive by their interpretation as finite-field point counts. Thus one fixed pair only sees a bounded finite set of coefficient powers. A projective limit over all p and n necessarily changes auxiliary levels; no transition maps between those distinct Jacobians or their normalized CM classes have been constructed in the preceding CRT argument.

Even an arbitrary compatible family in the full profinite completion of Z need not lie in the diagonal image of Q. The missing comparison cannot be replaced by choosing compatible residue representatives.

The known rational-point determinant R_P is a valid denominator on a detecting pair. It does not force beta_m to have a prescribed nonzero scalar. Establishing that scalar, its cross-prime support, or an adequate uniform valuation bound remains an arithmetic task.

## 7. Exact change to the working state

Recommended scoped revision:

    OLD: multiplicity one is only per p, therefore finite-m C3 construction is blocked.
    NEW: the fixed-base denominator and the finite Section 5 proof give
         C3 uniformly on its stated admissible domain; the natural maps
         assemble over Z/m. Written derivation, pending independent review.

Retain separately:

- The chosen seed primes have not individually been proved outside the uncomputed fixed base denominator.
- Second-law normalization/surjectivity at the p-free bottom level is not proved by C3.
- The orientation argument in C7 is retained, not independently recertified here.
- Higher-depth multiplicity one and a full compatible Euler system are separate from the first raised quotient.
- No exact common rational residue, nonvanishing theorem, cofinite content bound, FIN, ORDER9, or Q36 result is obtained.

The repaired construction is useful for the current comparison attempt because it removes an unnecessary demand for a characteristic-zero raised eigensystem before writing the finite arithmetic map. It should not be advertised as control of that map's value.

## Input bindings

- `BSD_EXACT_BD_CONSTANT_2026-10-07/construction/CONSTRUCTION.md`: SHA256 `af11a1abaf7086e871610afa756556485d92988c8c05cfca17f2c459b40461af`.
- Preserved `BSD_YUN_ZHANG_MECHANISM_READING_2026-10-07/sources/BD2005.txt`: SHA256 `7ece2d9174a761a561f98cab9f46767e7f5cc7fb93817f6fe9182b740bca7129`.
- October 7 `BSD_BD_INTEGRAL_REVIEW_CODEX_2026-10-07/MATHEMATICAL_REVIEW.md`: SHA256 `8b6aa4d15427a357f6f220a39899b78a129a9df4c134a997850cc46f108d2791`.

No historic input was edited. No large Shimura set, Selmer group, class group, or external research job was computed or launched.
