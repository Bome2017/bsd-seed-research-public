# Exact authentication of the 389 coefficient-five compact units

Status: **ACTUAL_UNITNESS_AUTHENTICATED_INDEPENDENTLY_OF_GRH**. This does not certify a fundamental-unit basis or any class group.

The saved 389 BNF supplies thirteen free-unit candidates as compact products. For each of the 317 distinct factors, `authenticate.gp` computes its principal fractional ideal in the saved maximal order and records an exact ideal factorization. It checks the literal reconstruction of every factor ideal. Across 295 finite-prime ideals, it forms the divisor matrix D and the matrix E of **full integer exponents**, without reducing exponents modulo five. The exact product is

    D E = 0.

Thus each of the thirteen compact products has trivial principal fractional ideal and is an actual unit. The proof does not assume GRH, the provisional class number three, completeness of the listed units, or a known Selmer/Sha dimension. The saved maximal order and field are the parent's exact number-field input.

The original computation completed in 17.33 seconds with peak observed RSS 136 MB, below the sealed 60-second/1GiB bound. Its completion marker is present and stderr is empty. `AUTHENTICATION_DATA.gp` retains the factor elements, ideal bases, divisor matrix, full exponent matrix, and zero product.

`replay.gp` performs a separate literal check of those ideal identities and reassembles the full exponent matrix from the source compact products. It refactors the small principal factors and needs no BNF, class-number computation, or fundamental-unit assumption. An initial generic-HNF replay hit its separate time cap and is preserved in `rejected_hnf_replay/`; `REPLAY_REPAIR.md` explains the representation-only repair. Ideal reconstruction plus D E=0 suffices: the individual recorded ideal factors need not be assumed prime for this verification.

Consequently scalar translates and integral products of these candidates—including the parent's character projector—are authenticated units. A nonzero finite-residue incidence norm on any such projected unit supplies a lower bound on the actual norm-map rank. That fact, combined with the independently known ambient character-unit rank, can yield an upper bound for its kernel. This packet authenticates unitness only; the parent's norm evaluation and ordinary class-supported contribution remain separate inputs.
