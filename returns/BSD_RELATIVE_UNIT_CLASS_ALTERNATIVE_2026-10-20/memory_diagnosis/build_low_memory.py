from pathlib import Path
import difflib,hashlib,json,subprocess,time
r=Path(__file__).resolve().parent
src=Path("/Users/bsm/BSD_RANK_TWO_JOINT_CONTINUATION_2026-10-18/pari_partial_source/buch2.c")
orig=src.read_text()
(r/"buch2.original.c").write_text(orig)
patched=orig.replace('#include "pari.h"','#define Buchall_param bsd_lowmem_Buchall_param\n#include "pari.h"',1)
needle="    prim[2] = p; LP = idealprimedec_limit_f(nf,prim, l);"
assert patched.count(needle)==1
replacement="""    prim[2] = p;
    {
      pari_sp avp = avma;
      LP = idealprimedec_limit_f(nf,prim, l);
      LP = gerepilecopy(avp, LP);
    }"""
patched=patched.replace(needle,replacement)
patched+="\nGEN bsd_lowmem_init(GEN nf) { return bsd_lowmem_Buchall_param(nf, 0.02, 0., 4, nf_FORCE, DEFAULTPREC); }\n"
(r/"buch2.lowmem.c").write_text(patched)
(r/"low_memory.patch").write_text("".join(difflib.unified_diff(orig.splitlines(True),patched.splitlines(True),fromfile="buch2.original.c",tofile="buch2.lowmem.c")))
prefix=Path("/Users/bsm/run040-order7-cayley-coordinate-slice-genus-census-2026-09-03/tools/sage-env")
cmd=["/usr/bin/clang","-arch","x86_64","-O1","-fPIC","-dynamiclib",str(r/"buch2.lowmem.c"),"-I"+str(prefix/"include/pari"),"-L"+str(prefix/"lib"),"-lpari","-Wl,-rpath,"+str(prefix/"lib"),"-o",str(r/"libbsd_lowmem.dylib")]
t=time.monotonic()
p=subprocess.run(cmd,capture_output=True,timeout=180)
(r/"BUILD.stdout").write_bytes(p.stdout);(r/"BUILD.stderr").write_bytes(p.stderr)
receipt={"command":cmd,"exit_code":p.returncode,"elapsed_seconds":time.monotonic()-t,"original_source_sha256":hashlib.sha256(orig.encode()).hexdigest(),"patched_source_sha256":hashlib.sha256(patched.encode()).hexdigest()}
if (r/"libbsd_lowmem.dylib").exists():receipt["library_sha256"]=hashlib.sha256((r/"libbsd_lowmem.dylib").read_bytes()).hexdigest()
(r/"BUILD_RECEIPT.json").write_text(json.dumps(receipt,indent=2)+"\n")
print(json.dumps(receipt,indent=2))
