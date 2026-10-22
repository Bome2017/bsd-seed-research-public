# Source register

Every digest below was **recomputed for this object**, not copied from a prior register. The
machine-generated register is `receipts/FREEZE_DIGEST_REGISTER.txt`.

## Mandatory bindings

| Object | Archive SHA-256 | Entries |
|---|---|---|
| `P04C_TWO_DESCENT_QUOTIENT_FORMALIZATION_FREEZE_001` | `6b93c2278b5afa174808b42ee9427a20a102f0420a991701ca2cfeefe13061bb` | 184 |
| `GATE_R_HEIGHT_PILOT_FORMALIZATION_FREEZE_001` | `810899ee5ee3ed04ef0d1f0316a8c830138e1462ba39b48cb1a4abf2f22a2de3` | 250 |
| `GATE_R_FINAL_ASSEMBLY_FORMALIZATION_FREEZE_001` | `5cf07602bf944129d74600bffefcdcdf6cf84150829161976ae27ee93cc736fd` | 223 |

The first matches the digest the operator supplied. The second matches its own freeze register.
The third was recomputed and its 223 members were fully replayed with zero mismatches.

## The rest of the certified chain

| Object | Archive SHA-256 | Entries |
|---|---|---|
| `F_FORMALIZATION_FREEZE_001` (.zip) | `8f59a4589c74d67cfc0b96c1c2e8e573c7f78e946273135a7669f4539733dc7e` | 89 |
| `S_DYADIC_FORMALIZATION_FREEZE_002` (.zip) | `d4b066aa7051dea698f6617003ac4189dbfb1a40a5f7e3f6636d2d92ff1a25b6` | 154 |
| `S_DYADIC_SATURATION_FORMALIZATION_FREEZE_002` (.zip) | `4013c2f312d6a15771e74c424512aa0ca530818f892d5eabda368825a595ea5d` | 107 |
| `P01_FAMILY_TWO_TORSION_FORMALIZATION_FREEZE_001` | `ab771cda4d92fe28b8b418156d6307b3a90ab49c46e895ad7d7002259d41475a` | 103 |
| `P03A_ACTUAL_ISOGENY_POINT_MAPS_FORMALIZATION_FREEZE_001` | `bc2366f7d3686e9fe621206ccb8fac91be6bc7612dff16b8b5b230d4360dcb53` | 99 |
| `P03B_ISOGENY_ADDITIVITY_FORMALIZATION_FREEZE_001` | `c1c8eb5f0d7ba3b2f4887d4f291036057db4dad9de77967166fc85c5efee2d4b` | 107 |
| `P03C_ISOGENY_KERNELS_FORMALIZATION_FREEZE_001` | `188105747df815cdde1d4d723ead969c2e116c54fab609f00a2dda15b74f04cf` | 108 |
| `P03D_ISOGENY_COMPOSITES_FORMALIZATION_FREEZE_001` | `4c3f0339b4b3f7104941b07d639aaaff50d0e6dc4bb1b20b66d60eeddcf1df8f` | 115 |
| `P03E_DESCENT_KERNEL_IS_ISOGENY_IMAGE_FORMALIZATION_FREEZE_001` | `a600565129efb76f38390b00ee10139add56fa536e1ab79c1a02a60041a243fb` | 104 |
| `P04A_ISOGENY_COKERNELS_FORMALIZATION_FREEZE_001` | `cffc277d189422f611f2296785b997a1ad11672f443720290510c4ecb4affbb2` | 128 |
| `P04B_SATURATION_RECONNECT_FORMALIZATION_FREEZE_001` | `92ed308c066d56bed45baa177bd03fb7e3b64175a856cc042db7c2793b8947fe` | 170 |

`F`, `S_DYADIC` and `S_DYADIC_SATURATION` were sealed in an earlier era of the programme as
`.zip`, not `.tar.gz`. Their digests are bound in the form in which they were actually sealed;
no archive was rebuilt for this register.

## Review and provenance objects

| Object | Archive SHA-256 | Entries |
|---|---|---|
| `CODEX_GATE_R_BLIND_AUDIT_FREEZE_001` | `91d30642ca85ab2ed1b3318ebc729f5958d671da6ea23ac101590d1dd7dd64cb` | 108 |
| `ARISTOTLE_GATE_R_FINAL_ASSEMBLY_V1` (the handoff) | `9f15927e08f65db8ea3c7d2d570112f49363189ddd651822fe4c8166cd765811` | 46 |
| `GATE_R_FINAL_ASSEMBLY_PRESHIP_RECORD_001` | `5190b65f8b6c197c3c0a5a3101cef27d071ec3e0a61b39b85de9cd5a7f858b1c` | 6 |

## Predecessor status object — PRESERVED, NOT SUPERSEDED IN PLACE

| Object | Archive SHA-256 | Entries |
|---|---|---|
| `THEOREM_STATUS_H1_FREE_BRIDGE_COMPLETE_001` | `e823ed125663279cc9a0d6ee96fd54401d0c65d7411c21426fc9de2cb10f3462` | 6 |

Frozen, unmodified, and retained as the historical status at the P04c boundary. Its corrections
are recorded in this object's `CORRECTIONS_TO_ROADMAP_PROSE.md`, never applied to it.

## Theorem-status source references

Every certified statement quoted in this object is cut verbatim from frozen source into
`receipts/CERTIFIED_STATEMENTS_VERBATIM.txt`, with file and line:

    SDyadic/Family.lean:70        Params
    SDyadic/Saturation.lean:29    H41
    P04c/TwoDescent.lean:352      two_descent_quotient
    R1/Height.lean:111            h41_multiplicative_duplication_height
    R0/Torsion.lean:37            properHeightTwoDescentTorsion
    GateR/Assembly.lean           translateMax, every_point_torsion, h41_rank_zero

The frozen tree used for those cuts is
`GATE_R_FINAL_ASSEMBLY_FORMALIZATION_FREEZE_001/00_handoff/RequestProject/` for the base and
`…/01_run_A/tree/RequestProject/GateR/Assembly.lean` for the returned outputs.

## Environment pin

    Lean     leanprover/lean4:v4.28.0
    mathlib  8f9d9cff6bd728b17a24e163c9402775d9e6a365

Unchanged across the entire programme.
