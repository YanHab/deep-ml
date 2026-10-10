import numpy as np

def precision_recall_at_threshold(y_true, y_scores, threshold):
    """
    Compute precision and recall at a given decision threshold.

    Args:
        y_true: list/array of true binary labels (0 or 1)
        y_scores: list/array of predicted scores in [0, 1]
        threshold: float, classification threshold (predict positive if score >= threshold)

    Returns:
        [precision, recall] as a list of two floats rounded to 4 decimals.
    """
    y_pred = np.where(np.array(y_scores) > threshold, 1, 0)
    TP = np.sum(np.where((y_pred == y_true) & (y_pred == 1), 1, 0))
    FP = np.sum(np.where((y_pred != y_true) & (y_pred == 1), 1, 0))
    FN = np.sum(np.where((y_pred != y_true) & (y_pred == 0), 1, 0))

    precision = TP / (TP + FP)
    recall = TP / (TP + FN)
    if TP == 0:
        return [0, 0]
    return np.round([precision, recall], 4)
