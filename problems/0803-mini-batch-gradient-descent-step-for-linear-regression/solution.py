import numpy as np

def mini_batch_gd_step(X: np.ndarray, y: np.ndarray, weights: np.ndarray, bias: float, batch_indices: list, lr: float) -> np.ndarray:
    """
    Perform one mini-batch gradient descent update step for linear regression with MSE loss.
    Returns a 1D array of length D+1: updated weights followed by updated bias.
    
    """

    x_i = X[batch_indices]
    y_i = y[batch_indices]

    y_hat = x_i @ weights + bias

    error = (y_hat - y_i)
    grad = (x_i.T @ error )*2/len(batch_indices)

    weights = weights - grad*lr
    bias = bias - np.mean(error*2, axis=0) * lr
    return np.concatenate((weights, [bias]), axis=0)




    