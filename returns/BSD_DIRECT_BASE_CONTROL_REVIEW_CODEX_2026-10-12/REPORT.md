# Direct base control: checked map and conditional Kato bound

2026-10-12. **MAP_SUPPORTED; CLEAN_TAME_TARGET_MATCHED; CONDITIONAL_KATO_BOUND_AVAILABLE; NO_SMALL_VALUE_ESTABLISHED; NO_NEW_SEED_BOUND.**

The degree-p modification does reach the base seed's Sha. The fixed-quintic obstruction does not exclude it. This review also supplies an explicit domain on which its finite kernel is the standard Selmer group of an actual abelian variety, and checks a published integral upper bound for that group. It does not produce a value small enough to settle a coefficient prime or a cofinite family.

These are written deductions and same-team model reviews under retained inputs. They are not formal verification, independent human certification or a novelty claim. The original six-file submission is preserved unchanged in `submitted/`.

## 1. The submitted map survives

With the notation of the submission,

\[
\Sha(E/\mathbf Q)[p]\hookrightarrow K_{p,L}[\pi]/\operatorname{res}W_p[p],
\qquad\pi=\sigma-1,
\]

is canonical and needs neither base primary finiteness nor injectivity of restriction on Sha itself. It is obtained from restriction on Selmer p-torsion, followed by quotienting by the same two-dimensional point plane. [MAP_AUDIT.md](MAP_AUDIT.md) gives the proof and the exact possible local error.

The map cannot be promoted to an isomorphism merely from absence of global p-torsion. The error consists of globally realizable local norm defects, with a further p-torsion lifting condition. Both conditions are retained.

## 2. The target is an actual standard Selmer group on a specified domain

Let p>=5 be good for E. Choose a good prime ell!=p with ell=1 mod p, let L be the degree-p subfield of Q(mu_ell), and require p not to divide #E(F_ell). Require also p-unit bad-prime Tamagawa numbers; the retained seed values satisfy this for p>=5. These conditions do not assert the existence of a nonzero twisted value in this family.

Put B=ker(Res_{L/Q}E -> E). Its kernel is connected, its dimension is p-1, and its integral Tate lattice is

\[
T_pB=T_pE\otimes I,\qquad I=\ker(\mathbf Z_p[G]\to\mathbf Z_p).
\]

The local norm cokernels vanish on this domain. Consequently the written argument gives

\[
K_{p,L}=\operatorname{Sel}_{p^\infty}(B/\mathbf Q),\qquad
K_{p,L}[\pi]/\operatorname{res}W_p[p]\simeq\Sha(E/\mathbf Q)[p].
\]

No ordinary filtration or point-group equality is used. The result covers the indicated tame domain also when the coefficient prime is supersingular. At auxiliary primes with p dividing #E(F_ell), the local terms must be retained instead.

## 3. There is a published upper-bound theorem, not only a finiteness theorem

The [source calculation](INTEGRAL_BOUND_SCREEN.md) checks Kato Theorem 14.5(3), Proposition 14.16(2), and Proposition 14.21(1). Under their image and lattice hypotheses, with the exact trace-zero lattice transported to the twisted representation, they give

\[
\operatorname{length}_{\mathcal O}K_{p,L}
\le v_\pi\!\left(\frac{L(g^*,1)}{\Omega_{g,T}}\right),
\qquad\mathcal O=\mathbf Z_p[\zeta_p].
\]

Here the faithful twisted central value must be nonzero, g* is Kato's conjugate-coefficient form, and Omega_(g,T) is his period built from the actual integral Betti and strongly divisible de Rham lattices. Its normalization is part of the theorem, not a free choice. The residue field has size p, so the right valuation uses v_pi(pi)=1 and v_pi(p)=p-1.

The packet's sufficient length-two test therefore has a genuine source theorem behind it on this domain. What this review has **not** established is a computable seed/Gauss-period identification for that exact lattice and an arithmetic upper bound of two for its value. The tentative simultaneous motivic transport argument was not completed or promoted. A tame Gauss sum being a p-unit, by itself, does not finish the required simultaneous comparison.

The natural embedded map I -> Z_p[G] -> O is multiplication by pi after the abstract identification O=I. This does not obstruct choosing an integral isomorphism; it does forbid silently identifying separately embedded lattices and their source classes. The proof retains that distinction.

## 4. The numerical requirement is still absent

Length at most two forces Sha[p^infinity]=0 without parity or prior primary finiteness. Length at most three suffices only after explicitly importing the separately retained residual-parity input on the same domain. Finiteness of K alone supplies neither threshold. [MODULE_BOUNDARY.md](MODULE_BOUNDARY.md) gives explicit abstract controls and distinguishes generator dimension from total primary order.

No exact twisted L-value or local Kato index was computed in this review. No uniform valuation estimate was proved. No equivalence with the existing Ota witness was asserted. The source screen does not show that this criterion is easier to satisfy than the retained one.

In particular, proving a theorem for all but finitely many coefficient primes for one fixed extension would not control this diagonal construction: here the extension degree is the coefficient prime, and the extension changes with it.

## 5. Operational conclusion

The construction is not disproved. It is now connected to a genuine conditional arithmetic upper bound. It has still supplied no independent control of the size of that bound.

Do not launch another task merely to reprove the injection, standard-Selmer identification, or the consequence of a length-two value. A continuation needs an actual bound on the normalized value, or another independently bounded input controlling K. Completing a period comparison without that arithmetic would remain prerequisite work, not seed closure. The existing derivative-content target remains available; this review does not replace it with a proved easier target.

FIN, ORDER9, Q36 and base coefficient-prime coverage remain unchanged. No claim that the seed is nearly proved, or that it can never be proved, follows.

## 6. Custody and checks

The supplied ZIP has SHA256 `3574f7d56d1af2f3ba4e02b00d2b68b6dc03ecaa6bc90c9071a0de97814685e7`. All six files match author commit `3f49551ab14268be879eb7f31820aa604350d7e3`; all five manifest entries and four historical blob bindings verify. The supplied 351 finite-module controls reproduce byte-for-byte. These are abstract checks, not seed computations. See [INPUT_BINDINGS.json](INPUT_BINDINGS.json).

The map, module boundary and Kato source were examined separately by model agents and read by the parent. A further read-only check found no gap in the clean tame local norm argument. This is same-team review. No mathematical endpoint was upgraded. The final narrow period attempt was interrupted; its proposed conclusion is not part of this return.
