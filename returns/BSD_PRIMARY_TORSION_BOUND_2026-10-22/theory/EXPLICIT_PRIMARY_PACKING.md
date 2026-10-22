# An explicit bound on relative five-torsion, with norm-unit errors retained

Written derivation under the retained exact field and analytic inputs. This is a direct bound on unseen p-torsion classes, not a relation rank on a selected list. On the tested seed it is weaker than the previously retained bound. No FIN, ORDER9, or Q36 conclusion follows.

Use the actual seed point field A of degree 24, K=A^{<tau>} of degree 12, signatures (4,10) and (4,4), and

    delta = N(d_A/K) = 707033045140895852346320.

Write C=ker(Cl(A)->Cl(K)) and h=|C|=h_A/h_K. The equality is retained from the preceding finite-ramification/norm-surjectivity proof. The earlier exact analytic inputs imply

    h (R_A/R_K) <= C_an < 42 * 10^71.

This last inequality follows afresh from the saved exact upper bounds for sqrt(D_A/D_K), the Hecke L-value, and the lower bound for pi; it does not multiply an upper class-number bound by a lower regulator bound.

## 1. A norm-one ideal group whose odd-primary part is the actual target

Let I^1 be the group of fractional A-ideals with ideal norm exactly O_K, and let P^1 be the subgroup {(alpha): alpha in A^*, N_A/K(alpha)=1}. Put C^1=I^1/P^1. Its natural map to C has image J.

The cokernel C/J is killed by 2: if a represents c in C and N(a)=(b), then a^2/(b) has norm one and represents 2c. The kernel is naturally

    (U_K intersect N_A/K(A^*)) / N_A/K(U_A).

Indeed, a principal ideal in I^1 has a generator whose norm is a K-unit; changing the generator changes this unit by the norm of an A-unit. Conversely, such an element norm gives a principal norm-one ideal. Squares of K-units are norms of A-units, so this kernel is also killed by 2. Neither assertion means the error group has order at most 2. It can have several independent two-torsion directions.

Both errors are finite, hence C^1 is finite, and for any odd p the induced map on p-primary groups is an isomorphism. In particular

    |C^1[5]| = |C[5]|.

No assumption about a computed ideal generating set enters this equality.

## 2. A compact relative divisor group and an explicit volume bound

Let E=ker(N:U_A->U_K), and use the all-embedding logarithm metric from the previous packet: a real place contributes one coordinate log|rho(u)|; a complex place contributes two equal coordinates. Let V be the six-dimensional anti-invariant real logarithm space, with Euclidean measure, and let V_E denote the covolume of Log(E).

Let I=[U_A:U_K E]. The previous metric calculation gives exactly

    R_A/R_K = 64 V_E/I,
    I = [N(U_A):U_K^2].

Since U_K has rank 7 and roots of unity {+1,-1},

    [U_K:N(U_A)] = 2^8/I.

Thus |ker(C^1->J)| <= 2^8/I, and

    |C^1| V_E <= h * (2^8/I) * V_E = 4 h (R_A/R_K).   (1)

This conservative factor four retains the entire norm-unit error. Additional sign information could improve it, but is not needed or silently used here.

Form the compact abelian group

    G = (I^1 x V) / {((alpha),Log(alpha)):N(alpha)=1}.

The identity component is V/Log(E); the component group is C^1. Hence its volume is |C^1|V_E. Multiplication by p is onto the identity component, so

    [G:pG] = |C^1/pC^1| = |C[p]|,
    vol(pG) = vol(G)/|C[p]|.                            (2)

Here pG is a finite-index compact subgroup, not a set of collected ideal rows.

## 3. Prime-pair balls and the fractional discriminant inequality

Take M distinct pairs (P_i,tau P_i) of unramified primes of A above distinct primes of K, with common norm n_i<=X. Set b_i=P_i/(tau P_i). All b_i belong to I^1. Let g_i be represented in G by (b_i,0). The centers p g_i belong to pG. Every ball of radius R in the identity component also belongs to pG.

The retained unit-lattice minimum is greater than 8.55. Hence for R<1 each ball injects into the identity torus. Suppose the radius-R balls at p g_i and p g_j overlap for i!=j. Then there is alpha of element norm one with

    (alpha)=(b_i/b_j)^p,
    ||Log(alpha)||_2 <= 2R.

Its denominator ideal has norm at most (n_i n_j)^p<=X^(2p). The valuations at P_i and tau P_i are opposite and nonzero, so alpha is not in K and generates A/K.

For completeness, the fractional version of the discriminant inequality is important here. Let J_alpha=O_A+alpha O_A. The rank-two O_K-lattice O_K+alpha O_K is contained in J_alpha, so comparison of their discriminants gives

    delta * N_A/Q(J_alpha)^2 <= |N_K/Q((alpha-tau alpha)^2)|.

As N(J_alpha) is the inverse norm of the denominator ideal, this is

    delta <= N(den alpha)^2 * |N_K/Q((alpha-alpha^{-1})^2)|.  (3)

It is not an inequality that treats alpha as an integral unit.

There are two split real places of K, two real places becoming complex, and four complex places. At a split real place put x=log|alpha|; the contribution is (2sinh x)^2. At a ramified real place |alpha|=1, so the contribution is at most 4. At each complex place the contribution is at most (2cosh x)^4. The all-embedding norm bound gives |x|<=sqrt(2)R at the split real places and |x|<=R at the complex places. Consequently (3) implies

    delta <= X^(4p) 2^24 sinh(sqrt(2)R)^4 cosh(R)^16.     (4)

Therefore the strict reverse inequality makes all M balls disjoint. This retains the real sinh factors; replacing them by exp bounds would give no positive radius for the two norm-seven pairs at this discriminant.

The Euclidean six-ball has volume pi^3 R^6/6. From (1), (2), and these disjoint balls,

    |C[p]| <= 4 C_an / (M * (pi^3/6) * R^6).             (5)

This is an explicit primary-torsion bound. It bounds the sum of the two faithful five-torsion dimensions because their sum is the scalar-minus-one part at p=5. It does NOT bound total p-primary length: a finite group killed by p^a may have much larger length than its p-torsion rank.

## 4. Actual seed calculation

The arithmetic lane authenticated 26 disjoint tau-pairs with norms at most 242, grouped at 13 rational primes. For each of the 13 prefixes, the checker chooses a common radius by exact rational bisection, verifies (4) in the disjoint direction, and applies (5). The binary search supplies a lower radius; it does not assume a floating root.

The best of these tested common-radius prefixes consists of the two norm-seven pairs. It admits

    R = 6889807/16777216,

and gives the exact safe integer upper bound

    |C[5]| <= 334809554342956104676612913920139327331389754537007507521626340458250851040
             < 5^107.

Thus this new direct packing calculation gives rank at most 106. The already retained whole-order argument gives the stronger rank bound 97, so 97 remains the operative bound. Later prefixes have larger discriminant denominator costs and give rank bounds 131 through 168 in this common-radius construction.

The numerical acceptance uses positive rational Taylor series with explicit geometric tail bounds for cosh, retained rational outward pi and L-value bounds, and integer comparisons with powers of 5. No class number, class dimension, Selmer value, or Sha value is fed to the test.

## 5. Scope of the failure

This tests a genuinely p-primary mechanism: it constructs volume inside pG and bounds G/pG. It does not move class directions into new ideal columns. But the measured p-image volume is far too small compared with the complete analytic volume budget. Counting more prime pairs in the tested range does not overcome their cost in the separation radius.

Only the stated 13 common-radius prefixes and this separation inequality were tested. No conclusion is drawn that every Arakelov packing, character-specific bound, or arithmetic class-control construction fails. Nonuniform packings, sharper arithmetic separation, or much stronger source-specific analytic volume estimates would require additional work and are not claimed here.

The p=5 outcome is not a scaling theorem. As p varies, both the relative logarithm dimension (p^2-1)/4 and the exponent 4p in the finite-denominator cost vary. The published relative torsion estimate has constants depending on the field degree; no cross-prime smallness can be obtained by treating those constants as fixed. The arithmetic lane separately records the admitted norm ranges and their limitations.
