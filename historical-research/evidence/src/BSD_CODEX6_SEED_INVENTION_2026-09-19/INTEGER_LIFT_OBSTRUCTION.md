# Obstruction to raw localization determinants as a common integer

This excludes a specified construction class. It does not exclude every
integer whose support might contain Sha.

Let D_{p,L} be the determinant of the rational-point localization matrix
at an admissible ordered pair L of auxiliary primes, as in F1.
Its value depends on coordinates by multiplication by a unit. Whether
it is zero is coordinate-independent.

## N6: no comparison across all auxiliary choices

Fix an odd p satisfying F1. There do not exist a scalar c in F_p and
units u_L in F_p^* such that
\[
D_{p,L}=u_L c
\qquad\text{for every admissible pair }L.
\tag{*}
\]

Proof: F1 supplies a pair with invertible matrix, forcing c nonzero.
It also supplies a pair of rank one, forcing c zero. Contradiction.
QED.

The same proof applies to any positive power of D, and to multiplication
by any nonzero normalizing factors. In particular no nonzero integer C
can satisfy
\[
D_{p,L}^{\,m}=u_{p,L}(C\bmod p)
\]
for all admissible pairs, with m>0, throughout an odd-prime tail.
A fixed rational normalization with bounded denominators cannot repair
the contradiction outside its finitely many numerator/denominator
primes. This is a non-coherence theorem for the stated raw determinant
comparison, not a general obstruction to characteristic-zero invariants.

Restricting the pairs to invertible ones deliberately removes this
contradiction. In that restricted family unit existence is automatic
by F1; it supplies no Sha vanishing statement.

## N7: simultaneous determinant content misses the known Sha prime

For every odd p of the seed the ideal
\[
\bigl(D_{p,L}: L\text{ an admissible pair}\bigr)\subseteq\mathbf F_p
\]
is the unit ideal, by F1.

Therefore an alleged nonzero integer C with the defining support rule
\[
p\mid C
\quad\Longleftrightarrow\quad
D_{p,L}=0\text{ for every admissible }L
\tag{**}
\]
has no odd prime divisor. Relative to the retained nonzero Sha[3]
import, such a C cannot satisfy
\[
\Sha[p]\ne0\Longrightarrow p\mid C
\]
for all primes: p=3 is an explicit counterexample. The p=3 certificate
is independently checkable without the general F1 theorem.

Multiplying this C by 3 by hand avoids that particular counterexample
but establishes no implication at any remaining prime. The proposition
that all other Sha components vanish would still need its own proof.
No claim is made that a bare integer supported at 3 is impossible;
indeed that is the expected support if the desired endpoint is true.

## What this eliminates, and what remains outside the theorem

Eliminated:

- A unit-normalized identity between one scalar and raw determinants
  over **all** these auxiliary pairs.
- The claim that a unit determinant of the known rational points
  forces Sha[p]=0.
- An integer defined by simultaneous raw-determinant content, used
  without a separate arithmetic comparison as a detector of every
  nonzero Sha[p].

Not eliminated:

- Determinants coupled to derived modular-symbol coefficients or other
  independently controlled global arithmetic classes.
- A rule choosing auxiliary data with extra arithmetic properties not
  supplied by F1.
- A nonlocal invariant, a congruence/Sha comparison with genuinely new
  hypotheses, or a proof of the expected support by another method.

The reason is explicit in F2: invertibility leaves a Selmer kernel
isomorphic to Sha[p]. The available determinant has controlled the
known-point summand only. No successor construction is proposed here.
