# Corrected relative torsion estimate: across-prime capacity test

This is a written check of the shape of the **relative** small-split-prime estimate. It is not a computed class rank at larger primes and not a lower bound on the class group.

Let p≥5 be in the retained good/full-image domain. Write

    n=p²−1, m=n/2, d=n/4,
    delta=N(discriminant(A_p/K_p)), D_K=|disc(K_p)|.

Use the author preprint's relative quadratic degree in Lemma2.1. Its prime window satisfies Y=delta^theta with theta<1/(4p). In a quadratic extension, at most one unordered split pair lies above each prime of K_p. There are at most m prime ideals above each rational prime, so, even granting every possible split prime,

    M <= m*pi(Y) <= mY.

Thus the uncalibrated discriminant factor appearing on the right of the torsion estimate satisfies

    sqrt(delta*D_K)/M
       >= sqrt(D_K)*delta^(1/2−1/(4p))/m.

The retained type-III inertia calculation at4547 gives both delta and D_K at least 4547^d. Therefore

    sqrt(delta*D_K)/M >= 4547^[d(1−1/(4p))]/m > p^4.

The final strict inequality has an elementary uniform check. Since d≥p, 1−1/(4p)>1/2, sqrt(4547)>64, m<p² and p≤2^(p−1), the left lower expression is greater than 64^p/p², which is greater than p^4.

This does not bound actual p-torsion from below. It shows why simply using the standard discriminant numerator with the largest allowed supply of split primes does not itself yield a small numerical ceiling. With any conservative explicit implied constant chosen at least1, and epsilon>0, that expression remains too large. The published estimate leaves the implied constant degree-dependent; it gives no uniform small class theorem as p varies.

This calculation concerns the shape of the quoted asymptotic estimate. It does NOT exclude sharper character-specific packing, additional arithmetic class relations, a stronger regulator result, or another p-torsion estimate. In particular the relative prime window itself grows as p grows; the source-version typo in the published display is not used to claim an eventual absence of small split primes.

No degree>24 seed maximal-order object was computed in this lane. The exact larger-prime calculations below test the integer inequality in the displayed expression, not a class group.
