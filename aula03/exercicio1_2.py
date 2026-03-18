# Aula 3 - Exercício 1
#
# Escreva um programa que, dados três números inteiros, imprima o
# menor deles.

a = int(input("Entre com o primeiro número: "))
b = int(input("Entre com o segundo número: "))
c = int(input("Entre com o terceiro número: "))
if (a <= b) and (a <= c):
    print(a)
elif b <= c:
    print(b)
else:
    print(c)
