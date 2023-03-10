# Python program to inverse
# a matrix using numpy

# Import required package
import numpy as np

# Taking a 3 * 3 matrix
A = np.array([[1, 1, 1],
			[1, 2, 3],
			[2, 4, 9]])

# Calculating the inverse of the matrix
print(np.linalg.inv(A))
