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