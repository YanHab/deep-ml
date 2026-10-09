import numpy as np

def recall(y_true, y_pred):
    """
    Calculate the recall metric for binary classification.
    
    Args:
        y_true: Array of true binary labels (0 or 1)
        y_pred: Array of predicted binary labels (0 or 1)
    
    Returns:
        Recall value as a float
    """

    TP = np.sum(np.where((y_pred == y_true)& (y_pred == 1), 1, 0))
    FN = np.sum(np.where((y_pred != y_true) & (y_pred == 0), 1, 0))
    
    if TP == 0:
        return  0
    
    return  TP /( TP + FN)
