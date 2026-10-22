# C4: a fixed fine-level cover and exact push–pull descent

2026-10-11. Bounded continuation of C3_ASSEMBLY.md. Written deductions, not independent or formal certification.

## Result and remaining interface

A fixed auxiliary level does suffice for the **cover-index and Ihara-kernel parts** of the proposed p-free argument. For this seed choose M=5, exclude coefficient p=5 conservatively, and disallow auxiliary reduction/raising primes equal to 5. The cover has fixed degree 12 on the usual connected norm-one curves; its principal-level core has index 60. Thus all descent losses have support in {2,3,5}, independent of the coefficient prime and of the two raised primes.

The exact identity is

    pi_* pi^* = [deg pi]

on the finite-field Jacobian. It provides the required p-primary surjectivity directly. We do not need to assert that the cokernel of rational points has a particular order dividing M-1, nor introduce a p-dependent stabilization root.

A published large-image Ihara theorem supplies the cohomological injectivity needed upstairs, for the retained full residual image. The source is Manning–Shotton, Theorem 6.5 (equivalently the introductory Theorem 1.1), not an unchecked extension of the original Diamond–Taylor theorem to arbitrary level.

The deduction proves supersingular generation in the **Ihara finite-field model**, and gives descent to the retained bottom model under an explicitly stated model-compatibility condition below. I have not independently completed that condition for the exact moduli conventions in the retained packet. In particular, an ordinary fine-level modular curve must not be substituted for Ihara's reduction model without checking its Frobenius descent. The remaining condition is a geometric model identification, not a new uniform nonvanishing assertion.

Even once that identification is checked, surjectivity of the matched geometric functional is not uniqueness of every definite level-raised eigensystem, and it does not prove its CM sum nonzero.

## 1. Primary sources actually inspected

1. Bertolini–Darmon, [published paper](https://www.math.mcgill.ca/darmon/pub/Articles/Research/27.Main-conjecture/pub27.pdf), Proposition 9.2 and its proof, equations (66)–(69). The preserved 2007 preprint has printed pp.72–74. Their cover is an extra Gamma_1(p) structure over a curve already having Gamma_0(p), and their last descent step uses a cokernel controlled by p-1. Neither feature should be quoted verbatim for the p-free base.
2. Y. Ihara, [1998 author survey](https://www.kurims.kyoto-u.ac.jp/~kyodo/kokyuroku/contents/pdf/1026-13.pdf), Main Theorem, Remark A, Remark G, and Section 4. This accessible version is not the 1999 pagination cited in BD. Remark G gives the same finite-field Jacobian/abelianization identity. Its Section 4 explicitly uses the reduction-prime-canonical model, not an arbitrary descent of the complex curve.
3. J. Manning and J. Shotton, [published open-access paper](https://d-nb.info/1221421131/34), Sections 2.4–2.6 and 6.1, Theorem 6.5, and introductory Theorem 1.1. Their small-level hypothesis and residual-image hypothesis are retained below.

The complete primary PDFs for items 2 and 3 are retained in the local source cache named in the file bindings; the return publishes their URLs and hashes rather than duplicating the papers. Text extraction was read; no fresh visual-page audit or complete rereading of their proofs is claimed. Diamond–Taylor's original Theorem 2 was not freshly retrieved; the stronger published Manning–Shotton theorem is the source used here.

## 2. The fixed cover, with its actual index

Let X be the retained Shimura curve with indefinite algebra discriminant N- ell1 and Eichler level N+. Assume ell1,ell2 are different from 5. Since 5 does not divide the seed conductor, the algebra and base level are unramified at 5. Impose Gamma_1(5) structure, leaving every other level condition unchanged. Write Y for the associated fine curve and pi:Y->X for the forgetful morphism.

On a norm-one connected complex component, the relevant finite quotient is SL_2(F_5), of order 120. The preimage of the unipotent subgroup, allowing the common central sign, has quotient subgroup of order 10. Strong approximation gives the full reduction at 5 for these norm-one arithmetic groups, so

    deg pi = 120/10 = 12.

Equivalently, a nonzero vector in F_5^2, modulo the common sign, gives `(25-1)/2=12` choices. The principal-level core has projective quotient PSL_2(F_5), of order 60. Keeping the coarser safe exclusion {2,3,5} also covers use of that core and any finite sign/component passage.

The smallness check is elementary here. A noncentral finite-order norm-one element has rational integral trace in {-1,0,1}. A representative in Gamma_1(5), up to the central sign, has trace congruent to 2 or -2 mod 5. These possibilities are disjoint. The projective arithmetic group is therefore torsion-free, including its conjugates. The same congruence condition makes the group obtained after inverting ell2 torsion-free. This is the relevant smallness condition for the connected Shimura curves and the corresponding tree action.

No Hecke eigensystem at 5 is chosen. Work throughout with the Hecke algebra away from the finite set containing 5, N, ell1, ell2 and p, and localize at the residual E[p] character there. On the fine level take all maximal ideals above that away-from-level character. They have the same residual representation; selecting one stabilization is unnecessary.

## 3. The Ihara hypothesis is available on this cover

Apply Manning–Shotton over F=Q, with coefficient prime p and degeneracy prime ell2. The hypotheses used are:

- p>2;
- the indefinite quaternion algebra is split at ell2;
- the fine level is maximal at ell2 and is sufficiently small;
- the residual representation attached to the chosen away-from-level maximal ideal is absolutely irreducible and its image contains SL_2(F_p);
- the exceptional extra condition in their statement at coefficient 5 is irrelevant on the conservative p!=5 domain.

These hold under the retained residual-image input and the preceding geometry. The theorem gives injectivity of the two-degeneracy map

    H^1(Y_bar,F_p)_m^2 -> H^1(Y_0(ell2)_bar,F_p)_m.

The theorem is valid at arbitrary admitted compact open level; it does not require choosing the fine-level prime equal to the coefficient prime. Its proof may introduce an internal auxiliary prime depending on p, but its statement supplies no variable denominator to the map above. We are applying the theorem, not replacing its proof by a uniform computation.

The tree-amalgam exact sequence used in BD then yields

    Hom(Gamma_fine[1/ell2],F_p)_m = 0.

Here the Hecke actions must be matched with Picard/Albanese adjoints just as in BD. Localizing at the appropriate dual maximal ideal gives the same large-image condition; the seed's Weil self-duality identifies the residual coefficient representation up to the already retained convention. Passing to all fine-level ideals over the downstairs away-character avoids a hidden choice of eigenform.

## 4. What Ihara's Jacobian formula actually says

For the torsion-free group above, Ihara's construction gives a smooth proper curve `Y_Ih/F_(ell2^2)` with a distinguished rational supersingular set S_Ih. Remark G identifies

    J_(Y_Ih)(F_(ell2^2)) / <s-s': s,s' in S_Ih>
      ~= Gamma_fine[1/ell2]^ab.

The group on the right is finite. The preceding mod-p Hom vanishing, with the matched dual Hecke action, makes its p-primary localization at the residual E-character zero. One can see the last implication directly: a nonzero finite p-primary module has nonzero quotient modulo p and hence a nonzero F_p-linear dual; Nakayama then removes all higher p-power quotients.

Thus the supersingular divisors generate the localized p-primary Jacobian group of this **specified** finite-field model. This establishes more than an unspecified claim that a sufficiently fine cover should work.

Ihara's Main Theorem makes all S_Ih points rational over F_(ell2^2). It does not say that every point above a supersingular point in every usual Gamma_1(5) descent is rational over that field. Section 4 deliberately chooses a reduction-prime-canonical model using a central-scalar descent modification. Omitting this distinction would invalidate a naive transplant of BD's equation (66).

## 5. Exact push–pull lemma

The following is an unconditional finite-geometric deduction once its morphism is supplied.

Let pi:Y->X be a finite morphism of smooth proper curves over a finite field k, of degree d. Let S_Y,S_X be distinguished finite sets with pi(S_Y) contained in S_X, and let J_Y^ss,J_X^ss be their degree-zero divisor images. Suppose the relevant Hecke actions commute with pi_* and pi^*, and let p not divide d.

Then

    pi_* pi^* = [d] on J_X(k),
    pi_*(J_Y^ss) subset J_X^ss.

The first identity follows from pullback and pushforward of divisors; it remains true with ramification and does not demand that individual fibers be k-rational. Consequently the cokernel of `pi_*:J_Y(k)->J_X(k)` is killed by d. On p-primary parts the map is surjective.

More precisely, if `J_Y(k)_m=(J_Y^ss)_m`, then every x in `J_X(k)_m` satisfies

    d x = pi_*(pi^*x) in (J_X^ss)_m.

Since d is invertible on the finite p-primary module, `x` already belongs to `(J_X^ss)_m`. Thus

    J_X(k)_m=(J_X^ss)_m.

Passing to any p^n eigenquotient of the downstairs module preserves this surjectivity. This does not require choosing a compatible full Hecke eigencharacter upstairs; the away-character localization and functoriality suffice. It also avoids inserting a Hecke degeneracy determinant such as `(M+1)^2-a_M^2`: pi is the one forgetful cover, not the sum of two M-degeneracy maps.

For the proposed M=5 cover, d=12. Even the conservative principal-core implementation has all index losses supported on 60. Therefore this entire descent is integral at p>=7 and introduces no new unbounded exception set.

## 6. The exact model-binding obligation

To apply Section 5 to the packet's actual J_ell1, the remaining interface is:

**MB.** The forgetful map of norm-one level structures realizes a morphism

    pi_Ih:Y_Ih -> X_(F_(ell2^2))

whose degree is the computed index, whose special set maps to the packet's supersingular set, and whose geometric cohomology degeneracy maps match those in Section 3 with the retained Hecke conventions.

Ihara's functorial Main Theorem and Remark A give the analogous morphism to the coarse **Ihara** model. Its Section 4 explains why the coarse model should match the standard bottom-level reduction here: the descent modification is central-scalar, and the bottom Gamma_0-type level is invariant under scalar units. Upstairs the modification need not be trivial. A full verification for the packet must write that central descent datum against its chosen Eichler-order moduli model and its Frobenius convention.

I did not complete that last identification from primary moduli definitions in this bounded pass. Accordingly, the statement obtained for the packet is

    MB + retained C3 quotient + published Ihara input
      => Div(S_ell2) -> J_ell1(F_(ell2^2))/I is onto
      => the geometric finite Kummer functional gamma is onto.

The variable coefficient-prime level and uncontrolled cover index are no longer missing arguments. The remaining MB condition is precisely located and should not be described as an unknown p-unit or a missing Selmer bound.

## 7. What surjectivity would and would not settle

Once MB is checked, gamma is an actual primitive functional on the supersingular divisor module with values in the finite local line. With C3's Hom-line convention this provides a **matched** primitive coefficient row. Its image is the whole target regardless of an arbitrary choice of a primitive definite eigenform.

Surjectivity does not prove the whole abstract quotient `Z[S']/I'` is rank one, or identify gamma with every primitive eigenform up to a unit. A separate multiplicity-one statement is needed for that stronger identification. It also does not make the particular CM trace sum nonzero: a surjective functional can vanish on that specific divisor.

Hence this work is a construction/interface repair. It supplies no uniform nonvanishing, no fixed rational C, and no new FIN, ORDER9 or Q36 conclusion.

## File bindings

- `/Users/bsm/BSD_OPENAI_CM_COMPARISON_PUSH_CODEX_2026-10-11_SOURCE_CACHE/Ihara1998.pdf`: 987341 bytes; SHA256 `d4f477da3d1f1fbc86f101cd7f6b00149e0376d5ca8068b1ed60e4f409ae3786`.
- `/Users/bsm/BSD_OPENAI_CM_COMPARISON_PUSH_CODEX_2026-10-11_SOURCE_CACHE/ManningShotton2020.pdf`: 650514 bytes; SHA256 `95892d371e25da2b9eab867cb6c4dd35dd127f38807f2a9e31767396882b1a34`.
- BD retained text binding is in C3_ASSEMBLY.md.

No old input was edited, and no finite-field seed Jacobian, full Brandt module, paid job, or prime campaign was evaluated.
