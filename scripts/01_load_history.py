"""Load the 13-round history from data/roundXX files.

Outputs are returned by the capstone portal (black-box), so we treat them as observations.
This script builds per-function X, y arrays you can feed into surrogate models.

Usage:
  python scripts/01_load_history.py
"""
import os
import numpy as np
from config import DIMS, N_FUNCS, parse_portal_string

ROOT = os.path.dirname(os.path.dirname(__file__))
DATA_DIR = os.path.join(ROOT, "data")

def load_round(r):
    rdir = os.path.join(DATA_DIR, f"round{r:02d}")
    x_lines = [ln.strip() for ln in open(os.path.join(rdir, "inputs.txt")).read().splitlines() if ln.strip() and not ln.startswith("#")]
    y_lines = [ln.strip() for ln in open(os.path.join(rdir, "outputs.txt")).read().splitlines() if ln.strip() and not ln.startswith("#")]
    assert len(x_lines)==N_FUNCS, f"Round {r}: expected {N_FUNCS} input lines"
    assert len(y_lines)==N_FUNCS, f"Round {r}: expected {N_FUNCS} output lines"
    X = [parse_portal_string(s) for s in x_lines]
    y = [float(v) for v in y_lines]
    return X, y

def load_history(n_rounds=13):
    Xs = [[] for _ in range(N_FUNCS)]
    ys = [[] for _ in range(N_FUNCS)]
    for r in range(1, n_rounds+1):
        Xr, yr = load_round(r)
        for i in range(N_FUNCS):
            Xs[i].append(Xr[i])
            ys[i].append(yr[i])
    Xs = [np.array(X, dtype=float) for X in Xs]
    ys = [np.array(y, dtype=float) for y in ys]
    return Xs, ys

if __name__ == "__main__":
    Xs, ys = load_history()
    for i,(X,y) in enumerate(zip(Xs,ys), start=1):
        print(f"Function {i}: X shape={X.shape}, y shape={y.shape}, best={y.max():.6f}")
