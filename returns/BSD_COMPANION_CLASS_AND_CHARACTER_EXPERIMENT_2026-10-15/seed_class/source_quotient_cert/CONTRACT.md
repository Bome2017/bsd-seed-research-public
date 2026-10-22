# Cached-source quotient certification

2026-10-17. New method after companion BNF timeouts: certify only that the actual ordinary source class group is a quotient of the cached presentation. No new bnfinit and no fundamental-unit claim.

Input is the exact cached seed A BNF, bound by SHA256 in SEAL.json. GP bnfcertify(B,1), 90 second internal alarm, 100 second outer cap, 1 GB PARI stack cap. A return value 1 plus completion marker and clean diagnostics is required. Timeout means no certificate, not a false class claim. If certification succeeds, authenticate the S-prime generating relations in the named generators before promoting S-class=0. No known Selmer, norm-kernel or Sha dimension enters.
