import numpy as np

def sgd_update(X: np.ndarray, y: np.ndarray, weights: np.ndarray, learning_rate: float, n_iter: int) -> list:
    """
    Perform n_iter steps of stochastic gradient descent on a linear regression
    model with MSE loss, cycling through samples in order.

    Returns the final weight vector as a Python list.
    """
    n, m = X.shape
    theta = weights.astype(float).copy()
    for i in range(n_iter):
        ind = i % n
        
        y_hat = X[ind] @ theta
        x_i = X[ind]

        grad = (y_hat - y[ind]) * x_i *2

        
        theta = theta - grad * learning_rate
    return theta.tolist()
