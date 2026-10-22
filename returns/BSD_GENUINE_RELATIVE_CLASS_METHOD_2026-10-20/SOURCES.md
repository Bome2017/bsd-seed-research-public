# Source scope

Retained arithmetic: original seed point field and exact maximal-order data from lab62cf86b31d24be543a4e5677231c130c712e353d; scalar relative tower from99b6c994191a2aaad66ebf2c32ade640752cdfa6. Exact input hashes in inputs/BINDINGS.json. These are retained construction inputs, not a new certification of the global residual-image or rank theorem.

New source inspection:
- Cohen, Advanced Topics in Computational Number Theory, §§7.3.2–7.3.3: relative ideal reduction and relative class/unit computation. Detailed page/source receipt in theory/.
- Elsenhans–Voight, Computing class groups and unit groups in Magma, https://jvoight.github.io/articles/clgpunitgp-magma-02Oct25.pdf , §§4,7: distinguish generating ideals from relation completeness. Used as methodological source; no Magma computation or theorem about this seed is imported.
- Grenié–Molteni, Explicit bounds for generators of the class group, https://arxiv.org/abs/1607.02430 : GRH qualification on small generator bounds. No unconditional seed bound imported.
- Etienne, Computing class groups by induction with generalised norm relations, https://www.math.u-bordeaux.fr/~fetienne002/computing_class_groups.pdf , introduction and TheoremsA–C: the method requires an actual norm relation and subfield arithmetic. No new such relation is asserted.

No finiteness of seed Sha, BSD formula, predicted class number, or known seed primary vanishing is used to fill a missing class or unit rank.

- Belabas–Diaz y Diaz–Friedman, Small generators of the ideal class group,
  https://www.math.u-bordeaux.fr/~kbelabas/research/OnBach.pdf , §5, Corollary5.2:
  a separate unconditional sufficient generation criterion. The full
  prime-ideal norm inventory fails this criterion at T=419776; the exact
  rational check is in theory/BDDF_RESULT.json. No nongeneration claim.
