# Sources and reading scope

This was a targeted continuation of the current complete-source experiments,
not a file-by-file review of the historical archive. No claim of an
exhaustive literature or novelty search is made.

The current lab branch was read and its remote head verified as
51434e21c788612ec21f552a1b1b92910679a46f before this return.
Root INPUT_BINDINGS.json binds the governing seed record and inherited
proofs. Each arithmetic lane has its own original-source bindings.

Read in the local record:

- Canonical MASTER_BSD_DAG.md: actual curve, rank/basis, residual-image
  imports, conductor, bad-place types and current FIN/ORDER9/Q36 status.
- Previous complete control/class-map experiment at1664n1 and its literal
  unit/class/valuation accounting.
- October15 general_character proofs: complete source inequality,
  chi versus chi^-1, actual unit index versus geometric index, and the
  ramification-corrected primitive divisor correspondence.
- October18 class-control and twist notes: old p7 certification failure,
  smaller-subfield obstruction and failure of transferring a class bound
  through a shared x-coordinate field. These were not relaunched as new
  experiments.
- Actual seed-three prior source representatives and certification
  receipts, as detailed in seed_three/REPORT.md.

Primary sources consulted in this run:

1. Edward F. Schaefer and Michael Stoll, *How to do a p-descent on an
   elliptic curve*, section7, including the source conditions and
   incidence correspondence. Author-hosted full text:
   https://mathe2.uni-bayreuth.de/stoll/papers/p-descent-long.pdf.
   This supplies the retained descent framework, not the new unit/class
   computation or its completeness certificate.
2. J.-P. Serre, *Proprietes galoisiennes des points d'ordre fini des courbes
   elliptiques*, Invent. Math.15 (1972), section1.11. The primary author
   archive was opened to check the reference. The ordinary/supersingular
   representation statements remain the retained theorem inputs; no
   independent reconstruction of Serre's full proof was undertaken.
   https://www.college-de-france.fr/media/jean-pierre-serre/UPL5874918517843398173_Serre_proprie_te_s_galoisiennes_des_courbes_elliptiques.pdf.
3. PARI official documentation, `bnfinit` and `bnfcertify`: provisional
   class-group completeness and unit completeness must be distinguished;
   flag1 class-quotient certification is useful only if it completes.
   https://pari.math.u-bordeaux.fr/dochtml/html-stable/General_number_fields.html#bnfcertify.

Tate uniformization, Artin/Swan conductor theory, Weil-pairing determinant,
and tame type-III inertia are standard imported local results, explicitly
retained in the written uniform proof. They are not asserted to have been
formally verified by the finite group checker.
