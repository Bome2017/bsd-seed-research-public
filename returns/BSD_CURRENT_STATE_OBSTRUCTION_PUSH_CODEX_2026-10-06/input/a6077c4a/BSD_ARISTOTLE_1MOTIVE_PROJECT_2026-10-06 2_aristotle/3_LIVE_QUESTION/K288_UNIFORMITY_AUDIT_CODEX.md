# K288 uniformity analysis: independent audit

Date: 2026-09-27. Verdict: **RETAIN THE CONDITIONAL TAIL IMPLICATION; SUBSTANTIVE CORRECTIONS REQUIRED. NO NEW GLOBAL THEOREM.**

Reviewed: `BSD_BUILD_MAP/K288_UNIFORMITY_ANALYSIS_2026-09-27.md`, preserved unchanged as `inputs/analysis.md`. Its SHA-256 and the other copied records are in `SOURCE_BINDINGS.json`.

This is a bounded source-and-logic audit. Prime computations remain frozen. No certificate, point count, corpus scan, Lean build, cloud job, successor construction, repository change, or expert message was launched. The arithmetic imports retain their earlier grades; this review does not re-prove the underlying main conjectures.

## 1. The valid implication, stated exactly

Let B be a finite set containing the exceptions to the proposed theorem and to the retained G2/Ota inputs. Suppose for each p outside B there is a G2-admissible auxiliary ell, with R_(p,ell) nonzero, for which

    C2(p,ell) = reduction(W) * u_(p,ell) * (a_ell - 2) * R_(p,ell) in F_p,

where W is one nonzero rational number, p does not divide its numerator or denominator, and u_(p,ell) is a nonzero residue. Compatible generator, symbol, and tame-height conventions are part of the statement.

G2 supplies an admissible auxiliary with nonzero regulator in its scope. Since ell = 1 modulo p and p does not divide #E(F_ell), the factor a_ell-2 = -#E(F_ell) modulo p is nonzero. Thus C2 is nonzero. The retained Ota criterion then gives

    Sha(E/Q)[p^infinity] = 0

outside B together with the prime support of W's numerator and denominator.

**This proves finite support, conditional on the displayed unproved comparison.** The comparison only needs to hold at one suitable auxiliary for each p. Proving a fixed exact value 288 at all auxiliaries is stronger than the nonvanishing input required by this argument. BKS is not needed for this final implication once the actual comparison is proved.

With W=288 and the note's B={2,3,5,19,59,487,2243,4547,5843}, the still-unsettled exceptions in the retained record are 59,487,2243,4547,5843. A theorem with an additional exceptional set would leave those additional primes too.

To infer FIN, the primary group at **every exceptional prime must also be proved finite**. Being eligible for an Ota run, or having a sufficient BH criterion, is not such a proof. No nonzero witness at these five primes is supplied. A fixed W=288 law outside B also says nothing directly about the 3-primary group, since 3 is excluded; that group's order 9 is an independent retained result.

## 2. A residue modulo p does not carry the claimed valuation

**Analysis sections 1–2.** The note defines w_p in F_p and then writes

    v_p(w_p) = v_p(#Sha[p^infinity]).

That is false as an assertion about the defined object. A nonzero residue records that an integral lift is a unit. The zero residue cannot distinguish p, p^2, p^4, or zero. Assigning valuation infinity to the zero residue does not recover the finite valuation of an integer that reduced to zero.

For example, both integral coefficients p^2 and p^4 reduce to the same zero in F_p although their valuations are 2 and 4. This is a logical example, not a proposed Sha group of this curve. The error was already identified in the corrected Kato finite-quotient audit.

The retained comparison instead distinguishes:

- s_p = 2 + corank_Zp Sha[p^infinity];
- A_p, the finite torsion quotient on the Selmer side;
- x_(Q,Sigma), the Kato coordinate in its specified integral determinant line;
- the coefficient **class** t_(p,ell) in I^2/I^3, which for a degree-p quotient is an F_p-line.

If s_p>2, the quadratic class vanishes. If s_p=2, the retained factorization is

    t_(p,ell) = u_(p,ell) * x_(Q,Sigma) * |A_p| * det(B_ell)

in that finite graded quotient. Here primary Sha is finite and |A_p| equals its order. At a G2 auxiliary, in the common good-ordinary scope and at the retained exact main-conjecture grade, this gives the **unit/nonzero equivalence**

    C2 != 0 mod p  iff  Sha[p^infinity] = 0.

It does not give the full order from a degree-p coefficient. At supersingular primes the retained inputs do not supply uniform unit status of x_(Q,Sigma). That qualification must remain.

## 3. Exact auxiliary independence was not established by the cited record

**Analysis section 1.** For a specific auxiliary with nonzero denominator the quotient

    w_(p,ell) = C2(p,ell) / ((a_ell-2) R_(p,ell)) in F_p

is well defined without mentioning Sha. Dropping ell from its name is an additional theorem.

The cited E10 derivation, Proposition D, step 4–5, expressly limits its conclusion to the valuation level. Its concluding sentence says: “Unit parts across different l are not claimed.” The later corrected d-infinity and Kato audits preserve this limitation.

A comparison C2=u_(p,ell) M_p R_(p,ell) does not establish that dividing by a_ell-2 removes **all** auxiliary dependence. For a simple formal example, let M_p=1 and choose the residual units to be a_ell-2 for one auxiliary and 2(a_ell-2) for another. Both comparisons have identical unit status, but the normalized quotients are 1 and 2. This refutes the inference from the cited up-to-unit statement; it does not disprove exact independence for the actual seed.

**Correction:** use w_(p,ell). Treat exact auxiliary independence, after every Euler, period, basis and generator convention is accounted for, as unestablished by this note. The numerical observations can still be stated at their actual pairs. In particular, the p=19 observation is valid data but lies outside the note's BKS scope.

## 4. The exact 288 law is not identified with the entire refined conjecture

**Analysis sections 3(b), 3(c), and 6.** A selected family of degree-p quadratic congruences with a prescribed constant is not automatically equivalent to the full refined Mazur–Tate conjecture, the p-adic Tamagawa-number conjecture, or Generalized Perrin–Riou.

At source, BKS II Conjecture 2.3 uses the algebraic BSD constant; its section 2.1 defines that using finite Sha. Theorem 1.1 assumes BSD **and** the relevant GPR conjecture under its stated hypotheses. This does not provide a finiteness-free proof of the note's exact constant or establish an equivalence with its selected mod-p tests. See [BKS II](https://arxiv.org/html/2103.11535v1), sections 2.1–2.2 and Theorem 1.1.

Thus the safe description is **a proposed seed-specific, degree-p leading-coefficient law motivated by refined Mazur–Tate**. Its exact 288 normalization and relation to a rational archimedean constant require their own argument. The shorthand “Burns; Tan” is not a theorem-level source specification for the broader claimed equivalence.

There are three different strengths here:

1. C2 nonzero at a suitable auxiliary for almost every p;
2. equality with a fixed rational W **up to independently specified units**;
3. exact equality w_(p,ell)=288 with no unspecified unit.

The first is sufficient for the desired tail. If arbitrary units are allowed in the second, then outside the support of W it only says w_(p,ell) is nonzero: any nonzero residue can be written reduction(W) times a unit. Such a representation alone does not construct a common rational structure on Kato's determinant lines. The third retains numerical information discarded by the first two.

A coordinate also changes when its integral line's basis is multiplied by a unit. Mod-p matches of selected coordinates do not imply that the full p-adic elements are realizations of one rational number.

## 5. Rationality would not make the multiplier 288

**Analysis section 5(1) and the pasted summary.** The retained quotient is

    q = L''(E,1)/(2 Omega_E Reg),
    35.99427 < q < 36.00573.

Rationality alone does not prove q=36. For example 36+1/1000 is rational and lies in that interval. Therefore even a proved exact comparison W=8q would not give W=288 merely from rationality. The denominator-at-most-174 condition or another exact comparison remains an additional sufficient input.

For finite support, a nonzero rational W could suffice without knowing its exact value. That distinction is useful, but conditional: neither rationality nor the required comparison was proved here.

There are also two different comparison proposals that must not be merged:

- A **direct, finiteness-free tame identity** C2=(a_ell-2)*8q*R_(p,ell), with exact normalizations and full prime scope, together with rationality and G2, would imply a tail theorem. This is a specification of a missing identity.
- The existing **cyclotomic p-adic Beilinson formula** does not automatically supply that direct identity. BKS I Hypothesis 2.2 includes primary finiteness, and Corollary 6.7 has the regulator qualifications. The retained d-infinity route also needs nondegeneracy, control, and order comparisons, and is only completed conditionally on the ordinary tail. It leaves supersingular and exceptional regimes separate. See [BKS I](https://arxiv.org/html/1910.07404v2), Hypothesis 2.2 and Corollary 6.7, and `inputs/dinf_corrected_chain.md`.

The one-line claim “rationality plus the p-adic identity attacks both at once” needs those distinctions. It is not a newly closed arrow.

## 6. The character-valuation reformulation is valid after normalization repairs

**Analysis section 5(3).** This part is a useful precise reformulation, not a proof of nonvanishing.

Use the actual production element theta in Z_p[C_p]. Its rational coefficients are certified in (1/1024)Z, so p-integrality holds at the considered odd primes. One may conclude

    chi(theta) in Z_p[zeta_p],

but not from that lattice alone that chi(theta) is a global algebraic integer in Z[zeta_p].

Write the degree-less-than-p representative as

    theta = sum_(j=0)^(p-1) C_j T^j, T=gamma-1,

and assume C_0=C_1=0 modulo p, as supplied by the retained rank/order argument. For a character of order p, put pi=1-zeta_p, normalize v_pi(pi)=1, and note v_pi(p)=p-1. The character sends T to a unit times pi.

For p>=5:

- the constant term has valuation at least p-1;
- the linear term has valuation at least p;
- every term of degree at least three has valuation at least three;
- the quadratic term has valuation exactly two precisely when C_2 is a p-unit.

The quadratic term is then the unique term of least valuation. Conversely, when C_2 is divisible by p, all terms have valuation at least three. Hence

    v_pi(chi(theta))=2  iff  C_2 != 0 mod p.

A nontrivial power of the chosen character has the same conclusion. This proof uses only the normalization and lower coefficients, not the empirical 288 law.

Ota Proposition 2.3(2) provides primitive-character interpolation in its own period convention. For an even order-p character that convention must be matched to the production period; the total-real-period convention would introduce the already reviewed factor 1/2. See [Ota](https://arxiv.org/html/1509.00682v1), Definition 2.1, Remark 2.2 and Proposition 2.3. No global integrality claim should be inserted when only the retained 1/1024 lattice is used.

Consequently a theorem producing this exact valuation at an admissible auxiliary for every sufficiently large p would give finite support. The note supplies no such analytic theorem, estimate, or construction. Naming modular-symbol distribution as a possible method does not yet distinguish an executable mathematical attempt from the target itself.

## 7. The necessity and nonexistence language must be narrowed

The following are not established:

- “On this route there is no weaker target.” Exact 288 is stronger than the unit statement needed, and intermediate lemmas or bounds can be useful even where their final conclusion is equivalent to a Sha statement.
- “A proof needs ... one p-independent object.” A new global object is one possible approach, not a proved requirement. Existing global modular-symbol families already exist; compatible arithmetic control is missing.
- “The only Sha-free handle ... is w_p itself.” The bounded work did not prove that these are all available arithmetic handles.
- “A proof needs one of the three external inputs.” The list is not exhaustive.
- “A rank-2 cycle ... is known only over function fields.” No such broad literature exclusion was established. A relevant rank-two comparison for this seed was not supplied. Derived classes are not ruled out by the vanishing of the classical Heegner point in the relevant Gross–Zagier setup.

These limitations were already present in the earlier reviews. Reintroducing them as categorical conclusions does not become correct by calling them a synthesis.

## 8. Disposition

**Keep:** the explicit quotient at a chosen auxiliary; the conditional fixed-W-to-finite-support argument; the correctly normalized character-valuation formulation; the separation of finite support from the exact real formula.

**Correct:** auxiliary independence, residue valuations, conjecture identifications, exceptional-prime status, rationality-to-288, and claims about necessary methods or unavailable objects.

**Do not claim:** FIN, ORDER9, Q36, exact W=288, a newly established all-prime scalar, or a new global construction. Do not count this audit as closing the global obstacle.

The proposed Kato/determinant question overlaps the already completed E10/E11 attempts. A further task would need a genuinely different map, estimate, identity or input; changing the phrasing of the same missing comparison is not such an input.

The corrected target could be communicated as an open question, but nothing was sent. The user has already contacted experts and has frozen prime computations. This audit launches no successor and does not recommend another run merely to keep activity going.
