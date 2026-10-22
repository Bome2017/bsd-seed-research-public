# Sources and custody

The governing seed endpoint was reread from
/Users/bsm/BSD_CODEX6_MASTER_HANDOFF_2026-09-19/MASTER_BSD_DAG.md.
Current lab state and parent proofs were read at
d61b2af9653be14e1da758ae81f26209bde2a117.

Per-lane SOURCE_BINDINGS/INPUT_BINDINGS files record actual source hashes.
They are not independent certifications of the historical mathematical inputs.
The original 2026-10-15 contract remains unchanged. Its mistaken reference
to bnfisintnorm was immediately corrected in CERTIFICATION_CLARIFICATION.md;
that function is not used as a class certificate.

Primary sources checked:

- PARI, General number fields, class groups and GRH, bnfinit, bnfcertify:
  https://pari.math.u-bordeaux.fr/dochtml/html-stable/General_number_fields.html
  Reopened October17. In particular bnfcertify(flag1) certifies a class
  quotient, not a fundamental-unit basis; an alarm is not success.
- Torzewski, Regulator constants of integral representations of finite groups,
  arXiv1703.10602, targeted source screen in general_character/PROOF.md.
  https://arxiv.org/abs/1703.10602
- Schaefer--Stoll descent source convention and the earlier incidence index
  theorem remain imported from pinned project audits. A fresh attempted
  retrieval of the old Bayreuth PDF URL failed; no new primary-source audit
  is claimed on that account.

The compact candidate units are used only after exact ideal identities
authenticate unitness. The new unit upper bound does not import their
fundamentalness. Class-group completeness is separately conditional.

The October17 continuation made no new BNF from scratch. It resumed the
saved class inputs, tried one separately sealed source quotient certificate,
and performed compact-unit/finite-field arithmetic. Earlier October15
bounded BNF/certification attempts and convention failures are preserved.
