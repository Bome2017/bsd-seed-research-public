# Alternative (b): arithmetic compatibility first, rationality second

## Correct input boundary

**DERIVED from v2 §3.** Arithmetic compatibility of the proposed level-p^k ratios is not proved input. An arbitrary lift of w_p to Z_p is not a level-p^k Mazur–Tate/tame identity. The present packet supplies no proved level-p^k comparison that repairs this gap; no such compatibility is assumed below.

## Candidate B-1: completion or CRT as the endpoint

**DERIVED — formal paired example.** Select an infinite set U of untested primes whose complement is also infinite, disjoint from the retained observed primes. In the abstract product of p-adic integers, set

    z_p=0 for p in U,
    z_p=288 otherwise.

Every z_p has compatible reductions at all powers p^k, and the family has compatible CRT reductions at composite moduli. It preserves the listed seed residues. Yet the family is not the diagonal image of a rational number: zero at infinitely many components forces any such rational number to be zero, contradicting the components equal to 288. The same argument applies already to cofinite mod-p agreement, since a nonzero rational numerator has only finitely many prime divisors.

This is an example about completed rings, not an assertion that these z_p are the actual arithmetic ratios of the seed. It shows exactly why completed compatibility, even if independently proved, would not by itself imply a nonzero rational scalar or eventual primary vanishing.

**DERIVED — first failing test.** K-S. The proposed endpoint from compatibility alone does not exclude infinitely many zero components. Actual arithmetic compatibility is also unproved, but it is not needed to see the earlier endpoint failure.

## Lemma B.2: a bounded-lift sufficient condition, without assuming arithmetic compatibility

**DERIVED — abstract statement.** Suppose x is an element of product_(p notin S) Z_p and D is a fixed positive integer supported on S. For each positive integer m coprime to S, let b_m be the balanced integral representative of D*x modulo m. Then x is the diagonal rational integer z/D for some integer z if and only if the b_m have a common absolute bound.

**DERIVED — proof.** If D*x=z, balanced representatives have absolute value at most |z|. Conversely, assume |b_m|<=H. For m,n>2H, compare both with a common multiple l: b_l-b_m is divisible by m and has absolute value at most 2H<m, so b_l=b_m; similarly b_l=b_n. Hence the representatives stabilize to one integer z at large moduli. For an arbitrary modulus, comparison with a sufficiently large multiple gives D*x=z modulo that modulus. Equality in the inverse limit follows.

**DERIVED — stopping point.** Applying this lemma to the arithmetic ratios would first require a proved arithmetic inverse system and then an independent common bound after clearing one fixed denominator. Neither was constructed. The comparison in Attempt (i) concerns minimum augmentation degree, not sizes of compatible integer lifts.

**DERIVED — test record.** The lemma is an abstract intermediate criterion, not an endpoint candidate. The complete route first lacks the uniform arithmetic comparison and bound required by K-P. It does not acquire a numerical failure merely because no candidate scalar has been computed.

**DERIVED — nonzero condition.** Rationality alone can produce zero. To use the bounded-lift route for the endpoint one must also prove that the resulting rational scalar is nonzero, for example through one retained nonzero residue that lies in the proved comparison domain. No such comparison domain is constructed here.

## Claim boundary

**DERIVED.** No w_p^infinity is newly certified. No common rational number is produced. No implication between a common mod-p scalar and equality of full p-adic lifts is assumed: the latter is strictly more data than the former.
