# Post-review source note (2026-09-16) — does NOT modify PROOF.md (rev 3, sha256 71024db1ca0893ac...)
Hardens the one load-bearing remark (referee_2 D12 / gate G4 remark): the Atkin–Lehner relation used for the Fricke sign in sec 3 (L2).
SOURCE (read verbatim by the author; PDF and text in post_review_sources/):
  A. Agashe and M. Winters, "Reducibility and rational torsion in elliptic curves", https://www.math.fsu.edu/~agashe/math/red.pdf.
  Standing setup: A an optimal elliptic curve over Q of squarefree conductor N, f its newform; w_p = sign of the Atkin–Lehner involution W_p on f.
  Lemma 2.1 (second clause, independent of the auxiliary prime r): "for all primes p | N, we have a_p(f) = -w_p." Proof: "a_p(f) = -w_p because
  U_p = -W_p on the new subspace of S_2(Gamma_0(N), C)."
APPLICATION: H41 conductors are squarefree (N = 6l positive, 2p negative). PROOF.md sec 2 derives a_2 = 1, a_3 = a_l = -1 (positive) and a_2 = 1,
  a_p = -1 (negative). Hence w_v = -a_v and epsilon_N(f) = prod_{v|N} w_v = (-1)(+1)(+1) = -1 (positive) and (-1)(+1) = -1 (negative): the full Fricke
  sign used in L2. (The Monsky 2-parity cross-route in ERRATA_AFTER_REVIEW.md remains an independent, unreviewed confirmation.)
SIDE CONFIRMATION: the same paper's Proposition 2.2 (citing Agashe 2018, Prop 2.1): for squarefree N and delta_p in {1, p} with delta_p = 1 for at
  least one p, there is a weight-2 Eisenstein eigenform on Gamma_0(N) with a_l = l + 1 (l !| N) and a_p = delta_p (p | N) — the comparison forms E+
  (delta = (1, 3, l)) and E- (delta = (1, p)) of PROOF.md sec 2.
