# Replay and evidence limits

Run `python3 pilot.py` in this directory. It checks INPUT_BINDINGS.json against the copied inputs, reconstructs the full necessary kernels, enumerates all 3^9 source vectors for 1913b1, and computes the common-point quotient on four saved panels. RESULTS.json and pilot.out are deterministic. Run `python3 independent_common_point.py` for exhaustive point-coordinate search for the three seed blocks, without importing pilot.py.

These are saved-data checks. No number field, modular symbol, rank descent or class group was recomputed. The source completeness certificates, full point lattices, exact class memberships and local evaluation tables are retained inputs. Hashes identify inputs, not their truth. The 433a1 local-image interface remains at its original grade. The 28042a1 source certification timeout and the seed source's conditional grade are preserved.

The first execution of pilot.py had an unmatched closing parenthesis in the old-detector line; Python rejected it before any computation. That syntax error was fixed before the accepted run and did not alter inputs, contracts or experiment selection. The independent checker initially asserted the stronger desired pair rank two and failed; the accepted checker retains the actual rank-one kernel and checks its disappearance at the third place. The rejected script is preserved. A shell git-status request was inadvertently run from the nonrepository pilot folder and returned not-a-git-repository; no repository mutation occurred in that call.

No new primary seed conclusion or global endpoint is claimed.
