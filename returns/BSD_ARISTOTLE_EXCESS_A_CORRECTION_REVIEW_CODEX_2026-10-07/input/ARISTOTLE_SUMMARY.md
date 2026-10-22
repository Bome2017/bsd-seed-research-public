# Summary of changes for run ea3c5608-a8d9-426e-b0b3-cd345320eb9c
You were right on both points. The return has been corrected in place, and nothing has been upgraded.

**The status is unchanged:** NO_BOUND_MECHANISM_FOUND_FOR_TESTED_CANDIDATES, and FIN, ORDER9 and Q36 are unchanged. The return now contains **no new derivation**.

**1. The Fitting-to-Heegner equivalence is withdrawn.** The step "\(\Theta_1(0)\otimes\mathbb F_p\) is a unit ⇔ some \(\kappa_\ell\not\equiv0\) mod \(p\)" treated three different objects as the same thing without proof:
- the Da Ronche–Longo–Vigni (DLV) ideals, whose construction was never read here;
- Howard's Λ-adic Heegner Kolyvagin system;
- Zhang's classical classes \(\kappa_n\).

Four missing comparisons are written out in `project/RETURN_LANE_A/CORRECTIONS_2026-10-07.md`:
- **C1:** which Euler system the DLV ideals are built from.
- **C2:** a factor at \(p\) that appears when the Λ-adic family is specialized at \(T=0\). It depends on \(p\), and nothing on the domain controls its \(p\)-adic valuation.
- **C3:** a Λ-coordinate versus a class. The classes \(\kappa_\ell\) are ramified at \(\ell\), and \(H^1_f(K,T)\) has rank 3 here.
- **C4:** fixed normalizations (modular parametrization, Manin constant, choice of Heegner point).

Two pieces survive:
- The control sequence with \(H^2\) kept. This is standard.
- The equivalence of \(\dim X_p\le1\), \(X_p=0\) and \(\nu_p=1\) where \(s^-=1\). This is not new: it is the record's existing `nu_le_two_iff_sha_of_twist`.

So the higher-Fitting candidate (A1) is **not** reduced to the derived-Heegner candidate (A2). Its status is now "control map written; comparison of generators open; not developed". The "common failed arrow" now covers only A2 and A3.

**2. The "−23 never computed" claim is withdrawn.** The trace is in `TWIST_D23_TRACE.md`. By date, the record holds:
- a **2026-09-21** Arb certificate, \(39.512236\le L'(E^{-23},1)\le40.182321\), recorded as PROVED_COMPUTER_ASSISTED;
- a **2026-10-06** floating-point value of 39.84727806412, computed with a separate coefficient engine and marked not certified by its author.

These are the reverse of the order you described. That is just what the files' dates show; I may be missing the sense of "later" you meant.

**What I could recheck exactly.** These are standard-library Python checks; no L-series sum was recomputed. They are in `checks/d23_trace_check.py`, with output in `checks/d23_trace_check.out.json`.
- **Manifest:** 17 of the certificate's 1,070 manifest entries are in the archive. All 17 match their hashes, and so do the hash fields inside `RESULT.json`.
- **Tail bound:** I checked the derivation line by line and evaluated it at 80 digits. It matches the logged value 0.33504179704832… to every printed digit.
- **Endpoints:** both lie inside the stated interval. The interval clears zero by a factor of about 119.
- **Root number:** \(\chi_{-23}(-N)=-1\), so the twist's root number is \(-1\), assuming the imported seed root number \(+1\).
- **Model:** the certificate's model and the governing model have the same \(c_4,c_6\), so they are the same curve.
- **Float value:** re-derived from its saved bucket sums, it lies inside the interval and differs from the certified partial sum by \(-2.5\cdot10^{-7}\).

**What I could not check:** the finite sum itself. The supplied archive lacks:
- `twist.c` and `retained_arbcore.c` (their hashes are in `BUILD_BINDINGS.json`; the host inventory lists both files, but without hashes);
- the binary;
- all 1,030 work units;
- the coefficient files, which are referenced by host paths and were reused without re-witnessing (`witness_replay: false`).

If you can locate those files on the host and they match the recorded hashes, the record's own `review_completion.py` is the replay entry point.

In this return the twist result is graded "record-certified, computer-assisted, core not replayable from the supplied archive". Whether to retain it is your decision.

**Files changed.** `RESULT.md`, `PROOF.md`, `CONSTRUCTION.md`, `ENDPOINT_EFFECT.md`, `ASSUMPTIONS.json`, `COLLISION_CHECK.md`, `SOURCES.md`, `RESUME.md`, `STATE.json`, `NOTES.md` and `MANIFEST.sha256` were updated to match; the first version stays in git history. No Lean was written, no remote job was run and nothing was published. The unpacked archive folders were deleted again before committing; rerunning `prepare_reference.py` restores them.

# Summary of changes for run cce37633-9132-472c-a958-a58afce2f667
**Result: NO_BOUND_MECHANISM_FOUND_FOR_TESTED_CANDIDATES.** I did not construct an independent arithmetic bound or annihilator for \(X_p=\mathrm{Sel}_p(E/\mathbb{Q})/W_p=\text{Ш}[p]\). FIN, ORDER9 and Q36 are unchanged for the seed curve. As far as I know, nobody has proved Ш finite, even outside finitely many primes, for any curve over \(\mathbb{Q}\) of analytic rank at least 2. This lane is aimed at that open problem, and I am not claiming that no mechanism exists.

**Setup.** I ran `prepare_reference.py`: both archives were verified (6,566 members hash-checked). Hash-checking is not reading. `STARTUP_RECEIPT.json` and `SOURCES.md` list what I actually read: the five governing documents in full, four record files in part, and keyword searches of the historical register. Before developing each candidate I checked the record for earlier attempts at it.

**Candidates tested, with the first step that fails:**
- **A1, anticyclotomic higher Fitting ideals (the source TASK.md suggested).** I wrote the control map down exactly, at the trivial character (\(T=0\)), keeping the H² torsion:
  \[0\to H^1_\Lambda/T\to H^1_f(K,T)\to H^2_\Lambda[T]\to 0,\qquad H^2_f(K,T)=H^2_\Lambda/T.\]
  The particular generator you asked me to identify is the image there of a one-prime derived Heegner class \(\kappa_\ell \bmod p\). The \(\Lambda\)-adic structure adds no control at that point. So A1 reduces to A2 and I stopped it.
- **A2, Kolyvagin's structure theorem via derived Heegner classes.** This collides with the existing `HEEGNER_NU.md` and the earlier continuation return. The step that fails is a uniform-in-\(p\) nonvanishing of some \(\kappa_\ell \bmod p\); nothing supplies it.
- **A3, Kato's divisibility plus the Perrin-Riou/Schneider leading term.** This gives
  \[\dim \text{Ш}[p] \le v_p(L_p^*) - v_p(R_p/p^2) - (\text{local terms}).\]
  Closing it would need \(R_p/p^2\) to be a unit uniformly, which is the forbidden wild-regulator unit property, and a bound on \(L_p^*\) that does not assume \(p\)-adic BSD. It also covers ordinary primes only. This collides with the record's d-infinity/HGZ2 entries and its \(p\)-adic regulator entries.

**The one new derivation** (`PROOF.md`, Proposition 1: written by me, not reviewed, not formalized). On an explicit set of primes \(D\), these are equivalent:
- \(\dim X_p \le 1\);
- \(X_p = 0\);
- \(\nu_p = 1\), meaning some one-prime class \(\kappa_\ell\) is nonzero mod \(p\);
- the \(T=0\) image of the first Euler-system ideal \(\Theta_1\) is a unit mod \(p\).

This makes the A1 → A2 reduction exact, but it is an equivalence, not a bound. Three caveats:
- \(D\) depends on \(\mathrm{ord}_{s=1}L(E^{(-23)},s)=1\) (the twist by \(-23\)), which neither this run nor the record has computed.
- The theorems of Kolyvagin/Zhang, Howard and Nekovář are cited at statement level only.
- The text of the higher Fitting ideals paper itself is not in the archive, so I relied on the summary in `LOCAL_ATTEMPT.md`.

**Common failure.** All three candidates break at the same point: there is no uniform-in-\(p\) nonvanishing mod \(p\) of a \(p\)-dependent second-order quantity (\(\kappa_\ell \bmod p\), or \(L_p^*/(R_p/p^2)\)).

**Files.** Everything is in `project/RETURN_LANE_A/`: `RESULT.md`, `PROOF.md`, `CONSTRUCTION.md`, `COLLISION_CHECK.md`, `ASSUMPTIONS.json`, `ENDPOINT_EFFECT.md`, `SOURCES.md`, `RESUME.md`, `STATE.json`, `NOTES.md`, `STARTUP_RECEIPT.json` and `MANIFEST.sha256`. I wrote no Lean: there was no new formal step to check, and the Kolyvagin bookkeeping is already checked in the record's `Coinvariant/KolyvaginOrder.lean`. I ran no computations or remote jobs and published nothing.

**Extracted archives removed.** The unpacked `reading_set/` and `current_overlay/` folders contain old Lean test files that declare deliberate unsound axioms. I deleted those unpacked folders from the project at the end so they are not returned with it. Rerunning `prepare_reference.py` restores them; this is noted in `RESUME.md`. The return is committed.