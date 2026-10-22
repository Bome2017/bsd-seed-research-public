#!/usr/bin/env python3
"""S4 all-in projection: measured local work (cost_s4.json) -> cloud dollars, as explicit SCENARIOS (no probabilities).
  dollars = W_lch * (1 + ops_overhead) / f * price_per_core_hour + storage + transfer + merge machine + pilot (capped)
W_lch   measured work in local core-hours (idle single-thread i9-10910; production + verification + engine + checkpoints)
f       cloud core throughput relative to one local idle thread, UNKNOWN until the pilot measures it (P2/P4). Scenario band
        0.75 / 1.00 / 1.25. (Local loaded-host data: 0.914 per physical core fully loaded without SMT.)
price   AWS c7a (1 vCPU = 1 physical AMD Genoa core): spot $1.199/h / 64 = $0.0187 (vantage.sh, 2026-09-23; spot moves),
        on-demand $3.2845/h / 64 = $0.0513 (us-east-1). Band: spot 0.015-0.025, on-demand 0.0513.
ops     restarts after interruptions (checkpoint every 600 s: ~400 s lost per worker per interruption), operator reruns,
        checkpoint compaction: 1% / 3% / 6%.
storage 100 GB gp3 per instance for the run's duration at $0.08/GB-month, plus 200 GB object storage for a month at
        $0.023/GB-month; transfer out 5 GB at $0.09/GB."""
import json
C = json.load(open('/Users/bsm/BSD_2243_PILOT_PREP_2026-09-22/S4_cost/cost_s4.json'))
SC = {'low': dict(f=1.25, price=0.015, ops=0.01, label='spot, fast cores'),
      'central': dict(f=1.00, price=0.0187, ops=0.03, label='spot at the listed price, local-speed cores'),
      'high-spot': dict(f=0.75, price=0.025, ops=0.06, label='spot, slow cores, frequent interruptions'),
      'on-demand': dict(f=1.00, price=0.0513, ops=0.01, label='on-demand, local-speed cores'),
      'worst': dict(f=0.75, price=0.0513, ops=0.06, label='on-demand, slow cores')}
CORES_PER_INSTANCE, INSTANCES = 64, 20
PILOT_CAP = 100.0
rows = []
for label, d in C.items():
    W = d['total_lch']
    for name, s in SC.items():
        core_h = W * (1 + s['ops']) / s['f']; compute = core_h * s['price']
        wall_h = core_h / (CORES_PER_INSTANCE * INSTANCES)
        storage = INSTANCES * 100 * 0.08 * max(wall_h / 730, 1 / 30) + 200 * 0.023 + 5 * 0.09
        merge = 2 * 3.2845 / 64 * 64                                   # one c7a.16xlarge-hour-equivalent x2 for the final merge/DFT
        rows.append((label, name, s['label'], W, core_h, compute, storage, merge, compute + storage + merge, wall_h))
print(f"{'cutoff':52s} {'scenario':10s} {'core-h':>10s} {'compute $':>10s} {'storage $':>9s} {'merge $':>7s} {'TOTAL $':>9s} {'wall @20x64 cores':>18s}")
for r in rows: print(f"{r[0][:52]:52s} {r[1]:10s} {r[4]:10.0f} {r[5]:10.0f} {r[6]:9.1f} {r[7]:7.1f} {r[8]:9.0f} {r[9]:12.1f} h ({r[9] / 24:.1f} d)")
print(f"\nplus the pilot itself: hard cap ${PILOT_CAP:.0f} (planned spend <= $50 by construction; see PILOT_PROPOSAL.md)")
top = 171.89 + 23.54 + 0.249                       # seconds per top-range chunk (q ~ 3.912e13), local single thread
avg = sum(C[list(C)[0]]['components_lch'][k] for k in ('production', 'verification', 'traversal_L', 'kernel_L', 'summation_L')) * 3600 / 2331727
for name in ('central', 'on-demand'):
    s = SC[name]; print(f"$ per fully verified accumulated chunk ({name}): top-range {top / s['f'] / 3600 * s['price']:.5f}, average segment {avg / s['f'] / 3600 * s['price']:.5f}")
json.dump({'scenarios': SC, 'rows': rows}, open('/Users/bsm/BSD_2243_PILOT_PREP_2026-09-22/S4_cost/allin.json', 'w'), indent=1)
