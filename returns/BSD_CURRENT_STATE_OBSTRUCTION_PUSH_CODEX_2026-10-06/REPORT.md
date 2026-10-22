# Current state reconciled; an arithmetic Stage-A construction

Date: 2026-10-06.

**Result: STAGE_A_EXCESS_OBSTRUCTION_DERIVED; HIGHER_POINT_LIFTS_AND_UNIFORM_CONTROL_OPEN.**

I checked the newer lab history, the research remote, the recent Downloads
archive inventory, and the supplied OpenAI rank-two task. I then attempted
Stage A directly. The result is a written arithmetic derivation, requiring
independent review, of a universal first-order lifting-obstruction map whose
kernel is precisely the two known point directions. It uses actual tame
character extensions and the classical seed Selmer conditions.

This is not a claim that BSD has been proved, or that the full three-stage
proposal is known to work. FIN, ORDER9 and Q36 remain unchanged.

## 1. The proposal's first stage can be repaired

The prompt's scalar obstruction must be replaced by the actual lifting map

    b_lambda : Sel_p(E/Q) -> Sel_p(E/Q)^*.

Let D be the span of conductor-q additive characters, trivial at the old
places, with q=1 mod p and Frobenius -I on E[p]. These are actual arithmetic
characters. Define D^W by requiring that both known point classes lift in
the corresponding first-order extensions, equivalently b_lambda(P_i)=0.

The new derivation gives

    ker[Sel_p -> Hom(D^W,Sel_p^*)] = W_p.

It does not choose an unknown Sha basis or a complementary subspace to
define the map. The proof instead uses the cochain formula for the
generalized Cassels--Tate pairing, residual full image, commutators and
Chebotarev to show that the arithmetic pairings span all symmetric forms
needed to separate the quotient. A temporary basis of the full Selmer space
is used to prove a span statement, not to manufacture the map.

The supplied OpenAI obstruction-span lemma cannot simply be imported: it
works over a generic residual parameter field and in different strict/opposite
spaces. The new proof works directly over F_p and avoids that specialization.
It does not require ordinarity, so includes supersingular good seed primes
under the retained residual-image and saturated-basis inputs.

Read [STAGE_A_DERIVATION.md](STAGE_A_DERIVATION.md). This is a same-worker
written proof with named imports, **not** an independently accepted or
kernel-checked theorem. Its arithmetic steps, especially the exact local
conditions and the cochain/reciprocity calculation, are the priority review.

## 2. What the next stage now has to construct

Stage A preserves the point classes only to first order. It does not provide
two compatible point sections in a full arithmetic family. I wrote the next
equation explicitly. With c_i the point cocycles, a_i their first-order lifts,
and chi=1+t lambda+t^2 mu modulo t^3, it is

    d b_i = -lambda cup a_i - mu cup c_i,       i=1,2.

The character itself can be lifted to this order by mu=lambda^2/2; changing
mu by another admissible additive character supplies the correction terms.
Simultaneous arithmetic solvability with the required local conditions is
not established. This is the first concrete higher-order calculation to
perform before treating a rank-two determinant switch as available.

The final cross-prime requirement has not changed: an independent fixed
nonzero integer, or another proved uniform bound, must control excess at the
original seed specialization. Separation of hypothetical excess directions
is not a bound on how many exist.

See [NEXT_ARITHMETIC_STEP.md](NEXT_ARITHMETIC_STEP.md). No remote job or
fixed-prime campaign was started.

## 3. Updated project state, with the newer returns included

The lab was refreshed through remote commit **00f6d152**. During this review
three more commits arrived: both 1-motive returns and the OpenAI rank-two
admission package. They were integrated without dropping our preceding
review. Thus those two returns, initially found only in Downloads, are now
also in the lab. The current return does not duplicate them as new research.

| Material | Current conclusion used here | Grade/qualification |
|---|---|---|
| Research release v0.2.6, 8414aea | Rank two and settled primary information through 47; FIN/ORDER9/Q36 still open | Existing released claims, not re-certified in this pass |
| Research status branch 9ebaca3 | October 4 graded supplement; no new October 6 release promotion | Remote head checked |
| Receiver exactness | B_p is identified with Sha[p] for p>=5 in the retained reviewed state | Written deductions under retained global inputs; no upper bound |
| G2 and Theorem W | Nondegenerate tame regulator auxiliaries and auxiliary-independent per-p scalar are already available | Retained reviewed inputs; do not rederive G2 |
| K288 custody audit | Nine settled-prime residues and two p=5 checks match 288 in the stated convention | Existing recomputation receipts, not a cross-prime theorem |
| Revised Heegner returns | On the cofinite minimal-twist tail, nu_p=1+dim Sha(E)[p] | The permissive two-prime threshold does not weaken the cofinite target |
| Later W3 p17/p19 return | Reported p17 coefficients (0,0,0,0,13), p19 ell_2=18 | Floating-point source values, not interval-certified; p17 is already Sha-trivial |
| W3 p31 | The requested source quantity was not produced | No new certificate |
| Rank-two anchor / derived Gross returns | The tested anchor constructions did not give the missing global comparison; canonical anticyclotomic pairing on the rational plus-space vanishes | Scoped failures; not a theorem excluding every anchor |
| Two fixed 1-motive returns | A fixed receiver and determinant setup, but no unconditional canonical generator or cross-prime bound | Prose/retained-source grades; the recorded Lean builds cover supporting skeletons |
| OpenAI rank-two task | A legitimate new admission question; its generic-rank-one switch is not a rank-two switch | Task, not result; repaired Stage A is the work in this return |

The earlier-input Codex review is preserved as
`BSD_HEEGNER_JET_RETURN_REVIEW_CODEX_2026-10-06`. Its source-certificate replays
and p5 adapter control remain valid, but its proposed p17 extraction is
historical in light of the later floating-point return. Its Heegner tail
observation had also already been obtained by the newer workers. It should
not be presented as a new discovery after this refresh.

## 4. Corrections that must travel with the new task

1. **The target of a lifting obstruction is not automatically a scalar.**
   The canonical pairings in Stage A retain a whole second Selmer argument.
   Requiring two scalar evaluations to vanish is not enough to preserve two
   point classes. Our D^W imposes their full obstruction vectors.
2. **The record uses different division fields.** For M=[Z^2 -> E],
   Q(M[p])=Q(E[p],p^-1 P1,p^-1 P2). The exact class-group receiver in the
   retained proof uses the larger field with the quadratic field F_p and a
   division point of its auxiliary R_p as well. The two are not literally
   the same field. This corrects the displayed identification in both new
   1-motive returns and in pre-check 3 of the OpenAI task. Abstract comparisons
   through Sha[p] do not need that false field equality. The present Stage-A
   proof uses neither class-group field as its definition.
3. **Split-prime restriction is not automatically deformation obstruction.**
   Chebotarev in a division field can separate cohomology restrictions. The
   new deformation proof needs the additional cochain pairing calculation;
   our deformation primes have invertible Frobenius-minus-one instead of
   identity Frobenius.
4. **A known-good false alarm does not refute a one-sided detector.**
   The reported p17 wild-regulator phenomenon does not by itself disprove
   any cofinite one-sided W3 bound. It prevents silently identifying that
   wild value with a tame scalar which is a unit at 17.
5. **No universal nonexistence conclusion.** Failure of the tested 1-motive
   element or the known rank-one anchor does not prove every possible
   arithmetic generator or rank-two anchor impossible. The MCS height
   identification and other imports keep their stated review boundaries.

## 5. Custody, checks and coverage

The Downloads scan inventoried **67 selected archives**, including historical
versions and other projects. After the concurrent sync, **21** have exact
archive-byte matches in the lab. Selected report bodies were also compared
with tracked Git blobs, since a differently packed archive can contain
already-published material. The remaining filenames are not all new BSD
results. Older September returns carry obsolete settled-prime lists and
thresholds; those were not promoted over the current frontier.

This is not a claim to have independently read or re-proved every file in
the terabyte-scale project. [DOWNLOAD_INVENTORY.json](DOWNLOAD_INVENTORY.json)
records the actual archive/body coverage; [SOURCES.md](SOURCES.md) identifies
the primary-source sections and current reports used in the mathematics.

Both new 1-motive inherited manifests replay **47/48**, with README the sole
mismatch. That agrees with the already-published banner explanation. New
output files are separately bound by this return's own manifest. No new Lean
build of those runs was performed here.

The new standalone checker verifies 20 symmetric-span/quotient-kernel
controls over five finite fields and 845 order-three character identities.
It also checks the explicit first-order-versus-generic-rank countercontrol.
Those are algebra controls, not computed seed Selmer groups and not proof
certificates for global reciprocity or Chebotarev.

Publication goes to the lab only. No research-release theorem promotion,
Aristotle submission, external message, paid compute or primary campaign is
part of this return.
