# Sources and coverage

## Pinned repository scope

- Lab: `Bome2017/bsd-seed-lab`, branch `research/state-sync-2026-10-04`, base `f74e44203478aa09556b65692a02347e0c7cf4c4`.
- Fetch and remote-reference census found no later remote update at the start of this audit. This statement is a dated snapshot.
- Ten recent return folders are enumerated in STATE.json and CUSTODY_CHECK.json. All ten reports/status files were read; their governing mathematical files are discussed in MATHEMATICAL_CHECK.md. This does not claim to reread all historical nested archives.
- Root README, work README, LATEST_RETURN, and the complete returns index were checked for local-link existence. The pre-edit count is 503; no missing local target was found.
- The research repository was queried read-only for refs. Its retained `v0.2.6` branch remains `8414aea58180f3a18bcee7fba23475c8cac90996`. No research-repository content was changed or promoted.

## Primary sources checked in this audit

1. [Howard, Bipartite Euler systems](https://arxiv.org/pdf/1202.6353): definition of index in §2, Theorem 2.5.1, and the introduction's distinction between an assumed full Euler system and the BD construction along selected paths. Fresh primary PDF text read. No claim that the supplied single-pair construction satisfies all these axioms.
2. [Milne, Arithmetic Duality](https://www.jmilne.org/math/xnotes/Tate100.pdf): finite-S global duality on printed p.5, freshly read in primary PDF text. The specific local index and limit argument are deductions in the retained proof, not quoted source theorems.
3. [Burns–Kurihara–Sano, On derivatives of Kato's Euler system](https://www.jstage.jst.go.jp/article/jmath/76/3/76_855/_pdf/-char/en): Theorem 6.2 and the Coleman/smoothing formula, freshly checked in primary PDF text. Its finiteness hypothesis is handled only through the retained case split, not omitted.
4. [Kato, Astérisque 295](https://www.numdam.org/item/AST_2004__295__117_0/): the PDF fetch failed in this audit. Re-read preserved text of 12.6, 13.4 and 13.14; existing PDF/text hashes were independently matched through INPUT_BINDINGS. No fresh visual inspection or end-to-end transport certification is claimed.
5. [Bertolini–Darmon, Iwasawa's main conjecture](https://www.math.mcgill.ca/darmon/pub/Articles/Research/27.Main-conjecture/pub27.pdf): the Proposition 9.2 label was checked in the preserved preprint text at `/Users/bsm/BSD_YUN_ZHANG_MECHANISM_READING_2026-10-07/sources/BD2005.txt`. The source already retained in the BD review distinguishes its own p-level hypotheses from the unconstructed bottom-layer extension. No new source-hypothesis theorem is asserted.

## Audit-method qualifications

Custody uses manifest hashing, ZIP CRC, byte equality between each archive and its tree, and the separately recorded archive digest. Source bindings check both copied and available original paths; they do not establish theorem correctness. The first verifier pass needed adaptation to four older custody JSON field names; after accepting their recorded schemas, all ten bindings match. This was a checker-schema correction, not corrupted repository evidence.

The replay list records every executed script and exact output digest. No unsupplied arithmetic was reconstructed, no remote job was launched, and no archived task was restarted.
