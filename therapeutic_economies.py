"""Dependency-free evolutionary model for therapeutic economies.

The model is explanatory and synthetic. It is not calibrated to any country.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
import hashlib
from math import exp
from typing import Dict, Iterable, List, Tuple


def clip(value: float, lower: float = 0.0, upper: float = 1.0) -> float:
    return max(lower, min(upper, value))


def stable_normal(seed: int, step: int, stream: str) -> float:
    """Return a deterministic, approximately standard-normal shock.

    Twelve SHA-256-derived uniforms form an Irwin-Hall approximation. This
    avoids platform-dependent pseudorandom Gaussian implementations.
    """
    total = 0.0
    for index in range(12):
        payload = f"{seed}:{step}:{stream}:{index}".encode("ascii")
        integer = int.from_bytes(hashlib.sha256(payload).digest()[:8], "big")
        total += integer / 18446744073709551616
    return total - 6.0


@dataclass(frozen=True)
class Parameters:
    steps: int = 120
    initial_protection_share: float = 0.30
    initial_capability: float = 0.62
    productive_base: float = 0.10
    protection_base: float = 0.04
    capability_return: float = 0.90
    exposure_return: float = 0.42
    exposure_cost: float = 0.20
    conditional_learning: float = 0.34
    protection_return: float = 0.95
    exposure_penalty: float = 0.38
    review_penalty: float = 0.52
    selection_strength: float = 1.25
    mutation_rate: float = 0.006
    formation_rate: float = 0.032
    base_learning: float = 0.15
    exposure_learning: float = 0.72
    conditional_capability: float = 0.022
    depreciation: float = 0.012
    dependency_damage: float = 0.048
    protected_activity: float = 0.48
    shock_sd: float = 0.018
    capability_shock_sd: float = 0.003


SCENARIOS = (
    "unconditional_protection",
    "conditional_support",
    "open_exposure",
    "sequenced_transition",
)


def policy(scenario: str, step: int, total_steps: int) -> Tuple[float, float, float]:
    if scenario == "unconditional_protection":
        return 0.88, 0.12, 0.08
    if scenario == "conditional_support":
        return 0.58, 0.78, 0.82
    if scenario == "open_exposure":
        return 0.10, 0.92, 0.55
    if scenario == "sequenced_transition":
        phase = step / total_steps
        if phase < 1 / 3:
            return 0.82, 0.20, 0.18
        if phase < 2 / 3:
            return 0.52, 0.68, 0.76
        return 0.14, 0.90, 0.68
    raise ValueError(f"unknown scenario: {scenario}")


def payoffs(x: float, capability: float, p: float, e: float, q: float,
            params: Parameters, shock: float = 0.0) -> Tuple[float, float]:
    productive = (
        params.productive_base
        + params.capability_return * capability
        + params.exposure_return * e
        + params.conditional_learning * p * e * q
        - params.exposure_cost * e
        + shock
    )
    protective = (
        params.protection_base
        + params.protection_return * p
        - params.exposure_penalty * e
        - params.review_penalty * q * p
        - shock
    )
    return productive, protective


def selection_update(x: float, productive: float, protective: float,
                     params: Parameters) -> float:
    f_c = exp(params.selection_strength * productive)
    f_p = exp(params.selection_strength * protective)
    denom = x * f_p + (1.0 - x) * f_c
    selected = x if denom == 0 else x * f_p / denom
    mutated = (1.0 - params.mutation_rate) * selected + params.mutation_rate * (1.0 - selected)
    return clip(mutated)


def capability_update(capability: float, x: float, p: float, e: float, q: float,
                      params: Parameters, shock: float) -> float:
    productive_share = 1.0 - x
    gain = params.formation_rate * productive_share * (
        params.base_learning + params.exposure_learning * e
    )
    conditional_gain = params.conditional_capability * p * e * q * productive_share
    loss = params.depreciation * capability + params.dependency_damage * p * x * capability
    return clip(capability + gain + conditional_gain - loss + shock)


def simulate(scenario: str, seed: int, endogenous: bool = True,
             params: Parameters | None = None) -> List[Dict[str, float]]:
    params = params or Parameters()
    x = params.initial_protection_share
    capability = params.initial_capability
    rows: List[Dict[str, float]] = []
    for step in range(params.steps + 1):
        p, e, q = policy(scenario, min(step, params.steps - 1), params.steps)
        payoff_shock = stable_normal(seed, step, "payoff") * params.shock_sd
        productive, protective = payoffs(x, capability, p, e, q, params, payoff_shock)
        output = capability * (1.0 - x) + params.protected_activity * p * x
        rows.append({
            "step": step,
            "protection_share": x,
            "capability": capability,
            "protection": p,
            "exposure": e,
            "review": q,
            "productive_payoff": productive,
            "protective_payoff": protective,
            "output_proxy": output,
        })
        if step == params.steps:
            break
        next_x = selection_update(x, productive, protective, params)
        if endogenous:
            cap_shock = stable_normal(seed, step, "capability") * params.capability_shock_sd
            capability = capability_update(capability, x, p, e, q, params, cap_shock)
        else:
            capability = params.initial_capability
        x = next_x
    return rows


def inversion(rows: List[Dict[str, float]]) -> bool:
    """Classify inversion across the declared full simulation horizon."""
    start = rows[0]
    evaluated = rows[1:]
    x_rise = rows[-1]["protection_share"] - start["protection_share"] >= 0.10
    cap_fall = rows[-1]["capability"] - start["capability"] <= -0.05
    mean_advantage = sum(
        r["protective_payoff"] - r["productive_payoff"] for r in evaluated
    ) / len(evaluated)
    return bool(x_rise and cap_fall and mean_advantage > 0)


def parameter_dict(params: Parameters) -> Dict[str, float]:
    return asdict(params)
