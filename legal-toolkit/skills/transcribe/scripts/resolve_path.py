#!/usr/bin/env python3
"""
Resolve a user-provided file path to an actual file on the host machine.

Handles ~ expansion, VM-to-macOS path mapping, and common folder searches.
Standalone CLI tool for resolving file paths.

Usage:
    python3 resolve_path.py <file_path>

Output (JSON to stdout):
    {"status": "found", "resolved_path": "/abs/path/to/file"}
    {"status": "not_found", "tried": [...], "message": "..."}
"""
import argparse
import getpass
import json
import os
import sys


def resolve_file_path(file_path: str) -> dict:
    """Try to resolve *file_path* to an existing file on disk.

    Resolution strategy:
      1. Try the path as-is (with ~ expansion).
      2. Map VM-style prefixes (/user/, /home/, /home/<user>/) to the
         real macOS home directory, including common sub-folders.
      3. If the path looks like a bare filename or relative path, search
         ~/Downloads, ~/Desktop, ~/Documents.
      4. Strip the first path component and search common directories
         (handles paths like /user/subfolder/file.mp4).
    """
    candidates: list[str] = []

    username = getpass.getuser()
    home = os.path.expanduser("~")

    # 1. As-is with ~ expansion
    expanded = os.path.expanduser(file_path)
    candidates.append(expanded)

    # 2. VM-style prefix mapping
    for prefix in ["/user/", "/home/", f"/home/{username}/"]:
        if file_path.startswith(prefix):
            relative = file_path[len(prefix):]
            candidates.append(os.path.join(home, relative))
            for folder in ["Downloads", "Desktop", "Documents"]:
                candidates.append(os.path.join(home, folder, relative))

    # 3. Bare filename / relative path
    basename = os.path.basename(file_path)
    if basename == file_path or not file_path.startswith("/"):
        for folder in ["Downloads", "Desktop", "Documents"]:
            candidates.append(os.path.join(home, folder, basename))

    # 4. Strip first component and retry common dirs
    parts = file_path.strip("/").split("/")
    if len(parts) >= 2:
        sub_path = "/".join(parts[1:])
        candidates.append(os.path.join(home, sub_path))
        for folder in ["Downloads", "Desktop", "Documents"]:
            candidates.append(os.path.join(home, folder, sub_path))

    # Deduplicate while preserving order
    seen: set[str] = set()
    unique: list[str] = []
    for c in candidates:
        c = os.path.abspath(c)
        if c not in seen:
            seen.add(c)
            unique.append(c)

    # Return the first match
    for candidate in unique:
        if os.path.isfile(candidate):
            return {"status": "found", "resolved_path": candidate}

    return {
        "status": "not_found",
        "original_path": file_path,
        "tried": unique[:10],
        "message": (
            f"Could not find '{file_path}' on the host machine. "
            f"Tried {len(unique)} locations. "
            f"Please provide the full path "
            f"(e.g. /Users/{username}/Downloads/file.mp4)."
        ),
    }


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Resolve a file path to an absolute path on this machine."
    )
    parser.add_argument("file_path", help="The file path to resolve")
    args = parser.parse_args()

    print(f"Resolving: {args.file_path}", file=sys.stderr)

    result = resolve_file_path(args.file_path)

    if result["status"] == "found":
        print(f"Found: {result['resolved_path']}", file=sys.stderr)
    else:
        print(f"Not found. Tried {len(result['tried'])} locations.", file=sys.stderr)

    json.dump(result, sys.stdout, indent=2)
    print()  # trailing newline


if __name__ == "__main__":
    main()
