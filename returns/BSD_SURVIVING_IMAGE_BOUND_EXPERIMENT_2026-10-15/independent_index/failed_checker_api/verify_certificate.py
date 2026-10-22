#!/usr/bin/env python3
"""Read-only literal divisor replay; determinant norm, no producer imported."""
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent
GP = '/Users/bsm/run040-order7-cayley-coordinate-slice-genus-census-2026-09-03/tools/sage-env/bin/gp'


def verify_case(folder):
    code = r'''
alarm(60);
C=read("divisor_certificate.gp");fA=C[1];fB=C[2];F=C[3];W=C[4];tau=C[5];
nA=nfinit(fA);nB=nfinit(fB);PA=C[6];PB=C[7];XA=C[8];XB=C[9];
S=Set(vector(#PA,i,PA[i].p));
PP=concat(vector(#S,i,idealprimedec(nA,S[i])));
QQ=concat(vector(#S,i,idealprimedec(nB,S[i])));
if(#PP!=#PA||#QQ!=#PB,error("prime list incomplete"));
for(i=1,#PA,if(idealhnf(nA,PP[i])!=idealhnf(nA,PA[i]),error("source prime identity")));
for(i=1,#PB,if(idealhnf(nB,QQ[i])!=idealhnf(nB,PB[i]),error("target prime identity")));
if(subst(fA,w,tau)!=0||subst(lift(tau),w,tau)!=Mod(w,fA),error("source involution"));
if(subst(fA,w,W)!=0,error("source embedding"));
VA=matrix(#PA,#XA,i,j,nfeltval(nA,XA[j],PA[i]));
VB=matrix(#PB,#XB,i,j,nfeltval(nB,XB[j],PB[i]));
if(VA!=matid(#PA)||VB!=matid(#PB),error("approximation valuations"));
TA=matrix(#PA,#XA,i,j,nfeltval(nA,subst(lift(XA[j]),w,tau),PA[i]));
TB=matrix(#PB,#XB,i,j,nfeltval(nB,subst(lift(XB[j]),z,Mod(-z,fB)),PB[i]));
if(TA!=C[10]||TB!=C[11],error("prime involution mismatch"));
DA=C[12];DB=C[13];
if(TA*DA!=-DA||TB*DB!=-DB,error("divisor anti condition"));
if(#DA!=(#PA-mattrace(TA))/2||#DB!=(#PB-mattrace(TB))/2,error("divisor rank"));
if(vecprod(matsnf(DA))!=1||vecprod(matsnf(DB))!=1,error("divisor lattice not primitive"));
AA=C[14];NN=C[15];
if(matrix(#PA,#AA,i,j,nfeltval(nA,AA[j],PA[i]))!=DA,error("source divisors"));
{for(j=1,#AA,my(g=subst(lift(AA[j]),w,W),M=matrix(3,3,i,k,polcoef(lift(g*Mod(x,F)^(k-1)),i-1,x)));if(matdet(M)!=NN[j],error("independent determinant norm mismatch")));}
VV=matrix(#PB,#NN,i,j,nfeltval(nB,NN[j],PB[i]));
if(VV!=C[16]||DB*C[17]!=VV,error("norm divisors"));
if(C[17]*C[18]!=3*matid(#DA)||C[18]*C[17]!=3*matid(#DA),error("reverse composition"));
print("CHECKED_DIVISOR_RANK=",#DA,";CHECKED_INDEX=",valuation(matdet(C[17]),3));
print("LITERAL_DIVISOR_CERTIFICATE_PASS");quit;
'''
    # readstr/eval is avoided; run one read file in an isolated temp directory.
    import tempfile
    import shutil
    with tempfile.TemporaryDirectory(prefix='bsd-divisor-verify-') as temp:
        temp = Path(temp)
        shutil.copyfile(folder / 'divisor_certificate.gp', temp / 'divisor_certificate.gp')
        (temp / 'verify.gp').write_text(code)
        result = subprocess.run([GP, '-q', '-f', '-s', '64000000'],
                                input='read("verify.gp");\nquit;\n', text=True,
                                capture_output=True, cwd=temp, timeout=70)
    assert result.returncode == 0 and not result.stderr, (result.returncode, result.stderr)
    assert 'LITERAL_DIVISOR_CERTIFICATE_PASS' in result.stdout, result.stdout
    return {'case': folder.name, 'stdout': result.stdout, 'stderr': result.stderr,
            'scope': 'literal prime decomposition, primitive divisor bases, determinant norms and valuations'}


if __name__ == '__main__':
    out = [verify_case(p) for p in [ROOT, ROOT / 'positive1913', ROOT / 'seed3_divisors']]
    print(json.dumps({'status': 'PASS', 'cases': out}, indent=2))
