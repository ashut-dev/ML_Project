# Model Card — Iterative BBO Strategy (13 Rounds)

## Overview
Sequential query strategy for maximising 8 black-box functions with limited evaluations.

## Intended use
Educational optimisation with expensive evaluations; supports analysis of exploration vs exploitation. Avoid safety-critical use without monitoring.

## Strategy evolution (summary)
Early space-filling (BO) → boundary focus (LR/SVM) → non-linear surrogate mindset (NN/DL) → coarse-to-fine refinement (CNN) → stability via tuning → structured prompting (GenAI) → transparency improvements → cluster tightening → PCA-guided refinement.

## Performance reporting
See `reports/best_so_far_by_round.csv` (per-function reward and best-so-far).

## Assumptions & limitations
Limited evaluations in high dimensions, local optima risk, and dependence on heuristic/model assumptions.

## Transparency
Round logs + context doc + scripts enable reproducibility.
