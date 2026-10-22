# Resume

This lane diagnoses and changes the PARI producer for the actual seed's
degree-24 nonzero-five-torsion-point field. It has not produced the seed's
complete class group or unit system.

Read `STATE.json`, `REPORT.md`, `DEFAULT_KC_COUNT_METHOD.md`, and the direct
gate receipts before doing anything further. Older sealed seed files have
not been changed.

The original default settings fail for two separate measured reasons:
512MB does not accommodate all required prime decompositions, and the
default later dense relation cache alone needs 10,223,928,008 entry bytes.
The added local garbage collection was tested but recovered zero bytes;
it is not a solution and is not used in the final producer.

Unmodified PARI with a small relation base completes factor-base
construction at about 733MB peak resident memory. Its small-norm and
random producers nevertheless added no columns during their bounded
windows. The final balanced-base test used c1=0.2, nrpid=-1, a 2GB stack,
and a 177-second internal alarm. It used 933,396,480 peak resident bytes,
stayed at its 24 initialized principal-ideal columns, and produced no BNF.
All producers in this lane are now stopped.

Do not extend an unchanged failed gate. A bounded producer failure does
not establish a mathematical obstruction. A BNF result would still need
unconditional certification, and authenticated character/norm maps before
it could bound the seed's class-supported contribution.
