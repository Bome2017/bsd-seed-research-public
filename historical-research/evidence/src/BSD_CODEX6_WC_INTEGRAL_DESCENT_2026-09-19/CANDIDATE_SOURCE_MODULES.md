# Candidate sources, tested against the actual content requirement

Every source below is considered only for this seed and for WC. 'Exists' never means that its distinguished arithmetic specialization is nonzero.

## 1. Fixed integral homology and modular symbols — actual construction

- Ring and finiteness: H=H_1(X_0(N)(C),Z) and M_Z=Hom(H,Z), finite free of rank 2g.
- Distinguished element: z_E is the real period of the modular parametrization divided by Ota's period. It exists before FIN and has odd-prime content one, relative to the retained isogeny-class data.
- Map: phi_{p,S} evaluates on the explicitly defined binomial/logarithmic cycles in HOMOLOGY_SOURCE_THEOREM.md and divides by the p-unit c_E. It produces the full degree-two Ota class, not a merely analogous scalar.
- Dependence: H and z_E are fixed; cycles, discrete logarithms, coefficient moduli and target vary with p and S.
- Denominators: c_E divides 2^9; none at p in P. The vanishing L(E,1)=0 lets relative modular-symbol paths be replaced by absolute cycles.
- Kernel/cokernel: kernel is the simultaneous system of evaluation congruences stated in H3; cokernel is finite p-primary. The target is torsion, so a rational determinant is vacuous. The relevant evaluated rank-one cokernel is R_k/D_{p,k} in UC.
- Primitivity: source primitivity is proved; image primitivity is not. Ordinary image primitivity is equivalent to primary Sha vanishing by O1.

This is the best fixed pre-FIN source constructed in the session. It meets the source-and-map part of the request, but not its uniform-index part.

## 2. Integral modular-symbol cohomology / parabolic lattices

One may dualize the preceding construction or use relative homology H_1(X,cusps;Z), which is also finitely generated and has explicit boundary maps. The distinguished newform functional becomes integral after the Manin/period normalization. Absolute cycles avoid needing a splitting of the cusp boundary map. The specialization is the same weighted period evaluation after the standard pairing. Any fixed change-of-lattice index only contributes a fixed finite exceptional set; it does not control the indices of the p-dependent weighted cycles inside the elliptic quotient. No better image bound was obtained by changing this presentation.

## 3. Kato's integral Euler system — actual pre-FIN p-adic source

For fixed p,S, the relevant unramified-outside-a-finite-set global cohomology module H^1(O_{Q(S),Sigma},T_pE) is finitely generated over Z_p, with Gamma_S-action. Ota Theorem 5.9 supplies z_S integrally under the seed hypotheses, before FIN. The exact map is global localization, then quotient by H_f, then U_S. Theorem L4 proves the last map is an isomorphism of free rank-one Z_p[Gamma_S]-modules, with index one. Its kernel is zero and cokernel zero. The unresolved kernel/cokernel is that of global localization and its degree-two augmentation specialization on z_S.

Both the coefficient ring Z_p and the global field/source vary with p,S. The norm-compatible system is a real arithmetic object, but not thereby a finite Z-lattice. Kato integrality, or an integral zeta-element map from modular symbols, does not force its degree-two localization to be nonzero. Ota's derivative vanishing detects exactly this obstruction.

## 4. Characteristic-zero Mazur-Tate family and distributions

Each theta_S is already an element of a finite group ring over Q, integral over Z[1/2] for the present good-conductor symbols. The family satisfies Euler-factor norm relations. Thus it is legitimate characteristic-zero, pre-FIN data. Its degree-two target at any fixed S is finite torsion: only primes dividing #G_S can be seen there. The coefficient rings and their ranks grow with S.

An inverse limit, a distribution receptacle with modified transition maps, or a completed group ring can store compatible data. One must specify the transitions: the actual theta elements are Euler-factor norm compatible, not automatically a plain inverse-limit element under unmodified projections. Such receptacles are not finite Z-modules. Norm maps have augmentation factors a_ell-2, which may be divisible by p. They prove T3 but give no inverse or uniform content bound across different p. No additional primitive distinguished element is obtained by calling the family universal.

## 5. Hecke and congruence modules

The finite Hecke algebra on H and the f-eigenquotient exist over Z, before FIN. A rational projector has denominators bounded by a fixed congruence integer. The distinguished period functional is an f-eigenfunctional; specialization remains evaluation on the weighted cycles. Therefore a congruence denominator could bound a fixed projection's cokernel, but cannot show that the chosen cycles generate the elliptic quotient modulo every large p.

More decisively, for any cycle subgroup W, z_E(TW) is contained in the ideal z_E(W), because z_E(TC)=a_T z_E(C) and a_T is integral. With the identity operator included, the Hecke-span image ideal equals the original image ideal. Hecke closure alone cannot remove a p-factor in UC. A theorem that the weighted cycles span the appropriate quotient with a fixed index would help; no such theorem was found or proved.

## 6. Determinant modules before FIN

A perfect arithmetic complex over Z_p[G] has an invertible determinant module without first choosing a Mordell-Weil/Sha realization. BKS's complex C_F in the proof of Theorem 4.3 is represented by a two-term finite free complex; its cohomology describes H^1 and H^2. This pre-FIN object is legitimate. The theorem's additional Fitting containment is an explicit hypothesis and not automatically a uniform bound over p.

A local determinant line's existence does not choose a primitive global zeta generator or identify its real leading term. A post-FIN BKS Mordell-Weil realization is excluded as a foundational input to FIN. A hypothetical rationally acyclic finite perfect Z-complex with cohomology realizing all primary defects would give finite support; building that complex and proving that realization is exactly the missing arithmetic theorem, not a consequence of taking products of local complexes.

## 7. Hida / ordinary large objects

These are over p-dependent Iwasawa or Hecke coefficient rings, typically finite over a power-series base only after specific hypotheses and localizations. Integral classes and ordinary specialization maps can be useful at a fixed p. Their denominators, congruence ideals and specialization kernels still require control; finite generation over one such ring is not finite generation over a single Z-lattice controlling every p.

No Hida candidate was substituted for the explicit source above. The H9R23 moving-character contraction via characteristic-zero equivariant coefficient maps remains excluded in its stated scope. No new specialization escaping that obstruction was constructed. A separate exterior contraction is not ruled out by that no-lift theorem.

## 8. Exterior powers of the known Mordell-Weil lattice

The free Mordell-Weil group of rank two, its exterior square and its tensor square are integral rank-one objects before FIN, since the rank/basis theorem is retained. They provide primitive bases and real/p-adic regulator contractions. They do not provide a distinguished arithmetic coefficient encoding the Ota/Kato leading term. Assigning that coefficient by assuming the desired comparison is circular.

The predecessor's exterior-contraction lemma remains valid: a rational determinant source can yield a strict p-adic line with a transcendental coordinate ratio. This removes a type obstruction only. Neither the kernel/cokernel of an unconstructed Ota realization nor its index can be read from the regulator lattice.

## Result

Only the fixed homology construction gives all requested fixed-source data and exact specialization maps here. The Kato local construction proves an additional index-one comparison. Neither proves UC. The ordinary equivalence gate makes clear why further generic source packaging is not the next arithmetic step.
