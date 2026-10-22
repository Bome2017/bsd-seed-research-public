# Response to the independent audit of `a38400a`

Audit: `work/review_input/BSD_PAIRED_KERNEL_REPAIR_HANDOFF_2026-09-23/audit/AUDIT.md`
(sha256 `e6b10459…eafb`, verified). Regression: the audit's `independent_checks.py` was re-run
in this environment; output identical to `INDEPENDENT_CHECKS.json` except `cpu_seconds`.

**No finding is rebutted.** Each was checked against the definitions; all corrections are
applied below. Original texts remain in git history (`a38400a`). Items follow `PROMPT.md`'s
numbering.

| # | finding | verdict | correction (file § ) |
|---|---|---|---|
| 1 | Preserve Theorem A: `K = psi psi^T / M`, `M = sum psi^2`, primitive integral `psi`, factor `1/2`, `B(1) = Id`, Eichler level `N^+ = 8*4547^2`, modular level `N = N^- N^+` | agreed (already proved) | notation `M` introduced; statements unchanged (`01` §3, `RESULT` §§1–2) |
| 2a | Deligne–Serre consequence only for the prime-to-level algebra; raw bad-prime norm matrices not identified with classical `U_q` on old constituents (audit: level-22 `U_2` has char. poly `t^2+2t+2`, nonreal eigenvalues, while raw norm matrices are symmetric) | agreed | `01` §4 Theorem B(4) restated for `T^(N)` with new proof; sufficient condition now "no away-from-level congruence"; `01` §3 Remark 2 now states it uses only commutation of raw `B(q)` with `T^(N)` (distinct places) and Theorem A's coefficientwise identity |
| 2b | Eisenstein exclusion must use a test prime `l != p` | agreed | adopted the audit's certificate `#E(F_5) = 8`, `#E(F_11) = 14` (`01` §4 proof). *Clarification, not rebuttal:* the original script already excluded `l = p` for `p < 10^6` and used the gcd for larger `p`, so the original conclusion was valid; its one-line summary omitted the caveat |
| 2c | `M` = order of the specified lattice quotient; not a Hecke congruence ideal or modular degree (countermodel `M = 2`, `eta = 6`) | agreed | `01` §4 title and "what remains"; `02` §6.2; `RESULT` §3 |
| 3 | R1: keep an integral multiple of the rational prime-to-level projector; remove the Sturm-supported integral expression (characteristic-zero recognition is not an integral spanning theorem) | agreed | `01` §4 end; `02` §6.2 (withdrawn explicitly); `RESULT` §§3–4 |
| 4 | Translation: with `g = diag(1,4547)`, `g^{-1}K_0(4547^2)g = K_T`, right covariance gives `psi(x) = <Psi(xg), v_T>` (not `xg^{-1}`); ratio exactly `4549 + 1/2273`; no runtime gain or integral type projection claimed | agreed (checked: `g^{-1}[[1,1],[0,1]]g = [[1,q],[0,1]] in K_T`) | `01` §5.4; `02` §6.5; `RESULT` §6 |
| 5a | Sturm test sufficient, not necessary | agreed | `01` §3.1; `RESULT` §2 |
| 5b | R1 "must compute the full class set" not proved | agreed | `02` §6.2 (baseline description only) |
| 5c | a single theta coefficient is not automatically "cheap" | agreed | `02` §6.0; `RESULT` §4 |
| 5d | Lemmas C/C' identities correct; component-by-component work not forced | agreed | `02` §§6.1, 6.1'; `RESULT` §4 |
| 5e | typed R2 "same cost" unproved (model volumes only) | agreed | `02` §§6.3, 6.5; `RESULT` §7 |
| 5f | R3: trivial-character conductor is `(7N)^2`; `|beta| >= N/(7p^4)` needs `O ⊕ Oj` to be an integral suborder; off-diagonal periods may carry phase data | agreed | `02` §6.4; `RESULT` §4 |
| 6 | Nelson supplies a general integration method (Thm 5.6, Rem. 5.8; Appendix A squarefree; Rem. B.4 / Thm B.5 general inputs); the gap is explicit nonsquarefree local inputs, certified truncation and cost — not a missing general projection theorem | agreed | `02` §§6.3, 6.6 (first run's "everything explicit except one identity" withdrawn); `RESULT` §§4–5. Source still unreachable here (egress policy); used at the audit's imported grade |
| 7 | Arithmetic reconstruction: `p ∤ M` gives entrywise integrality but a real enclosure needs a denominator/height/discrete-lattice bound or exact arithmetic implementation | agreed | `01` §4; `02` §6.6; `RESULT` §§3, 5, 8 |
| – | Status: keep `PRECISE_MISSING_LEMMA` only as an incomplete-operation label; no new no-go theorem | agreed | `RESULT` header and §5 |

Unchanged and confirmed by the audit: Theorem A with its normalization; Theorem B(1)–(3) for
the unimodular lattice; stabilizer triviality at both class sets; local types at 2 and 4547;
typed complex dimension `119,084,870,288`; `mu_N`, `S_N`, cusp count 145,536; the R2 residue
identity.
