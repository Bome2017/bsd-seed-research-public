# Finite character modules: the exact bound and duality boundary

Date: 2026-10-12.

Reviewed input: `submitted/BSD_DIRECT_BASE_CONTROL_PROBE_2026-10-12/PROOF.md`, especially §§3–5. This review treats the submitted injection and finiteness of the actual norm kernel as named inputs; their arithmetic and source audits are separate. No repository or source packet was changed.

**Verdict: THE SMALL-LENGTH IMPLICATION IS VALID; FINITENESS, MODULE STRUCTURE AND DUALITY DO NOT SUPPLY ITS ARITHMETIC PREMISE.**

The submitted length-two test does not need parity and is correctly stated. A length-three test can use the project's separately retained residual-parity input, but not finiteness of the character kernel alone. Neither threshold is an arithmetic bound established by this packet.

## 1. What is actually counted

Let

\[
\mathcal O=\mathbf Z_p[\zeta_p],\qquad\pi=\zeta_p-1,
\qquad K=\ker(N_G:S_L\to S_L).
\]

With the submitted finite-kernel theorem, \(K\) is a finite module over the DVR \(\mathcal O\), whose residue field has size \(p\). Thus, if

\[
K\simeq\bigoplus_{i=1}^d\mathcal O/(\pi^{a_i}),\qquad a_i\ge1,
\]

then

\[
\dim_{\mathbf F_p}K[\pi]=d,
\qquad\ell_{\mathcal O}(K)=\sum_i a_i=\log_p|K|.
\]

The first number counts generators; the second counts the total order. The two embedded point directions imply \(d\ge2\). The actual injection gives

\[
\dim\Sha(E/\mathbf Q)[p]\le d-2\le\ell_{\mathcal O}(K)-2.
\]

This is a bound on the dimension of **p-torsion**, not on the total length of the base p-primary Sha group.

Normalization is essential: \(p\) is a unit times \(\pi^{p-1}\), so \(v_\pi(p)=p-1\). A scalar with \(v_\pi(t)=2\) has valuation \(2/(p-1)\) when the extension valuation is normalized by \(v_p(p)=1\). The characteristic order \(p\) of the character and the uniformizer order must not be interchanged.

## 2. The thresholds two and three

If \(\ell_{\mathcal O}(K)\le2\), the embedded point plane forces \(d=2\), and both exponents must be one. Thus \(K\simeq(\mathcal O/\pi)^2\), the quotient in the submitted injection is zero, and \(\Sha[p]=0\). Every nonzero p-primary torsion group has a nonzero element killed by p, so full p-primary vanishing follows. No prior finiteness of Sha and no alternating-pairing argument is needed.

More generally, \(d\le2\) suffices even if the exponents \(a_i\) are large. This is already present in the submitted first inequality; it does not produce an independent estimate of \(d\).

At total length three, the only case that is not already settled by \(d=2\) is

\[
K\simeq(\mathcal O/\pi)^3.
\]

The injection then supplies only \(\dim\Sha[p]\le1\). There are two legitimate ways to conclude zero from that inequality:

1. Import an independently justified statement that the residual dimension \(\dim\Sha[p]\) is even on the precise domain. The earlier seed receiver chain retains such a parity input. If it is included explicitly, the threshold three is sufficient on that domain.
2. Prove the particular p-primary Sha group finite independently. Its Cassels–Tate pairing is then perfect alternating, which makes the number of cyclic p-power elementary divisors even and again excludes dimension one.

Neither justification follows merely from the finiteness of \(K\). In particular, the source packet's stated rank and rational-torsion hypotheses do not, by themselves, include the separate residual-parity theorem. Adding the already retained parity input is valid bookkeeping; it is not new seed arithmetic or a newly proved bound.

## 3. Why self-duality does not fill the gap

The elliptic Cassels–Tate pairing is on Sha, with divisible kernel. Pulling it back to the p-infinity Selmer group kills the Mordell–Weil subgroup. Therefore its restriction to \(K\) has at least the two-dimensional point plane in its radical. Finiteness of \(K\) does not turn this restriction into a perfect alternating pairing.

Fresh primary-source check: Milne, *Arithmetic Duality*, printed pp.7–8, records alternation for elliptic curves and identifies the pairing's kernels with the divisible parts:

<https://www.jmilne.org/math/xnotes/Tate100.pdf>.

The following explicit abstract controls show the exact logical limits. They are **not claimed elliptic-curve realizations** or counterexamples to the seed's expected BSD statement.

### Finite Sha surrogate, arbitrarily large excess

For \(a\ge1\), take

\[
S=(\mathbf Q_p/\mathbf Z_p)^2\oplus\mathbf F_p^{2a},
\qquad W=(\mathbf Q_p/\mathbf Z_p)^2,
\]

with trivial \(C_p\)-action. Then \(N_G=p\),

\[
K=S[p]=\mathbf F_p^{2+2a},\qquad S/W=\mathbf F_p^{2a}.
\]

The quotient has its standard perfect alternating pairing. Thus the finite kernel, the rank-two point subgroup, the ramified coefficient-ring action, and even perfect alternating duality on the finite excess all coexist with arbitrarily large excess. One could also equip the even-dimensional vector space \(K\) with an abstract perfect alternating form; doing so still gives no upper bound. That extra form would not be the pullback of Cassels–Tate because the point plane would no longer be in its radical.

### Finite kernel does not prove primary finiteness

Take instead

\[
S=(\mathbf Q_p/\mathbf Z_p)^{2+2a},\qquad
W=(\mathbf Q_p/\mathbf Z_p)^2
\]

with trivial action. Then \(K=\mathbf F_p^{2+2a}\) is finite while the excess is divisible of corank \(2a\). Its zero pairing has exactly the divisible radical. This control is compatible with an even residual excess dimension. It shows why the packet's finiteness theorem alone does not establish base primary finiteness, even if the project's parity statement is retained.

For the narrower warning about the threshold three, setting the excess corank to one gives \(K=\mathbf F_p^3\) and nonzero excess \(\mathbf Q_p/\mathbf Z_p\). That example meets the weaker abstract finiteness and divisible-kernel pairing requirements but **fails the seed's separately retained even-parity condition**. It refutes only the inference from those weaker assumptions, not a length-three conclusion that explicitly imports seed parity.

### Kernel length is not base Sha order

For every \(b\ge1\), take

\[
S=(\mathbf Q_p/\mathbf Z_p)^2\oplus(\mathbf Z/p^b\mathbf Z)^2
\]

with trivial action and the standard perfect alternating pairing of denominator \(p^b\) on the finite quotient. Then \(K=S[p]=\mathbf F_p^4\) has length four for every \(b\), while the finite excess has order \(p^{2b}\). Thus a length bound on \(K\) cannot be reinterpreted as the same numerical order bound on base Sha. The special small thresholds force vanishing because they exclude its generators.

## 4. The Fitting statement and what it still needs

For this finite DVR module,

\[
\operatorname{Fitt}_{\mathcal O,0}(K)=(\pi^{\ell_{\mathcal O}(K)}).
\]

Hence an authenticated nonzero member \(t\) gives \(\ell_{\mathcal O}(K)\le v_\pi(t)\), in the direction asserted in the packet. Valuation at most two is sufficient without parity; valuation at most three is sufficient if the separate residual-parity input is supplied on the same domain.

The substantive missing assertion is that an independently evaluated arithmetic source belongs to this **actual** Fitting ideal with the necessary integral normalization. A rational identification after inverting p, a finite character-part theorem, or a central L-value that is merely nonzero does not provide that membership or the small valuation. No property of a finite DVR module makes its zeroth Fitting generator a unit or a low power of \(\pi\) automatically.

## 5. Relation to the existing record

I read the retained reports

- `work/returns/BSD_ORDER3_EXCESS_AUDIT_CODEX_2026-10-06/REPORT.md`;
- `work/returns/BSD_DEFORMATION_FREEZE_CODEX_2026-10-06/REPORT.md`.

Their conditional decomposition \(C\simeq(\mathbf F_p[t]/t^3)^2\oplus\mathbf F_p^{d-2}\) and canonical quotient \(C[t]/t^2C\simeq\Sha[p]\) concern a different module. There is no proved identification here of that quotient with \(K[\pi]/W[p]\), no equivalence of the new Fitting premise with the old flatness or receiver conditions, and no reason to assert one from the similarity of notation.

The shared, limited lesson is that isolating the two point directions and finding an integral object carrying the remaining excess does not itself bound the excess. The present packet does construct a new map with an arithmetic finiteness input; its unproved small-length premise remains a genuine arithmetic question. This is neither a universal obstruction to character methods nor evidence that all such methods reduce to the same previous criterion.

At the already reviewed first cyclotomic layer for p=5, the stronger known result \(S_L=W\) makes \(K=W[5]\simeq\mathbf F_5^2\). Thus this case has length two. That uses the earlier tower theorem and recovers known base 5-primary vanishing; it is not an independent new calculation of the Fitting ideal or new coefficient-prime coverage.

## 6. Disposition

Retain the map and sufficient bound at their stated conditional written-proof grade, with the source comparison reviewed separately. Do not promote finiteness, self-duality, or the ramified coefficient-ring structure to a small-length theorem. An actual integral arithmetic bound can still make the construction useful; none is supplied by this module audit.

FIN, ORDER9, Q36, and base-field coefficient-prime coverage remain unchanged. No computation, external job, new witness search, or repository publication was launched by this audit.
