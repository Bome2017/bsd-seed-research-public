# Tiny nested-reading runtime test — stop after this test

This project tests whether your actual Aristotle runtime can execute the same
extractor used by a larger research project and read files created by it. It is
not a BSD research task, theorem proof, or Lean formalization. Do not start any
other job, fetch remote sources, or install dependencies.

1. From this project's root, execute `python3 prepare_reference.py`. Capture
   its actual exit code and stdout. The script uses only Python's standard
   library, verifies the supplied archive digest, extracts it, then verifies
   its three text-file hashes. Do not change the script or binding.
2. After successful execution, read the three text files inside the newly
   created `reading_set/` tree. Locate the line whose key is
   `ARISTOTLE_NESTED_READ_TEST`. Its value is deliberately absent from this
   task, the submission prompt, and the top-level files. Return the exact
   value, the file's project-relative path, and the SHA-256 of that file's
   bytes. Do not guess a token from prior conversations.
3. Create the three return files described below in the project root. Preserve
   the extracted tree in the returned project when your platform permits it.
4. Stop. Do not interpret this test as authorization to launch the larger BSD
   project or continue mathematical work.

If command execution is unavailable, say so. If extraction fails, preserve the
actual error. Do not claim that reading directly from an archive demonstrates
that Python ran or that files were created and subsequently read. If the
platform nevertheless exposes the nested content, you may report the token
with `execution_method` set to `direct_archive_access`; distinguish that from
successful extractor execution.

## Return files

`RUNTIME_RESULT.json` must use this schema, replacing placeholders with actual
observations (null is appropriate for unavailable fields):

```json
{
  "status": "completed",
  "token": "<exact discovered value>",
  "file": "<project-relative extracted filename>",
  "file_sha256": "<SHA-256 of that file>",
  "execution_method": "python3 prepare_reference.py",
  "extractor_exit_code": 0,
  "members_checked": 3,
  "read_after_extraction": true,
  "error": null
}
```

Use `unsupported` or `error` instead of `completed` when appropriate. Use
`direct_archive_access` for content read without running the extractor.

`EXTRACTOR_STDOUT.json`: save the exact successful extractor stdout, without
rewriting its absolute runtime path. On failure, omit this file and preserve
stdout/stderr in the transcript instead.

`RUNTIME_TRANSCRIPT.txt`: record the commands actually executed, Python
version, working directory, exit codes, and output. Include the command used
to read/hash the extracted file. If execution was unavailable, state that;
do not fabricate a transcript. If the service provides a native tool log,
retain it as well. A self-written transcript is evidence to inspect, not an
independent execution attestation.

In your final response state only the outcome and which return files exist.
A successful test establishes small-scale access; it does not establish
capacity to extract/index thousands of files or complete a research proof.
