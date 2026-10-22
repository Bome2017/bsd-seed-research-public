# A Kolyvagin-type bound from a global rank-two class — attempt (Claude Opus 5.5, 2026-10-15)

User: "give that a shot" (the third piece named on 10-15: a rank-two global class bounding Sha at every prime).
**Outcome: the bound is not a separate missing theorem. It collapses into the global-object question.** Endpoint effect:
none; FIN, ORDER9 and Q36 unchanged. This corrects my 10-15 summary, which listed it as a third open theorem.

## 1. Per prime, the bound already exists
- Ota's criterion (Kato's Euler system): theta_l in I^2 and c2(p,l) a p-unit give Sha[p^inf] = 0 (record; the seed's tame law).
- Kim, arXiv 2609.15328, Thm 1.1 / Thm 4.7: Sha(E/Q)[p^inf] finite iff the derived Heegner points P_n (nu(n) = r_p^+ - 1)
  lie in p^d (E(Q) + p^k E(K[n])) — a Kolyvagin-type statement in arbitrary rank, at each p.
- Kolyvagin's structure theorem for Heegner Kolyvagin systems, and the higher-core-rank Stark/Kolyvagin systems of
  Mazur–Rubin and Burns–Sakamoto–Sano: the index of the bottom class equals the length of the dual Selmer group, per p.

## 2. Uniformly, the bound is a formality
If, for every p outside a finite set S, the per-p bottom quantity equals the image of ONE fixed global class with
index n (e.g. c2(p,l_p) = kappa (a_l - 2) R(p,l_p) mod p with one rational kappa), then Sha[p^inf] = 0 for all p not in S
and not dividing n (three lines from Ota's criterion; the record already has this in Lean: link_iff_fin_and_kato).
So all the difficulty is in the hypothesis: identifying the per-p bottom classes with one fixed global class. That is
reopener 3 together with step C, the same frontier as before.

## 3. What the open questions in print actually ask
- Kim Q4.6: "Which principle for Heegner points would imply" that derived Heegner points land in E(Q) mod p^k for every k
  and n? — a principle uniform in p, i.e. the fixed global object.
- Banwait (arXiv 2609.08431) Q3, for CM curves of rank 2: "Is there a fixed algebraic number whose prime divisors contain
  every split prime at which the unit condition fails?" His §13 makes the obstruction quantitative: an argument built
  from a family of algebraic integers indexed by p, of height about (1/2) p log p, can only give bounds of order
  h(p)/log p; finiteness for large p "needs an input of height o(log p), which is to say one fixed algebraic number
  rather than a family indexed by p. The rank-two Selmer constructions do not supply one."

## 4. The nearest solved analogue (multiplicative group)
Gross's refined conjecture for Stickelberger elements is the G_m analogue of the tame law: leading term in I^r/I^(r+1)
= fixed constant x G-valued regulator, at all levels at once. Rank one: Dasgupta–Kakde (Brumer–Stark units, Ribet's method
with group-ring-valued Hilbert modular forms). Higher rank: announced as work in progress (Dasgupta–Spiess; their 2015
note proves the order of vanishing, up to a factor 2 in one case). So the seed's step C is the GL_2, rank-two version of a
frontier that is still open for G_m.

## 5. Next attack (theory, not compute)
Map the Dasgupta–Kakde / Dasgupta–Spiess mechanism onto the Mazur–Tate refined conjecture in rank 2: which steps have
GL_2 versions (Kato's Euler system; Skinner–Urban Eisenstein congruences on U(2,2)), and which is the first that breaks.
The output would be a transfer map naming the first missing lemma, not a theorem.

Sources: Kim arXiv 2609.15328 (local text); Banwait arXiv 2609.08431 (local text);
Dasgupta–Spiess note https://sites.math.duke.edu/~dasgupta/papers/Glennfest.pdf ;
Kakde talk abstract https://mediathek2.uni-regensburg.de/playthis/60e57ac53549f6.32121665 ;
Dasgupta–Kakde slides https://www.icts.res.in/sites/default/files/seminar%20doc%20files/Dasgupta2.pdf
