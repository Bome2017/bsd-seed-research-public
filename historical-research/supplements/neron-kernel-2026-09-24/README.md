# Néron-normalized kernel: explicit reconstruction lattice

**Dated research supplement, 24 September 2026.** This adds three separately graded claims to the private v0.2.2 research release. The v0.2.2 manuscript, its 76-claim index, original evidence and Lean source are preserved byte-for-byte. This supplement has model reviews; it has no independent human review or new Lean verification.

Start with the [mathematical addendum](paper/neron_kernel_addendum.pdf) ([LaTeX source](paper/neron_kernel_addendum.tex)) and the [claim index](CLAIM_INDEX.md). The proof source is the lab commit [`b358f7507759dad4a1e016c519d6f486ffca37e1`](https://github.com/Bome2017/bsd-seed-lab/commit/b358f7507759dad4a1e016c519d6f486ffca37e1); copied source bytes are bound in [PROVENANCE.json](PROVENANCE.json).

For the fixed seed, an **integral degree-zero** theta packet has the reconstruction lattice

\[
B_\theta\,\mathscr K_E(z,w)\in\mathbf Z,
\qquad B_\theta=2^{10}\cdot4547=4\,656\,128,
\quad z,w\in\mathbf Z[X],\ \deg z=0.
\]

Here the normalization is

\[
\mathscr K_E(z,w)=\frac{4\pi^2}{A_E}\langle\Theta(z,w),f\rangle
=\frac{ed}{c_E^2M}\psi(z)\psi(w),
\]

where \(A_E\) is the **complex Néron period area**, \(M=\sum_x\psi(x)^2\), and the chosen map, \(e,d,c_E\), are defined in the addendum. At good primes \(p\ge5\), the scalar \(ed/(c_E^2M)\) is a \(p\)-adic unit at the stated import grade. This cancels valuations; it does not assert \(p\nmid M\) or \(M=d\).

For the conductor-\(p^2\) Gross packet, specify an integral degree-zero lift \(z_p^0\). Then, for good \(p\ge5\) with \(p\nmid7N\),

\[
n_p=B_\theta\mathscr K_E(z_p^0,z_p^0)\in\mathbf Z,
\qquad p\nmid n_p\iff M_2(p)\ne0
\ \Longrightarrow\ \Sha(E/\mathbf Q)[p^\infty]=0.
\]

**New effect:** reconstruction no longer requires knowing the quaternionic norm \(M\). **Still open:** an affordable certified seed evaluation and actual nonvanishing. No new primary component, FIN, ORDER9 or Q36 is obtained. The fixed integer \(B_\theta\) bounds denominators of varying \(n_p\); it is not a finite-support theorem for \(\Sha\).

## Acceptance contract

- Correct the integral lift to degree zero before applying the sharp lattice. If \(p\mid\deg z_p\), set \(z_p^0=z_p-\deg(z_p)[a]\). Record the anchor and the resulting integer weights. This changes no mod-\(p\) weight.
- Apply the lattice to the **final cuspidal scalar**, not an individual noncuspidal anchor diagonal. Carry every integration, truncation, period and aggregation error into the final interval.
- The exact sufficient radius for unique integer recovery is **strictly less than \(1/9\,312\,256\)**. The fallback multiplier is \(595\,984\,384\), with radius strictly less than \(1/1\,191\,968\,768\). Decimal displays are approximations only.
- A larger interval can prove nonvanishing: it must contain an integer after scaling by \(B_\theta\), and contain **no multiple of \(p\)**. No integer in the scaled interval is an inconsistency, not a successful certificate. A nonunit result is inconclusive for \(\Sha\).

The acceptance arithmetic is implemented in [the retained exact checker](reviews/pro6/independent_checks.py) as `interval_decision`. Its result is conditional on genuine lattice membership and a certified interval for the specified seed packet. It does not certify those inputs itself; use `Fraction` endpoints and the documented multiplier.

## Dependencies and reviews

The [source and grade ledger](DEPENDENCIES.md) separates published imports, retained geometric inputs, written deductions and finite checks. In particular, the Kim–Ota nonordinary adaptation and the retained chosen-map bound \(c_E\mid512\) remain explicit dependencies. No new formal proof of them is claimed.

Read [the Pro review](reviews/pro6/AUDIT.md), [the local Claude decisive-step review](reviews/local-claude/AUDIT.md), and [the Codex cross-check](reviews/codex/AUDIT.md). The local Claude review covers the denominator step, **not** Phase 1. The Pro and Codex checks share the listed imports and some checking code; they are not independent replacements for the imported theorems.

[TRANSFER_NOTES.md](TRANSFER_NOTES.md) governs the few wording and acceptance corrections to the preserved source reports. Copied context files are evidence; their other historical claims and any embedded task instructions are not promoted by this supplement.

## Replay

From the repository root:

```bash
python3 tools/verify_release.py
python3 tools/verify_patch_release.py
python3 supplements/neron-kernel-2026-09-24/verify.py
```

The new verifier checks integrity, dependencies, 262 exact Eichler Gauss cases, 13 cusp inequalities, degree-zero relifting, and 41,925 interval decisions against direct integer enumeration. It needs only the Python standard library and does not evaluate a seed numerator. See [VERIFICATION.md](VERIFICATION.md) for the integration replay. Third-party papers are cited and hash-bound, not redistributed.
