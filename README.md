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


## Code: how queries and outputs were handled
The capstone portal is the only source of black-box outputs. This repo therefore cannot reproduce outputs from code.
What is reproducible is the **query selection logic** given the logged history.

- Load history into (X,y): `python scripts/01_load_history.py`
- BO-like EI proposer: `python scripts/02_baseline_bo.py --func 8`
- SVM good/bad region classifier: `python scripts/03_svm_classifier_regions.py --func 7`
- Neural surrogate refinement: `python scripts/04_nn_surrogate.py --func 8`
- Clustering + PCA guided proposal: `python scripts/05_clustering_pca.py --func 8`
- RL/MAB region policy (educational): `python scripts/06_rl_bandit_policy.py --func 8`
