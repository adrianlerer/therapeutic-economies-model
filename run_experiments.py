#!/usr/bin/env python3
"""Run deterministic experiments and write CSV, JSON, and SVG artifacts."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
from collections import defaultdict
from dataclasses import replace
from pathlib import Path
from statistics import mean, pstdev

from therapeutic_economies import Parameters, SCENARIOS, inversion, parameter_dict, simulate


def summarise_runs(runs):
    finals = [run[-1] for run in runs]
    return {
        "final_protection_share_mean": mean(r["protection_share"] for r in finals),
        "final_protection_share_sd": pstdev(r["protection_share"] for r in finals),
        "final_capability_mean": mean(r["capability"] for r in finals),
        "final_capability_sd": pstdev(r["capability"] for r in finals),
        "cumulative_output_mean": mean(sum(row["output_proxy"] for row in run) for run in runs),
        "inversion_frequency": mean(1.0 if inversion(run) else 0.0 for run in runs),
    }


def write_csv(path, rows, fieldnames):
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def mean_trajectories(all_runs):
    rows = []
    for (scenario, model), runs in sorted(all_runs.items()):
        for step in range(len(runs[0])):
            sample = [run[step] for run in runs]
            rows.append({
                "scenario": scenario,
                "model": model,
                "step": step,
                "protection_share": mean(r["protection_share"] for r in sample),
                "capability": mean(r["capability"] for r in sample),
                "output_proxy": mean(r["output_proxy"] for r in sample),
            })
    return rows


def sensitivity(params, seeds):
    rows = []
    for protection_return in (0.55, 0.75, 0.95, 1.15):
        for dependency_damage in (0.00, 0.02, 0.048, 0.08):
            test_params = replace(params, protection_return=protection_return,
                                  dependency_damage=dependency_damage)
            runs = [simulate("unconditional_protection", seed, True, test_params) for seed in range(seeds)]
            summary = summarise_runs(runs)
            rows.append({
                "protection_return": protection_return,
                "dependency_damage": dependency_damage,
                **summary,
            })
    return rows


def svg_figure(path, trajectory_rows):
    width, height = 1000, 720
    margin = 70
    panel_h = 250
    colors = {
        "unconditional_protection": "#111111",
        "conditional_support": "#555555",
        "open_exposure": "#888888",
        "sequenced_transition": "#BBBBBB",
    }
    grouped = defaultdict(list)
    for row in trajectory_rows:
        if row["model"] == "endogenous":
            grouped[row["scenario"]].append(row)
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
             '<rect width="100%" height="100%" fill="white"/>',
             '<style>text{font-family:Arial,sans-serif;fill:#111}.axis{stroke:#111;stroke-width:1}.grid{stroke:#ddd;stroke-width:1}.line{fill:none;stroke-width:3}</style>',
             '<text x="500" y="35" text-anchor="middle" font-size="22">Endogenous-capability trajectories</text>']
    for panel, (metric, label) in enumerate((("protection_share", "Protection-seeking share"), ("capability", "Capability stock"))):
        top = 70 + panel * 310
        bottom = top + panel_h
        parts.append(f'<text x="20" y="{top + panel_h/2}" transform="rotate(-90 20 {top + panel_h/2})" text-anchor="middle" font-size="16">{label}</text>')
        for tick in range(6):
            y = bottom - tick * panel_h / 5
            parts.append(f'<line class="grid" x1="{margin}" y1="{y}" x2="{width-margin}" y2="{y}"/>')
            parts.append(f'<text x="{margin-10}" y="{y+5}" text-anchor="end" font-size="12">{tick/5:.1f}</text>')
        parts.append(f'<line class="axis" x1="{margin}" y1="{top}" x2="{margin}" y2="{bottom}"/>')
        parts.append(f'<line class="axis" x1="{margin}" y1="{bottom}" x2="{width-margin}" y2="{bottom}"/>')
        for scenario, rows in grouped.items():
            points = []
            max_step = rows[-1]["step"]
            for row in rows:
                x = margin + (width - 2 * margin) * row["step"] / max_step
                y = bottom - panel_h * row[metric]
                points.append(f"{x:.1f},{y:.1f}")
            parts.append(f'<polyline class="line" stroke="{colors[scenario]}" points="{" ".join(points)}"/>')
    legend_y = 690
    for idx, scenario in enumerate(SCENARIOS):
        x = 90 + idx * 225
        parts.append(f'<line x1="{x}" y1="{legend_y}" x2="{x+28}" y2="{legend_y}" stroke="{colors[scenario]}" stroke-width="4"/>')
        parts.append(f'<text x="{x+35}" y="{legend_y+5}" font-size="12">{scenario.replace("_", " ")}</text>')
    parts.append('</svg>')
    path.write_text("\n".join(parts), encoding="utf-8")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--seeds", type=int, default=200)
    parser.add_argument("--output", type=Path, default=Path("results"))
    args = parser.parse_args()
    if args.seeds < 2:
        parser.error("--seeds must be at least 2")
    args.output.mkdir(parents=True, exist_ok=True)
    params = Parameters()
    all_runs = {}
    summary_rows = []
    for scenario in SCENARIOS:
        for endogenous, model in ((True, "endogenous"), (False, "fixed")):
            runs = [simulate(scenario, seed, endogenous, params) for seed in range(args.seeds)]
            all_runs[(scenario, model)] = runs
            summary_rows.append({"scenario": scenario, "model": model, **summarise_runs(runs)})
    trajectories = mean_trajectories(all_runs)
    sensitivity_rows = sensitivity(params, min(args.seeds, 100))
    write_csv(args.output / "summary.csv", summary_rows, list(summary_rows[0]))
    write_csv(args.output / "trajectories.csv", trajectories, list(trajectories[0]))
    write_csv(args.output / "sensitivity.csv", sensitivity_rows, list(sensitivity_rows[0]))
    payload = {"seeds": args.seeds, "parameters": parameter_dict(params), "summary": summary_rows}
    (args.output / "summary.json").write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    svg_figure(args.output / "trajectories.svg", trajectories)
    print(json.dumps({"status": "ok", "output": str(args.output), "runs": len(SCENARIOS) * 2 * args.seeds}))


if __name__ == "__main__":
    main()
