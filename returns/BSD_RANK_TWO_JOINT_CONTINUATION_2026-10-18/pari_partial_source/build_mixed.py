from pathlib import Path
import subprocess,time,json,hashlib,difflib
R=Path('/Users/bsm/BSD_RANK_TWO_JOINT_CONTINUATION_2026-10-18/pari_partial_source');B=Path('/Users/bsm/BSD_RANK_TWO_JOINT_CONTINUATION_2026-10-18_PARI_BUILD')
orig=(R/'buch2.c').read_text();s=orig.replace('#include "pari.h"','#define Buchall_param bsd_mixed_Buchall_param\n#include "pari.h"',1)
s=s.replace('#define DEBUGLEVEL DEBUGLEVEL_bnf','#define DEBUGLEVEL DEBUGLEVEL_bnf\nstatic GEN BSD_CENTRAL, BSD_ZK;\nstatic long BSD_TRIED=0, BSD_FOUND=0;',1)
needle='  r = gaussred_from_QR(RgM_mul(G, ideal), prec);'
block='''  if (!gequal(BSD_ZK, nf_get_zk(nf))) pari_err(e_MISC,"BSD integral basis changed");
  {
    long bi,bj,bs,nt=0;
    for (bi=2; bi<=N && nt<128; bi++) for (bj=1; bj<bi && bj<=8 && nt<128; bj++) for(bs=-1;bs<=1 && nt<128;bs+=2)
    {
      pari_sp bav=avma;
      GEN a=bs==1? gadd(gel(ideal,bi),gel(ideal,bj)):gsub(gel(ideal,bi),gel(ideal,bj));
      GEN ca=ZM_ZC_mul(BSD_CENTRAL,a);
      if (!gequal(a,ca) && !gequal(a,gneg(ca)))
      {
        nt++;BSD_TRIED++;
        if(factorgen(F,nf,I,NI,a,fact))
        {
          err_printf("BSD_MIXGEN=%Ps\\n",lift(basistoalg(nf,a)));
          BSD_FOUND++;
          if(BSD_FOUND>=64) pari_err(e_MISC,"BSD mixed capture limit reached");
        }
      }
      set_avma(bav);
    }
    err_printf("BSD_MIX_PROGRESS tried=%ld found=%ld\\n",BSD_TRIED,BSD_FOUND);
  }
  return 0; /* source-only pass, no claim of completed BNF */
'''
assert s.count(needle)==1;s=s.replace(needle,block+needle)
s+='\nGEN bsd_mixed_collect(GEN nf, GEN central) { BSD_CENTRAL=central; BSD_ZK=nf_get_zk(nf); BSD_TRIED=BSD_FOUND=0; return bsd_mixed_Buchall_param(nf,0.01,0.1,4,nf_FORCE,DEFAULTPREC); }\n'
(R/'buch2.mixed.c').write_text(s);(R/'mixed_instrumentation.patch').write_text(''.join(difflib.unified_diff(orig.splitlines(True),s.splitlines(True),fromfile='buch2.c',tofile='buch2.mixed.c')))
(R/'MIXED_CONTRACT.md').write_text('''# Changed mixed-parity geometry pass\n\nFirst capture: all1424 exact generators are fixed by central[-1]; their faithful projections are seventh powers identically. New source: for each LLL-reduced integral prime ideal, take sums/differences of two actual reduced-ideal columns, with the smaller index at most8; keep at most128 mixed-parity candidates per ideal. No half-projectors are used. factorgen is only a cheap candidate filter. Cap64 smooth exported mixed generators or117 seconds, whichever first. Each export is an exact algebraic polynomial. Current NF integral basis is compared literally with the input basis before applying its authenticated central matrix. All accepted ordinary units require independent complete principal ideals and integer kernel in unmodified GP. No completed class or full-unit claim.\n''')
P=Path('/Users/bsm/run040-order7-cayley-coordinate-slice-genus-census-2026-09-03/tools/sage-env')
cmd=['/usr/bin/clang','-arch','x86_64','-O1','-fPIC','-dynamiclib',str(R/'buch2.mixed.c'),'-I'+str(P/'include/pari'),'-L'+str(P/'lib'),'-lpari','-Wl,-rpath,'+str(P/'lib'),'-o',str(B/'libbsdmixed.dylib')];t=time.monotonic();p=subprocess.run(cmd,capture_output=True,text=True,timeout=120)
(R/'MIXED_BUILD.stdout').write_text(p.stdout);(R/'MIXED_BUILD.stderr').write_text(p.stderr);rec={'command':cmd,'elapsed_seconds':time.monotonic()-t,'exit_code':p.returncode,'source_sha256':hashlib.sha256(s.encode()).hexdigest()}
if p.returncode==0:rec['library_sha256']=hashlib.sha256((B/'libbsdmixed.dylib').read_bytes()).hexdigest()
(R/'MIXED_BUILD_RECEIPT.json').write_text(json.dumps(rec,indent=2)+'\n');print(rec);print(p.stderr[-1000:])
