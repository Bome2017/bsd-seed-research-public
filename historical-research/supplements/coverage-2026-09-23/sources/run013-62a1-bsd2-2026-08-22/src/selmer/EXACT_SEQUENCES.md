# Full 2-Selmer and Sha consequences

Status: proved from the two Selmer identities; independent review PASS.

Let `E=E_q` and `E'=E'_q`.  The isogeny Kummer sequences are

\[
0\to E'(\mathbf Q)/\phi E(\mathbf Q)
 \to\operatorname{Sel}^{\phi}(E/\mathbf Q)
 \to\Sha(E/\mathbf Q)[\phi]\to0,
\]

\[
0\to E(\mathbf Q)/\widehat\phi E'(\mathbf Q)
 \to\operatorname{Sel}^{\widehat\phi}(E'/\mathbf Q)
 \to\Sha(E'/\mathbf Q)[\widehat\phi]\to0.
\]

Compatibility with multiplication by `2` gives

\[
0\to
 \frac{E'[\widehat\phi](\mathbf Q)}{\phi(E[2](\mathbf Q))}
 \to\operatorname{Sel}^{\phi}(E/\mathbf Q)
 \to\operatorname{Sel}_2(E/\mathbf Q)
 \to\operatorname{Sel}^{\widehat\phi}(E'/\mathbf Q).
\]

Here `E[2](Q)=ker(phi)`, so its image under `phi` is trivial, while
`E'[widehat(phi)](Q)` has order `2`.  If the proved Selmer groups have orders
`4` and `1`, exactness gives

\[
 \#\operatorname{Sel}_2(E/\mathbf Q)=2.
\]

The full Kummer sequence

\[
0\to E(\mathbf Q)/2E(\mathbf Q)
 \to\operatorname{Sel}_2(E/\mathbf Q)
 \to\Sha(E/\mathbf Q)[2]\to0
\]

and `dim E(Q)[2]=1` force

\[
 \operatorname{rank}E(\mathbf Q)=0,
 \qquad \Sha(E/\mathbf Q)[2]=0.
\]

Any nonzero finite or torsion 2-primary group contains an element of order
`2`, hence

\[
 \Sha(E/\mathbf Q)[2^\infty]=0.
\]

The first two Kummer sequences also yield

\[
 \Sha(E)[\phi]=0,
 \qquad
 \Sha(E')[\widehat\phi]=0.
\]
