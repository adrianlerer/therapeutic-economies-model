# Model contract

## State variables

At time `t`, `x_t` is the share of modeled organizations using a protection-seeking strategy and `c_t` is their productive capability stock. Both are bounded to `[0, 1]`.

The policy schedule supplies protection `p_t`, external exposure `e_t`, and conditional review `q_t`.

## Payoffs and fitness

Productive strategy payoff:

```text
pi_C = productive_base + capability_return*c_t + exposure_return*e_t
       + conditional_learning*p_t*e_t*q_t - exposure_cost*e_t
```

Protection-seeking payoff:

```text
pi_P = protection_base + protection_return*p_t
       - exposure_penalty*e_t - review_penalty*q_t*p_t
```

Payoffs are mapped to positive fitness using `exp(selection_strength*pi)`. The share update is a two-strategy replicator step followed by symmetric mutation.

## Capability production

For the endogenous model:

```text
c_(t+1) = clip(
    c_t
    formation_rate*(1-x_t)*(base_learning + exposure_learning*e_t)
    + conditional_capability*p_t*e_t*q_t*(1-x_t)
    - depreciation*c_t
    - dependency_damage*p_t*x_t*c_t
    + capability_shock,
    0, 1)
```

For the fixed baseline, `c_(t+1) = c_0`.

## Output proxy

The output proxy is a declared model quantity, not GDP:

```text
y_t = c_t*(1-x_t) + protected_activity*p_t*x_t
```

It separates capability-supported activity from activity maintained by protection.

## Protective selection inversion

A run is classified as showing protective selection inversion when all three conditions hold from the initial state to the final state of the declared simulation horizon:

1. the protection-seeking share rises by at least 0.10;
2. capability falls by at least 0.05;
3. mean protection-seeking fitness exceeds mean productive fitness.

This is a model diagnostic, not a validated real-world index.

## EGT and EPT boundaries

The EGT component concerns the changing distribution of strategies under relative fitness. No evolutionary stable strategy is claimed without invasion and stability analysis.

The EPT mapping is conditional. The candidate transmissible package is the representation that preserving an incumbent organization is itself productive success. Candidate vehicles include rules, subsidies, administrative routines, and justificatory narratives. The modeled protected ecology is an extended effect only if variation, transmission, causal reach, and differential retention can be independently evidenced. The simulation does not prove those conditions in a real jurisdiction.

## Causal ceiling

The simulation establishes internal sufficiency only: under the declared equations and parameters, the mechanism can or cannot generate a pattern. It does not identify a causal effect, validate a construct, predict a country, or justify a policy.
