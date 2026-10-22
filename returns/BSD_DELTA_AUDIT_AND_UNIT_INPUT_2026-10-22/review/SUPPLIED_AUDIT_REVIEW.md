# Replay and scope review of the supplied GitHub delta audit

Date: 2026-10-22.

Verdict: **SUPPLIED_EXACT_CHECKS_REPRODUCED; NO_NEW_SEED_BOUND.**

This is a same-session agent review and fresh execution of the supplied
checker programs. It is not human review, formal verification, an independent
reconstruction of the seed number field, or an audit of the entire research
corpus. The supplied six-file directory is unchanged.

## Custody and execution

The six supplied files comprise five manifest-covered files and
`MANIFEST.sha256`. All five SHA-256 entries verified. The two Python programs
use only the standard library (`fractions`, `math`, `pathlib`, `json`), have
no network access code, and write their result JSON adjacent to themselves.
After source inspection, each was run twice in a separate disposable copy.
Both executions exited zero; both generated JSON files matched the supplied
results byte-for-byte and semantically on both runs. Input hashes were
compared before and after execution.

`AUDIT_REPLAY_RECEIPT.json` records the source hashes, Python version,
execution times, exact comparison results, and hashes of the prior outputs
used in cross-checking. The replay driver and stdout/stderr files are retained
here. No publication operation was performed by this review subtask.

## What the computation actually reproduces

The numerical program explicitly transcribes constants and radii from the
pinned lab snapshot. It derives the separation and volume bounds using exact
rational arithmetic, with a justified positive-series tail bound. It does
not read the former producer's claimed ceilings as the output of its own
calculation. Its integer ceilings and exact integer order bounds match all
13 records in `BSD_PRIMARY_TORSION_BOUND_2026-10-22/theory/PRIMARY_PACKING_RESULT.json`.
The minimum is 106; the preceding complete relative five-primary **length**
bound remains 97. The former controls five-torsion dimension only and is
weaker than the latter.

The four hypothetical reconstruction precision rows match the original
`RECONSTRUCTION_GATE_CHECK.json`: 236, 276, 316, and 396 binary digits;
72, 84, 96, and 120 decimal digits. These use hypothetical index bounds,
not computed seed indices. The numerical upper width near 9.0346e-53 is
the specific reconstruction scheme's gate, not a cost estimate or a general
lower bound on possible algorithms.

The finite-algebra program reconstructs the projected incidence matrices
modulo p² at p=3,5,7,11,13 and verifies the character-scalar identities,
orbit counts, ranks and coordinate kernels. Those results agree with the
prior implementation. The ranks p−1 concern the tested degree-one character;
the code does not establish this rank formula for every character or for
the actual arithmetic unit lattice. The all-prime orbit exclusion rests on
the written orbit argument, not the five samples.

The two monomial projector checks are exact identities in a, s and a sign
t with t²=1. They verify the algebra of the literal fifth powers. They do
not freshly establish that seven particular field elements have those scalar
actions or those ideal valuations. Those remain retained from the earlier
actual-field computation. The same distinction applies to the prime-pair
counts, discriminants, regulator lower bound, and one-sided L-value bound.

Thus the audit is an independent implementation/replay of selected
**implications of retained data**, not independent regeneration of all
underlying arithmetic data. The supplied report states this distinction.

## Mathematical deductions checked

The source parity argument survives products and roots that remain inside
the same real-embedded field: if (tau(b)/b)^n is a sign, tau(b)/b is a root
of unity; that field has only ±1. Both signs are fifth powers. This does
not exclude roots in larger fields or sources carrying additional structure.

The presentation-error formula is valid for finite **abelian** p-groups.
The snake sequence makes the quotient of ker(u) by the image of ker(U)
a subgroup of K_B/U(K_A). Generator ranks of subgroups and quotients of
finite abelian p-groups do not increase. The extension inequality therefore
gives the stated bound. Exact target relations and complete source
generation suffice; a selected invertible matrix without those interfaces
does not. This is bookkeeping, not a completed class certificate.

The relative reconstruction identity is coherent under the retained
class-number/regulator/field inputs. With V0=jV and I a power of two,

    t = T/(64 V0) = h_rel/(I j),

so v5(h_rel)=v5(t)+v5(j). Five-saturation is sufficient to eliminate the
index contribution, while an independently proved upper bound on v5(j)
also permits an upper bound. Six units in the full norm-one rank-six
lattice are required for this formula; three units in one character sector
do not provide the needed finite-index subgroup. Distinct reduced rationals
with denominator at most D are separated by at least 1/D², justifying the
isolation criterion. Neither the relative units nor the two-sided analytic
enclosure is supplied by the reviewed audit.

These checks do not recertify the prior field construction, analytic
class-number inputs, source injection, or parity theorem. Published-source
references in the supplied review were read as citations; their full papers
were not freshly audited in this subtask.

## Qualification on the proposed across-prime target

The stated condition

    r_U(p) − k_C(p) >= (p−5)/2

is a valid **sufficient coarse threshold**, not a necessary condition for
FIN or even for a small complete source bound. It uses all of the following:

1. The retained injection of the classical p-Selmer group into the complete
   faithful norm source, with the correct scalar character and support.
2. Faithful ordinary unit dimension (p+1)/2, and r_U a certified lower bound
   for the rank of the actual arithmetic norm on that unit space.
3. k_C an upper bound for the complete source-to-companion p-class kernel,
   not merely the kernel on displayed classes.
4. Zero extra valuation allowance on the stated domain.
5. The retained rank-two saturated point plane and the applicable parity
   conclusion for the excess Selmer quotient.

Indeed these give dim Sel_p <= (p+1)/2 − r_U + k_C <= 3. Subtracting the
two point directions and using retained evenness forces Sha[p]=0.
If the valuation allowance is t_D, the sufficient threshold instead is
r_U−k_C >= (p−5)/2+t_D.

The exact sequence also has a nonnegative connecting-map rank, and local
conditions can lower the containing space further. Such authenticated cuts
could certify a small source without satisfying the displayed coarse
threshold. The review must not turn that threshold into a necessity claim
or rule out those improvements. The October 18 rank-mechanism proof and
the October 17 class-map bound explicitly retain these qualifications.

## Publication and endpoint scope

The audit's historical snapshot/tag observation is plausible from the named
objects, but this review subtask did not freshly query GitHub or compare the
whole public corpus. Any release correction should be checked and made by
the publication task, preserving historical tags rather than silently moving
them. Publication status does not change proof grade.

The supplied audit is consistent with retaining the complete relative
five-primary length ceiling 97 and the conservative complete-source ceiling
100 under their retained interfaces. It supplies no new prime, arithmetic
unit, class-generator certificate, or endpoint theorem. FIN, ORDER9 and Q36
remain unchanged.
