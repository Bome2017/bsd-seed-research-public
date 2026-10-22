"""Parameter-bound actual coefficient-seven source evaluation.

Run with a config JSON. Its source_format is 'factored_units' (five-entry
export) or 'orbit_relations' (six-entry export). Unit authentication remains
the explicitly named external certificate, not inferred from residue ranks.
"""
import hashlib,json,re,subprocess,sys,time
from pathlib import Path

HERE=Path(__file__).resolve().parent
GP='/Users/bsm/run040-order7-cayley-coordinate-slice-genus-census-2026-09-03/tools/sage-env/bin/gp'

def digest(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def normalize(source,fmt):
    data=json.loads(Path(source).read_text())
    if fmt=='orbit_relations':
        assert len(data)==6 and len(data[5])==6*len(data[4])
        return data
    assert fmt=='factored_units' and len(data)==5
    factors=[];index={};units=[]
    for unit in data[4]:
        entries=[]
        for atom,e in unit:
            assert isinstance(e,int)
            key=json.dumps(atom)
            if key not in index:index[key]=len(factors);factors.append(atom)
            entries.append((index[key],e))
        units.append(entries)
    K=[[0]*len(units) for _ in range(6*len(factors))]
    for j,unit in enumerate(units):
        for k,e in unit:K[6*k][j]+=e
    return data[:4]+[factors,K]

def main():
    config=Path(sys.argv[1]).resolve();cfg=json.loads(config.read_text())
    assert cfg['p']==7
    curve=cfg['curve'];assert len(curve)==5 and all(isinstance(x,int) for x in curve)
    a1,a2,a3,a4,a6=curve
    count=1+sum((y*y+a1*x*y+a3*y-x**3-a2*x*x-a4*x-a6)%7==0 for x in range(7) for y in range(7))
    ap=8-count
    if count%7==0 or ap%7==0:raise ValueError('formal-branch criterion requires ordinary nonanomalous reduction')
    if not re.fullmatch(r'[A-Za-z0-9_-]+',cfg['label']):
        raise ValueError('label must be one simple output-directory name')
    out=HERE/cfg['label'];out.mkdir(exist_ok=True)
    source=Path(cfg['source']).resolve();nf=Path(cfg['nf']).resolve()
    certificate=Path(cfg['unit_authentication']).resolve()
    if not certificate.is_file():raise ValueError('unit admission certificate absent')
    data=normalize(source,cfg['source_format'])
    if not data[4] or not data[5] or not data[5][0]:
        raise ValueError('no authenticated unit columns supplied')
    cols=len(data[5][0])
    if not all(len(row)==cols and all(isinstance(x,int) for x in row) for row in data[5]):
        raise ValueError('relation matrix must be rectangular and integral')
    if len(data[0])!=49 or not all(len(pack[0])==48 and isinstance(pack[1],int) and pack[1] for pack in data[1:4]+data[4]):
        raise ValueError('wrong field/element packing')
    compact=out/'compact_source.json';compact.write_text(json.dumps(data)+'\n')
    binding={'config':str(config),'config_sha256':digest(config),'source':str(source),'source_sha256':digest(source),'nf':str(nf),'nf_sha256':digest(nf),'unit_authentication':str(certificate),'unit_authentication_sha256':digest(certificate),'compact_sha256':digest(compact),'curve':curve,'p':7,'point_count':count,'trace':ap,'source_unit_columns':len(data[5][0])}
    (out/'INPUT_BINDING.json').write_text(json.dumps(binding,indent=2)+'\n')
    receipts=[];spent=0.0
    def run_gp(name,code,marker):
        nonlocal spent
        if spent>=180:raise RuntimeError('cumulative lane cap')
        (out/(name+'.gp')).write_text(code)
        start=time.monotonic()
        try:
            proc=subprocess.run([GP,'-q','-f','-s','128000000','-D','parisizemax=1000000000',name+'.gp'],cwd=out,capture_output=True,text=True,timeout=min(60,180-spent))
        except subprocess.TimeoutExpired as exc:
            elapsed=time.monotonic()-start;spent+=elapsed
            def txt(x):return x.decode(errors='replace') if isinstance(x,bytes) else (x or '')
            (out/(name+'.out')).write_text(txt(exc.stdout));(out/(name+'.err')).write_text(txt(exc.stderr))
            receipts.append({'name':name,'elapsed_seconds':elapsed,'timeout':True,'complete_marker':False})
            (out/'RECEIPTS.json').write_text(json.dumps(receipts,indent=2)+'\n')
            raise RuntimeError('bounded subprocess timed out; partial output retained') from exc
        elapsed=time.monotonic()-start;spent+=elapsed
        (out/(name+'.out')).write_text(proc.stdout);(out/(name+'.err')).write_text(proc.stderr)
        receipt={'name':name,'elapsed_seconds':elapsed,'exit_code':proc.returncode,'complete_marker':marker in proc.stdout}
        receipts.append(receipt);(out/'RECEIPTS.json').write_text(json.dumps(receipts,indent=2)+'\n')
        if proc.returncode or proc.stderr or not receipt['complete_marker']:raise RuntimeError(receipt,proc.stderr)
    def gpstr(s):return json.dumps(str(s))
    finder='{alarm(55);gettime();C=read('+gpstr(compact)+');F=Polrev(C[1],w);den=C[2][2]*C[3][2]*C[4][2]*prod(j=1,#C[5],C[5][j][2]);OUT=List();forprime(q=11,1000000,if(q%7!=1||den%q==0,next);my(rr=polrootsmod(F,q));if(#rr!=48,next);my(ok=1);for(k=1,#C[5],for(j=1,48,if(subst(Polrev(C[5][k][1],w),w,rr[j])==0,ok=0;break));if(!ok,break));if(!ok,next);listput(OUT,[q,lift(Vec(rr))]);if(#OUT==3,break));if(#OUT<3,error("insufficient split primes"));write("split_primes.json",Vec(OUT));print("SPLIT_COMPLETE;MS=",gettime());quit;}\n'
    run_gp('find_split',finder,'SPLIT_COMPLETE')
    for precision in (8,9):
        template=(HERE/'formal_branch.template.gp').read_text().replace('@NF_PATH@',str(nf)).replace('@COMPACT_PATH@',str(compact)).replace('@PRECISION@',str(precision)).replace('@OUTPUT_NAME@',f'formal_{precision}.json')
        template=template.replace('SIG=packelt(C[4],F);','if(NF.pol!=F,error("field mismatch"));SIG=packelt(C[4],F);')
        run_gp('formal_'+str(precision),template,'FORMAL_LOCAL_COMPLETE')
    start=time.monotonic()
    proc=subprocess.run([sys.executable,str(HERE/'evaluate_split.py'),str(compact),str(out/'split_rows.json'),','.join(map(str,curve)),str(out/'split_primes.json')],capture_output=True,text=True,timeout=min(60,180-spent))
    spent+=time.monotonic()-start
    (out/'split.out').write_text(proc.stdout);(out/'split.err').write_text(proc.stderr)
    if proc.returncode:raise RuntimeError(proc.stderr)
    # rank() is intentionally loaded without interpreting this driver's argv.
    args=sys.argv;sys.argv=['evaluate_split.py']
    from evaluate_split import rank
    sys.argv=args
    split=json.loads((out/'split_rows.json').read_text());ranks=[]
    for precision in (8,9):
        local=json.loads((out/f'formal_{precision}.json').read_text())
        rows=local[6];cols=len(rows[0])
        stacked=[[v for q in split['rows'] for v in q['additivity_defects'][j]]+[row[j] for row in rows] for j in range(cols)]
        ranks.append({'precision':precision,'local_chi_rank':rank(rows),'global_rank':split['combined_defect_rank'],'joint_rank':rank(stacked)})
    if ranks[0]['joint_rank']!=ranks[1]['joint_rank']:raise RuntimeError('precision rank mismatch')
    d=4;joint=ranks[0]['joint_rank']
    if joint>d:raise RuntimeError('source rank exceeds theoretical ordinary-unit dimension')
    result={'curve':curve,'p':7,'point_count':count,'source_columns':binding['source_unit_columns'],'ordinary_chi_unit_dimension_under_retained_full_image':d,'rank_checks':ranks,'ordinary_unit_kernel_upper':d-joint,'class_term':'retained; no class completeness inferred','divisor_term':'retained unless separately bounded','unit_admission':binding['unit_authentication'],'source_or_Selmer_equality_not_claimed':True,'seconds':spent}
    (out/'RESULT.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result))

if __name__=='__main__':main()
