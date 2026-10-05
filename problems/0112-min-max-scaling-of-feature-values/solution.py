def min_max(x: list[float]) -> list[float]:
    """
    Perform Min-Max normalization to scale values to [0, 1].
    
    Args:
        x: A list of numerical values
    
    Returns:
        A new list with values normalized to [0, 1]
    """

    min_i = min(x)
    max_i = max(x)

    dif = max_i - min_i
    ans = []
    for i in x:
        ans.append( (i - min_i)/ dif)
    return ans