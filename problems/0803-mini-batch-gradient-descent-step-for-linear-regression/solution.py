import numpy as np

def mini_batch_gd_step(X: np.ndarray, y: np.ndarray, weights: np.ndarray, bias: float, batch_indices: list, lr: float) -> np.ndarray:
    """
    Perform one mini-batch gradient descent update step for linear regression with MSE loss.
    Returns a 1D array of length D+1: updated weights followed by updated bias.
    
    """
    error = 0
    grad = 0
    for i in batch_indices:
        x_i = X[i]
        y_i = y[i]

        y_hat = np.dot(x_i, weights) + bias 

        error += y_hat - y_i  
        grad += (y_hat - y_i)*x_i

    error /= len(batch_indices)
    grad /= len(batch_indices)

    grad *= 2
    error *= 2

    weights = weights - grad*lr
    bias = bias - error*lr
    return np.concatenate((weights, [bias]), axis=0)

    