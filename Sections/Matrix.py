import numpy as np

# Define the matrices using NumPy arrays
matrix_a = np.array([[1, 2], [3, 4]])
matrix_b = np.array([[5, 6], [7, 8]])

# Add the matrices using the addition operator
plus_matrix = matrix_a + matrix_b

dotted_matrix = matrix_a.dot(matrix_b)

# Print the results
print("Sum of the matrices added up:")
print(plus_matrix)

print("Sum of the matrices dotted:")
print(dotted_matrix)
