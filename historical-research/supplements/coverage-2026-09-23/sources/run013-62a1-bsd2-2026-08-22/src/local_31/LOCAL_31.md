# Local condition at 31

Status: theorem-bearing use closed; independent review PASS.

The prime `31` enters the support of the `phi_q` covering through
`b'=-31q^2`.  The four retained classes are not merely locally soluble: the
global points listed in `src/selmer/SUPPORT_AND_GLOBAL.md` give points over
`Q_31` directly.

Every other supported `phi_q` class is already excluded over `Q_2`, so no
claim about its `Q_31` solubility is needed for the global intersection.

In the dual orientation, the support lemma excludes a factor `31` because
`31` does not divide `64q^2`.  The Legendre condition at `31` is nevertheless
load-bearing at the moving prime: reciprocity turns `(q/31)=-1` into
`(-31/q)=-1`, which supplies both `Q_q` obstructions in `LOCAL_Q.md`.

Thus every globally retained class has an explicit `Q_31` point, and every
globally rejected class has a proved obstruction at another named place.
