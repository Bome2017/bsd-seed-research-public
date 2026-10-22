# Replay and custody

## Small final verification

From this folder run:

```sh
python3 verify_return.py
```

It checks all six nested lane manifests, reproduces the exact twist-model/point and 655 primitive-divisor checks in a temporary folder, recomputes the twist prime-permutation consequence, checks both large compressed captures against their raw and gzip hashes, and verifies the final status fields. Its output is saved as VERIFICATION.json. It does not modify the packet.

The 267 nested manifest entries are custody checks, not 267 independent mathematical tests. The small arithmetic replays do not regenerate the rank descent, maximal orders, degree-48 source factorizations or historical theorem inputs. Hashing the source captures does not replay the 1,424-element field calculation. The original producer scripts, full outputs and resource receipts remain included.

## Full packet manifest

The root MANIFEST.sha256 covers all other packet files, including the nested manifests and the saved verification. Check each SHA-256 against the named relative file. It does not hash itself. Files with historical errors and incomplete attempts are deliberately retained and are identified in their lane reports; their presence in the manifest does not admit their mathematical conclusions.

## Source computation boundary

The rank-two source searches are stopped. Archived launch scripts are reproducibility evidence, not instructions to start new jobs. Do not rerun BNF from a process exit code: every successful arithmetic output requires its saved completion marker and output artifact. No such complete BNF/class certificate exists here.

For the isolated PARI collector, read pari_partial_source/REPLAY.md and both root instrumentation reviews before any intentional rerun. Its official source archive and source patches are included. Builds were made outside this folder. The installed GP was never replaced. Captured generators are candidates; acceptance as units requires independent exact ideal/divisor authentication. A failed internal filter is not a proof of nonsmoothness.

Some arithmetic scripts retain absolute producer paths in the bound project roots. Their binding files identify those inputs; a full relocated replay must explicitly rebind the same files. The small root verifier is relocation-safe. No claim is made that an arbitrary host can execute every historical script unmodified.

## Interpretation

The complete norm/local ranks on the rank-two sources remain unmeasured. Only the complete valuation allowance is newly zero in both controls. No complete ordinary class upper bound, original-seed prime result, FIN, ORDER9 or Q36 result follows.
