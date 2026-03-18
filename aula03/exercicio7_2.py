# Aula 3 - Exercício 7
#
# Escreva um programa que leia os valores correspondentes aos três
# lados de um triângulo e determine se ele é retângulo.

a = float(input("Entre com o primeiro lado: "))
b = float(input("Entre com o segundo lado: "))
c = float(input("Entre com o terceiro lado: "))

x1 = min(a, b, c)
x2 = max(a, b, c)
x3 = (a + b + c) - x1 - x2

if x3 == (x1**2 + x2**2) ** (1 / 2):
    print("Triângulo retângulo")
else:
    print("Triângulo não retângulo")
