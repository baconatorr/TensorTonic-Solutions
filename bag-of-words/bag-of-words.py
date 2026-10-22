import numpy as np

def bag_of_words_vector(tokens: list, vocab: list) -> np.ndarray:
    """
    Returns a NumPy array with length len(vocab).
    """
    tokens = np.asarray(tokens)
    vocab = np.asarray(vocab)
    return np.array([np.sum(tokens == word) for word in vocab])
    pass