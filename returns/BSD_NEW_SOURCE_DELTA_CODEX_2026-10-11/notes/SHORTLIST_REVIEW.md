# Independent source-interface review of the shortlist

Date: 2026-10-11. Scope: a separate model-agent read of primary statements and the two new source notes, not an independent human review or a full proof audit.

## Verdict

The relevance claims in `EXTERNAL_PREPRINTS.md` and `OXFORD_DELTA.md` are appropriately limited. Neither the Loeffler–Zerbes index theorem nor the thesis's integral theta construction supplies the seed's missing arithmetic estimate. Both can be retained as newly inspected **comparison technology**, with the following qualifications attached to every proposed use.

## Loeffler–Zerbes, arXiv:2511.08793v2

Read Definition 6.2, hypotheses in §6.2, Theorem 6.8, the index definition preceding Lemma 6.11, Theorem 6.15, Remark 6.16, Proposition 6.17, and the beginning of §8.3 in the bound primary HTML.

The actual inequality is

\[
\operatorname{length}_{\mathcal O}H^1_{f\mathcal F}(\mathbf Q,T^\vee)
\le \operatorname{ind}_{\mathcal O}(\kappa_1,H^1(\mathbf Q,T)).
\]

Here `ind` is the largest power of the uniformizer dividing the supplied class, not a separately evaluated numerical invariant. The paper **bounds a dual Selmer group in terms of this content; it does not bound the content**.

Three comparisons are indispensable:

1. **Class:** `kappa_1` comes from the actual tame Euler system of Definition 6.2, with norm relations at all required squarefree conductors. The seed's divided cyclotomic derivative `delta_p = aug(z_infinity/U)` is not identified with this input merely because both are cohomology classes. No division by U at all tame conductors, compatible with every norm/local condition, has been supplied by this paper for the seed.
2. **Local conditions:** propagation to the ultra-Kolyvagin classes uses Theorem 6.8 and closedness of the local subspace in the relevant Banach topology (Hyp4), in addition to the image/cohomology hypotheses displayed with Theorem 6.15. One must keep those source conditions, rather than citing just its final displayed inequality.
3. **Target and index:** the dual modified Selmer group must be compared to the actual seed group and its local correction. The source theorem does not identify its length with `length Sha[p^infinity] + w_p`, nor identify its index with `m_p - w_p`. The existing seed comparison cannot be silently replaced by a new normalization.

Proposition 6.17 makes the restriction particularly visible: under its core-rank-one local dimension hypotheses, a nonzero `kappa_1` forces the source Selmer group to be rank one. The classical rank-two Mordell–Weil plane prevents simply substituting the seed's usual full source Selmer group and declaring its derivative to be this initial class. A new derived-system or local-condition comparison would have to explain the distinction.

Section 8.3 explicitly keeps the local H² term and a saturation-quotient term. Its analytic characteristic-ideal machinery must not be advertised as automatically controlling the integral height-one prime `(p)` or the seed's finite specialization errors.

**Allowed description:** a new-to-reading-record nonordinary local-condition and Euler-system index-bound toolkit. **Not allowed:** a new bound on the seed derivative's excess content, or proof of supersingular FIN.

## Sangiovanni Vincentelli thesis, Theorem E

Read printed pp28–33, including the definitions immediately preceding Theorem E and the author's period warning. The new note also independently records its later construction theorems; this review does not re-audit their proofs.

Theorem E concerns a Hecke character `mu` of infinity type `(1,0)`, an odd prime inert in the imaginary quadratic field, and a canonical CM pair. Its theta class belongs to the **CM part** of modular-curve cohomology, tensored with the inverse CM character. The absolute lift and de Rham realization are substantive source construction. They are not yet classes in the non-CM seed's Tate module.

A direct characteristic-zero Hecke projection of the same CM eigenspace is not the required non-CM seed construction. The proposed application first needs the actual pullback/product/pushforward operation (the thesis discusses replacing one Eisenstein factor in a Kato-style construction by a theta factor), then projection and integral control. Congruences modulo p cannot be used to bypass that characteristic-zero operation without another theorem.

The author explicitly warns on printed p29 that finite-character interpolation formulas for the Schneider–Venjakob big logarithm had not been established in that work; the periods `Omega_chi^univ` are ad hoc and their equality with the periods in the interpolation formulas needs verification. The claim that the resulting two-variable Euler system should recover Kato by Siegel–Weil is a proposed continuation in this introduction, not a theorem imported by Theorem E.

Therefore:

- integrality of the constructed theta source does not imply primitivity of a projected seed class;
- the de Rham comparison does not establish a p-unit comparison with the project's normalized derivative;
- the inert-prime theorem alone does not cover all coefficient primes;
- nonvanishing in its stated CM module does not prove nonvanishing after the needed non-CM arithmetic operations.

**Allowed description:** an overlooked concrete source construction that can replace an in-preparation-title placeholder, and a precise period/interpolation comparison to investigate. **Not allowed:** an already matched seed Kato source, a fixed rational tame scalar, or a new primary bound.

## Publication and reading scope

Both notes already preserve these boundaries. No correction to their mathematical status is requested. This independent interface check does not certify either paper or thesis. It does not change FIN, ORDER9 or Q36.
