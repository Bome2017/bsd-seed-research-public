# WC integral-descent verdict

**WC_REDUCED_TO_EXPLICIT_LEMMAS**

The source and maps have been constructed. The uniform arithmetic bound has not been proved. This classification means an explicit structural reduction; it does not claim lower mathematical difficulty or FIN closure. The user's ordinary-prime equivalence gate shows why that distinction is necessary.

For the unchanged seed E: y^2=x^3-22735x^2+106272484x, the top level remains FULL BSD = RANK AND FIN AND FORMULA. RANK is closed. FIN and FORMULA remain open.

## Main result and research pivot

At every good ordinary p outside S0={2,3,5,2243,4547,5843}, a depth-zero Ota witness exists if and only if Sha[p^infinity]=0. The converse is a deduction from Kim 1.10 and Castella-Sano B with seed hypotheses checked; Kim's two-dimensional localization isomorphism supplies Ota's cyclic auxiliary-prime condition. Thus the ordinary tail of WC expresses the ordinary vanishing tail of FIN. It is not an independently weaker arithmetic structure just because WC is weaker than LINE.

The session nevertheless produced concrete, pre-FIN mathematics:

- A fixed finite integral homology source and explicit specialization to the exact Ota classes.
- An exact reduction of optimal witness depth to conductors with at most two prime factors.
- An integral isomorphism for Ota's local regulator, of index one for every relevant p,S.
- A single fully specified remaining arithmetic statement UC on evaluated weighted-cycle ideals.

Read the dedicated proofs HOMOLOGY_SOURCE_THEOREM.md, TWO_PRIME_SUPPORT_THEOREM.md, LOCAL_REGULATOR_ISOMORPHISM.md, ORDINARY_CONVERSE_GATE.md and INTEGRAL_COMPARISON_ATTACK.md. These are mathematical deductions with named imports, not kernel certificates or novelty claims.

## The twelve requested answers

1. **Exact antecedent.** There exists A in Z minus {0} such that for every p outside S0 some admissible squarefree S has nonzero t(p,S) in I_S^2/I_S^3 with depth at most v_p(A). Zero has infinite depth. EXACT_WC_ANTECEDENT.md preserves the predecessor statement. Excluded-primary finiteness is required separately for global FIN.
2. **Actual source.** M_Z=Hom_Z(H_1(X_0(N)(C),Z),Z), finite free, with z_E the period functional of a modular parametrization divided by Ota's real period. It is defined before FIN and is primitive at odd p using the retained optimal-quotient/isogeny data.
3. **Exact map.** phi_{p,S} evaluates z_E on integral cycles obtained by weighting paths C_{a,S} with binom(log_ell(a),2) and log_ell(a)log_m(a), then divides by the p-unit c_E. The resulting diagonal and mixed coordinates are exactly t(p,S).
4. **Uniform control.** The local Kato-to-group-ring regulator has integral index one. The evaluated global weighted-cycle image has no proved uniform bound. Source primitivity and local perfectness do not fill that gap.
5. **First missing lemma.** UC: for every p, at some k the explicit image D_{p,k} of the evaluated cycle map Psi_{p,k} in R_k=Z/p^k is nonzero, and R_k/D_{p,k} is killed by one fixed nonzero integer A. U1 proves this is equivalent to the exact WC antecedent. UC itself is unproved and its ordinary depth-zero part is equivalent to primary vanishing.
6. **Formalizability.** The conditional ideal, depth, support-reduction and coefficient-isomorphism algebra is formalizable now. UC's arithmetic proof is missing. Full homology/local-duality instantiations have not been put into Lean. A compiled interface must retain those hypotheses and the user's warning.
7. **Auxiliary choice.** Yes: the best depth is attained using one or two primes, and Chebotarev provides many eligible primes. This does not force nonzero evaluated cycles. At ordinary p, the primitive witness existence theorem uses primary Sha vanishing as its converse hypothesis.
8. **Older objects.** The Manin/isogeny work materially removes denominators from the constructed source. Kato supplies integral classes. Lane 2, H9, H41, 62a1/66b1 and post-FIN BKS realizations supply no proved uniform image bound for this seed. The precise H9R23 coefficient-map obstruction stays in force; exterior contraction is not excluded by it.
9. **FIN executable?** No. No A was constructed, no new h_p value was computed, and finiteness at 2243,4547,5843 remains open. The positive-depth ordinary converse for the exact cyclic auxiliary subset is not fully transferred from the broader printed Kurihara prime set.
10. **FORMULA.** No new closure. The certified real interval is retained. COMMON_B_PIVOT.md preserves bounded rationality, bounded algebraicity and the one-sided rational B criterion. A rational B>0 with q=4B and finite primary orders bounded by v_p(B) would force B=9, #Sha=9 and q=36. Neither comparison is supplied by the source constructed here.
11. **Next premium session.** Require a concrete pre-FIN class and a proposed arithmetic/real comparison for the common-B target before committing another session. If none is available, no further generic source-packaging session is justified. The remaining positive-depth prime-set transfer can be checked separately; it would clarify equivalence, not prove FIN.
12. **No more resources for.** Generic denominator/finite-generation arguments, Hecke-span closure, local-regulator reproof, renaming ordinary FIN as WC, the killed H9 coefficient map, p=5 replay, new 7/23/29 or bad-prime campaigns, or more analytic digits without a theorem that needs them.

## Formalization and provenance boundary

> Formalizing WC proves only the implication from the stated witness-content antecedent. It does not establish that the antecedent is easier than FIN or that FIN has been reduced.

The source-only arithmetic research and required report are complete. All named files are in this directory and bound by MANIFEST.sha256. Bounded group-algebra checks passed; they prove no seed arithmetic. The predecessor's 27 manifested outputs were checked, and no predecessor source was edited. The p=3 theorem retains its original Skinner/Jones/period provenance qualifications. The latest Opus replay was user-reported and not inspected here. No Aristotle package, other task, large prime computation or paper was launched.
