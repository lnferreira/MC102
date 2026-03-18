# Aula 3 - Exercício 7
#
# Escreva um programa que leia os valores correspondentes aos três
# lados de um triângulo e determine se ele é retângulo.

a = float(input("Entre com o primeiro lado: "))
b = float(input("Entre com o segundo lado: "))
c = float(input("Entre com o terceiro lado: "))

if a == (b**2 + c**2) ** (1 / 2):
    print("Triângulo retângulo")
elif b == (a**2 + c**2) ** (1 / 2):
    print("Triângulo retângulo")
elif c == (a**2 + b**2) ** (1 / 2):
    print("Triângulo retângulo")
else:
    print("Triângulo não retângulo")
