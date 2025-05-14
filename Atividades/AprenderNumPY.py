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

print('A - Mínimo', np.min(matriz))
print('B - Máximo', np.max(matriz))