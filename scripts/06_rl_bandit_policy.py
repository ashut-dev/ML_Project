"""Multi-Armed Bandit style region policy (educational).

Discretise [0,1) into bins per dimension -> each bin is an 'arm'.
Reward per arm = best y observed in that bin.
Select arm via epsilon-greedy and sample uniformly inside it.

Usage:
  python scripts/06_rl_bandit_policy.py --func 8 --bins 4
"""
import argparse, numpy as np
from config import to_portal_string
from 01_load_history import load_history

def propose_next(X,y,bins=4,eps=0.1,seed=0):
    rng=np.random.default_rng(seed)
    d=X.shape[1]
    b = np.floor(X*bins).clip(0,bins-1).astype(int)
    mult = (bins ** np.arange(d))
    arm_id = (b * mult).sum(axis=1)

    n_arms = bins**d
    arm_val = np.full(n_arms, -np.inf)
    for aid, reward in zip(arm_id, y):
        arm_val[aid] = max(arm_val[aid], reward)

    if rng.random() < eps or not np.any(np.isfinite(arm_val)):
        chosen = int(rng.integers(0, n_arms))
    else:
        chosen = int(np.nanargmax(arm_val))

    coords=[]
    rem=chosen
    for _ in range(d):
        coords.append(rem % bins)
        rem //= bins
    coords=np.array(coords)
    low = coords / bins
    high = (coords+1)/bins
    x = rng.random(d)*(high-low) + low
    x = np.clip(x, 0.0, 0.999999)
    return x, chosen

if __name__=="__main__":
    ap=argparse.ArgumentParser()
    ap.add_argument("--func", type=int, default=1)
    ap.add_argument("--bins", type=int, default=4)
    ap.add_argument("--eps", type=float, default=0.1)
    ap.add_argument("--seed", type=int, default=0)
    args=ap.parse_args()

    Xs, ys = load_history()
    i=args.func-1
    x, arm = propose_next(Xs[i], ys[i], bins=args.bins, eps=args.eps, seed=args.seed)
    print(f"Chosen arm={arm} (eps={args.eps})")
    print(f"Proposed next for Function {args.func}: {to_portal_string(x)}")
