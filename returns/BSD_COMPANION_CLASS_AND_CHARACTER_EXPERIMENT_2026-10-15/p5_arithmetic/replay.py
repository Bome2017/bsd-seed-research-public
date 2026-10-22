#!/usr/bin/env python3
"""Cheap exact replay; never runs BNF or certification.
A process exit code is insufficient: algebra completion markers are required,
and the saved failed certification is required to stay failed.
"""
from pathlib import Path
import hashlib,json,subprocess,sys
R=Path(__file__).resolve().parent
GP=Path('/Users/bsm/run040-order7-cayley-coordinate-slice-genus-census-2026-09-03/tools/sage-env/bin/gp')
BIND=json.loads((R/'REPLAY_BINDINGS.json').read_text())
for f,h in BIND.items():
    assert hashlib.sha256((R/f).read_bytes()).hexdigest()==h,('binding mismatch',f)

def run(d):
    p=subprocess.run([str(GP),'-q','-f','-s','1000000000','check_exact.gp'],cwd=d,text=True,capture_output=True,timeout=30)
    marker='INDEPENDENT_EXACT_FIELD_POINT_SCALAR_IDEALS_PASS'
    assert p.returncode==0 and marker in p.stdout and not p.stderr.strip(),(d,p.returncode,p.stdout,p.stderr)
    return marker

def mm(a,b):
    return ((a[0]*b[0]+a[1]*b[2])%5,(a[0]*b[1]+a[1]*b[3])%5,(a[2]*b[0]+a[3]*b[2])%5,(a[2]*b[1]+a[3]*b[3])%5)
G={(1,0,0,1)};todo=list(G)
while todo:
    a=todo.pop()
    for b in [(1,1,0,1),(1,0,1,1)]:
        c=mm(a,b)
        if c not in G:G.add(c);todo.append(c)
assert len(G)==120 and all((a*d-b*c)%5==1 for a,b,c,d in G)

def invariants(a):
    a1,a2,a3,a4,a6=a;b2=a1*a1+4*a2;b4=2*a4+a1*a3;b6=a3*a3+4*a6
    b8=a1*a1*a6+4*a2*a6-a1*a3*a4+a2*a3*a3-a4*a4
    return {'disc':-b2*b2*b8-8*b4**3-27*b6*b6+9*b2*b4*b6,'c4':b2*b2-24*b4,'c6':-b2**3+36*b2*b4-216*b6}

def trace(a,q):
    a1,a2,a3,a4,a6=a
    # Count roots in y using the quadratic discriminant.
    n=1
    for x in range(q):
        d=((a1*x+a3)**2+4*(x**3+a2*x*x+a4*x+a6))%q
        n+=1+(0 if d==0 else (1 if pow(d,(q-1)//2,q)==1 else -1))
    return q+1-n

out={'field_exact_checks':{},'local_models':{},'saved_class_runs':{},'elementary_SL2_generation_order':len(G)}
for name,sub,q,cyc in [('389a1','',389,3),('37a1','control37',37,2)]:
    d=R/sub;a=json.loads((d/'arithmetic.json').read_text())
    out['field_exact_checks'][name]=run(d)
    inv=invariants(a['model']);assert inv['disc']==q and inv['c4']%q
    dd=int(a['discriminant']);fac={}
    for ell in (5,q):
        v=0
        while dd%ell==0:v+=1;dd//=ell
        fac[str(ell)]=v
    assert dd==1
    inv['point_field_discriminant_factorization']=fac
    inv.update({'bad_prime':q,'a5':trace(a['model'],5),'a_bad':trace(a['model'],q)})
    out['local_models'][name]=inv
    txt=(d/'class_group.gp.out').read_text()
    assert f'CLASS_NUMBER={cyc};' in txt
    cert_files=['class_group.gp']+(['class_quotient.gp'] if not sub else [])
    runs=[]
    for base in cert_files:
        so=(d/(base+'.out')).read_text();se=(d/(base+'.err')).read_text()
        assert 'CLASS_GROUP_QUOTIENT_CERTIFIED=' not in so
        assert 'CLASS_GROUP_CERTIFIED=' not in so and 'CERTIFIED_CLASS_GROUP_COMPLETE' not in so and 'BNFCERTIFY=1' not in so
        rec=json.loads((d/(base+'.receipt.json')).read_text())
        assert 'alarm interrupt' in se or rec['exit_code']!=0
        runs.append({'script':base,'certification':False,'alarm_seen':'alarm interrupt' in se,'exit_code':rec['exit_code']})
    out['saved_class_runs'][name]={'provisional_class_group':[cyc],'grade':'GRH_DEPENDENT','certification_attempts':runs,'whole_source_bound_if_class5_absent':3}
p=subprocess.run([sys.executable,'-B','check_divisors.py'],cwd=R,text=True,capture_output=True,timeout=30)
assert p.returncode==0 and 'EXACT_DIVISOR_AND_CHARACTER_CHECK_PASS' in p.stdout,(p.stdout,p.stderr)
out['divisor_character_status']='EXACT_PASS'
out['status']='EXACT_ARITHMETIC_REPLAY_PASS_CLASS_CERTIFICATION_NOT_OBTAINED'
(R/'REPLAY.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
