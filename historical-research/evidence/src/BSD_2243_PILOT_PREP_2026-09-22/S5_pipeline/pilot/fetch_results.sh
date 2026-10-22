#!/bin/bash
# fetch_results.sh <ip> -- copy the pilot's results tarball back (before the instance's self-termination) and summarize it.
set -euo pipefail
IP=${1:?ip}; SSH_KEY=${SSH_KEY:?set SSH_KEY}; HERE=$(cd "$(dirname "$0")" && pwd); D=$HERE/results_$IP; mkdir -p $D
scp -i $SSH_KEY "ubuntu@$IP:pilot_bundle_2243/pilot_results_*.tar.gz" $D/ || scp -i $SSH_KEY -r "ubuntu@$IP:pilot_bundle_2243/results" $D/
for t in $D/*.tar.gz; do [ -f "$t" ] && tar xzf "$t" -C $D; done
echo "== checks"; cat $D/results/checks.txt; echo "== pilot log"; grep -E 'RESULT|MIX|batch|full-size|killed|P1 m=' $D/results/pilot.log
python3 $HERE/parse_cloud_rates.py $D/results > $D/rates_cloud_summary.txt && cat $D/rates_cloud_summary.txt
