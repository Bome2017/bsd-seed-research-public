# Data binding and retained-arithmetic audit

2026-10-13. Scope: file identity, cheap exact replay, source binding, seed17 provenance, and the newer d=329233 control. This is not an audit of the imported main-conjecture or algebraic leading-term theorems, a rerun of descent, or a fresh coefficient computation. No repository was edited and no expensive job was run.

## 1. Supplied packet

All **6 entries** in SHA256SUMS verify. The packet contains seven files when the manifest itself is included, so “seven files published” is consistent with six hash entries. `checks/verify.py` uses the standard library, runs successfully, and reproduces `checks/RESULTS.json` **byte-for-byte**. The checks count small finite-field points twice, verify the residual-character witnesses, and operate on explicitly retained coefficient digits. They do not generate those coefficients.

All seven retained-source git blob IDs in SOURCE_BINDINGS.json match the exact named paths at baseline `f97843a1b4768606787a9760ea4bad727a3dc4a1` in Bome2017/bsd-seed-lab. The current local copies also match those baseline bytes. These facts are recorded in DATA_VERIFICATION.json; replay output is REPLAY_OUTPUT.json. Primary-source entries have null byte hashes, as the packet declares; this audit does not promote them to archived-source bindings.

## 2. Seed17: old arithmetic really is present

The retained release file

`work/state-sync-2026-09-30/release/v0.2.6/evidence/src/BSD_CERT_17_29_AUDIT_RETURN_FABLE_2026-09-29/RETURN.md`

records p=17, auxiliary ell=103, primitive root5, c0=0, c1=7242, c2=46298, and c2 mod17=7. It records a numerical-output audit with status PASS_AT_RETAINED_GRADE. Its explicit grade is MODEL_SAME_FAMILY; retained Ota, rank, image, Manin/lattice, engine and corpus inputs are not reproved there. This return describes exact interval identification, recombination and frozen-checker replay, not a re-evaluation of the enormous original Fourier sum. We retain that distinction. This audit only reread the bound file and recomputed 46298 mod17.

`work/returns/BSD_KATO_CONTENT_BOUND_CODEX_2026-10-07/VALUATION_TARGET.md` states the matched height value r17=1. Going one step below that statement, `context/SUBMITTED_REVIEW.md` gives the saved native entries

    h11 = 13*17 + 16*17^2 + O(17^3)
    h12 = 5*17 + 7*17^2 + O(17^3)
    h22 = 15*17 + 12*17^2 + O(17^3).

Direct determinant arithmetic gives native determinant valuation3 and leading unit13. Because log_17(18) has valuation1 and leading divided unit1, dividing the matrix entrywise by log_17(18) gives

    v17(det H_U)=1, (det H_U)/17=13 mod17.

The saved entries determine this first nonzero determinant digit: unknown O(17^3) entry terms affect the determinant only at O(17^4). This is stronger evidence than inferring exact valuation1 from a singular matrix mod17 alone. The underlying height engine remains retained. The context explicitly excludes a historically wrong raw-model regulator digit and uses the canonical-model PARI/Sage comparison instead.

Consequently the proposed seed17 deduction has genuine retained inputs. If the imported integral main-conjecture and leading-term application is accepted, those inputs can imply v17(L2)=1. It is a reverse deduction from old Sha17 vanishing, not a new numerical coefficient or independent new Sha17 proof.

## 3. Extension to the new combined control d=329233

The published valuation-mechanism packet predates the latest paired experiment. Its arithmetic application extends to the latter without needing a new numerator run, provided the same theorem audit succeeds.

Source folder:

`/Users/bsm/BSD_PAIRED_EXCESS_EXPERIMENT_2026-10-12`.

All **86 entries** in that packet's SHA256SUMS verify. Relevant source hashes and fresh residue calculations are in EXTENDED_ARITHMETIC.json.

The target curve is

    F=[0,-1,1,-847680091476076,-9499397825675855099600],
    d=329233.

Trial division confirms d is prime, d=1 mod4, d mod5=3, and (d/5)=-1. Independent small point counting gives #F(F5)=7, hence a5=-1, good ordinary and non-anomalous. Thus the residual characters chi_d and omega*chi_d have the same nontrivial unramified local factor at5 as in d43737. Neither local constituent is 1 or omega. This is the arithmetic character check; theorem applicability is assessed separately.

The actual precision8 raw producer output `outputs/combined329233_n8.out` contains a direct power series

    O(5^8)+O(5^6)*x+(3*5^4+O(5^5))*x^2+...,

and the independent height result

    det H_U=3*5^2+3*5^3+4*5^4+4*5^6+5^8+O(5^11).

The direct x^2 coefficient establishes valuation4 without treating the finite-precision constant and linear residues as exact zeros. The height determinant has valuation2. Its common conventions, chunked-engine precision and source normalization remain the paired packet's retained inputs. The precision8 stderr file is empty and the stdout ends DONE. The earlier precision7 zero residue is correctly labelled a lower bound, not an exact valuation.

Fresh integer modular arithmetic on these saved digits gives

    v5(L2)=4, v5(det H_U)=2,
    epsilon mod5=4, Tamagawa=4, torsion=1,
    corrected quotient Q=25 mod125, v5(Q)=2.

The leading-unit calculation is 3/(3*4*4)=1 mod5. The exact curve/isogeny proof in COMBINED_EXCESS_PROOF.md and `outputs/combined_exact.json` retains rank<=2 from PARI and proves dim_F5 Sha(F)[5]>=2 independently of these digits. That exact proof was inspected, not rerun in this audit.

**Conditional additional consequence:** if the integral main-conjecture/leading-term application holds as proposed, then the combined nonunit-regulator control also has finite 5-primary group of length2. Combined with its independently established residual dimension>=2, this forces

    Sha(F/Q)[5-infinity] = (Z/5)^2.

This is the same elementary abelian-group deduction as for d43737: among abelian groups of order25, the cyclic group has residual dimension1 and is excluded. It establishes neither the full Sha group's order nor finiteness.

## 4. Scope and disposition

The data support the proposed valuation applications and the additional d329233 application. There is no missing arithmetic digit at their stated precision. Source theorem and convention matching remain substantive requirements; this file does not replace that audit. No new seed prime, FIN, ORDER9 or Q36 result follows from the checks above.
