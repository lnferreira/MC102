# Contando Divisores
#
# Escreva um programa que leia um número inteiro positivo (n > 1) e
# imprima o número de seus divisores.

n = int(input("Digite um número inteiro positivo : "))
divisores = 0
for divisor in range(1, n + 1):
    if n % divisor == 0:
        divisores = divisores + 1
print(divisores)
