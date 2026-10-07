def inverse_2x2(matrix: list[list[float]]) -> list[list[float]] | None:
    """
    Calculate the inverse of a 2x2 matrix.
    
    Args:
        matrix: A 2x2 matrix represented as [[a, b], [c, d]]
    
    Returns:
        The inverse matrix as a 2x2 list, or None if the matrix is singular
        (i.e., determinant equals zero)
    """
    if len(matrix) != 2:
        return None
    det = matrix[0][0]*matrix[1][1] - matrix[1][0]*matrix[0][1]

    if det == 0:
        return None

    a = matrix[0][0]
    d = matrix[1][1]
    b = matrix[0][1]
    c = matrix[1][0]
    a/=  det
    b/= -det
    c/= -det
    d/=  det
    return [[d, b], [c, a]]