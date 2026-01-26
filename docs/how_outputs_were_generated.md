# How inputs and outputs were generated (capstone portal)

Inputs (queries) were generated weekly as one point per function. Each point is a vector in [0,1) and was submitted to the portal as:
`0.xxxxxx-0.yyyyyy-...` (six decimals).

Outputs were returned by the portal by evaluating hidden black-box functions. These functions are not available locally, so outputs cannot be regenerated offline. This repository focuses on:
- logging inputs/outputs round-wise, and
- providing reproducible query-selection code given the logged history.
