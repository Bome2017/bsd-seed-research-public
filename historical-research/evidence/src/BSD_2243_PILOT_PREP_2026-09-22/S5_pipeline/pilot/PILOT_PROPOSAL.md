# Proposed cloud pilot for 2243: a capped benchmark, not the certificate

Status: **proposal only**. Nothing has been launched and nothing has been spent. Running it needs your explicit authorization, and your cloud account: I hold no credentials.

## 1. Purpose

Replace the one unmeasured factor in the all-in projection with a measurement: the cloud core's speed on this exact pipeline, f. The pilot also re-validates the complete path on the rented machine before any large purchase:
* bit-identical results to the local reference;
* streaming produce → verify → accumulate;
* crash / restart / recombination.

It returns **$ per fully verified, accumulated chunk**, measured directly, and a re-run of the S4 cost model with cloud rates.

It is **not a certificate run.** It accumulates unit subsets only. The engine refuses to print a coefficient or unit test from a subset unless the output is labelled timing-only.

## 2. Machine and hard limits

| item | proposal |
|---|---|
| instance | **AWS c7a.16xlarge**: 64 vCPU, each a physical AMD EPYC 9R14 (Genoa) core (no SMT); 128 GiB; Ubuntu 24.04 amd64 |
| market | spot, with MaxPrice set to the on-demand price ($3.2845/h, us-east-1). About $1.20/h at the time of writing (vantage.sh, 2026-09-23) |
| count | **one instance at a time**, one invocation of `launch_aws.sh` per instance |
| wall limit | `shutdown -h +300` (5 h) from user-data **before anything else runs**; shutdown behavior = terminate; the root volume is deleted on termination |
| disk | 100 GB gp3 |
| data out | the results tarball, a few MB |
| **hard cap** | **$100 total**, enforced by construction. `launch_aws.sh` keeps a ledger of each launched instance's worst case (on-demand price × wall limit + disk) and refuses any launch that would push the ledger past $100 |
| second guard | an AWS Budgets cost budget of $100 with alerts at 50/80/100%, set by you in the console. Budget data lags by hours, so it is a backstop, not the cap |

**Worst case per instance** is $16.48 (5 h × $3.2845 + disk). The planned programme below has a worst case of **≤ $50**.

## 3. What runs (`pilot_run.sh`; bootstrap takes about 15 min)

| stage | what | pass criteria | expected time on 64 cores |
|---|---|---|---|
| P0 bootstrap | Builds FLINT 3.3.1 (upstream release, sha256 recorded), PARI 2.17.4 (bundled tarball, identical to local), the producer, the verifier and the accumulator. Sources are unchanged; the portable SHA-256 shim was validated against Apple CommonCrypto | builds; hashes recorded | ~15 min |
| P1 correctness replay | (a) v2 merge of the S2 checkpoints. (b) Full m = 27 run from scratch: all 288 a_q segments streamed. (c) Full m = 81 run: 885 segments | (a) identical to S2, and DFT = direct. (b, c) symbols identical to the certified ones; **a_{4,2} = 15480**; class-sum digests **bit-identical to the local runs**; every streamed a_q hash equal to the certified hash | ~20 min |
| P2 component rates | Producer and verifier at 4 heights (q ≈ 10⁹, 10¹¹, 10¹³, 3.912·10¹³), one process per core (loaded). Part L and Part S profiles (traversal / kernel / summation). Checkpoint write. Full-length DFT | top and other a_q hashes equal to the local ones | ~25 min |
| P3 2243-scale data flow | The local R5 selection: stored and streamed a_q, a crash after 12 units (checkpoint every unit) and a restart, two pooled shards, the stored path. Full-size merge: DFT, 5.03·10⁶ symbol identifications, weights (timing only) | all four digests equal the **local R5 digest** (`3ca80f2e…`); the restart resumes from checkpoints; **the maximum symbol radius at T_run is below 1/2048**. Locally it is 4.878033·10⁻⁴, exactly the tail budget (v2.1 and v2.3 fixes, S4 §6) | ~15 min |
| P4 sustained throughput | About 300 top-range chunks streamed at full load (sized so the stage completes even if cloud cores are 25% slower than this host). The **whole process group is killed (kill -9)** at 30% and restarted. Mixed heights (q ≈ 10¹³ and 10¹¹) | all chunks verified, accumulated and merged; verifier hashes equal accumulator hashes | ~40 min |

The expected total is about 2 h of c7a.16xlarge: roughly **$2.5 spot, $7 on-demand**.

**Optional, within the cap:** repeat P2 + P4 on a second type. Candidates are c7a.48xlarge (192 cores, to check scaling), a Graviton c8g.16xlarge (ARM; the producer is portable C) or an Intel c7i (SMT vCPUs).

## 4. Deliverables and the decision they inform

* `results/checks.txt`: every PASS/FAIL above.
* `results/pilot.log`: batch walls, the P4 RESULT line with chunks per hour and $ per chunk, the restart loss.
* `fetch_results.sh` → `parse_cloud_rates.py`:
  * per-height f (cloud loaded ÷ local single-thread);
  * `rates_cloud.json`;
  * the S4 model re-run with cloud rates.
* **The central all-in figure for the full run, with f measured:** the S4 scenario table collapses to the pricing choice (spot vs on-demand) plus 1–6% operations overhead.

**Abort rules.** Any FAIL in P1 or P3 means no full-run request; the discrepancy is investigated first. A P4 FAIL means the same.

## 5. Before any full-run purchase, independently of the pilot

1. **D2**: the split Selmer comparison char(X_Gr) = T·char(X_cl) at 2243, read and bound.
2. **D5**: an independent certificate that the split-case extended height regulator at 2243 is nonzero (a second code path).
3. **An independent check of the prototype** (Codex; see `CODEX_CHECK_REQUEST.md`).
4. **Pre-production of segments 0–2047** (the only segments with several sub-units at UNIT_TERMS = 10⁹; about 5.9 GB; about 34 CPU-h of production and verification for 1.48·10⁹ primes, already inside the production total), plus a checkpoint-compaction step for long spot runs.

**One untested step, stated plainly.** The Linux build (P0) has not been run anywhere yet. This Mac has no container runtime active, so the bundle's `bootstrap.sh` will first execute on the rented machine.
* The sources, the portable SHA-256 and the reference digests are validated locally.
* If the build fails, it costs minutes of a capped instance. I would fix it and relaunch, within the ledger cap.
* Optionally, I can first try the build in a local Ubuntu container. That needs Docker Desktop started, plus downloads of the ubuntu:24.04 image and the FLINT 3.3.1 source.

**Bundle:** `bundle/pilot_bundle_2243.tar.gz`, sha256 `cb24d5f71d92caa2247c1e19ce1aed845da5d9ee3fab850fb828f40996abacd4`, 5.8 MB. It contains:
* the sources: v2.3 engine, sealed verifier and producer, compat shim;
* the PARI 2.17.4 tarball;
* the scripts;
* the local reference digests and hashes;
* PROVENANCE, recording the sealed-manifest matches.

## 6. Commands (you run them; dry run is the default)

```bash
cd /Users/bsm/BSD_2243_PILOT_PREP_2026-09-22/S5_pipeline/pilot && ./make_bundle.sh
```

```bash
KEY=<ec2-key-name> SSH_KEY=~/.ssh/<key>.pem SG=<sg-id> ./launch_aws.sh
```

```bash
KEY=<ec2-key-name> SSH_KEY=~/.ssh/<key>.pem SG=<sg-id> ./launch_aws.sh --launch
```

```bash
SSH_KEY=~/.ssh/<key>.pem ./fetch_results.sh <instance-ip>
```

The first `launch_aws.sh` prints the plan, the worst-case spend and the current spot price, and starts nothing. `--launch` starts one capped instance.
