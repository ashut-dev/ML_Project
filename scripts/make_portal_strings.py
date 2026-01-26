import re
DIMS=[2,2,3,4,4,5,6,8]

def to_portal(nums):
    return "-".join([f"{x:0.6f}" for x in nums])

def parse_last_round_inputs(txt:str):
    vals=[float(x) for x in re.findall(r"[-+]?\d*\.\d+(?:e[-+]?\d+)?|[-+]?\d+(?:e[-+]?\d+)?", txt, flags=re.IGNORECASE)]
    total=sum(DIMS)
    vals=vals[-total:]
    out=[]
    idx=0
    for d in DIMS:
        out.append(vals[idx:idx+d])
        idx+=d
    return out

# Example:
# txt=open("InputOutput/inputs_13thround.txt").read()
# print("\n".join([to_portal(v) for v in parse_last_round_inputs(txt)]))
