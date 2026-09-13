# Therapeutic Economies Model

Reproducible simulation accompanying Ignacio Adrián Lerer's theoretical-computational preprint, *Therapeutic Economies: Protective Selection, Endogenous Capabilities, and Institutional Dependence*.

The manuscript is available as [Markdown](paper/MANUSCRIPT.md), [PDF](paper/Therapeutic_Economies_Preprint.pdf), and [DOCX](paper/Therapeutic_Economies_Preprint.docx). The source and claim boundary is documented in [the audit ledger](paper/SOURCE_AND_CLAIM_AUDIT.md).

## Research question

Can unconditional protection create a selection inversion in which protection-seeking becomes locally adaptive while the productive capability of the modeled population declines?

The code demonstrates only that the proposed mechanism can generate the reported patterns under explicit assumptions. It does not estimate, calibrate, or validate effects for Argentina or any real economy.

## Reproduce

Python 3.10 or newer is recommended. No third-party package is required.

```bash
python3 -m unittest discover -s tests -v
python3 run_experiments.py --seeds 200 --output results
python3 verify_release.py --check
```

The exact release environment used Python 3.14.0 on macOS. Continuous integration independently reproduces the result tables on Python 3.14/Linux with an absolute numerical tolerance of `1e-10`. Release hashes establish artifact integrity within the release environment; cross-platform byte identity is not claimed because standard-library transcendental functions can differ at machine precision. Shocks are derived from SHA-256 rather than a platform-dependent Gaussian pseudorandom implementation.

Generated artifacts:

- `results/summary.csv`: scenario-level results.
- `results/trajectories.csv`: mean time paths.
- `results/sensitivity.csv`: parameter-grid results, including negative cases.
- `results/summary.json`: machine-readable configuration and summary.
- `results/trajectories.svg`: dependency-free figure.
- `SHA256SUMS.txt`: release hashes.

## Models

The endogenous-capability model and fixed-capability baseline share the same policy schedules, initial states, shocks, payoff functions, selection rule, and seeds. They differ only in whether productive capability evolves.

The protection-seeking share follows a discrete replicator-mutator process. Capability evolves from retention, productive activity, external exposure, conditional learning, and dependence-related depreciation. See [`MODEL.md`](MODEL.md) for equations, assumptions, and claim limits.

## Scenarios

| Scenario | Protection | Exposure | Review |
|---|---:|---:|---:|
| Unconditional protection | High | Low | Low |
| Conditional support | Moderate | High | High |
| Open exposure | Low | High | Moderate |
| Sequenced transition | High to moderate to low | Low to high | Low to high |

## Repository boundaries

This repository contains synthetic code and generated data only. It excludes copyrighted source books, extracted text, private research materials, credentials, prompts, and unpublished operational methods.

## License and citation

Code is released under the MIT License. Paper text and documentation are released under CC BY 4.0; see `LICENSE-CONTENT`. Citation metadata is in `CITATION.cff`.

## Author

Ignacio Adrián Lerer, ORCID [0009-0007-6378-9749](https://orcid.org/0009-0007-6378-9749)  
[estudio.justitia.com.ar](https://estudio.justitia.com.ar)
