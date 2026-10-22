# Independent review of 997c1

Date: 2026-10-13. Scope and source qualifications are those of `SOURCE_REQUIREMENTS.md` and the companion 718b1 review.

The separate Python matrix reconstruction passes against `arithmetic/997c1/matrices.json`, SHA-256 `7a015a8dfdd9fd57bb0b52e0ddb351305d962079e4788c4a5838ca87cc38e7d9`. The complete allowed-valuation source has dimension10, its valuation-zero subspace5, ordinary units4, and ordinary class3 quotient1. The joint containing kernel has dimension2; its unit intersection has dimension1. Two actual point columns fill the kernel.

The ordinary point-class coordinates are `(0,1)`. The actual selected class lift is repairable by units, and the saved full repair has point coordinates `(2,1)`, hence represents `2P1+P2` modulo3. Every quotient class-defect matrix has rank0 even though the bare lift has a nonzero raw defect. This is the same repair-and-point-placement outcome as718b1, with the roles of point columns changed.

An independent exact field replay verifies all10 stored tau identities, both point identities, and all5 ordinary class-boundary ideal cube identities. The full BNF certification remains the producer's retained receipt; it was not rerun here.

All8 local rational approximants pass the separate Python exact Hensel check, with minimum cube-class precision margin44. A GP leaf replay recomputes their tangent values, valuations and residues in the original stored local bases and verifies that their spans are exactly the producer's local images: dimension1 at3 and1 at997. This is an independent replay of saved data through the same PARI library, not a second implementation of local fields.

This control supplies a second explicit example of a nonzero ordinary class source that is repaired and occupied by known points. It is not a seed bound and does not show that arbitrary class sources can be so repaired.
