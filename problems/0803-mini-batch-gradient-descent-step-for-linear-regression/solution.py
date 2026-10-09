import numpy as np

def mini_batch_gd_step(X: np.ndarray, y: np.ndarray, weights: np.ndarray, bias: float, batch_indices: list, lr: float) -> np.ndarray:
    """
    Perform one mini-batch gradient descent update step for linear regression with MSE loss.
    Returns a 1D array of length D+1: updated weights followed by updated bias.
    """
    error = 0
    grad = np.zeros(weights.shape)
    for i in batch_indices:
        y_hat = np.dot(weights, X[i]) + bias
        y_i = y[i]
        error += (y_hat - y_i)
        grad += (y_hat - y_i)* X[i]

    error /= len(batch_indices)
    error *= 2
    grad /= len(batch_indices)
    grad *=2

    weights = weights - grad * lr

    bias = bias - error * lr
    return np.concatenate((weights, [bias]), axis=0)



