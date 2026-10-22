# Wild-leg CONFIRMATION — rule fixed before any confirmation symbol (2026-10-14)
The pre-registered candidate list (linear factors) FAILED on the first data set (RESULTS_WILD.json). A theory-derived
factor, (a_p-1)^2 = (1-alpha)^2 mod p (Mazur-Tate-Teitelbaum: theta_{p^2}|W = alpha^2 * L_p|W and the p-adic leading term
carries (1-1/alpha)^2), was checked POST HOC on that same data: 24/24 pure, 110/110 mixed (sign +1).
Post-hoc fits are not evidence. This folder tests the single law on FRESH rows only:
  pure:  c2w == (a_p-1)^2 * K * det_w / (cexp^2 idx)^2 (mod p)
  mixed: c11 == (a_l-2) * (a_p-1)^2 * K * Dmix / (cexp^2 idx)^2 (mod p), sign +1
Fresh rows: new curves 571b1, 681c1, 707a1, 709a1 (Sha_an = 1, Cremona curvedata f45) at p <= 73, l <= 400; old curves
at p in [37,73] (pure) and l in (400,600] or p >= 37 (mixed). Pass = every clean row matches. Any clean miss = law refuted.
# CONFIRMATION SEALED 2026-10-15T01:44:04Z before any confirmation symbol; sha256 8466b34d7a9b8bd7943c1ec143bdc390decd30e0168c0c00e4b175f706f6fd71
- 707a1: kap check uses auxiliary level 13 instead of 7 (7 | 707); same Birch-ratio method.
