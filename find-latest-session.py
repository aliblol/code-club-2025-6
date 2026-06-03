#!/usr/bin/env python3
"""
Find and activate the latest micro:bit classroom session file by date.

This script scans the 'microbit classrom files' folder, finds the file with
the latest date in its name, and copies it to the root level for easy access.
"""

import re
from datetime import datetime
from pathlib import Path


def extract_date_from_filename(filename: str) -> datetime | None:
    """Extract date from filename like 'arcade - microbit classroom session - 2026-06-03-2.html'"""
    match = re.search(r'(\d{4})-(\d{2})-(\d{2})', filename)
    if match:
        try:
            return datetime(int(match.group(1)), int(match.group(2)), int(match.group(3)))
        except ValueError:
            return None
    return None


def find_latest_session() -> Path | None:
    """Find the latest session file by date in the microbit classrom files folder."""
    session_folder = Path(__file__).parent / 'coin-collector' / 'microbit classrom files'
    
    if not session_folder.exists():
        print(f"Error: Session folder not found: {session_folder}")
        return None
    
    html_files = list(session_folder.glob('*.html'))
    if not html_files:
        print(f"Error: No HTML files found in {session_folder}")
        return None
    
    # Sort files by extracted date (newest first)
    files_with_dates = []
    for file in html_files:
        date = extract_date_from_filename(file.name)
        if date:
            files_with_dates.append((file, date))
    
    if not files_with_dates:
        print("Error: No files with dates found")
        return None
    
    files_with_dates.sort(key=lambda x: x[1], reverse=True)
    latest_file, latest_date = files_with_dates[0]
    
    return latest_file


def main() -> int:
    latest = find_latest_session()
    if not latest:
        return 1
    
    print(f"Latest session: {latest.name}")
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
