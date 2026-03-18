# Aula 3 - Exercício 2
#
# Escreva um programa que, dados três números inteiros, imprima os
# números em ordem crescente.

a = int(input("Entre com o primeiro número: "))
b = int(input("Entre com o segundo número: "))
c = int(input("Entre com o terceiro número: "))

if (a <= b) and (a <= c):  # O menor é o primeiro (a)
    if b <= c:
        print(a, b, c)
    else:
        print(a, c, b)
elif b <= c:  # O menor é o segundo (b)
    if a <= c:
        print(b, a, c)
    else:
        print(b, c, a)
else:  # O menor é o terceiro (c)
    if a <= b:
        print(c, a, b)
    else:
        print(c, b, a)
