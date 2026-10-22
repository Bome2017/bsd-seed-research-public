# Independent return check: bad-prime BH singleton criterion

Date: 2026-09-27. Verdict: **AGREE — CRITERION_VALID_AT_ALL_THREE_PRIMES**, at the reported written/preprint/import grade.

The audit's mathematical implication, exact factor 1/2, and scope distinctions survive this check. No blocking error was found. This is acceptance of a sufficient criterion, not a claim that a nonzero singleton exists or that a computation is affordable.

## Custody and review scope

The received archive has SHA-256 `f86ab9c53515ef527f404bf3333d13e1976a82c639baed195f4686b9f57bf7cc`. Its outer manifest verifies 18 entries, the original handoff manifest verifies 10 entries, and the six source-copy bindings verify. All eleven files of the embedded original handoff, including its manifest, match this machine's original handoff byte-for-byte. See CUSTODY.json.

I read REPORT.md and CRITERION.md, re-derived the application, and reread the decisive primary-source statements listed below. Retained rank, residual image, symbol lattice, and underlying general Euler-system theorems remain imports at their existing grades. The residual-image review was inspected, not rerun end to end. No Lean build, numerical L-value calculation, symbol evaluation, coefficient generation, corpus scan or cloud job was launched. Batch C and both repositories were not accessed or modified in this return check.

## Decisive checks

1. **The theorem's target is the right group.** BH Theorem 1.4(b) concerns the dual of the classical p-primary Selmer group. The finite-Sha qualification in the introductory discussion applies to a different integral object. The conclusion of section 4.5 explicitly returns to the classical Selmer group. The application does not assume the finiteness it seeks to prove.
2. **The Fitting direction is correct.** In A=Fp[t]/(t^p), let d be the minimum number of generators of Y=X/pX. A minimal presentation has all entries in (t), so its d-by-d minors lie in (t)^d. Nonzero quadratic leading coefficient in Fitt^0(Y) forces d<=2. Arbitrary base change of Fitting ideals applies to reduction modulo p; flatness is not needed. This conclusion would fail for an annihilator bound alone.
3. **Restriction uses no division by p.** Full residual image over Q leaves no p-torsion over the abelian field K. Inflation-restriction is injective, and functoriality of local Kummer maps preserves classical local conditions. Dualizing bounds the generator count over Q by d. No local control isomorphism is needed.
4. **Generator count kills the whole group.** The dual Kummer sequence splits over Zp with free quotient Zp^2. Thus its generator count is 2 plus that of the finitely generated primary-Sha dual. A bound of two, followed by Nakayama, kills the latter. The proof does not merely kill its finite quotient or prove corank zero.
5. **Normalization is exact.** Positive discriminant gives two real components. BH divides by the total real Neron period 2*omega1, whereas the supplied production convention divides by omega1. Minus symbols cancel in the real quotient, and group-ring projection sums rather than averages. Therefore theta_BH=(1/2)*theta_pipeline. The # involution changes (C0,C1,C2) to (C0,-C1,C2+C1), so a quadratic leading term retains its nonvanishing. There is no additional Manin or derivative-factorial correction between these definitions.
6. **All three reduction types are admitted.** K is a real degree-p subfield of Q(mu_ell), unramified at p. Along with retained large image, this meets BH's field conditions even for additive p=4547. The coefficient is in the auxiliary-conductor variable, so the old split cyclotomic exceptional-zero cubic criterion does not impose a cubic correction here.

The same argument gives C0=C1=0 modulo p from the lower bound d>=2 even before a nonzero C2 is obtained. A bad-prime acceptance contract must use this BH argument, not cite Ota outside its hypotheses.

## Source-version check

The source range and period convention were checked at [BH v1](https://arxiv.org/html/2511.07203v1), Hypothesis 1.2, Theorem 1.4(b), section 2.1/Definition 2.2, Remark 2.9, Theorem 3.6 and the end of section 4.5. These are imports from the identified preprint.

[Bullach–Burns v1](https://arxiv.org/pdf/2509.13894v1), Corollary 9.6(i), gives determinant-image membership; the BSD-conditioned equality is the separate clause (ii). The current [author-hosted revision](https://dominikbullach.github.io/bb.pdf), Theorem 9.4 and Corollary 9.7, adds a quadratic-field roots-of-unity restriction at non-potentially-good p. The return correctly checked the stronger condition: any relevant conductor-ell base field is unramified at p, and a quadratic extension has ramification index at most two. It cannot contain Qp(mu_p), of index p-1>2. Potentially good 4547 uses the other alternative. Thus the version difference does not block this application. Neither long foundational proof was replayed. The author URL is mutable; this check does not pretend to provide a pinned byte hash of that PDF.

[Stacks 07Z6](https://stacks.math.columbia.edu/tag/07Z6), Lemma 15.8.4(3), confirms the base-change assertion. The minimal-generator/minor argument above was re-derived separately.

## What changes

At the retained grades all three outstanding bad primes now have the following explicitly normalized alternative:

    C2 = sum_{a=1}^{ell-1} binom(ind_g(a) mod p,2) s_a,
    C0 = C1 = 0 (mod p), C2 != 0 (mod p)
       => Sha(E/Q)[p^infinity] = 0.

For s_a=n_a/1024, the BH coefficient is 2048^(-1) times the integer weighted sum. Production can retain its 1024^(-1) convention under an explicitly separate BH theorem profile.

In particular, 4547 has a concrete quadratic singleton sufficient test. This is stronger project coverage than merely citing a general additive-prime paper. It is still only a forward implication. No prime has been settled by this review, and FIN, ORDER9, Q36 and the existing good-prime results are unchanged.

## Cost-screen boundary

The next practical question is worth measuring, but it is not answered here. Use the accompanying COST_SCREEN_TASK.md as a separately bounded planning task. Two traps need to remain explicit:

- The K=288 relation and the G2 auxiliary-selection theorem were not extended to these bad primes by this argument. Do not assume a predicted nonzero coefficient.
- The ratio ell/p^(3/2) compares exponential scales, not full runtime. Larger auxiliary denominators add symbol-accumulation and output costs, while coefficient production and verification must be counted separately.

No changes to the supplied audit are needed for acceptance at its declared grade. Retain the original audit and this independent check additively; do not call either a new human-refereed theorem or an end-to-end Lean proof.
