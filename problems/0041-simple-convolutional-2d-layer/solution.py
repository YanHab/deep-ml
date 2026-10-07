import numpy as np

def simple_conv2d(input_matrix: np.ndarray, kernel: np.ndarray, padding: int, stride: int):
	input_height, input_width = input_matrix.shape
	kernel_height, kernel_width = kernel.shape

	matr = np.pad(input_matrix, pad_width=padding, mode= "constant", constant_values = 0 )


	output_height = ((input_height + 2* padding - kernel_height )// stride) + 1
	output_width = ((input_width + 2* padding - kernel_width )// stride) + 1

	out = np.zeros((output_height, output_width))
	for x in range(output_height):
		
		for y in range(output_width):
			
			out[x][y] = (matr[ x*stride : kernel_height + x*stride, y*stride : kernel_width + y * stride ] * kernel).sum()

			
	return out
