# Bounded audit of A, B and C

Date: 2026-09-29.

| Return | Verdict | Decisive point |
|---|---|---|
| A: Theorem W | **CONFIRMED_WITH_CORRECTIONS** | Auxiliary independence survives. The p-primary use of BKS is justified, and the composite-symbol normalization is repaired below. |
| B: scalar target | **CONFIRMED_WITH_CORRECTIONS** | The sufficient target and height bound stand. Several candidate rejections and an ideal/lattice equivalence are overstated. |
| C: DK/BP screen | **CONFIRMED_WITH_CORRECTIONS** | The two screened mechanisms do not supply the needed bound. Their elliptic-curve analogies must remain scoped, rather than be called general impossibility results. |

Input manifests: A **15/15**, B **11/11**, C **6/6**. All 32 bound input files remain unchanged. The new derivation and corrections are contained in this output folder; no map or research return was edited. No seed prime run, push, message, successor construction or higher-power experiment was performed.

## A — answers to the four questions

**1. BKS and full finiteness: CONFIRMED_WITH_CORRECTIONS.** BKS §2.1 really does assume full finiteness. Nevertheless, the required instance of (27) follows without it. If Sha[p] is nonzero, Ota's contrapositive gives C2=0 at every eligible auxiliary. Otherwise Sha[p^infinity]=0, and the augmented Selmer complex has free H^1 and H^2 of rank two. Splitting off its invertible differential block identifies the degree-two determinant with its Bockstein determinant. This proves precisely the needed version of Proposition 5.4. Corollary 5.3 and Kataoka's determinant-element construction use the retained p-adic hypotheses; equality with the algebraic BSD element, (28), is unnecessary. The full proof is in [A_REPAIR.md](A_REPAIR.md), §1. This is a justified weakening for this argument, not the literal hypothesis list of the published statement. See [BKS II](https://arxiv.org/html/2103.11535v1).

**2. Compositum, line and production element: CONFIRMED_WITH_CORRECTIONS.** C_p x C_p is allowed; the relevant exterior-power target is one rank-one Z_p-module, hence one scalar works for the compositum. However, WORKING_2 incorrectly identifies the regularized composite element with the raw production sum up to a constant. [Darmon §2.3.1](https://www.math.mcgill.ca/darmon/pub/Articles/Research/06.Euler-systems/paper.pdf) includes lower-divisor corrections. For the present degree-p quotients these are norm elements times singleton sums. Modulo p they have degree at least p+1, so they disappear modulo I^3. **The exact identification is false, but the degree-two identification required by the proof is valid.** A_REPAIR §§2–3 supplies both this repair and a proof projecting BKS's element directly to the two singletons. The factors u and Eul_N then act by their stated unit augmentations.

**3. Pairing and augmentation: CONFIRMED at retained pairing grade.** Local p-divisibility follows from the formal group and p-free reduction. The local splitting difference consequently vanishes modulo p. Independently, Bockstein naturality gives both regulator projections on the same localized Mordell–Weil lattice. Multipliers act through augmentation on I^2/I^3. No factor of the extension degree p is introduced.

**4. Imports and sign: CONFIRMED_WITH_CORRECTIONS.** Odd residual surjectivity, including 5, is explicit in the retained G2 input; it is not reproved here. Ota 6.4 does not assume finiteness. The conclusion has sign **+** with the fixed conventions. Correct two side claims: a mismatched generator gives a square factor, which CAN be -1; and changing the period scales the ratios by a common constant rather than preserving their numeric values. Replace the malformed condition lq not-dividing pN by gcd(lq,pN)=1. At 5 this is a conditional comparison of eligible auxiliaries, not an extension of G2's infinitude theorem.

**Accepted conclusion:** outside B*={2,3,19,59,487,2243,4547,5843},

    w_(p,l) = w_(p,l')

for the stated admissible pairs. It is a written deduction at retained/imported-input grade. It establishes no nonzero value and no relation between different p.

**Numerical scope correction.** The 389a1 examples reproduce, including all five pairs and the negative controls. A new exact check also rejects equality of the full raw and regularized sums while confirming their degree-two agreement. The mixed-term test USES the assembled pairing from Step 2; it does not independently verify that arithmetic pairing. The supplied CHECKS.md correctly says this; Claude's pasted pre-audit overstates that test. I also strengthened the original sign check to reject vacuity, and it passes for the actual nonzero projection.

## B — target, consequences and mis-killed candidates

The scalar is well-defined on the stated G2/Ota domain, and its nonzero value implies the entire primary Sha group vanishes. PI_exists(B,m), for one fixed nonzero rational m, gives finite support outside B union primes(num m). Finiteness at that finite exceptional set is still required for FIN. The three bad-prime criteria do not yet supply those certificates.

A now identifies the some/every-auxiliary variants **outside 19,59,487** on B's domain. Do not use it at those three primes without a separate argument.

The exact height computation passes:

    M = 20,475,850,236,047,
    M/289 = 1,204,461,778,591/17 > 7.085 x 10^10.

It requires that the proposed law covers all nine observed residues. If its exceptional set includes 19, that residue cannot be included automatically. Omitting 19 gives the weaker bound 63,392,725,189/17. Finite observations establish neither PI nor an exact constant 288.

The target T is coherent and sufficient. Its Sha-free/q-free definition is a chosen admission rule, not a necessity theorem for all possible global proofs. No Z meeting all requirements was constructed.

**The ledger needs substantive scope corrections:**

- A factorization containing x_Q times #Sha does not exclude a new independent theorem controlling that factor. Likewise, proving rationality and the required reciprocity law could rescue the 8q route.
- “A p-independent ideal/lattice exists iff FIN” is false without specifying the arithmetic local lattices and their realization conditions. “An ideal is not an element” is not an intrinsic obstruction over Q.
- K2 must not equate LINE core pairs and singleton PI^infinity without a comparison. K10's universal wording about congruence modules must be restricted to the one-sided maps actually developed.
- PART1 §1.5's exact rational c_E comparison remains unchecked; the scalar and finite-support theorem do not depend on it. Its Kato assertions retain the smaller BKS domain.

The supported ledger conclusion is **none of the eleven entries supplied a complete construction in the reviewed material**, not that eleven mathematical possibilities were refuted. [B_CORRECTIONS.md](B_CORRECTIONS.md) supplies exact replacements, including the harmless augmentation typo and the status of the unreviewed p^k sketch.

## C — source and inequality checks

**DK:** the reverse-inclusion description is accurate. Over a DVR, Fitt(M) subset (Theta) means length(M)>=v(Theta). The paper turns the family of these inclusions into equalities using its analytic class-number input, notably Lemma 5.3. No analogous elliptic-curve theorem was constructed in this screen. Assuming BSD to supply it would be circular; proving a new arithmetic analogue would not be. [Dasgupta–Kakde, §5](https://arxiv.org/html/2010.00657v3).

**BP:** Theorems 1.7 and 3.5/Corollary 3.6 control combinations inside G-relations, not the absolute unknown Sha of the seed. The stated S3 comparison is consistent with prime-to-6 restriction and permutation-module additivity, but leaves other unknown primary groups. Also correct the description of (1.2): that display is already a relative equality derived from Cheeger–Müller, not an absolute elliptic-curve formula. [Bartel–Page](https://arxiv.org/html/1601.06821v3).

**Opposite inclusion:** Theta in Fitt(M) gives length(M)<=v(Theta) in the finite DVR setting. It does not prove that Theta, or the relevant leading coefficient, is a unit. In the group-ring Selmer setting keep the theorem's exact local hypotheses and Fitting interpretation; do not silently replace a positive-rank Selmer module by a finite one.

Thus NO_TRANSFER_FOR_THESE remains justified for the two screened transfers. It rules out neither a new equality theorem nor another torsion/spectral construction.

## Evidence and remaining boundary

Primary anchors and retained grades are in [SOURCES.md](SOURCES.md); exact results are in [CHECK_RESULTS.json](CHECK_RESULTS.json). The check driver replays three tiny PARI scripts and exact integer identities, with zero exit status and empty stderr required. All three PARI replays together took less than one second on this machine. No large scan was rerun.

The positive addition is A's fixed-p auxiliary independence with its repaired proof. The absent cross-prime law, nonvanishing and exceptional-prime conclusions remain absent. None of the source-return grades was changed in place.

FIN, ORDER9 and Q36 are unchanged.
