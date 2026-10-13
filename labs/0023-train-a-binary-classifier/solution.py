import numpy as np
# You can import any sklearn module you need

def train(X_train, y_train, X_val, y_val):
    """
    Train a binary classifier.
    
    Args:
        X_train: numpy array of shape (n_samples, 30) -- standardized features
        y_train: numpy array of shape (n_samples,) -- binary labels (0 or 1)
        X_val:   numpy array of shape (n_val, 30) -- standardized
        y_val:   numpy array of shape (n_val,) -- validation labels
    
    Returns:
        predict: callable that takes X (n, 30) and returns y_pred (n,) of 0s and 1s
    """
    n, m = X_train.shape
    w = np.zeros(m)

    b = 0
    lr = 0.01


    for i in range(1000):
        score = X_train @ w + b
        proba = np.ones(n) / ( 1 + np.exp(-score))
        pred = np.where(proba  > 0.5, 1, 0)
        error = y_train - pred
        grad = X_train.T @ error

        w = w - grad*lr/ n

        b = b - np.mean(error)*lr

    def predict(X):
        import numpy as np
        score = X @ w + b
        return np.where(1/(1 + np.exp(-score))> 0.5, 1, 0)


    return predict



    