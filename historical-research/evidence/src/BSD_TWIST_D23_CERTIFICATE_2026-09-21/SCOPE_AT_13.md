# Scope of the criterion at p = 13 — qualification accepted and made exact

Date 2026-09-21. Additive. Accepts the qualification in
`~/BSD_CODEX6_MASTER_HANDOFF_2026-09-19/_work/bridge_repair_assessment_2026-09-21/D23_COVERAGE_REVIEW.md`:
the ideal controls Sha **over K**, twist contribution included. Nothing launched.

## The qualification, stated as a decomposition

For **odd** `p` the idempotents `(1 ± sigma)/2` lie in `Z_p[Gal(K/Q)]`, so every `Z_p[Gal]`-module splits into
eigenspaces. Applied to `Sha(E/K)[p^inf]` with `K = Q(sqrt -23)`:

    Sha(E/K)[13] = Sha(E/Q)[13]  (+)  Sha(E^{-23}/Q)[13].

Hence the criterion is a **conjunction**, not a single statement about the seed:

    I_3(eps^Hg_{1,0}) = F_13   <=>   Sha(E/Q)[13] = 0   AND   Sha(E^{-23}/Q)[13] = 0.

Two consequences worth holding:

* **Success gives more than was asked.** If the ideal is the full ring, both 13-parts vanish; the seed's is the one we
  want, the twist's comes free.
* **Failure is ambiguous.** If `Sha(E^{-23}/Q)[13] != 0` then the ideal is not the full ring **even when
  `Sha(E/Q)[13] = 0`**. A negative outcome would therefore not be evidence about the seed.

## What the certificate does and does not give on the twist side

`ord_{s=1} L(E^{-23}, s) = 1` (now certified) gives, via Gross-Zagier-Kolyvagin applied **to the twist over Q**,
`rank E^{-23}(Q) = 1` and `Sha(E^{-23}/Q)` **finite**. It gives no information about that group's 13-part.

Note the two Heegner settings are different and must not be conflated:

* `E/K` has `ord L(E/K, s) = 2 + 1 = 3`, so `y_K` is torsion and Kolyvagin does **not** apply to `E/K`;
* the twist `E^{-23}/Q` has analytic rank 1, and Gross-Zagier-Kolyvagin applies to **it**, with its own auxiliary
  imaginary quadratic field satisfying the Heegner hypothesis for `E^{-23}` — not `K`.

So bounding `Sha(E^{-23}/Q)[13]` is a **separate** Heegner-index computation over a different auxiliary field. Its shape
is known (`#Sha` divides the square of the Heegner index; `13` not dividing that index would suffice); it is not
supplied by anything on record here, and **no such computation is proposed or launched**.

## Status

Threshold remains **1521**. `I_3` unevaluated, no method. The certificate supplies a premise; the criterion at 13 is a
conjunction whose second half is an independent obligation. FIN, ORDER9, Q36 open.
