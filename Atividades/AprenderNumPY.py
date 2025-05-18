import numpy as np

# 1. Criar um vetor nulo de tamanho 10.
teste = [10]
print("1 -", np.zeros(teste))

# 2. Criar um vetor nulo de tamanho 10, mas o quarto item possui valor 1
teste = np.zeros(10)
teste[3] = 1
print("2 -", teste)

# 3. Criar um vetor com valores que variam de 10 a 49.
teste = np.arange(9, 50) 
print("3 -", teste)

# 4. Criar uma matriz 3x3 com valores que variam de 0 a 9.
#   a) Encontrar valor mínimo
#   b) Encontrar valor máximo

matriz = np.arange(9).reshape(3, 3)
print("4 -\n", matriz)
print("4 - a) Mínimo\n", np.min(matriz))
print("4 - b) Máximo\n", np.max(matriz))

# 5. - Criar uma matriz identidade 3x3.
print("5 -\n", (np.eye(3,3)))

# 6. - Subtrair a média de cada linha de uma matriz.
matriz = np.arange(9).reshape(3, 3)
media_linhas = matriz.mean(axis=1)
print("6 - Matriz original:\n", matriz)
print("6 - Média de cada linha:", media_linhas.flatten())

