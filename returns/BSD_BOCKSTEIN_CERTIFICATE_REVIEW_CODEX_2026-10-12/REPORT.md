# Reviewed Bockstein certificate and its arithmetic continuation

2026-10-12. **REFINEMENT_SUPPORTED_UNDER_RETAINED_INPUTS; PRIMITIVE_TARGET_IDENTIFIED; MATCHED_HEIGHT_RATIO_DERIVED; NO_NEW_SEED_VALUE.**

The uploaded exact-content argument survives separate same-team mathematical review and replay of its supplied controls. I also pushed its main unfinished interface: the primitive target of the Bockstein can be identified from the known point lattice and the retained duality sequence. Combining this with the specified BKS height comparison removes the separate logarithm and cofactor contents from the ordinary numerical target.

The resulting ordinary sufficient test is

\[
K_p\ne0,\quad \det H_p\ne0,\quad
0\le v_p(K_p)-v_p(\det H_p)\le1
\quad\Longrightarrow\quad\Sha(E/\mathbf Q)[p^\infty]=0.
\]

Here **K is the actual transported, smoothed Kato coefficient and H is the matched height matrix in the U=gamma−1 coordinate**. An arbitrary modular-symbol coefficient or numerical height matrix cannot be substituted. This is a written conditional deduction, not a computation of K, a new uniform estimate, or a proof of BSD.

## 1. What passed review

For the nonzero specified derivative, the uploaded proof establishes

\[
m_p=\operatorname{length}\Sha[p^\infty]+w_p+b_p+e_p,
\qquad e_p\ge0.
\]

It retains the actual finite-free complex, the primitive torsion-free target of the first Bockstein, and finite specialization errors. The defect is the valuation of the augmentation of the full Kato characteristic quotient; it is not presumed zero. Thus

\[
\delta_p\ne0,\quad m_p-w_p-b_p\le1
\quad\Longrightarrow\quad\Sha[p^\infty]=0.
\]

The all-height-one inequality really is needed at every height-one prime. The review adds a control where the inequalities at both (p) and (U) hold but omission of (U+p²) produces a false result. It also shows that e can be positive even when the quotient has no factor (p). These are algebraic scope controls, not seed examples.

See [algebra audit](ALGEBRA_AUDIT.md) and the unmodified [submitted proof](submitted/BSD_BOCKSTEIN_CORRECTED_CERTIFICATE_2026-10-12/PROOF.md). The prior Kato/source, local-duality and saturated-basis inputs retain their earlier grades; this review does not re-certify that whole chain.

## 2. The primitive target can be specified without knowing Sha's order

Let W be the full point lattice, let

\[
L=(\log(P_1)/p,\log(P_2)/p)=p^w L_0,
\]

with L0 primitive, and set Qfine=ker(L0:W→Zp). The retained duality gives, once nonzero delta supplies primary finiteness,

\[
0\to\Sha[p^\infty]^\vee\to H^2_S\to K_{\rm MW}^\vee\to0,
\qquad K_{\rm MW}^\vee=W^*/\mathbf Z_p L.
\]

The torsion maps onto the torsion of the last term. Passing to torsion-free quotients therefore gives actual integral isomorphisms

\[
(H^2_S)_{\rm tf}\simeq W^*/\mathbf Z_pL_0
\simeq\operatorname{Hom}(Q_{\rm fine},\mathbf Z_p).
\]

There is no unknown Sha-order factor in these isomorphisms. In point coordinates, a primitive generator of Qfine is

\[
q_{\rm fine}=(-\log(P_2),\log(P_1))/p^{1+w}.
\]

This is generally a p-adic point combination, not one rational point. It is enough to specify the primitive target lattice. It does not assert that Qfine is the kernel of the Bockstein; they are different maps.

BKS Lemma 5.8 identifies the rational Bockstein with the height functional restricted to this fine point line. Using the integral target just identified gives the primitive row from the **BKS height in the U-coordinate**. For a height instead expressed through the scalar cyclotomic logarithm, divide by log_p(chi_cyc(gamma)); that number has valuation one. This division changes the height coordinate, not the Kato source. The exact source and convention requirements are in [the arithmetic interface](ARITHMETIC_INTERFACE.md).

## 3. The corrected ordinary target is a correlated ratio

Retain the earlier source-matched Rubin identity

\[
H_p(A_p,B_p)^t=\epsilon_p K_p\ell_p,
\qquad \ell_p=(\log P_1,\log P_2)^t,
\]

and assume the height matrix is nonsingular. Write r=v_p(det H) and c=content_p(adj(H)ell). Since H is symmetric and the primitive fine vector is Jell/p^(1+w), the Bockstein row calculation gives

\[
c=1+w+b.
\]

Substituting into the retained derivative formula yields

\[
\boxed{m-w-b=v_p(K)+v_p(\epsilon)+1-r.}
\]

At non-anomalous ordinary primes, v_p(epsilon)=−1, hence

\[
\boxed{v_p(K)-r=\operatorname{length}\Sha[p^\infty]+e.}
\]

This is the corrected ordinary test stated above. Neither logarithmic primitivity nor a unit height determinant is required. The numerator and determinant must be controlled together. A finite source defect remains, and the assertion is sufficient, not necessary, for vanishing.

For a matched supersingular root the retained prefactor has valuation zero, so the expression is v_p(K)+1−r in that root's height convention. This does not authorize importing the ordinary numerical engine. If H is singular, the determinant ratio is unavailable; the original cohomological corrected-content certificate still makes sense.

The K≠0 branch is not circular: the retained Rubin comparison proves delta=0 ⇒ K=0 without assuming primary finiteness. Nonzero K therefore gives nonzero delta first; the existing argument then supplies the primary finiteness used above. This uses the retained case-split proof, not deletion of BKS's finiteness hypothesis.

## 4. Existing seed evidence and the actual next arithmetic

The saved Exit 1 producer reports raw height-row valuation one on its ordinary panel. After division by the cyclotomic logarithm this corresponds to b=0. Such rows gain no new prime coverage from the correction. This run read the producer and summary; it did not replay its height computations. The producer's printed exclusion label is broader than its implemented filter; the arithmetic-interface note records that discrepancy. The old claim that these heights by themselves make delta_17 primitive remains unsupported.

No new actual Kato coefficient or derivative coordinate was recovered. The next substantive input remains a source-authenticated nonzero K and an upper bound on its valuation relative to the matched determinant, or a direct bound on m−w−b. The current CM control comparison is not such a seed input; its further comparison to the seed's actual Kato class remains separate.

This refinement should serve as the acceptance test for that arithmetic work. Re-proving the matrix identity, requiring separate unitness of the point logarithms, or rescaling the source by p would not supply it.

## 5. Verification and custody

- The supplied ZIP hash is `c35f5f04edc67d7e041fb062c5208ce254b979d24e39aebf88eefcc0fa7f068b`.
- All 15 entries in its manifest verified; there are 16 ZIP members including the manifest. Seven pinned lab Git-blob bindings matched the local pinned commit exactly.
- The supplied 864 first-jet checks (including 576 basis/gauge variants), 360 source-defect controls, nine boundary cases and five malformed-input cases replayed. The three regenerated output files matched byte-for-byte.
- Thirty-six separate exact rational controls verify the height/cofactor cancellation, including nonprimitive log vectors and Bockstein rows; splitting-change and singular-height controls are included. These are not seed computations.
- The two review agents are part of this same AI session. This is not independent human review or formal verification.
- The attached ZIP contains no Git patch. The claimed separate patch was not supplied here, so its `git apply --check` result is not independently verified. The archive is preserved unchanged; publication is assembled additively from inspected files.

## 6. Endpoint disposition

**FIN, ORDER9 and Q36 remain unchanged.** There is no new primary result, all-prime bound, actual coefficient, or certification of the named exceptional primes. The cohomological criterion retains its good-prime domain outside {19,59,487} and all source/smoothing qualifications. This return strengthens and source-specifies a usable conditional certificate; it does not establish the arithmetic premise.

Primary comparison source: [Burns–Kurihara–Sano, §5.2 Lemma 5.8 and the cyclotomic coordinate map (5.3.2)](https://arxiv.org/html/1910.07404v2). Its height compatibility is used with the retained finiteness-free case split and the integral target deduction here; its conjectural leading-term identity is not assumed.
