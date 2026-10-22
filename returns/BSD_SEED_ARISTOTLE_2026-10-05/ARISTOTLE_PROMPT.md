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
