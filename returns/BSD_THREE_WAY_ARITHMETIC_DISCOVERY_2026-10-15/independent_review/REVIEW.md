# Separate arithmetic reconstruction by the root worker

Status: exact finite arithmetic replay passed; written global arguments reviewed separately. This is not independent human certification or formal verification.

`check_local.py` imports no producer library or source-coordinate matrix. It takes the literal rational field polynomials for the named representatives, reduces them at all 120 new local-signature prime blocks, independently performs elliptic addition, and checks the cubic-residue characters. It verifies all true class additivity equations, the annihilation of point columns, annihilator dimension, and the quotient ranks. It separately retains the false candidate's failed additivity, rather than declaring it a class. All 9,864 unit-cube and point-shift controls pass.

A representative issue was found and repaired in the checker: for the seed at q=2767, root index 7 and P2, the literal tangent element has valuation 3, although the equivalent source-factor representation is a unit. Direct reduction would incorrectly produce zero. Independent Hensel lifting gives leading unit 916 modulo2767 and valuation3; the resulting cubic character agrees with the factor representation. The prime is retained. The actual result is recorded in `LOCAL_REPLAY.json`. The detector's selected root indices0 and1 are unaffected, but the full replay checks all eight.

`check_frobenius.py` independently evaluates the exact false source and its exact affine norm at all 40 fresh primes. It verifies 320 products over affine torsion lines and all1,280 nonzero-sum triple equations. It reproduces the three missed primes51439,56701,58237. It reads the sealed prediction for comparison only after independently computing the outcome. No producer Python module is imported.

`../incidence_review/check_incidence.py` separately verifies the integer incidence matrix, Smith factors(1,1,3,3), mod3 rank2, additive kernel, all48 GL2 actions and irreducibility of both relevant modules. In particular it checks the formal row-span under the point action, not only the image under the line action. This distinction is needed for the actual Kummer-module degree argument.

Fresh `polgalois` computations return GL2(F3) of order48 for the mirror and all four positive/point control fields. These checks bind the existing torsion-field identifications; they do not newly prove each source field parametrizes E[3]. The mirror has an independent simple residual-image check using Frobenius at11 and multiplicative inertia at389.

The global written deductions still use the retained exact source admission, full rational-point lattice, rank and saturation inputs. For the mirror, a noncube residue at a completely split prime proves noncubicity in the full torsion field, avoiding the invalid inference from noncubicity in its degree-eight subfield. The resulting degree-nine extension and conditional density argument are coherent under these bindings.

For true classes, a point-relative signature is a localization of an E[3]-Kummer lift modulo the localization of the global point subgroup. It is not nonzero torsor localization in H1(Q_q,E). All Sha torsors remain locally trivial. A nonzero signature proves a class is not from a rational point only after global admission is established. A finite signature matrix does not bound unlisted classes.

FIN, ORDER9 and Q36 remain open. This review verifies actual distinctions among false admission, true excess and point directions. It does not transform detection into an upper bound.
