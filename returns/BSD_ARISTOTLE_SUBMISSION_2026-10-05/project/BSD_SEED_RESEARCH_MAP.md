# BSD seed: research map and continuation brief

This reading document accompanies the full evidence package. It is a map, not a replacement for original source proofs.


---

Original package file: `ARISTOTLE_PROMPT.md`

# Aristotle/Harmonic: continue the fixed BSD seed from the complete research record

The task is research toward full Birch–Swinnerton-Dyer for the following **fixed rank-two curve**, not merely verification of convenient abstract lemmas:

    E: y^2 = x^3 - 22735*x^2 + 106272484*x
    minimal: y^2 = x^3 - x^2 - 66020924*x - 65074271436
    conductor: 6503188012738584 = 2^3*3*2243*4547^2*5843
    free basis on minimal model:
       P1=(-3031,327384), P2=(-2394,281520)

The exact requested endpoint is finite Sha(E/Q) of order 9 and

    L''(E,1)/(2*Omega_E*Reg(E)) = 36,

with the supplied total real Neron period and saturated basis convention. Rank two and the listed finite-primary certificates are retained inputs with their original proof grades. They are not assumptions of full BSD. FIN, conditional ORDER9, and Q36 are still open in this record.

Read `guide/01_ENDPOINT_AND_PROOF_BOUNDARY.md`, `guide/03_WALL_ATLAS.md`, and `guide/04_RESEARCH_INTERFACES.md`. Use `guide/02_HOW_TO_USE_THE_RECORD.md` to reach the actual sources. The full 7,042-unit compendium and its unit data are included, as are later dossiers and a searchable evidence catalog. This is intentionally more than a summary: proofs, errors, repairs, source contracts, code, recorded outputs, earlier Lean projects, and historical negative tests remain available. Read the governing correction with any older candidate. The coverage report identifies bulk binary files retained externally instead of pretending their bytes are in the upload.

You may change methods, combine records, or abandon an unsuccessful lane. The current plan is not sacred. A common rational scalar, W3, a class-group receiver, or a rank-two Heegner object is not compulsory. Do not infer that a family of methods is impossible merely because one listed construction failed.

Your first substantive task is to identify a concrete arithmetic construction or estimate whose proof would close a seed obligation or remove a genuinely missing step on its proof path, then attempt to prove it. Do not stop merely because that theorem is currently open. Do not return only a restatement of the target. Use the archive to avoid repeating the same errors and to find usable pieces.

For the uniform problem, the retained implication is:

    dim Sel_p(E/Q)<=3 cofinitely
       => dim Sel_p=2 by rank and retained parity
       => Sha[p]=0
       => Sha[p^infinity]=0 cofinitely.

Equivalent sufficient forms include dim B_p<=1 for the exact receiver, a proved bound on a rigorously defined containing relation kernel, an actual two-prime unit Kurihara witness, or a p-unit annihilator. These are possible outputs, not inputs you may assume. Full FIN also requires full-primary finiteness at the finite remainder. An ordinary-only theorem does not cover the infinite supersingular complement.

For conditional ORDER9, an independently proved consequence of FIN excluding #Sha>=25281 suffices. For Q36, a proof that the displayed quotient is rational with reduced denominator<=174 already suffices using its certified interval; a direct height identity or another rigorous argument is also welcome. Neither endpoint must wait for your preferred uniform method if a better route appears.

Important current facts:

* The class-group receiver is exactly Sha[p] on its stated cofinite domain. Its generation and local exactness are established at retained-input grade; its independent size/rank bound is not.
* The determinant law delta_ab=C_p e_a e_b D_ab^2 includes the previously missing z=0 branch. Nonzero known-point determinants do not determine C_p. Its nonzero value is still uncontrolled.
* The W3 four-value extractor is real code, but it consumes genuine normalized weight-five/six seed Hida symbols not yet supplied by an admitted seed input constructor. The Delta calibration and synthetic arrays are not seed values. A symbolic uniform identity may bypass numerical evaluation.
* The closed cycle with period -2 is not a proved admissible two-prime packet; the audit gives the exact mixed-augmentation mismatch.
* The naive global biextension tensor and ratio have the wrong determinant/scalar behavior. The correctly typed squared determinant line is old and does not yet contain the needed modular element.
* K167's small finite-field calibration **was completed**. The seed evaluator and 5843 conclusion remain open; this remains a fixed-prime route unless a new uniform connection is actually proved.
* RS2's analytic Laurent construction is explicit. Its arithmetic comparison with the global Mordell–Weil regulator is missing. The outside-log normalization was already recorded in September.

Use experiments only with actual authenticated arithmetic inputs, and use exact controls to distinguish competing identities. Do not fit a matrix to desired values and present it as an independent arithmetic law. Do not use a finite sample, a synthetic jet, a larger precision calculation without recognition bounds, or a source normalization unit of unknown valuation as a theorem.

If a new result can be formalized, provide the concrete Lean definitions, exact theorem type, toolchain, build, and axiom audit. Existing A1/A2 abstract assembly proofs should be reused. Do not claim seed BSD from a structure whose fields simply assume the missing arithmetic comparison or cofinite witness. Retained unformalized imports must remain explicit dependencies. A rigorous informal new arithmetic lemma is preferable to a formally checked tautology advertised as the seed.

Follow `guide/05_FORMALIZATION_AND_RETURN_CONTRACT.md`. Report the strongest new statement actually proved and its exact endpoint effect, together with the full proof, source/assumption ledger, collision check, seed specialization, code/Lean when applicable, and the first remaining arithmetic obligation. If one mechanism fails, repair or redirect when possible instead of polishing a known dead end. No existing negative screen is a universal impossibility theorem unless its exact proof says so.

The aim is to make new mathematics from the accumulated record. The maps and failure ledger are there to inform the attempt, not to force another review-only return.


---

Original package file: `guide/01_ENDPOINT_AND_PROOF_BOUNDARY.md`

# The fixed seed, the three obligations, and the evidence boundary

This is the governing orientation for this handoff, dated 2026-10-05. It preserves the earlier mathematical grades; it is not a new audit of every proof. It overrides historical planning language in the evidence archive. The task is to develop mathematics toward full BSD for **this curve**, with freedom to change method. It is not to find an easier curve and report that as completion.

## 1. Identify the actual arithmetic object

The original equation is

\[
E: y^2=x^3-22735x^2+106272484x.
\]

The global minimal equation is

\[
y^2=X^3-X^2-66020924X-65074271436,\qquad x=X+7578.
\]

The coordinate change has u=1 and preserves the invariant differential. The retained saturated free basis and torsion point are

| Point | Original model | Minimal model |
|---|---|---|
| P1 | (4547,327384) | (-3031,327384) |
| P2 | (5184,281520) | (-2394,281520) |
| T, order 2 | (0,0) | (-7578,0) |

The conductor is

\[
N=6503188012738584=2^3\cdot3\cdot2243\cdot4547^2\cdot5843.
\]

The retained minimal discriminant is 16586638656786071143743744 and c4=3169004368. The curve has no CM, torsion order 2, two real components, root number +1, and Tamagawa product 16. Local data:

| Prime | Reduction | Tamagawa number | a_l |
|---|---|---|---|
| 2 | I1* | 2 | see the actual local certificate |
| 3 | I2, nonsplit multiplicative | 2 | -1 |
| 2243 | I1, split multiplicative | 1 | +1 |
| 4547 | III, additive potentially good supersingular | 2 | 0 |
| 5843 | I2, nonsplit multiplicative | 2 | -1 |

Use release claim A.1 and its source files for these statements, not this transcription as a new certificate. In particular a change of model can change a software height convention even when the mathematical invariant has a canonical transport.

## 2. What completion means

The retained algebraic and analytic ranks are both 2. With the project's total real Neron period Omega_E and the Neron–Tate regulator of the saturated basis, define

\[
q_E=\frac{L''(E,1)}{2\Omega_E\operatorname{Reg}(E)}.
\]

The full seed endpoint is

\[
\Sha(E/\mathbf Q)\text{ is finite},\qquad
\#\Sha(E/\mathbf Q)=9,\qquad q_E=36.
\]

These are named FIN, ORDER9, and Q36. ORDER9 is often pursued conditionally on FIN; this does not discharge FIN. In these conventions BSD's order formula is q_E=4 #Sha, because Tam/torsion^2=16/4=4.

The certified interval is 35.99427 < q_E < 36.00573. A numerical value near 36 is not an equality certificate. A proof that q_E is rational with reduced denominator at most 174 would force q_E=36; a rank-two height formula is one possible source of that assertion, not a logically necessary form of any proof.

## 3. The retained arithmetic floor

The frozen research release v0.2.6 is commit 8414aea58180f3a18bcee7fba23475c8cac90996. Its 89 claim statements, evidence bindings, qualifications, theorem imports, and checks are included. Its stated grades are retained, not freshly re-certified by packaging.

* The rank-two basis and analytic rank are certified in the recorded computer-assisted sense.
* Sha[p^infinity]=0 for every prime p<=47 other than 3.
* Sha[3^infinity] is (Z/3)^2. The governing v0.2.5/v0.2.6 Route K proof supersedes the older attempt relying on the disputed Skinner/Skinner–Urban application. Read that proof's exact imports and reviews.
* Under FIN, square order and the settled primary components give #Sha=9 t^2, with every prime divisor of t at least 53. Thus #Sha=9 or #Sha>=25281.
* No later return inspected for this handoff supplies a new seed primary certificate, an independent cofinite vanishing theorem, or Q36. Later candidate proofs retain their own explicit review boundaries.

“Proved” in an archived model report is not automatically human referee acceptance or Lean verification. Consult the proof and audit grade. The 7,042-unit compendium is an extraction of records, not 7,042 newly certified theorems.

## 4. The exact uniform implication

Write S_p=Sel_p(E/Q) and W_p=E(Q)/p E(Q) inside S_p. For odd p the retained saturated rank-two basis makes dim W_p=2. The Kummer sequence gives

\[
0\longrightarrow W_p\longrightarrow S_p\longrightarrow\Sha[p]\longrightarrow0.
\]

Under the retained parity input, dim Sha[p] is even. Hence an independently proved dim S_p<=3 forces dim S_p=2 and Sha[p]=0. For a p-primary torsion group, vanishing of its p-torsion forces the entire primary group to vanish.

For good p>=5 the retained Kurihara framework supplies **some** nonzero witness. Its minimum length is r_p=dim S_p. The desired two-prime witness is a much stronger length bound. Source claim B.23 compares minimum character depth and witness length only in its stated truncated range; use its full statement, not an unrestricted slogan about all depths.

A theorem of the following form would close the uniform good-prime support obligation:

\[
\exists S\text{ finite}\quad\forall p\notin S,
\quad \dim_{\mathbf F_p}S_p\le3.
\]

It need not arise from a common rational scalar, a class group, the W3 family, or a fixed integral lattice. Those are possible methods, not an exhaustive classification. An equivalence can expose useful new tools; equivalence alone is neither proof of progress nor proof of futility.

## 5. FIN still needs the finite remainder

A torsion abelian group is finite exactly when it has finite prime support **and** every primary component is finite. A uniform theorem outside S leaves the full-primary finiteness of p in S. The bad primes 2243,4547,5843 remain outstanding in the retained seed state; an additional theorem may create further exceptions.

Do not replace finiteness of Sha[p^infinity] with finiteness of the vector space Sha[p]. A divisible group Q_p/Z_p has finite p-torsion and is infinite. Nor does primary finiteness at every individual prime exclude infinitely many nonzero components. The existing A2 Lean library already proves the abstract assembly and its countercontrols.

An ordinary-only theorem leaves a separate supersingular problem. Supersingular primes are not a finite exceptional set for this curve. A proof covering a density-one subset also leaves an infinite complement unless that complement is handled.

## 6. Conditional ORDER9 and Q36 are admissible endpoints

Conditional ORDER9 can be closed by any independently proved arithmetic argument yielding, under FIN, #Sha<25281. An annihilator with only settled prime factors, a size/index/support bound, or vanishing at every remaining prime could do this. It has not been proved that every such route passes through Q36.

One sufficient estimate is #Sha <= C q_E/4, with 0<C<=3370800000/1200191. Equality in the bound on C is allowed because the upper endpoint of the q interval is strict. The convenient integer C=2808 works. This inequality is not currently a theorem for the seed.

Q36 can be reached by a direct exact identity, the bounded rationality criterion, the recorded bounded algebraicity criterion with its exact hypotheses, or another rigorous arithmetic comparison. Computing another analytic representation of L'' without relating it to Omega_E Reg(E) does not prove Q36. Q36 alone does not determine the actual order of Sha without an order-formula comparison.

## 7. Non-anomalous and normalization inputs

For good p>=7, rational 2-torsion makes #E(F_p) even; the Hasse bound puts it below 2p, so it cannot be divisible by the odd prime p. The separate count #E(F_5)=8 handles p=5. This is the retained non-anomalous input, not an ordinary-only argument.

Keep these distinctions explicit in every construction:

* Total real Neron period versus least positive real period: here Omega_E=2 omega_1; modular-symbol conventions differ by that factor.
* Primitive modular parametrization versus a fixed p-unit multiple; its Manin constant has a proved power-of-two bound, with the exact bound determined by the applicable certificate (do not interchange the various c_E and 512 statements without their source).
* Z_p versus a ramified coefficient ring O with uniformizer varpi: valuations and lengths rescale under ramified extension.
* A primitive integral local generator changes valuations only by a unit; an arbitrary numerical eigenvector does not.
* Cohomological torsion coefficients E[p], a Tate twist of E[p], and an adjoint representation are different targets.
* Additive tame characters of a multiplicative torsor do not act like scalar reduction on a rational vector space.

## 8. Dependency policy for Aristotle

The supplied research implications can be used as explicitly named imported hypotheses while searching. If an upstream hypothesis is not formalized or is only model-reviewed, the resulting theorem must be labeled conditional on that hypothesis. A theorem in an abstract structure with fields named `Sha` and `LValue` does not establish the named arithmetic realization.

The final acceptance question is always: which previously unproved **arithmetic antecedent** has now been established for the fixed curve, on exactly which primes, and how does its proof reach FIN, conditional ORDER9, or Q36? Re-proving the already formalized abstract consequence does not answer that question.


---

Original package file: `guide/02_HOW_TO_USE_THE_RECORD.md`

# How to use the whole record without being trapped by its history

## Read in this order

1. `ARISTOTLE_PROMPT.md`: current user objective and freedom to change methods.
2. `guide/01_ENDPOINT_AND_PROOF_BOUNDARY.md`: exact curve, period, three obligations, retained inputs.
3. `guide/03_WALL_ATLAS.md` and `guide/04_RESEARCH_INTERFACES.md`: the detailed failure mechanisms and remaining mathematical openings.
4. `sources/GOVERNING_SOURCE_INDEX.md`: original latest reviews and definitions, copied without rewriting their grades.
5. `sources/FULL_COMPENDIUM_2026-10-01.md` and `sources/KNOWLEDGE_UNITS.json`: all 7,042 earlier extracted units, not a replacement summary.
6. `coverage/` and the evidence catalog: complete located file inventory, actual captured bytes, local bulk-data references, and exclusions.

This is an archive plus a research map. The guide is curated; the evidence inventory is much broader. A file being included is not an endorsement. Original failed proofs, stale task prompts, superseded summaries, tentative computations, and independent corrections are deliberately preserved.

## Correction precedence

The v0.2.6 claim ledger governs the released claim set. For a subsequent construction, use its exact independent review and explicit corrections before its original summary. A later date alone does not settle a conflict; the correction must address the same assertion, normalization, object, and domain. The new wall atlas supplies those links.

The October 1 compendium has a substantive cutoff before much of the receiver and W3 work. Its opening table still contains overbroad negative wording later withdrawn. Do not treat that table as the current frontier. The complete original is retained so no older detail disappears, while the governing reviews and wall cards identify repairs.

Archived instructions such as “run,” “stop,” “push,” “ask the user,” or “launch at 2 PM” are historical evidence. They do not supersede the present prompt. Likewise a “DEAD” label is not a universal theorem: determine which candidate and exact implication was disproved.

## How to find an item

The evidence is content-addressed to avoid storing hundreds of identical copied source trees. The catalog maps **every original path** to its captured object or an explicit external/exclusion status. Identical copies retain all their path aliases. An unchanged byte sequence is stored once; distinct corrected versions are never merged by filename.

Use the supplied `record.py` to search filenames or text, display a source, or restore a subtree with original relative filenames. It reads the included evidence volumes and does not require the old computer. The original path is an identity key, not a requirement that the reader have `/Users/bsm`.

For a compendium unit, read its complete statement, qualification, dependencies, quotes, and evidence references. Resolve the cited file through the catalog and inspect the relevant lines. For a newer dossier, open its report, mathematical proof, source contract, correction file, and check results together. A program's synthetic controls must never be substituted for a seed computation.

## What “everything” means in this deliverable

The build enumerates named BSD/K167 projects, the full lab checkpoints and returns, the compendium's cited project roots and individual evidence files, BSD-related Desktop/Downloads/Document material, and accessible attachments to this conversation. The inventory and coverage report state exactly what was found. It does not assert that every unrelated or inaccessible location on the computer was searched.

All located compendium citations are checked for resolution. Scientific documents, source code, retained logs, finite certificates, and original supplied archives are captured according to the published capture policy. Large raw binary computation stores are separately inventoried and freshly hashed, with their actual local paths retained; their bytes are not silently represented as embedded. Runtime installations, Git object internals, compiled outputs, and credentials have separate dispositions. Source code, toolchain/commit manifests, and recorded build outputs are retained.

This distinction is important: an evidence index is not the binary data it references. `coverage/COVERAGE.md` reports the actual numbers and any remaining missing items. No claim of new theorem verification follows from resolving a citation or verifying a hash.

## Evidence classes

* **Released arithmetic certificate:** a precise seed statement with the original producer/checker, output, dependencies, and audit; grade retained.
* **Imported theorem:** exact version and hypotheses matter. A source paper's abstract is not the theorem. Preserve published/preprint differences.
* **Written derivation:** supplied proof with its review tier; a new same-worker result is not an independent review of itself.
* **Formal proof:** inspect the actual theorem type, definitions, imports, axioms, and build receipts. Abstract bridge proofs retain their arithmetic hypotheses.
* **Computation:** distinguish exact, interval-certified, high-precision heuristic, finite sample, and synthetic control.
* **Negative test:** applies to the tested construction or implication. An abstract countermodel can refute an inference without being a seed counterexample.
* **Resource decision:** no affordable implementation found, stopped, not launched, or quota exhausted is not mathematical nonexistence.

## Avoid two opposite errors

Do not discard a potentially useful equivalence merely because it is equivalent to the target: a new theorem applicable on one side could solve it. But do not count the equivalence itself as that theorem. Similarly, do not freeze the listed methods as the only admissible architectures. The new input may recombine older constructions or use an entirely different invariant; it must carry its arithmetic realization and endpoint implication.


---

Original package file: `guide/03_WALL_ATLAS.md`

# Detailed wall atlas: operations, exact failure, and what remains available

This atlas is a current synthesis of the located record, not a new proof of every source. It is intentionally explicit about **what makes an argument fail**. Sources with capital-letter IDs are unmodified files in `sources/governing/`; the index there gives original paths and hashes. The full compendium, all its knowledge units, all located later dossiers, and the complete historical stop/correction register are supplied separately. This guide does not discard a route merely because its previous version failed.

The word “wall” below has several meanings. **Invalid inference** means a stated deduction does not follow, sometimes with an exact countercontrol. **Wrong object/domain** means a theorem or computation does not concern the required arithmetic object. **Open arithmetic input** means a needed theorem has not been proved; that is a research opportunity, not a refutation. **Implementation gap** means the mathematical operation exists but an appropriate evaluator has not been supplied. **Resource stop** and **review pending** are not mathematical obstructions. Each card distinguishes these.

## W01. Pointwise primary control versus finite prime support

**Aim and available parts.** Assemble all primary components into FIN. The record has exact small-primary results, per-prime sufficient criteria, witness existence at every good prime, and Lean-checked abstract assembly.

**Failure mechanism.** A direct sum of nonzero finite p-groups over infinitely many primes has each primary component finite and the whole group infinite. Conversely a single infinite p-primary group can have support at just one prime. Pointwise existence of a witness whose length is unbounded does not force vanishing. An integral source whose image at p is multiplied by p^2 can be uniformly well-defined and nonprimitive at every p.

**What remains possible.** Prove finite support independently, or obtain one global finite group/annihilator/index bound that implies it; then prove full-primary finiteness at exceptions. A direct whole-group argument need not follow this partition. Do not rerun the A2 abstract proof and call it the missing arithmetic input. Sources: RELEASE B.11, X.1, O.1; A2_FORMAL_BOUNDARY; MASTER.

## W02. Kurihara witness existence does not bound its first nonzero length

**Aim and parts.** B.20 supplies a nonzero residual Kurihara witness for every good p>=5 on its imported theorem domain. B.21 identifies the minimum length r_p with dim Sel_p. B.22/B.24 turn sufficiently small character depth or a length-two unit into primary vanishing.

**Failure mechanism.** Global primitivity of an entire Euler/Kolyvagin system permits its first nonzero entry to occur at length four or later. The two rational points give a lower bound of two; they do not give the upper bound of three. “There is some nonzero entry” cannot be specialized to “there is a nonzero two-prime entry.” B.23's truncated-depth comparison has an explicit range and cannot be extended without proof.

**Reopening input.** A theorem bounding the first nonzero level, or an independent construction of a unit entry in the two-prime ideal, with actual arithmetic source and p-integral coefficients. It can use p-dependent auxiliaries. An upper bound on the auxiliaries is useful computationally but is not itself the missing nonvanishing theorem. Source: RELEASE B.20–B.24, TWO_PRIME.

## W03. Singleton Kato classes and the lost localization condition

**Aim and parts.** Recover a convenient singleton class instead of a two-prime witness. The corrected minimum singleton/Kato-class length uses the p-strict Selmer dimension. In the relevant notation the first nonzero class length is r_p-epsilon_p, where epsilon_p is the dimension of the localization image, either zero or one.

**Failure mechanism.** Replacing epsilon_p by one assumes that some Selmer direction localizes nontrivially. The rational-point line need not do so. A two-prime witness cannot be turned into the proposed nonzero singleton merely by deleting that local hypothesis. The old assertion that this is strictly stronger than the seed target also needs an actual separating example in the relevant domain; logical implication alone does not prove strictness or comparative difficulty.

**What is retained.** The singleton method remains a valid sufficient route where localization is established. A prime-by-prime split can use it on one side and a two-prime construction on the other, but the split itself gives no upper bound on either side. Sources: MECHANISM_B, T0, TWO_PRIME, GL3.

## W04. Elliptic Wieferich data and finite-precision infinity

**Actual data.** The hardened check of 3,240 good primes through 30,000 found P1 exceptional at 5,73 and P2 at 107,2659,20353, with no simultaneous exceptional prime. These are exact/local controls, not a cofinite theorem. The earlier 3581 hit was false: finite p-adic precision returned [0], which was wrongly accepted as genuine infinity. The corrected exact computation at 3581 is nonzero at the required order.

**Failure mechanism.** Finite samples do not exclude future simultaneous local divisibility. A theorem producing infinitely many non-Wieferich primes for one point has the wrong quantifier for “only finitely many simultaneous Wieferich primes for two points.” The heuristic sum was also corrected from about .04 to .09113 for the stated range.

**Use without overclaim.** Keep these values as adversarial local controls for a proposed arithmetic identity. Require exact checks of reported hits, and treat precision-lost [0] as unresolved. The explicit quadratic auxiliary point in W13 removes this particular localization gap for the receiver; it does not prove a non-Wieferich theorem for P1,P2. Source: WIEFERICH, FOUR_LANES, RECEIVER_LOCAL.

## W05. G2 supplies regulator units, not Mazur–Tate units

**Parts.** G2 constructs suitable auxiliaries with a nondegenerate tame regulator from a fixed 1-motive and the known Mordell–Weil points, under the retained image/local hypotheses. This is an independently useful supply of nonzero determinants.

**Failure mechanism.** The arithmetic coefficient still has an uncontrolled multiplicative scalar. In the fixed-p law C2(p,l)=w_p(a_l-2)R_(p,l), G2 controls the last factors, not w_p. In the two-prime law delta_ab=C_p e_a e_b D_ab^2 it controls nondegenerate pairs, not C_p. A map being injective on the known point lattice says nothing by itself about excess Selmer directions.

**Repair condition.** Construct an arithmetic comparison whose additional factor has an independent unit/valuation bound, or obtain an upper bound by another method. Do not divide by w_p/C_p to “prove” it is nonzero. Use the exact domain and production regulator factors; changing points to 16P_i introduces determinant scaling. Sources: G2, TWO_PRIME, BIEXTENSION_PROOF, RELEASE B.16–B.19.

## W06. The corrected two-prime scalar law, including z=0

**Available theorem at retained/imported grade.** The coherent system satisfies delta_ab=C_p e_a e_b D_ab^2 for every distinct cyclic Kato pair, including the former z=0 and determinant-zero branches. For a nondegenerate pair, delta_ab!=0 iff Sha[p^infinity]=0; C_p!=0 iff that primary group vanishes.

**What was repaired.** The z=0 branch uses modified strict Selmer spaces, pair interpolation in a common relaxed space, and reciprocity for a three-prime class against the two rational point classes. It does not assume a nonzero singleton. Kim's printed normalization identifies the lattice coordinate coherently; this does not normalize arbitrary separately computed symbols automatically.

**Exact remaining gap.** The comparison proof is consistent with C_p=0 at an unsettled prime. Its case split does not decide which case occurs. All pair values span the ideal (C_p). Taking more pairs or demonstrating auxiliary independence leaves this scalar ideal unchanged. An independent proof of its unitness would be a real solution, even though the resulting statement is equivalent to primary vanishing. Source: TWO_PRIME and its AUDIT/NORMALIZATION_CHECK files.

## W07. Mixed conductors and a unit norm transfer

**Aim.** Combine a G2 prime, which has a regulator unit, with a Kato prime to force a nonzero quadratic coefficient.

**Failure mechanism.** The projected G2 Euler factor is -4-v^2/(1+v), a unit in the relevant residual augmentation ring. Multiplying by a unit passes through a quadratic term already present; it cannot create one from zero. At a Kato prime the factor a_q-2 is zero mod p, so a theorem requiring that factor to be a unit cannot be transported unchanged.

**Correction that must travel with this card.** A separate tame–wild projection from level l p^2 has multiplier (a_p-1)^2 on the quadratic term, not a_p^2-a_p+1. At p=7 the corrected multiplier is 2, so the old claimed obstruction at 7 was spurious. The corrected unit transfer still does not force the incoming term to be nonzero.

**Open information.** Mixed coefficients or pairing data discarded by a projection could supply a new relation. No theorem says every combination must pass through Q36. Sources: ABC_REPAIR, MECHANISM_B, W_REPAIR.

## W08. LINE, common scalars, and finite CRT observations

**Sufficient architecture.** A nonzero rational scalar with the specified integral realizations outside finitely many primes has finite prime support. Together with the retained witness implications, it would supply cofinite vanishing; stronger p-power realization laws can also control primary finiteness. This is a valid possible route.

**Failure mechanism.** A compatible scalar across auxiliaries at one p is not a scalar across different p. The observed 288 residues at settled primes fit a rational/integer hypothesis, but finitely many congruences allow infinitely many other numbers and arbitrary unconstrained future residual values. A height lower bound on a competing constant is not an existence proof or height upper bound for the desired constant. Theorem W is fixed-p; LINE is an unconstructed cross-prime input.

**Circular construction to avoid.** A BKS rational Mordell–Weil comparison defined only after primary finiteness cannot be used to prove that finiteness without an independent construction. Do not assume #Sha=9 to define the index and then use it to prove ORDER9. Conversely the failure of those definitions does not prove a common scalar is impossible or necessary for every uniform argument. Sources: K288, BKS_PREFLIGHT, MASTER, RELEASE B.11/B.19, BIEXTENSION.

## W09. Self-dual determinant bases and the BKS Euler factor

**Original error.** The claimed canonical determinant generator from odd-shift self-duality used the wrong duality sign: det(C^vee[-3])=det(C), not its inverse. Self-duality does not supply the advertised arithmetic basis. A chosen rational comparison basis also need not be an integral basis.

**Normalization that survives.** At good seed p, E_p=#E(F_p)/p has valuation -1. It cannot be declared a unit. A primitive formal local point has logarithm in p Z_p with exactly valuation one, which can compensate in a correctly identified lattice. That local cancellation is a unit exactly when the relevant point is not locally p-divisible. It does not establish the full global Bockstein regulator index formula unconditionally.

**Research opening.** Construct the arithmetic element and its integral realization before asserting primitivity. Integral duality can establish certain index/order identities under the stated finiteness inputs; keep those assumptions. The proposed torsion direct-sum splitting was stronger than the established order formula. Sources: BKS_PREFLIGHT, ABC_REPAIR, W3_PERIOD.

## W10. Fixed congruence integers, adjoint Selmer groups, and visibility

**Useful part.** DFG-type congruence ideals provide genuine bounds for an adjoint Selmer representation. A fixed nonzero integer D with Sha[p]!=0 => p|D would solve cofinite support. A zero target outside D would be excellent if an injection from excess seed classes were proved.

**Failure mechanism in tested maps.** E[p] and the adjoint representation are different coefficients. The indicated coefficient Hom vanishes under the retained full residual image. The ordinary symmetric cup product into the bounded target vanishes on the relevant classes, so it does not detect excess. Nullhomotopies introduce another H^1 ambiguity and are not an injection merely because they exist.

**Withdrawn overclaim.** The test bank's Sha orders were analytic predictions, and even certified counterexamples could only defeat the specific tested modular-degree/congruence-integer implication. They would not kill all fixed-integer methods. Visibility in a chosen Jacobian can miss classes visible at higher level. The record does not prove that only rank-two exterior-square methods survive. Sources: ABC_REPAIR, FIXED_INTEGER.

## W11. Fixed receptacles and fixed-field character decompositions

**Tested constructions.** A fixed abelian variety B receiving E[p] as a Galois subrepresentation for infinitely many p is constrained by the Faltings–Zarhin comparison to contain E up to isogeny. Over a fixed field of prime-to-p degree, the nontrivial character components and the trivial component have independent equivariant projectors.

**Scoped failure.** The proposed all-low-rank-factor receptacle inherits E's rank-two issue. Bounds on twisted components do not transfer to the trivial component through a nonexistent cross-character equivariant linear map. This rejects those linear transfers, not every arithmetic relation between the components or every p-dependent field. A different arithmetic comparison or injective secondary operation remains unconstructed, not disproved. Sources: ABC_REPAIR, FIXED_INTEGER; original A/B/C returns are retained as historical evidence with corrections.

## W12. U22 and GL3: inequality directions and wrong boundary channels

**U22 parts.** The record preserves its Klingen boundary coefficient carrying C2, corrected gluing/relaxed-lift results, and congruence-depth lower bounds under named hypotheses. Link 2 still lacks the required independently normalized comparison with the two Mordell–Weil directions.

**Failures.** A quotient of a deformation ring gives a length inequality in a particular direction; an infinite length is not a finite upper bound. R=T does not itself identify every Selmer class with a realized extension. Upper-triangular extensions can share trace and determinant, so their dimensions cannot simply be substituted for pseudodeformation cotangent dimensions. A product of off-diagonal modules is not automatically a scalar trace-cycle generator. At finite depth k the lower bound is min(r,k), not r without truncation.

**GL3 scope.** The balanced length-one boundary representative requires GL2 weight at least three, excluding the tested weight-two balanced channel. Other representatives are not excluded by that calculation. The weight-three ordinary deformation repairs the local coefficient problem; it does not by itself construct a global upper bound or supersingular extension. Sources: U22, GL3. Reopen with the missing integral arithmetic realization or an actual independent depth upper bound, not an assertion that the available lower bound is an upper bound.

## W13. The explicit class-group receiver really contains the excess

**Construction.** Put d_p=1-p^2-66020924p^4-65074271436p^6 and R_p=(p^-2,sqrt(d_p)p^-3) over Q(sqrt(d_p)). This field is quadratic and splits at p; t(R_p)=-p/sqrt(d_p) has valuation one. R_p supplies the local finite Kummer line independently of P1,P2. Adjoin E[p], this quadratic field, and p-division points Q1,Q2,Q3 of P1,P2,R_p to obtain L_p.

**Why the extra point does not accidentally kill the excess.** Its quadratic action is anti-invariant. The translation module is V+V+V epsilon, with the additional C2 distinguishing the third summand. The global restriction kernel on E[p]-cohomology is exactly the two rational-point directions under the retained full Kummer-image proof.

**Output and limit.** Restriction gives Sha[p] -> B_p=Hom_Gamma(Cl(O_Lp[1/p])/p,V). It is an actual arithmetic map, valid also at supersingular good primes in the forward domain. It is not an independently bounded target. The fields vary with p and have enormous growing degree. Calling each class group finite does not yield one fixed finite group. Sources: FOUR_LANES, RECEIVER_DESCENT, RECEIVER_LOCAL.

## W14. Exact local splitting removes the receiver's extra line

**Newer retained result.** For good non-anomalous E/Q_p and a primitive formal R, the restriction kernel to Q_p(E[p],p^-1 R) is exactly the finite Kummer line. Ordinary proof: the torsion image contains a nonidentity central scalar, killing its cohomology; the translation subgroup is the formal line V+, and Hom_G(V+,V) has dimension one. It is incorrect to replace it by End_G(V), which can have dimension two in a split ordinary representation.

**Supersingular safeguard.** Over Q_p the full nonsplit Cartan normalizer, including Frobenius, gives End_G(V)=F_p. The Cartan alone has a two-dimensional centralizer and is insufficient. These local facts are not asserted for arbitrary ramified bases.

**Global payoff.** Together with the retained H^2(Gamma,V)=0 and away-from-p checks, B_p is exactly Sha[p] outside {2,3,19,59,487,2243,4547,5843}. This repairs identification, not size. It is wrong to discount a surviving receiver direction as local garbage on this domain. It is equally wrong to infer dim B_p<=1 from exactness. Source: RECEIVER_LOCAL and its supplied local-exactness proof.

## W15. The two transfer operations have different effects

**Failed transfer.** Restriction followed by corestriction across the degree-p^6 translation extension multiplies a p-torsion class by zero. It cannot detect the image injectively.

**Successful repair.** Use H={(0,diag(1,a),+1):a in F_p^*}, J=L^H, degree [L:J]=p-1, and V^H=F_p T with oriented torsion point T. Ideal extension j and norm N satisfy Nj=p-1 and jN=sum_H h. For a nonzero equivariant f onto V, choose x with f(x)=T; then f(jNx)=(p-1)T!=0. Thus B_p injects into the scalar dual of Cl(O_J[1/p])/p.

**Remaining gap.** J still varies with p and is huge. The injection does not bound its class group or standard quotient. The unknown x is used to prove injectivity, not to define the field, so that argument is not circular. Dropping orientation to x(T) changes the stabilizer and must not be silently substituted. Source: RECEIVER_ARITHMETIC.

## W16. Minkowski generation, pivots, and product rows

**What is established.** Prime ideals in J with norm at most ceil(sqrt(|disc J|)) generate its p-inverted class group. This gives a finite covering source for every receiver functional. Minkowski small elements can yield principal ideals r b with coefficient one at a selected large prime and all tail factors inside the old factor base.

**First failure.** Rows [I | C] eliminate newly introduced columns in favor of old columns. They prove no rank among the old columns. Increasing the count of such pivots is not increasing useful relation rank.

**Real improvement already present.** Comparing reductions of a,d,ad gives the old-factor relation div(c_ad)-div(c_a)-div(c_d). These are actual relations, not only eliminations. What remains unproved is enough independent rank/saturation modulo p uniformly. Bounded coefficients and rational full rank do not suffice: two copies of the A_(p-1) Cartan matrix have small entries and determinant divisible by p twice. Source: RECEIVER_ARITHMETIC and its proof/checks.

## W17. Multiplicative coordinate functions and chord relations

**First tested chord.** The oriented chord through Q1,T evaluated at Q2 is an actual field element. Its good-prime zeros force P1=P2 or P1=-P2 after multiplication by p. The exact collision gcds are 637=7^2*13 and 1. Its support lies over a fixed short set plus p. At almost every coefficient prime the relevant decomposition fixed spaces V^D vanish at this support, so the relation is already zero on equivariant maps from the free divisor module.

**Second tested chord.** Replacing Q2 by Q3 permits p-dependent support. Its quadratic norm factors into three x-coordinate differences times a square. Suitable affine involutions act as -I on V and fix the factor divisors; the quadratic involution acts as +I on V. Therefore 2 f(div beta)=0, and the candidate row again gives no standard-coordinate constraint for odd p.

**Scope.** This is stronger than the tautology that class-group characters kill principal divisors: it vanishes before imposing class-group relations. It excludes the tested recipes and their stated multiplicative/conjugate closure. Divisors of sums need not obey the same argument. Source: RECEIVER_PRODUCTS; full norm and support proofs retained.

## W18. Support restrictions can still represent every class

**Temptation.** Use the restrictions q=1 mod p, a_q=2 mod p, and P1,P2 locally p-divisible at q to shrink the receiver.

**Exact failure.** These restrictions allow primes splitting completely in L_p. The exponent-p unramified p-split class field above L_p is Galois over Q. For every class a, Chebotarev applied to its conjugacy class supplies primes whose restriction to L_p is identity and whose Artin class is a. Selecting a prime above q gives the desired exact class, without requiring a split Galois extension.

**Implication and remaining room.** Thus the allowed support detects every actual receiver direction; it imposes no multiplicity bound by itself. The argument does not show that actual additive pencil divisors realize arbitrary valuation vectors. Their coefficients and correlations may still provide arithmetic relations. A nonidentity-unipotent restriction would define another set and needs its own proof. Source: RECEIVER_ADDITIVE.

## W19. The second-torsion pencil and balanced tails

**What the repaired pencil achieves.** An integral primitive element theta of J with prime-to-p stabilizer produces simple-root principal divisors theta-n with a coefficient-one selected prime. Generic good tail primes also have degree one in J; their upstairs decomposition groups lie in H and residue degrees divide p-1. They survive the old residue-degree-p filter.

**Why detection is not elimination.** For any hypothetical independent receiver maps f1,...,fr and any tuple w, joint Chebotarev realizes w at a selected prime. The two reduced tails have values -w and +w. The actual old relation therefore vanishes against every such map. This proves compatibility with any receiver that exists; it does not assert such excess exists for the seed.

**Where new rank could reside.** With fixed reductions, R_pencil=R_product-div(c_((theta-n))). A principal-normalized choice makes the last term zero, but does not prove redundancy for an arbitrary already-fixed finite relation list. A rank theorem must control these actual small principal-reduction rows or another new cross-member relation. Short support alone is not a p-unit determinant. Source: RECEIVER_LOCAL and the embedded PENCIL_SUPPORT/PENCIL_TAILS/REDUCTION_IDENTITY files.

## W20. Two attempted repairs of pencil rank do not add rank

**Cross-member cancellation.** If two pencil elements share a selected prime, taking their quotient and reducing with the fixed system gives exactly rho_n-rho_m. It is an integral combination of existing rows, so it cannot enlarge their span.

**Divided norm.** The selected prime's translation orbit has valuation vector (1,...,1); the first derivative has (0,1,...,p-1). Neither vector is componentwise divisible by p. Formal division of a group-ring expression does not create an integral divisor. Even if div(alpha)=p Delta, Delta need not be principal: a nonzero order-p ideal class is precisely such an obstruction. The retained Q(sqrt(-47)) order-five control remains nonzero after inverting five.

**Reopening requirement.** Produce an actual integral divided divisor and independently control its class, or a genuinely new relation outside the current row span. The result does not refute refined reciprocity, a different additive construction, or a saturation theorem. Source: RECEIVER_LOCAL.

## W21. Correct receiver dimension and row-space bookkeeping

B_p=Hom_Gamma(A_p,V) counts copies of V in the semisimple **head**, with End_Gamma(V)=F_p. It need not equal the total Jordan–Hölder multiplicity in A_p: Gamma has order divisible by p, so its group algebra is not semisimple in general.

Every true receiver functional kills every principal relation. The useful rank is measured on a larger candidate-functional space F_old, not “on B_p.” With the actual prime-ideal identifications and local zero rules imposed, a selected relation operator E_p has B_p injecting into ker E_p. Proving dim ker E_p<=1 would suffice; proving receiver exactness does not prove this selected kernel has no spurious directions.

Do not count dim V=2 as two receiver copies, or use a raw divisor-space codimension where an equivariant Hom dimension is required. “Cyclic over an algebra” is not a one-dimensional residual bound unless that algebra and its action are specified. Sources: RECEIVER_PRECISIONS, RECEIVER_LOCAL/RANK_TARGET.

## W22. Weil cups, Cassels–Tate, and higher lifting

**Ordinary cup.** Two Selmer lifts have locally finite Kummer images, a self-annihilating local condition. Their Weil cup vanishes at every place; Brauer–Hasse–Noether then makes the global H^2(Q,mu_p) class zero. It supplies no new constraint beyond Selmer membership.

**Secondary pairing.** The Cassels–Tate construction for E[p^2] yields radical im(Sel_(p^2)->Sel_p)/W, identified with Sha[p] intersect p Sha[p^infinity]. A nonzero pairing minor detects actual Sha directions that do not lift, rather than eliminating those directions. One cannot impose pairing-zero as a new definition of all receiver elements.

**Countercontrols.** (Z/p)^(2r) can have a perfect alternating pairing for any r. (Z/p^2)^(2r) can have perfect full pairing but zero restricted pairing on p-torsion. Higher layers detect finite elementary divisors, while divisible directions persist. The formal pairing properties alone give no uniform dimension or exponent bound. New arithmetic control of lifting or an additional non-Selmer input remains possible. Source: RECEIVER_PAIRING_RS2.

## W23. First-order, adjoint, and Massey no-go statements were overstated

The October 3 four-lane synthesis was not accepted wholesale. Its known-point height computations concern W intersect the strict Selmer group, not the unknown whole group at unsettled primes. A relative Schur-complement construction on the excess is not excluded by nondegeneracy on W. Another lane silently changed the coinvariant module; a comparison was missing. A vanishing bounded target is not a contradiction to a desired injection—it would make the injection useful.

In the separate Massey attempt, scalar-cochain conversion works, but the strong-vanishing theorem needs roots of unity not present in the chosen field. A general vanishing statement permits changing defining systems and does not kill a prescribed obstruction with required local conditions. Neither failure is a theorem against every secondary operation.

In particular withdraw “all architectures reduce to a single cyclotomic T^2 unit” and “no first-order receiver can work” as universal claims. Reopen with correctly typed coefficients, fixed defining systems, and the required integral/local comparison. Sources: FOUR_LANES, MASSEY, ABC_REPAIR.

## W24. W3 has a genuine one-way upper-bound mechanism

**Available inequality.** For the stated good ordinary specializations outside retained finite exceptions, the corrected global/discrete Selmer control and Kato index give dim Sha[p] <= b_p-2. Thus b_p<=3 forces primary vanishing, using parity. b_p is a length/index in the **actual integral local quotient** of the Kato class.

**Why this is not already the answer.** Neither a nonzero complex critical L-value nor an integral local lattice gives b_p<=3. An arbitrary period normalization can change the p-adic valuation. The weight-three form has ramification at p; applying a crystalline theorem outside its hypotheses would be invalid. The later local return derives the applicable lattice comparison instead.

**Necessary-condition correction.** A repaired pairing on the two rational-point directions and their dual satisfies b<=3 => nonzero restricted pairing; b<=2 => rank two. Its mixed weight/cyclotomic height interpretation was not established. A necessary condition does not prove that this route is impossible, strictly harder, or a second independent conjecture. Sources: W3_INDEX, W3_PAIRING, W3_LOCAL.

## W25. Hida control at a fixed p is not cross-p rigidity

**Later partial results.** The retained cofinite Hida-algebra argument supplies an integral family frame outside a fixed exceptional divisor. Its exact hypotheses and independent-review needs remain explicit. A de Rham critical value M_g=L(g,2)/Theta_g is constructed, but A_g=eta_g M_g had an uncontrolled period comparison.

**Failure mechanisms.** Separate ordinary Hida branches at different p are not a single common integral global object simply because each branch has controlled specializations. Nonvanishing on a Zariski-open or density set is not a residual unit estimate. A fixed exceptional integer that is defined but not enumerated can support a theoretical cofinite statement, but does not certify that a chosen small p is in a computational sample's domain.

**Viable change already made.** Work directly with a genuine integral Kato-family class and its local quotient, so an unfinished comparison to M_g is not an obligatory gate. That still requires actual arithmetic source and specialization, not an invented family satisfying formal norm relations. Sources: W3_PERIOD, W3_HIDA, W3_SOURCE.

## W26. Local Coleman freeness and pseudo-null errors

The local ordinary quotient over R=Z_p[[T,S]] has nontrivial residual unramified character. Vanishing residual H^0,H^2 and one-dimensional H^1, with perfectness/base change, give a free rank-one H^1 in the matched setting. If a matched integral Coleman map is between free rank-one modules and has pseudo-null cokernel, its multiplier has no height-one divisor and is a unit. This removes the error **before** specialization.

What this does not do: it does not discard an arbitrary pseudo-null module after specialization, which can create a defect. It does not prove global cohomology free, establish the old eta_g as a unit, or force the genuine Kato image to have a low-order coefficient. At T=S=p the representation and tame/Tate twists must match exactly. A nonzero multivariable jet may vanish on that diagonal; T-S is the elementary control.

This local receiving module is reusable. The hard input is the global arithmetic image, its exact source coordinate, and its uniform valuation. Sources: W3_SOURCE, W3_VARIABLE_INDEX and their retained local input documents.

## W27. The four-value functional-equation reduction is not a source evaluator

**What exists.** In the matched family frame, the arithmetic reflection S -> (1+T)/(1+S)-1 and an integral unit normalization make the jet even in Y. The retained double zero leaves H=A T^2+B Y^2+C T^3+D T Y^2 mod (p,T,Y)^4. A,B are needed mod p^2 and C,D mod p. Four evaluations at (w,s)=(3,2),(3,3),(4,3),(4,4), weights 5,6, have determinant 864 mod p on the stated domain. One actual value nonzero mod p^4 implies primary vanishing through the variable-weight index theorem.

**What is missing.** These are arithmetic coefficients, not free input variables that can be selected to pass the test. Invertibility reconstructs a jet from values; it does not prove a value is nonzero. The retained Hida/source/control/double-zero theorems remain dependencies. The result covers ordinary primes; a supersingular argument remains separate.

**Critical precision.** Keep the second digits of A,B and valuation-three cases. “Zero mod p^4” means valuation at least four, not exactly four. Independent primitive frames preserve each value's valuation but do not necessarily preserve the common four-coefficient functional equation. Source: W3_FOUR_REVIEW.

## W28. The actual symbol extraction and its missing seed input

For each w=3,4, the extractor consumes the actual primitive specialized family symbol on {infinity}-{a/p}, with polynomial coefficients c_(w,a,h). It computes a weighted sum of 2(p-1) such values, using p-unit binomial denominators and the matched tame character. These are the weight-five/six Hida fibers, not the seed's weight-two form.

The code is implemented and calibrated on genuine Delta symbols at level one against an independent Riemann sum. Synthetic reconstruction controls also pass. Neither is a seed source table. The current admission review found no demonstrated seed input constructor or affordable complete pipeline in the inspected W3 material. It did not prove one impossible or use the large ambient dimension as a lower bound.

A useful continuation could construct a source-specific finite-precision evaluator, or derive a symbolic identity for its sums without enumerating a full ambient module. It must authenticate branch, integral frame, exceptional-domain membership, and the exact source law. Do not generate a statistical sample from synthetic arrays or an arbitrarily normalized eigenvector. Sources: W3_EXTRACTION, W3_INPUT, W3_ADMISSION.

## W29. Discovery experiments need an independently defined discriminator

The proposal to compare W3 residues to local logarithms is a legitimate *question*. But fitting a 4x2 matrix M_p after observing a nonzero input l and output V explains nothing: extend l and V to bases and a full-column-rank matrix with M_p l=V can always be manufactured. M_p must be independently defined before the test, and the proposed identity derived from the actual source.

Even an exact independently defined rank-two matrix law would only transfer simultaneous vanishing to simultaneous local-log vanishing. It does not prove that the latter has finite support. A fixed integer/resultant would supply finite support only after its arithmetic identification and nonzero value are proved. The four-value experiment also must retain p^2-residues after forced divisibility, not discard useful index-three outcomes.

This is a specification for a meaningful experiment, not a ban on experiments. A small test should distinguish competing arithmetic explanations and lead to an identity or bound, rather than restart a prime-by-prime certification campaign. Source: W3_ADMISSION; WIEFERICH for actual controls.

## W30. Closed noninvariant cycles and the missing admissible-packet comparison

**Positive construction.** A closed noninvariant lift repaired the cancellation of an invariant full pullback and produced a quadratic weighted period -2 mod p. It is a real cycle calculation under its inputs.

**Stronger audit identity.** The final operator factors modulo p through the original projection: (sum j^2 beta_j*)(U*-1)^2 = 2(T_p alpha*-beta*) pi*. Consequently R_p=2u(T_p^2-1)v, with u((p+1)^2-a_p^2)=1. The final cycle loses the choice of noninvariant lift. Its unit period is the old primitive period transported by an invertible scalar on the relevant quotient.

**Explicit mixed mismatch.** The formal polarized class is -2XY in the mixed augmentation quotient. The genuine complete two-prime packet is eta delta_ab XY. Applying the two extra differences to the genuine packet, already in J^2, moves it into J^4 and kills the quadratic coefficient even if delta_ab was a unit. Removing the differences leaves delta_ab unevaluated. The two norm projections have exactly the mixed coordinate in their degree-two kernel.

Thus the cycle's nonzero value is not an admitted witness. Ideal membership remains sufficient, but all actual pair values span (C_p), so combinations do not remove the comparison. A genuinely new inhomogeneous arithmetic identity could do so. Sources: CYCLE, CYCLE_MIXED.

## W31. Formal projective moves are not arithmetic torsor relabelings

The earlier projective identity used a transformation w outside the allowed affine relabelings of the actual C_p-torsor. A formal action on a projective index set cannot automatically be lifted to the prescribed arithmetic packet. The cyclic-p^2 correspondence supplied a p-unit transfer, but its full pullback was deck-invariant, so the quadratic weight annihilated it. W30 records the later repair and why that repair still does not identify a witness.

At Kato auxiliaries, l=1 and a_l=2 mod p make the oldform degeneracy matrix [[l+1,a_l],[a_l,l+1]] singular mod p. An inverse available at another auxiliary cannot be used there. Joint assembly must retain the singular mixed direction; the audited four-old-transfer calculation supplies no independent unit coordinate.

Reopen with a genuine arithmetic correspondence, correct packet action, and integral image comparison. Matching polynomial degree is not that comparison. Source: CYCLE and the retained packet-transfer/closed-lift inputs it binds.

## W32. The global Poincare biextension ratio has the wrong scalar action

The naive tensor P11 P22/(P12 P21) realizes B11+B22-B12-B21, not det B. In the actual p=17,l=103 calibration on Q_i=16P_i, the former is 1 and the determinant is 7. The correct algebraic carrier is (wedge^2 L)^tensor2 with primitive map (P1 wedge P2)^2 -> (P1^2)(P2^2)-(P1P2)^2 into Sym^2(Sym^2 L). That carrier was already in September's LINE record.

The more important mismatch is scalar action. Scaling a Poincare torsor section by rational c adds its tame character; it does not multiply a height by c mod p. A global principal idele change disappears in the quotient. Thus two rational sections of a G_m-torsor do not automatically give the claimed residual scalar law.

A reduction-linear map on a **fixed integral determinant lattice** is the right type of carrier and exists for the regulator side in the retained construction. No modular section with the required realization is constructed. This tested tensor/ratio argument is stopped; rebuilding the old carrier is not a new uniform input. Sources: BIEXTENSION, BIEXTENSION_PROOF.

## W33. Rationalizing finite augmentation kills the desired positive degree

For a finite group over Q the augmentation ideal is idempotent; its positive-degree augmentation quotients disappear after rationalization. Therefore simply tensoring the finite Mazur–Tate leading-term class with Q does not construct a rational section carrying that class.

Keeping integral classes at each p preserves the data but produces only the existing family w_p. Theorem W identifies auxiliaries within one p, not that family as reductions of one rational section. U22's boundary coefficient also lacks the required map to the rational-point fibers. A BKS/TNC comparison whose algebraic scalar assumes finiteness cannot be inserted unconditionally.

These failures are about these operations. A new geometric construction, another integral realization, or a uniform bound with no rational ancestor is not excluded. Source: BIEXTENSION_PROOF; BKS_PREFLIGHT; U22.

## W34. Plectic sign, local Frobenius, and genuine prime coverage

The full plectic class and the mock projection are different objects. The earlier use of Darmon–Fornea's prime-conductor wrong-rank-split statement at the seed's composite conductor was invalid. A local (1-epsilon_p sigma_p) calculation alone does not determine the complex-conjugation eigenspace of the global factor. The later Fornea–Gehrmann sign/Selmer checks supply the applicable information.

At 2243 the mock class is zero on the retained imported-theorem argument: its global minus eigenspace lies in the twist Selmer group killed by the retained K.2 result. The two recorded proofs share that decisive input; do not exaggerate their independence. At 5843 the plus direction survives, and nonzero mock Q_K would give primary **finiteness**, not vanishing. The first derivative [kappa_infinity]_1=2 Q_K uses ord_5843(q_E)=2.

The full Fornea construction at these primes is not blocked by the same hypothesis at 2 that blocks its separate comparison theorems. Do not merge those scopes. Nor does a two-prime existence theorem cover an infinite ordinary or supersingular tail. Sources: PLECTIC_SIGN, PLECTIC_STEP1, PLECTIC_STEP2.

## W35. TH and the finite-field certificate: the evaluator gap is local in scope

At K=Q(sqrt(-7)), the first admissible auxiliary 46639 has the wrong sign and its linear coefficient is forced zero. The first viable recorded auxiliary is l=46807, a_l=64. The test is [374976]P_D!=O over F_(l^2); #E(F_(l^2))=46744*46872, and 374976=8*46872 removes the prime-to-5843 factor.

The coefficient can be expressed through 5843 trace sums, totaling 34,146,492 CM terms before grouping. The huge complete Brandt class-set size is the size of one implementation, **not a lower bound** on evaluating that functional. The unresolved seed operation is evaluating the appropriate primitive elliptic quotient or certified level-raised eigenfunction at those inputs, possibly directly as an aggregate.

A nonzero certificate would close a real remaining primary-finiteness obligation. It would not close uniform FIN, ORDER9, or Q36. BH's priced route is also one-way: payment/run completion does not guarantee a nonzero witness. Sources: PLECTIC_STEP2 and later evaluator dossiers in the complete catalog.

## W36. K167: what was actually completed and what did not transfer

Changing to K'=Q(sqrt(-167)) makes the indefinite source classical X_0(N), with p=5843 inert and the other conductor primes split. No twist L-value certificate is needed for NZ => seed primary finiteness: base change has L(E/K',1)=0 already, and the resulting Selmer-rank bound plus rank E(Q)=2 suffices. The old l=46807 splits in K' and cannot be reused. The 2243 zero control is not available in this new datum.

The historical claim that the small arithmetic calibration remained open is now superseded. The later exact evaluator produced [3825]Z_269=(186,210), order19, for the conductor817 calibration curve. Its source labels, arithmetic reduction, finite-field group checks, and review boundary are included. This is stronger than the earlier rigorous complex enclosures; a nonzero complex point alone would not have sufficed.

Later seed work built CM-isogeny kernels, a quartic-type projector, and compact source labels. These are not the global seed quotient value. A projector with fixed rational denominator controls local type uniformly; it does not force projected global classes nonzero. The seed 5843 certificate remains uncomputed. The default uniform campaign must not be displaced by this fixed-prime implementation project. Sources: PLECTIC_FIELD_SWITCH, K167_CALIBRATION, K167_DIRECTION, K167_REFOCUS.

## W37. RS2: an analytic construction is not the Mordell–Weil comparison

The corrected coefficient is A_(-3), not the early A2 target. The finite-level formula

    D_N(s) E*_(2,0,N)(z,s)
      = N^(-s) sum_(d | rad N) mu(d) d^(-s) E*_2(dz,s)

has 32 terms for the seed and works at the nonsquarefree level. The Laurent extraction was carried through. Its normalized pairing contains C_N L(f,2)L''(f,1)/pi^3, with C_N=270966167197441/2168324513321472.

The September 20 record had already removed the displayed product-of-logarithms prefactor. Repeating that rescaling in October was not new work. More fundamentally, removing a scalar prefactor does not remove logarithms inside parameter derivatives, establish arithmetic Fourier coefficients, or place the cusp projection in a rational lattice.

The missing equality is with the certified global regulator/period expression, not the existence of an analytic representation of L''. A finite-dimensional complex cusp space and finitely many determining coefficients do not prove that scalar rational. Reopen with a genuine arithmetic realization or a proved denominator/height comparison for this analytic object. Sources: RS2, RECEIVER_PAIRING_RS2, COMPENDIUM_RECONCILIATION.

## W38. Earlier Q36 kernels, midpoint completions, and local realizations

The record has an exact weighted Mellin-period expression, certified nonzero residuals excluding the tested midpoint/endpoint Eisenstein completions, and scoped no-go lemmas for specified finite logarithmic/local realization classes. Their exact hypotheses are preserved in RELEASE Q.4 and X.5–X.8, and all supporting sources are included.

Those results do not say “no arithmetic interpretation of L'' exists.” A limit, genuinely different global comparison, or construction outside the named finite realization class is not excluded by a local no-go proof. Nor do first-derivative/rank-one formulas automatically provide the rank-two regulator determinant. Parameter differentiation must carry the prescribed constants, boundary terms, local factors, and period convention.

The smallest useful new input can be weaker than a complete rank-two Gross–Zagier theory: e.g. the specific bounded rationality certificate suffices Q36. But writing that sufficient condition is not proving it or showing it easier. Sources: RELEASE Q.1–Q.4, X.5–X.8/X.11; historical kernel dossiers in the compendium.

## W39. Conditional ORDER9: effective support or size, not finiteness alone

Under FIN, the remaining order gap starts at 25281. FIN itself only says finitely many primes occur, not which primes; it does not exclude a new factor 53^2 or larger. Thus the statement #Sha=9 needs an effective support, size, index, or annihilator argument, or primary vanishing at all remaining primes.

The archimedean inequality #Sha<=C q_E/4 with the precise threshold in the endpoint document is one approach, not a necessary bridge through Q36. An explicit integer annihilator with prime support among settled primes would also work, subject to handling the exact 3-primary order. Flach's adjoint/Sym^2 annihilator cannot simply be applied to E, and visibility at one level controls only what it actually realizes.

Settling p=53 would move the next square gap to 31329=9*59^2 if its witness were nonzero. That is an actual local advance, not an infinite-tail theorem. Sources: RELEASE R/O/Q claims, the conditional ORDER9 dossiers, FIXED_INTEGER.

## W40. Finite computations, resource bounds, and one-way criteria

The singleton pipeline has genuine sealed certificates through47. The proposed p=53,l=107 run fails before production because the tame regulator is zero; l=743 is the recorded alternative, with a prediction rather than a computed witness. A source cutoff within an old corpus is not enough if the selected auxiliary forces zero. Historical CPU-hour/storage figures are implementation-specific estimates, not new measurements in this package.

The bad-prime BH sufficient criterion includes the additive prime4547 in the later source-reviewed record; older “no criterion” language is superseded. No nonzero bad-prime witness is supplied. Large ambient matrices, class numbers, or class-set cardinalities are not general complexity lower bounds. Conversely a formula with a small number of output coordinates is not a cheap evaluator if obtaining each coordinate requires an unimplemented global source.

A failed sufficient test proves no nonvanishing of Sha and is not a BSD counterexample. A sealed prediction is not data. Exact producer/checker contracts, periods, tail bounds, and point-selection rules must travel with any new computation. Sources: RELEASE B.18, X.14–X.16; K167_DIRECTION; W3_ADMISSION; production dossiers.

## W41. Earlier successful twist programs do not prove this rank-two seed

Run013, H41, and related rank-zero twist-family results are included because they may supply techniques, exact descent patterns, and formal infrastructure. Their nonvanishing L(E,1), sign, local, and residual hypotheses are not those of the seed, for which L(E,1)=0 and analytic rank is two. Do not substitute another curve, an infinite family with different rank, or a two-primary theorem for this full BSD endpoint.

The H5–H9 program's typed Kummer towers, Hom-valued carriers, Tate twists, p^3 factors, and sealed trace/projection constraints are also preserved. A compatible tower need not specialize to a rational Mordell–Weil point; a branch shown zero cannot be reused as the missing nonzero point. A different class or a newly proved nonzero projection could reopen that approach. Consult the full per-program records; their statement-level scopes are more precise than a blanket “Heegner methods are dead.” Sources: full compendium sections 10–13 and their resolved original evidence, historical MASTER/DNR with later corrections.

## W42. Formal verification can certify the wrong conclusion if the type is wrong

The A1/A2 libraries already formalize witness-content and primary-support assembly. A2's own boundary states that no elliptic curve occurs internally: it proves group-theoretic implications under supplied hypotheses. Calling a structure field `seedSha` does not supply the arithmetic identification. Adding a hypothesis “a unit witness exists cofinitely” and proving FIN from it is not a new uniform theorem.

Use Lean for the hard new implication when its concrete objects/imports can be specified. Check exact statement equivalence, universe/coefficient types, `#print axioms`, and reproducible build. An axiom encoding the desired arithmetic comparison, a `sorry`, a definition that makes the conclusion true by construction, or a different curve invalidates a claimed seed result. Standard logical axioms versus newly introduced mathematical assumptions must be reported separately.

Aristotle may search and formalize; it is not restricted to rechecking easy algebra. A partial theorem can count if it proves a new arithmetic lemma actually used in an endpoint route and states the remaining gap. Packaging does not certify novelty or guarantee discovery. Source: A2_FORMAL_BOUNDARY and the included complete earlier Aristotle/Lean projects.

## W43. False counterexamples and numerical/exactness flags

The identified LLM/Magma story misread a rank lower bound after losing the false exactness flag. It was not a verified discrepancy between algebraic and analytic ranks. The retained seed certificates instead agree at rank two. A failed witness, unresolved precision, analytic prediction of Sha, or approximate L-value cannot be promoted to a BSD counterexample.

Any contrary seed result needs independent exact arithmetic, a checked analytic certificate in the same model/conventions, and the complete software return flags. The package keeps failed and corrected computations so future experiments can test those errors explicitly. Source: MAGMA, WIEFERICH; released analytic/rank certificates.

## W44. No exhaustive theorem of impossibility has been proved

The atlas contains many failed **operations**, not a proof that no new uniform arithmetic mechanism can be made. The currently missing inputs are concrete: an independent cofinite Selmer/receiver bound, sufficient relation saturation, an arithmetic unit-content comparison, an actual low-index Kato image with uniform control, an effective annihilator, a Q36 arithmetic identity, or another proved mechanism with the same endpoint consequence.

These forms are examples, not a forced menu. A new equivalence with a theorem that can actually be applied, a repaired construction with new arithmetic information, or a combination exploiting data previously discarded can be useful. The required distinction is between identifying a target and proving something that constrains it. Do not return a new name for C_p, another unchanged relation span, or a success label for an uninstantiated input. Also do not abandon a potentially repairable construction merely because a theorem remains to invent. State the candidate, test its actual first arithmetic step, repair what can be repaired, and preserve its exact dependency on the seed.

## Source completeness beyond these cards

The cards group related failures for navigation. They are not the only included knowledge. `sources/FULL_COMPENDIUM_2026-10-01.md` preserves every earlier extracted unit; the generated historical stop register preserves the full selected unit text and its recorded review/supersession fields; `coverage/` indexes every located file and every captured later source version. Use those when a card's grouping is too coarse. If the source contradicts this synthesis, record the exact conflict and repair the synthesis before using it as a theorem.


---

Original package file: `guide/04_RESEARCH_INTERFACES.md`

# Research interfaces: what can be made from the retained parts

This file gives Aristotle concrete places to work, not a claim that one is known to succeed or that these exhaust possible methods. The primary mission is full BSD for the fixed seed. A new lemma is useful when its arithmetic conclusion connects to an endpoint through explicit, applicable implications. The current lack of that lemma is the research task; it is not, by itself, a reason to stop.

## Interface U: close cofinite support directly

**Requested arithmetic output:** one fixed finite set S and a proof that dim Sel_p(E/Q)<=3 for every p outside S, or an equivalent sufficient output with an independently established antecedent. No effective enumeration of S is needed for a purely theoretical cofinite theorem, but every hypothesis must be proved outside a fixed finite set. FIN still needs primary finiteness inside the resulting S.

**Already available:** rank-two Kummer subspace, retained parity, actual Kurihara witness system, exact receiver on a cofinite ordinary-and-supersingular domain, and multiple conditional bridges. The abstract implications after such a bound are not missing.

**Possible new constructions:** an arithmetic injection of the excess into an independently bounded module; a fixed annihilator with a proved action; a uniform p-dependent estimate; or a new geometric source with integrally controlled image. A fixed rational scalar is optional. A direct theorem may bypass every proxy in this package.

**Proof obligations:** the map is defined without selecting unknown Sha classes as input data; it kills precisely what it is supposed to kill or preserves detection; local conditions and p-integrality are explicit; the target bound is independent of the desired conclusion; ordinary and supersingular coverage is accounted for. A theorem equivalent to the endpoint is legitimate if its proof introduces genuinely new arithmetic information.

## Interface R: use the exact receiver, but constrain its surviving head

On the retained domain,

    B_p = Hom_Gamma_p(Cl(O_Lp[1/p])/p,E[p]) = Sha[p].

**Minimal sufficient result:** dim B_p<=1 cofinitely. An independent p-unit annihilator of B_p would be even more direct. On a selected finite relation presentation it suffices to bound the dimension of the correctly defined containing kernel, with generation proved.

**Available building blocks:** explicit L_p and auxiliary R_p; full affine Galois action; exact local kernel; global descent; prime-to-p stabilizer field J_p; a covering Minkowski factor base; actual product-reduction rows; second-torsion pencil rows. These are supplied with proofs and corrections, not just names.

**Where a new theorem would act:** on dependencies among *different old factor-base coordinates* after actual relations, or on the standard quotient of the class group. The pencil detects arbitrary receiver tuples and produces balanced tails. Thus a useful new relation must exploit arithmetic correlations not explained by those balancing equations. Coefficient-level additive identities, integral divided divisors with independently controlled ideal classes, or a different reciprocity/annihilator action are not excluded.

**First test of a proposal:** write the induced relation functional on actual prime ideals. Prove it is not already zero for symmetry reasons, not an existing row combination, and not merely a pivot introducing a new compensating column. Then attempt the uniform rank/saturation statement. Passing the first test is admission, not a dimension theorem. No enormous class-group enumeration is suggested.

## Interface K: an arithmetic comparison forcing low witness content

**Available source relation:** delta_ab=C_p e_a e_b D_ab^2, with independently obtainable D_ab!=0 and nonzero local factors for suitable pairs. The ideal generated by all length-two values is (C_p).

**Sufficient new result:** construct a p-integral identity expressing an independently known nonzero element in that ideal outside a fixed finite set. Alternatively bound C_p directly through an independent arithmetic realization. The coefficients need not identify one canonical pair or be common across p.

**What cannot be reused as that identity:** the closed cycle with period -2 reduces to the old primitive period and is not the canonical packet. The mixed quotient has an unconstrained XY coordinate under the existing norm maps. The extra finite differences on the actual packet kill its quadratic coefficient. Multipair summation still leaves the factor C_p.

**A legitimate reopening:** a new correspondence or reciprocity relation that controls that mixed arithmetic coordinate, with an inhomogeneous term whose nonzero value does not come from C_p itself. Spell out the exact source cycle, coefficient module, period, and augmentation quotient before manipulating it.

## Interface W: use the genuine four Kato values

The currently supplied sufficient arithmetic test is that at least one of the four genuine source values V_i(p) at weights 5 and 6 is nonzero modulo p^4. It retains the b=3 case. On the retained ordinary domain this forces Sha[p^infinity]=0.

**Available implementation:** the final extractor, exact input schema, finite-ring four-value reconstruction, symbolic functional-equation checks, and genuine Delta calibration. The input source is an integral signed Hida symbol specialized to the prescribed branch, not a weight-two proxy.

**Two distinct possible research tasks:**

1. Construct a certified source-specific finite-precision evaluator that actually provides the required polynomial symbol values, without building an unnecessary full ambient table. A single seed sample can validate that construction, but alone does not advance cofinite support. State what identity or uniform estimate the sample is meant to discriminate.
2. Work symbolically from the exact modular-symbol/Kato source and derive a relation that bounds the simultaneous p^4-divisibility. This can avoid constructing numerical source tables altogether. The key question is what arithmetic datum supplies a constraint beyond homogeneity, functional equation, and the already proved double zero.

**Do not impose an unnecessary gate:** a prime-independent ancestor is one possible solution, not required. The unfinished complex-period comparison is also not compulsory if the cohomological source law is proved. But do not replace the source by an arbitrary function with the same symmetries.

**Discrimination controls:** V_i/p^2 must be kept mod p^2; source normalization units must be controlled; the exceptional Hida domain must be established; fitted matrices do not count as independent identities; a reduction to simultaneous local Wieferich vanishing still needs its own finite-support argument. If a genuine equality with an old witness is derived, classify exactly what new tools it provides before spending further work—mere renaming supplies no new bound.

## Interface G: a genuinely global integral comparison

The repaired regulator carrier is the fixed squared determinant lattice (wedge^2 L)^tensor2, with L=Z P1+Z P2 and the retained finite-denominator model. Its reduction-linear regulator realizations are explicit. The raw G_m-torsor ratio is not such a linear realization.

**New object required:** a modular/arithmetic element in the same fixed rational line together with a lattice and compatible finite realizations that recover the actual C2 coefficients, plus independent nonzero value. A common nonzero rational ratio would then have finite prime support; identifying it as 288 is not required for that cofinite consequence.

**Possible avenues remain open:** a geometric correspondence supplying the two point directions, an integral motivic construction in the correct twist, a deformation comparison carrying cross-p content, or a global determinant map not built by assembling the desired residual scalars. None has been constructed by the tested raw tensor, rationalized augmentation, or BKS-after-finiteness operations.

**First test:** show the scalar action is actually linear on reductions and that the modular section is defined before assuming primary finiteness/BSD/TNC. Writing two names in one abstract one-dimensional vector space is insufficient. A proof may use an applicable theorem as an import, but must show that its hypotheses do not include the endpoint being proved.

## Interface Q: finish the analytic-to-arithmetic comparison

The RS2 Laurent/Poincare object is explicitly constructed and has a normalized pairing with L(f,2)L''(f,1). The real period and saturated Mordell–Weil regulator are separately certified. The missing assertion is their exact comparison, not another expression for the analytic function.

**Sufficient new result:** show q_E belongs to Q with reduced denominator at most174, prove the applicable bounded algebraicity certificate, establish the exact height identity, or produce another rigorous argument for q_E=36. A general rank-two Gross–Zagier theory is not required if a weaker seed-specific theorem suffices.

**First concrete questions:** does the RS2 projection lie in an independently defined arithmetic lattice with a computable scalar bound? Can an algebraic cycle, height pairing, or regulator calculation realize the required functional rather than only its analytic kernel? Can the fixed curve's structure force an exact period relation with a bound strong enough for the existing interval?

**Known limits:** rational Euler factors do not make derivative coefficients algebraic; a finite complex cusp space does not control their field of definition; removed outside logarithms leave internal derivative logarithms. Read the scoped finite-logarithmic no-go hypotheses before reusing a local realization. No need to recompute an already completed Laurent expansion unless a defect is found.

## Interface O: conditional order nine

Assume FIN explicitly. Prove an effective upper bound or support assertion sufficient to exclude #Sha>=25281. This can be an arithmetic size estimate, an explicit annihilator with settled support, an index formula with independent bound, or another construction. Do not presume it must pass through Q36 or an archimedean inequality.

A result closing this implication removes a main endpoint even while FIN is open. The exact exception set and the known 3-primary factor matter. A fixed-p certificate is admissible as a finite necessary step on a route with a separately controlled tail, but is not the default replacement for uniform research.

## Interface P: finite exceptional primaries, kept in their proper role

The BH singleton criteria and 5843 plectic test can discharge actual remaining FIN obligations if their arithmetic witnesses are nonzero. The K167 calibration and seed source/projector components are genuine reusable code. No seed 5843 conclusion follows yet.

These are eligible if Aristotle finds a theorem or evaluator that closes one of those obligations economically, or if a new uniform theorem leaves precisely such a finite residue. The package does not erase them. It also does not authorize a production computation or represent success at 5843 as uniform FIN. A proof of finiteness is not primary vanishing; keep the ORDER9 consequence separate.

## How to choose and continue

Do not select a lane merely because its next local manipulation is easy to verify. State the desired new arithmetic lemma, the existing endpoint implication, and which of the atlas failures the proposed construction changes. Then attempt that construction. If its exact operation is already disproved, stop repeating it; if a repair supplies different arithmetic input, try the repair. If it is simply unproved, investigate it rather than rejecting it for being open.

Use computations to distinguish concrete identities, with genuine inputs and exact/rigorous error controls. Use formal proof to secure a statement that matters to the endpoint. It is acceptable to return a partially proved new arithmetic theorem with a precise surviving gap. It is not acceptable to relabel an old equivalent criterion as the new theorem, or to call a hypothetical arithmetic interface “implemented” because its abstract algebra compiles.


---

Original package file: `guide/05_FORMALIZATION_AND_RETURN_CONTRACT.md`

# Aristotle research and formal proof contract

## Purpose

Find and prove new arithmetic input toward the fixed rank-two seed's BSD endpoint. The package invites theorem discovery and recombination. It does not confine Aristotle to checking previous prose or filling the already completed abstract bridge libraries.

## Start from the actual definitions

Identify which concrete elliptic curve, Galois module, local condition, arithmetic source, lattice, and normalizations the chosen target uses. If mathlib or supplied Lean files lack those definitions, record that boundary. An informal research derivation can be valuable before the whole arithmetic library exists, but it must not be reported as fully machine-verified seed BSD.

Do not introduce an abstract structure with arbitrary `Sha`, `Reg`, `Lsecond`, or `KatoValue` fields and certify the seed merely by proving a tautology about its assumptions. Such abstract deductions may be used as checked bridge lemmas; their actual arithmetic realization remains a separate theorem.

## Existing formal work to reuse

The archive includes the A1 witness-content and A2 primary-support/full assembly libraries, A4/A5 finite-part work, ordinary/supersingular bridge cores, and earlier Run013/H41 developments. Their toolchain manifests, exact sources, frozen statements, axiom/build logs, and boundary reports are retained. Do not assume a historical acceptance receipt applies to modified sources or an updated Lean/mathlib version.

A2 already checks finite iff finite primary groups plus finite support, content ideals, nonzero-integer comparison consequences, square-order algebra under hypotheses, and countermodels. Its theorem `order_nine_t_sq` is conditional and does not establish #Sha=9. Reusing it is encouraged; re-proving it is not a new arithmetic result.

## Imports are allowed, but must be visible

Maintain `ASSUMPTIONS.json` with, for each dependency:

* exact statement and prime/coefficient domain;
* formal theorem identifier or source file, theorem number, version and page;
* grade: kernel checked here, previously kernel checked, exact computation, imported published theorem, imported preprint, retained model-reviewed derivation, or open;
* whether it assumes FIN, primary finiteness, ORDER9, BSD, ETNC, a leading-term conjecture, nonzero witness content, or any equivalent of the target;
* normalization and realization hypotheses;
* proof location or explicit remaining obligation.

A conditional theorem may be returned honestly, but cannot be counted as an unconditional seed result if it introduces an open arithmetic antecedent of the same strength. The normal logical axioms in Lean are distinct from a new mathematical axiom asserting the desired comparison. Both the axiom list and the informal-to-formal statement match must be reviewed.

## What a successful new lemma should show

Write the new theorem before its proof, with every variable quantified. Include the exact chain from that conclusion to a seed obligation. Examples of acceptable outcomes are a cofinite upper bound, a new arithmetic map with a proved independent bound, a source nonvanishing theorem with full prime coverage, an effective order/support bound under FIN, or the necessary exact arithmetic identity for Q36.

A genuinely new intermediate lemma is also useful if it removes a specified missing step on such a construction and the remaining chain is explicit. Do not call it a closing theorem unless it actually supplies the remaining arithmetic premises. Local freeness, correct types, source normalization, and new relations can be real lemmas, but their endpoint effect must be stated without enlargement.

## Required return files

1. `RESULT.md`: strongest new statement actually proved; exact status; endpoint changed or unchanged; remaining gap.
2. `PROOF.md`: complete mathematical derivation in one named convention, with imports placed where used.
3. `ASSUMPTIONS.json`: explicit dependency ledger as above.
4. `COLLISION_CHECK.md`: which atlas cards apply, why this is not the same failed operation, and what genuinely new arithmetic input it uses.
5. `SEED_SPECIALIZATION.md`: apply every hypothesis to this curve, including residual image, local types, finite exceptions, periods and lattice scaling. State any application still conditional.
6. `lean/` with exact source/toolchain/project manifests if formalization was undertaken; include the build transcript and `#print axioms` for the claimed principal theorem. Report `sorry`, `admit`, newly introduced axioms, unsafe/native trust and external-checker boundaries honestly.
7. `checks/` with genuine inputs, producer and checker distinction, exact outputs, and a clear list of synthetic controls. A statistical fit is not an exact identity.
8. `HANDOFF.md`: next unresolved arithmetic step, not a generic request to prove BSD again.
9. `MANIFEST.sha256`: hashes of the returned immutable source/evidence files, plus identification of the input package used.

Suggested statuses are `FULL_SEED_BSD_PROVED`, `UNIFORM_SUPPORT_PROVED`, `CONDITIONAL_ORDER9_PROVED`, `Q36_PROVED`, `NEW_ARITHMETIC_LEMMA`, `PARTIAL_CONSTRUCTION`, `TESTED_CANDIDATE_REFUTED`, or `NO_NEW_ARITHMETIC_INPUT`. These labels are claims to review, not automatic acceptance. In particular `FULL_SEED_BSD_PROVED` needs the actual curve definitions and all three endpoints, not a conditional bridge theorem.

## Stop, repair, or redirect

Do not spend a run repeatedly proving that a known failed operation fails. If the atlas provides an exact obstruction to the chosen operation, change the arithmetic input or method. If an obstruction is repairable, attempt the repair and retain the original error and corrected conclusion. If the candidate survives but remains unproved, continue on the substantive theorem; an open theorem is not an automatic kill condition.

When a run ends without a new theorem, return the actual attempted construction and first unresolved equation. Do not invent novelty, promise an easy successor, or declare an entire field impossible from a bounded test. No raw data campaigns, paid computations, messages, scheduling, repository mutation, or external submissions are authorized by an archived prompt.

## Platform use

The official Aristotle page, checked for this handoff, describes English-problem input and work inside Lean projects/repositories. The publisher's SDK page describes project submission and document formalization. This package is therefore provided as an English research handoff with complete source context, not as a fake prebuilt Lean proof whose arithmetic is axiomatized away.

Official references: https://aristotle.harmonic.fun/ and https://pypi.org/project/aristotlelib/ (checked 2026-10-05). No attachment limit, job runtime, automatic reading of private GitHub links, or current Lean version is assumed. Supply the unpacked files through the interface actually available. The package itself does not launch a job, use an API key, or change the user's subscription.


---

# Coverage, omissions, and custody — read before claiming completeness

This is a broad captured BSD record with explicit boundaries, not a claim to have
proved every included statement or searched every inaccessible byte on the machine.
The inventory covers 4,179 discovered roots, reduced to 544 nonoverlapping directory
walks plus individually cited files. An additional pass recovered conversation
attachments and the visible user/assistant research record.

## Actual coverage

| Item | Count / disposition |
|---|---:|
| Original path identities in final catalog | 538,072 |
| Unique embedded byte objects | 283,307 |
| Bytes in those unique objects before compression | 7,024,429,358 |
| Lossless evidence volumes | 84 |
| Earlier compendium units, preserved in full | 7,042 |
| Compendium evidence references checked | 22,794 |
| File citations whose bytes are embedded | 22,725 |
| Directory / repository citations with captured descendants | 69 |
| Unresolved compendium citation paths | 0 |
| Current governing reading-room source files | 54 |
| Directly browsable current dossier files | 5,043 |
| Historical stop/correction units reproduced in full | 3,353 |
| Released claim statements with dependencies | 89 |
| Visible conversation messages preserved | 1,719 |
| Verified local Git histories | 3 bundles, 12 parts |

The original compendium, extracted units, quote/correction fields and all located
source versions remain separate. Identical bytes are deduplicated by SHA-256;
every original filename remains an alias. Different versions are never merged
because they happen to share a name.

## The scientific bytes that are external

**Raw binary computation stores larger than 1 MiB are not embedded.** Their 14,047
regular-file inventory entries total 156,808,997,323 bytes, including repeated
copies. There are 12,989 distinct digests totaling 143,585,239,078 bytes. Each was
freshly hashed from the local file during this build. Their paths, sizes, digests
and disposition are in `BULK_BINARY_RECEIPTS.jsonl.gz` and the catalog. Another
23,686 symlink aliases point to those external hashed files.

Their source producers, retained checkers, recorded results and custody manifests
are included when present in the discovered roots. A hash is not the binary data
and is not a replay. A run requiring those raw bytes must obtain them from the
recorded local source or regenerate them under the original contract. `record.py`
can explicitly restore verified local bulk files with `--include-bulk-from-local`.
This package alone cannot replay a calculation requiring an external corpus.

## Missing old upload paths

Five old temporary ZIP paths no longer exist. Each corresponding extracted dossier
was located and captured. `EXPIRED_UPLOAD_RECOVERY.json` lists the missing ZIP and
every matched surviving member. We do **not** claim to have recovered the original
ZIP bytes, its exact member order, or any absent member solely from a folder name.
The original source-binding/check records remain available for that comparison.

## Deliberate non-research exclusions

27 credential/OS metadata paths and 337 regenerable compiled outputs were excluded.
129 runtime/VCS/cache or symlink-directory locations were pruned by the published
discovery policy. Sources, toolchain identifiers and recorded build logs are kept;
the complete Lean/Python/Sage installations and package caches are not bundled.
The three principal local repositories additionally have verified full-ref Git
bundles. Other Git internals are not recursively copied. No un-fetched remote branch
or inaccessible cloud-only artifact is asserted to be present.

All 44,952 file symlinks were resolved to either an embedded digest (21,266) or an
external hashed digest (23,686). Original symlink identities and targets remain in
the catalog. The restoration tool uses verified bytes rather than creating
arbitrary filesystem links.

## Discovery scope

Discovery includes BSD/K167-named home projects; BSD-related Desktop, Downloads
and Documents material; the compendium's cited projects and slice inventory;
the current/release/cloud lab trees; this conversation's accessible remote
attachments; the exact older pasted attachments named by the user; and an explicit
supplement for the partially written earlier Aristotle handoff. Read
`DISCOVERY_ROOTS.json`, `PRUNED_DIRECTORIES.json`, and the complete compressed file
inventory for the exact boundary. This is not a forensic image of the entire Mac.

No source read errors or files changing during their individual capture were
reported. Captures are a file-by-file snapshot, not an atomic freeze of all work
on the computer. The source-stability check, when present, reports later changes
without silently replacing the captured identity.

## Search versus possession

All 538,072 paths are filename searchable. The compact full-text index covers
23,674 unique scientific prose/code objects, with a 2 MiB prefix
limit recorded per object. Vendor library sources and raw numeric tables are not
full-text indexed; embedded bytes remain retrievable in full. Search absence is
not evidence that the underlying mathematical item is absent.

## What verification means here

Source hashes, copied-source bindings, evidence-volume integrity, byte-for-byte
retrieval, citation coverage, complete unit counts, and Git bundle verification
are custody checks. They do not independently validate 283,307 mathematical files.
The new 44-card wall atlas is a source-linked synthesis, not a fresh referee report
for every theorem. Existing proof, review, computation, conjecture and formal
verification grades are retained. The three seed endpoints are unchanged.

The final coverage check also captured a [concurrent Aristotle draft](sources/concurrent_aristotle_draft/CAPTURE_READ_FIRST.md) with 37 additional files, including its newer wall atlas and Lean templates. These are a separate timestamped snapshot with no new proof promotion.
