# Sources, identity and reading boundary

## Current local/repository record

* Lab: Bome2017/bsd-seed-lab, branch research/state-sync-2026-10-04,
  refreshed through 00f6d152. The earlier local review and the concurrent
  updates are both preserved in the integrated history. Exact heads are in
  checks/GITHUB_STATE.json.
* Research: Bome2017/bsd-seed-research; status branch 9ebaca3b80adfd4a18e77eebe23c9db3bc201448;
  release v0.2.6 8414aea58180f3a18bcee7fba23475c8cac90996. Fetch/read only.
* Read: current frontier; current return ledger; the later W3/Heegner
  reports and corrections; rank-two-anchor and derived-Gross results;
  1-motive main results in both supplied archives and their newer Claude
  check; OpenAI task and the user's pasted universal-map refinement.
* Context files retain original wording/grades, including statements
  corrected in REPORT.md. They are sources, not new instructions.
* Downloads inventory is scoped to 67 selected Aristotle/BSD archives,
  not every file in Downloads. Exact report-content matching is custody,
  not proof checking. No claim that all historical returns have been read
  line by line is made.

## OpenAI source, pinned and not promoted wholesale

Commit: adc7f1241b42e322a6451854ab7e4b4c146bf78a of openai/math.

https://github.com/openai/math/tree/adc7f1241b42e322a6451854ab7e4b4c146bf78a

Downloaded exact source files in sources/:

* `04-vertical.tex`: the local tests, first-order lift formula and
  obstruction-span proof. In particular the printed argument is over
  generic residual parameter fields and uses paired strict/opposite spaces.
* `ring-determinants.tex`: `rd:det-switch` and the surrounding rank-two
  evaluation statements. The switch assumes generic rank one.
* `01-introduction.tex`, `05-single.tex`: setup and low-corank scope.

These are unformalized manuscripts. The repository's release does not turn
their claims into reviewed theorems. Their commutator method motivated our
direct residual-field construction; its arithmetic proof is written out
separately in STAGE_A_DERIVATION.md. The original Apache-2.0 license is
preserved in sources/OPENAI_LICENSE. Exact source bytes are in the manifest.

## Pairing source actually read

Adam Morgan and Alexander Smith, *The Cassels--Tate pairing for finite Galois
modules*, https://arxiv.org/abs/2103.08530
Full text: https://arxiv.org/pdf/2103.08530

Read the definition of exact sequences of Selmerable modules (Definition
1.1 and the subsequent exactness conditions), Theorem 1.3 and Example 1.4,
cochain conventions and Definition 3.2, the left-kernel proof, the duality
statement, and Proposition 4.4 on Baer sums. These supply the canonical
pairing, exact lift-kernel interpretation, and linearity used here. The
source does not itself state our seed's universal-kernel conclusion.

Standard arithmetic background used explicitly: local Tate duality and
Kummer self-annihilation; local Euler characteristic away from p;
Brauer--Hasse--Noether; Chebotarev; cyclotomic degree-p characters. None
is cited as a uniform Sha upper bound. The new argument must still be
independently checked with its local conditions.

## Checks run here

`checks/check_obstruction_algebra.py` and its JSON output: finite algebra
only. `checks/INPUT_MANIFESTS.json`: inherited 1-motive input manifests.
`checks/GITHUB_STATE.json`: repository and inventory snapshot.
No current seed primary computation or fresh Lean proof certification.
