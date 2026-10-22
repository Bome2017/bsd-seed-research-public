# Sources, exact use, and retained grades

The cached PDF and extracted-text hashes are in SOURCE_BINDINGS.json.
Whole third-party PDFs are not republished in this return. Source reads
are not claimed as independent reproofs of their theorems.

* [Emerton--Pollack--Weston, Variation of Iwasawa invariants in Hida families](https://arxiv.org/abs/math/0404484): Theorem 2.1.2 states integral finite freeness and classical control; Theorem 2.3.1 gives the ordinary representation; Propositions 4.1.1 and 4.1.4 give free signed modules and canonical-period specialization. These support the constructed cofinite control argument, not a cross-p L-value estimate.
* [Maksoud, A canonical generator for congruence ideals of Hida families](https://arxiv.org/abs/2312.16706): polynomial action and primitive period in section 2.1; integral ordinary/anti-ordinary control in section 2.2; formula (10), formula (14), Definitions 2.1.3 and 2.3.5. Its adjoint result is not invoked to annihilate standard seed Sha.
* [Futterer, A p-adic L-function with canonical motivic periods for Hida families](https://arxiv.org/abs/2005.00896): Theorems 2.22 and 2.39, Proposition 3.11, Condition 3.12, and Theorems 3.17/3.19/3.23. The final density inference in the proof of 3.17 was visually checked on page 53; SOURCE_UNIT_REPAIR.md replaces it on our domain by integral surjectivity. The 3.19 period has not been identified with the prior Gauss frame.
* [Mazur--Wiles, On p-adic analytic families of Galois representations](https://www.numdam.org/item/CM_1986__59_2_231_0/): Boston appendix Proposition 3, printed page 263 (PDF page 34), was visually read. All four hypotheses are applied to the ordinary family. The level-one examples in the main text are not substituted for a general tame-level theorem.
* [Kings--Loeffler--Zerbes, Rankin--Eisenstein classes and explicit reciprocity laws](https://arxiv.org/abs/1503.02888): sections 7.2--7.4 and 7.7 fix lattices and models; 9.5.1--9.5.3 compare Ohta and de Rham maps; 10.1.1 fixes the differential and congruence-ideal maps; 11.6 retains Gauss/congruence scalars. DE_RHAM_TRANSPORT.md records exactly which identification is still unproved.
* [Kim, Refined applications of Kato's Euler systems for modular forms](https://arxiv.org/abs/2203.12157): sections 3 and 7.9, especially 7.23/7.24, were read for primitive/optimal symbols. Its good-prime crystalline comparison is not asserted for our ramified weight-three specialization. This is a different paper from the source of the retained two-prime Kim reciprocity formula.
* [Kato, p-adic Hodge theory and values of zeta functions of modular forms](https://www.numdam.org/item/AST_2004__295__117_0/): period construction 4.10 and 6.3; 14.13; good-level restriction in 14.21 and 17.5. The prior index and ramified lattice are retained through the bound context files, not re-certified by this turn.
* [Pollack--Serban, Non-vanishing of critical L-values in Hida families](https://arxiv.org/abs/2208.02769): downloaded and background screened only. No theorem from this paper is used to infer p-adic unitness.

The cached KLZ is v6 with its November 2023 corrigendum, which was read.
The correction distinguishes cuspidal branches from integral parabolic
cohomology equality. On the present residual-irreducible localization the
paper explicitly identifies the parabolic and full modules, so the
corrected caveat does not require an extra Eisenstein denominator here.

Additional standard imports in the written Hida proof: newform decomposition,
weight-two trivial-character Steinberg relation U_p^2=1, strong multiplicity
one, Hasse, prime-to-p torsion reduction, Nakayama, and Hensel. Their use is
explicit in COFINITE_HIDA_CONTROL.md. This return does not claim to have
freshly source-audited every classical foundation.

Twelve historical project files are bound and copied in context/. Their
grades, correction precedence and conditional statements survive copying.
In particular the explicit arithmetic norm-relation gate in BRANCH_THETA.md
is not erased. A complete audit of the project's seed certificates or
literature novelty was not undertaken here.
