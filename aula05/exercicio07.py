# Intercalação de vetores ordenados

# Escreva um programa que, dados dois vetores ordenados de números
# inteiros, produza um vetor ordenado com todos os números dos dois
# vetores originais.

a = [1, 1, 2, 4, 5, 6, 8, 9, 9, 9]
b = [0, 1, 3, 3, 6, 7, 7, 8, 9]
c = []
while a and b:
    if a[0] < b[0]:
        c.append(a.pop(0))
    else:
        c.append(b.pop(0))
# Se um dos vetores ainda tiver elementos, adiciona-os a c
c = c + a + b
print(c)
