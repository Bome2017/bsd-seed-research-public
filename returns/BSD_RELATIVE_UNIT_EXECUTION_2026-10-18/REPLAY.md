# Replay and source scope

Run `python3 verify.py` from any directory. It performs read-only input hashes, nested manifest checks, norm-log/accounting checks and final outcome consistency. It prints JSON; it does not start field searches, re-run BNF, write state files, or evaluate a seed coefficient. After sealing, the root manifest can be checked with the same script.

The full source execution and repair history is in `source/`. The main numerical producer is resource-bounded: its exact completion count may depend on host speed. Repeating the search is not required for verification of the saved finite-family result. Cached embeddings are heuristic candidate-selection data; exact ideal arithmetic determines admission.

`review/` is the separately sealed initial review and contains its preserved diagnostic failures. `FINAL_SCOPE_REVIEW.md` and `FINAL_SCOPE_CHECK.*` add later adaptation checks without rewriting that sealed review. The final review states which exact computations it repeated. The full norm-log checks compare producer outputs to ideal norms; they do not independently reconstruct all14,326 original candidates.

The baseline arithmetic and dimension theorem remain retained inputs at lab commit89b0566ef61ba78d9d95853508f831ee3ee03440. Six portable arithmetic files are bound in INPUT_BINDINGS.json. The four evaluator code files retain their existing implementation and source grade.

No new unit reached the evaluator. Thus there is no missing numerical rank file that should be inferred as zero. The ordinary class group is not certified or bounded by this return. FIN, ORDER9 and Q36 remain open.
