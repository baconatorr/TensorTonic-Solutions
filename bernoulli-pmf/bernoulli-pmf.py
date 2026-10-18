import numpy as np

def bernoulli_pmf_and_moments(x: list, p: float) -> dict:
    """
    Returns a dictionary with pmf, mean, and variance.
    """
    mean = float(p)
    var = float(p*(1-p))
    x = np.array(x)
    result = np.where(x == 1, p, 1-p)
    return {
        "pmf": result,
        "mean": mean,
        "variance": var,
    }
    pass