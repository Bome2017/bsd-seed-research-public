# Aristotle/Harmonic BSD research submission

This is the SDK-compatible research input. The larger FULL ZIP is the
preservation archive and exceeds the SDK's single-input limit.

1. Extract this ZIP.
2. The directory to supply to Aristotle is **project/**, not this outer folder.
3. Use the prompt and command in `project/SUBMIT_COMMAND.txt`. It selects
   `aristotle submit ... --project-dir . --wait`, the prompt/project mode for
   attempting new mathematics. It does not merely formalize an old paper.
4. `project/TASK.md` directs Aristotle to unpack the verified reading set and
   continue toward FIN, ORDER9 or Q36 for the exact supplied curve.

The tested SDK is Harmonic's **aristotlelib 2.1.0**. Its actual directory
packager produced a 66,066,505-byte tar.gz, below its 104,857,600-byte limit.
All 16 project files were verified in that payload. The reading-set extractor
independently restored and verified all 5,180 included manifest entries.
The original SDK's size guard also rejected the larger FULL archive, as
expected. `checks/OFFLINE_SDK_PREFLIGHT.json` contains the exact receipts.

Transport was replaced with a local capture in the preflight. **No remote
project was created, no API key was read, and no server acceptance or model
result is claimed.** Account access and current service limits still apply.
The SDK source and official release digest were checked rather than assumed.

Included: the entire 7,042-unit compendium; 3,353 stop/correction entries;
44 detailed wall cards; the current governing record; 5,043 current dossier
files; prior Lean sources and version records; the complete original-path
and capture indexes. The detailed TASK permits a different mathematical
mechanism and demands a new result with an actual seed implication.

The 283,307-object full evidence archive, Git histories, and raw corpus are
not all inside this single SDK input. The complete archive and its coverage
document are delivered separately. The path/capture indexes identify each
original object and its disposition; they do not pretend its bytes have
been supplied. Private lab links require access. This division is imposed
by the measured SDK limit, not presented as a complete single-upload proof
corpus. The current mathematical dossiers themselves are included in full.

Official documentation: https://pypi.org/project/aristotlelib/2.1.0/
Product: https://aristotle.harmonic.fun/

To repeat the offline check in an environment with `aristotlelib==2.1.0`:

    python3 checks/offline_check.py --project-dir project --output-dir /tmp/aristotle-offline-check

Or use an isolated environment:

    uv run --with aristotlelib==2.1.0 python checks/offline_check.py --project-dir project --output-dir /tmp/aristotle-offline-check

The checker compares the imported SDK source hashes with the reviewed
release before exercising it. It mocks transport, does not read an API key,
and creates no remote project. The native submission itself has no dependency
on the checker. Do not confuse this local test with server acceptance.
