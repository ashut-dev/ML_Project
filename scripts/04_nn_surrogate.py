"""Neural surrogate using MLPRegressor + local refinement.

Fits an MLP to (X,y), then performs local random search around the best-known point.

Usage:
  python scripts/04_nn_surrogate.py --func 8
"""
import argparse, numpy as np
from sklearn.neural_network import MLPRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from config import to_portal_string
from 01_load_history import load_history

def propose_next(X, y, seed=0, n_steps=20000, step=0.05):
    rng = np.random.default_rng(seed)
    d=X.shape[1]
    mlp = make_pipeline(
        StandardScaler(),
        MLPRegressor(hidden_layer_sizes=(64,64), activation="relu",
                     alpha=1e-4, learning_rate_init=1e-3,
                     max_iter=3000, random_state=seed)
    )
    mlp.fit(X, y)

    x = X[np.argmax(y)].copy()
    best_pred = float(mlp.predict(x.reshape(1,-1))[0])

    for _ in range(n_steps):
        cand = x + rng.normal(0, step, size=d)
        cand = np.clip(cand, 0.0, 0.999999)
        pred = float(mlp.predict(cand.reshape(1,-1))[0])
        if pred > best_pred:
            best_pred = pred
            x = cand
    return x, best_pred

if __name__ == "__main__":
    ap=argparse.ArgumentParser()
    ap.add_argument("--func", type=int, default=1)
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--n_steps", type=int, default=20000)
    ap.add_argument("--step", type=float, default=0.05)
    args=ap.parse_args()

    Xs, ys = load_history()
    i=args.func-1
    x_next, pred = propose_next(Xs[i], ys[i], seed=args.seed, n_steps=args.n_steps, step=args.step)
    print(f"Proposed next for Function {args.func}: {to_portal_string(x_next)}")
    print(f"Surrogate predicted value ~ {pred:.6f}")
