import numpy as np

def sample_var_std(x: list) -> dict:
    """
    Returns a dictionary with variance and standard_deviation.
    """
    n = len(x)
    variance = (n/(n-1))*((sum(i**2 for i in x)/n) - (sum(x)/len(x))**2)
    std = variance**(1/2)
    return {
        "variance": variance,
        "standard_deviation": std,
    }
    pass