# An actual class rejected by incompatible unit repairs

2026-10-15. This is the saved -3 twist control of 389a1, not the BSD seed and not a rank-two/good-at-3 analogue. Its minimal model is

    y^2+y=x^3-21x-27,

with conductor 3501. The saved rank cross-check is zero. No new class-group certification or broad search was run. The previously saved certified BNF was reused.

The calculation now exhibits the missing experimental configuration: a class lift can be repaired separately for the global necessary conditions and for every local Kummer condition, but **no single unit repair satisfies both**.

## Actual source and output

The point field has degree eight, class group C3, S-class group C3, and S={3,389}. The new run checks the actual 3-torsion point, field irreducibility, full source dimension eleven, full-rank residue evaluation of all eleven source classes, and allowed ideal support. The valuation-zero source H0 has dimension five, its ordinary-unit kernel U has dimension four, and its ordinary-class quotient has dimension one.

Let G denote scalar anti-invariance plus the recorded necessary split-prime additivity rows, and let L denote the full local-Kummer defect rows. The following are computed on H0:

| conditions | admitted units | admitted class dimension | total kernel dimension |
|---|---:|---:|---:|
| scalar | 2 | 1 | 3 |
| G | 0 | 1 | 1 |
| L | 0 | 1 | 1 |
| G and L | 0 | 0 | 0 |

The full eleven-dimensional source also has joint kernel zero. Thus the result is not obtained by discarding S-valuation directions.

For the fixed class lift beta and the literal ordinary-unit basis in `class_witness.gp`, the unique unit repair exponents are

    u_G = (0,1,2,2),
    u_L = (2,2,2,2).

These differ by

    u_G-u_L = (1,2,0,0) in F3^4.

The literal fractional ideal I and field element beta satisfy I^3=(beta), with I representing the nonzero ordinary class. Both repairs are products of actual saved global units. These are arithmetic source representatives, not an arbitrary matrix model.

The globally repaired class fails the local test at 3: its ten defect coordinates are

    (0,2,0,1,0,0,0,0,0,0).

It passes the place389 rows. The locally repaired class passes both places. The local-image samples were regenerated at higher precision and independently checked by rational Hensel inequalities; six samples have minimum cubeclass precision margin40. Sampling stops only at the independently determined complete local-image dimension.

## The repair-compatibility quotient

In general, on the subspace of class directions admitting both marginal repairs, the difference of repairs defines

    kappa(c) = [u_G(c)-u_L(c)]
       in U / (ker(G|U)+ker(L|U)).

Changing a chosen repair changes the difference by the indicated sum. Changing the class lift adds the same correcting unit to both repairs. Hence the quotient class is independent of these choices. A simultaneous repair exists exactly when kappa(c)=0: equality of the two affine repair cosets is precisely intersection of those cosets.

Here both unit kernels are zero, so the quotient is F3^4 and kappa(beta)=(1,2,0,0) is nonzero. The functional (1,0,0,0) annihilates the sum of the repair kernels and evaluates to1 on this difference. Separately, the exported joint-row annihilator kills every ordinary-unit image and evaluates to1 on beta. Both witnesses were reconstructed independently from the actual matrices.

The comparison across the eight rank-two controls is in `../repair_compatibility.json`: their global and local unit kernels coincide in a one-dimensional line; the compatibility quotient has dimension three, and each recorded class has zero compatibility class. In the deterministic solves, the two unit repairs are literally equal. The mirror control is the first recorded nonzero compatibility class.

This is a detector for failure of simultaneous repair. It is not by itself an upper bound on the seed's source. The global rows are necessary additivity tests, not an asserted full global cohomology characterization. A nonzero defect is therefore a valid rejection; survival would require further analysis unless a containing upper bound already closes.

It is also **not** a local-only ray-class obstruction. The unrestricted local defect modulo all ordinary units is zero. Restricting the allowed further unit repairs to those preserving G is what creates the obstruction. The subsequent actual ray calculation does exhibit an order-nine lift in the raw ray group (and after quotienting by residue-kernel cubes), but its order drops to three after the local Kummer allowance is imposed. That raw order-nine lift therefore does not represent the joint obstruction; see [the actual ray calculation](ray/RESULT.md).

## Implementation correction and evidence

The old helper's condition `e == 0` treated a valid zero-column solution of `matsolvemod` as failure, because PARI compares a zero column equal to scalar zero. The new local library distinguishes integer0 (failure sentinel) from a zero column (valid solution). This changes no mathematical hypothesis. The first failed attempt and all its misleading completion-marker output are retained in `failed_zero_solution_guard/`.

A separate first export attempt had a GP reserved-variable/shape error; it is preserved in `failed_export_shape/` and is not accepted. The final `export_witness.err` is empty, and all final exact identities pass. The rank-two-only Python checker was adapted to allow zero point columns; it does not insert points or assume rank two.

Files: `data.gp`, `matrices.json`, `coupling.json`, `class_witness.gp`, `export_witness.gp/.out/.err`, `local_certify.*`, `local_witness_check.py/.json`, and `../repair_compatibility.py/.json` provide the actual objects and checks. All source originals remain unchanged.

No conclusion about FIN, ORDER9, Q36, or any new coefficient prime of the seed follows from this control. The new experimental fact is that marginal global and local admissibility can agree in dimensions and both accept a class, while their required unit repairs are incompatible. The compatibility quotient records that missing interaction explicitly.
