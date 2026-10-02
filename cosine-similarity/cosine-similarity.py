import numpy as np

def cosine_similarity(a: list, b: list) -> float:
    """
    Returns the cosine similarity as a Python float.
    """
    dot = 0
    aL2 = 0
    bL2 = 0
    for i in range(0, len(a)):
        dot+=a[i]*b[i]
        aL2+= a[i]**2
        bL2+= b[i]**2
    # Write code here
    aL2 **= 1/2
    bL2 **= 1/2
    if(aL2 * bL2 == 0): 
        return float(0)
    return float(dot/(aL2*bL2))
    pass