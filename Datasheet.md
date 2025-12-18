BBO Optimization Capstone Dataset
1. Motivation - The dataset is for a Black Box Optimization project. Aim is to optimize eight unidentified functions within a limited query budget.Each function is infrequently evaluated, underscoring the importance of efficient decision-making. The dataset facilitates research into optimisation methodologies, including Bayesian optimisation, surrogate modelling, and heuristic refinement. It is designed to replicate real-world situations where objective functions are costly, non-transparent, and noisy, such as hyperparameter tuning, scientific experimentation, or industrial optimisation challenges.

2. Composition - This dataset is made up of input–output pairs collected over ten optimisation rounds.
Inputs: Query vectors, ranging from 2 to 8 dimensions, with each value between 0 and just under 1, represented to six decimal places.
Outputs: Single scalar values produced by black-box functions, which indicate the objective being maximised.
Size: By the tenth round, there are typically 18–20 data points for each function.
Format: Data is stored as plain text or in CSV-like files, with each query as a separate row.
Due to a limited query budget, coverage—especially in higher dimensions—is intentionally incomplete.

3. Collection Process - Queries were generated iteratively across ten rounds, each round informed by the accumulated data from previous evaluations. Early rounds focused on broad exploration, while later rounds shifted toward local exploitation and fine-grained refinement. The strategy evolved from heuristic exploration to trend-based and surrogate-informed optimisation. Data collection occurred sequentially over the duration of the capstone project, with each new query dependent on prior outputs.

4. Preprocessing and Intended Uses - No substantial preprocessing or transformation was performed apart from formatting the inputs to comply with portal specifications. Outputs were utilized in their original form.
Intended uses are as follows:
•	Analysis of optimisation strategies in scenarios with limited feedback
•	Investigation of exploration–exploitation trade-offs
•	Educational demonstrations pertaining to black-box optimisation
Inappropriate uses are as follows:
•	Considering the data as definitive evidence for real-world systems
•	Employing the data to train general-purpose predictive models outside of the capstone context

5. Distribution and Maintenance - The dataset is hosted in a public GitHub repository as part of the BBO capstone submission. It is intended for educational and non-commercial use only. The dataset is maintained by the project author and will not be actively updated after submission, except for documentation improvements.
