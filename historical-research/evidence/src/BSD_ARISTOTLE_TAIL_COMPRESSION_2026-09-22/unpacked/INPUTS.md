# INPUTS — retained results. Do not re-derive these.

## 1. Seed and proved endpoint data
`E : y^2 = x^3 - 22735x^2 + 106272484x`, `N = 2^3*3*2243*4547^2*5843`.
`rank E(Q) = 2 = ord_{s=1}L(E,s)`; `E(Q) = <(0,0)> (+) Z P_1 (+) Z P_2`, `P_1=(4547,327384)`, `P_2=(5184,281520)`.
Primary: `Sha[2^inf]=0`, `Sha[3^inf]=(Z/3)^2`, `Sha[5^inf]=Sha[7^inf]=Sha[11^inf]=Sha[13^inf]=0`.
Under FIN: `#Sha = 9t^2`, `gcd(t, 2*3*5*7*11*13)=1`, conditional next order **2601**.
`RANK` closed; **FIN and the real leading-term comparison open**.

## 2. The certified twist lane (lane 1)
`39.512236 <= L'(E^{-23},1) <= 40.182321` (Arb ball + proved tail bound, 708 s), so `ord L(E^{-23},s)=1`, hence by
Gross-Zagier-Kolyvagin `rank E^{-23}(Q)=1`, `Sha(E^{-23}/Q)` finite, and `rank E(Q(sqrt -23)) = 3`.

## 3. The comparison and its regime
Regime (P): `p>=5`, `p ∤ N`, `p ∉ {19,59,487}`, `E` ordinary at `p`, `p ∤ #Etilde(F_p)`, **and `p` split in `K`**.
With a certified rank-one twist, dualizing the Kummer sequence and splitting the free rank-three quotient gives,
without assuming FIN,

    Fitt^i_{Z/p^n}( Sha(E/K)[p^n]^* ) = I_{i+3}( eps^Hg_{n,0} ),   in particular
    I_3(eps^Hg_{1,0}) = F_p  <=>  Sha(E/K)[p] = 0.

Lane 1 serves exactly `p = 13, 31, 41, 47, 71, 73, 101, 127, 139, 151` among primes 5..160 (independently verified by
direct point counts at all 35 good primes in range).

**Scope you must respect.** For odd `p` the idempotents `(1±sigma)/2` split the `p`-primary Sha over `K`:
`Sha(E/K)[p] = Sha(E/Q)[p] (+) Sha(E^D/Q)[p]`. So the unit-ideal test is a **conjunction**. Success gives both parts;
**failure is ambiguous**, since a nonzero twist part makes the ideal proper even when the seed part vanishes. Finiteness
of the twist's Sha (from analytic rank one) supplies no bound on its `p`-part.

## 4. Refuted shortcut — do not retry
The Heegner Λ-index does **not** determine `I_3`. Counterexample: in `Lambda = Z_p[[t]]`, two complexes with
`H^1 ≅ Lambda`, `H^2`-torsion of the same characteristic ideal `(g^2)`, the same `y = g b` in the same free rank-one
`H^1 = Lambda b`, hence identical `H^1/Lambda y` — yet **different specialized higher Fitting ideals**. The involution
condition is compatible. Characteristic-ideal data alone is a lossy shadow of the Selmer complex; MCS uses the full
comparison.

## 5. Local data at the calibration prime
`#E(F_17)=24`, `a_17=-6`: good, ordinary, nonanomalous. `chi_{-23}(17) = -1`, so lane 1 does **not** serve 17.

## 6. Bad places are generically vacuous
For `p` in regime (P) the five fixed bad places impose no condition: `l^2 | N` at `l = 2, 4547` forces `a_l(f) = 0`
there, and `E(Q_l)[p] = 0` at every bad `l` for `p` outside the explicit exceptional set. (Variables: `l` ranges over
the bad places of `N`; `p` is the Selmer prime.) A uniform theorem does **not** have to
wrestle with five unrelated bad-prime conditions.
