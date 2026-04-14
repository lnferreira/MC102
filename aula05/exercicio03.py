# Todas as posições de um elemento
#
# Escreva um programa que, dado um vetor de números inteiros e um número inteiro
# x, construa um vetor com os índices de todas as posições de x no vetor
# original.

v = [1, 2, 3, 2, 1, 1, 2, 2, 3, 1]
x = int(input("Entre com um número a ser buscado: "))
pos = []
for i in range(len(v)):
    if v[i] == x:
        pos.append(i)
print(pos)
