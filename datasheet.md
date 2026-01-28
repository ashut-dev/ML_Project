# Datasheet — BBO Capstone Dataset (13 Rounds)

## Motivation
This dataset was created incrementally as part of a controlled educational optimisation exercise, where each data point corresponds to a deliberate experimental decision informed by weekly learning objectives.

## Composition
- 13 rounds, 8 functions per round (2D → 8D).
- Stored as portal-ready strings (`data/roundXX/inputs.txt`) and scalar rewards (`data/roundXX/outputs.txt`).
- Each `inputs.txt` has 8 lines (one per function). Outputs likewise.

## Collection process
Queries were generated iteratively each week, informed by cumulative history and weekly learning topics (BO → LR → SVM → NN/DL → CNN → tuning → GenAI → interpretability → clustering → PCA).

## Preprocessing and intended uses
Formatting to six decimals for portal submission. Intended for reproducibility, learning reflection, and portfolio evidence.

## Distribution and maintenance
Public GitHub repository. Maintained by project author.
