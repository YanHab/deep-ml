import  numpy as np
def feature_scaling(data: np.ndarray) -> (np.ndarray, np.ndarray):
	
	
	n, m = data.shape
	maximum = data.max(axis=0)
	minimum = data.min(axis=0)

	normalized_data = (data - minimum)/(maximum - minimum)
	
	std_dev = np.std(data, axis=0)

	standardized_data = (data - np.mean(data, axis=0))/ std_dev
	return (standardized_data, normalized_data)