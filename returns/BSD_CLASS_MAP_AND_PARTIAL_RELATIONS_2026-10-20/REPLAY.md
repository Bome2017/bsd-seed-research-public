# Replay and scope

Use a copy of this packet: replay scripts write fresh output and can invalidate
the sealed manifest. Python 3 and PARI/GP 2.17.3 were used. No paid service,
network connection, or new elliptic database search is needed for the saved
certificate checks.

Run the independent inexpensive checks:

```sh
python3 review/run_review.py --gp /absolute/path/to/gp
```

Expected marker: `PORTABLE_INDEPENDENT_REVIEW_PASSED`. The runner requires
exit code zero, empty GP stderr, and the individual success markers. It checks
actual ideals, scalar actions, class and connecting identities, the full unit
matrix, and the faithful valuation allowance. It does not repeat BNF
certification or the original elliptic rank computation.

To reproduce the partial-relation producer's selected elements and witnesses
from bundled inputs in a fresh directory:

```sh
python3 partial_relations/portable_replay.py \
  --gp /absolute/path/to/gp \
  --output /absolute/path/to/a/new/replay-directory
```

`PORTABLE_REPLAY.json` records the root's successful clean replay and exact
byte comparisons. This reconstructs the selected eighty elements, not the
entire original weighted search.

The class lane's `replay.py` repeats authentication in clean temporary
directories and invokes target BNF certification. Set `PARI_GP` to the GP path.
Its saved `REPLAY.json` records two successful identical certificate outputs
per selected control. BNF binary inputs may require a compatible PARI version;
incompatibility is a failed replay, not a reason to waive checks.

`MANIFEST.sha256` binds the returned files. A matching hash establishes custody,
not truth of the mathematical statements. Rejected attempts remain preserved
and are not counted among successful checks.
