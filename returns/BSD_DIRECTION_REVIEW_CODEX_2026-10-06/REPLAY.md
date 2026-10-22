# Scope and replay

The review ZIP contains selected, unmodified evidence and full archive-member hash inventories. It deliberately does not duplicate the 66 MB reading-set payload. The original two Aristotle archives are preserved separately in the lab archives directory.

Run the bounded arithmetic checks from a scratch copy:

    python3 checks/review_checks.py --arithmetic-only --output /tmp/bsd-direction-replay.json

This recounts the 30 listed auxiliaries, checks factorizations/inertness, four ordinary-prime spot counts, the group-ring identity controls, and the small dimension/index controls. It does not test completeness of the prime list or compute derived points.

For the original archive-manifest audit, reconstruct the two complete archive trees at input/heegner and input/coinvariant (strip the single outer directory; reject links and unsafe paths), then run the same checker without --arithmetic-only. The sealed checks/REVIEW_RESULTS.json records the results on the complete extracted inputs in this review. Source files are not modified by the checker.

The current Heegner return manifest uses paths relative to its project root, not relative to research_return/. Historical task manifests are not new-return seals. The inherited coinvariant root manifest predates the continuation, as explained in REPORT.md.

No Lean build is asserted by this review. The original Lean files and build claims remain in the original archives; verifying arithmetic here is not a replay of those builds.
