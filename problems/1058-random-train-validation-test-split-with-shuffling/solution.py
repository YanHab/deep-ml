import numpy as np

def random_split(data: np.ndarray, train_frac: float, validation_frac: float, seed: int = 123) -> list:
    """
    Randomly split a dataset into train, validation, and test subsets.
    """
    n = data.shape[0]
    train_end = int(n*train_frac)
    validation_end = train_end + int(n*validation_frac)
    ind = np.random.default_rng(seed).permutation(n)
    
    dt = data[ind]
    train = dt[0:train_end]
    val = dt[train_end:validation_end]
    test = dt[validation_end:]
    return [train, val, test]