# Eighteenth addendum — H41 mod-4 successor: the optimal vertex is E and the base seed is odd on BOTH branches; retained-twist BSD(2); sealed

**Tier: SEALED_AREF_T — PROOF, REFEREE-AUDITED.** Two fresh Claude referees under a no-repair mandate: full reviews of revision 0 and
revision 1, delta reviews of revision 2 and revision 3; both ACCEPT WITH REMARKS on revision 3, **0 BLOCKING**. Imported inputs are at the
tiers listed in R/PROOF.md sec 1 and R9 (T = published theorem, A/A-ref = project-audited). NOT machine-checked. The operator gave the
go-ahead to seal on 2026-09-16 on the basis of the review record; no operator re-audit of the proof text is recorded.
Sealed text: `R/PROOF.md`, revision 3, sha256 `71024db1ca0893acf7cd20bd271fc80be5a6faf209feb15635b3a8d24201f2e3`.

## 1. The theorems

**Verbatim** — `R/PROOF.md` lines 14-16
```text
THEOREM P (positive). (i) E_0 = E. (ii) t = 2. (iii) 4 lambda is an odd integer; L(E,1) != 0, v_2(lambda) = -2.
 (iv) v_2(#E(F_q)) = 2 for every retained q; with I12: BSD(E^(q), 2). (v) With I13: BSD(E^(q)), qualified by BH v3 Remark 2.11.
COROLLARY N (negative). (i) E_0 = E. (ii) t = 4. (iii) 4 lambda odd. (iv)-(v) as in P with Zhai 1.5 in place of 1.7.
```

**Verbatim** — `R/PROOF.md` lines 72-73 (T1, the mod-4 Eisenstein congruence)
```text
Key congruence: -r_d d = w_d (mod 4) for all 8 positive divisors when l = 3 mod 4, and -r_d d = -w_d (mod 4) for the 4 negative ones when
p = 3 mod 4 (integer polynomials in l, p; checks sec 1). So theta_n = E+_n and theta_n = -E-_n (mod 4), n >= 1; theta_0 = 0 mod 8.
```

**Verbatim** — `R/PROOF.md` line 149 (the vertex)
```text
So 4 | n_0 = ord_2 Delta_min(E_0). By I1-I2 v_2(n_E) = 2, v_2(n_B) = 1, v_2(n_F) = v_2(n_G) = 0 (m odd): E_0 = E.  (i)
```

**Verbatim** — `R/PROOF.md` lines 153-154 (cusp order and seed, positive branch)
```text
the 2-part of the image: sp_{E}(pi(c)) has 2-primary component of order 2; t is even; t | 2 (I4): t = 2.  (ii)
I5 at positive E (delta_0 = 2, h = 1): z = 2 nu_0 lambda, reduced denominator 2, so z = 1/2 mod Z, 4 lambda = +-2z is an odd integer.  (iii)
```

Notation (R/PROOF.md sec 0): H41 bases E: y^2 = x^3 + (1-2r)x^2 + r^2 x, r = -2^m (positive, N = 6l) or r = +2^m (negative, N = 2p), m odd;
E_0 = the Gamma_0(N)-optimal quotient; t = order of the cusp image pi([0]-[inf]); lambda = L(E,1)/Omega_{E,R} (full real period); retained twists
q prime, q !| 2D, q = 5 mod 8, (D/q) = -1.

## 2. Mechanism (one paragraph)
d log F of the retained eta-quotient unit is congruent to +-omega_f modulo 4 (T1: an eight-term exponent-vector congruence against the Eisenstein
eigenform with U_2 = 1, U_3 = 3, U_l = l, and a_q = 1 + q mod 4 from the rational order-4 point). The full Fricke involution transports the
divisibility across the two components of X_0(N) at 2 (L2). Annular residues of the unit are the slopes s_x = 3(l-1)/e_x = 2 mod 4 (slope formula),
and annular residues of the pulled-back Neron differential are the integer coordinates of pi^* xi (Lemma R; Coleman 2000 Thm 4.1). So every
coordinate of pi^* xi is 2 mod 4 (positive) or has e_x u_x constant mod 4 (negative); Conrad–Stein then gives 4 | ord_2 Delta_min(E_0), forcing
E_0 = E, and the component-group image gives the cusp order and, through the retained real-logarithm identity, the odd seed. The new information
enters BEFORE the component-group quotient; the earlier proved blindness of Phi[2^inf] at the vertices F and G is not contradicted.

## 3. Review chain (all files carried in R/)
| review | text reviewed | verdict | blocking |
|---|---|---|---|
| referee_1/VERDICT.md | rev 0, 0cf7a5f9e598d8d8... | PASS WITH REMARKS (15 defects: 7 citation, 8 non-blocking) | 0 |
| referee_2/VERDICT.md, REPAIR_CHECK.md | rev 1, 953d4d6c2fb711a5... | PASS WITH REMARKS (D1-D14); referee_1 defects 14 resolved + 1 partial | 0 |
| referee_1/DELTA_REV2.md, referee_2/DELTA_REV2.md | rev 2, c5d806defa3bc55d... | ACCEPT WITH REMARKS / ACCEPT WITH REMARKS | 0 / 0 |
| referee_1/DELTA_REV3.md, referee_2/DELTA_REV3.md | rev 3, 71024db1ca0893ac... | ACCEPT WITH REMARKS / ACCEPT WITH REMARKS | 0 / 0 |
Final gates on rev 3 — referee_1: G1 PASS, G2 PASS WITH REMARKS (inputs it did not read: Coleman 2000 p. 322 / Bosch–Lutkebohmert, Coleman's proof
behind BR Rem 6.3), G3-G7 PASS. referee_2: G1-G3 PASS, G4 PASS WITH REMARKS (Atkin–Lehner sign), G5-G7 PASS. Sec 0 byte-identical across rev 0-3.
Author-side recheck by a separate model (R/src/author_recheck_2026-09-16) is NOT counted as an independent review.

## 4. Post-review records (do not modify the sealed proof text)
- `R/ERRATA_AFTER_REVIEW.md`: E1 BR locator L422-424; E2 R9 page ranges (Edixhoven p. 6, Coleman p. 319); E3 Omega(cusps) stalk: Edixhoven pp. 4, 6;
  an unreviewed Monsky 2-parity cross-route for epsilon_N = -1.
- `R/SOURCE_NOTE_POST_REVIEW.md`: Agashe–Winters, "Reducibility and rational torsion in elliptic curves", Lemma 2.1, read verbatim by the author
  (PDF and text in R/post_review_sources/): for an optimal E/Q of squarefree conductor N, "for all primes p | N, we have a_p(f) = -w_p", proof
  "U_p = -W_p on the new subspace of S_2(Gamma_0(N), C)". With sec 2 of PROOF.md this gives epsilon_N(f) = -1 on both branches: source hardening
  of the G4 remark.
- `R/SEAL_READINESS.md`.

## 5. Status flags (operator, 2026-09-16)
```text
H41_MOD4_SUCCESSOR = SEALED_AREF_T
POSITIVE_OPTIMAL_VERTEX = E
NEGATIVE_OPTIMAL_VERTEX = E
POSITIVE_CUSP_ORDER = 2
NEGATIVE_CUSP_ORDER = 4
POSITIVE_BASE_SEED: 4*L(E,1)/Omega_R odd; v2(L(E,1)/Omega_R) = -2; L(E,1) != 0
NEGATIVE_BASE_SEED: 4*L(E,1)/Omega_R odd; v2(L(E,1)/Omega_R) = -2; L(E,1) != 0
H41_RETAINED_TWISTS_BSD2 = CLOSED
H41_RETAINED_TWISTS_FULL_BSD = CLOSED_AT_EXTERNAL_LITERATURE_QUALIFIED_TIER
OLD_VERTEX_COMPONENT_ONLY_ROUTE = HISTORICAL_FAILED_MECHANISM / SUPERSEDED
OLD_H41_W_BLOCKED_STATUS = SUPERSEDED_BY_MOD4_INTEGRAL_CHARACTER_ROUTE
H9_STATUS = UNCHANGED
```

## 6. Supersessions and promotion
- H41_W_MECHANISM_AUDIT.md (sha dfa6291c...) NEGATIVE/POSITIVE_ROUTE = BLOCKED: superseded. Its conclusion remains correct for the mechanisms it
  audited (component groups and residual Eisenstein data do not evaluate the winding bit); the successful route adds the integral character vector.
- Vertex identification (PARKED 2026-09-15; Target W [Lambda_f : L(E)] | 2): CLOSED, in the stronger form E_0 = E on both branches.
- ADDENDUM_017 Theorems D/D' (negative bits, conditional on E_0 in {E,B}): the condition is now discharged; ADD_017 itself is unchanged.
- ~/H41_VERTEX_EXCLUSION_AUDIT_2026-09-16 (E_0 in {E,B}, one audit, unsealed): superseded by E_0 = E.
- Positive branch (POSITIVE_ROUTE = BLOCKED): closed at this tier.
- No longer needed: the Stevens/minimal-lattice 2-primary vertex search; a positive winding-value search; per-base optimality computations;
  F/G distinction through Phi[2^inf]; any re-assembly of the 62a1 or 66b1 families.

## 7. Non-claims
No Lean certification. No novelty assessment. No infinitude of H41 bases. No statement for twists outside the retained family. Full BSD for the
twists is qualified by Banwait–Huang v3 Remark 2.11 (BSTW, Castella–Ciperiani–Skinner–Sprung, Keller–Yin). The finite Cremona data (all ten H41
levels below 500000: E optimal, Manin constant 1) are regression evidence, not proof; eight exact lambda certificates remain eight. Nothing about the
general H9 bridge or general BSD.

## 8. Custody
R/ = the working directory ~/H41_MOD4_SUCCESSOR_PROOF_2026-09-16 at seal time, byte for byte except macOS .DS_Store files (history/, referee_1/,
referee_2/, checks/, src/, post_review_sources/, errata, source note, readiness record, its own MANIFEST.sha256). computation/build_addendum.py
regenerates R/, the receipts, DIGESTS.md and MANIFEST.sha256 and builds the archive without AppleDouble members; receipts/ records nested-manifest
custody, check reproduction against Cremona ecdata, prior-object digests and verbatim verification. The archive digest is recorded outside the
archive (ARCHIVE_DIGEST.txt beside it).
