# Acceptance and check scope

Accepted new arithmetic outputs: partner_A.out, paired_heights.out, geometry_screen.out, geometry_screen_second.out, combined329233_chunked.out (lower bounds only), combined329233_n8.out (nonzero digit), normalization329233.out. Each has a DONE marker and empty matching stderr. The separate exact checker and Pro replay support their stated algebraic/local scopes.

Rejected: combined329233.out is the official whole-sum memory overflow. It has process exit0 but no coefficient. It is not used as data.

The independent digit parser initially did not accept O(5) notation; it was repaired. When the precision7 result returned zero residues, the parser was extended to report lower bounds instead of treating the precision exponent as an exact valuation. The saved final JSON distinguishes these cases. These are parser repairs, not changes to producer digits.

The new source batching patch is a local GPL derivative of PARI2.17.3. It changes only the quadratic-character summation range and zero initialization. Four exact full-moment controls, a separate source-level audit, metadata assertions in the precision8 driver, and agreement of the lower/higher-precision coefficients are the validation. There is no independent second implementation of modular symbols or p-adic heights.

The source/local/point checker for d329233 was written separately from the producer, and replayed twice byte-for-byte. It retains the PARI rank upper bound and standard Cassels/Tate inputs. It is not a Lean theorem or independent human certification.

The sealed search caps were fixed before each screen; the second extension followed a two-second first screen and was sealed separately. This was an adaptive search for a discriminating case, not a random sample or frequency estimate. All candidates and unmeasured rank-two rows are retained. Class groups select candidates only.

No comparison here proves exact Sha order, Sha finiteness, a seed prime result, or a uniform estimate. A rational5-isogeny is not substituted for the seed's full residual image.
