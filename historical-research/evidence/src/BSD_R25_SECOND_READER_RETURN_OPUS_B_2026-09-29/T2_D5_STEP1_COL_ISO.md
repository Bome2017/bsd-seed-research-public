# T2 — D5 Step 1: Col : H^1_Iw(Q_3,T)/H^1_Iw(Q_3,T^0) -> Lambda is an isomorphism.  VERDICT: PASS
T^0 = T_3E^ = Z_3(1)(x)eta, T/T^0 = Z_3(eta), eta unramified quadratic (seed: I_2 nonsplit at 3, a_3 = -1; PARI
elllocalred gives Kodaira code 6 = I_2). k_n = Q_3(zeta_{3^{n+1}})^Delta, totally ramified of degree 3^n.

## (a) Vanishing — DERIVED (duality THEOREM: Kato 12.2, p.220 "H^2_loc(T) ~ Hom(H^0(Q_p(zeta_{p^inf}), Hom_{Z_p}(T,Q/Z)), Q/Z)(-1)")
Key fact: eta is non-trivial on G_{Q_3(mu_{3^inf})} and on every G_{k_n} (a totally ramified field contains no unramified
quadratic extension). Hence for M in {Q_3/Z_3(eta), mu_{3^inf}(x)eta}: an invariant x satisfies -x = x, so x = 0.
Consequences: H^2_Iw(T^0) = H^2_Iw(T/T^0) = H^2_Iw(T) = 0, and for every n: H^0(k_n,T^0) = H^2(k_n,T^0) = 0 and
H^0(k_n,Z_3(eta)) = H^2(k_n,Z_3(eta)) = 0 (H^2 dual to H^0 of Q_3/Z_3(eta), resp. mu_{3^inf}(x)eta). R25 (a): correct.
## (b) — DERIVED. Local Euler characteristic: rank_{Z_3} H^1(k_n, M) = 3^n for M = T^0, T/T^0; torsion of H^1(k_n,M) is
the image of H^0(k_n, M (x) Q/Z) = 0. T/T^0 = Hom(T^0, Z_3(1)) (eta^2 = 1), so Tate's pairing
H^1(k_n,T^0) x H^1(k_n,T/T^0) -> H^2(k_n,Z_3(1)) = Z_3 is perfect (free modules, H^0 = H^2 = 0 on both sides). Correct.
## (c) Kummer map E^(m_n) -> H^1(k_n,T^0) is ONTO — DERIVED (the cokernel argument holds)
Formal-group Kummer sequence (E^[3^m] -> E^(m-bar) -> E^(m-bar) exact, [3] an isogeny of height 1):
  0 -> E^(m_n)/3^m -> H^1(k_n, E^[3^m]) -> H^1(k_n, E^(m-bar))[3^m] -> 0.
Inverse limit (Mittag-Leffler, finite groups): 0 -> E^(m_n) -> H^1(k_n,T^0) -> T_3 H^1(k_n, E^(m-bar)) -> 0
(E^(m_n) is a finitely generated Z_3-module, 3-adically complete; E^(m_n)[3] = H^0(k_n, mu_3(x)eta) = 0).
rank E^(m_n) = [k_n:Q_3] = 3^n (log is an isomorphism on an open subgroup) = rank H^1(k_n,T^0). So the cokernel is
finite and a Tate module (torsion-free), hence 0. R25's "Tate module of rank 0, hence 0" is exactly right.
## (d) Z_3[Gamma_n]-freeness — DERIVED (sharper form of R25's norm argument)
Hochschild-Serre for k_n/Q_3 with H^0(k_n,T^0) = H^2(k_n,T^0) = 0 degenerates: H^p(Gamma_n, H^1(k_n,T^0)) = H^{p+1}(Q_3,T^0),
which is 0 for p >= 1 (cd = 2 and H^2(Q_3,T^0) = 0); the same over every k_m. Gamma_n cyclic, so H^1 = H^2 = 0 for every
subgroup gives cohomological triviality; Z_3-free + cohomologically trivial => projective (Nakayama-Rim, Serre Local
Fields IX, SECONDARY) => free of rank 1 over the local ring Z_3[Gamma_n]. Cores: H^1(k_n,T^0)_{Gamma_n} -> H^1(Q_3,T^0)
is onto (its cokernel is dual to H^1(Gamma_n, H^0(k_n,T/T^0)) = 0), both sides are Z_3 of rank 1, so it is an iso.
Nakayama: c_n generates iff cores(c_n) = c_0 generates H^1(Q_3,T^0) = E^(3Z_3). Norm-compatibility of (c_n) follows
from Tr L_n = L_{n-1} (checked exactly n <= 2) and injectivity of log on the torsion-free E^(m_n). Correct.
## (e) c_0 generates E^(3Z_3) — DERIVED + COMPUTED
- For any formal group over Z_3 (height 1 here), log and exp are inverse isomorphisms E^(m^r) <-> m^r for
  r > v(3)/(3-1) = 1/2 (Silverman AEC IV.6.4, SECONDARY); r = 1: log : E^(3Z_3) ~ 3Z_3. So E^(3Z_3) = Z_3 . c with
  v_3(log c) = 1, and an element generates iff v_3(log) = 1. log c_0 = L_0 = 3/2 (forced by the trace relation,
  independent of the realisation in D1.2), v_3 = 1: c_0 is a generator. The sign of log c_0 is irrelevant.
- PARI on the seed's minimal model (checks/ksr12.log): t = exp_{E^}(3/2) has v_3(t) = 1 and log_{E^}(t) = 3/2 + O(3^23)
  (truncation at 40 terms); formal-log coefficients c_n satisfy v_3(c_n) >= -v_3(n) (integral formal group).
- Hence {c_n^sigma} is a Z_3-basis of H^1(k_n,T^0), Col_n : H^1(k_n,T/T^0) -> Z_3[Gamma_n] is an isomorphism by (b), and
  H^1_Iw(T)/H^1_Iw(T^0) = H^1_Iw(T/T^0) (H^2_Iw(T^0) = 0; injectivity since H^0(k_n,T/T^0) = 0). Limit: Col is an iso.
## Cross-check at source — THEOREM (Kato Lemma 17.12, rendered pp.277-279)
"Let L be a finite extension of Q_p, and let T be an invertible O_L-module endowed with a continuous unramified
O_L-linear action of Gal(Q_p-bar/Q_p) such that H^0(Q_p,T) = 0. ... Then L : H^1_loc(T(1)) -> H_{inf,L} induces an injection
H^1_loc(T(1)) -> O_L[[G_inf]] whose cokernel is a finite group." Kato's proof bounds the cokernel by
H^1(F_p,T) = Coker(Frob_p - 1; T); for T = Z_3(eta) this is Z_3/(-2) = 0. So Kato's own proof also gives cokernel 0
here (17.11 applies it to T''(k-1) = Z_3(eta), the unramified QUOTIENT of V_{F_lambda}(f*)(k) = V_3E(1) twisted down;
H^1_loc(T''(k)) is R25's H^1_Iw(T/T^0) up to the Tate twist (1)). Consistent.
## Nothing found to break Step 1. (Delta-trivial branch as in R25; the other branch is identical and unused.)
