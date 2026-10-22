# W3_UNIFORM_PARTIAL

I derived the missing ramified local lattice, in an explicitly fixed
Gauss-sum frame, and matched its p-power to Kato's Euler factor. I did
not obtain the uniform upper bound on the normalized Kato value.

The new result is a written derivation under the retained arithmetic
inputs and imported local theorems. It still needs independent review.

## The local calculation

For every retained good ordinary p >= 5 outside {19,59,487}, let O be
the actual coefficient DVR and Q the integral singular quotient of
the weight-three representation. The calculation gives

\[
\boxed{\exp^*(Q)=p^{-2}\mathcal O\,e_g,\qquad
b_p=v_\varpi(p^2\xi_g),\quad
\exp^*(\operatorname{loc}_p z_g)=\xi_g e_g.}
\]

The frame e_g includes the specified omega Gauss sum. Its precise
definition and proof are in [LOCAL_LATTICE.md](LOCAL_LATTICE.md).
The proof first identifies Q integrally with cohomology of the
rank-one quotient character. Venjakob's integral Coleman sequence and
finite-level formula then determine the whole image lattice. There
is no unknown extension-class index and no application of Kato 14.21.

## Match to the arithmetic value

Keep Kato's period convention. Write w_g=c_g e_g for a rational
modular de Rham vector and per_g^+(w_g)=Omega_g gamma^+. Then

\[
\boxed{b_p=v_\varpi(A_g),\qquad
A_g=c_g\frac{L(g,2)}{\Omega_g}.}
\]

Indeed p^2 xi_g=(p^2-a_p(g)) A_g, and the factor p^2-a_p(g) is a
unit. The calculation has removed the unknown local denominator.
The remaining comparison scalar c_g is explicitly defined but not
evaluated or assumed a unit. See [KATO_MATCH.md](KATO_MATCH.md).

The exact further claim needed is A_{g_p} not in varpi_p^4 O_p
cofinitely on the ordinary domain. The retained theorem would then
give Sha[p^infinity]=0 there. That claim has not been proved here.

## The family step was tested

The brief needs two corrections: these are separate p-adic Hida
families as p varies, and a weight parameter need not have
varpi-valuation one. Integral analyticity, a double zero, mu=0 and
the tested functional symmetry do not supply the valuation bound.
The canonical rational family basis in the cited literature does
not by itself identify the required integral lattice.

[HIDA_ATTEMPT.md](HIDA_ATTEMPT.md) records the actual test and its
scope. No identity with the old C_p was proved, so the collapse verdict
would be unjustified. No universal impossibility claim is made.

This closes the brief's local-lattice calculation at written-proof
grade. It does not close its integral modular-period comparison or
global valuation bound. The proof directly feeds the already reviewed
ordinary BSD implication; it supplies no new seed primary conclusion.
Supersingular and excluded primes remain separate. FIN, ORDER9 and
Q36 are unchanged.

## Evidence

The input ZIP hash matches the supplied value. The three retained
review manifests pass (53, 37 and 31 files). Exact controls pass for
9 tame-character primes, 137 rank-one parameter cases, 822 Euler
cancellations, 72 formal family examples and 15 ramification cases.
These are formula controls, not seed-index computations or an
independent mathematical review.

[Review handoff](HANDOFF.md) · [Sources](SOURCES.md) ·
[Exact controls](checks/EXACT_CONTROLS.json)
