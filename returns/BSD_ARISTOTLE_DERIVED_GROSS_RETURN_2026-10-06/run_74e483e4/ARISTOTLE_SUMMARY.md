# Summary of changes for run 74e483e4-9494-42cc-b7ea-918bcb21ba10
**STATUS: PRECISE_OBSTRUCTION.** It stays the same under your tightened four-condition test. No identity was found, not even one that holds only up to a unit or with a constant that changes with the level, so none of the weaker labels fits. The full return is in `DERIVED_GROSS_RESULT.md`, with every claim labelled PROVED, IMPORTED or HEURISTIC; your tightened test is applied in §6A. Both Lean files build with no `sorry`.

**Setting** (§1). The theta element comes from a definite quaternion algebra ramified at 3, 2243, 5843 and ∞, with an Eichler order of level \(2^3\cdot4547^2\), at prime levels \(\ell\nmid 7Np\).
- **The element and the ideal.** \(\theta_\ell=\sum_\sigma\varphi_E(x_\ell^\sigma)\sigma\), with \(I\) the augmentation ideal of \(\mathbb Z_p[G]\), where \(G\) is the \(p\)-part of \(\mathrm{Gal}(K[\ell]/K)\).
- **Which element interpolates L.** It is \(\theta\theta^*\) (Gross / Waldspurger / Cai–Shu–Tian; IMPORTED, exact theorem numbers not re-checked).
- **\(\theta\in I\) at every level.** The distribution relation gives \(\mathrm{aug}\,\theta_\ell=(a_\ell-2)\varphi_E(x_1)\) for split \(\ell\). Gross's formula at the trivial character forces \(\varphi_E(x_1)=0\).
- **The degree-two coefficient** is \(\sum_\sigma\varphi_E(x_\ell^\sigma)\binom{a(\sigma)}{2}\) (PROVED in Lean).
- **It is \(\theta\), not \(\theta\theta^*\), whose first nonzero coefficient lies in \(I^2/I^3\).** With a + sign in the functional equation, \(\theta\in I^2\) and \(\theta\theta^*\in I^4\). The algebra is PROVED; that the sign is + was not checked (HEURISTIC).

**The pairing in θ's own group (route A): proved vacuous.**
- Complex conjugation inverts \(\mathrm{Gal}(K[\ell]/K)\) and fixes \(E(\mathbb Q)\), so the Mazur–Tate pairing on \(E(\mathbb Q)\) is zero in \(G\otimes\mathbb Z_p\) for odd \(p\).
- Hence \(\det H\in I^3\) at every level and every odd \(p\).
- So "\(\Theta^{(2)}=m\det H\)" holds for one \(m\) exactly when it holds for every \(m\), exactly when \(\Theta^{(2)}=0\). No \(m_E\) is ever fixed, and the per-prime definite detector never fires.
- The only outside input is that the pairing respects complex conjugation (IMPORTED, Mazur–Tate / Tan).

**The other two routes fail as well:**
- **(B) G2's cyclotomic pairing, carried over** to the theta element's group (canonical on \(I^2/I^3\), split \(\ell\) only). This needs at least two new theorems: the comparison identity itself, and a map from the anticyclotomic theta coefficient to \(C_2(p,\ell)\).
  - Closing the comparison on the K side instead fails: the definite detector covers only ordinary \(p\), and there are infinitely many supersingular primes (Elkies), so the exceptional set would be infinite.
  - G2 also does not control whether its \(\ell\) split in \(K\).
- **(C) Bertolini–Darmon derived heights.** These are rebuilt for each \(p\), and the conjectured constant contains \(\#Ш(E/\mathbb Q)\) (HEURISTIC).

**Your tightened test** (`DerivedGross/Threshold.lean`, all PROVED):
- **Sufficiency of the four conditions.** One fixed \(m=a/b\), one finite exceptional set \(S\), the congruence \(bC_2\equiv aD\pmod p\), G2's \(D\not\equiv0\) and the detector together give \(Ш[p]\neq0\Rightarrow p\mid a\) outside \(S\), and finite support when \(a\neq0\). The deduction is formal, so the four interfaces carry all the content.
- **One unit on the final congruence** does not change whether it is zero.
- **A correction to your second case.** Two separate units on the two maps, both proved nonzero mod \(p\), still preserve the zero test. Only the value is lost: \(C v=u m D\). The bridge actually fails only when a factor assumed to be a unit is not proved nonzero mod \(p\).
- **A level-dependent constant gives no bound.** With \(m_{E,\ell}=\ell\) and \(\ell_p=p\), every per-prime hypothesis holds while every prime is in the support. This is why the test must require one rational number at every level.

**Lean.** The files are `DerivedGross/Parity.lean` and `DerivedGross/Threshold.lean`, in a new library `DerivedGross` added to `lakefile.toml` and to the default targets. The full `lake build` succeeds. `#print axioms` for every new theorem shows only `propext`, `Classical.choice` and `Quot.sound`; the output is in `DerivedGross/AXIOMS.txt` and §7 of the return. The files are pure algebra: the arithmetic inputs appear as explicit hypotheses, and nothing in them is a statement about Ш of the seed curve. Four of the results are listed in the properties table as proved.

FIN, ORDER9 and Q36: unchanged.