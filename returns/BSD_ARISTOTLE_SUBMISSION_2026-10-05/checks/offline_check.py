"""Run Harmonic's real SDK packer, with its transport replaced and no job sent."""
from pathlib import Path
import sys, asyncio, hashlib, json, tarfile, socket, tempfile, subprocess, os, argparse, importlib
from unittest.mock import patch
from types import SimpleNamespace

ROOT=Path(__file__).resolve().parent
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--project-dir',type=Path)
parser.add_argument('--sdk-dir',type=Path,default=ROOT/'sdk')
parser.add_argument('--output-dir',type=Path,default=ROOT)
parser.add_argument('--full-archive',type=Path)
args=parser.parse_args()
sys.path.insert(0,str(args.sdk_dir))
from aristotlelib.project import Project
from aristotlelib import api_request, local_file_utils
O=ROOT.parent
D=args.project_dir or (O/'project' if (O/'project').is_dir() else O/'aristotle_submission/BSD_SEED_ARISTOTLE_NATIVE_2026-10-05')
args.output_dir.mkdir(parents=True,exist_ok=True)
OUT=args.output_dir/'SDK_GENERATED_INPUT.tar.gz'
receipt={}
def sha(b):return hashlib.sha256(b).hexdigest()
bindings_path=ROOT/'SDK_SOURCE_BINDINGS.json'
modules=['aristotlelib.project','aristotlelib.local_file_utils','aristotlelib.api_request','aristotlelib.cli.command.submit']
bindings={name:sha(Path(importlib.import_module(name).__file__).read_bytes()) for name in modules}
if bindings_path.exists():
    assert bindings==json.loads(bindings_path.read_text()),'SDK source differs from the reviewed 2.1.0 files'
else:
    bindings_path.write_text(json.dumps(bindings,indent=2)+'\n')
class CapturedClient:
    async def __aenter__(self):return self
    async def __aexit__(self,*args):pass
    async def get(self,*args,**kw):raise AssertionError('Unexpected GET: preflight must be fully offline')
    async def post(self,endpoint,*,data,files,**kw):
        assert endpoint=='/project'
        assert len(files)==1 and files[0][0]=='input'
        name,body,kind=files[0][1]
        assert kind=='application/x-tar'
        assert len(body)<=local_file_utils.MAX_FILE_SIZE_BYTES
        OUT.write_bytes(body)
        receipt.update(transport='MOCKED_LOCAL_CAPTURE_NO_NETWORK',request_body=json.loads(data['body']),upload_name=name,payload_bytes=len(body),payload_sha256=sha(body),sdk_limit_bytes=local_file_utils.MAX_FILE_SIZE_BYTES)
        return SimpleNamespace(json=lambda:{'project_id':'OFFLINE-NOT-A-REAL-PROJECT','created_at':'2026-10-05T00:00:00Z','last_updated':'2026-10-05T00:00:00Z','description':'Offline packaging control','status':2,'has_input':True,'has_files':True})
def refuse_network(*args,**kwargs):raise AssertionError('Network forbidden in offline preflight')
async def main():
    with patch.object(api_request,'AristotleRequestClient',CapturedClient),patch.object(socket,'create_connection',refuse_network):
        r=await Project.create_from_directory(prompt='Read TASK.md. Run python3 prepare_reference.py, then follow the extracted ARISTOTLE_PROMPT.md. Attempt new arithmetic toward the fixed BSD seed.',project_dir=D)
        assert r.project_id=='OFFLINE-NOT-A-REAL-PROJECT'
asyncio.run(main())
expected={str(p.relative_to(D)):sha(p.read_bytes()) for p in D.rglob('*') if p.is_file()}
with tarfile.open(OUT) as t:
    actual={}
    for m in t.getmembers():
        assert m.isfile()
        assert not Path(m.name).is_absolute() and '..' not in Path(m.name).parts
        actual[m.name]=sha(t.extractfile(m).read())
assert expected==actual, {'missing':list(expected.keys()-actual.keys()),'extra':list(actual.keys()-expected.keys())}
receipt['all_project_files_in_sdk_payload']=True
receipt['files_verified']=len(actual)
receipt['source_file_sha256']=actual
with tempfile.TemporaryDirectory() as td:
    oversized=args.full_archive
    if oversized is None:
        oversized=Path(td)/'synthetic_oversize.bin'
        with oversized.open('wb') as f:f.truncate(local_file_utils.MAX_FILE_SIZE_BYTES+1)
    try:
        local_file_utils.read_file_safely(oversized)
        raise AssertionError('Oversize archive unexpectedly accepted')
    except local_file_utils.LeanProjectError as e:
        receipt['oversize_rejection_control']=str(e)
with tempfile.TemporaryDirectory() as td:
    temp=Path(td)
    (temp/'payload').mkdir()
    for name in ['prepare_reference.py','READING_SET_BINDING.json']:
        (temp/name).write_bytes((D/name).read_bytes())
    os.link(D/'payload/COMPLETE_READING_SET.zip',temp/'payload/COMPLETE_READING_SET.zip')
    run=subprocess.run([sys.executable,str(temp/'prepare_reference.py')],capture_output=True,text=True,check=True)
    receipt['reading_set_extraction']=json.loads(run.stdout)
    receipt['reading_set_extraction']['path']='temporary offline extraction; original files unchanged'
receipt['sdk_distribution']=json.loads((ROOT/'PYPI_RECEIPT.json').read_text())
receipt['status']='OFFLINE_SDK_PACKAGING_AND_READING_SET_VERIFIED'
receipt['server_submission']=False
receipt['real_project_created']=False
receipt['server_acceptance_or_quota_tested']=False
receipt['mathematical_proof_verified_by_this_check']=False
(args.output_dir/'OFFLINE_SDK_PREFLIGHT.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps({k:v for k,v in receipt.items() if k not in ['source_file_sha256','request_body']},indent=2))
