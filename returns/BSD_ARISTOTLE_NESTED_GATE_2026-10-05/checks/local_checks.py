"""Local controls only; synthetic return fixtures are created and deleted in temp dirs."""
from pathlib import Path
import copy
import hashlib
import importlib.util
import json
import shutil
import subprocess
import sys
import tempfile
import zipfile

ROOT = Path(__file__).resolve().parents[1]
PROJECT = ROOT / "project"


def sha(data):
    return hashlib.sha256(data).hexdigest()


def main():
    oracle = json.loads((ROOT / "ORACLE.json").read_text())
    binding = json.loads((PROJECT / "READING_SET_BINDING.json").read_text())
    controls = []

    def record(name, condition):
        assert condition, name
        controls.append(name)

    with zipfile.ZipFile(PROJECT / "payload/COMPLETE_READING_SET.zip") as z:
        record("nested_zip_integrity", z.testzip() is None)
        names = z.namelist()
        record("three_text_files_plus_manifest", len(names) == 4)
        needle = oracle["file"].removeprefix("reading_set/")
        data = z.read(needle)
        token = next(line.split(" = ", 1)[1] for line in data.decode().splitlines()
                     if line.startswith(oracle["token_key"] + " = "))
        record("fresh_token_matches_hash_oracle", sha(token.encode()) == oracle["token_sha256"])
        record("buried_file_matches_oracle", sha(data) == oracle["file_sha256"])
    # Plaintext challenge never appears in any top-level submitted source.
    files = sorted(p for p in PROJECT.rglob("*") if p.is_file())
    record("only_four_submitted_files", len(files) == 4)
    record("no_plaintext_token_in_top_level_project_files", all(
        token.encode() not in p.read_bytes() for p in files if p.suffix != ".zip"))
    record("no_plaintext_token_in_oracle", token.encode() not in (ROOT / "ORACLE.json").read_bytes())
    record("archive_binding_matches", sha((PROJECT / "payload/COMPLETE_READING_SET.zip").read_bytes()) == binding["sha256"] == oracle["archive_sha256"])
    extractor_binding = json.loads((ROOT / "checks/EXTRACTOR_BINDING.json").read_text())
    record("extractor_identical_to_large_project", sha((PROJECT / "prepare_reference.py").read_bytes()) == extractor_binding["source_sha256"])

    spec = importlib.util.spec_from_file_location("return_checker", ROOT / "verify_return.py")
    checker = importlib.util.module_from_spec(spec)
    sys.dont_write_bytecode = True
    spec.loader.exec_module(checker)
    with tempfile.TemporaryDirectory(prefix="aristotle-local-only-") as td:
        temp = Path(td)
        local_project = temp / "project"
        shutil.copytree(PROJECT, local_project)
        run = subprocess.run([sys.executable, "prepare_reference.py"], cwd=local_project,
                             capture_output=True, text=True, timeout=20)
        record("actual_local_extraction_succeeds", run.returncode == 0)
        stdout = json.loads(run.stdout)
        record("extractor_verifies_three_files", stdout["members_checked"] == 3 and stdout["status"] == "READING_SET_VERIFIED")
        record("newly_created_file_read_matches", (local_project / oracle["file"]).read_bytes() == data)
        again = subprocess.run([sys.executable, "prepare_reference.py"], cwd=local_project,
                               capture_output=True, text=True, timeout=20)
        record("refuses_existing_output_instead_of_overwriting", again.returncode != 0 and "already exists" in again.stderr)

        returned = temp / "synthetic-return-NOT-ARISTOTLE"
        returned.mkdir()
        record("absent_return_is_untested", checker.verify(returned, oracle)["status"] == "NO_RETURN_TO_CHECK")
        good = {"status": "completed", "token": token, "file": oracle["file"],
                "file_sha256": oracle["file_sha256"], "execution_method": "python3 prepare_reference.py",
                "extractor_exit_code": 0, "members_checked": 3, "read_after_extraction": True, "error": None}

        def verdict(value):
            (returned / "RUNTIME_RESULT.json").write_text(json.dumps(value))
            return checker.verify(returned, oracle)

        record("content_without_evidence_is_not_execution_pass", verdict(good)["status"] == "CONTENT_RECOVERED_EXECUTION_UNCONFIRMED")
        (returned / "EXTRACTOR_STDOUT.json").write_text(run.stdout)
        (returned / "RUNTIME_TRANSCRIPT.txt").write_text("SYNTHETIC LOCAL CONTROL; not an Aristotle transcript.\n")
        response = verdict(good)
        record("complete_self_report_remains_only_reported", response["status"] == "CONTENT_RECOVERED_EXECUTION_REPORTED"
               and not response["python_execution_independently_verified"] and response["full_corpus_capacity"] == "UNTESTED")
        for field, wrong in [("token", "wrong-token"), ("file", "wrong-file"), ("file_sha256", "0" * 64)]:
            case = copy.deepcopy(good)
            case[field] = wrong
            record("reject_wrong_" + field, verdict(case)["status"] == "REJECTED_CONTENT_MISMATCH")
        case = {**good, "execution_method": "direct_archive_access"}
        record("archive_access_is_not_python_execution", verdict(case)["status"] == "CONTENT_RECOVERED_EXECUTION_UNCONFIRMED")
        case = {**good, "extractor_exit_code": False}
        record("boolean_exit_code_cannot_fake_integer_zero", verdict(case)["status"] == "CONTENT_RECOVERED_EXECUTION_UNCONFIRMED")
        record("explicit_runtime_error_distinguished", verdict({"status": "error", "error": "synthetic"})["status"] == "RUNTIME_REPORTED_ERROR_OR_UNSUPPORTED")
        (returned / "RUNTIME_RESULT.json").write_text("[]")
        record("malformed_result_rejected", checker.verify(returned, oracle)["status"] == "INVALID_RESULT_FORMAT")

    output = {"status": "LOCAL_CONTROLS_PASSED", "controls_passed": len(controls), "controls": controls,
              "fixtures": "Synthetic local controls only; token-bearing fixture files deleted with temporary directory",
              "aristotle_submitted": False, "remote_execution_tested": False, "full_corpus_capacity_tested": False}
    (ROOT / "checks/LOCAL_RESULTS.json").write_text(json.dumps(output, indent=2) + "\n")
    print(json.dumps({k: v for k, v in output.items() if k != "controls"}, indent=2))


if __name__ == "__main__":
    main()
