
import numpy as np

def rmse(y_true, y_pred):
	

	rmse_res = np.sqrt(np.mean((y_true- y_pred)**2))
	return np.round(rmse_res,3)
