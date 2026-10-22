# Sources and exactly what was used

All sources below were opened in this run. No literature novelty claim is
made. The elementary presentation and ideal-identity proofs are written
in this packet; they are not attributed to a source merely by analogy.

1. [Henri Cohen, advanced computational number theory manuscript](https://www.math.utoronto.ca/~ila/Cohen%20--%20Advanced%20topics%20in%20computational%20number%20theory.pdf),
   §§7.1.1–7.1.2 and §§7.3.2–7.3.3, especially Algorithms 7.3.7–7.3.8.
   Read the distinction between norm-kernel and extension-quotient relative
   class groups, the relative ideal reduction invariant, and the algorithm's
   generation/stopping assumptions. The source demonstrates a genuine
   relative reduction method. Its full implementation uses base arithmetic
   and GRH tests; neither is silently assumed here. The selected reading
   receipt is SOURCE_RECEIPT.json. The full book and text extraction are
   excluded from the deliverable.

2. [Andreas-Stephan Elsenhans and John Voight, Computing class groups and
   unit groups in Magma, 2 October 2025](https://jvoight.github.io/articles/clgpunitgp-magma-02Oct25.pdf),
   §§4, 7, and the concluding discussion of computation modulo a prime.
   Read the distinction between missing ideal generators and missing
   relations. This supports keeping the former as a separate certification
   obligation. It does not certify this seed or supply the relative code.

3. [Karim Belabas, Francisco Diaz y Diaz, Eduardo Friedman, Small generators
   of the ideal class group](https://www.math.u-bordeaux.fr/~kbelabas/research/OnBach.pdf),
   Author-hosted manuscript dated 5 December 2005, §5, Theorem 5.1 and
   Corollary 5.2, inequality (23), printed page 12 (PDF page index 11).
   This is the unconditional part of the paper, distinct from its earlier
   GRH bounds. The actual field's complete norm inventory was used to test
   this specific criterion at T=419776. An exact rational inequality proves
   failure at that cutoff; decimal values are only diagnostic. Failure of
   a sufficient criterion does not prove nongeneration.

   The complete 15-page PDF body was retrieved through the web tool, not a
   search snippet. The test's displayed inequality, transcribed into the
   checker's notation, is

       4 sum_{Norm(P)^a<T} log(Norm(P))/(1+Norm(P)^a)
           * (1-log(Norm(P)^a)/log(T))
       > log(Delta)-n*(gamma+log(4*pi)-pi^2/(4*log(T)))
           -r1*(1-log(4)/log(T)).

   The preceding §5 proof explicitly removes GRH; this is not inequality
   (10) from the earlier conditional section.

Retained project inputs: the seed A24 maximal order and scalar action;
the Aplus12 fixed field; full scalar-character unit dimensions; and the
complete source sequence with the valuation term vanishing on its stated
domain. These are not recertified by the presentation proof. The review
lane's norm inventory, discriminant identity, and source script are bound
by SHA-256 in BDDF_RESULT.json.

The cutoff 419775 originates in the retained PARI 2.17.3 `LIMC2` output,
not in an unconditional theorem. In the bound source `buch2.c`, lines
3809–3819 compute `GRHchk` and explicitly label the resulting prime-ideal
generation assertion as assuming GRH. The matching seed discriminant and
`LIMC2=419775` are printed in the prior `unmodified_small_base.err`.
The local source hash matches the retained official-archive binding; that
archive was not downloaded anew. CUTOFF_SOURCE.json records the hashes.
No re-evaluation or proof-assistant certification of PARI's GRH checker is
claimed. Our independent BDDF test concerns a different, unconditional
criterion at this same numeric cutoff.
