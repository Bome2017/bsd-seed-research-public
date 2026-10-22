# Aristotle upper-control return: independent review

Date: 2026-10-06.

**Verdict: EXACTNESS_EXTENSION_CONFIRMED_WITH_CORRECTIONS; NO_NEW_UPPER_BOUND.**

The corrected argument extends the exact receiver comparison to every prime
\(p\ge5\) except 4547, under the retained seed inputs. At 4547 it gives an
error of dimension at most one. The return does **not** prove that arithmetic
control through the division fields is impossible or must come from elsewhere.
That claimed exhaustion of the method is withdrawn in this review.

This is an independent model review and a written repair. The full receiver
theorem is not a Lean theorem or a human-refereed result. No new primary
vanishing, FIN, ORDER9, or Q36 conclusion is obtained.

## Accepted statement

Keep precisely the submitted seed, fields, and coefficient action, and put
\[
B_p=\operatorname{Hom}_{\Gamma_p}
 \bigl(\operatorname{Cl}(\mathcal O_{L_p}[1/p])/p,E[p]\bigr).
\]
Under the full residual/Kummer image, saturated rank-two basis, local data,
and forward receiver inputs listed in the return:

* \(H^2(\Gamma_p,E[p])=0\) for every \(p\ge5\).
* Restriction identifies \(B_p\) with the pulled-back global Selmer space
  \(\mathcal S_p\), modulo the two rational-point directions.
* \(\mathcal S_p=\operatorname{Sel}_p(E/\mathbb Q)\) for \(p\ne4547\).
  This is a **global equality**, not equality of every local condition.
* Therefore \(B_p\simeq\Sha[p]\) for \(p\ne4547\), while
  \(0\le\dim B_{4547}-\dim\Sha[4547]\le1\).
* With the separately retained even-parity input,
  \(\dim B_p\le1\iff\Sha[p]=0\) for all \(p\ge5\).

The repaired proof is in [CORRECTED_PROOF.md](CORRECTED_PROOF.md).
The implication from vanishing p-torsion to vanishing p-primary torsion is
elementary and does not assume finiteness of Sha.

## What actually changed relative to the supplied history

| Component | Prior record | This return's accepted delta |
| --- | --- | --- |
| Finite-group H2 vanishing and global descent | Already proved in the supplied RECEIVER_DESCENT.md for the full twisted translation module | Reconstructed proof, allowing the twisted constituent to be zero; new Lean support for the no-lift step |
| Exact receiver at good primes outside 19,59,487 | Already in the reviewed local-exactness packet | Retained, not a newly discovered comparison |
| Coefficient primes 19,59,487 | Previously excluded from exactness | Exact local images of the known points remove the **global** relaxation error |
| Coefficient primes 2243,5843 | Reviewed BFR supplied the forward injection | Reverse comparison now established under the retained inputs |
| Coefficient prime 4547 | Reviewed BFR supplied the forward injection | Reverse error bounded by one; exact equality remains undecided |
| Independent upper control | Missing | Still missing |

The old RECEIVER_DESCENT.md even explicitly says that an independent proof of
an equivalent statement is admissible. The new return's claim that it could not
locate this comparison in the supplied record should not be retained unchanged.
This is a record comparison, not an exhaustive literature-novelty judgment.

## Corrections that matter

1. **Global versus local equality.** The opening statement of Theorem C is
   false as written. At p=19 or 59 and q=2243, and at p=487 and q=5843, its own
   proof uses a relaxed local condition. The global groups nevertheless agree:
   the nonzero local image of a known point and global duality remove the
   possible new global direction.
2. **The place 2.** The suggested ramified Tate-twist explanation is wrong for
   this seed. Exact arithmetic gives \(v_2(c_4)=4\), \(v_2(\Delta)=8\), hence
   \(v_2(j)=4\): reduction is potentially good, not potentially multiplicative.
   The required local vanishing follows instead from additive reduction,
   Tamagawa number 2, and the pro-2 formal group. This repair preserves the
   theorem.
3. **Supersingular centralizer.** Distinct inertia characters alone do not
   prove the asserted scalar endomorphism ring. Include Frobenius, which
   interchanges them: the full nonsplit-Cartan normalizer over Q_p has
   endomorphism ring F_p. This is the already retained Serre input.
4. **Relative Brauer localization.** The claimed injection of all
   \(H^2(P,L^\times)\) into the places above p is false. Localization over all
   places is required. The p-supported assertion is valid for the image coming
   from S-units, which is enough for the intended ambiguous-class discussion.
   [CORRECTIONS.md](CORRECTIONS.md) gives a counterexample to the printed
   assertion and the replacement.
5. **The Mordell–Weil kernel need not be a line.** The displayed space
   \(\ell_p\) has dimension \(2-\dim\operatorname{loc}_p W\), hence one **or
   two**. No simultaneous non-Wieferich theorem has been proved.
6. **No impossibility conclusion.** An exact arithmetic model of Sha does not
   make independent arithmetic bounds on that model circular. The tested
   formal sequences do not yield a bound; they do not exhaust class-group
   arithmetic.

The global-duality step agrees with the finite-module formula in
[Darmon–Diamond–Taylor, Theorems 2.18–2.19](https://www.math.mcgill.ca/darmon/pub/Articles/Expository/05.DDT/paper.pdf).
The corrected Brauer distinction is supported by
[Milne, Class Field Theory, III §1 and IV Example 2.14(e)](https://www.jmilne.org/math/CourseNotes/CFT.pdf).

## Independent checks

The three new Lean modules were freshly compiled with Lean 4.28.0 and the
submitted pinned dependency revisions, using existing compiled dependency
libraries. Mathlib itself was not rebuilt. The axiom audit is supplied with the
return. These modules check the no-lift lemma, exceptional-prime arithmetic,
and concrete Boolean evaluations; they do not formalize Galois cohomology,
class field theory, or the whole Selmer comparison.

The submitted local-image program reproduced. A separate implementation using
the multiplicative torus of the nodal reduction, without the submitted elliptic
addition routine, independently confirms all six nonzero local images.
The exact c4/discriminant calculation exposes and repairs the place-2 error.

The original archive is preserved. Its top-level 21-entry manifest and nested
project 15-entry manifest pass, but the research-return manifest has a stale
HANDOFF.md entry, and none of those old manifests binds all the new proof and
Lean files. The old build/axiom receipts also describe the preceding BFR return.
Fresh review bindings and replay outputs replace those receipts for this review;
the supplied files themselves are unchanged.

## Meaning for the BSD project

This return supplies a broader, checked comparison and more formally verified
supporting arithmetic. It does not move through the independent-bound step.
Do not launch another job just to finish the remaining 4547 reverse comparison;
that is not required for the retained sufficient vanishing criterion.

Keep the corrected exactness theorem available as an interface: a genuinely
independent bound on this class-group component would settle the corresponding
primary obstruction. No such bound is produced here, and this review supplies
no reason to declare all possible field-arithmetic methods dead. The distinct
source-construction jobs are not assessed or changed by this return.

Original archive SHA-256:
`f11c5378fd746cbf46ee2e22888e93d914929d23470e2f3c1f8090d126bcef71`.

Publication preserves research evidence; it does not promote this result into
the research release or imply any endpoint has closed.
