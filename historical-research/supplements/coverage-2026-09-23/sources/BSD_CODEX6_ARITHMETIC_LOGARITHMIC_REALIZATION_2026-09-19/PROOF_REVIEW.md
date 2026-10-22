# Internal mathematical and scope review

This is the author's internal review of the written arguments.
It is not an independent referee report or kernel verification.
No computation of the new unit period was performed, and none is
required for the scoped obstruction.

| Check | Result and reason |
|---|---|
| L1 orientation and parity | Alpha on the descending imaginary ray gives the positive integral from t=1 to infinity. Substitution t=1/u gives exactly the factor (-1)^j for the other half. |
| L1 analytic rank | Differentiating the completed L-function at a double zero removes derivatives of the completion factors, giving J2=L'' and H2=L''/2. |
| L1 formal counterexample | The Gaussian transform is sqrt(pi) u^2 exp(u^2/4)/4. The half moments are 0, 1/4, sqrt(pi)/4. It is explicitly not a modular newform. |
| L1 endpoint term | Integration of dG contributes G(terminal)-G(initial). Lower full moments do not remove that term. |
| L2 rational unit | Weight-twelve transformation cancels the modular factors. The discriminant ratio on the cyclic isogeny is invariant under differential scaling and is defined over Q. The normalized ratio is N^6 Delta(Nz)/Delta(z). |
| L2 Fricke factor | Delta(-1/z)=z^12 Delta(z) gives u(Wz)=1/u(z). Positivity on the imaginary axis selects u(i/sqrt(N))=1. |
| L2 algebraic base point | W_N is a nonidentity Q-involution, so its fixed locus on the curve is finite and algebraic. No small degree bound is inferred. |
| L2 connection and integral factors | Differentiating (1,U,U^2/2,V) gives exactly the displayed rank-four system. Reversing the path gives P_u=-lim(V)/72. The normalization 144 is a choice, not a proved comparison. |
| L2 cusp convergence | U=O(y), while alpha_f decays exponentially. The V component has a convergent cusp limit even though other horizontal coordinates diverge. |
| L3 solution-coordinate scope | In a single-valued meromorphic frame near a cusp, connection coefficients are periodic. A fundamental solution obeys Phi(z+w)=Phi(z)M. All translated scalar coordinates have finite-dimensional span. |
| L3 algebraic gauges and covers | Gauge entries are meromorphic on the curve, hence periodic near the cusp; after a finite cover use a multiple of its cusp width. This does not cover an arbitrary analytic gauge upstairs. |
| L3 exact primitive | Differentiation preserves finite-dimensional translation span. For twisted exact terms the pairing identity d<v,s>=<v,nabla s> supplies an admissible scalar primitive. |
| L3 boundary argument | A finite translation relation for fP(ell) divides by f on an open set. Only the resulting explicit log relation is continued to H. No global continuation of the correction connection is assumed. |
| L3 geometric scope | The theorem rejects the local identity in the defined class. It does not reject every equality of periods on a single path, all mixed motives, or all common certificates. |
| G1 converse | The retained separation theorems give the forward implications; q=36 supplies each reverse arithmetic hypothesis immediately. No equivalence with FIN is inferred for these one-sided certificates. |
| Common-B converse | FIN plus FORMULA and the interval force order nine, allowing a post-FIN numerical B=9. This does not construct the desired pre-FIN object or its independent interfaces. |
| Retained FIN no-go scopes | Ordinary depth-zero equivalence is restricted to the ordinary tail. Positive-depth Ota transfer and supersingular/global converses are not silently asserted. |
| Status discipline | No arithmeticity of q, Sha finiteness, order-nine theorem, or strict difficulty reduction is newly claimed. |

## Audit labels

**FATAL for the specified local bridge:** L3 forbids its differential
identity when the representative and exact primitive belong to the
finite class. This is not a FATAL verdict on every possible scalar
comparison or on BSD.

**REPAIRABLE as a proof contract, not repaired into a successful
bridge:** use the full ray with verified endpoint/parity data, or
prove the missing half-ray cancellation separately. L3 still blocks
the tested finite local comparison after that correction.

**UNVERIFIED / OPEN:** the unit-period equality as a scalar statement;
quantitative arithmeticity of the normalized period; a Sha map for
the connection; and the retained p=3 provenance seams. No conclusion
is obtained from the absence of an applicable theorem in this task.

## Verification performed

The written identities and quantifiers were checked as above. File
custody verification checks the six opening inputs, the predecessor
manifest identity, and all 20 manifest entries. The final bundle also
checks JSON readability and the existence of its absolute local file
links. Those mechanical checks establish artifact integrity, not
mathematical truth.

No sealed numerical calculation, Lean build, external prover run, or
other task was replayed or modified. Broader arithmetic results are
retained with their qualifications.
