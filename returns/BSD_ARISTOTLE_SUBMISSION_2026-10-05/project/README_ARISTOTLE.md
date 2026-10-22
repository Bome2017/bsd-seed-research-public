# Actual Aristotle project input

Use this folder with Harmonic's `aristotle submit PROMPT --project-dir DIRECTORY`.
The version inspected and used for the offline preflight is `aristotlelib 2.1.0`
from Harmonic's official PyPI distribution. Its `Project.create_from_directory`
builds a tar.gz and `Project.create` rejects that archive above 104,857,600 bytes.
The larger full-record ZIP is a preservation artifact and cannot be submitted
through that SDK path as one project.

Official documentation: https://pypi.org/project/aristotlelib/2.1.0/
Product: https://aristotle.harmonic.fun/

After extracting the delivery ZIP, submit the directory containing this file.
The exact command is in `SUBMIT_COMMAND.txt`. It uses the SDK's general prompt
and project mode because the request is to discover and prove new mathematics.
`aristotle formalize` is for formalizing an existing document and would not by
itself express the intended research task. Account access and its key are the
user's; no key is stored here and no job was launched during preparation.

The receiver should run `prepare_reference.py` inside its project. That exposes
all current dossier files and prior Lean projects under `reading_set/`, with all
5,180 original starter-manifest entries verified. Do not run that extractor in
the directory BEFORE submitting with this documented command: it would expand
the reference projects into the submitted context again. If already expanded,
use a fresh copy of this input folder; do not delete original research folders.

## What was and was not tested

The accompanying offline preflight uses the actual downloaded SDK's directory
packer, file-size checker, request-body construction, and response parser. Its
HTTP client is replaced by a local capture object, and network connections are
disabled. It verifies every file in the generated tar.gz against this folder.
It does not establish server acceptance, available quota, a supported current
remote Lean version, research success, or a BSD proof. Those require a real run.

## Completeness distinction

The full master record remains separately available on the Desktop and in the
lab repository. This native input contains its full compendium, current readable
dossiers and detailed map, plus complete path/capture indexes. It omits the large
evidence volumes, compressed full-text database, Git bundles and external raw
corpora. Its limits are explicit; the metadata is not a substitute for the bytes.
All original starter bytes are included in `payload/COMPLETE_READING_SET.zip`.
