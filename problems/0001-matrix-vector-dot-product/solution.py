def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	m = len(a[0])
	if m != len(b):
		return -1
	
	ans = [0]*len(a)
	for row in range(len(a)):
		row_sum = 0
		for it2, item in enumerate(a[row]):
			row_sum+= a[row][it2] * b[it2]
		ans[row] = row_sum
	return ans