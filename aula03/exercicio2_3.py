# Aula 3 - Exercício 2
#
# Escreva um programa que, dados três números inteiros, imprima os
# números em ordem crescente.

a = int(input("Entre com o primeiro número: "))
b = int(input("Entre com o segundo número: "))
c = int(input("Entre com o terceiro número: "))

x1 = min(a, b, c)
x3 = max(a, b, c)
x2 = (a + b + c) - x1 - x3

print(x1, x2, x3)
