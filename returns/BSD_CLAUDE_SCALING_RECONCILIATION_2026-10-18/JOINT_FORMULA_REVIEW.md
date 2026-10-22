# Root review of the joint bound

For an exact sequence of finite F_p spaces 0 -> U -> H0 -> C -> 0 and a linear necessary-condition map R:H0 -> Y, a choice of class lifts defines a map C -> Y/R(U). Changing a lift changes R by an element of R(U), so the induced map is canonical. Projection gives an exact sequence

    0 -> ker(R|U) -> ker(R|H0) -> ker(C -> Y/R(U)) -> 0.

Therefore dim ker(R|H0) = dim U-rank(R|U)+dim C-rank(Rbar). With H0 the zero-valuation part of a larger complete source H, the quotient of ker(R|H) by its intersection with H0 is the actual surviving valuation image. Its dimension q must be added, giving the formula in REPORT.md. Here C is the ordinary class layer of the chosen actual filtration; it must not silently be exchanged for an S-class group.

If all true Selmer classes map into H and every row is a necessary condition, ker R is a containing space. Equality to Selmer is not required for an upper bound. Completeness, containment and row validity are retained arithmetic hypotheses, not consequences of matrix rank.

The root checker uses streamed row-basis elimination independently of the agent's reduced-echelon, class-map and exhaustive H0 enumeration implementation. It reconstructs whole, zero-valuation and ordinary-unit kernels from the saved matrices and agrees in all ten cases. It uses no printed rank or previous kernel as an arithmetic input; the two output summaries are compared only after calculation. This checks saved matrix arithmetic, not the production of the underlying units, ideal classes or local images.

This is same-team model review. The growing-p statement is a sufficient target, not an achieved arithmetic bound.
