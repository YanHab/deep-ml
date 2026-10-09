
import numpy as np

def r_squared(y_true, y_pred):
	

	mean = sum(y_true)/len(y_true)

	ssr = sum(np.power(y_true - y_pred, 2))
	sst = sum(np.power(y_true- mean, 2))
	return  1 - ssr/sst