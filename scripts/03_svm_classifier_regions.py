"""SVM 'good vs bad' region classifier to guide exploration.

Label points GOOD if y >= quantile (e.g., top 25%).
Fit an RBF SVM classifier, sample candidates, pick:
  high p(GOOD) + diversity (distance from nearest observed point).

Usage:
  python scripts/03_svm_classifier_regions.py --func 7
"""
import argparse, numpy as np
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from config import to_portal_string
from 01_load_history import load_history

def propose_next(X, y, n_cand=50000, q=0.75, seed=0):
    rng = np.random.default_rng(seed)
    thr = np.quantile(y, q)
    y_bin = (y >= thr).astype(int)

    clf = make_pipeline(
        StandardScaler(),
        SVC(kernel="rbf", C=10.0, gamma="scale", probability=True, random_state=seed)
    )
    clf.fit(X, y_bin)

    d = X.shape[1]
    cand = rng.random((n_cand, d))
    p_good = clf.predict_proba(cand)[:,1]

    diffs = cand[:,None,:] - X[None,:,:]
    dist = np.sqrt((diffs*diffs).sum(axis=2)).min(axis=1)

    score = p_good + 0.25*dist
    j = int(np.argmax(score))
    return cand[j], float(p_good[j]), float(dist[j]), float(thr)

if __name__ == "__main__":
    ap=argparse.ArgumentParser()
    ap.add_argument("--func", type=int, default=1)
    ap.add_argument("--n_cand", type=int, default=50000)
    ap.add_argument("--q", type=float, default=0.75)
    ap.add_argument("--seed", type=int, default=0)
    args=ap.parse_args()

    Xs, ys = load_history()
    i=args.func-1
    x_next, p, dist, thr = propose_next(Xs[i], ys[i], n_cand=args.n_cand, q=args.q, seed=args.seed)
    print(f"GOOD threshold (q={args.q}): {thr:.6f}")
    print(f"Proposed next for Function {args.func}: {to_portal_string(x_next)}")
    print(f"p_good={p:.3f}  diversity_dist={dist:.3f}")
