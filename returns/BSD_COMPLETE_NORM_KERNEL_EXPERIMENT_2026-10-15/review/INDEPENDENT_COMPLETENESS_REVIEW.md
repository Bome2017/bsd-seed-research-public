# Independent review of scalar-source split-prime completeness

Date: 2026-10-15.

Verdict: **WRITTEN_DEDUCTION_SUPPORTED_UNDER_EXPLICIT_SOURCE_AND_IMAGE_INPUTS**.

This is a separate mathematical review of SPLIT_PRIME_COMPLETENESS.md, not formal verification, human certification, a novelty assessment, or a new audit of the elliptic curves' residual images or source completeness. I read the named source statements in the cached primary text and independently checked the two Cardano identities. I found no remaining mathematical defect in the reviewed version after the ambient-target clarification in §4.

Reviewed theorem SHA-256: `677a14cca3ec4b7f915b54505dc86a38d913157eabd6d14eb4442800d5c79959`.

Primary text: `/Users/bsm/BSD_JOINT_REPAIR_TARGET_SOURCE_CACHE_2026-10-15/p-descent-long.txt`, SHA-256 `c572b0ad0f2200cc210448a4fb705327759df7d92add34f6261e017eaec22634`. Relevant text is Lemma 7.2, Lemma 7.6, Proposition 7.8, Corollary 7.9 and Proposition 7.10 (printed pp.13–19). This review uses the cached primary source; it does not claim a fresh network retrieval.

## 1. The source and target really have the required central character

Lemma 7.2 defines μ_p(Dbar)^(1) as the direct summand where a central scalar aI acts as multiplication by a. It identifies its H¹ with the stated scalar-compatible Kummer classes. For p=3 this is the norm-zero/odd part under the involution. The direct-summand statement is valid because p does not divide p−1; no semisimplicity of the whole modular GL₂ group algebra is required.

The crucial source check is Lemma 7.6: its target is explicitly **μ_p(Bbar)^(1)**, not unrestricted μ_p(Bbar). Its exact sequence is

    0 → V → μ_p(Abar)^(1) → μ_p(Bbar)^(1) → V^∨⊗μ_p → 0.

Thus the map u has geometric kernel V and carries the homogeneous source into the homogeneous target. Proposition 7.8 supplies exactness at the H¹ level; it should not be inferred merely by applying H¹ to the displayed four-term module sequence. Corollary 7.9 states precisely the global admission criterion used in the theorem. Proposition 7.10 identifies u with the incidence-algebra norm, matching the new exact norm calculations.

The cyclotomic action is included in these modules. On M and N, −I acts as −1. If −I belongs to the actual residual image G, its order-two subgroup is central and has order invertible in F_p. Averaging gives H^j(⟨−I⟩,M)=H^j(⟨−I⟩,N)=0 for j>0, while their invariants are zero. Hochschild–Serre therefore gives H^i(G,M)=H^i(G,N)=0 in every degree. Only H¹ is needed for the restriction argument. Full residual image is sufficient; the argument itself needs only the stated central element and authenticated module realization.

## 2. Restriction and complete split-prime separation

The full torsion field K contains μ_p and trivializes both modules. The inflation–restriction sequence therefore makes H¹(Q,M)→H¹(K,M) injective, and similarly for N. Consequently a nonzero norm class in H¹(Q,N) cannot disappear upon restriction to K. This establishes the needed source-specific assertion without asserting injectivity on unrestricted B*/B*^p.

For a finite-dimensional subspace U of H¹(Q,M), every nonzero class restricts to a nonzero homomorphism G_K→M. The cocycle and residual representation define a finite Galois quotient over Q. Choose an element over the identity of G whose translation is nonzero. Chebotarev gives rational primes with that Frobenius conjugacy class; they split in K. Conjugation applies an invertible G-action to the translation, so nonvanishing survives. Excluding finitely many bad, ramified and denominator primes leaves such primes available.

At these primes the full pth-power residue characters of all torsion-field coordinates detect precisely whether that unramified translation is zero. This is an arithmetic realization requirement: a subset of coordinates, an incorrectly normalized evaluation, or a sampled local Kummer subspace cannot be silently substituted for the full source evaluation.

It follows that the common kernel of all eligible evaluations on U is zero. If the present kernel is nonzero, some prime lowers its dimension; therefore at most dim U suitably chosen blocks suffice. This is an existence argument, not a bound on how far an enumeration must search, an effective bound on the prime sizes, or an assertion that arbitrary blocks have independent information.

The same reasoning applies to u(U)⊂H¹(Q,N). Thus there is no permanently invisible nonzero *actual homogeneous norm class*. A finite list of zero residues still does not certify cubehood. The packet's exact cube roots plus a matching negative residue rank provide the finite completion certificate.

## 3. The common-point quotient and its scope

The clarification added during this review is necessary. On an oversized U containing false global candidates, the target is the direct sum of ambient homogeneous residue-coordinate spaces, modulo the image E_Q(W) of the **same** point subspace W. Those candidates need not lie in the local E-Kummer images. On genuine Selmer classes the target can be restricted to the corresponding local Kummer spaces.

In that ambient target,

    E_Q(x) ∈ E_Q(W)  ⇔  x∈W+(U∩ker E_Q),

because W⊂U. This proves the displayed kernel formula. One quotient after stacking all point images imposes one common point repair; separate per-prime quotients permit unrelated point coefficients and can have a larger kernel.

Once the raw evaluation stack is injective on U, the common-point detector is injective on U/W. This strengthens the earlier termination statement from the true Selmer space to the whole authenticated scalar-compatible source. It does not apply, by this proof, to arbitrary multiplicative source elements before the scalar condition.

If a complete source U contains Sel_p, a computed invisible kernel W really excludes additional invisible classes. It does not exclude classes with nonzero detector image. In particular, injectivity into a target of uncontrolled dimension supplies no useful small upper bound by itself. An omitted source direction remains omitted from every subsequent matrix. None of these statements supplies source completeness, controls dim U across coefficient primes, or proves the seed's FIN, ORDER9 or Q36 obligations.

## 4. Cardano countercontrol

I independently substituted

    b=(m⁸+2am⁴−a²/3)/(4m²)

into the two rational identities. With depressed coefficients

    P=2m⁴/3+2a,   Q=−20m⁶/27−4am²/3+4b,

and r=(a+3m⁴)(3a+m⁴)/(18m²), exact PARI rational arithmetic gives

    Q²/4+P³/27−r²=0,
    −Q/2−r=−8m²(m⁴+3a)/27.

For the nonsingular full-GL₂(F₃) situation, the incidence cubic is irreducible over its line field. Its three roots are the three nonzero torsion points on that affine line; two of them form a basis, so its splitting field over B is the full torsion field K. The stabilizer acts as S₃. Cardano therefore gives K=B(μ₃,∛h), with h=m²(m⁴+3a), on the nondegenerate domain stated in the theorem. If h were already a cube in B, Cardano would give a root of the incidence cubic in B, contradicting irreducibility. The rational factor −8/27 is indeed the cube of −2/3.

The involution m↦−m fixes h. Hence [h] lies in the even part of B*/B*³, whereas the actual homogeneous norms are odd. A nonzero even order-three class cannot also be odd, because that would give 2[h]=0. Thus this unrestricted noncube-which-becomes-a-cube example is consistent with, and does not refute, homogeneous restriction injectivity. The full-image and nonzero-denominator qualifications in the theorem must remain attached.

## 5. Review conclusion

The adaptive deduction removes a real limitation in the fixed-source detector argument: authentic scalar compatibility rules out a permanent split-prime blind kernel, including for false global candidates. The primary source supports the exact modules needed for this repair. The finite-module checks at other odd primes support implementation of the representation calculation; they are not new arithmetic descent data for those primes.

The repaired conclusion is about eventual separation of a supplied finite arithmetic source. It is not a theorem bounding its genuine excess and should not be described as one.
