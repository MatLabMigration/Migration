import numpy as np

# Definieer de matrices met behulp van NumPy arrays
matrix_a = np.array([[1, 2], [3, 4]])
matrix_b = np.array([[5, 6], [7, 8]])

# Optellen van de matrices
plus_matrix = matrix_a + matrix_b
print("\nSom van de matrices opgeteld:")
print(plus_matrix)

# Aftrekken van de matrices
min_matrix = matrix_a - matrix_b
print("\nVerschil van de matrices afgetrokken:")
print(min_matrix)

# Matrixvermenigvuldiging (dot product) van de matrices
maal_matrix = matrix_a.dot(matrix_b)
print("\nMatrixvermenigvuldiging (dot product) van de matrices:")
print(maal_matrix)

# Deling van de matrices
deel_matrix = matrix_a / matrix_b
print("\nDeling van de matrices:")
print(deel_matrix)

# Vermenigvuldiging van matrix_a met een factor
factor = 2
factor_matrix = factor * matrix_a
print("\nMatrix a vermenigvuldigd met een factor van 2:")
print(factor_matrix)