"""Check a downloaded probe result. No submission, networking or remote attestation."""
from pathlib import Path
import argparse
import hashlib
import hmac
import json

ROOT = Path(__file__).resolve().parent


def verify(result_dir, oracle):
    result_dir = Path(result_dir)
    report = {
        "status": "NO_RETURN_TO_CHECK",
        "content_match": False,
        "execution_evidence": "NOT_PROVIDED",
        "remote_run_identity_verified": False,
        "python_execution_independently_verified": False,
        "full_corpus_capacity": "UNTESTED",
        "large_research_job_authorized": False,
        "mathematical_result": False,
    }
    path = result_dir / "RUNTIME_RESULT.json"
    if not path.is_file():
        return report
    try:
        result = json.loads(path.read_text())
        if not isinstance(result, dict):
            raise ValueError("Result must be a JSON object")
    except (ValueError, OSError) as exc:
        report.update(status="INVALID_RESULT_FORMAT", error=str(exc))
        return report
    if result.get("status") != "completed":
        report.update(status="RUNTIME_REPORTED_ERROR_OR_UNSUPPORTED",
                      reported_status=result.get("status"), error=result.get("error"))
        return report
    token = result.get("token")
    digest = hashlib.sha256(token.encode()).hexdigest() if isinstance(token, str) else ""
    checks = {
        "token": hmac.compare_digest(digest, oracle["token_sha256"]),
        "file": result.get("file") == oracle["file"],
        "file_sha256": result.get("file_sha256") == oracle["file_sha256"],
    }
    report["content_checks"] = checks
    if not all(checks.values()):
        report["status"] = "REJECTED_CONTENT_MISMATCH"
        return report
    report.update(content_match=True, status="CONTENT_RECOVERED_EXECUTION_UNCONFIRMED")
    if result.get("execution_method") == "direct_archive_access":
        report["execution_evidence"] = "DIRECT_ARCHIVE_ACCESS_REPORTED"
        return report
    stdout_path = result_dir / "EXTRACTOR_STDOUT.json"
    transcript_path = result_dir / "RUNTIME_TRANSCRIPT.txt"
    stdout = {}
    if stdout_path.is_file():
        try:
            stdout = json.loads(stdout_path.read_text())
            if not isinstance(stdout, dict):
                stdout = {}
        except (ValueError, OSError):
            pass
    reported = (
        result.get("execution_method") == "python3 prepare_reference.py"
        and type(result.get("extractor_exit_code")) is int
        and result["extractor_exit_code"] == 0
        and type(result.get("members_checked")) is int
        and result["members_checked"] == oracle["manifest_entries"]
        and result.get("read_after_extraction") is True
        and stdout.get("status") == "READING_SET_VERIFIED"
        and type(stdout.get("members_checked")) is int
        and stdout["members_checked"] == oracle["manifest_entries"]
        and isinstance(stdout.get("path"), str) and bool(stdout["path"])
        and transcript_path.is_file() and bool(transcript_path.read_text().strip())
    )
    if reported:
        report.update(status="CONTENT_RECOVERED_EXECUTION_REPORTED",
                      execution_evidence="SELF_REPORTED_TRANSCRIPT_AND_STDOUT; INSPECT_NATIVE_PLATFORM_LOGS")
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("result_dir", type=Path,
                        help="Directory containing RUNTIME_RESULT.json from a downloaded return")
    parser.add_argument("--oracle", type=Path, default=ROOT / "ORACLE.json")
    args = parser.parse_args()
    report = verify(args.result_dir, json.loads(args.oracle.read_text()))
    print(json.dumps(report, indent=2))
    raise SystemExit(0 if report["content_match"] else 1)


if __name__ == "__main__":
    main()
