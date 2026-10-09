import numpy as np

def train_logreg(X: np.ndarray, y: np.ndarray, learning_rate: float, iterations: int) -> tuple[list[float], ...]:
	"""
	Gradient-descent training algorithm for logistic regression, optimizing parameters with Binary Cross Entropy loss.
	"""

	n, m = X.shape

	w = np.zeros(m)
	b = 0
	history = []
	for it in range(iterations):
		proba = X @ w + b
		
		pred = 1 / (1 + np.exp(-proba))
		
		# logit = np.log(proba/(1-proba))
		loss = np.round(np.sum( -( y*np.log(pred) + (1- y)*np.log(1 - pred))), 4)
		history.append(loss)
		grad = X.T @ (pred - y)
		grad_b = np.sum(pred - y)
		w = w - learning_rate * grad
		b = b - learning_rate * grad_b


	
	return (np.concatenate([[np.round(b,4)], np.round(w, 4)], axis=0).tolist() ,history)
