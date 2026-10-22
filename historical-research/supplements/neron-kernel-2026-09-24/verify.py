#!/usr/bin/env python3
"""Portable integrity and finite-algebra replay for the dated supplement.

No network, seed evaluation, large corpus, Lean build or repository mutation.
The published theorems and the actual enclosure remain mathematical inputs.
"""
from fractions import Fraction
from pathlib import Path
import hashlib
import importlib.util
import json
import re
import sys

S = Path(__file__).resolve().parent
R = S.parent.parent
BASE = '2a726213a27a12f10fece5bc70137e65e30911ba'
LAB = 'b358f7507759dad4a1e016c519d6f486ffca37e1'
OLD_MANIFEST_HASH = '8d33aa9187c5ca96af4df8d932ce186a79b61b0284e56dd36bccab6e2a0c8489'


def need(ok, message):
    if not ok:
        raise ValueError(message)


def safe(root, relative):
    rel = Path(relative)
    need(not rel.is_absolute() and '..' not in rel.parts, 'unsafe path: ' + relative)
    result = root / rel
    need(not result.is_symlink() and result.is_file(), 'missing/nonregular file: ' + relative)
    need(result.resolve().is_relative_to(root.resolve()), 'path escaped root: ' + relative)
    return result


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def entries(root, name):
    found = {}
    for line in safe(root, name).read_text().splitlines():
        h, relative = line.split('  ', 1)
        need(re.fullmatch('[0-9a-f]{64}', h) is not None, 'invalid hash')
        need(relative not in found, 'duplicate manifest path: ' + relative)
        safe(root, relative)
        found[relative] = h
    return found


def manifest(root, name):
    rows = entries(root, name)
    for relative, h in rows.items():
        need(sha(safe(root, relative)) == h, 'hash mismatch: ' + relative)
    return rows


def main():
    need(not sys.flags.optimize, 'run without -O: retained finite tests use assertions')
    sys.dont_write_bytecode = True
    whole = manifest(R, 'MANIFEST.sha256')
    local = manifest(S, 'SHA256SUMS')
    prefix = S.relative_to(R).as_posix() + '/'
    for p, h in local.items():
        need(whole.get(prefix+p) == h, 'root/supplement manifest disagreement: ' + p)
    actual = {p.relative_to(S).as_posix() for p in S.rglob('*')
              if p.is_file() and '__pycache__' not in p.parts and p.name != '.DS_Store'}
    need(set(local) == actual - {'SHA256SUMS'}, 'supplement manifest omits or adds a file')

    transition = json.loads(safe(R, 'review/NERON_SUPPLEMENT_APPLIED.json').read_text())
    need(transition['research_base'] == BASE and transition['lab_source_commit'] == LAB,
         'transition identity mismatch')
    historical = safe(R, 'review/history/v0.2.2/MANIFEST.sha256')
    need(sha(historical) == OLD_MANIFEST_HASH, 'original root manifest changed')
    old = {}
    # Its paths refer to the original root, not to the history directory.
    for line in historical.read_text().splitlines():
        h, p = line.split('  ', 1)
        need(p not in old and re.fullmatch('[0-9a-f]{64}', h), 'invalid historical entry')
        old[p] = h
    redirects = transition['historical_v022_bindings']
    need(set(redirects) == {'README.md', 'tools/verify_patch_release.py'}, 'unexpected history redirect')
    for p, h in old.items():
        target = 'review/history/v0.2.2/'+p if p in redirects else p
        need(sha(safe(R, target)) == h, 'v0.2.2 bytes changed: ' + p)
    for p, data in redirects.items():
        need(data == {'path': 'review/history/v0.2.2/'+p, 'sha256': old[p]}, 'redirect did not preserve binding')
    nav = transition['current_navigation_bindings']
    need(set(nav) == set(redirects), 'unexpected current-navigation binding')
    need(all(sha(safe(R,p)) == h for p,h in nav.items()), 'current-navigation hash mismatch')
    need(len(old) == 4226, 'historical manifest count mismatch')

    provenance = json.loads(safe(S, 'PROVENANCE.json').read_text())
    need(provenance['research_base'] == BASE and provenance['lab_source_commit'] == LAB,
         'provenance identity mismatch')
    imported = provenance['imported_files']
    need(len(imported) == 31 and len({x['path'] for x in imported}) == 31,
         'unexpected/duplicate imported evidence entries')
    for row in imported:
        data = safe(S,row['path']).read_bytes()
        need(hashlib.sha256(data).hexdigest() == row['sha256'], 'imported bytes changed')
        origin = row['origin']
        if 'git_blob' in origin:
            blob = hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
            need(blob == origin['git_blob'] and origin['commit'] == LAB, 'Git blob mismatch')
    pro_entries = manifest(S/'reviews/pro6', 'SHA256SUMS')
    need(len(pro_entries) == 10, 'original review manifest count mismatch')

    baseline = json.loads(safe(R, 'claims/claims.json').read_text())['claims']
    need(len(baseline) == 76, 'frozen manuscript claim count changed')
    new = json.loads(safe(S, 'CLAIMS.json').read_text())['claims']
    need([c['id'] for c in new] == ['NK.1','NK.2','NK.3'], 'unexpected new claim IDs')
    known = {c['id'] for c in baseline}
    graph = {}
    for c in new:
        need(c['kind'] == ('CONDITIONAL' if c['id'] == 'NK.3' else 'THEOREM'), 'wrong claim kind')
        need('LEAN_CHECKED' not in c['grades'] and not c['verification']['human_review']
             and not c['verification']['new_lean_replay'], 'review grade was promoted')
        need(set(c['depends_on']) <= known, 'unknown or forward/cyclic claim dependency')
        for e in c['evidence']:
            need(sha(safe(S,e['path'])) == e['sha256'], 'claim evidence mismatch')
        graph[c['id']] = c['depends_on']
        known.add(c['id'])

    # Reuse the review's unmodified exact polynomial checker. These are finite
    # regression checks, not a second proof of the imported source theorems.
    spec = importlib.util.spec_from_file_location('neron_exact', S/'reviews/pro6/independent_checks.py')
    checks = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(checks)
    gauss = checks.gauss_test()
    thresholds = checks.thresholds()
    arithmetic = checks.arithmetic_checks()
    expected = json.loads(safe(S,'reviews/pro6/CHECKS.json').read_text())
    need(gauss == expected['gauss_sums'] and thresholds == expected['cusp_inequalities']
         and arithmetic == expected['arithmetic'], 'exact replay differs from supplied review')

    # Separate oracle: enumerate the integers directly, rather than duplicate
    # the floor/ceiling decision formula of the acceptance implementation.
    cases = 0
    F = Fraction
    for p in [5,11,13,17,23]:
        for x in range(-64,65):
            for y in range(x,65):
                lo,hi = F(x,4),F(y,4)
                possible = [k for k in range(-17,18) if lo <= k <= hi]
                if not possible:
                    status = 'EMPTY_LATTICE_INCONSISTENCY'
                elif all(k % p for k in possible):
                    status = 'UNIT_WITNESS_IF_MEMBERSHIP'
                elif len(possible) == 1:
                    status = 'DIVISIBLE_WITNESS_INCONCLUSIVE_FOR_SHA'
                else:
                    status = 'INCONCLUSIVE'
                got = checks.interval_decision(lo/checks.B_THETA,hi/checks.B_THETA,p)
                need(got['status'] == status, 'integer-oracle disagreement')
                cases += 1
    rejected = 0
    for p in [2,3,7,9,15,2243,4547,5843]:
        try:
            checks.interval_decision(F(0),F(1),p)
        except ValueError:
            rejected += 1
        else:
            raise ValueError('inadmissible prime accepted')
    # Also exercise exact fallback scale and endpoints, with no decimal proxy.
    for B in [checks.B_THETA,checks.B_JOIN]:
        need(checks.interval_decision(F(1,B),F(4,B),5,B)['status'].startswith('UNIT'), 'scale error')
        need(checks.interval_decision(F(5,B),F(5,B),5,B)['status'].startswith('DIVISIBLE'), 'endpoint error')
        need(checks.interval_decision(F(1,4*B),F(1,2*B),5,B)['status'].startswith('EMPTY'), 'empty accepted')
    need(cases == 41925 and rejected == 8, 'oracle coverage count mismatch')
    print(json.dumps({'status':'NERON_SUPPLEMENT_PASS','root_manifest_entries':len(whole),
        'supplement_manifest_entries':len(local),'preserved_v022_manifest_entries':len(old),
        'copied_evidence_files':len(imported),'original_review_hashes':len(pro_entries),
        'frozen_claims':76,'new_claims':graph,'exact_Eichler_cases':gauss['exact_cases'],
        'wrong_phase_amplitude_rejected':gauss['negative_controls_rejected'],
        'cusp_inequalities':len(thresholds),'degree_zero_relift_primes':arithmetic['degree_zero_relift_primes'],
        'direct_integer_oracle_cases':cases,'inadmissible_primes_rejected':rejected,
        'actual_seed_witness_evaluated':False,'new_Lean_replay':False,
        'scope':'Integrity and finite exact algebra only; source theorems and enclosure remain inputs.'},indent=2))


if __name__ == '__main__':
    try:
        main()
    except (AssertionError, ValueError, KeyError, FileNotFoundError) as error:
        raise SystemExit('NERON_SUPPLEMENT_FAIL: '+str(error))
