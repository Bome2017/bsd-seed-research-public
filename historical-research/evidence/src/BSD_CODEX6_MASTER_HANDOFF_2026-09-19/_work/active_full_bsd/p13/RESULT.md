# Completed certified C13 result

**SHA13_ZERO_PROVED_COMPUTER_ASSISTED — 2026-09-21.**

The [qualified theorem](../../../audits/P13_PRIMARY_THEOREM.md) proves

\[
C_{13}=2\pmod{13}\quad(\omega_1),\qquad
C_{13}=1\pmod{13}\quad(\Omega_E=2\omega_1),
\qquad \Sha(E/\mathbf Q)[13^\infty]=0.
\]

The exact weighted sum is -3950. Both the Fermat-quotient functional and the full depth-two measure give residue2, with 179 checks passing. The same code recovers the retained results at7 and11.

The external return's 7 and8 are fully reconciled: both summed lattice numerators rather than the symbols, and the alternative weights additionally omitted alpha^-2. The corrections are 7*4=2 and 8*4*9=2 modulo13. See [NORMALIZATION.md](NORMALIZATION.md).

All 3,281 coefficient/verifier files were freshly hash-checked, including 2,333 reused files against pre-incident C11 bindings. All 948 new witness files were bound to their original receipts and checked. All 17,605 Arb work units passed custody/coverage checks. Recombining the complete saved units with the unchanged engine and rerunning Stage C reproduced both original Arb outputs and all symbols byte for byte. See [COMPLETION_REVIEW.json](COMPLETION_REVIEW.json), [DOWNSTREAM.json](DOWNSTREAM.json) and [CERTIFICATE_BINDINGS.json](CERTIFICATE_BINDINGS.json).

The write-through incident is preserved and qualified in the theorem. The numerical corpus, witness-verifier receipts and imported theorem qualifications remain the trust base; no fresh full integer-verifier replay, independent numerical implementation, human review or Lean verification is claimed.

Under FIN the current consequence is #Sha=9*t^2 with gcd(t,30030)=1; the next possible order after9 is2601. FIN, total order9 and q=36 remain open. No I3 or auxiliary-twist primary result is supplied. This completed run has no successor.
