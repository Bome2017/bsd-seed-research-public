#!/usr/bin/env python3
"""Compile unchanged old/repaired arithmetic; shim only the SHA-256 API.
Reproduce exact regression using independently enumerated curve point counts.
Outputs are confined to this audit directory, not the release.
"""
import contextlib, io, json, pathlib, runpy, struct, subprocess
ROOT=pathlib.Path('/mnt/data/fresh_audit/bsd-seed-research')
OUT=pathlib.Path('/mnt/data/fresh_audit_results/c_verifier_test'); OUT.mkdir(exist_ok=True)
inc=OUT/'include'/'CommonCrypto'; inc.mkdir(parents=True,exist_ok=True)
(inc/'CommonDigest.h').write_text('''#include <openssl/sha.h>
typedef SHA256_CTX CC_SHA256_CTX;
typedef unsigned int CC_LONG;
#define CC_SHA256_Init SHA256_Init
#define CC_SHA256_Update SHA256_Update
#define CC_SHA256_Final SHA256_Final
#define CC_SHA256 SHA256
''')
with contextlib.redirect_stdout(io.StringIO()):
    g=runpy.run_path(str(ROOT/'tools/replay/coefficient_verifier_regression.py'))
assert g['true_a']==86
wd=OUT/'wit'; wd.mkdir(exist_ok=True)
od=OUT/'ap'; od.mkdir(exist_ok=True)
def witness(a,x,fs):
    return struct.pack('<QQQ',0,4100,1)+struct.pack('<QiBB',4099,a,x,len(fs))+b''.join(struct.pack('<QB',p,e) for p,e in fs)
genuine=witness(86,*g['good']); malicious=witness(68,59,g['bad'])
cases=[('false_duplicate',malicious),('genuine',genuine),('truncated',genuine[:-1]),('trailing',genuine+b'\x00'),('wrong_count',struct.pack('<QQQ',0,4100,2)+genuine[24:]),('wrong_q',genuine[:24]+struct.pack('<Q',4093)+genuine[32:])]
results=[]
for name,rel in [('legacy','evidence/src/BSD_RIGOROUS_STREAM_CORE_2026-09-19/verifier/wverify.c'),('repaired','review/repairs/wverify_distinct.c')]:
    exe=OUT/name
    cmd=['gcc','-O2','-fsanitize=undefined','-fno-sanitize-recover=all','-Wno-deprecated-declarations','-I',str(OUT/'include'),str(ROOT/rel),'-lcrypto','-o',str(exe)]
    r=subprocess.run(cmd,capture_output=True,text=True,timeout=30)
    assert r.returncode==0,r.stderr
    for cname,data in cases:
        (wd/'wit_000000.bin').write_bytes(data)
        cmd=[str(exe),'wit','0','-22735','0','106272484','0','4099','4096','4100',str(wd),str(od),'0','1']
        r=subprocess.run(cmd,capture_output=True,text=True,timeout=30)
        expected=0 if cname=='genuine' or (name=='legacy' and cname=='false_duplicate') else 3
        assert r.returncode==expected,(name,cname,r.returncode,r.stderr)
        aout=None
        if not r.returncode:
            aout=struct.unpack('<i',(od/'ap_000000.bin').read_bytes()[-4:])[0]
            assert aout==(68 if cname=='false_duplicate' else 86)
        results.append({'version':name,'case':cname,'exit_code':r.returncode,'last_coefficient':aout,'stdout':r.stdout.strip(),'stderr':r.stderr.strip()})
report={'platform':'Linux/GCC/OpenSSL SHA API shim; unchanged arithmetic; UBSan enabled','true_a4099':86,'malicious_a4099':68,'genuine_witness':g['good'],'cases':results}
(OUT/'results.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
