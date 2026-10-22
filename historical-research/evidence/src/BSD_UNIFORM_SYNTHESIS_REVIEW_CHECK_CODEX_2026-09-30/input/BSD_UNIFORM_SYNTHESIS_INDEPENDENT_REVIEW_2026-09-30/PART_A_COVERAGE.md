# Part A — CLW / Castella–Sano coverage audit

## Scope and evidentiary level

This checks the implication in `NEXT_TASK.md`, using the source versions supplied in the archive. A source theorem is an import, not a reproof. The model, rank two, residual surjectivity for every odd prime, local reduction data, Tamagawa product 16, and the stated Manin-unit input are retained inputs. The underlying local proof files named in `LOCAL_BINDINGS.json` are not contained in this archive and were not independently replayed.

The good primes under discussion are precisely the primes p >= 5 outside {2243,4547,5843}. There is no extra exclusion of 19, 59, or 487 in the audited implication.

Source identifiers below refer to `SOURCE_AUDIT.md` and `SOURCE_BINDINGS.json`. Page numbers are printed PDF pages. All mathematical assertions below are either **THEOREM (imported)** or **DERIVED**; retained premises are marked explicitly.

## A1. The new theorem and the squarefree issue

**THEOREM (imported, S1, CLW Theorem A, p.3).** In the standing large-image setting of p.2, let f be a newform on Gamma_0(N), with trivial nebentypus, and p > 2 a good nonordinary prime. Assume 2 <= k < p, p-regularity, and either k=2 together with a prime q || N where the residual representation is ramified, or the stated local root-number condition (rtn). Then the omega^(k/2) component of Kato's main conjecture, Conjecture 1.1, holds. In the second alternative, (rtn) is the condition at a prime q || N that the local automorphic representation is special twisted by the unramified character taking q to -q^(k/2-1).

**DERIVED — version comparison.** The pinned September 21, 2026 author PDF has no squarefree-level hypothesis in this statement. The pinned August arXiv version S2 does have one. This is an actual change in the theorem, not an inference from the abstract.

The standing assumptions in S1 §2.1, p.8, are good reduction, trivial nebentypus, nonordinarity and Fontaine–Laffaille weight. None restores squarefree N. Section 1.5(3), p.7, retains the need for a prime exactly dividing N, rather than squarefreeness. Theorem 5.1, p.35, repeats the revised hypotheses. Theorem 5.3 and its proof, pp.36–37, explicitly address primes whose squares divide N, including 2. Section 5.5, pp.39–40, uses an auxiliary quadratic field in which the primes dividing N/q split. Squarefreeness of a selected inert part is not squarefreeness of the entire level.

Conclusion for A1: no failing hypothesis was found. This is not a reproof of the extended Eisenstein-congruence argument in Theorem 5.3.

## A2. The seed at every good supersingular prime

**DERIVED from retained inputs.** Put q=2243. The conductor exponent is one and the retained reduction type is split multiplicative I_1. In Tate uniformization the parameter has valuation one. At any p != q, inertia acts on E[p] through a matrix of the form

    [1, t_p(sigma) * v_q(q_E)]
    [0,             1       ],

where the tame p-component t_p is nonzero modulo p for a suitable inertia element. Since v_q(q_E)=1, the action is nontrivial. Passing to the dual and Tate twist used for V_f does not destroy ramification: the cyclotomic character is unramified at q != p. Thus the same q supplies (ram) for every good p in this audit.

The numerical discriminant and c4 entries in `SEED_LOCAL_CHECK.json` are imported arithmetic from the packet. They were not recomputed in this review. In particular, the claimed global minimality and all-prime residual-image theorem were not re-established by a discriminant calculation.

**DERIVED — large image.** Residual surjectivity at p >= 5 implies the p-adic image contains SL_2(Z_p). Here is the group-theoretic step, separated from the retained arithmetic surjectivity premise. For a closed image G in GL_2(Z_p), the closure of its commutator subgroup lies in SL_2(Z_p) and maps onto SL_2(F_p). A closed subgroup of SL_2(Z_p) surjecting modulo p is the full group for p >= 5: a lift of a nontrivial elementary unipotent has p-th power congruent to 1+pE_12 modulo p^2; conjugation supplies the full trace-zero first congruence layer, and p-th powers supply subsequent layers. Closure completes the argument. For clarity, the first p-th-power calculation is unchanged by an arbitrary p-times perturbation of the lift because the sums of 1, i and i^2 over F_p vanish for p >= 5. The determinant is the cyclotomic character, with full image over Q, so the entire image is GL_2(Z_p). The SL_2 conclusion already suffices here and for BH.

**DERIVED — nonordinary and p-regular.** At a good supersingular p >= 5, p divides a_p and |a_p| <= 2 sqrt(p) < p; hence a_p=0. The polynomial X^2+p has distinct characteristic-zero roots. Thus p-regularity holds, even though its reduction modulo p has repeated roots. The theorem asks for the former, not residual regularity. Weight k=2 satisfies 2 <= k < p.

Modularity, trivial nebentypus, and the identification of the newform with the retained elliptic curve are retained. No application at the bad primes p=2243,4547,5843 is inferred.

Conclusion for A2: every stated supersingular hypothesis is met at the retained input grade.

## A3. Character, integral lattice, and Euler factors

**THEOREM (imported, S1, Remark 2.20, p.16).** With the source's conventions, Conjecture 2.19 on the eta component for T_f(k-1) is equivalent to Conjecture 1.1 on the eta*omega^(k-1) component. This uses the source's strict-Selmer/cohomology comparison, in its nonordinary Fontaine–Laffaille setting.

**DERIVED.** At k=2, the component supplied by Theorem A is omega. Solving eta*omega=omega gives eta=1 for T_f(1), the elliptic-curve Tate-module representation. It would be incorrect to apply the theorem to the trivial component of untwisted T_f. The second shift in §5.6 is trivial when k=2: its eta=omega^(1-k/2) is again 1.

**THEOREM (imported normalization facts, S1, §2.4.2 and Lemma 2.10, p.13).** The source distinguishes generators gamma_f^+/- of the canonical quotient lattice from generators delta_f^+/- of the Hecke eigensubspace lattice. Their ratio is the congruence ideal. The integral Kato class used in its main conjecture is the class indexed by gamma_f^+ + gamma_f^-, not by delta_f^+ + delta_f^-.

**DERIVED.** The congruence ideal is not being declared a p-unit. It is also not the Manin constant. Confusing these two integers would invalidate a primitivity argument. The bridge instead uses the source's integral class and the elliptic-curve normalization of S3 §2.1.1, p.6. At the retained modular/Manin-unit grade these agree under the lattice comparison up to a p-adic unit, which is enough for an integral main-conjecture equality. The elliptic period comparison is discussed explicitly in S1 §5.6.2, pp.41–42. Irreducibility excludes an isogeny of degree p between representatives of the rational isogeny class; passing to an optimal representative does not introduce a p-isogeny factor. The relevant comparison need not be independent of p for this task.

No assertion that the congruence ideal is a unit is needed, and no historical E11 scalar is identified by this comparison.

**THEOREM (imported, S3, §2.2, p.9).** For the elliptic Tate module, assuming E(Q)[p]=0, the cyclotomic arithmetic complex is perfect in degrees one and two; its second Iwasawa cohomology is torsion by the cited Kato theorem. Conjecture 2.2.2 is the determinant-basis assertion for the S-imprimitive Kato element. Proposition 2.2.3 equates this assertion to the corresponding integral characteristic-ideal equality. This statement imposes no finiteness of base-field Sha.

**DERIVED — exact bad-prime product.** In both S1 (5.18), p.40, and S3 (2.10)–(2.11), p.9, the primitive Kato element is multiplied by

    P_N = product_(q|N) (1-alpha_q*q^(-1)*gamma_q)
                         (1-beta_q*q^(-1)*gamma_q).

For the seed this becomes

    P_N = (1 + gamma_3/3)
          (1 - gamma_2243/2243)
          (1 + gamma_5843/5843).

The additive primes contribute 1. These factors are integral at every good p, but they are not all units. In particular, the augmentation at 2243 has numerator 2242=2*19*59, and the augmentation at 5843 has numerator 5844=12*487. Therefore the relevant factors are nonunits of Z_p[[Gamma]] at p=19,59,487. They must remain in the imprimitive class and in the matching cohomological formulation. The two sources keep the same factors; no illegitimate unit cancellation is required. Consequently these primes are not extra coverage exceptions.

The determinant equivalence in S1 (5.21)–(5.22), p.41, explicitly cites S3 Proposition 2.2.3. It is this general equivalence, with the just-checked twist and normalization, that provides the input for S3 Theorem A.

Conclusion for A3: the character and integral-normalization bridge survives at the stated import/retained-input grade. It does not establish an exact global scalar or a normalization comparison for any unrelated stored coefficient.

## A4. Rank-zero firewall

**DERIVED.** S1 §5.6 contains rank-zero calculations as well as a general determinant equivalence. Its equations (5.19), (5.20), (5.23), and (5.24) use finite-level cardinalities, indices, or nonzero critical L-values in that rank-zero application. None is used here.

In particular, an integral determinant basis over the Iwasawa algebra is not being turned into a finite cardinality of base-field H^2 in rank two. Torsion over Z_p[[Gamma]] is not the same as finiteness of Sha(E/Q)[p^infinity]. S3 §2.2 independently formulates the determinant equivalence with no analytic-rank restriction, so extracting that equivalence does not inherit the neighboring rank-zero steps.

Conclusion for A4: no rank-zero insertion is needed or present in the accepted chain.

## A5. Ordinary coverage and the final implication

**THEOREM (imported, S3, Theorem A, Corollary A and Theorem B, p.3).** For a non-CM E/Q and p>3 with surjective residual representation and p not dividing the specified Manin constant, the determinant main conjecture is equivalent to M_infinity(delta)=ord_p(Tam_E). If p does not divide Tam_E, it is equivalent to existence of a mod-p unit Kurihara quantity. Theorem B supplies the equality at good ordinary primes under these conditions; its separate supersingular clause assumes squarefree level.

**DERIVED.** Use Theorem B only for the ordinary case. At supersingular primes use S1 followed by S3's general Theorem A, not S3's older squarefree supersingular clause. The retained Tamagawa product 16 and Manin input c_phi | 512 are p-units at every good p>=5. Thus

    for every good p >= 5:
        M_infinity(delta)=0,
        and some squarefree Kato conductor n has delta_n mod p != 0.

The Manin bound is a retained premise, not an independently revalidated certificate in this packet. The ordinary theorem has no additional non-anomalous condition in its printed statement. No such condition is silently added here.

The auxiliary primes defining these Kurihara quantities satisfy ell=1 mod p and a_ell=2 mod p. They are not the Frobenius-minus-identity G2 auxiliary primes. No G2 regulator is substituted for a Kurihara quantity.

## Disposition

All five requested checks survive. There is no first failing step in Part A at the stated import/retained-input grade. The mathematical conclusion of `NEW_INPUT_APPLICATION.md` does not require correction. The source-delivery limitation and the unavailable retained certificates are documented separately, rather than disguised as mathematical obstructions.

This result supplies existence of some finite-length unit witness, with conductor allowed to depend on p. It supplies neither a witness of length two nor a uniform low-depth bound.

FIN, ORDER9 and Q36 are unchanged.
