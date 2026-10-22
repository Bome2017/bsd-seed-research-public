from pathlib import Path
import difflib,hashlib,json,subprocess,time
r=Path(__file__).resolve().parent
s=(r/"buch2.lowmem.c").read_text()
a=s.index("FBgen(FB_t *F")
b=s.index("\nstatic int\nGRHchk",a)
part=s[a:b]
part=part.replace("  long i, ip;","  long i, ip;\n  ulong bsd_seen=0, bsd_logical=0, bsd_retained=0, bsd_discarded=0;")
part=part.replace("    ulong p = pr->p;","    ulong p = pr->p;\n    if (++bsd_seen % 1000 == 0) err_printf(\"BSD_FB_PROFILE p=%lu seen=%lu accepted=%ld stack=%lu retained=%lu logical=%lu discarded=%lu\\n\",p,bsd_seen,i,(ulong)(pari_mainstack->top-avma),bsd_retained,bsd_logical,bsd_discarded);")
part=part.replace("      LP = gerepilecopy(avp, LP);","      { ulong bsd_before = (ulong)(avp-avma);\n        LP = gerepilecopy(avp, LP);\n        bsd_retained += (ulong)(avp-avma);\n        bsd_discarded += bsd_before-(ulong)(avp-avma);\n        bsd_logical += (ulong)gsizebyte(LP);\n      }")
part=part.replace("  F->perm = NULL;","  err_printf(\"BSD_FB_PROFILE_COMPLETE seen=%lu accepted=%ld stack=%lu retained=%lu logical=%lu discarded=%lu KC=%ld\\n\",bsd_seen,i,(ulong)(pari_mainstack->top-avma),bsd_retained,bsd_logical,bsd_discarded,F->KC);\n  F->perm = NULL;")
patched=s[:a]+part+s[b:]
(r/"buch2.profile.c").write_text(patched)
(r/"profile.patch").write_text("".join(difflib.unified_diff(s.splitlines(True),patched.splitlines(True),fromfile="buch2.lowmem.c",tofile="buch2.profile.c")))
prefix=Path("/Users/bsm/run040-order7-cayley-coordinate-slice-genus-census-2026-09-03/tools/sage-env")
cmd=["/usr/bin/clang","-arch","x86_64","-O1","-fPIC","-dynamiclib",str(r/"buch2.profile.c"),"-I"+str(prefix/"include/pari"),"-L"+str(prefix/"lib"),"-lpari","-Wl,-rpath,"+str(prefix/"lib"),"-Wl,-exported_symbol,_bsd_lowmem_init","-o",str(r/"libbsd_profile.dylib")]
t=time.monotonic();p=subprocess.run(cmd,capture_output=True,timeout=180)
(r/"PROFILE_BUILD.stdout").write_bytes(p.stdout);(r/"PROFILE_BUILD.stderr").write_bytes(p.stderr)
receipt={"command":cmd,"exit_code":p.returncode,"elapsed_seconds":time.monotonic()-t,"source_sha256":hashlib.sha256(patched.encode()).hexdigest()}
if (r/"libbsd_profile.dylib").exists():receipt["library_sha256"]=hashlib.sha256((r/"libbsd_profile.dylib").read_bytes()).hexdigest()
(r/"PROFILE_BUILD_RECEIPT.json").write_text(json.dumps(receipt,indent=2)+"\n");print(json.dumps(receipt,indent=2))
