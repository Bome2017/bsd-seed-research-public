# Combining the retained seed BSD methods

**Verdict: FABLE_CLOSURE_NOT_SUPPORTED.** Several links in the supplied note are incorrect or exceed the cited theorem's scope. The note does not establish that every successful combination must pass through Q36 or a common rational scalar. Conversely, no combination checked here proves a new uniform bound.

This is a bounded source and logical check, with one explicit mixed-conductor calculation. Seed arithmetic, the prior audits and imported theorem grades are retained. No computation campaign or successor session was launched.

## 1. Corrections to the supplied note

### The singleton equivalence again omits finite localization

The retained result is

    exists nonzero cyclic residual singleton
      iff [Sha[p^infinity]=0 AND finite loc_p != 0].

Existence of a two-prime unit Kurihara witness is equivalent to Sha[p^infinity]=0 at the retained grades. Thus Fable's first iff between singleton existence and pair existence drops an additional condition. The scan proves local nonvanishing only at the 3,240 tested good primes, not outside a finite set. Statements about existence must also not be converted into claims about every prescribed auxiliary pair.

### Theorem W cannot be substituted at Kato auxiliaries

At Kato auxiliaries b, b=1 and a_b=2 modulo p, so #E(F_b)=0 and a_b-2=0 modulo p. Theorem W/B.19 requires p not dividing #E(F_b) and uses the inverse of a_b-2. At G2 auxiliaries, residual Frobenius is -I, so a_b=-2 and #E(F_b)=4 modulo p. These are different auxiliary families.

Consequently the chain from a two-prime Kurihara number to w_p*(a_b-2)*R_(p,b) is not an established identity. A comparison between families would need proof with its actual local terms. G2 does not make the Kato-prime factor a_b-2 a unit.

### Kim's theorem is not an entrywise description of the equivariant matrix

[Kim, Theorem 1.8](https://arxiv.org/html/2203.12159v6), describes the higher Fitting ideals over Z_p of the classical Selmer dual over Q through normalized minima of valuations of Kurihara numbers, with the stated parity and nontriviality hypotheses. It does not identify each minor of an equivariant Selmer presentation with an individual Kurihara number. Section 1.9.3 explicitly limits this result to no equivariant variation.

The one-index target uses X_B, obtained from the Selmer dual over an auxiliary extension by mod-p reduction and group-ring base change. It is a different module over a different coefficient ring. No identification transporting Kim's displayed ideals to these equivariant ideals was supplied in Fable's note.

More fundamentally, even a correctly applicable exact dictionary would not prove that no further arithmetic relation can be found on either side. It would translate the consequence of such a relation. The inference “therefore all useful input must come from outside the Euler system, specifically the analytic side” is unsupported.

### Neither the unique-route claim nor the claimed joint conclusion follows

The assertions that every possible uniform proof needs a common global number, that Q36 is the only property which can supply the missing arithmetic, and that the two targets cannot be easier than that route are not established by the screened failures.

A rational nonzero q, a correctly normalized and finiteness-free tame comparison, and G2 could give eventual unit witnesses on their shared cofinite domain. But constructing an analytic object with leading term L''/2 alone supplies neither that comparison nor its integral lattice. Rationality alone also does not determine q=36: a denominator/separation bound or exact scalar value is still required. The finite exceptional primary groups remain separate obligations. The proposed common-scalar route is sufficient when its full hypotheses are proved, not shown necessary.

The note's instruction to keep an unrun correlation gate also needs chronology correction: the nearby Codex correlation gate already returned NO_NEW_BOUND, and the subsequent Mechanism B return has been read. This is not an instruction to relaunch either unchanged.

## 2. A concrete combination checked here: G2 plus a Kato conductor

Let p>=5 lie in the shared retained domain, n be a squarefree Kato conductor, and ell a distinct G2 auxiliary not dividing npN. Project the Mazur-Tate element at conductor n*ell to the retained real p-extension of conductor n. By [Bullach-Honnor, Proposition 2.4](https://arxiv.org/html/2511.07203v1),

    pi(theta_(n*ell)) = (a_ell - sigma_ell - sigma_ell^(-1))*theta_n.

Work modulo p in the group ring of this finite abelian p-extension. Its augmentation ideal J is nilpotent. For ell of G2 type, the factor U has augmentation

    aug(U) = a_ell-2 = -4 mod p.

Thus U is a unit. Explicitly, writing sigma_ell=1+v with v in J,

    U = -4 - v^2/(1+v).

Consequently U preserves every augmentation filtration step, and for theta_n in J^2 its quadratic leading term is multiplied by -4. The projected element has a nonzero quadratic term exactly when theta_n already did. If theta_n lies in J^4, the projection still lies in J^4.

For contrast, at a Kato auxiliary q the corresponding factor is

    2 - sigma_q - sigma_q^(-1) = -v^2/(1+v),

which belongs to J^2 and has zero augmentation. This explains precisely why the two kinds of auxiliary cannot simply be substituted into the same unit-normalized formula.

**Scoped outcome:** ordinary norm projection after adding a G2 auxiliary transmits the lower-conductor quadratic information but does not create nonvanishing. This is an elementary deduction from the source norm relation, not a new arithmetic upper bound. It does not exclude a relation using the larger conductor's unprojected mixed coefficients, G2's biextension data or additional cochain identities. Those data are lost or unused in this projection argument.

## 3. A valid combination of coverage that avoids a uniform Wieferich premise

For each good prime p let A(p) mean that at least one of the two rational generators has nonzero image in E(Q_p)/pE(Q_p). This condition does not assume Sha vanishes.

A sufficient mixed strategy would prove, outside one fixed finite exceptional set:

    A(p)  => some nonzero residual cyclic singleton exists;
    not A(p) => some two-prime Kurihara witness is a unit.

The singleton lemma handles the first case and B.21/B.23 the second. Together they give eventual Sha-primary vanishing. No theorem that simultaneous Wieferich primes themselves are finite is required for this design.

Both new implications remain unproved. The point is that different methods may cover complementary prime sets; a single method or a shared rational scalar is not a mandatory admission rule. A proof on a density-one set alone would still leave a potentially infinite uncovered set, and therefore would not suffice.

## 4. What a productive combination would actually add

Two useful principles must be kept distinct:

1. Separate failures do not prove the methods fail jointly. A countermodel to one chosen set of algebraic assumptions need not satisfy the extra arithmetic data of another method. No full joint arithmetic countermodel was constructed here.
2. Listing true statements together does not supply the missing comparison. To claim progress from a combination, identify the exact object or map where one method supplies information absent from the other, and derive a new constraint there.

For the G2/Kato/presentation combination, the concrete unfilled interface is an integral comparison involving the distinguished Kato classes, G2's normalized biextension data, and the full Selmer presentation, with local terms at Kato primes retained. The norm calculation above shows why ordinary projection is insufficient. A candidate calculation should expose these additional terms and determine their contribution to a minor or residual coordinate. It must not assume they are units, erase extra Selmer directions, or substitute a known rational-point class for the distinguished Kato class without proof.

This is a testable interface, not a supplied construction, an impossibility theorem, or evidence that the endpoint is close. A new intermediate compatibility identity could be worth retaining without already proving the complete uniform bound.

## 5. Disposition

Do not adopt the supplied note as the closing statement of the uniform step or as a reason to permit only Q36/archimedean work. Retain its observation that no complete construction was supplied. Correct the singleton implication, auxiliary-family substitution and Kim-theorem scope.

The combination question remains mathematically legitimate. One natural combination has been evaluated above and yields only a unit multiple; a second combination is a valid coverage design with explicitly open inputs. Neither closes FIN.

Only this output folder was written. Original documents, release, maps and memories are unchanged. No agents, messages, prime runs, paid jobs or pushes were launched.

FIN, ORDER9 and Q36 are unchanged.
