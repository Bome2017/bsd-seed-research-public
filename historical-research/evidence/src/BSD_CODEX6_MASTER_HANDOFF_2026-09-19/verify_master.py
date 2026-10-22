#!/usr/bin/env python3
"""Read-only freshness/integrity check. This does not verify mathematics."""
from pathlib import Path
import hashlib
import json
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parent
PREFIXES = (
    'BSD_', 'H41_', 'H9', 'FABLE_FIXED_E5', 'FABLE_TZ', 'FIXED_E5_',
    'SEED_2243', 'C1_', 'GATE_R_', 'ULTRA_GATE_R_', 'run013-', 'run014-',
)
# These locations contain older proofs and supersession records missed by the
# original top-level prefix search. Discovery includes historical controls and
# unrelated records in mixed archives; it is not mathematical admission.
ADDITIONAL_ROOTS = (
    'Desktop/INTELLECTUAL_OUTREACH/04_RESEARCH_OBJECTS',
    'clay-work-chat-audit-2026-09-09',
)
EXCLUSIONS = ('sources', 'evidence', 'provenance', '_work', 'history', 'run', 'logs', '.lake', 'src')


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def discover(home):
    roots = {p for p in home.iterdir() if p.is_dir() and p.name.startswith(PREFIXES)}
    roots.update(home / name for name in ADDITIONAL_ROOTS if (home / name).is_dir())
    roots = sorted(roots)
    if not roots:
        return [], []
    args = ['rg', '--files', '-g', '*.md', '-g', '*.json', '-g', '*.txt']
    for directory in EXCLUSIONS:
        args += ['-g', '!**/' + directory + '/**']
    proc = subprocess.run(args + [str(p) for p in roots], text=True, capture_output=True)
    if proc.returncode not in (0, 1):
        raise RuntimeError(proc.stderr.strip())
    return [str(p) for p in roots], sorted(set(proc.stdout.splitlines()))


def changed_sources(entries):
    issues = []
    for entry in entries:
        path = Path(entry['path'])
        if not path.is_file():
            issues.append({'kind': 'missing_bound_source', 'path': str(path)})
        elif digest(path) != entry['sha256']:
            issues.append({'kind': 'changed_bound_source', 'path': str(path)})
    return issues


def discovery_changes(previous, current):
    return {
        'new_records': sorted(set(current) - set(previous)),
        'missing_records': sorted(set(previous) - set(current)),
    }


def local_targets(path):
    content = path.read_text()
    content = re.sub(r'\\\[.*?\\\]|\\\(.*?\\\)', '', content, flags=re.S)
    for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)', content):
        if target.startswith(('https://', 'http://', '#')):
            continue
        target = re.sub(r':\d+$', '', target.strip('<>').split('#', 1)[0])
        resolved = Path(target)
        yield resolved if resolved.is_absolute() else path.parent / resolved


def check(root=ROOT):
    bindings = json.loads((root / 'SOURCE_BINDINGS.json').read_text())
    inventory = json.loads((root / 'RECONCILIATION_INVENTORY.json').read_text())
    issues = changed_sources(bindings['sources'])
    document = root / 'MASTER_BSD_DAG.md'
    if digest(document) != bindings['canonical_document_sha256']:
        issues.append({'kind': 'canonical_document_changed_without_reconciliation'})
    for path in local_targets(document):
        if not path.exists():
            issues.append({'kind': 'broken_canonical_link', 'path': str(path)})
    roots, paths = discover(root.parent)
    changes = discovery_changes(inventory['discovered_paths'], paths)
    if changes['new_records'] or changes['missing_records']:
        issues.append({'kind': 'discovery_scope_changed', **changes})
    if set(roots) != set(inventory['roots']):
        issues.append({'kind': 'research_root_set_changed'})
    return {
        'result': 'RECONCILIATION_REQUIRED' if issues else 'PASS_WITH_STATED_COVERAGE_LIMITS',
        'canonical_document': str(document),
        'bound_sources_checked': len(bindings['sources']),
        'discovered_records': len(paths),
        'issues': issues,
        'scope': 'Freshness and local integrity only. No proof validation, exhaustive history recovery, or automatic maintenance.',
    }


if __name__ == '__main__':
    try:
        result = check()
    except (OSError, ValueError, KeyError, RuntimeError) as exc:
        result = {'result': 'RECONCILIATION_REQUIRED', 'issues': [{'kind': 'checker_error', 'message': str(exc)}]}
    print(json.dumps(result, indent=2))
    sys.exit(0 if result['result'] == 'PASS_WITH_STATED_COVERAGE_LIMITS' else 1)
