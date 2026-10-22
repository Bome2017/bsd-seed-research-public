# Bounded check of U22 engine Link 2

2026-09-29. **Overall: CONFIRMED_WITH_CORRECTIONS.**

Retain `OBSTRUCTION_FOR_THESE_MECHANISMS` only as a bounded insufficiency finding: the supplied constructions do not establish the requested independently normalized determinant relation. Several purported necessity arguments do not survive. In particular, this return does **not** prove that every successful comparison must assume a Selmer upper bound.

Return manifest **10/10** and task manifest **25/25** verified; Claude's pre-audit was also read and hash-bound. Inputs were unchanged. This check concerns the four requested questions, not a re-audit of Link 1, G2, Stage 1, or the coefficient family. Their grades and the task's H1/H2 assumptions remain in force.

## (1) Per-mechanism statements — CONFIRMED_WITH_CORRECTIONS

**M-a: retain the failure of the specified DKV transplant.** DKV's operators at local trivial-zero places provide a relation in their actual Hecke orbit; the supplied E-constituent has no corresponding slots on the retained domain. Their character calculation is not a theorem about the present rank-two constituent. [DKV, Theorem 3.3 and equations (34), (38)](https://arxiv.org/html/1605.08169).

Two corrections are necessary:

- SU's selected Hecke algebra does not **specify the needed bad-place operators or their action**. Its list of generators does not prove that no such endomorphism can ever exist or be constructed in a different algebra.
- At p, ordinarity kills the restriction after projection to the ordinary quotient. It does not make the entire restriction to `H^1(I_p,E[p])` zero. Narrow M-a item 4 accordingly. The missing exceptional-zero slot still blocks this transplant.

**M-b: the directions are correct under the named hypotheses.** For the same residual partition and a compatible surjection of pseudorepresentations, BC Proposition 1.5.1 gives `J_T = J_R T`. Consequently

\[
 R/J_R\twoheadrightarrow\mathbb T/J,
 \qquad \operatorname{length}(\mathbb T/J)\leq
 \operatorname{length}(R/J_R).
\]

This is a finite-length assertion only when those lengths are finite. Here `R/J_R ->> O` makes the right side infinite, so it supplies no numerical bound. BC's extension injection, followed by the stipulated local-condition comparison and R11, gives `r_E <= dim V`. BC identifies its image with extensions realized by the chosen Cayley–Hamilton quotient, not automatically all Selmer classes. [BC, Proposition 1.5.1 and Theorems 1.5.5–1.5.6](https://arxiv.org/abs/math/0602340).

The surjection and `R/I_R = O` alone cannot bound e. For example, formally take `R=O[[x]]`, `I_R=(x)`, and `T=O` via `x -> lambda^n`. Then `T/I_R T=O/lambda^n` for arbitrary positive n. This is a ring-theoretic illustration, not an automorphic counterexample.

**Withdraw the stronger M-b/M-d claims.** Neither `r_E <= dim V` nor BC proves that an exact comparison must assume `dim V <= 2`. Even that upper bound alone would not prove `r_E=2` without a lower bound. Likewise, `R=T` alone does not prove realization of all Selmer classes.

Most importantly, the asserted inclusion of a full `dim V`-dimensional extension space in the pseudodeformation cotangent space is unproved; the return's own SOURCES.md marks the calculation unchecked. Upper-triangular extensions with fixed diagonal blocks have the same trace and determinant regardless of extension class. Thus extension dimensions cannot simply be substituted for pseudodeformation tangent dimensions. This refutes the stated justification that M-d necessarily requires FIN as an input; it does not construct the missing deformation ring.

WWE's numerical criterion compares `length(I_R/I_R^2)` with a congruence ideal for **augmented finite-flat** algebras. Transplanting it requires those objects and a calculation; it is not the asserted Selmer-dimension criterion. Their surjectivity is established in Proposition 4.2.4, following Lemma 4.2.1. [WWE, §§4.2, 7.1](https://arxiv.org/html/1707.01894).

**M-c: the conditional lower-bound direction is correct.** SU's proof constructs an integral boundary lift F, then a cusp form `H = E_D - L_D F`; a primitive coefficient supplies the surjective linear functional. Its height-one theorem is not itself a closed-point primitivity theorem. At the specified point, retain the boundary lift and compatible action as well as H2-unit before using the argument. Distinguish the Eisenstein *form* in the nonvanishing hypothesis from the Eisenstein *ideal*. [SU, §6.5.3, Theorem 6.5.4 and its proof, pp. 98–99](https://www.math.columbia.edu/~urban/eurp/MC.pdf).

In an untruncated O-algebra this gives, with extended lengths if necessary,

\[
 J\subseteq I_D\mathbb T,
 \quad\mathbb T/J\twoheadrightarrow\mathbb T/I_D\mathbb T
 \twoheadrightarrow O/\lambda^r,
 \quad\operatorname{length}(\mathbb T/J)\geq e\geq r,
 \quad r=v_\lambda(L_D).
\]

But the return also says it works at truncated depth k. There the target is `O/lambda^min(r,k)`, and the valid lower bound is **`e_k >= min(r,k)`**, not an unbounded `e_k >= r`. Define the untruncated algebra if claiming the latter. Depth nine still distinguishes r=8 from r>=9 on the retained p>=11 domain.

Finally, BC's scalar ideal J is generated by **trace cycles**. The bare product `A_32 A_21` lies in the off-diagonal module `A_31`; it is not itself a scalar generator of J. The missing map from that corner to the pairing is not supplied by the ideal inclusion.

## (2) Kill criterion — CONFIRMED_WITH_CORRECTIONS

No actually developed mechanism in this return supplies an exact or two-sided relation joining Eisenstein depth to `det h` with independent unit control. That bounded failure is confirmed.

The stronger wording “none can force C2 nonzero without an upper bound on dim V” is not proved as a necessity theorem. M-d is an unconstructed transfer with an unchecked cotangent calculation, not a demonstrated obstruction. M-e's geometry is unscreened. BKS already relates the determinant and C2, but retains the uncontrolled factor.

Replace the summary by: **“The screened constructions, with the inputs established here, give no independent upper bound or unit-normalized identity forcing C2 nonzero.”** For example, an independently proved `e<=8`, combined with the conditional `e>=r>=8`, would force r=8. No such bound is supplied; its possible construction has not been excluded.

M-g's nonlifting statement concerns the **unrelaxed** derived Selmer filtration. It does not undo Link 1's corrected relaxed-lift construction on all V.

## (3) Scope — CONFIRMED_WITH_CORRECTIONS

Claude is right that V6, a geometric construction from P1 and P2, was **not genuinely screened**. Delete the claim that this unconstructed object could supply only `e<=r`.

Use “the required DKV-type operators and action were not constructed in this fixed setting,” not “operators which do not exist.” Use “none of the displayed boundary identities establishes the required determinant comparison,” not “no constant-term identity” or even “no automorphic-side identity” without that restriction.

Correct the BKS notation in RETURN.md, M-f and Claude's pre-audit: in `C2 = u*x_Q*#A_p*det B`, **u is the retained unit**; `u*x_Q*#A_p` is the potentially nonunit compound multiplier. It is this compound multiplier, not u alone, that retains the uncontrolled arithmetic information.

## (4) Interfaces I1–I3 — CONFIRMED_WITH_CORRECTIONS

**I1 is sufficient for finite support, not alone for full FIN.** With rank two and no rational p-torsion, Kummer gives

\[
 \dim_{\mathbf F_p}\operatorname{Sel}_p(E/\mathbf Q)
 =2+\dim_{\mathbf F_p}\Sha(E/\mathbf Q)[p].
\]

An upper bound two kills the whole p-primary group. Doing so outside a finite set leaves finiteness of each exceptional primary group to establish. The current ordinary, split-in-K domain also does not cover all but finitely many primes. Neither qualification disappears in this audit.

**I2 is an incomplete possible route, not a necessary-and-sufficient interface.** Realization, exact congruence depth and an additional pairing relation remain separate obligations; neither R=T nor exact depth supplies them automatically. A DKV-shaped operator construction is not proved to be the only option.

**I3 is a genuinely stronger, independent proof target than the retained factorization.** An identity `C2=u*det h` with an independently proved unit and an identified nondegenerate pair would imply nonvanishing. Merely renaming `x_Q*#A_p` as u does not do this. If the pair consists of unspecified Hecke classes, Link 3/nondegeneracy is still needed. An independent proof may conclude a statement equivalent in strength to Sha-vanishing; equivalence is not circularity. Uniformity and prime coverage remain additional obligations.

## Disposition and provenance

Keep the conditional inequalities and scoped non-result; correct the stronger claims together. This is not a clean confirmation of every argument in the return or pre-audit. It establishes no overlooked successful mechanism and does not authorize Link 3.

Sources were checked directly: pinned SU text; BC's cached primary PDF (SHA-256 `f593756809df6c39ee5cf83b7cce82965cebec55a075bd4c84430203394e1c34`); DKV arXiv HTML; WWE arXiv v3 HTML. Source numbering above is version-specific. Prior arithmetic certificates and Link 1 were retained, not replayed. `INPUT_BINDINGS.json` pins 36 input files. No prime computation, build, repository change, external message, or successor task was performed.

**FIN, ORDER9 and Q36 are unchanged.**
