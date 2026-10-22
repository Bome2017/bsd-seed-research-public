# Follow-up review: the two Kato returns and the completed p=37/41 tests

Date: 2026-09-27. Read-only review of the two supplied ZIPs, the pinned Kato RESULT on GitHub, and selected primary-source statements. No production run, repository edit, cloud job, or successor was launched.

## Disposition

- **Kato/E11:** retain the determinant leading-term lemma and its corrected Selmer realization at the explicitly stated written/imported-input grade. Retain Codex's F1–F5 corrections. No new blocking flaw was found in this targeted reading; this is not a fresh proof of all the imported arithmetic theorems.
- **p=41, l=83:** ACCEPT_WITH_REPLAY_LIMITS at the retained Ota/lattice/corpus grade.
- **p=37, l=149:** ACCEPT_WITH_REPLAY_LIMITS at the same grade. This is a completed result in the newer two-test ZIP, not the pending run described by the older dual-audit snapshot.
- **Global target:** no prime-uniform bound, FIN, ORDER9 or Q36 has been obtained. The categorical claim that no property of Kato's element can ever control the witnesses is not established by the factorization or its countermodels.

## 1. Inputs and integrity

The supplied archives were checked for duplicate paths, unsafe traversal paths and symbolic-link entries before extraction. No such entries were found.

| Input | SHA-256 | Manifest |
|---|---|---|
| BSD_KATO_DUAL_RETURN_AUDIT_CODEX_2026-09-26.zip | bd8e0558ba76379c9e139a68c5c6890f5daf062e87b7682907b5b75825777f6b | 69/69 |
| BSD_TWO_TESTS_P41_P37_2026-09-27.zip | 9fae7f08465585588dbdf21328a4fd3036495d2fe530fbe93cb77648c5765845 | 28/28 |

Both root manifests cover precisely every payload file except themselves. The nested Kato and E11 manifests pass 11/11 and 12/12 respectively. All input hashes still pass after execution of the checks.

The GitHub connector fetched work/kato/RESULT.md at commit 9f7c6e548da178cd64d1eeb232f2e2f9399dff50. Its Git blob hash, 58ec5997f4dc93b01170d87f636bc82e7548fc32, matches the supplied snapshot. This confirms that specific pinned file, not every current branch or working tree.

## 2. The two numerical results

The independent implementation in code/independent_checks.py does not call the frozen checker or a supplied recomputation routine. It identifies the unique 1/1024-lattice point in each printed interval by exact rational endpoint comparisons, then compares it to the declared point. It parses every label exactly once, checks both symmetries, traverses powers of primitive roots directly, and evaluates the binomial moments.

| p | l | plus/minus intervals | c0 | c1 | c2 | c2 mod p |
|---|---|---:|---:|---:|---:|---:|
| 41 | 83 | 164 | 0 | -5904 | -83420 | 15 |
| 37 | 149 | 296 | 0 | 28860 | 762756 | 1 |

Both count identities, segment alignment, output hashes, PARAMS strings, prediction-file hashes and available freeze-file bindings agree. Eight referenced frozen files per run could be checked from these two ZIPs. Twenty-four additional files per freeze are absent; their hashes were not converted into a claim of fresh verification. The common checker bytes match the hash named by both freeze manifests.

Direct finite-field counting, using Legendre symbols rather than the supplied root-multiplicity code, gives:

    #E(F_41)=36, #E(F_83)=92,
    #E(F_37)=28, #E(F_149)=160.

Thus a_41=6 and a_37=10; both p are good ordinary, subject to the retained conductor. Their auxiliary primes satisfy v_p(l-1)=1 and have no p-torsion in the reduction group. The determinant-freezing/theorem dependencies still include the retained rank, residual surjectivity, Manin/period lattice and valid numerical enclosures.

All 40 primitive roots modulo 83 and all 72 modulo 149 satisfy the expected degree-two covariance. This is a relabeling consistency test, not an independent authentication of the symbols.

The largest printed interval width is 0.249856 lattice spacings in both runs. These are well inside the one-point identification margin. The check establishes uniqueness for the supplied intervals; it does not establish that the large Fourier computations originally produced valid enclosures.

### Tame side independently recomputed

code/tame_pairing_checks.py uses newly written rational elliptic-curve arithmetic on the minimal model and the retained formula ind_g(-a/b). It does not import the GP script or any supplied arithmetic-check module.

    p=41, l=83, M=92:
       H(ME) = [[32,4],[4,34]], det=6, R=19 mod 41;
       (-92)*288*19 = 15 mod 41.

    p=37, l=149, M=80:
       H(ME) = [[33,30],[30,26]], det=32, R=32 mod 37;
       (-160)*288*32 = 1 mod 37.

Both quadraticity and parallelogram checks pass. The tame pairings are independently calculated; the relation to c2 with the fitted constant 288 remains a diagnostic, not an imported theorem.

### Chronology and consequences

The common forecast hash is 4853a5fbdb0a6a16a63c13681a010f19d47d7e439c493c565988372b51396ffd. Both freeze manifests report 04:29:25Z. The run starts are 04:29:32Z for 41 and 04:53:42Z for 37. The records therefore support the claimed pre-run chronology at the custodian-attested grade; they are not external timestamps.

Ota, Theorem 6.4 (printed p.37), yields Sha[p]=0 from the nonzero leading term under its hypotheses. A nonzero element of p-power order would have a nonzero multiple of order p, so the entire primary group vanishes. The two primary-vanishing claims survive this targeted downstream audit.

The old bound is unchanged: with 31 unresolved, the retained primary data imply, conditional on finiteness, #Sha=9 or #Sha>=8649. Adding 37 and 41 does not close the 31 gap. If the six observed multiplier residues are represented by a common integer K, they impose K=288 modulo 326823997=17*19*23*29*37*41. They do not establish such a global integer or equality K=288.

No coefficient corpus, coefficient witness files, per-segment receipts, engine binary, or full acceptance fixtures were supplied here. These checks are not a full original-engine/corpus replay.

## 3. Corrected determinant theorem

Let

    P_K = {primes outside {2,3,5,19,59,487,2243,4547,5843}}.

For p in P_K, take a squarefree conductor m whose prime divisors l satisfy

    l does not divide pN, l=1 mod p, p does not divide #E(F_l).

Let F be the corresponding abelian p-extension, R=Z_p[Gal(F/Q)], and I its augmentation ideal. Define

    s_p = rank_Zp H^1_f(Q,T_pE)
        = 2 + corank_Zp Sha(E/Q)[p^infinity],
    A_p = H^2_f(Q,T_pE)_tors.

The duality identification retained in the source is

    A_p ~= (Sha[p^infinity]/Div)^vee.

Let x_{Q,Sigma} be the coordinate of the determinantal Kato element in its specified integral determinant line. The Sigma label must be retained unless the separately graded auxiliary-compatibility result is invoked.

The corrected statement is:

1. If s_p>2, the degree-two witness t_{p,m} is zero.
2. If s_p=2, primary Sha is finite, |A_p|=|Sha[p^infinity]|, and

       t_{p,m}=u_{p,m} x_{Q,Sigma} |A_p| det(B_m) in I^2/I^3,
       u_{p,m} in Z_p^times.

The Bockstein-to-Mazur–Tate identification is an arithmetic import and is not replaced by a numerical match. This casewise statement makes no global FIN assumption. The finite-case use of |Sha[p^infinity]| is not an assumption of its value.

The extra exclusions are necessary for the cited BKS hypotheses: the good nonsingular-order factors at bad places have product

    2*4*2242*4547*5844 = 2^6*3*19*59*487*4547.

Consequently, the accepted p=19 Ota certificate cannot be fed into this particular BKS comparison. The p=37 and p=41 results can, at its import grade.

### Elementary proof of the determinant identity

Given a square presentation matrix Psi over R, its augmentation can be put into Smith form by integral changes of basis. If the augmented kernel has rank s, choose the s zero columns last. Each determinant term then has at least s augmentation factors. Modulo I^(s+1), the only surviving terms use the nonzero constant Smith pivots and the linear s-by-s complementary minor. The pivot product is |A|, up to a unit, and that minor is the free-quotient Bockstein determinant. This argument never divides by a nonunit pivot.

This proves the algebraic lemma for the stated presentation data. The transfer to arithmetic uses the BKS determinant map, derived base change, and the retained Selmer duality. These are named imports, not silently new formal proofs.

## 4. Substantive corrections

### 4.1 Finite quotient depth is not capped valuation

For a singleton quotient M=Z/p^k, primitive e, and u a p-unit,

    depth_M(p^v*u*e) = v,        v<k;
                        infinity, v>=k.

Zero has infinite depth under the project's definition. The original min(k,v) is a numerical cap, not that depth. If the regulator is nonprimitive its depth is added before imposing the zero case.

For example Psi=diag(p,p,T,T) has formal leading coefficient p^2. Its degree-two class in Z_p[C_p] is zero, since I^2/I^3 is killed by p, not a nonzero depth-2 witness. In a cyclic order-p^3 quotient the corresponding primitive case has depth 2. The 78 successful model checks do not certify the erroneous finite-depth interpretation.

### 4.2 Finite-part torsion does not control corank

A putative bound on |A_p| alone omits the divisible-primary part. The formal complex with differential T*Id_4 has torsion-free augmented H^2, unit determinant coordinate, determinant T^4, and zero degree-two witness. Its augmented cohomology rank is four, not two.

This is a counterexample to the abstract implication used in the summary, not an elliptic-curve counterexample. The corrected large-prime target includes s_p=2, A_p=0 and unit x_{Q,Sigma}; controlling A_p alone is insufficient.

### 4.3 Kato specialization can vanish

At supersingular primes, no relevant global IMC is supplied in the packet. An integral Iwasawa element can specialize to zero; f(T)=T illustrates the issue. Finite primary Sha alone does not exclude x_Q=0 from the listed premises.

At good ordinary p, the unit-coordinate statement retains the exact characteristic-ideal equality and its determinant translation. I reviewed that translation but did not reprove the arithmetic main conjecture or every hypothesis in its seed application.

### 4.4 The repaired Ota–Darmon comparison is integral

For a prime l|m, let L_l=p^v_p(l-1), N_l=sum_{g in G_l}g, c_l=(l-1)/L_l, and h_l be Frobenius in the complementary factor. Set

    A_l=a_l-h_l-h_l^-1,
    D_l=a_l-l*h_l-h_l^-1,
    V_l=1-c_l*N_l*h_l*A_l^-1.

The no-p-torsion condition makes A_l,D_l units, and

    V_l^-1=1+c_l*N_l*h_l*D_l^-1.

Indeed N_l^2=L_l*N_l and D_l=A_l-c_l*L_l*h_l cancel the product error. The character evaluations yield theta_Darmon=(product_l V_l)theta_Ota in the matching period convention. The element V_l has unit augmentation and preserves graded vanishing/depth. This is a comparison up to an explicitly constructed unit, not equality of the two original elements.

The proof needs p not dividing #E(F_l). It has not been extended here to Kolyvagin-type auxiliaries with nontrivial p-torsion.

### 4.5 Factorization is not arithmetic independence

The sentence in the original cloud return that no property of the Kato element can control the Selmer factor does not follow. A factorization identifies factors; it does not prove all arithmetic constraints involving them are independent.

A genuinely independent bound or nonvanishing theorem for the actual image could use the factorization to constrain the Selmer factor. The countermodels show only that the listed integrality, primitivity and perfect-complex data do not supply that extra control. They do not satisfy every asserted arithmetic/Euler-system property of this seed.

The corrected global-lattice lemma likewise requires primary finiteness throughout its domain; assigning standard lattices to unspecified primes cannot establish that omitted condition.

## 5. What is new and what is not

The cloud construction gives an actual determinant realization preceding the Mordell–Weil identification, and an explicit rank/torsion leading-term rule. This is more than a renamed demand for FIN, but no novelty relative to the literature is asserted.

It also allows each accepted nonzero degree-p witness in the BKS scope to certify that its relevant Sigma-specific integral determinantal Kato element is primitive. This includes the previously accepted supersingular witnesses at 23 and 29 and, now, ordinary 37 and 41. It does not prove the Iwasawa main conjecture at every supersingular prime, and it does not glue these local elements across p.

The two local tests are finished. Their 8.61 CPU-hour total and no-new-paid-compute statement are retained execution claims, not a benchmark performed here. Their additional arithmetic outcomes are independent of the cloud attempt's failure to get a uniform bound.

## 6. Primary sources checked and review limits

[1] David Burns, Masato Kurihara, Takamichi Sano, On derivatives of Kato's Euler system and the Mazur–Tate conjecture, arXiv:2103.11535v1.
    https://arxiv.org/html/2103.11535v1
    https://arxiv.org/pdf/2103.11535v1

    Checked: Hypothesis 2.2 (no ordinarity clause); Lemma 4.2 and Definition 4.3; Proposition 5.2 and Corollary 5.3; the initial derived-base-change and Bockstein construction of section 5.3; the distinction from the later Mordell–Weil realization; and Lemma 5.5's cancellation of the p-factor.
    The PDF has Corollary 5.3 on printed p.21 and Lemma 5.5 on p.23. HTML and PDF equation numbering differs, so theorem/section labels are used rather than silently mixing equation numbers.
    The web renderer successfully displayed PDF p.21. Screenshot requests for pp.19,22,23 failed with cache misses; these portions were checked in parsed/HTML text instead. Direct container download failed because network name resolution was unavailable.

[2] Kazuto Ota, Kato's Euler system and the Mazur–Tate refined conjecture of BSD type, arXiv:1509.00682v1.
    https://arxiv.org/pdf/1509.00682

    Checked: Proposition 2.3 (printed p.5), its primitive-character interpolation and imprimitive factors; Theorem 6.4 (printed p.37) for the accepted leading-term implication. All retained seed hypotheses were not independently reconstructed in this follow-up.

Not re-proved here: Kataoka's underlying Euler/Stark-system inputs, arithmetic Selmer duality, Burns–Macias Castillo's full biextension/Bockstein theorem, the main conjecture, the all-odd residual-image theorem, lattice membership, or the original Fourier coefficients and their numerical enclosures.

## 7. Reproduction and files

Extract each original user ZIP under inputs/<archive-stem>/; each archive contains its own top-level folder, as reflected in the scripts. Then execute:

    python -B code/independent_checks.py
    python -B code/tame_pairing_checks.py

The first script uses Python's standard library plus SymPy for a single symbolic identity. The tame pairing script uses only the standard library and caps its own CPU use at 40 seconds. Original source checks were read first and replayed in disposable copies, never in the preserved inputs. Their outputs and comparisons are under results/replay/ and results/replay_summary.json.

No artifacts were promoted to the expert release and no new task was launched.
