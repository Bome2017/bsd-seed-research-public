#!/usr/bin/env python3
from pathlib import Path
import subprocess,time,json,re,hashlib
R=Path(__file__).resolve().parent
GP='/Users/bsm/run040-order7-cayley-coordinate-slice-genus-census-2026-09-03/tools/sage-env/bin/gp'
cs=json.loads((R/'SCREEN_CANDIDATES.json').read_text());out=[];start=time.monotonic()
for c in cs:
 if time.monotonic()-start>90:break
 d=R/'screen'/c['label'];d.mkdir(parents=True,exist_ok=True)
 script='''alarm(12);setrand(20261020);read("../../lib/cubinv.gp");read("../../lib/classimg.gp");read("../../lib/selmer.gp");
E=ellinit(MODEL);P=POINTS;for(i=1,#P,if(!ellisoncurve(E,P[i]),error("point")));
FD=field3(E);B=bnfinit(FD[1],1);ix=select(i->B.cyc[i]%3==0,[1..#B.cyc]);print("CLASS=",B.cyc,";DIM=",#ix);
if(#ix<2,print("SCREEN_COMPLETE_NO_MULTIPLE_CLASS");quit);
nf=B.nf;T=torsT(E,nf);tau=tauL(nf,E,T);CA=matrix(#ix,#ix);
{for(j=1,#ix,my(J=idealpow(nf,B.gen[ix[j]],B.cyc[ix[j]]/3),v=bnfisprincipal(B,nfgaloisapply(nf,tau,J),0));for(i=1,#ix,if(v[ix[i]]%(B.cyc[ix[i]]/3),error("class action nonintegral"));CA[i,j]=v[ix[i]]/(B.cyc[ix[i]]/3)));}
F=matker(Mod(CA+matid(#ix),3));print("FAITHFUL_DIM=",#F,";ACTION=",CA);
if(#F>=2,writebin("provisional_bnf.bin",B);write("context.gp",[E,P,FD,T,tau,ix,CA,F]);print("SCREEN_SELECTED_PROVISIONAL"),print("SCREEN_COMPLETE_NO_MULTIPLE_FAITHFUL_CLASS"));quit;
'''.replace('MODEL',c['model']).replace('POINTS',c['points'])
 (d/'screen.gp').write_text(script);st=time.monotonic()
 try:
  p=subprocess.run([GP,'-q','-f','-s','128000000'],input=script,text=True,cwd=d,capture_output=True,timeout=min(15,max(1,94-(st-start))))
  so,se=p.stdout,p.stderr;selected='SCREEN_SELECTED_PROVISIONAL' in so;valid=p.returncode==0 and not se.strip() and ('SCREEN_COMPLETE' in so or selected);status='selected_provisional' if selected and valid else 'screened' if valid else 'rejected'
 except subprocess.TimeoutExpired as e:
  so=(e.stdout or b'').decode() if isinstance(e.stdout,bytes) else e.stdout or '';se=(e.stderr or b'').decode() if isinstance(e.stderr,bytes) else e.stderr or '';status='timeout';selected=False
 (d/'screen.out').write_text(so);(d/'screen.err').write_text(se)
 rec={'label':c['label'],'status':status,'seconds':round(time.monotonic()-st,3),'stdout':so.strip(),'source':'provisional_selection_only'};out.append(rec)
 (R/'SCREEN_RESULT.json').write_text(json.dumps({'completed':len(out),'panel':len(cs),'seconds':round(time.monotonic()-start,3),'results':out},indent=2)+'\n')
 print(json.dumps(rec),flush=True)
 if selected:break
