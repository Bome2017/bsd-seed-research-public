"""Independent Linux execution of the legacy/patched C acceptance regression.
The supplied C files are compiled unchanged. A local compatibility header maps
only CommonCrypto SHA-256 calls to OpenSSL; elliptic-curve arithmetic is untouched.
This checks two small records, not the large retained corpus.
"""
from pathlib import Path
import argparse, contextlib, hashlib, io, json, runpy, struct, subprocess, tempfile
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('release', type=Path, help='Extracted bsd-seed-research directory')
ROOT = parser.parse_args().release.resolve()
if not (ROOT/'tools/replay/coefficient_verifier_regression.py').is_file():
    raise SystemExit('Not a supported release directory')
res = {}
with contextlib.redirect_stdout(io.StringIO()):
    ns = runpy.run_path(str(ROOT/'tools/replay/coefficient_verifier_regression.py'))
res['genuine_witness'] = ns['good']
res['true_trace'] = ns['true_a']
res['sources'] = {}
res['tests'] = []
with tempfile.TemporaryDirectory() as td:
    t=Path(td); (t/'CommonCrypto').mkdir(); (t/'wit').mkdir(); (t/'out').mkdir()
    (t/'CommonCrypto/CommonDigest.h').write_text('''#include <stdint.h>
#include <openssl/sha.h>
typedef SHA256_CTX CC_SHA256_CTX;
typedef uint32_t CC_LONG;
#define CC_SHA256_Init SHA256_Init
#define CC_SHA256_Update SHA256_Update
#define CC_SHA256_Final SHA256_Final
#define CC_SHA256 SHA256
''')
    sources = [('legacy', ROOT/'evidence/src/BSD_RIGOROUS_STREAM_CORE_2026-09-19/verifier/wverify.c'),
               ('repaired', ROOT/'review/repairs/wverify_distinct.c')]
    for label,src in sources:
        res['sources'][label] = hashlib.sha256(src.read_bytes()).hexdigest()
        for sanitized in (False,True):
            exe=t/(label+('_ubsan' if sanitized else ''))
            cmd=['clang','-O2','-Wno-deprecated-declarations','-I',str(t),str(src),'-lcrypto','-o',str(exe)]
            if sanitized: cmd += ['-fsanitize=undefined','-fno-sanitize-recover=all']
            cp=subprocess.run(cmd,capture_output=True,text=True,timeout=30)
            assert cp.returncode==0, cp.stderr
            for name,a,x,fs in [('malicious',68,59,ns['bad']),('genuine',ns['true_a'],*ns['good'])]:
                data=struct.pack('<QQQ',0,4100,1)+struct.pack('<QiBB',4099,a,x,len(fs))+b''.join(struct.pack('<QB',q,e) for q,e in fs)
                (t/'wit/wit_000000.bin').write_bytes(data)
                args=[str(exe),'wit','0','-22735','0','106272484','0','4099','4096','4100',str(t/'wit'),str(t/'out'),'0','1']
                p=subprocess.run(args,capture_output=True,text=True,timeout=15)
                expect=3 if label=='repaired' and name=='malicious' else 0
                assert p.returncode==expect,(label,name,p.returncode,p.stderr)
                if expect==0:
                    assert struct.unpack('<i',(t/'out/ap_000000.bin').read_bytes()[-4:])[0]==a
                else:
                    assert 'duplicate prime factor' in p.stderr
                res['tests'].append({'source':label,'ubsan':sanitized,'case':name,'exit':p.returncode,'stdout':p.stdout.strip(),'stderr':p.stderr.strip()})
res['status']='PASS'
res['scope']='Unchanged mathematical C sources; SHA-256 compatibility header only; two records, with and without UBSan.'
print(json.dumps(res,indent=2))
