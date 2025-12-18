Model Name - Imperial ML Course BBO Optimization V1.0

Overview - This is a heuristic and surrogate-informed optimisation approach designed for black-box functions with limited evaluation budgets. It combines exploration, trend-following and local refinement across multiple rounds.

Intended Use - The approach is suitable for:
•	Expensive black-box optimisation problems
•	Educational demonstrations of Bayesian-style optimisation
•	Low-sample optimisation scenarios
It should not be used for:
•	High-stakes decision-making without uncertainty modelling
•	Problems requiring guaranteed global optimality

Strategy Details - Across ten rounds, the strategy evolved as follows:
•	Rounds 1–3: Broad exploration to understand the search space
•	Rounds 4–6: Trend-based refinement and cautious exploitation
•	Rounds 7–10: Fine-grained local optimisation with micro-adjustments
Decisions were guided by observed improvements, output stability and sensitivity to small input changes.

Performance - Performance was evaluated qualitatively using:
•	Improvement over rounds
•	Stability of outputs
•	Responsiveness to local refinements
No single numeric benchmark was used, as the true optima are unknown.

Assumptions and Limitations - Key assumptions include local smoothness of functions and relevance of recent trends. Limitations include susceptibility to local optima, uneven search-space coverage and reliance on heuristic judgement rather than formal uncertainty estimates

Ethical Considerations - Transparency in documenting decisions supports reproducibility and learning. The model card clarifies assumptions and constraints, helping prevent misuse or over-interpretation of results in real-world contexts.

Reflection On Documentation - The current structure balances clarity and completeness. Adding excessive detail may reduce readability without improving understanding. The datasheet and model card together provide sufficient context for peers and facilitators to interpret, reproduce and critique the approach.

