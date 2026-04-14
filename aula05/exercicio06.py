# Moda dos valores de um vetor
#
# Escreva um programa que, dado um vetor de números inteiros, construa
# um vetor com os elementos que são a moda do vetor.

v = [1, 2, 3, 2, 1, 1, 2, 2, 3, 1, 5, 5, 5, 5, 5, 5]
moda = []
max = 0
for i in v:
    # se a contagem for maior, atualiza a moda
    if v.count(i) > max:
        moda = [i]
        max = v.count(i)
    # se for igual, adiciona a moda
    elif v.count(i) == max:
        if not (i in moda):
            moda.append(i)
print(moda)
