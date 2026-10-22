# Resume: local-signature lane

State: complete, pending parent package integration. Do not resume another prime scan by default.

Start with REPORT.md, then PROOF.md and JOINT_EVALUATION_DENSITY.md. Actual arithmetic in RESULTS.json; every block and annihilator in each case/SIGNATURES.json. Literal independent-of-source-exponent arithmetic in LITERAL_REPLAY.json. False candidate's decisive actual norm residue in mirror389_false/GLOBAL_NORM_REJECTION.json.

The result is the two-stage classifier (authenticate global/all-place membership, then quotient-local comparison with all rational points) and the exact fixed-coefficient-prime density explanation. It distinguishes the named three categories, including the actual seed's two known 3-primary directions. It supplies no ambient completeness or uniform upper bound and changes no seed endpoint.

Replay saved arithmetic without changing originals:

    python3 replay.py

The isolated replay recomputes 120 local blocks, representative changes and sealed matrix enumeration. It does not replay global norm membership or rank/descent prerequisites. The density prediction file in the sibling incidence_review directory is required and hash-bound.

For a fresh GP scan, use a disposable COPY of this whole directory and the retained source inputs. In each case remove coordinates.json, bad_local.gpdata and scan.gpdata from that disposable copy first: GP write() appends. Then run from the copy's parent:

    python3 run_stage.py /absolute/path/to/copied/case scan LOCAL_SIGNATURE_SCAN_COMPLETE

The retained runner uses the known local GP binary and stdin, not argv source execution; the GP script itself has a 90-second alarm, and the wrapper has a 130-second outer cap. No BNF construction or certification occurs. For a literal export, remove actual_polynomials.json in that disposable copy and invoke stage export_actual with marker ACTUAL_POLYNOMIALS_EXPORTED. Never overwrite retained originals.

All source copies are bound in SOURCE.json. Earlier false field-variable exports are preserved under failed_field_variable_export/. The other discovered normalization issue was literal seed P2 at q2767/root7: valuation 3, leading unit 916; correct replay uses Hensel leading units. Do not revert to direct reduction or discard that prime.

Independent peer scope review: ../secondary/PEER_SCOPE_REVIEW.md. Parent literal replay: ../independent_review/LOCAL_REPLAY.json. Those checks have different scopes; neither silently recertifies every prior input.
