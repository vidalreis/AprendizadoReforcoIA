# 📌 LISTAS

# 1. Obter o maior número de uma lista
lista = [1, 8, 3, 5, 12]
print("1 - Maior número:", max(lista))

# 2. Remover duplicatas de uma lista
lista = [1, 2, 2, 3, 4, 4, 5]
print("2 - Sem duplicatas:", list(set(lista)))

# 3. Verificar se uma lista está vazia
lista = []
print("3 - Lista está vazia?", len(lista) == 0)

# 4. Verifica se duas listas têm pelo menos um membro em comum
def tem_comum(lista1, lista2):
    return bool(set(lista1) & set(lista2))

print("4 - Tem item em comum:", tem_comum([1, 2, 3], [5, 6, 3]))

# 5. Gerar e imprimir primeiros e últimos 5 números quadrados de 1 a 30
quadrados = [i**2 for i in range(1, 31)]
print("5 - Primeiros e últimos 5 quadrados:", quadrados[:5] + quadrados[-5:])

# 6. Verificar se todos os números da lista são primos
def eh_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def todos_primos(lista):
    return all(eh_primo(n) for n in lista)

print("6 - [0, 3, 4, 7, 9] =>", todos_primos([0, 3, 4, 7, 9]))
print("6 - [3, 5, 7, 13] =>", todos_primos([3, 5, 7, 13]))
print("6 - [1, 5, 3] =>", todos_primos([1, 5, 3]))

# 📌 TUPLAS

# 7. Desempacotar tupla em variáveis
tupla = (1, 2, 3)
a, b, c = tupla
print("7 - Desempacotado:", a, b, c)

# 8. Converter uma tupla para string
tupla = ('P', 'y', 't', 'h', 'o', 'n')
print("8 - Tupla como string:", ''.join(tupla))

# 9. Encontrar itens repetidos em uma tupla
tupla = (1, 2, 3, 2, 4, 2, 5)
repetidos = set([x for x in tupla if tupla.count(x) > 1])
print("9 - Itens repetidos:", repetidos)

# 📌 CONJUNTOS

# 10. Verificar se um valor está presente em um set
s = {1, 2, 3, 4, 5}
print("10 - Valor 3 está presente?", 3 in s)

# 11. Verificar se dois sets não têm elementos em comum
a = {1, 2, 3}
b = {4, 5, 6}
print("11 - Sets têm interseção?", a.isdisjoint(b))

# 12. Encontrar os números ausentes entre dois sets
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7}
print("12 - Faltando em set2:", set1 - set2)
print("12 - Faltando em set1:", set2 - set1)

# 13. Remover duplicatas de uma lista de strings com set
lista = ["a", "b", "a", "c", "b"]
print("13 - Strings únicas:", list(set(lista)))

# 📌 DICIONÁRIOS

# 14. Verificar se uma chave existe em um dicionário
d = {"nome": "Vidal", "idade": 25}
print("14 - A chave 'nome' existe?", "nome" in d)

# 15. Gerar dicionário com (x, x*x)
n = 5
quadrados = {x: x**2 for x in range(1, n+1)}
print("15 - Dicionário (x, x²):", quadrados)

# 16. Obter maior e menor valor de um dicionário
d = {"a": 5, "b": 9, "c": 2}
print("16 - Máximo:", max(d.values()))
print("16 - Mínimo:", min(d.values()))

# 17. Imprimir todos os valores distintos de uma lista de dicionários
dados = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"}, {"VIII":"S007"}]
valores = set()
for dic in dados:
    for valor in dic.values():
        valores.add(valor)
print("17 - Valores únicos:", valores)

# 18. Filtrar números pares de um dicionário
def filtrar_pares(d):
    return {k: [x for x in v if x % 2 == 0] for k, v in d.items()}

original1 = {'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}
original2 = {'V': [1, 3, 5], 'VI': [1, 5], 'VII': [2, 7, 9]}
print("18 - Dicionário 1 filtrado:", filtrar_pares(original1))
print("18 - Dicionário 2 filtrado:", filtrar_pares(original2))
