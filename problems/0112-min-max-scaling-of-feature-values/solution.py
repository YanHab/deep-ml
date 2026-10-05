def min_max(x: list[float]) -> list[float]:
    """
    Perform Min-Max normalization to scale values to [0, 1].
    
    Args:
        x: A list of numerical values
    
    Returns:
        A new list with values normalized to [0, 1]
    """
    import numpy as np

    x = np.asarray(x)
    

    min_i = x.min()
    max_i = x.max()
    ans = (x - min_i)/(max_i - min_i)
    return ans