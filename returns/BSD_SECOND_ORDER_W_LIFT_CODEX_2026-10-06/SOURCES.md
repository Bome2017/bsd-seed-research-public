# Sources, retained inputs, and claim grades

## Primary sources read in this turn

1. Adam Morgan and Alexander Smith, *The Cassels--Tate pairing for finite
   Galois modules*, arXiv:2103.08530v3.
   https://arxiv.org/html/2103.08530
   https://arxiv.org/pdf/2103.08530
   Read Definition 1.1 and the following exactness convention, Theorem 1.3
   (kernels, duality, naturality), and Proposition 4.4 (Baer sums).
   These supply the pairing formalism. The M4 comparison, second-order
   correction criterion, and arithmetic realization tests are derived here;
   the paper is not cited as already proving those statements for this seed.

2. J.S. Milne, *Class Field Theory*, version 4.03 (2020).
   https://www.jmilne.org/math/CourseNotes/CFT.pdf
   Chapter I, Theorem 1.1 and §§1.8--1.11, printed pages 20 and 23--24,
   PDF pages 28 and 31--32 (zero based): local reciprocity, the unit
   filtration, and abelian inertia. The local finite-inertia calculation
   and the power-series torsion argument are written in this return.

Howard's *Derived p-adic heights and p-adic L-functions*
(https://arxiv.org/abs/1202.6343) was located as related literature.
It is NOT used as a theorem: its Iwasawa/local hypotheses are not silently
transferred to our tame finite-module setting. Alternation is proved
directly using Morgan--Smith and M4 instead. No novelty claim is made.

## Retained inputs

- Stage-A arithmetic span and seed assumptions: bound copies in input/.
- Pro's review: bound copy in input/; an assessment, not formal verification.
- The concurrently uploaded Aristotle return and revised task:
  lab e7abad93, copied and bound. Read, not independently certified here.
- `input/OPENAI_04_VERTICAL.tex`: byte copy of the prior pinned manuscript
  source (OpenAI math adc7f1241b42e322a6451854ab7e4b4c146bf78a). Its opening
  distinguishes moving tame conductors from the true torsion-free variable.
  No theorem from this manuscript is imported into the new proofs.

INPUT_BINDINGS.json records exact local origins and SHA-256 values.

## Scope of the checks

`checks/check_second_order.py` uses only the Python standard library.
It checks truncated character multiplicativity, the J_n signs and Galois
similitude, the common-correction cokernel, finite-order tame failures,
and the cyclotomic coordinate change. Its formal obstruction model is
not claimed to be realized by this curve. Counts are in checks/RESULTS.json.

The written proofs and source hypotheses require independent review.
No assertion about a seed value follows by extrapolating the controls.
