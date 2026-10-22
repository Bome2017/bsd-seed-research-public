# BSD seed return — October 12, 2026

**SHARPER_CONDITIONAL_CERTIFICATE_DERIVED; NO_NEW_PRIMARY_RESULT.**

Start with `REPORT.md`; the complete mathematical argument is in `PROOF.md`.

The strengthened sufficient criterion is

\[
 \delta_p\ne0,\qquad m_p-w_p-b_p\le1
 \quad\Longrightarrow\quad\Sha(E/\mathbb Q)[p^\infty]=0,
\]

under the retained integral Kato/cohomological inputs. The new term is the actual first-Bockstein image index in primitive `H^2_tf`. No main-conjecture equality is assumed. The stronger premise has not been verified for an additional seed prime.

Run the exact controls with `python3 checks/test_certificate.py` and the example with `python3 refined_certificate.py examples/abstract_improved.json`. Standard library only, Python 3.10 or later. The executable never authenticates a seed source or reports a new seed theorem.

`SOURCES.md` and `INPUT_BINDINGS.json` give repository provenance. `HANDOFF.md` isolates the remaining integral normalization interface. `MANIFEST.sha256` binds this package's files. Both remote repositories were left unchanged.
