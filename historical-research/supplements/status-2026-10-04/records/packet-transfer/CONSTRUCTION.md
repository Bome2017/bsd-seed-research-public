# Three construction attempts for uniform seed vanishing

Status: **NO_NEW_UNIFORM_INPUT_FOR_THE_THREE_TESTED_CONSTRUCTIONS**.

There are two written auxiliary derivations below: a six-term marked-point identity and a crossed cyclic-p-squared transfer. The latter repairs a p-divisible self-trace by changing the actual correspondence. Neither has been shown to generate admissible witnesses. No novelty, independent review, or formal verification is asserted. No new seed primary component or BSD endpoint is settled.

## 0. The implication being attempted

The retained homology source is H = H_1(X_0(N), Z), with elliptic period functional z_E. Its image has index dividing two. The definite theta source is a different, retained integral model. We do not identify arbitrary vectors in these two sources, or transplant a local permutation action between them without a map.

The desired output is a fixed v with z_E(v) != 0 and, for every relevant p outside a fixed finite set, a formula for its period modulo p as a combination of *admissible* quadratic witness periods. Such a formula would force a unit witness outside the prime divisors of z_E(v), and would close cofinite primary vanishing on the demonstrated domain. The formula's existence is not an input.

The historical UC assertion is precisely an unproved generation/content target. Replacing its letters or reproving source primitivity is not a new result. The present work tries three actual operations in sequence.

## 1. Construction A: move the base point and retain branches

### 1.1 The initial operation

Start with the traced conductor-p^2 Gross packet v_j = psi(gamma^j P_1). Change the compatible sequence of CM points, and change the generator of its degree-p Galois group. These changes have affine indexing j -> a j + b, a != 0 modulo p.

For M_k = sum_j j^k v_j, the resulting weighted value, with weights (a j+b)^2, is

    M_2(a,b) = a^2 M_2 + 2ab M_1 + b^2 M_0.

On the retained rank-two, vanishing-lower-moment domain, this is a^2 M_2. Thus this operation transports a supplied value; it does not generate another value with independently controlled content.

This is also visible at source: BLV, Section 4.2, the paragraph after Lemma 4.2, says that changing the compatible system multiplies the square-root series by a group-like element. The first nonzero coefficient does not gain independent content that way. This disposes of the particular same-field/same-conductor base-point operation; it does not dispose of changing the arithmetic family itself.

### 1.2 Modification attempted: split an auxiliary-conductor trace

Instead retain the individual branches in a prime-to-p auxiliary extension F/K, with group Delta of order d prime to p. The trivial-character projector is the genuine integral operator

    e_0 = d^(-1) sum_{delta in Delta} delta.

In an abelian compositum where Delta commutes with the degree-p group, e_0 commutes with the quadratic weighting. Therefore the untwisted weighted image is exactly the average of the branch images, with no hidden p-denominator.

That does **not** let us pick one nonzero branch and use the untwisted descent theorem. The projector can kill nonzero branches: values 1 and -1 on a two-element fiber have zero trivial projection. This is a control of the proposed inference, not a seed example.

To make this modification useful we would need a new constraint on this projected combination, or an applicable descent theorem for the different object. No such constraint was obtained. We do not claim that all character-changing or conductor-changing methods fail. We also do not silently import B.5 for a new CM field or untraced point.

## 2. Construction B: a six-term projective transfer

The first operation could not escape affine changes. The second explicitly uses a non-affine transformation.

### 2.1 Integral marked module

For p >= 5 let M = Z[P^1(F_p)] with basis e_x, including e_infinity. Define permutations

    U(x) = x+1, U(infinity)=infinity;
    w(x) = -1/x, w(0)=infinity, w(infinity)=0.

Use the action U e_x = e_(U(x)), and similarly for w. With integer representatives 0,...,p-1 put

    W_2 = sum_{j=0}^{p-1} j^2 e_j,
    W_1 = sum_{j=0}^{p-1} j e_j,
    s = sum_{j=0}^{p-1} e_j,
    delta = e_0-e_infinity.

These are formal marked-point divisors. The symbol infinity has not yet been assigned an arithmetic CM point, cusp, or boundary class. Adding it cannot be treated as a free arithmetic operation.

When an integral degree-zero input is required, use W_hat_k = W_k - (sum_j j^k)e_infinity, for k=1,2. Both correction coefficients are divisible by p for p>=5. Thus W_hat_k and W_k agree modulo p. Since U fixes infinity, the differences (U-1)W_hat_1 and (U-1)^2 W_hat_2 equal the corresponding expressions for W_1 and W_2 exactly over Z. All identities below therefore have degree-zero integral lifts without invoking a theta denominator theorem for a vector of nonzero degree.

### 2.2 Exact integer identity

Direct coefficient calculation, including wraparound at 0 and 1, gives

    (U-1)^2 W_2 = 2s + p((p-2)e_1 - p e_0).

Indeed its coefficient at j >= 2 is (j-2)^2-2(j-1)^2+j^2 = 2; at 1 it is 2+p(p-2); at 0 it is 2-p^2. The infinity coefficient is zero.

Since s-ws = delta, we obtain the exact identity

    (1-w)(U-1)^2 W_2
      = (2-p^2) delta + p(p-2)(e_1-e_(-1)).             (B1)

In particular, modulo p,

    delta = (1/2)(1-w)(U-1)^2 W_2.                    (B2)

Expanding the right side uses six transformed quadratic-weight divisors, with coefficients 1,-2,1,-1,2,-1, followed by multiplication by 1/2. No factor p is inverted. Translating B2 gives every e_a-e_infinity; these form a basis for the augmentation-zero subspace. Thus the full projective orbit of W_2 generates that subspace modulo p.

This is an elementary local representation calculation, not an asserted new theorem in the literature.

### 2.3 The two-prime variant

There is also an exact first-weight identity

    (U-1) W_1 = -s+p e_0,
    (1-w)(U-1) W_1 = (p-1) delta.                     (B3)

Taking the external tensor product of two copies gives a sixteen-term identity expressing delta tensor delta through transformed mixed weights W_1 tensor W_1, divided by (p-1)^2, a p-unit. This matches the *formal weight shape* of a two-prime mixed coefficient. It is not a realization by two admissible Kato primes, and it does not identify discrete-log coordinates with modular cusp coordinates.

### 2.4 Arithmetic test

B2 would be useful if the six transformed sums were actual admissible packets, their infinity terms had a justified arithmetic meaning, and their resulting point differences generated a fixed vector with nonzero elliptic period.

The actual degree-p CM Galois orbit is a C_p-torsor. Changing its origin and generator acts affinely. A bijection conjugating its regular translation group to itself has the form j -> a j+b: if F(j+1)=F(j)+a, iteration gives F(j)=F(0)+aj. In PGL_2(F_p), this affine subgroup fixes infinity; w does not. Thus w is not a change of the allowed Galois labels of that packet.

This pinpoints a missing *realization*, not a refutation of B2 or of every possible correspondence. A geometric construction could change conductor, level, or CM data and realize a different torus action. Its trace, descent implication, and infinity term would all need proof. We attempted a level-changing realization next.

## 3. Construction C: crossed degeneracy maps

### 3.1 The failed self-trace and the proposed repair

Let X=X_0(N) and Y=X_0(Np^2), with p not dividing N. The two extreme degeneracy maps are

    alpha(A,C_N,D) = (A,C_N),
    beta(A,C_N,D)  = (A/D,(C_N+D)/D),

where D is cyclic of order p^2. Each map has degree d=p(p+1). They extend over the cusps. Pullback and pushforward induce integral maps on Jacobians and hence on their integral homology lattices.

Using the same map both ways gives alpha_* alpha^* = d, divisible by p. Dividing this self-trace by p is not justified. The repair uses the other map for the return.

### 3.2 Derivation from cyclic isogeny paths

Let C_(p^2) be the correspondence summing cyclic p^2-isogenies. Compose two p-isogeny correspondences. For each first kernel of order p, exactly one second kernel is that of the dual isogeny. These p+1 paths compose to multiplication by p, which gives the identity point on X_0(N): multiplication by p preserves the level-N subgroup because p is prime to N.

Every other path has cyclic total kernel of order p^2. Conversely, every such cyclic subgroup has exactly one subgroup of order p, hence supplies exactly one such path. Therefore, as correspondences and on homology,

    T_p^2 = C_(p^2) + (p+1) id,
    beta_* alpha^* = alpha_* beta^* = C_(p^2).         (C1)

Duality exchanges the two cyclic-isogeny directions. This proves C1 without confusing the cyclic correspondence with the usual full T_(p^2). In the customary weight-two Hecke convention,

    T_(p^2) = T_p^2-p,
    C_(p^2) = T_(p^2)-1.

Omitting the final -1 is a normalization error. The proof uses the cyclic moduli problem, not an ambiguous definition of T_n at composite n.

The standard p-isogeny correspondence and its integral push-pull conventions are the primary-source input; the p^2 path count above is the written derivation here.

### 3.3 A seed-unit cross-composition

The fixed elliptic period functional satisfies z_E(T_p C)=a_p z_E(C). Consequently

    z_E(beta_* alpha^* C) = lambda_p z_E(C),
    lambda_p = a_p^2-p-1.                             (C2)

For this seed, lambda_p is a p-unit at every good p >= 5.

Proof: rational two-torsion makes #E(F_p) even, hence a_p even. For p>=7, the Hasse interval |a_p|<=2 sqrt(p)<p-1 contains no even integer congruent to +/-1 modulo p. At p=5 the retained count #E(F_5)=8 gives a_5=-2. Thus a_p^2-1 is nonzero modulo p in every case, and lambda_p is congruent to it. No ordinarity is used. In particular, at a supersingular prime lambda_p=-(p+1).

For any k>=1 choose u_(p,k) with u_(p,k) lambda_p = 1 modulo p^k. There is then a concrete period-level lift

    j_(p,k)(C) = u_(p,k) alpha^* C mod p^k,
    z_E(beta_* j_(p,k)(C)) = z_E(C) mod p^k.           (C3)

This is an actual integral correspondence at varying level. It preserves the fixed primitive period source without inverting p. It is **not** a splitting on every Hecke constituent, a full-level marking theorem, or a bound on Sha.

On the rational f-isotypic homology space the two extreme pullbacks have push-pull matrix

    [[d, lambda_p], [lambda_p, d]],

whose determinant is congruent to -(a_p^2-1)^2 modulo p and is a unit. The narrower scalar C3 is sufficient for the attempted construction and does not require choosing a primitive integral f-isotypic splitting inside the whole Jacobian.

### 3.4 Relation to prior work

The level-Np matrix [[p+1,a_p],[a_p,p+1]] and its seed-unit determinant were already proved in BSD_U22_B1_STAGE1_AUDIT_CODEX_2026-09-28/AUDIT.md, Section 4 (compendium E14a-037). The p^2 cross-composition above is an extension of that standard calculation. It is not a newly discovered fixed integer controlling Sha, and the calculation's literature novelty has not been assessed.

### 3.5 Does this realize the six-term packet formula?

Not by itself. C3 transports a full pulled-back cycle; it does not decompose that cycle into admissible CM packets or Kurihara cycles with the desired weights.

We tested the direct splice: refine alpha to a regular marking cover rho:Z->X and apply the quadratic group-algebra weight for a C_p subgroup of its deck group to rho^* C. The full pullback is deck-invariant. Hence

    (sum_j j^2 gamma^j) rho^* C
      = (sum_j j^2) rho^* C = 0 mod p,                (C4)

for p>=5. Applying any further map after this step still gives zero. Using the crossed return map does not undo C4. This is only a failure of this ordering and full-pullback construction. It is not a statement about an arbitrary intervening correspondence, or about a chosen non-invariant CM branch.

Choosing a non-invariant branch avoids C4 but removes the averaging that defines the retained packet and makes the full trace identity applicable. No arithmetic branch-selection/packet-realization formula was obtained here. The maps of C1 therefore repair the self-trace denominator but do not close the packet-generation claim.

## 4. Outcome and exact scope

The operation tried in A retains the original scalar after the necessary trivial projection. B supplies explicit coefficients for generation on a formal marked projective line. C supplies an actual p-integral transfer of seed periods through cyclic-p^2 level, but the attempted weighted splice kills a full pulled-back cycle. We have not connected B's non-affine packets to the admissible arithmetic packets.

No independent arithmetic bound, fixed annihilator, unit short witness, or verified uniform generation identity has been produced. These three attempted constructions do not close an endpoint. The two auxiliary derivations are preserved for review, not counted as progress through uniform FIN. In particular the next missing packet-realization theorem is not claimed easier than the original problem.

No production computation, class group calculation, p=53 run, K167 continuation, external job, message, push, or scheduling occurred. No model setting was changed. Existing project files were not edited.
