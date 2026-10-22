# Two-prime Heegner allowance and the fixed rank-one twist

Grade: written deduction from the matched ordinary theorem and retained seed/twist inputs. No new Selmer computation, literature-novelty claim, or Lean verification.

Fix p>=5, p not dividing 23N, with good ordinary reduction. Use the primitive residual Heegner system for K=Q(sqrt(-23)) in the domain matched by the preceding review. Write nu for its first nonzero residual length. Zhang's nonvanishing theorem supplies finiteness of nu under those hypotheses; arbitrary rescalings of the system by p are not permitted.

The project retains rank E(Q)=2, rank E^(-23)(Q)=1, and no relevant rational p-torsion. Quadratic restriction/descent, since 2 is a p-unit, identifies the two eigenspaces of Sel_p(E/K) with the two rational Selmer groups. If s=dim Sha(E/Q)[p] and t=dim Sha(E^(-23)/Q)[p], their dimensions are

    d_+ = 2+s,   d_- = 1+t.

The source lemma, [Wei Zhang, Lemma 8.4](https://math.mit.edu/~wz2113/math/online/Kconj.pdf), and the matched sign give

    d_epsilon = nu+1,   d_opposite <= nu,
    epsilon = (-1)^(nu+1).

Consequently max(d_+,d_-)=nu+1, proving the exact formula in the report. In particular nu=0 is impossible because it would require d_+<=0. If nu=1 then d_+=2, so s=0. If nu=2 then d_+<=2 and d_-=3, so s=0 and t=2. This proves the proposed sufficient criterion without asserting that any length-two class has actually been evaluated.

The retained twist certificate has L'(E^(-23),1) in [39.512236,40.182321] and root number -1. Its retained Gross–Zagier–Kolyvagin consequence includes finiteness of the twist's Sha. The exact input is recorded in the supplied FULL_COMPENDIUM.md, units E4a-005 and E6-030, and in BSD_ARISTOTLE_TAIL_COMPRESSION_2026-09-22/unpacked/INPUTS.md. This review uses that input at its retained grade; it does not rerun the analytic certificate.

Let S_tw be the prime support of that finite twist Sha. For p outside S_tw in the above ordinary domain, t=0. Since d_+>=2>d_-=1, the maximum formula gives nu=1+s. The retained evenness of s then proves

    nu<=2 iff s=0 iff nu=1.

The finite set S_tw need not have been explicitly computed for this cofinite deduction. It is not a fixed annihilator for the seed's Sha. It merely locates the extra nu=2 case in the twist's finite exceptional support.

The conclusion is about the target's logical strength. An independent theorem proving nu=1, or controlling the actual Heegner classes, could still solve the ordinary tail. The equivalence does not prove such an approach circular or impossible; it shows that changing the numerical threshold alone supplies no independent upper control.
