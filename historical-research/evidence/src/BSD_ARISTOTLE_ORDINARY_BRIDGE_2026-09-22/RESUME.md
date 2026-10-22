# RESUME — Aristotle packet, ordinary anticyclotomic bridge

Built 2026-09-22 from gate stages 5-8 plus the D=-7 certificate. Ordinary primes only.

## Question
Conditional on [c_2] != 0, and given certified L(E^-7,1) != 0 (hence rank E^-7(Q) = 0, Sha(E^-7/Q) finite,
(r+,r-) = (2,0)), do BLV + Bertolini-Darmon already give Sha(E/K)[p^inf] = 0 at good-ordinary p?

## Chain under audit
  [c_2] != 0  --A0-->  calL_p in I^2\I^3  -->  L_p in I^4\I^5, unit leading coeff
              --BLV Thm A (EQUALITY at ordinary p)-->  sigma = ord_I Char_p = 4, unit leading coeff
              --BD derived heights-->  sigma >= 2 max(s^+,s^-)  =>  d^+ = 0
              --D=-7 certificate + tau-eigenspace bridge-->  s^- = 0  =>  d^- = 0
              --BD Thm 2.23 + Rmk 2.21-->  Sha(E/K)[p^inf] = 0

## Known weak links, in order
1. TASK 2  module identification: is BLV's Char_p the char ideal of BD's X_inf? OPEN, never checked.
2. TASK 3  BD Thms 2.7/2.18/2.23 + Rmk 2.21 have NEVER been source-read by this project.
3. TASK 4  the tau-eigenspace bridge is needed for pro-p Selmer and T_p Sha, NOT just for E(K).
4. TASK 6  A2a. A Lambda-module example (STAGE6) shows it does NOT follow from order + unit coefficient alone.

## Packet contents
  00_READ_ME_FIRST.md  INPUTS.md  GATE.md  TASK.md  evidence/ (6 files)  RESUME.md  STATE.json  MANIFEST.sha256

## Not in scope
supersingular (A3), anomalous primes (B), proving [c_2] != 0, redoing the certificate, BSD/FIN/FORMULA.
