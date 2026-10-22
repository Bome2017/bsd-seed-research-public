# Nineteenth addendum — custody binding of the imports I3-I5 of ADDENDUM_018 (no proof reopened)

**Tier: CUSTODY.** This addendum proves nothing new and reopens no proof. It binds the three imports I3, I4, I5 of the sealed
ADDENDUM_018 (R/PROOF.md revision 3) to exact sealed statements, and carries the H41 W mechanism audit as a negative-result artifact.

## 1. The imports being bound
**Verbatim** — `H41_MOD4_SUCCESSOR_ADDENDUM_018/R/PROOF.md` lines 24-26 (I3, I4, I5 as imported by ADDENDUM_018)
```text
I3  [A] Position table (delta_0, h, a): positive E (2, 1, 0); negative E (1, 1, 0) — W audit sec 1 table (Stage II / identity-component review).
I4  [A] Cusp-image bounds: t | 2 at positive E; t | 4 at negative E — W audit table (ICR; E(Q)_tors = C_4, real identity component).
I5  [A] Real-logarithm identity: z = nu_0 delta_0 lambda / h (nu_0 = +-1), and t = reduced denominator of z — W audit (1)-(2)
```

## 2. Binding
**I3 needs no import once ADDENDUM_018 (i) holds.** With E_0 = E: h = Omega_(0,R)/Omega_(E,R) = 1 and a = -v_2(h) = 0; delta_0 = #pi_0(E(R)) is 2 when
Delta_E > 0 (positive branch) and 1 when Delta_E < 0 (negative branch). These are the values (2, 1, 0) and (1, 1, 0) quoted in I3.

**I4 and I5 are statements of the sealed identity-component review** (sha256 544e1c9c1c8e4551dc8a92fbbea602427b1e146094b443a18c7e36a6ffd7a84f, byte-identical
to its member inside the sealed CODEX_H41_SEED_RESEARCH_FREEZE_001.tar.gz, archive sha256 ac82f3ad90ce42a610a411b24a26629affde209ee90d2c33e7cab7148e355560):

**Verbatim** — `R/IDENTITY_COMPONENT_REVIEW.md` line 28 (I4, positive E: t divides 2)
```text
Then alpha<r<beta<0. The points P=(r,r) and −P lie on the bounded oval, while 2P=(0,0), at the largest root, lies in the identity component. Since E(Q)_tors=C4, the rational identity-component torsion is precisely {O,2P}. Thus an optimal E in this branch has t dividing 2.
```

**Verbatim** — `R/IDENTITY_COMPONENT_REVIEW.md` line 30 (I4, negative E: exponent 4)
```text
The other positions retain the prior exponent bounds. In particular, B has rational torsion C2×C2 and hence any cusp image has order dividing 2; negative E has exponent 4; negative G and positive F have exponent 2.
```

**Verbatim** — `R/IDENTITY_COMPONENT_REVIEW.md` lines 36-38 (I5: z = nu0 delta0 lambda / h with reduced denominator t)
```text
    z = nu0 delta0 lambda / h = A/t,   nu0=±1,

with reduced denominator t, taking A=0,t=1 if z=0. The resulting bounds are:
```

**Verbatim** — `R/IDENTITY_COMPONENT_REVIEW.md` lines 40-42 (table header and negative E row)
```text
| Branch / optimal position | s=v2(delta0)−v2(h) | Forced divisor bound for t | Forced denominator divisor for lambda |
|---|---:|---:|---:|
| negative E | 0 | 4 | 4 |
```

**Verbatim** — `R/IDENTITY_COMPONENT_REVIEW.md` line 46 (positive E row)
```text
| positive E | 1 | 2 | 4 |
```

## 3. Agreement with the W audit (carried, not promoted)
The digest-pinned audit cited by ADDENDUM_018 (sha256 dfa6291c900dab0bf2d1a9f4469f2a6be39a135ba5d59225a892d772565fbfc5) states the same rows:

**Verbatim** — `R/H41_W_MECHANISM_AUDIT.md` lines 50-56 (the sealed exact identities (1))
```text
The sealed exact identities are
\[
w_\ell\Omega_{0,\mathbf R}=-\nu_0 B_\ell L(E,1),\qquad
4\lambda=-\frac{w_\ell}{\nu_0 b_\ell2^a},\qquad
z:=\frac{\nu_0\delta_0\lambda}{h}=-\frac{\delta_0w_\ell}{B_\ell}.
\tag{1}
\]
```

**Verbatim** — `R/H41_W_MECHANISM_AUDIT.md` lines 72-74 (table header and negative E row)
```text
| Branch / position | \(\delta_0\) | h | a | s | Proved t bound | Proved winding divisibility | Proved scalar integrality |
|---|---:|---:|---:|---:|---|---|---|
| Negative E | 1 | 1 | 0 | 0 | \(t\mid4\) | \(w_3\in\mathbf Z\) | \(4\lambda\in\mathbf Z\) |
```

**Verbatim** — `R/H41_W_MECHANISM_AUDIT.md` line 78 (positive E row)
```text
| Positive E | 2 | 1 | 0 | 1 | \(t\mid2\) | \(w_\ell\in\mathbf Z\) | \(4\lambda\in\mathbf Z\) |
```

## 4. Status of the W audit
```text
H41_W_MECHANISM_AUDIT = CARRIED AS A NEGATIVE-RESULT ARTIFACT (byte-identical copy in R/)
ITS GLOBAL NEGATIVE_ROUTE / POSITIVE_ROUTE = BLOCKED = SUPERSEDED BY ADDENDUM_018 (mod-4 integral character route)
ITS NEGATIVE RESULT STANDS: component-group and residual Eisenstein data alone do not evaluate the missing winding bit
NOTHING ELSE IN THE W AUDIT IS PROMOTED BY THIS ADDENDUM
ADDENDUM_018 IMPORTS I3-I5 = BOUND (I3 elementary given E_0 = E; I4, I5 = sealed identity-component review)
H41 = FROZEN: DO-NOT-REDO EXCEPT AN IDENTIFIED DEFECT
H9 = UNCHANGED
```

## 5. Custody
R/ holds byte copies of the two cited files. computation/build_addendum.py re-verifies the digests (including the member inside the sealed
CODEX archive and the ADDENDUM_018 archive), every verbatim block, writes receipts, DIGESTS.md and MANIFEST.sha256, and builds the archive
without AppleDouble members; the archive digest is recorded beside it.
