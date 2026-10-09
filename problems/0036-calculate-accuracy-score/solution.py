import numpy as np

def accuracy_score(y_true, y_pred):
	# Your code here
	return np.mean(np.where(y_pred==y_true, 1, 0))