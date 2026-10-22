# Independent check of the mirror389 ray maps

2026-10-15. Verdict: the actual quotient maps support the reported distinction
between the raw order-nine lift and the nonzero global/local repair mismatch.
This check retains the certified saved BNF and the earlier authenticated local
Kummer images. It does not repeat their construction or prove a seed bound.

Write `R=Cl_m(L)` and `K=ker(R→Cl(L))`. The actual CRT principal-ideal map has
image `K`: its elements have trivial ordinary ideal class, and the saved full
integer image has index three, the order of the ordinary class group. Thus
the first quotient really is `R/3K`. This is not `R/3R`.

The comparison from old local unit coordinates to `K/3K` is legitimate. A
right inverse of the actual old-log matrix supplies representatives, and a
different such choice changes them by something trivial in `K/3K`. Global
units already map to zero in the ray group; unit cubes map to `3K`.

The local allowance is the valuation-zero part of each actual local Kummer
image, transported through that map. The earlier adjustment `J=I(γ)` and
`β′=βγ³` makes the ideal and element prime to the modulus; it changes no local
cube class. Therefore the second quotient is the specified

`R/(3K + image(local Kummer unit allowance))`.

The independent checker verifies the following on saved arithmetic:

- The literal ideal equality `J³=(β′)` and modulus norm `3^14·389^4`.
- All twelve saved CRT elements have valuation zero at the modulus primes,
  equal one at the other prime-power components, and have exactly the saved
  old local-log coordinates. Their principal ideals have exactly the saved
  BNR coordinates.
- The old-log right inverse, transported allowance, two integer relation
  lattices and their Smith transformations.
- The integer expressions proving the `β′` residue-to-ray relation and that
  `3[J]` lies in the final relation lattice.
- The concrete orders of `J` in both quotients, as calculated using the saved
  Smith transformations.

The result is

\[
R/3K\cong\mathbf Z/9\oplus(\mathbf Z/3)^5,
\qquad
R/(3K+A_{\rm loc})\cong(\mathbf Z/3)^4,
\]

and the actual lift has orders nine and three respectively. This agrees with
the zero ordinary-class boundary in the residue pushout. It does not negate
the nonzero repair obstruction: ordinary ray quotienting permits all global
unit corrections, whereas the joint experiment requires a correction that
also preserves the scalar and additivity conditions.

No unconditional ray-theoretic substitute for those additional global
conditions has been supplied. The arithmetic identity in
`ARITHMETIC_ROW_MAP.md` retains precisely such extra information on this
control's finite source. Its possible generalization remains unproved.

`check_ray_maps.gp` uses a 60-second alarm and reads saved objects only. The
passing output is `RAY_MAP_CHECK.out`. An initial attempted check wrongly
assumed that freshly generated `idealstar` generators could be compared
literally with the historical generator representatives; that failed check
is preserved in `ray_checker_initial_vector_representation/` and is not a
passing receipt. The final check evaluates the actual saved CRT elements in
the saved old-log bases and through the actual ray map, avoiding that extra
representative assumption. The final stderr contains only the normal PARI
stack-size warning. `RAY_MAP_REPLAY_RECEIPT.json` records two matching runs.
