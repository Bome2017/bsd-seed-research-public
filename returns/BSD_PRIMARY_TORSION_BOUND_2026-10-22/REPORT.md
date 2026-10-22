# Primary-class continuation and public research edition

Started October 20; resumed and completed October 22, 2026.

**Direct primary-torsion construction tested; no improved small class bound.**
The new source experiments supplied on October 22 were reviewed and used to
exclude repeating their tested families. FIN, ORDER9 and Q36 remain open.

## What was executed toward FIN

The previous complete relative-five class-length ceiling is 97. The remaining
source bound needs the relevant faithful class contribution, compatible with
unit/global/local constraints, to be much smaller. This run tested a different
construction that bounds primary torsion directly rather than the entire class
group or the rank of a selected relation matrix.

For the actual degree-24 seed point field A and its scalar-minus-one fixed
field K of degree 12, exact maximal-order ideal decomposition finds:

| Tested prime window | Exact split pairs | Meaning |
| --- | ---: | --- |
| Relative theorem's preprint window, norm below delta^(1/20) | 2, both norm 7 | Actual eligible inputs for a relative torsion construction. |
| Original Ellenberg–Venkatesh wider window, norm below delta^(1/10) | 26 | Inputs to its absolute-class estimate; that numerator cannot be replaced by the relative one without a proof. |

Here delta=707033045140895852346320. The strict integer cutoffs are 15 and
242. Independent K-prime quadratic-residue tests, seed point counts and a fresh
exact replay agree. These counts are not class ranks or authenticated
independent class generators.

## An explicit bound, with its unit error retained

The published estimates hide constants and have a degree-convention discrepancy
between versions. Instead of assigning those constants convenient values, the
theory calculation writes a finite norm-one Arakelov packing argument directly.

It retains the kernel between norm-one principal ideals and ordinary relative
classes. That kernel is 2-primary, so it does not change the 5-torsion, but it
must still be included in the volume calculation. Its unit index cancels against
the relative regulator index, giving a controlled volume. A discriminant
separation calculation then proves disjointness of actual balls coming from the
small split-prime pairs. No known seed Sha value or GRH is used.

For all thirteen tested common-radius prefixes of the 26 pairs, the strongest
result occurs at the two norm-7 pairs. The exact checker gives

    dim_F5 ker(Cl(A) -> Cl(K))[5] <= 106.

This contains both faithful character sectors and includes undiscovered
classes. It is a bound on the **five-torsion dimension**, not a bound of 106 on
the length of the entire five-primary group. The earlier length ceiling 97
already gives a better dimension bound. Thus the new construction does not
improve the class allowance; it is not a FIN advance.

See `theory/EXPLICIT_PRIMARY_PACKING.md`, `theory/PRIMARY_PACKING_RESULT.json`
and the separate same-session mathematical review. This is not human review or
proof-assistant certification. The proof grade and any retained qualifications
there govern this summary. Thirteen common-radius prefixes are not an
exhaustive search of possible Arakelov or character-specific arguments.

## Across-prime test

There is also an explicit limit on this particular packing budget. Retaining
the same analytic product estimate and the unit-lattice radius certificate
R <= lambda_p/2, its computed upper-bound expression satisfies

    B_pack >= 2 B_old / M.

Even granting every possible split prime in the wider tested range
X <= delta_p^(1/(2p)), the elementary bound M <= ((p^2-1)/2) X and the retained
discriminant contribution at 4547 give B_pack > p^4. This excludes obtaining a
class allowance at most three from this expression and norm window, even under
optimistic prime supply. See `theory/SCALING_LIMIT.md` and its separate review.

This is a lower bound on a proposed **upper-bound expression**, not on the
actual class group. It does not exclude other norm windows, stronger regulator
or separation estimates, nonuniform packing, or an independently controlled
character-specific kernel. No class group at p>5 was computed. This run supplies
no small bound across primes.

## What Pro's new packet contributes

`review/PRO_PACKET_REVIEW.md` records the scope of the review. All 45 uploaded
manifest entries match. This run independently reconstructed all 20,440 norm
inputs and small/discriminant-prime exclusions, replayed the direct-product
private-support verifier on all rows, checked 20,180 linear fifth-power
remainders, repeated 17 companion-matrix trace samples, and checked the
analytic-expression constants and derivation.

The supported conclusions exclude the tested Cayley multiplicative families
as sources of non-torsion ordinary units and show that the old whole-order
expression cannot itself become small enough. Neither exclusion says that the
actual class group is large. Those families and that finishing use of the
expression are closed for this search; no further enumeration was performed.

## Publication and evidence scope

The separately prepared public evidence edition collects the retained research
release, later mathematical returns, corrections, exact checkers and selected
data. Its public manifest is distinct from the historical packet manifests.
Private correspondence/history, third-party publication copies and specified
bulk inputs are excluded with a source/transformation ledger. Publishing the
record does not upgrade its mathematical grades or establish novelty.

Publication receipts and the final response identify the exact public commit.
This mathematical packet does not recursively contain the public corpus.

## Endpoint effect

No new seed prime is settled. FIN, ORDER9, Q36 and the complete surviving
unit/class source bound are unchanged. What was tried is a genuine primary
upper-bound construction, and its computed failure to beat the existing bound
is recorded quantitatively rather than replaced by a promise of a new route.
