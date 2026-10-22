# Independent arithmetic upper bounds from primitive divisor norms

The executed test gives an upper bound on the entire containing global norm kernel, using companion class data and a primitive divisor index. It does not compute that bound by taking the rank of the existing Selmer/admission matrix.

The p=3 written deduction is

    dim K_A <= 1+t_D+c_BS^--(c_AS^--r_AS^-)
             <=1+t_D+c_BS^-
             <=1+t_D+v3(#Cl(B,S)).

Here K_A is the actual scalar-and-affine-norm kernel in A(S,3), c denotes a minus class-group **length**, r its3-rank, and t_D is the incidence-norm index on the **primitive anti divisor lattice** above S. The source class-group contribution is retained and cancels against its denominator in the S-unit norm index. This controls unit and class contributions together. PROOF.md gives the exact sequences and all conditions.

The producer uses curve/torsion geometry, prime decompositions, exact approximation elements, literal norms and cached certified BNF class data. It does not read point columns, local Kummer rows, full norm-kernel columns or Sha values. It constructs primitive divisor bases from prime pairs, rather than substituting the finite-index valuation image of selected S-units.

| Input | Actual divisor matrix | t_D | Independent upper information |
|---|---|---:|---|
|389a1|diag(1,-1)|0|Companion S-class length1 gives dim K_A<=2|
|Its -3 mirror|diag(3,-3), from integral reverse composition|2|Companion S-class length0 gives dim K_B<=3|
|1913b1|(-1)|0|Trivial ordinary source class group and injective divisor map force ordinary units; dim K_A<=2|
|Seed at3|diag(1,3)|1|Divisor shortcut fails; companion class bound not computed|

The389/mirror forward computation took39ms;1913 took87ms; seed divisor arithmetic took57ms. No BNF was newly constructed or certified. Each extension had a written contract and hash seal before its calculation. The reverse mirror divisor index is a deduction from the integral norm composition and the forward primitive matrix, not a second independent direct evaluation.

Comparing only after the upper arithmetic was produced: the complete global kernels previously computed for389/mirror have dimensions2/3, and the genuine1913 classes span dimension2. Thus the independent bounds are sharp on these controls. The rank-two389 point plane fills its upper bound; rank-zero1913 can fill the same bound with genuine excess. The bound never treats the opposite norm image as rational points.

For the seed, t_D=1 is a new direct geometric calculation in this experiment. The bound becomes dim K_seed <=2+c_BS^-; the companion minus S-class length c_BS^- has not been independently computed, so this does not yet give a small numerical global image bound. The potentially useful input in the displayed inequality is now an actual companion S-class estimate. None has been proved across coefficient primes. The argument is specific to the p3 minus component, and coefficient3 is bad for the seed. FIN, ORDER9 and Q36 are unchanged.

The result is a written arithmetic-bound mechanism with bounded exact control calculations, not a claimed novel theorem or a uniform seed solution. The original ordinary-unit comparison and source embedding remain retained inputs; their implications have not been upgraded by computation alone.

## Verification and provenance

`python3 verify_certificate.py` is read-only on this packet. It copies each literal certificate into a temporary directory, independently reconstructs the prime decompositions and involutions, verifies primitive divisor bases, computes norms as3-by-3 multiplication-matrix determinants, and checks their target valuations and integer matrices. It imports no producer functions and uses no saved norm-kernel or Selmer matrix. Its output is saved in LITERAL_REPLAY.json. PARI remains the common number-field arithmetic backend.

`python3 replay.py` performs an isolated full producer replay for all three forward probes and compares their INDEX.json outputs byte-for-byte. It also runs the independent literal checker and verifies input hashes. Original files are not changed.

The earliest attempts exposed two storage/interface issues: the389 binary contains two appended BNF objects with a serialized variable name, and the raw seed model required ellinit. Both were repaired by explicit checks/normalization. Two checker failures involved PARI's trace function name and the zero padding of rectangular Smith form. Failed scripts and outputs remain under failed*/; none was accepted as arithmetic output.

The cached BNF certificates retain their original grades. The seed probe uses only NF geometry, so no class-group completeness claim enters that probe. The companion minus length was bounded above by the total companion class length in the executable bound; the output does not silently label total lengths as minus lengths.
