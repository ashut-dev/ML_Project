Black-Box Optimisation (BBO) Capstone Project
This repository contains my final submission for the Black-Box Optimisation (BBO) capstone project.
The project spans 13 iterative query rounds, each aligned with weekly learning objectives across optimisation, machine learning, deep learning, interpretability and unsupervised learning.
The central objective is to maximise eight unknown black-box functions (ranging from 2D to 8D) under a strict query budget of one query per function per round.
All optimisation decisions are made without access to gradients or internal function structure, reflecting real-world black-box constraints.
This submission emphasises process, reasoning and learning progression, not just final performance.
1. Project Objective
The BBO capstone aims to:
•	efficiently explore and exploit unknown objective functions,
•	adapt optimisation strategy as more data becomes available,
•	demonstrate how theoretical ML concepts translate into practical decision-making under uncertainty.
Each round represents a deliberate optimisation decision informed by newly learned methods, rather than a fixed optimiser applied repeatedly.
2. Learning-Driven Iterative Strategy
The optimisation strategy evolves week-by-week, directly reflecting the programme’s curriculum.
Round	Learning Focus
01	Bayesian Optimisation (uncertainty-aware exploration)
02	Logistic Regression (good vs bad region separation)
03	Support Vector Machines (decision boundary reasoning)
04	Neural Networks (non-linear surrogate modelling)
05	Advanced NN (backpropagation, gradients)
06	CNN analogy (coarse-to-fine refinement)
07	Hyperparameter sensitivity
08	Hyperparameter tuning strategies
09	GenAI & prompt structuring
10	Advanced GenAI (decoding, hallucination control)
11	Transparency & interpretability
12	Unsupervised learning – Clustering
13	Unsupervised learning – PCA
Each round produces exactly one portal-ready query per function, submitted and evaluated before proceeding to the next iteration.
A detailed narrative of how each learning theme influenced query design is provided in
 docs/round_context.md.
3. Primary Assessment Artefacts: Round-wise Notebooks
The core evidence for assessment is contained in the Jupyter notebooks under the notebooks/ directory.
Each notebook corresponds to one round and documents:
•	query selection logic,
•	returned black-box outputs,
•	best-so-far tracking,
•	reflective reasoning for decisions made.
Round	Notebook
01	notebooks/round01.ipynb
02	notebooks/round02.ipynb
03	notebooks/round03.ipynb
04	notebooks/round04.ipynb
05	notebooks/round05.ipynb
06	notebooks/round06.ipynb
07	notebooks/round07.ipynb
08	notebooks/round08.ipynb
09	notebooks/round09.ipynb
10	notebooks/round10.ipynb
11	notebooks/round11.ipynb
12	notebooks/round12.ipynb
13	notebooks/round13.ipynb

4. Data Organisation
All portal interactions are logged transparently.
data/
 └── roundXX/
     ├── inputs.txt     # Submitted query points
     └── outputs.txt    # Returned black-box outputs
The capstone portal is the only source of function evaluations.
As a result, numerical outputs cannot be regenerated offline; however, the decision logic used to select queries is fully documented and reproducible.
5. Supporting Code and Methods
Scripts under scripts/ support analysis, visualisation and reasoning:
•	01_load_history.py – load cumulative query history
•	02_baseline_bo.py – Bayesian-style expected improvement baseline
•	03_svm_classifier_regions.py – region classification using SVMs
•	04_nn_surrogate.py – neural surrogate modelling
•	05_clustering_pca.py – clustering and PCA for structure discovery
•	06_rl_bandit_policy.py – educational RL / MAB framing
•	make_portal_strings.py – portal submission formatting
These scripts support the notebooks and demonstrate method application, not offline reproduction of portal outputs.

6. Documentation for Transparency and Reproducibility
•	 datasheet.md – dataset documentation (Mini-lesson 21.1)
•	 model_card.md – optimisation approach description (Mini-lesson 21.2)
•	docs/round_context.md – round-by-round learning rationale
•	 reports/best_so_far_by_round.csv – performance tracking
Together, these provide a clear audit trail from learning objective → modelling choice → query decision → observed outcome.

7. Key Takeaways
•	Optimisation performance improves as model understanding matures
•	Later rounds prioritise structure discovery and interpretability
•	The project mirrors real-world ML workflows, where strategy adapts as data accumulates
•	Transparency and documentation are treated as first-class outcomes

