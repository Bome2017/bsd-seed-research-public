# Reading and replay

Start with REPORT.md, then PROOF.md and FINAL_JOINT_REVIEW.md. STATE.json records the completed result and its open class contribution. VERIFICATION.json distinguishes completed checks from the failed class certificate.

The following lightweight arithmetic replays use only Python standard libraries and the saved data inside this packet:

```sh
python3 check_11a1_joint.py
PYTHONDONTWRITEBYTECODE=1 python3 local_rank/replay_arithmetic.py
```

The first reconstructs actual multiplicative unit residues, elliptic group laws, scalar action and affine norm rows at three split primes, then combines them with the saved authenticated local quotient. It writes INDEPENDENT_11A1_JOINT.json deterministically. The second independently rechecks the saved local-product cancellation, projection, ranks and a different nonzero minor. These replays do not regenerate the exact maximal order or rerun PARI idealstar.

The exact PARI producers, their stdout/stderr and bounded runtime receipts are retained in the arithmetic subfolders. Some original producer scripts use bound absolute paths on the originating host. For a new host, rebase those paths deliberately while preserving the mathematical data and script binding; do not treat an unmodified exit code as a replay certificate. The complete compact unit authentication and actual primitive divisor replay are in small_conductor_review/ and small_conductor_divisor/. The BNF cache is an optional retained computational artifact, not evidence of class completeness.

MANIFEST.sha256 covers all regular delivered files except itself. The five lane manifests bind their original sealed subsets. An archive hash or matching manifest establishes identity, not a mathematical theorem.
