# Correction — FRONTIER.md rev 6, lines 111-112. Additive; FRONTIER.md is not edited.

FRONTIER.md l.111-112 says `C_1 := |gcd(all k x k minors)|` "is nonzero — forced by the single good specialization
at p = 13". The same claim appears in
`~/BSD_ARISTOTLE_TAIL_COMPRESSION_2026-09-22/review_2026-09-22/SYNTHESIS_AB.md` l.15 ("nondegeneracy free from the
certified p = 13 unit specialization").

**Not supported.** `~/BSD_TWIST_D23_CERTIFICATE_2026-09-21/SCOPE_AT_13.md` records that over `K = Q(sqrt -23)`

    I_3(eps^Hg_{1,0}) = F_13   <=>   Sha(E/Q)[13] = 0   AND   Sha(E^{-23}/Q)[13] = 0

and only the seed's 13-part is supplied. The twist's is not. So there is **no** certified good specialization at 13,
and `C_1 != 0` is **not established**.

The matrix lemma (`effective_constant_of_integral_model`, `minorGcd_ne_zero_of_unit_prime`) is unaffected: it is a
correct implication *from* a unit specialization. What is withdrawn is the claim that its premise is satisfied.

FRONTIER.md also contradicts itself: l.125 correctly calls the comparison at 13 "open, not closed". L.125 is right;
l.111-112 is wrong.

Found by an external read-only review, 2026-09-22. Missed by the author's own search because l.111 says "good
specialization" rather than "unit" — a grep for the conclusion's vocabulary does not find a premise stated in other
words.
