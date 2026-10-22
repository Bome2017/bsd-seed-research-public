# Joint witness distillation: actual coefficient and regulator arithmetic

**Result: SHARED_SCALAR_OBSERVATION_WITH_TWO_IDENTIFIED_DEGENERACIES.** This is a retrospective arithmetic reconstruction, not a new uniform theorem or a new seed-prime certificate. FIN, ORDER9, Q36 do not change.

## What was computed

`checks/distill.py` independently reconstructs all quadratic coefficients from copied exact tables, never importing printed coefficient results as its answer. The original interval identification remains retained evidence: no Fourier sum or coefficient witness engine was replayed. All 47 copied inputs are bound by source path and SHA-256.

The script covers sixteen tame rows: the seed's nine certified 17--47 rows, newest83 row, two extra5 rows, the known3-primary positive-excess check, the failed29/59 row, and the control389a1 at7 with both a successful and a failed conductor. Two generators per row and the entire primitive-root orbit are checked. All denominators are inverted only when units. Both zero-regulator rows retain a null scalar; no division by zero is attempted.

Fresh GP arithmetic recomputes the tame regulators from actual rational points, including both polarizations. This uses the retained tame-height formula and the historical algorithm, not a second implementation of that formula. The initial replay's only stderr is expected PARI stack-growth warnings. Other replays have clean stderr. Exact source symmetry and coefficient arithmetic are independently implemented in Python.

Separately the actual saved p² symbol tables for5,7,11,13 give the ordinary quadratic coefficients, and a fresh GP script calculates their canonical ordinary regulators without receiving any numerator or Sha value.

## A common residual scalar across the two types of successful witnesses

In the tame convention, symbols are normalized by the least real period omega1, the discrete logarithm uses one common primitive root, and the regulator is evaluated on the full retained point basis:

    w(p,ell)=c2/((a_ell-2) R(p,ell)).

All twelve nonzero seed tame rows give `w=288 mod p`. This reproduces the historical pattern and adds an explicit readback of the newest83 arithmetic to that same pattern. At83, fresh regulator calculation gives42 and the saved table gives44:

    44 / ((0-2)*42) = 39 = 288 mod83.

For the ordinary measure, let `L2=[U²]L_std` with full Neron period `Omega=2 omega1`, `gamma=1+p`, `U=gamma-1`. The canonical scalar regulator is divided by `log_p(1+p)^2` to give `R_U`. Set

    Q_p = L2/(epsilon_p R_U) * 4/16,
    epsilon_p=(1-alpha_p^(-1))^2,
    alpha_p mod p = a_p mod p.

The actual reconstruction gives:

| p | L2 mod p, full period | R_U mod p, fresh height | epsilon mod p | Q_p mod p | 9 mod p |
|---|---:|---:|---:|---:|---:|
|5|1|1|1|4|4|
|7|4|1|4|2|2|
|11|4|1|5|9|9|
|13|1|1|4|9|9|

The height calculation uses the minimal model `[0,-1,0,-66020924,-65074271436]` and points `[-3031,327384],[-2394,281520]`. It is finite-precision PARI arithmetic in the retained canonical convention, not a new independent certification of the height implementation. Higher height digits cannot increase the one proved digit of L2.

Thus, after the historically prescribed candidate tame normalization `8*C/torsion²=8*16/4=32`, the observation is

    w(p,ell)/32 = 9 mod p,
    Q_p = 9 mod p.

There are fourteen distinct successful seed coefficient primes in the union: four ordinary primes5,7,11,13, and ten singleton primes17,19,23,29,31,37,41,43,47,83. There is also an actual same-prime overlap at5, where two tame auxiliaries and the cyclotomic computation agree. We have not computed independent cyclotomic numerator values for the ten singleton primes; the17 valuation deduced backwards from its Sha certificate is deliberately excluded.

This is stronger evidence than a list of nonzero residues: two differently constructed source coefficients give compatible leading **units** after point-regulator and explicit local corrections. It does not prove that the source classes are realizations of one rational object. Choosing the integer9 by CRT does not prove rationality or bounded height of an unknown global scalar. The factor32 is a convention-specific historical candidate comparison, not a free fitted p-unit and not an independently proved all-prime comparison theorem.

## Two failures distinguish a bad detector from arithmetic excess

| curve | p | ell | a_ell-2 mod p | R mod p | c2 mod p | Interpretation supported by arithmetic |
|---|---:|---:|---:|---:|---:|---|
|seed|29|59|23|0|0|the point-plane regulator is singular|
|seed|29|233|13|2|6|a different conductor repairs that singular detector|
|389a1|7|379|2|0|0|the point-plane regulator is singular|
|389a1|7|29|6|6|1|a different conductor repairs that singular detector|
|seed|3|103|2|2|0|nonzero point detector but zero coefficient; compatible with independently known3-primary excess|

For the last row3 is a bad coefficient prime, outside the good-prime Ota/Kato application in the other rows. It is an arithmetic negative control, not a theorem imported across that domain boundary. The integer168 is the actual c2; its reduction is zero even though the Euler and tame-regulator factors are nonzero. The zero agrees with288 modulo3, but the old check itself is not a new explanation of Sha3.

The two conductor failures are **not unresolved coefficient-prime failures**:29 and7 were settled using other conductors. Neither Euler factor vanishes. At29/59 the exact Gram determinant is `27*10-26²=-406=-14*29`. At7/379 it is `1*4-2²=0`. These are concrete mechanisms for losing the two-point information before any inference about Sha.

## What the combined data suggest constructing

The useful common quantity is a **normalized degree-two source coefficient relative to the determinant carried by the two rational points**. In a direct unit/class computation, the analogous comparison would need a determinant or Fitting morphism for the *whole admission complex*, keeping both the units and the liftable class defects. A unit-only determinant cannot capture the class-supported part seen at3.

The conductor failures explain one task such a construction must perform: it must permit a change of detector without changing the underlying arithmetic scalar. Existing G2 is a source of nondegenerate point detectors on its retained domain. The unexplained step is still the comparison tying the analytic/arithmetic source coefficient to those point detectors with a fixed normalization. The experiments now test that comparison on units, and test its zero behavior when a point detector degenerates.

A precise follow-up candidate is therefore a determinant-line comparison between the full unit/class admission complex and the modular-symbol source, normalized on the full point lattice. Its output must recover the displayed units and both kinds of zeros. This paragraph identifies the desired map; it does **not** construct it, prove a rank bound, or certify that such a map exists independently of refined BSD. An abstract statement that both sides measure Sha would not supply it.

The samples are deliberately selected, not statistically representative. Later singleton conductors were chosen using the nonzero tame-regulator prescreen and computational price. Small ordinary primes were feasible first. Most mathematical imports and the original symbol engine are shared. The independent evidence here is actual downstream arithmetic, fresh point-regulator evaluations, and distinct cyclotomic/tame extraction; it is not fourteen independent complete BSD implementations.

## Replay

`python3 checks/distill.py` verifies the copied-input hashes and recomputes the JSON. Fresh arithmetic producers can be rerun with the documented GP runtime on `checks/tame_replay.gp`, `checks/tame_negative.gp`, `checks/tame_389.gp`, and `checks/ordinary_heights.gp`; use `-D parisize=128000000 -D parisizemax=1024000000`. The tame producer costs about one minute on the current host; the ordinary height calculation is inexpensive. This does not rerun modular-symbol production.
