# BSD seed — full-record Aristotle/Harmonic handoff

**Purpose: make new mathematics toward this fixed rank-two curve's BSD theorem.**
This is a research handoff with original evidence, not a claim that BSD is proved.
The current gaps are uniform prime support, the remaining primary obligations,
conditional exact order, and the arithmetic leading-term comparison.

Start with [the research prompt](ARISTOTLE_PROMPT.md) and the
[single reading document](BSD_SEED_RESEARCH_MAP.md). The latter gives the exact
curve and endpoint, a 44-card obstruction/correction atlas, concrete research
interfaces and the formal-proof return contract. A missing theorem is a task to
attempt, not an instruction to stop. The recipient may change methods.

## The complete record behind the map

- [Full 7,042-unit compendium](sources/FULL_COMPENDIUM_2026-10-01.md), with
  [structured units](sources/KNOWLEDGE_UNITS.json).
- [Current source index](sources/GOVERNING_SOURCE_INDEX.md) and
  [5,043 directly readable dossier files](sources/WORKING_SET_INDEX.md).
- [3,353 full historical stop/correction entries](sources/HISTORICAL_STOPS_AND_CORRECTIONS.md).
- [All 89 release claims and their qualifications](sources/RELEASE_CLAIMS_FULL.md).
- [Full dossier index](sources/DOSSIER_INDEX.md) and
  [visible research conversation](sources/CONVERSATION_RECORD.md).
- `evidence/`: 84 lossless volumes containing 283,307 distinct source/evidence
  objects, with every original path retained in the catalog.
- [Preserved Git histories](history/README.md), including the research release.
- [Exact coverage and exclusions](coverage/COVERAGE.md). Large raw binary
  computation stores remain external with freshly checked digests; their bytes
  are not represented as embedded.

## Use it with Aristotle

Provide the unpacked project through the Aristotle interface available to you and
use `ARISTOTLE_PROMPT.md` as the task. No API key or job is embedded. The full local
ZIP contains the entire portable package; its size reflects the user's request
to preserve the evidence, not just a short prompt. A separate starter ZIP, if
provided alongside it, contains the readable map/current dossiers but is not the
whole evidence archive. Do not silently substitute that smaller upload for the
complete record when the task needs a source outside it.

If an interface cannot ingest the whole project at once, start with the map,
compendium and current working dossiers, then use the catalog to retrieve the
exact needed original sources. Private GitHub links do not automatically confer
access. No particular platform attachment limit or runtime is assumed.

## Retrieve any original file

Python 3 with its standard library is sufficient. No research code is executed.
The first invocation expands the 487 MB search catalog into a temporary cache.

```sh
python3 record.py info
python3 record.py find 'W3_FOUR_VALUE'
python3 record.py search 'mixed augmentation'
python3 record.py unit A1-001
python3 record.py show '/Users/bsm/BSD_W3_DISCOVERY_ADMISSION_CODEX_2026-10-05/REPORT.md'
python3 record.py restore '/Users/bsm/BSD_W3_FOUR_VALUE_RETURN_CODEX_2026-10-04' --to ./restored-w3
python3 record.py verify
```

`extract PATH --output FILE` restores an individual binary or text source.
`verify --deep` reconstructs and hashes every evidence object. `history` assembles
a selected Git bundle. For external raw corpus files, restoration is possible
only from a matching local file and requires the explicit bulk option.

All original paths are identity keys. They do not require the recipient to use
macOS or own the original computer. The catalog maps them to the included volumes.
The package has no installation script, background job, paid computation or
external submission side effect.

## Mathematical status

FIN, ORDER9 and Q36 remain open. This package preserves the released facts and
later derivations at their existing grades. It does not turn old model claims,
hash checks, synthetic controls or abstract Lean bridges into new arithmetic
theorems. The goal of the next run is a new arithmetic theorem or construction
with its actual implication to one of these endpoints.

A [concurrent Aristotle draft](sources/concurrent_aristotle_draft/CAPTURE_READ_FIRST.md) is also preserved with its later atlas and Lean templates, explicitly marked as a snapshot requiring review.
