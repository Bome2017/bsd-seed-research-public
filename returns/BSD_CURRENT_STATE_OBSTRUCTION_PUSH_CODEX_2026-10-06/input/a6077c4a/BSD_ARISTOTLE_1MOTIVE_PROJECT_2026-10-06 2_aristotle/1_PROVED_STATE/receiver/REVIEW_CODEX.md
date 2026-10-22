# Review of the all-prime global receiver addendum

Date: 2026-10-06. **CONFIRMED_UNDER_RETAINED_INPUTS.**

The supplied argument is correct. It closes the remaining global comparison
at 4547 using inputs already available in my preceding review. Leaving that
global error undecided was an omission in my review, not a missing local
calculation that requires another research job.

The accepted statement is now

\[
\boxed{B_p\simeq\Sha(E/\mathbb Q)[p]\quad\text{for every prime }p\ge5,}
\]

with exactly the fields, coefficient action, class group and retained inputs
of the preceding receiver reviews. This is an independently reviewed written
deduction; the new step is not formalized in Lean.

## Why the additional step works

For p=4547, the preceding proof already shows that each c in the pulled-back
global space S_p is locally finite at every v≠p. The earlier BFR review proves
that the global Kummer class k of P2 spans the one-dimensional finite local
space f_p.

Every local Tate pairing of c with k away from p is therefore zero. Global
reciprocity forces the pairing at p to be zero too. Since k_p spans f_p and
f_p is its own annihilator, c_p belongs to f_p. Hence S_p=Sel_p. The retained
restriction sequence then gives B_p=Sel_p/W=Sha[p].

Neither parity nor finiteness of Sha is used in this step. Nor does it assert
that the whole pulled-back **local** subspace equals f_p. It shows that any
possible extra local direction is absent from the specified **global** space.

The two duality facts are applicable at additive reduction and at the
coefficient prime. I checked them against [Poonen–Rains, Proposition 4.10 and
the proof of Theorem 4.13](https://arxiv.org/pdf/1009.0287), with the principal
polarization and the odd-degree self-dual isogeny [p].

## Verification of the P2 input

The translated coefficients are

    4547, -59129188, -161680134380.

The discriminant valuation is 3, so this integral model is minimal; all its
lower coefficients belong to 4547 Z_4547. The reduction of P2 is the smooth
affine point (637,4153) on y²=X³. Thus P2 is in E0 but outside E1.
[Pannekoek, Theorem 1](https://arxiv.org/pdf/1211.5833) gives E0≅Z_p here,
since p=4547 is outside its small-prime exceptions. Reduction has index p,
so E1=pE0. The retained component number 2 is a p-unit. Consequently P2
generates E(Q_p)/p as required.

The supplied arithmetic program reproduced CHECK_RESULTS.json byte-for-byte,
including the normalized addition residue 1274. The replay was performed in
a separate directory; the input files were preserved. The earlier Lean
modules and original seed certificates were not rerun or promoted.

## What changes in the record

This addendum supersedes the remaining 4547 global-error qualification in
the report at commit 6c1cb9398ce6d4791fc7988ee18893cd74bc1cdf. It leaves the
other corrections in that review intact. The older sealed report remains
preserved as history.

An independently established dimension bound on B_p now transfers through an
exact identification at every p≥5. Under retained parity, an actual receiver
of dimension one is impossible, including at 4547. A selected-row containing
kernel may still be one-dimensional; it need not be the actual receiver.

This does not strengthen the previously sufficient threshold dim B_p≤1,
which already implied primary vanishing at 4547. No bound or new primary
vanishing has been proved. FIN, ORDER9 and Q36 remain unchanged. Orthogonality
against P2 is already satisfied by all Selmer classes, so repeating this
argument supplies no further constraint on their Sha quotient.

The addendum gives no reason to redirect any source-construction job. No
worker was messaged, interrupted, or launched in this review.

## Custody

Input ZIP SHA-256:
`fc843c8bfc3a7e9def27f97e800f4b57bc010e366b435f82341c063068e7fcc3`.
ZIP integrity and all 8 supplied manifest entries pass. All four referenced
Git blobs match the pinned commit, and the cited BFR archive hash matches the
published archive. Those four source documents are included in context/ for
offline verification. The two pasted attachments have identical contents.

This review verifies the short new deduction against its named inputs. It
does not claim to recertify the complete residual-image, basis-saturation,
parity, or class-field evidence chains, or establish literature novelty.
