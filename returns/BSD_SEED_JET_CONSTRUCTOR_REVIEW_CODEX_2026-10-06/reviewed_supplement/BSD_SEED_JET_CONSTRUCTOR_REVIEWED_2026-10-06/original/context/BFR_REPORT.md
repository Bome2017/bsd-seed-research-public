# Independent review of Aristotle's BSD return

Date: 2026-10-06. Status: **BFR_CONFIRMED_UNDER_RETAINED_INPUTS_WITH_CORRECTIONS**.

**Aristotle produced a valid extension of the forward receiver to the three bad
coefficient primes. It did not produce the independent bound needed to settle
any primary component, uniform FIN, ORDER9, or Q36.** Its four submitted Lean
modules compile in this review, with the scope described below. This is a
model-based independent review, not a human referee report or a formal proof of
BFR.

Input: `13920c22-e3bc-4dfb-a137-cf15033983a9-aristotle.tar.gz`.
SHA-256: `654c743693b33df14ac4e80db51cf27910d8981f93a3156c6c18bbaadb4e4bca`.

## 1. Accepted mathematical result

Use exactly the field and curve in the submitted proof. Let
\(V=E[p]\), \(A_p=\mathrm{Cl}(\mathcal O_{L_p}[1/p])/p\), and
\(B_p=\operatorname{Hom}_{\Gamma_p}(A_p,V)\). For
\(p\in\{2243,4547,5843\}\), restriction induces

\[
\Sha(E/\mathbb Q)[p]\hookrightarrow B_p.
\]

Consequently, if \(s_p=\dim_{\mathbb F_p}\Sha[p]\), then
\(p^{2s_p}\mid\#\mathrm{Cl}(\mathcal O_{L_p}[1/p])\).
Using the explicitly retained even-parity input, either
\(\dim B_p\le1\) or \(p^4\nmid\#\mathrm{Cl}(\mathcal O_{L_p}[1/p])\)
would force \(\Sha[p^\infty]=0\). Neither sufficient hypothesis is proved.

The residual-image theorem A.3, saturated basis R.1, Tamagawa data A.1, and
parity remain imported at their existing grades. I checked the statements of
these imports against the bound release record; I have not recertified their
entire evidence chains. Standard Galois cohomology, Kummer sequences and class
field theory are mathematical imports, not newly formalized declarations.

## 2. Load-bearing checks

| Step | Review | Reason |
| --- | --- | --- |
| Local line at 2243, 5843 | Confirmed under retained local data | The indices of \(E_1\) are 2242 and 11688, respectively, prime to the coefficient prime. The formal point \(R_p\) is primitive. |
| Local line at 4547 | Confirmed | \(E_0\simeq\mathbb Z_p\), \(E_1=pE_0\); \(P_2\) has nonzero smooth reduction and generates the local quotient. The auxiliary \(R_p\) has zero Kummer class here. |
| Global restriction kernel | Confirmed | Inflation-restriction and the central scalar give kernel exactly the two known point directions. The third, quadratic-twisted translation constituent can be zero without affecting this argument. |
| Unramifiedness away from p | Confirmed | Tamagawa factors are p-units. Kummer classes of the identity component become trivial on inertia after passing to the division field. Extra ramification of the quadratic field does not invalidate restriction. |
| Splitting at p | Confirmed | The local generator is divided in each completion of \(L_p\): use \(Q_3\) at the multiplicative primes and \(Q_2\) at 4547. |
| Class-group injection and exponent | Confirmed | Class field theory gives the p-inverted receiver. Independent equivariant maps give a quotient \(V^{s_p}\), of order \(p^{2s_p}\). |
| Dimension at most one implies vanishing | Confirmed with parity import | Parity eliminates dimension one. Vanishing of p-torsion eliminates all p-primary torsion. |

The proof does not assume FIN, a nonzero Kurihara witness, a leading-term
conjecture, or the bound it is trying to obtain. It also does not prove a reverse
comparison at the bad primes. The correct conclusion here is an injection.

## 3. Corrections and repairs

### 3.1 Exact residue versus the submitted Lean assertion

The prose and assumptions identify the residue 1274 with
`Seed.Local.chainCert_true`. That theorem actually checks that the x-coordinate
difference is divisible by 4547 but not by its square, together with unit
denominator conditions. It does not state the exact residue 1274. The returned
Python JSON likewise reports the valuation, not that residue.

I independently obtained

\[
\frac{x([4546]P_2)-x(P_2)}{4547}\equiv1274\pmod{4547}
\]

by binary addition modulo \(4547^4\), checking every denominator. A separate
review-only Lean assertion in `audit/Audit.lean` checks the corresponding
projective congruence. It leaves the original submission unchanged. This repairs
the evidence attribution; BFR needs only valuation one.

### 3.2 A shorter independent verification at 4547

The additive local conclusion also follows from Pannekoek's Theorem 1. The
translation \(x=X+1516\) gives

\[
y^2=X^3+4547X^2-59129188X-161680134380.
\]

All coefficients are divisible by 4547; divided by 4547 the nonzero ones are
\(1,-13004,-35557540\). The equation remains minimal (its discriminant valuation
is 3). Since 4547 exceeds the theorem's exceptional primes, \(E_0(\mathbb Q_{4547})
\simeq\mathbb Z_{4547}\). Its index-4547 subgroup is \(E_1=pE_0\). The nonsingular
affine reduction of \(P_2\) is nonidentity, so it generates \(E_0/E_1\).
See [Pannekoek, Theorem 1](https://arxiv.org/pdf/1211.5833).

This independently supports the submitted computation and shows why the local
group structure itself should not be advertised as a newly discovered general
theorem. No literature-novelty claim for BFR is made.

### 3.3 Genus-two rejection needs a narrower argument

Different rational j-invariants establish that the two elliptic curves are not
twists. They do **not** establish nonisomorphism of their p-torsion Galois
representations. The submitted collision check skips this implication.

For these particular curves, the omitted claim can be repaired cheaply:

| Good test prime q | #E(F_q) | #E2(F_q) | a_q(E)-a_q(E2) |
| --- | ---: | ---: | ---: |
| 11 | 14 | 18 | 4 |
| 19 | 16 | 20 | 4 |

An isomorphism \(E[p]\simeq E_2[p]\) requires congruent Frobenius traces at each
common good prime different from p. Use q=11 unless p=11, then q=19. Thus there
is no such isomorphism for **any odd p**. These point counts are reproduced by
`independent_checks.py`. Together with irreducibility of E[p], this also rules
out a nonzero Galois-equivariant linear map E2[p] to E[p].

The repaired conclusion excludes that direct linear transfer. The separate
quadratic-character argument excludes the direct map from the anti-invariant
auxiliary-point constituent. Neither argument excludes every use of the genus-two
curve, its E factor, higher operations, or additional correspondences. The
statement that the whole source can only touch a summand carrying no Sha should
be withdrawn in that broad form.

### 3.4 Claim B.20 is a different theorem

B.20 is the existence of some unit Kurihara witness at every good prime. Its
bad-prime exclusions do not themselves describe the scope of the forward
receiver. The correct predecessor for BFR is
`context/FORWARD_RECEIVER_RETAINED.md`, which is explicitly good-prime only.
BFR does not extend B.20, construct a bad-prime witness, or prove its existence.

At 4547 the full third translation constituent is not established. The original
return correctly permits its degeneration. The old exact degree formula must
not be copied to that prime without an additional proof.

## 4. What was actually replayed

All four submitted modules were compiled anew with Lean 4.28.0. Their Mathlib
revision and all nine package revisions match the submitted lock file. Existing
compiled dependencies at those revisions were used; Mathlib itself was not
rebuilt. No returned compiled theorem files were reused.

The 27 selected theorem declarations, including the added residue assertion,
were checked with `#print axioms`. The receipt identifies their actual axiom
sets. No `sorryAx`, new project axiom, or native evaluation axiom is used by
these declarations. The submitted source has no `sorry` or `native_decide`.

The formal scope is concrete Weierstrass arithmetic, point membership/order,
Hensel square roots and p-adic norm statements, and a finite modular-arithmetic
certificate. In particular:

- Point membership is not a formal proof that the two points form a saturated basis.
- The finite 4547 algorithm is not formally connected to the p-adic group law.
  That connection and the formal-group consequence are written mathematical steps.
- No Lean theorem in this return proves the Selmer/class-group injection or a
  bound on Sha. BFR remains a written proof with explicit imports.

All three returned Python controls reproduce their saved JSON byte-for-byte.
The genus-two control uses randomly chosen rational inputs; those finite checks
are not the proof of its rational-function identities. Direct substitution
establishes those identities.

## 5. Custody and remote-runtime conclusion

The safe archive inventory contains 51 regular files. All 21 original delivery
manifest entries are unchanged. The 15-entry project manifest, 21-entry research
manifest, and 5,180-entry nested reading manifest verify. The four startup
reading-path hashes also agree.

The full reading ZIP arrived intact and the returned work cites concrete
material from it. Extraction, all-card reading and execution on the remote
service are reported in self-written receipts; no native service execution log
or Git history was supplied. The absent extracted reading tree is disclosed
and reconstructible. This is no longer just a tiny token test, but hashing the
corpus does not demonstrate that every historical file was read or understood.

## 6. Effect on the BSD objective

The result supplies a common *forward comparison* for the three outstanding bad
primes. It gives no upper control of the arithmetic receiver, even at one of
them. A future theorem valid at these primes could use it, but an unspecified
cofinite bound may still exclude all three.

The run therefore did **not** meet the principal research objective of supplying
an independent constraint on the infinite tail. There is no new settled primary
component. FIN, ORDER9 and Q36 are unchanged.

Keep BFR and the arithmetic files as reviewed supporting material. This return
does not justify a further job extending local cases, formalizing more of this
comparison, or computing the enormous class groups. Any next research job needs
a specific proposed source of upper control, whose successful conclusion bounds
the actual receiver or establishes an independent uniform witness theorem.
No such source was constructed in this review, and no new job was launched.

## 7. Primary-source checks and supporting files

For the away-from-p local condition I checked the Tamagawa comparison and
finite-coefficient statement in [Dainobu, Propositions 3.2 and 2.8](https://arxiv.org/pdf/2304.05035).
Their use is restricted to places different from the coefficient prime. The
submitted proof also gives the Neron-model/Hensel argument directly.

See `MATHEMATICAL_RECONSTRUCTION.md`, `CORRECTIONS.md`, `checks/`, and
`original_return/` for the reconstruction, original claims and reproducible
controls. The original tarball is archived separately; this compact review does
not duplicate the unchanged large input indexes or nested reading ZIP.
