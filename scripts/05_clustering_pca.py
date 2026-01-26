"""Clustering + PCA helper for a single function.

- Cluster X (k-means)
- Select cluster with best mean y
- Propose a point near that centroid (+ small noise) for boundary tightening
- PCA is computed for visualisation (optional)

Usage:
  python scripts/05_clustering_pca.py --func 8 --k 3
"""
import argparse, numpy as np
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from config import to_portal_string
from 01_load_history import load_history

def propose_next(X,y,k=3,seed=0,eps=0.05):
    km=KMeans(n_clusters=min(k,len(X)), random_state=seed, n_init="auto")
    lab=km.fit_predict(X)
    cent=km.cluster_centers_

    best_cluster=int(np.argmax([y[lab==c].mean() for c in range(cent.shape[0])]))
    best_mean=float(y[lab==best_cluster].mean())

    rng=np.random.default_rng(seed)
    x=cent[best_cluster] + rng.normal(0, eps, size=X.shape[1])
    x=np.clip(x,0.0,0.999999)

    pca=PCA(n_components=2, random_state=seed)
    X2=pca.fit_transform(X)
    return x, best_cluster, best_mean, pca.explained_variance_ratio_, X2

if __name__=="__main__":
    ap=argparse.ArgumentParser()
    ap.add_argument("--func", type=int, default=1)
    ap.add_argument("--k", type=int, default=3)
    ap.add_argument("--seed", type=int, default=0)
    ap.add_argument("--eps", type=float, default=0.05)
    args=ap.parse_args()

    Xs, ys = load_history()
    i=args.func-1
    x, c, m, var, _ = propose_next(Xs[i], ys[i], k=args.k, seed=args.seed, eps=args.eps)
    print(f"Best cluster={c} mean_y={m:.6f}  PCA var ratio={var}")
    print(f"Proposed next for Function {args.func}: {to_portal_string(x)}")
