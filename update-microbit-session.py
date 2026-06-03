#!/usr/bin/env python3
import argparse
import datetime
import hashlib
import json
import os
import re
import shutil
from pathlib import Path

SCRIPT = Path(__file__).name
DEFAULT_DEST = Path("coin-collector") / "microbit classroom session.html"
RESUME_DATA_RE = re.compile(
    r"<script[^>]*id=[\"']resumeData[\"'][^>]*>(.*?)</script>",
    re.DOTALL | re.IGNORECASE,
)


def load_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def validate_resume_data(html: str) -> dict:
    match = RESUME_DATA_RE.search(html)
    if not match:
        raise ValueError(
            "The file does not appear to contain a micro:bit Classroom resumeData script."
        )
    payload = match.group(1).strip()
    if not payload:
        raise ValueError("resumeData script was found but contains no JSON payload.")
    try:
        return json.loads(payload)
    except json.JSONDecodeError as exc:
        raise ValueError(f"resumeData JSON could not be parsed: {exc}") from exc


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(8192), b""):
            digest.update(chunk)
    return digest.hexdigest()


def create_backup(dest: Path) -> Path:
    timestamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    backup_path = dest.with_name(dest.name + f".backup-{timestamp}")
    shutil.copy2(dest, backup_path)
    return backup_path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Update the repo's micro:bit classroom session HTML file from a downloaded session file."
        )
    )
    parser.add_argument(
        "source",
        type=Path,
        help="Path to the downloaded micro:bit classroom session HTML file.",
    )
    parser.add_argument(
        "--dest",
        type=Path,
        default=DEFAULT_DEST,
        help=(
            "Repository destination file to update. Defaults to 'coin-collector/microbit classroom session.html'."
        ),
    )
    parser.add_argument(
        "--no-backup",
        action="store_true",
        help="Do not keep a backup copy of the current destination file.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    source = args.source.resolve()
    dest = args.dest.resolve()

    if not source.exists():
        print(f"Error: source file not found: {source}")
        return 1
    if not source.is_file():
        print(f"Error: source path is not a file: {source}")
        return 1

    print(f"Loading source file: {source}")
    source_html = load_text(source)

    try:
        resume_data = validate_resume_data(source_html)
    except ValueError as exc:
        print(f"Validation failed: {exc}")
        return 1

    print("Validated micro:bit Classroom saved session payload.")
    print(f"Activity: {resume_data.get('activity', {}).get('name', '<unknown>')}")

    if dest.exists():
        source_hash = hashlib.sha256(source_html.encode("utf-8")).hexdigest()
        dest_hash = file_sha256(dest)
        if source_hash == dest_hash:
            print("Destination file is already up to date. No changes made.")
            return 0
        if not args.no_backup:
            backup_path = create_backup(dest)
            print(f"Created backup: {backup_path}")

    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, dest)
    print(f"Updated destination file: {dest}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
