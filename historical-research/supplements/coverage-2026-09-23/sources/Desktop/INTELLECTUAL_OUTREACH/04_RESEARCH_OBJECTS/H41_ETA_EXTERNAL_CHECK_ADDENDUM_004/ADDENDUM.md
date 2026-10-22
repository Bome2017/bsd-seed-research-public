# Fourth addendum — the external check, and four corrections to Claude

**Tier: COMPUTATION plus recorded corrections.** No prior object is reopened.
`CODEX_H41_SEED_RESEARCH_FREEZE_001` (`ac82f3ad…`), `H41_SEED_FREEZE_ADDENDUM_001` (`82b6730f…`),
`H41_ETA_CHARACTER_ATTEMPT_ADDENDUM_002` (`81ac107b…`) and
`H41_ETA_CHARACTER_TEST_ADDENDUM_003` (`35f21882…`) are unmodified.

External check archive: `h41_eta_character_external_check.zip`,
`911bbae6de3e944c712cc3ae55a0a9174105a6353c82dd5e4bc5be8f2e2b707e`. Its own manifest replays 29/29,
it carries a byte-identical copy of `ADDENDUM_003`, and its scripts run and reproduce their recorded
output byte-identically. Full audit in `receipts/CLAUDE_AUDIT.txt`.

## 1. A real defect in Claude's test: the sample does not span at N = 254

This is the substantive correction and it is against my work.

    level    my sample     compact homology rank    rank my sample spans
    62       1338 cycles   14                       14
    254      1367 cycles   62                       61

At `N = 254` **my sample misses one compact-homology direction.** The test I reported therefore did
not establish the character equality on full homology at that level — one direction was never probed.
I had no spanning argument at all; I offered gcd stability under a wider sample as evidence, and their
calculation shows directly that stability of the gcd does not establish spanning. That inference of
mine was unsound.

Their witness makes it concrete: `γ = [[71,45],[254,161]]` lies in `Γ₀(254)` with `det = 1` and
`γ(0) = 45/161`, and `d = 161` exceeds my sample bound `d ≤ 120`, so my sample provably could not
contain it. Recomputed here: its eta winding is `−1810`, exactly as they state, and even, while the
reconstructed functional gives `0` — both even, consistent.

**Their repair uses existing information rather than more sampling.** The supplied symbol is in the
plus eigenspace, so its value on a conjugate cycle equals its value on the original; it is cuspidal, so
it vanishes on peripheral cusp loops. The eta character has the matching properties mod 2 — conjugation
negates the integer winding, which does not change parity, and the even cusp-divisor orders make the
parity vanish around the cusps. Adjoining conjugates and cusp loops gives an index-one integral
generating set at `N = 254`; `N = 62` already had one. Their replayed output records
`sample_plus_cusps_plus_conjugates: rank 65, index_if_full 1` at `N = 254`.

They then checked the eta winding against the reconstructed functional on complete redundant Schreier
generating sets: **192 instances at `N = 62` and 768 at `N = 254`, zero parity disagreements**, with the
reconstructed functional integral and of gcd 1 at both levels.

## 2. `mslattice` is integral cohomology — my residual question was mis-framed

I left the result conditional on "whether PARI's `mslattice` is the `U₀` lattice or the plus
eigensublattice." That is the wrong dichotomy. `mslattice(M,H)` is defined through the inverse image of
integral group **cohomology**; with `H` omitted it uses the cuspidal subspace. So the rank-14 lattice at
`N = 62` is an integral cuspidal **cohomology** lattice — neither `U₀` nor plus homology. Corroborated
directly here: `msdim` is 17 and 65 (the open Betti numbers) while `mslattice` has rank 14 and 62 (the
compact ones).

The correct comparison is obtained by dualizing. With `π : J₀(N) → E₀` the connected optimal quotient,
connectedness of the kernel gives a surjection on integral homology, so

    π* : H¹(E₀,ℤ) ↪ H¹(X₀(N),ℤ)   is saturated,

and inside the rational newform plane, taking the integral lattice and then its plus eigenline gives
`π* Hom(U₀,ℤ)`. The elementary identity that makes this work:

    Hom(U₀,ℤ) = H¹(E₀,ℤ)^{τ=1}

**Verified here in both directions.** Forward: if `f` is τ-invariant and `τx = −x` then `f(x) = −f(x)`,
so `f(x) = 0` because `ℤ` is torsion-free. Converse: `τ² = 1` makes `(1−τ)x ∈ ker(1+τ)`, so an `f`
killing that kernel satisfies `f(x) = f(τx)` for every `x`.

**Plus cohomology is the correct dual object; plus homology is not the same object.** Their
counterexample verified: for `τ = [[1,1],[0,−1]]`, `ker(1+τ) = ⟨(1,−2)⟩` so `Hom(U₀,ℤ) = ⟨2x+y⟩`, while
plus homology is `ker(τ−1) = ⟨(1,0)⟩`, where `2x+y` takes the value `2`. That is exactly the factor of
two the frozen report warned about — and it does **not** mean a further factor must be inserted after a
functional has already been shown primitive in the correct integral cohomology eigenline. So once the
rational elliptic plus eigenline is correctly identified, primitive integral normalization supplies the
required quotient functional up to sign.

## 3. Two of Claude's significance claims corrected

**The four-curve agreement is expected, not four independent tests.** I presented identical parities
across all four curves of the isogeny class as robustness. They share the same rational newform line
with different period-dependent scalings, and dividing each by its sample gcd removes those scalars up
to sign. So it is a consistency check on my normalization, not four independent probes of the mechanism,
and it is not evidence that the raw period factors agree. My claim overstated it.

**My "reproduces parities already implied by λ = 1/4 and 3/4" understated the experiment.** Those
central values constrain the **distinguished cycle's** evaluation only. They do not imply equality of
two characters on every homology generator, and many distinct characters agree on a single cycle. So the
full-character comparison has genuine additional content: the candidate survived a test the two known
central values did not automatically make it pass. That is the gain — not the number of matrices.

## 4. An evidence gap in ADDENDUM_003, now closed

They noted that `ADDENDUM_003` shipped `norm62.gp` with no saved output and no `norm254.gp`. Confirmed.
`receipts/norm_both.gp` and `receipts/NORM_BOTH_OUTPUT.txt` now record the normalization check at both
levels with output retained:

    N = 62 : xs-coordinates in the mslattice basis have denominators in {1,2}; 2·xs integral
             with coordinate gcd 1, hence primitive.   mseval{0,1/3} = −1/2
    N = 254: same denominators {1,2}; 2·xs primitive, gcd 1.   mseval{0,1/3} = −3/2

So `α_p({0,1/3})` is `−1` at `N = 62` and `−3` at `N = 254` — both odd, consistent with `4λ = 1` and
`4λ = 3`. That consistency is a check on the pipeline, not evidence for the seed.

## 5. Corrected conclusion

    At N = 62 and N = 254, the supplied elliptic-symbol data support  chi_p = alpha_p mod 2
    on FULL homology -- not merely on an unverified sample.

with the qualification the external check itself states: this rests on the supplied PARI eigenline and
evaluations, which were not independently recomputed there or here. What was independently established
is the spanning, the integral normalization, the dual identity, and the extension of the comparison to
complete generating sets.

## 6. Status — unchanged

    negative branch   u₃ ∈ 2^a U₀              PROVED
                      u₃ ∉ 2^(a+1) U₀          OPEN
    identification    chi_p = alpha_p mod 2    holds on full homology at N = 62, 254;
                                               UNPROVED uniformly in p
    a = 1 case        factorization fails there; occurrence unknown
    positive branch   OPEN

**The H41 seed remains unproved.** Two levels are a tested candidate mechanism, not a family theorem.
No Aristotle or additional model run was used for any check in this object, and none is authorised.
