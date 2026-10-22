"""Synthetic negative controls for the new reference extractor, not BSD tests."""
from pathlib import Path
import hashlib
import json
import subprocess
import sys
import tempfile
import warnings
import zipfile

ROOT = Path(__file__).resolve().parent.parent
extractor = ROOT / 'templates/common/prepare_reference.py'
results = []
for case in ['parent_path','absolute_path','backslash','symlink','duplicate','digest_mismatch']:
    with tempfile.TemporaryDirectory() as td:
        p = Path(td)
        (p/'prepare_reference.py').write_bytes(extractor.read_bytes())
        zpath = p/'probe.zip'
        names = {'parent_path':'../escape','absolute_path':'/escape',
                 'backslash':'root/..\\escape','symlink':'root/link',
                 'duplicate':'root/a','digest_mismatch':'root/a'}
        with warnings.catch_warnings():
            warnings.simplefilter('ignore', UserWarning)
            with zipfile.ZipFile(zpath,'w') as z:
                info = zipfile.ZipInfo(names[case])
                info.external_attr = (0o120777 if case=='symlink' else 0o100644) << 16
                z.writestr(info,b'x')
                if case=='duplicate': z.writestr(info,b'y')
        with zipfile.ZipFile(zpath) as z: size = sum(i.file_size for i in z.infolist())
        digest = hashlib.sha256(zpath.read_bytes()).hexdigest()
        if case=='digest_mismatch': digest = '0'*64
        binding = {'path':'probe.zip','bytes':zpath.stat().st_size,'sha256':digest,
                   'destination':'dest','root':'root','manifest':'MANIFEST.sha256',
                   'manifest_entries':0,'expanded_bytes':size}
        (p/'REFERENCE_BINDINGS.json').write_text(json.dumps([binding]))
        run = subprocess.run([sys.executable,str(p/'prepare_reference.py')],capture_output=True,text=True)
        assert run.returncode != 0, case
        assert not (p/'escape').exists(), case
        results.append({'case':case,'rejected':True,'diagnostic':run.stderr.splitlines()[-1]})
(ROOT/'checks/EXTRACTOR_SECURITY.json').write_text(json.dumps(results,indent=2)+'\n')
print(json.dumps({'negative_controls_passed':len(results),'mathematical_claims_checked':False}))
