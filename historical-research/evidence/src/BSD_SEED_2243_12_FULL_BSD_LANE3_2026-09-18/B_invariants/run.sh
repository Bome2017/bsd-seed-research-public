#!/bin/zsh
# usage: run.sh <tag> <timeout_s> cmd...   -- runs under nice 15 + timeout, logs CPU/RSS to cpu_log.tsv
tag=$1; shift; to=$1; shift
D=/Users/bsm/BSD_SEED_2243_12_FULL_BSD_LANE3_2026-09-18/B_invariants
/usr/bin/time -l nice -n 15 timeout $to "$@" > $D/out/$tag.out 2> $D/out/$tag.time
rc=$?
u=$(grep -E ' real .* user ' $D/out/$tag.time | tail -1 | awk '{print $3}'); s=$(grep -E ' real .* user ' $D/out/$tag.time | tail -1 | awk '{print $5}')
r=$(grep 'maximum resident set size' $D/out/$tag.time | awk '{print $1}')
echo "$tag\trc=$rc\tuser=$u\tsys=$s\tmaxrss_bytes=$r\t$(date +%H:%M:%S)" >> $D/cpu_log.tsv
tail -1 $D/cpu_log.tsv
