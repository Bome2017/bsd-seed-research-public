from pathlib import Path
import json,re,subprocess,time
R=Path(__file__).resolve().parent;GP='/Users/bsm/run040-order7-cayley-coordinate-slice-genus-census-2026-09-03/tools/sage-env/bin/gp'
cs={c['label']:c for c in json.loads((R/'SCREEN_CANDIDATES.json').read_text())}
rows=[x for x in json.loads((R/'SCREEN_RESULT.json').read_text())['results'] if x['status']=='screened' and re.search(r';DIM=[1-9]',x['stdout'])]
results=[]
for row in rows:
 c=cs[row['label']];d=R/'occupancy'/c['label'];d.mkdir(parents=True,exist_ok=True)
 script='''alarm(30);setrand(20261020);read("../../lib/cubinv.gp");read("../../lib/classimg.gp");read("../../lib/selmer.gp");
E=ellinit(MODEL);P=POINTS;FD=field3(E);B=bnfinit(FD[1],1);nf=B.nf;T=torsT(E,nf);tau=tauL(nf,E,T);ix=select(i->B.cyc[i]%3==0,[1..#B.cyc]);CA=matrix(#ix,#ix);
{for(j=1,#ix,my(J=idealpow(nf,B.gen[ix[j]],B.cyc[ix[j]]/3),v=bnfisprincipal(B,nfgaloisapply(nf,tau,J),0));for(i=1,#ix,if(v[ix[i]]%(B.cyc[ix[i]]/3),error("class action"));CA[i,j]=v[ix[i]]/(B.cyc[ix[i]]/3)));}
CF=matker(Mod(CA+matid(#ix),3));PC=vector(#P,j,ftan(E,T,P[j]));PF=vector(#P,j,idealfactor(nf,PC[j]));PL=List();
{for(j=1,#P,for(i=1,matsize(PF[j])[1],my(pr=PF[j][i,1],known=0);for(k=1,#PL,if(pr==PL[k],known=1));if(!known,listput(PL,pr))));}
PL=Vec(PL);V=matrix(#PL,#P,i,j,nfeltval(nf,PC[j],PL[i]));K=matker(Mod(V,3));CP=matrix(#ix,#K);
{for(j=1,#K,my(v=V*lift(K[,j]),J=matid(8),lc);for(i=1,#PL,if(v[i]%3,error("point ideal val"));J=idealmul(nf,J,idealpow(nf,PL[i],v[i]/3)));lc=bnfisprincipal(B,J,0);for(i=1,#ix,if(lc[ix[i]]%(B.cyc[ix[i]]/3),error("point class denominator"));CP[i,j]=lc[ix[i]]/(B.cyc[ix[i]]/3)));}
CP=Mod(CP,3);if(Mod(CA+matid(#ix),3)*CP!=0*CP,error("point class notfaithful"));
print("CLASS=",B.cyc,";FAITHFUL_DIM=",#CF,";POINT_ORDINARY_DIM=",#K,";POINT_CLASS_RANK=",matrank(CP),";CLASS_ACTION=",CA,";POINT_CLASSES=",lift(CP));
write("arithmetic.gp",[E,P,FD,T,tau,ix,CA,CF,PC,PL,V,K,CP]);writebin("provisional_bnf.bin",B);
if(#CF>matrank(CP),print("UNOCCUPIED_CLASS_SELECTED"),print("POINT_OCCUPIED_ONLY"));quit;
'''.replace('MODEL',c['model']).replace('POINTS',c['points'])
 (d/'occupancy.gp').write_text(script);st=time.monotonic()
 try:
  x=subprocess.run([GP,'-q','-f','-s','128000000'],input=script,text=True,cwd=d,capture_output=True,timeout=35);so,se=x.stdout,x.stderr;ok=x.returncode==0 and not se.strip();selected=ok and 'UNOCCUPIED_CLASS_SELECTED' in so
 except subprocess.TimeoutExpired as e:so=str(e.stdout);se=str(e.stderr);ok=False;selected=False
 (d/'occupancy.out').write_text(so);(d/'occupancy.err').write_text(se)
 rec={'label':c['label'],'status':'selected_provisional' if selected else 'point_occupied_provisional' if ok and 'POINT_OCCUPIED_ONLY' in so else 'rejected','seconds':round(time.monotonic()-st,3),'stdout':so};results.append(rec)
 (R/'OCCUPANCY_RESULT.json').write_text(json.dumps({'panel':len(rows),'results':results},indent=2)+'\n');print(json.dumps(rec),flush=True)
 if selected:break
