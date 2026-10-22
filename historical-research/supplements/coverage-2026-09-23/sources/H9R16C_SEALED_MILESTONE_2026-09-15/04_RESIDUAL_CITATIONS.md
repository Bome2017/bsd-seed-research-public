# 04 — Residual citation ledger

**None of these is an unproved mathematical step of the assembly.** All three are citation-level items.

## R1 — `(AJ-corr)`: étale Abel–Jacobi functoriality under algebraic correspondences

Used for the evaluationwise (scalar) D4. Named as Jannsen, *Mixed motives and algebraic K-theory* (LNM 1400)
§9, and Nekovář, *p-adic Abel–Jacobi maps and p-adic heights* (2000) §1; **the numbered statement is not
pinned** and neither source is in the packet. BCPV themselves use the same principle (their Prop 6.2, via
Daub's thesis Prop 2.3.5, de Rham side; and the Hecke-equivariance of `cl_1` in the proof of their Cor 4.11).
Status: **frozen `PROVED_FORMAL` by the operator.**

## R2 — `(G2)`: `ϖ_{1,*}U'_p = U'_pϖ_{1,*}`

**Printed twice** in DR22 §1.3 (DR22.tex l.1220–1222, "the operator `U_p^*` is compatible with the transition
maps…", and l.1569, "Since `U_p^*` commutes with the push-forward maps `ϖ_{1*}`"), with `U_p^* = π_{1*}π_2^*`
their (= our) `U'_p`. **DR22 give no proof of it**, and none of our lanes re-proved it. It is verified
numerically in ten independent exact runs. The `H_π` lane, which leans on it, calls it its one black box and
names the route to a proof if a referee insists: the explicit `π_{1*}π_2^*` computation on `X_{r,r+1}`. It is
also *not* provable by the base-change argument that handles `ℓ ≠ p`: the `q_2`-square for `ℓ = p` is not
cartesian, which is why DR22 state it separately.

## R3 — the tame push-down convention

`NOT_PRINTED` in BCPV: they write `ϖ_{1,*}` for the tame direction (`definition_big_diagonal_Hida_families`
l.1457; `pr_h` in (4.16), l.1486–1487) but define `ϖ_1` only in the `p`-direction (l.1198–1199). Decided here
as the forgetful `pr^t_1`, on the inherited KLZ17/DR22 index-1 convention (KLZ17 l.541–551 defines `pr_1`,
`pr_2` for arbitrary `A` with `pr_1` the identity on `ℍ`; KLZ17 l.800 uses the "natural" degeneracy for the
common→native step). **Both audits proved the tower relation and its constant are unchanged by the choice**,
provided it is used uniformly in `r`; what the choice moves is the identity of the constructed point, by the
tame-degeneracy interchange of `01` §3.

## Not used anywhere in this seal

**Ohta 2000 (Math. Ann. 318), Cor 1.3.8 / 2.3.6** — `NOT_OBTAINED` throughout the program. KLZ17 cites it for
the proof of the Λ-adic pairing. Nothing sealed here depends on it: the finite-level group-ring form (`01` §4)
is derived, not extracted. Also unused: KLZ17's control theorem and its standing `p ≥ 5`; BCPV (4.9);
Hida's Mordell–Weil control theorems; any Selmer, Sha, `L`-value, density or weight-one input.
