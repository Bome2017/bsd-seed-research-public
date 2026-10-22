# Aristotle nested-reading test — prepared, not submitted

The tiny test is ready. **No Aristotle job has been created.** The user's
instruction is: "Prepare the test without submitting."

If you later choose to run it, submit only **project/**. It contains four
files: the task, the exact extractor from the large package, its archive
binding, and a ZIP containing three small text files plus their manifest.
The fresh challenge value appears only inside the nested ZIP. The external
oracle stores its hash, not the answer. No BSD record is needed for this probe.

[SUBMIT_LATER.txt](SUBMIT_LATER.txt) contains the prepared command. It is an
inert text file, not an automatic launcher. The interface is the one documented
by [Harmonic's SDK 2.1.0](https://pypi.org/project/aristotlelib/2.1.0/).
Authentication and an installed CLI are needed only if you later submit.

The real SDK directory packager was exercised **with transport mocked**:
four files, 3,739 upload bytes. Local extraction verified all three reading
files. Twenty-three local controls passed, including rejection of wrong
tokens, paths and hashes. These are local results, not remote-runtime results.

After a later run, locate `RUNTIME_RESULT.json` in the downloaded return and
give its containing directory to the checker:

```text
python3 verify_return.py /absolute/path/to/downloaded/result_directory
```

The checker reports content recovery separately from execution evidence.
Its exit code zero means the token, path and hash match; **read its status**
before interpreting that as anything more. A model-written transcript cannot
independently attest Python execution; inspect the native service tool log
when available. A refusal, extraction error, missing return, and wrong answer
have different statuses.

Even a successful remote tiny test would establish only small-scale nested
access. It would not establish 5,180-file extraction/indexing capacity,
full-corpus disk or context capacity, a usable BSD proof, or permission to
launch the larger research job. The full-scale runtime question remains open.

For the later full research task, use
[TASK_PRIORITY_ADDENDUM.md](TASK_PRIORITY_ADDENDUM.md) and the ready-to-copy
[revised prompt](REVISED_RESEARCH_PROMPT.txt). They require checking historical
failures and identifying the changed arithmetic step before developing a
mechanism. They are outside this tiny test's upload.

The earlier large submission, full preservation ZIP, and starter ZIP retain
their original SHA-256 hashes. [Report](REPORT.md) ·
[Local checks](checks/LOCAL_RESULTS.json) ·
[SDK receipt](checks/sdk/OFFLINE_SDK_PREFLIGHT.json) ·
[Archive-preservation check](checks/LARGE_ARCHIVES_UNCHANGED.json).
