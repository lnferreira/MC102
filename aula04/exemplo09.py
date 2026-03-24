# numeros = [3, 1, 7, 9, 4]
numeros = [-3, -1, -7, -9, -4]
maximo = numeros[0]

i = 1
while i < len(numeros):
    if numeros[i] > maximo:
        maximo = numeros[i]
    i = i + 1

print(maximo)
