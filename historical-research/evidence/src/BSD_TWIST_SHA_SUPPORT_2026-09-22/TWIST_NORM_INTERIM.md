# Twist-normalization route — INTERIM (parts C and D done, A and B not read)

Date 2026-09-22. **No verdict returned**: the brief's five verdicts all turn on Wiersema–Wuthrich 2022 and
Wuthrich 2014, which I have not read. What follows is parts C and D, which are done and checkable, plus the two
corrections to the previous gate.

---

## 1. Corrections accepted

**Pasten's bound — arithmetic verified exactly.** `d(N²) = 4725` (confirmed: `N² = 2^6·3^2·7^4·2243^2·4547^4·5843^2`,
`d = 7·3·5·3·5·3 = 4725`). With `log N = 40.3029`, `log log N = 3.69642`:

    log deg(phi) <= (N/12 + 7 d(N^2)/12)(log N + 4 log N / log log N) = 2.228e18
    => v_7(deg phi) <= 2.228e18 / log 7 = 1.145e18

Matches the brief to three digits. **Effective, and useless**: rational reconstruction at denominator `32·7^{1.15e18}`
would need roughly `1e18` decimal digits of `L`.

    V7_MODULAR_DEGREE_UNRESOLVED   ->   V7_MODULAR_DEGREE_EFFECTIVE_BOUND_TOO_LARGE

Operational conclusion in `MODDEG_GATE.md` unchanged: more `L`-digits remain unjustified.

**`ellmaninconstant` exists and closes that loophole.** This PARI (2.17.3) has it; its own help: *"Return the Manin
constant of the curve, see ellweilcurve. **The algorithm is slow but unconditional.**"* So an exact unconditional
algorithm exists — and its complexity kills it at `N ≈ 3.19e17`. Worth recording precisely because it removes the
suspicion that we simply hadn't found the right tool.

## 2. Part D — exact period conversion. DONE, and the factor is exactly 1.

First, a correction to the record: **the seed model in use throughout the project is not minimal.**

    seed as given  : [0, -22735, 0, 106272484, 0]        is_minimal = FALSE
    seed minimal   : [0, -1, 0, -66020924, -65074271436]
    N_seed = 6503188012738584 = 2^3 · 3 · 2243 · 4547^2 · 5843        <- 7 does NOT divide it
    Delta > 0, 2 real components, torsion Z/2, prod c_v = 16, isogeny class size 2 (degrees 1,2),
    non_surjective = [2]

Period lattices at 200 bits, both minimal models:

    seed   omega_1 = 0.028044901519436404448309401807930384171135047866634966579801
           omega_2 = 0.030555626496343424956117345073281248877666623783763062584952 * I
    twist  omega_1 = 0.011548941266157222748917603067270380053596934957191939001661

    Omega(E^{-7}) * sqrt(7) / Im(omega_2(E))  =  1.0000000000000000000000000000000000000000000000000000000000

**58 digits.** So, with the structural reason: the twist map is defined over `Q(sqrt -7)` and pulls the differential
back by `D^{-1/2} = -i/sqrt 7`, which swaps real and imaginary periods — hence

    Omega(E^{-7})  =  Omega_-(E) / sqrt(7),      index factor exactly 1 (no 2's lost or gained between minimal models).

Consistency with the brief's normalization: `chi_{-7}` is **odd** (since `-7 < 0`), and for a primitive odd quadratic
character of conductor 7, `tau(chi_{-7}) = i sqrt 7`. So

    tau(chi_{-7}) · Omega(E^{-7})  =  i · Omega_-(E)

i.e. the Gauss sum exactly absorbs the `sqrt 7`, and the twisted normalization pairs with the seed's **minus** period,
which is the correct parity for an odd character. The two normalizations line up with **no fudge factor** — this was
derived and checked at 58 digits, not inferred from agreement to a few places.

## 3. Part C — the seed's Manin constant. DONE, and this is the payoff.

`N_seed = 2^3 · 3 · 2243 · 4547^2 · 5843`. The **only** odd `l` with `l^2 | N_seed` is **4547**. So ARS Cor 3.7
(`l | c ==> l = 2 or l^2 | N`) gives immediately

    Supp_odd( c_0(E_seed) )  ⊆  {4547}        and in particular   7 ∤ c_0(E_seed).

And 4547 falls too. The seed at 4547: Kodaira **III**, `v_4547(j) = 0`, and Sage reports the reduction **potentially
supersingular**. Edixhoven Thm 4.6.3's hypotheses all hold — `4547 > 7`; additive but not `I_0^*`/`I_ν^*`; no
`Q`-isogeny of degree 4547 (class degrees `(1,2)`, and `4547` is not in Mazur's list); potentially supersingular — so
`4547 ∤ c`. **Robust across the isogeny class:** both members are type III potentially supersingular at 4547
(`[0,-1,0,-66020924,-65074271436]` and `[0,-1,0,-597383344,5572681004764]`, both `prod c_v = 16`, `tors = 2`), so
whichever is the optimal curve, the conclusion holds.

    => Supp_odd( c_0(E_seed) ) = EMPTY.   The seed's Manin constant is a POWER OF 2.
    => 7 ∤ c_0(E_seed), PROVED, with no use of the Manin conjecture.

**The `I_0^*`-at-7 problem genuinely disappears on the seed side**, exactly as the brief predicted: that additive place
exists only after twisting, and `7 ∤ N_seed`.

## 4. But the obstruction RELOCATES to 2 rather than vanishing

`c_0(E_seed)` being a power of 2 bounds its *support*, not its *exponent* — the same distinction that sank the previous
gate, so it must not be collapsed again. And CNS Thm 1.2's `p = 2` exception **also fails to fire for the seed**
(`val_2(N_seed) = 3 >= 3`, but `3, 2243, 4547, 5843` are all `≡ 3 mod 4`), giving

    val_2( c_0(E_seed) )  <=  val_2( deg phi_seed )

which is the identical modular-degree problem, moved from 7 to 2. Raynaud (`4 | c ==> 4 | N`) does not help: `8 | N_seed`.

Two things make this *less* bad than the 7 case, and one makes it no better:

* `p = 2` is excluded from Kato's theorem (`p != 2`) and from the BLV-admissible lane anyway, so a 2-adic failure
  costs nothing **downstream**;
* the quantity we want, `v_p(#Sha_an)` for odd admissible `p`, is unaffected by a 2-power denominator **in value**;
* but the **rational reconstruction** still needs the *total* denominator bounded, and an unbounded 2-power blocks the
  rounding just as an unbounded 7-power did.

So the route has genuinely changed which Manin constant obstructs — from `c(E^{-7})` at `I_0^*`/7 to `c_0(E_seed)` at
2 — and whether that is an improvement depends entirely on parts A and B.

## 5. What is NOT done

* **Part A: Wiersema–Wuthrich, *Integrality of twisted L-values of elliptic curves*, Doc. Math. 27 (2022).** Not read.
  Their Theorem 2 / Theorem 17 and the `c_0 = 1` vs `7 ∤ c_0` vs `c_1 = 1` distinctions are exactly what would decide
  whether the 2-adic residue above is fatal. **`7 ∤ c_0(E_seed)` is now proved (§3), so if their theorem needs only
  that rather than `c_0 = 1`, the route may close — this is the single highest-value unread item.**
* **Part B: Wuthrich, *On the integrality of modular symbols and Kato's Euler system*, Doc. Math. 19 (2014).** Not
  read. Note the brief's caution stands and is the crux: per-prime `p`-integrality statements do **not** combine into
  an effective rational-reconstruction bound unless they are uniform.
* No exponent bound on `val_2(c_0(E_seed))` located.

**No verdict returned.** Returning one of the five would require A and B.

    STATUS: TWIST_NORMALIZATION_ROUTE = PARTS C,D DONE; A,B UNREAD; NO VERDICT
    Omega(E^{-7}) = Omega_-(E)/sqrt 7, factor exactly 1        PROVED (58-digit check + structural reason)
    tau(chi_{-7}) Omega(E^{-7}) = i Omega_-(E)                 PROVED
    Supp_odd(c_0(E_seed)) = EMPTY, c_0 a power of 2             PROVED (ARS 3.7 + Edixhoven 4.6.3, robust in class)
    7 ∤ c_0(E_seed)                                            PROVED
    val_2(c_0(E_seed)) <= val_2(deg phi_seed)                   PROVED (CNS 1.2, exception fails to fire)
    val_2(c_0(E_seed)) bound                                    NOT LOCATED   <- the relocated obstruction
    seed model in project use is NON-MINIMAL                    recorded; minimal is [0,-1,0,-66020924,-65074271436]
