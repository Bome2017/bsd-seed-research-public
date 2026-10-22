# Summary of changes for run 5c324e1c-0209-479d-8e28-e61764af67d7
**Outcome:** FIN, ORDER9 and Q36 are unchanged. I proved one scoped new lemma about the exceptional bad primes and kernel-checked the concrete arithmetic of the seed curve that it relies on. Finiteness of Sha for a curve of analytic rank two remains a well-known open problem, and no cofinite bound was obtained.

**Startup (`STARTUP_RECEIPT.json`).** I worked inside `project/` and did not run the offline-check helper.
- `cd project && python3 prepare_reference.py` exited with status 0. It printed `READING_SET_VERIFIED`, `members_checked: 5180`, with root `project/reading_set/BSD_SEED_ARISTOTLE_2026-10-05`.
- The archive digest matches `READING_SET_BINDING.json`. I re-hashed all 5,180 manifest entries independently, and all match.
- No path or extraction fix was needed.
- The receipt keeps extraction checks separate from reading. It records paths and hashes for `ARISTOTLE_PROMPT.md`, `BSD_SEED_RESEARCH_MAP.md`, `sources/HISTORICAL_STOPS_AND_CORRECTIONS.md` and `guide/03_WALL_ATLAS.md`.
- The governing task, read from those files: FIN, ORDER9 and Q36, kept distinct, for the fixed curve.
- I deleted the extracted copy before returning. It can be rebuilt with the same command and is not in your returned folder. It contains historical Lean projects, including a deliberate axiom-injection control file, which is reference evidence and not part of this build.

**Historical search (`research_return/COLLISION_CHECK.md`).** I read all 44 wall cards and keyword-searched the stop/correction register, the receiver dossiers and the release claims. This was not an exhaustive novelty search. I tested three uniform mechanisms, and each leaves its recorded first failed implication unchanged, so I did not develop them:
- **Heegner–Kolyvagin systems:** register entries E12a-158 and E13-112 record that these give no bound across primes.
- **Second coefficient of the p-adic L-function:** release claim B.1 and cards W24/W25 record that it is not controlled uniformly across primes.
- **New genus-two source curve:** I found a splitting `Jac(C) ~ E × E2` with an explicit `E2`. It only touches the twisted summand of the receiver, which carries no Sha.

**New result (`research_return/RESULT.md`, `PROOF.md`).** Theorem BFR: for \(p \in \{2243, 4547, 5843\}\), restriction gives an injection `Sha[p] ↪ B_p = Hom_Γ(Cl(O_{L_p}[1/p])/p, E[p])`. So \(p^{2\dim \text{Sha}[p]}\) divides that class number, and `dim B_p ≤ 1` implies `Sha[p^∞] = 0`.
- Previously the forward receiver was stated only for good primes, and claim B.20 explicitly leaves these three primes out.
- The proof also finds a scope limit in the record: at 4547 the auxiliary point `R_p` is locally p-divisible, so it does not supply the local Kummer line there. I replaced it with `P2`, using an exact local check.
- BFR is a written proof. Its imports (residual image A.3, Mordell–Weil basis R.1, Tamagawa numbers, formal groups, class field theory, and parity for the vanishing part) are listed in `ASSUMPTIONS.json`. It is not kernel-checked as a whole, so it stays in progress in the Properties table.
- Effect on the endpoints: none. The bad-prime obligations are still open but now share the receiver criterion used at good primes. BFR does not supply the receiver's missing independent bound, so it is not a uniform mechanism.

**Lean (`RequestProject/Seed/*.lean`).** Everything builds with no `sorry`, no new axioms and no `native_decide`, using only `propext`, `Classical.choice` and `Quot.sound` (see `research_return/lean/`). It covers:
- the model change, \(\Delta = 2^8\cdot3^2\cdot2243\cdot4547^3\cdot5843^2\), the basis points, `T` of order 2, and \(\#E(\mathbb F_5)=8\);
- for every odd prime \(p\), the receiver point `R_p` lies in \(E_1(\mathbb Q_p)\setminus E_2(\mathbb Q_p)\) (via Hensel), and \(d_p\cdot(\pm p)\) is not a rational square;
- the 4547 certificate, evaluated by the kernel. It agrees with an independent Python computation (the same residue, 1274 mod p).

`research_return/HANDOFF.md` states the next unresolved step: an independent bound on `dim B_p` for all but finitely many primes. No follow-up jobs, paid computations, messages or publication were made.