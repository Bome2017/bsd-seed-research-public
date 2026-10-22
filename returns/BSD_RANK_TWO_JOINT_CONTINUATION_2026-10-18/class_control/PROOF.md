# The lower-degree norm-relation test

## Scope and inputs

Retain the checked full-image framework for 11a1 at 7. Its normal closure L has Galois group G = GL2(F7), of order 2016. The degree-48 point field is A=L^H, where H is the stabilizer of one nonzero vector and |H|=42. The scalar center Z has order six and intersects H trivially. The character chi used for the source is faithful on Z (either faithful character is covered).

The conclusion below concerns norm relations through subfields **inside this normal closure**. It is not an unconditional assertion about arbitrary number fields or all class-control mechanisms. In particular it does not identify the class group of A with invariants in the class group of L; the extension degree 42 is divisible by seven, so that shortcut would need separate justification.

## Exact finite computation

`scalar_subgroup_screen.g` constructs GL(2,7), passes through an explicit permutation-group isomorphism, and enumerates `ConjugacyClassesSubgroups(G)`. It computes the order and index of every representative J and the exact order of J intersect Z. All 84 records are in SUBFIELD_SCREEN.json. They satisfy:

- every J with [G:J]<48 has |J intersect Z|>1;
- the least index with |J intersect Z|=1 is 48.

This is an exact finite group computation in GAP, not a proof-assistant certificate or a class-group computation. The source framework supplying G for the arithmetic field remains retained. The standalone replay demands both the completion marker and absence of GAP error text; a zero process exit is insufficient.

## Derived obstruction for generalized norm relations

Let K be a characteristic-zero field containing the sixth roots of unity, for example Q_7, and form the permutation module V=K[G/H]. There is a nonzero vector

v = sum_{z in Z} chi(z)^(-1) [zH].

The cosets zH are distinct. Since Z is central, v is H-fixed and Z acts on v through chi. Let V_chi be the chi-eigenspace of V for Z. It is a G-submodule and contains v. If N_J denotes sum_{j in J} j, then N_H v=42v, which is nonzero in characteristic zero.

For any subgroup J with index below48, choose a nonidentity z in J intersect Z. Faithfulness gives chi(z) !=1. For every x in V_chi, N_J x is J-fixed and still belongs to V_chi. Hence

N_J x = z N_J x = chi(z) N_J x,

so N_J x=0. Every term a N_J b with a,b in K[G] also annihilates V_chi, because the latter is G-stable. Therefore no identity

N_H = sum_i a_i N_{J_i} b_i

can hold in K[G] if all [G:J_i]<48: its right side kills v and its left side does not. In particular there is no rational generalized norm relation of that form, even before asking for a seven-integral denominator.

The same central-character argument explains why norms to proper scalar-fixed subfields alone cannot retain the faithful source. It does not assert that its seven-class group is nonzero. It says this family of norm reductions has no access to the character that must be controlled.

## No class conclusion from the failed certification

The previous `bnfcertify(B,1)` log records an alarm before the required completion marker. Neither a successful quotient theorem nor a numerical bound for an unrepresented class quotient follows. Known principal-ideal relations and the authenticated unit lattice can remain valid, but they do not establish that the tested ideal classes generate the full ordinary seven-class component. The exact source remains

0 -> U^chi -> H_0^chi -> Cl(A)[7]^chi -> 0.

The previously proved joint kernel on U^chi is zero and the valuation contribution is zero. Thus K injects into Cl(A)[7]^chi; this screen does not further bound the latter.
