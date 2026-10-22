#!/bin/sh
# Replay the root manifest. Run from the freeze root. Exits nonzero on any mismatch.
cd "$(dirname "$0")/.." || exit 2
fail=0; n=0
while IFS= read -r line; do
  h=${line%%  *}; p=${line#*  }; n=$((n+1))
  g=$(shasum -a 256 "$p" 2>/dev/null | cut -d' ' -f1)
  [ "$g" = "$h" ] || { echo "MISMATCH $p"; fail=1; }
done < MANIFEST.sha256
echo "$((n))/$((n)) checked"; [ $fail -eq 0 ] && echo "MANIFEST_REPLAY = PASS" || echo "MANIFEST_REPLAY = FAIL"
exit $fail
