def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	m = len(a[0])
	if m != len(b):
		return -1
	
	ans = []
	for row in a:
		row_sum = 0
		for it1, it2 in zip(row, b):
			row_sum += it1*it2
		ans.append(row_sum)
	return ans