import numpy as np
import math

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

# Exercícios de Lógica de Programação PYTHON
# 1. Calcule a área de um círculo (raio = 5)
raio = 5
area = math.pi * raio ** 2
print("1 - Área do círculo:", area)

# 2. Inverta uma string ("Python" → "nohtyP")
string = "Python"
print("2 - String invertida:", string[::-1])

# 3. Some todos os elementos de uma lista ([1, 2, 3, 4] → 10)
lista = [1, 2, 3, 4]
print("3 - Soma dos elementos:", sum(lista))

# 4. Verifique se um número é par ou ímpar
numero = 7
if numero % 2 == 0:
    print("4 - Par")
else:
    print("4 - Ímpar")

# 5. Imprima os números de 1 a 10, exceto o 5
print("5 - Números de 1 a 10 (exceto o 5):")
for i in range(1, 11):
    if i == 5:
        continue
    print(i)

# 6. Crie uma função que calcula o fatorial de um número
def fatorial(n):
    if n == 0 or n == 1:
        return 1
    return n * fatorial(n - 1)

print("6 - Fatorial de 5:", fatorial(5))
