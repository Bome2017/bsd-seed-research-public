# Representation-only replay repair

The original exact authentication finished in17.33seconds. A separate replay multiplying large24x24 HNF ideal bases hit its37-second wall cap. Its files are preserved in `rejected_hnf_replay/`. This is a resource failure of that replay, not an invalid unit identity.

Use PARI's prime-ideal descriptors instead: refactor the same317 small principal factors in the exact number field, compare their canonical ideal valuation vectors to the saved matrix, and reconstruct each factor ideal with those descriptors. This repeats the successful producer's exact arithmetic and avoids the expensive generic-HNF product path. New replay cap35-second GP alarm /37-second wall /1GiB. No BNF or class certification.
