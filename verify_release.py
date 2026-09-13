#!/usr/bin/env python3
"""Verify release artifacts and key negative/positive model conditions."""

import argparse
import csv
import hashlib
from pathlib import Path


REQUIRED = (
    "results/summary.csv",
    "results/trajectories.csv",
    "results/sensitivity.csv",
    "results/summary.json",
    "results/trajectories.svg",
)


def sha256(path):
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--check",
        action="store_true",
        help="compare generated artifacts with the committed checksum manifest",
    )
    args = parser.parse_args()
    root = Path(__file__).resolve().parent
    missing = [item for item in REQUIRED if not (root / item).exists()]
    if missing:
        raise SystemExit(f"BLOCK missing artifacts: {', '.join(missing)}")
    with (root / "results/sensitivity.csv").open(encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    frequencies = [float(row["inversion_frequency"]) for row in rows]
    if not any(value > 0.5 for value in frequencies):
        raise SystemExit("BLOCK sensitivity grid has no positive inversion region")
    if not any(value == 0.0 for value in frequencies):
        raise SystemExit("BLOCK sensitivity grid has no negative inversion region")
    hashes = []
    for relative in REQUIRED:
        hashes.append(f"{sha256(root / relative)}  {relative}")
    manifest = "\n".join(hashes) + "\n"
    manifest_path = root / "SHA256SUMS.txt"
    if args.check:
        if not manifest_path.exists():
            raise SystemExit("BLOCK checksum manifest is missing")
        if manifest_path.read_text(encoding="utf-8") != manifest:
            raise SystemExit("BLOCK generated artifacts differ from SHA256SUMS.txt")
    else:
        manifest_path.write_text(manifest, encoding="utf-8")
    print(f"PASS {len(REQUIRED)} artifacts; positive and negative sensitivity regions present")


if __name__ == "__main__":
    main()
