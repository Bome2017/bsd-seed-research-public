"""Create a fresh nested-read probe once; does not submit or access the network."""
from pathlib import Path
import hashlib
import json
import secrets
import shutil
import zipfile

ROOT = Path(__file__).resolve().parents[1]
PROJECT = ROOT / "project"
SOURCE = Path("/Users/bsm/BSD_ARISTOTLE_FULL_RECORD_2026-10-05/aristotle_submission/BSD_SEED_ARISTOTLE_NATIVE_2026-10-05/prepare_reference.py")


def sha(data):
    return hashlib.sha256(data).hexdigest()


def write_json(path, value):
    path.write_text(json.dumps(value, indent=2) + "\n")


def main():
    if any(PROJECT.iterdir()) or (ROOT / "ORACLE.json").exists():
        raise SystemExit("Refusing to replace an existing test or its challenge.")
    token = secrets.token_hex(24)
    archive_root = "BSD_NESTED_RUNTIME_SMOKE"
    needle = "dossiers/deep/runtime_probe.txt"
    entries = {
        "START_HERE.md": b"# Tiny nested reading set\n\nThis is a runtime access probe, not a mathematical research task. Read the three text files after extraction.\n",
        "controls/three_lines.txt": b"alpha\nbeta\ngamma\n",
        needle: ("# Buried runtime probe\n\nARISTOTLE_NESTED_READ_TEST = " + token + "\n\nReturn this exact value and this file's path only after reading the extracted file.\n").encode(),
    }
    manifest = "".join(f"{sha(data)}  {name}\n" for name, data in sorted(entries.items()))
    (PROJECT / "payload").mkdir()
    archive = PROJECT / "payload/COMPLETE_READING_SET.zip"
    with zipfile.ZipFile(archive, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as z:
        for name, data in sorted({**entries, "STARTER_MANIFEST.sha256": manifest.encode()}.items()):
            info = zipfile.ZipInfo(f"{archive_root}/{name}", date_time=(2026, 10, 5, 0, 0, 0))
            info.external_attr = 0o100644 << 16
            info.compress_type = zipfile.ZIP_DEFLATED
            z.writestr(info, data)
    shutil.copyfile(SOURCE, PROJECT / "prepare_reference.py")
    write_json(PROJECT / "READING_SET_BINDING.json", {
        "root": archive_root,
        "sha256": sha(archive.read_bytes()),
        "bytes": archive.stat().st_size,
        "manifest_entries": 3,
        "zip_file_entries_including_manifest": 4,
        "expanded_bytes_including_manifest": sum(map(len, entries.values())) + len(manifest.encode()),
        "purpose": "Tiny nested extraction/read probe only; no BSD computation"
    })
    write_json(ROOT / "ORACLE.json", {
        "schema_version": 1,
        "token_key": "ARISTOTLE_NESTED_READ_TEST",
        "token_sha256": sha(token.encode()),
        "token_encoding": "UTF-8; exact value, without newline or surrounding spaces",
        "file": f"reading_set/{archive_root}/{needle}",
        "file_sha256": sha(entries[needle]),
        "archive_sha256": sha(archive.read_bytes()),
        "manifest_entries": 3,
        "project_upload_only": True,
        "execution_attestation": "None. Returned files and self-reported transcripts cannot independently attest a remote process."
    })
    write_json(ROOT / "checks/EXTRACTOR_BINDING.json", {
        "source": str(SOURCE),
        "source_lab_commit": "99dac1e217fbd67e4c747406f5d22e0a95a71e7c",
        "source_sha256": sha(SOURCE.read_bytes()),
        "copy_sha256": sha((PROJECT / "prepare_reference.py").read_bytes()),
        "byte_for_byte_identical": True
    })
    print(json.dumps({"status": "TINY_PROBE_CREATED_NOT_SUBMITTED", "nested_files": 3,
                      "zip_bytes": archive.stat().st_size, "plaintext_token_printed": False}))


if __name__ == "__main__":
    main()
