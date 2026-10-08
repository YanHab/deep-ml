import numpy as np

def make_diagonal(x):
	matr = []
	for item in range(len(x)):
		row = np.zeros(len(x))
		row[item] = x[item]
		matr.append(row)
	return matr
	