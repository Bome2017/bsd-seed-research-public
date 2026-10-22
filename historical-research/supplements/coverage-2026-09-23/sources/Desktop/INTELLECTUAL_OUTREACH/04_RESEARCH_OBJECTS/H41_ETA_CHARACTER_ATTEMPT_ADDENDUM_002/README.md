# H41_ETA_CHARACTER_ATTEMPT_ADDENDUM_002

Custody of the operator's explicit eta-character proof attempt, with Claude's independent audit.

**Exploratory tier.** Not a proof of the H41 seed and not a certification. The two prior objects are
untouched: `CODEX_H41_SEED_RESEARCH_FREEZE_001` at `ac82f3ad…` and
`H41_SEED_FREEZE_ADDENDUM_001` at `82b6730f…`.

    ADDENDUM.md     the construction, the audit, the rank-one reduction, what remains unproved
    01_attempt/     the attempt byte-identically, plus its archive (7b2c4be3…)
    receipts/       verify_eta_attempt.py and its output (18 checks, 18 PASS);
                    the byte-identical replay of the attempt's own checker
    MANIFEST.sha256 the authority
    DIGESTS.md      readable digests; omits its own entry

Summary: the construction side checks out completely — divisor, character, determinants, Dedekind
reciprocity, and the odd winding `−(p−1)(p+3)/12` reproduced independently at `p = 31, 127, 8191`. The
divisor degree turns out to be the cusp-class order already audited in the freeze. The identification
of `χ_p` with the elliptic character is **not** established; rank one reduces it to one kernel
containment. The `a = 1` case is untouched by a mod-2 character. **The seed remains unproved.**
