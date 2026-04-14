# Mediana dos valores de um vetor

# Escreva um programa que, dado um vetor de números inteiros, calcule
# a mediana dos elementos do vetor.

v = [1, 2, 3, 2, 1, 1, 2, 2, 3, 1]
v.sort()
n = len(v)
if n % 2 == 1:
    mediana = v[(n - 1) // 2]
else:
    mediana = (v[(n // 2) - 1] + v[(n // 2)]) / 2
print(mediana)
