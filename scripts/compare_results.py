#!/usr/bin/env python3
"""Compare reproduced CSV results with reference artifacts within tolerance."""

import argparse
import csv
from pathlib import Path


FILES = ("summary.csv", "trajectories.csv", "sensitivity.csv")


def numeric(value):
    try:
        return float(value)
    except ValueError:
        return None


def compare(reference, candidate, tolerance):
    with reference.open(encoding="utf-8") as handle:
        expected = list(csv.DictReader(handle))
    with candidate.open(encoding="utf-8") as handle:
        actual = list(csv.DictReader(handle))
    if len(expected) != len(actual):
        raise SystemExit(f"BLOCK row count differs for {reference.name}")
    if expected and actual and expected[0].keys() != actual[0].keys():
        raise SystemExit(f"BLOCK columns differ for {reference.name}")
    for row_index, (left, right) in enumerate(zip(expected, actual), start=2):
        for key in left:
            left_num, right_num = numeric(left[key]), numeric(right[key])
            if left_num is None or right_num is None:
                if left[key] != right[key]:
                    raise SystemExit(f"BLOCK {reference.name}:{row_index} {key} differs")
            elif abs(left_num - right_num) > tolerance:
                raise SystemExit(
                    f"BLOCK {reference.name}:{row_index} {key} differs by "
                    f"{abs(left_num - right_num):.3g}, tolerance {tolerance}"
                )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("reference", type=Path)
    parser.add_argument("candidate", type=Path)
    parser.add_argument("--tolerance", type=float, default=1e-10)
    args = parser.parse_args()
    for name in FILES:
        compare(args.reference / name, args.candidate / name, args.tolerance)
    print(f"PASS {len(FILES)} result tables reproduced within {args.tolerance:g}")


if __name__ == "__main__":
    main()
