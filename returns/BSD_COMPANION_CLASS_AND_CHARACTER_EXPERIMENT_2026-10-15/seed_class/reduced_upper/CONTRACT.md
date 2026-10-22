# Separately sealed reduced-polynomial class-upper repair

2026-10-15. The original exact-unit bnfinit(flag=1) timed out at 120 seconds; its files remain untouched. This repair targets a rigorous class-group upper bound, not exact units or exact class-group equality.

1. polredbest(saved exact NF,1): GP alarm 30s, outer40s, max PARI stack1,000,000,000 bytes. Verify the original polynomial at the returned generator image is exactly zero, charpoly equals the original polynomial, and inverse-map identities. Save the exact field isomorphism.
2. bnfinit(reduced NF,0): GP alarm120s, outer130s, same memory cap. This is provisional until the next step.
3. bnfcertify(B,1): GP alarm180s, outer190s. Acceptance requires returned1 and clean error channel. This certifies that the actual ideal class group is a quotient of the computed presentation, hence its order and 3-length are bounded above by the computed ones. Exact units are not claimed.
4. Optional S-prime/minus sharpening requires actual verified ideal relations and equivariant presentation. Coarse full class-group upper remains valid without that sharpening. No predicted class number, known Sha, norm-kernel dimension, or unit-admission rank enters a calculation.

Primary source: PARI General_number_fields.html, bnfcertify flag1 and bnfinit flag0 documentation. No additional attempt or budget increase after a resource failure at the repaired stage.
