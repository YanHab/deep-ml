import numpy as np
def precision(y_true, y_pred):
	TP = np.sum(np.where((y_pred == y_true) &( y_pred == 1), 1, 0))
	FP = np.sum(np.where((y_pred != y_true )&( y_pred == 1), 1, 0))
	if TP == 0:
		return 0
	return  TP / (TP +FP)
