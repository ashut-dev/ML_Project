# Model Card — Iterative BBO Strategy (13 Rounds)

## Overview
Sequential query strategy for maximising 8 black-box functions with limited evaluations.

## Intended use
Educational optimisation with expensive evaluations; supports analysis of exploration vs exploitation. Avoid safety-critical use without monitoring.

## Strategy evolution (summary)
This optimisation approach is explicitly iterative and curriculum-driven. Rather than fixing a single optimiser, the strategy evolves weekly in response to new learning outcomes.Early rounds prioritised uncertainty-aware exploration, while later rounds focused on interpretability, clustering and structure discovery. This progression mirrors real-world ML workflows where optimisation strategies mature alongside domain understanding and data availability

## Performance reporting
See `reports/best_so_far_by_round.csv` (per-function reward and best-so-far).

## Assumptions & limitations
Limited evaluations in high dimensions, local optima risk, and dependence on heuristic/model assumptions.

## Transparency
Round logs + context doc + scripts enable reproducibility.
