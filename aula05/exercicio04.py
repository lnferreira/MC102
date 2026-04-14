# Média dos valores de um vetor
#
# Escreva um programa que, dado um vetor de números inteiros, calcule a média
# dos elementos do vetor.

v = [1, 2, 3, 2, 1, 1, 2, 2, 3, 1]
soma = 0
n = 0
for i in v:
    soma = soma + i
    n = n + 1
print(soma / n)
