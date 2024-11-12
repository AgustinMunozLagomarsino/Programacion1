#"" Tema 3.7 desafios 1,2 y 3 progrmacion de Agustin Muñoz""
import numpy as np

# Desafío 1
# Definimos las matrices A y B
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

# Calculamos 2A
two_A = 2 * A

# Calculamos la transpuesta de B (B^T)
B_T = B.T

# Calculamos 2A + B^T
resultado_desafio_1 = two_A + B_T
print("Resultado Desafío 1 (2A + B^T):\n", resultado_desafio_1)

# Desafío 2
# Definimos la matriz A para el segundo desafío
A_desafio_2 = np.array([[1, 0, 1], [4, -1, 4], [5, 6, 7]])

# Calculamos la inversa de A
A_inv = np.linalg.inv(A_desafio_2)

# Calculamos la traza de la matriz inversa
traza_desafio_2 = np.trace(A_inv)
print("Resultado Desafío 2 (traza de la matriz inversa de A):", traza_desafio_2)

# Desafío 3
# Definimos la matriz A para el tercer desafío
A_desafio_3 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Calculamos la transpuesta de A
A_T = A_desafio_3.T

# Calculamos A + A^T
A_plus_A_T = A_desafio_3 + A_T

# Calculamos el rango de la matriz resultante
rango_desafio_3 = np.linalg.matrix_rank(A_plus_A_T)
print("Resultado Desafío 3 (rango de A + A^T):", rango_desafio_3)


