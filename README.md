# BBO Capstone Project — Final (13 Rounds)

This repo is my final submission for the **Black-Box Optimisation** capstone. It contains **all 13 rounds** of portal-ready query strings and returned outputs for **8 functions** (2D → 8D), plus documentation showing how the strategy evolved with weekly learning.

## Goal
Maximise each black-box function with a strict query budget (1 query per function per round).

## Learning progression aligned to rounds
1. Bayesian Optimisation  
2. Logistic Regression  
3. SVM  
4. Neural Networks & Deep Learning  
5. Advanced NN/DL (backprop, gradients)  
6. CNNs (coarse-to-fine refinement)  
7. Hyperparameters  
8. Hyperparameter tuning  
9. GenAI & LLM prompting  
10. Advanced GenAI & LLM (decoding, hallucination control)  
11. Transparency & interpretability  
12. Clustering  
13. PCA  

See `docs/round_context.md` for how each topic influenced the weekly query choices.

## Repo structure
- `data/roundXX/inputs.txt` and `data/roundXX/outputs.txt`
- `queries/roundXX_queries.txt` (portal submission format)
- `reports/best_so_far_by_round.csv` (quick performance tracking)
- `datasheet.md` and `model_card.md` (mini-lesson frameworks)
- `scripts/make_portal_strings.py` (working / reproducibility)

