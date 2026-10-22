# Sources and retained scope

1. Lab commit `62cf86b31d24be543a4e5677231c130c712e353d`,
   `BSD_SEED_COMPLETE_BOUND_SCALING_2026-10-20`: actual seed field,
   scalar automorphism, integral number-field data, complete-source
   formula and uniform valuation calculation. Their earlier proof
   grades are retained, not upgraded by this return.
2. PARI 2.17.3 official source archive, SHA-256
   `8d9c4fcd584c468d27e0f23c36836587284452094c4b1c404c20c4b810462dcb`:
   `src/basemath/buch2.c`, `src/basemath/buch4.c`. Exact member hashes
   are in the lane source receipts. The GPL license accompanies the
   copied source. These supply the actual allocation and algorithm
   behavior inspected here.
3. [PARI general number-field documentation](https://pari.math.u-bordeaux.fr/dochtml/html-stable/General_number_fields.html):
   `bnfinit`, technical parameters, `bnfcertify`, relative norm routines.
   Provisional computation is kept distinct from certified class
   generation.
4. The norm/extension identities on ideal classes are derived directly
   in `class_control/PROOF.md`, including ramification. The unit
   character count and signatures are derived in `SCALING.md`.
   General norm-relation papers consulted by that lane are listed in
   its own `SOURCES.md`; no unproved relation is imported from them.

The small degree-eight arithmetic test validates the experimental
patch against an independent unmodified-runtime replay. It is software
validation only and is not an additional seed/control-bound experiment.
