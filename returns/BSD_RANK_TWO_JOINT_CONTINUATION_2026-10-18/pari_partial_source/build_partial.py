from pathlib import Path
import json,hashlib,subprocess,time,difflib
root=Path('/Users/bsm/BSD_RANK_TWO_JOINT_CONTINUATION_2026-10-18/pari_partial_source')
build=Path('/Users/bsm/BSD_RANK_TWO_JOINT_CONTINUATION_2026-10-18_PARI_BUILD');build.mkdir(exist_ok=True)
orig=(root/'buch2.c').read_text()
patched=orig.replace('#include "pari.h"','#define Buchall_param bsd_Buchall_param\n#include "pari.h"',1)
needle='    /* make sure we get maximal rank first, then allow all relations */'
assert patched.count(needle)==1
patched=patched.replace(needle,'    err_printf("BSD_RELGEN=%Ps\\n", lift(basistoalg(nf, gx)));\n'+needle)
patched+='\nGEN bsd_partial_collect(GEN nf) { return bsd_Buchall_param(nf, 0.01, 0.1, 4, nf_FORCE, DEFAULTPREC); }\n'
(root/'buch2.partial.c').write_text(patched)
(root/'instrumentation.patch').write_text(''.join(difflib.unified_diff(orig.splitlines(True),patched.splitlines(True),fromfile='buch2.c',tofile='buch2.partial.c')))
(root/'CONTRACT.md').write_text('''# Partial relation-generator capture\n\nChanged source: export the exact algebraic generator before PARI 2.17.3 rejects a relation during rank collection. No internal relation vector will be trusted. Every admitted product requires complete principal-ideal authentication in unmodified GP and an integer divisor relation. Build <=120 s; one harvest <=120 s; independent authentication/kernel <=120 s. No BNF or class-group conclusion follows from unfinished collection. The fixed source is the rank-two -47 twist of 11a1 at p=7. Goal: at least two independently rejecting faithful unit directions, not a complete unit basis. Failure of this bounded capture is not nonexistence.\n''')
prefix=Path('/Users/bsm/run040-order7-cayley-coordinate-slice-genus-census-2026-09-03/tools/sage-env')
cmd=['/usr/bin/clang','-arch','x86_64','-O1','-fPIC','-dynamiclib',str(root/'buch2.partial.c'),'-I'+str(prefix/'include/pari'),'-L'+str(prefix/'lib'),'-lpari','-Wl,-rpath,'+str(prefix/'lib'),'-o',str(build/'libbsdpartial.dylib')]
t=time.monotonic()
try:
 p=subprocess.run(cmd,capture_output=True,text=True,timeout=120)
 status={'exit_code':p.returncode,'timeout':False};out,err=p.stdout,p.stderr
except subprocess.TimeoutExpired as e:status={'exit_code':None,'timeout':True};out=e.stdout or '';err=e.stderr or ''
(root/'BUILD.stdout').write_text(out);(root/'BUILD.stderr').write_text(err)
status.update(command=cmd,wall_seconds=time.monotonic()-t,source_sha256=hashlib.sha256(patched.encode()).hexdigest())
lib=build/'libbsdpartial.dylib'
if lib.exists():status['library_sha256']=hashlib.sha256(lib.read_bytes()).hexdigest()
(root/'BUILD_RECEIPT.json').write_text(json.dumps(status,indent=2)+'\n')
print(json.dumps(status,indent=2));print(err[-5000:])
