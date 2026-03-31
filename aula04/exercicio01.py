# Imprimindo Divisores
#
# Escreva um programa que leia um número inteiro positivo (n > 1) e
# imprima os seus divisores.

n = int(input("Digite um número inteiro positivo : "))

for divisor in range(1, n + 1):
    if n % divisor == 0:
        print(divisor)
