"""Exercise Harmonic's actual project packer with local mocked transport only."""
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch
import argparse
import asyncio
import hashlib
import importlib
import importlib.metadata
import json
import socket
import subprocess
import sys
import tarfile
import tempfile

from aristotlelib.project import Project
from aristotlelib import api_request, local_file_utils

ROOT = Path(__file__).resolve().parent
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--project-dir', type=Path, required=True)
parser.add_argument('--output-dir', type=Path, required=True)
args = parser.parse_args()
D, OUT = args.project_dir.resolve(), args.output_dir.resolve()
OUT.mkdir(parents=True, exist_ok=True)
def sha(data): return hashlib.sha256(data).hexdigest()
assert importlib.metadata.version('aristotlelib') == '2.1.0'
names = ['aristotlelib.project','aristotlelib.local_file_utils','aristotlelib.api_request','aristotlelib.cli.command.submit']
sources = {name: sha(Path(importlib.import_module(name).__file__).read_bytes()) for name in names}
assert sources == json.loads((ROOT / 'SDK_SOURCE_BINDINGS.json').read_text())
receipt = {'sdk_version': '2.1.0', 'sdk_source_bindings': sources,
           'server_submission': False, 'real_project_created': False,
           'credentials_requested': False, 'mathematical_proof_verified': False}
payload = OUT / 'SDK_GENERATED_INPUT.tar.gz'
prompt = (D / 'SUBMISSION_PROMPT.txt').read_text().strip()
class Capture:
    async def __aenter__(self): return self
    async def __aexit__(self, *args): pass
    async def get(self, *args, **kwargs): raise AssertionError('Unexpected GET')
    async def post(self, endpoint, *, data, files, **kwargs):
        assert endpoint == '/project' and len(files) == 1 and files[0][0] == 'input'
        name, body, kind = files[0][1]
        assert kind == 'application/x-tar'
        assert len(body) <= local_file_utils.MAX_FILE_SIZE_BYTES
        payload.write_bytes(body)
        receipt.update(transport='MOCKED_LOCAL_CAPTURE_NO_NETWORK',
                       request_body=json.loads(data['body']), upload_name=name,
                       payload_bytes=len(body), payload_sha256=sha(body),
                       sdk_limit_bytes=local_file_utils.MAX_FILE_SIZE_BYTES)
        return SimpleNamespace(json=lambda: {'project_id': 'OFFLINE-NOT-A-REAL-PROJECT',
            'created_at': '2026-10-07T00:00:00Z','last_updated': '2026-10-07T00:00:00Z',
            'description': 'Offline packaging control','status': 2,'has_input': True,'has_files': True})
def forbidden(*args, **kwargs): raise AssertionError('Network forbidden in offline check')
async def run():
    with patch.object(api_request,'AristotleRequestClient',Capture), \
         patch.object(socket,'create_connection',forbidden), \
         patch.object(socket.socket,'connect',forbidden):
        result = await Project.create_from_directory(prompt=prompt, project_dir=D)
        assert result.project_id == 'OFFLINE-NOT-A-REAL-PROJECT'
asyncio.run(run())
expected = {p.relative_to(D).as_posix(): sha(p.read_bytes()) for p in D.rglob('*') if p.is_file()}
actual = {}
with tarfile.open(payload) as t:
    for m in t:
        assert m.isfile() and not Path(m.name).is_absolute() and '..' not in Path(m.name).parts
        assert m.name not in actual
        actual[m.name] = sha(t.extractfile(m).read())
assert actual == expected
receipt.update(all_project_files_in_sdk_payload=True, files_verified=len(actual), source_file_sha256=actual)

with tempfile.TemporaryDirectory() as td:
    temp = Path(td)
    oversized = temp / 'oversize.bin'
    with oversized.open('wb') as f: f.truncate(local_file_utils.MAX_FILE_SIZE_BYTES + 1)
    try:
        local_file_utils.read_file_safely(oversized)
        raise AssertionError('oversize not rejected')
    except local_file_utils.LeanProjectError as e:
        receipt['oversize_rejection_control'] = str(e)

with tempfile.TemporaryDirectory() as td:
    temp = Path(td)
    # Minimal direct project, full two bound archive payloads.
    for name in ['prepare_reference.py','REFERENCE_BINDINGS.json']:
        (temp / name).write_bytes((D / name).read_bytes())
    (temp / 'payload').mkdir()
    for item in json.loads((D / 'REFERENCE_BINDINGS.json').read_text()):
        (temp / item['path']).write_bytes((D / item['path']).read_bytes())
    first = subprocess.run([sys.executable, str(temp / 'prepare_reference.py')], check=True, capture_output=True, text=True)
    second = subprocess.run([sys.executable, str(temp / 'prepare_reference.py')], check=True, capture_output=True, text=True)
    result = json.loads(first.stdout)
    assert json.loads(second.stdout) == result
    for item in result['archives']: item['root'] = Path(item['root']).name
    receipt['full_extraction_and_idempotent_recheck'] = result
receipt['status'] = 'OFFLINE_NATIVE_SDK_AND_BOTH_READING_SETS_VERIFIED'
(OUT / 'OFFLINE_SDK_PREFLIGHT.json').write_text(json.dumps(receipt, indent=2) + '\n')
print(json.dumps({k:v for k,v in receipt.items() if k not in ['source_file_sha256','request_body']}, indent=2))
