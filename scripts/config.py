# Shared configuration for BBO capstone
DIMS = [2,2,3,4,4,5,6,8]  # Function 1..8
N_FUNCS = 8

def to_portal_string(x):
    """Format a vector to portal string x1-x2-... with 6 decimals."""
    return "-".join([f"{v:0.6f}" for v in x])

def parse_portal_string(s):
    """Parse portal string into list[float]."""
    return [float(t) for t in s.strip().split("-") if t.strip()]
