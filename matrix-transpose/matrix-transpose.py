import numpy as np

def matrix_transpose(A: list) -> np.ndarray:
    """
    Returns the transposed matrix as a NumPy array.
    """
    t = np.empty((len(A[0]), len(A)))
    for row in range(len(A)):
        for column in range(len(A[0])):
                 t[column][row] = A[row][column]
    return t
    pass
