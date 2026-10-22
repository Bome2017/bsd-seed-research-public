# Simultaneous principal-divisor relations at coefficient seven

Status: **CHANGED_SOURCE_TESTED; ALL ADMITTED UNIT PRODUCTS ARE EXACTLY +/-1**.

This is actual degree-48 389a1 arithmetic, not a geometric incidence model. It changes the previous unsuccessful method: instead of asking one small element to have norm 1 or two principal ideals to agree, it takes the complete integer relation lattice among many principal ideals and their scalar translates. Every relation product is authenticated as an ordinary global unit without BNF or GRH.

Three finite source batches were completed:

|Batch|Base elements|Scalar factors|Prime-divisor rows|Divisor rank over Q and F_7|Integer relation rank|Distinct exact factors up to sign|
|---|---:|---:|---:|---:|---:|---:|
|Small norm groups|26|156|150|57|99|57|
|Changed mixed-parity source|40|240|285|120|120|120|
|Combined cached sources|57|342|378|157|185|157|

All principal ideal factorizations were reconstructed exactly. Each scalar translate was checked against the transformed principal ideal. The integer kernel matrices satisfy D K=0 over Z. No completeness of units or class groups is used.

The decisive additional calculation is not a residue detector. Merge factors that are literally equal up to sign in the exact number field. For each of the three batches, the merged exponent matrix is identically zero over Z. Therefore every admitted relation product is literally +1 or -1. This completely explains their zero faithful-character residue images: it is not merely vanishing at a finite list of test primes.

For the first batch, the separate local lane checked the actual coefficient-prime local quotient and split-prime quotients; a separate review freshly factored all 156 orbit principal ideals and agreed with the matrix. Those checks are complementary; the exact factor merge is what establishes the scoped structural failure.

## What was changed after the first failure

The first 99 relations collapsed to signs. We then excluded candidates satisfying sigma^3(a)=+/-a and selected from genuinely mixed-parity candidates. There were 1980 such elements among the previously computed 2000 candidates; this reused saved norms rather than repeating the scan. Among the 100 smallest mixed norms, 45 factorizations were fully certified, but only 2 had all prime factors <=10^7. The pre-registered relaxation selected 40 candidates with the smallest largest certified prime factor. Their actual ideals were factored and reconstructed, and the full relation calculation was repeated. This second family also collapsed to signs. A final combined lattice used both batches' cached ideals, without another factorization campaign; it also collapsed to signs.

Thus the failure is not explained solely by using even elements or pairing only two ideals. This particular small-element pool has independent principal-divisor columns once exact repetitions are removed.

## Virtual classes in these finite families

In each batch the divisor matrix has the same rank over Q and F_7, and the integer-kernel columns have full complementary rank modulo7. Hence ker(D mod7) is exactly the reduction of the recorded integer kernel. Within these finite multiplicative families, a divisor divisible by 7 produces no additional virtual-unit direction beyond recorded units and seventh powers. This is a statement about the chosen families, not a bound on the full 7-class group or the complete descent source.

## Bounds and limits

No nontrivial faithful-character unit, nonzero incidence-norm witness, improved whole-unit kernel bound, or class-supported bound was obtained for 389a1 at 7. The genuine ambient character-unit dimension remains 4; zero ranks on these trivial relation products do not say that the actual norm map has rank zero.

The experiments were bounded and all scripts/receipts are retained. There was no BNF retry, publication, remote job, or inference from known Sha. The exact source failure is recorded so this same finite pool is not used again as if its 185 relations were 185 new arithmetic directions. FIN, ORDER9 and Q36 are unchanged.
