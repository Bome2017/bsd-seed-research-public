"""Prepare B's October 7 correction overlay; no network or research execution."""
from pathlib import Path, PurePosixPath
import difflib
import hashlib
import io
import json
import shutil
import subprocess
import tarfile
import zipfile

ROOT = Path(__file__).resolve().parent
BASE = ROOT.parent
LAB = Path('/Users/bsm/BSD_GITHUB_UPDATE_CODEX_2026-10-04/lab')
OLDROOT = Path('/Users/bsm/BSD_EXCESS_CONTROL_ATTEMPT_CODEX_2026-10-06')
OLD = OLDROOT/'build_release/BSD_ARISTOTLE_GLOBAL_SUPPORT_B_2026-10-06/project'
PIN = '062b7f9c858e64cbf2037148c1d6c7fe635595ca'
REVIEWS = [
    'BSD_ARISTOTLE_EXCESS_A_REVIEW_CODEX_2026-10-07',
    'BSD_ARISTOTLE_EXCESS_A_CORRECTION_REVIEW_CODEX_2026-10-07',
]
BUILD = BASE/'build'
OUTER = BUILD/'BSD_ARISTOTLE_GLOBAL_SUPPORT_B_2026-10-07'
PROJECT = OUTER/'project'

def sha(data): return hashlib.sha256(data).hexdigest()
def write(p, data):
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_bytes(data if isinstance(data, bytes) else data.encode())
def js(p, data): write(p, json.dumps(data, indent=2, ensure_ascii=False)+'\n')
def verify(root, manifest='MANIFEST.sha256'):
    seen = set()
    for line in (root/manifest).read_text().splitlines():
        digest, name = line.split('  ', 1)
        rel = PurePosixPath(name)
        assert not rel.is_absolute() and '..' not in rel.parts and name not in seen
        seen.add(name)
        assert sha((root/name).read_bytes()) == digest, name
    assert seen == {p.relative_to(root).as_posix() for p in root.rglob('*') if p.is_file() and p != root/manifest}
    return len(seen)
def manifest(root):
    # Nested manifests are also evidence and must be bound by the outer manifest.
    files = sorted(p for p in root.rglob('*') if p.is_file() and p != root/'MANIFEST.sha256')
    write(root/'MANIFEST.sha256', ''.join(f'{sha(p.read_bytes())}  {p.relative_to(root).as_posix()}\n' for p in files))
    return verify(root)
def makezip(root, dest):
    with zipfile.ZipFile(dest,'w',zipfile.ZIP_DEFLATED,compresslevel=9) as z:
        for p in sorted(root.rglob('*')):
            if not p.is_file(): continue
            assert not p.is_symlink()
            entry = zipfile.ZipInfo(f'{root.name}/{p.relative_to(root).as_posix()}', (2026,10,7,0,0,0))
            entry.external_attr = 0o100644 << 16
            entry.compress_type = zipfile.ZIP_DEFLATED
            z.writestr(entry,p.read_bytes())
    with zipfile.ZipFile(dest) as z:
        assert z.testzip() is None
        return sum(i.file_size for i in z.infolist())

assert subprocess.check_output(['git','-C',str(LAB),'rev-parse',PIN]).decode().strip()==PIN
oldcount = verify(OLD)
BUILD.mkdir(exist_ok=False)
shutil.copytree(OLD,PROJECT)
overlay = BUILD/'overlay/BSD_A_CORRECTIONS_2026-10-07'
overlay.mkdir(parents=True)
paths = ['work/returns/'+name for name in REVIEWS]
data = subprocess.check_output(['git','-C',str(LAB),'archive',PIN,*paths])
with tarfile.open(fileobj=io.BytesIO(data)) as tar:
    for item in tar:
        if item.isdir(): continue
        rel = PurePosixPath(item.name)
        assert item.isfile() and not rel.is_absolute() and '..' not in rel.parts
        assert rel.parts[:2]==('work','returns') and rel.parts[2] in REVIEWS
        write(overlay/Path(*rel.parts[2:]),tar.extractfile(item).read())
review_counts = {name:verify(overlay/name) for name in REVIEWS}
shutil.copy2(ROOT/'CORRECTIONS_FIRST.md',overlay/'READ_FIRST.md')
bindings = {
    'source_commit':PIN,
    'first_review_commit':'8ee52fb55c6788d48f288257ef12e6da7b4d8c4c',
    'reviews_copied_from_git_blobs':True,
    'review_manifest_counts':review_counts,
    'archive_containers_not_duplicated':True,
    'certificate_core_included':True,
    'external_coefficient_prefix_included':False,
    'runtime_included':False,
    'new_finite_sum_replay':False,
    'mathematical_grades_unchanged':True,
    'source_urls':{name:f'https://github.com/Bome2017/bsd-seed-lab/tree/{PIN}/work/returns/{name}' for name in REVIEWS},
}
js(overlay/'SOURCE_BINDINGS.json',bindings)
count=manifest(overlay)
zip_path=PROJECT/'payload/A_CORRECTIONS.zip'
expanded=makezip(overlay,zip_path)
refs=json.loads((PROJECT/'REFERENCE_BINDINGS.json').read_text())
refs.append({'path':'payload/A_CORRECTIONS.zip','bytes':zip_path.stat().st_size,'sha256':sha(zip_path.read_bytes()),
    'destination':'a_corrections','root':overlay.name,'manifest':'MANIFEST.sha256','manifest_entries':count,'expanded_bytes':expanded})
js(PROJECT/'REFERENCE_BINDINGS.json',refs)
shutil.copy2(ROOT/'CORRECTIONS_FIRST.md',PROJECT/'CORRECTIONS_FIRST.md')

task=(PROJECT/'TASK.md').read_text()
task=task.replace('Start by running `python3 prepare_reference.py`. Read COMMON_CONTRACT.md,',
    'Start by running `python3 prepare_reference.py`. Read CORRECTIONS_FIRST.md\n'
    'and both named A reviews before selecting a candidate. Its October 7\n'
    'corrections override conflicting older claims. Then read COMMON_CONTRACT.md,')
task=task.replace('including both runs and CLAUDE_CHECK.md.',
    'including both runs and CLAUDE_CHECK.md. That path is relative to\n'
    '`current_overlay/BSD_CURRENT_OVERLAY_2026-10-06/`.')
task=task.replace('## Search freedom and exact success criterion',
    '## Corrected A comparisons are not automatic collision rules\n\n'
    'A1 has not been identified with A2. The direct nonexceptional augmentation\n'
    'corollary is unavailable here, but that is not a ban on higher Fitting\n'
    'theory. Howard\'s reviewed scalar augmentation is a unit on its source\n'
    'domain. A3 could use a proved joint valuation bound without a separate\n'
    'regulator unit. Preserve the exact qualifications in CORRECTIONS_FIRST.md.\n'
    'A source-independent construction is not established merely because\n'
    'other candidates failed. Before substantial work, name the new arithmetic\n'
    'input that changes the first failed step of the closest prior candidate.\n\n'
    '## Search freedom and exact success criterion')
write(PROJECT/'TASK.md',task)
common=(PROJECT/'COMMON_CONTRACT.md').read_text()
common=common.replace("1. This project's TASK.md, COMMON_CONTRACT.md, CURRENT_FRONTIER.md and\n   RECENT_WALLS.md govern the new work.",
    '1. CORRECTIONS_FIRST.md and its two named October 7 reviews qualify the\n'
    '   older sources on their specified claims. TASK.md and this contract\n'
    '   govern the new work; CURRENT_FRONTIER.md and RECENT_WALLS.md retain\n'
    '   their other grades under that correction precedence.')
common=common.replace('It extracts and verifies both\narchives.', 'It extracts and verifies all three\nbound archives.')
common=common.replace('COVERAGE.json declares\nthe subsequent overlay and exact deduplications/omissions.',
    'COVERAGE.json preserves the original\noverlay inventory; COVERAGE_ADDENDUM.json declares this October 7 revision.')
write(PROJECT/'COMMON_CONTRACT.md',common)
extractor=(PROJECT/'prepare_reference.py').read_text().replace('Verify both bound archives','Verify all bound archives')
write(PROJECT/'prepare_reference.py',extractor)
write(PROJECT/'START_HERE.md', '''# Aristotle B: corrected October 7 input

PREPARED_NOT_SUBMITTED. This revision replaces the October 6 B input for a
future submission; it does not update or restart any existing remote job.

Work inside project/ (or the submitted project root). Run
`python3 prepare_reference.py`, then read CORRECTIONS_FIRST.md, TASK.md,
COMMON_CONTRACT.md and the two named A reviews. The extractor verifies three
archives and creates reading_set/, current_overlay/ and a_corrections/.
Hash verification is not reading or mathematical verification.

The original 5,180-entry reading set and 1,386-entry overlay are unchanged.
The added overlay contains both October 7 A reviews and the recovered small
twist certificate core. No claim of a fresh whole-computer search is made.
COVERAGE.json is the original inventory; COVERAGE_ADDENDUM.json binds this
revision and its limits. Missing external raw coefficients remain external.

The target is a construction controlling cofinite Sha[p] vanishing. It is
not another review of A, a twist-certificate replay, or a request to formalize
an already completed BSD proof. See SUBMISSION_PROMPT.txt if submitting.
''')
write(PROJECT/'SUBMISSION_PROMPT.txt', '''Read project/TASK.md (or TASK.md if the working directory is already the submitted project root). This is lane B: arithmetic construction of independent global support control for the fixed BSD seed. First run python3 prepare_reference.py. Read CORRECTIONS_FIRST.md and both named October 7 review reports/correction documents before selecting a candidate; they qualify the older sources. Then follow TASK.md and COMMON_CONTRACT.md. The -23 twist premise is retained, the A1-to-A2 identification is withdrawn, and a separate regulator unit is not logically mandatory for a correlated valuation bound. B still needs an actual construction and proved integral realization, not another equivalence. Historical launch instructions and scripts are reference material. Do not start remote follow-up jobs or publish. Record actual reading separately from extraction; preserve FIN, ORDER9 and Q36 unless a proved arithmetic result changes them.
''')
coverage={**bindings,
    'revision_scope':'Only the two reviewed October 7 A returns and the governing B instructions; no new whole-disk or Downloads scan.',
    'old_project_manifest_entries':oldcount,
    'original_reference_archives_unchanged':all(sha((PROJECT/r['path']).read_bytes())==r['sha256'] for r in refs[:2]),
    'original_coverage_json_unchanged':sha((OLD/'COVERAGE.json').read_bytes())==sha((PROJECT/'COVERAGE.json').read_bytes()),
    'added_reference_binding':refs[-1],
    'original_B_zip_sha256':sha((OLD.parent.with_suffix('.zip')).read_bytes()),
    'all_computer_files_included':False,
    'latest_remote_B_job_status_inspected':False,
    'new_job_submitted':False,
}
js(PROJECT/'COVERAGE_ADDENDUM.json',coverage)
changed=[]
diffs=[]
for old in sorted(OLD.rglob('*')):
    if not old.is_file(): continue
    rel=old.relative_to(OLD)
    now=PROJECT/rel
    if old.read_bytes()!=now.read_bytes() and rel.as_posix()!='MANIFEST.sha256':
        changed.append(rel.as_posix())
        diffs.extend(difflib.unified_diff(old.read_text().splitlines(True),now.read_text().splitlines(True),fromfile='2026-10-06/'+str(rel),tofile='2026-10-07/'+str(rel)))
js(ROOT/'PROJECT_CHANGES.json',{'format':'unified diff','diff':''.join(diffs)})
project_count=manifest(PROJECT)
js(ROOT/'checks/BUILD_RECEIPT.json', {**coverage,'review_manifest_counts':review_counts,
    'correction_overlay_manifest_entries':count,'project_manifest_entries':project_count,
    'project_files':project_count+1,'modified_old_project_files':changed,
    'reference_entries_declared_for_extractor':sum(r['manifest_entries'] for r in refs),
    'note':'Builder verifies original project, review manifests, all new bound files and archive containers. Offline extractor checks all nested reference entries separately.'})
shutil.copytree(PROJECT,ROOT/'project_text',ignore=shutil.ignore_patterns('payload','full_record_index','historical_submission','FULL_COMPENDIUM.md','HISTORICAL_STOPS_AND_CORRECTIONS.md','BSD_SEED_RESEARCH_MAP.md','COVERAGE.json','MANIFEST.sha256'))
js(ROOT/'checks/REFERENCE_BINDINGS.json',refs)
print(json.dumps({'project':str(PROJECT),'project_files':project_count+1,'new_overlay_entries':count,'review_entries':review_counts,'original_archives_unchanged':coverage['original_reference_archives_unchanged']}))
