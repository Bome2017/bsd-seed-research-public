# BH singleton certificate: compact theorem and implementation boundary

**Status:** written corollary of Bullach–Honnor arXiv:2511.07203v1, Theorem 1.4(b), using the seed's retained rank, Galois-image and symbol-lattice inputs. No new value evaluated. No production authorized.

## Theorem

For every p in {2243,4547,5843} and every prime ell coprime to pN with p | ell-1, take the degree-p field K inside Q(mu_ell). Let g be a primitive root modulo ell and j(a)=ind_g(a) mod p in {0,...,p-1}. Set

    s_a = Re(lambda_f(a/ell))/omega_1,
    C_i = sum_(a=1)^(ell-1) binom(j(a),i) s_a  (i=0,1,2).

Here omega_1 is the pipeline's least positive real period and s_a lies in (1/1024)Z by retained claim A.4. If

    C_0 = C_1 = 0 (mod p),   C_2 != 0 (mod p),

then Sha(E/Q)[p^infinity]=0, without assuming its finiteness.

## Exact conversion

The source uses Omega_BH^+ = 2 omega_1. Since K is real, the minus symbols cancel, and its unaveraged projection gives

    theta_K^MT = (1/2) sum_a s_a gamma^j(a).

For certified n_a=1024*s_a, its quadratic coefficient modulo p is

    2048^(-1) sum_a binom(j(a),2)n_a  (mod p).

The existing pipeline's coefficient is twice this. All target primes are odd; nonvanishing is identical.

The source involution sends t=gamma-1 to -t+t^2 modulo t^3. Thus it changes (C_0,C_1,C_2) to (C_0,-C_1,C_2+C_1). It leaves the quadratic leading coefficient unchanged when C_1=0.

There is no additional Manin, cyclotomic alpha, Euler-removal, L-invariant, or factorial factor in this conversion. No averaging over (Z/ell)^*/Gal(K/Q) is allowed.

## Proof in one chain

K is real of odd prime degree, contains no primitive pth root, and is unramified at p. These facts, the retained p-adic image, and at additive 4547 the unramified condition, establish BH Hypothesis 1.2. The theorem gives theta_K^(MT,#) in Fitt_R^0(X), where R=Zp[C_p] and X is the dual of the **classical p-infinity Selmer group** over K.

After reduction to A=Fp[t]/t^p, let d be the minimal number of generators of X/pX. A minimal presentation has entries in (t); hence its zeroth Fitting ideal is contained in (t)^d. A nonzero quadratic leading term forces d<=2.

Large image gives E(K)[p^infinity]=0. Inflation–restriction and compatibility of local Kummer maps give Sel(Q) -> Sel(K)^G injective. Dualizing gives X_G -> Sel(Q)^dual surjective. Its target therefore needs at most two Zp-generators.

The Kummer exact sequence over Q splits on duals as

    Sel(Q)^dual = Zp^2 direct_sum Sha(Q)[p^infinity]^dual.

The free summand uses both available generators. The other summand is finitely generated and has zero reduction modulo p; Nakayama gives zero. This kills finite and divisible Sha contributions, not only its corank.

## Future specification, not a launcher

Use a new BH-labelled theorem profile, not an unlabelled deletion of Ota's good-reduction gate. Keep m=ell, M=1, Q=N, sign +1 and LATDEN=1024 in the existing table convention. Use exact all-label coverage and all existing custody/error controls. In this profile C_1=0 follows from BH plus rank two, not Ota at a bad prime.

The mathematical theorem needs only p|ell-1; the current singleton data format may retain v_p(ell-1)=1. Ota's extra auxiliary cyclicity check is not required by this proof.

No suitable auxiliary was selected, no cost computed, and no nonzero singleton existence theorem obtained. A later bounded cost screen must include full rigorous cutoffs, latest margin policy, the then-current verified corpus, and all production/verification/assembly costs before a separate user decision.
