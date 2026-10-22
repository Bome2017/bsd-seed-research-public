# BSD target-curve push: weight-three local-index route

Date: 2026-10-04

## Status

**ACTIVE CONSTRUCTION TARGET --- not a theorem that FIN is solved.**

This brief deliberately abandons the recently tested closed-cycle /
two-prime-content / (C_p) repair loop.

The retained weight-three theorem gives a genuinely one-way upper bound.
For each good ordinary seed prime (p`\ge5`{=tex}) outside ({19,59,487}),
let (g_p) be the retained weight-three ordinary specialization with
nebentypus (`\omega`{=tex}\^{-1}), let (`\mathcal `{=tex}O_p) be its
coefficient DVR with uniformizer (`\varpi`{=tex}), and let

\[ b_p=`\operatorname{length}`{=tex}\_{`\mathcal `{=tex}O_p}
`\left`{=tex}(
Q_p/`\mathcal `{=tex}O_p,`\operatorname{loc}`{=tex}*p\^s(z*{g_p})
`\right`{=tex}), \]

where
(Q_p=H^1(`\mathbf `{=tex}Q_p,T\_{g_p})/H_f^1(`\mathbf `{=tex}Q_p,T\_{g_p})).

The retained reviewed derivation proves

\[
`\dim`{=tex}\_{`\mathbf `{=tex}F_p}`\Sha`{=tex}(E/`\mathbf `{=tex}Q)\[p\]
`\le `{=tex}b_p-2. `\tag{1}`{=tex} \]

Retained parity therefore gives

\[ `\boxed{b_p\le3\Longrightarrow\Sha(E/\mathbf Q)[p^\infty]=0.}`{=tex}
`\tag{2}`{=tex} \]

Unlike the two-prime scalar (C_p), (b_p) is not *defined* by whether
(`\Sha[p]`{=tex}) vanishes. It is a local integral index attached to a
noncentral weight-three Kato class. This makes an independent local
calculation a legitimate possible upper bound.

## 1. Exact construction problem

Write

\[ P\_{g_p}:=`\exp`{=tex}\^\* `\left`{=tex}(
H^1(`\mathbf `{=tex}Q_p,T\_{g_p})/H_f^1(`\mathbf `{=tex}Q_p,T\_{g_p})
`\right`{=tex}) =d\_{g_p}`\mathcal `{=tex}O_p \]

inside the one-dimensional de Rham target and put

\[ x\_{g_p}:=`\exp`{=tex}\^\*(`\operatorname{loc}`{=tex}*p\^s z*{g_p}).
\]

Then

\[ `\boxed{b_p=v_\varpi(x_{g_p}/d_{g_p}).}`{=tex} `\tag{3}`{=tex} \]

The construction target is therefore **not** "prove a uniform Selmer
bound." It is the following explicit integral local statement:

\[ `\boxed{v_\varpi(x_{g_p})-v_\varpi(d_{g_p})\le3}`{=tex}
`\tag{W3}`{=tex} \]

for all but finitely many good ordinary seed primes.

A proof of (W3), combined with the already reviewed theorem (1), closes
the ordinary cofinite part of FIN.

## 2. First subproblem: compute the actual lattice (d\_{g_p})

The previous project stopped because Kato 14.21 assumes (p`\nmid`{=tex})
the modular level, whereas (g_p) has nebentypus (`\omega`{=tex}\^{-1})
ramified at (p). Do **not** invoke 14.21.

Instead use the explicit ordinary filtration retained in the review:

\[ 0`\to`{=tex} `\mathcal `{=tex}O_p(`\alpha`{=tex}\^{-1}`\chi`{=tex})
`\to `{=tex}T\_{g_p} `\to`{=tex}
`\mathcal `{=tex}O_p(`\alpha`{=tex}`\chi`{=tex}\^{-1}`\omega`{=tex})
`\to0`{=tex}, `\qquad `{=tex}`\bar`{=tex}`\alpha`{=tex}`\ne1`{=tex}.
`\tag{4}`{=tex} \]

Compute the image of the integral singular quotient under
(`\exp`{=tex}\^\*) directly from (4).

Required output of this subproblem:

\[ `\boxed{d_{g_p}=\varpi^{\,\lambda_p}u_p}`{=tex} `\qquad`{=tex}
(u_p`\in`{=tex}`\mathcal `{=tex}O_p\^`\times`{=tex}) `\tag{5}`{=tex} \]

with an explicit formula/bound for (`\lambda`{=tex}\_p) that is uniform
in (p).

A statement merely saying that the rational dual exponential is an
isomorphism does not count. The integral lattice is the entire point.

### Candidate local technology

Use a rank-one ((`\varphi`{=tex},`\Gamma`{=tex}))-module /
local-(`\varepsilon`{=tex})-isomorphism computation for the quotient
character (`\alpha`{=tex}`\chi`{=tex}\^{-1}`\omega`{=tex}), together
with the extension (4). Berger's explicit formulas for Bloch--Kato
exponentials and later rank-one epsilon-isomorphism formulas are
relevant because they retain Gauss/epsilon and integral lattice factors
that disappear after tensoring with the coefficient field.

The first decisive test is whether the tame (`\omega`{=tex})-factor
contributes a fixed valuation (expected to be small) rather than an
uncontrolled (p)-dependent denominator.

If the exact computation gives (`\lambda`{=tex}\_p) unbounded or
requires the unknown seed Selmer group, stop this route. Otherwise
freeze (5) before touching the global Kato value.

## 3. Second subproblem: compute (x\_{g_p}) in the same basis

Kato explicit reciprocity identifies the dual-exponential image of the
normalized zeta class with a critical algebraic (L)-value after fixing
the correct de Rham basis.

The project must use **the same basis as (5)**. No arbitrary period
rescaling is allowed.

The desired formula has the form

\[ x\_{g_p} = `\mathcal `{=tex}E_p, L\^{`\mathrm{alg}`{=tex}}(g_p,2),
`\eta`{=tex}\_{g_p}, `\tag{6}`{=tex} \]

where every Euler, Gauss, congruence and period factor in
(`\mathcal `{=tex}E_p) is written explicitly and (`\eta`{=tex}*{g_p}) is
the integral de Rham generator used to compute (d*{g_p}).

A potentially useful source-level repair is the canonical
ordinary-Hida-family basis used in modern formulations of Kato
reciprocity: in that normalization the otherwise arbitrary correction
factors can be made explicit (and in some formulations equal to one).
This must be checked against the project's exact (g_p), lattice and
nebentypus; it is not an imported conclusion.

Substitute (5) and (6) into (3):

\[ b_p= v\_`\varpi`{=tex}(`\mathcal `{=tex}E_p
L\^{`\mathrm{alg}`{=tex}}(g_p,2)) -`\lambda`{=tex}\_p. `\tag{7}`{=tex}
\]

Equation (7) is the first acceptable endpoint of the local calculation.

## 4. Third subproblem: exploit the fact that (g_p) is a specialization of one ordinary family

Do not treat the (g_p) as unrelated forms.

Let (`\mathbf `{=tex}g) be the retained ordinary Hida branch through the
seed. Package (6) as the specialization of the branch's integral
two-variable/weight-variable (p)-adic (L)-element or normalized Kato
regulator (`\mathcal `{=tex}L\_{`\mathbf `{=tex}g}).

The required construction is an **integral Taylor statement at the
weight-two seed point**:

\[ `\mathcal `{=tex}L\_{`\mathbf `{=tex}g}(T) = T\^2 U_p(T)
`\tag{8}`{=tex} \]

in the appropriate local branch coordinate, with

\[ `\boxed{v_\varpi(U_p(t_3))\le 1}`{=tex} `\tag{9}`{=tex} \]

at the weight-three specialization (t_3), after all factors from
(5)--(7) have been included.

The (T\^2) is not to be assumed from complex analytic rank. Its integral
source must be the already retained rank-two/Kato/Fitting information or
a proved specialization identity. Likewise, (9) is the new arithmetic
content; calling (U_p) a "unit" without proving it is exactly the old
(C_p) mistake.

If (8)--(9) are proved, then (7) gives (b_p`\le3`{=tex}), hence (2)
gives (`\Sha[p^\infty]=0`{=tex}) on the ordinary cofinite domain.

## 5. Anti-circularity tests

The route is admitted only if all of the following pass.

1.  **No (C_p) substitution.** If (U_p(t_3)`\bmod`{=tex}`\varpi`{=tex})
    is identified with the old two-prime scalar (C_p), the route has
    collapsed back to the already open problem. Record that identity and
    stop.
2.  **No Sha-defined lattice.** Neither (d\_{g_p}) nor its valuation may
    be defined using the size or vanishing of (`\Sha[p]`{=tex}).
3.  **No Kato-14.21 shortcut.** Its printed (p`\nmid `{=tex}N_g)
    hypothesis fails for this datum.
4.  **No rational-only computation.** An isomorphism after tensoring
    with (L_p) gives no bound on (b_p).
5.  **No finite-pool argument.** (g_p) varies with (p); a fixed finite
    set of weight-three forms is not the target.
6.  **Endpoint test.** The return must end with either a proved
    numerical inequality (b_p`\le3`{=tex}) on a cofinite ordinary
    domain, a genuinely new bound (b_p`\le `{=tex}C) with (C)
    independent of (p), or an explicit theorem-level obstruction showing
    why the integral local calculation cannot provide such a bound.

## 6. Why this is currently preferable to the exhausted (C_p) repair

The two-prime work now gives \[ `\delta`{=tex}*{ab}=C_p e_a
e_bD*{ab}\^2, `\qquad`{=tex}
C_p`\ne0`{=tex}`\Longleftrightarrow`{=tex}`\Sha[p^\infty]=0`{=tex}. \]
The recent conductor-descent attempt did not independently evaluate
(C_p).

By contrast the weight-three theorem has already proved an inequality
whose direction is useful:

\[ `\dim`{=tex}`\Sha[p]`{=tex}`\le `{=tex}b_p-2. \]

Thus an independent *upper bound* on a concrete local integral index
suffices; equality with a Sha-detecting scalar is not built into the
definition of (b_p).

That is the mathematical reason for changing branches.

## 7. Coverage after success

A successful proof of (W3) handles good **ordinary** primes outside the
retained finite exception set. It does not by itself cover supersingular
good primes or the bad primes (2243,4547,5843). Those become
finite/structured remaining obligations rather than an infinite ordinary
tail.

The project must not describe this as full FIN until those remaining
domains are discharged.

## 8. Required return status

Return exactly one of:

-   `W3_COFINITE_BOUND`: proved (b_p`\le3`{=tex}) on a cofinite ordinary
    seed domain, with all lattice normalizations.
-   `W3_UNIFORM_PARTIAL`: a new proved (p)-independent bound or exact
    lattice formula that strictly reduces (W3).
-   `W3_COLLAPSES_TO_CP`: the leading integral coefficient is proved to
    be the already-open (C_p) (or equivalent witness).
-   `W3_LOCAL_OBSTRUCTION`: a proved obstruction to obtaining the
    required integral bound from this weight-three datum.
-   `NO_NEW_RESULT`.

Do not return an audit narrative in place of one of these mathematical
outcomes.
