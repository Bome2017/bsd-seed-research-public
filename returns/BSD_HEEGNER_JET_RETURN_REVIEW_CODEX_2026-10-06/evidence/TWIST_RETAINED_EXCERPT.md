# Retained twist input

Source: supplied heegner/FULL_COMPENDIUM.md, lines 331-352. The full source is bound in INPUT_BINDINGS.json and in the original archive.

##### D=-23 twist: certified L-prime interval 39.512236 <= L'(E^{-23},1) <= 40.182321; analytic rank one

**Statement.** The isolated table-free computation (_work/d23_twist_2026-09-21/RESULT.md, PROOF.md) proves 39.512236 <= L'(E^{-23},1) <= 40.182321. The root number of the twist is -1, so the twist has analytic rank exactly one. With the retained Gross-Zagier-Kolyvagin rank-one theorem and the seed rank theorem: rank E^{-23}(Q)=1 and rank E(Q(sqrt(-23)))=3. This supplies the suitable certified rank-one twist premise of the Fitting-ideal shift; no Stark ideal is evaluated; no new seed primary component, FIN, ORDER9 or Q36 follows. Finiteness of Sha of the twist does not imply finiteness for the seed or for E/K.

**Status.** PROVED_COMPUTER_ASSISTED (record: "TWIST_D23_NONZERO_CERTIFIED"). **Reviewed by:** completion review (same-family session); Arb enclosure [tier: SAME_FAMILY_MODEL, EXACT]. **Date:** 2026-09-21.

**Depends on:** seed RANK theorem; Gross-Zagier-Kolyvagin rank-one theorem; C11 coefficient corpus. **Connects to:** Fitting shift by three; MCS join; p=13 splitting conditions.

> "39.512236\le L'(E^{-23},1)\le40.182321." (`~/BSD_CODEX6_MASTER_HANDOFF_2026-09-19/MASTER_BSD_DAG.md:689`)

**Evidence:** `~/BSD_CODEX6_MASTER_HANDOFF_2026-09-19/00_READ_FIRST.md:12`, `~/BSD_CODEX6_MASTER_HANDOFF_2026-09-19/RESUME.md:16-18`, `~/BSD_CODEX6_MASTER_HANDOFF_2026-09-19/MASTER_BSD_DAG.md:687-693` [unit E4a-005]

##### Consequence of D=-23 certificate: ord L(E^{-23},s) = 1, rank E^{-23}(Q) = 1, Sha(E^{-23}/Q) finite, rank E(Q(sqrt -23)) = 3

**Statement.** From the certified interval and odd root number: ord_{s=1} L(E^{-23},s) = 1; by Gross-Zagier-Kolyvagin (retained theorem, applied) rank E^{-23}(Q) = 1, Sha(E^{-23}/Q) finite, rank E(Q(sqrt -23)) = 3; ord L(E/K,s) = 3 over K = Q(sqrt -23) so y_K is torsion and the Heegner index [E(K):Z y_K] is infinite. All five bad primes split in Q(sqrt -23) (indefinite / Heegner case). Gives no new Sha vanishing by itself.

**Status.** PROVED_COMPUTER_ASSISTED (record: "rank E(Q(sqrt -23)) = 3"). **Reviewed by:** author; retained GZK import [tier: EXACT]. **Date:** 2026-09-21.

**Depends on:** D=-23 certificate; Gross-Zagier; Kolyvagin.

> "Gross-Zagier-Kolyvagin `rank E^{-23}(Q)=1`, `Sha(E^{-23}/Q)` finite, and `rank E(Q(sqrt -23)) = 3`." (`~/BSD_ARISTOTLE_TAIL_COMPRESSION_2026-09-22/unpacked/INPUTS.md:12`)

