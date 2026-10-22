# Actual seed principal-source construction and rejection

Status: EXACT BOUNDED SOURCE EXPERIMENT; NO NEW SEED BOUND.

This experiment uses the seed E=[0,-1,0,-66020924,-65074271436] and coefficient prime 5. It does not use known Sha[5] vanishing, an L-value, a height determinant, a class-group computation, or a claimed finite Selmer basis. Retained full residual image identifies the nonzero point field L=Q(T), T in E[5], as a degree-24 field. The published full-5 descent map has additional norm/additivity constraints; a character-eigenvector in L*/L*5 is not automatically a class in H1(Q,E[5]).

## 1. An actual field source

Let sigma act on L by T -> 2T, with sigma^4=1. For z in L*, form

    P(z)=z sigma(z)^3 sigma²(z)^4 sigma³(z)^2.

Then

    sigma(P(z))/P(z)^2 = (sigma(z) sigma²(z))^-5.

Thus P(z) lies in the scalar-2 eigenspace modulo fifth powers. This assertion is an exact multiplicative identity, not a claim that it passes all full-descent constraints.

Set q=1783 and choose the actual local point T1=(1591,1089) of order 5. The first candidate was z=y(T)-1089. Its norm is computed exactly by

    Norm_L/Q(y(T)-r)=Res_X(psi5(X), f(X)-r²)/5³,

where f=X³-X²-66020924X-65074271436 and the conventional psi5 has leading coefficient 5. Pairing T with -T proves this formula directly. The denominator is 125, not 5.

For r=1089, the exact numerator norm has valuations

    v3=12, v73=1, v149=1, v991=1, v1783=1, v58043=1.

These are small-prime factors, not a complete factorization. At 73 the unique zero is the actual 5-torsion point (51,67). Its scalar orbit in order 1,2,4,3 gives y-values 67,52,6,21. Exactly one factor y-1089 vanishes modulo73. The norm valuation one proves simple valuation one, so the scalar projection remains ramified at this good prime.

The first candidate also fails coefficient additivity already at q: its valuation profile is supported on one scalar orbit, whereas a nonzero linear functional on E[5] is nonzero on 20 of the 24 nonzero points. Scalar homogeneity was not enough.

## 2. One local repair does not enforce global admission

The lift r=1089+1783=2872 preserves the original local zero at q and removes all zeros at73. Its exact norm has v1783=1, but now v7=v839=v1877=1. Thus this literal repair of the first offending place introduces other unsupported places. This is a statement about these two candidates; it is not a proof that every repair must fail.

## 3. Repair the coefficient-valuation pattern first

The parent experiment constructs over F1783 the affine-line polynomial

    h(Y)=Y^5+1013Y^4+799Y^3+389Y²+655Y+1152
        = product_{j=0}^4 (Y-y(T1+jS)),

where Frobenius(S)=3S and T1,S form a basis of E[5]. Its integer coefficient lift defines a genuine global field element h(y(T)). Projecting as above makes the valuation profile on nonzero torsion points the desired linear functional (i,j) -> i. See the parent local-pairing record for its all-point check. This repairs the valuation-additivity defect of the first candidate; it does not establish all unit/norm relations of full descent.

This source's exact norm was calculated independently in two ways. Write

    h(Y)h(-Y)=C(Y²),
    g(X)=C(f(X)).

Then

    Norm_L/Q(h(y(T)))=Res_X(psi5(X),g(X))/5^15.

Sage computes the resultant; a separate standard-library implementation derives psi5 from division-polynomial recurrences and evaluates the 27-by-27 Sylvester determinant by exact integer Bareiss elimination. The entire rational result matches, not only its displayed valuations.

The norm has v1783=5 exactly. The five prescribed geometric zeros consist of one residue-degree-one point and one residue-degree-four orbit. Each has valuation at least one; equality of the norm valuation with 1+4 proves that both primes have valuation exactly one. This authenticates the claimed linear ramification pattern at q.

But v7(Norm)=1. The unique zero at7 is T=(0,6), and its scalar orbit is

| multiplier | point | h(y) mod7 |
|---|---|---|
| 1 | (0,6) | 0 |
| 2 | (5,5) | 3 |
| 4 | (0,1) | 5 |
| 3 | (5,2) | 1 |

Since 7 is a good prime and 7 !=5, the nonzero torsion field is unramified there and the torsion coordinates are integral. Norm valuation one means one degree-one prime has valuation one and all others zero. The four scalar-conjugate primes are distinct. Consequently the projected source has valuations (1,2,4,3) modulo5 at this orbit: its extra ramification is genuine and cannot be removed by multiplying by a fifth power.

Every full-5 Selmer class is unramified at a good prime away from5. Restriction and the Weil-pairing Kummer representation preserve that fact. Over the unramified torsion field, an unramified Kummer class has valuation divisible by5. Therefore this projected field element cannot represent a seed Selmer class or a class relaxed only at1783. This exclusion does not require knowing whether it satisfies the other descent relations: failure of this necessary local condition is decisive.

The corrected affine-line candidate thus passes the desired q-valuation pattern and fails a different, explicitly computed global-support requirement at7. No conclusion about all possible sources follows.

## 4. What was already present, and the minimal computational issue

Historical source paths and hashes are in HISTORICAL_BINDINGS.json. The existing point-field and dual-field constructions are already available in

    /Users/bsm/BSD_SMALL_SEED_FIXED_PRIME_2026-09-17/runs/fields_2243_12.gp.

The record has degree24, signature(4,10), discriminant about10^213.06, a 10.4-second field-construction run, and a separate prohibitive stock class-group estimate. Its old exact relations already include local rows at31 and181 and leave the relevant class-group dimension undetermined. We did not rerun a full BNF or present that old descent criterion as new.

Restricting to the degree-six field of a cyclic order-five subgroup makes a 5-isogeny rational, and degree6 is prime to5. But its kernel character still has order4; the usual scalar Kummer construction trivializes it over the degree24 point field. The restriction does not, by itself, supply a cheaper complete Selmer computation. This is a limitation of that immediate implementation, not a theorem against every degree-six method.

## 5. Exact output and scope

- principal_probe.py/json: first source norm and q-torsion orbit.
- leak_repair.py/json: two lifts, exact norms and local residues.
- verify_principal.py/json: independent standard-library norm and local checks.
- line_source_probe.py/json: affine-line source, exact norm and offending prime7.
- verify_line_source.py/json: independent 27-by-27 resultant and residue replay.

The desired global source must satisfy both coefficient additivity and its allowed ramification/local conditions. This experiment has constructed and repaired specific sources far enough to test both, rather than defining the answer through Sha. It has not supplied a source that passes them all, and has not excluded every possible source. FIN, ORDER9 and Q36 are unchanged.

## 6. Standalone replay and cost

The three source producers are self-contained and write relative to their own directory. The independent verifier imports only the adjacent standard-library checker; it does not invoke Sage, PARI, a source theorem, or an external dataset. Reproduce with:

    python3 replay.py --sage-python /path/to/sage/environment/bin/python

The historical field file is copied as `source_inputs/fields_2243_12.gp`, SHA-256 `19512f63278df2678008e7f4669214f6fa0b8c19407713f2c01413745238d81a`. It is custody evidence for the old field interface; the exact resultant probes do not depend on its huge coordinate formulas. All historical source hashes appear in HISTORICAL_BINDINGS.json.

The completed replay took 2.840, 2.813, and 2.853 seconds for the three Sage producers and 0.050 seconds for the independent verifier, including process startup. All exit codes were zero, stderr was empty, and all five saved result JSON files reproduced byte-for-byte. REPLAY.json retains exact timing and hash fields. No full number-field class-group computation or large relation search was run.
