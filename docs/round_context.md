# Round-by-round learning context
Each submission round aligns with the weekly learning topic and influenced how the next query points were chosen.

## Round 01: Bayesian Optimisation (initial exploration + EI/UCB intuition)
How it influenced my query decisions:
- Space-filling exploration to understand the surface; avoid premature convergence.

## Round 02: Logistic Regression (linear trends, thresholds, simple boundaries)
How it influenced my query decisions:
- Used a ‘good vs bad’ lens and linear trend intuition to bias towards improving regions.

## Round 03: SVM (margin thinking, boundary points, kernel intuition)
How it influenced my query decisions:
- Focused on boundary points and small moves around strong regions (support-vector mindset).

## Round 04: Neural Networks & Deep Learning (non-linear surrogate intuition)
How it influenced my query decisions:
- Allowed non-linear interactions; moved multiple coordinates together instead of one-by-one.

## Round 05: Advanced NN/DL (backprop/gradients, sensitivity)
How it influenced my query decisions:
- Gradient intuition: smaller directional steps to refine rather than random jumps.

## Round 06: CNNs (coarse-to-fine refinement mindset)
How it influenced my query decisions:
- Coarse-to-fine: broad region first, then tighten locally like CNN feature hierarchy.

## Round 07: Hyperparameters (what to tune, stability vs performance)
How it influenced my query decisions:
- Stabilised the search: reduced volatility by controlling step size / exploration intensity.

## Round 08: Hyperparameter Tuning (search strategies, trade-offs)
How it influenced my query decisions:
- More systematic tuning mindset: tested settings rather than ad-hoc changes.

## Round 09: GenAI & LLM (prompt patterns, formatting discipline)
How it influenced my query decisions:
- Prompt discipline: consistent templates + strict output formatting to avoid submission errors.

## Round 10: Advanced GenAI & LLM (decoding choices, hallucination control)
How it influenced my query decisions:
- Controlled ‘decoding’: keep outputs structured, reduce drift, cross-check numbers.

## Round 11: Transparency & Interpretability (documenting assumptions/decisions)
How it influenced my query decisions:
- Increased transparency: documented why points were chosen so strategy is reproducible.

## Round 12: Unsupervised Learning – Clustering (clusters, centroids, distances)
How it influenced my query decisions:
- Clustering: identified recurring promising regions and tightened around centroids / boundaries.

## Round 13: Unsupervised Learning – PCA (dimensionality reduction, variance focus)
How it influenced my query decisions:
- PCA: focused refinement along dominant directions of variation; reduced irrelevant movement.

