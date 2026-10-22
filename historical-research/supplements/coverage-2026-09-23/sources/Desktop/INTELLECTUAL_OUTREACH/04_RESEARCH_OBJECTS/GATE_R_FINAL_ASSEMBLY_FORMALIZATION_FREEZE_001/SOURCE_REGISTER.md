# Source register

| Slot | Content |
|---|---|
| `00_handoff/` | `ARISTOTLE_GATE_R_FINAL_ASSEMBLY_V1` exactly as released. Archive `9f15927e08f65db8ea3c7d2d570112f49363189ddd651822fe4c8166cd765811`. |
| `01_run_A/tree/` | Run A working tree as delivered. Run UUID `1b7c66a4-d0b6-492e-9c44-1eccf828fe18`. Wrapper `44203bac-5c1e-4b57-94a0-53be437808b7-aristotle.tar.gz`, sha256 `89c70e42f00d66db87cfb2fcdaf13778092558274f00cd3042b58c1ea23233ec`. |
| `01_run_A/preserved_input/` | The untouched input skeleton the wrapper also carried — **five `sorry`s, not the return.** Do not audit it. |
| `01_run_A/preserved_input_archive/` | The input archive the wrapper carried; digest equals the released packet. |
| `02_run_B/tree/` | Run B working tree as delivered. Run UUID `294dcf54-c2b6-46c0-9cd5-6a2ea0a45e61`. Wrapper `06f5c7c7-efbf-4079-9555-bb56516c53b8-aristotle.tar.gz`, sha256 `d3636dc6584b8d3050dccadeb80ff18aff2f09e83e4099f23c716566cdaf3523`. |
| `receipts/` | Claude's external verification. Every figure regenerated, none taken from a return. |

Upstream: `CODEX_GATE_R_BLIND_AUDIT_FREEZE_001` (`91d30642…`) — the three-review reconciliation
that produced this specification. `GATE_R_HEIGHT_PILOT_FORMALIZATION_FREEZE_001` (`810899ee…`) —
the certified R1 and R0 this assembly consumes. `GATE_R_FINAL_ASSEMBLY_PRESHIP_RECORD_001`
(`5190b65f…`) — the pre-release reachability record.

Wrapper-layout warning, for whoever audits next: each wrapper contains **two** trees. The
return is at the wrapper root; a byte-identical copy of the input, still carrying the five
shipped `sorry`s, sits in a nested directory. Auditing the nested copy would report a failure
that is not there. Both are preserved here, separated and labelled.
