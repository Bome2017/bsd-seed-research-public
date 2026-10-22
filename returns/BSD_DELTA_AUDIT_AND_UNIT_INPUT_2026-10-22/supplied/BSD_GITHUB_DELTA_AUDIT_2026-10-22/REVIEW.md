# BSD GitHub delta review — 22 October 2026

## Verdict

The substantive new work consists of the direct primary-torsion bound packet and the joint class continuation, together with a public evidence edition. Neither mathematical packet improves the retained complete class allowance, settles a new seed prime, or proves FIN, ORDER9, or Q36. The most useful new positive construction is an explicit relative class-number reconstruction certificate. It is a sufficient certificate with missing arithmetic inputs, not an executable demonstrated path to completion.

This review reads the new arguments and reimplements selected exact numerical and finite-algebra checks. It is not an independent human review, a proof-assistant verification, a full replay of number-field ideal arithmetic, or an audit of all historical evidence.

## Snapshots

- Private lab substantive continuation: `1c782871e9b26787b6cd1909ee37bafe947b0a69`, branch `research/state-sync-2026-10-04`. Three commits beyond `ceadfa43c5543cf5efd75d0ed72cad5728d6e7cc`.
- Previous experiment branch: `b204bbf582cf5cdfc081c7f93ddb9e0bc5976444`, unchanged when read.
- Public edition main: `c110d899d215c5caf2c0dcc058a5ad896199f47d`.
- Public release tag `evidence-2026-10-22`: `f08cdfb3743b0e2a04443ad4a88c9d51d05a1bc6`. Main is one commit ahead and includes the joint-class continuation absent from the tagged snapshot.
- Private research release v0.2.6: `8414aea58180f3a18bcee7fba23475c8cac90996`; status supplement `9ebaca3b80adfd4a18e77eebe23c9db3bc201448` is dated October 4. No new release theorem identified.
- Separate `bsd-seed-sha3-note`: `fded6828978017b9f83b7d4abef0307736c441ad`, dated September 30. It repackages the established 3-primary chain; it is not a newly completed ORDER9 result.

## 1. Direct primary-torsion packing

The construction works with the full norm-one ideal/divisor group, not a selected list of classes. It retains the possibly multi-dimensional 2-primary norm-unit error. The volume accounting cancels its index against the relative regulator index, and small split-prime pairs yield a direct bound on the full relative five-torsion dimension.

The two norm windows have strict integer cutoffs 15 and 242. The repository's field arithmetic reports two eligible norm-7 pairs in the narrower window and 26 pairs in the wider window. Those actual ideal counts were not regenerated here.

I independently evaluated the rational separation and volume inequalities at all thirteen published radii. The resulting rank ceilings are:

`106, 131, 132, 142, 146, 147, 155, 159, 160, 161, 164, 168, 168`.

At the best radius `6889807/16777216`, the exact upper integer reproduces:

`334809554342956104676612913920139327331389754537007507521626340458250851040 < 5^107`.

This gives dimension at most 106, not total five-primary length at most 106. The earlier length bound 97 already implies a stronger dimension bound. The operative allowance therefore remains 97, with the conservative full-source ceiling 100.

The across-prime argument is correctly limited to the selected analytic majorant, radius certificate and norm window. Its lower bound on the *upper-bound expression* does not lower-bound actual class groups. Increasing only the admitted prime count within that budget cannot yield the desired source ceiling three.

## 2. Seven actual S-units and the parity exclusion

The new packet authenticates seven torsion-coordinate S-units and fourteen fifth-power identities for their two faithful scalar projections. I reviewed the parity argument and independently checked the two monomial identities. I did not rerun their maximal-order ideal reconstruction.

If tau(a)/a is a sign, then [a] is tau-even modulo odd powers. It cannot contribute to a scalar character on which tau acts as minus one. The argument also covers multiplicative scalar combinations and saturation by roots that remain in the same real-embedded field. It does not cover arbitrary additional structures, field extensions, or all possible unit sources.

The arithmetic change is real: these elements pass support admission, unlike the prior Cayley sources. The reason they fail is their character projection, not a new discovery that all small-support sources fail.

## 3. Orbit-weighted incidence maps

For nonzero vector/covector sets with full GL2 action, the orbits are the values of lambda(v). On a nontrivial homogeneous scalar character, N_0=0 and N_t=chi(t)N_1 for nonzero t. Thus this entire orbit-correspondence family supplies no independent class-kernel constraint beyond the existing incidence map.

I rebuilt the finite matrices independently modulo p^2 at p=3,5,7,11,13 and checked the scalar identities, orbit cardinalities and degree-one-character ranks p-1. This supports the implementation. The written orbit argument supplies the all-p statement; the finite tests are not its proof.

## 4. Complete-presentation error

The snake-lemma accounting is valid for authenticated finite p-group presentations:

`d_p ker(u) <= d_p ker(U) + d_p(K_B/U(K_A))`.

An exact target p-presentation with a complete source surjection is enough; the complete source class number is unnecessary. In contrast, an invertible selected matrix can hide a large genuine class kernel in the target relation error. Integral presentations matter: a surjection Z/p^2 -> Z/p is not surjective on p-torsion. I separately checked this counterexample at the finite primes above.

This is useful certificate design, not new arithmetic control of the seed's target error.

## 5. Relative analytic reconstruction

The new certificate uses the actual rank-six relative norm-one unit group. If E0 has index j and covolume V0, while I is the power-of-two index with I<=128, then

`t = T/(64 V0) = h_rel/(I j)`.

If the unit subgroup is independently five-saturated, `v5(t)=v5(h_rel)`. More generally, a bound `v5(j)<=a` gives the upper allowance `v5(h_rel)<=v5(t)+a`. This avoids class-presentation generator/relation cancellation. It does not use the elliptic BSD formula.

The required independent inputs remain absent: six suitable relative units with adequate index control, and a certified two-sided number-field L-value enclosure. Three units in one character component do not certify the full rank-six index.

I reproduced the stated sufficient precision policy exactly: for hypothetical J=1,10^6,10^12,10^24, the requirements are 236,276,316,396 bits (72,84,96,120 decimal digits). The scheme's optimistic absolute L-interval gate is less than `9.034615265876167e-53`, hence less than `9.1e-53`.

These are scheme-specific precision statements, not runtime guarantees or lower bounds on all possible algorithms. A successful p=5 reconstruction would still be a fixed-prime class result at a seed prime already settled by a separate method. It would not give the cofinite FIN estimate without further arguments.

## 6. Public evidence and release mismatch

Public main reports 114 dossiers, 12,290 source records and a 12,301-entry public manifest check. I read these publication records; I did not independently download and hash the entire public corpus.

The tagged release still contains the earlier 113-dossier snapshot. Its attached ZIP is the primary-torsion packet plus the preceding experiment input, not the entire public edition, and not the later joint-class continuation. Reviewers needing the latest continuation should use the pinned public main snapshot or a newly prepared successor release. No tag, branch, or file was modified in this review.

## Source locations

All lab paths below are pinned to `1c782871e9b26787b6cd1909ee37bafe947b0a69`:

- `work/returns/BSD_PRIMARY_TORSION_BOUND_2026-10-22/REPORT.md`
- `.../theory/EXPLICIT_PRIMARY_PACKING.md`
- `.../theory/PRIMARY_PACKING_RESULT.json`
- `.../theory/RETAINED_ANALYTIC_INPUT.json`
- `.../theory/SCALING_LIMIT.md`
- `.../review/independent_primary_packing_check.py`
- `.../review/PRO_PACKET_REVIEW.md`
- `work/returns/BSD_JOINT_CLASS_CONTINUATION_2026-10-22/REPORT.md`
- `.../arithmetic/PROOF.md`
- `.../theory/HISTORICAL_AND_OPERATOR_SCREEN.md`
- `.../sources/PRESENTATION_DEFECT.md`
- `.../sources/RELATIVE_RECONSTRUCTION.md`
- `.../sources/PRIMARY_SOURCE_ADMISSION.md`
- `.../review/RELATIVE_RECONSTRUCTION_REVIEW.md`

Primary-source statement checks included BFHP, *Norm relations and computational problems in number fields*, arXiv:2002.12332v4, especially Propositions 4.6, 4.8 and 4.28, and Hofmann–Johnston, *Algorithms for p-rationality and for p-saturation of units*, arXiv:2609.15190v1, especially the regulator/index framework of Algorithm 14.1. Those sources do not supply the missing seed units or analytic values. The fast unramified-prime shortcut must not be silently applied at the ramified prime five.

## Replay this review's checks

```
python3 check_numeric_claims.py
python3 check_algebra_claims.py
```

Python standard library only. These scripts use explicitly transcribed, pinned source values and independently implemented formulas; they are not byte-for-byte copies of the repository's checkers. Neither script accesses a network or performs a class-group calculation.
