# 66b1 continuation addendum

This is a post-freeze supplement. It does not replace either preserved reconstruction.
The Stage-I SHA-256 remains
`0f9468a2747c98794e3c7ff3991439cd8f2355095fd2b370b6c641daaca19050`.

## Period-signoff boundary

For a minimal Neron differential, let Omega_plus be the least positive real period
and Omega_R the integral of the absolute differential over the full real locus.
The curve and the stated positive twists have two real components. Thus

    Omega_R = 2 Omega_plus,
    L/Omega_R = (1/2) Lalg_Zhai,
    v2(L/Omega_R) = v2(Lalg_Zhai)-1.

Zhai's definition is explicit (arXiv:1409.0231, p.2). Miller's full-real definition
is explicit (arXiv:1010.2431, p.1). Banwait--Huang Definitions 2.1, 2.7 and the
remark in the proof of Theorem 2.14 identify their convention with Miller and
Cai--Li--Zhai (arXiv:2601.16044v3, pp.3,4,8; arXiv:1712.01271v2, pp.1-2).

BSTW Conjecture 1.1 and Theorem 10.12 (arXiv:2409.01350v2, pp.2,89) have not yielded
an explicit definition fixing whether the real-component factor is inside the
period. No identification of that symbol is authorized by this addendum. Its
literal Theorem 10.12 separately fails a_3(E)=0, since a_3(66b1)=-1.

## An explicit global minimal model of the positive prime twist

For a prime q congruent to 5 modulo 8 in the stated family, put

    M_q: V^2+UV+V = U^3 + ((5q-1)/4)U^2
                            - ((3q^2+1)/2)U - (3q^3+1)/4.

Its coefficients are integral. The substitution

    x=4(U-q), y=8V+4U+4

gives C_q: y^2=x^3+17q x^2+64q^2 x, with the equation residual multiplied by 64.
Its inverse is U=x/4+q, V=(y-x-4q-4)/8.
The invariants are

    c4=97q^2, c6=-17q^3, Delta=528q^6.

At 2,3,11, c4 is a unit, so the equation is minimal. At q the discriminant
valuation is 6, less than 12, so it is minimal. At every remaining prime except
those already listed the discriminant is a unit. Thus this is globally minimal.
The differential transformation is

    pullback(dx/(2y)) = (1/2) dU/(2V+U+1).

This differential factor is separate from the real-component factor.

At 2, the displayed equation reduces to V^2+UV+V=U^3. Its singular point is
(1,1). Translating U=1+s, V=1+t gives tangent cone t^2+st+s^2, irreducible over
F_2. The reduction is nonsplit I_4; the order of the Frobenius-fixed part of the
geometric component group Z/4 under negation is 2, so c_2=2.
At 3 and 11 the discriminant valuations are 1, giving I_1 and Tamagawa number 1.
At q>=5 the C_q model has I_0^* reduction. Its component polynomial is
T(T^2+17T+64), with exactly one residue-field root because (33/q)=-1.
Therefore c_q=1+1=2. See Barrios et al., arXiv:2501.03209v2, Theorem 4.1 and
Table 4, pp.13-14, for the odd-characteristic ramified-good-twist rule.

These computations justify the finite-Tamagawa ledger independently of a
choice for BSTW's period symbol. They neither edit the frozen prediction nor
supply an unqualified BSTW/full-strong-BSD theorem import.

## Receipt verification in this continuation

The 100000-bound point counts were retained rather than rerun. The separate
script verify_continuation.py verifies exact prime coverage by an Eratosthenes
sieve, recalculates every quadratic character and every arithmetic relation in
the stored CSV, and checks the frozen criterion. It newly enumerates both
curve equations literally at p=5 and p=19. These primes have the same unsigned
control pair (-1,-1), but counts 4 and 16 respectively.

The supplied prior rerun remains byte-identical to the supplied output.
The symbolic model identity and invariants above were checked independently
with SymPy. This symbolic check corroborates the displayed polynomial identities;
it is not an analytic period certificate or a Lean proof.
