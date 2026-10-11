import numpy as np

def shuffle_data(X, y, seed=None):
	n = len(y)
	ind = np.array([i for i in range(n)])
	np.random.seed(seed)
	np.random.shuffle(ind)
	X_shuffled = X[ind]
	y_shuffled = y[ind]
	return (X_shuffled, y_shuffled)