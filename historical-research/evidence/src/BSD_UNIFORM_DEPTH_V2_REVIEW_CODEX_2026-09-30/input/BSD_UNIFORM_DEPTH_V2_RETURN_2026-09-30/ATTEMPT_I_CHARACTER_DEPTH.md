# Attempt (i): cyclic character depth

## Scope and claim labels

**DERIVED — scope.** This file attempts v2 §5(i). It produces an exact, capped comparison between minimum character depth and the Selmer dimension, conditional only on the imported statements specified below. It does not prove a uniform upper bound. The original seed arithmetic certificates are retained, not replayed. No novelty claim about the literature is made.

**DERIVED — notation.** Fix a good prime p>=5. Put

    d_p = dim_Fp Sel_p(E/Q) = r_p,
    h_p = min_{(K,chi)} v_lambda(chi(theta_K^MT)),
    lambda = zeta_p - 1,    v_lambda(lambda)=1.

The minimum ranges over real cyclic degree-p fields at their actual conductors m, with (m,pN)=1, and faithful characters. Include the value +infinity for a zero character value; use +infinity if all such values vanish. Since possible finite depths are nonnegative integers, a finite infimum is attained. B.20 and B.21 of the controlling brief give finite d_p, even and at least two. The distinction between d_p and a Z_p-corank is maintained throughout.

## Printed inputs

**THEOREM — imported.** Bullach–Honnor, arXiv:2511.07203v1, Hypothesis 1.2 and Theorem 1.4(b), printed p.2: for an abelian field L and p>3, assume that the p-adic image contains SL_2(Z_p); either L contains no primitive p-th root of unity or E has potentially good reduction at p with the specified reduction having no p-torsion; and, if E is additive at p, p is unramified in L. Then the inverted full Mazur–Tate element belongs to the zeroth Fitting ideal of the classical p-primary Selmer dual over Z_p[Gal(L/Q)]. No finiteness of Sha is assumed in this clause.

**THEOREM — imported.** The same paper, Proposition 2.4, printed p.9: if q does not divide mN, projection from conductor mq to m multiplies the full theta element by

    a_q - sigma_q^(-1) - sigma_q.

The full formula, including its separate q|m clause, is not needed here. All uses below have q not dividing mN.

**DERIVED — normalization from the printed definition.** BH Definition 2.2 and §2.1, printed p.8, use the total positive real period. On a real quotient the minus symbols cancel in the complete sum over (Z/m)^*. Thus the coefficients relevant here use precisely the Castella–Sano symbol Re(lambda_f(a/m))/Omega_E^+ of v2 §5, not the production symbol. For this seed that symbol is one half of the production symbol and has denominators dividing 2048. No representatives modulo sign, Gauss-sum division, Euler-factor deletion, or regulator normalization is introduced.

**DERIVED — applicability beyond degree p.** Each finite elementary abelian p-extension considered below is real, has conductor prime to pN, and satisfies the same BH hypotheses as the degree-p fields. Residual surjectivity supplies SL_2(Z_p) in the image by the elementary lifting argument below. Reality supplies Hypothesis 1.2(ii)(a), and good reduction makes (iii) vacuous. Therefore the theorem can be used over the compositum as well as over its cyclic subfields.

**DERIVED — lifting check.** Let G be the closed p-adic image and H the closure of its commutator subgroup. Then H lies in SL_2(Z_p), and its reduction is SL_2(F_p), since the commutator of GL_2(F_p) is SL_2(F_p). To verify the required lifting fact, take any closed subgroup H of SL_2(Z_p) surjective modulo p. Lift the elementary unipotent u_0=I+N, N=E_12, to u=u_0(1+pA) modulo p^2. Expanding u^p modulo p^2 gives u_0^p multiplied by 1+p times the sum of the conjugates of A by u_0^j. Modulo p these conjugates are quadratic polynomials in j. For p>=5 the sums of 1, j, and j^2 over j=0,...,p-1 vanish modulo p. Thus u^p=I+pN modulo p^2. Conjugating this element by H shows that the first congruence kernel contains the span of the SL_2(F_p)-conjugates of N, namely all of sl_2(F_p). Taking p-th powers of elements congruent to I+p^a B gives I+p^(a+1)B at the next layer. Induction yields every congruence layer; closedness then gives H=SL_2(Z_p). This proves the required image condition from the retained residual surjectivity without assuming a new arithmetic certificate.

## Lemma I.1: multivariable Fitting lower bound

**DERIVED.** Let L/Q be a real abelian p-extension of conductor prime to pN, let Gamma=Gal(L/Q), and put

    A = F_p[Gamma],   J = augmentation ideal of A,
    Y_L = Sel_(p^infinity)(E/L)^dual,
    X_p = Sel_(p^infinity)(E/Q)^dual.

Then

    theta_L^MT mod p belongs to J^(d_p).                       (I.1)

**DERIVED — proof.** The image of G_L under the residual representation contains the commutator subgroup SL_2(F_p), because L/Q is abelian. Hence E(L)[p]=0, and therefore E(L)[p^infinity]=0. Inflation–restriction makes restriction on H^1 with coefficients E[p^infinity] injective. Local Kummer conditions are preserved by restriction, so restriction on classical Selmer groups is injective too. Dualizing yields a surjection

    (Y_L)_Gamma ->> X_p.

Consequently

    d_L := dim_Fp(Y_L/(p,J)Y_L) >= dim_Fp(X_p/pX_p)=d_p.

The ring A is local because Gamma is a finite p-group. In a minimal presentation of Y_L/pY_L over A, all matrix entries lie in J. Thus every d_L-by-d_L minor lies in J^(d_L); if there are insufficient columns the Fitting ideal is zero and the inclusion still holds. Fitting ideals commute with base change. The BH theorem therefore puts the inverted theta element modulo p in J^(d_L), hence in J^(d_p). Inversion preserves every augmentation power, proving (I.1). The equality dim_Fp(X_p/pX_p)=d_p is the finite-level comparison retained in B.21; it does not identify corank with Mordell–Weil rank.

## Lemma I.2: low character depth cannot be below d_p

**DERIVED.** For every field-character pair in the definition of h_p, if its depth e is less than p-1, then e>=d_p.

**DERIVED — proof.** Write R=Z_p[C_p], t=gamma-1, and expand theta_K^MT uniquely as sum_{j=0}^{p-1} b_j t^j. Such an expansion exists because the relation (1+t)^p-1 is monic of degree p. Lemma I.1 gives theta mod p in (t)^(d_p). At a faithful character t maps to a unit multiple of lambda to first order, and v_lambda(p)=p-1. Below p-1 a p-divisible coefficient cannot contribute. The degrees of the p-unit terms are distinct, so the smallest such degree below p-1 cannot cancel. A value of depth e<p-1 therefore forces a nonzero mod-p coefficient at degree e, and e>=d_p follows.

## Lemma I.3: exact leading form at a minimum unit witness

**DERIVED.** Let d=d_p=r_p, and choose a minimum unit Kurihara witness

    n=q_1 ... q_d,    delta_n mod p != 0.

Let L_i be the unique degree-p subfield of Q(mu_(q_i)), and L their compositum. Choose gamma_i so that the image of a modulo q_i is gamma_i^(ind_(g_i)(a) mod p). Put T_i=gamma_i-1. Then

    A = F_p[T_1,...,T_d]/(T_1^p,...,T_d^p),
    theta_L^MT mod p
      = delta_n T_1 ... T_d  modulo J^(d+1).                 (I.2)

This identity uses the total-real-period delta_n from v2 §5.

**DERIVED — proof.** The fields L_i are linearly disjoint: each nontrivial subfield of L_i ramifies at q_i, whereas the compositum of the other fields is unramified there. Thus Gamma is C_p^d and L has actual conductor n. Lemma I.1 puts theta_L mod p in J^d.

Fix i and project to L^{(i)}=product_{j!=i} L_j, which amounts to setting T_i=0. The conductor norm relation gives

    pi_i(theta_L) = (a_(q_i) - u_i - u_i^(-1)) theta_(L^(i)),

where u_i is the image of Frobenius q_i in Gal(L^(i)/Q). Because q_i is a Kato prime, a_(q_i)=2 mod p. Therefore

    2-u_i-u_i^(-1) = -(u_i-1)^2 u_i^(-1) belongs to (J')^2.

Lemma I.1 applied to L^(i) puts its theta element modulo p in (J')^d. The projected product consequently lies in (J')^(d+2). In particular the degree-d initial form of theta_L vanishes whenever T_i=0. This holds for every i. The truncated polynomial presentation of A has a monomial basis. A degree-d monomial involving all d variables must be T_1...T_d. Hence that is the only possible nonzero degree-d term.

Finally expand each group element as product_i (1+T_i)^(ind_(g_i)(a) mod p). The coefficient of T_1...T_d in the full plus-symbol sum is exactly

    sum_(a,n)=1 [a/n]^+_(total period) product_i ind_(g_i)(a) mod p
      = delta_n mod p.

The minus part has already cancelled on the real quotient. This proves (I.2), with no hidden factor of 2.

## Proposition I.4: exact character depth from a minimum witness

**DERIVED.** If d_p<=p-2, every cyclic degree-p quotient of Gal(L/Q) that is nontrivial on all d inertia factors has actual conductor n and every faithful character has depth exactly d_p.

**DERIVED — proof.** Write such a quotient as gamma_i |-> gamma^(s_i), with every s_i in F_p^*. Its inertia at every q_i is nontrivial, so its conductor is n. Because the conductors agree, BH Definition 2.2 identifies theta_K with the projection of theta_L without an imprimitive Euler correction. On group rings,

    T_i |-> (1+t)^(s_i)-1 = s_i t modulo t^2.

Formula (I.2) gives

    theta_K^MT mod p
      = delta_n (product_i s_i) t^d modulo t^(d+1),          (I.3)

with unit leading coefficient. Choose gamma so that the faithful character takes it to zeta_p. In the integral expansion all coefficients of degrees below d are divisible by p. Their character valuations are at least p-1>d; all terms of degree above d also have greater valuation. Thus the degree-d unit term uniquely determines valuation d. Replacing the faithful character rescales the first-order parameter by an F_p-unit, so the same result holds for every faithful character.

## Corollary I.5: exact capped minimum-depth identity

**DERIVED at imported-theorem / retained-seed-input grade.** For every good p>=5,

    min(h_p,p-1) = min(r_p,p-1)
                 = min(dim_Fp Sel_p(E/Q),p-1).              (I.4)

**DERIVED — proof.** Lemma I.2 supplies the lower bound below p-1. If r_p<=p-2, choose its unit witness using B.20/B.21 and apply Proposition I.4 to attain depth r_p. If r_p>=p-1, Lemma I.2 prohibits every depth below p-1, and both capped sides equal p-1, including the possibility h_p=+infinity.

**DERIVED — important scope.** The cap is necessary for this argument. Once the relevant degree reaches p-1, coefficients divisible by p can have the same or smaller character valuation; the mod-p leading form alone does not justify uncapped equality. No claim about h_p=r_p above that range is made.

## Rank-two consequence: the missing converse is supplied

**DERIVED.** For the retained rank-two seed and every good p>=5, the following are equivalent:

    a field/character of v2 §5(i) has depth <4;
    some two-prime Kato quantity delta_(q_1 q_2) is a unit;
    dim_Fp Sel_p(E/Q)<=3;
    Sha(E/Q)[p^infinity]=0.

Moreover, if these conditions hold then h_p=2. A two-prime unit witness produces a real degree-p field of actual conductor q_1 q_2 with exact depth 2; no extra auxiliary conductor prime is required. The implication from the two-prime witness to the character is (I.3); the reverse direction and equivalence with Sha use I.2 and the parity/Nakayama statements retained in B.21. This strengthens the recorded one-way comparison, but establishes no new witness at any unsettled prime.

## Concrete independent endpoint attempt: an algebraic norm budget

**DERIVED — sufficient norm inequality.** Let D=2048, beta=D chi(theta_K^MT), and suppose beta!=0. The seed's denominator bound gives beta in Z[zeta_p]. Since D is a p-unit and p is totally ramified with residue degree one,

    v_p(Norm_(Q(zeta_p)/Q)(beta)) = v_lambda(chi(theta_K^MT)).

Consequently

    0 < |Norm(beta)| < p^4                                    (I.5)

would give a v2 §5(i) witness. This is an independent sufficient inequality, not a consequence of complex nonvanishing.

**DERIVED — actual stopping point.** To prove finite support this route needs, for every p outside one fixed finite set, a choice of actual conductor and character satisfying (I.5). Neither the retained certified interval for q nor a finite collection of modular-symbol residues bounds these character norms. A triangle bound |sigma(beta)|<=B gives only |Norm(beta)|<=B^(p-1); to imply (I.5) it would require B<p^(4/(p-1)). No such uniform estimate or construction was obtained. The p-dependent conductors cannot be silently bounded by a single finite list: an order-p character at a fixed conductor m requires p to divide phi(m).

## Ordered tests and endpoint decision

**DERIVED — candidate I-A, use unspecified-length primitivity plus a character transfer as the endpoint.** First failing test: K-S. Formula (I.4) shows exactly why this does not exclude excess Selmer: if d_p=4 and p>=7, the corresponding minimum character depth is 4, not <4. At p=5 the capped value is still 4. The transfer is retained as an intermediate comparison, not promoted to a vanishing mechanism.

**DERIVED — candidate I-B, the norm-budget construction.** K-S passes for the conditional implication (I.5), because excess Selmer forces depth at least four and hence p^4 divisibility of every nonzero norm. First failing test for the proposed complete construction: K-P, since no cofinite construction satisfying (I.5) was proved. Later tests are not assigned endpoint pass statuses. No norm for an unsettled prime was computed.

**DERIVED — intermediate gate record for I.1–I.5.** K-S is addressed by declaring the exact new arrow rather than a FIN consequence; K-P holds for the comparison statements uniformly for every good p>=5; K-F uses no unknown primary orders, finiteness, rationality, or desired unit witness as an unconditional fact; K-C uses the multivariable Fitting lower bound and conductor norm relations to sharpen the old witness-to-depth comparison, not to pretend to bound r_p; K-num fixes the full BH/total-period convention and asserts no rational specialization scalar. The 288 and 24 observations are neither used nor contradicted. The statements for any other curve require that curve's own rank, integrality, image, and B.20/B.21 hypotheses; they are not automatically asserted from the seed's certificates.
