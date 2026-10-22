# Return check of the independent uniform-synthesis review

Status: **ACCEPT_REVIEW_AT_STATED_GRADE; LIVE_SOURCE_HASH_MATCH_CONFIRMED**.

Date: 2026-09-30. This is a bounded return check, not another full audit of the seed or a new construction attempt.

## Integrity

The received review zip has SHA-256

    5b722afcd7cdc4b97dfc0017c9ae794bad232085e231a32a0f6bee5f6a03dccf.

All 24 entries of its manifest verify. The loose `RETURN (1).md` is byte-identical to RETURN.md inside the zip, and the loose review-state JSON agrees with STATE.json. Its INPUT_INTEGRITY.json identifies the exact synthesis archive produced here, SHA-256

    09538488923ff4836a134042604b17fc6a49d0c181f780bda1297129a0c58e1d.

The 26 recorded input hashes were checked again against the existing synthesis files. This confirms review identity and custody, not the truth of imported mathematical theorems.

## Mathematical disposition

I read PART_A_COVERAGE.md and PART_B_DEPTH.md in full and compared their arguments with the prior synthesis. No mathematical correction to the stated conclusions is needed. Retain:

1. At the imported-theorem/retained-seed-input grade, every good p>=5 has M_infinity(delta)=0 and some mod-p unit Kurihara witness, with conductor allowed to depend on p.
2. The minimum unit length r_p equals dim_Fp Sel_p(E/Q), and r_p=2 is equivalent to vanishing of the entire p-primary Sha group. The first merely nonzero quantity is not substituted for the first unit quantity.
3. A faithful value of the full BH-normalized element of a real cyclic degree-p extension, at its actual conductor coprime to pN, with lambda-depth strictly below four is sufficient for primary vanishing. Composite conductor is allowed.

Carry two explicit qualifications into any integration:

- There is no extra exclusion of 19, 59 or 487 in the all-good-prime existence result. The matching imprimitive Euler factors are retained, even where they are nonunits. This is not permission to discard them in other historical scalar comparisons.
- The BH element is at the actual conductor of K. Artificially enlarging that conductor requires the norm relation and its Euler factors; one cannot silently use the enlarged element as the same normalized object.

The review's abstract group-ring countermodel for the weaker bound <=4 is valid and reinforces the strict threshold. It does not claim to model the actual seed at an uncomputed prime.

## The one source caveat, now closed as a byte-identity check

The reviewer documented conflicting browser renderings and could not independently retrieve the author's binary PDF. I performed that missing check here.

A fresh HTTPS download from

    https://web.math.ucsb.edu/~castella/CLW2.pdf

at 2026-09-30 15:19:54 UTC returned 684246 bytes with SHA-256

    0686fa414b242e8e3b1cccd3fe906c8eefcfdb7b568563daa3089701d036fb98.

It is byte-identical to the pinned September 21 source. The server's Last-Modified header is September 21; headers and retrieval metadata are in FRESH_SOURCE.json. I rendered the downloaded PDF's printed page 3 and visually confirmed Theorem A's revised (ram)/(rtn) alternatives and the absence of a squarefree-level hypothesis.

This establishes that the accepted pinned version is the version currently delivered by the author URL. It does not explain the browser screenshot discrepancy, reprove the underlying paper, or upgrade its preprint grade.

## Consequence for the next step

The independent check requested in NEXT_TASK.md is complete and accepted. Another identical review is not needed from this session. The accepted statements are ready to be recorded at their existing grades.

There is still no independent uniform bound forcing r_p=2, or normalized character depth below four. No new prime has been settled. The open construction must supply that upper bound or another mechanism excluding excess Selmer classes; existence at unspecified length is now an available input.

This check writes only to its own folder. It does not alter the received review, original synthesis, governing map, release repository, or memory. No production arithmetic, external message, push, or successor session was launched.

FIN, ORDER9 and Q36 are unchanged.
