# Replay and custody

Run from this directory:

    python3 verify_packet.py

This checks every root/nested MANIFEST.sha256 and the cross-certificate dimensions. It also verifies that the independent review binds the exact current separation-proof bytes. It is not a proof of the retained inputs.

Arithmetic replay commands (run inside each named directory):

| Directory | Command | What is regenerated |
|---|---|---|
|norm_controls|python3 run_replay.py --gp /path/to/gp|All scalar norms and complete kernels for1913/389 in a temporary directory; independent determinants and finite enumeration.|
|norm433|PARI_GP=/path/to/gp python3 replay.py|433 whole norm map, roots, noncube rank, local/Hensel certificate in a temporary directory.|
|norm_mirror|PARI_GP=/path/to/gp python3 replay.py|Mirror whole norm map, roots, noncube rank, local/Hensel certificate in a temporary directory.|
|joint_kernel|python3 replay.py|Source-wide kernel reconstruction, withheld comparison,624 literal433 evaluations.|
|class_comparison|See RESUME.md|Class image modulo the actual point image; exact lower control.|
|review|python3 check_homogeneous_modules.py|Finite geometric modules at five odd primes and exact formal Cardano identities.|

PARI used here: /Users/bsm/run040-order7-cayley-coordinate-slice-genus-census-2026-09-03/tools/sage-env/bin/gp (resolves to gp-2.17). Python3 standard library suffices for the finite arithmetic checks; the final symbolic checker additionally uses SymPy1.14.0.

The subpacket replays fail on GP stderr or missing completion markers, not only nonzero exit codes. Original rejected implementation attempts remain explicitly marked. No replay starts a new BNF certification or a remote computation.

The norm_controls runner was hardened after the root replay: by default it prints the result without rewriting the sealed receipt; --receipt PATH explicitly requests a new log. The earlier manifest and old runner are preserved under review. All accepted arithmetic products remained byte-identical.

Source binding identifies the exact cached inputs. Complete-source grades for the four controls remain retained inputs. The seed's conditional source and28042's incomplete source remain so. Root/nested manifests certify custody, not mathematical correctness.
