# Excerpts of the actually submitted FULL_COMPENDIUM.md

Source SHA-256: a7d5db63eae00fb9433fa2276e7a9f876c0c32cbd4d99fb2e9d887f14a6d3a97

## Source lines 329–342

329: **Evidence:** `~/BSD_SEED_V026_BANK_2026-09-30/repo/claims/claims.json:314`, `~/BSD_SEED_V026_BANK_2026-09-30/repo/claims/CLAIM_INDEX.md:197`, `~/BSD_SEED_V026_BANK_2026-09-30/repo/paper/sections/03_rank.tex:8` [unit E9a-014]
330:
331: ##### D=-23 twist: certified L-prime interval 39.512236 <= L'(E^{-23},1) <= 40.182321; analytic rank one
332:
333: **Statement.** The isolated table-free computation (_work/d23_twist_2026-09-21/RESULT.md, PROOF.md) proves 39.512236 <= L'(E^{-23},1) <= 40.182321. The root number of the twist is -1, so the twist has analytic rank exactly one. With the retained Gross-Zagier-Kolyvagin rank-one theorem and the seed rank theorem: rank E^{-23}(Q)=1 and rank E(Q(sqrt(-23)))=3. This supplies the suitable certified rank-one twist premise of the Fitting-ideal shift; no Stark ideal is evaluated; no new seed primary component, FIN, ORDER9 or Q36 follows. Finiteness of Sha of the twist does not imply finiteness for the seed or for E/K.
334:
335: **Status.** PROVED_COMPUTER_ASSISTED (record: "TWIST_D23_NONZERO_CERTIFIED"). **Reviewed by:** completion review (same-family session); Arb enclosure [tier: SAME_FAMILY_MODEL, EXACT]. **Date:** 2026-09-21.
336:
337: **Depends on:** seed RANK theorem; Gross-Zagier-Kolyvagin rank-one theorem; C11 coefficient corpus. **Connects to:** Fitting shift by three; MCS join; p=13 splitting conditions.
338:
339: > "39.512236\le L'(E^{-23},1)\le40.182321." (`~/BSD_CODEX6_MASTER_HANDOFF_2026-09-19/MASTER_BSD_DAG.md:689`)
340:
341: **Evidence:** `~/BSD_CODEX6_MASTER_HANDOFF_2026-09-19/00_READ_FIRST.md:12`, `~/BSD_CODEX6_MASTER_HANDOFF_2026-09-19/RESUME.md:16-18`, `~/BSD_CODEX6_MASTER_HANDOFF_2026-09-19/MASTER_BSD_DAG.md:687-693` [unit E4a-005]
342:

## Source lines 518–530

518:   - Also recorded: R.3: certified interval for L''(E,1)/2 (PROVED_COMPUTER_ASSISTED, 2026-09-29; `~/BSD_BUILD_MAP/PARTS_MAP.md:34`) [unit E12a-004]
519:
520: ##### D=-23 twist: 39.512236 <= L'(E^-23,1) <= 40.182321 (TWIST_D23_NONZERO_CERTIFIED)
521:
522: **Statement.** For E: y^2=x^3-22735x^2+106272484x and K=Q(sqrt(-23)): computer-assisted Arb enclosure 39.512236 <= L'(E^{-23},1) <= 40.182321 (integer form [39512236, 40182321]/1000000; outward-rounded rationals). At cutoff T=3,456,106,495 the finite sum has conservative enclosure 2S_T = 39.847278312318874 +- 4.28*10^-16 (includes all Arb rounding and Taylor remainder); infinite tail B_{-23}(T) <= 0.335041797049. Original cutoff sufficed; the seven-billion extension (max 7012876287, 418 segments) was not executed. Root number of twist -1 so central value vanishes; ord_{s=1}L(E^{-23},s)=1.
523:
524: **Status.** PROVED_COMPUTER_ASSISTED (record: "TWIST_D23_NONZERO_CERTIFIED"). **Reviewed by:** COMPLETION_REVIEW.json metadata/custody replay (same session); exact rational recheck of endpoint arithmetic in D23_COVERAGE_REVIEW [tier: EXACT]. **Date:** 2026-09-21.
525:
526: **Depends on:** retained verified coefficient corpus (C11 bindings); imported functional equation and conductor facts; written tail/model bounds; new compiled Arb adapter twist.c 4eef4e086e69c7cd. **History:** Supersedes 'No suitable rank-one twist is certified' (MCS_DERIVED_HEIGHT_GATE section 3); D23 feasibility: cutoff adequacy not established. **Connects to:** MCS_NONSQUAREFREE_JOIN; MCS_DERIVED_HEIGHT_GATE eq (4); p=13 I3.
527:
528: > "\boxed{39.512236\le L'(E^{-23},1)\le40.182321.}" (`~/BSD_CODEX6_MASTER_HANDOFF_2026-09-19/_work/d23_twist_2026-09-21/RESULT.md:6`)
529:
530: **Evidence:** `~/BSD_CODEX6_MASTER_HANDOFF_2026-09-19/_work/d23_twist_2026-09-21/PROOF.md:6`, `~/BSD_CODEX6_MASTER_HANDOFF_2026-09-19/_work/d23_twist_2026-09-21/RESULT.md:6`, `~/BSD_CODEX6_MASTER_HANDOFF_2026-09-19/_work/d23_twist_2026-09-21/RESULT.md:22` [unit E4c-081]
