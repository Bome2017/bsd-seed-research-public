## 2. The statement proved here

Throughout, [TZ] = Tao–Ziegler, *Polynomial patterns in the primes*, arXiv:1603.07817v1; all
numbers are v1's (see §0 for the published-version concordance). Notation is [TZ]'s: `[N] = {1,…,N}`,
`E` = average, `Λ_p(n) = (p/(p−1))·1_{n≢0 (p)}`, `β_p` the local factor (1.2).

**Lemma A (Theorem 1.4 with the additive variable in a fixed residue class).**
Let `d, r, k`, `P_1,…,P_k ∈ Z[m_1,…,m_r]`, `N`, `M = M(N)` satisfy the hypotheses of [TZ, Theorem 1.4]
(degree ≤ d, degree-d components pairwise distinct, `M = o(N^{1/d})`, `M ≥ ω(N) N^{1/d}` with `ω → 0`
sufficiently slowly). Fix an integer `q ≥ 1` and a residue `a ∈ Z`. Then

    E_{n∈[N]} E_{m∈[M]^r} 1_{n ≡ a (mod q)} Λ(n+P_1(m)) ⋯ Λ(n+P_k(m))
        = (1/q) · ∏_{p | q} β_p^{(a)} · ∏_{p ∤ q} β_p  +  o_{N→∞}(1),

where for `p | q`

    β_p^{(a)} := E_{m ∈ (Z/pZ)^r} Λ_p(a+P_1(m)) ⋯ Λ_p(a+P_k(m)).

The function `ω` and the `o(1)` may depend on `q, a` in addition to `d, r, k, P_i`. No hypothesis on
`M, N` is changed. Nothing is assumed about `q`: it may be a prime power, and `a` need not be
coprime to `q` (if it is not, one of the factors `β_p^{(a)}` may vanish, which is the correct answer).

**Corollary A′ (qualitative form).** If in addition `β_p^{(a)} ≠ 0` for every `p | q` and
`β_p ≠ 0` for every `p ∤ q` (i.e. there is `m mod p` with `p ∤ a+P_i(m)` for all `i` when `p | q`,
and `(n,m) mod p` with `p ∤ n+P_i(m)` for all `i` when `p ∤ q`), then there are infinitely many
`(n, m_1,…,m_r) ∈ N^{1+r}` with `n ≡ a (mod q)` and `n+P_1(m),…,n+P_k(m)` simultaneously prime.

*Proof of A′ from A.* `β_p = 1 + O(1/p²)` for large `p` (quoted in [TZ] after (1.2) from
[TZ08, Lemma 9.5]), so `∏_{p∤q} β_p` converges to a nonzero limit; the main term is positive; the
prime-power contribution is negligible exactly as in the proof sketch of [TZ, Corollary 1.5]. ∎

Sanity check of the shape of the main term: summing the right-hand side over `a ∈ Z/qZ` gives
`(1/q)∑_a ∏_{p|q} β_p^{(a)} · ∏_{p∤q} β_p = ∏_p β_p` by CRT and the definition (1.2), i.e. the
unrestricted asymptotic of Theorem 1.4.

## 3. Proof of Lemma A

### 3.1 Standing parameters (unchanged from [TZ, §3 and §5])

Rename the `N` of Lemma A as `N′` and `M(N′)` as `M′`, as [TZ, §5] does. Take the parameters
`d, r, D, d_0, D_*, κ, w = w(N′), W, N, A, R, M` exactly as in the bullet list opening [TZ, §3], with
`d_0 := d` (this is the case used in [TZ, §5]), and with `D := k` when some `P_i` is constant (only
configuration (C1) below is then used, with exactly the printed number of nodes; this is the
handoff's case) and `D := k+1` otherwise (configuration (C2) adjoins one node). `D` is only a
bookkeeping constant on which `D_*, κ` may depend; [TZ, Theorem 4.4] is stated for systems with at
most `C_0` nodes, so Theorem 4.1 and Corollary 5.1 remain available for fewer than `D` nodes.
In particular

    W := ∏_{p ≤ w} p                                           (3.1)
    A := W^{1/κ},   R := N^κ                                   (3.2)
    Λ′_{b,W}(x) := (φ(W)/W) Λ′(Wx+b)  for x ∈ [R,N] ⊂ Z/NZ, and 0 otherwise    (3.3)

`W` remains the squarefree primorial; **it is never replaced.** Three harmless adjustments to the
free parameters:

* (P1) Since `w → ∞`, for `N′` large every prime factor of `q` divides `W`. Put
  `g := gcd(W, q) = rad(q)` and `q′ := q/g` (so `q′ = 1` iff `q` is squarefree; for `q = 8`, `g = 2`,
  `q′ = 4`). Note `rad(q′) | W` and `gcd(W/g, q′) = 1`.
* (P2) Take `N := q′ ⌊N′/(q′W)⌋` instead of `⌊N′/W⌋`. This changes `N` by less than `q′`, so that
  `q′ | N`. Sections 3–4 of [TZ] use `N` only as "a large integer from which `R, A, M` are defined",
  and the approximation step of [TZ, §5] (progressions `{n′ ≡ b (W)} ∩ [N′]` vs `{Wn+b : n∈[N]}`)
  is affected by `O(q′W)` elements out of `≍ N′/W`, i.e. by `o(1)`.
* (P3) "`w` sufficiently slowly growing" is taken to include `q′W ≤ log N`. Since
  `W = e^{ϑ(w)} ≤ 4^w`, `w ≤ ½ log log N` suffices for `N` large depending on `q`. [TZ] already
  requires `w` slow enough for the prime number theorem in progressions modulo `W` (used in §5 for
  Theorem 1.6) and for (3.7), so this is the same kind of condition.

### 3.2 The `W`-trick of [TZ, §5], with the weight carried along

Follow the paragraph of [TZ, §5] beginning "With this corollary and the `W`-trick" step by step; the
indicator `1_{n′ ≡ a (q)}` is bounded by 1 and all summands are nonnegative, so every `o(1)` bound
used there survives multiplication by the indicator.

* (a) *Truncating the Euler product.* As in [TZ], `∏_{p>w} β_p = 1+o(1)`, so it suffices to prove

      E_{n′∈[N′]} E_{m′∈[M′]^r} 1_{n′≡a (q)} ∏_i Λ(n′+P_i(m′)) = (1/q) ∏_{p|q} β_p^{(a)} ∏_{p≤w, p∤q} β_p + o(1).

* (b) *Prime powers.* Replace `Λ` by `Λ′` (restriction to primes); the discarded contribution is
  `o(1)` (power saving), as in [TZ].
* (c) *Residue classes modulo `W`.* Split `n′ ≡ b (W)`, `m′ ≡ c (W)`, `b ∈ [W]`, `c ∈ [W]^r`.
  Call `(b,c)` admissible if `gcd(b+P_i(c), W) = 1` for all `i`. Inadmissible pairs contribute
  `o(1)` exactly as in [TZ] (a form divisible by some `p ≤ w` is prime only if it equals that `p`).
* (d) *The congruence on `n′` becomes a congruence on the `W`-tricked variable.* For `n′ = Wn+b`:
  `Wn + b ≡ a (mod q)` has a solution `n` iff `b ≡ a (mod g)`; when it has, it is equivalent to

      n ≡ a′(b) (mod q′),   a′(b) := (W/g)^{-1} · (a−b)/g   (mod q′),

  a single residue class modulo `q′`, because `gcd(W/g, q′) = 1`. Admissible pairs with
  `b ≢ a (g)` contribute exactly `0`.
* (e) *Approximation by progressions.* For admissible `(b,c)` with `b ≡ a (g)`, approximate
  `{n′∈[N′]: n′≡b (W)}` by `{Wn+b : n∈[N]}` and `{m′∈[M′]^r : m′≡c (W)}` by `{Wm+c : m∈[M_0]^r}`,
  `M_0 := ⌊M′/W⌋`, with multiplicative and additive errors `o(1)` (as in [TZ]; (P2) is absorbed
  here). It therefore suffices to show, **uniformly in admissible `(b,c)` with `b ≡ a (g)`**,

      (5.1)^w   E_{n∈[N]} E_{m∈[M_0]^r} 1_{n≡a′(b) (q′)} ∏_{i=1}^k Λ′(Wn+b+P_i(Wm+c))
                    = (1/q′) (W/φ(W))^k (1+o(1)).

  This is [TZ, (5.1)] with the indicator inserted and `1` replaced by `1/q′`.
* (f) *Passage to `Λ′_{b_i,W}` on `Z/NZ`.* As in [TZ]: `Wn+b+P_i(Wm+c) = W(n+R_i(m)) + b_i` with
  `b_i ∈ [W]` coprime to `W` and `R_i ∈ Z[m_1,…,m_r]` of degree ≤ d, coefficients ≤ A, and
  `R_i − R_j` of degree exactly `d` for `i ≠ j`. (If `P_{i_0}` is constant then `R_{i_0}` is a
  constant `t_{i_0}`; otherwise `deg R_i = deg P_i`, since `P_i(Wm+c)` has the same degree as `P_i`.)
  For `n ∈ [N]` outside `n = o(N)` and `n = N−o(N)` all `n+R_i(m)` lie in `[R,N]`; the boundary
  `n` contribute `o((W/φ(W))^k)` by an upper-bound sieve (unchanged). Hence by (3.3), and using
  `q′ | N` so that `1_{n≡a′ (q′)}` is a well-defined function on `Z/NZ` compatible with the
  embedding `[N] ↪ Z/NZ`, (5.1)^w is equivalent to

      (★)   E_{x∈Z/NZ} E_{m∈[M_0]^r} 1_{x≡a′ (q′)} ∏_{i=1}^k Λ′_{b_i,W}(x+R_i(m)) = 1/q′ + o(1),

  which is Lemma B below. (For `q′ = 1`, (★) is literally [TZ, Corollary 5.1].)
* (g) *Assembly.* Granting (★), the left side of (a) equals

      ∑_{(b,c) admissible, b≡a (g)} W^{-(r+1)} · (1/q′) (W/φ(W))^k (1+o(1)) + o(1)
      = (1/q′) (W/φ(W))^k W^{-(r+1)} · #{(b,c) ∈ (Z/WZ)^{1+r} admissible : b ≡ a (g)} + o(1).

  Since `W` **is** squarefree, CRT gives `(Z/WZ)^{1+r} = ∏_{p≤w} (Z/pZ)^{1+r}` and

      #{…} = ∏_{p≤w, p∤q} #{(b,c) mod p : p∤b+P_i(c) ∀i} · ∏_{p|q} #{c mod p : p∤a+P_i(c) ∀i}
           = ∏_{p≤w, p∤q} p^{r+1}(1−1/p)^k β_p · ∏_{p|q} p^{r}(1−1/p)^k β_p^{(a)},

  using (1.2) and the definition of `β_p^{(a)}`. As `∏_{p≤w}(1−1/p)^k = (φ(W)/W)^k` and
  `∏_{p≤w,p∤q} p^{r+1} ∏_{p|q} p^{r} = W^{r+1}/g`, the main term is
  `(1/(q′g)) ∏_{p≤w,p∤q} β_p ∏_{p|q} β_p^{(a)} = (1/q) ∏_{p≤w,p∤q} β_p ∏_{p|q} β_p^{(a)}`,
  which is (a). This proves Lemma A from Lemma B. ∎

### 3.3 Lemma B: the weighted `W`-tricked estimate

**Lemma B.** In the setting of [TZ, Corollary 5.1] (parameters as in §3.1, `b_i ∈ [W]` coprime to
`W`, `R_i` of degree ≤ d with coefficients ≤ A and `R_i − R_j` of degree exactly `d` for `i ≠ j`,
`A^{-1}N^{1/d} ≤ M_0 ≤ AN^{1/d}`), let `q′ ≥ 1` with `rad(q′) | W` and `q′ | N`, and `a′ ∈ Z/q′Z`.
Then (★) holds, uniformly in `b_1,…,b_k, a′`.

*Proof.* Write `g_i := Λ′_{b_i,W} − 1` (a function on `Z/NZ`). Expand the indicator in additive
characters of `Z/NZ` (legitimate because `q′ | N`):

    1_{x≡a′ (q′)} = (1/q′) ∑_{j=0}^{q′−1} e(j(x−a′)/q′).

The `j = 0` term contributes `(1/q′)·(1+o(1))` by [TZ, Corollary 5.1] as printed. For
`1 ≤ j ≤ q′−1` put

    T_j := E_{x∈Z/NZ} E_{m∈[M_0]^r} e(jx/q′) ∏_{i=1}^k Λ′_{b_i,W}(x+R_i(m)),

and expand `∏_i Λ′_{b_i,W} = ∏_i (1+g_i)`:

    T_j = ∑_{S⊆[k]} T_{j,S},    T_{j,S} := E_{x∈Z/NZ} E_{m∈[M_0]^r} e(jx/q′) ∏_{i∈S} g_i(x+R_i(m)).

It suffices to show `T_{j,S} = o(1)` for every `S` (there are `2^k` of them). Call a node `i`
*full* if `deg P_i = d` (equivalently `deg R_i = d`); since the degree-`d` components of the `P_i`
are pairwise distinct, **at most one** node is not full.

*Case 0: `S = ∅`.* `T_{j,∅} = E_{x∈Z/NZ} e(jx/q′) = 0`, because `q′ | N` and `q′ ∤ j`.

*Case 1: `S` contains no full node.* Then `S = {i_2}` for the unique non-full node `i_2`
(constant or of degree strictly between 0 and d). Substituting `y = x + R_{i_2}(m)` (a bijection of
`Z/NZ` for each `m`) and using that `e(j·/q′)` is `q′`-periodic, hence well defined on `Z/NZ`,

    T_{j,{i_2}} = E_m e(−jR_{i_2}(m)/q′) · E_{y∈Z/NZ} e(jy/q′) Λ′_{b_{i_2},W}(y) − E_x e(jx/q′),

so `|T_{j,{i_2}}| ≤ |E_{y} e(jy/q′) Λ′_{b_{i_2},W}(y)| = o(1)` by Lemma C below. This is the **only**
place where the fixed prime-power part `q′` of the modulus enters the arithmetic.

*Case 2: `S` contains a full node `i_1`.* Split `e(jx/q′) = θ^{c}(x) + i·θ^{s}(x)`,
`θ^{c}(x) := cos(2πjx/q′)`, `θ^{s}(x) := sin(2πjx/q′)`: real-valued, `|θ| ≤ 1`, `q′`-periodic hence
functions on `Z/NZ`. Then `T_{j,S} = T^{c} + i·T^{s}` with `T^{c}` (resp. `T^{s}`) the same average
with `e(jx/q′)` replaced by `θ^{c}` (resp. `θ^{s}`). Each of `T^{c}, T^{s}` is an average of the form
treated by [TZ, Theorem 4.1], with distinguished node `i_1`, for one of the following two
realizations (θ stands for `θ^{c}` or `θ^{s}`):

  (C1) *some `P_{i_0}` is constant* (so `R_{i_0} ≡ t_{i_0} ∈ Z`, and `i_0 ≠ i_1`). Nodes `[k]`,
  polynomials `R_1,…,R_k` (unchanged), functions

        f_{i_1} := g_{i_1};
        f_{i_0} := θ(· − t_{i_0}) · g_{i_0}   if i_0 ∈ S,     f_{i_0} := θ(· − t_{i_0})   if i_0 ∉ S;
        f_i := g_i  for i ∈ S∖{i_0,i_1};        f_i := 1  for i ∉ S ∪ {i_0}.

  Then `f_{i_0}(x+R_{i_0}(m)) = f_{i_0}(x+t_{i_0}) = θ(x)·g_{i_0}(x+t_{i_0})` or `θ(x)`, so
  `∏_i f_i(x+R_i(m)) = θ(x) ∏_{i∈S} g_i(x+R_i(m))`, as required.

  (C2) *no `P_i` is constant.* Nodes `{0} ∪ [k]`, `R_0 := 0`, `R_1,…,R_k` unchanged, functions
  `f_0 := θ`, `f_i := g_i` for `i ∈ S`, `f_i := 1` for `i ∈ [k]∖S`; majorant index `b_0 := b_{i_1}`.
  Then `∏_i f_i(x+R_i(m)) = θ(x) ∏_{i∈S} g_i(x+R_i(m))`.

  Verification of the hypotheses of [TZ, Theorem 4.1] and of the polynomial-system axioms of
  [TZ, Definition 4.2] (which Theorem 4.1 relies on through Theorem 4.4; the paper's own use in
  Corollary 5.1 is the configuration (C1)/(C2) with `θ ≡ 1`):
   - pointwise bounds: `|f_i| ≪ Λ′_{b_i,W} + 1` for all nodes: `|θ(·−t) g_{i_0}| ≤ |g_{i_0}| ≤ Λ′_{b_{i_0},W}+1`;
     `|θ| ≤ 1`; `|g_i| ≤ Λ′_{b_i,W}+1`; `|1| ≤ 1`. Via (3.6) this gives `|f_α| ≪ ν_{b_α}+1`
     (Definition 4.3). The distinguished node carries `f_{i_1} = g_{i_1} = Λ′_{b_{i_1},W} − 1`,
     exactly as in the printed Corollary 5.1.
   - degrees and coefficients: all `R_α` have degree ≤ d and coefficients ≤ A (`R_0 = 0` trivially).
   - `R_α − R_{i_1}` has degree ≥ d_0 = d for every `α ≠ i_1`: for `α ∈ [k]` this is the printed
     hypothesis (degree exactly `d`); in (C2), `R_0 − R_{i_1} = −R_{i_1}` has degree exactly `d`
     because `i_1` is full.
   - Definition 4.2, axiom 1 (`R_α − R_β` non-constant for distinct nodes): for `α,β ∈ [k]`,
     degree exactly `d ≥ 1`; in (C2), `R_0 − R_i = −R_i` is non-constant because no `P_i` is
     constant. (This axiom is exactly why (C1) is used when a constant polynomial is present:
     adjoining `R_0 = 0` next to a constant `R_{i_0}` would violate it.)
   - axiom 2: same as the third bullet.
   - axiom 3 (linear nodes): a node is linear iff `R_α − R_{i_1}` has `m`-degree ≤ 1. If `d ≥ 2`
     all differences with `R_{i_1}` have degree `d ≥ 2`, so `i_1` is the only linear node and there
     is nothing to check. If `d = 1`, all nodes are linear and the pairwise differences
     (`R_i−R_j`, and `−R_i` in (C2)) have degree exactly 1 in `m`, i.e. are non-constant in `m`.
   - the number of nodes (`k` or `k+1`) and fine degrees of freedom (`0`) are bounded by a constant
     depending on `d, r, D` with `D = k+1`, and the coefficient bound `A ≤ A^{C_1}` holds.
   - the range of `M_0`: `A^{-1}N^{1/d} ≤ M_0 ≤ AN^{1/d}` implies `log^{1/κ}N ≤ M_0 ≤ AN^{1/d}` as
     required by Theorem 4.1, and `M := A^{-1}M_0` is the `M` of the norm (4.1); these are the
     printed choices of Corollary 5.1 and §5 and are not altered.

  [TZ, Theorem 4.1] therefore gives `|T^{c}|, |T^{s}| ≪ ‖g_{i_1}‖^{c} + o(1)` for some `c > 0`, where
  `‖·‖` is a norm of the form (4.1) with `d_0 = d`, `D′ = O(1)` polynomials of degree `d−1` and
  coefficients `O(A^{O(1)})`. By the second part of [TZ, Theorem 3.1] (`d_0 = d`,
  `M ≥ (A^{-1}N)^{1/d}`, `f = Λ′_{b_{i_1},W}`, dense model `f′ = 1`), `‖g_{i_1}‖ = o(1)`. This is
  the identical pair of citations used in the printed proof of Corollary 5.1, applied to the same
  polynomials `R_i`; the only difference is that one non-distinguished node carries a bounded
  periodic factor, which Theorem 4.1 permits since its hypotheses on non-distinguished nodes are
  pointwise bounds only (this is visible in the proof: the PET step bounds `F_h` by `H_h` and
  `G` by `K`, parallelopipedization bounds `|f_{α,m,h,k}| ≤ ν_{α,m,h,k}`, and the final
  Cauchy–Schwarz bounds `f_{α_0}` by `ν_{b_{α_0}}+1`; no other property of the `f_α` is used).

*Uniformity.* Theorems 3.1 and 4.1 are uniform in the `b_i ∈ [W]` coprime to `W` (this uniformity
is already needed for the printed "(5.1) uniformly for all admissible pairs"); Lemma C is uniform
in `b` and `j`; there are `2^k · (q′−1)` terms. Hence (★) holds uniformly in `(b_1,…,b_k, a′)`. ∎

### 3.4 Lemma C: the one new arithmetic input (Siegel–Walfisz for the modulus `q′W`)

**Lemma C.** Let `b ∈ [W]` be coprime to `W`, let `q′ ≥ 1` with `rad(q′) | W` and `q′ | N`, and let
`j ∈ Z` with `q′ ∤ j`. Under (P3),

    E_{y∈Z/NZ} e(jy/q′) Λ′_{b,W}(y) = o(1),  uniformly in b and j.

*Proof.* By (3.3),

    E_{y∈Z/NZ} e(jy/q′) Λ′_{b,W}(y) = (φ(W)/(WN)) ∑_{u∈Z/q′Z} e(ju/q′) ∑_{y∈[R,N], y≡u (q′)} Λ′(Wy+b).

Fix `u`. The integers `Wy+b` with `y ≡ u (mod q′)` form the progression `Wu+b (mod q′W)`, and
`gcd(Wu+b, q′W) = 1`: every prime `p | q′W` divides `W` (as `rad(q′) | W`), so `Wu+b ≡ b (mod p)`
and `p ∤ b`. Thus

    ∑_{y≤N, y≡u (q′)} Λ(Wy+b) = ψ(WN+b; q′W, Wu+b) + O(W log N),

and by the Siegel–Walfisz theorem (`ψ(X;Q,A) = X/φ(Q) + O_C(X log^{-C} X)` uniformly for
`Q ≤ log^C X`, `gcd(A,Q)=1`), applicable because `q′W ≤ log N` by (P3),

    ψ(WN+b; q′W, Wu+b) = WN/φ(q′W) + O_C(WN log^{-C} N).

Since `rad(q′) | W`, `φ(q′W) = q′W ∏_{p|W}(1−1/p) = q′ φ(W)`. Discarding prime powers costs
`O((WN)^{1/2} log(WN))` and the range `y < R` costs `O(R log(WR)) = o(N)` (as `R = N^κ`, `κ < 1`).
Hence

    (φ(W)/(WN)) ∑_{y∈[R,N], y≡u (q′)} Λ′(Wy+b) = 1/q′ + O_C(log^{-C} N) + o(1),

uniformly in `u, b`, and the character sum `∑_{u∈Z/q′Z} e(ju/q′)` vanishes for `q′ ∤ j`. ∎

Remark. For `q′ = 1` Lemma C is vacuous, and Lemma B reduces to the printed Corollary 5.1. For
`q′ > 1` Lemma C says that primes `≡ b (mod W)` are equidistributed among the `q′` classes
`b, b+W, …, b+(q′−1)W (mod q′W)`; this is the exact arithmetic content of the "fixed prime-power
factor" and it is supplied by Siegel–Walfisz for the (non-squarefree) modulus `q′W`, a theorem
that has no squarefreeness hypothesis. Nothing else in the argument sees `q′`.
