# Relative class-control admission test

2026-10-20. Fixed curve: the original BSD seed. Coefficient prime: five.
No new control curve is allowed.

Changed proposed computation: use the actual scalar-fixed degree-six
field F and degree-twelve field F2 inside the degree-24 point field A,
where Gal(A/F)=C4 and F2=A^{sigma^2}. Test whether certified lower-field
class data and ordinary extension-norm indices can bound the missing
faithful five-class contribution.

Before allowing an expensive class computation, derive which scalar
components those maps see. Execute exact character/module countercontrols.
If the proper-subfield maps annihilate the requested component, do not
run a lower-field class calculation merely to claim it bounds that
component. A sibling may compute F for an independent relative-unit
construction; its class result must retain its actual role and grade.

No full A BNF is launched here. No failed previous certificate is
repeated. No GRH-dependent table is promoted to an unconditional bound.
The finite module tests are controls on a proposed inference, not
number-field realizations or seed class-group computations.

Required endpoint of this admission test: an exact relative-class
sequence retaining all missing classes, together with either a justified
complete upper bound or a precise explanation of which additional
relative arithmetic would still be required.
