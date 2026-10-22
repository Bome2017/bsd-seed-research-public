# Sources, prior work, and scope

Primary source read in this continuation:

- William Stein, *Hecke operators as correspondences*, Math 252, 31 October 2003, pp.111-114. The prime-level degeneracy maps, their differential convention, and the correspondence interpretation are used. The closed-cover lift and moment calculation are proved in PROOF.md, not attributed to Stein. https://wstein.org/edu/Fall2003/252/lectures/10-31-03/10-31-03.pdf
- Stein's weight-two chapter was also consulted for the modular-curve and period conventions. Its composite-index Hecke summary is not used. https://wstein.org/books/modform/modform/weight_two.html

Retained project sources are hash-bound in INPUT_BINDINGS.json. They include the fixed homology period functional; the existing Np matrix audit; the previous three-construction attempt; and the actual modular-symbol and Gross-packet definitions.

Collision search: 14 keyword matches in the structured compendium were saved in COLLISION_SEARCH.json. The relevant E08 task and corrected E05 review were read at their original paths. Noninvariant correspondences and the need for a witness comparison were already on record. No novelty claim is made for that strategy. The old Np matrix is explicitly reused, not reclassified as new. This was a scoped collision search, not an exhaustive audit of the corpus or a literature novelty screen.

The new derivation's review priorities are: (1) compact-cover homology surjectivity despite ramification; (2) the full marking and isogeny-map conventions; (3) the two prescribed periods; (4) keeping the constructed cycle separate from the canonical arithmetic packets.
