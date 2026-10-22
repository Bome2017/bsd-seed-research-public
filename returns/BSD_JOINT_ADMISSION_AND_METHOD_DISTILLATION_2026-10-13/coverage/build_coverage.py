#!/usr/bin/env python3
"""Bind located seed certificates; never rerun expensive numerical arithmetic."""
import hashlib,json,re
from pathlib import Path
OUT=Path(__file__).resolve().parent
HOME=Path('/Users/bsm')
LAB=HOME/'BSD_GITHUB_UPDATE_CODEX_2026-10-04/lab'
RET=LAB/'work/returns'
H=HOME/'BSD_CODEX6_MASTER_HANDOFF_2026-09-19'
S=HOME/'BSD_P17_PREREQUISITES_2026-09-25/singleton_probe'
inputs={}
def bind(path,anchor=None):
 p=Path(path); data=p.read_bytes(); ls=data.decode('utf-8').splitlines()
 key=str(p)
 if key not in inputs:inputs[key]={'path':key,'sha256':hashlib.sha256(data).hexdigest(),'bytes':len(data),'lines':len(ls),'read_scope':'whole text or indicated anchors; historical production not rerun'}
 if anchor:
  rr=[i+1 for i,l in enumerate(ls) if re.search(anchor,l)]
  return {'path':key,'line_matches':rr,'anchor':anchor}
 return {'path':key,'lines':[1,len(ls)]}
def count(p):
 a,b=-22735,106272484
 squares={y*y%p for y in range(p)}
 return 1+sum(1 if (v:=(x**3+a*x*x+b*x)%p)==0 else 2 if v in squares else 0 for x in range(p))
base_theorem=['retained rank two and saturated point basis','retained full residual and integral image','retained Manin/lattice and period conventions','retained local Tamagawa product16']
rows=[]
rows.append({'p':2,'result':'Sha[2-infinity]=0','method':'rational two-isogeny descent','trigger':'Zywina theorem explicitly gives Sha[2]=0; PARI ellrank=[2,2,0] is a rank replay, not here promoted to a separate proof of Sha[2]=0','source':[bind(H/'MASTER_BSD_DAG.md',r'Mordell|G\[2|Zywina'),bind(H/'SEED_PROVED_STATE.md',r'2 \| Sha|index 1'),bind(HOME/'SEED_2243_12_MASTER_CERTIFICATE_2026-09-18/00_CERTIFICATE.md',r'N1 MW|N1 \(PUB')],'grade':'retained preprint theorem with exact rank/saturation checks','dependencies':['Zywina arXiv:2502.01957v1 Theorem1.2','finite-level Kummer/descent'],'shared_evidence':'rank/basis theorem also used in every later certificate','not_independent':['ellrank s=0 is recorded as consistency evidence'],'limitations':'This is a rational2-isogeny method; no analogous rational odd isogeny for the seed.'})
p3=HOME/'BSD_SEED_2243_12_P3_RIGOROUS_RUN_2026-09-19'
rows.append({'p':3,'result':'Sha[3-infinity]=(Z/3)^2','method':'multiplicative cyclotomic coefficient plus integral main conjecture and leading term','trigger':{'denominator':81,'omega1_quadratic_coefficient':15480,'modulus':27,'residue':9,'valuation':2,'normalized_regulator_valuation':0},'source':[bind(p3/'SHA3_THEOREM.md',r'15480|Skinner|Jones|Reg_γ'),bind(p3/'P3_CERTIFICATE.md'),bind(H/'MASTER_BSD_DAG.md',r'R1 passes|R2|Euler-removal|3-primary theorem retained')],'grade':'retained computer-assisted theorem via published Skinner Theorem A; source history governed by canonical master corrections','dependencies':base_theorem+['Skinner2016 TheoremA integral equality','Stein-Wuthrich Proposition3.5 and Theorem6.1; multiplicative Jones input','Cassels-Tate finite-primary alternating pairing'],'shared_evidence':'same fixed rational modular symbol and Fourier certificate engine as later vanishing primes','limitations':'Bad nonsplit multiplicative prime; Kato good-ordinary divisibility is not the source at3. Historical internal SU Euler-removal audit remains incomplete; no new source re-certification here.'})
for p,res,raw in [(5,2,152),(7,1,-1931),(11,8,-190),(13,2,-3950)]:
 path=HOME/'BSD_SEED_2243_12_P5_RIGOROUS_UPGRADE_2026-09-19/SHA5_RIGOROUS_THEOREM.md' if p==5 else H/f'audits/P{p}_PRIMARY_THEOREM.md'
 rows.append({'p':p,'result':f'Sha[{p}-infinity]=0','method':'ordinary cyclotomic quadratic modular-symbol moment plus integral Kato divisibility','trigger':{'denominators':[p*p,p],'omega1_evaluation_integer':raw,'omega1_residue':res,'neron_residue':res*pow(2,-1,p)%p,'certified_precision':f'mod{p}','a_p':p+1-count(p),'cardinality_EFp':count(p)},'source':[bind(path)],'grade':'retained computer-assisted fixed-prime theorem','dependencies':base_theorem+['Stein-Wuthrich Proposition3.5','Kato good-ordinary integral divisibility as Stein-Wuthrich Theorem7.3','algebraic leading-term Theorem6.1','canonical-height integrality; at5 also retained normalized regulator unit certificate'],'shared_evidence':'common rational modular symbol, lattice1/1024, ordinary finite measure, Arb engine and partially overlapping certified Fourier coefficient corpus','limitations':'Two extraction checks share certified symbol table. One quadratic digit is certified, not higher precision from finite-polynomial outputs. No integral main-conjecture equality required at5/7/11/13.'})
runlist=[(17,'l103','RESULT_P17.md'),(19,'p19_l191_v2','RESULT_P19.md'),(23,'p23_l47','RESULT_P23.md'),(29,'p29_l233_v2','RESULT_P29_L233.md'),(31,'p31_l311','RESULT_P31.md'),(37,'p37_l149','RESULT_P37.md'),(41,'p41_l83','RESULT_P41.md'),(43,'p43_l173','RESULT_P43.md'),(47,'p47_l283','RESULT_P47.md')]
for p,r,f in runlist+[(83,'p83_l167',None)]:
 directory=S/'seed_runs'/r if p!=83 else RET/'BSD_SEED_P83_CERTIFICATE_2026-10-13/production/p83_l167'
 report=directory/f if f else RET/'BSD_SEED_P83_CERTIFICATE_2026-10-13/REPORT.md'
 jpath=directory/'SINGLETON_REPORT.json';d=json.loads(jpath.read_text())
 assert d['verdict']=='NONZERO' and d['p']==p and int(d['c2'])%p==d['c2_mod_p']!=0
 assert int(d['c0'])%p==int(d['c1'])%p==0
 output=directory/'msl.txt'; actual=hashlib.sha256(output.read_bytes()).hexdigest();assert actual==d['msl_sha256']
 ell=d['l']; assert count(ell)==d['E_Fl_order']
 rows.append({'p':p,'result':f'Sha[{p}-infinity]=0','method':'Ota singleton tame quadratic augmentation moment','trigger':{k:d[k] for k in ['l','generator','c0','c1','c2','c2_mod_p','symbols','E_Fl_order']},'exact_local_recheck':{'a_p':p+1-count(p),'cardinality_EFp':count(p),'ordinary':(p+1-count(p))%p!=0,'a_l':ell+1-count(ell),'l_minus_1_over_p':(ell-1)//p,'reduced_p_torsion_zero':count(ell)%p!=0},'source':[bind(report),bind(jpath)],'output_binding':{'path':str(output),'sha256':actual,'matches_checker_field':True},'grade':'retained computer-assisted fixed-prime theorem; model review, with per-return scope limitations','dependencies':base_theorem+['Ota Theorems1.5/6.4 with order-of-vanishing input5.17','auxiliary ell=1 modp, v_p(ell-1)=1 and cyclic E(Fell)[p]'],'shared_evidence':'same engine47d07f2e..., same fixed modular form, same period/lattice, overlapping Fourier coefficient corpus; downstream/checker replays are not new independent symbols','limitations':'No main conjecture or prior Sha finiteness assumed. Ordinary/supersingular both allowed. Numerical independence limited by common engine/corpus; no implication to other coefficient primes from this single conductor.'})
negative=[]
for r in ['p29_l59','p19_l191']:
 dr=S/'seed_runs'/r;d=json.loads((dr/'SINGLETON_REPORT.json').read_text());f=next(dr.glob('RESULT*.md'))
 negative.append({'run':r,'result':d['verdict'],'p':d['p'],'ell':d['l'],'c2':d.get('c2'),'c2_mod_p':d.get('c2_mod_p'),'source':[bind(f),bind(dr/'SINGLETON_REPORT.json')],'meaning':'valid mathematical zero at chosen auxiliary, not Sha nonzero' if d['verdict']=='INCONCLUSIVE_ZERO' else 'failed numerical identification; no witness value accepted'})
other_sources=[RET/'BSD_CYCLOTOMIC5_MOMENT_REVIEW_CODEX_2026-10-12/REPORT.md',RET/'BSD_VALUATION_MECHANISM_REVIEW_2026-10-13/REPORT.md',RET/'BSD_UNIT_ADMISSION_CONTINUATION_2026-10-13/REPORT.md',RET/'BSD_UNIT_ADMISSION_CONTINUATION_2026-10-13/PROOF.md',HOME/'BSD_K288_UNIFORMITY_AUDIT_CODEX_2026-09-27/AUDIT.md',HOME/'BSD_TAME_LAW_EXACTNESS_TEST_2026-10-07/REPORT.md',S/'mt_prescreen/MT_PRESCREEN.md',S/'mt_prescreen/PREDICTIONS_2026-09-26.md',HOME/'BSD_BUILD_MAP/PARTS_MAP.md',LAB/'CURRENT_STATE.md']
for x in other_sources:bind(x)
extras=[{'type':'field_tower_not_new_coefficient_coverage','p':5,'statement':'E(Q_n)=E(Q), rank2, Sha(E/Q_n)[5-infinity]=0 for every cyclotomicZ5 finite layer','source':str(other_sources[0]),'new_arithmetic':'none: uses original L2,5 unit plus Greenberg finite-submodule exclusion'}, {'type':'reverse_deduction_not_new_coefficient','p':17,'statement':'v17(L2,17)=1','source':str(other_sources[1]),'new_arithmetic':'none: inferred from prior Ota17 vanishing, matched regulatorvaluation1 and integral main conjecture'}, {'type':'descent_structural_experiment_not_new_primary_order','p':3,'statement':'four actual classes; unit/class excess dimensions1/1; complete norm-one unit componentrank2','source':str(other_sources[2]),'new_arithmetic':'actual representative maps, units, local/norm matrices; does not independently prove higher3-primary order'}]
res={'status':'LOCATED_ACTUAL_COVERAGE_NOT_EXHAUSTIVE_HOST_AUDIT','as_of':'2026-10-13','rows':rows,'negative_runs':negative,'additional_consequences':extras,'coefficient_primes_proved_zero':[r['p'] for r in rows if r['p']!=3],'coefficient_primary_nonzero':{'3':'(Z/3)^2'},'unresolved_explicit':[53,59,487,2243,4547,5843],'eligibility_only_not_coverage':[89,113],'infinite_unresolved':['ordinary coefficient-prime tail','supersingular coefficient-prime tail'],'endpoint_effect':'No new prime; FIN ORDER9 Q36 unchanged','search_scope':['canonicalDAG and subordinatePARTS_MAP','all current top-level lab return REPORT.md files for later89/113/53 coverage','historical singleton seed RESULT and checkerJSON files','specific original5/7/11/13/3 theorems'],'not_claimed':'No completeTB/archive audit, no numericalproduction replay, no independent recertification of imported theorem hypotheses.'}
(OUT/'coverage.json').write_text(json.dumps(res,indent=2,ensure_ascii=False)+'\n')
(OUT/'INPUT_BINDINGS.json').write_text(json.dumps({'files':list(inputs.values())},indent=2,ensure_ascii=False)+'\n')
print(json.dumps({'rows':len(rows),'bound_text_files':len(inputs),'singleton_output_hashes_rechecked':len(runlist)+1,'exact_local_counts_recomputed':len(set([r['p'] for r in rows if r['p']>=5]+[r['trigger']['l'] for r in rows if isinstance(r.get('trigger'),dict) and 'l' in r['trigger']]))},sort_keys=True))
