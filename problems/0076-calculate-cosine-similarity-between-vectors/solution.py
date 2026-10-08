import numpy as np

def cosine_similarity(v1, v2):
	"""
	Calculate the cosine_similarity of two vectors.
	Args:
		vec1 (numpy.ndarray): 1D array representing the first vector.
		vec2 (numpy.ndarray): 1D array representing the second vector.
	Returns:
		The cosine_similarity of the two vectors.
	"""
	vec1 = np.array(v1)
	vec2 = np.array(v2)

	cos = np.sum(vec1*vec2)/ (np.sqrt(np.sum(vec1*vec1))*np.sqrt(np.sum(vec2*vec2)))
	return cos