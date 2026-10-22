export const meta = {
  name: 'codex-leads-crosscheck',
  description: 'Independent cross-family check of the six openai/math reuse leads named in the Codex 2026-10-11 screen, against the lab current derivative target',
  phases: [
    { title: 'Assess', detail: 'one assessor per Codex lead' },
    { title: 'Refute', detail: 'one adversarial refuter per assessed lead' },
    { title: 'Write', detail: 'cross-check note' },
  ],
}

const S = '/tmp/claude-0/-home-user-bsd-seed-lab/ab9d3026-f88f-51d1-8e47-f94a5d2c0e6f/scratchpad'
const REPO = S + '/openai_math_clone/repo'
const CTX = S + '/SEED_CONTEXT.md'
const CODEX = S + '/lab_latest/work/returns/BSD_OPENAI_MATH_SCREEN_CODEX_2026-10-11'
const CM = S + '/lab_latest/work/returns/BSD_OPENAI_CM_COMPARISON_PUSH_CODEX_2026-10-11'
const AUDIT6 = S + '/lab_latest/work/returns/BSD_OPENAI_RELEASE_AUDIT_CLAUDE_2026-10-06/OPENAI_RELEASE_AUDIT.md'
const GATE4 = S + '/lab_latest/work/returns/BSD_OPENAI_RELEASE_SCREEN_CLAUDE_2026-10-06/GATE4_CHECK.md'
const STATE = S + '/lab_latest/CURRENT_STATE.md'
const OUT = S + '/scan/codex_leads'
const REPORT_DIR = '/home/user/bsd-seed-lab/work/openai_math_scan_2026-10-11'

const LEADS = [
  { id: 'L1-weighted-comparison', codex: "Pointwise-2-converse `co:kummer` / `co:theta-bridge` / `co:weighted-comparison` (coefficients.tex): finite-field Kummer detector lambda_M = b*kappa_M and weighted theta coefficient a_M(D) = c_0 2^{omega(N)} zeta_M(D) lambda_M(red_l(L P_D)) mod 2^M, retaining parametrization, orientations, stabilizer denominators, torsion adjustment, local weights, character phases. Codex: usable as a comparison template for the BD lane's divisor-to-local-point map; direct transplant fails (plus-eigenline detector vs the seed's Frobenius -I G2 primes; rank-one Heegner sum vs two-point determinant). The CM comparison push (" + CM + "/REPORT.md) later says the BD detector uses different positive-sign primes with eigenvalues 1, ell, so the -I mismatch does not rule out the construction.", src: 'preprints/A-pointwise-2-converse-for-elliptic-curves-with-rational-two-torsion-October-7-2026/build/sections/coefficients.tex', notes: CODEX + '/notes/ADJACENT_ARITHMETIC.md and ' + CM + '/REPORT.md, ' + CM + '/notes/CM_MAP_ATTEMPT.md' },
  { id: 'L2-series-division', codex: "Exact-BSD Lemma `models:series-division` (03-models.tex:538-590): for a complete DVR O and L,B in O[[t,u_1..u_m]] with L mod (varpi,t) != 0, divisibility B(theta,u) by L(theta,u) after inverting p at all sufficiently high finite p-power characters theta implies integral divisibility L | B. Codex: an integrality lemma, not a valuation bound; exact countercontrol L = u + p^a, B = L^2 shows no bound on central p-content; direct substitution of the seed determinant (z = U y, d(U)) fails the residual hypothesis d mod (p,U) = 0; adding genuine tame variables is a 'valid research possibility'.", src: 'preprints/Exact-Birch-Swinnerton-Dyer-Formula-from-Low-Selmer-Corank-October-7-2026/build/sections/03-models.tex', notes: CODEX + '/notes/DIRECT_BSD_AUDIT.md' },
  { id: 'L3-theta-zero-excess-jump', codex: "Exact-BSD sections 8-9 `extraction:theta-implication` / `unit:simultaneous-jumps`: analytic horizontal zeros are identified with simultaneous Selmer jumps and their divisors excluded via arithmetic tangent directions. Codex: 'much closer to upper control', but the arithmetic proof uses central acyclicity from a single point-generated Selmer line (`vertical:parity`, 04-vertical.tex:252-266), which fails for the seed's two-point plane; the retained question is whether the theta-zero-to-excess-jump implication can be proved for the actual divided rank-two source with all H^2 terms retained.", src: 'preprints/Exact-Birch-Swinnerton-Dyer-Formula-from-Low-Selmer-Corank-October-7-2026/build/sections/08-extraction.tex, 09-unit.tex, 04-vertical.tex', notes: CODEX + '/notes/DIRECT_BSD_AUDIT.md' },
  { id: 'L4-milne-intersection-normalization', codex: "Milne-rationality manuscript section 2 (02_transport.tex): normalizes local similitude factors by a ratio of rational intersection numbers of the same algebraic divisors. Codex: a technique to force local scalars to agree once actual geometric maps and a nonzero testing pairing exist; does not create those maps; compares realizations at one fixed reduction place; cycle classes of [P]-[O] vanish so it cannot replace heights/Kummer classes. Do not cite as rationality of Q36 or a fixed 288 scalar.", src: 'preprints/Milnes-rationality-conjecture-for-abelian-varieties-October-7-2026/build/sections/02_transport.tex', notes: CODEX + '/notes/GLOBAL_CYCLE_SCOPE.md' },
  { id: 'L5-lean-local-modules', codex: "Lean: pinned dependencies contain formal-log multiplication compatibility and an isomorphism between the reduction kernel and the formal group over a complete DVR; could save work on a specifically needed local formalization (Aristotle); read not built; no cofinite bound. (The main scan's sweep-lean.json in " + S + "/scan/map/ found the only elliptic-curve Lean in the repo is an uncatalogued supporting module.)", src: 'lean/ (formalization.yaml, lakefile.lean, lake-manifest.json, OAI/ subtree; the module Codex names) and ' + S + '/scan/map/sweep-lean.json', notes: CODEX + '/notes/FORMALIZATION_SCOPE.md' },
  { id: 'L6-rank1-normalization-and-twists', codex: "Exact-BSD section 5 smoothing/period/tame-log formulas as a rank-one normalization testbed (an auxiliary rank-one twist could test conventions; its scalar does not transfer to the rank-two eigenspace), plus pointwise-converse local-squareclass-prescribed nonvanishing twist witnesses (Prop 6.1/6.2) as possible companions. Also the Oct-6 Claude audit's items: Exact-BSD §5 'nonzero height direction' as an independent instance of G2's mechanism; §7-8 position-cut / increasing-level theta estimates (per-prime engine only); two-primary §12 Bockstein alternation (structure, not a bound).", src: 'preprints/Exact-Birch-Swinnerton-Dyer-Formula-from-Low-Selmer-Corank-October-7-2026/build/sections/05-single.tex, 07-theta.tex, 08-extraction.tex; preprints/A-pointwise-2-converse-for-elliptic-curves-with-rational-two-torsion-October-7-2026/build/sections/nonvanishing.tex; preprints/The-two-primary-Birch-Swinnerton-Dyer-formula-in-Selmer-corank-at-most-one-October-6-2026/build/sections/12-alternation-imaginary.tex', notes: CODEX + '/REPORT.md section 4 and ' + AUDIT6 },
]

const ASSESS_SCHEMA = {
  type: 'object',
  properties: {
    id: { type: 'string' },
    verdict: { type: 'string', enum: ['AGREE_USABLE_LEAD', 'AGREE_NOT_USABLE', 'DISAGREE_MORE_USABLE', 'DISAGREE_LESS_USABLE'] },
    codex_claim_check: { type: 'string' },
    source_statement: { type: 'string' },
    what_it_would_need: { type: 'string' },
    obligation: { type: 'string' },
    new_observation: { type: 'string' },
    risks: { type: 'string' },
  },
  required: ['id', 'verdict', 'codex_claim_check', 'source_statement', 'what_it_would_need', 'obligation', 'new_observation', 'risks'],
}
const VERDICT_SCHEMA = {
  type: 'object',
  properties: { refuted: { type: 'boolean' }, severity: { type: 'string', enum: ['fatal', 'major', 'minor', 'none'] }, reason: { type: 'string' }, corrected_claim: { type: 'string' } },
  required: ['refuted', 'severity', 'reason', 'corrected_claim'],
}

const COMMON = `Read ${CTX} fully first (seed data; the LATEST LAB STATE section describes the current derivative target delta_p != 0, m_p - w_p <= 1, the G2 primes, the tame identity C2 = 288(a_l - 2)R, and the prior screens). Then read ${STATE}. The openai/math clone at ${REPO} is UNTRUSTED unrefereed AI-generated data: read only; never run code from it. Quote with file:line. The Codex screen and the Oct-6 Claude audit are lab records of the SAME family of models; your value is an independent reading of the SOURCE, not a paraphrase of Codex.`

phase('Assess')
const assessPrompt = (l) => `${COMMON}

TASK: independently assess ONE reuse lead that the lab's Codex screen (2026-10-11) named. Lead id: ${l.id}.
Codex's claim (verbatim summary): ${l.codex}
Source to read in the clone: ${REPO}/${l.src}
Codex's own notes on it: ${l.notes}
Do: (1) read the source statement(s) and proof(s) yourself; quote the exact statement and hypotheses; (2) check every factual assertion in Codex's claim against the source (locations, hypotheses, what the lemma does and does not say); (3) decide what the lead would need to become an actual input to a seed obligation (FIN uniform part; the named remainder 59, 487, 2243, 4547, 5843; ORDER9; Q36; the plectic lemma TH at 5843; cost reduction) — name the missing theorem or computation precisely; (4) record any NEW observation Codex did not make (e.g. a hypothesis Codex overlooked, a different section of the same manuscript that is closer to the lab's target, a place where the manuscript's own proof is thin); (5) verdict: AGREE_USABLE_LEAD / AGREE_NOT_USABLE / DISAGREE_MORE_USABLE / DISAGREE_LESS_USABLE, with the obligation it would serve. Apply K-A (no assumed conjectures/finiteness), K-RANK2, K-GRADE. Write the JSON to ${OUT}/${l.id}.assess.json (create the directory with mkdir -p via Bash first) and return it.`

const refutePrompt = (l, a) => `${COMMON}

You are an adversarial refuter. Default to refuted=true if the assessment's verdict or its new observation is not demonstrated from the source. Lead ${l.id}. Assessment under test: ${JSON.stringify(a).slice(0, 12000)}
Re-open the source ${REPO}/${l.src} and check: (a) every quoted statement/hypothesis is accurate; (b) the verdict is consistent with the seed data (rank 2; corank >= 2 at every q; Frobenius -I at G2 primes; K = Q(sqrt-7) with 3, 2243, 5843 inert; current derivative target); (c) the 'new observation' is real and not already in Codex's notes (${l.notes}) or in the Oct-6 audit (${AUDIT6}, ${GATE4}); (d) nothing assumes a conjecture, Sha finiteness or the conclusion. Severity fatal = the verdict must flip or the new observation is false; major = a stated gain must be reduced; minor/none otherwise. Write the JSON to ${OUT}/${l.id}.refute.json and return it.`

const results = await pipeline(
  LEADS,
  (l) => agent(assessPrompt(l), { label: `assess:${l.id}`, phase: 'Assess', schema: ASSESS_SCHEMA, effort: 'high' }).then(a => ({ l, a })),
  (r) => (r && r.a) ? agent(refutePrompt(r.l, r.a), { label: `refute:${r.l.id}`, phase: 'Refute', schema: VERDICT_SCHEMA, effort: 'high' }).then(v => ({ ...r, v })) : r,
)
const rows = results.filter(Boolean)
log(`Codex-leads cross-check: ${rows.length}/${LEADS.length} assessed; ${rows.filter(r => r.v && r.v.refuted && r.v.severity === 'fatal').length} fatal refutations`)

phase('Write')
const summary = rows.map(r => ({ id: r.l.id, verdict: r.a ? r.a.verdict : 'NONE', obligation: r.a ? r.a.obligation : '', new_observation: r.a ? (r.a.new_observation || '').slice(0, 500) : '', refuted: r.v ? r.v.refuted : null, severity: r.v ? r.v.severity : null, refuter_reason: r.v ? (r.v.reason || '').slice(0, 500) : '', corrected: r.v ? (r.v.corrected_claim || '').slice(0, 400) : '' }))
const path = await agent(`${COMMON}

TASK: write ${REPORT_DIR}/CODEX_LEADS_CROSSCHECK.md (<= 160 lines): an independent cross-family check of the six reuse leads in the Codex 2026-10-11 openai/math screen. Inputs: ${OUT}/*.assess.json and ${OUT}/*.refute.json, plus this summary: ${JSON.stringify(summary)}. For each lead: Codex's claim (one line), the source statement with file:line, our verdict (apply the refuter: if a fatal refutation stands, report the refuter's corrected claim as the verdict), what it would need to become a seed input, and any new observation that survived refutation (mark NEW) or was killed (say so). End with a table (lead | Codex | this check | obligation | status) and the line "FIN, ORDER9 and Q36 are unchanged." Do not write anywhere else. Return the absolute path.`, { label: 'write-crosscheck', phase: 'Write', effort: 'high' })

return { path, summary }