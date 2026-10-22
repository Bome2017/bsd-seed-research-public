# Arithmetic receipts — corroboration, not proof

`counts_66b1.py` is dependency-free Python. It counts points on the 66b1 minimal model and on the
proposed descent model `Y² = X³ + 17X² + 64X` by brute force over `F_q`, for primes below 4000.
Run it, or replace it — nothing here is load-bearing.

`counts_66b1_output.txt` is its output on this machine.

What it reports, without interpretation:

- the 38 primes below 4000 satisfying `q ≡ 5 (mod 8)`, `(q/3) = −1`, `(q/11) = +1`, with the point
  counts of both models, `v₂(#Ẽ(F_q))` and `a_q`;
- whether the two model counts agree on those primes;
- a control table: the `v₂` histogram over all good odd primes below 4000, split by the pair of
  quadratic characters `((2/q), (33/q))`.

The control table is included because `33 = A² − 4B` for the proposed 66b1 model, the same role
`−31` plays for 62a1. Draw your own conclusions from it. Note again that the proposed family fixes
`(q/3)` and `(q/11)` separately, which is not the same condition as fixing `(33/q)`.

Independently established curve data (conductor, discriminant, Kodaira types, Tamagawa numbers,
torsion, rank, `L(E,1)/Ω`) is in `01_target/66b1_target.md` §1 and comes from Cremona/LMFDB rows,
not from this script.
