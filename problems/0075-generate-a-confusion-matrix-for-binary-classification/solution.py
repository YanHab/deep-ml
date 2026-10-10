
from collections import Counter

def confusion_matrix(data):
	

	count = Counter(map(tuple, data))

	matr = [[count[(1, 1)], count[(1, 0)]], 
	[count[(0, 1)], count[(0, 0)]]]
	return matr