import numpy as np

def f_score(y_true, y_pred, beta):
	"""
	Calculate F-Score for a binary classification task.

	:param y_true: Numpy array of true labels
	:param y_pred: Numpy array of predicted labels
	:param beta: The weight of precision in the harmonic mean
	:return: F-Score rounded to three decimal places
	"""

	TP = np.sum(np.where((y_pred==y_true)& (y_pred==1), 1, 0))
	FP = np.sum(np.where((y_pred!=y_true)& (y_pred==1), 1, 0))
	FN = np.sum(np.where((y_pred!=y_true)& (y_pred==0), 1, 0))

	if TP != 0:
		precision = TP/(TP+FP)
		recall = TP /( TP + FN)

		f_beta = (1 + beta**2) * (precision * recall) / (((beta**2)*precision)+ recall)
		return  np.round(f_beta, 4)
	else:
		return 0
	

	pass
