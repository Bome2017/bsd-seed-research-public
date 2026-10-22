# Review: fixed auxiliary primes, mod-5 saturation, and the residual Sha comparison (2026-09-17)

Verdict: **PER_MEMBER_COMPARISON_VERIFIED_INFINITUDE_OPEN**, with **NO_SHA_UPPER_BOUND** and **NO_SYSTEM_CONSTRUCTED**.

Input: `src/PROOF.md` (sha256 11fb98f260856caf0ffaa3b31e61f19d6eafbec8a857088335c358b0c438529f), `src/EXACT_CHECK_RECEIPT.json`,
`src/OPUS_NEXT_TASK.md`. Private directory; no shared ledger, seal or memory changed by this task. No number field, class group, Selmer
group, Sha order, Kurihara number or modular symbol was computed. About 0.1 CPU-second of the 60 allowed, one process.

## 1. Per-member arithmetic — verified

Everything below I recomputed independently (`runs/finite_checks.gp`), not read off the receipt.

| claim | my result |
|---|---|
| Q = 4200·71·181 = 53,974,200, prime divisors 2,3,5,7,71,181 | confirmed |
| m₀ ≡ 491 (mod 4200), n₀ ≡ 420 (mod 4200) | confirmed |
| C1 containment | m₀ ≡ 491 (mod 840), n₀ ≡ 0 (mod 420), m₀ ≡ 11 (mod 24) |
| auxiliary residues | m₀ ≡ n₀ ≡ 1 (mod 71) and (mod 181) |
| v₅(n) = 1 on the whole subfamily | n₀ ≡ 20 (mod 25), so v₅ = 1 exactly |
| local admissibility at every prime dividing Q | (m,A,B) ≡ (1,1,1), (2,2,2), (1,1,1), (1,1,1), (1,17,26), (1,17,26) at 2,3,5,7,71,181 — all nonzero, matching the note |
| admissibility away from Q | for p ∤ Q the additive form covers all residues and at most three are excluded; every such p is ≥ 11, so a choice exists. The check is complete, not a bounded search |
| distinct degree-2 leading coefficients | 0, 16Q², 25Q² are distinct |
| the common reduction | m ≡ n ≡ 1 at both primes gives E_* : y² = x³ − 85x² + 1768x with P₁ = (17,102), P₂ = (36,−12) |
| ℓ = 71 | #E = 80, a = −8, 25 ∤ 80, cofactor 16, generator (5,38) of exact order 5, [16]P₂ = 2·g → row (1,2) |
| ℓ = 181 | #E = 180, a = 2, 25 ∤ 180, cofactor 36, generator (117,180) of exact order 5, [36]P₂ = 3·g → row (1,3) |
| R = [[1,2],[1,3]] | det ≡ 1 (mod 5), inverse [[3,3],[4,1]] |
| Kurihara depth-one data | 71 ≡ 181 ≡ 1 (mod 5); a₇₁ ≡ a₁₈₁ ≡ 2 (mod 5); gcds 10 and 180, each of 5-valuation exactly 1 |
| the certified member | m = 447086291, n = 2171820 give A = 75469280884691, B = 117920499896291; m ≡ m₀ and n ≡ n₀ (mod Q); all three prime by PARI `isprime` (an APR-CL **proof**, independent of the supplied Lucas certificates); all three ≡ 11 (mod 24) |

**§4 (mod-5 saturation) is correct.** Reduction is a homomorphism and E(Q_ℓ)/5 ≅ E(F_ℓ)/5 ≅ Z/5 at both primes (good reduction, ℓ ≠ 5,
formal group uniquely 5-divisible, and 25 ∤ #E(F_ℓ)), so aP₁ + bP₂ ∈ 5E(Q) forces a + 2b ≡ a + 3b ≡ 0, hence a ≡ b ≡ 0. With Zywina's
E(Q) ≅ Z/2 × Z², [P₁],[P₂] is therefore a basis of the **actual** E(Q)/5E(Q). The note is careful that this is saturation at 5 only, not
integral index one, and that Zywina's printed generation statement is mod 2.

**§5 (the Sha identification) is correct**, and I checked the explicit projection rather than accepting it: ℓ(δP₁) = (1,1) and
ℓ(δP₂) = (2,3), so solving α(1,1) + β(2,3) = (u,v) gives α = 3u − 2v, β = v − u — exactly the displayed π(s). Since ℓ|_W is invertible,
S = W ⊕ K, and Kummer–Selmer gives K ≅ Sha(E/Q)[5]. No finiteness hypothesis enters, and the note does not claim K = 0.

**§6 (the relaxed structure) is correct.** The reciprocity argument is right: for s satisfying F_rel and w ∈ W, all local terms away from
71, 181 vanish by self-orthogonality of the Kummer conditions, W surjects onto L₇₁ ⊕ L₁₈₁ by the matrix, and L^⊥ = L forces s to be
Kummer at both primes, so H¹_{F_rel}(Q,V) = S. The dual structure is zero at those primes and Kummer elsewhere, so its global group is K.
The dimension difference 2 is independently consistent with Greenberg–Wiles: at each of 71, 181 one has h⁰ = 1 (E[5]^{G_ℓ} is a line since
5 ‖ #E(F_ℓ)), hence dim H¹ = 2 and dim L = 1, so relaxing adds 1 + 1 = 2.

## 2. Infinitude — OPEN, and I can say precisely why

I checked the two printed sources rather than the paraphrase.

- **TZ08, Theorem 1.3** (local copy): "Let A ⊂ P be a set of primes of positive relative upper density … given any P₁,…,P_k ∈ Z[m] with
  P₁(0) = … = P_k(0) = 0, A contains infinitely many progressions x + P₁(m), …, x + P_k(m)". This is how Zywina gets m, A, B ≡ 11 (mod 24):
  a **single** density class A, with 24 | n² forced by the conclusion. The congruence on the additive variable is free in that formulation.
- **Tao–Ziegler 2016/2018, Theorem 1.4 and Corollary 1.5**: the asymptotic
  E_{n∈[N]} E_{m∈[M]^r} Λ(n+P₁(m))···Λ(n+P_k(m)) = ∏_p β_p + o(1) under distinct top-degree components, and the qualitative corollary under
  admissibility. Nonzero constant terms are allowed — which is what this subfamily needs. **But** the density/congruence formulation is
  Theorem 1.7, and that one still requires P_i(0) = 0. The W-trick modulus in the proof is the primorial W = ∏_{p≤w} p, i.e. squarefree.

So the note's own assessment is right, and here is the sharp reason its adaptation cannot be avoided by Zywina's route: once n is pinned
to a nonzero residue mod 71, the three forms m, m+16n², m+25n² lie in **three different classes** mod 71 (1, 17, 26). A single
positive-density set A can never contain all three, so the TZ08 mechanism is unavailable, and prescribing n's residue destroys the
zero-constant-term hypothesis that Theorem 1.7 needs. The only printed statement that accepts the polynomials is Theorem 1.4/Corollary 1.5,
which averages over all n and offers no way to select the class of the additive variable.

Consequently infinitude rests entirely on the author-derived modification in §2.1 (replace W by W̃ = lcm(Q,W), restrict to fixed-index
progressions, argue that the Gowers-uniformity and majorant estimates survive). That argument is standard in shape — restriction to a
subprogression of bounded index, linear-phase insertion, constant-factor renormalisation — but verifying it requires working through §5 of a
technical paper, which is beyond this ceiling and is exactly the step the note asks a referee to check. **I therefore leave infinitude open
and do not treat it as established.**

One reduction that may help whoever checks it: on the additive variable, only m ≡ 3 (mod 8), m ≡ 2 (mod 3), m ≡ 1 (mod 5), m ≡ 1 (mod 71),
m ≡ 1 (mod 181) are actually needed — the mod-7 conditions are inherited from C1's old Frobenius test and are unnecessary given the accepted
all-odd-image theorem, and m mod 25 plays no role (only v₅(n) = 1 matters, and that is a condition on the polynomial variable, which is free
by substitution). If the additive modulus were squarefree, the printed proof's own W-trick would already cover it, since one could take
w large enough that the modulus divides W and then select admissible residues. So the entire difficulty is concentrated in the single prime
power 2³.

## 3. The gap that remains, stated precisely

The note is correct that ω = δ(P₁) ∧ δ(P₂) ∈ ∧²S with (ℓ₇₁ ∧ ℓ₁₈₁)(ω) = det R = 1 is an explicit element with unit evaluation, and correct
that this is **not** system membership. Stating the consequence exactly, so that no one later mistakes one for the other:

> If ω were the bottom component of a genuine Stark system for (E[5], F_rel), then — the structure theorem for the module of Stark systems
> at core rank 2 being free of rank one — a unit bottom evaluation would make it a generator, its zeroth ideal would be the unit ideal, and
> the dual Selmer group, i.e. Sha(E/Q)[5], would vanish. **The missing assertion is exactly the existence of compatible classes ε_n at
> admissible indices n with ε_1 = ω and the Kolyvagin transition relations.** Nothing in the rational-point computation supplies them, and a
> nonzero wedge with unit determinant is compatible with K ≠ 0.

The hypotheses that would additionally have to be matched literally for a named higher-rank theorem: self-duality of E[5] under the Weil
pairing (available), residual irreducibility and large image (available from the accepted all-odd-image theorem), p ≥ 5 (yes), the core-rank
computation for F_rel (consistent with the dimension difference 2 verified above), and the hypotheses on the auxiliary-prime set used in the
chosen formulation. None of that produces the transition classes.

## 4. Proposed addendum (not a merge)

> **Fixed-prime rational input on a specified subfamily (reviewed).** On the subfamily of C1 defined by m ≡ m₀, n ≡ n₀ (mod Q) with
> Q = 4200·71·181, every member reduces at 71 and 181 to y² = x³ − 85x² + 1768x, the localization matrix of the two Zywina points is
> [[1,2],[1,3]] with determinant 1 mod 5, and hence **[P₁],[P₂] is a basis of the actual E(Q)/5E(Q)** — saturation at 5, not integral index
> one. Consequently Sel₅ = W ⊕ K with K = ker(loc₇₁, loc₁₈₁) ≅ Sha(E/Q)[5] by an explicit projection, and the relaxed residual structure
> F_rel (full H¹ at 71, 181; Kummer elsewhere) has primal group Sel₅ and dual group exactly that Sha[5], with dimension difference 2 over F₅.
> C1 is unchanged; v₅(n) = 1 holds throughout, so ε = 1 there.
>
> **Infinitude of this subfamily is OPEN.** The printed Tao–Ziegler statements do not cover it: the relative-density formulation requires
> zero constant terms, which prescribing n's residue destroys, and the three prime forms occupy three distinct classes mod 71 so a single
> density class cannot hold them; the nonzero-constant-term theorem averages over the additive variable with a squarefree primorial W-trick.
> The supplied W̃ = lcm(Q,W) adaptation is author-derived and unverified here. The per-member statements and the Lucas/APR-CL-certified
> member (m,n) = (447086291, 2171820) stand regardless.
>
> **No Sha bound and no system.** K has not been computed or bounded. The wedge δ(P₁) ∧ δ(P₂) has unit local determinant but has not been
> extended to a compatible Stark system; only that extension, not the determinant, would give Sha[5] = 0.

## 5. Escalation

Fable is warranted for exactly one isolated question, if the operator wants it adjudicated: whether the Tao–Ziegler asymptotic of
Theorem 1.4 survives restricting the additive variable to a fixed residue class modulo a non-squarefree modulus (concretely, modulo 8).
Nothing else in this note is in dispute.
