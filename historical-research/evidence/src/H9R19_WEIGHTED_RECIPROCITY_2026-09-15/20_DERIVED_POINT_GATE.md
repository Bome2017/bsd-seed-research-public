# 20 — DERIVED-POINT GATE (operator architecture, 2026-09-16): differentiate the sealed same-sheet point family along Rivero's C
Sources: sealed milestone ~/H9R16C_SEALED_MILESTONE_2026-09-15 (00_MILESTONE.md theorem block; 01_THEOREMS.md sec 6, sec 9;
05_NON_CLAIMS.md l.41); Rivero, "Generalized Kato classes and exceptional zero conjectures" (WRAP 166838; archived as lane file 21):
l.127-130 (standing hypothesis), l.795-830 (Euler factor (14), Prop 3.5), l.884-902 (S, C, Prop 3.6, (16)), l.905-935 (Prop 3.7, (17),
delta), l.321-323 (p split CM remark), l.955-962 (Thm 3.10). Two gates, in order, kill-first; no new H9R number.

## Gate 1 — does the sealed H9R16-C point object exist over a 2-dimensional local base containing C, before specialization?
What the seal says (00 theorem block; 01 sec 6, sec 9):
 (a) The sealed system Q_inf = (Q_r)_r lies in P^nat_inf, "a module over Hida's big ordinary Hecke algebra T'_inf(N_g) = lim_r R_r",
     R_r = e'_ord T'_{N_g p^r} (x) Z_p. That is ONE Hida direction: the g-tower. No other family structure is sealed.
 (b) The two auxiliary factors are COLLAPSED to the diagonal at the carrier level: "B^bal_r = R_r (x)_{R_r} R_r ~ R_r, [t_2 (x) t_3] -> t_2 t_3"
     (01 sec 6; the balancing relation IS R_r-bilinearity). The h = g^c factor carries the same R_r as g; the direction wt(h) != wt(g)
     does not exist in the sealed object. It is destroyed by construction, not by a later specialization.
 (c) The f-factor is a receptacle, not a family parameter: values in J^(1)_r(F'_r)^ord (Jacobian of X_1(N_f p^r)), "weight 2 throughout"
     (01 conventions), indexed by the SAME r as the g-tower. No f-weight (Hida) module structure is sealed.
 (d) Even the specialization to E is an explicit non-claim: 05 l.41, "the chain P^nat_inf -> P^nat_{inf,p_g} -> (E(Q) (x) Q_p) (x)^ R_{g,p_g}
     --lambda_g--> E(Q) (x) F_g | NOT PROVED, and does not follow from anything sealed here."
What Rivero's derivative needs (Prop 3.7, l.905-935): S = Lambda_{U_f} (x)^ Lambda_{U_h} ~ Z_p[[X, Z]] (the surface wt(x) + wt(z) = wt(y) + 2),
C = {X = 0} = {wt(x) = 2, wt(y) = wt(z)}, delta = (gamma - 1) (x) 1: the derivative is taken in the f-WEIGHT direction X, and off C the
h-weight moves with it (wt(z) = wt(y) + 2 - wt(x)). Both transverse ingredients — an f-weight family variable and wt(z) != wt(y) — are
absent from the sealed object by (b) and (c). The sealed object lives on (the g-direction of) C only.
  GATE_1 = NO. The sealed point object is not defined over any 2-dimensional base containing C; the transverse direction of Rivero's S
  does not exist in it. Operator rule: kill immediately.

## Premise check (recorded; not a gate) — "the entire big class vanishes on C" is an exceptional-zero statement
Rivero l.127-130: "To simplify the exposition, we assume that f has split multiplicative reduction at p ... We keep this assumption from
now on." Prop 3.6 proves kappa|_C = 0 through (16): kappa(f,g,h)|_S = (1 - chi-bar(p) alpha_{g_y} / (alpha_{f_x} alpha_{h_z})) kappa*_g, and on C
with h = g*, chi-bar(p) alpha_{g_y} = alpha_{h_y}, so the factor is 1 - alpha_f^{-1}, which vanishes iff alpha_f = a_p(f) = 1 (split
multiplicative). For the lane's E (good ordinary at p, p not dividing N, p split in K) alpha_f != 1, the factor is a nonzero constant on
C, and kappa|_C = 0 iff the improved class kappa*_g|_C = 0 — not printed. On our line I the only printed vanishing is at the target
(Cornut–Vatsal, CH Cor 4.8(2); lane 03/09), not along the line. So even with a 2-dimensional point object, P|_C = 0 would be an
unproved premise for E, and Prop 3.7's division by delta would not apply.
Also recorded: Rivero l.321-323, for CM theta series with p SPLIT "one has a trivial equality of the form 0 = 0" — his derived-class
formulas degenerate in exactly the lane's dihedral configuration.

## Gate 2 — NOT RUN (gate 1 failed). For the record, what it would have needed: Thm 3.10 computes only the g-projection of the derived
local class, <log_BK(kappa'_p)^g, omega_f (x) eta_g (x) omega_h> = L . L_p^{g_alpha}(f,g,h)(x_0,y_0,z_0) (mod L^x); strictness (loc_p P'_0 = 0)
is a statement about the f-projection, which Thm 3.10 does not compute.

## Return
```
SEALED_OBJECT_BASE             = one Hida direction (T'_inf(N_g)); g/h collapsed to the diagonal at the carrier (B^bal_r ~ R_r);
                                 f-factor a weight-2 Jacobian-tower receptacle indexed by the same r; E-specialization a NON-CLAIM (05 l.41)
TRANSVERSE_DIRECTION_AVAILABLE = NO (Rivero's delta = f-weight variable X, with wt(z) - wt(y) = 2 - wt(x) off C; neither exists in the seal)
RIVERO_VANISHING_HYPOTHESIS    = f split multiplicative at p (l.127-130); Euler factor on C = 1 - alpha_f^{-1}; nonzero for the lane's good-ordinary E
GATE_1                         = NO
GATE_2                         = NOT RUN
FIRST_DEFECT                   = the sealed point object has no transverse direction to C: its only family variable is the g-tower, its two
                                 auxiliary factors are identified at the carrier, and its f-side is a fixed-weight receptacle. Division by delta
                                 has nothing to act on.
ARCHITECTURE                   = KILLED at gate 1 (operator rule). No new H9R number. No agent launched.
```
