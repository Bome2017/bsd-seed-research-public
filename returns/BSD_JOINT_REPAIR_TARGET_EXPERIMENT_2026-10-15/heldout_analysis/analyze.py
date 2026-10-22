#!/usr/bin/env python3
import hashlib,itertools,json,sys,time
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'theory'))
import dual_overlap as z
OUT=ROOT/'heldout_analysis'
LABELS=['718b1','997c1','1070a1','1141a1','1246c1_retry600','1480a1','1525c1','1613a1_grh','mirror389','seed3']

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def matvec(A,v):return [sum(a*b for a,b in zip(r,v))%3 for r in A]
def different(A,B):return z.rank(z.cat(A,B))!=z.cols(A) or z.cols(A)!=z.cols(B)
def witness(K,reject):
    """Exact minimum by Hamming support then lexicographic exponent tuple."""
    k=z.cols(K);assert k<=10, ('bounded witness search exceeded',k)
    best=None
    for a in itertools.product(range(3),repeat=k):
        v=matvec(K,a)
        if not any(matvec(reject,v)):continue
        key=(sum(x!=0 for x in v),tuple(v))
        if best is None or key<best[0]:best=(key,v)
    assert best is not None
    return best[1]
def freshkiller(v,blocks,used):
    for b in blocks:
        if b['q'] in used:continue
        for i,row in enumerate(b['rows']):
            val=sum(a*x for a,x in zip(row,v))%3
            if val:return dict(prime=b['q'],row_zero_based=i,triple_zero_based=b['triples'][i],value=val,source_row=row)
    return None
def analysis(label):
    base=ROOT/'heldout'/label;path=base/'matrices.json';bp=base/'blocks.json'
    raw=json.loads(path.read_text());data=z.adapt(raw);bs=json.loads(bp.read_text())
    pre=sha(bp);old=json.loads((ROOT/'heldout/rejected_polynomial_json'/label/'blocks.json').read_text())
    assert old['blocks']==bs['blocks']
    assert (ROOT/'heldout/rejected_polynomial_json'/label/'blocks.jsonl').read_bytes()==(base/'blocks.jsonl').read_bytes()
    bs['source_sha256']=sha(path);bp.write_text(json.dumps(bs,indent=2)+'\n')
    blocks=bs['blocks'];assert len(blocks)==12
    binding=dict(label=label,source_sha256=sha(path),blocks_before_sha256=pre,blocks_after_sha256=sha(bp),
        old_and_corrected_rows_identical=True,source_json_sha256=sha(base/'source.json'))
    n=data['n'];Dbase=data['G0']+data['A']+data['L'];Kbase=z.ker(Dbase,n)
    local3=[r for b in data['locals'] if b['prime']==3 for r in b['rows']]
    other=[r for b in data['locals'] if b['prime']!=3 for r in b['rows']]
    choices=[('single',(i,))for i in range(12)]+[('pair',ij)for ij in itertools.combinations(range(12),2)]
    results=[];failures=[];localfails=[]
    for kind,ix in choices:
        used=[blocks[i]['q']for i in ix];G=data['G0']+[r for i in ix for r in blocks[i]['rows']]
        prof={name:z.profile(data,G,L,str(used)+'__'+name)for name,L in [('all_local',data['L']),('local3',local3),('other_local',other)]}
        K=z.ker(G+data['L'],n);K3=z.ker(G+local3,n)
        assert z.rank(z.cat(K,Kbase))==z.cols(K), 'Saved genuine/reference kernel rejected by new block'
        same=not different(K,Kbase)
        entry=dict(kind=kind,primes=used,saved_kernel_recovered=same,profiles=prof)
        if not same:
            v=witness(K,Dbase)
            f=dict(kind=kind,primes=used,extra_dimension=z.cols(K)-z.cols(Kbase),exponents=v,
                valuations=matvec(data['V'],v),local_defects={str(b['prime']):matvec(b['rows'],v)for b in data['locals']},
                fresh_eliminating_row=freshkiller(v,blocks,used))
            failures.append(f);entry['extra_witness']=f
        # Record both the class-specific and the stronger full-kernel reading.
        C=prof['all_local']['source_class_lift_basis'];B=z.cat(data['U'],C);nu=z.cols(data['U'])
        J0=z.mm(data['H0'],z.ker(z.mm(G+data['L'],data['H0']),z.cols(data['H0'])))
        J03=z.mm(data['H0'],z.ker(z.mm(G+local3,data['H0']),z.cols(data['H0'])))
        CA=z.colbasis(z.coordinates(B,J0)[nu:]);C3=z.colbasis(z.coordinates(B,J03)[nu:])
        classsame=not different(CA,C3)
        entry['local3_same_admitted_classes']=classsame
        entry['local3_same_full_kernel']=not different(K,K3)
        if different(K,K3):
            v=witness(K3,data['L'])
            lf=dict(kind=kind,primes=used,class_admission_differs=not classsame,
                all_local_class_dimension=z.cols(CA),local3_class_dimension=z.cols(C3),
                all_local_kernel_dimension=z.cols(K),local3_kernel_dimension=z.cols(K3),
                exponents=v,valuations=matvec(data['V'],v),local_defects={str(b['prime']):matvec(b['rows'],v)for b in data['locals']},
                fresh_eliminating_row=freshkiller(v,blocks,used))
            # If class admission differs, construct a witness of exactly that difference.
            if not classsame:
                Ann=z.tr(z.ker(z.tr(CA,ncols=z.cols(CA)),z.cols(C)))
                HC=z.coordinates(B,data['H0'])[nu:]
                rejects=z.mm(Ann,HC)
                Hparam=z.ker(z.mm(G+local3,data['H0']),z.cols(data['H0']))
                cv=witness(Hparam,rejects);sv=matvec(data['H0'],cv)
                lf['class_specific_exponents']=sv
                lf['class_specific_local_defects']={str(b['prime']):matvec(b['rows'],sv)for b in data['locals']}
            localfails.append(lf)
        results.append(entry)
    counts=dict(single_failures=sum(f['kind']=='single'for f in failures),pair_failures=sum(f['kind']=='pair'for f in failures),
       local3_full_kernel_failures=len(localfails),local3_class_failures=sum(f['class_admission_differs']for f in localfails),
       protected_columns=results[0]['profiles']['all_local']['protected_columns'])
    out=dict(binding=binding,counts=counts,failures=failures,local3_failures=localfails,results=results)
    (OUT/(label+'.json')).write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(dict(label=label,**counts)),flush=True)
    return dict(label=label,binding=binding,counts=counts)

if __name__=='__main__':
    start=time.monotonic();summaries=[analysis(label)for label in LABELS]
    out=dict(seconds=time.monotonic()-start,sources=len(summaries),single_cases=120,pair_cases=660,profiles=2340,
        source_summaries=summaries,witness_order='Exact minimum Hamming support then lexicographic exponent tuple',
        selection='12 sealed split primes per source, all singles and all unordered pairs; fixed source and local maps')
    (OUT/'SUMMARY.json').write_text(json.dumps(out,indent=2)+'\n')
