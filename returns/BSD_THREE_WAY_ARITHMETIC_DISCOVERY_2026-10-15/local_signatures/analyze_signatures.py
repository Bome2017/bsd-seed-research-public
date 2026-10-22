from pathlib import Path
import ast,json,hashlib,importlib.util
R=Path(__file__).resolve().parent
sp=importlib.util.spec_from_file_location('f3',R/'f3.py');f=importlib.util.module_from_spec(sp);sp.loader.exec_module(f)

def ann(a,n):return f.tr(f.ker(f.tr(a),n))
def data(s):return ast.literal_eval(s.replace(']~',']'))
def one(M,W,K):
 n=len(M);PW=f.mul(M,W);Q=ann(PW,n);SK=f.mul(Q,f.mul(M,K));assert f.zero(f.mul(Q,PW))
 return {'point_image_rank':f.rank(PW),'annihilator_rows':Q,'known_values':f.mul(M,K),'quotient_signatures':SK,'known_quotient_rank':f.rank(SK)}
allout=[]
for nm,np in [('1913b1',0),('28042a1',1),('seed3',2),('389a1',2),('mirror389_false',0)]:
 p=R/nm;x=json.loads((p/'coordinates.json').read_text());n=x['source_dimension'];W=x['points'] or [[]for _ in range(n)];K=x['known'];kc=len(K[0]);blocks,skips=data((p/'scan.gpdata').read_text());out=[];stack=[];greedy=[];greedym=[]
 for prime,roots,pts,om,M,triples in blocks:
  failures=[]
  for i,j,k in triples:
   rel=[(a+b-c)%3 for a,b,c in zip(M[i],M[j],M[k])];value=f.mul([rel],K)
   if not f.zero(value):failures.append({'triple_zero_based':[i,j,k],'value':value[0]})
   if nm!='mirror389_false':assert f.zero(value)
  d=one(M,W,K);d.update(prime=prime,roots=roots,torsion_points=pts,cubic_root=om,source_residue_rows=M,global_additivity_failures=failures)
  for j,row in enumerate(d['quotient_signatures']):
   if f.rank(greedym+[row])>len(greedym):
    greedym.append(row);greedy.append({'prime':prime,'annihilator_index':j,'root_weights':d['annihilator_rows'][j],'known_signature':row})
  stack+=d['quotient_signatures'];out.append(d)
 if nm=='seed3':
  z=json.loads((p/'cached_matrices.json').read_text());bad0=z['local_source_evaluation_rows']
 else:bad0=[(q,M)for q,B,M in data((p/'bad_local.gpdata').read_text())]
 bad=[dict(prime=q,**one(M,W,K))for q,M in bad0]
 summary={'case':nm,'known_class_dimension':kc,'point_dimension':np,'known_excess_dimension':(kc-np if nm!='mirror389_false' else None),'declared_membership':('KNOWN_FALSE_GLOBAL_CLASS' if nm=='mirror389_false' else 'RETAINED_GENUINE_SELMER_CLASSES'),'bad_place_signature_rank':f.rank(sum((d['quotient_signatures']for d in bad),[])),'fresh_good_prime_count':len(out),'fresh_signature_rank':f.rank(stack),'known_quotient_fully_detected':f.rank(stack)==kc-np,'first_global_failure':next(({'prime':d['prime'],**d['global_additivity_failures'][0]}for d in out if d['global_additivity_failures']),None),'greedy_independent_detectors':greedy,'all_place_point_ranks':[[d['prime'],d['point_image_rank'],d['known_quotient_rank']]for d in out],'skipped_primes':skips,'scope':'Detection only on named known classes. No absence or upper bound on unlisted classes.'}
 (p/'SIGNATURES.json').write_text(json.dumps({'summary':summary,'bad_places':bad,'fresh_primes':out},indent=2)+'\n');allout.append(summary)
(R/'RESULTS.json').write_text(json.dumps(allout,indent=2)+'\n')
for a in allout:print(json.dumps({k:v for k,v in a.items()if k not in ['all_place_point_ranks','skipped_primes']}))
