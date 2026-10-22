"""Produce a bounded-memory partial-sum variant of official PARI 2.17.3.
Only the quadratic twist summation range changes. No arithmetic approximation.
GPL-2.0-or-later derivative patch; original source retained separately.
"""
from pathlib import Path
import hashlib,subprocess,difflib,json
src=Path('third_party/pari-2.17.3-modsym.c')
runtime=Path('/Users/bsm/run040-order7-cayley-coordinate-slice-genus-census-2026-09-03/tools/sage-env')
s=src.read_text();assert hashlib.sha256(src.read_bytes()).hexdigest()=='27d2b2dfe6a836465f1c54bec1bd892c5bc223eca2f73bcbbaf3352cafe29851'
a=s.index('GEN\nmspadicmoments(GEN W, GEN PHI, long D)');b=s.index('static void\ncheckoms',a)
f=s[a:b]
f=f.replace('mspadicmoments(GEN W, GEN PHI, long D)','mspadicmoments_chunk(GEN W, GEN PHI, long D, long lo, long hi)')
f=f.replace('  checkmspadic(W);','  if (D == 1 || lo < 1 || hi > labs(D) || lo >= hi) pari_err_DOMAIN("mspadicmoments_chunk", "range", "invalid", stoi(lo), stoi(hi));\n  checkmspadic(W);')
assert f.count('for (b = 1; b < aD; b++)')==3
f=f.replace('for (b = 1; b < aD; b++)','for (b = lo; b < hi; b++)')
f=f.replace('      vca = cgetg(lphi,t_VEC);','      vca = cgetg(lphi,t_VEC);\n      for (i = 1; i < lphi; i++) gel(vca,i) = zerocol(S.dim);')
f=f.replace('gel(vca,i) = b==1? z: ZC_add(gel(vca,i), z);','gel(vca,i) = ZC_add(gel(vca,i), z);')
u=s[:a]+f+s[b:]
build=Path('build');build.mkdir(exist_ok=True)
(build/'modsym_chunk.c').write_text(u)
Path('checks/pari_chunk.patch').write_text(''.join(difflib.unified_diff(s.splitlines(True),u.splitlines(True),fromfile='pari-2.17.3/src/basemath/modsym.c',tofile='modsym_chunk.c')))
cmd=['clang','-O2','-dynamiclib',str(build/'modsym_chunk.c'),'-I'+str(runtime/'include/pari'),'-L'+str(runtime/'lib'),'-lpari','-Wl,-rpath,'+str(runtime/'lib'),'-o',str(build/'modsym_chunk.dylib')]
p=subprocess.run(cmd,capture_output=True,text=True)
Path('outputs/chunk_build.log').write_text(p.stdout+p.stderr)
assert p.returncode==0,p.stderr
Path('outputs/chunk_build.json').write_text(json.dumps({'source_sha256':hashlib.sha256(src.read_bytes()).hexdigest(),'patched_source_sha256':hashlib.sha256(u.encode()).hexdigest(),'command':cmd,'exit':p.returncode},indent=2)+'\n')
print('built partial-sum function')
