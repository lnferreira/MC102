# Aula 3 - Exercício 6
#
# Escreva um programa que leia os valores correspondentes aos três
# lados de um triângulo e determine se ele é isósceles, escaleno ou
# equilátero.

a = float(input("Entre com o primeiro lado: "))
b = float(input("Entre com o segundo lado: "))
c = float(input("Entre com o terceiro lado: "))

if (a != b) and (b != c) and (a != c):
    print("Triângulo escaleno")
elif (a == b) and (b == c):  # Se chegou aqui, é porque dois lados são diferentes
    print("Triângulo equilátero")
else:  # Se chegou aqui, é porque os três lados também não são iguais
    print("Triângulo isósceles")
