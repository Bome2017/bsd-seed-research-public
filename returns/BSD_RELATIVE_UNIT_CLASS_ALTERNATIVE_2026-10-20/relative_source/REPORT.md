# Actual relative fields constructed; standard relative API does not avoid the missing computation

The seed's actual degree24 point field A contains C=A^C4 of degree6 and Aplus=A^<-1> of degree12. Exact field equations and embeddings were constructed using Theta6=5(x(T)+x(2T)) and Z12=5x(T), with literal quadratic equations for Aplus/C and A/Aplus. Signatures are (2,2), (4,4), (4,10), respectively. The free ranks of their units are3,7,13; the genuine relative norm-one unit group for A/Aplus has rank6, comprising the two faithful rank3 character spaces. These are exact structural facts, not generated relative units.

The bounded degree6 BNF attempt overflowed its256MB stack after26seconds. No class or unit output was accepted. There was no full-A BNF attempt in this lane. Even a complete smaller-field class calculation would not bound the faithful component, as the separate class-control argument explains.

We checked the actual official PARI2.17.3 source corresponding to the installed runtime. `rnfisnorminit` calls `Buchall` on the absolute extension polynomial unless an existing extension BNF is supplied (buch4.c lines106–107). `rnfisnorm` then uses the extension's fundamental units and S-units (lines202–204). Asking it for a norm preimage of1 returns the trivial element1 (line166); it is not a relative-unit basis generator. Thus invoking this API would conceal the same missing full-field computation, not avoid it. It was not launched. The source member and official-download hash receipt are retained.

Proper scalar-fixed-field unit pullbacks are killed in the faithful characters; arbitrary Hilbert90 quotients have norm1 but need not be units. No such quotient was falsely accepted as a unit. The original p7 norm-relation obstruction was read before choosing this test.

This lane constructed useful exact relative-field bindings, but produced no faithful unit source or complete seed bound. It does not rule out a genuinely relative algorithm that handles the faithful unit and relative-class components. The separate low-memory implementation investigation is a different attempt and is not covered by this negative API screen.

Repairs: an unavailable `polsqrfree` call was replaced by exact squarefree extraction f/gcd(f,f'); the raw nonintegral generators were scaled by5 to make the accepted field polynomials monic integral. Both rejected runs are retained. Accepted construction has empty stderr and its completion marker. `fields.gp` is [FA,T,sigma,F6,Theta6,F12,Z12,G12,G24], where G12 has root x(T)=Z12/5 and G24 has root y(T).
