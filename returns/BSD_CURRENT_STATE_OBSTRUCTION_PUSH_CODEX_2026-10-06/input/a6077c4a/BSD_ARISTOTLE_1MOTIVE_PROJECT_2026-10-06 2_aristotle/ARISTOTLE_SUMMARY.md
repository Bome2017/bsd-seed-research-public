# Summary of changes for run 9b34c862-4d5e-4337-bf18-863d4bdffeb0
**STATUS: `NO_CANONICAL_GENERATOR`.** A determinant module exists and is computed below. No canonical p-adic generator intrinsic to \(M_E\) is proved to exist, so I stopped at step 5 and did not attempt step 6. The full write-up, with every claim labelled, is in `RequestProject/OneMotive/RESULT.md`. The Lean skeleton is `RequestProject/OneMotive/Skeleton.lean`: it builds with no `sorry`, and each theorem uses only the standard axioms `propext`, `Classical.choice` and `Quot.sound`.

**Step 1: PRE-CHECK verified, PROVED, no FIN.** \(\mathrm{Sel}(\mathbb Q,M_E)(n)\cong Ш(E/\mathbb Q)[n]\) for every odd \(n\), and so for every odd prime \(p\).
- \(H^0(\mathbb Q,M_E)=E(\mathbb Q)/\langle P_1,P_2\rangle\cong\mathbb Z/2\).
- The Selmer sequence holds by definition.
- \(Ш^2(\mathbb Q,\mathbb Z)=Ш^1(\mathbb Q,\mathbb Q/\mathbb Z)=0\): a character trivial on every decomposition group is unramified everywhere, hence trivial (Minkowski).
- None of \(\infty\), \(p=3\) or the bad primes needs special care.

The proof is uniform in \(p\), but it gives no bound on Ш. One caveat matters for step 3. This Selmer group is strict on the lattice quotient at every place, so it is not of the form the Selmer-complex framework allows, which needs unramified conditions at almost all places.

Two corrections to the task files:
- The torus quotient of the G2 1-motive is \([\mathbb Z^2\to E]\) with \(e_i\mapsto 16P_i\), not \(M_E\) itself. Its \(p\)-adic realization is the same for odd \(p\), so nothing changes.
- PRE-CHECK (f)'s rational claim is wrong (step 4).

**Step 2: PROVED (Lean), recorded only.** Burns–Sakamoto–Sano and Sakamoto rank-zero theory do not apply:
- \(M_E[p]\) is reducible.
- \(T/(1-\tau)T\) surjects onto \(\mathbb Z_p^2\) for every \(\tau\).
- For \(q\equiv1\pmod p\) the singular quotient has rank at least 2, so classical Kolyvagin primes do not exist for \(T_pM_E\).

**Step 3: Macias Castillo–Sano, checked against the arXiv source.** The standing hypotheses (their Hypothesis 2.11) hold outside an explicit finite set of primes for two Greenberg conditions at \(p\):
- the ordinary choice \(T'\) (ordinary \(p\)), with core rank 0;
- the relaxed choice (every good \(p\) in the range), with core rank 1.

Four other choices fail the local hypothesis (ii). The \(p\)-dependent local Kummer line gives core rank −2, for which Stark systems are not defined. With that same line, the class of \(p\) also rules out core vertices built from their rank-one primes.

Whether a core vertex exists (Hypothesis 2.17) for \(T'\) or the relaxed choice is **not verified**. Their Theorems 2.20 (Selmer complex ≃ Poitou–Tate complex) and 3.4 (determinant ≅ Stark systems) are therefore not established for \(T_pM_E\). This does not affect the verdict: an isomorphism of rank-one modules carries canonical elements both ways and cannot create one.

The other two objects do no better:
- **Cartier dual:** its Selmer group contains \((\mathbb Q^\times/p)^2\), which is infinite. By duality its determinant line is the inverse of \(M_E\)'s.
- **G2 1-motive:** no better; this is HEURISTIC.

**Step 4: determinant line, PROVED from imported results (Nekovář's Selmer complexes and heights, Greenberg's comparison, Knudsen–Mumford determinants).**
- The line is canonically \(E\)'s own determinant line. The two lattice factors have canonical bases, and \(P_1,P_2\) enter only the trivialization.
- The complex is acyclic iff \(Ш[p^\infty]\) is finite **and** the cyclotomic \(p\)-adic regulator \(\mathrm{Reg}_p^{\rm int}\) of \(P_1,P_2\) is nonzero.
- In that case \(\#H^2=\#Ш[p^\infty]\cdot|\mathrm{Reg}_p^{\rm int}|_p^{-1}\).
- The resulting mod-\(p\) group is nonzero iff \(Ш[p]\ne0\) or \(p\mid\mathrm{Reg}_p^{\rm int}\). The Mordell–Weil plane that \(M_E\) removes comes back as the height matrix.

**Step 5: verdict.** The only element \(M_E\) supplies on its own is the rational trivialization \(\vartheta_p\).
- It exists only under finiteness at \(p\) plus a nonzero regulator.
- It is just the tautological \(\#Ш[p^\infty]\cdot\mathrm{Reg}_p^{\rm int}\).
- Any other generator would be a generator of \(E\)'s own determinant line. The only known ones come from Kato's zeta element, Heegner points, or an ETNC/BSD normalization, all excluded.

Comparison with the tame scalar (HEURISTIC): \(s_p\doteq x_{\mathbb Q,\Sigma}\#Ш[p^\infty]\) and \(\vartheta_p\doteq\#Ш[p^\infty]\mathrm{Reg}_p^{\rm int}\). Both carry \(\#Ш\), and neither is free of Ш.

I recorded the four Lean results as proved in the Properties table. The written steps 3–5 result is listed as in progress because it is not formalized.

FIN, ORDER9 and Q36: unchanged.