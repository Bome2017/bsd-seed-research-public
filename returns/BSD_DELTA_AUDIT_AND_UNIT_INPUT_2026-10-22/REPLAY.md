# Replay

Python 3 and PARI/GP (producer: PARI 2.17.3) are required. From this folder:

```sh
python3 verify_packet.py --gp /absolute/path/to/gp
```

The verifier checks the root and nested manifests, copies the packet to a temporary directory, runs the two supplied checkers twice, compares their exact saved outputs and prior comparison records, then reruns the 2,232-candidate seed norm test. The GP stack is capped at 512,000,000 bytes, with a 110-second internal alarm and 120-second external timeout. No BNF or L-value computation is invoked. Outputs containing timing data are generated only in the temporary copy; the sealed inputs are not rewritten.

Without `--gp`, the verifier checks custody and the supplied Python audit only, explicitly recording that the GP replay was skipped. `VERIFICATION.json` records the completed replay with GP. Hash identity is separate from mathematical validity. The maximal order, field construction, scalar action, source injection and earlier BSD inputs retain their prior grades.
