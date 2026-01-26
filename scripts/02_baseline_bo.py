"""BO-like proposer using a tree surrogate + EI-style score.

The black-box outputs come only from the portal; this script proposes the next query given history.

Usage:
  python scripts/02_baseline_bo.py --func 8 --n_cand 50000
"""
import argparse, numpy as np
from sklearn.ensemble import RandomForestRegressor
from scipy.stats import norm
from config import to_portal_string
from 01_load_history import load_history

def propose_next(X, y, n_cand=20000, seed=0, xi=0.01):
    rng = np.random.default_rng(seed)
    d = X.shape[1]
    rf = RandomForestRegressor(
        n_estimators=400,
        random_state=seed,
        min_samples_leaf=max(1, int(0.05*len(X))),
        n_jobs=-1
    )
    rf.fit(X, y)

    cand = rng.random((n_cand, d))
    preds = np.stack([t.predict(cand) for t in rf.estimators_], axis=0)
    mu = preds.mean(axis=0)
    sigma = preds.std(axis=0) + 1e-9

    best = y.max()
    z = (mu - best - xi) / sigma
    ei = (mu - best - xi) * norm.cdf(z) + sigma * norm.pdf(z)
    j = int(np.argmax(ei))
    return cand[j], float(ei[j]), float(mu[j]), float(sigma[j])

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--func", type=int, default=1)
    ap.add_argument("--n_cand", type=int, default=20000)
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--xi", type=float, default=0.01)
    args = ap.parse_args()

    Xs, ys = load_history()
    i = args.func - 1
    x_next, ei, mu, sig = propose_next(Xs[i], ys[i], n_cand=args.n_cand, seed=args.seed, xi=args.xi)
    print(f"Proposed next for Function {args.func}: {to_portal_string(x_next)}")
    print(f"EI={ei:.6f}  pred_mu={mu:.6f}  pred_sigma={sig:.6f}")
