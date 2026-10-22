# Sources, retained inputs and boundary

## Primary sources read

1. Robert L. Miller and Michael Stoll, *Explicit isogeny descent on elliptic curves*, January23,2011 version, sections2--3 and7, especially Definition4, Definition8 and Theorem11 (printedp12). https://www.mathe2.uni-bayreuth.de/stoll/papers/isogeny-descent.pdf
   - Supplies the Kummer/descent identification and the local-condition theorem.
   - Substitution: E=A, E'=F, ell=5, kernel fieldQ(sqrt43737), w=1, Sigma1={11}, Sigma2=empty, A(Q5)[phi]=0, so S1={5,11},S2=empty.
   - The real kernel convention, minimal differentials and local Tamagawa ratios are retained or checked from the prior exact isogeny record. Conjugation acts byminus on the kernel. The absence of a residual local map here is source-specific, not a general rule for5-descent.
2. Tom Fisher, *Explicit 5-descent on elliptic curves*, Open Book Series1 (2013),395--411, Theorem5.3 (printedp402). https://msp.org/obs/2013/1-1/obs-v1-n1-p20-s.pdf
   - Supplies the Pfaffian covering formula and its cohomology/Jacobian interpretation.
   - Its isogeny C_lambda->D_lambda is F->A after twist and minimalization. It is the dual of the original phi:A->F.
   - The source page was visually inspected. Local source digest is recorded in INPUT_BINDINGS.json; the paper itself is not redistributed in this packet.

## Retained arithmetic

The exact models, rational points, rank-upper-bound output, saturation certificates, isogeny formula and local reduction output are copied under evidence/retained/ from BSD_ODD_EXCESS_CONTROL_EXPERIMENT_2026-10-12. INPUT_BINDINGS.json records original paths, SHA256 values and the frozen lab snapshot containing those data.

- Rank exactly2: prior PARI descent output `[2,2,0,...]`; not rerun here by an independent descent engine.
- Both displayed point pairs are5-saturated: prior exact reduction matrices at7 and19. Only the A pair is needed for the new unit-class exclusion.
- Minimal models, good reduction at5, no rational torsion, Tamagawa products20 and4, differential multiplier1 forphi: retained exact record; some curve/point identities are rechecked this turn.
- No previous numerical L-value, height, main-conjecture equality or exact primary Sha order is used in the new class construction.

## New computations

- Certified quadratic class-group computation and explicit principal generators.
- Explicit descent function, point evaluations, exact fifth-power relation.
- Fundamental-unit certification by a separate finite integer argument.
- Two independent explicit Selmer quotient classes.
- One Pfaffian genus-one model, exact smoothness and Hilbert calculations, six explicit Hensel witnesses.
- An affine equation and exact rational covering map identity on its specified open chart.

These are written mathematics and exact software calculations. The audit is a separate agent in the same session, not external expert certification. `bnfcertify=1` applies to the number-field computation, not to the whole theorem. A build or manifest does not certify local descent or the retained rank computation.

The independently obtained explicit subgroup is Sha(F)[hatphi], killed by5. This calculation alone does not control deeper5-primary layers or the entire Sha group, and it does not change any BSD seed endpoint.
